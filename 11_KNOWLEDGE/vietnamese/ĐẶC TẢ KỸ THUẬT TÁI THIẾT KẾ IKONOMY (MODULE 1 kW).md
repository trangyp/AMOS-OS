---
tags: [vietnamese]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>ĐẶC TẢ KỸ THUẬT TÁI THIẾT KẾ IKONOMY (MODULE 1 kW)</title><style>
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
	
</style></head><body><article id="2e9c5e6f-95bd-8089-a5c9-e2f241d30e68" class="page sans"><header><h1 class="page-title" dir="auto"><strong>ĐẶC TẢ KỸ THUẬT TÁI THIẾT KẾ IKONOMY (MODULE 1 kW)</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2e9c5e6f-95bd-8075-87ae-f50ce4837c23" class="">
</p></div><div style="display:contents" dir="auto"><p id="2e9c5e6f-95bd-80b1-8a5f-f3a4ce1c2102" class="">
</p></div><div style="display:contents" dir="auto"><p id="2e9c5e6f-95bd-803d-8ede-e4af9e8cd075" class="">
</p></div><div style="display:contents" dir="auto"><p id="2e9c5e6f-95bd-8078-9708-f7bda268bd77" class="">
</p></div><div style="display:contents" dir="auto"><p id="2e9c5e6f-95bd-80b9-b7ee-d9ad94b6bb25" class="">
</p></div><div style="display:contents" dir="auto"><h2 id="2e9c5e6f-95bd-80fc-a27e-ee389c83c9c2" class=""><strong>1. Kiến trúc tổng thể hệ thống</strong></h2></div><div style="display:contents" dir="auto"><p id="2e9c5e6f-95bd-8053-ad9f-fe107571c8bc" class=""><strong>Sơ đồ khối chức năng:</strong></p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2e9c5e6f-95bd-8008-9fe3-e05a70a8271b" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">DC Input (48–96 VDC)
   ↓
Power Conditioning &amp; Protection
   ↓
Cannon Drive Stage (Current-Controlled Switching Converter)
   ↓
Electrolysis Stack
   ↓
Thermal Management System
   ↓
Gas Separation &amp; Conditioning
   ↓
