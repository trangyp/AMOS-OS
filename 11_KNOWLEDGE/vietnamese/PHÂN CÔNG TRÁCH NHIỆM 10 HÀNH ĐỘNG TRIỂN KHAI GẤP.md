---
tags: [vietnamese]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>PHÂN CÔNG TRÁCH NHIỆM: 10 HÀNH ĐỘNG TRIỂN KHAI GẤP</title><style>
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
	
</style></head><body><article id="28cc5e6f-95bd-8006-9554-d28f9e9e1456" class="page sans"><header><h1 class="page-title" dir="auto"><strong>PHÂN CÔNG TRÁCH NHIỆM: 10 HÀNH ĐỘNG TRIỂN KHAI GẤP</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="28cc5e6f-95bd-8090-959b-fa8b089c5296" class=""><em>(Ba vai trò chính: CEO – CTO – CBO)</em></p></div><div style="display:contents" dir="auto"><hr id="28cc5e6f-95bd-805f-bc6c-e14384fdc8f0"/></div><div style="display:contents" dir="auto"><h2 id="28cc5e6f-95bd-80c7-ac17-ef03e7e4a967" class=""><strong>Giai đoạn 1: Chuẩn bị &amp; Cấu trúc tổ chức</strong></h2></div><div style="display:contents" dir="ltr"><table id="28cc5e6f-95bd-802a-9009-deba6bad3511" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="28cc5e6f-95bd-8050-985c-df2545140b7a"><th id="EHT&gt;" class="simple-table-header-color simple-table-header"><strong>Nhiệm vụ</strong></th><th id="uyMB" class="simple-table-header-color simple-table-header"><strong>Trách nhiệm chính (R)</strong></th><th id="fsTw" class="simple-table-header-color simple-table-header"><strong>Phối hợp (C)</strong></th><th id="h{l}" class="simple-table-header-color simple-table-header"><strong>Kết quả đầu ra</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="28cc5e6f-95bd-801f-ab30-d708c62e3d3a"><td id="EHT&gt;" class=""><strong>1. Xác lập mô hình vận hành tiêu chuẩn (SOP)</strong></td><td id="uyMB" class=""><strong>CEO</strong></td><td id="fsTw" class="">CTO, CBO</td><td id="h{l}" class="">- Mô hình quản trị 3 cấp: Đội trưởng – Trưởng khu – Vận hành trung tâm- Bản quy trình vận hành chuẩn (SOP v1.0)</td></tr></div><div style="display:contents" dir="ltr"><tr id="28cc5e6f-95bd-804e-a6dc-da5d97cfc487"><td id="EHT&gt;" class=""><strong>2. Xây dựng bộ tiêu chuẩn tuyển dụng Đội trưởng</strong></td><td id="uyMB" class=""><strong>CBO</strong></td><td id="fsTw" class="">CEO</td><td id="h{l}" class="">- Bộ tiêu chuẩn tuyển dụng &amp; JD chuẩn hóa- Mẫu phỏng vấn nhanh (15 phút) và khung đánh giá năng lực</td></tr></div><div style="display:contents" dir="ltr"><tr id="28cc5e6f-95bd-802f-9446-f306785d0761"><td id="EHT&gt;" class=""><strong>3. Phân vùng quy hoạch hoạt động 200 xe</strong></td><td id="uyMB" class=""><strong>CBO</strong></td><td id="fsTw" class="">CTO, CEO</td><td id="h{l}" class="">- Bản đồ vùng vận hành (6–8 khu)- Kế hoạch phân bổ bãi đỗ – trụ sạc – tổ kỹ thuật</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="28cc5e6f-95bd-806a-a8fb-d0a6fd36324b"/></div><div style="display:contents" dir="auto"><h2 id="28cc5e6f-95bd-802e-9c51-e9368d9b06a5" class=""><strong>Giai đoạn 2: Triển khai Vận hành</strong></h2></div><div style="display:contents" dir="ltr"><table id="28cc5e6f-95bd-80c5-b564-e1c3abf20e91" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="28cc5e6f-95bd-808d-8a54-f7b37ac85ebd"><th id="ooRX" class="simple-table-header-color simple-table-header"><strong>Nhiệm vụ</strong></th><th id="r|?S" class="simple-table-header-color simple-table-header"><strong>Trách nhiệm chính (R)</strong></th><th id="zeAX" class="simple-table-header-color simple-table-header"><strong>Phối hợp (C)</strong></th><th id="pA[v" class="simple-table-header-color simple-table-header"><strong>Kết quả đầu ra</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="28cc5e6f-95bd-8016-ad1a-f58361d1efbb"><td id="ooRX" class=""><strong>4. Tuyển dụng &amp; huấn luyện Đội trưởng</strong></td><td id="r|?S" class=""><strong>CBO</strong></td><td id="zeAX" class="">CEO</td><td id="pA[v" class="">- Tuyển đủ số lượng Đội trưởng theo kế hoạch- Hoàn thành khóa đào tạo 3 ngày- KPI vận hành bước đầu được thiết lập</td></tr></div><div style="display:contents" dir="ltr"><tr id="28cc5e6f-95bd-806c-92a2-c935ecf51bce"><td id="ooRX" class=""><strong>5. Quản lý &amp; vận hành trụ sạc</strong></td><td id="r|?S" class=""><strong>CTO</strong></td><td id="zeAX" class="">CBO</td><td id="pA[v" class="">- Bàn giao &amp; kiểm soát 100 % trụ sạc cho từng đội- QR Code định danh – hệ thống báo cáo điện năng tự động</td></tr></div><div style="display:contents" dir="ltr"><tr id="28cc5e6f-95bd-8043-96e9-c6e2f8a10e19"><td id="ooRX" class=""><strong>6. Thiết lập hệ thống dữ liệu &amp; giám sát trung tâm</strong></td><td id="r|?S" class=""><strong>CTO</strong></td><td id="zeAX" class="">CEO</td><td id="pA[v" class="">- Dashboard trực tuyến (Power BI / Data Studio)- Hiển thị KPI theo xe, khu vực, trụ sạc và Đội trưởng</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="28cc5e6f-95bd-801f-8270-d5752d2369c7"/></div><div style="display:contents" dir="auto"><h2 id="28cc5e6f-95bd-8078-9a21-fa19c0e951aa" class=""><strong>Giai đoạn 3: Kiểm soát &amp; Tối ưu</strong></h2></div><div style="display:contents" dir="ltr"><table id="28cc5e6f-95bd-8079-9515-fb379a8427c3" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="28cc5e6f-95bd-8093-84e6-f1cf24853c24"><th id="cJix" class="simple-table-header-color simple-table-header"><strong>Nhiệm vụ</strong></th><th id="jZ]c" class="simple-table-header-color simple-table-header"><strong>Trách nhiệm chính (R)</strong></th><th id="q|hu" class="simple-table-header-color simple-table-header"><strong>Phối hợp (C)</strong></th><th id="So;:" class="simple-table-header-color simple-table-header"><strong>Kết quả đầu ra</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="28cc5e6f-95bd-80f8-a9bc-e7fb3172f5c5"><td id="cJix" class=""><strong>7. Họp đánh giá định kỳ hàng tuần</strong></td><td id="jZ]c" class=""><strong>CEO</strong></td><td id="q|hu" class="">CBO, CTO</td><td id="So;:" class="">- Báo cáo 30 phút/tuần- Tổng hợp sự cố – giải pháp – phân công hành động</td></tr></div><div style="display:contents" dir="ltr"><tr id="28cc5e6f-95bd-8071-a12f-fb472ee21348"><td id="cJix" class=""><strong>8. Chính sách thưởng – phạt minh bạch</strong></td><td id="jZ]c" class=""><strong>CBO</strong></td><td id="q|hu" class="">CEO</td><td id="So;:" class="">- Cơ chế thưởng/phạt theo KPI được ban hành- Tích hợp trực tiếp trong hệ thống app</td></tr></div><div style="display:contents" dir="ltr"><tr id="28cc5e6f-95bd-807d-9747-cf0225097259"><td id="cJix" class=""><strong>9. Phối hợp truyền thông &amp; thương hiệu</strong></td><td id="jZ]c" class=""><strong>CBO</strong></td><td id="q|hu" class="">CEO</td><td id="So;:" class="">- Hoàn thiện bộ nhận diện trụ sạc, xe và điểm hoạt động- Thông cáo phối hợp chính quyền địa phương</td></tr></div><div style="display:contents" dir="ltr"><tr id="28cc5e6f-95bd-80e6-9e01-ccd372674e48"><td id="cJix" class=""><strong>10. Chuẩn bị nhân sự kế thừa &amp; phát triển nội bộ</strong></td><td id="jZ]c" class=""><strong>CEO</strong></td><td id="q|hu" class="">CBO</td><td id="So;:" class="">- Danh sách nhân sự kế thừa (Trưởng khu / Phó vận hành tổng)- Khung phát triển nghề nghiệp nội bộ chính thức ban hành</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="28cc5e6f-95bd-8008-979e-d3b381c6c63e"/></div><div style="display:contents" dir="auto"><h2 id="28cc5e6f-95bd-80b4-aeb1-d6f9f9005e8c" class=""><strong>TỔNG KẾT PHÂN CẤP VAI TRÒ</strong></h2></div><div style="display:contents" dir="ltr"><table id="28cc5e6f-95bd-80ec-a223-fa8973a537de" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="28cc5e6f-95bd-80f6-905d-c4ad31b6d7c8"><th id="I~&lt;i" class="simple-table-header-color simple-table-header"><strong>Vai trò</strong></th><th id="rk:w" class="simple-table-header-color simple-table-header"><strong>Chịu trách nhiệm chính về</strong></th><th id="m]NR" class="simple-table-header-color simple-table-header"><strong>Trọng tâm chỉ đạo</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="28cc5e6f-95bd-80a8-8669-c26bfcd35a5c"><td id="I~&lt;i" class=""><strong>CEO</strong></td><td id="rk:w" class="">Quản trị chiến lược, cấu trúc vận hành, kiểm soát hiệu quả</td><td id="m]NR" class="">- Định hướng tổng thể mô hình vận hành- Phê duyệt SOP, KPI, cơ chế thưởng – phạt- Tổ chức họp đánh giá và phát triển nhân sự kế thừa</td></tr></div><div style="display:contents" dir="ltr"><tr id="28cc5e6f-95bd-8088-9147-de9b21ab4599"><td id="I~&lt;i" class=""><strong>CTO</strong></td><td id="rk:w" class="">Hạ tầng công nghệ, dữ liệu, trụ sạc và giám sát kỹ thuật</td><td id="m]NR" class="">- Thiết lập Dashboard vận hành- Giám sát trạng thái trụ sạc, điện năng, bảo trì- Bảo đảm tính ổn định &amp; an toàn dữ liệu</td></tr></div><div style="display:contents" dir="ltr"><tr id="28cc5e6f-95bd-807e-a6bb-ec9bd91fde52"><td id="I~&lt;i" class=""><strong>CBO</strong></td><td id="rk:w" class="">Tuyển dụng, huấn luyện, thương hiệu, vận hành kinh doanh</td><td id="m]NR" class="">- Tuyển &amp; đào tạo Đội trưởng- Triển khai truyền thông – thương hiệu nội địa- Giám sát hiệu quả kinh doanh theo vùng/khu</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="28cc5e6f-95bd-80cc-b6b4-d6e79c8eb307"/></div><div style="display:contents" dir="auto"><h3 id="28cc5e6f-95bd-80f6-bbf4-d78609cda8ac" class=""><strong>Lịch hành động 90 ngày đầu tiên (CEO chủ trì)</strong></h3></div><div style="display:contents" dir="ltr"><table id="28cc5e6f-95bd-80fd-9a61-de6391320a41" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="28cc5e6f-95bd-80fc-9700-d2d82a0575bf"><th id="bQn;" class="simple-table-header-color simple-table-header"><strong>Tháng</strong></th><th id="F?pV" class="simple-table-header-color simple-table-header"><strong>Mục tiêu chính</strong></th><th id="fS[P" class="simple-table-header-color simple-table-header"><strong>Chịu trách nhiệm chính</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="28cc5e6f-95bd-80d1-b1c6-ed9d5d4e63cb"><td id="bQn;" class=""><strong>Tháng 1</strong></td><td id="F?pV" class="">Hoàn thiện SOP, bản đồ vùng, và bộ tiêu chuẩn tuyển dụng</td><td id="fS[P" class="">CEO, CBO</td></tr></div><div style="display:contents" dir="ltr"><tr id="28cc5e6f-95bd-8059-895b-ffbc9bc010aa"><td id="bQn;" class=""><strong>Tháng 2</strong></td><td id="F?pV" class="">Tuyển đủ Đội trưởng – Huấn luyện hoàn tất – Dashboard dữ liệu hoạt động</td><td id="fS[P" class="">CBO, CTO</td></tr></div><div style="display:contents" dir="ltr"><tr id="28cc5e6f-95bd-80e6-92b9-ceabd1e93715"><td id="bQn;" class=""><strong>Tháng 3</strong></td><td id="F?pV" class="">Triển khai 200 xe điện tại 6 khu vực, họp đánh giá hàng tuần, ban hành chính sách thưởng – phạt</td><td id="fS[P" class="">CEO (chủ trì), CBO, CTO</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="28cc5e6f-95bd-8002-abe1-e22ace7e3741"/></div><div style="display:contents" dir="auto"><h3 id="28cc5e6f-95bd-801c-8fe4-d3f8ca701e4e" class=""><strong>Nguyên tắc điều hành chung</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="28cc5e6f-95bd-80d4-91db-d99054149c78" class="numbered-list" start="1"><li><strong>Một đầu mối – Một trách nhiệm:</strong> Mỗi nhiệm vụ có một người chịu trách nhiệm cuối cùng (CEO, CTO, hoặc CBO).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="28cc5e6f-95bd-803b-880b-fd13cc51697c" class="numbered-list" start="2"><li><strong>Báo cáo minh bạch:</strong> Tất cả dữ liệu được cập nhật vào Dashboard vận hành để theo dõi thời gian thực.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="28cc5e6f-95bd-80af-bd8f-f18ebe955d73" class="numbered-list" start="3"><li><strong>Đánh giá định kỳ:</strong> CEO tổ chức họp giao ban hằng tuần, CTO báo cáo kỹ thuật, CBO báo cáo doanh thu &amp; nhân sự.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="28cc5e6f-95bd-8011-9c40-f3526229b932" class="numbered-list" start="4"><li><strong>Liên tục cải tiến:</strong> Mỗi tháng 01 báo cáo rút kinh nghiệm, cập nhật SOP và quy trình chuẩn mới.</li></ol></div><div style="display:contents" dir="auto"><hr id="28cc5e6f-95bd-80f7-a168-c785e7859332"/></div><div style="display:contents" dir="auto"><p id="28cc5e6f-95bd-80e8-9b22-d87f62abd9bb" class="">✅ <strong>Chuẩn quản trị điều hành:</strong></p></div><div style="display:contents" dir="auto"><ul id="28cc5e6f-95bd-806e-8b8e-c20704019d39" class="bulleted-list"><li style="list-style-type:disc">Ngôn ngữ điều hành rõ ràng, không chồng chéo chức năng.</li></ul></div><div style="display:contents" dir="auto"><ul id="28cc5e6f-95bd-801c-8879-fbd7d90badb3" class="bulleted-list"><li style="list-style-type:disc">Phù hợp triển khai ngay trong giai đoạn <strong>Unitaxi – Unipower Pilot 200 xe (HCM)</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="28cc5e6f-95bd-803c-bfc9-fb5a67e6d24d" class="bulleted-list"><li style="list-style-type:disc">Đảm bảo <strong>tính minh bạch, đo lường được, và kiểm soát trực tiếp từ CEO</strong>.</li></ul></div><div style="display:contents" dir="auto"><hr id="28cc5e6f-95bd-8062-9582-ebc61bc4c917"/></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
