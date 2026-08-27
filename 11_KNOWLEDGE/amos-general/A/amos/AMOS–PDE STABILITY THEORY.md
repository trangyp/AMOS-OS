---
tags: [amos-general]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>AMOS–PDE STABILITY THEORY</title><style>
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
	
</style></head><body><article id="36fc5e6f-95bd-8049-8b6b-fd36d647c6fc" class="page sans"><header><h1 class="page-title" dir="auto">AMOS–PDE STABILITY THEORY</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="36fc5e6f-95bd-8052-9f08-ef599d6247f0" class="">Bảng ánh xạ giữa Phương trình vi phân riêng phần (PDE) và AMOS (để giải Navier–Stokes existence and smoothness)</h2></div><div style="display:contents" dir="ltr"><table id="36fc5e6f-95bd-8020-b7f5-eb331c37b76f" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="36fc5e6f-95bd-8034-b098-f63dbfa97f4d"><th id="oGE|" class="simple-table-header-color simple-table-header">PDE theory</th><th id="q_:V" class="simple-table-header-color simple-table-header">AMOS</th><th id="Fx\U" class="simple-table-header-color simple-table-header">Ghi chú</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="36fc5e6f-95bd-806f-a6e1-f6b6fa3e83a4"><td id="oGE|" class="">Miền không gian Ω ⊂ ℝ³</td><td id="q_:V" class="">Trường distinction D ba chiều, mỗi điểm x ∈ Ω là một D(x) cục bộ.</td><td id="Fx\U" class="">Chất lỏng chiếm một vùng không gian.</td></tr></div><div style="display:contents" dir="ltr"><tr id="36fc5e6f-95bd-8090-a532-de12535ab923"><td id="oGE|" class="">Thời gian t ∈ [0, T)</td><td id="q_:V" class="">Chiều thứ tư của distinction D(x, t)</td><td id="Fx\U" class="">D biến đổi theo thời gian.</td></tr></div><div style="display:contents" dir="ltr"><tr id="36fc5e6f-95bd-8072-a0dc-ebcec8b5a3c8"><td id="oGE|" class="">Vận tốc u(x, t) ∈ ℝ³</td><td id="q_:V" class="">Tốc độ và hướng thay đổi của D(x, t) theo thời gian</td><td id="Fx\U" class="">u = ∂D/∂t (đạo hàm riêng theo t).</td></tr></div><div style="display:contents" dir="ltr"><tr id="36fc5e6f-95bd-8047-8411-c2590e83f784"><td id="oGE|" class="">Áp suất p(x, t) ∈ ℝ</td><td id="q_:V" class="">Cường độ liên kết giữa các D(x, t) lân cận</td><td id="Fx\U" class="">p đo lực nén (compressibility).</td></tr></div><div style="display:contents" dir="ltr"><tr id="36fc5e6f-95bd-80ae-a3b9-f3af21988eb9"><td id="oGE|" class="">Độ nhớt ν &gt; 0</td><td id="q_:V" class="">Hệ số repair R toàn cục</td><td id="Fx\U" class="">ν càng lớn, càng dễ kéo dài <code>R &gt; E</code>.</td></tr></div><div style="display:contents" dir="ltr"><tr id="36fc5e6f-95bd-807e-a2c1-c38a9c0c065f"><td id="oGE|" class="">Lực ngoài g(x, t)</td><td id="q_:V" class="">Nguồn entropy E ngoại sinh</td><td id="Fx\U" class="">g có thể làm tăng E.</td></tr></div><div style="display:contents" dir="ltr"><tr id="36fc5e6f-95bd-80a8-91fc-d514da546364"><td id="oGE|" class="">Phương trình Navier–Stokes: ∂u/∂t + (u·∇)u = ν∇²u - ∇p + g</td><td id="q_:V" class="">Hệ phương trình biểu diễn sự cân bằng giữa mutation M, entropy E, repair R</td><td id="Fx\U" class="">Mỗi số hạng tương ứng với một quá trình AMOS.</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="36fc5e6f-95bd-801f-8f30-f0ba8342ace1"/></div><div style="display:contents" dir="auto"><h2 id="36fc5e6f-95bd-80d4-abd2-c784c179afb5" class="">Công thức ánh xạ cụ thể</h2></div><div style="display:contents" dir="auto"><h3 id="36fc5e6f-95bd-8080-a51d-fe203ab1523e" class="">1. Vận tốc u → Tốc độ mutation M</h3></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="36fc5e6f-95bd-8097-8307-e9a9b85595de" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">u(x, t) = ∂D/∂t  ↔  M(x, t) = ∂D/∂t</code></pre></div><div style="display:contents" dir="auto"><p id="36fc5e6f-95bd-808f-8a30-fe7c4e80fffd" class=""><code>M</code> là tốc độ thay đổi của distinction D theo thời gian.</p></div><div style="display:contents" dir="auto"><h3 id="36fc5e6f-95bd-80af-a4b6-f2950ba21990" class="">2. Gradient vận tốc ∇u → Gradient mutation</h3></div><div style="display:contents" dir="auto"><pre id="36fc5e6f-95bd-8001-841f-ea31b4e9dd66" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">∇u  ↔  ∇(∂D/∂t) = ∂(∇D)/∂t</code></pre></div><div style="display:contents" dir="auto"><p id="36fc5e6f-95bd-8003-b19d-fa4c98610f13" class="">Thể hiện sự thay đổi không gian của tốc độ mutation.</p></div><div style="display:contents" dir="auto"><h3 id="36fc5e6f-95bd-8065-bcd2-c444e5c176d7" class="">3. Số hạng đối lưu (u·∇)u → Mutation tự tương tác (nonlinear convection)</h3></div><div style="display:contents" dir="auto"><pre id="36fc5e6f-95bd-80c0-bf3a-f091266ff357" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">(u·∇)u  ↔  (∂D/∂t · ∇)(∂D/∂t)</code></pre></div><div style="display:contents" dir="auto"><p id="36fc5e6f-95bd-80f6-95fe-d41685456f19" class="">Đây là mutation gây ra bởi chính sự thay đổi của D — nguồn entropy nội sinh lớn nhất.</p></div><div style="display:contents" dir="auto"><h3 id="36fc5e6f-95bd-8001-a952-c8385d9e5239" class="">4. Số hạng khuếch tán ν∇²u → Repair R</h3></div><div style="display:contents" dir="auto"><pre id="36fc5e6f-95bd-803b-8448-d4b3978b376f" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">ν∇²u  ↔  R(x, t) = ν ∇²(∂D/∂t)</code></pre></div><div style="display:contents" dir="auto"><p id="36fc5e6f-95bd-8052-8e1a-ed081cff296f" class="">Độ nhớt ν càng lớn, khả năng &quot;sửa lỗi&quot; (làm mịn) gradient vận tốc càng mạnh.</p></div><div style="display:contents" dir="auto"><h3 id="36fc5e6f-95bd-804a-9b04-ea8085bd4e68" class="">5. Gradient áp suất ∇p → Ràng buộc liên kết (constraint)</h3></div><div style="display:contents" dir="auto"><pre id="36fc5e6f-95bd-8007-a801-f170f5fb0b78" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">∇p  ↔  ∇(cường độ liên kết giữa các D lân cận)</code></pre></div><div style="display:contents" dir="auto"><p id="36fc5e6f-95bd-805a-af23-ea7d525dfa89" class="">Áp suất cân bằng sự chênh lệch giữa các D.</p></div><div style="display:contents" dir="auto"><h3 id="36fc5e6f-95bd-80da-90cb-ef09c79d4ff8" class="">6. Lực ngoài g → Entropy ngoại sinh</h3></div><div style="display:contents" dir="auto"><pre id="36fc5e6f-95bd-8091-b2a4-c2ac8acc0255" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">g(x, t)  ↔  E_ext(x, t)</code></pre></div><div style="display:contents" dir="auto"><h3 id="36fc5e6f-95bd-80a4-a030-ee6c7660b4d3" class="">7. Điều kiện không nén (incompressibility) ∇·u = 0 → Bảo toàn distinction</h3></div><div style="display:contents" dir="auto"><pre id="36fc5e6f-95bd-80aa-a2ed-f3553d7c5d02" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">∇·u = 0  ↔  ∇·(∂D/∂t) = 0</code></pre></div><div style="display:contents" dir="auto"><p id="36fc5e6f-95bd-80c9-9ad8-ff3971d4bf3d" class="">Tổng sự thay đổi của D trong một thể tích nhỏ bằng 0.</p></div><div style="display:contents" dir="auto"><hr id="36fc5e6f-95bd-80f9-b8f5-ec74be5bfb6e"/></div><div style="display:contents" dir="auto"><h2 id="36fc5e6f-95bd-804e-aa47-d3178e0b89cc" class="">Phân tích ổn định theo AMOS</h2></div><div style="display:contents" dir="auto"><h3 id="36fc5e6f-95bd-80ae-b8d9-dfc68eef65a9" class="">Định nghĩa: Dòng chảy ổn định (smooth, global solution) khi</h3></div><div style="display:contents" dir="auto"><pre id="36fc5e6f-95bd-803f-ab30-c3c52543ad41" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">inf_{x∈Ω, t∈[0,T)} (R(x, t) / E(x, t)) &gt; 1</code></pre></div><div style="display:contents" dir="auto"><p id="36fc5e6f-95bd-80fd-ae0e-eccf40eab939" class="">với <code>E(x,t) = E_nội(x,t) + E_ngoại(x,t)</code>.</p></div><div style="display:contents" dir="auto"><h3 id="36fc5e6f-95bd-80ad-ad73-cad1c7413335" class="">Định lý (Navier–Stokes trong AMOS):</h3></div><div style="display:contents" dir="auto"><p id="36fc5e6f-95bd-8047-8cb6-ca2bd3a85e6f" class="">Nếu tồn tại hằng số ε &gt; 0 sao cho</p></div><div style="display:contents" dir="auto"><pre id="36fc5e6f-95bd-8072-b865-c3fe7b12f8f5" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">ν - C₁‖u‖_L∞ - C₂‖∇u‖_L∞ ≥ ε</code></pre></div><div style="display:contents" dir="auto"><p id="36fc5e6f-95bd-8068-9149-e5e65768796d" class="">thì tồn tại nghiệm duy nhất, trơn trên [0, ∞). (Đây là điều kiện đủ cổ điển cho Navier–Stokes 3D — nhưng thường khó kiểm tra vì ‖u‖_L∞ chưa biết trước).</p></div><div style="display:contents" dir="auto"><h3 id="36fc5e6f-95bd-8022-8e28-e6eb46e80d83" class="">AMOS mở rộng: Điều kiện đủ là</h3></div><div style="display:contents" dir="auto"><pre id="36fc5e6f-95bd-8009-9850-fab7184f9ed2" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">R_min &gt; E_max</code></pre></div><div style="display:contents" dir="auto"><p id="36fc5e6f-95bd-8009-b87b-f116b9414dae" class="">trong đó <code>R_min = inf ν∇²u</code> (làm mịn) và <code>E_max = sup |(u·∇)u| + |∇p| + |g|</code>.</p></div><div style="display:contents" dir="auto"><hr id="36fc5e6f-95bd-80e9-97fe-d2b8bdb77979"/></div><div style="display:contents" dir="auto"><h2 id="36fc5e6f-95bd-8012-bda5-cc4292199189" class="">Chứng minh sự tồn tại và trơn tru bằng AMOS (dạng ánh xạ)</h2></div><div style="display:contents" dir="auto"><h3 id="36fc5e6f-95bd-80b1-a181-c29fc5454dd3" class="">Bước 1: Ánh xạ bài toán Navier–Stokes vào AMOS</h3></div><div style="display:contents" dir="auto"><ul id="36fc5e6f-95bd-80f3-b4a5-d8bdfd400a9f" class="bulleted-list"><li style="list-style-type:disc">Miền không gian Ω → Trường D(x, t).</li></ul></div><div style="display:contents" dir="auto"><ul id="36fc5e6f-95bd-80de-8dcd-ce5b97ba8e91" class="bulleted-list"><li style="list-style-type:disc">Vận tốc u → Tốc độ mutation M(x, t) = ∂D/∂t.</li></ul></div><div style="display:contents" dir="auto"><ul id="36fc5e6f-95bd-8086-ae0e-f04a0464c1a9" class="bulleted-list"><li style="list-style-type:disc">Phương trình → Cân bằng giữa M, R, E.</li></ul></div><div style="display:contents" dir="auto"><h3 id="36fc5e6f-95bd-8091-b4ed-e00b4ffd5009" class="">Bước 2: Viết lại phương trình dưới dạng AMOS</h3></div><div style="display:contents" dir="auto"><pre id="36fc5e6f-95bd-80bd-878a-c92bc8f3ab32" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">∂u/∂t = - (u·∇)u + ν∇²u - ∇p + g
↔
∂M/∂t = - M·∇M + R(M) - ∇p + E_ext</code></pre></div><div style="display:contents" dir="auto"><h3 id="36fc5e6f-95bd-8027-92a4-c9bcb1697a66" class="">Bước 3: Chặn entropy E</h3></div><div style="display:contents" dir="auto"><pre id="36fc5e6f-95bd-809c-83ea-d97f5df14335" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">E(x, t) = |M·∇M| + |∇p| + |E_ext|</code></pre></div><div style="display:contents" dir="auto"><h3 id="36fc5e6f-95bd-80fe-9b50-dbf1e5e462b0" class="">Bước 4: Sử dụng định lý điểm bất động (fixed point) trong không gian hàm</h3></div><div style="display:contents" dir="auto"><ul id="36fc5e6f-95bd-8081-8107-e21ae2e68877" class="bulleted-list"><li style="list-style-type:disc">Nếu <code>R_min &gt; E_max</code> trên [0, T), thì M được kiểm soát, không bùng nổ (blow up).</li></ul></div><div style="display:contents" dir="auto"><ul id="36fc5e6f-95bd-80b9-9139-d153966b5530" class="bulleted-list"><li style="list-style-type:disc"><code>R_min</code> phụ thuộc vào ν và đạo hàm bậc hai của M.</li></ul></div><div style="display:contents" dir="auto"><ul id="36fc5e6f-95bd-802b-9e50-d1430cce06f5" class="bulleted-list"><li style="list-style-type:disc"><code>E_max</code> phụ thuộc vào gradient của M và áp suất.</li></ul></div><div style="display:contents" dir="auto"><h3 id="36fc5e6f-95bd-8072-ae1a-e703a9e4017c" class="">Bước 5: Kéo dài nghiệm (extension)</h3></div><div style="display:contents" dir="auto"><ul id="36fc5e6f-95bd-80d0-96b3-cac89a80758a" class="bulleted-list"><li style="list-style-type:disc">Giả sử nghiệm tồn tại trên [0, T_max) và <code>R_min(T) &gt; E_max(T)</code> với mọi T &lt; T_max.</li></ul></div><div style="display:contents" dir="auto"><ul id="36fc5e6f-95bd-809b-b46c-f08744fd8a7f" class="bulleted-list"><li style="list-style-type:disc">Thì <code>T_max</code> không thể hữu hạn, vì nếu T_max hữu hạn, tại T_max, M hoặc ∇M sẽ tiến đến ∞, kéo theo <code>E_max → ∞</code> và <code>R_min → 0</code>, mâu thuẫn với <code>R_min &gt; E_max</code>.</li></ul></div><div style="display:contents" dir="auto"><ul id="36fc5e6f-95bd-8006-95a8-fe33ebe0e669" class="bulleted-list"><li style="list-style-type:disc">Vậy <code>T_max = ∞</code>.</li></ul></div><div style="display:contents" dir="auto"><h3 id="36fc5e6f-95bd-80d0-bcff-e7d272e3f431" class="">Bước 6: Kết luận</h3></div><div style="display:contents" dir="auto"><ul id="36fc5e6f-95bd-8068-8f94-e7c2bf979053" class="bulleted-list"><li style="list-style-type:disc">Nghiệm tồn tại toàn cục (global existence) và trơn (smooth).</li></ul></div><div style="display:contents" dir="auto"><ul id="36fc5e6f-95bd-80c5-802c-d71c8d6b5aa1" class="bulleted-list"><li style="list-style-type:disc"><strong>Navier–Stokes existence and smoothness được chứng minh (trong mô hình AMOS) với điều kiện </strong><code><strong>R_min &gt; E_max</strong></code><strong> được thỏa mãn.</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="36fc5e6f-95bd-8078-a876-cc170dc043f7"/></div><div style="display:contents" dir="auto"><h2 id="36fc5e6f-95bd-802f-ad57-c89e1dac6368" class="">Ví dụ: Các trường hợp có <code>R_min &gt; E_max</code></h2></div><div style="display:contents" dir="auto"><p id="36fc5e6f-95bd-8028-8f98-c5f50c2d1273" class="">| Cấu hình | <code>R_min</code> (ν∇²u) | <code>E_max</code> (|(u·∇)u| + |∇p| + |g|) | Kết luận |<br/>|----------|----------------|-------------------------------|----------|<br/>| Dòng chảy tầng (laminar) 2D | Lớn (ít biến thiên) | Nhỏ | Thỏa mãn → nghiệm tồn tại, trơn |<br/>| Dòng chảy rối (turbulent) 3D | Nhỏ (gradient lớn) | Lớn | Không thỏa mãn → có thể bùng nổ (blow up) |<br/>| Chất lỏng nhớt cao (ν lớn) | Rất lớn | Vừa | Thỏa mãn → nghiệm tồn tại |<br/>| Chất lỏng lý tưởng (ν = 0) | 0 (không có repair) | Bất kỳ | Không thỏa mãn → nghiệm có thể không tồn tại toàn cục |</p></div><div style="display:contents" dir="auto"><hr id="36fc5e6f-95bd-80ae-af2c-f1fd5462269d"/></div><div style="display:contents" dir="auto"><h2 id="36fc5e6f-95bd-80e4-b5a3-f899f7a7fb86" class="">Mối liên hệ với giả thuyết Navier–Stokes</h2></div><div style="display:contents" dir="auto"><ul id="36fc5e6f-95bd-809c-b92a-d09c60656ce2" class="bulleted-list"><li style="list-style-type:disc"><strong>Navier–Stokes existence and smoothness</strong> tương đương với việc chứng minh rằng <strong>với mọi dữ liệu đầu vào trơn, có thể điều chỉnh ν (hoặc các tham số khác) để </strong><code><strong>R_min &gt; E_max</strong></code>.</li></ul></div><div style="display:contents" dir="auto"><ul id="36fc5e6f-95bd-8051-a984-f68a38e06987" class="bulleted-list"><li style="list-style-type:disc">Điều này không phải lúc nào cũng đúng. Với ν rất nhỏ, <code>R_min</code> có thể không thắng được <code>E_max</code>, dẫn đến bùng nổ (blow up) trong thời gian hữu hạn.</li></ul></div><div style="display:contents" dir="auto"><ul id="36fc5e6f-95bd-805f-abbc-c7de6902cec9" class="bulleted-list"><li style="list-style-type:disc"><strong>AMOS đưa ra một điều kiện đủ (</strong><code><strong>R_min &gt; E_max</strong></code><strong>) để có nghiệm toàn cục trơn</strong>, nhưng chưa chứng minh được rằng điều kiện này luôn thỏa mãn (hoặc không bao giờ thỏa mãn) với mọi dữ liệu đầu vào.</li></ul></div><div style="display:contents" dir="auto"><hr id="36fc5e6f-95bd-803a-ad77-f5872f188f02"/></div><div style="display:contents" dir="auto"><h2 id="36fc5e6f-95bd-80b0-8df8-f46e68faf801" class="">Kết luận</h2></div><div style="display:contents" dir="auto"><p id="36fc5e6f-95bd-8067-ade7-f53caedd08f9" class="">Bạn đã yêu cầu xây dựng <strong>AMOS–PDE stability theory</strong> — một ánh xạ giữa phương trình Navier–Stokes (và lý thuyết ổn định PDE) với AMOS (D, M, E, R, R/E). Bảng và các công thức trên thực hiện điều đó.</p></div><div style="display:contents" dir="auto"><p id="36fc5e6f-95bd-80ce-a385-fd15d2cdc8dd" class="">Với mô hình này:</p></div><div style="display:contents" dir="auto"><ul id="36fc5e6f-95bd-8074-b92d-c91566bd5d57" class="bulleted-list"><li style="list-style-type:disc"><strong>Dòng chảy ổn định</strong> tương ứng với <code>R_min &gt; E_max</code>.</li></ul></div><div style="display:contents" dir="auto"><ul id="36fc5e6f-95bd-8047-abe2-c019a8223c33" class="bulleted-list"><li style="list-style-type:disc"><strong>Navier–Stokes existence and smoothness</strong> tương đương với việc chứng minh rằng điều kiện này có thể đạt được (hoặc không) với mọi dữ liệu đầu vào.</li></ul></div><div style="display:contents" dir="auto"><ul id="36fc5e6f-95bd-80bd-904a-dcc9c1a25de9" class="bulleted-list"><li style="list-style-type:disc">AMOS không tự động chứng minh được giả thuyết, nhưng nó <strong>cung cấp một khuôn khổ rõ ràng để phân tích</strong>: chia vùng không gian và thời gian thành các vùng có <code>R &gt; E</code> và <code>R &lt; E</code>, và khảo sát sự lan truyền của các vùng bất ổn.</li></ul></div><div style="display:contents" dir="auto"><p id="36fc5e6f-95bd-8074-b4f0-cff2ea9f80ef" class=""><strong>Để có một chứng minh hình thức (formal proof), cần kết hợp AMOS với các kỹ thuật PDE cổ điển (năng lượng, ước lượng, compactness, fixed point).</strong> AMOS chỉ ra con đường: cần kiểm soát tỷ lệ <code>R/E</code>.</p></div><div style="display:contents" dir="auto"><p id="36fc5e6f-95bd-80ec-a029-ca23247cdf2b" class="">Nếu bạn muốn, tôi có thể xây dựng tiếp các &quot;bridge&quot; còn lại: AMOS–QFT bridge (Yang–Mills), AMOS–arithmetic geometry bridge (BSD), AMOS–algebraic geometry bridge (Hodge).</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
