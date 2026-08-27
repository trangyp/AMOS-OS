---
tags: [economy]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Emotional Stability → Market Risk Dashboard </title><style>
/* cspell:disable-file */
/* webkit printing magic: print all background colors */
html {
	-webkit-print-color-adjust: exact;
}
* {
	box-sizing: border-box;
	-webkit-print-color-adjust: exact;
}

html,
body {
	margin: 0;
	padding: 0;
}
@media only screen {
	body {
		margin: 2em auto;
		max-width: 900px;
		color: rgb(55, 53, 47);
	}
}

body {
	line-height: 1.5;
	white-space: pre-wrap;
}

a,
a.visited {
	color: inherit;
	text-decoration: underline;
}

.pdf-relative-link-path {
	font-size: 80%;
	color: #444;
}

h1,
h2,
h3 {
	letter-spacing: -0.01em;
	line-height: 1.2;
	font-weight: 600;
	margin-bottom: 0;
}

/* Override strong tags inside headings to maintain consistent weight */
h1 strong,
h2 strong,
h3 strong {
	font-weight: 600;
}

.page-title {
	font-size: 2.5rem;
	font-weight: 700;
	margin-top: 0;
	margin-bottom: 0.75em;
}

h1 {
	font-size: 1.875rem;
	margin-top: 1.875rem;
}

h2 {
	font-size: 1.5rem;
	margin-top: 1.5rem;
}

h3 {
	font-size: 1.25rem;
	margin-top: 1.25rem;
}

.source {
	border: 1px solid #ddd;
	border-radius: 3px;
	padding: 1.5em;
	word-break: break-all;
}

.callout {
	border-radius: 10px;
	padding: 1rem;
}

figure {
	margin: 1.25em 0;
	page-break-inside: avoid;
}

figcaption {
	opacity: 0.5;
	font-size: 85%;
	margin-top: 0.5em;
}

mark {
	background-color: transparent;
}

.indented {
	padding-left: 1.5em;
}

hr {
	background: transparent;
	display: block;
	width: 100%;
	height: 1px;
	visibility: visible;
	border: none;
	border-bottom: 1px solid rgba(55, 53, 47, 0.09);
}

img {
	max-width: 100%;
}

@media only print {
	img {
		max-height: 100vh;
		object-fit: contain;
	}

	table.collection-content {
		width: 100%;
		table-layout: fixed;
	}

	table.collection-content th,
	table.collection-content td {
		overflow-wrap: anywhere;
	}

	table.collection-content td > .user,
	table.collection-content td > time {
		white-space: pre-wrap;
	}
}

@page {
	margin: 1in;
}

.collection-content-wrapper {
	overflow-x: auto;
}

@media only print {
	.collection-content-wrapper {
		overflow-x: visible;
	}
}

.collection-content {
	font-size: 0.875rem;
}

.collection-content td {
	white-space: pre-wrap;
	word-break: break-word;
}

.column-list {
	display: flex;
	gap: 46px;
}

.column {
	min-width: 0;
	overflow: hidden;
}

.column > *:first-child {
	margin-top: 0;
}

.table_of_contents-item {
	display: block;
	font-size: 0.875rem;
	line-height: 1.3;
	padding: 0.125rem;
}

.table_of_contents-indent-1 {
	margin-left: 1.5rem;
}

.table_of_contents-indent-2 {
	margin-left: 3rem;
}

.table_of_contents-indent-3 {
	margin-left: 4.5rem;
}

.table_of_contents-link {
	text-decoration: none;
	opacity: 0.7;
	border-bottom: 1px solid rgba(55, 53, 47, 0.18);
}

table,
th,
td {
	border: 1px solid rgba(55, 53, 47, 0.09);
	border-collapse: collapse;
}

table {
	border-left: none;
	border-right: none;
}

th,
td {
	font-weight: normal;
	padding: 0.25em 0.5em;
	line-height: 1.5;
	min-height: 1.5em;
	text-align: left;
}

th {
	color: rgba(55, 53, 47, 0.6);
}

ol,
ul {
	margin: 0;
	margin-block-start: 0.6em;
	margin-block-end: 0.6em;
}

li > ol:first-child,
li > ul:first-child {
	margin-block-start: 0.6em;
}

ul > li {
	list-style: disc;
}

ul.to-do-list {
	padding-inline-start: 0;
}

ul.to-do-list > li {
	list-style: none;
}

.to-do-children-checked {
	text-decoration: line-through;
	opacity: 0.375;
}

ul.toggle > li {
	list-style: none;
}

ul {
	padding-inline-start: 1.7em;
}

ul > li {
	padding-left: 0.1em;
}

ol {
	padding-inline-start: 1.6em;
}

ol.numbered-list.numbered-list-digits-2 {
	padding-inline-start: 2em;
}

ol.numbered-list.numbered-list-digits-3plus {
	padding-inline-start: 2.4em;
}

ol > li {
	padding-left: 0.2em;
}

.mono ol {
	padding-inline-start: 2em;
}

.mono ol > li {
	text-indent: -0.4em;
}

.toggle {
	padding-inline-start: 0em;
	list-style-type: none;
}

/* Indent toggle children */
.toggle > li > details {
	padding-left: 1.7em;
}

.toggle > li > details > summary {
	margin-left: -1.1em;
}

.selected-value {
	display: inline-block;
	padding: 0 0.5em;
	background: rgba(206, 205, 202, 0.5);
	border-radius: 3px;
	margin-right: 0.5em;
	margin-top: 0.3em;
	margin-bottom: 0.3em;
	white-space: nowrap;
}

.collection-title {
	display: inline-block;
	margin-right: 1em;
}

.page-description {
	margin-bottom: 2em;
}

.simple-table {
	margin-top: 1em;
	font-size: 0.875rem;
	empty-cells: show;
}
.simple-table td {
	height: 29px;
	min-width: 120px;
}

.simple-table th {
	height: 29px;
	min-width: 120px;
}

.simple-table-header-color {
	background: rgb(247, 246, 243);
	color: black;
}
.simple-table-header {
	font-weight: 500;
}

time {
	opacity: 0.5;
}

.icon {
	display: inline-flex;
	align-items: center;
	justify-content: center;
	max-width: 1.2em;
	max-height: 1.2em;
	text-decoration: none;
	vertical-align: text-bottom;
	margin-right: 0.5em;
}

img.icon {
	border-radius: 3px;
}

.callout img.notion-static-icon {
	width: 1em;
	height: 1em;
}

.callout p {
	margin: 0;
}

.callout h1,
.callout h2,
.callout h3 {
	margin: 0 0 0.6rem;
}

.user-icon {
	width: 1.5em;
	height: 1.5em;
	border-radius: 100%;
	margin-right: 0.5rem;
}

.user-icon-inner {
	font-size: 0.8em;
}

.text-icon {
	border: 1px solid #000;
	text-align: center;
}

.page-cover-image {
	display: block;
	object-fit: cover;
	width: 100%;
	max-height: 30vh;
}

