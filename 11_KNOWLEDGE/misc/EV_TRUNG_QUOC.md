---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>EV Trung Quốc</title><style>
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
	
</style></head><body><article id="2b2c5e6f-95bd-80f8-84f1-ee31f080a314" class="page sans"><header><h1 class="page-title" dir="auto">EV Trung Quốc</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><hr id="2b3c5e6f-95bd-8052-aa6e-e6ffd1435ff1"/></div><div style="display:contents" dir="auto"><h2 id="2b3c5e6f-95bd-8086-93fa-d15a42475c8f" class=""><strong>I. BẢN ĐỒ HỆ THỐNG EV TRUNG QUỐC (2024–2030)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2b3c5e6f-95bd-8005-9711-d062178db25f" class=""><strong>1. Quy mô và trạng thái hệ thống</strong></h3></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80ba-891c-cbf3bc26da7f" class="bulleted-list"><li style="list-style-type:disc">Tổng thị trường EV 2025: <strong>10–12 triệu xe/năm</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80ca-b7f3-c82a510a848e" class="bulleted-list"><li style="list-style-type:disc">Tỷ lệ EV: <strong>38–45%</strong> tổng xe mới</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-808a-b413-f6f4db8cbdae" class="bulleted-list"><li style="list-style-type:disc">Xuất khẩu 2024: <strong>~5,26 triệu xe</strong>, hướng tới <strong>7–8 triệu</strong> vào 2027</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-8081-8329-d894fc2a9e06" class="bulleted-list"><li style="list-style-type:disc">Số hãng: <strong>300+</strong>, đến 2030 chỉ còn <strong>15–30</strong> hãng có ý nghĩa hệ thống.</li></ul></div><div style="display:contents" dir="auto"><p id="2b3c5e6f-95bd-8011-983e-d2fd2d696227" class="">→ Đây không phải “ngành ô tô”, mà là <strong>hạ tầng quốc gia + hệ sinh thái dữ liệu + năng lượng</strong>.</p></div><div style="display:contents" dir="auto"><h3 id="2b3c5e6f-95bd-80ac-b478-cfeebd56f08f" class=""><strong>2. Phân lớp quyền lực trong ngành</strong></h3></div><div style="display:contents" dir="ltr"><table id="2b3c5e6f-95bd-8088-99f2-c14f73650ea2" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-80a3-87d4-d4ab42615f3f"><th id="_xX&gt;" class="simple-table-header-color simple-table-header"><strong>Nhóm</strong></th><th id="iyDF" class="simple-table-header-color simple-table-header"><strong>Hãng</strong></th><th id="ZwWY" class="simple-table-header-color simple-table-header"><strong>Cấu trúc quyền lực</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-803e-bd62-c7c57ad23ccc"><td id="_xX&gt;" class="">Tier 0</td><td id="iyDF" class="">BYD, Tesla (TQ)</td><td id="ZwWY" class="">Làm chủ pin + chip + OS + nhà máy</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8037-b031-c45dcc045fe4"><td id="_xX&gt;" class="">Tier 1</td><td id="iyDF" class="">Geely, GAC Aion, SAIC</td><td id="ZwWY" class="">Tài chính mạnh, hậu thuẫn nhà nước</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-80f4-8231-d605a9af160e"><td id="_xX&gt;" class="">Tier 2</td><td id="iyDF" class="">NIO, XPeng, Li Auto</td><td id="ZwWY" class="">Mạnh R&amp;D, yếu lợi nhuận, sống bằng vốn</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8021-93ad-d88e0c406fd1"><td id="_xX&gt;" class="">Tier 3–4</td><td id="iyDF" class="">200+ micro brands</td><td id="ZwWY" class="">Không pin, không OS, không ecosystem</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b3c5e6f-95bd-8044-97f3-fffe9360461b" class="">→ Từ góc nhìn “đại bản canon”:</p></div><div style="display:contents" dir="auto"><p id="2b3c5e6f-95bd-803f-82ce-eaaee120c75c" class="">Chỉ những hãng kiểm soát <strong>(1) pin, (2) OS, (3) dữ liệu, (4) chuỗi cung ứng, (5) mạng sạc / năng lượng</strong> mới có “quyền sống”.</p></div><div style="display:contents" dir="auto"><hr id="2b3c5e6f-95bd-8013-9f98-ed6b745ad74e"/></div><div style="display:contents" dir="auto"><h2 id="2b3c5e6f-95bd-80d3-b071-ca48f28f86ac" class=""><strong>II. VÌ SAO TẤT CẢ ĐỀU LỖ MÀ VẪN CHẠY TIẾP?</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2b3c5e6f-95bd-800f-b6fd-ee0b45d5f8f1" class=""><strong>1. Giai đoạn “chiếm đất” giống smartphone 2010</strong></h3></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-808c-aa78-fe47ef163911" class="bulleted-list"><li style="list-style-type:disc">Mục tiêu không phải lợi nhuận ngắn hạn, mà là:<div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80d3-b3f0-c72936f14a8f" class="bulleted-list"><li style="list-style-type:circle">Chiếm <strong>thị phần</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-809b-9d0f-e1dfc37a3d42" class="bulleted-list"><li style="list-style-type:circle">Chiếm <strong>dữ liệu lái xe</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-8066-8029-d5d4cd2a4b9a" class="bulleted-list"><li style="list-style-type:circle">Khóa <strong>người dùng vào OS + ecosystem</strong></li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-800a-8e37-d0973ac9f24e" class="bulleted-list"><li style="list-style-type:disc">Lợi nhuận ngành sẽ tập trung vào <strong>top 5–10 hãng</strong>, giống smartphone → sau khi đào thải.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2b3c5e6f-95bd-807c-ba93-e22a726c75ac" class=""><strong>2. Lõi lợi nhuận: không nằm ở chiếc xe</strong></h3></div><div style="display:contents" dir="auto"><p id="2b3c5e6f-95bd-8072-9a09-f9333b9e39bb" class="">EV = “cổng vào hệ sinh thái”. Lợi nhuận nằm ở:</p></div><div style="display:contents" dir="ltr"><table id="2b3c5e6f-95bd-8024-a02b-c80dbf584f08" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8067-9021-f12d714d6236"><th id="GoVl" class="simple-table-header-color simple-table-header"><strong>Mảng</strong></th><th id="|V{}" class="simple-table-header-color simple-table-header"><strong>Vai trò thật sự</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8010-b456-d9ca267b9a51"><td id="GoVl" class="">Pin</td><td id="|V{}" class="">Biên lợi nhuận ổn định, kiểm soát chuỗi cung ứng</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-808a-986c-c8004e5cba44"><td id="GoVl" class="">Bán điện / charging</td><td id="|V{}" class="">Dòng tiền đều, dài hạn</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-80bc-860c-eab0b7882544"><td id="GoVl" class="">Dữ liệu lái xe</td><td id="|V{}" class="">Tài sản chiến lược (chính phủ + OEM)</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-800b-a67a-e4a049c9f3c4"><td id="GoVl" class="">Phần mềm / in-car services</td><td id="|V{}" class="">Biên lợi nhuận cực cao</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8022-a270-c5e2b3fa1495"><td id="GoVl" class="">Subscription bảo trì</td><td id="|V{}" class="">Dòng tiền lặp lại</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-80d2-8d06-fe6f26629561"><td id="GoVl" class="">Lifestyle / ecosystem</td><td id="|V{}" class="">Tăng ARPU trên mỗi khách</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b3c5e6f-95bd-8030-bba9-e4efc9923532" class="">→ Hãng “khôn” sẵn sàng <strong>bán xe lỗ 8–15%</strong> để khoá khách vào hệ sinh thái.</p></div><div style="display:contents" dir="auto"><h3 id="2b3c5e6f-95bd-80e0-86e5-c03157ec303f" class=""><strong>3. EV là công cụ chiến lược quốc gia</strong></h3></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80cc-b6ae-f37002103a34" class="bulleted-list"><li style="list-style-type:disc">EV được gắn vào:<div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-8080-802e-c335afbe92e8" class="bulleted-list"><li style="list-style-type:circle">“Made in China 2025”</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-8097-a159-c5c5f292ba49" class="bulleted-list"><li style="list-style-type:circle">Chiến lược xuất khẩu công nghệ</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80f9-8515-e8b02c1fb937" class="bulleted-list"><li style="list-style-type:disc">Hỗ trợ:<div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80e9-8f90-ce83293c7673" class="bulleted-list"><li style="list-style-type:circle">Đất, thuế, vốn, logistics, FTA<div style="display:contents" dir="auto"><p id="2b3c5e6f-95bd-80a2-91cb-c7390aa8ca42" class="">→ Nhiều hãng lớn không được phép “chết” đơn thuần theo logic thị trường.</p></div></li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2b3c5e6f-95bd-8083-b00d-d8fbaee72b1c" class=""><strong>4. Lỗ kế toán, không lỗ hệ sinh thái</strong></h3></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-8012-971e-c3976d168fee" class="bulleted-list"><li style="list-style-type:disc">Chi phí R&amp;D được “kéo dài” thành tài sản.</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-8074-8477-d5b37cad2125" class="bulleted-list"><li style="list-style-type:disc">Lỗ từ xe được bù bằng:<div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-801e-95df-fa78b5d10d87" class="bulleted-list"><li style="list-style-type:circle">Dịch vụ pin</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-8069-a59f-cd258320f075" class="bulleted-list"><li style="list-style-type:circle">Subscription phần mềm</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80e4-aa96-eb3b5821a116" class="bulleted-list"><li style="list-style-type:circle">Dữ liệu bán lại cho địa phương</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80c0-874e-f7267282f755" class="bulleted-list"><li style="list-style-type:circle">Bảo dưỡng, ecosystem dịch vụ</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2b3c5e6f-95bd-80e4-a94b-db8cdc1a4e60" class="">→ Nhìn đúng cấu trúc: <strong>xe chỉ là “đầu phễu”</strong>, không phải sản phẩm cuối cùng.</p></div><div style="display:contents" dir="auto"><hr id="2b3c5e6f-95bd-8097-a048-c2ce774bd491"/></div><div style="display:contents" dir="auto"><h2 id="2b3c5e6f-95bd-80bd-9fb8-fe7ec8300ef1" class=""><strong>III. TẠI SAO XE ĐIỆN CAO CẤP ÍT XUẤT HIỆN Ở ASEAN?</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2b3c5e6f-95bd-80be-b97d-d573dbca70ba" class="numbered-list" start="1"><li>Giá quá cao so với sức mua thị trường mới nổi.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b3c5e6f-95bd-80f8-a146-f8dc419790ed" class="numbered-list" start="2"><li>Nguy cơ pháp lý cao tại EU/US nếu mang xe flagship đi xuất khẩu.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b3c5e6f-95bd-808c-8717-c53bcb1f4910" class="numbered-list" start="3"><li>Hệ thống hậu mãi, linh kiện cao cấp (lidar, chip, 800V) chưa sẵn.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b3c5e6f-95bd-80d5-b5ee-cab77defcedf" class="numbered-list" start="4"><li>Chiến lược: ưu tiên xuất <strong>xe rẻ</strong> để:<div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80b4-8846-ea3e1c9bbdd5" class="bulleted-list"><li style="list-style-type:disc">Chiếm <strong>đường</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-8093-8173-cce40a36a012" class="bulleted-list"><li style="list-style-type:disc">Chiếm <strong>trạm sạc</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80b9-b7ed-c1358f91fe55" class="bulleted-list"><li style="list-style-type:disc">Chiếm <strong>dữ liệu</strong></li></ul></div></li></ol></div><div style="display:contents" dir="auto"><p id="2b3c5e6f-95bd-8002-868c-d8fed42910dc" class="">→ Xe sang sẽ được đẩy mạnh từ <strong>sau 2030</strong>, khi hạ tầng &amp; dữ liệu đã đủ.</p></div><div style="display:contents" dir="auto"><hr id="2b3c5e6f-95bd-80b9-8366-f662f16729eb"/></div><div style="display:contents" dir="auto"><h2 id="2b3c5e6f-95bd-800c-a15f-ea3a5076ab8d" class=""><strong>IV. CẤU TRÚC TÀI CHÍNH: HỌ “SỐNG” NHƯ THẾ NÀO?</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2b3c5e6f-95bd-809d-affd-de28783499fa" class=""><strong>1. 6 nguồn dòng tiền cốt lõi</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="2b3c5e6f-95bd-806a-9b65-ed9a17bb2896" class="numbered-list" start="1"><li>Pin</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b3c5e6f-95bd-803d-82a0-eee62b3d282a" class="numbered-list" start="2"><li>Energy services (sạc, V2G, lưu điện)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b3c5e6f-95bd-80fa-b66b-d0e1c2248fed" class="numbered-list" start="3"><li>Subscription phần mềm</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b3c5e6f-95bd-807c-8bcf-e819fbc0f148" class="numbered-list" start="4"><li>Battery swap</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b3c5e6f-95bd-80d2-b17a-e4e6ca42b361" class="numbered-list" start="5"><li>Bảo trì/sửa chữa</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b3c5e6f-95bd-8000-95e7-d16b170ec1ab" class="numbered-list" start="6"><li>Ecosystem / lifestyle</li></ol></div><div style="display:contents" dir="auto"><p id="2b3c5e6f-95bd-807c-baa7-f9e442200162" class="">→ Đây mới là “P&amp;L thật”, không phải P&amp;L trên mỗi chiếc xe.</p></div><div style="display:contents" dir="auto"><h3 id="2b3c5e6f-95bd-804b-b868-c29cbd3c9781" class=""><strong>2. Kỹ thuật giảm lỗ trên báo cáo</strong></h3></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-8092-9c79-ed3f8d4e0675" class="bulleted-list"><li style="list-style-type:disc">Vốn hóa R&amp;D</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-8058-b62f-c6c065b841a6" class="bulleted-list"><li style="list-style-type:disc">Trợ cấp chính quyền địa phương</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80fe-991d-c8a11cf7e4fe" class="bulleted-list"><li style="list-style-type:disc">Thuê nhà máy thay vì sở hữu</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80b2-81f3-ea5fb4a712fd" class="bulleted-list"><li style="list-style-type:disc">IPO liên tục để bơm vốn</li></ul></div><div style="display:contents" dir="auto"><p id="2b3c5e6f-95bd-809d-b3e9-dfce860e40b2" class="">→ Không thể đọc các hãng EV TQ như doanh nghiệp ô tô truyền thống.</p></div><div style="display:contents" dir="auto"><hr id="2b3c5e6f-95bd-8036-a5bc-f05588699654"/></div><div style="display:contents" dir="auto"><h2 id="2b3c5e6f-95bd-80a3-9f1d-e88cd6f713b7" class=""><strong>V. BẢNG XẾP HẠNG “SỐNG – CHẾT” ĐẾN 2030</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2b3c5e6f-95bd-80fa-8ee7-f8ba4a66d3c9" class=""><strong>1. Nhóm 0 – Sống chắc (0–5% rủi ro)</strong></h3></div><div style="display:contents" dir="ltr"><table id="2b3c5e6f-95bd-80dc-a36a-c542d5a8ff00" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-80ed-8748-c5bce56f063c"><th id="j@BX" class="simple-table-header-color simple-table-header"><strong>Hãng</strong></th><th id="ULe^" class="simple-table-header-color simple-table-header"><strong>Rủi ro</strong></th><th id="_]QG" class="simple-table-header-color simple-table-header"><strong>Lý do hệ thống</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8004-9f01-fbfaa3d6ab91"><td id="j@BX" class="">BYD</td><td id="ULe^" class="">~0%</td><td id="_]QG" class="">Pin + xe + chip + chuỗi cung ứng, lợi nhuận thật</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8033-b354-f9cc0c384d89"><td id="j@BX" class="">Huawei Aito</td><td id="ULe^" class="">2–3%</td><td id="_]QG" class="">OS + AI mạnh, chống lưng chính trị</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-80e5-ba17-cadcf8c422e5"><td id="j@BX" class="">Geely/Zeekr</td><td id="ULe^" class="">5%</td><td id="_]QG" class="">Volvo, Polestar, hệ SEA, tài chính mạnh</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-80b0-9a56-ec80a88db083"><td id="j@BX" class="">SAIC (MG)</td><td id="ULe^" class="">5%</td><td id="_]QG" class="">Nhà nước chống lưng, quá lớn để chết</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-80e7-afb5-d964d010c16a"><td id="j@BX" class="">Li Auto</td><td id="ULe^" class="">3%</td><td id="_]QG" class="">Dòng tiền dương, hybrid logic, ít phụ thuộc trợ cấp</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b3c5e6f-95bd-80d4-9bff-cb98978c0fba" class="">→ 5 “tàu mẹ” này sẽ chắc chắn tồn tại qua 2030, kể cả khi thị trường sụp.</p></div><div style="display:contents" dir="auto"><h3 id="2b3c5e6f-95bd-80ea-9d92-c60376000950" class=""><strong>2. Nhóm 1 – Sống nhưng phải tái cấu trúc (40–60% rủi ro)</strong></h3></div><div style="display:contents" dir="ltr"><table id="2b3c5e6f-95bd-8049-a55a-d0c7caa84700" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-808f-968d-ebfec7be21a3"><th id="LgCx" class="simple-table-header-color simple-table-header"><strong>Hãng</strong></th><th id="]WfU" class="simple-table-header-color simple-table-header"><strong>Rủi ro</strong></th><th id="oo=|" class="simple-table-header-color simple-table-header"><strong>Vấn đề chính</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8003-80fa-e74fd9f290cb"><td id="LgCx" class="">NIO</td><td id="]WfU" class="">~55%</td><td id="oo=|" class="">Burn rate cực cao, không có pin, phụ thuộc vốn</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8047-86e4-df2cce586173"><td id="LgCx" class="">XPeng</td><td id="]WfU" class="">~45%</td><td id="oo=|" class="">Công nghệ tốt, bán chậm, lợi nhuận thấp</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-80e2-a092-ec1afb206c28"><td id="LgCx" class="">Aion (GAC)</td><td id="]WfU" class="">~50%</td><td id="oo=|" class="">Sống nhờ trợ cấp địa phương</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8068-99bd-e66a67602c7d"><td id="LgCx" class="">Leapmotor</td><td id="]WfU" class="">~60%</td><td id="oo=|" class="">Quá nhỏ, phụ thuộc Stellantis</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-807e-83e5-f653b23e0c73"><td id="LgCx" class="">Changan EV</td><td id="]WfU" class="">~50%</td><td id="oo=|" class="">Không có lợi thế rõ ràng trước BYD/Geely</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b3c5e6f-95bd-80b6-a149-fb1738003390" class="">→ Sống nếu:</p></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-8008-90b7-f206f94ce25b" class="bulleted-list"><li style="list-style-type:disc">Hạ burn rate 2025–2027</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-8015-bf11-c75f8379390c" class="bulleted-list"><li style="list-style-type:disc">Hợp tác / sáp nhập với các tập đoàn lớn</li></ul></div><div style="display:contents" dir="auto"><h3 id="2b3c5e6f-95bd-8065-8ed0-d9c3f4d56429" class=""><strong>3. Nhóm 2 – Rủi ro cao (70–85%)</strong></h3></div><div style="display:contents" dir="ltr"><table id="2b3c5e6f-95bd-8003-bf01-f6d68419d7e7" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-800b-9519-c795c838a39a"><th id="Rp[W" class="simple-table-header-color simple-table-header"><strong>Hãng</strong></th><th id="qeHP" class="simple-table-header-color simple-table-header"><strong>Rủi ro</strong></th><th id="O&gt;dA" class="simple-table-header-color simple-table-header"><strong>Lý do</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8098-82ad-efa6dbedaba2"><td id="Rp[W" class="">Hozon (Neta)</td><td id="qeHP" class="">~75%</td><td id="O&gt;dA" class="">Xuất khẩu mạnh nhưng margin âm, không pin</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8036-8eed-fdb91f40467e"><td id="Rp[W" class="">WM Motor</td><td id="qeHP" class="">~90%</td><td id="O&gt;dA" class="">Đã phá sản một lần, niềm tin yếu</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-80ed-a83b-ede449f3b304"><td id="Rp[W" class="">Seres (ngoài Huawei Aito)</td><td id="qeHP" class="">~80%</td><td id="O&gt;dA" class="">Không có OS mạnh, phụ thuộc Huawei</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-80ad-b445-dc4a66c852e4"><td id="Rp[W" class="">Baojun / Wuling EV series</td><td id="qeHP" class="">~70%</td><td id="O&gt;dA" class="">Biên lợi nhuận rất thấp, cạnh tranh bão hòa</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b3c5e6f-95bd-80f5-bdcb-c601ca3bf2ee" class="">→ Đa số sẽ bị thâu tóm hoặc biến mất khỏi thị trường nội địa trước 2030.</p></div><div style="display:contents" dir="auto"><h3 id="2b3c5e6f-95bd-8049-a1c3-d5ffdb1a4079" class=""><strong>4. Nhóm 3 – Chắc chắn chết (90–99%)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-802d-9c15-d9a8f83d04f9" class="bulleted-list"><li style="list-style-type:disc">200+ hãng mini EV: XEV, Gingko, Jiangnan, Yudo, Levdeo, Singulato, Enovate, Skyworth EV, các nhái Wuling,…</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80eb-9e9d-db5a39356b6b" class="bulleted-list"><li style="list-style-type:disc">Đặc điểm chung:<div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-8002-acd9-c6812ef167fa" class="bulleted-list"><li style="list-style-type:circle">Không pin</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-8027-be45-ebfc3e6a6a07" class="bulleted-list"><li style="list-style-type:circle">Không OS</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80e8-a09f-f8b10d927867" class="bulleted-list"><li style="list-style-type:circle">Không R&amp;D</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80c2-a6f4-d9d7cc18eb9f" class="bulleted-list"><li style="list-style-type:circle">Không ecosystem</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80a5-a4be-f0285024d290" class="bulleted-list"><li style="list-style-type:circle">Thị phần nhỏ, không được nhà nước ưu tiên</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2b3c5e6f-95bd-80e4-b699-e722455a0771" class="">→ <strong>2025–2028</strong> là làn sóng phá sản chính, sau đó là sáp nhập, xóa sổ.</p></div><div style="display:contents" dir="auto"><h3 id="2b3c5e6f-95bd-8002-af8f-f33fc6efb6ba" class=""><strong>5. Nhóm 4 – “Xác sống” (tồn tại danh nghĩa)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80e7-823e-d0b251bd12c1" class="bulleted-list"><li style="list-style-type:disc">BAIC EV, JAC EV, FAW EV, Shenlan, Dongfeng EV (ngoài Voyah)</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80e9-b446-f50be698f088" class="bulleted-list"><li style="list-style-type:disc">Tồn tại vì:<div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80b7-9c21-e72a7088ae12" class="bulleted-list"><li style="list-style-type:circle">Được bơm vốn tỉnh</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-8061-ade8-d986b76b7da6" class="bulleted-list"><li style="list-style-type:circle">Không cho phá sản vì lý do chính trị–xã hội</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-8067-bd0d-f69431d0d42e" class="bulleted-list"><li style="list-style-type:disc">Thị phần rất nhỏ, không còn sức cạnh tranh thực.</li></ul></div><div style="display:contents" dir="auto"><hr id="2b3c5e6f-95bd-80e6-88c0-df2fb84b9e78"/></div><div style="display:contents" dir="auto"><h2 id="2b3c5e6f-95bd-8069-9066-ca16c598d21d" class=""><strong>VI. DÒNG THỜI GIAN SỐNG–CHẾT (2025–2030)</strong></h2></div><div style="display:contents" dir="ltr"><table id="2b3c5e6f-95bd-802f-a64e-c6d2535ed25f" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8046-8ff7-cbf87d020d13"><th id="IYax" class="simple-table-header-color simple-table-header"><strong>Năm</strong></th><th id="~_SN" class="simple-table-header-color simple-table-header"><strong>Sự kiện hệ thống</strong></th><th id="&gt;=f^" class="simple-table-header-color simple-table-header"><strong>Kết quả</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8021-a50d-c83135405c7c"><td id="IYax" class="">2025</td><td id="~_SN" class="">Vòng giảm giá thứ 3</td><td id="&gt;=f^" class="">Mini EV và Tier 3–4 bắt đầu chết</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-80f1-b752-fb1ca49e4a5c"><td id="IYax" class="">2026</td><td id="~_SN" class="">Thương mại hóa pin semi-solid</td><td id="&gt;=f^" class="">Hãng không có pin → bị loại dần</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-80ec-9194-caadf2895220"><td id="IYax" class="">2027</td><td id="~_SN" class="">Hợp nhất thị trường</td><td id="&gt;=f^" class="">30–40 hãng bị sáp nhập</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8090-b0d5-d0f509985688"><td id="IYax" class="">2028</td><td id="~_SN" class="">Siết tiêu chuẩn EV</td><td id="&gt;=f^" class="">100 hãng yếu biến mất</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-80a7-930c-f9fa3abd8c24"><td id="IYax" class="">2029</td><td id="~_SN" class="">Xuất khẩu trở thành trụ cột</td><td id="&gt;=f^" class="">Hãng không có chuỗi cung ứng bị ép sáp nhập</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-806e-a180-e2161c484184"><td id="IYax" class="">2030</td><td id="~_SN" class="">Ổn định cấu trúc</td><td id="&gt;=f^" class="">Chỉ còn 15–30 hãng có ý nghĩa hệ thống</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b3c5e6f-95bd-807b-bdfa-e9726ead4bca"/></div><div style="display:contents" dir="auto"><h2 id="2b3c5e6f-95bd-807d-8d1a-d32b10182622" class=""><strong>VII. DỰ BÁO GIÁ EV TRUNG QUỐC 2025–2030 (FOB)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2b3c5e6f-95bd-8084-87de-d87884d6f88d" class=""><strong>1. 2025 – Vòng giảm giá 3</strong></h3></div><div style="display:contents" dir="ltr"><table id="2b3c5e6f-95bd-8076-8756-ecfba1fcd4a9" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8052-b725-c1c5cad20127"><th id="PiZy" class="simple-table-header-color simple-table-header"><strong>Phân khúc</strong></th><th id="A;Qr" class="simple-table-header-color simple-table-header"><strong>2024</strong></th><th id="Q&gt;JH" class="simple-table-header-color simple-table-header"><strong>2025 (dự)</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8094-a7b7-dd7b30ca0ba6"><td id="PiZy" class="">Mini EV</td><td id="A;Qr" class="">3.500–4.500</td><td id="Q&gt;JH" class=""><strong>2.900–3.500 USD</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-80ec-afe7-e409b763f13c"><td id="PiZy" class="">Đô thị 2–4 chỗ</td><td id="A;Qr" class="">5.000–7.000</td><td id="Q&gt;JH" class=""><strong>4.000–5.500 USD</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8034-870c-d9b8bd7df161"><td id="PiZy" class="">Sedan C</td><td id="A;Qr" class="">12.000–16.000</td><td id="Q&gt;JH" class=""><strong>10.000–14.000 USD</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-80d8-b1f0-d14c8e7bd33e"><td id="PiZy" class="">SUV C</td><td id="A;Qr" class="">14.000–20.000</td><td id="Q&gt;JH" class=""><strong>12.000–18.000 USD</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-809e-a7c7-fdac2711e588"><td id="PiZy" class="">Premium</td><td id="A;Qr" class="">40.000–60.000</td><td id="Q&gt;JH" class="">Gần như giữ nguyên</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b3c5e6f-95bd-8063-b749-fb2a22a3d7dd" class="">→ Mục tiêu: ép chết micro brands, gom thị phần về Tier 0–1.</p></div><div style="display:contents" dir="auto"><h3 id="2b3c5e6f-95bd-807c-864b-f104b181725d" class=""><strong>2. 2026 – Xuất hiện 2 “tầng” giá (LFP vs semi-solid)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80aa-9ee8-dbba5a0a742b" class="bulleted-list"><li style="list-style-type:disc">LFP phổ thông: giảm thêm 5–8%</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-8060-b334-ddc57de7dceb" class="bulleted-list"><li style="list-style-type:disc">EV dùng semi-solid: ~18.000–25.000 USD (chưa scale, giá cao)</li></ul></div><div style="display:contents" dir="auto"><h3 id="2b3c5e6f-95bd-80bd-a98f-c6c7e9579ad5" class=""><strong>3. 2027 – Năm hợp nhất</strong></h3></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80d9-bb13-c86eca83a159" class="bulleted-list"><li style="list-style-type:disc">Giá cell pin giảm 8–12% nữa</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80e2-ae6e-e7c8a6ce246a" class="bulleted-list"><li style="list-style-type:disc">Giá sedan/SUV C giảm thêm ~10% so với 2026</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-8020-8516-c27799b6ee18" class="bulleted-list"><li style="list-style-type:disc">Mini EV chạm đáy: <strong>2.600–3.000 USD</strong></li></ul></div><div style="display:contents" dir="auto"><h3 id="2b3c5e6f-95bd-80fc-86ba-e1ee83d6372d" class=""><strong>4. 2028 – Dư thừa công suất, đẩy mạnh xuất khẩu</strong></h3></div><div style="display:contents" dir="ltr"><table id="2b3c5e6f-95bd-80e7-8a13-f54a132a3705" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-80d2-a4c0-e213c0d85ee1"><th id="uryU" class="simple-table-header-color simple-table-header"><strong>Phân khúc</strong></th><th id="tNLf" class="simple-table-header-color simple-table-header"><strong>2028 FOB (dự)</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-806e-b274-f1c1904dfef7"><td id="uryU" class="">Mini EV</td><td id="tNLf" class=""><strong>2.400–2.800 USD</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8041-b738-fef0ead1c0c4"><td id="uryU" class="">Đô thị</td><td id="tNLf" class=""><strong>3.300–4.200 USD</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8060-8bb2-e848979eb14c"><td id="uryU" class="">Sedan C</td><td id="tNLf" class=""><strong>8.000–11.000 USD</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-809e-b943-ea0ab015928a"><td id="uryU" class="">SUV C</td><td id="tNLf" class=""><strong>10.000–14.000 USD</strong></td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b3c5e6f-95bd-8097-8a70-cd238d110d91" class="">→ Giai đoạn tốt nhất để các nước như Việt Nam nhập xe giá rẻ.</p></div><div style="display:contents" dir="auto"><h3 id="2b3c5e6f-95bd-80fb-909f-f47d77b86e34" class=""><strong>5. 2029–2030 – Đáy giá, thị trường ổn định</strong></h3></div><div style="display:contents" dir="ltr"><table id="2b3c5e6f-95bd-80aa-bcc4-ccef56dd6bbb" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8002-8a53-c603fed09457"><th id="RH]H" class="simple-table-header-color simple-table-header"><strong>Phân khúc</strong></th><th id="PWm\" class="simple-table-header-color simple-table-header"><strong>Giá đáy 2029–2030</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-807e-bca8-d57a193ceefc"><td id="RH]H" class="">Mini EV</td><td id="PWm\" class="">2.300–2.700 USD</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8034-8028-d6fc036d8c56"><td id="RH]H" class="">Đô thị</td><td id="PWm\" class="">3.200–4.000 USD</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-8003-a8f0-d60a34b54211"><td id="RH]H" class="">Sedan C</td><td id="PWm\" class="">8.500–10.500 USD</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-80b9-a44e-d6b4513bd137"><td id="RH]H" class="">SUV C</td><td id="PWm\" class="">9.500–13.000 USD</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b3c5e6f-95bd-807b-962e-e69594e8542b"><td id="RH]H" class="">Premium</td><td id="PWm\" class="">Gần như giữ nguyên</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b3c5e6f-95bd-80cf-bf7e-f832af0005e5" class="">→ Sau 2030, giảm thêm là rất khó vì đã chạm giới hạn chi phí vật liệu.</p></div><div style="display:contents" dir="auto"><hr id="2b3c5e6f-95bd-8057-8c0e-d491e7860238"/></div><div style="display:contents" dir="auto"><h2 id="2b3c5e6f-95bd-80b2-9b65-e8ffd0822177" class=""><strong>VIII. GIÁ XE TRUNG QUỐC VỀ VIỆT NAM (CIF + LOGISTICS)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2b3c5e6f-95bd-8010-841b-f4fc4dd33da8" class=""><strong>1. 2025–2027 (giai đoạn không thuế nhập EV &lt; 9 chỗ)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-803e-a4d2-d74a73436654" class="bulleted-list"><li style="list-style-type:disc">Chi phí đến tay đại lý VN ≈ <strong>FOB + 2.000–3.000 USD</strong><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-8012-a6a6-e26eaf41cfa0" class="bulleted-list"><li style="list-style-type:circle">Mini EV: ~110–140 triệu VND</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80cd-b903-da532c13fc76" class="bulleted-list"><li style="list-style-type:circle">Xe đô thị 4 chỗ: ~160–220 triệu VND</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-801a-83f2-d04754521b6d" class="bulleted-list"><li style="list-style-type:circle">SUV đô thị: ~300–380 triệu VND</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2b3c5e6f-95bd-804a-b72c-d5bc67b92918" class="">→ Đây là “cửa sổ vàng” 2025–2027 cho ai muốn:</p></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-8037-bcce-e55fc705d0b1" class="bulleted-list"><li style="list-style-type:disc">Xây thương hiệu EV giá rẻ</li></ul></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-8015-a062-c0f95c54c548" class="bulleted-list"><li style="list-style-type:disc">Mở rộng đội xe logistics/di chuyển nội đô</li></ul></div><div style="display:contents" dir="auto"><h3 id="2b3c5e6f-95bd-80b0-ba49-ed05460d29d1" class=""><strong>2. 2028–2030 (nếu thuế quay lại ~40%)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2b3c5e6f-95bd-80fb-85fd-dca5b9380c50" class="bulleted-list"><li style="list-style-type:disc">Giá VN sẽ tăng thêm <strong>25–40%</strong> so với mức trên.</li></ul></div><div style="display:contents" dir="auto"><hr id="2b3c5e6f-95bd-8068-801a-fd51782b139f"/></div><div style="display:contents" dir="auto"><h2 id="2b3c5e6f-95bd-8063-bb1c-dea803e5be8a" class=""><strong>IX. NGUYÊN NHÂN CỐT LÕI KHIẾN GIÁ EV CÀNG NGÀY CÀNG RẺ</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2b3c5e6f-95bd-80eb-a1a3-c61272e1e168" class="numbered-list" start="1"><li>Công suất sản xuất <strong>&gt; nhu cầu nội địa</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b3c5e6f-95bd-80ed-9e4a-c901746b38e8" class="numbered-list" start="2"><li>Cuộc chiến pin BYD vs CATL kéo giá cell xuống liên tục</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b3c5e6f-95bd-80d4-b248-c34829f81e90" class="numbered-list" start="3"><li>Chính phủ chủ động đẩy xe ra nước ngoài</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b3c5e6f-95bd-8076-835e-f3f230fb549c" class="numbered-list" start="4"><li>Đào thải tự nhiên: 200 hãng chết, chỉ 20 hãng sống → gom quy mô</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b3c5e6f-95bd-80e2-a08a-c114e9accb97" class="numbered-list" start="5"><li>Pin/motor/controller trở thành “hàng phổ thông”, giống linh kiện smartphone</li></ol></div><div style="display:contents" dir="auto"><hr id="2b3c5e6f-95bd-802b-856c-e3097f157c40"/></div><div style="display:contents" dir="auto"><h2 id="2b3c5e6f-95bd-80bd-9152-cf286e131dec" class=""><strong>X. LÝ DO XE TỪ HÃNG “GIÀU NHẤT” KHÔNG VÀO VIỆT NAM</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2b3c5e6f-95bd-8095-b756-d81341423ca4" class="numbered-list" start="1"><li>Giá premium &gt; 40.000 USD → không phù hợp sức mua.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b3c5e6f-95bd-8071-a247-ca519567d783" class="numbered-list" start="2"><li>OS gắn với server TQ → vướng bài toán dữ liệu &amp; pháp lý.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b3c5e6f-95bd-8029-8bb2-de32afada4ba" class="numbered-list" start="3"><li>Không muốn phá hình ảnh thương hiệu bằng việc giảm giá mạnh ở ASEAN.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b3c5e6f-95bd-801b-90b7-dff8e33c4138" class="numbered-list" start="4"><li>Ưu tiên chiến lược: xuất xe phổ thông để chiếm số lượng và hạ tầng trước.</li></ol></div><div style="display:contents" dir="auto"><p id="2b3c5e6f-95bd-807f-afaf-d0f4656e7340" class="">→ Việt Nam sẽ chủ yếu thấy: <strong>BYD, Wuling/Baojun, Chery, Geely, SAIC/MG</strong></p></div><div style="display:contents" dir="auto"><p id="2b3c5e6f-95bd-8006-8631-d955e8e7d690" class="">→ Gần như không thấy: <strong>NIO, Li Auto, Aito, Zeekr flagship</strong> trong 5 năm tới.</p></div><div style="display:contents" dir="auto"><hr id="2b3c5e6f-95bd-8031-8455-de304cb11261"/></div><div style="display:contents" dir="auto"><h2 id="2b3c5e6f-95bd-8017-b28c-dd37dd84f657" class=""><strong>XI. TÓM TẮT CHO CEO/CHỦ ĐẦU TƯ (1 CÂU)</strong></h2></div><div style="display:contents" dir="auto"><p id="2b3c5e6f-95bd-8085-9cb0-ccb5fc059ba3" class=""><strong>Đến 2030, 90% hãng EV Trung Quốc biến mất. Chỉ các hãng kiểm soát được pin, OS, dữ liệu, năng lượng và chuỗi cung ứng mới sống, và chính giai đoạn 2025–2027 là cửa sổ tốt nhất để Việt Nam “bắt tay đúng hãng + nhập đúng phân khúc giá rẻ” trước khi thị trường khóa cứng.</strong></p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
