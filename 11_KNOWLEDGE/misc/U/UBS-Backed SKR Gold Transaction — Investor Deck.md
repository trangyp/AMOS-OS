---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>UBS-Backed SKR Gold Transaction — Investor Deck</title><style>
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
	
</style></head><body><article id="24ac5e6f-95bd-8091-8b0d-f2f6807d0fa4" class="page sans"><header><h1 class="page-title" dir="auto"><strong>UBS-Backed SKR Gold Transaction — Investor Deck</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-80e1-8fe0-c62b0ec6edd0" class=""><strong>1) Deal Overview</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8041-9fd4-e19966646a4d" class="bulleted-list"><li style="list-style-type:disc"><strong>Asset</strong>: 500,000 kg (500 metric tonnes) of LBMA Good Delivery gold</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-806e-9992-f271860a830b" class="bulleted-list"><li style="list-style-type:disc"><strong>Custody</strong>: UBS (authenticated SKR; bar list, assays, chain of custody)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8035-84da-e7dec47ee550" class="bulleted-list"><li style="list-style-type:disc"><strong>Structure</strong>: Outright sale, collateralized monetization, or hybrid (tranche-based)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8024-b008-ec003ad8884a" class="bulleted-list"><li style="list-style-type:disc"><strong>Venues</strong>: Switzerland (primary), with options in London, Singapore, Dubai</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80c2-8aee-e988a7ab652d" class="bulleted-list"><li style="list-style-type:disc"><strong>Eligible Buyers</strong>: Central banks, SWFs, LBMA bullion banks, regulated institutions</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8085-a685-f21440f1adde" class="bulleted-list"><li style="list-style-type:disc"><strong>Settlement</strong>: Bank-to-bank (MT103/202) or instrumented (MT799/760 + escrow)</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-808f-b319-d82b2959a4b3"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-803d-9985-ffe675bc4b04" class=""><strong>2) Investment Thesis</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-803f-a3ce-e2e447e1c517" class="bulleted-list"><li style="list-style-type:disc"><strong>Sovereign-Scale Access</strong>: 500t is central-bank grade; rare liquidity event.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8095-aa22-c73401058e34" class="bulleted-list"><li style="list-style-type:disc"><strong>Risk-Controlled Execution</strong>: In-vault title transfer; tranche-based settlement; Tier-1 escrow.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8086-b09f-f2cdfd9f8a15" class="bulleted-list"><li style="list-style-type:disc"><strong>Macro Hedge</strong>: Structural allocation amid currency debasement, geopolitical risk, and rate cycles.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8014-bdea-e11c7f445551" class="bulleted-list"><li style="list-style-type:disc"><strong>Optional Impact Mandate</strong>: Proceeds can be directed to trust structures funding <strong>Unified Biological Intelligence™</strong> and <strong>NeuroSyncAI™</strong> infrastructure (health, education, governance).</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-801f-be09-e698c62f8dd1"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-805d-a845-df60c0a66677" class=""><strong>3) End-to-End Deal Flow</strong></h2></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="24ac5e6f-95bd-8024-b69e-dc0bb11739a4" class="code code-wrap"><code class="language-Mermaid" style="white-space:pre-wrap;word-break:break-all">flowchart TB
A[NDA / NCNDA Signed] --&gt; B[Counterparty Screening&lt;br/&gt;KYC / AML &amp; Mandate Check]
B --&gt; C[Bank-to-Bank POP&lt;br/&gt;UBS Confirmation]
C --&gt; D[On-Site Inspection or Assay&lt;br/&gt; Optional, Pre-1st Tranche]
D --&gt; E[SPA / IMFPA Executed]
E --&gt; F[POF Issuance&lt;br/&gt;MT799, Comfort Letter, Escrow Funded]
F --&gt; G[Tranche Title Transfer&lt;br/&gt;In-Vault Reallocation]
G --&gt; H[MT103 Settlement&lt;br/&gt;Funds Release]
H --&gt; I[Post-Settlement Logistics&lt;br/&gt;Optional Loco Move]
I --&gt; J[Rolling Tranches&lt;br/&gt;Completion &amp; Reconciliation]</code></pre></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-801c-a21b-c9d81ad041e4"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-80c7-b7af-e4b78c8ce2f7" class=""><strong>4) Banking Message Sequence (Instruments + Escrow)</strong></h2></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="24ac5e6f-95bd-80db-a935-f62a4796c922" class="code code-wrap"><code class="language-Mermaid" style="white-space:pre-wrap;word-break:break-all">sequenceDiagram
    participant BuyerBank
    participant SellerBank(UBS)
    participant EscrowBank
    participant Assayer

    BuyerBank-&gt;&gt;SellerBank(UBS): MT799 (RWA / POF) or Escrow Confirmation
    SellerBank(UBS)--&gt;&gt;BuyerBank: POP Confirmation (Custodial / Bar List Redacted)
    BuyerBank-&gt;&gt;Assayer: (Optional) On-site Inspection Request
    Assayer--&gt;&gt;BuyerBank: Inspection/Assay Report
    BuyerBank-&gt;&gt;SellerBank(UBS): MT760 SBLC (if instrumented) or Escrow Prefund
    SellerBank(UBS)-&gt;&gt;EscrowBank: Tranche Title Transfer Instructions
    EscrowBank--&gt;&gt;SellerBank(UBS): Confirm Escrow Conditions Met
    SellerBank(UBS)-&gt;&gt;BuyerBank: Confirm Title Transfer (In-Vault)
    BuyerBank-&gt;&gt;SellerBank(UBS): MT103 (Funds Release)
    EscrowBank--&gt;&gt;Both: Dual Release Confirmation</code></pre></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-804c-8261-d0e67f8e995e"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8011-9550-f4667519b920" class=""><strong>5) Tranche Plan &amp; Timeline (Example)</strong></h2></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="24ac5e6f-95bd-8073-9147-c46c340cb1d8" class="code code-wrap"><code class="language-Mermaid" style="white-space:pre-wrap;word-break:break-all">gantt
    dateFormat  YYYY-MM-DD
    title Tranche Execution Timeline (Illustrative)
    section Compliance
    NDA &amp; Screening           :done,    t1, 2025-08-10, 3d
    Bank POP &amp; RWA            :active,  t2, 2025-08-13, 4d
    SPA &amp; IMFPA               :         t3, 2025-08-17, 3d
    section Tranche 1 (50t)
    Inspection/Assay (opt)    :         t4, 2025-08-20, 3d
    Title Transfer            :         t5, 2025-08-23, 1d
    MT103 Settlement          :         t6, 2025-08-24, 1d
    section Tranche 2 (50t)
    Title Transfer            :         t7, 2025-08-27, 1d
    MT103 Settlement          :         t8, 2025-08-28, 1d
    section Rolling Tranches
    Repeat Until Completion   :         t9, 2025-08-29, 30d</code></pre></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8047-894c-e5725c7ca1d8" class=""><strong>Notes:</strong> 25–50t per tranche is standard to minimize counterparty and market impact risk. Cadence can accelerate after first two tranches.</p></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-802a-8138-e17c9eb51e04"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-80e9-9f77-f64a404f24ef" class=""><strong>6) Commercial Terms Framework</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8067-b3ba-c858093cb894" class="bulleted-list"><li style="list-style-type:disc"><strong>Price Reference</strong>: LBMA spot/PM fix (trade day)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-805b-b4f1-cd48af7e806e" class="bulleted-list"><li style="list-style-type:disc"><strong>Spread</strong>: Standard market discount/premium, negotiated by tranche &amp; venue</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80eb-9848-e5389e6e6ac2" class="bulleted-list"><li style="list-style-type:disc"><strong>Delivery</strong>: Preferred <strong>in-vault title transfer</strong> at UBS; optional reallocation (London/Zurich/Singapore/Dubai)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8027-8d27-c03035603ffe" class="bulleted-list"><li style="list-style-type:disc"><strong>Settlement</strong>:<div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-808e-b960-cb3be3eaa631" class="bulleted-list"><li style="list-style-type:circle"><strong>Cash</strong>: MT103/202 post title confirmation; or</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80e7-8949-d7dd56597631" class="bulleted-list"><li style="list-style-type:circle"><strong>Instrumented</strong>: MT799 pre-advice → MT760 SBLC → drawdown; or</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-804d-ae9b-d8e5f68b9bde" class="bulleted-list"><li style="list-style-type:circle"><strong>Escrow</strong>: Tier-1 dual-release</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80bb-b7b3-c1a46722651e" class="bulleted-list"><li style="list-style-type:disc"><strong>Commissions</strong>: If applicable, locked via <strong>IMFPA</strong> appended to SPA</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80ec-b008-fdc1ae9c508a" class="bulleted-list"><li style="list-style-type:disc"><strong>Governing Law</strong>: Switzerland or England &amp; Wales; arbitration venue specified in SPA</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-806a-9cb1-fa415a5c7fe1"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8057-ae14-c711532c75da" class=""><strong>7) Compliance &amp; Risk Controls</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8013-9c5f-cade8a96163e" class="bulleted-list"><li style="list-style-type:disc"><strong>Custody Integrity</strong>: UBS vault; no movement pre-settlement</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-804e-b4ae-df7f3522fe63" class="bulleted-list"><li style="list-style-type:disc"><strong>Audits</strong>: Optional <strong>SGS/Bureau Veritas</strong> pre- or post-first tranche</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80d7-a535-ed291d92e5d5" class="bulleted-list"><li style="list-style-type:disc"><strong>AML/KYC</strong>: FATF-aligned; continuous sanctions screening (UN/EU/OFAC)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8084-9150-fdb5ba5afa7e" class="bulleted-list"><li style="list-style-type:disc"><strong>Escrow</strong>: Tier-1 neutral escrow with dual-release conditions</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-806a-b0c5-e04863328da1" class="bulleted-list"><li style="list-style-type:disc"><strong>Counterparty Proofs</strong>: Bank-issued POF; named officers for SWIFT; institutional onboarding readiness</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80a1-a4f9-cce977739e40" class="bulleted-list"><li style="list-style-type:disc"><strong>Dispute Framework</strong>: Force majeure and arbitration clauses embedded in SPA</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80d7-94e2-c4ea97216a6b"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-805a-8a74-e7789f8c072e" class=""><strong>8) Buyer Qualification (Minimum Requirements)</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80d8-ba5e-e88e1ded5d54" class="bulleted-list"><li style="list-style-type:disc"><strong>Entity Type</strong>: Central bank, SWF, LBMA bullion desk, or regulated institution</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-806d-a32f-d48148a17e87" class="bulleted-list"><li style="list-style-type:disc"><strong>POF</strong>: Bank comfort or verifiable capacity for tranche size</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80bf-94ed-c3085c2698ef" class="bulleted-list"><li style="list-style-type:disc"><strong>Process Acceptance</strong>: In-vault title transfer, tranche cadence, POP/RWA sequence</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-807d-925d-c81130b44c04" class="bulleted-list"><li style="list-style-type:disc"><strong>Compliance</strong>: Full corporate KYC/AML; approval authority for SPA/instruments</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80b0-ba01-e0d67d869d0b"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-80f3-8c4e-decd24e4f5f8" class=""><strong>9) Strategic Options</strong></h2></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-8042-aa22-c64e022ad6bf" class=""><strong>A) Outright Sale</strong></h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8044-a39d-f04e40a794cb" class="bulleted-list"><li style="list-style-type:disc">Fastest exit; maximizes certainty; simplest operationally.</li></ul></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-8069-8e88-eb2ce7314c51" class=""><strong>B) Collateral Monetization</strong></h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80a9-bbb3-c80e00c888ff" class="bulleted-list"><li style="list-style-type:disc">SBLC/BG against SKR; unlocks credit lines (1–3% LTV monthly typical, negotiable).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8017-a7dc-fac2a725daf6" class="bulleted-list"><li style="list-style-type:disc">Suitable for staged deployment into projects while retaining exposure.</li></ul></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-807d-835c-f38f5240c7b6" class=""><strong>C) Hybrid Program</strong></h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80d9-80aa-e08ef99929e7" class="bulleted-list"><li style="list-style-type:disc">Partial sale to seed trust + partial monetization to scale impact and maintain flexibility.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-800f-9932-dc40362d8e28"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8081-9780-f51abb674dfb" class=""><strong>10) Use-of-Proceeds (Impact Option for Aligned Buyers)</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8032-b161-ea4b507a2154" class="bulleted-list"><li style="list-style-type:disc"><strong>Unified Biological Intelligence™</strong>: Public health, education, justice reform modeled on measurable nervous-system regulation.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80bf-97f9-c999980a3864" class="bulleted-list"><li style="list-style-type:disc"><strong>NeuroSyncAI™</strong>: Live integrity interfaces for governance, finance, and critical infrastructure.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8068-91d4-c5916dd176d3" class="bulleted-list"><li style="list-style-type:disc"><strong>Trauma Reversal &amp; Stability</strong>: Clinics, protocols, and national programs (loop-closure metrics).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-808d-9177-c491814d395e" class="bulleted-list"><li style="list-style-type:disc"><strong>Ethical AI &amp; Digital Trust</strong>: Deterministic integrity layers for institutions and citizens.</li></ul></div><div style="display:contents" dir="auto"><blockquote id="24ac5e6f-95bd-8030-b868-e039a7462235" class="">Optional: Establish a<div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8060-8958-f6c2d8f74db2" class=""><strong>gold-backed trust</strong></p></div></blockquote></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-8011-9d8b-cb078f72ce41"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-804f-a8c0-da193db88ec3" class=""><strong>11) Deal Readiness Pack (Available Under NDA)</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8031-8580-cd143ae9ceea" class="bulleted-list"><li style="list-style-type:disc">UBS <strong>SKR</strong> (redacted)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-805e-a363-e7db89e0397d" class="bulleted-list"><li style="list-style-type:disc"><strong>Bar List</strong> (serials/weights/fineness/refiners)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80c0-a44b-c47b1a17ae1a" class="bulleted-list"><li style="list-style-type:disc"><strong>POP</strong> template; bank-to-bank verbiage</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8004-ad67-e99cd967d0ae" class="bulleted-list"><li style="list-style-type:disc"><strong>SPA + IMFPA</strong> drafts</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-806e-8f54-f4eb0c925f8a" class="bulleted-list"><li style="list-style-type:disc"><strong>KYC/AML</strong> (sell-side)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8010-aa80-c7a3050e879d" class="bulleted-list"><li style="list-style-type:disc"><strong>Assay/Audit</strong> protocol (SGS/Bureau Veritas)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80ca-b89d-e5e26112c699" class="bulleted-list"><li style="list-style-type:disc"><strong>Escrow Term Sheet</strong> (Tier-1)</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-805a-9f1d-e9ff231bf758"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-80e5-b730-d5ae0e57827c" class=""><strong>12) One-Page Email Cover (Use with the deck)</strong></h2></div><div style="display:contents" dir="auto"><blockquote id="24ac5e6f-95bd-80dc-8df3-f5b262ae784b" class="">Subject:</blockquote></div><div style="display:contents" dir="auto"><blockquote id="24ac5e6f-95bd-80fc-90ee-cc1e82851525" class=""></blockquote></div><div style="display:contents" dir="auto"><blockquote id="24ac5e6f-95bd-809a-bea5-c497e152328d" class="">We represent the principal holder of<div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8071-9acf-faeae68a506f" class=""><strong>500 metric tonnes of LBMA Good Delivery gold</strong></p></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8054-8c84-f67e21b22c88" class=""><strong>UBS-authenticated SKR</strong></p></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8018-8545-f6d24c4426c8" class=""><strong>allocated, serialized, and compliance-ready</strong></p></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-80e8-a4b4-f623f4248c1a" class=""><strong>tranche-based execution</strong></p></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8086-a90b-c9d0719a4ba6" class=""><strong>in-vault title transfer</strong></p></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8085-9aab-f401f95ccbc9" class=""><strong>MT103/202</strong></p></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8020-af37-cb3f2cf8caae" class=""><strong>instrumented rails (MT799/760)</strong></p></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8010-9cb5-fb95c02943bd" class=""><strong>Tier-1 escrow</strong></p></div></blockquote></div><div style="display:contents" dir="auto"><blockquote id="24ac5e6f-95bd-8082-bfc7-e93b4b6a8565" class=""></blockquote></div><div style="display:contents" dir="auto"><blockquote id="24ac5e6f-95bd-80b5-95d7-e663919eedd6" class="">Eligible counterparties include<div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-80fa-ac3a-c7835dab352e" class=""><strong>central banks</strong></p></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-80a4-b7d5-fb4848935b04" class=""><strong>sovereign wealth funds</strong></p></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-802f-b1b4-e1bf89ee40af" class=""><strong>LBMA bullion banks</strong></p></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-806a-89ca-c36ffe79f2f0" class=""><strong>POP</strong></p></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8073-bc6e-f686f4752920" class=""><strong>under NDA</strong></p></div></blockquote></div><div style="display:contents" dir="auto"><blockquote id="24ac5e6f-95bd-8064-9640-d5c3d5c5af93" class=""></blockquote></div><div style="display:contents" dir="auto"><blockquote id="24ac5e6f-95bd-80cf-afdf-c24a701930d1" class="">Please indicate your<div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-80f3-bf3b-eaff4692b8e0" class=""><strong>preferred tranche size</strong></p></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-80c7-95c1-f08c8caec95a" class=""><strong>settlement rail</strong></p></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-808b-a508-e13b157a7e65" class=""><strong>inspection requirements</strong></p></div></blockquote></div><div style="display:contents" dir="auto"><blockquote id="24ac5e6f-95bd-80f7-8fda-fec98fc13007" class=""></blockquote></div><div style="display:contents" dir="auto"><blockquote id="24ac5e6f-95bd-805b-b5a9-ee947e2b8b8b" class="">Best regards,</blockquote></div><div style="display:contents" dir="auto"><blockquote id="24ac5e6f-95bd-804a-8d8b-e7e53ab70e94" class="">[Your Name / Entity]</blockquote></div><div style="display:contents" dir="auto"><blockquote id="24ac5e6f-95bd-801c-887f-e1db6d3f4a0e" class="">Counsel:</blockquote></div><div style="display:contents" dir="auto"><blockquote id="24ac5e6f-95bd-806b-9ff7-daf927942883" class="">Bank Liaison:</blockquote></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80ab-947e-eae3fb64c7bd"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8013-a88d-c969856e136f" class=""><strong>13) Appendix — Risk Matrix (Abbrev.)</strong></h2></div><div style="display:contents" dir="ltr"><table id="24ac5e6f-95bd-8091-85cd-df9b9ec3a791" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-80c3-b318-ed5e2e8143b3"><th id="`Q_D" class="simple-table-header-color simple-table-header"><strong>Risk</strong></th><th id="P^b]" class="simple-table-header-color simple-table-header"><strong>Likelihood</strong></th><th id="lWYX" class="simple-table-header-color simple-table-header"><strong>Impact</strong></th><th id="z&gt;&gt;D" class="simple-table-header-color simple-table-header"><strong>Mitigation</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-8094-bf11-d5746572b62f"><td id="`Q_D" class="">Buyer POF insufficiency</td><td id="P^b]" class="">Med</td><td id="lWYX" class="">High</td><td id="z&gt;&gt;D" class="">Pre-screen POF; named officers; bank calls</td></tr></div><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-80df-9a6d-dabb8e033c1b"><td id="`Q_D" class="">Broker chain interference</td><td id="P^b]" class="">High</td><td id="lWYX" class="">Med</td><td id="z&gt;&gt;D" class="">Direct-to-mandate; NCNDA; tight circulation</td></tr></div><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-804f-92e0-e9decb64e763"><td id="`Q_D" class="">Sanctions/AML flags</td><td id="P^b]" class="">Low</td><td id="lWYX" class="">High</td><td id="z&gt;&gt;D" class="">Continuous screening; automated checks</td></tr></div><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-8020-838e-e710aaec921d"><td id="`Q_D" class="">Settlement delay</td><td id="P^b]" class="">Med</td><td id="lWYX" class="">Med</td><td id="z&gt;&gt;D" class="">Tier-1 escrow; sequenced tranches</td></tr></div><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-8007-b871-f26d048b440d"><td id="`Q_D" class="">Assay disputes</td><td id="P^b]" class="">Low</td><td id="lWYX" class="">Med</td><td id="z&gt;&gt;D" class="">Pre-agreed LBMA assay protocol</td></tr></div></tbody></table></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
