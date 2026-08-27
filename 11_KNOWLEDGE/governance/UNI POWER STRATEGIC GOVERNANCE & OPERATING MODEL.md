---
tags: [governance]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>UNI POWER STRATEGIC GOVERNANCE &amp; OPERATING MODEL</title><style>
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
	
</style></head><body><article id="29bc5e6f-95bd-803a-ae16-e7c309e8f16f" class="page sans"><header><h1 class="page-title" dir="auto"><strong>UNI POWER STRATEGIC GOVERNANCE &amp; OPERATING MODEL</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><hr id="29bc5e6f-95bd-80aa-9dfd-c9a9f8007ae6"/></div><div style="display:contents" dir="auto"><h3 id="29bc5e6f-95bd-809e-9da7-dec666cdd0eb" class=""><em>Centralised Intelligence — Decentralised Execution — Deterministic Growth</em></h3></div><div style="display:contents" dir="auto"><hr id="29bc5e6f-95bd-800d-9615-e15a3ff9b90a"/></div><div style="display:contents" dir="auto"><h2 id="29bc5e6f-95bd-8010-85fe-d7df34555ee7" class=""><strong>I. Strategic Intent</strong></h2></div><div style="display:contents" dir="auto"><blockquote id="29bc5e6f-95bd-806f-a08f-f75301bedfb7" class="">Build a deterministic, low-friction organisation that scales fast and sustainably — combining centralised strategic control with decentralised operational execution, aligned to international governance standards (OECD, IFC, ISO 27001/27701, COSO).</blockquote></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-80fe-af57-f55c251f7369" class="bulleted-list"><li style="list-style-type:disc">The <strong>Chairman</strong> and <strong>Board of Directors (BoD)</strong> hold all <em>thinking, capital, and decision rights</em>.</li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-809e-8d4e-ceb6b3836606" class="bulleted-list"><li style="list-style-type:disc">The <strong>CEO and six functional leaders (CXOs)</strong> convert strategy into <em>repeatable, measurable systems</em>.</li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-8076-b192-faaaffef8a2c" class="bulleted-list"><li style="list-style-type:disc">Every process is designed for <strong>transparency, accountability, and scalability</strong> — enabling low ego, low cost, and high velocity across the ecosystem.</li></ul></div><div style="display:contents" dir="auto"><hr id="29bc5e6f-95bd-80a3-b63f-ccfdd879df63"/></div><div style="display:contents" dir="auto"><h2 id="29bc5e6f-95bd-80a2-aad0-c0b0367449d2" class=""><strong>II. Core Design Philosophy</strong></h2></div><div style="display:contents" dir="ltr"><table id="29bc5e6f-95bd-802c-a4a8-da6694397586" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-809a-8c53-da1515730a4b"><th id="N;ZD" class="simple-table-header-color simple-table-header"><strong>Centralised Elements</strong></th><th id="yEao" class="simple-table-header-color simple-table-header"><strong>Decentralised Elements</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-80e0-94fc-fdf081e7ada6"><td id="N;ZD" class="">Strategy, capital allocation, brand, compliance, governance</td><td id="yEao" class="">Execution, fleet operations, customer experience, product rollout</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-804b-9109-c5caa4a00207"><td id="N;ZD" class="">Decisions made by Chairman + BoD</td><td id="yEao" class="">Actions executed by CEO + CXOs</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-803c-a7c1-f10979393fbc"><td id="N;ZD" class="">One <strong>Single Source of Truth (SSOT)</strong> for all data</td><td id="yEao" class="">Independent operational domains connected by shared data standards</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-808a-99ac-d2def77a7840"><td id="N;ZD" class="">Deep due diligence before scaling</td><td id="yEao" class="">Rapid iteration within approved frameworks</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="29bc5e6f-95bd-8055-94bc-d2f5f4cde357" class=""><strong>Goal:</strong> High-speed, low-entropy organisation — <em>tight on logic, loose on method.</em></p></div><div style="display:contents" dir="auto"><p id="29bc5e6f-95bd-80c0-aa52-ee2506794c22" class=""><strong>Global Benchmark:</strong></p></div><div style="display:contents" dir="auto"><p id="29bc5e6f-95bd-80ae-bcb6-e99e36fa0774" class="">McKinsey Hybrid Operating Model 2020 – “Centralised thinking, decentralised doing”</p></div><div style="display:contents" dir="auto"><p id="29bc5e6f-95bd-8070-8856-f3e9c679ad5e" class="">IFC Corporate Governance 2021 – “Separation of oversight and execution”</p></div><div style="display:contents" dir="auto"><p id="29bc5e6f-95bd-80e0-a8d2-de82aef20dc1" class="">Tesla/Grab Ops Model – “Central command, local speed”</p></div><div style="display:contents" dir="auto"><hr id="29bc5e6f-95bd-8058-974a-f3abaa1d9d27"/></div><div style="display:contents" dir="auto"><h2 id="29bc5e6f-95bd-80e2-8390-c0b710bba70e" class=""><strong>III. Leadership Architecture</strong></h2></div><div style="display:contents" dir="auto"><h3 id="29bc5e6f-95bd-805d-b705-d5231d0124ee" class=""><strong>1. Chairman &amp; Board of Directors</strong></h3></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-804c-9892-e4c6e12f0e1f" class="bulleted-list"><li style="list-style-type:disc">Set strategy, approve capital, monitor compliance, and define <em>“what must never fail.”</em></li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-80ec-be4c-dc617c100a8b" class="bulleted-list"><li style="list-style-type:disc">Govern through four committees aligned with OECD &amp; IFC best practice:<div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-805b-a90b-f159171d4627" class="bulleted-list"><li style="list-style-type:circle"><strong>Audit &amp; Risk Committee (ARC)</strong> – financial control, PDP compliance, cybersecurity (COSO, ISO 27001).</li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-804a-bc52-ef399fe442ef" class="bulleted-list"><li style="list-style-type:circle"><strong>Technology &amp; Data Committee (TDC)</strong> – SSOT, AI ethics, ISO 27701, data governance.</li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-80a9-a5b0-e1d24012e4e1" class="bulleted-list"><li style="list-style-type:circle"><strong>Remuneration &amp; Nomination Committee (RemNom)</strong> – succession, performance, ESOP.</li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-8062-97a7-ea13a2732ee5" class="bulleted-list"><li style="list-style-type:circle"><strong>ESG &amp; Safety Committee (ESC)</strong> – ESG reporting, carbon tracking (IFRS S2 / GHG Protocol).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-80dc-96d4-d4649e037095" class="bulleted-list"><li style="list-style-type:disc">Approve all expansion, investment, and partnership decisions above threshold.</li></ul></div><div style="display:contents" dir="auto"><h3 id="29bc5e6f-95bd-80c1-9869-cb9eaa037324" class=""><strong>2. CEO – Executive Integrator</strong></h3></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-8026-a14c-cb533a642da3" class="bulleted-list"><li style="list-style-type:disc">Converts board strategy into operational architecture.</li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-8097-911e-f5d9e5734416" class="bulleted-list"><li style="list-style-type:disc">Owns data integrity, cross-domain alignment, and delivery discipline.</li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-80f2-9f9f-cd06c7aaaace" class="bulleted-list"><li style="list-style-type:disc">Leads the six executive domains and ensures deterministic reporting to BoD.</li></ul></div><div style="display:contents" dir="auto"><hr id="29bc5e6f-95bd-80d8-acc2-ce131d846758"/></div><div style="display:contents" dir="auto"><h2 id="29bc5e6f-95bd-806d-bc63-c99f32033e5e" class=""><strong>IV. Six Executive Domains (CXOs Under CEO)</strong></h2></div><div style="display:contents" dir="ltr"><table id="29bc5e6f-95bd-807b-8723-e61e712950d6" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-8002-b06f-c27c4c7031fd"><th id="`\Jv" class="simple-table-header-color simple-table-header"><strong>Role</strong></th><th id="_Frk" class="simple-table-header-color simple-table-header"><strong>Core Focus</strong></th><th id="OKsE" class="simple-table-header-color simple-table-header"><strong>International Benchmark Alignment</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-801e-b391-d9bbefc031e0"><td id="`\Jv" class=""><strong>COO</strong></td><td id="_Frk" class="">Fleet ops, drivers, charging, service quality</td><td id="OKsE" class="">Tesla Fleet Ops / ISO 39001 (Road Safety)</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-80bd-a2f2-fd372ad5778c"><td id="`\Jv" class=""><strong>CFO</strong></td><td id="_Frk" class="">Finance, tax, audit, investor relations</td><td id="OKsE" class="">IFRS, COSO Internal Control</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-80ff-bb67-e73e5bc4914c"><td id="`\Jv" class=""><strong>CTO</strong></td><td id="_Frk" class="">Technology, product, data, security, privacy</td><td id="OKsE" class="">ISO 27001 / 27701 / NIST CSF</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-805d-91bf-ec863dc20f0a"><td id="`\Jv" class=""><strong>CBO</strong></td><td id="_Frk" class="">Commercial, partnerships, B2B/ESG monetisation</td><td id="OKsE" class="">Uber B2B / Shell EV Alliances</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-802a-a3e4-e51e7e52ea7d"><td id="`\Jv" class=""><strong>CHRO</strong></td><td id="_Frk" class="">Talent, performance, culture, compliance</td><td id="OKsE" class="">McKinsey Org Health Index / ILO standards</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-8008-a49e-ff5a40bc9b67"><td id="`\Jv" class=""><strong>CMO</strong></td><td id="_Frk" class="">Brand, growth, digital marketing automation</td><td id="OKsE" class="">Apple Marketing Governance Model</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="29bc5e6f-95bd-80dc-b99c-e6dcaca0a625" class=""><strong>Legal/Compliance</strong> reports to CEO but maintains <em>direct access to Chairman / ARC</em> for independence.</p></div><div style="display:contents" dir="auto"><hr id="29bc5e6f-95bd-80bf-a27d-e055aed55fc6"/></div><div style="display:contents" dir="auto"><h2 id="29bc5e6f-95bd-80b5-a7af-d2fcfb97789d" class=""><strong>V. How the Model Works</strong></h2></div><div style="display:contents" dir="auto"><h3 id="29bc5e6f-95bd-8063-b43a-e0aaa9d403d1" class=""><strong>1. Central Brain — Chairman + BoD + CEO</strong></h3></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-80e1-bb45-f87cd63d5454" class="bulleted-list"><li style="list-style-type:disc">Owns <strong>strategy, capital logic, brand, and systemic integrity</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-8087-baab-eb0a70031c15" class="bulleted-list"><li style="list-style-type:disc">Sets <strong>KPIs, SLOs, and compliance boundaries</strong> for each domain.</li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-801b-8a62-ef8a6324af39" class="bulleted-list"><li style="list-style-type:disc">Approves architecture decisions; ensures deterministic, auditable outcomes.</li></ul></div><div style="display:contents" dir="auto"><h3 id="29bc5e6f-95bd-80fa-a38c-d561877aa407" class=""><strong>2. Decentralised Muscles — Six Domains</strong></h3></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-80c2-a1f0-daee6d4a1e0e" class="bulleted-list"><li style="list-style-type:disc">Operate autonomously under <strong>data contracts</strong> and <strong>KPI ownership</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-80bb-9566-c2d383c46522" class="bulleted-list"><li style="list-style-type:disc">Scale execution locally without re-approval — provided output meets SSOT thresholds.</li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-8034-bedf-f300c8f6e772" class="bulleted-list"><li style="list-style-type:disc">Continuous auto-synchronisation → no manual reports, no information lag.</li></ul></div><div style="display:contents" dir="auto"><h3 id="29bc5e6f-95bd-80a1-b28d-c92816eeb421" class=""><strong>3. Feedback Loop</strong></h3></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-801c-a377-d84b37bf2673" class="bulleted-list"><li style="list-style-type:disc"><strong>Weekly:</strong> Executive sync (performance + blockers).</li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-806b-b2d0-d1d485ff1f1b" class="bulleted-list"><li style="list-style-type:disc"><strong>Monthly:</strong> Board dashboards (cash, ESG, data, risk).</li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-8064-af14-cc0a7fbdec0d" class="bulleted-list"><li style="list-style-type:disc"><strong>Quarterly:</strong> Strategic recalibration (cross-domain adjustments).</li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-803f-973d-e22db9205ba1" class="bulleted-list"><li style="list-style-type:disc">Data replaces debate; errors trigger root-cause learning, not blame.</li></ul></div><div style="display:contents" dir="auto"><hr id="29bc5e6f-95bd-80e6-aed4-d3e62a93e3db"/></div><div style="display:contents" dir="auto"><h2 id="29bc5e6f-95bd-8014-9ab4-f825d254058d" class=""><strong>VI. Decision &amp; Incentive Architecture</strong></h2></div><div style="display:contents" dir="auto"><h3 id="29bc5e6f-95bd-80fa-ab61-c0c42d2092c2" class=""><strong>Decision Hierarchy</strong></h3></div><div style="display:contents" dir="ltr"><table id="29bc5e6f-95bd-8019-8d5f-cb005cf69cce" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-8022-9d84-f33fc3bdc890"><th id="rzqN" class="simple-table-header-color simple-table-header">Level</th><th id="Osy|" class="simple-table-header-color simple-table-header">Responsibility</th><th id="^nc~" class="simple-table-header-color simple-table-header">Approval Authority</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-8078-9918-fd22a433111c"><td id="rzqN" class=""><strong>BoD</strong></td><td id="Osy|" class="">Capital allocation, risk appetite, M&amp;A, governance, ESG</td><td id="^nc~" class="">Chairman-led BoD vote</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-806d-89f1-e29ee500ffba"><td id="rzqN" class=""><strong>CEO</strong></td><td id="Osy|" class="">Resource distribution, structural decisions</td><td id="^nc~" class="">BoD oversight</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-8086-b509-ffbd66db50f6"><td id="rzqN" class=""><strong>CXOs</strong></td><td id="Osy|" class="">Domain operations within SLO/KPI limits</td><td id="^nc~" class="">CEO approval within budget</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-8070-be7e-d6c89caaf3f0"><td id="rzqN" class=""><strong>Managers/Teams</strong></td><td id="Osy|" class="">Process execution</td><td id="^nc~" class="">CXO-level approval</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h3 id="29bc5e6f-95bd-8068-b5e3-de7dad17d426" class=""><strong>Incentive Model (Benchmark: BlackRock ESG Compensation 2024)</strong></h3></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-80f8-94c3-df8e1857d196" class="bulleted-list"><li style="list-style-type:disc"><strong>BoD, CEO, CXOs:</strong> Long-term incentives (LTI/ESOP) tied to company valuation, ESG, audit results.</li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-80fe-a4bc-ef4bce679449" class="bulleted-list"><li style="list-style-type:disc"><strong>Functional Teams:</strong> Fixed + process reliability bonuses (accuracy, uptime, NPS).</li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-80fe-922a-dd8b4b419ec3" class="bulleted-list"><li style="list-style-type:disc">Reinforces <strong>clarity over creativity, execution over ego</strong>.</li></ul></div><div style="display:contents" dir="auto"><hr id="29bc5e6f-95bd-8009-a7c3-d53473ff0d95"/></div><div style="display:contents" dir="auto"><h2 id="29bc5e6f-95bd-80aa-9f59-e4bae38f5130" class=""><strong>VII. Operating System (McKinsey-standard cadence)</strong></h2></div><div style="display:contents" dir="ltr"><table id="29bc5e6f-95bd-8044-861b-e6ba375eb285" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-8076-92cd-fec672b07a41"><th id="Qgdr" class="simple-table-header-color simple-table-header"><strong>Cadence</strong></th><th id="bPEU" class="simple-table-header-color simple-table-header"><strong>Forum</strong></th><th id="xEAT" class="simple-table-header-color simple-table-header"><strong>Purpose</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-80e4-807d-ce918e403b6c"><td id="Qgdr" class="">Weekly</td><td id="bPEU" class="">Executive Council (CEO + CXOs)</td><td id="xEAT" class="">Review KPIs, unblock actions</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-8057-8017-c047f0598e69"><td id="Qgdr" class="">Monthly</td><td id="bPEU" class="">Board Pack (≤15 pages, digital)</td><td id="xEAT" class="">P&amp;L, ESG, risk, audit, compliance</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-804c-a12e-ce44719d4425"><td id="Qgdr" class="">Quarterly</td><td id="bPEU" class="">Committee Deep Dives</td><td id="xEAT" class="">Tech/Data, ESG, HR, Commercial</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-8061-aeef-ccc451c52ab3"><td id="Qgdr" class="">Annually</td><td id="bPEU" class="">Strategy Offsite</td><td id="xEAT" class="">Capital review, structure optimisation</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="29bc5e6f-95bd-807a-bc8d-dcb62ec2f7c3" class=""><strong>Global Benchmark:</strong></p></div><div style="display:contents" dir="auto"><p id="29bc5e6f-95bd-805f-94ed-dbc7dd7fb7ae" class="">Tesla cadence (real-time ops), OECD audit transparency, Grab data-driven governance.</p></div><div style="display:contents" dir="auto"><p id="29bc5e6f-95bd-802a-83ae-e189b4c0f1a7" class="">All meetings supported by <strong>real-time dashboards from SSOT</strong> — no manual slides, no distortion.</p></div><div style="display:contents" dir="auto"><hr id="29bc5e6f-95bd-8045-9c58-de39a8eac6fc"/></div><div style="display:contents" dir="auto"><h2 id="29bc5e6f-95bd-8039-a167-d72e4c036223" class=""><strong>VIII. Transparency &amp; Compliance Framework</strong></h2></div><div style="display:contents" dir="ltr"><table id="29bc5e6f-95bd-80b7-bce3-f9e623572867" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-801a-bad3-cf6ba81f2e9a"><th id="&gt;?mP" class="simple-table-header-color simple-table-header"><strong>International Framework</strong></th><th id="Y\:m" class="simple-table-header-color simple-table-header"><strong>UniPower Application</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-80bb-a212-f7e7f0df2400"><td id="&gt;?mP" class=""><strong>OECD Corporate Governance 2023</strong></td><td id="Y\:m" class="">Clear role separation; transparent decision records</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-8094-9195-d700e711bfcc"><td id="&gt;?mP" class=""><strong>IFC Governance Index 2021</strong></td><td id="Y\:m" class="">Public data lineage, audit-ready controls</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-8010-99b5-fa0369876b77"><td id="&gt;?mP" class=""><strong>ISO 27001 / 27701</strong></td><td id="Y\:m" class="">Full encryption, DPIA-by-design, immutable audit logs</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-80ae-bdd9-f0d1f1e22e6f"><td id="&gt;?mP" class=""><strong>COSO Enterprise Risk</strong></td><td id="Y\:m" class="">Live risk register, reconciliation trip–invoice ≤0.1%</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-80ad-9e63-d8b9dcb51440"><td id="&gt;?mP" class=""><strong>IFRS S2 / GHG Protocol</strong></td><td id="Y\:m" class="">ESG dashboard (CO₂ avoided/trip, fleet energy efficiency)</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="29bc5e6f-95bd-80e7-9d59-d6cb4e8babaf"/></div><div style="display:contents" dir="auto"><h2 id="29bc5e6f-95bd-808a-a92b-d40dd082aa1d" class=""><strong>IX. Cultural DNA</strong></h2></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-80e6-a146-f0d74c72cdd7" class="bulleted-list"><li style="list-style-type:disc"><strong>Transparent:</strong> everyone sees identical metrics; no private data silos.</li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-8001-9c35-e342a61925aa" class="bulleted-list"><li style="list-style-type:disc"><strong>Accountable:</strong> every KPI has an owner, escalation path, and log.</li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-808a-b2ce-d794b7c4f119" class="bulleted-list"><li style="list-style-type:disc"><strong>Low-Ego:</strong> decisions by data, not emotion.</li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-80b1-bd6d-eb380fbc5ec6" class="bulleted-list"><li style="list-style-type:disc"><strong>Deterministic:</strong> no “opinions” — only measurable truths.</li></ul></div><div style="display:contents" dir="auto"><ul id="29bc5e6f-95bd-8095-ab1f-e6016edc6665" class="bulleted-list"><li style="list-style-type:disc"><strong>Sustainable:</strong> ESG and compliance embedded into daily decision logic.</li></ul></div><div style="display:contents" dir="auto"><p id="29bc5e6f-95bd-8059-b8f0-e8c96142c040" class=""><strong>Cultural Benchmark:</strong> Bridgewater’s “Radical Transparency” × McKinsey’s “Process Discipline”.</p></div><div style="display:contents" dir="auto"><hr id="29bc5e6f-95bd-80bf-9bcf-e333594b0b25"/></div><div style="display:contents" dir="auto"><h2 id="29bc5e6f-95bd-8043-9000-e0e4cdea19be" class=""><strong>X. Global Benchmark Comparison</strong></h2></div><div style="display:contents" dir="ltr"><table id="29bc5e6f-95bd-8032-942b-c68bd54d947d" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-80b3-a360-c2151b002582"><th id="@sT]" class="simple-table-header-color simple-table-header"><strong>Dimension</strong></th><th id="fwRx" class="simple-table-header-color simple-table-header"><strong>Typical Emerging-Market Company</strong></th><th id="XU~~" class="simple-table-header-color simple-table-header"><strong>UniPower Model</strong></th><th id="?CgL" class="simple-table-header-color simple-table-header"><strong>International Benchmark</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-8025-953d-f3cce41c46a0"><td id="@sT]" class="">Governance</td><td id="fwRx" class="">Founder-centric</td><td id="XU~~" class="">Institutional-grade hybrid model</td><td id="?CgL" class="">OECD / IFC</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-801e-a4f0-f8d537e2ae23"><td id="@sT]" class="">Data Integrity</td><td id="fwRx" class="">Fragmented reports</td><td id="XU~~" class="">SSOT with lineage and DQ monitoring</td><td id="?CgL" class="">Tesla / Grab</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-8091-9f45-dc51ac5d0bfd"><td id="@sT]" class="">Compliance</td><td id="fwRx" class="">Reactive</td><td id="XU~~" class="">Built-in PDP, ISO standards</td><td id="?CgL" class="">EU GDPR / VN PDP 13</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-802c-8e93-f5e1d7b47306"><td id="@sT]" class="">Decision-Making</td><td id="fwRx" class="">Consensus-driven</td><td id="XU~~" class="">Deterministic, KPI-based</td><td id="?CgL" class="">McKinsey Hybrid Model</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-80b4-ae9f-e5bc5dc727e1"><td id="@sT]" class="">Culture</td><td id="fwRx" class="">Charisma-led</td><td id="XU~~" class="">Low-ego, process-led</td><td id="?CgL" class="">Bridgewater Principles</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-80df-b46d-de37d2036ac9"><td id="@sT]" class="">ESG Readiness</td><td id="fwRx" class="">Post-hoc</td><td id="XU~~" class="">Embedded from day one</td><td id="?CgL" class="">IFRS S2 / GHG Protocol</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="29bc5e6f-95bd-8033-aa32-c2771480913a"/></div><div style="display:contents" dir="auto"><h2 id="29bc5e6f-95bd-8004-ba6a-dbca43c24122" class=""><strong>XI. Strategic Outcomes (Global Benchmark Targets)</strong></h2></div><div style="display:contents" dir="ltr"><table id="29bc5e6f-95bd-80fa-869c-e6c9749ef82b" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-803a-ac7e-ebb752e85d89"><th id="Hp=E" class="simple-table-header-color simple-table-header"><strong>Metric</strong></th><th id="kmI\" class="simple-table-header-color simple-table-header"><strong>Benchmark</strong></th><th id="Xgo|" class="simple-table-header-color simple-table-header"><strong>UniPower Target</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-80a8-93e1-ee3cc4c6bcb4"><td id="Hp=E" class="">Fleet Uptime</td><td id="kmI\" class="">Tesla ≥98%</td><td id="Xgo|" class="">≥98%</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-80e9-a7a7-c4d3abdfc48e"><td id="Hp=E" class="">Data Latency</td><td id="kmI\" class="">ISO / AWS ≤300 ms</td><td id="Xgo|" class="">≤300 ms</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-8052-97ae-ff9dc123957e"><td id="Hp=E" class="">ESG Reporting Cycle</td><td id="kmI\" class="">IFRS S2 (quarterly)</td><td id="Xgo|" class="">Real-time dashboard</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-8072-9168-e3a1b00c8875"><td id="Hp=E" class="">Audit Trail Completeness</td><td id="kmI\" class="">COSO ≥95%</td><td id="Xgo|" class="">100% immutable logs</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-80c3-9430-c4bee28366b5"><td id="Hp=E" class="">Compliance Coverage</td><td id="kmI\" class="">OECD ≥95%</td><td id="Xgo|" class="">≥98%</td></tr></div><div style="display:contents" dir="ltr"><tr id="29bc5e6f-95bd-8051-a162-d81c41301341"><td id="Hp=E" class="">Organisational Efficiency</td><td id="kmI\" class="">McKinsey hybrid (30–40% leaner)</td><td id="Xgo|" class="">35% lean structure</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="29bc5e6f-95bd-80b1-ac10-e6408bdb8c3d"/></div><div style="display:contents" dir="auto"><h2 id="29bc5e6f-95bd-8009-afd6-edb8be9fb398" class=""><strong>XII. Key Takeaways</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="29bc5e6f-95bd-807a-937f-c289a4478609" class="numbered-list" start="1"><li><strong>Centralised thinking, decentralised doing</strong> — strategy tight, execution flexible.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="29bc5e6f-95bd-80b7-a2b7-d30cd157bd2b" class="numbered-list" start="2"><li><strong>All data in one truth system (SSOT)</strong> — live, auditable, compliant.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="29bc5e6f-95bd-80d5-93b0-f9288a0b6398" class="numbered-list" start="3"><li><strong>Decision rights = accountability</strong> — no duplication, no politics.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="29bc5e6f-95bd-80be-8da4-ea395cca4a64" class="numbered-list" start="4"><li><strong>Incentives reward clarity, not chaos.</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="29bc5e6f-95bd-8016-83a5-ce8415e56036" class="numbered-list" start="5"><li><strong>Culture = transparency × discipline = velocity.</strong></li></ol></div><div style="display:contents" dir="auto"><blockquote id="29bc5e6f-95bd-809c-854c-ce49b51d4d83" class="">This governance model aligns UniPower with global institutional standards —<div style="display:contents" dir="auto"><p id="29bc5e6f-95bd-808d-a763-ccc437248410" class="">combining <strong>Tesla’s operational speed</strong>, <strong>McKinsey’s organisational logic</strong>, and <strong>OECD’s governance discipline</strong> —</p></div><div style="display:contents" dir="auto"><p id="29bc5e6f-95bd-80f0-bc64-dbb1aff27c1f" class="">enabling the company to scale internationally <strong>without friction, ego, or compliance risk.</strong></p></div></blockquote></div><div style="display:contents" dir="auto"><hr id="29bc5e6f-95bd-804d-9355-cf831b66d192"/></div><div style="display:contents" dir="auto"><p id="29bc5e6f-95bd-8082-aa84-e0b2aaedd77d" class="">Would you like me to now turn this into a <strong>12-slide investor/board deck</strong>, with visual diagrams (decision pyramid, centralised–decentralised flow, governance committees, KPI flow from SSOT)?</p></div><div style="display:contents" dir="auto"><p id="29bc5e6f-95bd-806c-8cde-dd8fc8ba3883" class="">This would make it presentation-ready for institutional investors, IFC partners, or IPO roadshows.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
