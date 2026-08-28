---
title: AMOS CHART ENGINE
tags: [engine, processing, runtime, canon/knowledge]
type: document
source: 11_KNOWLEDGE/engine
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: engine_specification
---


# amos_omega_chart_engine

```python
#!/usr/bin/env python3
"""
AMOS OMEGA Live Chart Engine
Multi-timeframe chart engine with price overlay, volatility overlay, regime coloring, margin bands, and shock simulation
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum
import time
import logging
from datetime import datetime, timezone, timedelta
import json
from collections import deque

logger = logging.getLogger("AMOS_OMEGA_CHARTS")

class Timeframe(Enum):
    M1 = "1m"      # 1 minute
    M5 = "5m"      # 5 minutes
    M15 = "15m"    # 15 minutes
    M30 = "30m"    # 30 minutes
    H1 = "1h"      # 1 hour
    H4 = "4h"      # 4 hours
    D1 = "1d"      # 1 day
    W1 = "1w"      # 1 week
    MN1 = "1M"     # 1 month

class ChartType(Enum):
    PRICE = "price"
    CANDLESTICK = "candlestick"
    LINE = "line"
    AREA = "area"
    RENKO = "renko"

@dataclass
class PriceData:
    """Price data point"""
    timestamp: float
    open: float
    high: float
    low: float
    close: float
    volume: int = 0
    
@dataclass
class ChartOverlay:
    """Chart overlay configuration"""
    name: str
    data: List[float]
    color: str
    opacity: float = 0.7
    line_width: int = 2
    style: str = "solid"  # solid, dashed, dotted

@dataclass
class ShockEvent:
    """Shock event for simulation"""
    timestamp: float
    shock_type: str
    magnitude: float
    duration: float
    description: str

@dataclass
class ChartConfiguration:
    """Chart configuration"""
    symbol: str
    timeframe: Timeframe
    chart_type: ChartType
    show_volume: bool = True
    show_volatility: bool = True
    show_regime_colors: bool = True
    show_margin_bands: bool = True
    show_event_markers: bool = True
    shock_simulation: bool = False
    replay_mode: bool = False
    replay_speed: float = 1.0

class AMOSOmegaChartEngine:
    """AMOS OMEGA Live Chart Engine"""
    
    def __init__(self):
        self.price_data: Dict[str, deque] = {}
        self.volatility_data: Dict[str, deque] = {}
        self.regime_data: Dict[str, deque] = {}
        self.shock_events: List[ShockEvent] = []
        
        # Chart configuration
        self.default_config = ChartConfiguration(
            symbol="EURUSD",
            timeframe=Timeframe.H1,
            chart_type=ChartType.CANDLESTICK
        )
        
        # Technical indicators
        self.indicators = {
            "sma_20": {"period": 20, "type": "sma"},
            "sma_50": {"period": 50, "type": "sma"},
            "ema_12": {"period": 12, "type": "ema"},
            "ema_26": {"period": 26, "type": "ema"},
            "bollinger_upper": {"period": 20, "std": 2, "type": "bollinger"},
            "bollinger_lower": {"period": 20, "std": 2, "type": "bollinger"},
            "atr": {"period": 14, "type": "atr"}
        }
        
        # Regime colors
        self.regime_colors = {
            "stable": "#10b981",      # Green
            "transitioning": "#f59e0b", # Orange
            "volatile": "#ef4444",     # Red
            "stressed": "#f97316",     # Dark Orange
            "crisis": "#991b1b"        # Dark Red
        }
        
        # Initialize data storage
        self.max_data_points = 10000
        self._initialize_data_storage()
    
    def _initialize_data_storage(self):
        """Initialize data storage for common symbols"""
        common_symbols = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCAD"]
        
        for symbol in common_symbols:
            self.price_data[symbol] = deque(maxlen=self.max_data_points)
            self.volatility_data[symbol] = deque(maxlen=self.max_data_points)
            self.regime_data[symbol] = deque(maxlen=self.max_data_points)
    
    def add_price_data(self, symbol: str, data: PriceData) -> bool:
        """Add price data point"""
        try:
            if symbol not in self.price_data:
                self.price_data[symbol] = deque(maxlen=self.max_data_points)
                self.volatility_data[symbol] = deque(maxlen=self.max_data_points)
                self.regime_data[symbol] = deque(maxlen=self.max_data_points)
            
            self.price_data[symbol].append(data)
            
            # Calculate volatility
            volatility = self._calculate_volatility(symbol)
            self.volatility_data[symbol].append(volatility)
            
            # Determine regime
            regime = self._determine_regime(symbol, volatility)
            self.regime_data[symbol].append(regime)
            
            return True
            
        except Exception as e:
            logger.error(f"Error adding price data for {symbol}: {e}")
            return False
    
    def _calculate_volatility(self, symbol: str, window: int = 20) -> float:
        """Calculate rolling volatility"""
        if len(self.price_data[symbol]) < window:
            return 0.0
        
        prices = [p.close for p in list(self.price_data[symbol])[-window:]]
        returns = np.diff(prices) / prices[:-1]
        
        if len(returns) == 0:
            return 0.0
        
        return np.std(returns) * np.sqrt(252)  # Annualized volatility
    
    def _determine_regime(self, symbol: str, volatility: float) -> str:
        """Determine market regime based on volatility and other factors"""
        if volatility < 0.08:
            return "stable"
        elif volatility < 0.15:
            return "transitioning"
        elif volatility < 0.25:
            return "volatile"
        elif volatility < 0.35:
            return "stressed"
        else:
            return "crisis"
    
    def calculate_indicators(self, symbol: str) -> Dict[str, List[float]]:
        """Calculate technical indicators"""
        if symbol not in self.price_data or len(self.price_data[symbol]) < 50:
            return {}
        
        prices = list(self.price_data[symbol])
        close_prices = [p.close for p in prices]
        
        indicators = {}
        
        # Simple Moving Averages
        for name, config in self.indicators.items():
            if config["type"] == "sma":
                period = config["period"]
                if len(close_prices) >= period:
                    sma = self._calculate_sma(close_prices, period)
                    indicators[name] = sma
            elif config["type"] == "ema":
                period = config["period"]
                if len(close_prices) >= period:
                    ema = self._calculate_ema(close_prices, period)
                    indicators[name] = ema
            elif config["type"] == "bollinger":
                period = config["period"]
                std = config["std"]
                if len(close_prices) >= period:
                    upper, lower = self._calculate_bollinger_bands(close_prices, period, std)
                    indicators[f"bollinger_upper"] = upper
                    indicators[f"bollinger_lower"] = lower
            elif config["type"] == "atr":
                period = config["period"]
                if len(prices) >= period:
                    atr = self._calculate_atr(prices, period)
                    indicators[name] = atr
        
        return indicators
    
    def _calculate_sma(self, prices: List[float], period: int) -> List[float]:
        """Calculate Simple Moving Average"""
        sma = []
        for i in range(period - 1, len(prices)):
            avg = np.mean(prices[i - period + 1:i + 1])
            sma.append(avg)
        return sma
    
    def _calculate_ema(self, prices: List[float], period: int) -> List[float]:
        """Calculate Exponential Moving Average"""
        multiplier = 2 / (period + 1)
        ema = []
        
        # Start with SMA
        initial_sma = np.mean(prices[:period])
        ema.append(initial_sma)
        
        # Calculate EMA
        for i in range(period, len(prices)):
            current_ema = (prices[i] - ema[-1]) * multiplier + ema[-1]
            ema.append(current_ema)
        
        return ema
    
    def _calculate_bollinger_bands(self, prices: List[float], period: int, std: float) -> Tuple[List[float], List[float]]:
        """Calculate Bollinger Bands"""
        upper = []
        lower = []
        
        for i in range(period - 1, len(prices)):
            window = prices[i - period + 1:i + 1]
            sma = np.mean(window)
            std_dev = np.std(window)
            
            upper.append(sma + (std_dev * std))
            lower.append(sma - (std_dev * std))
        
        return upper, lower
    
    def _calculate_atr(self, price_data: List[PriceData], period: int) -> List[float]:
        """Calculate Average True Range"""
        tr_values = []
        
        for i in range(1, len(price_data)):
            high = price_data[i].high
            low = price_data[i].low
            prev_close = price_data[i-1].close
            
            tr1 = high - low
            tr2 = abs(high - prev_close)
            tr3 = abs(low - prev_close)
            
            true_range = max(tr1, tr2, tr3)
            tr_values.append(true_range)
        
        if len(tr_values) < period:
            return []
        
        atr = []
        for i in range(period - 1, len(tr_values)):
            atr_value = np.mean(tr_values[i - period + 1:i + 1])
            atr.append(atr_value)
        
        return atr
    
    def generate_chart_data(self, config: ChartConfiguration) -> Dict[str, Any]:
        """Generate complete chart data"""
        symbol = config.symbol
        
        if symbol not in self.price_data or len(self.price_data[symbol]) == 0:
            return {"error": f"No data available for {symbol}"}
        
        # Get price data
        prices = list(self.price_data[symbol])
        
        # Calculate indicators
        indicators = self.calculate_indicators(symbol)
        
        # Prepare overlays
        overlays = []
        
        # Volatility overlay
        if config.show_volatility and symbol in self.volatility_data:
            volatility = list(self.volatility_data[symbol])
            overlays.append(ChartOverlay(
                name="Volatility",
                data=volatility,
                color="#f59e0b",
                opacity=0.6
            ))
        
        # Moving averages
        if "sma_20" in indicators:
            overlays.append(ChartOverlay(
                name="SMA 20",
                data=indicators["sma_20"],
                color="#3b82f6",
                opacity=0.8
            ))
        
        if "sma_50" in indicators:
            overlays.append(ChartOverlay(
                name="SMA 50",
                data=indicators["sma_50"],
                color="#8b5cf6",
                opacity=0.8
            ))
        
        # Bollinger Bands
        if "bollinger_upper" in indicators and "bollinger_lower" in indicators:
            overlays.append(ChartOverlay(
                name="BB Upper",
                data=indicators["bollinger_upper"],
                color="#ef4444",
                opacity=0.5,
                style="dashed"
            ))
            overlays.append(ChartOverlay(
                name="BB Lower",
                data=indicators["bollinger_lower"],
                color="#ef4444",
                opacity=0.5,
                style="dashed"
            ))
        
        # Margin bands
        margin_bands = []
        if config.show_margin_bands:
            margin_bands = self._calculate_margin_bands(prices)
        
        # Event markers
        event_markers = []
        if config.show_event_markers:
            event_markers = self._get_event_markers(symbol)
        
        # Regime coloring
        regime_segments = []
        if config.show_regime_colors and symbol in self.regime_data:
            regime_segments = self._get_regime_segments(symbol)
        
        # Shock simulation
        shock_overlays = []
        if config.shock_simulation:
            shock_overlays = self._simulate_shocks(prices)
        
        return {
            "symbol": symbol,
            "timeframe": config.timeframe.value,
            "chart_type": config.chart_type.value,
            "price_data": [
                {
                    "timestamp": p.timestamp,
                    "open": p.open,
                    "high": p.high,
                    "low": p.low,
                    "close": p.close,
                    "volume": p.volume
                }
                for p in prices
            ],
            "overlays": [asdict(overlay) for overlay in overlays],
            "margin_bands": margin_bands,
            "event_markers": event_markers,
            "regime_segments": regime_segments,
            "shock_overlays": shock_overlays,
            "indicators": indicators,
            "configuration": asdict(config)
        }
    
    def _calculate_margin_bands(self, price_data: List[PriceData]) -> List[Dict[str, Any]]:
        """Calculate margin bands"""
        if len(price_data) < 20:
            return []
        
        closes = [p.close for p in price_data]
        
        # Calculate support and resistance levels
        recent_highs = []
        recent_lows = []
        
        for i in range(10, len(price_data) - 10):
            # Check for local high
            is_high = all(price_data[i].high >= price_data[j].high for j in range(i-10, i+10))
            if is_high:
                recent_highs.append(price_data[i].high)
            
            # Check for local low
            is_low = all(price_data[i].low <= price_data[j].low for j in range(i-10, i+10))
            if is_low:
                recent_lows.append(price_data[i].low)
        
        if not recent_highs or not recent_lows:
            return []
        
        # Calculate margin bands
        resistance = np.mean(recent_highs[-5:]) if len(recent_highs) >= 5 else np.mean(recent_highs)
        support = np.mean(recent_lows[-5:]) if len(recent_lows) >= 5 else np.mean(recent_lows)
        
        current_price = closes[-1]
        
        return [
            {
                "type": "resistance",
                "price": resistance,
                "distance": (resistance - current_price) / current_price * 100,
                "strength": "strong" if len(recent_highs) >= 3 else "weak"
            },
            {
                "type": "support",
                "price": support,
                "distance": (current_price - support) / current_price * 100,
                "strength": "strong" if len(recent_lows) >= 3 else "weak"
            }
        ]
    
    def _get_event_markers(self, symbol: str) -> List[Dict[str, Any]]:
        """Get event markers for the symbol"""
        markers = []
        
        # Add shock events
        for shock in self.shock_events:
            markers.append({
                "timestamp": shock.timestamp,
                "type": "shock",
                "description": f"{shock.shock_type}: {shock.description}",
                "severity": "high" if shock.magnitude > 0.1 else "medium",
                "color": "#ef4444"
            })
        
        return markers
    
    def _get_regime_segments(self, symbol: str) -> List[Dict[str, Any]]:
        """Get regime segments for coloring"""
        if symbol not in self.regime_data:
            return []
        
        regimes = list(self.regime_data[symbol])
        prices = list(self.price_data[symbol])
        
        if len(regimes) != len(prices):
            return []
        
        segments = []
        current_regime = regimes[0]
        start_timestamp = prices[0].timestamp
        
        for i, (regime, price) in enumerate(zip(regimes, prices)):
            if regime != current_regime:
                # End current segment
                segments.append({
                    "start_timestamp": start_timestamp,
                    "end_timestamp": price.timestamp,
                    "regime": current_regime,
                    "color": self.regime_colors.get(current_regime, "#6b7280")
                })
                
                # Start new segment
                current_regime = regime
                start_timestamp = price.timestamp
        
        # Add final segment
        if len(prices) > 0:
            segments.append({
                "start_timestamp": start_timestamp,
                "end_timestamp": prices[-1].timestamp,
                "regime": current_regime,
                "color": self.regime_colors.get(current_regime, "#6b7280")
            })
        
        return segments
    
    def _simulate_shocks(self, price_data: List[PriceData]) -> List[Dict[str, Any]]:
        """Simulate shock events on price data"""
        shock_overlays = []
        
        for shock in self.shock_events:
            # Find the price data point closest to shock timestamp
            shock_index = None
            for i, price in enumerate(price_data):
                if abs(price.timestamp - shock.timestamp) < 3600:  # Within 1 hour
                    shock_index = i
                    break
            
            if shock_index is not None:
                # Calculate shock effect
                base_price = price_data[shock_index].close
                shock_effect = shock.magnitude * base_price
                
                # Create shock overlay data
                overlay_data = []
                for i in range(max(0, shock_index - 10), min(len(price_data), shock_index + 20)):
                    distance = abs(i - shock_index)
                    decay = np.exp(-distance / 5)  # Exponential decay
                    
                    if i < shock_index:
                        # Before shock - no effect
                        overlay_data.append(0)
                    else:
                        # After shock - decaying effect
                        overlay_data.append(shock_effect * decay)
                
                shock_overlays.append({
                    "name": f"Shock: {shock.shock_type}",
                    "data": overlay_data,
                    "color": "#ef4444",
                    "opacity": 0.7,
                    "start_index": max(0, shock_index - 10),
                    "description": shock.description
                })
        
        return shock_overlays
    
    def add_shock_event(self, shock: ShockEvent):
        """Add a shock event for simulation"""
        self.shock_events.append(shock)
        logger.info(f"Added shock event: {shock.shock_type} at {shock.timestamp}")
    
    def multi_timeframe_analysis(self, symbol: str) -> Dict[str, Any]:
        """Generate multi-timeframe analysis"""
        timeframes = [Timeframe.M15, Timeframe.H1, Timeframe.H4, Timeframe.D1]
        analysis = {}
        
        for timeframe in timeframes:
            config = ChartConfiguration(
                symbol=symbol,
                timeframe=timeframe,
                chart_type=ChartType.CANDLESTICK
            )
            
            chart_data = self.generate_chart_data(config)
            
            if "error" not in chart_data:
                # Calculate timeframe-specific metrics
                prices = [p["close"] for p in chart_data["price_data"]]
                
                if len(prices) > 0:
                    analysis[timeframe.value] = {
                        "current_price": prices[-1],
                        "change": ((prices[-1] - prices[0]) / prices[0] * 100) if len(prices) > 1 else 0,
                        "volatility": np.std(prices) if len(prices) > 1 else 0,
                        "trend": "up" if prices[-1] > prices[0] else "down" if len(prices) > 1 else "neutral",
                        "regime": chart_data.get("regime_segments", [{}])[-1].get("regime", "unknown")
                    }
        
        return analysis
    
    def compare_before_after_shock(self, symbol: str, shock_timestamp: float) -> Dict[str, Any]:
        """Compare market state before and after shock"""
        if symbol not in self.price_data:
            return {"error": f"No data for {symbol}"}
        
        prices = list(self.price_data[symbol])
        
        # Find shock index
        shock_index = None
        for i, price in enumerate(prices):
            if abs(price.timestamp - shock_timestamp) < 3600:
                shock_index = i
                break
        
        if shock_index is None or shock_index < 20 or shock_index > len(prices) - 20:
            return {"error": "Insufficient data around shock timestamp"}
        
        # Before shock (20 periods)
        before_prices = [p.close for p in prices[shock_index - 20:shock_index]]
        
        # After shock (20 periods)
        after_prices = [p.close for p in prices[shock_index:shock_index + 20]]
        
        # Calculate metrics
        before_volatility = np.std(before_prices) if len(before_prices) > 1 else 0
        after_volatility = np.std(after_prices) if len(after_prices) > 1 else 0
        
        before_trend = (before_prices[-1] - before_prices[0]) / before_prices[0] if len(before_prices) > 1 else 0
        after_trend = (after_prices[-1] - after_prices[0]) / after_prices[0] if len(after_prices) > 1 else 0
        
        return {
            "symbol": symbol,
            "shock_timestamp": shock_timestamp,
            "before": {
                "periods": len(before_prices),
                "avg_price": np.mean(before_prices),
                "volatility": before_volatility,
                "trend": before_trend * 100
            },
            "after": {
                "periods": len(after_prices),
                "avg_price": np.mean(after_prices),
                "volatility": after_volatility,
                "trend": after_trend * 100
            },
            "impact": {
                "volatility_change": (after_volatility - before_volatility) / before_volatility * 100 if before_volatility > 0 else 0,
                "trend_change": (after_trend - before_trend) * 100,
                "price_impact": (after_prices[0] - before_prices[-1]) / before_prices[-1] * 100 if len(before_prices) > 0 and len(after_prices) > 0 else 0
            }
        }
    
    def get_chart_summary(self, symbol: str) -> Dict[str, Any]:
        """Get comprehensive chart summary"""
        if symbol not in self.price_data or len(self.price_data[symbol]) == 0:
            return {"error": f"No data for {symbol}"}
        
        prices = list(self.price_data[symbol])
        close_prices = [p.close for p in prices]
        
        # Basic metrics
        current_price = close_prices[-1]
        price_change = (current_price - close_prices[0]) / close_prices[0] * 100 if len(close_prices) > 1 else 0
        
        # Volatility
        volatility = list(self.volatility_data[symbol])[-1] if symbol in self.volatility_data and len(self.volatility_data[symbol]) > 0 else 0
        
        # Current regime
        current_regime = list(self.regime_data[symbol])[-1] if symbol in self.regime_data and len(self.regime_data[symbol]) > 0 else "unknown"
        
        # Technical indicators
        indicators = self.calculate_indicators(symbol)
        
        # Support/Resistance
        margin_bands = self._calculate_margin_bands(prices)
        
        return {
            "symbol": symbol,
            "current_price": current_price,
            "price_change": price_change,
            "volatility": volatility,
            "regime": current_regime,
            "indicators": {
                "sma_20": indicators.get("sma_20", [])[-1] if indicators.get("sma_20") else None,
                "sma_50": indicators.get("sma_50", [])[-1] if indicators.get("sma_50") else None,
                "ema_12": indicators.get("ema_12", [])[-1] if indicators.get("ema_12") else None,
                "ema_26": indicators.get("ema_26", [])[-1] if indicators.get("ema_26") else None,
                "atr": indicators.get("atr", [])[-1] if indicators.get("atr") else None
            },
            "margin_bands": margin_bands,
            "data_points": len(prices),
            "time_range": {
                "start": prices[0].timestamp,
                "end": prices[-1].timestamp
            }
        }

# Global chart engine instance
chart_engine = AMOSOmegaChartEngine()

if __name__ == "__main__":
    # Test chart engine
    print("AMOS OMEGA Chart Engine Test...")
    
    # Generate sample data
    now = time.time()
    symbol = "EURUSD"
    
    # Add sample price data
    base_price = 1.0850
    for i in range(100):
        timestamp = now - (100 - i) * 3600  # Hourly data
        
        # Generate realistic price movement
        price_change = np.random.normal(0, 0.001)  # 0.1% standard deviation
        new_price = base_price * (1 + price_change * i / 100)
        
        price_data = PriceData(
            timestamp=timestamp,
            open=new_price,
            high=new_price * (1 + abs(np.random.normal(0, 0.0005))),
            low=new_price * (1 - abs(np.random.normal(0, 0.0005))),
            close=new_price,
            volume=int(np.random.normal(1000000, 200000))
        )
        
        chart_engine.add_price_data(symbol, price_data)
        base_price = new_price
    
    # Add a shock event
    shock = ShockEvent(
        timestamp=now - 50 * 3600,
        shock_type="liquidity_crisis",
        magnitude=0.03,  # 3% shock
        duration=4 * 3600,  # 4 hours
        description="Sudden liquidity withdrawal"
    )
    chart_engine.add_shock_event(shock)
    
    # Generate chart data
    config = ChartConfiguration(
        symbol=symbol,
        timeframe=Timeframe.H1,
        chart_type=ChartType.CANDLESTICK,
        show_volatility=True,
        show_regime_colors=True,
        show_margin_bands=True,
        shock_simulation=True
    )
    
    chart_data = chart_engine.generate_chart_data(config)
    print("Chart data generated:", json.dumps(chart_data, indent=2, default=str))
    
    # Multi-timeframe analysis
    mtf_analysis = chart_engine.multi_timeframe_analysis(symbol)
    print("Multi-timeframe analysis:", json.dumps(mtf_analysis, indent=2, default=str))
    
    # Before/after shock comparison
    shock_comparison = chart_engine.compare_before_after_shock(symbol, shock.timestamp)
    print("Shock comparison:", json.dumps(shock_comparison, indent=2, default=str))
    
    # Chart summary
    summary = chart_engine.get_chart_summary(symbol)
    print("Chart summary:", json.dumps(summary, indent=2, default=str))


```

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[ENGINE_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
