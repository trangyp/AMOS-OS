---
tags: [vietnamese]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>ĐỀ ÁN THÍ ĐIỂM</title><style>
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
	
</style></head><body><article id="2cdc5e6f-95bd-8027-9db8-c2536ea66a80" class="page sans"><header><h1 class="page-title" dir="auto"><strong>ĐỀ ÁN THÍ ĐIỂM</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="2cdc5e6f-95bd-80dd-9152-eb00aebd9955" class=""><strong>CHƯƠNG TRÌNH HỖ TRỢ SINH VIÊN:</strong></h2></div><div style="display:contents" dir="auto"><p id="2cdc5e6f-95bd-80a2-acf1-c088d1162909" class="">XE ĐIỆN – VIỆC LÀM BÁN THỜI GIAN – TÀI CHÍNH VI MÔ</p></div><div style="display:contents" dir="auto"><hr id="2cdc5e6f-95bd-8030-af01-f988a4682756"/></div><div style="display:contents" dir="auto"><h2 id="2cdc5e6f-95bd-8021-b028-f22995423157" class=""><strong>I. MỤC TIÊU CHƯƠNG TRÌNH</strong></h2></div><div style="display:contents" dir="auto"><p id="2cdc5e6f-95bd-80b6-8f09-e9d9891e529a" class="">Chương trình được xây dựng nhằm hỗ trợ sinh viên:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2cdc5e6f-95bd-8022-848a-f89619b71bd1" class="numbered-list" start="1"><li>Có <strong>phương tiện di chuyển bằng xe máy điện</strong> phục vụ học tập và làm việc;</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2cdc5e6f-95bd-80e3-aaae-f1e3438ab46c" class="numbered-list" start="2"><li>Có <strong>việc làm bán thời gian ổn định</strong>, phù hợp thời gian học;</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2cdc5e6f-95bd-80d8-8d64-c99466075d85" class="numbered-list" start="3"><li>Từng bước hình thành <strong>kỷ luật tài chính cá nhân</strong> thông qua cơ chế quản lý thu nhập – chi tiêu minh bạch.</li></ol></div><div style="display:contents" dir="auto"><p id="2cdc5e6f-95bd-8066-b3a7-d390070114c4" class="">Đồng thời, chương trình góp phần:</p></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-80d6-9aff-d89d6c76f47a" class="bulleted-list"><li style="list-style-type:disc">Giảm áp lực tài chính cho sinh viên;</li></ul></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-80e0-98cd-fe0af9acbc25" class="bulleted-list"><li style="list-style-type:disc">Tăng khả năng duy trì học tập, hạn chế bỏ học vì lý do kinh tế;</li></ul></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-804d-b9a7-f805331c51bf" class="bulleted-list"><li style="list-style-type:disc">Thúc đẩy xu hướng sử dụng phương tiện giao thông thân thiện môi trường.</li></ul></div><div style="display:contents" dir="auto"><hr id="2cdc5e6f-95bd-803e-aa2b-edc051126ad1"/></div><div style="display:contents" dir="auto"><h2 id="2cdc5e6f-95bd-8062-ade2-fdc6db3d59c9" class=""><strong>II. ĐỐI TƯỢNG THAM GIA</strong></h2></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-808d-8e57-cfec2bd6767b" class="bulleted-list"><li style="list-style-type:disc">Sinh viên đang theo học tại Trường (ưu tiên sinh viên năm 1–3);</li></ul></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-8068-9759-fb75daa54716" class="bulleted-list"><li style="list-style-type:disc">Có nhu cầu làm thêm và phương tiện di chuyển;</li></ul></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-80e0-8db0-da4efbe03bad" class="bulleted-list"><li style="list-style-type:disc">Có gia đình xác nhận thông tin và đồng ý tham gia cơ chế quản lý của chương trình;</li></ul></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-8074-810c-e914801fd129" class="bulleted-list"><li style="list-style-type:disc">Tham gia theo <strong>nhóm 03 sinh viên</strong> nhằm tăng tính kỷ luật và hỗ trợ lẫn nhau.</li></ul></div><div style="display:contents" dir="auto"><hr id="2cdc5e6f-95bd-8013-9e7c-e95015e7c9c7"/></div><div style="display:contents" dir="auto"><h2 id="2cdc5e6f-95bd-80ee-b067-d4861b76d60f" class=""><strong>III. NỘI DUNG CHƯƠNG TRÌNH</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2cdc5e6f-95bd-8040-b3f6-d7633641d9ad" class=""><strong>1. Hỗ trợ phương tiện</strong></h3></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-8027-8234-cbf7c9015723" class="bulleted-list"><li style="list-style-type:disc">Sinh viên được sử dụng xe máy điện theo hình thức <strong>thuê – mua có quản lý</strong>;</li></ul></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-80c7-9e22-c6b09d196a5f" class="bulleted-list"><li style="list-style-type:disc">Xe do đơn vị triển khai quản lý trong giai đoạn đầu nhằm bảo đảm an toàn và giảm rủi ro.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2cdc5e6f-95bd-8059-aca4-cbed0e328197" class=""><strong>2. Bố trí việc làm bán thời gian</strong></h3></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-80aa-91af-fc3df503b7b6" class="bulleted-list"><li style="list-style-type:disc">Sinh viên được sắp xếp việc làm phù hợp thời khóa biểu;</li></ul></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-80bc-aa07-e83b9a8af1bf" class="bulleted-list"><li style="list-style-type:disc">Thu nhập từ việc làm là <strong>nguồn chính để chi trả nghĩa vụ tài chính</strong>;</li></ul></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-8006-8e61-c6599f547667" class="bulleted-list"><li style="list-style-type:disc">Nguyên tắc triển khai: <strong>có việc làm trước, sau đó mới cấp phương tiện</strong>.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2cdc5e6f-95bd-8079-96ee-c283ffa5219f" class=""><strong>3. Tài chính vi mô có kiểm soát</strong></h3></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-80ca-99aa-ea367606b814" class="bulleted-list"><li style="list-style-type:disc">Sinh viên được tiếp cận khoản hỗ trợ tài chính quy mô nhỏ;</li></ul></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-8020-86c3-c935aab1e6a5" class="bulleted-list"><li style="list-style-type:disc">Thu hồi theo kỳ ngắn (ngày/tuần) gắn với thu nhập thực tế;</li></ul></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-80fe-824d-d071705896b2" class="bulleted-list"><li style="list-style-type:disc">Không giải ngân tiền mặt tự do, toàn bộ dòng tiền được quản lý tập trung.</li></ul></div><div style="display:contents" dir="auto"><hr id="2cdc5e6f-95bd-8078-9b18-e1c2ac79e694"/></div><div style="display:contents" dir="auto"><h2 id="2cdc5e6f-95bd-80a5-a85e-f70b970d5490" class=""><strong>IV. CƠ CHẾ QUẢN LÝ &amp; GIẢM RỦI RO</strong></h2></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-80f2-a596-f9d1f0d671e6" class="bulleted-list"><li style="list-style-type:disc"><strong>Bảo lãnh nhiều lớp</strong>: gia đình xác nhận + nhóm sinh viên hỗ trợ chéo;</li></ul></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-807b-8e1e-f367ada553e7" class="bulleted-list"><li style="list-style-type:disc">Theo dõi sớm tình trạng học tập, việc làm và thu nhập;</li></ul></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-80ee-987f-d9d8f5a4bc79" class="bulleted-list"><li style="list-style-type:disc">Ưu tiên hỗ trợ điều chỉnh việc làm trước khi phát sinh vi phạm;</li></ul></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-80cc-9b50-cce37f1c4be7" class="bulleted-list"><li style="list-style-type:disc">Quy trình xử lý minh bạch, bảo đảm quyền lợi sinh viên và tính bền vững của chương trình.</li></ul></div><div style="display:contents" dir="auto"><hr id="2cdc5e6f-95bd-8091-8c97-d4f4520fccf8"/></div><div style="display:contents" dir="auto"><h2 id="2cdc5e6f-95bd-8015-85be-ce85a78fc020" class=""><strong>V. VAI TRÒ PHỐI HỢP CỦA NHÀ TRƯỜNG</strong></h2></div><div style="display:contents" dir="auto"><p id="2cdc5e6f-95bd-8043-9b0b-ce266ffe6bdb" class="">Nhà trường <strong>không tham gia hoạt động tài chính</strong> và <strong>không chịu trách nhiệm thu hồi nợ</strong>.</p></div><div style="display:contents" dir="auto"><p id="2cdc5e6f-95bd-80cb-927a-e1b67c8f7fa4" class="">Vai trò của Nhà trường bao gồm:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2cdc5e6f-95bd-8088-b9bf-feb551289be1" class="numbered-list" start="1"><li>Thông tin, giới thiệu chương trình đến sinh viên;</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2cdc5e6f-95bd-8084-beb9-d0c50eb8b80d" class="numbered-list" start="2"><li>Xác nhận sinh viên đang theo học tại Trường;</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2cdc5e6f-95bd-8036-94f4-dd3c16ad0d74" class="numbered-list" start="3"><li>Hỗ trợ đầu mối phối hợp triển khai (Phòng CTSV/Đoàn–Hội);</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2cdc5e6f-95bd-80e2-a504-c046ca1a8a4d" class="numbered-list" start="4"><li>Theo dõi, đánh giá tác động xã hội của chương trình đối với sinh viên.</li></ol></div><div style="display:contents" dir="auto"><hr id="2cdc5e6f-95bd-80f5-ac54-d4fd6369f414"/></div><div style="display:contents" dir="auto"><h2 id="2cdc5e6f-95bd-80b3-9ab9-dc97f2937384" class=""><strong>VI. KẾ HOẠCH THÍ ĐIỂM</strong></h2></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-801a-afb1-c5b03acf2f15" class="bulleted-list"><li style="list-style-type:disc">Quy mô dự kiến: <strong>300–500 sinh viên</strong>;</li></ul></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-8089-bc10-ceaa50ed51ce" class="bulleted-list"><li style="list-style-type:disc">Thời gian thí điểm: <strong>03–06 tháng</strong>;</li></ul></div><div style="display:contents" dir="auto"><ul id="2cdc5e6f-95bd-804f-9117-ed9121bd312b" class="bulleted-list"><li style="list-style-type:disc">Sau giai đoạn thí điểm, hai bên sẽ tổng kết, đánh giá hiệu quả và xem xét khả năng mở rộng.</li></ul></div><div style="display:contents" dir="auto"><hr id="2cdc5e6f-95bd-8029-afff-de1d0f2d73a9"/></div><div style="display:contents" dir="auto"><h2 id="2cdc5e6f-95bd-805b-b957-e8b8ea262e44" class=""><strong>VII. ĐỀ NGHỊ</strong></h2></div><div style="display:contents" dir="auto"><p id="2cdc5e6f-95bd-80ef-b34c-c90621f2c539" class="">Kính đề nghị Ban Giám hiệu Nhà trường xem xét chủ trương cho phép triển khai <strong>chương trình thí điểm</strong>, đồng thời cử đơn vị đầu mối phối hợp để hoàn thiện quy trình triển khai phù hợp với điều kiện thực tế của Trường.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