.page-header-icon {
	font-size: 3rem;
	margin-bottom: 1rem;
}

.page-header-icon-with-cover {
	margin-top: -0.72em;
	margin-left: 0.07em;
}

.page-header-icon img {
	border-radius: 3px;
}

.link-to-page {
	margin: 1em 0;
	padding: 0;
	border: none;
	font-weight: 500;
}

p > .user {
	opacity: 0.5;
}

td > .user,
td > time {
	white-space: nowrap;
}

input[type="checkbox"] {
	transform: scale(1.5);
	margin-right: 0.6em;
	vertical-align: middle;
}

p {
	margin-top: 0.5em;
	margin-bottom: 0.5em;
}

.image {
	border: none;
	margin: 1.5em 0;
	padding: 0;
	border-radius: 0;
	text-align: center;
}

.code,
code {
	background: rgba(135, 131, 120, 0.15);
	border-radius: 3px;
	padding: 0.2em 0.4em;
	border-radius: 3px;
	font-size: 85%;
	tab-size: 2;
}

code {
	color: #eb5757;
}

.code {
	padding: 1.5em 1em;
}

.code-wrap {
	white-space: pre-wrap;
	word-break: break-all;
}

.code > code {
	background: none;
	padding: 0;
	font-size: 100%;
	color: inherit;
}

blockquote {
	font-size: 1em;
	margin: 1em 0;
	padding-left: 1em;
	border-left: 3px solid rgb(55, 53, 47);
}

blockquote.quote-large {
	font-size: 1.25em;
}

.bookmark {
	text-decoration: none;
	max-height: 8em;
	padding: 0;
	display: flex;
	width: 100%;
	align-items: stretch;
}

.bookmark-title {
	font-size: 0.85em;
	overflow: hidden;
	text-overflow: ellipsis;
	height: 1.75em;
	white-space: nowrap;
}

.bookmark-text {
	display: flex;
	flex-direction: column;
}

.bookmark-info {
	flex: 4 1 180px;
	padding: 12px 14px 14px;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}

.bookmark-image {
	width: 33%;
	flex: 1 1 180px;
	display: block;
	position: relative;
	object-fit: cover;
	border-radius: 1px;
}

.bookmark-description {
	color: rgba(55, 53, 47, 0.6);
	font-size: 0.75em;
	overflow: hidden;
	max-height: 4.5em;
	word-break: break-word;
}

.bookmark-href {
	font-size: 0.75em;
	margin-top: 0.25em;
}

.sans { font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", "Noto Sans Arabic", "Noto Sans Hebrew", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol"; }
.code { font-family: "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace; }
.serif { font-family: Lyon-Text, Georgia, ui-serif, serif; }
.mono { font-family: iawriter-mono, Nitti, Menlo, Courier, monospace; }
.pdf .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", "Noto Sans Arabic", "Noto Sans Hebrew", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK JP'; }
.pdf:lang(zh-CN) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", "Noto Sans Arabic", "Noto Sans Hebrew", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK SC'; }
.pdf:lang(zh-TW) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", "Noto Sans Arabic", "Noto Sans Hebrew", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK TC'; }
.pdf:lang(ko-KR) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", "Noto Sans Arabic", "Noto Sans Hebrew", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK KR'; }
.pdf .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.pdf .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK JP'; }
.pdf:lang(zh-CN) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK SC'; }
.pdf:lang(zh-TW) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK TC'; }
.pdf:lang(ko-KR) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK KR'; }
.pdf .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.highlight-default {
	color: rgba(44, 44, 43, 1);
}
.highlight-gray {
	color: rgba(125, 122, 117, 1);
	fill: rgba(125, 122, 117, 1);
}
.highlight-brown {
	color: rgba(159, 118, 90, 1);
	fill: rgba(159, 118, 90, 1);
}
.highlight-orange {
	color: rgba(210, 123, 45, 1);
	fill: rgba(210, 123, 45, 1);
}
.highlight-yellow {
	color: rgba(203, 148, 52, 1);
	fill: rgba(203, 148, 52, 1);
}
.highlight-teal {
	color: rgba(80, 148, 110, 1);
	fill: rgba(80, 148, 110, 1);
}
.highlight-blue {
	color: rgba(56, 125, 201, 1);
	fill: rgba(56, 125, 201, 1);
}
.highlight-purple {
	color: rgba(154, 107, 180, 1);
	fill: rgba(154, 107, 180, 1);
}
.highlight-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(193, 76, 138, 1);
}
.highlight-red {
	color: rgba(207, 81, 72, 1);
	fill: rgba(207, 81, 72, 1);
}
.highlight-default_background {
	color: rgba(44, 44, 43, 1);
}
.highlight-gray_background {
	background: rgba(42, 28, 0, 0.07);
}
.highlight-brown_background {
	background: rgba(139, 46, 0, 0.086);
}
.highlight-orange_background {
	background: rgba(224, 101, 1, 0.129);
}
.highlight-yellow_background {
	background: rgba(211, 168, 0, 0.137);
}
.highlight-teal_background {
	background: rgba(0, 100, 45, 0.09);
}
.highlight-blue_background {
	background: rgba(0, 124, 215, 0.094);
}
.highlight-purple_background {
	background: rgba(102, 0, 178, 0.078);
}
.highlight-pink_background {
	background: rgba(197, 0, 93, 0.086);
}
.highlight-red_background {
	background: rgba(223, 22, 0, 0.094);
}
.block-color-default {
	color: inherit;
	fill: inherit;
}
.block-color-gray {
	color: rgba(125, 122, 117, 1);
	fill: rgba(125, 122, 117, 1);
}
.block-color-brown {
	color: rgba(159, 118, 90, 1);
	fill: rgba(159, 118, 90, 1);
}
.block-color-orange {
	color: rgba(210, 123, 45, 1);
	fill: rgba(210, 123, 45, 1);
}
.block-color-yellow {
	color: rgba(203, 148, 52, 1);
	fill: rgba(203, 148, 52, 1);
}
.block-color-teal {
	color: rgba(80, 148, 110, 1);
	fill: rgba(80, 148, 110, 1);
}
.block-color-blue {
	color: rgba(56, 125, 201, 1);
	fill: rgba(56, 125, 201, 1);
}
.block-color-purple {
	color: rgba(154, 107, 180, 1);
	fill: rgba(154, 107, 180, 1);
}
.block-color-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(193, 76, 138, 1);
}
.block-color-red {
	color: rgba(207, 81, 72, 1);
	fill: rgba(207, 81, 72, 1);
}
.block-color-default_background {
	color: inherit;
	fill: inherit;
}
.block-color-gray_background {
	background: rgba(240, 239, 237, 1);
}
.block-color-brown_background {
	background: rgba(245, 237, 233, 1);
}
.block-color-orange_background {
	background: rgba(251, 235, 222, 1);
}
.block-color-yellow_background {
	background: rgba(249, 243, 220, 1);
}
.block-color-teal_background {
	background: rgba(232, 241, 236, 1);
}
.block-color-blue_background {
	background: rgba(229, 242, 252, 1);
}
.block-color-purple_background {
	background: rgba(243, 235, 249, 1);
}
.block-color-pink_background {
	background: rgba(250, 233, 241, 1);
}
.block-color-red_background {
	background: rgba(252, 233, 231, 1);
}
.select-value-color-default { background-color: rgba(42, 28, 0, 0.07); }
.select-value-color-gray { background-color: rgba(28, 19, 1, 0.11); }
.select-value-color-brown { background-color: rgba(127, 51, 0, 0.156); }
.select-value-color-orange { background-color: rgba(196, 88, 0, 0.203); }
.select-value-color-yellow { background-color: rgba(209, 156, 0, 0.282); }
.select-value-color-green { background-color: rgba(0, 96, 38, 0.156); }
.select-value-color-blue { background-color: rgba(0, 118, 217, 0.203); }
.select-value-color-purple { background-color: rgba(92, 0, 163, 0.141); }
.select-value-color-pink { background-color: rgba(183, 0, 78, 0.152); }
.select-value-color-red { background-color: rgba(206, 24, 0, 0.164); }

