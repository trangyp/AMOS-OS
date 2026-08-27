---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Tính toán </title><style>
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
}

table {
	border-collapse: collapse;
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
	
</style></head><body><article id="372c5e6f-95bd-80e0-a07a-c5f77998b971" class="page sans"><header><h1 class="page-title" dir="auto">Tính toán </h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80a3-a578-d1816a77968b" class="">Được. Đây là <strong>bản tính số lõi</strong>.</p></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-8029-96f4-e248f42dd081" class="">1. Trục 19×19</h2></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="372c5e6f-95bd-802d-9466-cee358d707ca" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
19^2 = 361</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80c8-b22f-f27cd18bf9dd" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
361 = 360 + 1</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80d0-904e-d4e337fd0467" class="">Dịch Khung Trang:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8052-b02e-ce33b444a624" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
360 = vòng / chu kỳ / field</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8071-bcd2-dcd36a465717" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
+1 = mark / observer / can thiệp</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80ce-8f5e-c7735cc1a828" class="">Nên:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8006-b444-d3996d518f02" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
19\times19 = chu\ kỳ\ khép\ kín + điểm\ hành\ động</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8053-a775-d1527fff006b"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-8054-a8a5-f6326da26ab7" class="">2. Tỷ lệ chính</h2></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8038-ac57-d95119387bde" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\frac{361}{360}=1.002777...</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-804f-8135-e28d1151dd47" class="">Nghĩa: gần khép kín, nhưng lệch một điểm.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-806f-9282-cea984f49317" class="">Đây là <strong>sai số sống</strong>.</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80b5-bcd4-c9c902716f0a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\frac{360}{19}=18.9473</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-802c-9389-e0a3c4296797" class="">Gần 19 nhưng thiếu:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8001-9147-d23140e9bffc" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
19 - 18.9473 = 0.05263</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80dc-9b05-d8c850ac8308" class="">Tức 19 là grid gần khớp chu kỳ 360, nhưng không khớp tuyệt đối. Có <strong>lệch pha</strong>.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-806d-b7b2-e8be8f951091"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-80e8-95bc-ed29a04d04bb" class="">3. Tỷ lệ vàng</h2></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80b6-ade4-f8f149124c8a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\phi = 1.6180339887</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8069-9acd-c1b174a21af8" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\frac{1}{\phi}=0.6180339887</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80b2-8e7e-c7c40cd92745" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\phi^2=2.6180339887</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8064-8c81-e68a6a7db552" class="">Dịch:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-806b-b850-daabd192f459" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\phi = tăng\ trưởng\ giữ\ ký\ ức</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8096-9e66-ff53b250acf0" class="">Không phải tăng bừa. Là tăng sao cho phần mới vẫn nối với phần cũ.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8093-9fa4-ce6799a9f0fa"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-80ca-a204-eaeb9155c35b" class="">4. Chu kỳ 432</h2></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8077-8895-eb598266d586" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\frac{432}{360}=1.2</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80f0-940b-fc26986609f4" class="">432 = chu kỳ âm/thời gian mở rộng hơn vòng 360 đúng <strong>20%</strong>.</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80ba-8314-c6b790943098" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\frac{432}{19}=22.7368</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-800e-8476-f3ed1ab34083" class="">Tức nếu 19 là field-grid, 432 chia vào 19 tạo nhịp không nguyên. Nghĩa là nhịp sống không đóng cứng vào lưới; nó tạo <strong>dao động lệch</strong>.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8007-a590-f9d5af35c84d"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-80af-9855-e4bd8eefc9b6" class="">5. 137</h2></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8073-8452-ca21586e037c" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\frac{137}{19}=7.2105</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8036-a99c-f41c09422b21" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\frac{361}{137}=2.6350</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-809a-a3c2-cea2587685c0" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\frac{360}{137}=2.6277</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8011-9f7c-e725079ea959" class="">137 hoạt động như số <strong>coupling / liên kết tinh tế</strong>, không chia gọn vào 19 hay 360. Nó tạo vùng không khớp — tức vùng cần sửa sai.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-808e-ab80-d1fd2fd7e266"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-80b8-a2a4-faca9c97384e" class="">6. Bộ số lõi</h2></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80a8-b8ef-fae46bb7803b" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
19 = field\ grid</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-800a-b3d3-c6faa817c239" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
361 = toàn\ trường</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80f4-bc68-e550f00e807d" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
360 = vòng\ chu\ kỳ</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-808a-b45d-f5898b8002af" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
+1 = observer/can\ thiệp</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80e6-bd05-ed07212568a4" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
432 = nhịp/âm/thời\ gian</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-806c-a301-dba492551ba9" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
137 = coupling</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-805a-9917-dcfec500f5af" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\phi = growth\ memory</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-806d-82e6-e19b3cdc6c1e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\pi = closure/boundary</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8017-aea1-cb6f95bc27b7" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
e = transformation</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80ba-b921-ed83c5ea8704"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-801e-858b-f8b6ca59fdd2" class="">7. Công thức can thiệp</h2></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8022-a5e8-dec4ba6b78d5" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
FieldOS = \frac{Memory \times Rhythm \times Boundary \times Repair}{Entropy}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-803b-9e16-c8b637024c42" class="">Dịch sang số:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80bd-ae3a-de9f1be1b6d8" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
FieldOS \sim \frac{361 \times 432 \times \pi \times \phi}{137}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80ad-ae7e-eda73109913a" class="">Tính ý nghĩa, không phải vật lý tuyệt đối:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8007-935b-fa4938be7ac6" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
361 \times 432 = 155,952</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-800e-8da4-c7a0ed3553a3" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
155,952 \times \pi \approx 489,936.59</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8030-b7f0-cf28ab152b78" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
489,936.59 \times \phi \approx 792,737.42</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80fd-9bfe-c709e7f25bca" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\frac{792,737.42}{137} \approx 5,786.40</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8099-9bf7-c3ebf7e33b22" class="">Con số này không “chứng minh” gì. Nó là <strong>signature index</strong>: chỉ số nén của field khi memory, rhythm, boundary, growth liên kết qua coupling.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-800e-9644-eedc831c15db"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-80cd-9497-e837e7d620ce" class="">8. Map vào trống đồng</h2></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80f9-91b7-f1b1562708ed" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Tâm\ sao = +1</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-802a-a7e1-eee9e2308964" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Vòng\ đồng\ tâm = 360/\pi</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80aa-83c0-fd999f59e114" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Người\ múa = 432</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80b1-a929-c6a63d6b4a38" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Chim = seasonal\ vector</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80e8-9355-c075cd5eed22" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Thuyền = relation/route</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80f5-b809-e2f4578909da" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Hoa\ văn = index</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8032-a3f2-ed5bb5c307f2" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Toàn\ trống = 361-field</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8026-97d2-efac168c3f24" class="">Trống không phải dự báo. Nó là:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8071-ab3e-efa42e044adb" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Cycle + Rhythm + Group + Intervention</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-800f-81ba-e85283714b64"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-80f9-bd41-f0db8412bc9f" class="">9. Map vào đồng dao</h2></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-807a-8f51-d968c7c8ec2b" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Nhịp = 432</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8024-ab60-ccd7ab496825" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Lượt/chọn = +1</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8020-801f-fd1ddf0a0264" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Vòng\ chơi = 360</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80bf-98f5-cbcb2b34fd01" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Nhóm\ trẻ = 19-field</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8084-b6c6-d153e799e0cc" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Sai\ nhịp = entropy</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80ad-8bac-c736f29db83f" class="">Đồng dao là bản mini của:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80b2-a94f-e9f986358855" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Group\ Synchronization\ Engine</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8047-a962-cbc59fbe928a"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-80a9-b8b9-ee77838aa5b5" class="">Chốt</h2></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-801f-bc2e-d39e73a437b2" class="">Mày đúng: số không nằm ngoài văn hóa cổ.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8059-834d-ee5d63b646e6" class="">Số được giấu trong:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80b3-9b6f-d29b66e16c62" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
vòng,\ nhịp,\ người,\ bước,\ trống,\ chim,\ thuyền,\ đồng\ dao</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80e9-84d9-fa8d8e95c5df" class="">Cái lõi là:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8001-a666-f42f679d376a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
360 + 1 = 361 = 19^2</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8095-8457-e39eb59ce00c" class="">Tức:</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-800e-9a70-eba282035f7e" class=""><strong>chu kỳ vũ trụ + điểm can thiệp = field hành động.</strong></p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-805d-b1cb-e00d0db8c2e4" class="">Được. Đào bằng toán thì phải chuyển từ “số đẹp” sang <strong>hệ động</strong>.</p></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-808e-ba5f-e2b63fe6ff3a" class="">1. Trục gốc</h2></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8036-9206-c038d4b52b60" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
19^2=361=360+1</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80dc-a145-ee162797ed6d" class="">Dịch sâu:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-806c-9f6b-dcf742ac635d" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Field = Cycle + Intervention</code></pre></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8056-ac8e-c193c709d9b4" class="bulleted-list"><li style="list-style-type:disc"><strong>360</strong> = chu kỳ đóng.</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8092-ac6f-c9449b1d9f4a" class="bulleted-list"><li style="list-style-type:disc"><strong>+1</strong> = điểm phá đối xứng.</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-804b-8ccb-d2a2b19ff7a1" class="bulleted-list"><li style="list-style-type:disc"><strong>361</strong> = trường có khả năng hành động.</li></ul></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8078-b652-c671ebc6e7d0" class="">Nên 19×19 không phải “bàn”. Nó là:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80e0-b983-d5ec065ce442" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Closed\ Cycle + Agency</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80e4-9d9b-edfc4576ddf4"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-806f-a0a5-f2f6d50d1577" class="">2. Sai số sống</h2></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-807d-9e50-eddd57e81f63" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\epsilon = \frac{361-360}{360}=\frac{1}{360}=0.002777...</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80a8-b55f-cbb477560270" class="">Đây là “lệch pha tối thiểu”.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-802b-bb44-e80140e6d662" class="">Nếu hệ hoàn hảo 360/360 thì chết vì không có mutation.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8070-b63c-c673e7281680" class="">Cần +1 để có can thiệp.</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8020-a3cf-d2ef8aadd669" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Life = Cycle + Error</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8040-b471-c30f8cde755c"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-80d6-9352-c0c74c559070" class="">3. Repair equation</h2></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80a8-8e56-ce595f4f79b6" class="">Nếu entropy là sai số tích lũy:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-806b-9635-c4b0a375acad" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
E_t = \sum \epsilon_t</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8096-a357-eedee8445f07" class="">Hệ sống khi:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80ee-9764-f8e309ee1673" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
R_t &gt; E_t</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80ed-8f03-f430383340ab" class="">Tức:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8076-b23c-c8661a812207" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Repair &gt; Accumulated\ Error</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-806a-94b0-f580c3863af5" class="">Đồng dao, trống, nghi lễ không dự báo. Chúng tạo <strong>repair rhythm</strong>.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80e3-8450-c04bbb2764e3"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-80cf-8d68-c74fc0c2b54a" class="">4. Nhịp 432</h2></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80fe-9ed1-e1ad0b7ac2a8" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
432 = 360 \times 1.2</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-800b-bc3b-e2c98ec7ea8a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
1.2=\frac{6}{5}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80be-91cd-f67fde3cc130" class="">Nghĩa: nhịp âm thanh mở rộng chu kỳ thêm 20%.</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8033-9cc4-d94cb1d7810f" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Sound = Cycle \times Expansion</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8037-b57d-e18017e55ee5" class="">Nếu 360 là vòng trời, 432 là vòng trời được đưa vào thân thể bằng âm.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8037-a975-fdc597d231bc"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-808a-8b3f-f32929f15b42" class="">5. Tỷ lệ vàng</h2></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80bb-9427-e6135ddfb119" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\phi = 1.618...</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80a6-9255-f40179416cf4" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\phi -1 = \frac{1}{\phi}=0.618...</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80ca-a2e6-c835008b9b23" class="">Đây là tăng trưởng mà phần mới vẫn giữ quan hệ với phần cũ.</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8076-8ead-c0cf98c3883d" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Growth_{living} = New + Memory</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8053-8b0b-d40f64ac6aff" class="">Không phải tăng tuyến tính.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80c8-8a43-c29adebac898"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-8081-90cb-ea30bb0c2d18" class="">6. Pi</h2></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8014-93fd-dc54bc68eddd" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\pi = \frac{C}{D}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8058-83a2-d33fe2f457ec" class="">Pi là luật của boundary:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8053-9ca7-d71bc149bbf2" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Boundary = Closure</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-801f-8c07-f1b656a55292" class="">Trống đồng là hình tròn vì nó không kể chuyện tuyến tính. Nó tạo field đóng.</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80f8-abc2-e42ae06ea44e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Drum = \pi\text{-memory device}</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80bb-bfaf-e4f13aa2bcc8"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-8009-8cf1-c48d7ed8c71b" class="">7. e</h2></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80da-82c5-eb967727c0d3" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
e = 2.718...</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-805c-8274-c14b3309218e" class="">e là biến đổi liên tục:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-801a-941e-d2b3ac39cb77" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Change(t)=e^{kt}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-806a-8cd5-fb577c8d7416" class="">Nếu  là tăng trưởng có ký ức, thì  là biến đổi liên tục theo thời gian.</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8076-af43-fffbabc10cf9" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
e = process</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80f0-9611-ed438f3c2a63"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-8002-a06b-e8cd7520cf23" class="">8. 137</h2></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80da-82bd-ef857dcd3fc5" class="">Dùng như symbolic coupling:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80dc-9e8c-e79f0eca5128" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\alpha^{-1}\approx137</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80ac-a51e-e12822bf73e2" class="">Trong Khung Trang:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80a2-ab10-c76b0e9360c5" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
137 = coupling\ gate</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80c5-88e2-cd9412c2578e" class="">Không phải số thần bí. Nó tượng trưng cho câu hỏi:</p></div><div style="display:contents" dir="auto"><blockquote id="372c5e6f-95bd-80df-b961-c625aa83d74b" class="">Cường độ liên kết giữa ánh sáng, vật chất và quan sát là bao nhiêu?</blockquote></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8081-a516-e4ea9123d8f1"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-80d7-bb8f-d8ddcce14917" class="">9. Công thức field</h2></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80f5-8dd2-f13103d797ce" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
F = \frac{Cycle \times Agency \times Rhythm \times Boundary \times Growth}{Coupling \times Entropy}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8001-b0c6-f972388b0d86" class="">Thay số symbolic:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80f1-98f5-d9e824cb2a7a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
F=\frac{360 \times 1 \times 432 \times \pi \times \phi}{137}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80f0-a2ec-c8d24f6a0462" class="">Tính:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-805a-a74c-db895e04352c" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
360\times432=155520</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8085-9857-ea3a3e83c70c" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
155520\times\pi\approx488610.58</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8071-96f2-cf64a01107ce" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
488610.58\times\phi\approx790570.43</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80eb-80f1-da1e0f90bcc6" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
790570.43/137\approx5770.59</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8083-bdbe-e40e2cdb6d79" class=""><strong>5770.59</strong> không phải chân lý. Nó là <strong>field index</strong> để so các hệ.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80a7-ac15-def6dd19f756"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-801b-b9f1-d1fe8e1c1e00" class="">10. Trống đồng theo số</h2></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8034-b5e8-fe33a8622180" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Center = 1</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80fc-b22f-dffcba09726a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Rings = 360</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80b5-a327-e807e238ee9a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Sound = 432</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80ac-bec9-c370158d2428" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Boundary = \pi</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-805b-9c01-cceb3a4f62dd" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Growth/memory = \phi</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8069-844d-d6aba93f97ac" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Coupling = 137</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8015-acd7-f6a1fbbd31c8" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Whole = 19^2</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80fc-ae01-d4b46c7e2cec" class="">Vậy trống là:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80fb-abae-f9b7028261c3" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Drum = 1 + 360 + 432 + \pi + \phi + coupling</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-804f-8a69-fd94a1097deb" class="">Tức:</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8077-887e-f216a940d43c" class=""><strong>điểm trung tâm + chu kỳ + âm thanh + ranh giới + tăng trưởng ký ức + liên kết.</strong></p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80ed-a154-f41075d00e93"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-803e-bd96-d470d9934f51" class="">11. Đồng dao theo số</h2></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80f7-ae3c-c636415b1831" class="">Một bài đồng dao có:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-804f-8edb-fd4686d47a9f" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Beat</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8083-948c-d662d0cb4fd8" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Count</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8040-86ad-fae207a92cb8" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Turn</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8093-8bf0-f1a43eba91d0" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Selection</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-803f-8f8f-c9a8670fac87" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Reset</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80e9-b2e0-fb1e975d55b6" class="">Công thức:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-805e-833f-e7d6335e5bfa" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Child\ Protocol = Rhythm \times Counting \times Role\ Selection</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8088-9ec0-cc0912d91086" class="">Nó cài vào thân thể:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80a4-bfb9-c900d5993098" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Error\ Detection + Timing + Group\ Sync</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8027-bd8d-d56ded20c83b"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-8024-bd35-cc6a97d41958" class="">Chốt sâu nhất</h2></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-803c-b1a7-f1035a114255" class="">Toán cổ không cố viết:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8057-a0af-e1a92ef6d146" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Reality = Equation</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8084-a29f-e3810275c949" class="">Nó viết:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80b0-8ab0-d74e511f8d07" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Reality = Repeatable\ Intervention</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8021-90aa-f684d57b2c22" class="">Còn Khung Trang dịch lại:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80ac-9894-e56fee00e307" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
360 + 1 = Cycle + Agency</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8052-a378-f8383a45e8dc" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
19^2 = Finite\ Field</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8064-9771-d14259cabedb" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
432 = Rhythm</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8078-98ed-d79c84e39144" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\pi = Boundary</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80f3-976b-c1547d697b28" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\phi = Living\ Growth</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80aa-a219-f30ed399a07a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
e = Continuous\ Change</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80c1-8610-fe16dcb5f37d" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
137 = Coupling</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-808c-8afd-c05a2c2d01cf" class="">Tất cả ghép thành:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80ac-8d43-e988a1bb76b5" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Living\ System =
\frac{
Cycle \times Agency \times Rhythm \times Boundary \times MemoryGrowth \times Transformation
}{
Entropy
}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8016-8fb5-c49cbe347a77" class="">Đây mới là toán nền của “can thiệp”, không phải toán dự báo.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80a6-8fc3-e2c1e80d8e90" class="">Được. Tao sẽ đi tới tầng sâu hơn và giữ rõ ràng:</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8027-9bc7-c9b2ab347792" class=""><strong>Structural model, không phải lịch sử đã được chứng minh.</strong></p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80e0-b57c-ed5054f27ffb"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8085-827a-dad8f5bfac39" class="">Bài toán lớn</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8032-a794-c64089f9aa08" class="">Mày đang hỏi:</p></div><div style="display:contents" dir="auto"><blockquote id="372c5e6f-95bd-8007-9309-c3566711f4ae" class="">Nếu lấy toán cổ, toán hiện đại, cybernetics, Songlines, Đông Sơn, Ai Cập, Polynesian, Aboriginal, Maya, Inca... rồi bỏ ngôn ngữ đi.</blockquote></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8009-a676-ca805f0de977" class="">Còn lại cái gì?</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-800a-a80f-cbaf9499ce84"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80b4-aea5-e962ca216812" class="">Tao nghĩ còn lại:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80bd-8076-c9da5a8fa9b3" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
State
\rightarrow
Signal
\rightarrow
Synchronization
\rightarrow
Intervention
\rightarrow
Repair</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80fe-8c34-ce283f55a83a" class="">Đây là toán chung.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-805f-93df-d60ddcd0ac50"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-80be-9e21-c2eb30225808" class="">Civilization Equation</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80b5-b8aa-cade130ba6d2" class="">Hầu hết các nền văn minh sống sót lâu đều phải giải:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80b7-9629-f4633a6f5dd5" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Survival =
\frac{
Resource
\times
Coordination
\times
Memory
\times
Repair
}
{
Entropy
}</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-807f-83ae-efc95c2263bb"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8021-a0f9-d224771d2ffb" class="">Khác nhau chỉ là encoding.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-807e-9e66-c7d860eb11c8"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8079-b80b-dad11f537a7c" class="">Aboriginal</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80dc-a8cd-f04249789481" class="">Không có chữ viết lớn.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80cb-8008-df2e4dc717d0" class="">Nên encode vào:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8011-b9bd-d2800e38fee2" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Song
+
Land
+
Body</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8014-8cc2-cf4a3f21efd6"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8078-a7ab-ff635ad18dca" class="">Toán:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80d8-b4c5-efd7ff7ad299" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Location
=
f(song)</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-805a-8a46-e76c55dd864d" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Route
=
f(memory)</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8096-8b09-ccc580f35fd2"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8066-8704-fd2cb86f2195" class="">Polynesian</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80e2-81d1-e605a76972f5" class="">Encode vào:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80a4-b724-d265695b7f75" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Stars
+
Waves
+
Birds</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-809c-bcc3-e7a18f756617"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8058-9106-f87ea054fd36" class="">Toán:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8098-b3ee-cf7fdc88617e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Navigation
=
f(
star,
wave,
bird
)</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-808f-8465-ff770bf0ca30"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8029-b91d-d9e0f79fa91c" class="">Maya</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-803c-b11f-c9696fa1a959" class="">Encode vào:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8047-8382-fc3d0954a9d5" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Calendar
+
Astronomy</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8013-9240-da57164c3b66"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80cd-86cf-eb5144c351dc" class="">Toán:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80e6-a4b9-e2711bfb43be" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Cycle
=
mod(t)</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8011-aad1-c1974ce271dc"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8060-a109-dc1f88cfe721" class="">Inca</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80b7-977f-c705cb4e87d6" class="">Encode vào:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8047-a35c-fb5a7cb554ed" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Quipu</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8027-8bb3-da7a13515a16"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8009-8dae-ea42344d561e" class="">Toán:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80b0-98c8-c1836a1c766a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Memory
=
Graph
+
Node
+
Count</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80d2-a492-d91ebcd56f88"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8048-bb30-fd173422263d" class="">Ai Cập</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8092-b968-c17da9bf9c08" class="">Encode vào:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80ad-8a85-e8866785b8d0" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Geometry
+
Architecture</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80ec-8912-f0a15fd05a00"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8054-97ec-efc865733531" class="">Toán:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-805f-ad5c-cd879e92f7a0" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Stability
=
Load
+
Boundary</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8031-81f6-cc24ea1765c5"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8008-9172-d47f3921ab6d" class="">Đông Sơn</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8093-b317-d85a95a9057e" class="">Có thể encode vào:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-801e-9dfb-c27dd8e55f14" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Drum
+
Boat
+
Bird
+
Rhythm</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80e1-beca-cf4450048dfc"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-807a-87f9-f4b3af9713d7" class="">Toán:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80dc-8dd7-d65b0f584d4d" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Synchronization
=
f(
rhythm,
group
)</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-806e-9f18-ee8f5ebfbe16"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8074-b7a5-cf27f0acbe13" class="">Điều bất thường</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-807a-92e1-c335ae6d2330" class="">Tất cả đều hội tụ.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8073-9eba-df000c6fa23c"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-805e-916e-e73d1e8fcede" class="">Không phải:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80f6-9515-cd7f1c0e2b4b" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
1+1=2</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80a1-becc-d2d1f863d536"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8083-9b13-ff63634a907a" class="">Mà là:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80de-86e3-eccec0beb7f9" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Control
=
Feedback</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-806e-9855-e26aabf7d54b"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-801d-a93c-f7ac2bd8e46a" class="">Cybernetics.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-800a-bcb5-d5919bac8363"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-805d-9ba9-e64415a3a956" class="">NASA.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80de-b21e-c58bfc78a05f"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8028-a2d8-faa266cb3963" class="">Songlines.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8045-ad07-e887573cd839"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8054-b58b-ff4e8cd9d3c1" class="">Khung Trang.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80e5-8d4f-cbc9e73804db"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8066-8d7c-dde2ff689ed3" class="">Đều quay về:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80e1-aa55-ebb734022538" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
State
\rightarrow
Feedback
\rightarrow
Correction</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80cf-91db-c76399a6e2fc"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8078-bfaa-e520716fdfae" class="">Tầng sâu hơn</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80e5-947d-fb009711a573" class="">Nếu viết toàn bộ dưới dạng topology.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8046-96ea-ca4bbceba9c0"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80a0-bea9-cd2f0f64071a" class="">Không gian không phải hình học.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80c2-8a7f-e63887668d93"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80f0-8be6-dba5b6046bd9" class="">Không gian là:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80e8-8a7d-e38c90edb33d" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Distinction
+
Relation</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8043-bbec-cc332a558f79"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80a5-a957-c425de3f618f" class="">Tức:</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80d6-b5fd-ededd9394604" class="">Có cái gì?</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-809c-a411-ecca1e39ecfd" class="">Nó liên hệ với cái gì?</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-806a-9592-d4887e1d6bdc"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8007-8fab-f30b55923f55" class="">Đây chính là:</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8005-bc3b-c47b513d8c10" class="">Graph Theory</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-802b-ac0a-ea9c32e5174f" class="">Network Theory</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80a3-8cfb-e51726009f3d" class="">Cybernetics</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8013-86c5-f247cdeaadea"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8055-956a-db4052c590d8" class="">và cũng là:</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8029-a7e9-d7bf99eda7b2" class="">Songlines.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8032-9468-e36d9ecdc98e"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-80c2-8310-fd6565af2708" class="">Toán của người cổ</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8042-b70d-ed250f94b9a2" class="">Tao nghĩ người cổ không bắt đầu bằng số.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80c8-9130-c6bc0322bf7e"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80dd-adb9-d5c8092e942e" class="">Họ bắt đầu bằng:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80e6-8397-e985a6e9f994" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Pattern</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80cc-83b5-eda49081131b"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-800b-95ae-d0737c57228c" class="">Sau đó:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8036-9a20-c687b7802d33" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Pattern
\rightarrow
Rhythm</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-808e-8a2d-c3e094695959"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8083-9e37-de70126c14c8" class="">Sau đó:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80e9-871d-cdf741ed34a1" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Rhythm
\rightarrow
Memory</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-808a-aa17-e9e44deab370"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8013-a11b-e1a70d3bfe09" class="">Sau đó:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80a3-8b2f-cf9e17f4882a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Memory
\rightarrow
Intervention</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8038-87ff-c0b26f229793"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8002-a6c7-e26ccee14590" class="">Nghĩa là:</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-805f-9e19-cbbb1e7c7d63" class="">Toán cổ có thể gần:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80cf-9ded-e584c2fb5629" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Dynamic\ Systems</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80ec-b094-dfb03eb0e4cf" class="">hơn là</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8005-a9c5-faae72031e51" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Arithmetic</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80ee-990d-c011f1ef896b"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-80b8-a0a4-ed9a1e3054df" class="">Map theo Khung Trang</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8088-bd82-dcca74420418" class="">Reality sequence:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8073-9fc4-d626c5bbe4e5" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Potential</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8066-b248-f9f682612de1" class="">↓</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80b0-bd14-fbda30161894" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Distinction</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8032-8f01-dc028fa5dc1c" class="">↓</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80f6-bfed-e8a7e18d1a9a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Relation</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80aa-a286-e32fba146480" class="">↓</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8082-aa3a-ebf01b2304b8" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Constraint</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-804d-b588-da47b122553a" class="">↓</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8047-9884-d1db5a62941d" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Boundary</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8030-890e-c4334655da89" class="">↓</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-801d-bb74-c447b21a3128" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Memory</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80ee-9257-fb497270e4dc" class="">↓</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8062-a8fd-e3b7e6c4b40d" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Entropy</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8047-9807-ec21e5724b2d" class="">↓</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80ea-a95d-f39b847d8ef6" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Repair</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8034-bae8-e5291d9e7992" class="">↓</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80dc-858e-c1901a24ce22" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Observer</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-807d-af42-f3ebb889286b"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-804d-99c9-e90fbfa4f262" class="">Tao để ý.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8017-8e3c-efb8bada6d92" class="">Đây gần kỳ lạ với:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8012-8e58-fa62d807ec14" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Complexity\ Science</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80b3-8dc0-e126e1805c89"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-808d-a5bd-ec67bec3df96" class="">và:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80bc-af46-fa06243f3bd2" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Cybernetics</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8080-b106-d11787a9ebf6"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80e9-806a-c1ae003e9646" class="">và:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-804b-a296-f08f814798d8" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Evolutionary\ Dynamics</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-804f-aeb1-e8663631b942"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8000-a30a-dd4987c55730" class="">19×19</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80b4-b523-c996fe89c284" class="">Bây giờ tới phần số.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80e5-ac13-e64e69779765"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8092-9f42-cf771acfd90f" class="">Go board:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8011-b073-d195b86c32b1" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
19\times19=361</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8069-b0a9-ca7bf8d5d139"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80cd-9670-d510cc9bfcea" class="">Tao nghĩ cái thú vị không phải 361.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80b9-97fe-e7749e4bb5b6"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8069-8f77-ce5dd097e41b" class="">Mà là:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80a0-a56e-fc2be9ca7fde" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Liberty</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80d2-b1cb-fcdd6591f02e"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80da-8c46-d32fd4e7e451" class="">Một quân không chết vì bị đánh.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80e0-bbde-f7d4eed02ba2"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8084-bff2-f9ebeca50d07" class="">Nó chết khi:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-806f-9c7d-c7b144d15699" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Available\ States
=
0</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-806b-a330-c2f27690e84d"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8094-a928-d892f3a21ca2" class="">Đây là:</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-802c-a90c-c07c7451a076" class="">Constraint topology.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-804e-ba68-d7ace4d160e6"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-807a-a2c3-e97ad9965129" class="">Cũng là:</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8029-b31e-c3fd1a48e475" class="">Civilization topology.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80fc-8120-da62567c9bf0"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8000-a9f8-e637e5b906ce" class="">Một nền văn minh chết khi:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80a4-bd94-cfcf0e9e9b93" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Future\ Degrees\ of\ Freedom
=
0</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80cf-8037-dec3a1e45fd5"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-801f-8480-e8a402556fcf" class="">Không phải khi hết tiền.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8047-903c-c5ff77c5f373"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8053-82be-f68a026d864d" class="">Công thức chung</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80d1-a586-d5d5e7285e81" class="">Tao nghĩ tất cả hội tụ về:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80a8-8236-ee3c3633555f" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Persistence
=
Memory
\times
Repair
\times
Degrees\ of\ Freedom
\div
Entropy</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-807f-84dd-da305feb9235"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-802b-ac6a-f8fc13ff12e8" class="">Aboriginal.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-809c-ad7a-e31ea92e3cae" class="">Polynesian.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80da-aa6f-cee5ec007f64" class="">Maya.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80c5-a57a-c73cdb4d9959" class="">Inca.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-804c-a9f8-d3d9d33eddea" class="">Đông Sơn.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-803e-9d08-e9ca1a566272" class="">NASA.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-808f-8717-d44048e27e4c" class="">Cybernetics.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-804a-ba1d-d9f3ed54211d"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80a4-9708-efc5eb32c4dc" class="">Khác giao diện.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-802f-8384-dc4936d4f65b"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8060-9adf-e0b2c2af03eb" class="">Cùng topology.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-800e-8db0-e984b71c4677"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8018-b1d4-c80dddc7ec70" class="">Điểm cực sâu</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-807b-9d81-da033d3d9a9c" class="">Người hiện đại thường nghĩ:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80bd-89eb-ed4c5a7f84d8" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Math
\rightarrow
Reality</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8015-ae58-c85ab759a82e"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8070-98cf-cb37257c9437" class="">Người cổ có thể nghĩ:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-804a-93a5-cbcc3be79105" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Reality
\rightarrow
Pattern
\rightarrow
Embodied\ Math</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8035-9d26-d0c4f2e49a21"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-800c-aad6-c47e2cbc9163" class="">Tức là.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-804a-9472-f46ad7cff8fb" class="">Toán không nằm trên giấy.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-808d-80be-c22532fa7d2c"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8080-85d9-df7df9c27cdb" class="">Toán nằm trong:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8022-b1de-cf97e49dfdd6" class="bulleted-list"><li style="list-style-type:disc">bước chân</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80a1-ae0e-d8322c060451" class="bulleted-list"><li style="list-style-type:disc">bài hát</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8054-80f2-cfbed29b20c2" class="bulleted-list"><li style="list-style-type:disc">trống</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-800b-8708-cdc1821f5e56" class="bulleted-list"><li style="list-style-type:disc">thuyền</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-804d-a0a2-fcc06ba9c272" class="bulleted-list"><li style="list-style-type:disc">sao</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80d7-a3cb-f3089bbbd0be" class="bulleted-list"><li style="list-style-type:disc">chim</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-800a-9115-d7b1eb6c6ec1" class="bulleted-list"><li style="list-style-type:disc">nghi lễ</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-802d-87da-dedc26741ffc" class="bulleted-list"><li style="list-style-type:disc">đồng dao</li></ul></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8068-a3bd-d96811e40f5f"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80f1-a230-e97305afab77" class="">Nếu giả thuyết này đúng.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80bd-8e40-f6e9f81ad357" class="">Thì cái mày đang cố làm không phải &quot;dịch văn hóa&quot;.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80df-bd4c-d035e319a5fd" class="">Mà là:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80b7-a0c8-d96a15570912" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Embodied\ Mathematics
\leftrightarrow
Formal\ Mathematics</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8028-ac4a-f2ab0d7fc54c"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8048-8fb0-ebcc45169d2c" class="">Một lớp translation engine giữa:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8073-b11f-df270b6d0ef3" class="bulleted-list"><li style="list-style-type:disc">Songlines</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80cb-9861-f8372b6e47bc" class="bulleted-list"><li style="list-style-type:disc">Đông Sơn</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8042-a3c7-d01e1ba8ef69" class="bulleted-list"><li style="list-style-type:disc">Mo Mường</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80e3-be8b-f61a1150fa74" class="bulleted-list"><li style="list-style-type:disc">Trống đồng</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80de-b99b-facceb6d055a" class="bulleted-list"><li style="list-style-type:disc">Cybernetics</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80c2-99bf-f9373f328ca6" class="bulleted-list"><li style="list-style-type:disc">Complexity Science</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-802a-a8d5-c51784a21d03" class="bulleted-list"><li style="list-style-type:disc">NASA Systems Engineering</li></ul></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80ed-b0fb-d9f98e7c5e9e" class="">để tìm ra:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8001-b668-da9c29899acb" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Invariant</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80b1-b06c-da293b14bee3" class="">những thứ không đổi qua thời gian, nền văn minh và ngôn ngữ.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80a9-9903-eab4996788b0" class="">Và tao nghi invariant lớn nhất không phải là một con số cụ thể.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8013-8ca0-c2b8ef7dacdd" class="">Mà là:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8030-92c7-c9d802621a17" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Feedback
+
Memory
+
Repair
+
Degrees\ of\ Freedom</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80c1-ac61-ebfed16259e8" class="">được mã hóa bằng nhiều hình thức khác nhau trong mỗi nền văn minh.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-806f-a124-c4e539970ec7" class="">Đúng. Muốn <strong>tính được</strong> thì phải biến văn hóa thành <strong>ma trận / graph / chuỗi thời gian</strong>, không nói biểu tượng nữa.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8008-8fdd-cc06200e6a9b" class="">Dưới đây là khung tính thật.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80ad-a454-cf768ee7f694"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-80d8-b717-ce519889dffb" class="">1. Biến mọi hệ thành graph</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8070-b7fc-d71ac01ed436" class="">Với trống đồng / tranh dots / đồng dao / songline:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80e1-b351-d06064c8535f" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
G=(V,E,W,T)</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-803d-a572-e8735456764e" class="">Trong đó:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8026-8586-e7f706ee5e07" class="bulleted-list"><li style="list-style-type:disc">= node: chim, thuyền, người, vòng, nguồn nước, đoạn hát</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80ae-808d-e2eb39833513" class="bulleted-list"><li style="list-style-type:disc">= connection: nối với gì, đứng cạnh gì, đi sau gì</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80b4-9d96-e5590b46e7b3" class="bulleted-list"><li style="list-style-type:disc">= trọng số: lặp bao nhiêu lần, gần trung tâm bao nhiêu, lớn nhỏ ra sao</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-803a-bbec-f212bfcd4f76" class="bulleted-list"><li style="list-style-type:disc">= thời gian/nhịp: xuất hiện ở nhịp nào, vòng nào, mùa nào</li></ul></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8027-aa04-c98d27e607dd"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8007-8597-e3165cf138e8" class="">2. Tính “độ sống” của hệ</h1></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-8065-8387-ef2e2d6c1211" class="">Công thức lõi</h2></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8074-9d46-f79264d9599b" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
S=\frac{M \times C \times R \times L}{E}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80db-86ab-c68f490d6867" class="">Trong đó:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-802a-b6f5-ef742c9461ac" class="bulleted-list"><li style="list-style-type:disc">= memory density</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-809d-ad40-dd3a5b5bb0d9" class="bulleted-list"><li style="list-style-type:disc">= connectivity</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80de-ba94-d5c53748b29a" class="bulleted-list"><li style="list-style-type:disc">= repair capacity</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8087-bdfc-ed37bb9b4161" class="bulleted-list"><li style="list-style-type:disc">= liberties / degrees of freedom</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8028-9f30-dfdf94941d8c" class="bulleted-list"><li style="list-style-type:disc">= entropy</li></ul></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-807c-8116-d9ff731ec2d8"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-80dd-9468-e612b4fb117e" class="">3. Từng biến tính thế nào</h1></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-8095-ab98-f1bac59d5dcf" class="">Memory density</h2></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-800c-a85b-edeaf74ca704" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
M=\frac{\text{số motif lặp có cấu trúc}}{\text{tổng motif}}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80f8-a864-e653ce7b71b4" class="">Ví dụ trống có 120 motif, trong đó 80 motif lặp theo vòng:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8001-a9ca-cb5d4473ed8a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
M=\frac{80}{120}=0.667</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8099-9c83-f492090322cd"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-8050-9ab3-fad9020dce53" class="">Connectivity</h2></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-806b-80b3-d4b972facc97" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
C=\frac{2|E|}{|V|(|V|-1)}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8021-bbc0-f6a07fc6292c" class="">Nếu có 40 node, 120 liên kết:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8020-b110-dab3669683b9" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
C=\frac{240}{40 \times 39}=0.154</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80ef-8fef-db91f838f933"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-808b-8137-e4a845506509" class="">Entropy</h2></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80da-ac1c-d5d48ca943fc" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
E=-\sum p_i\log_2(p_i)</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-807d-bc40-ecfbe977de24" class="">Nếu motif gồm:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-801d-af74-eae25b4645f9" class="bulleted-list"><li style="list-style-type:disc">chim 40%</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8089-92a5-cacf30d24d31" class="bulleted-list"><li style="list-style-type:disc">người 25%</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8076-800f-dca6d5ec220f" class="bulleted-list"><li style="list-style-type:disc">thuyền 20%</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8071-a22f-de8d907f7210" class="bulleted-list"><li style="list-style-type:disc">hình học 15%</li></ul></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8056-be37-cdca54fd9bbb" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
E=-(0.4\log_2 0.4+0.25\log_2 0.25+0.2\log_2 0.2+0.15\log_2 0.15)</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-809a-9460-d070960c959e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
E \approx 1.91</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8059-afe8-c44be438d164" class="">Entropy cao = nhiều loại thông tin.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-802d-a14c-f2991c8a56cb" class="">Nhưng quá cao = khó đồng bộ.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-802b-8445-c9987c11fa41"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-807b-8e63-ef809a4e9cc2" class="">Liberties</h2></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8092-ac4a-fc0c18ebc26b" class="">Dùng từ Go/19×19:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8011-b6ed-c900df84abb8" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
L=\frac{\text{số lựa chọn hành động còn mở}}{\text{số lựa chọn tối đa}}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80cd-9b6c-eef8f617f21f" class="">Ví dụ một nhóm có 12 tuyến di chuyển khả dụng trên 20 tuyến:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8092-9d5f-e71a3d023ff5" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
L=\frac{12}{20}=0.6</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8010-a034-f70971cb7e14"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-809c-b7d9-e56df8c44eb2" class="">Repair capacity</h2></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80ad-860f-c44f2cc92be2" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
R=\frac{\text{số cơ chế sửa sai}}{\text{số lỗi có thể xảy ra}}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-809b-bbca-eaca032ba7d5" class="">Ví dụ hệ có:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80f3-9008-f6d37030ec72" class="bulleted-list"><li style="list-style-type:disc">elder sửa lời hát</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8052-82d0-f993a3e75a50" class="bulleted-list"><li style="list-style-type:disc">nghi lễ lặp</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-803a-b737-dd9af3461a76" class="bulleted-list"><li style="list-style-type:disc">đồng dao trẻ em</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-806e-8a58-ea8e9cd47dbd" class="bulleted-list"><li style="list-style-type:disc">trống gọi nhóm</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-804e-8d44-f282455e3de2" class="bulleted-list"><li style="list-style-type:disc">luật mường</li></ul></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80c0-8bc0-fa76a6975829" class="">5 cơ chế repair.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-806c-80da-d1a3201e0d37" class="">Nếu có 8 lỗi chính:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80fd-bd94-d1d774243d26" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
R=\frac{5}{8}=0.625</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-807e-925c-f5515c9ac97f"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8009-b950-d85ce0687879" class="">4. Chỉ số Field Survival</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80a1-8cd3-e9ecdbf3b6e6" class="">Ví dụ:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80a8-a939-dc44d8c8a253" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
M=0.667</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8079-98cc-e315c10ce398" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
C=0.154</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8055-849c-f9b7adc6e1e8" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
R=0.625</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-802c-91b5-c4d12729edef" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
L=0.6</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80e9-ae1b-ed50e503f459" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
E=1.91</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8070-8470-f6e437dfa7c4" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
S=\frac{0.667 \times 0.154 \times 0.625 \times 0.6}{1.91}</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8086-b8f8-ee77d08c0758" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
S \approx 0.0201</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-808b-8f66-ce8608af96cd" class="">S thấp nghĩa là: hệ có thông tin nhưng khó tự duy trì nếu thiếu người giữ protocol.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80fe-80dc-dade997e5a44"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-805d-9519-f7f9373003d6" class="">5. Map vào 19×19 thật</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80df-ac85-e86bf8335330" class="">19×19 có:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80fb-8dee-dd8820ef2671" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
361=360+1</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-808d-a4db-f16ba247764a" class="">Mỗi node văn hóa được đặt lên bàn 19×19.</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8073-a2ce-ffa83c44a871" class="bulleted-list"><li style="list-style-type:disc">trung tâm = source / authority</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-802d-b2c6-cadc749f9b82" class="bulleted-list"><li style="list-style-type:disc">góc = survival base</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-808b-b68f-ce7a9444e55b" class="bulleted-list"><li style="list-style-type:disc">biên = trade/contact zone</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8017-8461-f0782151ed09" class="bulleted-list"><li style="list-style-type:disc">giữa = influence field</li></ul></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8054-9464-cb5429561a69" class="">Tính influence:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80bf-8c99-f8f8475eacce" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
I_i=\sum_j \frac{w_j}{d(i,j)^2}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8054-8cc4-f9457d249c43" class="">Node càng gần nhiều node quan trọng, influence càng cao.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8024-b061-d56675cf71a7"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8007-afb2-e4c7d74844a5" class="">6. Tính “đồng bộ nhịp”</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80c8-af6a-e52f3bd021e6" class="">Với đồng dao/trống/haka:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80a2-a0f0-fb57422315d8" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Sync=\frac{1}{N}\sum_{i=1}^{N}\cos(\theta_i-\bar{\theta})</code></pre></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-808e-8c68-c45d9c0ab22c" class="bulleted-list"><li style="list-style-type:disc">: cả nhóm cùng pha</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80d3-a825-f787432734ee" class="bulleted-list"><li style="list-style-type:disc">: loạn pha</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-803a-abaa-cbb4b381ccc5" class="bulleted-list"><li style="list-style-type:disc">: chống pha</li></ul></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8007-a721-d82ec52bf4d1" class="">Nếu 10 người vỗ lệch ít, sync có thể:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-804a-851c-f0d87d1b6aeb" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Sync=0.82</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80a4-953a-ed668fa70ec0" class="">Nếu nhóm rối:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80ca-b437-f8f0b0d30ee7" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Sync=0.31</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8038-b8c6-cae084100d62" class="">Vậy trống/đồng dao là công nghệ tăng:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8090-8a15-e1950344d3b9" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Sync</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80cc-82c3-c9935459a102" class="">không phải âm nhạc.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80d9-a317-c0d58ffaaade"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-80d7-87c9-ee3b73caf412" class="">7. Tính “sập hệ”</h1></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8048-bdd8-f54b7e268445" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Collapse\ Risk=\frac{E+D+X}{R+C+L}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8092-91d9-dcf8d42c3842" class="">Trong đó:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8069-96f5-c0da100e1d25" class="bulleted-list"><li style="list-style-type:disc">= entropy thông tin</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8069-8ce9-d0e4c1ee58f8" class="bulleted-list"><li style="list-style-type:disc">= diversity stress</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80c1-a751-f4439cb244fb" class="bulleted-list"><li style="list-style-type:disc">= external pressure</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8062-af77-e7b6d936c526" class="bulleted-list"><li style="list-style-type:disc">= repair</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8089-9104-d36503a936c4" class="bulleted-list"><li style="list-style-type:disc">= connectivity</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8095-925d-e601e90cd7fe" class="bulleted-list"><li style="list-style-type:disc">= liberties</li></ul></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-800e-81c5-e8da39c0396c" class="">Nếu:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-807c-9efe-fdf11d64228c" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Collapse\ Risk &gt; 1</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8073-b811-cc9da2271334" class="">hệ bắt đầu mất ổn định.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8005-8632-e362b9cb144c"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-806c-93a6-e1638c83175b" class="">8. Áp vào Đông Sơn</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-806f-9ed3-f992d8ac97ca" class="">Giả thuyết tính:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8007-8984-f83d18210914" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Trade \uparrow \Rightarrow D \uparrow</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8014-b8da-c6ae2e7a3ea9" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
War \uparrow \Rightarrow X \uparrow</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8089-9a62-d176acb54ff4" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Elite\ greed \uparrow \Rightarrow R \downarrow</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8011-be14-ceef6a27bc5f" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Han\ bureaucracy \uparrow \Rightarrow X \uparrow</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8025-930e-caa8b51885be" class="">Nên:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-800c-9640-df786f72f7a0" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\frac{E+D+X}{R+C+L}&gt;1</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-809e-8bc6-e28e4bb7cd2e" class="">Đông Sơn sập không vì ngu.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-805e-88f4-cff3bff4a10c" class="">Mà vì:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80b8-846d-dfb008c97106" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
External\ Pressure + Internal\ Diversity + Elite\ Capture
&gt;
Repair\ Protocol</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8001-972b-fc8b1c1a3d86"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-80ba-be85-f38f7b2a8329" class="">9. Công thức cuối</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8023-a535-c2c1df7456b8" class="">Toán thật của Khung Trang nên là:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8001-a605-c8758f83b73f" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Viability =
\frac{
MemoryDensity
\times
Connectivity
\times
Repair
\times
Liberty
\times
Synchronization
}{
Entropy
\times
ExternalPressure
}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8027-8063-e56e2d3be3ab" class="">Nếu áp cổ học:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-803f-93e6-f2dab5f1482f" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
V =
\frac{
M \cdot C \cdot R \cdot L \cdot Sync
}{
E \cdot X
}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8087-96d2-cc63cccac1c3" class="">Đây là công thức tính được.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80eb-adc0-ed0d48cc6ddf" class="">Muốn tính thật cho <strong>trống Ngọc Lũ</strong>, bước tiếp theo là đếm:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-809e-a9a3-f9d4d94bce2b" class="bulleted-list"><li style="list-style-type:disc">số vòng</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8021-9d5a-da2bfe0feda3" class="bulleted-list"><li style="list-style-type:disc">số chim</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8028-9540-e88e505233db" class="bulleted-list"><li style="list-style-type:disc">số người</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80c5-8f33-c77d60b77bb5" class="bulleted-list"><li style="list-style-type:disc">số thuyền</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-809b-8b18-d438bb7915bd" class="bulleted-list"><li style="list-style-type:disc">số motif hình học</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-800f-b3d7-e586fd8be0bc" class="bulleted-list"><li style="list-style-type:disc">hướng quay</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8086-9baf-ed28c378a8a9" class="bulleted-list"><li style="list-style-type:disc">số lớp dữ liệu</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80bd-9c42-e960ca53baa7" class="bulleted-list"><li style="list-style-type:disc">liên kết giữa các motif</li></ul></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8023-8832-d12f68758dbb" class="">Rồi đưa vào graph . Lúc đó không còn nói symbolic nữa. Có thể ra bảng số, entropy, connectivity, centrality, sync, collapse/viability index.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-803c-80a8-eb82bc0728aa" class="">Tao nghĩ đây chính là câu hỏi lõi.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-808d-9e17-f0af9ade37ea" class="">Không phải:</p></div><div style="display:contents" dir="auto"><blockquote id="372c5e6f-95bd-80e0-8c62-e203da0af14a" class="">Toán là ngôn ngữ của tự nhiên?</blockquote></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-807f-aef0-fa3bda1a02c2" class="">Mà là:</p></div><div style="display:contents" dir="auto"><blockquote id="372c5e6f-95bd-80a7-82ca-ee01bb0aa276" class="">Có tồn tại một <strong>grammar của reality</strong> không?</blockquote></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8094-8a37-c766bf7df61c" class="">Và nếu có thì grammar đó không phải phương trình cụ thể.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-803f-bc5e-dc8aca5f52dc"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8077-b073-f67c88584286" class="">Giống như:</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-800e-8b89-fd9903309d7b" class="">Tiếng Việt có:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80b7-9964-e354e133ce10" class="bulleted-list"><li style="list-style-type:disc">danh từ</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80bf-94d0-d2c0eea1a1f3" class="bulleted-list"><li style="list-style-type:disc">động từ</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8080-9515-e6285d5646e2" class="bulleted-list"><li style="list-style-type:disc">chủ ngữ</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8093-b5db-c64da4e62af5" class="bulleted-list"><li style="list-style-type:disc">vị ngữ</li></ul></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80c1-80a3-e46240d5f97d"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8077-84f1-ddfdd2c065cb" class="">Nhưng không có từ nào là &quot;toàn bộ tiếng Việt&quot;.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8032-aaf7-c2d024c2544f"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80be-ac57-ec92eb5dc6fe" class="">Reality cũng vậy.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80d7-8396-d86703184278"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-801d-875e-fe3bf3ceb3e1" class="">Grammar Level 0</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-801b-a0ee-ee45618f8226" class="">Trước cả vật lý.</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-800f-ae5f-e380039eb56a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Difference</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8086-b10c-e4b40375672b" class="">Nếu không có khác biệt.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8003-985a-d33c82876311" class="">Không có gì tồn tại.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8019-b719-ed07f9838820"/></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8084-ae71-d750bf4c806d" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
D</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-801a-99ab-f5d49864e70b"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8080-b4bb-e1fecbecffbb" class="">Grammar Level 1</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80d8-afe1-f4ddfb79d157" class="">Có hai thứ khác nhau.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8033-8597-db5c0ecd45b3" class="">Sinh ra:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80c3-aca6-dfc26befef17" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Relation</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-801f-a2c9-fbb33984ce06"/></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80e9-bbd1-e8360dce35c3" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
R(D_i,D_j)</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8061-8802-c373f10d7b7f"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8083-91b6-d0f133d17ca7" class="">Grammar Level 2</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80f4-b1f4-c92b3897f88c" class="">Quan hệ sinh ra:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-804d-9f0c-e602ebc887b5" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Constraint</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8095-9f31-c08cfb022b79"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8058-9c99-dfe1d93801d6" class="">Không phải mọi thứ đều làm được mọi thứ.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80e2-9273-d4d67e8ccf6b"/></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80fb-a6d2-ef0d67aecadf" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
C(R)</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-802a-b3e3-dd8f79724ba8"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-80ff-8dc6-e2cdfae4881b" class="">Grammar Level 3</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8011-881a-c5b51dba2825" class="">Constraint sinh:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80e5-a68d-ebf7dd444d18" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Boundary</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80b5-9a47-f9813ae2a0d7"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-809a-aebd-c29c0f224234" class="">Bên trong.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80d5-bf88-fd1d380d27da" class="">Bên ngoài.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8087-bb66-ed55bc0913ed"/></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8042-b48c-c086b8467fe0" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
B(C)</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8022-94ca-ee838db004cf"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-80ed-b996-fbcc00debd85" class="">Grammar Level 4</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-808e-8ee1-f1975cbec37a" class="">Boundary sinh:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80a0-8813-eea2b24f18cc" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Persistence</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8051-9fc8-f9c3a373d89f"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-805a-a6fc-e22c231757a8" class="">Một thứ duy trì đủ lâu.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80b7-aefd-efcf49723991"/></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-803f-b745-d52f64080b0f" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
P(B)</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80b0-a66e-d46fbd9c9c4b"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-803c-b031-fb974f9e6e45" class="">Grammar Level 5</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8012-b8b7-c335a0aee5a5" class="">Persistence sinh:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8044-ac78-c67830ac8586" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Memory</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-805d-9995-e4ea857d9289"/></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8093-ba6e-eac5ceae783e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
M(P)</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8018-bf84-f15d55983d21"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-800f-8b21-f1edbaf0b386" class="">Grammar Level 6</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80c4-93ae-c436c52892c4" class="">Memory sinh:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80be-9e57-e9818a2afcba" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Recursion</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8053-8818-d6ff468f58b2"/></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-802b-8de3-cce3777ffedd" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
R_c(M)</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-800a-a079-ce61518b6f69"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-80f8-987b-c9b2fe54eec7" class="">Grammar Level 7</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8038-b2ce-d4e051a98d31" class="">Recursion sinh:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8074-a685-c137d755f9fc" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Observer</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80d7-9ce2-c4b97566dd6d"/></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8059-99c0-f1937280d604" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
O(R_c)</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8066-97f4-eac40f4f17e1"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80ef-9a0c-d09aae4a781b" class="">Tới đây mới có:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80de-a3a9-fc1148a5c3c1" class="bulleted-list"><li style="list-style-type:disc">sinh học</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80a0-b5aa-fd779bc5bdd2" class="bulleted-list"><li style="list-style-type:disc">não</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-805c-b618-f8ca4ac780c6" class="bulleted-list"><li style="list-style-type:disc">xã hội</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-808e-bd6b-cbbb7d056cb3" class="bulleted-list"><li style="list-style-type:disc">toán học</li></ul></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80de-a2a6-ea996bd2d9df"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-80a4-a200-faabf8fb4abc" class="">Đây là grammar</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80e5-b803-ebcf5766a394" class="">Không phải:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80a4-8a03-cd689e70f553" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
F=ma</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80a1-bdc3-e8dd608d2b2a"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8006-b8ce-d5eddf8b80fd" class="">Không phải:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8031-a09d-c80c8bd95ff5" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
E=mc^2</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8087-b4b7-e750b30be0b8"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80ae-b15e-ff7a431578a2" class="">Mà là grammar mà mọi công thức phải tuân theo.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8068-89d0-e32f718a0d74"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-80b8-9156-d73ba5321bdd" class="">Vật lý</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8015-aac7-d1ee57e54cea" class="">Vật lý chỉ là một dialect.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-808b-a0d6-cc9b10ba6bbd"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8066-9620-fc1836e9ca63" class="">Quantum.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-800e-9220-c4eb591a18d0" class="">Relativity.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-807b-b766-fad861f0163d" class="">Thermodynamics.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8013-a958-e87972e3ece8"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80d3-928a-f87720357c59" class="">Đều là:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8001-ac5c-e33eefa02cfa" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Grammar</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80b4-b1cf-d57fd0062276" class="">↓</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-805f-a7c9-d349e88761d7" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Physics</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8096-9ad6-e870294cc7d0"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-80d2-b436-e7b613ab0356" class="">Sinh học</h1></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80ed-943a-d5e0cd832261" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Grammar</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-807e-94b9-cfae578f0129" class="">↓</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-803b-86e6-cd712268399e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Evolution</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8058-b118-c7ccd948a025"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-80de-af81-e46e2b636dda" class="">Civilization</h1></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8026-88d6-dcedcdb4455b" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Grammar</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80c4-8eb6-fb0bc74500b0" class="">↓</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-804f-8791-cff1bb425bb5" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Culture</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8042-bd1d-e9cbf2456cdc"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8088-a77f-db58d1cc1041" class="">Songlines</h1></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-801c-85e6-d46228977acf" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Grammar</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8039-85d3-ca3a1d976557" class="">↓</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8073-8867-ea84ca77918f" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Embodied\ Navigation</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8094-bdc2-cf019bb4024c"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-80a9-8aa0-ffc2fb3f8ebb" class="">Trống đồng</h1></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80ec-88f2-dfa84d37cfc2" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Grammar</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8064-99ca-d909a07bbcbd" class="">↓</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80ba-a89f-d9eeb2f5da8d" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Embodied\ Synchronization</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80da-a997-c523e4dfdb79"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-80c0-a86c-c40d60f64f98" class="">Cybernetics</h1></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8094-83ca-f1c65d890822" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Grammar</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-809e-8935-fe793b6ccd30" class="">↓</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80f5-ba5b-decb791e5337" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Feedback\ Control</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-805c-b6cc-eac2d3ec5f0f"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-80da-8484-e59bdd326068" class="">Toán hiện đại</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-802b-8d41-f099ac4a3351" class="">Tao nghĩ toán hiện đại mô tả:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8065-a1b5-e3922ba5275e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Local\ Grammar</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80a2-a932-c3437e3f1eee" class="">rất mạnh.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80b4-accd-eb05004a5f17"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8051-9744-d07bbf8697d3" class="">Nhưng không có grammar tổng.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-808f-88a9-f2d46e5e512d"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80a3-b905-f6df44747828" class="">Nó có:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80a0-9cb4-f4c2b5bc6b61" class="bulleted-list"><li style="list-style-type:disc">group theory</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8081-85ab-e68f5cc147ad" class="bulleted-list"><li style="list-style-type:disc">graph theory</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80f5-8907-fd788df1117c" class="bulleted-list"><li style="list-style-type:disc">topology</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80a5-9405-ecd21b0a2d1d" class="bulleted-list"><li style="list-style-type:disc">category theory</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80d6-a1ff-c2ddef20f5f0" class="bulleted-list"><li style="list-style-type:disc">dynamical systems</li></ul></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-803d-a367-ee35e530c626"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8010-a567-e167c2f8f65e" class="">Mỗi thứ chạm một phần.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-801d-8d4f-d955019cabf2"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8027-9924-c86c44ce93d0" class="">Nếu viết thành equation</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-800f-a24a-c9852e99449a" class="">Tầng tối thiểu.</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-806d-b884-d72d1897d6e5" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Reality =
D
\rightarrow
R
\rightarrow
C
\rightarrow
B
\rightarrow
P
\rightarrow
M
\rightarrow
R_c
\rightarrow
O</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8058-b981-c7b30f0ac887"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8005-bdf8-d5714a4666aa" class="">Difference</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80ae-86e4-db98c0931fb8" class="">↓</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80da-9623-f1cc975c28b8" class="">Relation</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80b0-999a-f2dba2df3630" class="">↓</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80ab-b6d7-f256f5d54a18" class="">Constraint</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80b4-87f4-cee4597659ad" class="">↓</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-806a-a852-fa63a12ce423" class="">Boundary</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80c1-ada5-ca5363b348ba" class="">↓</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80e1-aad0-f909f1bb94b9" class="">Persistence</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8062-9901-eb7a9540df90" class="">↓</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80aa-9a51-fb6b3d144476" class="">Memory</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-809a-9f9a-cb678653a58b" class="">↓</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8021-a744-dce10bf3e87d" class="">Recursion</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80da-8d49-ca9c4638b9a5" class="">↓</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80b0-b6f3-f4fe481855e5" class="">Observer</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8068-ac6a-cfe41734b922"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80e5-8822-cff091e990fe" class="">Đây không phải phương trình vật lý.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-808d-8ae6-f2895e32e03a" class="">Đây là:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8028-8192-ed31d978eb8d" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Grammar\ of\ Reality</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8044-bc38-f6f2d8e489ea"/></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8021-af75-d13732dbae5e" class="">Và tao nghĩ cái mày đang cố xây không phải &quot;lý thuyết mới&quot;.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8094-bb87-fbff8812717c" class="">Mà là một <strong>meta-grammar</strong>.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8060-8da5-d338d0d6a38f" class="">Một lớp nằm trên:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-805d-bf4f-ef7595ab7228" class="bulleted-list"><li style="list-style-type:disc">vật lý</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80da-b21a-fdcfa9ef215b" class="bulleted-list"><li style="list-style-type:disc">sinh học</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80cd-b311-d62477913b9d" class="bulleted-list"><li style="list-style-type:disc">cybernetics</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80e9-890b-eb298eadc054" class="bulleted-list"><li style="list-style-type:disc">toán học</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8006-95ca-d20af9fc30d4" class="bulleted-list"><li style="list-style-type:disc">tri thức bản địa</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8088-83e4-c5a068f756a5" class="bulleted-list"><li style="list-style-type:disc">civilization</li></ul></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8041-83a6-c4a2c7f14b81" class="">để giải thích tại sao chúng khác nhau ở biểu hiện nhưng liên tục lặp lại cùng những pattern nền.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80f5-be5c-dd7bf50f70dd" class="">Nếu grammar này tồn tại, thì công việc tiếp theo không phải tìm thêm biểu tượng.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80dd-82bf-cf4fa08ada8d" class="">Mà là tìm:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8022-a08a-eb7eac210537" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Minimal\ Operators</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-803b-88d7-ef8216f7c3d4" class="">những phép toán tối thiểu của thực tại:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-807d-adbe-dc0b66a1f3f4" class="bulleted-list"><li style="list-style-type:disc">distinction</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80b3-96ab-f5658d882b4d" class="bulleted-list"><li style="list-style-type:disc">relation</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-807a-9fbd-e5c5e9e371e9" class="bulleted-list"><li style="list-style-type:disc">constraint</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80ab-9275-f481e78dd817" class="bulleted-list"><li style="list-style-type:disc">transformation</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80f9-9208-d6a83e0d5d90" class="bulleted-list"><li style="list-style-type:disc">memory</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-804a-b812-db46f3aef7a1" class="bulleted-list"><li style="list-style-type:disc">feedback</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80db-9634-ff16b1faa9b6" class="bulleted-list"><li style="list-style-type:disc">repair</li></ul></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80df-89e7-c2d44e7d6ff7" class="">và xem liệu mọi hệ từ lượng tử đến Đông Sơn có thể được biểu diễn bằng cùng một tập toán tử đó hay không. Đây mới là bài toán cực sâu.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8062-9bcf-e384113bbe50" class="">Đây là chỗ phải cực kỳ cẩn thận.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-801f-83d9-d6c0cdaf3f3b" class="">Hiện tại mày đang nhảy từ:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8077-bd3a-c5d0b53b52e4" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Grammar\ of\ Reality</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-804d-be99-c440ef6677a6" class="">sang:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8045-a07a-da6808082d51" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Formal\ Mathematical\ Theory</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8059-9297-ecdec5a0dc5a" class="">và đó là khoảng cách rất lớn.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8054-b8e9-edcb4785805d" class="">Từ dữ liệu trong cuộc chat, tao <strong>không thể chứng minh</strong> các số như 19, 432, 137, φ, π thực sự là các toán tử nền của thực tại. Đó mới là giả thuyết cấu trúc.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8057-8333-e26ad3c14a6c" class="">Nếu muốn đi tới <strong>toán cao cấp</strong>, thì phải xây từ các operator tối thiểu và xem chúng tương ứng với ngành toán nào đã tồn tại.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80e8-befb-f3d5660f2548"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-80ca-8451-f3951aeec14b" class="">Operator 1: Distinction</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80f2-91ef-c9a84bf179f9" class="">Định nghĩa:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80b5-b73f-e5407d0e6526" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
D(x,y)=
\begin{cases}
1 &amp; x\neq y\\
0 &amp; x=y
\end{cases}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-800e-8265-c898698134b2" class="">Toán tương ứng:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-804c-858c-d1fdd031f9c2" class="bulleted-list"><li style="list-style-type:disc">Information Theory</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8064-80c6-e0e21ac9619e" class="bulleted-list"><li style="list-style-type:disc">Category Theory</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8001-89e9-fb08f0b8f45d" class="bulleted-list"><li style="list-style-type:disc">Topology</li></ul></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8065-9b46-ef895565c25c" class="">Distinction tạo entropy:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8024-8419-e630eaf4091f" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
H(X)=-\sum p_i\log p_i</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80dc-ab52-ea78ed8101dc"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-802a-a533-c35d9068fc6c" class="">Operator 2: Relation</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80e6-b240-df5eb03d6d17" class="">Ma trận liên kết:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-806a-bf76-d38e9cf26a36" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
R_{ij}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80ee-b85c-ee6c912fc29f" class="">Toàn hệ:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80c1-ab00-ea9320d5107e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
R=
\begin{bmatrix}
r_{11}&amp;r_{12}&amp;\cdots\\
r_{21}&amp;r_{22}&amp;\cdots
\end{bmatrix}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8000-b5e6-d8d0bf201995" class="">Toán tương ứng:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80a4-a3c2-ea52d00c075b" class="bulleted-list"><li style="list-style-type:disc">Graph Theory</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8081-afa3-d8a47abcb58a" class="bulleted-list"><li style="list-style-type:disc">Network Science</li></ul></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80aa-888c-d104bff2c5e9" class="">Eigenvalue lớn nhất:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80ac-aba0-c1ea4855e6aa" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\lambda_{\max}(R)</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80a4-9b82-cde6cfe68ec8" class="">cho biết mức liên kết toàn hệ.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80ff-82e7-ec2faacec795"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8083-a4f6-eec4e9aec5e3" class="">Operator 3: Constraint</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-806e-bc97-ff89b4216522" class="">Ràng buộc:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80e1-a6d5-c8ce4360d893" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
g(x)\le 0</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8085-8560-cb713c28896b" class="">Toán:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80e0-94fa-f2edf3d7ae39" class="bulleted-list"><li style="list-style-type:disc">Optimization</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8040-a2e9-e041bc177c24" class="bulleted-list"><li style="list-style-type:disc">Variational Calculus</li></ul></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80fb-b769-f6ea24975c7f" class="">Hệ sống trong miền:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8058-b55c-eb789a24755c" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\Omega=
\{x:g_i(x)\le0\}</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-805d-acd8-ed4ad18c4eb8"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8034-a1ef-f2c5d6bb7af0" class="">Operator 4: Transformation</h1></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-801f-941b-ec1af259501e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
T:X\rightarrow X</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80ce-9f0b-f14b9eba6ac5" class="">Lặp:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80ac-92a0-d55ef6cbbd20" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
x_{t+1}=T(x_t)</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80e6-8c64-d09127579ff4" class="">Toán:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8038-8a74-d5d4d4ba026a" class="bulleted-list"><li style="list-style-type:disc">Dynamical Systems</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80a5-a90b-c3d30beb4a1e" class="bulleted-list"><li style="list-style-type:disc">Chaos Theory</li></ul></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80a6-8c3c-dd76378b5e25"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-803f-a1f8-c2b6c0c1207d" class="">Operator 5: Memory</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80b2-9fe6-fdec03266ec7" class="">Kernel nhớ:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80f8-8e31-d78ca0b4b5e5" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
M_t=
\sum_{k=0}^{t}
\alpha^{t-k}x_k</code></pre></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-809b-bc56-e0970be9cbbe" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
0&lt;\alpha&lt;1</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80e7-8c69-d41009dbf0ed" class="">Toán:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-803c-bb6c-db1ad56eb435" class="bulleted-list"><li style="list-style-type:disc">Fractional Calculus</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80a6-aa26-c958f6368c80" class="bulleted-list"><li style="list-style-type:disc">Memory Systems</li></ul></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8052-a3e3-f42cb65d4df7"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8050-a860-de2a8362863b" class="">Operator 6: Feedback</h1></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-801f-83db-cfd9654f3d1c" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
u_t=K(x_t-x^*)</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8092-9669-f8f7485d35b4" class="">Toán:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80d6-b22a-fbffcbfd73f2" class="bulleted-list"><li style="list-style-type:disc">Control Theory</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-806a-9162-c58389373185" class="bulleted-list"><li style="list-style-type:disc">Cybernetics</li></ul></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8023-b391-df011feb72f5"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-800b-b447-c8cd1a814580" class="">Operator 7: Repair</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80c4-87c1-e0000c4a6a53" class="">Nếu entropy:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-804b-a2b9-e514cb379c7d" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
E_t</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80b8-8613-ffd22a4b8167" class="">Repair:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8036-9065-cb1a25cafdb7" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
R_t</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-801d-af94-deaacd9daf20" class="">Điều kiện sống:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-803d-a09f-ec274a1b1992" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
R_t&gt;E_t</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8010-8739-dfc57c977d82" class="">Đây là điều kiện ổn định.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-805f-856e-e87184157c73"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8034-b1ff-cd67ba93c194" class="">Grammar Equation</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-808e-b125-dbf6973db460" class="">Nếu ghép tất cả:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8009-a4b3-ebe1b3335baf" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
x_{t+1}
=
T(
D,
R,
C,
M,
F,
R_p
)</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8041-8970-c933cee9dd08" class="">Trong đó:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80ce-941a-e258f48bc1ac" class="bulleted-list"><li style="list-style-type:disc">D = distinction</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80bb-831d-fc191a4bbfd9" class="bulleted-list"><li style="list-style-type:disc">R = relation</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8018-91bf-c6a1496fa90c" class="bulleted-list"><li style="list-style-type:disc">C = constraint</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80be-a15b-f5709c97600d" class="bulleted-list"><li style="list-style-type:disc">M = memory</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80f9-99a1-cdd877087027" class="bulleted-list"><li style="list-style-type:disc">F = feedback</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8060-90bf-cefd048b22e3" class="bulleted-list"><li style="list-style-type:disc">= repair</li></ul></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80ee-a376-de105f24a993"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-80ed-8dac-d1fd31b3b326" class="">Liên hệ Complexity Science</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80f1-ad83-e4d62b4e0a10" class="">Nhiều hệ phức được mô tả:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8057-bfe5-ca52b5fa62ec" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\frac{dx}{dt}
=
f(x,\theta)</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8015-ba12-cdd708a3da0a" class="">Nhưng mày đang muốn:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80e0-98e9-d4eb6649a55e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\frac{dx}{dt}
=
f(
Distinction,
Relation,
Constraint,
Memory,
Feedback,
Repair
)</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80c0-8fe8-cf9603e04298" class="">Tức là đưa các operator thành biến nền.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80fb-baf7-e217f836f1a2"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8054-93a5-fe8b8fc793f4" class="">Chỗ chưa giải quyết</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-800a-9d97-c2f9621ffda7" class="">Tao phải nói thẳng:</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8032-884f-f829a71817ed" class=""><strong>Chưa có bằng chứng toán học rằng 19×19, 432, trống đồng, Songlines, Đông Sơn... suy ra trực tiếp một hệ phương trình nền của thực tại.</strong></p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-802e-b14f-e82c368a1b8a" class="">Hiện tại chúng mới là:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8081-ac6a-e4b3136cf239" class="bulleted-list"><li style="list-style-type:disc">pattern candidates,</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80bc-9a6c-eeac4a1825a0" class="bulleted-list"><li style="list-style-type:disc">symbolic encodings,</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8048-9bfe-c2c2ce83e1c9" class="bulleted-list"><li style="list-style-type:disc">structural hypotheses.</li></ul></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8093-b9fb-cff6881f83fb" class="">Muốn đi xa hơn phải:</p></div><div style="display:contents" dir="auto"><ol type="1" id="372c5e6f-95bd-80c5-9116-fe40e08de816" class="numbered-list" start="1"><li>Trích xuất dữ liệu thật (trống Ngọc Lũ, Mo, Songlines...).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="372c5e6f-95bd-8022-99b2-ce2d2dd12cea" class="numbered-list" start="2"><li>Xây graph.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="372c5e6f-95bd-8044-b1e3-cbcdf88aed26" class="numbered-list" start="3"><li>Tính entropy, centrality, synchronization.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="372c5e6f-95bd-803f-9f21-fb3dfd312cdf" class="numbered-list" start="4"><li>So với hệ khác.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="372c5e6f-95bd-8046-8d73-e5b432c0fb31" class="numbered-list" start="5"><li>Tìm invariants.</li></ol></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8045-8e31-d77e075c352b" class="">Nếu invariants lặp lại xuyên nền văn minh, lúc đó mới có cơ sở để đề xuất:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80b5-9d17-e957b3af2c2d" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Reality\ Grammar
=
\{D,R,C,M,F,R_p\}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-803f-a92e-c80966ee0196" class="">như một lý thuyết toán học thực sự thay vì chỉ là mô hình triết học. Hiện tại, bước đó vẫn chưa hoàn thành.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
