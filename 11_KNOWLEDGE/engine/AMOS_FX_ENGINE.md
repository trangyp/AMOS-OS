---
title: AMOS FX ENGINE
tags:
- engine
- processing
- runtime
- canon/knowledge
type: document
source: 11_KNOWLEDGE/engine
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: engine_specification
---


# amos_omega_fx_engine

```python
#!/usr/bin/env python3
"""
AMOS OMEGA FX Structural Analysis Engine
Structural (NOT predictive) FX analysis with regime classification, fragility gradients, and coupling heatmaps
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum
import time
import logging
from datetime import datetime, timezone
import hashlib

logger = logging.getLogger("AMOS_OMEGA_FX")

class FXRegimeType(Enum):
    STABLE = "stable"
    TRANSITIONING = "transitioning"
    VOLATILE = "volatile"
    STRESSED = "stressed"
    CRISIS = "crisis"

class ShockType(Enum):
    LIQUIDITY = "liquidity"
    VOLATILITY = "volatility"
    POLICY = "policy"
    CONTAGION = "contagion"
    EXTERNAL = "external"

@dataclass
class FXMetrics:
    """Core FX structural metrics"""
    price: float = 0.0
    volatility: float = 0.0
    volume: float = 0.0
    spread: float = 0.0
    liquidity_score: float = 1.0
    momentum: float = 0.0
    mean_reversion_score: float = 0.0
    correlation_index: float = 0.0
    timestamp: float = 0.0

@dataclass
class RegimeClassification:
    """FX regime classification"""
    regime: FXRegimeType
    confidence: float = 0.0
    stability_margin: float = 0.0
    transition_probability: float = 0.0
    duration_expected: float = 0.0
    key_drivers: List[str] = None

@dataclass
class FragilityGradient:
    """System fragility gradient analysis"""
    overall_fragility: float = 0.0
    liquidity_fragility: float = 0.0
    volatility_fragility: float = 0.0
    correlation_fragility: float = 0.0
    policy_fragility: float = 0.0
    external_fragility: float = 0.0
    critical_thresholds: Dict[str, float] = None
    breach_probability: float = 0.0

@dataclass
class CouplingHeatmap:
    """Inter-market coupling analysis"""
    coupling_matrix: np.ndarray = None
    coupling_strength: float = 0.0
    dominant_pairs: List[Tuple[str, str]] = None
    contagion_risk: float = 0.0
    decoupling_points: List[str] = None

@dataclass
class ShockSensitivity:
    """Shock sensitivity analysis"""
    sensitivity_score: float = 0.0
    liquidity_sensitivity: float = 0.0
    volatility_sensitivity: float = 0.0
    policy_sensitivity: float = 0.0
    contagion_sensitivity: float = 0.0
    worst_case_delta: float = 0.0
    recovery_time_estimate: float = 0.0

@dataclass
class RiskEnvelope:
    """Risk envelope analysis"""
    var_estimate: float = 0.0  # Value at Risk
    expected_shortfall: float = 0.0
    max_drawdown: float = 0.0
    tail_risk: float = 0.0
    liquidity_gap: float = 0.0
    margin_requirement: float = 0.0
    buffer_distance: float = 0.0

@dataclass
class CoherenceAnalysis:
    """Market coherence analysis"""
    coherence_score: float = 0.0
    signal_to_noise: float = 0.0
    structural_integrity: float = 0.0
    information_efficiency: float = 0.0
    anomaly_detection: List[str] = None

class AMOSOmegaFXEngine:
    """AMOS OMEGA FX Structural Analysis Engine"""
    
    def __init__(self):
        self.trace_id = None
        self.determinism_hash = None
        
        # Historical data storage
        self.price_history = deque(maxlen=1000)
        self.volatility_history = deque(maxlen=1000)
        self.volume_history = deque(maxlen=1000)
        self.regime_history = deque(maxlen=100)
        
        # Coupling matrix (simplified 5x5 for major pairs)
        self.pairs = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCAD"]
        self.coupling_matrix = np.eye(len(self.pairs))
        
        # Analysis parameters
        self.regime_thresholds = {
            "volatility_low": 0.01,
            "volatility_high": 0.03,
            "liquidity_low": 0.3,
            "correlation_high": 0.8,
            "spread_wide": 0.002
        }
        
        self.fragility_weights = {
            "liquidity": 0.3,
            "volatility": 0.25,
            "correlation": 0.2,
            "policy": 0.15,
            "external": 0.1
        }
        
        # Shock scenarios
        self.shock_scenarios = {
            ShockType.LIQUIDITY: {"volume_shock": -0.5, "spread_shock": 2.0},
            ShockType.VOLATILITY: {"vol_shock": 3.0, "correlation_shock": 0.3},
            ShockType.POLICY: {"rate_shock": 0.01, "forward_shock": 0.02},
            ShockType.CONTAGION: {"correlation_shock": 0.5, "volatility_spillover": 0.4},
            ShockType.EXTERNAL: {"risk_shock": -0.02, "safe_haven_flow": 0.3}
        }
    
    def _generate_trace_id(self) -> str:
        """Generate trace ID for analysis"""
        timestamp = time.time()
        return hashlib.sha256(f"FX_ANALYSIS_{timestamp}".encode()).hexdigest()[:16]
    
    def _calculate_determinism_hash(self, data: Any) -> str:
        """Calculate deterministic hash"""
        data_str = json.dumps(data, sort_keys=True, default=str)
        return hashlib.sha256(data_str.encode()).hexdigest()
    
    def update_market_data(self, metrics: FXMetrics) -> bool:
        """Update market data with new metrics"""
        try:
            self.price_history.append(metrics.price)
            self.volatility_history.append(metrics.volatility)
            self.volume_history.append(metrics.volume)
            
            # Update coupling matrix (simplified correlation update)
            if len(self.price_history) > 10:
                self._update_coupling_matrix()
            
            return True
            
        except Exception as e:
            logger.error(f"Market data update error: {e}")
            return False
    
    def _update_coupling_matrix(self):
        """Update inter-market coupling matrix"""
        # Simplified correlation calculation
        if len(self.price_history) < 20:
            return
        
        # Create synthetic correlation matrix based on volatility regime
        vol_regime = np.mean(list(self.volatility_history)[-20:])
        
        if vol_regime < self.regime_thresholds["volatility_low"]:
            # Low volatility - lower correlations
            base_correlation = 0.3
        elif vol_regime > self.regime_thresholds["volatility_high"]:
            # High volatility - higher correlations
            base_correlation = 0.7
        else:
            # Normal volatility
            base_correlation = 0.5
        
        # Update coupling matrix with some noise
        noise = np.random.normal(0, 0.1, (len(self.pairs), len(self.pairs)))
        self.coupling_matrix = base_correlation * np.ones((len(self.pairs), len(self.pairs))) + noise
        self.coupling_matrix = (self.coupling_matrix + self.coupling_matrix.T) / 2
        np.fill_diagonal(self.coupling_matrix, 1.0)
        
        # Ensure bounds
        self.coupling_matrix = np.clip(self.coupling_matrix, -1.0, 1.0)
    
    def classify_regime(self, metrics: FXMetrics) -> RegimeClassification:
        """Classify current market regime"""
        regime_features = {
            "volatility_level": metrics.volatility,
            "liquidity_score": metrics.liquidity_score,
            "spread_level": metrics.spread,
            "correlation_index": metrics.correlation_index,
            "momentum_strength": abs(metrics.momentum)
        }
        
        # Calculate regime scores
        stability_score = 1.0
        
        # Volatility assessment
        if metrics.volatility < self.regime_thresholds["volatility_low"]:
            stability_score += 0.2
        elif metrics.volatility > self.regime_thresholds["volatility_high"]:
            stability_score -= 0.3
        
        # Liquidity assessment
        if metrics.liquidity_score > self.regime_thresholds["liquidity_low"]:
            stability_score += 0.2
        else:
            stability_score -= 0.3
        
        # Correlation assessment
        if metrics.correlation_index < self.regime_thresholds["correlation_high"]:
            stability_score += 0.1
        else:
            stability_score -= 0.2
        
        # Spread assessment
        if metrics.spread < self.regime_thresholds["spread_wide"]:
            stability_score += 0.1
        else:
            stability_score -= 0.2
        
        # Determine regime
        if stability_score > 1.2:
            regime = FXRegimeType.STABLE
            confidence = min(1.0, (stability_score - 1.2) / 0.3)
        elif stability_score > 0.8:
            regime = FXRegimeType.TRANSITIONING
            confidence = min(1.0, (stability_score - 0.8) / 0.4)
        elif stability_score > 0.4:
            regime = FXRegimeType.VOLATILE
            confidence = min(1.0, (stability_score - 0.4) / 0.4)
        elif stability_score > 0.0:
            regime = FXRegimeType.STRESSED
            confidence = min(1.0, stability_score / 0.4)
        else:
            regime = FXRegimeType.CRISIS
            confidence = 1.0
        
        # Calculate stability margin
        stability_margin = max(0.0, stability_score)
        
        # Estimate transition probability
        transition_probability = 1.0 - confidence
        
        # Identify key drivers
        key_drivers = []
        if metrics.volatility > self.regime_thresholds["volatility_high"]:
            key_drivers.append("high_volatility")
        if metrics.liquidity_score < self.regime_thresholds["liquidity_low"]:
            key_drivers.append("low_liquidity")
        if metrics.correlation_index > self.regime_thresholds["correlation_high"]:
            key_drivers.append("high_correlation")
        if metrics.spread > self.regime_thresholds["spread_wide"]:
            key_drivers.append("wide_spreads")
        
        return RegimeClassification(
            regime=regime,
            confidence=confidence,
            stability_margin=stability_margin,
            transition_probability=transition_probability,
            duration_expected=self._estimate_regime_duration(regime),
            key_drivers=key_drivers
        )
    
    def _estimate_regime_duration(self, regime: FXRegimeType) -> float:
        """Estimate expected regime duration in hours"""
        duration_map = {
            FXRegimeType.STABLE: 24.0,
            FXRegimeType.TRANSITIONING: 6.0,
            FXRegimeType.VOLATILE: 12.0,
            FXRegimeType.STRESSED: 8.0,
            FXRegimeType.CRISIS: 2.0
        }
        return duration_map.get(regime, 12.0)
    
    def calculate_fragility_gradient(self, metrics: FXMetrics) -> FragilityGradient:
        """Calculate system fragility gradient"""
        # Individual fragility components
        liquidity_fragility = max(0.0, 1.0 - metrics.liquidity_score)
        
        volatility_fragility = min(1.0, metrics.volatility / self.regime_thresholds["volatility_high"])
        
        correlation_fragility = min(1.0, metrics.correlation_index / self.regime_thresholds["correlation_high"])
        
        policy_fragility = 0.3  # Simplified policy risk assessment
        external_fragility = 0.2  # Simplified external risk assessment
        
        # Weighted overall fragility
        overall_fragility = (
            liquidity_fragility * self.fragility_weights["liquidity"] +
            volatility_fragility * self.fragility_weights["volatility"] +
            correlation_fragility * self.fragility_weights["correlation"] +
            policy_fragility * self.fragility_weights["policy"] +
            external_fragility * self.fragility_weights["external"]
        )
        
        # Critical thresholds
        critical_thresholds = {
            "liquidity_critical": 0.2,
            "volatility_critical": 0.05,
            "correlation_critical": 0.9,
            "spread_critical": 0.005
        }
        
        # Breach probability
        breach_probability = min(1.0, overall_fragility * 1.5)
        
        return FragilityGradient(
            overall_fragility=overall_fragility,
            liquidity_fragility=liquidity_fragility,
            volatility_fragility=volatility_fragility,
            correlation_fragility=correlation_fragility,
            policy_fragility=policy_fragility,
            external_fragility=external_fragility,
            critical_thresholds=critical_thresholds,
            breach_probability=breach_probability
        )
    
    def analyze_coupling_heatmap(self) -> CouplingHeatmap:
        """Analyze inter-market coupling heatmap"""
        # Calculate coupling strength
        coupling_strength = np.mean(np.abs(self.coupling_matrix[np.triu_indices(len(self.pairs), k=1)]))
        
        # Find dominant pairs
        dominant_pairs = []
        threshold = 0.6
        
        for i in range(len(self.pairs)):
            for j in range(i + 1, len(self.pairs)):
                if abs(self.coupling_matrix[i, j]) > threshold:
                    dominant_pairs.append((self.pairs[i], self.pairs[j]))
        
        # Assess contagion risk
        contagion_risk = min(1.0, coupling_strength * 1.2)
        
        # Identify decoupling points
        decoupling_points = []
        for i in range(len(self.pairs)):
            if np.mean(np.abs(self.coupling_matrix[i, :])) < 0.3:
                decoupling_points.append(self.pairs[i])
        
        return CouplingHeatmap(
            coupling_matrix=self.coupling_matrix.copy(),
            coupling_strength=coupling_strength,
            dominant_pairs=dominant_pairs,
            contagion_risk=contagion_risk,
            decoupling_points=decoupling_points
        )
    
    def analyze_shock_sensitivity(self, metrics: FXMetrics, shock_type: ShockType) -> ShockSensitivity:
        """Analyze sensitivity to specific shock types"""
        scenario = self.shock_scenarios.get(shock_type, {})
        
        # Calculate sensitivity components
        if shock_type == ShockType.LIQUIDITY:
            liquidity_sensitivity = 0.9
            volatility_sensitivity = 0.6
            policy_sensitivity = 0.3
            contagion_sensitivity = 0.7
        elif shock_type == ShockType.VOLATILITY:
            liquidity_sensitivity = 0.7
            volatility_sensitivity = 0.9
            policy_sensitivity = 0.4
            contagion_sensitivity = 0.8
        elif shock_type == ShockType.POLICY:
            liquidity_sensitivity = 0.5
            volatility_sensitivity = 0.7
            policy_sensitivity = 0.9
            contagion_sensitivity = 0.6
        elif shock_type == ShockType.CONTAGION:
            liquidity_sensitivity = 0.8
            volatility_sensitivity = 0.8
            policy_sensitivity = 0.5
            contagion_sensitivity = 0.9
        else:  # EXTERNAL
            liquidity_sensitivity = 0.6
            volatility_sensitivity = 0.7
            policy_sensitivity = 0.4
            contagion_sensitivity = 0.5
        
        # Overall sensitivity
        sensitivity_score = (
            liquidity_sensitivity * 0.3 +
            volatility_sensitivity * 0.3 +
            policy_sensitivity * 0.2 +
            contagion_sensitivity * 0.2
        )
        
        # Worst case delta (simplified)
        worst_case_delta = sensitivity_score * 0.05  # 5% max move
        
        # Recovery time estimate
        if shock_type == ShockType.LIQUIDITY:
            recovery_time = 24.0  # hours
        elif shock_type == ShockType.VOLATILITY:
            recovery_time = 12.0
        elif shock_type == ShockType.POLICY:
            recovery_time = 48.0
        elif shock_type == ShockType.CONTAGION:
            recovery_time = 72.0
        else:
            recovery_time = 18.0
        
        return ShockSensitivity(
            sensitivity_score=sensitivity_score,
            liquidity_sensitivity=liquidity_sensitivity,
            volatility_sensitivity=volatility_sensitivity,
            policy_sensitivity=policy_sensitivity,
            contagion_sensitivity=contagion_sensitivity,
            worst_case_delta=worst_case_delta,
            recovery_time_estimate=recovery_time
        )
    
    def calculate_risk_envelope(self, metrics: FXMetrics, lookback_days: int = 20) -> RiskEnvelope:
        """Calculate risk envelope with structural metrics"""
        if len(self.price_history) < lookback_days:
            # Default values if insufficient data
            return RiskEnvelope(
                var_estimate=0.02,
                expected_shortfall=0.03,
                max_drawdown=0.05,
                tail_risk=0.1,
                liquidity_gap=0.001,
                margin_requirement=0.02,
                buffer_distance=0.8
            )
        
        # Calculate returns
        prices = np.array(list(self.price_history)[-lookback_days:])
        returns = np.diff(prices) / prices[:-1]
        
        # VaR calculation (95% confidence)
        var_estimate = np.percentile(abs(returns), 95)
        
        # Expected shortfall
        var_threshold = var_estimate
        tail_returns = returns[abs(returns) > var_threshold]
        expected_shortfall = np.mean(abs(tail_returns)) if len(tail_returns) > 0 else var_estimate
        
        # Maximum drawdown
        cumulative_returns = np.cumprod(1 + returns)
        peak = np.maximum.accumulate(cumulative_returns)
        drawdown = (cumulative_returns - peak) / peak
        max_drawdown = abs(np.min(drawdown))
        
        # Tail risk (kurtosis-based)
        tail_risk = np.mean(returns**4) / (np.mean(returns**2)**2) - 3
        
        # Liquidity gap
        liquidity_gap = max(0.0, self.regime_thresholds["spread_wide"] - metrics.spread)
        
        # Margin requirement (simplified)
        margin_requirement = var_estimate * 2.0
        
        # Buffer distance
        buffer_distance = max(0.0, 1.0 - (var_estimate / 0.05))
        
        return RiskEnvelope(
            var_estimate=var_estimate,
            expected_shortfall=expected_shortfall,
            max_drawdown=max_drawdown,
            tail_risk=tail_risk,
            liquidity_gap=liquidity_gap,
            margin_requirement=margin_requirement,
            buffer_distance=buffer_distance
        )
    
    def analyze_coherence(self, metrics: FXMetrics) -> CoherenceAnalysis:
        """Analyze market coherence and structural integrity"""
        # Coherence score based on multiple factors
        coherence_factors = {
            "liquidity_coherence": metrics.liquidity_score,
            "volatility_coherence": 1.0 - min(1.0, metrics.volatility / 0.05),
            "spread_coherence": 1.0 - min(1.0, metrics.spread / 0.005),
            "correlation_coherence": 1.0 - min(1.0, metrics.correlation_index / 0.9),
            "momentum_coherence": 1.0 - min(1.0, abs(metrics.momentum) / 0.1)
        }
        
        coherence_score = np.mean(list(coherence_factors.values()))
        
        # Signal to noise ratio
        signal_strength = abs(metrics.momentum)
        noise_level = metrics.volatility
        signal_to_noise = signal_strength / (noise_level + 0.001)
        
        # Structural integrity
        structural_integrity = min(1.0, coherence_score * (1.0 + signal_to_noise * 0.1))
        
        # Information efficiency
        information_efficiency = 1.0 - min(1.0, metrics.mean_reversion_score)
        
        # Anomaly detection
        anomalies = []
        if metrics.volatility > 0.04:
            anomalies.append("extreme_volatility")
        if metrics.liquidity_score < 0.2:
            anomalies.append("liquidity_crisis")
        if metrics.spread > 0.01:
            anomalies.append("extreme_spread")
        if abs(metrics.momentum) > 0.15:
            anomalies.append("extreme_momentum")
        
        return CoherenceAnalysis(
            coherence_score=coherence_score,
            signal_to_noise=signal_to_noise,
            structural_integrity=structural_integrity,
            information_efficiency=information_efficiency,
            anomaly_detection=anomalies
        )
    
    def comprehensive_analysis(self, metrics: FXMetrics) -> Dict[str, Any]:
        """Perform comprehensive FX structural analysis"""
        self.trace_id = self._generate_trace_id()
        
        try:
            # Update market data
            self.update_market_data(metrics)
            
            # Perform all analyses
            regime = self.classify_regime(metrics)
            fragility = self.calculate_fragility_gradient(metrics)
            coupling = self.analyze_coupling_heatmap()
            risk_envelope = self.calculate_risk_envelope(metrics)
            coherence = self.analyze_coherence(metrics)
            
            # Shock sensitivity for all types
            shock_sensitivities = {}
            for shock_type in ShockType:
                shock_sensitivities[shock_type.value] = self.analyze_shock_sensitivity(metrics, shock_type)
            
            # Compile results
            analysis_result = {
                "trace_id": self.trace_id,
                "timestamp": time.time(),
                "input_metrics": asdict(metrics),
                "regime_classification": asdict(regime),
                "fragility_gradient": asdict(fragility),
                "coupling_heatmap": {
                    "coupling_strength": coupling.coupling_strength,
                    "dominant_pairs": coupling.dominant_pairs,
                    "contagion_risk": coupling.contagion_risk,
                    "decoupling_points": coupling.decoupling_points
                },
                "risk_envelope": asdict(risk_envelope),
                "coherence_analysis": asdict(coherence),
                "shock_sensitivities": {k: asdict(v) for k, v in shock_sensitivities.items()},
                "system_health": {
                    "overall_stability": regime.stability_margin,
                    "fragility_level": fragility.overall_fragility,
                    "risk_level": risk_envelope.var_estimate,
                    "coherence_level": coherence.coherence_score
                }
            }
            
            # Calculate determinism hash
            self.determinism_hash = self._calculate_determinism_hash(analysis_result)
            analysis_result["determinism_hash"] = self.determinism_hash
            
            return analysis_result
            
        except Exception as e:
            logger.error(f"Comprehensive analysis error: {e}")
            return {
                "trace_id": self.trace_id,
                "error": str(e),
                "timestamp": time.time()
            }

# Global FX engine instance
fx_engine = AMOSOmegaFXEngine()

if __name__ == "__main__":
    # Test FX engine
    print("AMOS OMEGA FX Engine Test...")
    
    # Create test metrics
    test_metrics = FXMetrics(
        price=1.0850,
        volatility=0.025,
        volume=1000000,
        spread=0.0002,
        liquidity_score=0.8,
        momentum=0.02,
        mean_reversion_score=0.3,
        correlation_index=0.6,
        timestamp=time.time()
    )
    
    # Run comprehensive analysis
    result = fx_engine.comprehensive_analysis(test_metrics)
    
    print("FX Analysis Result:")
    print(json.dumps(result, indent=2, default=str))


```

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[ENGINE_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