.checkbox {
	display: inline-flex;
	vertical-align: text-bottom;
	width: 16;
	height: 16;
	background-size: 16px;
	margin-left: 2px;
	margin-right: 5px;
}

.checkbox-on {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20width%3D%2216%22%20height%3D%2216%22%20fill%3D%22%2358A9D7%22%2F%3E%0A%3Cpath%20d%3D%22M6.71429%2012.2852L14%204.9995L12.7143%203.71436L6.71429%209.71378L3.28571%206.2831L2%207.57092L6.71429%2012.2852Z%22%20fill%3D%22white%22%2F%3E%0A%3C%2Fsvg%3E");
}

.checkbox-off {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20x%3D%220.75%22%20y%3D%220.75%22%20width%3D%2214.5%22%20height%3D%2214.5%22%20fill%3D%22white%22%20stroke%3D%22%2336352F%22%20stroke-width%3D%221.5%22%2F%3E%0A%3C%2Fsvg%3E");
}
	
</style></head><body><article id="277c5e6f-95bd-80a3-ba2c-d5a79f60a241" class="page sans"><header><h1 class="page-title" dir="auto">Emotional Stability → Market Risk Dashboard </h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-80e8-ae88-ee17ea9189b6" class=""><strong>Why We Need It</strong></p></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-80b0-bd50-d29e07c000e4" class="">This dashboard is a predictive early-warning system that monitors market behaviour, liquidity, leverage, sentiment, and on-chain flows to detect when the market becomes unstable.</p></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-806d-b46d-c415da9b387b" class=""><strong>Why It Matters</strong></p></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-80f7-b36e-f256181b04cf" class="">Protects Capital: Gives us hours or days of lead time before major market drops, letting us adjust exposure and preserve value.</p></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-8057-a278-c1bd8696ff59" class="">Builds Trust: Shows users and investors that Educhain Fintech is professionally managed with institutional-grade risk controls.</p></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-80bf-a565-db7981c47eba" class="">Strengthens Decisions: Converts complex market data into a single, clear Market Risk Index (MRI) that management can act on.</p></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-8076-a7bf-ddae10dd6148" class="">Supports Growth: A stable, risk-aware platform attracts more partners and larger capital inflows because we can prove we manage volatility intelligently.</p></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-804a-a024-d9411670b945" class=""><strong>Outcome</strong></p></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-8000-81fa-f7088bdae6cc" class="">By building this dashboard, Educhain Fintech positions itself as a safer, more professional ecosystem, capable of navigating volatile markets and protecting both investors and users — which directly increases confidence, adoption, and valuation.</p></div><div style="display:contents" dir="auto"><h2 id="277c5e6f-95bd-80a5-9928-e2388d231a5b" class="">Goal</h2></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-807c-86ed-c737f15634e7" class="">Build a <strong>predictive early-warning system</strong> for sharp drawdowns by converting market “emotional instability” into a 0–100 <strong>Market Risk Index (MRI)</strong> with actionable alerts.</p></div><div style="display:contents" dir="auto"><hr id="277c5e6f-95bd-80b8-81d7-d58a55da8268"/></div><div style="display:contents" dir="auto"><h2 id="277c5e6f-95bd-8016-a34f-d44134d431ee" class="">🏆 What is it? </h2></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-80e5-9632-c1c521da499f" class="">This model isn’t just “cool tech” — it’s a <strong>decision-making weapon</strong>:</p></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80a2-bc64-ff5a25031c74" class="bulleted-list"><li style="list-style-type:disc">Lets you <strong>front-run liquidations</strong> and avoid getting trapped.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-807b-a861-c2052fd92f9e" class="bulleted-list"><li style="list-style-type:disc">Lets you <strong>scale in or out strategically</strong> rather than emotionally.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80e3-9870-e18bded6f6c1" class="bulleted-list"><li style="list-style-type:disc">Gives you the confidence to speak with investors, partners, and boards with data, not guesswork.</li></ul></div><div style="display:contents" dir="auto"><h1 id="277c5e6f-95bd-80a3-83ec-d45e88e824a6" class="">Core signals</h1></div><div style="display:contents" dir="auto"><ol type="1" id="277c5e6f-95bd-8099-a56f-c143f2c803bc" class="numbered-list" start="1"><li><strong>Volatility Shock</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-807b-9f46-ff320272e000" class="bulleted-list"><li style="list-style-type:disc">Realized vol (24h, 7d), ATR(14), Bollinger Band width.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8071-92d5-f06c8b1c1afd" class="bulleted-list"><li style="list-style-type:disc">Trigger: 7d vol / 30d vol &gt; <strong>1.6</strong> or BB width &gt; <strong>2.2×</strong> 90-day median.</li></ul></div><div style="display:contents" dir="auto"><ol type="1" id="277c5e6f-95bd-80fc-b0f2-e4845f31eec6" class="numbered-list" start="1"><li><strong>Liquidity Fragility</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80e1-a128-d46a8e36f46d" class="bulleted-list"><li style="list-style-type:disc">Order-book depth within ±1% and ±2% mid-price.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8029-b5a7-ec09afd332ed" class="bulleted-list"><li style="list-style-type:disc">Bid/ask imbalance = (BidDepth − AskDepth) / (BidDepth + AskDepth).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80e5-a8e5-f37a40a1ca7d" class="bulleted-list"><li style="list-style-type:disc">Trigger: Depth/MarketCap in bottom <strong>10%</strong> of 1-year history or imbalance &lt; <strong>−0.35</strong>.</li></ul></div><div style="display:contents" dir="auto"><ol type="1" id="277c5e6f-95bd-80a2-b1a0-faf2d56df89c" class="numbered-list" start="1"><li><strong>Leverage Stress</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8092-89d9-c870748920eb" class="bulleted-list"><li style="list-style-type:disc">Perp funding rate (hourly, 8h), open interest (OI), OI/MarketCap.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80bf-9e33-d8a8651e99e2" class="bulleted-list"><li style="list-style-type:disc">“Crowded Longs” index = z-score(funding) + z-score(OI/MCAP).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80be-bd1b-e5a93a44ad47" class="bulleted-list"><li style="list-style-type:disc">Trigger: index &gt; <strong>2.0</strong> and price momentum turns negative (5×1h EMAs cross down).</li></ul></div><div style="display:contents" dir="auto"><ol type="1" id="277c5e6f-95bd-80b7-a797-d0bf49c9942b" class="numbered-list" start="1"><li><strong>Liquidation Overhang</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80b9-9525-dd3e75bf1405" class="bulleted-list"><li style="list-style-type:disc">Cumulative long liquidation levels (heatmap by price) from derivatives venues.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-801f-8be8-f88ebff578c4" class="bulleted-list"><li style="list-style-type:disc">Trigger: ≥ <strong>$X</strong> notional liquidations sitting within <strong>−3%</strong> of spot and growing &gt; <strong>20%</strong> d/d.</li></ul></div><div style="display:contents" dir="auto"><ol type="1" id="277c5e6f-95bd-80a7-aca8-e3e2578635fc" class="numbered-list" start="1"><li><strong>Flow &amp; Breadth</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80ab-80f7-d1fb2a9a5c18" class="bulleted-list"><li style="list-style-type:disc">Net exchange inflows (spot) 24h &amp; 7d.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80ef-88b1-ea247f5048f5" class="bulleted-list"><li style="list-style-type:disc">% of majors above 20D MA (market breadth).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8077-95a5-e95acff00e41" class="bulleted-list"><li style="list-style-type:disc">Trigger: inflows &gt; <strong>95th</strong> percentile <strong>and</strong> breadth &lt; <strong>40%</strong>.</li></ul></div><div style="display:contents" dir="auto"><ol type="1" id="277c5e6f-95bd-80ac-a0a4-c2898de4b0a7" class="numbered-list" start="1"><li><strong>Sentiment Instability</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80fd-afe0-c12d1f4b6772" class="bulleted-list"><li style="list-style-type:disc">News/Twitter/Reddit headline polarity (VADER/FinBERT) → rolling 1h &amp; 24h averages.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8004-9111-e0be9a26e739" class="bulleted-list"><li style="list-style-type:disc">“Tone whiplash” = |1h tone − 24h tone|.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8067-9a38-d02618986864" class="bulleted-list"><li style="list-style-type:disc">Trigger: whiplash &gt; <strong>1.2σ</strong> and tone &lt; <strong>−0.2</strong>.</li></ul></div><div style="display:contents" dir="auto"><ol type="1" id="277c5e6f-95bd-8056-84a5-d17c1ffd18ba" class="numbered-list" start="1"><li><strong>Search Anxiety</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8074-9352-ebe85be5c923" class="bulleted-list"><li style="list-style-type:disc">Google Trends for “sell crypto”, “crypto crash”, “recession”, plus local language terms.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8070-aebc-f99430c27260" class="bulleted-list"><li style="list-style-type:disc">Trigger: 3-week MA crosses above 12-week MA by <strong>&gt;25%</strong>.</li></ul></div><div style="display:contents" dir="auto"><ol type="1" id="277c5e6f-95bd-8005-bc14-ede56d59d20e" class="numbered-list" start="1"><li><strong>On-chain Stress (if L1 tokens)</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-807e-93f4-f0e283b3d2f3" class="bulleted-list"><li style="list-style-type:disc">Exchange-bound flows, realized profit/loss (SOPR), age-band distribution (old coins waking up).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80b4-b18a-c4c8588c7d69" class="bulleted-list"><li style="list-style-type:disc">Trigger: SOPR &gt; <strong>1.05</strong> then flips &lt; <strong>1.0</strong> within 72h <strong>and</strong> dormant→active &gt; <strong>2σ</strong>.<br/></li></ul></div><div style="display:contents" dir="auto"><ol type="1" id="277c5e6f-95bd-8098-9f93-dceeef197e85" class="numbered-list" start="1"><li><strong>Options Market Signals (if available)</strong><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80fe-b213-fce7a566c32c" class="bulleted-list"><li style="list-style-type:disc"><strong>Put/Call Skew</strong> (25Δ options): When traders rush for downside protection.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-805e-90c7-d417127c838c" class="bulleted-list"><li style="list-style-type:disc"><strong>IV Rank:</strong> Where implied volatility sits vs its 1y range → cheap/expensive hedging.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8055-9610-c451f5488f27" class="bulleted-list"><li style="list-style-type:disc"><strong>Gamma Exposure:</strong> Shows where dealers will need to sell more as price drops (gamma flip zones).</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="277c5e6f-95bd-80ca-8946-e9a7c565672b" class="numbered-list" start="2"><li><strong>Correlated Asset Stress</strong><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-807d-bad3-ef5c61bfe3d3" class="bulleted-list"><li style="list-style-type:disc">BTC-DXY (dollar index) correlation spikes → risk-off environments.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8087-ab10-de7a78e0019f" class="bulleted-list"><li style="list-style-type:disc">Nasdaq or S&amp;P futures overnight → global macro sentiment feed.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-809f-85a7-c2739b84fa83" class="bulleted-list"><li style="list-style-type:disc">Oil &amp; gold moves — often trigger liquidity events in EM/crypto.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="277c5e6f-95bd-805f-8e18-fd3569c4fa87" class="numbered-list" start="3"><li><strong>Stablecoin Health</strong><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-809a-a46f-d6ba7fb97fe3" class="bulleted-list"><li style="list-style-type:disc">Supply changes in USDT/USDC/BUSD.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8057-a028-e9fcfa9cd777" class="bulleted-list"><li style="list-style-type:disc">Peg deviations &gt;0.3% (especially USDT on CEX/DEX).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-802d-9039-e2f597823526" class="bulleted-list"><li style="list-style-type:disc">On-chain mint/burn activity surges (signal of cash entering/leaving).</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="277c5e6f-95bd-8090-a35b-dc7bf8882051" class="numbered-list" start="4"><li><strong>Whale Behaviour</strong><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80ea-bf29-c557a101e508" class="bulleted-list"><li style="list-style-type:disc">Top wallet cluster netflows (Glassnode/Nansen).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80ff-8f60-f4b968eea278" class="bulleted-list"><li style="list-style-type:disc">Whale CEX deposits &gt; historical 90th percentile = dump risk.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="277c5e6f-95bd-80a3-8749-f82ee1cfe00c" class="numbered-list" start="5"><li><strong>Funding Mix / OI Quality</strong><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-801e-abfb-d4aabc6ce6ec" class="bulleted-list"><li style="list-style-type:disc">Share of OI that’s perps vs dated futures (perps = more fragile).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8065-b3f9-ceec805c657d" class="bulleted-list"><li style="list-style-type:disc">Long/short ratio skew (if &gt;70% long, big squeeze risk).</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="277c5e6f-95bd-80dc-bcbd-f0159ee430be" class="numbered-list" start="6"><li><strong>Cross-venue Stress</strong><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80ff-bdc8-c060f2fc3657" class="bulleted-list"><li style="list-style-type:disc">Spread divergence (spot vs perp, CEX vs DEX) → market dislocation early warning.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8033-9860-c7df6f2000a1" class="bulleted-list"><li style="list-style-type:disc">Rising borrow rates on DeFi lending protocols → leverage getting expensive.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="277c5e6f-95bd-8012-9a7a-e6fc23605ab2" class="numbered-list" start="7"><li><strong>Regulatory / News Shocks</strong><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8067-ba13-d739e3731b15" class="bulleted-list"><li style="list-style-type:disc">Classify headlines: SEC actions, exchange hacks, insolvency rumours.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8023-ac74-f460c5f77503" class="bulleted-list"><li style="list-style-type:disc">Give these a <strong>shock score</strong> (can spike MRI even if market is calm).</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="277c5e6f-95bd-80bf-971d-c2ac89dc0bf2"/></div><div style="display:contents" dir="auto"><h1 id="277c5e6f-95bd-80ef-916a-f63f0b7f1a70" class="">Risk engine</h1></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8018-af3a-c0f33421fb0a" class="bulleted-list"><li style="list-style-type:disc">Normalize each signal to 0–100 (min-max or robust z).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8083-b098-c07739c232d6" class="bulleted-list"><li style="list-style-type:disc">Weighted score (example weights):<br/>Vol 15, Liquidity 15, Leverage 15, Liquidations 15, Flow/Breadth 15, Sentiment 15, Search 5, On-chain 5.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8065-8464-f5bf3c2c45b2" class="bulleted-list"><li style="list-style-type:disc"><strong>Market Risk Index (MRI)</strong> bands:<div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-803f-9671-cc3e3ec8f85e" class="bulleted-list"><li style="list-style-type:circle">0–39: Stable</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80de-b567-daeacfd82904" class="bulleted-list"><li style="list-style-type:circle">40–59: Watch</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8026-894b-f51a8f06c4f3" class="bulleted-list"><li style="list-style-type:circle">60–74: <strong>Elevated</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80df-b973-e11d5731624b" class="bulleted-list"><li style="list-style-type:circle">75–100: <strong>Imminent Risk</strong></li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80ef-a66d-e2cda6bced99" class="bulleted-list"><li style="list-style-type:disc">Add <strong>Hysteresis</strong>: need 2 consecutive intervals above a band to upgrade; 3 below to downgrade (reduces noise).</li></ul></div><div style="display:contents" dir="auto"><h1 id="277c5e6f-95bd-802c-baa2-f20fa7d65bac" class="">Dashboard layout</h1></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-807b-9d43-da63fb2d6b75" class="bulleted-list"><li style="list-style-type:disc"><strong>Top bar</strong>: MRI gauge + 24h/7d trend sparkline, current band, last change.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8085-8e6d-f15c2bf9e420" class="bulleted-list"><li style="list-style-type:disc"><strong>Heatmap</strong>: Signals by venue (Binance/OKX/Bybit), by asset (BTC/ETH/EDC/majors).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80e3-a530-c1dfc0fe01e6" class="bulleted-list"><li style="list-style-type:disc"><strong>Panels</strong>:<div style="display:contents" dir="auto"><ol type="1" id="277c5e6f-95bd-806f-920f-e1316d9b09d7" class="numbered-list" start="1"><li>Volatility &amp; Liquidity (BB width, depth, imbalance)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="277c5e6f-95bd-8037-821f-dc564996c001" class="numbered-list" start="2"><li>Leverage &amp; Liquidations (funding, OI, liquidation map)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="277c5e6f-95bd-80e2-8327-c70ae8e997aa" class="numbered-list" start="3"><li>Flows &amp; Breadth (exchange netflows, % above MA)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="277c5e6f-95bd-80c1-bb73-c2d5da2d23c1" class="numbered-list" start="4"><li>Sentiment &amp; Search (tone, whiplash, GT)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="277c5e6f-95bd-80cb-b520-cfe3062dbf79" class="numbered-list" start="5"><li>On-chain (if applicable)</li></ol></div></li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-800c-ba3e-e6551e189881" class="bulleted-list"><li style="list-style-type:disc"><strong>Event tape</strong>: notable spikes/crosses with timestamps (“Funding z&gt;2.5”, “Depth bottom decile”, etc.).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80e5-aaee-d3cb45092615" class="bulleted-list"><li style="list-style-type:disc"><strong>What-if</strong>: MRI components with weights (sliders) to test sensitivity.</li></ul></div><div style="display:contents" dir="auto"><h1 id="277c5e6f-95bd-80ab-9406-c6085d21a697" class="">Alerts</h1></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80a8-984a-eee76ccb1abc" class="bulleted-list"><li style="list-style-type:disc">Telegram/Slack: when MRI crosses <strong>60</strong> (Elevated) or <strong>75</strong> (Imminent), or any single signal breaches <strong>99th</strong> percentile.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8017-9927-f9e2a560f939" class="bulleted-list"><li style="list-style-type:disc">Daily 09:00 ICT digest with key diffs vs. yesterday.</li></ul></div><div style="display:contents" dir="auto"><h1 id="277c5e6f-95bd-80fe-93e5-d11502035ccc" class="">Data &amp; stack (pragmatic)</h1></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8049-973a-d916734fb0c7" class="bulleted-list"><li style="list-style-type:disc"><strong>Market/derivatives</strong>: CCXT (spot), exchange APIs for depth/OI/funding; Kaiko/CoinGlass/Laevitas if you have subs.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-804c-8f11-ed9df5b3cea6" class="bulleted-list"><li style="list-style-type:disc"><strong>News/Social</strong>: NewsAPI/Twitter/X API or Firehose alternative; run text through VADER/FinBERT.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-805b-a914-ee5a1ba8a06e" class="bulleted-list"><li style="list-style-type:disc"><strong>Search</strong>: pytrends (Google Trends).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8053-aa76-fb7a1d36c9ce" class="bulleted-list"><li style="list-style-type:disc"><strong>On-chain</strong>: Glassnode/Nansen/Dune (or node + ETL if you prefer).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8056-ad07-d70f8d7221ee" class="bulleted-list"><li style="list-style-type:disc">Backend: Python (pandas, numpy), tasks via Airflow/Prefect;<br/>Store: Postgres/BigQuery;<br/>Frontend: Streamlit/Plotly Dash/Grafana for speed;<br/>Alerts: Bot to Telegram/Slack.</li></ul></div><div style="display:contents" dir="auto"><h1 id="277c5e6f-95bd-806f-8781-c836376c56a7" class="">Example formulas (for Long)</h1></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80f0-9f01-c385bbcc9521" class="bulleted-list"><li style="list-style-type:disc"><strong>Vol-shock</strong> = (RealizedVol7d / RealizedVol30d).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-803d-a3e3-f7168f82572c" class="bulleted-list"><li style="list-style-type:disc"><strong>Depth ratio</strong> = (Depth±1%) / MktCap.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8060-b8dd-fccc6bdb65a0" class="bulleted-list"><li style="list-style-type:disc"><strong>Leverage index</strong> = z(funding) + z(OI/MktCap).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80c6-be61-e525672e2fc8" class="bulleted-list"><li style="list-style-type:disc"><strong>Tone whiplash</strong> = |Tone_1h − Tone_24h|.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80d9-aa0a-c1099a7eeea5" class="bulleted-list"><li style="list-style-type:disc"><strong>MRI</strong> = Σ(weight_i × normalized_signal_i).</li></ul></div><div style="display:contents" dir="auto"><h1 id="277c5e6f-95bd-80d0-9619-c0d17f519834" class="">Privacy &amp; abuse guardrails</h1></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80dd-ae1f-d86016ac02a6" class="bulleted-list"><li style="list-style-type:disc">Log sources &amp; transforms; show “confidence” next to each signal.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8010-82be-f0fa5c07d73f" class="bulleted-list"><li style="list-style-type:disc">Rate-limit alerts to avoid spam; add manual override/snooze.</li></ul></div><div style="display:contents" dir="auto"><hr id="277c5e6f-95bd-806d-b3ea-dab64679a296"/></div><div style="display:contents" dir="auto"><h3 id="277c5e6f-95bd-8027-bbdd-f7a175724665" class="">Brief for the team</h3></div><div style="display:contents" dir="auto"><blockquote id="277c5e6f-95bd-80d3-97f3-cc95f0abcdcf" class="">Task: Build an Emotional Stability → Market Risk dashboard to warn of drawdowns.<div style="display:contents" dir="auto"><p id="277c5e6f-95bd-804f-85b1-fc3699f02249" class=""><strong>Inputs:</strong> price/vol, order-book depth &amp; imbalance, funding &amp; OI, liquidation levels, exchange netflows &amp; market breadth, news/social sentiment, Google Trends, optional on-chain (SOPR, exchange flows).</p></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-80e2-8bfa-eed70ce259e0" class=""><strong>Output:</strong> A 0–100 <strong>Market Risk Index</strong> with bands (Stable/Watch/Elevated/Imminent), per-signal heatmap, and alerts (MRI≥60/75; 99th-percentile spikes).</p></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-8063-ba6d-c5a210181936" class=""><strong>Methods:</strong> Normalize each signal, weighted sum (Vol 15, Liquidity 15, Leverage 15, Liquidations 15, Flow/Breadth 15, Sentiment 15, Search 5, On-chain 5). Add hysteresis on band changes.</p></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-8024-9141-e1b73e36934e" class=""><strong>Stack:</strong> Python + Postgres/BigQuery; Streamlit/Plotly/Grafana UI; Telegram/Slack alerts.</p></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-80c3-9b95-e28de5a199e5" class=""><strong>Deliverables:</strong> (1) Live dashboard, (2) JSON/CSV feed of MRI and components, (3) alert bot, (4) README with formulas and data sources.</p></div></blockquote></div><div style="display:contents" dir="auto"><h1 id="277c5e6f-95bd-8031-8de7-f66ceb3c9c21" class="">1) Signal → Score (0–100)</h1></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-80d8-9c0e-f886961e7acc" class="">Normalize each raw metric into a <strong>tail-aware score</strong> so spikes matter more than drift.</p></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-8052-8875-c7851d34a772" class=""><strong>Robust z-score (winsorized):</strong></p></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80c9-a739-de20e29327dc" class="bulleted-list"><li style="list-style-type:disc">Compute rolling median <code>m_t</code> and MAD <code>mad_t</code> over lookback L (e.g., 180d).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80e5-b351-cf61e1e1e965" class="bulleted-list"><li style="list-style-type:disc"><code>rz_t = (x_t - m_t) / (1.4826 * mad_t)</code> clipped to [-5, +5].</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80dc-b5e6-fc889d21544e" class="bulleted-list"><li style="list-style-type:disc">Convert to 0–100 risk:<div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80d8-9d26-fd264b1f4029" class="bulleted-list"><li style="list-style-type:circle">If higher = riskier: <code>s_t = 50 + 10*rz_t</code> → clamp [0,100].</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8069-8c39-c9188c7a3c6b" class="bulleted-list"><li style="list-style-type:circle">If lower = riskier (e.g., depth): <code>s_t = 50 - 10*rz_t</code>.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-801e-8c0e-e6c19b1a1547" class="bulleted-list"><li style="list-style-type:disc">Apply <strong>EWMA smoothing</strong>: <code>s*_t = α*s_t + (1-α)*s*_{t-1}</code> with α=0.3.</li></ul></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-8021-9413-cf0b0fc5c36b" class=""><strong>Tail boost:</strong> if <code>|rz_t| &gt; 2.5</code>, add +5 (clamped), if &gt;3.5 add +10.</p></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-80c4-b2f6-d18aa5065f34" class="">This turns <strong>rare events</strong> into clear warnings.</p></div><div style="display:contents" dir="auto"><h1 id="277c5e6f-95bd-8009-871d-c6ce06e6bb2c" class="">2) Baseline Weights (start simple)</h1></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="277c5e6f-95bd-801e-855f-f64ff56ebe51" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">Volatility 15
Liquidity 15
Leverage 15
Liquidations 15
Flows/Breadth 15
Sentiment 15
Search 5
On-chain 5
[Optional add-ons: Options 5, Stablecoin Health 5]  // if/when you ingest
</code></pre></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-80ea-8ae2-cffabccf0b6d" class=""><strong>Market Risk Index (MRI):</strong></p></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-8032-a5b0-e7703f1c448a" class=""><code>MRI_t = Σ (w_i * s*_i,t) / Σ w_i</code>  → 0–100.</p></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-8041-a35f-ca1e1aeaea64" class=""><strong>Bands + Hysteresis:</strong></p></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8048-8a39-cd29e3dfe523" class="bulleted-list"><li style="list-style-type:disc">Stable &lt;40, Watch 40–59, <strong>Elevated 60–74</strong>, <strong>Imminent ≥75</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80b8-8e99-cf861d6571f0" class="bulleted-list"><li style="list-style-type:disc">Upgrade if 2 consecutive intervals breach; downgrade if 3 below (reduces whipsaw).</li></ul></div><div style="display:contents" dir="auto"><h1 id="277c5e6f-95bd-80aa-822c-e516f4ec8de3" class="">3) Ground Truth (labels)</h1></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-8094-8838-dbf991f448db" class="">Create objective “risk event” labels for backtesting.</p></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8068-b7fd-c456d6383eff" class="bulleted-list"><li style="list-style-type:disc"><strong>Drawdown label:</strong> <code>DD_k = 1</code> if max peak-to-trough in next <code>k</code> days ≤ −10% (test <code>k∈{3,5,7}</code> and −8/−12% too).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80b2-a819-daa6ac040af3" class="bulleted-list"><li style="list-style-type:disc"><strong>Vol-shock label:</strong> realized vol (next 3d) in top 10% of 1y history.<br/>Use drawdown as primary; vol-shock for sensitivity.</li></ul></div><div style="display:contents" dir="auto"><h1 id="277c5e6f-95bd-8062-b590-fbe44a84d6cd" class="">4) Backtest Framework</h1></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-8098-8ddb-cf87f8dcae15" class=""><strong>Split:</strong> rolling time windows to avoid look-ahead.</p></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8000-b81f-f65621d102d9" class="bulleted-list"><li style="list-style-type:disc">Train: months 1–6, Validate: month 7, Test: month 8; roll forward (walk-forward).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8044-8775-ddc8946e6c71" class="bulleted-list"><li style="list-style-type:disc">Or 70/15/15 chronological.</li></ul></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-802a-9f94-d3d1b16b6a65" class=""><strong>Metrics:</strong></p></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80da-89f2-cf1a929a983a" class="bulleted-list"><li style="list-style-type:disc"><strong>AUROC</strong>, <strong>AUPRC</strong> (imbalanced events), <strong>Recall@fixed False Alarm Rate</strong> (e.g., &lt;=1 alert/week), <strong>Lead time</strong> (median hours between first Imminent alert and event).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8076-abb5-cb66cf04790a" class="bulleted-list"><li style="list-style-type:disc"><strong>Economic</strong>: cost-weighted loss: <code>Cost = 8*FN + 1*FP</code> (missing a crash hurts more).</li></ul></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-80ae-bcd6-c022649ae146" class=""><strong>Calibration:</strong></p></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80ac-b45a-ce4c9be14594" class="bulleted-list"><li style="list-style-type:disc">Optimize α (EWMA), L (lookback), thresholds (60/75), and weights <code>w_i</code> to <strong>maximize cost-adjusted F1</strong> or <strong>minimize cost</strong> on validation.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8019-9f0b-d0ff8d6de31f" class="bulleted-list"><li style="list-style-type:disc">Keep a <strong>parsimonious</strong> set (avoid overfitting): cap any weight ≤25 and ≥5.</li></ul></div><div style="display:contents" dir="auto"><h1 id="277c5e6f-95bd-802d-9437-caab26541c5b" class="">5) Auto-Tuning (two layers)</h1></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-80c8-9b81-fc7486cd6930" class=""><strong>(A) Heuristic grid search:</strong></p></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80c7-b37b-f8820eeeabf1" class="bulleted-list"><li style="list-style-type:disc">For each regime (low/high vol), test:<div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80d3-953f-d031f70be010" class="bulleted-list"><li style="list-style-type:circle">α ∈ {0.2, 0.3, 0.5}</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8023-bb17-d6f4566c8168" class="bulleted-list"><li style="list-style-type:circle">L ∈ {120, 180, 360 days}</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80d1-88c3-eaca307a8bea" class="bulleted-list"><li style="list-style-type:circle">thresholds: Elevated ∈ {55,60,65}, Imminent ∈ {70,75,80}</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-801d-a5b8-d825b3b27587" class="bulleted-list"><li style="list-style-type:circle">reweight top 3 predictive signals by +5 each (others −2)</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80f3-b4e4-d10f03faf410" class="bulleted-list"><li style="list-style-type:disc">Pick combo with best <strong>cost-min</strong> + <strong>lead time</strong>.</li></ul></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-808c-9cb9-e6ad004fff79" class=""><strong>(B) Meta-model (optional, simple):</strong></p></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-802a-9aac-fe2639a6fbda" class="bulleted-list"><li style="list-style-type:disc">Logistic regression (lasso) on the <strong>individual scores</strong> <code>s*_i,t</code> to predict label (next 3–5d drawdown).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8064-af5a-f99bad0c7960" class="bulleted-list"><li style="list-style-type:disc">Convert predicted prob to MRI via monotonic map (e.g., <code>MRI = 100*prob</code>).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-806e-868d-ed63261b6315" class="bulleted-list"><li style="list-style-type:disc">Keep interpretability: inspect coefficients → these become <strong>data-driven weights</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8064-a147-c1ded175078b" class="bulleted-list"><li style="list-style-type:disc">For non-linear lift later: LightGBM with <strong>monotonic constraints</strong> (risk ↑ with worse signals).</li></ul></div><div style="display:contents" dir="auto"><h1 id="277c5e6f-95bd-8052-8d71-f738ed4de1ca" class="">6) Regime Detection (stability booster)</h1></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-80c1-8150-e4b22bc4d44e" class="">Market behaves differently in calm vs. wild regimes.</p></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8067-a1b2-fff2c4dcf0e5" class="bulleted-list"><li style="list-style-type:disc"><strong>Regime score:</strong> <code>Regime = z(RealizedVol30d) + z(BB width 20d)</code></li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-802f-9c93-c34bdcc69650" class="bulleted-list"><li style="list-style-type:disc">If Regime &gt; 1.5 → <strong>High-vol regime</strong> → increase weights on <strong>Liquidity, Liquidations, Leverage</strong> by +3 each; decrease <strong>Search</strong> by −2.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80bb-9c7c-c7e28df70f6c" class="bulleted-list"><li style="list-style-type:disc">If Regime &lt; 0 → <strong>Calm regime</strong> → up-weight <strong>Sentiment &amp; Search</strong> (early retail anxiety) by +3.</li></ul></div><div style="display:contents" dir="auto"><h1 id="277c5e6f-95bd-80e1-b4b7-e655ec2de0cd" class="">7) Feature sanity (what you asked “what’s missing”)</h1></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-8044-9dba-fdb06a7906eb" class="">Add when ready and allow the tuner to reweight:</p></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8013-b107-fe34df3c85aa" class="bulleted-list"><li style="list-style-type:disc"><strong>Options skew / IV rank / gamma flip</strong> (if data available).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8021-9e18-d05171aa4cae" class="bulleted-list"><li style="list-style-type:disc"><strong>Stablecoin health</strong> (USDT/USDC peg drift, supply Δ).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8090-b6b3-cb038f174bed" class="bulleted-list"><li style="list-style-type:disc"><strong>Whale CEX deposits</strong> (90th pct spikes).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8080-8c91-e2f28d5ca3f1" class="bulleted-list"><li style="list-style-type:disc"><strong>Cross-venue spreads</strong> (spot–perp dislocations).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8037-b435-fe4b2192fc4f" class="bulleted-list"><li style="list-style-type:disc"><strong>Macro link</strong> (DXY↑ &amp; Nasdaq↓ correlation spike).</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8035-a66f-c2765c0b933f" class="bulleted-list"><li style="list-style-type:disc"><strong>Regulatory shock score</strong> (NER + keyword rules; cap a hard floor MRI≥65 for X hours).</li></ul></div><div style="display:contents" dir="auto"><h1 id="277c5e6f-95bd-8076-be73-d38ef1f4ecc0" class="">8) Alert logic (precision over spam)</h1></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8051-a813-c8aed8d63f78" class="bulleted-list"><li style="list-style-type:disc"><strong>Pre-alerts (“Watch”)</strong>: MRI≥60 sustained 2 ticks <strong>and</strong> at least 2 of {Liquidity, Leverage, Liquidations, Sentiment} ≥70.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-802d-bc54-de8ebfd275d9" class="bulleted-list"><li style="list-style-type:disc"><strong>Imminent</strong>: MRI≥75 <strong>or</strong> (any of Liquidity/Leverage/Liquidations ≥85 and rising) <strong>and</strong> price &lt; 5×1h EMA.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-809f-918b-fe16fe6d4ed6" class="bulleted-list"><li style="list-style-type:disc"><strong>Cooldown:</strong> minimum 3h between identical alert types; merge duplicates.</li></ul></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-80ab-9cb0-d6505d221449" class=""><strong>Telegram copy (clear &amp; actionable):</strong></p></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80c8-b319-c95fde881e72" class="bulleted-list"><li style="list-style-type:disc"><em>ELEVATED RISK (MRI 66 ↑)</em> – Liquidity thin (depth p10), funding crowded longs (z=2.3). Tighten risk, reduce leverage.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8041-a7e8-de0015ba8bdf" class="bulleted-list"><li style="list-style-type:disc"><em>IMMINENT RISK (MRI 78)</em> – Liquidation overhang within −2.8%, sentiment whiplash high. Consider de-risking / hedge.</li></ul></div><div style="display:contents" dir="auto"><h1 id="277c5e6f-95bd-8009-9903-ffe22e23fadf" class="">9) Drift &amp; health checks</h1></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80e4-a9ee-c2c240b26296" class="bulleted-list"><li style="list-style-type:disc">Weekly <strong>PSI</strong> (population stability index) on each signal to catch distribution drift.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8091-a8e9-f4663f120d35" class="bulleted-list"><li style="list-style-type:disc">Refit medians/MAD monthly; lock thresholds for a month to avoid jitter.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-804e-a7fa-eae1f567c6ab" class="bulleted-list"><li style="list-style-type:disc">Backtest refresh weekly; human-in-the-loop approves weight shifts.</li></ul></div><div style="display:contents" dir="auto"><h1 id="277c5e6f-95bd-808c-9b0b-f539ac95e5ad" class="">10) Config schema (portable &amp; auditable)</h1></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="277c5e6f-95bd-8016-a1b6-d1b103f18c8f" class="code code-wrap"><code class="language-JSON" style="white-space:pre-wrap;word-break:break-all">{
  &quot;lookbacks&quot;: {&quot;median_days&quot;: 180, &quot;ewma_alpha&quot;: 0.3},
  &quot;bands&quot;: {&quot;watch&quot;: 60, &quot;imminent&quot;: 75, &quot;upgrade_ticks&quot;: 2, &quot;downgrade_ticks&quot;: 3},
  &quot;weights&quot;: {
    &quot;volatility&quot;: 15, &quot;liquidity&quot;: 15, &quot;leverage&quot;: 15, &quot;liquidations&quot;: 15,
    &quot;flows_breadth&quot;: 15, &quot;sentiment&quot;: 15, &quot;search&quot;: 5, &quot;onchain&quot;: 5,
    &quot;options&quot;: 0, &quot;stablecoin_health&quot;: 0
  },
  &quot;tail_boost&quot;: {&quot;z25&quot;: 5, &quot;z35&quot;: 10},
  &quot;regime&quot;: {&quot;high_vol_threshold&quot;: 1.5, &quot;calm_threshold&quot;: 0.0,
    &quot;adjustments&quot;: {
      &quot;high_vol&quot;: {&quot;liquidity&quot;: 3, &quot;leverage&quot;: 3, &quot;liquidations&quot;: 3, &quot;search&quot;: -2},
      &quot;calm&quot;: {&quot;sentiment&quot;: 3, &quot;search&quot;: 3}
    }
  },
  &quot;alerts&quot;: {&quot;cooldown_minutes&quot;: 180, &quot;component_tripwire&quot;: 85}
}
</code></pre></div><div style="display:contents" dir="auto"><h1 id="277c5e6f-95bd-8069-9fb1-ce184df0f982" class="">11) Minimal backtest pseudocode (readable)</h1></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="277c5e6f-95bd-809e-8402-f78a83115f0c" class="code code-wrap"><code class="language-Python" style="white-space:pre-wrap;word-break:break-all"># signals_df: time index, columns like s_vol, s_liq, s_lev, s_liqdn, s_flow, s_sent, s_search, s_onchain
# price: close series; labels via future drawdown

