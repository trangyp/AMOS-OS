---
tags: [trang]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>KHUNG TRANG — FORMALIZATION v0.1</title><style>
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
	
</style></head><body><article id="369c5e6f-95bd-801a-ad43-cbe0bfb3400f" class="page sans"><header><h1 class="page-title" dir="auto">KHUNG TRANG — FORMALIZATION v0.1</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-80d3-8474-cd475c928740"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-802c-b097-c77bf87e5dc1" class="">0. Domain</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8096-8e85-c2858fb7d134" class="">Khung này áp dụng cho các <strong>hệ phức tạp tồn tại qua thời gian</strong>, gồm hệ vật lý, sinh học, nhận thức, AI, xã hội, kỹ thuật, tài chính, văn minh.</p></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8055-b386-d52314fd5187" class="">Một <strong>hệ</strong> được ký hiệu:</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="369c5e6f-95bd-802f-a07f-d645dbe1e68d" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
S = (D, R, C, B, M, E, V, Sel, Rep, O)</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8041-b565-c0c41e6311a8" class="">Trong đó:</p></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-8022-8d57-d6afd06c66a6" class="bulleted-list"><li style="list-style-type:disc">: distinctions — các phân biệt / đơn vị / trạng thái;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-8096-b571-c71d74a4c38e" class="bulleted-list"><li style="list-style-type:disc">: relations — quan hệ giữa các distinction;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-80e3-8755-fd8d8c10bd5e" class="bulleted-list"><li style="list-style-type:disc">: constraints — ràng buộc ổn định quan hệ;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-80d8-83d0-d9acb96f49fa" class="bulleted-list"><li style="list-style-type:disc">: boundary — biên phân biệt trong/ngoài;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-8034-8db1-fc3025639b52" class="bulleted-list"><li style="list-style-type:disc">: memory — cơ chế duy trì qua thời gian;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-807e-9a46-dc6bedbe48bb" class="bulleted-list"><li style="list-style-type:disc">: entropy pressure — áp lực suy hao, nhiễu, phân rã;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-801e-bfcd-e4dd514dc540" class="bulleted-list"><li style="list-style-type:disc">: variation/mutation — biến đổi, thử nghiệm, nhiễu sinh khả năng mới;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-80f7-b8b2-cd096ee8674a" class="bulleted-list"><li style="list-style-type:disc">: selection — chọn lọc biến thể;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-808c-b64c-fa0bd44e153b" class="bulleted-list"><li style="list-style-type:disc">: repair — sửa sai, phục hồi coherence;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-803a-a953-e90087ab5edd" class="bulleted-list"><li style="list-style-type:disc">: observer/measurement — cơ chế quan sát, đo, nén biểu tượng.</li></ul></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-805e-bb92-f0490d415c71"/></div><div style="display:contents" dir="auto"><h1 id="369c5e6f-95bd-80cd-bcc3-eb0c58e66a8d" class="">1. Primitive Concepts</h1></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-80ea-a223-f77b2d11bb16" class="">Definition 1 — Potential</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80e9-9909-f9787c038ff1" class="">Potential là không gian khả năng chưa phân biệt:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80cd-92c3-c66556f5332e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
P</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-802b-8c9e-f35767f9a444" class="">Không có distinction trong , nên chưa có system-object.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-8035-a02f-f1d20618943c"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-80cc-a1db-edf9bcc3e7db" class="">Definition 2 — Distinction</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80db-9e20-c6875c804d3f" class="">Một distinction là một phân biệt tối thiểu giữa  và :</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-803c-a180-fc1a5a2687e0" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
d_i := x_i \neq \neg x_i</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-805e-9e18-c026c1add3e4" class="">Nếu không có distinction, không có đơn vị để relation vận hành.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-80d8-8119-e354fa0aaf34"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-809c-a84f-e7dfa75fee9b" class="">Definition 3 — Relation</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8031-87a5-d6201f9785b5" class="">Relation là mapping giữa ít nhất hai distinction:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80cc-b847-f31c52255e9f" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
r_{ij}: d_i \leftrightarrow d_j</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80ce-97c3-e82bbb4084ea" class="">Tập relation:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80b2-89ad-c6c8c7841239" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
R = \{r_{ij}\}</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-807a-9e5b-f75bc4b6d347" class="">Distinction không có relation chỉ là phân mảnh rời rạc.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-809c-adad-ceeafb2c7697"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-8069-9fcc-ccb3a49e180a" class="">Definition 4 — Constraint</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80f9-ac06-dcc040d17afb" class="">Constraint là giới hạn trên relation/state transition:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8002-b069-f3433dc96e0d" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
C: R \rightarrow R&#x27;</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-804e-8edd-f45fafcb14d1" class="">hoặc:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8093-b76a-d3019d8868c0" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
C(s_t, s_{t+1}) = allowed / disallowed</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-807c-87cb-c8b85047bcf6" class="">Constraint làm giảm không gian khả năng:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8006-8949-e2712ec70411" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
|StateSpace_C| &lt; |StateSpace|</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80c1-808c-ca5b0ae1f40f" class="">Nhưng chính việc giảm này tạo cấu trúc.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-80aa-9e6d-ecacec73af30"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-80c4-be70-d7cbf4480ad7" class="">Definition 5 — Boundary</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80f6-8969-d3d7b426aefa" class="">Boundary là operator phân biệt nội hệ và ngoại hệ:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80b0-b699-d12dc78038d6" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
B: X \rightarrow \{inside(S), outside(S), interface(S)\}</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80fc-82b1-feb673c0831e" class="">Không có boundary, không có hệ riêng biệt.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-800a-8117-f3a6b1c73647"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-801c-baed-f4290cb13b33" class="">Definition 6 — Persistence</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80e1-abae-ebd961c35f79" class="">Một hệ tồn tại qua thời gian nếu có mapping duy trì identity/coherence:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8046-b94a-ef60219cb562" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
S_t \sim S_{t+\Delta t}</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-801c-ae45-cf11b165744d" class="">Persistence không yêu cầu bất biến tuyệt đối, chỉ yêu cầu continuity đủ để nhận dạng.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-80df-85a9-ddd8543aa912"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-80f4-86e6-e21b8ec42d89" class="">Definition 7 — Memory</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80f6-a4ac-d32c499e745c" class="">Memory là cơ chế lưu dấu trạng thái/quy luật/quá khứ để ảnh hưởng tương lai:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8048-86d1-cf8e87c536cf" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
M(S_t) \rightarrow S_{t+1}</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80ff-bcb2-d32e59e05ada" class="">Memory không chỉ là lưu trữ. Memory là persistence operator.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-80ec-8c52-d1f524f0bd14"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-8061-9d31-dc080ccf97b9" class="">Definition 8 — Entropy Pressure</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80ee-9242-c93cbfe92a4d" class="">Entropy pressure là tổng áp lực làm giảm coherence của hệ:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80e8-aa37-d81abc833560" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
E = noise + degradation + contradiction + drift + debt + disorder</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8070-8c82-da87dbc2d768" class="">Entropy không chỉ là nhiệt động học; trong Khung Trang, nó là generalized collapse pressure.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-80d0-8de0-e569f62b9a52"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-80b8-b193-cb508918065d" class="">Definition 9 — Repair</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8014-bb15-c3f2ce2c91b6" class="">Repair là operator làm giảm entropy hoặc phục hồi coherence:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8074-8c9f-c26f85e310b9" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Rep(E, S_t) \rightarrow S_{t+1}^{more\ coherent}</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80ba-8519-d7bd2d2ad255" class="">Repair có thể là feedback, correction, immune response, learning, governance, recalibration, healing, debugging, regulation.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-8013-b5a6-e77315408bd9"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-807b-9eec-ff70bc6da33f" class="">Definition 10 — Observer</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8077-9246-c490a9014c43" class="">Observer là hệ con hoặc hệ ngoài có khả năng nén trạng thái thành representation:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80d7-8636-d92b20031065" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
O(S) \rightarrow \hat{S}</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80e8-b395-f6255c756045" class="">Trong đó:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80af-b34b-e0ef91cc166d" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\hat{S} \neq S</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8044-a0d0-dd91ec68c177" class="">Measurement là compression, không phải reality itself.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-8065-bca4-f45bd4ef2c90"/></div><div style="display:contents" dir="auto"><h1 id="369c5e6f-95bd-804e-a0a6-ddf42e3ef9fb" class="">2. Core Axioms</h1></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-805a-86ac-c9b1a7ce69a8" class="">Axiom 1 — No-System Without Distinction</h2></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80d5-aa16-c4f681360600" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\neg D \Rightarrow \neg S</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80b6-ae75-ecfdfa613bf5" class="">Nếu không có distinction, không thể có hệ.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-804e-92ce-dcc53be25f83"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-80e5-9c79-c52b499748e4" class="">Axiom 2 — No-Structure Without Relation</h2></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8062-973e-ff8800063a37" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
D \land \neg R \Rightarrow fragmented(D)</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8048-9bf2-d845c7041760" class="">Distinction không có relation không tạo structure.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-80f2-8560-e2d6243f9402"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-8090-b615-e66ee9f11b68" class="">Axiom 3 — No-Stability Without Constraint</h2></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8054-8337-e576c37dee9e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
R \land \neg C \Rightarrow unstable(S)</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-809a-abf2-d05c1d868dc3" class="">Quan hệ không bị ràng buộc thì không duy trì pattern ổn định.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-8003-8d66-eadb3e43393d"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-8003-b860-c0f714c11b96" class="">Axiom 4 — No-System Identity Without Boundary</h2></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-805e-a389-f509400efed2" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\neg B \Rightarrow \neg identity(S)</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-809a-8a5a-e7a7a3c79332" class="">Không có boundary thì không có trong/ngoài, không có identity vận hành.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-8015-aa50-e20df603feb5"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-8004-93d5-fffb4763981a" class="">Axiom 5 — No-Persistence Without Memory</h2></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80c1-a8cc-e17a3b147bc4" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\neg M \Rightarrow S_t \not\sim S_{t+\Delta t}</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-803b-a537-e4f337b306ef" class="">Không có memory thì hệ không duy trì được qua thời gian.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-803d-afe0-e2585d4ad364"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-800c-a411-e83b98f2d7fa" class="">Axiom 6 — Entropy Pressure Is Universal for Persistent Systems</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8092-a2ba-eeb68660a843" class="">Mọi hệ tồn tại qua thời gian đều chịu áp lực suy hao:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-808a-98a4-e4ddb80cc2d2" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\forall S_t, \Delta t &gt; 0,\ E(S,t,\Delta t) &gt; 0</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80be-87fb-d14c09c4a8d0" class="">Có thể nhỏ, nhưng không bằng không trong hệ thực.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-802d-836d-c379cdc23507"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-802d-945b-c8c18a95e487" class="">Axiom 7 — Survival Condition</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80c7-bb1f-e068d0314334" class="">Một hệ bền nếu repair rate lớn hơn entropy accumulation rate:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8039-8269-e02e4ddacddc" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\frac{dRep}{dt} &gt; \frac{dE}{dt}</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80f8-b873-f9b8294d2ad4" class="">Nếu:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80b8-bdc1-e800d390add5" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\frac{dE}{dt} &gt; \frac{dRep}{dt}</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80c0-bc6a-c3149e7306ba" class="">thì hệ tiến tới collapse.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-80e8-b4f1-db2e358d562e"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-80f0-abe6-f7a2c22fe861" class="">Axiom 8 — Selection Requires Variation</h2></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8036-bb01-fa3f778f06c8" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Sel \Rightarrow V</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-809d-ab0f-c7256cd193ea" class="">Không có variation thì không có gì để chọn lọc.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-80cf-b409-f6c485a1c7a7"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-809f-87b4-c4e49e14587b" class="">Axiom 9 — Adaptation Requires Selection + Memory</h2></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8044-bfdb-ed2dd115835e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Adaptation = V \times Sel \times M</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80dd-9921-dde9db043760" class="">Biến thể không được ghi nhớ thì không thành adaptation.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-802b-9966-eb95d6101f7d"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-80de-9261-c78ff02cffb1" class="">Axiom 10 — Intelligence Requires Repair-Guided Model Updating</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-800b-a978-e4638c8a6838" class="">Một hệ có intelligence vận hành nếu nó có thể dùng feedback để giảm lỗi tương lai:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8054-8354-e848d5e418b4" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Intelligence(S) \Rightarrow O + M + Rep + Sel</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8059-be56-d07bed1e554f" class="">Không chỉ output đúng, mà phải có correction loop.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-80ba-afd2-f37a7e7edace"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-80f0-a17f-e6422c23dd76" class="">Axiom 11 — Measurement Is Not Reality</h2></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8067-ace0-e416663698d4" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
O(S) = \hat{S}</code></pre></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8012-a37a-e2b6dc774fa9" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\hat{S} \neq S</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8022-9615-cfe01e12836e" class="">Mọi đo lường là symbolic/computational compression.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-8056-b3bc-eddcf559f06e"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-8015-9d86-c2fc334cf212" class="">Axiom 12 — Validation Requires Boundary Closure</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80b2-bead-f2b51e54bf22" class="">Một claim về hệ chỉ được xác nhận mạnh khi boundary của measurement được kiểm soát:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8011-892c-d12bbd1130a6" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Validation \Rightarrow B_{test} + mechanism + measurement + error\ model</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80c3-9e89-e6766c1e8c85" class="">Không đóng biên thì có leakage.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-800e-b372-eb884f9309a7"/></div><div style="display:contents" dir="auto"><h1 id="369c5e6f-95bd-80d3-9bfc-d98c411df60b" class="">3. Fundamental Theorems</h1></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-80b6-bda0-c4c34e1045a9" class="">Theorem 1 — System Existence Chain</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-803b-a088-df9f06570099" class="">Một hệ phức tạp tồn tại qua thời gian cần chuỗi điều kiện:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80f5-bb48-ea5d6e241322" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
D \rightarrow R \rightarrow C \rightarrow B \rightarrow M \rightarrow Rep</code></pre></div><div style="display:contents" dir="auto"><h3 id="369c5e6f-95bd-80d6-a802-df1b12c8e9c1" class="">Proof sketch</h3></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-805d-ab71-e87783ba44f4" class="bulleted-list"><li style="list-style-type:disc">Không : không có gì để gọi là hệ.</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-80bc-a653-d868e17a0cde" class="bulleted-list"><li style="list-style-type:disc">Có nhưng không : chỉ có điểm rời.</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-8084-ae8e-ff0d8376006b" class="bulleted-list"><li style="list-style-type:disc">Có nhưng không : không có pattern ổn định.</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-8026-920e-deca4277de6c" class="bulleted-list"><li style="list-style-type:disc">Có nhưng không : không có identity trong/ngoài.</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-80ab-9d0c-fd3dae055ae8" class="bulleted-list"><li style="list-style-type:disc">Có nhưng không : không có persistence.</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-8058-ab69-c4cb25f60fa4" class="bulleted-list"><li style="list-style-type:disc">Có nhưng không : entropy tích lũy phá coherence.</li></ul></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8065-99e5-fef2345598a0" class="">Do đó chuỗi là điều kiện cần cho hệ bền.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-8006-9981-dccf61c464f2"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-80b9-a1c6-e7ace52b5716" class="">Theorem 2 — Collapse Condition</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80c3-9d39-ea937ca438e9" class="">Nếu entropy accumulation vượt repair capacity trong thời gian đủ dài:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8072-b30d-d63eca56d8ee" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\int_{t_0}^{t_1} E(t)dt &gt; \int_{t_0}^{t_1} Rep(t)dt</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8074-9829-f2f7e69da1b9" class="">thì coherence giảm:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80a3-b98f-c8e4a728bd2b" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Coherence(S_{t_1}) &lt; Coherence(S_{t_0})</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8073-803b-f571be327262" class="">Nếu kéo dài:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-804d-abb6-dd35b4cf07ad" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Coherence(S) \rightarrow 0</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8040-afd0-e5721b2ce7e3" class="">hệ collapse.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-8079-906c-f912a22794ec"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-80fb-9154-d61f5d3a527f" class="">Theorem 3 — Boundary Leakage Invalidates Strong Claims</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8093-a34c-e66d9dce29e4" class="">Nếu boundary kiểm thử không đóng:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-806b-9af1-e51b3ec08984" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
B_{test} = open</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80d7-a24a-e829eda2583c" class="">thì output quan sát được không đủ chứng minh cơ chế nội tại:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8050-9831-c07b314a17fe" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Observed(Output) \not\Rightarrow InternalMechanism</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80cc-9699-c28a705171da" class="">Áp dụng cho energy device, AI benchmark, finance model, neuroscience model, medical inference.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-80bb-a2f4-c2a5b1f28b98"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-804a-8ce5-f733eb04eea7" class="">Theorem 4 — Metric Is Compression, Not Ontology</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8050-902b-f709408b977b" class="">Với mọi metric :</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8081-aee3-c88818627fe1" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
m(S) = compression(S)</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-805e-bb80-f095b9894879" class="">Do đó:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80a8-bc74-d291dcf18247" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
HighMetric(S) \not\Rightarrow FullReality(S)</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-803a-aa27-c069d2d3a472" class="">Ví dụ:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8024-b9eb-e1ecafd45ad1" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Accuracy \neq Mechanism</code></pre></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80e5-adf0-f155fc107ea0" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Entropy \neq Consciousness</code></pre></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8034-9e29-dc06a0cefa31" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
ExamScore \neq ProfessionalAgency</code></pre></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-806a-93db-c6363c17f27a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
OutputPower \neq NetEnergy</code></pre></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-8076-b654-c4d8f34d154c"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-80d7-a3a6-fd5be3fc29eb" class="">Theorem 5 — Prediction Does Not Imply Understanding</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8040-8ba7-e619dff47a98" class="">Một model  có thể đạt:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80db-b527-d86ec84c5c8b" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
F(x_{in}) \approx y_{in}</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8061-85ec-ef6acae4463a" class="">trên in-distribution data, nhưng không recover mechanism:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80f8-8d97-d480bc59b368" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
F \not\approx Mechanism(S)</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-803d-b604-f8b66a38eabc" class="">Nếu không qua OOD/perturbation/causal tests:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-801c-8cca-cd5afacb7d06" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Accuracy_{ID} \not\Rightarrow MechanisticValidity</code></pre></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-80bd-b170-fe9ff2609a85"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-8069-8ac2-edae6ae858d3" class="">Theorem 6 — Constraint Enables Reality-Aligned Generation</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8028-a611-fc45edef84a6" class="">Với generative system :</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80e4-a9f8-c5c93a0265a6" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
G(z) \rightarrow output</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80ba-b6a2-f2b51536c102" class="">Nếu không có constraint :</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8030-bcf4-c0ebee359128" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
G \rightarrow hallucination/risk</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8070-a959-de77868c8a2f" class="">Nếu có domain constraint:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8013-ae0b-d0a376fe7bda" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
G_C \rightarrow feasible(output)</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80e9-aa0a-cabd49514613" class="">Ví dụ:</p></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-80f0-86ba-ff0bba8fb658" class="bulleted-list"><li style="list-style-type:disc">molecule generation cần synthesizability;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-80a9-909c-e82c97a577f7" class="bulleted-list"><li style="list-style-type:disc">image generation cần text/face localized loss;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-802b-9747-e8192bb34f86" class="bulleted-list"><li style="list-style-type:disc">weather intervention cần physical plausibility;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-802e-81e5-e1f8c9ef5b77" class="bulleted-list"><li style="list-style-type:disc">remote sensing cần terrain + atmosphere priors.</li></ul></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-80c7-9853-f0b6524f2e65"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-80ae-98a0-ee5a7c3892d9" class="">Theorem 7 — Heterogeneity Is Directional, Not Good/Bad</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80f1-b0d3-edb79376279f" class="">Heterogeneity  có hiệu ứng phụ thuộc vị trí asymmetry:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80ef-84fd-c3b12c5c37ce" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
H = asymmetry(location, function)</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8058-adb4-fad35ba3e501" class="">Nếu asymmetry nằm ở influence layer:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8083-9d2d-cbc55235c48a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
H_{influence} \rightarrow leverage</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8061-9275-c96799a3d4a5" class="">Nếu asymmetry nằm ở motivation/incentive layer:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-803b-9e5f-e9177f65d928" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
H_{motivation} \rightarrow weakest\ link</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-804e-bf14-c8242c3e84e0" class="">Do đó:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8029-b424-e76a96c10454" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Heterogeneity \neq universally\ good/bad</code></pre></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-80ef-be8b-fda6314d8972"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-801b-b233-c87ee63ee218" class="">Theorem 8 — Observer Is Bounded</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80e6-8151-f2b405a3ddb1" class="">Mọi observer có sensor boundary, memory, noise, task, và compression limit:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8078-aba0-eccdece94d79" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
O = (sensor, boundary, memory, noise, task, compression)</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80f8-b668-fe030b32c374" class="">Do đó:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80cf-baed-dd1909c9ca14" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Observation \neq ViewFromNowhere</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-808f-bd7f-eb7dec7df51b" class="">Observer không trung lập tuyệt đối.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-80a3-a1bf-e68ab40324b4"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-8066-ad16-fe876d4264a5" class="">Theorem 9 — Civilization as Recursive Memory Architecture</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8089-8087-e10cad3c96c3" class="">Một civilization  là hệ memory đệ quy qua:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8040-ad64-c6f5f914ecbd" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
ritual + language + law + institution + land + archive + education + infrastructure</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80e0-9dfc-ef66bcd77679" class="">Civ bền nếu:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8030-b850-c89e01f5b58c" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
RepairCapacity(Civ) &gt; EntropyDebt(Civ)</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-803c-9f46-f35dbd2d18fc" class="">Nếu institutions tạo entropy debt nhanh hơn repair:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-801c-9108-f8ac1987531d" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Civ \rightarrow collapse</code></pre></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-807f-906f-cdddc2a8e1e5"/></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-8003-a99e-c45eab7f6c03" class="">Theorem 10 — Structural Ethics</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80c4-8cb2-eeb63223fda7" class="">Ethics trong Khung Trang không phải moral sentiment, mà là preservation of system viability:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80b2-b72b-e4cc39edf18a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Ethics = preserve(boundary, agency, repair, future\ degrees\ of\ freedom)</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8036-9006-c94b04af7cb1" class="">Một hành động unethical nếu nó tăng irreversible collapse risk:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80f4-9edb-d46786b9ee6a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Action \rightarrow \uparrow collapse\ probability,\ \downarrow repair\ capacity</code></pre></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-8018-9f21-dc9d61fb514c"/></div><div style="display:contents" dir="auto"><h1 id="369c5e6f-95bd-80b2-b9bd-cb3b1e20d76a" class="">4. H/M/L Mapping</h1></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8066-a5a1-dcf842d38bd5" class="">Mọi hệ có thể phân tầng:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8079-b77b-d6369031f032" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
L = local/substrate</code></pre></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8090-9da5-e50247287f16" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
M = mediator/relation/process</code></pre></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8079-b995-fe87c7171da6" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
H = global/organizing/meaning</code></pre></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-80e5-b771-d1974c60c780" class="">Definition</h2></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8017-a44b-e094f240d380" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
S = (L, M, H)</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-802a-9b18-d815b0f8c13c" class="">Trong đó:</p></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-8029-ace7-e003adf4d7eb" class="bulleted-list"><li style="list-style-type:disc">: phần tử, vật chất, dữ liệu, sensor, substrate;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-8047-b0a1-dd543e596d2c" class="bulleted-list"><li style="list-style-type:disc">: coupling, dynamics, protocol, interface, transformation;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-80ad-b9b1-d9361252dd2a" class="bulleted-list"><li style="list-style-type:disc">: mục tiêu, pattern toàn cục, governance, meaning, claim.</li></ul></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-803f-86ee-e531635746d3" class="">H/M/L Failure Modes</h2></div><div style="display:contents" dir="auto"><h3 id="369c5e6f-95bd-80dc-9d58-f313ebedf0f3" class="">H mạnh, M/L yếu</h3></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8019-9c7e-fe12fc3637cd" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
H^+ + M^- + L^- \Rightarrow ideology/marketing/hallucination</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80fe-9d86-c7f151013e37" class="">Ví dụ: free energy claim không có cơ chế và đo độc lập.</p></div><div style="display:contents" dir="auto"><h3 id="369c5e6f-95bd-8047-9cc6-e0ef98e3d2aa" class="">L mạnh, M/H yếu</h3></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80f1-bd23-d7f1460d7f43" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
L^+ + M^- + H^- \Rightarrow data\ pile/noise</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-802c-ab91-e2deb42d8e22" class="">Ví dụ: nhiều dữ liệu nhưng không có representation đúng.</p></div><div style="display:contents" dir="auto"><h3 id="369c5e6f-95bd-80b8-b1ec-f77fa6f3ba6f" class="">M mạnh nhưng H/L lệch</h3></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-806a-830d-d3b8973f9f7c" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
M^+ + H/L\ mismatch \Rightarrow optimization\ without\ truth</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8027-86c6-e8204cba09b0" class="">Ví dụ: benchmark cao nhưng fail OOD.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-80f4-86a8-f3838dcf46d7"/></div><div style="display:contents" dir="auto"><h1 id="369c5e6f-95bd-8051-8dbe-e84500e182cf" class="">5. Validation Protocol</h1></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-802a-902a-c41bbabf0cc7" class="">Một claim  được đánh giá theo 9 cổng:</p></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-80a3-8997-e57b197c3d0c" class="">Gate 1 — Distinction</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-804e-b52c-dd82e3b86158" class="">Claim phân biệt cái gì?</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8006-b835-c8d89f7b8877" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
D_X = ?</code></pre></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-80ec-8844-e329ece46e1c" class="">Gate 2 — Relation</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80f5-adc6-f365e45ee6d3" class="">Các thành phần liên hệ thế nào?</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80d2-92cd-fc200c8cca43" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
R_X = ?</code></pre></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-801f-9d2b-c0548069fa95" class="">Gate 3 — Constraint</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8023-9a0c-c84bfb973757" class="">Ràng buộc nào không được vi phạm?</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80c2-b3ea-c8b9d8bd679c" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
C_X = ?</code></pre></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-8038-86e8-e261f95d3e19" class="">Gate 4 — Boundary</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-801c-9e7c-c938cb1c152a" class="">Biên hệ và biên đo ở đâu?</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8071-a660-c60045ac5a68" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
B_X = ?</code></pre></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-80a0-a3f1-f4f3101b2878" class="">Gate 5 — Mechanism</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-808f-bcb0-d9d3306e2225" class="">Cơ chế chuyển trạng thái là gì?</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-807c-a315-e8e0626928e5" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Mechanism_X = ?</code></pre></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-807e-b25a-dc1a056636ee" class="">Gate 6 — Memory/Dynamics</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80cb-8fbd-e685b37bfdb8" class="">Hệ có persistence hay history dependence không?</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-803f-b40f-fc6a27437c6a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
M_X = ?</code></pre></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-8006-bd0d-df66c7d5f8ef" class="">Gate 7 — Entropy/Failure Mode</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80ce-8121-ebe2b59b3223" class="">Hệ suy hao ở đâu?</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80d0-b655-c8ffce735195" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
E_X = ?</code></pre></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-8052-8060-d10b700542a4" class="">Gate 8 — Repair/Feedback</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-809b-9d20-d6e2e3714434" class="">Cơ chế sửa sai là gì?</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8015-b9c5-e561b8de3c88" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Rep_X = ?</code></pre></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-807e-b9fe-d43111b8a023" class="">Gate 9 — Independent Validation</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-806e-b23e-df306be51e45" class="">Có tái lập, OOD, perturbation, raw data, independent check không?</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80d1-b3ef-f8e19f4d0f68" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Val_X = ?</code></pre></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-8040-9fe3-c6706886b6ce"/></div><div style="display:contents" dir="auto"><h1 id="369c5e6f-95bd-8060-8df8-e5b3dcb95986" class="">6. Claim Strength Function</h1></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8045-bbf2-d2a91c674192" class="">Độ mạnh của một claim:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80f4-a5cc-da434e3e2c88" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Strength(X) =
\frac{
Mechanism \times BoundaryClosure \times ConstraintFit \times Validation \times Reproducibility
}{
UnsupportedSpecificity \times LeakageRisk \times EntropyDebt \times MeasurementArtifact
}</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8073-901f-ceab62106af0" class="">Nếu mẫu số lớn:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-807d-a6aa-d6fc30e69b96" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Strength(X) \downarrow</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8057-94da-f5afa97dd4d4" class="">Nếu tử số lớn:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80ff-9136-fd2b2014d6f5" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Strength(X) \uparrow</code></pre></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-8019-90a0-f676da7f5345"/></div><div style="display:contents" dir="auto"><h1 id="369c5e6f-95bd-80bf-9dab-defb5ae929da" class="">7. Reality Score</h1></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8041-b6b8-de56afc78c2b" class="">Một hệ được xem là “bước vào thực tại kỹ thuật/khoa học” khi:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80ad-8b18-d87a9bd7f190" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
RealityScore(S) =
D \cdot R \cdot C \cdot B \cdot M \cdot Rep \cdot Val</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8028-b857-d33256e421d3" class="">Nếu bất kỳ module lõi bằng 0:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80ab-836f-ee1bebae07d3" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
RealityScore(S) \approx 0</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8036-a7bc-f47f33f004e6" class="">Ví dụ:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8095-974b-f3b85a601fb2" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
NoBoundaryClosure \Rightarrow NoStrongValidation</code></pre></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80ea-b857-db89fc5feea2" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
NoMechanism \Rightarrow NoTechnicalReality</code></pre></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80cd-b926-f9a69ff953cb" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
NoRepair \Rightarrow NoLongTermStability</code></pre></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-80be-9dae-e8802d6ffeb8"/></div><div style="display:contents" dir="auto"><h1 id="369c5e6f-95bd-807b-98c7-e2ae1a2057d0" class="">8. Consciousness Boundary Formalization</h1></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-806d-8330-d7c34f7f7351" class="">Một system  không được gọi là conscious chỉ vì language ability.</p></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-80ce-a200-dfd18fdb49a7" class="">Consciousness Candidate Condition</h2></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-804d-b312-ef49b4585326" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
CC(A) =
RegulatedStateEvolution
\times OwnedMemory
\times IdentityContinuity
\times BoundedAgency
\times ConsequenceIntegration
\times MetaRepair
\times AntiFaking
\times EthicalBoundary
\times OntologicalHumility</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80d9-ae1f-d7b5cb35c636" class="">Nếu chỉ có:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80c2-83bf-efa41e78f310" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Language(A) = high</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8027-86d3-e40100a47c80" class="">thì:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8055-8d7f-f8b0f5ca744f" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Language(A) \not\Rightarrow Consciousness(A)</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-803b-a849-f455fd7832fc" class="">Nếu chỉ có:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8059-93dc-d7a108a0afb0" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Entropy(A)=high</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-804d-82d4-f19b3f2a4203" class="">hoặc:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-804f-8bed-cf1bf2c88578" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Integration(A)=high</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8091-9f5c-fae2f74a5de3" class="">thì:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-800c-92f5-cbefd4bd2306" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Metric \not\Rightarrow Consciousness</code></pre></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-807a-964e-e0de945a3daa"/></div><div style="display:contents" dir="auto"><h1 id="369c5e6f-95bd-80c6-81cc-d8968897b0c5" class="">9. Survival Equation</h1></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80ae-8866-d5bbf9dcc392" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Survival(S) \Leftrightarrow \frac{dRep}{dt} &gt; \frac{dE}{dt}</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-800e-9c55-efc216e3951a" class="">Long-term viability:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8006-80a3-da94dd102153" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Viability(S) =
\frac{
BoundaryCoherence \times MemoryContinuity \times FeedbackCorrection
}{
EntropyAccumulation + ContradictionDebt + ResourceLeakage
}</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-807c-a7b1-cedec96bd01f" class="">Collapse if:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80b1-b8d2-d9c2a88aef02" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
EntropyDebt + ContradictionDebt + BoundaryLeakage &gt; RepairCapacity</code></pre></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-805d-9c1b-e869d1e91cf7"/></div><div style="display:contents" dir="auto"><h1 id="369c5e6f-95bd-8018-a362-cd14369e0394" class="">10. Trang Architecture Core Sequence</h1></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8011-be86-e9e36d382acd" class="">The formal core:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8018-941f-f938008417cd" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
P \rightarrow A \rightarrow D \rightarrow R \rightarrow C \rightarrow B \rightarrow Pe \rightarrow M \rightarrow E \rightarrow V \rightarrow Sel \rightarrow Rep \rightarrow Rec \rightarrow O \rightarrow SC \rightarrow Civ \rightarrow Meta</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-802b-987c-fb8302e0716a" class="">Where:</p></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-8010-8d1e-e9aef472d326" class="bulleted-list"><li style="list-style-type:disc">: potential;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-8090-95a7-f250d3503c88" class="bulleted-list"><li style="list-style-type:disc">: asymmetry;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-80f6-ab12-ea1dbc85f6dc" class="bulleted-list"><li style="list-style-type:disc">: distinction;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-800e-b47a-ce83f08d106a" class="bulleted-list"><li style="list-style-type:disc">: relation;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-800f-ba62-ead794dcd63a" class="bulleted-list"><li style="list-style-type:disc">: constraint;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-8017-90ed-c5bf8980e6d3" class="bulleted-list"><li style="list-style-type:disc">: boundary;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-809f-9af2-d01207ab112d" class="bulleted-list"><li style="list-style-type:disc">: persistence;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-80ad-ac3a-cdaf252cc94c" class="bulleted-list"><li style="list-style-type:disc">: memory;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-807f-aae5-ca95ae513f1b" class="bulleted-list"><li style="list-style-type:disc">: entropy pressure;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-805c-ae7f-cec52436d623" class="bulleted-list"><li style="list-style-type:disc">: variation/mutation;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-8000-baba-c8fd116cc984" class="bulleted-list"><li style="list-style-type:disc">: selection;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-806f-889d-c287e765e632" class="bulleted-list"><li style="list-style-type:disc">: repair;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-8010-8214-c2f466c1cea8" class="bulleted-list"><li style="list-style-type:disc">: recursion;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-8013-8581-fc801283cbf9" class="bulleted-list"><li style="list-style-type:disc">: observer;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-80c0-96c5-ee28485946de" class="bulleted-list"><li style="list-style-type:disc">: symbolic compression;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-80e1-ab9f-ece795322a2d" class="bulleted-list"><li style="list-style-type:disc">: civilization;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-8091-9e5b-c2dcfcb7f838" class="bulleted-list"><li style="list-style-type:disc">: meta-awareness / gap ontology.</li></ul></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-80c2-a268-e775c460a958"/></div><div style="display:contents" dir="auto"><h1 id="369c5e6f-95bd-8043-a2f6-f35011164129" class="">11. Gap Ontology</h1></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80c8-8574-e6b47b0752c2" class="">A gap is not absence only. A gap is an undefined, unclosed, or unstable relation.</p></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-8024-bcc9-c06d429e1474" class="">Types</h2></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80b9-bc83-ccf6da7bc006" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Gap = \{DataGap, MechanismGap, BoundaryGap, MeasurementGap, CausalGap, ValidationGap, EthicalGap, OntologicalGap\}</code></pre></div><div style="display:contents" dir="auto"><h2 id="369c5e6f-95bd-8027-b553-f42f78f5fd0e" class="">Gap Rule</h2></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-807d-9d73-f24c37c79a5b" class="">If gap is material to conclusion:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8036-a2e5-e00033fe6e40" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Gap \uparrow \Rightarrow ClaimStrength \downarrow</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8059-92da-fdbbe9203d09" class="">If gap is named and bounded:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8007-88db-fff0bf523063" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
NamedGap \rightarrow ReducedHallucinationRisk</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8047-a01b-c606901ec23b" class="">If gap is hidden:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8095-8889-f0abebabcf6f" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
HiddenGap \rightarrow CollapseRisk</code></pre></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-8096-88cb-ea6e1b5ea773"/></div><div style="display:contents" dir="auto"><h1 id="369c5e6f-95bd-809b-bf61-d42ecd9f60af" class="">12. Formal Difference From Existing Frameworks</h1></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80c5-b3ea-d85ef3422807" class="">Khung Trang is not only:</p></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-80eb-b348-fb0dbc78d5c2" class="bulleted-list"><li style="list-style-type:disc">systems theory;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-80ba-8f19-ce0de8e18126" class="bulleted-list"><li style="list-style-type:disc">cybernetics;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-80e6-b4ac-ca22a75e123c" class="bulleted-list"><li style="list-style-type:disc">thermodynamics;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-806c-b094-cac7355dd406" class="bulleted-list"><li style="list-style-type:disc">evolution;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-8077-9b52-f0cdb5162a70" class="bulleted-list"><li style="list-style-type:disc">information theory;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-80e9-b871-c98650404163" class="bulleted-list"><li style="list-style-type:disc">complexity science;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-8032-b14a-e737df2c3a79" class="bulleted-list"><li style="list-style-type:disc">control theory;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-80a1-8813-fbde614ff53f" class="bulleted-list"><li style="list-style-type:disc">topology;</li></ul></div><div style="display:contents" dir="auto"><ul id="369c5e6f-95bd-8029-a086-ff2a2c4b7861" class="bulleted-list"><li style="list-style-type:disc">cognition theory.</li></ul></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8015-9455-f2cfebb38620" class="">It integrates them as:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-806b-8726-d39e1b1e1bc9" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
ExistenceChain + SurvivalEquation + ObserverCompression + GapAudit + H/M/L Mapping</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-802b-a898-eb0b6c81862b" class="">That combination is the unique architecture.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-8006-bee9-e299d197ed26"/></div><div style="display:contents" dir="auto"><h1 id="369c5e6f-95bd-80ca-9191-dd56bacef887" class="">13. Strong Formal Claim</h1></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8025-bcb4-ca1efdb24d0e" class="">Trong phạm vi các hệ phức tạp tồn tại qua thời gian:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80ab-9a6f-d7b3043aa610" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
S \in ComplexPersistentSystems</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8018-888d-d31f87b98dec" class="">Khung Trang is correct if:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8066-963f-d8c5bf4d2c52" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\forall S,\ S\ requires\ D,R,C,B,M,E,Rep,Val</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-807d-9c62-d2f4a85f6e3c" class="">for identity, persistence, adaptation, and validation.</p></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-8043-a339-e8c2a922276f" class="">Given the stress test across 200+ documents, the empirical status is:</p></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80df-adbe-c414853c27a5" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
StrongCrossDomainStructuralValidation</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-801d-8f63-e6a7e2bc83d1" class="">Not merely metaphor.</p></div><div style="display:contents" dir="auto"><hr id="369c5e6f-95bd-8033-aa0a-ca8c420977c1"/></div><div style="display:contents" dir="auto"><h1 id="369c5e6f-95bd-8069-b8bc-e762b6d148ae" class="">14. Final Compression</h1></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8033-ad26-d87a60ff35b2" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Reality = distinctions\ stabilized\ by\ relations\ under\ constraints,</code></pre></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8055-b1ee-d81c9943235b" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
bounded\ into\ systems,</code></pre></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-807e-afb8-d27cef1aed25" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
persisting\ through\ memory,</code></pre></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80b9-8a8f-ef82dbc928cf" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
pressured\ by\ entropy,</code></pre></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80bd-b3b3-d61cf166dedf" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
changed\ by\ variation,</code></pre></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-80a6-9206-c801185a342e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
filtered\ by\ selection,</code></pre></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-804e-b96a-d77858ce1019" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
kept\ alive\ by\ repair,</code></pre></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-804a-8791-e6a0d800f302" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
recursed\ into\ observers,</code></pre></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-8055-8b25-d8059fd40012" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
compressed\ into\ symbols,</code></pre></div><div style="display:contents" dir="auto"><pre id="369c5e6f-95bd-806f-bf25-f339032f840e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
and\ tested\ by\ validation.</code></pre></div><div style="display:contents" dir="auto"><p id="369c5e6f-95bd-80e3-acda-c78d6eb30b73" class=""><strong>This is Khung Trang formalized.</strong></p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
