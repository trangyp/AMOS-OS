---
tags: [vietnamese]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>BÁO CÁO ĐẠI HỘI ĐỒNG CỔ ĐÔNG &amp; HỘI ĐỒNG QUẢN TRỊ</title><style>
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
	
</style></head><body><article id="2bbc5e6f-95bd-8022-8433-e9bc90dd950f" class="page sans"><header><h1 class="page-title" dir="auto"><strong>BÁO CÁO ĐẠI HỘI ĐỒNG CỔ ĐÔNG &amp; HỘI ĐỒNG QUẢN TRỊ</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-8093-a1eb-f44755ecedd9" class=""><strong>MÔ HÌNH QUỸ TÍN DỤNG VI MÔ UNICAPITAL – NGÂN HÀNG NHỎ CỦA CHÚNG TA</strong></h2></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80a0-a395-e0009a5c6d19" class=""><strong>Người trình bày:</strong> Hồ Anh Tuấn – Tổng Giám đốc, Thành viên HĐQT</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80b0-965a-d4ea0dea360f" class=""><strong>Ngày:</strong> 30/11/2025</p></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-8034-ab63-fccbcca2383f"/></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-80f7-805d-eaae144af84b" class=""><strong>I. 
LỜI MỞ ĐẦU</strong></h1></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80c2-8567-e4ba55a51d0f" class="">Kính thưa Quý Cổ đông, Quý Thành viên Hội đồng Quản trị và Quý Đối tác,</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80b6-9c16-cf88ccb26ffa" class="">Hôm nay tôi trình bày mô hình <strong>UniCapital</strong> – một <strong>ngân hàng vi mô chuẩn quốc tế</strong>, đóng vai trò <strong>động cơ tài chính trung tâm</strong> của toàn bộ hệ sinh thái Unipower.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8080-9129-dac382aa4923" class="">Trong 36 tháng, chúng ta đã xây dựng xong 5 lớp nền tảng:</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8087-a5e0-eb64874dbb11" class=""><strong>(1) Nguồn vốn 0% từ Membership</strong></p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80ed-9aaf-d452628f2568" class=""><strong>(2) Công nghệ scoring – thu nợ tự động</strong></p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80e0-bc45-d53f7925dbe3" class=""><strong>(3) Hệ sinh thái khách hàng captive (tài xế – công nhân)</strong></p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80a1-ad3f-ecc4e17cd24f" class=""><strong>(4) Tài sản đảm bảo thật (xe EV – thu nhập thật)</strong></p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80fc-954d-f35ce0c256cb" class=""><strong>(5) Mô hình rủi ro nhiều lớp</strong></p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-803d-bdae-e6f053b50b83" class="">Đến thời điểm này, UniCapital đủ điều kiện tăng tốc và tạo ra mức lợi nhuận mà các ngân hàng thương mại không thể đạt vì chi phí vốn của họ gấp 2–3 lần chúng ta.</p></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-8040-96a2-ee9bdbff5f84"/></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-80a9-892d-f7191dea78be" class=""><strong>II. 
CẤU TRÚC VỐN UNICAPITAL – LỢI THẾ KHÔNG TỔ CHỨC TÀI CHÍNH NÀO CÓ</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-8009-8307-d4382801d02b" class=""><strong>1. 
Nguồn vốn 2025–2026</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-807e-8983-d5f85c48b038" class=""><strong>Bảng 1 – Cơ cấu nguồn vốn UniCapital (đơn vị: tỷ đồng)</strong></h3></div><div style="display:contents" dir="ltr"><table id="2bbc5e6f-95bd-8042-966b-d193f644d01b" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8045-880a-dd6bad27460a"><th id="Vb~M" class="simple-table-header-color simple-table-header"><strong>Khoản mục</strong></th><th id="L[eY" class="simple-table-header-color simple-table-header"><strong>Giá trị</strong></th><th id="hshg" class="simple-table-header-color simple-table-header"><strong>Lãi suất</strong></th><th id="KXOo" class="simple-table-header-color simple-table-header"><strong>Đặc điểm dòng vốn</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8082-b985-d6af8083b074"><td id="Vb~M" class=""><strong>Vốn Membership iSAC</strong></td><td id="L[eY" class=""><strong>200</strong></td><td id="hshg" class=""><strong>0%</strong></td><td id="KXOo" class="">Dài hạn 10–15 năm, không rút gốc</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80a7-a2a5-df8a1f8569b7"><td id="Vb~M" class=""><strong>Vốn vay ưu đãi/ODA</strong></td><td id="L[eY" class=""><strong>300–500</strong></td><td id="hshg" class=""><strong>1,8–2,5%</strong></td><td id="KXOo" class="">Gắn với xe điện – năng lượng xanh</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80e5-8d60-c14cd31392e4"><td id="Vb~M" class=""><strong>Vốn vay thương mại</strong></td><td id="L[eY" class=""><strong>700–1.000</strong></td><td id="hshg" class=""><strong>7,5–8,5%</strong></td><td id="KXOo" class="">Bổ sung, 
mở rộng đội xe EV</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8075-8b94-eb246d8944df"><td id="Vb~M" class=""><strong>Vốn huy động nội bộ</strong></td><td id="L[eY" class=""><strong>50–80</strong></td><td id="hshg" class=""><strong>0%</strong></td><td id="KXOo" class="">Nhân viên – cổ đông</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80e7-b894-d8366014be5d" class=""><strong>Tổng nguồn vốn khả dụng 2026:</strong> <strong>1.250 – 1.780 tỷ đồng</strong></p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80d9-b954-f6e0d55ea718" class=""><strong>Chi phí vốn bình quân (CoF):</strong></p></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-807c-aeb7-f6724a84d69e" class="bulleted-list"><li style="list-style-type:disc">UniCapital: <strong>~3,2%</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-800f-8c67-fdaac0a06b10" class="bulleted-list"><li style="list-style-type:disc">Ngân hàng thương mại: <strong>6,0–7,5%</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-803b-b1ac-cf5ea20461c9" class="">→ <strong>UniCapital rẻ hơn ~55% chi phí vốn.</strong></p></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-80d2-b715-e455d7271ab1"/></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-802e-abe1-fb150b4d3e74" class=""><strong>III. HAI DÒNG TÍN DỤNG LÕI – “CỖ MÁY LỢI NHUẬN”</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-80aa-af86-e518481b8f2a" class=""><strong>1. 
Tín dụng xe điện EV</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-8090-9ec5-d1f2b4cf881a" class=""><strong>Giả định hoạt động 2026</strong></h3></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8033-a95a-c96aa4e68c3c" class="bulleted-list"><li style="list-style-type:disc"><strong>10.000 xe EV</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80e4-b414-fb9d7a8c5ce6" class="bulleted-list"><li style="list-style-type:disc"><strong>Giá xe:</strong> <strong>500 triệu/xe</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-807d-80f9-d14829cbb630" class="bulleted-list"><li style="list-style-type:disc"><strong>Cho vay:</strong> <strong>80%</strong> giá trị xe</li></ul></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-8092-aaed-d292a83ac56c" class=""><strong>Bảng 2 – Lợi nhuận tín dụng EV</strong></h3></div><div style="display:contents" dir="ltr"><table id="2bbc5e6f-95bd-80eb-a77a-d12a99c7cd20" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8098-9ed1-c06b2ae32e44"><th id=":eV}" class="simple-table-header-color simple-table-header"><strong>Khoản mục</strong></th><th id="eide" class="simple-table-header-color simple-table-header"><strong>Công thức</strong></th><th id="Ga@B" class="simple-table-header-color simple-table-header"><strong>Kết quả</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8002-95da-d0b412e8b2d6"><td id=":eV}" class=""><strong>Dư nợ EV</strong></td><td id="eide" class="">10.000 × 500 triệu × 80%</td><td id="Ga@B" class=""><strong>4.000 tỷ</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8049-b202-d1de2b1a664d"><td id=":eV}" class=""><strong>Doanh thu lãi</strong></td><td id="eide" class="">4.000 tỷ × <strong>10%</strong></td><td id="Ga@B" class=""><strong>400 t
ỷ/năm</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80de-bdf1-c7b494f921ad"><td id=":eV}" class=""><strong>Chi phí vốn ngoại</strong></td><td id="eide" class="">4.000 tỷ × <strong>2%</strong></td><td id="Ga@B" class=""><strong>80 tỷ/năm</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80ea-92ac-c5af412cee99"><td id=":eV}" class=""><strong>Lợi nhuận gộp mảng EV</strong></td><td id="eide" class="">400 – 80</td><td id="Ga@B" class=""><strong>320 tỷ/năm</strong></td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-8043-880a-ef4a463f4b5d" class=""><strong>Lợi thế rủi ro thấp</strong></h3></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80c2-8ee9-eff93aad4ecf" class="bulleted-list"><li style="list-style-type:disc">Xe là tài sản đảm bảo → thu hồi nhanh</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80e8-9e89-db315daa5b86" class="bulleted-list"><li style="list-style-type:disc">GPS + khóa từ xa</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8027-a097-d1161a115dc6" class="bulleted-list"><li style="list-style-type:disc">Bảo hiểm vật chất toàn phần</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-808b-94be-d768d81db475" class="bulleted-list"><li style="list-style-type:disc">Thu nhập tài xế → dòng tiền trả nợ thật</li></ul></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-808e-9b50-f5268faca765"/></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-8059-91b5-e992a3645007" class=""><strong>2. 
Tín dụng tiêu dùng vi mô (Công nhân VSIP)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-8083-8950-f3da03948bc6" class=""><strong>Giả định hoạt động 2026</strong></h3></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-802e-aa22-f2d30076f502" class="bulleted-list"><li style="list-style-type:disc"><strong>10.000 công nhân</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80b9-926f-ea1d704f6afa" class="bulleted-list"><li style="list-style-type:disc"><strong>Hạn mức:</strong> <strong>30–50 triệu/người</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80b7-a847-cedae82414b4" class="bulleted-list"><li style="list-style-type:disc"><strong>Lãi suất:</strong> <strong>18–24%/năm</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-802c-8861-dc1faaecd941" class="bulleted-list"><li style="list-style-type:disc"><strong>Dư nợ bình quân:</strong> <strong>~450 tỷ đồng</strong></li></ul></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-805f-9e1e-db9c8b52b8ec" class=""><strong>Bảng 3 – Lợi nhuận tín dụng vi mô</strong></h3></div><div style="display:contents" dir="ltr"><table id="2bbc5e6f-95bd-80ea-8b6f-f4468e1fcab8" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8075-bf90-ef96a2ad1844"><th id="gK@a" class="simple-table-header-color simple-table-header"><strong>Khoản mục</strong></th><th id="yxkA" class="simple-table-header-color simple-table-header"><strong>Công thức</strong></th><th id="@RWy" class="simple-table-header-color simple-table-header"><strong>Kết quả</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-808b-a1cc-d8467fb7865b"><td id="gK@a" class=""><strong>Dư nợ vi mô</strong></td><td id="yxkA" class="">10.000 × 45 triệu</td><td id="@RWy" class=""><strong>450 t
ỷ</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8049-bce9-e3124ff8e51e"><td id="gK@a" class=""><strong>Doanh thu lãi</strong></td><td id="yxkA" class="">450 tỷ × <strong>20%</strong></td><td id="@RWy" class=""><strong>90 tỷ/năm</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-805b-a665-d9910f3d44a2"><td id="gK@a" class=""><strong>Chi phí vốn</strong></td><td id="yxkA" class="">0%</td><td id="@RWy" class=""><strong>0 tỷ</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8045-8c17-f288182aca2a"><td id="gK@a" class=""><strong>Lợi nhuận gộp</strong></td><td id="yxkA" class="">90 – 0</td><td id="@RWy" class=""><strong>90 tỷ/năm</strong></td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-8021-b964-c1dddb394872"/></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-809c-9140-e6e530f6759a" class=""><strong>3. 
Tổng lợi nhuận gộp từ hai mảng</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-808b-98f3-dca0c40a57dd" class=""><strong>Bảng 4 – Lợi nhuận gộp 2 dòng tín dụng</strong></h3></div><div style="display:contents" dir="ltr"><table id="2bbc5e6f-95bd-8075-9440-cbd18838a632" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80f9-bb98-dc8402d064f7"><th id="@?TZ" class="simple-table-header-color simple-table-header"><strong>Hạng mục</strong></th><th id="KSB~" class="simple-table-header-color simple-table-header"><strong>Giá trị</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-801b-8cc5-e0e22bd33f61"><td id="@?TZ" class=""><strong>EV Lending</strong></td><td id="KSB~" class=""><strong>320 tỷ/năm</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80bb-8ca9-d33a14e0b4eb"><td id="@?TZ" class=""><strong>Vi mô tiêu dùng</strong></td><td id="KSB~" class=""><strong>90 tỷ/năm</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-804d-b39d-eb079462fce8"><td id="@?TZ" class=""><strong>Tổng lợi nhuận gộp</strong></td><td id="KSB~" class=""><strong>410 tỷ/năm</strong></td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80e7-957d-d7e803fb5f1b" class="">Đây mới chỉ là lợi nhuận từ <strong>lãi vay</strong>.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8051-9257-f298ca61080c" class="">UniCapital còn 5 nguồn thu phụ rất lớn (em sẽ đưa ở phần tiếp theo):</p></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80e2-975f-d682cdacc8d4" class="bulleted-list"><li style="list-style-type:disc">Phí bảo hiểm tín dụng</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80a6-8af5-cbf219a83af8" class="bulleted-list"><li style="list-style-type:disc">Phí quản lý khoản v
ay</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80a3-a517-ec89f4727db5" class="bulleted-list"><li style="list-style-type:disc">Phí ví điện tử UniApp</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80a2-bda7-dfe004e24894" class="bulleted-list"><li style="list-style-type:disc">Phí sạc iSAC</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80cd-8b38-cc745ab6ae6d" class="bulleted-list"><li style="list-style-type:disc">Phí bảo trì – dịch vụ EV</li></ul></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-80ae-a47b-c533e62e39ae"/></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-8053-887a-e3caf0feb3bd" class=""><strong>PHẦN 2 – BÁO CÁO TÀI CHÍNH DỰ PHÓNG 2026 (FS)</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-8004-bc06-e7da7823bea8" class=""><strong>1. Quy mô tài sản – dư nợ – vốn chủ</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80d3-805b-f8589d3d3f29" class=""><strong>Bảng 5 – Cơ cấu tài sản và nguồn vốn (tỷ đồng)</strong></h3></div><div style="display:contents" dir="ltr"><table id="2bbc5e6f-95bd-80e8-918d-c258a9a7dcf7" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80a7-b164-d8371147a9a4"><th id="Oxkx" class="simple-table-header-color simple-table-header"><strong>Khoản mục</strong></th><th id="HGC^" class="simple-table-header-color simple-table-header"><strong>Giá trị</strong></th><th id="[q}C" class="simple-table-header-color simple-table-header"><strong>Tỷ lệ cấu trúc</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-803d-9da5-f621a7763fb4"><td id="Oxkx" class=""><strong>1. 
Tài sản sinh lãi</strong></td><td id="HGC^" class=""></td><td id="[q}C" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80cf-a310-ebde703951bb"><td id="Oxkx" class="">• Dư nợ cho vay EV</td><td id="HGC^" class=""><strong>4.000</strong></td><td id="[q}C" class=""><strong>86,2%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8046-8a5e-e110b2b84e08"><td id="Oxkx" class="">• Dư nợ cho vay vi mô</td><td id="HGC^" class=""><strong>450</strong></td><td id="[q}C" class=""><strong>9,7%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80a9-b2f7-d71daec78800"><td id="Oxkx" class=""><strong>Tổng tài sản sinh lãi</strong></td><td id="HGC^" class=""><strong>4.450</strong></td><td id="[q}C" class=""><strong>95,9%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-806f-aab2-c3282c9a26e9"><td id="Oxkx" class=""><strong>2. 
Tài sản khác</strong></td><td id="HGC^" class=""><strong>190</strong></td><td id="[q}C" class=""><strong>4,1%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8092-a885-d047fbcce5e9"><td id="Oxkx" class=""><strong>Tổng tài sản</strong></td><td id="HGC^" class=""><strong>4.640</strong></td><td id="[q}C" class=""><strong>100%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80b9-be2c-fa803f2bdd48"><td id="Oxkx" class=""><strong>Nguồn vốn</strong></td><td id="HGC^" class=""></td><td id="[q}C" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80aa-a434-ed14c7694fe8"><td id="Oxkx" class="">• Vốn Membership 0%</td><td id="HGC^" class=""><strong>200</strong></td><td id="[q}C" class=""><strong>4,3%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80ce-ac5e-e7a1d01ccaed"><td id="Oxkx" class="">• Vốn vay ưu đãi 2%</td><td id="HGC^" class=""><strong>500</strong></td><td id="[q}C" class=""><strong>10,7%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8055-87b8-ff7d5d6e7c86"><td id="Oxkx" class="">• Vốn vay TMCP 8%</td><td id="HGC^" class=""><strong>900</strong></td><td id="[q}C" class=""><strong>19,4%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8036-971e-d4152f674d44"><td id="Oxkx" class="">• Vốn tái đầu tư (LN giữ lại)</td><td id="HGC^" class=""><strong>250–300</strong></td><td id="[q}C" class=""><strong>6%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8047-b5fb-d69275dece2a"><td id="Oxkx" class=""><strong>Tổng nguồn vốn</strong></td><td id="HGC^" class=""><strong>~1.850</strong></td><td id="[q}C" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-804d-be09-fc957ae28f8a"><td id="Oxkx" class=""><strong>Hệ số đòn bẩy</strong> (Asset/Equity)</td><td id="HGC^" class=""><strong>~2,5 
ần</strong></td><td id="[q}C" class="">Chuẩn ngân hàng vi mô</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80a1-b10c-e44c1eb4292d" class="">Ghi chú:</p></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8032-b140-ee7deabf0d8e" class="bulleted-list"><li style="list-style-type:disc">Tài sản ≥ vốn vì UniCapital vận hành theo mô hình ngân hàng vi mô (MicroBank), không phải doanh nghiệp.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80c3-9722-c67735fbebe2" class="bulleted-list"><li style="list-style-type:disc">Vốn chủ + Membership + LN giữ lại → đủ tiêu chuẩn CAR.</li></ul></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-80f9-b5b5-c19c6fe3e27f"/></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-8026-a82b-de6dabb45d26" class=""><strong>2. Báo cáo kết quả hoạt động 2026</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80df-8fff-c283a5bbbf44" class=""><strong>Bảng 6 – Báo cáo thu nhập (tỷ đồng)</strong></h3></div><div style="display:contents" dir="ltr"><table id="2bbc5e6f-95bd-80e5-b66f-d001d746ae48" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-806e-a298-e74de9d946e1"><th id="Xs~\" class="simple-table-header-color simple-table-header"><strong>Khoản mục</strong></th><th id="WWaV" class="simple-table-header-color simple-table-header"><strong>Công thức</strong></th><th id="~tN_" class="simple-table-header-color simple-table-header"><strong>Giá trị</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8008-881f-f4f31b447f69"><td id="Xs~\" class=""><strong>1. 
Doanh thu lãi thuần</strong></td><td id="WWaV" class=""></td><td id="~tN_" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8022-87fd-cf187af63bd6"><td id="Xs~\" class="">• Lãi từ EV Lending</td><td id="WWaV" class="">4.000 × <strong>10%</strong></td><td id="~tN_" class=""><strong>400</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-805a-98b7-eb6985319916"><td id="Xs~\" class="">• Lãi từ Vi mô</td><td id="WWaV" class="">450 × <strong>20%</strong></td><td id="~tN_" class=""><strong>90</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-803a-aa0b-d802bb26a340"><td id="Xs~\" class=""><strong>Tổng doanh thu lãi</strong></td><td id="WWaV" class=""></td><td id="~tN_" class=""><strong>490</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8043-b3ef-c46099cd0004"><td id="Xs~\" class=""><strong>2. Chi phí vốn</strong></td><td id="WWaV" class="">4.000 × <strong>2%</strong></td><td id="~tN_" class=""><strong>80</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80be-9709-d994b9ead924"><td id="Xs~\" class=""><strong>3. 
Thu nhập ngoài lãi</strong></td><td id="WWaV" class=""></td><td id="~tN_" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-801d-b947-de51b4cd6b1e"><td id="Xs~\" class="">• Phí bảo hiểm</td><td id="WWaV" class=""><strong>25–35</strong></td><td id="~tN_" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80cc-951b-cda0fa845645"><td id="Xs~\" class="">• Phí quản lý khoản vay</td><td id="WWaV" class=""><strong>15–20</strong></td><td id="~tN_" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-807b-be8f-df1bd2379d45"><td id="Xs~\" class="">• Phí iSAC – sạc – bảo trì</td><td id="WWaV" class=""><strong>30–45</strong></td><td id="~tN_" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8093-aa84-fbf5893a473e"><td id="Xs~\" class="">• Phí ví UniApp – thanh toán</td><td id="WWaV" class=""><strong>10–12</strong></td><td id="~tN_" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8023-b71f-c440e4aaed01"><td id="Xs~\" class=""><strong>Tổng Non-interest income</strong></td><td id="WWaV" class=""></td><td id="~tN_" class=""><strong>80–110</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-807b-ac87-d9c2f6aeabf5"><td id="Xs~\" class=""><strong>4. Dự phòng rủi ro (LLR)</strong></td><td id="WWaV" class="">~1,2% dư nợ</td><td id="~tN_" class=""><strong>55</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8022-8bb6-e2893345fbba"><td id="Xs~\" class=""><strong>5. 
Chi phí vận hành (OPEX)</strong></td><td id="WWaV" class="">12% doanh thu lãi</td><td id="~tN_" class=""><strong>58</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-803f-afb7-d65d98025319"><td id="Xs~\" class=""><strong>LỢI NHUẬN TRƯỚC THUẾ</strong></td><td id="WWaV" class="">490 – 80 + (80–110) – 55 – 58</td><td id="~tN_" class=""><strong>~380–405</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-806b-8279-d05d16ecb595"><td id="Xs~\" class=""><strong>Thuế TNDN (20%)</strong></td><td id="WWaV" class=""></td><td id="~tN_" class=""><strong>~75–80</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80d4-a0af-ddb5df870896"><td id="Xs~\" class=""><strong>LỢI NHUẬN SAU THUẾ</strong></td><td id="WWaV" class=""></td><td id="~tN_" class=""><strong>~305–325</strong></td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8066-99b5-c09f3b21a36f" class=""><strong>Dòng tiền hàng tháng:</strong></p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-801e-a1e3-e52464d4d4e4" class="">≈ <strong>26–28 tỷ/tháng</strong></p></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-80a8-b6e2-f92b9a067da6"/></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-801b-81f1-de7ca400ee93" class=""><strong>3. 
Chỉ số tài chính then chốt</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-8052-aae4-d1aab8b5e808" class=""><strong>Bảng 7 – KPI tài chính (Chuẩn ngân hàng vi mô)</strong></h3></div><div style="display:contents" dir="ltr"><table id="2bbc5e6f-95bd-8076-992b-d07f4a640324" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80aa-b975-c396a55c0bc3"><th id="`snw" class="simple-table-header-color simple-table-header"><strong>Chỉ số</strong></th><th id="f}KU" class="simple-table-header-color simple-table-header"><strong>UniCapital 2026</strong></th><th id="@tDS" class="simple-table-header-color simple-table-header"><strong>Ngân hàng TMCP</strong></th><th id=":r_X" class="simple-table-header-color simple-table-header"><strong>Nhận xét</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8078-97e9-e332fe2b9894"><td id="`snw" class=""><strong>NIM – Biên lãi ròng</strong></td><td id="f}KU" class=""><strong>~9,2%</strong></td><td id="@tDS" class="">3,2–3,8%</td><td id=":r_X" class="">Gấp 2,4–3 lần</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80d1-bf8d-c64f1b309c3b"><td id="`snw" class=""><strong>ROE – Tỷ suất sinh lời vốn chủ</strong></td><td id="f}KU" class=""><strong>140–150%</strong></td><td id="@tDS" class="">12–18%</td><td id=":r_X" class="">Gấp 8–12 lần</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-803d-a920-d421291f3e6e"><td id="`snw" class=""><strong>ROA – Tỷ suất sinh lời tài sản</strong></td><td id="f}KU" class=""><strong>6,3%</strong></td><td id="@tDS" class="">0,9–1,3%</td><td id=":r_X" class="">Gấp 6–7 lần</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80b1-a682-d3ca73117326"><td id="`snw" class=""><strong>CAR – Tỷ lệ an toàn vốn</strong></td><td id="f}KU" class=""><strong>&gt;12%</strong></td><td id="@tDS" c
lass="">8–11%</td><td id=":r_X" class="">Vượt chuẩn</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80c6-aaf7-f9e81cfb294a"><td id="`snw" class=""><strong>NPL – Tỷ lệ nợ xấu</strong></td><td id="f}KU" class=""><strong>&lt;1,5%</strong></td><td id="@tDS" class="">1,7–2,5%</td><td id=":r_X" class="">Kiểm soát tốt</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80c6-9521-d50a44c682a4"><td id="`snw" class=""><strong>Cost-to-income ratio (CIR)</strong></td><td id="f}KU" class=""><strong>~18–22%</strong></td><td id="@tDS" class="">35–45%</td><td id=":r_X" class="">Tối ưu vượt trội</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8061-a2e5-f076fda499c5"><td id="`snw" class=""><strong>Loan-to-Deposit Ratio (LDR)</strong></td><td id="f}KU" class=""><strong>&gt;120% (hợp lý)</strong></td><td id="@tDS" class="">80–95%</td><td id=":r_X" class="">Kiểu MicroBank</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-807b-bca0-fa35cfda34d1" class=""><strong>Kết luận:</strong> Hiệu suất UniCapital cao nhất trong toàn bộ ngành tài chính Việt Nam.</p></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-80bc-80ec-d57cba0f5c2a"/></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-80f3-a7dd-fb50bec75fab" class=""><strong>4. 
Biểu đồ phân tích</strong></h2></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8064-ae65-c67675fbbb68" class="">(Em trình bày dạng mô tả rõ, 
để khi đưa vào bản trình chiếu có thể dựng lại nhanh)</p></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80e0-8649-db5212942aab" class=""><strong>Biểu đồ 1 – Cơ cấu dư nợ 2026</strong></h3></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8075-a343-ca8f46ab9d81" class="bulleted-list"><li style="list-style-type:disc">EV Lending: <strong>89%</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80dd-9eed-faeac70bbe05" class="bulleted-list"><li style="list-style-type:disc">Vi mô công nhân: <strong>11%</strong></li></ul></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80a3-b361-cd7564d5f88b" class=""><strong>Biểu đồ 2 – Cơ cấu lợi nhuận</strong></h3></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80dd-8756-cfd82e7c9ccc" class="bulleted-list"><li style="list-style-type:disc">Lãi EV: <strong>78%</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80bb-a259-e919929bb4ee" class="bulleted-list"><li style="list-style-type:disc">Lãi vi mô: <strong>17%</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8055-a522-e9bcdb75e8e3" class="bulleted-list"><li style="list-style-type:disc">Non-interest income: <strong>5%</strong></li></ul></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-808a-b836-fbcb3951efd2" class=""><strong>Biểu đồ 3 – So sánh UniCapital vs Ngân hàng</strong></h3></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80fd-8ac6-d644291d2543" class="bulleted-list"><li style="list-style-type:disc">ROE: <strong>150% vs 15%</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8098-83ae-df64f31bd1bc" class="bulleted-list"><li style="list-style-type:disc">NIM: <strong>9,2% vs 3,5%</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-809e-8599-ce8b92050015" class="bulleted-list"><li s
tyle="list-style-type:disc">CIR: <strong>20% vs 40%</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80bd-b37b-ea050cb9984f" class="">→ Thể hiện rõ: UniCapital là <strong>ngân hàng vi mô hiệu suất cao nhất Việt Nam</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-8011-afc4-eebdb1cff3af"/></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-8027-b716-fb1161721ca2" class=""><strong>5. 
Phân tích nhạy cảm – Rủi ro – Kịch bản xấu</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-8088-a777-c5a352a419fc" class=""><strong>Bảng 8 – Kiểm thử sức chịu đựng (Stress Test)</strong></h3></div><div style="display:contents" dir="ltr"><table id="2bbc5e6f-95bd-8014-ab06-ccf7189a36d8" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8023-b8e9-ee2a0989ca96"><th id="^rzx" class="simple-table-header-color simple-table-header"><strong>Yếu tố</strong></th><th id="`NbZ" class="simple-table-header-color simple-table-header"><strong>Biến động</strong></th><th id="osLd" class="simple-table-header-color simple-table-header"><strong>Tác động</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80ef-90bf-f219fc015258"><td id="^rzx" class="">Nợ xấu tăng từ 1,5% → 3%</td><td id="`NbZ" class="">-1% lợi nhuận</td><td id="osLd" class="">LSST còn <strong>~260–280 tỷ</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8012-95fb-dd2c928c5649"><td id="^rzx" class="">Chi phí vốn tăng thêm 1%</td><td id="`NbZ" class="">-40 tỷ lợi nhuận</td><td id="osLd" class="">LSST còn <strong>~260–270 tỷ</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8033-b491-f4c35aa4b57e"><td id="^rzx" class="">EV trễ hạn 5%</td><td id="`NbZ" class="">-30 tỷ</td><td id="osLd" class="">Kiểm soát GPS/khóa xe</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80d2-a3a2-c2c72ffcec67"><td id="^rzx" class="">Công nhân mất việc 3%</td><td id="`NbZ" class="">-12 tỷ</td><td id="osLd" class="">Khấu trừ bảng lương giữ ổn</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80e9-914d-f3815179f898" class="">→ <strong>Mô hình rất bền</strong>, 
nhờ tài sản đảm bảo + dòng tiền thật.</p></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-80af-a313-ff36923d73de"/></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-8069-9667-cfb3b8558af4" class=""><strong>6. Tổng kết tài chính</strong></h2></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-805e-a555-c86dadd5ae98" class=""><strong>Lợi nhuận 2026:</strong> <strong>305–325 tỷ</strong></p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80d4-a55d-de67b4721ce5" class=""><strong>Tốc độ tăng trưởng LN kỳ vọng 2027:</strong> <strong>+70–90%</strong> (mở rộng đội xe + vi mô)</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8090-bf7e-fc903c30f2f6" class=""><strong>Dòng tiền tự do:</strong> <strong>dương liên tục – không phụ thuộc tín dụng ngân hàng</strong></p></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-80e2-b334-eaddf8ced5d9"/></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-8049-82f5-f3b7113bdd5e" class="">III. MÔ HÌNH VẬN HÀNH UNICAPITAL – NGÂN HÀNG VI MÔ CHUẨN QUỐC TẾ</h2></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80c1-bc2b-d9803c059f0a" class=""><strong>1. Cấu trúc tổ chức và tuyến báo cáo</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80da-8ba0-dc2300dc24c3" class=""><strong>1.1. 
Sơ đồ tổ chức tổng thể (cấp điều hành)</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8061-a082-c65d0eede3ee" class=""><strong>Bảng 1 – Cấu trúc tổ chức UniCapital (tinh gọn nhưng đủ lớp kiểm soát)</strong></p></div><div style="display:contents" dir="ltr"><table id="2bbc5e6f-95bd-8068-ad05-f14980a856d6" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80d8-8428-ef7f87c37ba3"><th id=":V|o" class="simple-table-header-color simple-table-header"><strong>Khối/Bộ phận</strong></th><th id="vT~|" class="simple-table-header-color simple-table-header"><strong>Nhân sự 2026 (dự kiến)</strong></th><th id="v]CR" class="simple-table-header-color simple-table-header"><strong>Vai trò chính</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-806d-8901-f01869e27284"><td id=":V|o" class="">Ban điều hành (Tổng – Phó TGĐ)</td><td id="vT~|" class="">3–4</td><td id="v]CR" class="">Định hướng chiến lược, phê duyệt tín dụng theo khung, làm việc với đối tác</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8038-bc80-f466e73cc84a"><td id=":V|o" class="">Khối Tín dụng EV</td><td id="vT~|" class="">10–12</td><td id="v]CR" class="">Thẩm định hồ sơ tài xế, xét duyệt hạn mức, theo dõi chất lượng dư nợ EV</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8058-8632-fae910626291"><td id=":V|o" class="">Khối Tín dụng vi mô công nhân</td><td id="vT~|" class="">6–8</td><td id="v]CR" class="">Thiết kế gói vay, làm việc với khu công nghiệp, xử lý hồ sơ nhanh</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-800c-8a93-c353d8b0547b"><td id=":V|o" class="">Khối Quản trị rủi ro (Rủi ro + Pháp chế)</td><td id="vT~|" class="">6–7</td><td id="v]CR" class="">Xây chính sách, giám sát nợ xấu, 
kiểm soát pháp lý hợp đồng</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8002-abed-f3c0daa1d1be"><td id=":V|o" class="">Khối Công nghệ – Dữ liệu</td><td id="vT~|" class="">8–10</td><td id="v]CR" class="">Vận hành hệ thống chấm điểm, ứng dụng di động, thu nợ tự động, báo cáo</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80db-99a3-f61c6fd5c4a5"><td id=":V|o" class="">Khối Vận hành – Thu hồi nợ</td><td id="vT~|" class="">10–12</td><td id="v]CR" class="">Nhắc nợ, thu nợ, xử lý nợ quá hạn, thu hồi tài sản, chăm sóc khách hàng</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8087-8a2b-e8b0226272c2"><td id=":V|o" class="">Khối Tài chính – Kế toán</td><td id="vT~|" class="">4–5</td><td id="v]CR" class="">Hạch toán, lập báo cáo tài chính, quản trị dòng tiền, làm việc với ngân hàng</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8040-b540-fb3dae713ab6"><td id=":V|o" class="">Khối Kiểm soát nội bộ</td><td id="vT~|" class="">3–4</td><td id="v]CR" class="">Kiểm tra chéo, kiểm soát quy trình, đánh giá tuân thủ</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80a4-9d4e-c7b3a5c35c5b"><td id=":V|o" class="">Tổng</td><td id="vT~|" class="">50–60</td><td id="v]CR" class="">Tương đương quy mô một ngân hàng vi mô đầy đủ chức năng</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8003-bfd0-caa04e13910c" class=""><strong>Tuyến báo cáo</strong></p></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80c5-969a-dd9f4fb89ac0" class="bulleted-list"><li style="list-style-type:disc">Các khối nghiệp vụ (Tín dụng, Vận hành, Công nghệ, 
Tài chính) báo cáo Tổng Giám đốc UniCapital.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80ab-bff1-fe18e7759125" class="bulleted-list"><li style="list-style-type:disc">Khối Kiểm soát nội bộ báo cáo trực tiếp Hội đồng Quản trị/Ủy ban Kiểm toán, không phụ thuộc Ban điều hành, bảo đảm khách quan.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-805e-a31b-e3092e63c8e9" class=""><strong>1.2. Nguyên tắc tổ chức</strong></h3></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8012-af75-f42917ffbb4e" class="bulleted-list"><li style="list-style-type:disc">Mọi quyết định cấp tín dụng đều phải đi qua ít nhất hai lớp:<div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8073-b877-c7ed4f76744d" class="bulleted-list"><li style="list-style-type:circle">Lớp chấm điểm định lượng (hệ thống).</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80e1-9cbd-db753781ec98" class="bulleted-list"><li style="list-style-type:circle">Lớp phê duyệt định tính (chuyên viên + cấp quản lý).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8042-9a63-e9570e215e14" class="bulleted-list"><li style="list-style-type:disc">Các chức năng “bán hàng – thẩm định – phê duyệt – thu nợ – kiểm soát nội bộ” được tách bạch rõ, tránh xung đột lợi ích.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80af-83ec-c4675ed565d4" class="bulleted-list"><li style="list-style-type:disc">Tất cả sản phẩm, hạn mức, lãi suất, điều kiện vay đều được chuẩn hóa thành quy trình, không đàm phán tùy hứng.</li></ul></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-80b7-9314-fc13ce8c8009"/></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80b6-8dd0-e369d44e7160" class=""><strong>2. 
Quy trình tín dụng EV – chuẩn hóa như dây chuyền</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80ca-92a6-e3fcd019e203" class=""><strong>2.1. Mục tiêu</strong></h3></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80e6-ae30-d00abb3adbde" class="bulleted-list"><li style="list-style-type:disc">Thời gian từ lúc tài xế nộp hồ sơ đến khi giải ngân:<div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8058-9209-e422f9225a62" class="bulleted-list"><li style="list-style-type:circle">Nội bộ (đã trong hệ sinh thái Unipower/iSAC): 1–2 ngày.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80b5-92da-f9cdb2ccc153" class="bulleted-list"><li style="list-style-type:circle">Tài xế mới: 3–5 ngày.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80d4-997b-e535ca56fb63" class="bulleted-list"><li style="list-style-type:disc">Nợ xấu EV mục tiêu: dưới 1,2% dư nợ.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-8033-9b0d-d9abc792af93" class=""><strong>2.2. 
Các bước chi tiết</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8034-9494-f04d9625a28b" class=""><strong>Bảng 2 – Quy trình cho vay EV</strong></p></div><div style="display:contents" dir="ltr"><table id="2bbc5e6f-95bd-809d-a5f7-db52c414b4c0" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-800b-b7d7-f8160f045444"><th id="[eZ_" class="simple-table-header-color simple-table-header"><strong>Bước</strong></th><th id="kY;c" class="simple-table-header-color simple-table-header"><strong>Trách nhiệm</strong></th><th id="QYos" class="simple-table-header-color simple-table-header"><strong>Công việc cụ thể</strong></th><th id="Ptp[" class="simple-table-header-color simple-table-header"><strong>Công cụ sử dụng</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8027-840b-dbf91d390d70"><td id="[eZ_" class="">1</td><td id="kY;c" class="">Tài xế – UniApp</td><td id="QYos" class="">Đăng ký nhu cầu vay mua EV/trả góp; 
nhập thông tin cá nhân, thu nhập, lịch sử lái xe (nếu có)</td><td id="Ptp[" class="">Ứng dụng UniApp</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80a0-8856-fc06eb85ab2b"><td id="[eZ_" class="">2</td><td id="kY;c" class="">Hệ thống chấm điểm</td><td id="QYos" class="">Tự động chấm điểm dựa trên lịch sử chạy xe, dữ liệu thu nhập, khu vực hoạt động</td><td id="Ptp[" class="">Mô-đun chấm điểm (AI scoring)</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80a0-a1d4-e380192d8681"><td id="[eZ_" class="">3</td><td id="kY;c" class="">Khối Tín dụng EV</td><td id="QYos" class="">Kiểm tra nhanh hồ sơ: CCCD, hộ khẩu, sao kê, hợp đồng lao động (nếu có)</td><td id="Ptp[" class="">Cổng kiểm tra hồ sơ</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80ee-beba-d8156a83d55a"><td id="[eZ_" class="">4</td><td id="kY;c" class="">Khối Rủi ro</td><td id="QYos" class="">Kiểm tra danh sách đen nội bộ, CIC (nếu tích hợp), xác nhận không có khoản vay rủi ro cao</td><td id="Ptp[" class="">Hệ thống tra cứu rủi ro</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-800e-a1b0-fe6e7a101fa6"><td id="[eZ_" class="">5</td><td id="kY;c" class="">Phê duyệt</td><td id="QYos" class="">Chuyên viên + Trưởng bộ phận phê duyệt trong khung; 
hồ sơ lớn báo cáo Ban TGĐ</td><td id="Ptp[" class="">Hệ thống phê duyệt 2 lớp</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80cd-aafe-ef34d5d867e1"><td id="[eZ_" class="">6</td><td id="kY;c" class="">Khối Tín dụng/Khách</td><td id="QYos" class="">Ký hợp đồng tín dụng, điều khoản thu hồi xe, gắn thiết bị, bảo hiểm bắt buộc</td><td id="Ptp[" class="">Ký số qua UniApp hoặc tại điểm giao dịch</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80a2-88bd-d0ee7b143b72"><td id="[eZ_" class="">7</td><td id="kY;c" class="">Khối Tài chính</td><td id="QYos" class="">Giải ngân thẳng cho bên bán xe (hãng EV/đại lý), tránh sử dụng sai mục đích</td><td id="Ptp[" class="">Kết nối ngân hàng thanh toán</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8050-a4d5-c86deec56a59"><td id="[eZ_" class="">8</td><td id="kY;c" class="">Khối Công nghệ</td><td id="QYos" class="">Gắn GPS, khóa xe từ xa, tích hợp vào hệ thống quản lý đội xe và ứng dụng</td><td id="Ptp[" class="">Hệ thống quản lý xe – thiết bị IoT</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8008-9d25-fb0769d5054b"><td id="[eZ_" class="">9</td><td id="kY;c" class="">Cổng thanh toán</td><td id="QYos" class="">Hàng ngày trích một phần doanh thu từ hoạt động chạy xe để thu nợ tự động</td><td id="Ptp[" class="">Cổng thanh toán, kết nối ví điện tử</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80d5-afc5-e19f1feabe5b"><td id="[eZ_" class="">10</td><td id="kY;c" class="">Khối Rủi ro/Vận hành</td><td id="QYos" class="">Theo dõi km/ngày, doanh thu/ngày, số ngày không hoạt động → cảnh báo sớm rủi ro</td><td id="Ptp[" class="">Bảng điều khiển rủi ro (dashboard)</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-801c-ad60-d03beb664b45" class=""><strong>2.3. 
Ma trận cảnh báo sớm</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80a7-b51d-c4cb1089c0ea" class=""><strong>Bảng 3 – Hệ thống cảnh báo sớm đối với khoản vay EV</strong></p></div><div style="display:contents" dir="ltr"><table id="2bbc5e6f-95bd-8072-b4f5-f534b32db3c8" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-805a-81c6-e079d0f6b876"><th id="&lt;fqS" class="simple-table-header-color simple-table-header"><strong>Chỉ số giám sát</strong></th><th id="Uj\E" class="simple-table-header-color simple-table-header"><strong>Ngưỡng 1 – Cảnh báo nhẹ</strong></th><th id="=lKi" class="simple-table-header-color simple-table-header"><strong>Ngưỡng 2 – Nguy cơ cao</strong></th><th id="]tTy" class="simple-table-header-color simple-table-header"><strong>Hành động</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8006-8791-fcd3164b6ed4"><td id="&lt;fqS" class="">Số ngày không chạy xe</td><td id="Uj\E" class="">3 ngày liên tiếp</td><td id="=lKi" class="">Từ 7 ngày liên tiếp trở lên</td><td id="]tTy" class="">Gọi điện xác minh, nhắc nhở, xem xét hạn chế tính năng</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8025-b953-cd4116bd729d"><td id="&lt;fqS" class="">Tỷ lệ trả nợ so với kế hoạch</td><td id="Uj\E" class="">Dưới 80% kế hoạch trong 30 ngày</td><td id="=lKi" class="">Dưới 60% kế hoạch trong 60 ngày</td><td id="]tTy" class="">Làm việc với tài xế, xem xét cơ cấu lại khoản vay</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8010-ad99-c73a8d9d4020"><td id="&lt;fqS" class="">Định vị GPS xe</td><td id="Uj\E" class="">Thường xuyên qua biên tỉnh, khu lạ</td><td id="=lKi" class="">Gần khu vực biên giới, cảng, bãi xe lạ</td><td id="]tTy" class="">Cảnh báo rủi ro, 
xem xét thu hồi xe</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80f5-bfc7-ca573a6f5ea2"><td id="&lt;fqS" class="">Lịch sử tai nạn/vi phạm</td><td id="Uj\E" class="">1–2 lần/năm</td><td id="=lKi" class="">Trên 3 lần/năm</td><td id="]tTy" class="">Tăng giám sát, yêu cầu đào tạo lại</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8080-8fca-c8d8e2db7d60"><td id="&lt;fqS" class="">Phản hồi tiêu cực từ khách hàng</td><td id="Uj\E" class="">Rải rác</td><td id="=lKi" class="">Nhiều phản ánh nghiêm trọng (an toàn, đạo đức)</td><td id="]tTy" class="">Dừng cấp chuyến, xem xét chấm dứt hợp đồng, thu hồi xe</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-800d-a97b-d33207b9eadd"/></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-805c-b022-cf709de06c00" class=""><strong>3. Quy trình tín dụng vi mô công nhân – đơn giản, khép kín, thu nợ qua bảng lương</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-8044-944e-f22633173c67" class=""><strong>3.1. 
Thiết kế sản phẩm chuẩn</strong></h3></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8082-8a36-dedcface6277" class="bulleted-list"><li style="list-style-type:disc">Đối tượng: công nhân làm việc tại các khu công nghiệp có ký kết hợp tác (VSIP, AMATA, Long Hậu…).</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8012-84f7-deba1184facc" class="bulleted-list"><li style="list-style-type:disc">Hạn mức: 10–50 triệu đồng/người, theo thâm niên, thu nhập, lịch sử tín dụng nội bộ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8010-b953-d5784e84f7e8" class="bulleted-list"><li style="list-style-type:disc">Thời hạn: 6–24 tháng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80a7-88d4-ebdeb9018b06" class="bulleted-list"><li style="list-style-type:disc">Mục đích vay: chi tiêu gia đình, học phí con, sửa nhà, y tế… (không cho vay đầu cơ rủi ro).</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80e9-ae71-e579ecfe8af5" class="bulleted-list"><li style="list-style-type:disc">Cách thu nợ: khấu trừ trực tiếp vào bảng lương hằng tháng qua thỏa thuận ba bên (UniCapital – Doanh nghiệp – Người lao động).</li></ul></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-800a-8cb1-d23e5ca2ad08" class=""><strong>3.2. 
Quy trình chi tiết</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8054-a09d-f893756625a0" class=""><strong>Bảng 4 – Quy trình cho vay vi mô công nhân</strong></p></div><div style="display:contents" dir="ltr"><table id="2bbc5e6f-95bd-8025-b9e9-f2e51c5f73c9" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80fb-8f17-dec738812d63"><th id="\pcI" class="simple-table-header-color simple-table-header"><strong>Bước</strong></th><th id="{@UH" class="simple-table-header-color simple-table-header"><strong>Trách nhiệm</strong></th><th id="e\no" class="simple-table-header-color simple-table-header"><strong>Nội dung</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80cc-b7bc-fbd1f3f586b7"><td id="\pcI" class="">1</td><td id="{@UH" class="">Doanh nghiệp (khu công nghiệp)</td><td id="e\no" class="">Ký thỏa thuận hợp tác: chia sẻ dữ liệu lương, danh sách nhân sự, quy trình khấu trừ lương</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80d5-8393-fec9a0743c79"><td id="\pcI" class="">2</td><td id="{@UH" class="">Công nhân</td><td id="e\no" class="">Đăng ký vay qua ứng dụng, kiosk tại khu công nghiệp hoặc thông qua cán bộ nhân sự</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80c4-8479-ff4d5f98317d"><td id="\pcI" class="">3</td><td id="{@UH" class="">Hệ thống chấm điểm</td><td id="e\no" class="">Chấm điểm dựa trên thu nhập, thời gian làm việc, lịch sử vay, số người phụ thuộc</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8029-b4b6-cfaadf5a4b9f"><td id="\pcI" class="">4</td><td id="{@UH" class="">Khối Tín dụng vi mô</td><td id="e\no" class="">Kiểm tra hồ sơ đơn giản (CCCD, hợp đồng lao động, 
bảng lương gần nhất)</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-804d-b7a5-ced93493450b"><td id="\pcI" class="">5</td><td id="{@UH" class="">Bộ phận phê duyệt</td><td id="e\no" class="">Phê duyệt dựa trên khung hạn mức theo điểm tín dụng, không phê duyệt cảm tính</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-807b-8670-c3388e752188"><td id="\pcI" class="">6</td><td id="{@UH" class="">UniCapital – Doanh nghiệp – NLĐ</td><td id="e\no" class="">Ký hợp đồng ba bên, xác nhận cơ chế khấu trừ lương</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8077-a5e6-c7113d555756"><td id="\pcI" class="">7</td><td id="{@UH" class="">Khối Tài chính</td><td id="e\no" class="">Giải ngân qua tài khoản ngân hàng hoặc ví điện tử của người lao động</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80cb-841f-ebf19fd8959d"><td id="\pcI" class="">8</td><td id="{@UH" class="">Doanh nghiệp/UniCapital</td><td id="e\no" class="">Hằng tháng doanh nghiệp khấu trừ lương và chuyển về UniCapital</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80a4-8313-eb4d16bc3610"><td id="\pcI" class="">9</td><td id="{@UH" class="">Khối Thu nợ/Rủi ro</td><td id="e\no" class="">Nếu nghỉ việc: kích hoạt nhắc nợ sớm, đề nghị trả một lần hoặc tái cơ cấu khoản vay</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-8095-804f-feda159c110a" class=""><strong>3.3. 
Ưu điểm mô hình</strong></h3></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80f3-9fab-d968128079bf" class="bulleted-list"><li style="list-style-type:disc">Nợ xấu thấp, do thu nợ trực tiếp từ bảng lương.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8099-a50d-c9c2e80d8eba" class="bulleted-list"><li style="list-style-type:disc">Chi phí thẩm định và thu nợ rất thấp, phần lớn tự động.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-804d-b24c-c01820c7affb" class="bulleted-list"><li style="list-style-type:disc">Tăng gắn kết lâu dài với khu công nghiệp: khoản vay trở thành một phần “phúc lợi tài chính” cho người lao động.</li></ul></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-80a3-bcd5-d1f12a4c7d83"/></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-8098-b364-ca40301d2adf" class=""><strong>4. Hệ thống công nghệ – trái tim vận hành</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80c5-90b4-ff9412bf41c0" class=""><strong>4.1. 
Kiến trúc hệ thống</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8089-ad47-d1e3fb3677c8" class=""><strong>Bảng 5 – Các mô-đun công nghệ chính</strong></p></div><div style="display:contents" dir="ltr"><table id="2bbc5e6f-95bd-8014-8fc2-de27296689cf" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80c5-a51b-fb0bda06da6c"><th id="rjsO" class="simple-table-header-color simple-table-header"><strong>Mô-đun</strong></th><th id="Qn[m" class="simple-table-header-color simple-table-header"><strong>Chức năng chính</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80be-85a4-c1603ae4737a"><td id="rjsO" class="">Ứng dụng UniApp</td><td id="Qn[m" class="">Đăng ký vay, tra cứu dư nợ, lịch sử trả nợ, nhận thông báo, tương tác CSKH</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-806c-a3fd-dd20c32106fe"><td id="rjsO" class="">Hệ thống chấm điểm (Scoring)</td><td id="Qn[m" class="">Thu thập dữ liệu, tính điểm tín dụng EV và vi mô</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-804b-bc09-faa58f0d0c70"><td id="rjsO" class="">Hệ thống quản lý khoản vay</td><td id="Qn[m" class="">Lưu toàn bộ hợp đồng, kế hoạch trả nợ, lịch sử thay đổi</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80e7-a5f0-ebda32596076"><td id="rjsO" class="">Cổng thanh toán</td><td id="Qn[m" class="">Kết nối ngân hàng, ví, thu tự động, khấu trừ doanh thu, khấu trừ lương</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80f6-9877-f14398c36419"><td id="rjsO" class="">Bảng điều khiển rủi ro</td><td id="Qn[m" class="">Theo dõi nợ quá hạn, nợ xấu, các cảnh báo sớm</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8045-83f8-fd4de044e9a0"><td id="rjsO" class="">Hệ thống báo cáo quản trị</td><td id="Qn[m" class="">Lập báo cáo HĐQT, 
báo cáo cơ quan quản lý, phân tích lợi nhuận theo phân khúc</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80e5-88c6-f4c65e82ec4e" class=""><strong>4.2. Nguyên tắc thiết kế</strong></h3></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80a2-a684-d0a0b3c65b8d" class="bulleted-list"><li style="list-style-type:disc">Mọi giao dịch đều có dấu vết, truy xuất được (audit trail) theo chuẩn ngân hàng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8028-8c5a-faaf2efbba6b" class="bulleted-list"><li style="list-style-type:disc">Hạn chế thao tác tay: hệ thống tự sinh lịch trả nợ, tự tính lãi, tự phân loại nợ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80a7-9cd2-f3f7e2187da2" class="bulleted-list"><li style="list-style-type:disc">Phân quyền chặt chẽ: nhân viên chỉ được xem và thao tác đúng phần mình phụ trách.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80c0-921f-d392cfb6da77" class="bulleted-list"><li style="list-style-type:disc">Kết nối hai chiều với các nền tảng khác trong hệ sinh thái Unipower (iSAC, nền tảng vận tải, chăm sóc khách hàng…).</li></ul></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-80be-ba2b-e90efdc365cc"/></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80e7-afc0-d32864cda96a" class=""><strong>5. Quản trị rủi ro – lớp phòng thủ ba tầng</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-807b-8d4d-c4ea9d5c83ab" class=""><strong>5.1. 
Khung rủi ro tổng thể</strong></h3></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8082-99c8-cc0e5b45c7ac" class="bulleted-list"><li style="list-style-type:disc">Tầng 1: Bộ phận kinh doanh và tín dụng – quản lý rủi ro trong hoạt động hằng ngày.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-807b-b93f-d6a540551aa4" class="bulleted-list"><li style="list-style-type:disc">Tầng 2: Khối Quản trị rủi ro – thiết lập chính sách, giám sát, phân tích, cảnh báo.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80d2-8ba0-eba659b79df6" class="bulleted-list"><li style="list-style-type:disc">Tầng 3: Kiểm soát nội bộ – kiểm tra độc lập, đánh giá tuân thủ, đề xuất xử lý vi phạm.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80ea-9ab0-e3689e26ca98" class=""><strong>5.2. 
Các loại rủi ro chính</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80bf-9de8-cf6b38c6126b" class=""><strong>Bảng 6 – Ma trận rủi ro</strong></p></div><div style="display:contents" dir="ltr"><table id="2bbc5e6f-95bd-80e5-ac44-e1e4b2fe45d4" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8061-abb0-c7572dfc6238"><th id="yz`V" class="simple-table-header-color simple-table-header"><strong>Loại rủi ro</strong></th><th id="cXS[" class="simple-table-header-color simple-table-header"><strong>Nguồn phát sinh</strong></th><th id="|GAD" class="simple-table-header-color simple-table-header"><strong>Cách kiểm soát chính</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80c7-b5d0-fa992aafde6d"><td id="yz`V" class="">Rủi ro tín dụng</td><td id="cXS[" class="">Tài xế mất thu nhập, công nhân nghỉ việc, lạm dụng</td><td id="|GAD" class="">Chấm điểm chặt, tài sản đảm bảo, thu nợ tự động, hợp đồng ba bên</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80b3-aa78-e77f1a52b17e"><td id="yz`V" class="">Rủi ro vận hành</td><td id="cXS[" class="">Sai sót quy trình, gian lận nội bộ</td><td id="|GAD" class="">Chuẩn hóa quy trình, phân quyền, kiểm soát nội bộ định kỳ</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80fd-b9e1-f9006014d79d"><td id="yz`V" class="">Rủi ro pháp lý</td><td id="cXS[" class="">Hợp đồng, tranh chấp, vi phạm quy định</td><td id="|GAD" class="">Pháp chế rà soát trước khi triển khai sản phẩm, tư vấn độc lập</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80bf-9f39-db8575a5183b"><td id="yz`V" class="">Rủi ro công nghệ</td><td id="cXS[" class="">Mất dữ liệu, tấn công mạng</td><td id="|GAD" class="">Sao lưu, mã hóa, giám sát an ninh mạng, 
phân quyền hệ thống</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80c0-84cd-d05c872b1fba"><td id="yz`V" class="">Rủi ro thanh khoản</td><td id="cXS[" class="">Mismatch dòng tiền vào – ra</td><td id="|GAD" class="">Lập kế hoạch dòng tiền tuần/tháng, hạn mức dự phòng với ngân hàng</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-806f-ac9c-ceb1311df5d9" class=""><strong>5.3. Chỉ tiêu kiểm soát rủi ro</strong></h3></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80f0-9bfb-f3ca3d58ca92" class="bulleted-list"><li style="list-style-type:disc">Nợ xấu (NPL):<div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8097-aeb3-dccf6c14b0a3" class="bulleted-list"><li style="list-style-type:circle">EV: không vượt 1,5%.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8007-abbf-fdf4f2b5de9f" class="bulleted-list"><li style="list-style-type:circle">Vi mô: không vượt 2%.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-808e-bc95-f6b6a4f837ce" class="bulleted-list"><li style="list-style-type:disc">Dự phòng bao phủ nợ xấu (Coverage ratio): tối thiểu 120%.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80de-bf51-cae284b72cfa" class="bulleted-list"><li style="list-style-type:disc">Tỷ lệ tập trung: dư nợ với một khách hàng/nhóm khách hàng không vượt khung quy định nội bộ.</li></ul></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-80c9-9cf6-fc465dcb7ff1"/></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80b2-8dfd-f6f093df3477" class=""><strong>6. Nhân sự – cơ chế đãi ngộ gắn với chất lượng tài sản</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80fb-b241-fa2a7a8eb9e8" class=""><strong>6.1. 
Nguyên tắc</strong></h3></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80ed-ade1-c399b0f09e2e" class="bulleted-list"><li style="list-style-type:disc">Thưởng không gắn với “số tiền giải ngân”, mà gắn với chất lượng danh mục sau 6–12 tháng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8081-8db3-da11420eb898" class="bulleted-list"><li style="list-style-type:disc">Gắn lợi ích cá nhân với nợ xấu: bộ phận để nợ xấu vượt khung sẽ bị trừ thưởng.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80f7-9f5d-fa7a11f05fc1" class=""><strong>6.2. 
Bảng gợi ý KPI cho các khối chính</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8012-ae0f-c31aef7c591b" class=""><strong>Bảng 7 – KPI theo khối</strong></p></div><div style="display:contents" dir="ltr"><table id="2bbc5e6f-95bd-8016-84d0-ee0ec1e2797b" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80f3-a454-ec5f6ccd44fb"><th id="L&gt;kg" class="simple-table-header-color simple-table-header"><strong>Khối</strong></th><th id="Bcc:" class="simple-table-header-color simple-table-header"><strong>KPI chính</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8016-9a52-de0abfec7483"><td id="L&gt;kg" class="">Tín dụng EV</td><td id="Bcc:" class="">Tăng trưởng dư nợ, tỷ lệ nợ xấu, thời gian xử lý hồ sơ</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-808b-ae4c-c6abcb1e73e4"><td id="L&gt;kg" class="">Tín dụng vi mô</td><td id="Bcc:" class="">Số lượng khách được phục vụ, tỷ lệ khách nghỉ việc nhưng vẫn thu hồi đủ nợ</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-808f-a753-c2c170469f65"><td id="L&gt;kg" class="">Quản trị rủi ro</td><td id="Bcc:" class="">Tỷ lệ nợ xấu toàn hệ, số cảnh báo sớm, số vụ việc được xử lý kịp thời</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-8099-acdf-e35de4d20596"><td id="L&gt;kg" class="">Công nghệ – Dữ liệu</td><td id="Bcc:" class="">Thời gian xử lý giao dịch, thời gian hệ thống ngừng hoạt động</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80ab-87f2-f8e569d37f06"><td id="L&gt;kg" class="">Vận hành – Thu nợ</td><td id="Bcc:" class="">Tỷ lệ thu nợ đúng hạn, số nợ nhóm 2 kéo về nhóm 1, 
chi phí thu hồi trên một đồng nợ thu được</td></tr></div><div style="display:contents" dir="ltr"><tr id="2bbc5e6f-95bd-80be-b725-eaab013c4bcb"><td id="L&gt;kg" class="">Kiểm soát nội bộ</td><td id="Bcc:" class="">Số lỗi quy trình phát hiện, số kiến nghị cải tiến được áp dụng</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-808f-8f7a-e2bd4256d0fa"/></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-8081-ac84-c0baa18b23e2" class=""><strong>7. Kiểm soát nội bộ – bảo vệ cổ đông và hệ thống</strong></h3></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8064-8d76-f30d05e2af8d" class="bulleted-list"><li style="list-style-type:disc">Kiểm tra định kỳ theo quý: chọn mẫu hồ sơ cho vay để kiểm tra lại đầy đủ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80ef-9e02-c4606321e766" class="bulleted-list"><li style="list-style-type:disc">Kiểm tra đột xuất khi xuất hiện dấu hiệu bất thường (nợ xấu tăng, vi phạm quy trình tăng).</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80cf-af5e-e7856e8d40a1" class="bulleted-list"><li style="list-style-type:disc">Báo cáo trực tiếp HĐQT: Khối Kiểm soát nội bộ độc lập với Ban điều hành trong đánh giá và kiến nghị.</li></ul></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-80d4-82cf-d38429b19f43"/></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80df-b3c5-f1d7c6673906" class=""><strong>8. 
Tổng kết vận hành</strong></h3></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80af-9667-fdb4b8c17337" class="bulleted-list"><li style="list-style-type:disc">Mô hình UniCapital được thiết kế như một ngân hàng vi mô hoàn chỉnh:<div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80c1-a900-cfe2383d5638" class="bulleted-list"><li style="list-style-type:circle">Sản phẩm rõ ràng, tập khách hàng rõ ràng, nguồn vốn rẻ rõ ràng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8026-abf9-c637aac31c81" class="bulleted-list"><li style="list-style-type:circle">Hệ thống công nghệ chấm điểm, quản lý, thu nợ tự động.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-803d-aa70-ffd016e72999" class="bulleted-list"><li style="list-style-type:circle">Khung quản trị rủi ro ba tầng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8062-b966-dcca4d972d73" class="bulleted-list"><li style="list-style-type:circle">Cơ chế nhân sự gắn với chất lượng tài sản, không chỉ chạy theo quy mô giải ngân.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-800f-9d80-c298992e93d3" class="bulleted-list"><li style="list-style-type:disc">Nhờ đó, UniCapital có khả năng:<div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80d6-8e00-f9435c299c20" class="bulleted-list"><li style="list-style-type:circle">Duy trì biên lợi nhuận (NIM) ở mức rất cao.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80fe-adc2-eaa30017e5f1" class="bulleted-list"><li style="list-style-type:circle">Kiểm soát nợ xấu trong vùng an toàn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-806d-baa3-cd1752c89e89" class="bulleted-list"><li style="list-style-type:circle">Tăng trưởng dư nợ mà không phải tăng nhân sự tương ứng, 
giữ chi phí vận hành trên dư nợ ở mức thấp.</li></ul></div></li></ul></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