# 1. robust z + 0-100 scaling + EWMA
for col in signals_df.columns:
    m = rolling_median(signals_df[col], L)
    mad = rolling_mad(signals_df[col], L)
    rz = (signals_df[col]-m)/(1.4826*mad)
    rz = rz.clip(-5,5)
    s = 50 + 10*rz * direction[col]   # direction +1/-1
    s = apply_tail_boost(s, rz)
    signals_df[col] = ewma(s, alpha=0.3).clip(0,100)

# 2. regime-adjusted weights
regime = z(realized_vol_30d) + z(bb_width_20d)
W = base_weights.copy()
W = adjust_by_regime(W, regime_t)

# 3. MRI
MRI = (signals_df @ W.values) / sum(W.values)

# 4. labels
label = future_drawdown(price, horizon_days=5, threshold=-0.10)  # 10% in 5d

# 5. evaluate thresholds / weights via grid search
best = None
for thr_watch in [55,60,65]:
    for thr_imm in [70,75,80]:
        metrics = evaluate(MRI, label, cost_fn, lead_time)
        best = keep_if_better(best, metrics)

# 6. (optional) logistic meta-model
X = signals_df.values
y = label.values
logit = fit_l1_logistic(X_train, y_train)
prob = logit.predict_proba(X_valid)[:,1]
MRI2 = 100*prob
</code></pre></div><div style="display:contents" dir="auto"><h1 id="277c5e6f-95bd-8014-882e-e18611385c32" class="">12) “What good looks like” (targets)</h1></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-8093-a246-de3d73267b24" class="bulleted-list"><li style="list-style-type:disc"><strong>Recall (Imminent)</strong> ≥ 0.65 at ≤ 3 false Imminent alerts/week.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-80f9-9853-d84c0ef0b636" class="bulleted-list"><li style="list-style-type:disc"><strong>Median lead time</strong> ≥ 6–12 hours before −8%/−10% events.</li></ul></div><div style="display:contents" dir="auto"><ul id="277c5e6f-95bd-807c-9aed-d0ba6172863c" class="bulleted-list"><li style="list-style-type:disc"><strong>Cost reduction</strong> vs. naive (price-only) alert by ≥ 30%.</li></ul></div><div style="display:contents" dir="auto"><hr id="277c5e6f-95bd-807c-a537-d134b6e1a437"/></div><div style="display:contents" dir="auto"><p id="277c5e6f-95bd-80d3-afa0-ec2ff26a6ecd" class="">
</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
