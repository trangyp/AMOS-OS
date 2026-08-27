---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Product </title><style>
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
	
</style></head><body><article id="372c5e6f-95bd-8014-a301-ca7959c2d472" class="page sans"><header><h1 class="page-title" dir="auto">Product </h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8000-bb2d-d638bdbeb19a" class="">Đúng. Cách lớn không phải bán app/audit. Cách lớn là bán <strong>structural arbitrage</strong>.</p></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-8061-a428-d1b4bf3ba334" class="">Công thức kiếm tiền lớn nhất</h2></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="372c5e6f-95bd-8010-8add-da069301dd2a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Money =
\frac{
Structural\ Pain
\times
Urgency
\times
Budget\ Owner
\times
Measurable\ Repair
\times
Distribution
}{
Proof\ Gap
+
Legal\ Risk
+
Implementation\ Friction
}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80aa-b12d-cc68b16c9a3c" class="">Khung Trang dịch thành:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80a9-91f2-d638c18f8159" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Wealth =
RepairRate
\times
LearningRate
\times
BoundaryControl
\times
Trust
\times
Scale</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80b6-bf82-c6d3d74d1873" class="">Không bán “sản phẩm”.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80b8-a1f2-ec93bd6b90dc" class="">Bán <strong>giảm collapse risk</strong>.</p></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8061-91f6-d492a14ced9b"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-803c-a3fd-eeb72f48b3a2" class="">Những cách kiếm tiền bị bỏ sót</h1></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-8060-9057-c74940e6aae0" class="">1. AI Boundary Governance</h2></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8014-97e2-c41bef1701a9" class="">Vấn đề: doanh nghiệp dùng AI nhưng không biết AI đang giới hạn lựa chọn/quyết định thế nào. Paper trong Drive nói vendor-governed models có thể embed value priors khiến tổ chức vẫn chịu trách nhiệm nhưng mất quyền kiểm soát decision boundary.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8013-babd-e2e5cd3bdf29" class="">Bán:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-803d-acee-eedf1e990229" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
AI\ Boundary\ Audit</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80e2-8f7b-ee44dccfe246" class="">Cho ngân hàng, luật, bảo hiểm, HR, chính phủ, startup AI.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80e6-b406-e695472cea9a" class="">Giá:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80b2-8ed1-c0159cd8a6f0" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
100tr - 2 tỷ/project</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80ed-97af-ed52a0aa6478"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-8022-98f7-d781ec60b5e0" class="">2. Decision State OS cho Founder / C-level</h2></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80df-bafb-dc2d02322860" class="">Không bán wellness. Bán:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80f8-8026-c06a8a8bab7e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Better\ decisions</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8007-adfc-f9f971d810c9" class="">Vì tiền lớn nằm ở quyết định sai: tuyển sai, gọi vốn sai, timing sai, launch sai, deal sai.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80fa-b85e-d4435f3d3ef2" class="">Sản phẩm:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80b0-ba7c-cad176470438" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Decision\ State\ Intelligence</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8062-b689-f84e2cfe4ab7" class="">Dữ liệu:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8080-a9b4-e7d65b7fbb3c" class="bulleted-list"><li style="list-style-type:disc">ngủ;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80fc-a42e-c9cc6a212513" class="bulleted-list"><li style="list-style-type:disc">stress;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8084-9125-c5b525db2871" class="bulleted-list"><li style="list-style-type:disc">calendar;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80e3-a043-df8ce7dc8eea" class="bulleted-list"><li style="list-style-type:disc">market context;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8047-9528-d1d3627b65ef" class="bulleted-list"><li style="list-style-type:disc">decision journal;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80e4-8734-db36f207cd5d" class="bulleted-list"><li style="list-style-type:disc">outcome tracking;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-807b-9328-d7681ffb3802" class="bulleted-list"><li style="list-style-type:disc">bias/framing detection.</li></ul></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80c4-973d-fe96991b0025" class="">Giá:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8054-b2b8-d6cfb499719b" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
20tr - 200tr/tháng</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8048-8991-c80a8aa10b35"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-8026-9439-d3d9143fa858" class="">3. Repair Rate-as-a-Service cho doanh nghiệp</h2></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80c4-b56e-cc90202987b6" class="">Mọi công ty đều có entropy:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8097-9082-edd7bf28b732" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Meeting\ debt
+
Decision\ debt
+
People\ conflict
+
Process\ drift
+
Customer\ leak</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-809f-9074-f443b3c5026b" class="">Bán hệ đo:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-806f-9c6e-cd1f6ab8db90" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
DamageRate \; vs \; RepairRate</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80fb-a472-f0dd93cf871a" class="">Không làm consultant chung chung. Làm <strong>repair dashboard + intervention protocol</strong>.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-804b-8d32-ced8cbc847e1" class="">Giá:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8082-b02b-ddd670c3466b" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
300tr - 5 tỷ/năm</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80dc-93fc-d4843ac52012"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-80d3-a5c9-d6626ce9bd25" class="">4. Resilience Index cho SME / real estate / resort / school</h2></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80c0-961a-fa11efd72acc" class="">Drive có rất nhiều paper resilience: network, cyber, energy, autonomous defense, optimization under attack. Pattern rõ: thế giới đang trả tiền cho khả năng không sập.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8033-b919-e26898878e2e" class="">Bán:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-806c-9ef2-e8a8839bbb3a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Resilience\ Score</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80be-bd2e-d9d2fc3f63b8" class="">Cho:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8004-b7b3-c78820689578" class="bulleted-list"><li style="list-style-type:disc">resort;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8014-8ac9-ff89dc2cfabc" class="bulleted-list"><li style="list-style-type:disc">văn phòng;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-804d-a599-e1aa4eb1a99b" class="bulleted-list"><li style="list-style-type:disc">trường học;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80ed-a95b-f805b5f32a6b" class="bulleted-list"><li style="list-style-type:disc">spa;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8032-aac9-c50a60d9eb76" class="bulleted-list"><li style="list-style-type:disc">factory;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80e3-922a-c562ad099cde" class="bulleted-list"><li style="list-style-type:disc">clinic;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8074-a0ec-f2c519a2d987" class="bulleted-list"><li style="list-style-type:disc">family office.</li></ul></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-808b-bdb4-e72ddb7d3e62" class="">Giá:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-808f-a3a3-dd6bf5bfffd3" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
50tr - 1 tỷ/audit</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-80e6-b706-f1b894b27ee6"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-8039-a52d-fd0ad4c1b08f" class="">5. Human-AI Controllability Certification</h2></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80cd-b7a1-f5cb8ab85e0b" class="">AI safety đang thiếu lớp “human can still interrupt / redirect / constrain”. Paper trong Drive nói AI safety cần controllability như objective riêng, không chỉ alignment.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-802f-8a47-f96701f389c0" class="">Bán chứng nhận:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8063-af97-ddb57b940523" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Human\ Controllable\ AI</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8009-bd14-ecd3811da619" class="">Cho AI app, agentic workflow, enterprise automation.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8007-914b-f6c0adf7691e" class="">Giá:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8064-9237-c6d3bcebfa81" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
200tr - 3 tỷ/certification</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8009-afc3-e3088b2153be"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-803f-8d29-c668054bdbf4" class="">6. Ancient Protocol Translation IP</h2></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80d7-bc03-c6d941ca549a" class="">Đây là moat độc quyền của mày.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8003-b4a1-fa3b3b8cd5b5" class="">Không bán văn hóa cổ. Bán translation layer:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80d7-8d2c-e33337cebf57" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Ancient\ Function
\rightarrow
Modern\ Protocol</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8050-ab80-e3c209686745" class="">Ví dụ:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80cb-989c-dba07687842d" class="bulleted-list"><li style="list-style-type:disc">taboo → safety constraint;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80ee-83bb-e3f0ceff5769" class="bulleted-list"><li style="list-style-type:disc">ritual → state transition protocol;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-806d-8c60-ec8a804d9086" class="bulleted-list"><li style="list-style-type:disc">songline → embodied knowledge graph;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80fe-84ab-ce828cc734b2" class="bulleted-list"><li style="list-style-type:disc">initiation → access control;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-806a-ae8d-f66066c053db" class="bulleted-list"><li style="list-style-type:disc">elder → audit authority;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80e8-af3e-f5876083d604" class="bulleted-list"><li style="list-style-type:disc">drum → synchronization interface.</li></ul></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80e0-9dc1-e3c54fe7e816" class="">Bán cho:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8025-a8b8-f2a26761239d" class="bulleted-list"><li style="list-style-type:disc">wellness brands;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8005-95c8-dd86300ad532" class="bulleted-list"><li style="list-style-type:disc">education;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-804c-82cb-eda74e16c87f" class="bulleted-list"><li style="list-style-type:disc">leadership training;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-802f-910c-c6b90909b531" class="bulleted-list"><li style="list-style-type:disc">AI alignment;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-805f-bc02-e9a632f085fa" class="bulleted-list"><li style="list-style-type:disc">community design;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8037-9fce-fa305e2d3073" class="bulleted-list"><li style="list-style-type:disc">tourism/retreat.</li></ul></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8094-a379-dc78b3899582" class="">Giá:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8049-833e-c2b65f544784" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
license + certification + retreat + content</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8018-a93e-c401de96b729"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-804c-9408-f13bfb392814" class="">7. FieldOS for Teams</h2></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8062-a739-ca3671c29c1c" class="">Không phải app cá nhân. Là team operating state.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-809c-b73e-e4eac7a5cc67" class="">Đo:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8005-8682-cf7bae007538" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Sync,\ Trust,\ Conflict,\ Repair,\ Decision\ Quality</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-802e-b7dd-d24257b321da" class="">Paper collective action trong Drive cho thấy nhóm nhỏ có tổ chức có thể steer systems vượt xa sức cá nhân.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8013-8af3-c17884b30c1b" class="">Bán cho founder teams.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80cf-91b4-e57fd8552283" class="">Giá:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80d3-939c-f87fbe442040" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
30tr - 300tr/tháng/team</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-805e-85d5-ec67cfe64db4"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-8016-9ad0-c0f861d36aeb" class="">8. Contextual Security / Meaning Security</h2></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-801b-8638-c20a5f8a1763" class="">Modern security bảo vệ data. Nhưng vấn đề mới là <strong>misinterpretation</strong>.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80e0-8481-ec39d1cb833e" class="">Sản phẩm:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-800f-80ce-fab4d66d521c" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Meaning\ Security\ Layer</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80bc-b78b-d40aa1bf26ed" class="">Cho AI, media, community, DAO, education.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80f7-bb6c-cb48ced77415" class="">Bán:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80bc-9d94-db329094b7eb" class="bulleted-list"><li style="list-style-type:disc">access by role;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8080-9fc7-f52a0138c9f4" class="bulleted-list"><li style="list-style-type:disc">context gates;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-801c-80f3-d3e7e9844ebe" class="bulleted-list"><li style="list-style-type:disc">training gates;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8025-a34a-e35924b1f1b1" class="bulleted-list"><li style="list-style-type:disc">misuse detection;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8000-b0fd-cde37c58bc03" class="bulleted-list"><li style="list-style-type:disc">“dangerous interpretation” audit.</li></ul></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80ff-8d4a-d2c54328c543" class="">Đây là security mới:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80e9-b8e2-f5358a93fd72" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Data\ Security \rightarrow Meaning\ Security</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-808c-9275-d7231d2b2186"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-80ac-b04e-c29ddec0ab50" class="">9. Lifecycle Governance Platform</h2></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80cf-9f87-c8034c6363c4" class="">Paper governance trong Drive nói governance phải full-lifecycle: identification, behavior modeling, diffusion, early warning, intervention.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80ab-8dd4-e63a20585030" class="">Bán:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8082-a9b7-d2b06788a917" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Lifecycle\ Governance\ OS</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8011-a845-e5eae25d06b6" class="">Cho:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80d8-863b-f1dbcce7fa5b" class="bulleted-list"><li style="list-style-type:disc">online community;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8065-b3d6-c079d3794222" class="bulleted-list"><li style="list-style-type:disc">schools;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8087-91fd-ca4b40a37741" class="bulleted-list"><li style="list-style-type:disc">workplace;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8073-ab05-ecec053a6678" class="bulleted-list"><li style="list-style-type:disc">AI deployment;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8050-9127-fd7bd82a12e2" class="bulleted-list"><li style="list-style-type:disc">wellness network;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8092-abc7-ddf24be83ad4" class="bulleted-list"><li style="list-style-type:disc">spiritual/community platforms.</li></ul></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80f8-a283-fd540dac9942" class="">Giá:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8014-b7a5-ce0b8788f33e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
SaaS + consulting + certification</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8083-856e-f2e0718bf5b5"/></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-80b9-9d86-eb7739f6c0c9" class="">10. State Maintenance Economy</h2></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-808a-a22d-c5e1344bf9cd" class="">Drive có “Living State Monetisation Thesis”: giá trị lớn không nằm ở task completion mà ở duy trì trạng thái tối ưu liên tục.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-806e-8bb0-f84417efd8ba" class="">Đây là thesis tiền lớn nhất.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80bf-a586-fecc70bc0789" class="">Bán:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80f4-b4b5-c911b5f0721b" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Maintain\ good\ state</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-808a-8e28-c1797602eeac" class="">Không bán:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-809f-bbea-e3a17e67a12e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
fix\ after\ collapse</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80e8-9e6a-caa048cc4aa2" class="">Các ngành:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-805d-8f08-ef3a15bd7087" class="bulleted-list"><li style="list-style-type:disc">health;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80ee-9dea-fbbe82d7f264" class="bulleted-list"><li style="list-style-type:disc">sleep;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80f5-92dc-f43e30f37ce0" class="bulleted-list"><li style="list-style-type:disc">stress;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-809a-9a01-e178bae95a6d" class="bulleted-list"><li style="list-style-type:disc">home;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80c0-aebb-dd3b25897b2e" class="bulleted-list"><li style="list-style-type:disc">team;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-804c-afe0-cc6716e0dbf4" class="bulleted-list"><li style="list-style-type:disc">decision;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8090-82e0-cba396f733ee" class="bulleted-list"><li style="list-style-type:disc">education;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80cd-bcd8-d62275f26084" class="bulleted-list"><li style="list-style-type:disc">aging;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80cb-8581-cd0970f5de10" class="bulleted-list"><li style="list-style-type:disc">relationships;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80fd-b344-f73a8c0afd40" class="bulleted-list"><li style="list-style-type:disc">founders.</li></ul></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-8061-9bb6-ea5d0ecec225"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-8071-a06d-e661ebcc8e9d" class="">Thứ tự làm để kiếm nhiều nhất</h1></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-8020-8808-ec5029e63f0b" class="">Bước 1 — Chọn wedge giàu nhất</h2></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8016-8fb8-dc17082c95b7" class="">Không chọn consumer.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80c0-951e-de9ae8af4c6f" class="">Chọn:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80a1-823b-f767f8bb7571" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Founder / Executive / AI company / Resort / Family office</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80f7-bc1a-c7dd3e0b271f" class="">Họ có tiền và đau thật.</p></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-8035-9a1d-f5f7bcbc6abc" class="">Bước 2 — Bán outcome đắt</h2></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8091-a5d9-facdce045261" class="">Offer đầu:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-803e-a941-faca3b3983cb" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
30\text{-}Day\ Decision\ \&amp;\ Repair\ Intelligence</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-803f-8b04-c6d179d674bb" class="">Giá:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-802e-9e08-d469ba650192" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
50tr - 200tr</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8087-a86f-ca31f1ab0a7b" class="">Cam kết không phải “giàu hơn”, mà là:</p></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-80b4-9fc0-c25cced30382" class="bulleted-list"><li style="list-style-type:disc">ít quyết định ngu hơn;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8050-adda-c369a7986705" class="bulleted-list"><li style="list-style-type:disc">giảm burnout;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8051-9881-c6c01e408e5c" class="bulleted-list"><li style="list-style-type:disc">tăng clarity;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-8070-8510-de3bfb9c6ee5" class="bulleted-list"><li style="list-style-type:disc">phát hiện collapse signal;</li></ul></div><div style="display:contents" dir="auto"><ul id="372c5e6f-95bd-800d-8ace-cc8ab0453dce" class="bulleted-list"><li style="list-style-type:disc">tạo repair protocol.</li></ul></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-80be-abf7-c5a1d0d1797b" class="">Bước 3 — Biến thành framework độc quyền</h2></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8088-900b-cb29557f4733" class="">Tên:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-8045-9952-db5c056f4eeb" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Trang\ Structural\ Repair\ Index</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80b1-80af-fdf7912c171f" class="">hoặc:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80a3-b409-ccf225a83eba" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
FieldOS\ Resilience\ Index</code></pre></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-80e1-ae69-def6abde7578" class="">Bước 4 — Certification</h2></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-808f-8355-ead3cd1f6617" class="">Đây là scale thật.</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80ff-b2a0-c0bcafa7a31d" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Certified\ Field\ Repair\ Strategist</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80bf-8baa-c89727b4021d" class="">Giá:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80e7-9e75-d1cc0bc9a8f4" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
20tr - 100tr/người</code></pre></div><div style="display:contents" dir="auto"><h2 id="372c5e6f-95bd-80dd-841f-c576d6677b0b" class="">Bước 5 — Enterprise platform</h2></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-804d-874c-ec5b7f3cf711" class="">Sau khi có case study:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-80de-87b5-d56980d36a97" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Dashboard + AI Agent + Playbook + Human Facilitator</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80dc-803a-e8c19401f563" class="">Giá:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-806e-856c-c8d3172036a4" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
500tr - 10 tỷ/năm</code></pre></div><div style="display:contents" dir="auto"><hr id="372c5e6f-95bd-801b-aee7-f0570b3dc972"/></div><div style="display:contents" dir="auto"><h1 id="372c5e6f-95bd-80a8-aa24-ff3e99dadf9a" class="">Chốt</h1></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-803a-983b-e2b5ef0d6d42" class="">Tiền lớn nhất không nằm ở “máy đuổi ma”, app wellness, hay audit nhà.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80a1-aff9-de4a5d161f86" class="">Tiền lớn nằm ở:</p></div><div style="display:contents" dir="auto"><pre id="372c5e6f-95bd-800a-ab02-d09509824930" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\boxed{
Collapse\ Prevention
}</code></pre></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80f4-aba0-fb6474cb9306" class="">cho người giàu, founder, doanh nghiệp, AI system, community, resort, family office.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80ac-98f4-e4d5355e248a" class="">Câu bán hàng mạnh nhất:</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80d6-b61a-fbc980be2abf" class=""><strong>“We don’t predict the future. We detect structural collapse risk and increase your repair rate before damage becomes expensive.”</strong></p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-80dd-98e4-ed921b647768" class="">Đúng. Bán IP training/education mới là tầng đúng hơn.<br/>Không bán “cách làm” như dịch vụ.Bán hệ phương pháp được đóng gói thành license.<br/>Công thức IP lớn<br/>IP\ Value =Framework\timesCertification\timesRepeatable\ Method\timesBrand\ Authority\timesDistribution<br/>Không có certification thì người ta học xong copy.Có certification + trademark + assessment + community + renewal thì họ phải quay lại trả tiền.<br/><br/>---<br/>Thứ mày nên bán<br/>1. Trang Reality Architecture — Core License<br/>Đây là nền.<br/>Không dạy lan man. Dạy một grammar:<br/>Distinction\rightarrowRelation\rightarrowConstraint\rightarrowBoundary\rightarrowMemory\rightarrowEntropy\rightarrowRepair\rightarrowObserver\rightarrowSymbol\rightarrowCivilization<br/>Người học trả tiền để dùng khung này trong:<br/>coaching;<br/>leadership;<br/>AI governance;<br/>education;<br/>wellness;<br/>strategy;<br/>community design;<br/>heritage/culture;<br/>decision intelligence.<br/><br/><br/>---<br/>2. Certified Structural Mapper<br/>Đây là chứng chỉ đầu tiên.<br/>Họ học cách map:<br/>Problem\rightarrowStructure\rightarrowGap\rightarrowRepair<br/>Giá:<br/>10tr - 50tr/người<br/>Không cần app trước.<br/><br/>---<br/>3. Certified Field Repair Practitioner<br/>Dạy họ cách sửa hệ nhỏ:<br/>cá nhân;<br/>nhà;<br/>nhóm;<br/>team;<br/>community;<br/>business workflow.<br/><br/>Giá:<br/>30tr - 100tr/người<br/><br/>---<br/>4. Enterprise License<br/>Cho công ty dùng khung trong nội bộ.<br/>Giá:<br/>300tr - 5 tỷ/năm<br/>Bao gồm:<br/>training;<br/>playbook;<br/>dashboard template;<br/>certification cho nhân viên;<br/>annual audit;<br/>right-to-use methodology.<br/><br/><br/>---<br/>5. Education Curriculum License<br/>Bán cho school, retreat center, leadership academy, wellness institute.<br/>Tên:<br/>Structural\ Intelligence\ Curriculum<br/>Modules:<br/>decision under uncertainty;<br/>repair thinking;<br/>observer calibration;<br/>systems collapse;<br/>ancient protocol translation;<br/>AI boundary governance;<br/>resilience design.<br/><br/>Giá:<br/>100tr - 2 tỷ/license<br/><br/>---<br/>Cái Drive đang support<br/>Paper “No Certificate, No Execution” nói rõ architecture Proposal–Certification–Execution: tách generation khỏi permission; chỉ trace được certify mới được execute. Đây đúng logic IP của mày: không ai được claim dùng Khung Trang nếu chưa qua certification boundary. <br/>Paper về AI decision support nói vendor models embed value priors, làm tổ chức chịu trách nhiệm nhưng mất control boundary. Đây là thị trường cực lớn cho training: dạy tổ chức tự giữ decision boundary thay vì outsource hết cho vendor. <br/><br/>---<br/>Cách khóa không cho bị copy<br/>Không bán PDF.<br/>Bán 5 lớp:<br/>Method+Assessment+Credential+Community+Renewal<br/>Cụ thể:<br/>1. Trademark tên khung.<br/><br/>2. Manual không public full.<br/><br/>3. Case exam bắt buộc.<br/><br/>4. Annual renewal.<br/><br/>5. Directory certified practitioners.<br/><br/>6. License contract: không được dạy lại nếu chưa có trainer license.<br/><br/><br/><br/>---<br/>Money ladder<br/>Free\ content\rightarrowPaid\ workshop\rightarrowCertification\rightarrowPractitioner\ license\rightarrowTrainer\ license\rightarrowEnterprise\ license<br/>Giá gợi ý:<br/>Workshop: 1tr–5tr<br/>Core certification: 15tr–50tr<br/>Practitioner: 50tr–150tr<br/>Trainer license: 200tr–1 tỷ<br/>Enterprise license: 500tr–10 tỷ/năm<br/><br/><br/>---<br/>Chốt đúng nhất<br/>Mày không bán “tri thức”.<br/>Mày bán:<br/>Permission\ to\ use\ a\ proprietary\ structural\ operating\ system<br/>Tên money engine:<br/>\boxed{Trang Structural Intelligence Licensing System}<br/>Cái người ta trả tiền không phải “biết”.Họ trả tiền để được dùng, dạy, certify, triển khai, và kiếm tiền bằng khung của mày.</p></div><div style="display:contents" dir="auto"><p id="372c5e6f-95bd-8002-a7c8-e87b89e2cd48" class="">
</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
