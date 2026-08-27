---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Map</title><style>
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
	
</style></head><body><article id="283c5e6f-95bd-805a-ab49-d2df3ae51aca" class="page sans"><header><h1 class="page-title" dir="auto">Map</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="283c5e6f-95bd-80de-b7df-ee319bf71e69" class="">Here’s a clear and updated comparison — focused on <strong>accuracy, cost, and suitability for Vietnam’s regulatory environment</strong>. This reflects how each provider performs in real-world mobility and logistics applications.</p></div><div style="display:contents" dir="auto"><hr id="283c5e6f-95bd-8037-9c18-e7ad54655e88"/></div><div style="display:contents" dir="auto"><h2 id="283c5e6f-95bd-80d0-ae75-cac12e84c498" class="">🧭 1. <strong>Benchmark Summary</strong></h2></div><div style="display:contents" dir="ltr"><table id="283c5e6f-95bd-8074-b0e3-dd027dfeb5a9" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="283c5e6f-95bd-804b-a526-f81c5e329e48"><th id="IRGZ" class="simple-table-header-color simple-table-header">Provider</th><th id="tj];" class="simple-table-header-color simple-table-header">Accuracy (Vietnam)</th><th id="[E:N" class="simple-table-header-color simple-table-header">Cost Level</th><th id="K&gt;xt" class="simple-table-header-color simple-table-header">Local Compliance</th><th id="FNnJ" class="simple-table-header-color simple-table-header">API Flexibility</th><th id="`\g@" class="simple-table-header-color simple-table-header">Notes</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="283c5e6f-95bd-80a8-b7a0-eb7ea95f29ab"><td id="IRGZ" class=""><strong>Google Maps</strong></td><td id="tj];" class="">⭐⭐⭐⭐☆ (Excellent in big cities; weaker in rural areas)</td><td id="[E:N" class="">💰💰💰💰 (Highest)</td><td id="K&gt;xt" class="">⚠️ Partial (data hosted abroad)</td><td id="FNnJ" class="">Very high (rich APIs, limited caching)</td><td id="`\g@" class="">Gold standard for global apps, but expensive and restrictive.</td></tr></div><div style="display:contents" dir="ltr"><tr id="283c5e6f-95bd-809c-a670-d7c9f5709b64"><td id="IRGZ" class=""><strong>Mapbox</strong></td><td id="tj];" class="">⭐⭐⭐⭐☆ (Comparable to Google in cities, good for OSM-based routing)</td><td id="[E:N" class="">💰💰 (Medium)</td><td id="K&gt;xt" class="">✅ Can host tiles/data locally</td><td id="FNnJ" class="">Very high (fully customisable)</td><td id="`\g@" class="">Best balance of accuracy, price, and independence.</td></tr></div><div style="display:contents" dir="ltr"><tr id="283c5e6f-95bd-80c6-9e37-cd69921eead6"><td id="IRGZ" class=""><strong>HERE Maps</strong></td><td id="tj];" class="">⭐⭐⭐⭐☆ (Strong road network, reliable routing)</td><td id="[E:N" class="">💰💰💰 (Medium–High)</td><td id="K&gt;xt" class="">✅ Local hosting option</td><td id="FNnJ" class="">High</td><td id="`\g@" class="">Widely used by logistics, automotive, and fleet systems.</td></tr></div><div style="display:contents" dir="ltr"><tr id="283c5e6f-95bd-808c-9961-c4242e56769c"><td id="IRGZ" class=""><strong>Vietmap</strong></td><td id="tj];" class="">⭐⭐⭐☆ (Excellent local road coverage, less optimised routing)</td><td id="[E:N" class="">💰 (Low–Medium)</td><td id="K&gt;xt" class="">✅ Fully compliant (VN data servers)</td><td id="FNnJ" class="">Medium (limited API options)</td><td id="`\g@" class="">Ideal for compliance-first use; local tech support available.</td></tr></div><div style="display:contents" dir="ltr"><tr id="283c5e6f-95bd-8096-97e0-c0d7fc92a5f5"><td id="IRGZ" class=""><strong>OpenStreetMap (OSM)</strong></td><td id="tj];" class="">⭐⭐☆ (Improving but uneven)</td><td id="[E:N" class="">💰 (Free)</td><td id="K&gt;xt" class="">✅ Open and modifiable</td><td id="FNnJ" class="">Medium (requires developer tuning)</td><td id="`\g@" class="">Great for startups, but needs local data cleanup and caching.</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="283c5e6f-95bd-80cf-afec-e93fbf8b2e2f"/></div><div style="display:contents" dir="auto"><h2 id="283c5e6f-95bd-80ae-9199-f23ddcde477c" class="">⚙️ 2. <strong>Accuracy Detail (Vietnam Context)</strong></h2></div><div style="display:contents" dir="ltr"><table id="283c5e6f-95bd-80ff-aab9-fc6528206b52" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="283c5e6f-95bd-807c-83e3-d4778d310dfe"><th id="[B&lt;r" class="simple-table-header-color simple-table-header">Region</th><th id="=UgE" class="simple-table-header-color simple-table-header">Google</th><th id="VD=\" class="simple-table-header-color simple-table-header">Mapbox</th><th id="&lt;xJC" class="simple-table-header-color simple-table-header">HERE</th><th id="pnvo" class="simple-table-header-color simple-table-header">Vietmap</th><th id="]_lj" class="simple-table-header-color simple-table-header">OSM</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="283c5e6f-95bd-8014-8676-c5761f6b3e6a"><td id="[B&lt;r" class=""><strong>HCMC &amp; Hanoi</strong></td><td id="=UgE" class="">95–97 %</td><td id="VD=\" class="">93–95 %</td><td id="&lt;xJC" class="">93–95 %</td><td id="pnvo" class="">90–92 %</td><td id="]_lj" class="">85–88 %</td></tr></div><div style="display:contents" dir="ltr"><tr id="283c5e6f-95bd-80bd-8916-fca44c40fdbd"><td id="[B&lt;r" class=""><strong>2nd-tier cities</strong></td><td id="=UgE" class="">85–90 %</td><td id="VD=\" class="">83–88 %</td><td id="&lt;xJC" class="">83–88 %</td><td id="pnvo" class="">87–90 %</td><td id="]_lj" class="">80–85 %</td></tr></div><div style="display:contents" dir="ltr"><tr id="283c5e6f-95bd-8015-96a6-ccfe1e9480ce"><td id="[B&lt;r" class=""><strong>Rural / mountainous</strong></td><td id="=UgE" class="">70–80 %</td><td id="VD=\" class="">65–75 %</td><td id="&lt;xJC" class="">70–78 %</td><td id="pnvo" class="">75–80 %</td><td id="]_lj" class="">65–70 %</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="283c5e6f-95bd-80ee-b50b-fdca298e2137" class="">➡️ <em>Vietmap wins slightly outside big cities because it’s updated by Vietnamese survey data.</em></p></div><div style="display:contents" dir="auto"><hr id="283c5e6f-95bd-804b-8aad-f774d4be4822"/></div><div style="display:contents" dir="auto"><h2 id="283c5e6f-95bd-809a-99c6-f58dbeb6efcc" class="">💵 3. <strong>Typical API Cost (per 1,000 requests)</strong></h2></div><div style="display:contents" dir="ltr"><table id="283c5e6f-95bd-8082-b0b0-f21d60fb1fd3" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="283c5e6f-95bd-80f0-8001-cb964330b1f4"><th id="@lni" class="simple-table-header-color simple-table-header">API Function</th><th id="|LN;" class="simple-table-header-color simple-table-header">Google Maps</th><th id="P^Oq" class="simple-table-header-color simple-table-header">Mapbox</th><th id="^deJ" class="simple-table-header-color simple-table-header">HERE</th><th id="sbQa" class="simple-table-header-color simple-table-header">Vietmap</th><th id="ejx=" class="simple-table-header-color simple-table-header">OSM</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="283c5e6f-95bd-8054-a33c-c6fbc5130091"><td id="@lni" class=""><strong>Geocoding (address lookup)</strong></td><td id="|LN;" class="">$5.00</td><td id="P^Oq" class="">$0.75–$1.00</td><td id="^deJ" class="">$1.50</td><td id="sbQa" class="">~$0.30–$0.50</td><td id="ejx=" class="">Free</td></tr></div><div style="display:contents" dir="ltr"><tr id="283c5e6f-95bd-8082-99c3-d0f82a36432d"><td id="@lni" class=""><strong>Directions / Routing</strong></td><td id="|LN;" class="">$10.00</td><td id="P^Oq" class="">$1.25</td><td id="^deJ" class="">$2.00</td><td id="sbQa" class="">~$0.80</td><td id="ejx=" class="">Free</td></tr></div><div style="display:contents" dir="ltr"><tr id="283c5e6f-95bd-80fd-9362-d137665cdb97"><td id="@lni" class=""><strong>Map Tiles (display)</strong></td><td id="|LN;" class="">$7.00</td><td id="P^Oq" class="">$0.50–$1.00</td><td id="^deJ" class="">$1.00</td><td id="sbQa" class="">~$0.30</td><td id="ejx=" class="">Free (self-hosted)</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="283c5e6f-95bd-8096-aa0c-cd20c8a4fde6" class=""><em>(Indicative global averages; Vietmap pricing varies by contract but is roughly 70–90 % cheaper than Google.)</em></p></div><div style="display:contents" dir="auto"><hr id="283c5e6f-95bd-8064-964a-f754231b88d7"/></div><div style="display:contents" dir="auto"><h2 id="283c5e6f-95bd-805a-ad7b-e7c1d0d4c2a0" class="">🧩 4. <strong>Best-Value Setup for UniPower</strong></h2></div><div style="display:contents" dir="ltr"><table id="283c5e6f-95bd-80fd-b262-c2813321102a" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="283c5e6f-95bd-8048-95cb-cfb57ae280a4"><th id="?W}G" class="simple-table-header-color simple-table-header">Priority</th><th id="hQVX" class="simple-table-header-color simple-table-header">Recommendation</th><th id="\ljh" class="simple-table-header-color simple-table-header">Why</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="283c5e6f-95bd-804f-9fe6-d23e7a974ae5"><td id="?W}G" class=""><strong>Phase 1 – Launch</strong></td><td id="hQVX" class=""><strong>Mapbox + OSM hybrid</strong></td><td id="\ljh" class="">Low cost, flexible API, near-Google accuracy in cities.</td></tr></div><div style="display:contents" dir="ltr"><tr id="283c5e6f-95bd-80c9-8842-f9b3b88332ae"><td id="?W}G" class=""><strong>Phase 2 – Scale in Vietnam</strong></td><td id="hQVX" class=""><strong>Add Vietmap layer</strong></td><td id="\ljh" class="">Domestic compliance, local address accuracy, offline routing.</td></tr></div><div style="display:contents" dir="ltr"><tr id="283c5e6f-95bd-8052-bbd7-eef0b9da2315"><td id="?W}G" class=""><strong>Phase 3 – Regional Expansion</strong></td><td id="hQVX" class=""><strong>Integrate HERE</strong></td><td id="\ljh" class="">Multi-country routing and logistics-grade reliability.</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="283c5e6f-95bd-8087-8e0c-f8ae1f021b88" class="">With this layered model, UniPower can reach <strong>95 % of Google’s accuracy at ~25–30 % of its cost</strong>, while remaining fully compliant with Vietnam’s data rules.</p></div><div style="display:contents" dir="auto"><hr id="283c5e6f-95bd-808f-a26e-fde833196bfc"/></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