H₂ Output (regulated)</code></pre></div><div style="display:contents" dir="auto"><p id="2e9c5e6f-95bd-80dc-9fd4-c2130a6dafa9" class="">Hệ thống được thiết kế theo nguyên tắc:</p></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80b3-bf67-d4a45fa8d1b4" class="bulleted-list"><li style="list-style-type:disc"><strong>Current-driven electrochemistry</strong> (dòng quyết định phản ứng, không phải áp).</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80f3-bcbf-f6b74f2ecf73" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều khiển điện – nhiệt – khí đồng thời</strong> (multi-domain control).</li></ul></div><div style="display:contents" dir="auto"><hr id="2e9c5e6f-95bd-80b1-abf9-f75e84d163e5"/></div><div style="display:contents" dir="auto"><h2 id="2e9c5e6f-95bd-80e6-8090-c1d40b2cb869" class=""><strong>2. Đặc tả điện – công suất (Electrical &amp; Power Electronics)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e9c5e6f-95bd-80b2-9a48-df1732bf41c0" class=""><strong>2.1 Nguồn vào DC</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80f6-bf69-e8388d750753" class="bulleted-list"><li style="list-style-type:disc">Điện áp danh định: <strong>48–96 VDC</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80f2-9a1c-fafd9c5a2d8f" class="bulleted-list"><li style="list-style-type:disc">Dải cho phép: ±15%</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80f3-ad75-e8d0250d6f5e" class="bulleted-list"><li style="list-style-type:disc">Dòng tối đa (boost): xác định theo công suất 2 kW @ 48 V → ~42 A</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8048-84e9-ed4b9011f4bf" class="bulleted-list"><li style="list-style-type:disc">Bảo vệ:<div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-808a-a86d-f4c5644ff7df" class="bulleted-list"><li style="list-style-type:circle">OVP / UVP</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8028-95a0-f033dbc7f536" class="bulleted-list"><li style="list-style-type:circle">Reverse polarity</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80b8-bedd-c51cce96d469" class="bulleted-list"><li style="list-style-type:circle">Inrush current limiting</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8015-9045-f79a592a555d" class="bulleted-list"><li style="list-style-type:circle">Surge suppression (TVS + LC input filter)</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2e9c5e6f-95bd-80e3-86d3-f748c9a487b2"/></div><div style="display:contents" dir="auto"><h3 id="2e9c5e6f-95bd-80c1-8638-f01ae1bf824c" class=""><strong>2.2 Cannon Drive Stage (trái tim hệ thống)</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2e9c5e6f-95bd-808d-8865-f06237681856" class=""><strong>2.2.1 Cấu trúc</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8031-98d4-da7a9a51a51f" class="bulleted-list"><li style="list-style-type:disc"><strong>Converter kiểu:</strong><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8024-a7c7-c650f6ed5e9f" class="bulleted-list"><li style="list-style-type:circle">Buck / Buck-Boost đồng bộ (tuỳ cấu hình stack)</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-809b-a829-c279d9829d02" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều khiển:</strong><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80c3-9cd5-de4e506c0e36" class="bulleted-list"><li style="list-style-type:circle">Closed-loop <strong>current control</strong> (PI hoặc PI + feedforward)</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80c1-88db-d5e920121c85" class="bulleted-list"><li style="list-style-type:disc"><strong>Switching device:</strong><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80e6-91b4-f6d698caddac" class="bulleted-list"><li style="list-style-type:circle">MOSFET công suất thấp Rds(on) hoặc SiC MOSFET (nếu cần boost cao)</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2e9c5e6f-95bd-80ee-a5e3-cdbf3d1853b0" class=""><strong>2.2.2 Thông số chuyển mạch</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-800c-866f-fae73fd44556" class="bulleted-list"><li style="list-style-type:disc">Tần số đóng cắt: <strong>200 Hz – 5 kHz</strong> (có thể lập trình)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80a9-9464-c3a7f7f61ef3" class="bulleted-list"><li style="list-style-type:disc">Slew rate giới hạn:<div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80bd-927f-e79f27370955" class="bulleted-list"><li style="list-style-type:circle">dI/dt ≤ giá trị xác định theo stack (ví dụ &lt; 0.5 A/ms)</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-801f-95fc-e429d2d951ed" class="bulleted-list"><li style="list-style-type:disc">Dead-time kiểm soát để giảm switching loss + EMI</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e9c5e6f-95bd-8087-97fa-f4833d1f7525" class=""><strong>2.2.3 Đo lường &amp; phản hồi</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80cf-b28e-d472cc177611" class="bulleted-list"><li style="list-style-type:disc">Cảm biến dòng:<div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-805f-92e0-daa07add1728" class="bulleted-list"><li style="list-style-type:circle">Hall-effect hoặc shunt + amplifier</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8091-87f1-d6ece64be3ea" class="bulleted-list"><li style="list-style-type:circle">Độ chính xác: ≤1%</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8086-921b-cbb8260fd0ab" class="bulleted-list"><li style="list-style-type:disc">Đo áp:<div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8088-bf86-fbcf7e726796" class="bulleted-list"><li style="list-style-type:circle">Tổng áp stack</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80d8-bd21-f6d669f148c7" class="bulleted-list"><li style="list-style-type:circle">(khuyến nghị) chia segment nếu stack nhiều cell</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2e9c5e6f-95bd-800c-b182-ddf67d8bfc15"/></div><div style="display:contents" dir="auto"><h3 id="2e9c5e6f-95bd-80ff-b33d-f0b98985caa4" class=""><strong>2.2.4 Điều khiển dạng sóng (Waveform Control)</strong></h3></div><div style="display:contents" dir="auto"><p id="2e9c5e6f-95bd-804b-82cf-fb29fc63eec1" class="">Không chỉ PWM on/off, mà là <strong>thư viện dạng kích thích</strong>:</p></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8077-a42b-cc000ed57e56" class="bulleted-list"><li style="list-style-type:disc">DC mượt (baseline)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8091-bd2b-f406ff03a9bc" class="bulleted-list"><li style="list-style-type:disc">Pulsed DC có duty + frequency thay đổi</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80c9-9dc1-f6525084ad1f" class="bulleted-list"><li style="list-style-type:disc">Soft-burst (burst envelope có ramp)</li></ul></div><div style="display:contents" dir="auto"><p id="2e9c5e6f-95bd-8001-bf08-cf8d95cfef46" class="">Thuật toán chọn waveform dựa trên:</p></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8004-adcd-d0987f7bae74" class="bulleted-list"><li style="list-style-type:disc">Điện trở tương đương stack (R_eq)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-809d-b82b-d6964fec845b" class="bulleted-list"><li style="list-style-type:disc">Độ lệch nhiệt</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80da-946d-f562044938f1" class="bulleted-list"><li style="list-style-type:disc">Dao động áp / dòng</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80ba-ae11-eff14dd5edfe" class="bulleted-list"><li style="list-style-type:disc">Proxy suy giảm (degradation indicator)</li></ul></div><div style="display:contents" dir="auto"><hr id="2e9c5e6f-95bd-8007-aee1-ecd22462d9f8"/></div><div style="display:contents" dir="auto"><h2 id="2e9c5e6f-95bd-8051-a2aa-c70ebc9fefe7" class=""><strong>3. Đặc tả stack điện phân (Electrolysis Stack)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e9c5e6f-95bd-807e-a86e-e5624c2de138" class=""><em>(Giữ trung lập hoá học vì chưa xác nhận PEM/AEM/alkaline)</em></p></div><div style="display:contents" dir="auto"><h3 id="2e9c5e6f-95bd-80b7-875b-ddef198d17d5" class=""><strong>3.1 Thông số vận hành</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-802c-bf13-e6c116d515f6" class="bulleted-list"><li style="list-style-type:disc">Nhiệt độ làm việc: <strong>55–75 °C</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80a3-87a4-ec3b71edfc1e" class="bulleted-list"><li style="list-style-type:disc">Gradient nhiệt cho phép: <strong>≤5 °C</strong> trong vùng phản ứng</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80a6-97e6-fe79e7d24f4a" class="bulleted-list"><li style="list-style-type:disc">Áp suất làm việc: <strong>1.5–3 bar</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-800e-a3b6-cb1942ed1eb6" class="bulleted-list"><li style="list-style-type:disc">Điểm cruise:<div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8051-b7fb-eea7670fb040" class="bulleted-list"><li style="list-style-type:circle">Dòng riêng (A/cm²) nằm dưới ngưỡng Tafel cliff</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8067-b301-e079e0b71ad5" class="bulleted-list"><li style="list-style-type:disc">Điểm boost:<div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-804d-aa84-fea95bd8f578" class="bulleted-list"><li style="list-style-type:circle">Cho phép vượt dòng cruise nhưng bị giới hạn thời gian</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2e9c5e6f-95bd-80a6-8790-d5ca335b5ab4" class=""><strong>3.2 Giới hạn không được vượt</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8072-9c2b-d03116496569" class="bulleted-list"><li style="list-style-type:disc">Overpotential vượt ngưỡng → <strong>derate ngay</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8026-bcb4-c3820d90b66d" class="bulleted-list"><li style="list-style-type:disc">Dao động dòng lớn → <strong>giảm tần số / duty</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8030-b116-d41878b2963b" class="bulleted-list"><li style="list-style-type:disc">Crossover khí vượt ngưỡng → <strong>lock boost</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="2e9c5e6f-95bd-80c3-b2a3-e7f3e8efc6c3"/></div><div style="display:contents" dir="auto"><h2 id="2e9c5e6f-95bd-8026-a590-e61e5bc6cea3" class=""><strong>4. Hệ thống nhiệt (Thermal Management)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e9c5e6f-95bd-80fd-a17f-da7ab87a653c" class=""><strong>4.1 Mục tiêu</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-805a-9e9d-d0b88885a7a0" class="bulleted-list"><li style="list-style-type:disc">Không tối đa hoá tản nhiệt, mà <strong>tối ưu phân bố nhiệt</strong>.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e9c5e6f-95bd-803b-ae3f-d4b78f99d8a0" class=""><strong>4.2 Thiết kế</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8047-aa98-fd54b518993d" class="bulleted-list"><li style="list-style-type:disc">Thermal mass đặt gần vùng mật độ phản ứng cao</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-803c-b3ac-f6219ef24a8f" class="bulleted-list"><li style="list-style-type:disc">Heat spreader (nhôm / đồng)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80f3-a3fe-c0064e3e3e7c" class="bulleted-list"><li style="list-style-type:disc">Đường nước / khí làm mát có tiết diện đủ lớn</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80a9-a79c-eb3bf6c180e2" class="bulleted-list"><li style="list-style-type:disc">Quạt / bơm chỉ là <strong>phụ trợ</strong>, không phải tuyến chính</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e9c5e6f-95bd-805f-880d-d491b4f71164" class=""><strong>4.3 Luật điều khiển nhiệt</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8075-a15f-db7ef378b40d" class="bulleted-list"><li style="list-style-type:disc">dT/dt ≤ 1 °C/phút</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8015-ba24-e52e5aa7ad0a" class="bulleted-list"><li style="list-style-type:disc">Nếu gradient tăng nhanh → giảm dòng trước, <strong>không chờ alarm</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="2e9c5e6f-95bd-8053-a51b-cd7ee40b5bc1"/></div><div style="display:contents" dir="auto"><h2 id="2e9c5e6f-95bd-80e5-9458-e898ab192718" class=""><strong>5. Hệ thống nước (Water Management)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e9c5e6f-95bd-80bb-b5bf-d16e31316c73" class=""><strong>5.1 Chức năng</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8070-9782-d1e16f6da15d" class="bulleted-list"><li style="list-style-type:disc">Cấp nước phản ứng</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-806c-a166-f2e5ac3ba7c4" class="bulleted-list"><li style="list-style-type:disc">Bù nước thất thoát</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80d7-9357-d52273ab6429" class="bulleted-list"><li style="list-style-type:disc">Giám sát chất lượng</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e9c5e6f-95bd-8074-9a65-daf66b7b722a" class=""><strong>5.2 Cảm biến &amp; điều khiển</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8090-b5ea-e2d5fed8f9ec" class="bulleted-list"><li style="list-style-type:disc">Cảm biến mức nước</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-800e-a7cb-e463b90580d6" class="bulleted-list"><li style="list-style-type:disc">(Khuyến nghị) cảm biến độ dẫn điện</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8002-97b3-fa460cc911a8" class="bulleted-list"><li style="list-style-type:disc">Logic:<div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-800d-858a-dd4ec0d9d4f2" class="bulleted-list"><li style="list-style-type:circle">Nước kém → giảm công suất</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8042-9223-cd1e23e39b80" class="bulleted-list"><li style="list-style-type:circle">Không bao giờ “cố chạy”</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2e9c5e6f-95bd-80a4-b343-f748c4c2aca7"/></div><div style="display:contents" dir="auto"><h2 id="2e9c5e6f-95bd-801d-8531-e05e3362432a" class=""><strong>6. Hệ thống khí H₂ (Gas Handling)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e9c5e6f-95bd-80a4-b750-f75f783481bd" class=""><strong>6.1 Tách &amp; làm sạch</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8072-8673-c898f5f1bdb0" class="bulleted-list"><li style="list-style-type:disc">Bubbler / water trap đủ lớn cho <strong>lưu lượng boost</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80bf-bb8f-db0f5602f7f3" class="bulleted-list"><li style="list-style-type:disc">Thiết kế tránh carryover nước</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e9c5e6f-95bd-80f5-887b-cfeccb09b752" class=""><strong>6.2 Áp suất &amp; an toàn</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80df-b982-c1249232af57" class="bulleted-list"><li style="list-style-type:disc">Buffer volume để triệt xung áp</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80e9-b857-e65bb25d4620" class="bulleted-list"><li style="list-style-type:disc">Pressure ripple ≤3%</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-806c-ac17-ea7c0814ffce" class="bulleted-list"><li style="list-style-type:disc">Van một chiều + chống backflow</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-803e-8eaa-fd2dd3473cb2" class="bulleted-list"><li style="list-style-type:disc">Không lưu trữ H₂ khi hệ thống dừng (đúng triết lý patent)</li></ul></div><div style="display:contents" dir="auto"><hr id="2e9c5e6f-95bd-8092-b24f-dafd35c68a07"/></div><div style="display:contents" dir="auto"><h2 id="2e9c5e6f-95bd-8052-bc50-ffd84730262e" class=""><strong>7. Hệ thống điều khiển &amp; firmware</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e9c5e6f-95bd-8012-9c19-d451ccc65328" class=""><strong>7.1 Các mode bắt buộc</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-806c-ad5f-d9e8e0c70bbc" class="bulleted-list"><li style="list-style-type:disc">Cruise</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8096-8bc0-da2dff8bdb35" class="bulleted-list"><li style="list-style-type:disc">Boost</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80e4-9d0d-e583b0207baf" class="bulleted-list"><li style="list-style-type:disc">Degraded</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80a1-8d40-cbc3daa8646d" class="bulleted-list"><li style="list-style-type:disc">Protective</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80ee-ab98-c74876cb8ad2" class="bulleted-list"><li style="list-style-type:disc">Lockout</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e9c5e6f-95bd-80bd-9c8d-c24115212f0b" class=""><strong>7.2 Luật cấp Boost (hard logic)</strong></h3></div><div style="display:contents" dir="auto"><p id="2e9c5e6f-95bd-802b-930d-f9f3830d49ce" class="">Boost chỉ được phép khi <strong>TẤT CẢ</strong> điều kiện:</p></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80ab-be0c-efa215a36e4f" class="bulleted-list"><li style="list-style-type:disc">Thermal headroom OK</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80de-b5c8-f4133a46acde" class="bulleted-list"><li style="list-style-type:disc">Gradient nhiệt thấp</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80b0-9a83-c5e0c6d38109" class="bulleted-list"><li style="list-style-type:disc">Áp suất ổn định</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8005-8ec5-f559bc9dcfc6" class="bulleted-list"><li style="list-style-type:disc">Không có fault gần đây</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8053-87df-e0c0b2cffc02" class="bulleted-list"><li style="list-style-type:disc">Drift điện trở trong giới hạn</li></ul></div><div style="display:contents" dir="auto"><p id="2e9c5e6f-95bd-808a-97ec-f646a702e903" class="">Nếu <strong>1 điều kiện fail → từ chối boost</strong></p></div><div style="display:contents" dir="auto"><hr id="2e9c5e6f-95bd-80f5-abab-db478fb235b3"/></div><div style="display:contents" dir="auto"><h2 id="2e9c5e6f-95bd-8032-b68b-c7d9f05180a6" class=""><strong>8. Tiêu chí kiểm chứng (Verification Targets)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e9c5e6f-95bd-802a-bee8-d00b5ccacc5b" class=""><strong>8.1 Điện – hoá</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8097-828e-d7d0aa72db6a" class="bulleted-list"><li style="list-style-type:disc">Hiệu suất Faraday ≥ xác định</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8086-b204-fc75d2dc03fd" class="bulleted-list"><li style="list-style-type:disc">L/kWh ổn định qua thời gian</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e9c5e6f-95bd-80d3-b040-c1c316e4bc5d" class=""><strong>8.2 Độ bền</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8077-9fa7-f7cd5ff11c88" class="bulleted-list"><li style="list-style-type:disc">Test ≥1.000 h chạy liên tục</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80f8-a811-cc68b721f3a9" class="bulleted-list"><li style="list-style-type:disc">Test start/stop chu kỳ ngày</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8005-b92a-d61fc4ffb4e7" class="bulleted-list"><li style="list-style-type:disc">Test boost lặp có cooldown</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e9c5e6f-95bd-807c-b97c-e16b17004721" class=""><strong>8.3 Vận hành</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80df-8b4d-cd3c45881074" class="bulleted-list"><li style="list-style-type:disc">Alarm rate thấp</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8083-b06f-dfbd2b71ca02" class="bulleted-list"><li style="list-style-type:disc">Không cần “canh máy”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8046-a6cc-c4ce14736604" class="bulleted-list"><li style="list-style-type:disc">Derate diễn ra êm, không shock</li></ul></div><div style="display:contents" dir="auto"><hr id="2e9c5e6f-95bd-8015-9bf6-d92db9a28fe7"/></div><div style="display:contents" dir="auto"><h2 id="2e9c5e6f-95bd-8078-a4d6-f60fbfda4b44" class=""><strong>KẾT LUẬN KỸ THUẬT (Technical Conclusion)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e9c5e6f-95bd-806d-92bd-fb29a8336de6" class="">Bản tái thiết kế này <strong>không thay đổi hoá học</strong>, <strong>không phá luật Faraday</strong>, <strong>không vượt thermodynamics</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e9c5e6f-95bd-80c1-8be9-ffc26d40a375" class="">Nó làm 3 việc rất kỹ thuật:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e9c5e6f-95bd-80b4-b2d1-cb30f2baf7f4" class="numbered-list" start="1"><li><strong>Ép toàn bộ hệ thống tuân theo dòng (current)</strong> thay vì áp.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e9c5e6f-95bd-80af-b6df-f34c094d9a0f" class="numbered-list" start="2"><li><strong>Dùng Cannon để shape quá trình điện hoá</strong>, không “đánh mạnh”.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e9c5e6f-95bd-802f-b36c-f85b5002bb0c" class="numbered-list" start="3"><li><strong>Chuyển giới hạn từ “cắt khẩn cấp” sang “derate thông minh”</strong>.</li></ol></div><div style="display:contents" dir="auto"><p id="2e9c5e6f-95bd-8096-aaf1-eeb75af128d9" class="">Đó là lý do nó <strong>thực sự tốt hơn</strong>, chứ không chỉ “nghe hay”.</p></div><div style="display:contents" dir="auto"><p id="2e9c5e6f-95bd-80fa-ba57-dc9247652288" class="">Nếu bạn muốn bước tiếp:</p></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8010-a10f-c1aec4c7aff0" class="bulleted-list"><li style="list-style-type:disc">mình có thể viết <strong>pseudo-code điều khiển Cannon</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-80dd-b350-d50801d5f2e8" class="bulleted-list"><li style="list-style-type:disc">hoặc <strong>sơ đồ mạch power stage</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e9c5e6f-95bd-8069-b0b2-ef72b92f7039" class="bulleted-list"><li style="list-style-type:disc">hoặc <strong>bản spec so sánh với PEM thương mại</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2e9c5e6f-95bd-8003-a7a3-edfd037877b8" class="">Bạn chọn hướng tiếp theo.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
