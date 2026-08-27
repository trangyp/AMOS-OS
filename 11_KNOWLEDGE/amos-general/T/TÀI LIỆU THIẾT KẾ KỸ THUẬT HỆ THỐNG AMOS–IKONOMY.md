---
tags: [amos-general]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>TÀI LIỆU THIẾT KẾ KỸ THUẬT HỆ THỐNG AMOS–IKONOMY</title><style>
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
	
</style></head><body><article id="2eac5e6f-95bd-801e-b207-db48cde904eb" class="page sans"><header><h1 class="page-title" dir="auto"><strong>TÀI LIỆU THIẾT KẾ KỸ THUẬT HỆ THỐNG AMOS–IKONOMY</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80b4-865f-c5c7bff0b2e3" class=""><strong>(So với thiết kế IKONOMY ban đầu và mặt bằng công nghệ hiện hành)</strong></p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80b2-8f23-c010c2f74ffd" class=""><strong>Phiên bản:</strong> 1.0</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8049-bc98-d1709a2674d4" class=""><strong>Phạm vi:</strong> 01 mô-đun điện phân nước công suất nhỏ (≈1 kW) và lớp điều khiển AMOS</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80c2-b765-ff9493b5d24b" class=""><strong>Mục đích tài liệu:</strong> thiết kế – sản xuất – tích hợp – thẩm định – triển khai thực tế</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80a3-88f1-ceb43c0a30f4" class="">AMOS-IKONOMY được đánh giá là dẫn đầu trong phân khúc module vì <strong>đồng thời đạt được các yếu tố vốn mâu thuẫn nhau</strong>:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-806e-983d-ee8e1f487c82" class="numbered-list" start="1"><li>Hiệu suất điện năng cao, 
gần trần vật lý.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-80be-ad71-c03d7ff0d5c9" class="numbered-list" start="2"><li>Tuổi thọ dài hơn đáng kể so với cùng cấu hình.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-809e-9240-ede6ddd71c8e" class="numbered-list" start="3"><li>Uptime ≥98% trong điều kiện thực tế.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-8007-82ce-e82d0eb50b14" class="numbered-list" start="4"><li>Chi phí vòng đời thấp hơn 25–40%.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-80a3-897d-fa39dd3a2175" class="numbered-list" start="5"><li>Có thể triển khai tại các khu vực khó, không yêu cầu hạ tầng phức tạp.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-80df-9318-f49056aaaa17" class="numbered-list" start="6"><li>Mức độ an toàn cao, giảm rủi ro xã hội và truyền thông.</li></ol></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8006-a4d9-d86bb2164565" class="">Hầu hết hệ thống khác chỉ tối ưu <strong>một hoặc hai</strong> yếu tố trong số trên.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-805f-9d32-d1b6c8c59580" class="">AMOS-IKONOMY tối ưu <strong>toàn bộ cùng lúc</strong> nhờ logic điều khiển AMOS. AMOS-IKONOMY không phá vỡ định luật Faraday và không vượt giới hạn nhiệt động học. 
Giá trị vượt trội của hệ thống nằm ở việc <strong>chuyển giới hạn vật lý và giới hạn con người thành luật điều khiển bắt buộc</strong>, giúp hệ thống:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80b5-875e-d9c3e74d99b8" class="bulleted-list"><li style="list-style-type:disc">vận hành sát trần vật lý nhưng không vượt ngưỡng an toàn,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8037-acfb-eb1319617163" class="bulleted-list"><li style="list-style-type:disc">duy trì hiệu quả trong thời gian dài,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-804a-8802-dc5e8853b7c0" class="bulleted-list"><li style="list-style-type:disc">và phù hợp với điều kiện triển khai tại Việt Nam.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-802e-a9a4-e58da109df18" class="">Đây chính là lý do AMOS-IKONOMY <strong>vượt trội so với IKONOMY nguyên bản và các hệ thống điện phân module hiện có trên thị trường</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80a3-84e0-d173208592b3"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-80d2-9e64-f6f8ba73b23c" class=""><strong>1. 
Tổng quan kỹ thuật</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-803b-b891-de67239a586c" class="">AMOS–IKONOMY là hệ thống sản xuất hydro bằng điện phân nước, cấu hình <strong>mô-đun công suất nhỏ</strong>, thiết kế cho vận hành liên tục trong điều kiện thực tế.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8013-8899-d44a7a12e424" class="">Hệ thống hướng tới các điều kiện biên sau:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8097-bef6-d25688dbe50a" class="bulleted-list"><li style="list-style-type:disc">nguồn điện DC dao động trong dải 48–96 V,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ad-b033-ddc3faaeabb0" class="bulleted-list"><li style="list-style-type:disc">môi trường vận hành không được kiểm soát chặt,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8009-ba6f-c21a1c5db2df" class="bulleted-list"><li style="list-style-type:disc">nhân lực vận hành hạn chế,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8076-804c-d6619e4a8694" class="bulleted-list"><li style="list-style-type:disc">yêu cầu an toàn và độ tin cậy cao.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80e3-ad4f-f1acfd25cec8" class="">AMOS–IKONOMY <strong>không thay đổi phản ứng điện hóa cơ bản</strong> của quá trình điện phân nước. 
Khác biệt kỹ thuật của hệ thống nằm ở:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ea-8357-dd00974e42ed" class="bulleted-list"><li style="list-style-type:disc">kiến trúc điều khiển dựa trên giới hạn vật lý,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80eb-8086-f71934e55b4b" class="bulleted-list"><li style="list-style-type:disc">cơ chế giám sát suy giảm theo xu hướng thời gian,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ef-ad96-db713e1db4fe" class="bulleted-list"><li style="list-style-type:disc">cơ chế tự bảo vệ chủ động trong toàn bộ vòng đời vận hành.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80e3-b7dd-eb8e89aef418" class="">Hệ thống được thiết kế để đáp ứng đồng thời ba mục tiêu kỹ thuật sau:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-8054-960e-d5b24a4d996d" class="numbered-list" start="1"><li><strong>Sản lượng:</strong> sản lượng hydro tỷ lệ trực tiếp với dòng điện và tiệm cận giới hạn vật lý ứng với công suất điện cấp vào.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-80fb-9c35-e735d629a5bd" class="numbered-list" start="2"><li><strong>Độ bền:</strong> suy giảm điện hóa được theo dõi định lượng và được điều tiết chủ động nhằm kéo dài tuổi thọ hữu dụng của stack.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-80bd-bc64-fdb150b145b0" class="numbered-list" start="3"><li><strong>An toàn:</strong> giảm tối đa phụ thuộc vào phản ứng kịp thời của người vận hành; 
ưu tiên cơ chế giảm tải có kiểm soát thay cho ngắt đột ngột.</li></ol></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2eac5e6f-95bd-802b-a91e-e7b453c2bcd2" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">flowchart TB
  A[Nguon DC 48-96 VDC] --&gt; B[Bao ve nguon: qua ap, thap ap, dao cuc, han dong khoi dong, TVS, LC]
  B --&gt; C[Loc EMI EMC: tach mass tin hieu va cong suat, noi dat khung]
  C --&gt; D[Khoi cong suat Cannon: Buck hoac Buck-Boost dong bo, dieu khien theo dong]
  D --&gt; E[Cam bien dong: Hall hoac Shunt + ADC]
  D --&gt; F[Cam bien ap Stack: tong ap, tuy chon do theo doan]
  D --&gt; G[Driver cong: gioi han toc do canh, dieu chinh dead-time]
  D --&gt; H[Stack dien phan: cell plate bar]
  H --&gt; I[Khoi nhiet: tam phan bo nhiet, khoi tich nhiet, duong lam mat]
  I --&gt; J[Cam bien nhiet do: T1 T2 T3]
  H --&gt; K[Khoi tach khi: tach H2 va O2]
  K --&gt; L[Bubbler Bay nuoc Loc khi: thiet ke chiu luu luong boost]
  L --&gt; M[Van dieu ap va van an toan H2]
  M --&gt; N[Ngo ra khi H2]
  K --&gt; O[Cam bien ap suat: P_trung_binh va gợn_ap]
  H --&gt; P[He thong nuoc: bon cap hoi]
  P --&gt; Q[Cam bien muc nuoc]
  P --&gt; R[Cam bien do dan dien: tuy chon]

  subgraph MCU[Vi dieu khien thoi gian thuc]
    S[Vong dieu khien nhanh 0.1-1 kHz: PI dong + feedforward, gioi han dI dt, ramp]
    T[Thu vien dang song: DC muot, DC xung, burst mem]
  end

  E --&gt; S
  F --&gt; S
  T --&gt; S
  S --&gt; G

  subgraph AMOS[Lop loi AMOS]
    U[Uoc luong trang thai: T_tb, dT dt, deltaT, R_eq, dR dt, chi so tro khang]
    V[Tich luy suy giam: D_index, ngan sach boost]
    W[Quan ly phong bi van hanh: on dinh, boost, suy giam, bao ve]
    X[Khoi quyet dinh: cap boost, tu choi, giam tai]
  end

  J --&gt; U
  O --&gt; U
  Q --&gt; U
  R --&gt; U
  S --&gt; U
  U --&gt; V
  V --&gt; X
  X --&gt; W
  W --&gt; T

  subgraph GIAMSAT[Lop giam sat va kiem toan]
    Y[Ghi log va truy vet: su kien, nguong, ly do]
    Z[Giam sat tu xa tuy chon: cau hinh, bao cao]
    AA[Goi kiem toan: uptime, so lan can thiep, lich su boost, xu huong D_index]
  end

  X --&gt; Y
  U --&gt; Y
  W --&gt; Y
  Y --&gt; AA
  Z --&gt; Y</code></pre></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-80e9-87b2-da5941be98fd" class=""><strong>2. 
Kiến trúc tổng thể hệ thống</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8011-9bd3-efe808e5eea4" class=""><strong>2.1 Chuỗi chức năng</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80ce-a995-e22fe3257737" class="">Hệ thống AMOS–IKONOMY được tổ chức theo chuỗi chức năng cố định:</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-804e-9508-c130634f405e" class="">Nguồn DC 48–96 VDC</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80a5-aa02-d3be935c7f67" class="">→ Khối điều hòa và bảo vệ nguồn</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80b9-8f67-c1ab45a8ef6f" class="">→ Khối điều khiển dòng điện Cannon</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80c8-b0fc-f89dfdfc8e75" class="">→ Stack điện phân</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8025-a9f5-c0ba275ad142" class="">→ Hệ thống quản lý nhiệt</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8093-b138-e448cc70d547" class="">→ Hệ thống tách và điều hòa khí</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8016-afc3-fdf639a01d74" class="">→ Ngõ ra hydro</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8058-b5f0-c637e6bced5a" class="">Chuỗi chức năng này là <strong>bắt buộc</strong> và không được thay đổi trong thiết kế tích hợp.</p></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80ee-b7fc-e06d29e8bc5b" class=""><strong>2.2 Nguyên tắc kiến trúc bắt buộc</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-8083-a2e3-db5c37086eb6" class="numbered-list" start="1"><li><strong>Không điều khiển trực tiếp stack theo nhu cầu sản lượng.</strong><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-801c-b9e8-f380cba3e146" class="">Mọi yêu cầu tăng hoặc giảm sản lượng hydro phải được chuyển đổi thành yêu cầu d
òng điện và xử lý qua lớp điều khiển trung gian.</p></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-807a-a6d8-d5345600e1f9" class="numbered-list" start="2"><li><strong>Mọi thay đổi dòng điện phải tuân thủ đồng thời các giới hạn sau:</strong><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80b4-9197-f84ff1527364" class="bulleted-list"><li style="list-style-type:disc">giới hạn điện: dòng, tốc độ thay đổi dòng, điều kiện nguồn,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8094-9b89-ee20723577a6" class="bulleted-list"><li style="list-style-type:disc">giới hạn nhiệt: nhiệt độ tuyệt đối, tốc độ tăng nhiệt, gradient nhiệt,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8049-b276-fa4b2b00f577" class="bulleted-list"><li style="list-style-type:disc">giới hạn khí: áp suất, dao động áp suất, ổn định lưu lượng,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80fe-b306-fd447afa73ba" class="bulleted-list"><li style="list-style-type:disc">giới hạn suy giảm: xu hướng điện áp và điện trở theo thời gian.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-808c-bf74-c2af2dbe7146" class="numbered-list" start="3"><li><strong>Ưu tiên bảo toàn stack và an toàn hệ thống.</strong><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80b4-84f5-d51fde4cbcf9" class="">Trong mọi tình huống xung đột giữa sản lượng tức thời và rủi ro suy giảm hoặc rủi ro an toàn, hệ thống bắt buộc lựa chọn phương án giảm tải.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8027-910d-f94403fb85ec" class="">
</p></div></li></ol></div><div style="display:contents" dir="auto"><pre id="2eac5e6f-95bd-80ba-b60d-c0ba54fc32f4" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">                     HE THONG AMOS-IKONOMY (Kien truc tong the)

 [1] NGUON DC 48-96V
        |
        v
 [2] BAO VE + DIEU HOA NGUON
     - Qua ap / thap ap (OVP/UVP)
     - Dao cuc
     - Han dong khoi dong (inrush)
     - Chong xung (TVS)
     - Loc dau vao (LC)
        |
        v
 [3] LOC EMI/EMC + NOI DAT
     - Tach mass tin hieu / mass cong suat
     - Noi dat khung may, bo tri day dan dung quy tac
        |
        v
 [4] KHOI CONG SUAT &quot;CANNON&quot; (BO BIEN DOI THEO DONG)
     - Buck / Buck-Boost dong bo
     - Dieu khien vong kin theo dong (current-mode)
     - Gioi han toc do tang dong (dI/dt) + ramp
     - Dieu chinh dead-time + gioi han canh xung (slew-rate)
        |
        |------------------------------\
        |                               \
        v                                v
 [4a] CAM BIEN DONG                    [4b] CAM BIEN AP STACK
     - Hall hoac Shunt + ADC               - Tong ap
     - Do chinh xac muc tieu &lt;= 1%         - Tuy chon do theo doan (segment)
        |                               /
        |                              /
        \-------------\    /----------/
                      v  v
               [5] MCU THOI GIAN THUC (0.1-1 kHz)
                   - PI dieu khien dong + feed-forward
                   - Gioi han dI/dt, ramp, gioi han cong suat
                   - Thu vien dang song:
                       (a) DC muot (on dinh)
                       (b) DC xung (giam bam bot khi)
                       (c) Burst mem (boost co gioi han)
                      |
                      v
             [6] DRIVER CONG (gate driver)
                 - Tao xung dieu khien MOSFET/SiC
                 - Kiem soat dead-time, slew-rate
                      |
                      v
 [7] STACK DIEN PHAN (vung phan ung)
     - Cell / plate / bar (tuy cau hinh)
     - Sinh khi H2 va O2
        |
        |------------------------\
        |                         \
        v                          v
 [8] HE THONG NHIET               [9] HE THONG NUOC
     - Tam phan bo nhiet              - Bon nuoc, cap/hoi
     - Khoi tich nhiet                - Cam bien muc nuoc
     - Duong lam mat                  - Tuy chon cam bien do dan dien
     - Cam bien nhiet do T1 T2 T3     - Logic: nuoc kem =&gt; giam tai
        |                         /
        |                        /
        \-----------\   /--------/
                    v v
               [10] AMOS CORE (lop quyet dinh)
                   A. Uoc luong trang thai
                      - T_avg, dT/dt, deltaT
                      - R_eq, dR_eq/dt (xu huong suy giam)
                      - P, do gon ap, on dinh khi
                   B. Tich luy suy giam
                      - D_index (chi so suy giam)
                      - Ngan sach boost (boost budget)
                   C. Quan ly phong bi van hanh (envelope)
                      - On dinh (cruise)
                      - Boost (gioi han thoi gian + cooldown)
                      - Suy giam (degraded)
                      - Bao ve (protective)
                      - Khoa (lockout)
                   D. Logic quyet dinh
                      - Cap boost neu tat ca nguong dat
                      - Tu choi boost neu bat ky nguong vi pham
                      - Giam tai som, khong doi den cat khan cap
                    |
                    v
             (Lenh dieu khien tra ve MCU)
     &quot;Chon dang song&quot; + &quot;Muc dong muc tieu&quot; + &quot;Gioi han thoi gian&quot;

        |
        v
 [11] HE THONG TACH VA DIEU HOA KHI
     - Tach H2 / O2
     - Bubbler / bay nuoc / loc khi (chiu duoc luu luong boost)
     - Cam bien ap suat (P trung binh, do gon ap)
     - Van dieu ap / van an toan
        |
        v
 [12] NGO RA H2 (co dieu tiet)
     - Khong luu tru H2 khi dung may (theo triet ly an toan)

        |
        v
 [13] LOP GIAM SAT + KIEM TOAN (tuy chon)
     - Ghi log va truy vet: su kien, nguong, ly do
     - Giam sat tu xa: cau hinh, bao cao
     - Goi kiem toan: uptime, so lan can thiep, lich su boost, xu huong D_index</code></pre></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-80b0-9d21-ffb2dbaccfb7" class=""><strong>1) Sơ đồ luồng dữ liệu (Data Flow Diagram)</strong></h2></div><div style="display:contents" dir="auto"><pre id="2eac5e6f-95bd-8044-aaeb-f05a372a0ed2" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">                    SO DO LUONG DU LIEU (AMOS-IKONOMY)

 CAM BIEN (INPUT)                         TANG DIEU KHIEN (CONTROL)                    TANG THUC THI (ACTUATION)
 ----------------                         -------------------------                    -------------------------

  Dong I_meas  ----------------------\
  Ap  V_stack  -----------------------\
  Nhiet T1,T2,T3 -----------------------&gt;  [MCU VONG NHANH 0.1-1 kHz]  -----------------&gt; [DRIVER CONG]
  Ap suat P, ripple -------------------/        - Dieu khien PI theo dong               - Dead-time
  Muc nuoc Level ---------------------/         - Gioi han dI/dt, ramp                  - Slew-rate
  Do dan Cond (tuy chon) ------------/          - Thuc thi waveform da duoc cap         - Gate timing
                                                 |
                                                 | (truyen telemetry / sample tong hop 1-10 Hz)
                                                 v
                                         [AMOS CORE 1-10 Hz]
                                          - Uoc luong trang thai (State Estimator)
                                          - Tinh chi so suy giam D_index
                                          - Tinh ngan sach boost (Boost budget)
                                          - Quan ly phong bi (Envelope Manager)
                                          - Logic ra quyet dinh (Decision Logic)
                                                 |
                                                 | (lenh dieu khien cap cao)
                                                 v
                                    LENH TU AMOS TRA VE MCU
                                    - I_set: dong muc tieu
                                    - waveform_id: loai dang song
                                    - boost_time_limit: gioi han thoi gian boost
                                    - cooldown_time: thoi gian hoi phuc bat buoc
                                    - envelope_mode: cruise / boost / degraded / protective / lockout
                                                 |
                                                 v
                                  [MCU AP DUNG LENH + KIEM TRA RANG BUOC]
                                  - Neu lenh vi pham nguong nhanh =&gt; tu choi / cat giam
                                  - Neu hop le =&gt; phat xung dieu khien khoi Cannon
                                                 |
                                                 v
                                    [KHOI CANNON + STACK DIEN PHAN]
                                    - Dong thuc thi I(t)
                                    - Sinh khi H2/O2
                                    - Phat sinh nhiet va dao dong ap
                                                 |
                                                 v
                                    [HE NHIET + HE KHI + HE NUOC]
                                    - Nhiet duoc truyen va giam gradient
                                    - Khi duoc tach va dieu hoa
                                    - Nuoc duoc cap va giam sat
                                                 |
                                                 v
                                    [LOGGER + TRUY VET + KIEM TOAN]
                                    - Luu: gia tri, su kien, nguong, ly do
                                    - Bao cao: uptime, can thiep, boost usage, D_index trend</code></pre></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80b4-9171-e1a6cd22fbab" class=""><strong>Ghi chú kỹ thuật</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8014-a5ad-d64c9824827b" class="bulleted-list"><li style="list-style-type:disc"><strong>MCU vòng nhanh</strong> chịu trách nhiệm “phản xạ”: giữ dòng đúng, không rung, không sốc.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8090-aecd-e3968317b40b" class="bulleted-list"><li style="list-style-type:disc"><strong>AMOS</strong> chịu trách nhiệm “quyết định”: có boost hay không, boost bao lâu, khi nào phải giảm tải trước khi hỏng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ce-93d0-d743bac72f04" class="bulleted-list"><li style="list-style-type:disc"><strong>Logger/kiểm toán</strong> ghi rõ “ai ra quyết định gì và vì sao”, để phục vụ thẩm định và chứng minh an toàn.</li></ul></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80af-af5b-de872347d2f6"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-809d-bbd7-ef07c50c7bea" class=""><strong>2) Sơ đồ trạng thái vận hành (State Machine)</strong></h2></div><div style="display:contents" dir="auto"><pre id="2eac5e6f-95bd-80ac-b7ca-fddd72e6a2f1" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">                         SO DO TRANG THAI VAN HANH (AMOS-IKONOMY)

 [OFF]
   |
   | Dieu kien: co nguon, tat ca cam bien hop le, muc nuoc dat, khong loi
   v
 [STARTUP - KHOI DONG AN TOAN]
   - Ramp dong tu 0 -&gt; I_cruise theo dI/dt gioi han
   - Kiem tra nhiet, ap, on dinh trong cua so thoi gian
   |
   | Neu on dinh du thoi gian =&gt; vao CRUISE
   | Neu loi / bat thuong =&gt; vao PROTECTIVE hoac LOCKOUT
   v
 [CRUISE - VAN HANH ON DINH DAI HAN]
   - Muc tieu: san luong on dinh, suy giam thap, it can thiep
   - AMOS theo doi: T_avg, deltaT, dT/dt, R_eq, dR/dt, P_ripple, Level, Cond
   |
   | Neu co yeu cau tai cao (demand) VA tat ca nguong Boost OK
   v
 [BOOST - TANG CONG SUAT NGAN HAN]
   - I_set tang den I_boost theo ramp
   - Gioi han thoi gian: 30-180 s (do AMOS cap)
   - Theo doi sat: nhiet, gradient, ap, trinh trang dien hoa
   |
   | Ket thuc boost (het gio) HOAC bat ky nguong vi pham
   v
 [COOLDOWN - HOI PHUC BAT BUOC]
   - Dua dong ve I_cruise hoac thap hon
   - Giu trong thoi gian 5-10 phut
   - Muc tieu: dua T_avg, deltaT, P_ripple ve vung an toan
   |
   | Neu on dinh =&gt; quay lai CRUISE
   | Neu xau di =&gt; vao DEGRADED hoac PROTECTIVE
   v

 [DEGRADED - SUY GIAM CO KIEM SOAT]
   - Giam san luong de bao toan stack va tranh su co
   - Gioi han: I_max_deg &lt; I_cruise
   - Chi cho phep hoat dong khi cac nguong toi thieu dat
   |
   | Neu phuc hoi du =&gt; quay lai CRUISE
   | Neu vi pham nguong an toan =&gt; PROTECTIVE
   v

 [PROTECTIVE - BAO VE]
   - Giam dong nhanh nhung co kiem soat (khong cat giat)
   - Co the dua ve muc an toan thap hoac dung co trinh tu
   |
   | Neu su co lap lai qua so lan trong cua so thoi gian
   v

 [LOCKOUT - KHOA AN TOAN]
   - Tu choi boost
   - Tu choi khoi dong lai ngay lap tuc
   - Bat buoc cooldown / kiem tra / thao tac reset theo quy trinh
   |
   | Sau khi dat dieu kien reset (thoi gian, nhiet, muc nuoc, loi cleared)
   v
 [STARTUP - KHOI DONG AN TOAN]</code></pre></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8061-aa47-c1301d8bfcc3" class=""><strong>Bảng điều kiện chuyển trạng thái (rõ ràng, dễ audit)</strong></h3></div><div style="display:contents" dir="auto"><pre id="2eac5e6f-95bd-8067-a83f-f01c18cd4634" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">CRUISE -&gt; BOOST
  Dieu kien bat buoc (tat ca):
  - T_avg trong 55-75 C
  - deltaT &lt;= 5 C
  - dT/dt &lt;= 1 C/phut
  - P trong 1.5-3 bar va P_ripple &lt;= 3%
  - dR_eq/dt nho hon nguong (khong co xu huong suy giam nhanh)
  - Level OK, Cond trong nguong (neu co)
  - so lan boost trong cua so thoi gian chua vuot han

BOOST -&gt; COOLDOWN
  - Het boost_time_limit HOAC
  - Bat ky nguong nao vi pham HOAC
  - D_index tang nhanh (vuot nguong)

BAT KY TRANG THAI -&gt; PROTECTIVE
  - Vuot nguong an toan: nhiet qua cao, ap qua cao, dao dong ap lon
  - Cam bien khong dong thuan (sensor disagreement)
  - Loi phan cung cong suat (driver fault)

PROTECTIVE -&gt; LOCKOUT
  - Loi lap lai qua N lan trong M phut
  - De phong thao tac sai hoac co loi dai</code></pre></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-80ef-ba49-de2e2edc3c86" class=""><strong>3. Nguyên lý thiết kế cốt lõi</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-805c-8576-f825d1ab38cb" class=""><strong>3.1. Nguyên lý điều khiển theo dòng điện</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8007-ad34-de7615b43750" class="">Trong hệ thống điện phân nước, các đại lượng quyết định gồm: tốc độ sinh hydro, mức phân cực điện cực, tốc độ hình thành bọt khí và tốc độ suy giảm vật liệu. 
Các đại lượng này <strong>phụ thuộc trực tiếp vào dòng điện và mật độ dòng điện</strong> đi qua stack.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-800c-bb1d-cd6f45d45d83" class="">Điện áp đặt lên stack là kết quả của:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ae-a58f-c2f8aded0e0e" class="bulleted-list"><li style="list-style-type:disc">điện áp thuận nghịch,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-809c-b601-cb90a23a3bdc" class="bulleted-list"><li style="list-style-type:disc">tổn hao hoạt hóa,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80b0-810c-efffa838f67e" class="bulleted-list"><li style="list-style-type:disc">tổn hao ohmic,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8006-a884-c7e09afede88" class="bulleted-list"><li style="list-style-type:disc">tổn hao truyền khối.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8075-a1dc-f76054a6f7f1" class="">Điện áp <strong>không phải</strong> là biến điều khiển an toàn cho sản lượng hydro.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8031-a330-c89aa948c1a4" class="">Các nguyên tắc thiết kế bắt buộc:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8001-9e9b-e87b541709a8" class="bulleted-list"><li style="list-style-type:disc">Không điều khiển công suất bằng cách tăng điện áp.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8079-836a-ca91fc2e9b65" class="bulleted-list"><li style="list-style-type:disc">Không cưỡng bức dòng điện vượt ngưỡng thiết kế thông qua “đẩy áp”.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8052-bb0e-c056c40e0b35" class="bulleted-list"><li style="list-style-type:disc">Chỉ cho phép điều khiển dòng điện theo thời gian, 
với tốc độ thay đổi và giá trị tuyệt đối bị giới hạn bởi các điều kiện vật lý của hệ thống.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-801f-8e97-fedda9c9f179" class="">Kết luận nguyên lý điều khiển:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-809c-9a28-f34e297e0dc5" class="bulleted-list"><li style="list-style-type:disc"><strong>Dòng điện là biến điều khiển duy nhất đối với quá trình điện phân.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8082-b6f7-db3d796a81ee" class="bulleted-list"><li style="list-style-type:disc"><strong>Điện áp chỉ được sử dụng làm biến giám sát và chẩn đoán trạng thái stack.</strong></li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8065-93ba-fbf97d52a571" class=""><strong>3.2. Nguyên lý điều khiển liên hợp đa miền vật lý</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8023-9a10-f9834ded50c2" class="">AMOS–IKONOMY không tách rời các miền điện, nhiệt và khí trong điều khiển. 
Ba miền này được xem là <strong>một hệ liên hợp bắt buộc</strong>.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80ff-aa5f-f080de26519e" class="">Quan hệ nhân quả trong vận hành:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-801d-8842-c6837294e505" class="bulleted-list"><li style="list-style-type:disc">Tăng dòng điện → tăng tổn hao điện → tăng nhiệt độ stack.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-805a-baab-efe2dc4d508d" class="bulleted-list"><li style="list-style-type:disc">Tăng nhiệt độ → thay đổi điện trở nội → tăng tốc độ suy giảm vật liệu.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8071-abc8-e426e411f6ee" class="bulleted-list"><li style="list-style-type:disc">Tăng tốc độ sinh khí → tăng dao động áp suất → tăng rủi ro an toàn.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8030-9827-ecc84018b41c" class="">Do đó, <strong>mọi quyết định tăng dòng điện chỉ được phép thực hiện khi đồng thời thỏa mãn tất cả các điều kiện sau</strong>:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80bb-8271-ee61f3c52b45" class="bulleted-list"><li style="list-style-type:disc">Điều kiện nhiệt: nhiệt độ tuyệt đối, 
tốc độ tăng nhiệt và gradient nhiệt trong giới hạn cho phép.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-803d-8780-e80229a826f2" class="bulleted-list"><li style="list-style-type:disc">Điều kiện khí: áp suất và dao động áp suất ổn định trong dải thiết kế.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8069-83f0-e01b8402c332" class="bulleted-list"><li style="list-style-type:disc">Điều kiện suy giảm: xu hướng điện áp và điện trở nội không tăng nhanh theo thời gian.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8016-b40e-fba7f40cbbef" class="bulleted-list"><li style="list-style-type:disc">Điều kiện lịch sử tải: mức độ stress tích lũy chưa vượt ngưỡng vận hành an toàn.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8072-b9ec-f327ef294c17" class="">Luật điều khiển bắt buộc:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80bb-b499-e54abe5f17fe" class="bulleted-list"><li style="list-style-type:disc">Nếu <strong>bất kỳ một điều kiện nào không thỏa mãn</strong>, hệ thống <strong>bắt buộc giảm dòng điện</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8034-aa4a-d7b52ae8ae63" class="bulleted-list"><li style="list-style-type:disc">Không tồn tại ngoại lệ vì lý do sản lượng hoặc yêu cầu tức thời.</li></ul></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8096-b417-fe1ebe469a27" class=""><strong>3. Nguyên lý thiết kế cốt lõi</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8052-9c3e-c8629be3050d" class=""><strong>3.1 Điều khiển theo dòng điện</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8099-8dcc-e9485aab31d0" class="">Trong điện phân nước, tốc độ sinh hydro và mức suy giảm vật liệu phụ thuộc trực tiếp vào dòng điện/mật độ dòng. 
Điện áp chủ yếu phản ánh trạng thái phân cực và điện trở nội, 
không phải biến điều khiển an toàn.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-804e-8c0a-cd847880da13" class="">Nguyên tắc bắt buộc:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80d8-84fd-c88042d20d98" class="bulleted-list"><li style="list-style-type:disc">Không điều khiển công suất bằng cách “đẩy áp”.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-803e-9df1-da9fe2623e09" class="bulleted-list"><li style="list-style-type:disc">Không cưỡng bức dòng vượt ngưỡng bằng điện áp.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-807a-9907-fde1bcb9e63d" class="bulleted-list"><li style="list-style-type:disc">Chỉ điều khiển dòng theo thời gian trong giới hạn vật lý xác định.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8079-a3fd-c28a6c47eef8" class="">Kết luận nguyên lý:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80fc-87e2-cda09ec95595" class="bulleted-list"><li style="list-style-type:disc"><strong>Dòng điện là biến điều khiển chính.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80dd-897d-e4e672821171" class="bulleted-list"><li style="list-style-type:disc"><strong>Điện áp là biến quan sát/chẩn đoán.</strong></li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8057-9957-fb5877d0b353" class=""><strong>3.2 Điều khiển liên hợp đa miền vật lý</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-809e-a0a7-fcfc5453a3cc" class="">AMOS–IKONOMY coi điện–nhiệt–khí là một hệ liên hợp:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8090-80e1-e8d2f273eef4" class="bulleted-list"><li style="list-style-type:disc">Tăng dòng → tăng tổn hao → tăng nhiệt.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-801b-9ddb-c9fc4a98f694" class="bulleted-list"><li s
tyle="list-style-type:disc">Tăng nhiệt → thay đổi điện trở → tăng suy giảm.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ab-a605-cfd260cd5a1a" class="bulleted-list"><li style="list-style-type:disc">Tăng sinh khí → tăng dao động áp → tăng rủi ro an toàn.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80f7-a84a-d6c020b8fdec" class="">Mọi quyết định tăng dòng chỉ được phép khi đồng thời thỏa:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ba-bb4b-fcde3188cfec" class="bulleted-list"><li style="list-style-type:disc">điều kiện nhiệt (nhiệt độ và gradient),</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8007-9c2d-c901539a648d" class="bulleted-list"><li style="list-style-type:disc">điều kiện khí (áp suất và dao động),</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-804f-9b80-d4183eed1195" class="bulleted-list"><li style="list-style-type:disc">điều kiện suy giảm (xu hướng điện trở/phân cực),</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8008-90af-cd384f5b5f76" class="bulleted-list"><li style="list-style-type:disc">điều kiện lịch sử tải (stress tích lũy).</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80f4-8c49-d83993bfdcc7" class="">Chỉ cần 1 điều kiện không đạt → giảm tải.</p></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8010-9742-fe94193d3ca0" class=""><strong>4. Khối điều khiển công suất Cannon</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-803e-808b-cbf991d37827" class="">Khối Cannon là <strong>bộ biến đổi công suất điều khiển theo dòng điện</strong>, được thiết kế để <strong>cấp dòng chính xác cho stack trong các giới hạn cho phép</strong>. 
Khối này <strong>không được thiết kế để tối đa hóa công suất</strong> và <strong>không có quyền vượt giới hạn vận hành</strong>.</p></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80a8-943c-d9fceada60fd" class=""><strong>4.1. Chức năng bắt buộc</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80b2-a641-ce495d456d43" class="bulleted-list"><li style="list-style-type:disc">Tạo và duy trì dòng điện theo giá trị đặt.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8071-bfc8-dd85a3f01a44" class="bulleted-list"><li style="list-style-type:disc">Ổn định dòng điện khi điện áp nguồn dao động trong dải cho phép.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80b5-a7ef-c58a1373b270" class="bulleted-list"><li style="list-style-type:disc">Giới hạn động học dòng điện nhằm bảo vệ stack.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80d8-bdd0-dc3230adbd7e" class=""><strong>4.2. 
Ràng buộc thiết kế</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80f9-a5be-f48fad131815" class="bulleted-list"><li style="list-style-type:disc">Bắt buộc sử dụng điều khiển dòng vòng kín.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80bb-bfe4-e252ef9ff307" class="bulleted-list"><li style="list-style-type:disc">Bắt buộc giới hạn tốc độ thay đổi dòng (dI/dt) để tránh:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8022-a5ed-f2d1aeda4876" class="bulleted-list"><li style="list-style-type:circle">sốc điện hóa,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-802a-b9f2-f9406f60bf7c" class="bulleted-list"><li style="list-style-type:circle">sốc nhiệt,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8005-b378-e2b455a9f979" class="bulleted-list"><li style="list-style-type:circle">tăng suy giảm không hồi phục.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8086-8858-caffb0920e5f" class="bulleted-list"><li style="list-style-type:disc">Dòng điện đầu ra <strong>không được vượt</strong> các ngưỡng do hệ thống AMOS xác định.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8034-bfa0-ff7b64691f4f" class="bulleted-list"><li style="list-style-type:disc">Không cho phép bỏ qua, nới lỏng hoặc ghi đè giới hạn, <strong>kể cả khi nguồn điện đầu vào còn dư công suất</strong>.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-804e-a98e-cbb2f751101d" class="">Khối Cannon chỉ đóng vai trò <strong>thực thi mệnh lệnh dòng điện trong phong bì cho phép</strong>, không tham gia ra quyết định tăng tải.</p></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8028-b41b-ee68c3b9af00" class=""><strong>5. 
Stack điện phân và các vùng vận hành</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8082-8c58-f7e16e6ba714" class="">Stack điện phân được vận hành theo các vùng dòng điện đã được xác định trước, dựa trên đặc tính nhiệt, đặc tính suy giảm và yêu cầu an toàn.</p></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8082-8013-e6e3fe8b5858" class=""><strong>5.1. 
Vùng vận hành ổn định dài hạn</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-801a-8b3a-e5dbac779a3b" class="">Vùng vận hành ổn định được định nghĩa bởi các điều kiện sau:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-806a-a95e-dc1a7ce88fe1" class="bulleted-list"><li style="list-style-type:disc">Mật độ dòng điện thấp hơn ngưỡng gây suy giảm nhanh.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8092-bc8e-d37d73fe45c4" class="bulleted-list"><li style="list-style-type:disc">Nhiệt độ vận hành và gradient nhiệt nằm trong giới hạn thiết kế.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8038-a70d-fac9b3bf95c6" class="bulleted-list"><li style="list-style-type:disc">Xu hướng điện áp và điện trở nội ổn định theo thời gian.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80f4-a2c5-f1de5af2cb3a" class="">Đặc tính vận hành:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8081-97b1-d59ec4a3934f" class="bulleted-list"><li style="list-style-type:disc">Cho phép vận hành liên tục dài hạn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8064-8a97-d0c8d77f0cea" class="bulleted-list"><li style="list-style-type:disc">Ít yêu cầu can thiệp của người vận hành.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-803f-af58-db65200034cc" class="bulleted-list"><li style="list-style-type:disc">Là vùng vận hành mặc định của hệ thống.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80e7-8b99-db7d3f1f01ca" class=""><strong>5.2. 
Vùng tăng công suất ngắn hạn (Boost)</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8052-8341-f71b3d31919f" class="">Vùng tăng công suất chỉ được phép kích hoạt khi <strong>đồng thời thỏa mãn tất cả các điều kiện sau</strong>:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80dd-b98a-e7d6cb504e2a" class="bulleted-list"><li style="list-style-type:disc">Hệ thống còn dư địa nhiệt (nhiệt độ tuyệt đối và tốc độ tăng nhiệt dưới ngưỡng).</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8040-93c3-c70d2f371473" class="bulleted-list"><li style="list-style-type:disc">Không xuất hiện xu hướng tăng nhanh của điện áp hoặc điện trở nội.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8088-be62-d6313d4cd11b" class="bulleted-list"><li style="list-style-type:disc">Áp suất và dao động áp suất khí nằm trong dải cho phép.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80cb-8416-ed4806540e4a" class="bulleted-list"><li style="list-style-type:disc">Tần suất và mật độ boost chưa vượt ngưỡng vận hành an toàn.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80b6-9c8f-c11f3b764121" class="">Quy tắc bắt buộc:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8005-badc-fcf7ae69c901" class="bulleted-list"><li style="list-style-type:disc">Boost chỉ được phép trong thời gian giới hạn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8013-b79c-f12231542316" class="bulleted-list"><li style="list-style-type:disc">Không cho phép các chu kỳ boost liên tiếp với mật độ cao.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80d8-a93e-d18f74419bbf" class="bulleted-list"><li style="list-style-type:disc">Khi bất kỳ điều kiện nào không còn thỏa mãn, 
hệ thống <strong>bắt buộc tự động quay về vùng vận hành ổn định</strong>.</li></ul></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-807b-a82f-d7a68ab868d0" class=""><strong>6. Lớp điều khiển AMOS</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80b6-b9b0-e523ec605918" class="">AMOS là <strong>lớp logic điều khiển quyết định</strong> của toàn bộ hệ thống AMOS–IKONOMY. AMOS được xây dựng trên <strong>các luật vật lý, luật suy giảm vật liệu và kinh nghiệm vận hành</strong>, <strong>không phải</strong> hệ thống học máy thích nghi tự do. AMOS không “tối ưu theo mục tiêu tức thời”, mà <strong>đánh giá trạng thái vận hành tổng thể theo thời gian</strong>.</p></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80e1-b1d8-d0e79b225a14" class=""><strong>6.1. 
Các đại lượng giám sát bắt buộc</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8098-b8c9-c69a7cc25c7c" class="">AMOS liên tục giám sát và cập nhật các đại lượng sau:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80d6-a58d-e5bb67dd6e5d" class="bulleted-list"><li style="list-style-type:disc">Nhiệt độ stack và <strong>tốc độ tăng nhiệt theo thời gian (dT/dt)</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8027-9ab6-e164203ca2d1" class="bulleted-list"><li style="list-style-type:disc">Gradient nhiệt trong stack.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-802a-ac9e-c79bffdace1f" class="bulleted-list"><li style="list-style-type:disc">Điện áp stack và <strong>xu hướng biến thiên theo thời gian</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8030-8839-dc60e035313d" class="bulleted-list"><li style="list-style-type:disc">Điện trở tương đương của stack và <strong>tốc độ tăng điện trở (dR/dt)</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80f6-afa1-eb3bfabf7a59" class="bulleted-list"><li style="list-style-type:disc">Áp suất khí hydro và mức dao động áp suất.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80af-91d2-eac31e0d9e67" class="bulleted-list"><li style="list-style-type:disc">Lịch sử vận hành: số lần boost, thời gian boost, và <strong>stress tích lũy</strong>.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80ab-8d28-d957b7ef7148" class="">AMOS <strong>không ra quyết định dựa trên giá trị tức thời</strong>, mà dựa trên <strong>xu hướng và tốc độ biến đổi</strong> của các đại lượng trên.</p></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-807e-9607-f26ba7e875f0" class=""><strong>6.2. 
Nguyên tắc ra quyết định</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-805d-837a-ca6cf6a91c0b" class="">Nguyên tắc điều khiển cốt lõi của AMOS được xác định như sau:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ff-8928-e46b1c37cbaa" class="bulleted-list"><li style="list-style-type:disc">Nếu một hành động làm tăng sản lượng hydro trong ngắn hạn <strong>nhưng làm tăng xác suất suy giảm hoặc hư hỏng trong tương lai</strong>, hành động đó <strong>không được cho phép</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8088-9eb4-d144220dcb57" class="bulleted-list"><li style="list-style-type:disc">Khi xuất hiện xung đột giữa sản lượng tức thời và độ bền/an toàn, AMOS <strong>bắt buộc ưu tiên bảo toàn hệ thống</strong>.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80a1-b428-dac6ad887efb" class="">Chiến lược bảo vệ chính:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8026-b70f-e537fc66f278" class="bulleted-list"><li style="list-style-type:disc"><strong>Giảm tải sớm, có kiểm soát</strong> (derating chủ động).</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8019-9b6c-cc8f90c772e6" class="bulleted-list"><li style="list-style-type:disc">Tránh tối đa cơ chế <strong>cắt khẩn cấp (shutdown)</strong> trừ trường hợp vượt ngưỡng an toàn tuyệt đối.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-801b-857b-f7d4fb66a398" class="">AMOS được thiết kế để <strong>ngăn sự cố trước khi xảy ra</strong>, không chỉ phản ứng khi sự cố đã hình thành.</p></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-807c-9ac5-f3402f0fbe4c" class=""><strong>7. So sánh với thiết kế IKONOMY ban đầu</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80e3-b008-d843c92b9c2d" class=""><strong>7.1. 
Hạn chế của thiết kế IKONOMY ban đầu</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-804a-8f4d-cc7ba590a819" class="">Thiết kế IKONOMY ban đầu tập trung mạnh vào:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8010-8eab-f3249c0951a1" class="bulleted-list"><li style="list-style-type:disc">phần cứng công suất,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-803b-ab28-ee331e92963a" class="bulleted-list"><li style="list-style-type:disc">khả năng tạo dạng dòng điện đặc biệt.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8054-bd60-eb5c497c2733" class="">Tuy nhiên, trong vận hành thực tế, hệ thống bộc lộ các hạn chế sau:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-809a-b002-db213977b6af" class="bulleted-list"><li style="list-style-type:disc">Phụ thuộc lớn vào kinh nghiệm và phản ứng của người vận hành.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80b0-aaaf-edfa21d09483" class="bulleted-list"><li style="list-style-type:disc">Nhiều tình huống yêu cầu can thiệp thủ công khi xuất hiện dấu hiệu bất thường.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80f8-99d4-fc06d794cbff" class="bulleted-list"><li style="list-style-type:disc">Cơ chế bảo vệ chủ yếu dựa trên <strong>ngưỡng cắt cứng</strong>, dẫn đến dừng hệ thống đột ngột và stress nhiệt – điện cao.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8093-bd78-dcaec65a7930" class=""><strong>7.2. 
Thay đổi cấp kiến trúc của AMOS–IKONOMY</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-808d-8a40-c38a695c13ff" class="">AMOS–IKONOMY thay đổi cách tiếp cận ở <strong>cấp kiến trúc hệ thống</strong>, không phải tinh chỉnh cục bộ:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8041-9487-f7d609b897b4" class="bulleted-list"><li style="list-style-type:disc">Các giới hạn vật lý (dòng, nhiệt, suy giảm, khí) được <strong>đưa trực tiếp vào lõi logic quyết định</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-808f-b321-f80f274ea009" class="bulleted-list"><li style="list-style-type:disc">Quyền “ép chạy” của con người bị loại bỏ khỏi chuỗi điều khiển.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80fe-a2b3-f82391d4caed" class="bulleted-list"><li style="list-style-type:disc">Cơ chế bảo vệ chuyển từ:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80db-a603-eb77901f4840" class="bulleted-list"><li style="list-style-type:circle"><strong>shutdown phản ứng </strong>sang</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-803c-95f2-e21c1a17f406" class="bulleted-list"><li style="list-style-type:circle"><strong>derating chủ động và êm</strong>.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8092-b6ba-f0f0bc6685d3" class=""><strong>7.3. 
Kết quả vận hành kỳ vọng</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-803d-9653-f2a727787bc3" class="">Với kiến trúc AMOS–IKONOMY, các chỉ tiêu vận hành được cải thiện theo hướng:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80a2-a2d6-f62d255dc991" class="bulleted-list"><li style="list-style-type:disc"><strong>Uptime cao hơn</strong> do giảm số lần dừng đột ngột.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8016-9c5f-c00759a372c9" class="bulleted-list"><li style="list-style-type:disc"><strong>Tuổi thọ stack dài hơn</strong> nhờ giảm sốc điện hóa và sốc nhiệt.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80a3-9a39-d56d7d755121" class="bulleted-list"><li style="list-style-type:disc"><strong>Mức độ an toàn cao hơn</strong> khi triển khai trong điều kiện hạ tầng và nhân lực hạn chế tại Việt Nam.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-801d-a263-ce1a728f60ff" class="">AMOS–IKONOMY không làm phần cứng mạnh hơn về lý thuyết, nhưng <strong>làm cho phần cứng được sử dụng đúng giới hạn trong suốt vòng đời</strong>, đây là yếu tố tạo khác biệt quyết định so với thiết kế IKONOMY ban đầu.</p></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-804c-9bba-f96c90326e91" class=""><strong>8. 
Thông số kỹ thuật mục tiêu cho 01 mô-đun AMOS–IKONOMY</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80dd-a3ad-e3d9eca22b0a" class="">Các thông số dưới đây là <strong>giá trị thiết kế mục tiêu</strong>, dùng làm cơ sở cho:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-805a-836b-ec3b4e1902e5" class="bulleted-list"><li style="list-style-type:disc">thiết kế phần cứng,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8014-a0bc-f7f2d9d37d3a" class="bulleted-list"><li style="list-style-type:disc">xây dựng thuật toán điều khiển AMOS,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80d6-8349-fb28387b0d38" class="bulleted-list"><li style="list-style-type:disc">thẩm định kỹ thuật và đánh giá vận hành.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-802e-b009-f5b8b6b4940b" class=""><strong>8.1. 
Thông số điện – công suất</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-80b4-af96-d0bd4aaa7e20" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8077-b0bd-e4b394d0194c"><th id="]Djk" class="simple-table-header-color simple-table-header"><strong>Thông số</strong></th><th id="ZU`v" class="simple-table-header-color simple-table-header"><strong>Giá trị thiết kế</strong></th><th id="u~Y&lt;" class="simple-table-header-color simple-table-header"><strong>Ghi chú kỹ thuật</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80ca-aa0d-ce156e6541d3"><td id="]Djk" class="">Điện áp nguồn vào</td><td id="ZU`v" class="">48–96 VDC</td><td id="u~Y&lt;" class="">Dải cho phép, đã tính đến dao động nguồn</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80c4-8ec3-da62abfdeb1c"><td id="]Djk" class="">Công suất danh định</td><td id="ZU`v" class="">1,0 kW</td><td id="u~Y&lt;" class="">Vận hành liên tục dài hạn</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8035-8a43-ff460ec1cc2b"><td id="]Djk" class="">Công suất boost</td><td id="ZU`v" class="">1,5–2,0 kW</td><td id="u~Y&lt;" class="">Chỉ cho phép ngắn hạn, 
có điều kiện AMOS</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-804a-96fe-d2e2a25f8e13"><td id="]Djk" class="">Dòng làm việc danh định</td><td id="ZU`v" class="">20–25 A</td><td id="u~Y&lt;" class="">Xác định theo cấu hình stack</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80fd-a843-fb4dfcaecd5c"><td id="]Djk" class="">Hiệu suất chuyển đổi điện</td><td id="ZU`v" class="">≥ 95%</td><td id="u~Y&lt;" class="">Áp dụng cho khối Cannon Drive</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-804b-847d-dec69bc3443e" class=""><strong>Ràng buộc vận hành:</strong></p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80f2-88c3-dcd92e3c629e" class="bulleted-list"><li style="list-style-type:disc">Công suất boost <strong>không được xem là chế độ vận hành thường xuyên</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8061-8e36-e49f9746bb4f" class="bulleted-list"><li style="list-style-type:disc">Mọi trạng thái vượt công suất danh định đều chịu kiểm soát thời gian và điều kiện vật lý.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8012-866c-eb21c9b9a80a" class=""><strong>8.2. 
Thông số điện phân – hydro</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-8023-a140-dc445d3b77f9" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8062-ae46-f70c5aceb896"><th id="\pwf" class="simple-table-header-color simple-table-header"><strong>Thông số</strong></th><th id="DfrU" class="simple-table-header-color simple-table-header"><strong>Giá trị thiết kế</strong></th><th id="h;qr" class="simple-table-header-color simple-table-header"><strong>Ghi chú kỹ thuật</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80cc-8640-e5a593ab767f"><td id="\pwf" class="">Sản lượng hydro danh định</td><td id="DfrU" class="">~300 L/giờ</td><td id="h;qr" class="">Tại dòng danh định, điều kiện ổn định</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80c4-882f-f0af91b89110"><td id="\pwf" class="">Hiệu suất Faraday</td><td id="DfrU" class="">90–98%</td><td id="h;qr" class="">Phụ thuộc cấu hình stack</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8074-858c-d52f1c00d951"><td id="\pwf" class="">Áp suất vận hành</td><td id="DfrU" class="">1,5–3 bar</td><td id="h;qr" class="">Áp suất thấp, ưu tiên an toàn</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80cb-9a58-d8ae0dbd580e"><td id="\pwf" class="">Lưu trữ H₂ khi dừng</td><td id="DfrU" class="">Không</td><td id="h;qr" class="">Thiết kế dừng an toàn, 
không tích khí</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8066-a0d3-eaf219b1da6b" class=""><strong>Nguyên tắc thiết kế:</strong></p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80c4-9705-ded786a7bceb" class="bulleted-list"><li style="list-style-type:disc">Sản lượng hydro được xác định trực tiếp bởi dòng điện.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80dd-8cf5-d0ba83928aab" class="bulleted-list"><li style="list-style-type:disc">Không sử dụng tích trữ hydro trong mô-đun để giảm rủi ro an toàn và áp lực cơ khí.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-806a-9f8f-fd0142c5d3ab" class=""><strong>8.3. 
Thông số nhiệt – độ bền</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-808b-9ec3-ecc04cbf55da" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8038-8d45-f883054d7943"><th id="ip|n" class="simple-table-header-color simple-table-header"><strong>Thông số</strong></th><th id="U&gt;de" class="simple-table-header-color simple-table-header"><strong>Giá trị thiết kế</strong></th><th id="tDdA" class="simple-table-header-color simple-table-header"><strong>Ý nghĩa vận hành</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80ee-ad63-fd0c58948521"><td id="ip|n" class="">Nhiệt độ vận hành</td><td id="U&gt;de" class="">55–75 °C</td><td id="tDdA" class="">Vùng tối ưu cho hiệu suất và độ bền</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80b8-bb99-ce479d5447bf"><td id="ip|n" class="">Gradient nhiệt tối đa</td><td id="U&gt;de" class="">≤ 5 °C</td><td id="tDdA" class="">Giới hạn bắt buộc để tránh ứng suất nhiệt</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80f4-86f1-c02a36e8ed18"><td id="ip|n" class="">Tốc độ tăng nhiệt tối đa</td><td id="U&gt;de" class="">≤ 1 °C/phút</td><td id="tDdA" class="">Tránh sốc nhiệt và suy giảm nhanh</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8096-8c7d-c474a04ae20c"><td id="ip|n" class="">Tuổi thọ mục tiêu</td><td id="U&gt;de" class="">1,5–2× thiết kế gốc</td><td id="tDdA" class="">So với cùng cấu hình stack</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8014-9ab3-ea52df201f32"><td id="ip|n" class="">Uptime mục tiêu</td><td id="U&gt;de" class="">≥ 98%</td><td id="tDdA" class="">Trong điều kiện vận hành thực tế</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-802f-947b-c4611c19046f" class=""><strong>Ràng buộc bắt b
uộc:</strong></p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8045-ab76-e653ad5e622f" class="bulleted-list"><li style="list-style-type:disc">Khi vi phạm bất kỳ giới hạn nhiệt nào, hệ thống <strong>bắt buộc giảm tải</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80bb-902f-f2a0cc495487" class="bulleted-list"><li style="list-style-type:disc">Không cho phép duy trì công suất cao bằng cách chấp nhận vượt giới hạn nhiệt.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80aa-8cb7-fabc357bb8c0" class=""><strong>8.4. Nhận xét kỹ thuật tổng hợp</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80a7-a6a1-e519d69dd072" class="bulleted-list"><li style="list-style-type:disc">Các thông số trên <strong>không tối ưu cho công suất đỉnh</strong>, mà tối ưu cho <strong>vận hành ổn định dài hạn</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ca-8b68-de6f76aab065" class="bulleted-list"><li style="list-style-type:disc">Hiệu quả của AMOS–IKONOMY được đánh giá theo <strong>hiệu suất vòng đời (lifetime performance)</strong>, không theo giá trị tức thời.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8011-b256-c81d4691f792" class="bulleted-list"><li style="list-style-type:disc">Toàn bộ thuật toán AMOS được thiết kế để <strong>bảo vệ các thông số này</strong>, không cho phép vận hành ngoài phong bì đã định.</li></ul></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-806c-8020-e28e4fe0d377" class=""><strong>9. 
Định nghĩa mặt bằng công nghệ hiện hành</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8093-a4e2-c366e31ff277" class=""><em>(Điện phân công suất nhỏ–trung bình)</em></p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8059-b586-e6342db6a2b3" class="">Trong bối cảnh hiện nay, <strong>state-of-the-art (SOTA)</strong> đối với hệ thống điện phân hydro công suất nhỏ–trung bình chủ yếu bao gồm các nhóm công nghệ sau:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8015-91dd-e60f343c9203" class="bulleted-list"><li style="list-style-type:disc"><strong>PEM electrolyzer thương mại</strong> do các hãng EU, Mỹ và Nhật Bản phát triển.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8093-93f7-d6a7176bda47" class="bulleted-list"><li style="list-style-type:disc"><strong>Alkaline electrolyzer thế hệ cải tiến</strong>, tối ưu hiệu suất và độ ổn định so với thiết kế truyền thống.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80e9-8042-d1571de3e7d1" class="bulleted-list"><li style="list-style-type:disc"><strong>AEM electrolyzer thế hệ mới</strong>, đang trong giai đoạn thương mại hóa sớm, độ ổn định dài hạn chưa được chứng minh đầy đủ.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-808b-adab-d0417a21966b" class=""><strong>9.1. 
Đặc trưng kỹ thuật chung của SOTA</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-807c-bf8e-d967138697cc" class="">Các hệ thống SOTA hiện nay có các đặc điểm kỹ thuật chủ đạo sau:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-803e-a7e8-e16161c5d2ed" class="bulleted-list"><li style="list-style-type:disc">Tối ưu hiệu suất điện năng tại <strong>điều kiện vận hành chuẩn</strong>, 
với nguồn điện ổn định và môi trường được kiểm soát.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80fe-bf20-c2f4d64e3760" class="bulleted-list"><li style="list-style-type:disc">Thiết kế giả định:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80a9-8adf-db27a8e67c14" class="bulleted-list"><li style="list-style-type:circle">nguồn điện ít dao động,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-803d-a0a2-fe0193c5b0ff" class="bulleted-list"><li style="list-style-type:circle">có kỹ sư vận hành hoặc hệ thống giám sát chuyên sâu,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80a9-8279-ff7ed7628c0b" class="bulleted-list"><li style="list-style-type:circle">quy trình bảo trì được thực hiện đúng chuẩn nhà sản xuất.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8075-afed-fd9cb064fe27" class="bulleted-list"><li style="list-style-type:disc">Cơ chế bảo vệ chủ yếu dựa trên:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80a8-9042-fec9054721a3" class="bulleted-list"><li style="list-style-type:circle">ngưỡng điện áp,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ce-a4d0-ff371d57b6ae" class="bulleted-list"><li style="list-style-type:circle">ngưỡng nhiệt,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8074-a3ac-d3d63b67cd4d" class="bulleted-list"><li style="list-style-type:circle">và shutdown hoặc derating khi vượt ngưỡng.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-803d-be5e-e90e8e1d3b2c" class="">Hạn chế chung của SOTA là <strong>hiệu quả vận hành giảm đáng kể khi triển khai trong điều kiện thực tế biến động</strong>, nơi các giả định về nguồn điện và nhân lực không còn đúng.</p></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-806a-8ce7-db9bea64fe69" class=""><strong>10. 
So sánh trực tiếp AMOS–IKONOMY với IKONOMY ban đầu và SOTA</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8037-84aa-c981cfdb630f" class=""><strong>10.1. 
Kiến trúc và triết lý điều khiển</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-80a5-b51f-c6c8bd9b3b53" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-802b-b8cb-ded1cd41c655"><th id="wdWW" class="simple-table-header-color simple-table-header"><strong>Tiêu chí</strong></th><th id="wvt?" class="simple-table-header-color simple-table-header"><strong>IKONOMY ban đầu</strong></th><th id="`o?T" class="simple-table-header-color simple-table-header"><strong>SOTA (PEM / Alkaline)</strong></th><th id="CypX" class="simple-table-header-color simple-table-header"><strong>AMOS–IKONOMY</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8001-aa49-fc7948011cfa"><td id="wdWW" class="">Triết lý điều khiển</td><td id="wvt?" class="">Dựa nhiều vào phần cứng và thao tác vận hành</td><td id="`o?T" class="">Điều khiển PID, derating theo ngưỡng chuẩn</td><td id="CypX" class="">Điều khiển theo dòng với phong bì vật lý</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8065-95f1-e1599269cc77"><td id="wdWW" class="">Biến điều khiển chính</td><td id="wvt?" class="">Dòng điện (chưa khóa cứng)</td><td id="`o?T" class="">Công suất/điện áp theo cấu hình hệ</td><td id="CypX" class="">Dòng điện (giới hạn cứng)</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8015-8ac6-e32092d03ca8"><td id="wdWW" class="">Liên kết điện–nhiệt–khí</td><td id="wvt?" class="">Yếu, xử lý rời rạc</td><td id="`o?T" class="">Thường tách khối</td><td id="CypX" class="">Liên hợp, 
đồng thời</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80a8-99dd-fc29a983fd7b"><td id="wdWW" class="">Khả năng vượt giới hạn</td><td id="wvt?" class="">Phụ thuộc người vận hành</td><td id="`o?T" class="">Có thể xảy ra trước khi derating</td><td id="CypX" class="">Không cho phép</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8014-b164-e1869f4b0de8" class=""><strong>10.2. 
Công suất và sản lượng</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-804d-9250-ca64c4757726" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8036-bf08-d9fd25b58fd5"><th id="sb?m" class="simple-table-header-color simple-table-header"><strong>Thông số</strong></th><th id="rPSj" class="simple-table-header-color simple-table-header"><strong>IKONOMY ban đầu</strong></th><th id="Yo&gt;E" class="simple-table-header-color simple-table-header"><strong>SOTA</strong></th><th id="BxKl" class="simple-table-header-color simple-table-header"><strong>AMOS–IKONOMY</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80f6-b4b8-f9204bca03ff"><td id="sb?m" class="">Công suất danh định</td><td id="rPSj" class="">≈ 1 kW</td><td id="Yo&gt;E" class="">1–5 kW/mô-đun (tùy nhà sản xuất)</td><td id="BxKl" class="">1 kW/mô-đun</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-804e-822c-c9edfc044eae"><td id="sb?m" class="">Chế độ boost</td><td id="rPSj" class="">Không xác định rõ</td><td id="Yo&gt;E" class="">Thường không khuyến nghị</td><td id="BxKl" class="">Có, kèm điều kiện bắt buộc</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-805f-af89-f5e737c5e689"><td id="sb?m" class="">Sản lượng hydro</td><td id="rPSj" class="">280–300 L/h</td><td id="Yo&gt;E" class="">280–320 L/h</td><td id="BxKl" class="">≈ 300 L/h ổn định</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8002-a77a-f4039227ab6e" class="">AMOS–IKONOMY không nhắm tăng sản lượng danh định, mà <strong>duy trì sản lượng gần trần vật lý trong thời gian dài</strong>.</p></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-800e-a974-f4d91a62b045" class=""><strong>10.3. 
Tuổi thọ và suy giảm</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-8052-ba95-c263e193da44" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80c5-95cb-f08b6c54df34"><th id="uTu]" class="simple-table-header-color simple-table-header"><strong>Tiêu chí</strong></th><th id="&gt;MpB" class="simple-table-header-color simple-table-header"><strong>IKONOMY ban đầu</strong></th><th id="~Bpb" class="simple-table-header-color simple-table-header"><strong>SOTA</strong></th><th id="Y\~V" class="simple-table-header-color simple-table-header"><strong>AMOS–IKONOMY</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80b1-b3ad-f18ff7fd325c"><td id="uTu]" class="">Phương thức theo dõi suy giảm</td><td id="&gt;MpB" class="">Thủ công hoặc gián tiếp</td><td id="~Bpb" class="">Theo lịch bảo trì, cảnh báo ngưỡng</td><td id="Y\~V" class="">Theo xu hướng thời gian thực</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8056-9d7d-d10f70191015"><td id="uTu]" class="">Phát hiện suy giảm sớm</td><td id="&gt;MpB" class="">Không hệ thống</td><td id="~Bpb" class="">Hạn chế</td><td id="Y\~V" class="">Có (dR/dt, dT/dt, áp suất)</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80bb-9a9f-c8bd512f27eb"><td id="uTu]" class="">Cơ chế phản ứng</td><td id="&gt;MpB" class="">Cắt đột ngột</td><td id="~Bpb" class="">Shutdown hoặc derating muộn</td><td id="Y\~V" class="">Giảm tải sớm, 
có kiểm soát</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8060-9b9e-e856c8ed3025"><td id="uTu]" class="">Tuổi thọ hữu dụng thực tế</td><td id="&gt;MpB" class="">Phụ thuộc vận hành</td><td id="~Bpb" class="">Cao nếu điều kiện chuẩn</td><td id="Y\~V" class="">Cao hơn trong điều kiện biến động</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80d4-8591-c8099af3ef73" class=""><strong>10.4. 
Vận hành và an toàn</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-802a-baa0-c2308f8afaa0" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80b9-b963-db21ce006b29"><th id="Lpzm" class="simple-table-header-color simple-table-header"><strong>Tiêu chí</strong></th><th id="dB&lt;@" class="simple-table-header-color simple-table-header"><strong>IKONOMY ban đầu</strong></th><th id="q_Fv" class="simple-table-header-color simple-table-header"><strong>SOTA</strong></th><th id="?i@&lt;" class="simple-table-header-color simple-table-header"><strong>AMOS–IKONOMY</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8039-a775-fbf1c9b17224"><td id="Lpzm" class="">Phụ thuộc con người</td><td id="dB&lt;@" class="">Cao</td><td id="q_Fv" class="">Cao</td><td id="?i@&lt;" class="">Thấp</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80f7-993b-d9218fd826a2"><td id="Lpzm" class="">Khả năng chịu dao động nguồn</td><td id="dB&lt;@" class="">Trung bình</td><td id="q_Fv" class="">Thấp–trung bình</td><td id="?i@&lt;" class="">Cao</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80e9-8959-efbd01bed368"><td id="Lpzm" class="">Trạng thái khi dừng hệ thống</td><td id="dB&lt;@" class="">Có thể còn khí tồn</td><td id="q_Fv" class="">Phụ thuộc thiết kế</td><td id="?i@&lt;" class="">Không lưu trữ khí khi dừng</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-800d-aead-fad20b17e7bb"><td id="Lpzm" class="">Phản ứng khi lỗi</td><td id="dB&lt;@" class="">Đột ngột</td><td id="q_Fv" class="">Đột ngột</td><td id="?i@&lt;" class="">Êm, có kiểm soát</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80df-b80c-cacb56750a60" class=""><strong>10.5. 
Nhận xét tổng hợp</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ec-a316-fd9e160a28df" class="bulleted-list"><li style="list-style-type:disc"><strong>IKONOMY ban đầu</strong> mạnh về phần cứng nhưng thiếu cơ chế khóa giới hạn ở cấp logic.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8000-bad2-c91efe1e3bce" class="bulleted-list"><li style="list-style-type:disc"><strong>SOTA hiện nay</strong> đạt hiệu suất cao trong điều kiện chuẩn nhưng kém thích nghi với môi trường biến động.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-806b-85cc-d9b280a97c6e" class="bulleted-list"><li style="list-style-type:disc"><strong>AMOS–IKONOMY</strong> không vượt SOTA về hiệu suất phòng thí nghiệm, nhưng vượt trội về:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-808e-96ce-f63338e13c22" class="bulleted-list"><li style="list-style-type:circle">độ ổn định vận hành,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8021-bc33-c9fe49597b4e" class="bulleted-list"><li style="list-style-type:circle">tuổi thọ hữu dụng,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-808b-aa91-dc8d0048ef9c" class="bulleted-list"><li style="list-style-type:circle">an toàn triển khai thực tế.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8029-92a5-c8682caa0728" class="">AMOS–IKONOMY được thiết kế cho <strong>điều kiện triển khai thật</strong>, nơi các giả định của SOTA không còn đúng, và do đó đạt hiệu quả vòng đời cao hơn.</p></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8084-accc-eb475e0bc257" class=""><strong>9. 
Định nghĩa SOTA hiện nay (điện phân công suất nhỏ–trung bình)</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80cb-a1fb-d3c1fbe26843" class="">SOTA hiện nay chủ yếu gồm:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8015-88cd-d5f0803e46e4" class="bulleted-list"><li style="list-style-type:disc">PEM electrolyzer thương mại (EU/Mỹ/Nhật),</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-806a-8d97-e00018027d4a" class="bulleted-list"><li style="list-style-type:disc">Alkaline cải tiến,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80e3-bbfe-e769eeb16164" class="bulleted-list"><li style="list-style-type:disc">AEM thế hệ mới (nhiều hệ còn chưa ổn định dài hạn).</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8023-a5bf-cc6a95baa652" class="">Đặc trưng chung của SOTA:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8075-9d97-d58efe2b0baa" class="bulleted-list"><li style="list-style-type:disc">tối ưu hiệu suất tại điều kiện chuẩn,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8008-a867-c44203ab11df" class="bulleted-list"><li style="list-style-type:disc">thiết kế cho môi trường vận hành được kiểm soát tốt,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-800e-956a-eeefed9fa9e3" class="bulleted-list"><li style="list-style-type:disc">phụ thuộc cao vào nguồn điện ổn định, quy trình bảo trì chuẩn, và kỹ sư vận hành.</li></ul></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8077-b201-e1e4d36d1034" class=""><strong>10. Bảng so sánh trực tiếp</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8008-9c99-fc6c059d3722" class=""><strong>10.1. 
Kiến trúc và điều khiển</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-8012-8751-fa4d69c09398" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80f4-b830-d767b7572144"><th id="qreq" class="simple-table-header-color simple-table-header"><strong>Tiêu chí</strong></th><th id="ACFN" class="simple-table-header-color simple-table-header"><strong>IKONOMY ban đầu</strong></th><th id="bhoJ" class="simple-table-header-color simple-table-header"><strong>SOTA (PEM / Alkaline)</strong></th><th id="]b&lt;&gt;" class="simple-table-header-color simple-table-header"><strong>AMOS–IKONOMY</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80ac-a51c-d792be839018"><td id="qreq" class="">Triết lý điều khiển</td><td id="ACFN" class="">Tập trung phần cứng, phụ thuộc thao tác vận hành</td><td id="bhoJ" class="">PID và derating theo ngưỡng nhà sản xuất</td><td id="]b&lt;&gt;" class="">Điều khiển theo dòng với phong bì vật lý bắt buộc</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80f1-8349-d323f4be0845"><td id="qreq" class="">Biến điều khiển chính</td><td id="ACFN" class="">Dòng điện (chưa khóa cứng)</td><td id="bhoJ" class="">Công suất/điện áp theo cấu hình hệ</td><td id="]b&lt;&gt;" class="">Dòng điện (giới hạn cứng, không vượt)</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8066-a210-dc9b070c07a4"><td id="qreq" class="">Liên kết điện–nhiệt–khí</td><td id="ACFN" class="">Yếu, xử lý rời rạc</td><td id="bhoJ" class="">Phần lớn tách khối</td><td id="]b&lt;&gt;" class="">Liên hợp, 
đánh giá đồng thời</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80b7-b866-c7b2e8bec311"><td id="qreq" class="">Khả năng vượt giới hạn</td><td id="ACFN" class="">Có thể xảy ra do thao tác con người</td><td id="bhoJ" class="">Có thể xảy ra trước khi derating</td><td id="]b&lt;&gt;" class="">Không cho phép trong mọi trạng thái</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80b5-bb91-efb6e0041eb9" class=""><strong>Nhận xét kỹ thuật:</strong> AMOS–IKONOMY chuyển quyền quyết định từ con người và phần cứng sang logic vật lý bắt buộc.</p></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-804f-8c37-d9973f9810e1" class=""><strong>10.2. 
Công suất và sản lượng</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-801f-a682-d1d868c267f1" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8062-9f1b-dfdb0a305b97"><th id="v_U&lt;" class="simple-table-header-color simple-table-header"><strong>Thông số</strong></th><th id="Rii~" class="simple-table-header-color simple-table-header"><strong>IKONOMY ban đầu</strong></th><th id="XhFo" class="simple-table-header-color simple-table-header"><strong>SOTA</strong></th><th id="m|WX" class="simple-table-header-color simple-table-header"><strong>AMOS–IKONOMY</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8081-9a31-d06a89f0ed72"><td id="v_U&lt;" class="">Công suất danh định</td><td id="Rii~" class="">≈ 1 kW</td><td id="XhFo" class="">1–5 kW/mô-đun (tùy hãng)</td><td id="m|WX" class="">1 kW/mô-đun</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80e4-a528-d977916ad59d"><td id="v_U&lt;" class="">Chế độ boost</td><td id="Rii~" class="">Không định nghĩa rõ ràng</td><td id="XhFo" class="">Thường không khuyến nghị</td><td id="m|WX" class="">Có, nhưng bị khóa điều kiện vật lý</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80a2-a1ad-f868647e7b30"><td id="v_U&lt;" class="">Sản lượng H₂</td><td id="Rii~" class="">≈ 280–300 L/h</td><td id="XhFo" class="">280–320 L/h</td><td id="m|WX" class="">≈ 300 L/h ổn định dài hạn</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-808c-897c-cd96ae3fe909" class=""><strong>Nhận xét kỹ thuật:</strong> AMOS–IKONOMY không nhắm tăng sản lượng đỉnh, mà duy trì sản lượng gần trần vật lý trong thời gian dài.</p></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-804e-aa32-f262682fec20" class=""><strong>10.3. 
Tuổi thọ và suy giảm</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-806e-9c1a-d1a63973981d" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80e6-9268-c4676d8cfc44"><th id="UTxI" class="simple-table-header-color simple-table-header"><strong>Tiêu chí</strong></th><th id="Qxug" class="simple-table-header-color simple-table-header"><strong>IKONOMY ban đầu</strong></th><th id="s=qj" class="simple-table-header-color simple-table-header"><strong>SOTA</strong></th><th id="Uv&gt;B" class="simple-table-header-color simple-table-header"><strong>AMOS–IKONOMY</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-808c-b623-c38b18a9e9a4"><td id="UTxI" class="">Theo dõi suy giảm</td><td id="Qxug" class="">Thủ công hoặc gián tiếp</td><td id="s=qj" class="">Theo lịch bảo trì, cảnh báo ngưỡng</td><td id="Uv&gt;B" class="">Theo thời gian thực, dựa trên xu hướng</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80a6-969d-d894c43a99ba"><td id="UTxI" class="">Phát hiện suy giảm sớm</td><td id="Qxug" class="">Không hệ thống</td><td id="s=qj" class="">Hạn chế</td><td id="Uv&gt;B" class="">Có (điện trở, nhiệt, áp suất)</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-807f-9f5a-df2177cec999"><td id="UTxI" class="">Cơ chế phản ứng</td><td id="Qxug" class="">Cắt đột ngột</td><td id="s=qj" class="">Shutdown hoặc derating muộn</td><td id="Uv&gt;B" class="">Giảm tải sớm, 
có kiểm soát</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8011-b371-cd7b639c705b"><td id="UTxI" class="">Tuổi thọ hữu dụng</td><td id="Qxug" class="">Phụ thuộc vận hành</td><td id="s=qj" class="">Cao nếu điều kiện chuẩn</td><td id="Uv&gt;B" class="">Cao hơn trong điều kiện biến động</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8098-b143-dd09d02736da" class=""><strong>Nhận xét kỹ thuật:</strong> Lợi thế của AMOS–IKONOMY nằm ở quản lý suy giảm chủ động, không chờ đến ngưỡng hỏng.</p></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80e6-ac90-dc08da81470f" class=""><strong>10.4. 
Vận hành và an toàn</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-8069-9aa6-d32817211ed7" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80e3-ba67-ddec21a947ed"><th id="Bbgt" class="simple-table-header-color simple-table-header"><strong>Tiêu chí</strong></th><th id="Ff{{" class="simple-table-header-color simple-table-header"><strong>IKONOMY ban đầu</strong></th><th id="bL[@" class="simple-table-header-color simple-table-header"><strong>SOTA</strong></th><th id="p&lt;::" class="simple-table-header-color simple-table-header"><strong>AMOS–IKONOMY</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-809f-ab72-dd99b832ef84"><td id="Bbgt" class="">Phụ thuộc con người</td><td id="Ff{{" class="">Cao</td><td id="bL[@" class="">Cao</td><td id="p&lt;::" class="">Thấp</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8000-a490-df944d93c9be"><td id="Bbgt" class="">Khả năng chịu dao động nguồn</td><td id="Ff{{" class="">Trung bình</td><td id="bL[@" class="">Thấp–trung bình</td><td id="p&lt;::" class="">Cao</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80e0-a257-ce0a8b62ae2e"><td id="Bbgt" class="">Trạng thái khi dừng</td><td id="Ff{{" class="">Có thể còn khí tồn</td><td id="bL[@" class="">Phụ thuộc thiết kế</td><td id="p&lt;::" class="">Ưu tiên không lưu trữ H₂ khi dừng</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80d9-9543-f9591b908ed9"><td id="Bbgt" class="">Phản ứng khi lỗi</td><td id="Ff{{" class="">Đột ngột</td><td id="bL[@" class="">Đột ngột</td><td id="p&lt;::" class="">Êm, giảm tải có kiểm soát</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8097-a874-cc4059628e0e" class=""><strong>Kết luận phần so sánh: </strong>IKONOMY ban đầu mạnh về phần cứng nhưng thiếu khóa logic. 
SOTA mạnh trong điều kiện chuẩn nhưng kém thích nghi. AMOS–IKONOMY tối ưu cho vận hành thực tế biến động bằng cách khóa cứng giới hạn vật lý và tự động hóa quyết định bảo vệ, từ đó đạt hiệu quả vòng đời cao hơn.</p></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8050-994d-c44592448397" class=""><strong>11. Phân tích nguyên nhân tạo ưu thế kỹ thuật</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80d2-86c5-d98182937dee" class=""><strong>11.1. So với thiết kế IKONOMY ban đầu</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8050-81e3-fa86764b276c" class="">Ưu thế của AMOS–IKONOMY so với IKONOMY ban đầu <strong>không xuất phát từ phần cứng</strong>, mà từ <strong>cơ chế ra quyết định ở cấp hệ thống</strong>.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8037-bd9b-e3767334df7b" class="">Ba nguyên nhân kỹ thuật mang tính quyết định:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-8080-864b-d6c98014c51c" class="numbered-list" start="1"><li><strong>Giới hạn vật lý được tích hợp trực tiếp vào logic điều khiển</strong><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8020-8ab1-ebba55ec71bc" class="">Các giới hạn về dòng điện, nhiệt độ, gradient nhiệt, suy giảm điện hóa và áp suất khí được xem là ràng buộc bắt buộc trong mọi quyết định vận hành. Hệ thống không cho phép vượt phong bì vận hành đã xác định, ngay cả khi phần cứng còn dư khả năng chịu tải.</p></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-80d9-b89f-ccda7bcd2f62" class="numbered-list" start="2"><li><strong>Loại bỏ khả năng cưỡng bức vận hành từ con người</strong><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8084-877d-e49db60167bf" class="">Quyền “ép chạy” do áp lực sản lượng hoặc đánh giá chủ quan bị loại bỏ khỏi chuỗi điều khiển. 
Người vận hành không thể buộc hệ thống vượt giới hạn thông qua thao tác thủ công.</p></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-80f9-ae55-cf0a3940734e" class="numbered-list" start="3"><li><strong>Chuyển từ bảo vệ phản ứng sang bảo vệ phòng ngừa</strong><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8022-86e6-c55ced4e28b7" class="">Thiết kế ban đầu chủ yếu dựa trên ngưỡng cắt khi sự cố đã hình thành.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-807b-be16-c26525431f0e" class="">AMOS–IKONOMY giám sát xu hướng suy giảm và giảm tải chủ động trước khi vượt ngưỡng nguy hiểm.</p></div></li></ol></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8000-88e4-f35f5562a573" class="">Hệ quả trực tiếp:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-805d-a686-ea57634d6c25" class="bulleted-list"><li style="list-style-type:disc">giảm sốc điện hóa và sốc nhiệt,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8081-a892-f3e8592bdd85" class="bulleted-list"><li style="list-style-type:disc">giảm dừng hệ thống đột ngột,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80cc-88ff-f16936a69efd" class="bulleted-list"><li style="list-style-type:disc">duy trì trạng thái vận hành ổn định trong thời gian dài hơn.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-802b-9224-edb70cbb5311" class=""><strong>11.2. So với mặt bằng công nghệ SOTA hiện nay</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80d2-a014-eb254d3bf754" class="">AMOS–IKONOMY <strong>không cạnh tranh với SOTA ở hiệu suất phòng thí nghiệm</strong>. 
Ưu thế của hệ thống thể hiện rõ khi triển khai trong <strong>điều kiện vận hành thực tế có biến động</strong>, nơi các giả định tiêu chuẩn của SOTA không còn hiệu lực.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80bf-a759-e5697cb9eae7" class="">Ba nguyên nhân chính:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-8076-a6a0-e4ebb16d32b4" class="numbered-list" start="1"><li><strong>Thiết kế chịu dao động nguồn</strong><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8005-9692-d559d791fe5e" class="">Hệ thống không giả định nguồn điện ổn định. Logic điều khiển được xây dựng để duy trì an toàn và ổn định khi điện áp và công suất nguồn biến thiên.</p></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-80fa-956c-d86d1ccc85c3" class="numbered-list" start="2"><li><strong>Giảm yêu cầu nhân lực vận hành trình độ cao</strong><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80a6-a5b0-e4ced3e13e1e" class="">AMOS–IKONOMY không yêu cầu kỹ sư túc trực liên tục. Các quyết định bảo vệ chính được tự động hóa bằng luật vật lý cứng, không phụ thuộc phản ứng con người.</p></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-8068-976e-f07db59c6928" class="numbered-list" start="3"><li><strong>Tối ưu theo hiệu quả vòng đời</strong><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8059-b85e-cef4b0037f2a" class="">Uptime, tuổi thọ stack và chi phí bảo trì được ưu tiên hơn hiệu suất đỉnh ngắn hạn. 
Điều này tạo lợi thế kinh tế rõ rệt trong vận hành dài hạn.</p></div></li></ol></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80dc-ac53-f5b32cc6fe14" class="">Trong điều kiện triển khai thực tế, AMOS–IKONOMY duy trì <strong>hiệu quả sử dụng tổng thể cao hơn SOTA</strong>, dù hiệu suất danh định tương đương.</p></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-80c6-85c9-e5a04eb8f38e" class=""><strong>12. 
Kết luận kỹ thuật</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-808d-a2cf-f71f4b320da6" class="">AMOS–IKONOMY <strong>không nhằm vượt các định luật vật lý</strong>, không thay đổi cơ chế điện phân nước và không theo đuổi các chỉ tiêu hiệu suất phòng thí nghiệm.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8060-bac1-d392f369e3c8" class="">Giá trị kỹ thuật cốt lõi của hệ thống nằm ở việc <strong>tổ chức và thực thi vận hành</strong> theo các nguyên tắc sau:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8046-824d-c1213e9a12eb" class="bulleted-list"><li style="list-style-type:disc"><strong>Chuyển các giới hạn vật lý, nhiệt và suy giảm vật liệu thành ràng buộc điều khiển bắt buộc</strong>, được thực thi ở cấp logic trung tâm, không phụ thuộc vào quyết định vận hành.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8071-b272-d94641c25469" class="bulleted-list"><li style="list-style-type:disc"><strong>Giảm phụ thuộc vào con người</strong>, loại bỏ khả năng cưỡng bức hệ thống vượt giới hạn do áp lực sản lượng hoặc đánh giá chủ quan.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8057-b676-e535c6fa0f61" class="bulleted-list"><li style="list-style-type:disc"><strong>Duy trì vận hành ổn định gần giới hạn vật lý cho phép trong thời gian dài</strong>, thay vì tối ưu công suất đỉnh ngắn hạn dẫn đến suy giảm nhanh.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8001-9c56-fd24fcaa1e0c" class="">So với thiết kế IKONOMY ban đầu và mặt bằng công nghệ điện phân hiện hành, AMOS–IKONOMY đạt <strong>hiệu quả sử dụng thực tế cao hơn trên toàn bộ vòng đời</strong>, 
đặc biệt phù hợp với điều kiện triển khai tại Việt Nam và các môi trường có đặc tính vận hành tương đương.</p></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80cb-8830-df231ae2d78d"/></div><div style="display:contents" dir="auto"><h1 id="2eac5e6f-95bd-8043-a62a-d81257bda547" class=""><strong>KIẾN TRÚC TỔNG THỂ &amp; CHI PHÍ HỆ THỐNG AMOS–IKONOMY (01 MÔ-ĐUN ~1 kW)</strong></h1></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-800a-a9d3-d54920479784"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8065-abaf-ed3a638a526b" class=""><strong>I. KIẾN TRÚC TỔNG THỂ (ARCHITECTURE CHART)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80e8-a727-c4b73ad5cb48" class=""><strong>1. 
Chuỗi chức năng bắt buộc</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-806c-aa47-c5c3b0a8b975" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8059-8a29-fc07f93d491c"><th id="xmij" class="simple-table-header-color simple-table-header"><strong>STT</strong></th><th id="h&gt;mw" class="simple-table-header-color simple-table-header"><strong>Khối</strong></th><th id="aJZS" class="simple-table-header-color simple-table-header"><strong>Đầu vào</strong></th><th id="YNsP" class="simple-table-header-color simple-table-header"><strong>Đầu ra</strong></th><th id="gJhx" class="simple-table-header-color simple-table-header"><strong>Chức năng kỹ thuật</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8017-88b4-c82731dd1e71"><td id="xmij" class="">1</td><td id="h&gt;mw" class="">Nguồn DC</td><td id="aJZS" class="">48–96 VDC</td><td id="YNsP" class="">DC thô</td><td id="gJhx" class="">Cấp năng lượng</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-806d-919f-d88dc8d3e9a3"><td id="xmij" class="">2</td><td id="h&gt;mw" class="">Điều hòa &amp; 
bảo vệ</td><td id="aJZS" class="">DC thô</td><td id="YNsP" class="">DC sạch</td><td id="gJhx" class="">Chống xung, đảo cực, inrush</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80e7-986b-e3115681c9e9"><td id="xmij" class="">3</td><td id="h&gt;mw" class="">Cannon (điều khiển dòng)</td><td id="aJZS" class="">DC sạch</td><td id="YNsP" class="">Dòng DC định hình</td><td id="gJhx" class="">Điều khiển dòng theo AMOS</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8038-a0e9-d0acfe15cd0b"><td id="xmij" class="">4</td><td id="h&gt;mw" class="">Stack điện phân</td><td id="aJZS" class="">Dòng DC</td><td id="YNsP" class="">H₂ + nhiệt</td><td id="gJhx" class="">Tạo hydro</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-806c-954e-fac041b3370e"><td id="xmij" class="">5</td><td id="h&gt;mw" class="">Quản lý nhiệt</td><td id="aJZS" class="">Nhiệt</td><td id="YNsP" class="">Nhiệt ổn định</td><td id="gJhx" class="">Giới hạn dT/dt, ΔT</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80f3-a66e-c80978384b80"><td id="xmij" class="">6</td><td id="h&gt;mw" class="">Tách &amp; điều hòa khí</td><td id="aJZS" class="">H₂ thô</td><td id="YNsP" class="">H₂ ổn định</td><td id="gJhx" class="">Ổn định áp, an toàn</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-808a-9883-e5aedd358ae6"><td id="xmij" class="">7</td><td id="h&gt;mw" class="">Ngõ ra H₂</td><td id="aJZS" class="">H₂</td><td id="YNsP" class="">H₂ sử dụng</td><td id="gJhx" class="">Không lưu trữ khi dừng</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8074-89e5-d19e7066dc00" class=""><strong>Nguyên tắc:</strong> Không có quyết định công suất nào đi thẳng từ “nhu cầu H₂” xuống stack. 
Mọi thay đổi dòng phải qua Cannon và bị khóa bởi AMOS.</p></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-807e-83ad-c671d49efd43"/></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-803f-9065-c0d4138e3656" class=""><strong>2. 
Phân quyền quyết định</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-806a-9955-da4c43d605d3" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-807a-be84-f5b3245b3b5c"><th id="eofO" class="simple-table-header-color simple-table-header"><strong>Thực thể</strong></th><th id="{;~&gt;" class="simple-table-header-color simple-table-header"><strong>Tăng dòng</strong></th><th id="}ej]" class="simple-table-header-color simple-table-header"><strong>Giảm dòng</strong></th><th id="cCK?" class="simple-table-header-color simple-table-header"><strong>Ghi chú</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-806a-972e-f9e77431eef0"><td id="eofO" class="">Người vận hành</td><td id="{;~&gt;" class="">Không</td><td id="}ej]" class="">Không</td><td id="cCK?" class="">Không có quyền ép chạy</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8034-aa76-f62b4aa6d0fe"><td id="eofO" class="">Cannon</td><td id="{;~&gt;" class="">Không</td><td id="}ej]" class="">Có (theo lệnh)</td><td id="cCK?" class="">Chỉ thực thi</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80df-8c71-c1bc43c1712e"><td id="eofO" class="">AMOS</td><td id="{;~&gt;" class="">Có</td><td id="}ej]" class="">Có</td><td id="cCK?" class="">Bị ràng buộc vật lý</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80b5-aece-c7685e6ad0bf"><td id="eofO" class="">Stack</td><td id="{;~&gt;" class="">Không</td><td id="}ej]" class="">Không</td><td id="cCK?" class="">Thụ động</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-8040-af3d-c8466d189395"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8085-abef-e637cb737af9" class=""><strong>II. 
CẤU TRÚC THEO KHỐI (TECH BLOCK CHART)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8030-a47a-c20a0d55ba5d" class=""><strong>3. Khối nguồn &amp; bảo vệ</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-80ae-ade0-d90bcaaeab89" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80fe-a633-d327abec64c4"><th id="Vi&lt;@" class="simple-table-header-color simple-table-header"><strong>Hạng mục</strong></th><th id="^&lt;@x" class="simple-table-header-color simple-table-header"><strong>Mục tiêu</strong></th><th id="[iOF" class="simple-table-header-color simple-table-header"><strong>Cách kiểm chứng</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8001-bca1-d09d23d52af2"><td id="Vi&lt;@" class="">Dải điện áp</td><td id="^&lt;@x" class="">48–96 VDC (±15%)</td><td id="[iOF" class="">Test brown-out/ripple</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-806e-b8d7-ee7e00a2af48"><td id="Vi&lt;@" class="">Inrush</td><td id="^&lt;@x" class="">≤ 1,5×I_nom</td><td id="[iOF" class="">Đo clamp ≥10 kHz</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-809a-b2ba-ee1aef15e81a"><td id="Vi&lt;@" class="">Bảo vệ</td><td id="^&lt;@x" class="">TVS, LC, đảo cực</td><td id="[iOF" class="">Test xung/đảo cực</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80c1-86d2-fe35a6c1c3d1"/></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80fe-814a-f8e8124bbc4a" class=""><strong>4. 
Khối Cannon (Power + Control)</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-8069-96e1-cdd0c504798c" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80a1-ab45-c2c8e894e6f3"><th id="EICf" class="simple-table-header-color simple-table-header"><strong>Hạng mục</strong></th><th id="sEQr" class="simple-table-header-color simple-table-header"><strong>Mục tiêu</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8043-8bb5-de015612ddaf"><td id="EICf" class="">Topology</td><td id="sEQr" class="">Buck/Buck–Boost đồng bộ</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8088-90c1-f675e6f87967"><td id="EICf" class="">Điều khiển</td><td id="sEQr" class="">Vòng kín theo dòng</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80a1-9cfc-f9fbe0c46aee"><td id="EICf" class="">Dải dòng</td><td id="sEQr" class="">1–20 A (rated); 25–30 A (boost)</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8054-8a90-d19cbb19ddd8"><td id="EICf" class="">Giới hạn</td><td id="sEQr" class="">dI/dt ≤ 0,5 A/ms</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80f0-adb8-ffe60546fc86"><td id="EICf" class="">Hiệu suất</td><td id="sEQr" class="">94–97%</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80f5-83d2-d99ec68c9b28"><td id="EICf" class="">Đo dòng</td><td id="sEQr" class="">Sai số ≤ 1%</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-8014-9b9d-e1314100a276"/></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-805e-8001-fece3e02b1fb" class=""><strong>5. 
Stack điện phân</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-8007-80d0-c5519cd66d09" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-807a-a173-f16d2b4e0b77"><th id="usOH" class="simple-table-header-color simple-table-header"><strong>Tham số</strong></th><th id="Rqqs" class="simple-table-header-color simple-table-header"><strong>Giá trị mục tiêu</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80bb-82dc-f526e5b75401"><td id="usOH" class="">Công suất</td><td id="Rqqs" class="">1,0 kW danh định</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8004-b78d-fd745d6827f5"><td id="usOH" class="">Dòng</td><td id="Rqqs" class="">20–25 A</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80f4-9c1e-c39fee0b011b"><td id="usOH" class="">Điện áp</td><td id="Rqqs" class="">40–60 V</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-800c-92fb-fc6f737f35c9"><td id="usOH" class="">Vùng chạy</td><td id="Rqqs" class="">Ổn định + boost ngắn</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80b1-ad11-f82f4106ed9d"><td id="usOH" class="">Giới hạn</td><td id="Rqqs" class="">Tafel, nhiệt, suy giảm</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80d2-b68c-c3d8f570f9e5"/></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80b8-8f03-c6c42281e480" class=""><strong>6. 
Quản lý nhiệt</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-80c4-8641-de272aed0bd0" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80a0-bc2d-d4311b0a8953"><th id="i]Hb" class="simple-table-header-color simple-table-header"><strong>Tham số</strong></th><th id="RApI" class="simple-table-header-color simple-table-header"><strong>Ngưỡng</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80c5-9473-fd3692080743"><td id="i]Hb" class="">Nhiệt độ</td><td id="RApI" class="">55–75 °C</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80a4-ab1e-c53b195a8cd7"><td id="i]Hb" class="">dT/dt</td><td id="RApI" class="">≤ 1 °C/phút</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-808d-b2f3-ce623f4702c6"><td id="i]Hb" class="">ΔT stack</td><td id="RApI" class="">≤ 5 °C</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-807b-9ddd-f25096746bfa"><td id="i]Hb" class="">Chiến lược</td><td id="RApI" class="">Giảm dòng trước, không cắt</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80d3-9193-c99358abd24f"/></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8060-a1cb-f55f7997efa7" class=""><strong>7. 
Nước &amp; khí</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-807e-a621-cb4edb55f163" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-806b-b548-e73a65f562ab"><th id="|D:s" class="simple-table-header-color simple-table-header"><strong>Thành phần</strong></th><th id="K\MO" class="simple-table-header-color simple-table-header"><strong>Mục tiêu</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80f5-8f74-e90886cc5626"><td id="|D:s" class="">Áp suất</td><td id="K\MO" class="">1,5–3 bar</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80e6-a71c-e9ee52c67a06"><td id="|D:s" class="">Ripple áp</td><td id="K\MO" class="">≤ 3% RMS</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8062-83b8-f618a8b190a1"><td id="|D:s" class="">Carry-over nước</td><td id="K\MO" class="">0 (thiết kế)</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8022-b980-e5d0c2c363fd"><td id="|D:s" class="">Dừng máy</td><td id="K\MO" class="">Không lưu trữ H₂</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80e5-8127-c49864f97099"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-805b-850d-f51328e42793" class=""><strong>III. CHI PHÍ CHI TIẾT (COST BREAKDOWN)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80ed-abe8-d64d64f39158" class=""><strong>8. 
Chi phí phần cứng theo khối (USD/mô-đun)</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-806b-897c-e86509f5fbd6" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80f4-9e96-ee84fe4ba6d9"><th id="o\b@" class="simple-table-header-color simple-table-header"><strong>STT</strong></th><th id="z`@;" class="simple-table-header-color simple-table-header"><strong>Khối</strong></th><th id="{pvB" class="simple-table-header-color simple-table-header"><strong>Thấp</strong></th><th id="K{kG" class="simple-table-header-color simple-table-header"><strong>Cao</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80fa-80b0-de26874c06f4"><td id="o\b@" class="">1</td><td id="z`@;" class="">Nguồn &amp; bảo vệ</td><td id="{pvB" class="">40</td><td id="K{kG" class="">55</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80ba-b988-ddb1179766b3"><td id="o\b@" class="">2</td><td id="z`@;" class="">Cannon (công suất + MCU)</td><td id="{pvB" class="">80</td><td id="K{kG" class="">120</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80f1-a137-fa9344a3101d"><td id="o\b@" class="">3</td><td id="z`@;" class="">Stack điện phân</td><td id="{pvB" class="">230</td><td id="K{kG" class="">390</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8078-a371-cb66e7d7f62b"><td id="o\b@" class="">4</td><td id="z`@;" class="">Hệ thống nhiệt</td><td id="{pvB" class="">50</td><td id="K{kG" class="">80</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80a4-9f64-e261f8961162"><td id="o\b@" class="">5</td><td id="z`@;" class="">Nước &amp; 
khí</td><td id="{pvB" class="">40</td><td id="K{kG" class="">70</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80e5-936f-c56d4692f366"><td id="o\b@" class="">6</td><td id="z`@;" class="">Khung + dây + lắp</td><td id="{pvB" class="">30</td><td id="K{kG" class="">50</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8061-b77a-d75a3a4951b0"><td id="o\b@" class=""><strong>—</strong></td><td id="z`@;" class=""><strong>Tổng</strong></td><td id="{pvB" class=""><strong>470</strong></td><td id="K{kG" class=""><strong>760</strong></td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-8015-b6c6-c0d5590d83b2"/></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-804b-b704-ed62c2c8cc01" class=""><strong>9. 
Tỷ trọng chi phí</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-8078-9ae7-da839a6c8fe5" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8088-99bd-f22f0141cf9f"><th id="KJEo" class="simple-table-header-color simple-table-header"><strong>Khối</strong></th><th id="E;?U" class="simple-table-header-color simple-table-header"><strong>Tỷ trọng</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-806c-9a48-dd3458c72007"><td id="KJEo" class="">Stack</td><td id="E;?U" class="">45–55%</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80ec-b069-ecca577ec541"><td id="KJEo" class="">Cannon</td><td id="E;?U" class="">15–20%</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80fb-b7c9-fea8206a1a47"><td id="KJEo" class="">Nhiệt</td><td id="E;?U" class="">8–10%</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8056-9252-e9272e95a5bc"><td id="KJEo" class="">Nước &amp; khí</td><td id="E;?U" class="">8–10%</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-809c-8999-e07512d1fc5e"><td id="KJEo" class="">Khác</td><td id="E;?U" class="">10–15%</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80b4-ae84-dc348fa6eb60"/></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8085-a4f4-faea774d7488" class=""><strong>10. 
Chi phí theo quy mô sản xuất</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-80dc-93bb-d2213f81b85a" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80fe-9646-e0f4e15fe973"><th id="kra~" class="simple-table-header-color simple-table-header"><strong>Quy mô</strong></th><th id="_\cX" class="simple-table-header-color simple-table-header"><strong>USD/mô-đun</strong></th><th id="l^p&gt;" class="simple-table-header-color simple-table-header"><strong>Ghi chú</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80cb-af2c-fa07ee2221d5"><td id="kra~" class="">50–100/năm</td><td id="_\cX" class="">650–800</td><td id="l^p&gt;" class="">Lắp thủ công</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-800c-b768-c1eb144e82da"><td id="kra~" class="">300–500/năm</td><td id="_\cX" class="">520–650</td><td id="l^p&gt;" class="">Chuẩn hóa</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8037-aaa2-e9f3e1ebefb0"><td id="kra~" class="">~1.000/năm</td><td id="_\cX" class="">450–600</td><td id="l^p&gt;" class="">Mua số lượng</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-804a-9fde-dcd1996d30ac"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8033-8201-df732453b293" class=""><strong>IV. GIÁ TRỊ VÒNG ĐỜI (LIFETIME VALUE)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-807f-91df-dc131ebc19fc" class=""><strong>11. 
So sánh vận hành</strong></h3></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-8075-8a86-f6de14f9106e" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8071-af75-ea423f20c4c0"><th id="XCAn" class="simple-table-header-color simple-table-header"><strong>Chỉ tiêu</strong></th><th id="Ug[M" class="simple-table-header-color simple-table-header"><strong>Hệ thường</strong></th><th id="[nY\" class="simple-table-header-color simple-table-header"><strong>AMOS–IKONOMY</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80fa-8c87-cba7db3157a8"><td id="XCAn" class="">Uptime mục tiêu</td><td id="Ug[M" class="">90–95%</td><td id="[nY\" class="">≥ 98%</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8028-93cd-d62bb549f4dd"><td id="XCAn" class="">Tuổi thọ stack</td><td id="Ug[M" class="">Chuẩn</td><td id="[nY\" class="">+50–100%</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-803c-899a-fbe10a7ddca4"><td id="XCAn" class="">Dừng đột ngột</td><td id="Ug[M" class="">Có</td><td id="[nY\" class="">Rất thấp</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8039-9160-d0f18bcbdc20"><td id="XCAn" class="">Chi phí vòng đời</td><td id="Ug[M" class="">Cao</td><td id="[nY\" class="">Thấp hơn 25–40%</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8070-b78b-de8c75f3746f" class=""><strong>KẾT LUẬN VỀ CHI PHÍ HỆ THỐNG AMOS–IKONOMY</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-8018-be15-dc5de300056a" class="numbered-list" start="1"><li><strong>Chi phí đầu tư ban đầu (CAPEX) ở mức trung bình–thấp trong phân khúc</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8056-be3f-f58f9ce74172" class="bulleted-list"><li style="list-style-type:disc">Chi phí p
hần cứng cho 01 mô-đun ~1 kW nằm trong khoảng <strong>470–760 USD</strong> ở quy mô nhỏ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80cc-93e6-fd0f71bb0a0c" class="bulleted-list"><li style="list-style-type:disc">Khi sản xuất 300–1.000 mô-đun/năm, chi phí có thể giảm về <strong>450–600 USD/mô-đun</strong> nhờ chuẩn hóa và mua linh kiện số lượng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8002-8190-dcf5f2584fb7" class="bulleted-list"><li style="list-style-type:disc">Mức này <strong>thấp hơn rõ rệt</strong> so với mô-đun điện phân nhập khẩu cùng công suất, vốn thường cao hơn do chi phí stack, logistics và phụ thuộc nhà cung cấp.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8094-aa40-d50548abb904" class=""><strong>Cấu trúc chi phí hợp lý, không “đội giá” ở phần điều khiển</strong></p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80f9-9a69-c15a459dc274" class="bulleted-list"><li style="list-style-type:disc">Stack điện phân chiếm <strong>45–55% tổng chi phí</strong>, đúng với mặt bằng kỹ thuật chung.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-809c-88bb-cb9728c878bd" class="bulleted-list"><li style="list-style-type:disc">Phần điều khiển Cannon + AMOS chỉ chiếm <strong>15–20%</strong>, 
nhưng tạo ra giá trị lớn nhất về tuổi thọ và độ ổn định.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80fb-bfa1-f2a05fec3e88" class="bulleted-list"><li style="list-style-type:disc">Không phát sinh chi phí cho phần cứng phức tạp hoặc vật liệu đặc biệt khó nội địa hóa.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80ce-b048-e23b872d0510" class=""><strong>Chi phí vận hành (OPEX) thấp nhờ logic giảm tải sớm</strong></p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80d0-9fd9-f13f43bfdcdf" class="bulleted-list"><li style="list-style-type:disc">AMOS giảm số lần dừng đột ngột và sự cố ngoài kế hoạch.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80a8-823e-e9790103880b" class="bulleted-list"><li style="list-style-type:disc">Tuổi thọ stack tăng <strong>50–100%</strong>, kéo dài chu kỳ thay thế.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-808f-a368-c353c1893c73" class="bulleted-list"><li style="list-style-type:disc">Nhu cầu kỹ sư túc trực thấp, giảm chi phí nhân sự vận hành.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-800b-9b8b-fd4edd681d96" class=""><strong>Chi phí vòng đời (LCOH) thấp hơn dù CAPEX không tối thiểu</strong></p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8024-b228-c41e57fc255b" class="bulleted-list"><li style="list-style-type:disc">AMOS–IKONOMY không tối ưu để rẻ nhất lúc mua, mà tối ưu để <strong>rẻ nhất trong suốt vòng đời</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-802e-b278-c9d85ec1dd25" class="bulleted-list"><li style="list-style-type:disc">Với uptime mục tiêu ≥ 98% và suy giảm được kiểm soát, 
<strong>chi phí hydro/kg trong vòng đời giảm 25–40%</strong> so với hệ thống vận hành theo ngưỡng cắt thông thường.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80b3-ac4c-c1aaff5d10a4" class="bulleted-list"><li style="list-style-type:disc">Lợi thế này càng rõ trong điều kiện nguồn điện dao động và môi trường khó kiểm soát.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-807e-831f-f7c48be03840" class=""><strong>Phù hợp nội địa hóa và mở rộng quy mô tại Việt Nam</strong></p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80bf-9c3a-c6a73cb9afd0" class="bulleted-list"><li style="list-style-type:disc">Tỷ lệ nội địa hóa phần cơ khí, nhiệt, lắp ráp đạt <strong>60–70%</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ca-8824-c3a4b99e5dc7" class="bulleted-list"><li style="list-style-type:disc">Không phụ thuộc chuỗi cung ứng phức tạp.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-803f-ab04-f8bc8800ce8f" class="bulleted-list"><li style="list-style-type:disc">Mô hình chi phí tuyến tính theo số mô-đun, phù hợp triển khai phân tán (đảo, cảng, khu công nghiệp).</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8026-80aa-f32fc64acf17" class="">Về chi phí, AMOS–IKONOMY đạt <strong>điểm cân bằng tối ưu</strong> giữa CAPEX, OPEX và rủi ro vận hành. Hệ thống <strong>không rẻ nhất khi mua</strong>, nhưng <strong>rẻ nhất khi vận hành dài hạn</strong>, đặc biệt trong điều kiện thực tế tại Việt Nam.</p></div><div style="display:contents" dir="auto"><h1 id="2eac5e6f-95bd-80b4-a441-ce0b8a4625ae" class=""><strong>TẬP PHƯƠNG TRÌNH CỐT LÕI CỦA HỆ THỐNG AMOS–IKONOMY</strong></h1></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80f1-8b70-f402f83e707e"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-80f3-971b-de64e5b66f63" class=""><strong>I. 
Cơ sở vật lý bắt buộc của điện phân nước</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-809e-95a9-f45e2c5cfd9a" class=""><strong>1. Quan hệ giữa dòng điện và sản lượng hydro (Luật Faraday)</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80a4-a56f-c1465b67ce0c" class="">1.1. Sản lượng hydro sinh ra tỉ lệ tuyến tính với dòng điện chạy qua stack.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80d6-b661-d5db5a693167" class="">1.2. Điện áp không quyết định lượng hydro tạo thành.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8057-98fd-de8d41f54a20" class="">1.3. Không thể tăng sản lượng nếu không tăng dòng điện.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-803d-ae0a-e1a1c62388a3" class="">1.4. Phương trình:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8061-84a8-f23533ae888b" class="bulleted-list"><li style="list-style-type:disc">Lưu lượng H₂ (mol/s) = (η_F × I) / (2 × F)</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8059-8017-c110b3b1d735" class="bulleted-list"><li style="list-style-type:disc">Viết dạng số: Lưu lượng H₂ (mol/s) = (η_F × I) / 192970</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80aa-ac6e-c62bb0298131" class="">1.5. 
Biến số:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-802e-81bf-e1d27dc58ca8" class="bulleted-list"><li style="list-style-type:disc">I: dòng điện qua stack, dải 10–30 A.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80bf-a678-c0ef3db5a2e8" class="bulleted-list"><li style="list-style-type:disc">η_F: hiệu suất Faraday, dải 0,90–0,98.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-800e-af05-c79ce41265bb" class="bulleted-list"><li style="list-style-type:disc">F: hằng số Faraday, 96485 C/mol.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-801c-9df1-f99d3773024a" class="">1.6. Áp dụng trong AMOS:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-808a-9f45-ce1f3ce1b587" class="bulleted-list"><li style="list-style-type:disc">Dòng điện là biến điều khiển duy nhất.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8046-85f4-d612e12c6bc2" class="bulleted-list"><li style="list-style-type:disc">Điện áp không được dùng để điều khiển công suất.</li></ul></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80c7-a951-dd4e962fe4ea"/></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80cd-a339-f77bdaf679e6" class=""><strong>2. Quy đổi sang lưu lượng thể tích (phục vụ thiết kế)</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8084-a02e-e87109ef0ade" class="">2.1. Ở điều kiện tiêu chuẩn, 1 mol H₂ ≈ 22,4 L.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8015-abfa-da622b21e1ba" class="">2.2. Công thức thực dụng:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8073-bb88-ee0542700901" class="bulleted-list"><li style="list-style-type:disc">Lưu lượng H₂ (L/h) ≈ 0,418 × I × η_F.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80d2-87b1-d20221287f76" class="">2.3. 
Ví dụ:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8027-aff2-f6d3538a43e3" class="bulleted-list"><li style="list-style-type:disc">I = 25 A.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80d6-8224-fe6c2fbc3675" class="bulleted-list"><li style="list-style-type:disc">η_F = 0,95.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8024-96cf-e923c0ad8aed" class="bulleted-list"><li style="list-style-type:disc">Lưu lượng ≈ 9,9 L/h.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80b6-bb6a-c633e047ea88" class="">2.4. Ý nghĩa thiết kế:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8062-a5f3-ce30e1c47e8c" class="bulleted-list"><li style="list-style-type:disc">Công suất và sản lượng module được xác định trực tiếp từ dòng điện thiết kế.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8055-b033-e129d06985d1" class="bulleted-list"><li style="list-style-type:disc">Không tồn tại hệ số tối ưu vượt phương trình này.</li></ul></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-803b-be00-dc648406919d"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-80ab-88bf-c9a37edcb215" class=""><strong>II. Phương trình điện áp stack (chỉ dùng giám sát)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80c0-9c67-d7546f21a887" class=""><strong>3. Phân rã điện áp stack</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-801e-9bb8-d49de6a6e291" class="">3.1. 
Biểu thức tổng quát:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80f7-a4fe-e3220f7d715f" class="bulleted-list"><li style="list-style-type:disc">V_stack = E_rev(T)<div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8059-8186-d78518daf7ae" class="">+ η_hoạt_hóa(I,T)</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80e4-acb3-f6d2c9753326" class="">+ I × R_tương_đương(T)</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-804e-853a-ce123d54a57e" class="">+ η_truyền_khối(I).</p></div></li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80d9-bbae-c42527941a65" class="">3.2. Ý nghĩa thành phần:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8001-9f3b-f654b26e503f" class="bulleted-list"><li style="list-style-type:disc">E_rev: điện áp thuận nghịch, phụ thuộc nhiệt độ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-802f-92e9-c6459cad9d16" class="bulleted-list"><li style="list-style-type:disc">η_hoạt_hóa: tổn hao động học phản ứng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80bd-b47d-c2afc7ae1f2b" class="bulleted-list"><li style="list-style-type:disc">I × R: tổn hao điện trở.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8071-8471-d47529df0beb" class="bulleted-list"><li style="list-style-type:disc">η_truyền_khối: tổn hao khuếch tán và bọt khí.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8096-b937-ea1d7a79f706" class="">3.3. 
Nguyên tắc sử dụng trong AMOS:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8056-899e-d6ae9308ff2a" class="bulleted-list"><li style="list-style-type:disc">Không dùng điện áp để ép dòng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80d7-976e-f2ffcb76938b" class="bulleted-list"><li style="list-style-type:disc">Chỉ dùng để giám sát trạng thái.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8068-9bfb-fbcc9650e9fd" class="bulleted-list"><li style="list-style-type:disc">Chỉ dùng để phát hiện suy giảm và bất thường vận hành.</li></ul></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80f8-8258-dc798fb0b82f"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-80dd-bb04-fbb4977b580f" class=""><strong>III. Phương trình suy giảm – lõi khác biệt của AMOS</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80d5-b691-c71e9fdbb5de" class=""><strong>4. Điện trở tương đương của stack</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8025-80ef-ee1021f4c3cd" class="">4.1. Định nghĩa:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8096-b7cb-d5102dae7c20" class="bulleted-list"><li style="list-style-type:disc">R_eq(t) = [V_stack(t) − E_rev(T)] / I(t).</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8059-b103-c56adda25c25" class="">4.2. AMOS không sử dụng giá trị tức thời.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80cd-b116-eb2a45486a7d" class="">4.3. AMOS theo dõi xu hướng thay đổi theo thời gian.</p></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80bf-b9cd-ed3909d1abbe"/></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80fc-b8d0-f59de957aa34" class=""><strong>5. 
Tốc độ suy giảm điện trở</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80bc-b93a-d86575681efb" class="">5.1. Chỉ số giám sát chính:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8033-9891-e02bb9481a74" class="bulleted-list"><li style="list-style-type:disc">dR/dt = ΔR / Δt.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8043-837b-e5b3f71454cd" class="">5.2. Diễn giải vận hành:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-809e-9999-c23018d0a8a7" class="bulleted-list"><li style="list-style-type:disc">dR/dt ≈ 0: stack ổn định.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8022-a316-f524f5055bb9" class="bulleted-list"><li style="list-style-type:disc">dR/dt tăng chậm: lão hóa bình thường.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-800a-b1c7-f1bd819a7fe2" class="bulleted-list"><li style="list-style-type:disc">dR/dt tăng nhanh: suy giảm không hồi phục.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80c9-8119-cca6c7fc3d9b" class="">5.3. Luật điều khiển cứng:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80e6-af46-caebd37ef4d7" class="bulleted-list"><li style="list-style-type:disc">dR/dt vượt ngưỡng → cấm tăng dòng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-806f-bb72-d9adf0a2ad97" class="bulleted-list"><li style="list-style-type:disc">dR/dt tiếp tục tăng → giảm dòng chủ động.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-800e-9369-f3095f0d8613" class="">5.4. AMOS không chờ hỏng mới phản ứng.</p></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80e4-b779-e0920ec2216b"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-808b-aba1-c5d9d6f6718a" class=""><strong>IV. 
Tránh vùng Tafel dốc (vùng phá tuổi thọ)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-809c-92d8-db4613d3d50e" class=""><strong>6. Quan hệ Tafel (xấp xỉ)</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8039-a90d-c7838d38dd25" class="">6.1. Biểu thức:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8052-bddb-faad3aa85874" class="bulleted-list"><li style="list-style-type:disc">η_hoạt_hóa ≈ a + b × log(I).</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-807b-9e9b-e7ade5c1e167" class="">6.2. Khi dòng vượt ngưỡng:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80fc-a97d-d7a54e2530b1" class="bulleted-list"><li style="list-style-type:disc">Tổn hao tăng phi tuyến.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ae-bf9b-db3d43238e74" class="bulleted-list"><li style="list-style-type:disc">Suy giảm vật liệu tăng mạnh.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-804b-a325-e1aa0d1f8cfa" class="">6.3. Định nghĩa vùng cấm:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8023-8bf0-caf028e85b57" class="bulleted-list"><li style="list-style-type:disc">I &gt; I_Tafel.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8042-9693-f48e994e8f0a" class="bulleted-list"><li style="list-style-type:disc">Chỉ cho phép trong thời gian ngắn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8017-a657-e551f2a6bec0" class="bulleted-list"><li style="list-style-type:disc">Bắt buộc có giai đoạn hồi phục.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80f7-bff2-f9f857be233a" class="">6.4. 
Luật AMOS:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80f0-ac71-d14305d53aef" class="bulleted-list"><li style="list-style-type:disc">Boost trên I_Tafel bị giới hạn thời gian.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80f4-9768-dd9babd030f6" class="bulleted-list"><li style="list-style-type:disc">Không cho phép boost lặp dày.</li></ul></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-8018-9e2c-e55c48ecf22e"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-80e6-90d2-d7d4f029a041" class=""><strong>V. Phương trình nhiệt – giới hạn sống còn</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-806a-84a8-d84d5a086ff3" class=""><strong>7. Cân bằng nhiệt đơn giản hóa</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80be-9dc0-fe8ebc11c46c" class="">7.1. Biểu thức điều khiển:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-808a-b78a-fc87e670c601" class="bulleted-list"><li style="list-style-type:disc">C_nhiệt × (dT/dt)<div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8093-8da3-cf47e7418ccb" class="">= P_điện − P_phản_ứng − hA(T − T_môi_trường).</p></div></li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80c7-ae85-ef6141217f89" class="">7.2. 
Biến số:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80c5-ac21-f941ef69195b" class="bulleted-list"><li style="list-style-type:disc">C_nhiệt: nhiệt dung hiệu dụng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80f7-9d73-e3d80fafd818" class="bulleted-list"><li style="list-style-type:disc">dT/dt: tốc độ tăng nhiệt.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80c8-8980-f986efd08d56" class="bulleted-list"><li style="list-style-type:disc">P_điện: công suất điện vào.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8073-be09-eb510347503d" class="bulleted-list"><li style="list-style-type:disc">P_phản_ứng: công suất tạo H₂.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8031-828c-d099bd0ce786" class="bulleted-list"><li style="list-style-type:disc">hA: khả năng tản nhiệt.</li></ul></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-8095-a8f7-ea76153955c4"/></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8007-9179-f76c17620930" class=""><strong>8. Giới hạn nhiệt bắt buộc</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8095-864e-c27eb6ab8153" class="">8.1. Giới hạn cứng:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8004-ad75-f79f622a211f" class="bulleted-list"><li style="list-style-type:disc">dT/dt ≤ 1 °C/phút.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8080-a962-f3ee0f77b426" class="bulleted-list"><li style="list-style-type:disc">ΔT_stack ≤ 5 °C.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-803d-a47b-ef902174dafb" class="">8.2. 
Luật điều khiển:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80bf-8a83-d70c902e9b63" class="bulleted-list"><li style="list-style-type:disc">Vi phạm bất kỳ giới hạn nào → giảm dòng ngay.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8049-9917-e1d510a3dbcc" class="bulleted-list"><li style="list-style-type:disc">Không chờ cảnh báo.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80a3-a097-db40904c00c6" class="bulleted-list"><li style="list-style-type:disc">Không cắt đột ngột, trừ trường hợp an toàn tuyệt đối.</li></ul></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80f5-9666-fcbdafebd4a4"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-80dc-a6da-c4ccf4040b76" class=""><strong>VI. Luật tổng hợp ra quyết định của AMOS</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-802f-9c7f-f27548ac10d2" class="">9.1. AMOS chỉ cho phép tăng dòng khi đồng thời thỏa mãn:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8045-9c35-dd62ee298764" class="bulleted-list"><li style="list-style-type:disc">dR/dt thấp.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80eb-b07b-e93763b822ad" class="bulleted-list"><li style="list-style-type:disc">Nhiệt độ và gradient ổn định.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80dd-b48f-ff87a9c84db2" class="bulleted-list"><li style="list-style-type:disc">Áp suất khí ổn định.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-803c-9e62-d3bad6abce54" class="bulleted-list"><li style="list-style-type:disc">Không có stress tích lũy gần đây.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80bf-8251-f0527ce4d3d2" class="">9.2. 
Nguyên tắc quyết định:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-809e-8aaf-cef12d32febb" class="bulleted-list"><li style="list-style-type:disc">Nếu tăng sản lượng ngắn hạn nhưng làm tăng xác suất hỏng trong tương lai → hành động bị từ chối.</li></ul></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80f0-ac50-c49433364a44"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-80fc-9bf7-eaa18b58c463" class=""><strong>Kết luận kỹ thuật</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8028-a0f6-f145aad264d5" class="">10.1. AMOS–IKONOMY không vượt định luật vật lý.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8012-ac15-cae02df2ebf5" class="">10.2. AMOS–IKONOMY không thay đổi hóa học.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8060-a6c5-cca7c79dd28d" class="">10.3. AMOS–IKONOMY không phá Luật Faraday.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80df-a544-f8782c79ab0a" class="">10.4. Khác biệt cốt lõi:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8072-a578-c98339c19f54" class="bulleted-list"><li style="list-style-type:disc">Chuyển các phương trình vật lý thành luật điều khiển bắt buộc.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-809b-8905-e67f143dc65f" class="bulleted-list"><li style="list-style-type:disc">Không phụ thuộc giám sát thủ công của con người.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8050-ad0c-c24a2e875a71" class="">10.5. 
Hệ quả trực tiếp:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80d5-acbe-c3bde5acbe65" class="bulleted-list"><li style="list-style-type:disc">Tuổi thọ hệ thống dài hơn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80fa-ba62-d00da69a6c60" class="bulleted-list"><li style="list-style-type:disc">Mức độ an toàn cao hơn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8010-86d1-e0ee681232f2" class="bulleted-list"><li style="list-style-type:disc">Chi phí vòng đời thấp hơn.</li></ul></div><div style="display:contents" dir="auto"><h1 id="2eac5e6f-95bd-8013-ace0-dc4e071931dc" class=""><strong>Sơ đồ khối tổng thể </strong></h1></div><div style="display:contents" dir="auto"><pre id="2eac5e6f-95bd-806b-88bf-da737da1f441" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">[NGUỒN DC 48–96V]
   |
   v
[KHỐI BẢO VỆ &amp; ĐIỀU HÒA NGUỒN]
(OVP/UVP, đảo cực, hạn dòng khởi động, TVS, lọc LC)
   |
   v
[LỌC EMI/EMC &amp; PHÂN VÙNG NỐI ĐẤT]
(tách mass công suất / mass tín hiệu / chassis)
   |
   v
[KHỐI CÔNG SUẤT CANNON]
(buck hoặc buck-boost đồng bộ, điều khiển theo DÒNG)
   |--------------------\
   |                     \
   v                      v
[ĐO DÒNG]              [ĐO ÁP STACK]
(shunt/Hall + ADC)     (tổng + tuỳ chọn chia đoạn)
   \                     /
    \                   /
     v                 v
[MCU THỜI GIAN THỰC]
(vòng điều khiển dòng 0,1–1 kHz,
giới hạn dI/dt, tạo thư viện dạng sóng)
     |
     v
[STACK ĐIỆN PHÂN]
     |
     +--&gt; [PHẦN CỨNG NHIỆT] --&gt; [CẢM BIẾN NHIỆT T1..T3]
     |
     +--&gt; [TÁCH KHÍ H2/O2] --&gt; [BẪY NƯỚC / BUBBLER / LỌC]
     |                          |
     |                          v
     |                      [VAN/ĐIỀU ÁP H2] --&gt; [NGÕ RA H2]
     |
     +--&gt; [HỆ NƯỚC] --&gt; [CẢM BIẾN MỨC] + [CẢM BIẾN ĐỘ DẪN (tuỳ chọn)]
     |
     +--&gt; [CẢM BIẾN ÁP SUẤT P + DAO ĐỘNG ÁP]

[AMOS CORE]
(ước lượng trạng thái, tích luỹ suy giảm, quản lý phong bì,
logic cấp/khóa boost, chính sách giảm tải)
     |
     v
[GIÁM SÁT / KIỂM TOÁN]
(log, truy vết quyết định, báo cáo uptime, can thiệp, trend suy giảm)</code></pre></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80f5-90dd-c44c2d87f7f5"/></div><div style="display:contents" dir="auto"><h1 id="2eac5e6f-95bd-801f-8a04-e4b574dc3300" class=""><strong>1) Bảng tín hiệu I/O (đủ để viết firmware + thiết kế mạch đo)</strong></h1></div><div style="display:contents" dir="auto"><blockquote id="2eac5e6f-95bd-80f1-a04c-cd879e5503db" class="">Gợi ý đọc: “Tần số lấy mẫu” là <strong>tốc độ MCU đọc và xử lý</strong>. 
Một số tín hiệu đo nhanh nhưng chỉ cần <strong>lọc và downsample</strong> cho AMOS.</blockquote></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-80b5-9045-dd83d127f8da" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8060-a789-fc0b5967df14"><th id="jbC|" class="simple-table-header-color simple-table-header"><strong>Tên tín hiệu</strong></th><th id="{tYZ" class="simple-table-header-color simple-table-header"><strong>Loại cảm biến/nguồn</strong></th><th id="ZJEf" class="simple-table-header-color simple-table-header"><strong>Kiểu tín hiệu</strong></th><th id="&gt;dMM" class="simple-table-header-color simple-table-header"><strong>Tần số lấy mẫu (khuyến nghị)</strong></th><th id="gbXE" class="simple-table-header-color simple-table-header"><strong>Độ chính xác mục tiêu</strong></th><th id="^Wif" class="simple-table-header-color simple-table-header"><strong>Mục đích điều khiển</strong></th><th id="^T@P" class="simple-table-header-color simple-table-header"><strong>Nếu lỗi tín hiệu (fail-safe)</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80a4-9a5b-fd4bfd344014"><td id="jbC|" class="">VBUS_IN</td><td id="{tYZ" class="">Chia áp + ADC</td><td id="ZJEf" class="">Analog</td><td id="&gt;dMM" class="">100–500 Hz</td><td id="gbXE" class="">±2%</td><td id="^Wif" class="">phát hiện sụt áp/dao động nguồn, feed-forward</td><td id="^T@P" class="">giới hạn công suất, cấm boost</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-804b-86ef-e6ceaf7f6d66"><td id="jbC|" class="">I_STACK</td><td id="{tYZ" class="">Shunt + INA / Hall + ADC</td><td id="ZJEf" class="">Analog</td><td id="&gt;dMM" class="">1–5 kHz (vòng dòng), log 10–50 Hz</td><td id="gbXE" class="">≤±1%</td><td id="^Wif" class="">điều khiển dòng vòng kín, tính Faraday</td><td id="^T@P" class="">clamp dòng về 0, 
vào Protective</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8027-9269-e754fa01c78a"><td id="jbC|" class="">V_STACK_TOTAL</td><td id="{tYZ" class="">Chia áp + ADC</td><td id="ZJEf" class="">Analog</td><td id="&gt;dMM" class="">500–1.000 Hz, log 10–50 Hz</td><td id="gbXE" class="">≤±1%</td><td id="^Wif" class="">tính R_eq, phát hiện bất thường điện hoá</td><td id="^T@P" class="">cấm boost, derate</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80ca-b2ac-c844988188d2"><td id="jbC|" class="">V_STACK_SEG[i] (tuỳ chọn)</td><td id="{tYZ" class="">Chia áp nhiều kênh</td><td id="ZJEf" class="">Analog</td><td id="&gt;dMM" class="">100–500 Hz</td><td id="gbXE" class="">≤±1.5%</td><td id="^Wif" class="">phát hiện lệch cục bộ (hotspot điện hoá)</td><td id="^T@P" class="">derate, báo bảo trì</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80a6-87f5-ccb2fb6e124d"><td id="jbC|" class="">T1 (inlet/plate)</td><td id="{tYZ" class="">NTC/PT1000</td><td id="ZJEf" class="">Analog</td><td id="&gt;dMM" class="">10–50 Hz</td><td id="gbXE" class="">±0.5°C</td><td id="^Wif" class="">kiểm soát dT/dt</td><td id="^T@P" class="">kết thúc boost, derate</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8034-af71-d8f95fe7e63e"><td id="jbC|" class="">T2 (core/hotspot)</td><td id="{tYZ" class="">NTC/PT1000</td><td id="ZJEf" class="">Analog</td><td id="&gt;dMM" class="">10–50 Hz</td><td id="gbXE" class="">±0.5°C</td><td id="^Wif" class="">kiểm soát T_max, 
ΔT</td><td id="^T@P" class="">Protective nếu vượt hard</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8091-9736-ce5bfb6cb4cb"><td id="jbC|" class="">T3 (outlet/case)</td><td id="{tYZ" class="">NTC/PT1000</td><td id="ZJEf" class="">Analog</td><td id="&gt;dMM" class="">10–50 Hz</td><td id="gbXE" class="">±0.5°C</td><td id="^Wif" class="">đánh giá gradient và tản nhiệt</td><td id="^T@P" class="">cấm boost</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80c3-b2a7-da5e9f1d0427"><td id="jbC|" class="">P_H2</td><td id="{tYZ" class="">Cảm biến áp suất</td><td id="ZJEf" class="">Analog</td><td id="&gt;dMM" class="">10–50 Hz</td><td id="gbXE" class="">±1% FS</td><td id="^Wif" class="">kiểm soát áp, phát hiện surge</td><td id="^T@P" class="">derate, Protective nếu vượt hard</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80fc-aba7-d52890c9ba26"><td id="jbC|" class="">P_RIPPLE (tính toán)</td><td id="{tYZ" class="">từ P_H2</td><td id="ZJEf" class="">số</td><td id="&gt;dMM" class="">10–50 Hz</td><td id="gbXE" class="">—</td><td id="^Wif" class="">cấm boost khi dao động áp cao</td><td id="^T@P" class="">cấm boost, derate</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8080-bbec-cc261fd33ac0"><td id="jbC|" class="">WL (mức nước)</td><td id="{tYZ" class="">phao/siêu âm/cảm biến mức</td><td id="ZJEf" class="">Digital/Analog</td><td id="&gt;dMM" class="">1–5 Hz</td><td id="gbXE" class="">±5% mức</td><td id="^Wif" class="">cấm boost khi thiếu nước</td><td id="^T@P" class="">Degraded hoặc shutdown có kiểm soát</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80b5-9c71-f58935275270"><td id="jbC|" class="">COND (tuỳ chọn)</td><td id="{tYZ" class="">cảm biến độ dẫn</td><td id="ZJEf" class="">Analog</td><td id="&gt;dMM" class="">0,2–1 Hz</td><td id="gbXE" class="">±5–10%</td><td id="^Wif" class="">đánh giá chất lượng nước, 
derate theo bậc</td><td id="^T@P" class="">Degraded, yêu cầu thay nước</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80dd-a3dc-c2bce833eca1"><td id="jbC|" class="">H2_LEAK (khuyến nghị)</td><td id="{tYZ" class="">cảm biến H2</td><td id="ZJEf" class="">Digital/Analog</td><td id="&gt;dMM" class="">1–10 Hz</td><td id="gbXE" class="">theo ISO/IEC</td><td id="^Wif" class="">an toàn rò rỉ</td><td id="^T@P" class="">Safety trip độc lập</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8027-a9ba-f45941e38b69"><td id="jbC|" class="">DOOR/INTERLOCK</td><td id="{tYZ" class="">công tắc</td><td id="ZJEf" class="">Digital</td><td id="&gt;dMM" class="">10–100 Hz</td><td id="gbXE" class="">—</td><td id="^Wif" class="">liên động an toàn</td><td id="^T@P" class="">Safety trip</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8055-b907-cab62c2b5b73"><td id="jbC|" class="">FAN_PUMP_FB</td><td id="{tYZ" class="">tach/feedback</td><td id="ZJEf" class="">Digital</td><td id="&gt;dMM" class="">10–50 Hz</td><td id="gbXE" class="">—</td><td id="^Wif" class="">xác nhận làm mát hoạt động</td><td id="^T@P" class="">cấm boost, 
derate</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80d4-9d15-df4bc6a2d06e"><td id="jbC|" class="">E_STOP</td><td id="{tYZ" class="">nút dừng khẩn</td><td id="ZJEf" class="">Digital</td><td id="&gt;dMM" class="">100 Hz</td><td id="gbXE" class="">—</td><td id="^Wif" class="">cắt an toàn</td><td id="^T@P" class="">cắt enable lập tức</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-806d-b6ed-e5382169c705"/></div><div style="display:contents" dir="auto"><h1 id="2eac5e6f-95bd-80ae-9876-cee1c41a504b" class=""><strong>2) Bảng ngưỡng vận hành (Cruise / Boost / Degraded) + phản ứng hệ thống</strong></h1></div><div style="display:contents" dir="auto"><blockquote id="2eac5e6f-95bd-808e-bdc5-d8d12eeec420" class="">Lưu ý quan trọng để “đứng hồ sơ”: các số dưới đây là <strong>giá trị cấu hình mục tiêu</strong> (design targets) cho mô-đun ~1 kW. 
Khi chốt hoá học (PEM/AEM/kiềm) và dữ liệu chạy dài hạn, bạn sẽ <strong>điều chỉnh dải</strong>.</blockquote></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-80c8-b0ac-fd0c8bff289f" class=""><strong>2.1 Ngưỡng nhiệt</strong></h2></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-80c3-b5fb-f08abdff1710" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8083-a511-c5fe486c2680"><th id="_W^c" class="simple-table-header-color simple-table-header"><strong>Tham số</strong></th><th id="IF_k" class="simple-table-header-color simple-table-header"><strong>Cruise</strong></th><th id="gdkV" class="simple-table-header-color simple-table-header"><strong>Boost (được phép)</strong></th><th id="Ht:A" class="simple-table-header-color simple-table-header"><strong>Degraded</strong></th><th id="gE&lt;s" class="simple-table-header-color simple-table-header"><strong>Phản ứng hệ thống</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8009-9cb1-d55a1e1df78e"><td id="_W^c" class="">Nhiệt độ trung bình T_avg</td><td id="IF_k" class="">58–65°C</td><td id="gdkV" class="">chỉ khi T_avg ≤ (T_soft − 2°C)</td><td id="Ht:A" class="">50–60°C</td><td id="gE&lt;s" class="">vượt T_soft → derate theo bậc; 
vượt T_hard → Protective</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80c1-b1ad-edc1475fbbe2"><td id="_W^c" class="">Nhiệt độ cực đại T_max</td><td id="IF_k" class="">T_hard = 72–78°C (tuỳ profile)</td><td id="gdkV" class="">cấm nếu gần T_hard</td><td id="Ht:A" class="">—</td><td id="gE&lt;s" class="">T ≥ T_hard → ramp-down + lockout nếu lặp</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80e3-b2aa-ee363410331b"><td id="_W^c" class="">Gradient nhiệt ΔT</td><td id="IF_k" class="">≤3–5°C</td><td id="gdkV" class="">phải ≤ (ΔT_soft − margin)</td><td id="Ht:A" class="">≤2–4°C</td><td id="gE&lt;s" class="">ΔT vượt soft → cấm boost; 
vượt hard → Protective</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80f9-9d5b-da7dc3d2aa93"><td id="_W^c" class="">Tốc độ tăng nhiệt dT/dt</td><td id="IF_k" class="">≤0,6–1,0°C/phút</td><td id="gdkV" class="">chỉ khi dT/dt thấp</td><td id="Ht:A" class="">≤0,5°C/phút</td><td id="gE&lt;s" class="">dT/dt cao → kết thúc boost + cooldown</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8053-9575-cf2e055dbfac" class=""><strong>2.2 Ngưỡng điện – công suất</strong></h2></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-80e1-9214-c6b41f70d588" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80a0-99cd-cb3c1da8e647"><th id="td\A" class="simple-table-header-color simple-table-header"><strong>Tham số</strong></th><th id="RGri" class="simple-table-header-color simple-table-header"><strong>Cruise</strong></th><th id="PRqv" class="simple-table-header-color simple-table-header"><strong>Boost</strong></th><th id="ftcQ" class="simple-table-header-color simple-table-header"><strong>Degraded</strong></th><th id="cExa" class="simple-table-header-color simple-table-header"><strong>Phản ứng hệ thống</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80f6-a660-c9433a95b343"><td id="td\A" class="">Công suất P_in</td><td id="RGri" class="">0,8–1,0 kW</td><td id="PRqv" class="">1,2–2,0 kW (tuỳ profile)</td><td id="ftcQ" class="">0,3–0,8 kW</td><td id="cExa" class="">boost chỉ theo “ngân sách” và điều kiện</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8083-910b-eac02db8ece0"><td id="td\A" class="">Dòng I_stack</td><td id="RGri" class="">8–15 A</td><td id="PRqv" class="">18–30 A</td><td id="ftcQ" class="">3–12 A</td><td id="cExa" class="">hard clamp khi vượt I_hard</td></tr></div><div style="display:contents" dir="ltr"><tr i
d="2eac5e6f-95bd-80fb-8415-dd69d2d97852"><td id="td\A" class="">Giới hạn dI/dt</td><td id="RGri" class="">≤0,3–0,6 A/ms</td><td id="PRqv" class="">bắt buộc</td><td id="ftcQ" class="">bắt buộc</td><td id="cExa" class="">vượt → gate driver/MCU không cho phép</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-806e-8f5d-df81e31e1761"><td id="td\A" class="">Ripple dòng RMS</td><td id="RGri" class="">≤1–3%</td><td id="PRqv" class="">≤2–4%</td><td id="ftcQ" class="">≤2%</td><td id="cExa" class="">ripple cao → đổi dạng sóng / giảm I</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-809f-8d12-c59af0768e44" class=""><strong>2.3 Ngưỡng khí</strong></h2></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-801f-852c-e00de35b3caf" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8021-94fc-fce4615e8cb0"><th id="f^bQ" class="simple-table-header-color simple-table-header"><strong>Tham số</strong></th><th id="ZMe~" class="simple-table-header-color simple-table-header"><strong>Cruise</strong></th><th id="z=;X" class="simple-table-header-color simple-table-header"><strong>Boost</strong></th><th id="V{nF" class="simple-table-header-color simple-table-header"><strong>Degraded</strong></th><th id="GkGt" class="simple-table-header-color simple-table-header"><strong>Phản ứng hệ thống</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80bb-8d41-d726edd3b21c"><td id="f^bQ" class="">Áp suất P_H2</td><td id="ZMe~" class="">1,2–3,0 bar</td><td id="z=;X" class="">chỉ khi P còn headroom</td><td id="V{nF" class="">1,0–2,5 bar</td><td id="GkGt" class="">vượt P_soft → derate; 
vượt P_hard → Protective</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80c5-98e4-c83c88c309e8"><td id="f^bQ" class="">Ripple áp suất P_ripple</td><td id="ZMe~" class="">≤2–3%</td><td id="z=;X" class="">≤2–3%</td><td id="V{nF" class="">≤2%</td><td id="GkGt" class="">ripple cao → cấm boost + giảm dòng</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8085-8d75-c3f5fce26a1b"><td id="f^bQ" class="">dP/dt</td><td id="ZMe~" class="">giới hạn theo profile</td><td id="z=;X" class="">chặt hơn</td><td id="V{nF" class="">chặt</td><td id="GkGt" class="">surge → giảm dòng ngay</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8024-bbb4-cc3e03d28a75" class=""><strong>2.4 Ngưỡng nước</strong></h2></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-8066-a608-d81af76eece7" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8003-b451-d716aa6800a7"><th id="xs@R" class="simple-table-header-color simple-table-header"><strong>Tham số</strong></th><th id="T=@X" class="simple-table-header-color simple-table-header"><strong>Cruise</strong></th><th id="E]]r" class="simple-table-header-color simple-table-header"><strong>Boost</strong></th><th id="Bg?Z" class="simple-table-header-color simple-table-header"><strong>Degraded</strong></th><th id="~Gj[" class="simple-table-header-color simple-table-header"><strong>Phản ứng hệ thống</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80ef-b668-d5d6ed99e81f"><td id="xs@R" class="">Mức nước WL</td><td id="T=@X" class="">≥35–40%</td><td id="E]]r" class="">≥55–60%</td><td id="Bg?Z" class="">≥25–35%</td><td id="~Gj[" class="">WL thấp → cấm boost, derate; 
WL_crit → shutdown có kiểm soát</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-801e-8cb5-e8c5b1c454b8"><td id="xs@R" class="">Độ dẫn COND (tuỳ chọn)</td><td id="T=@X" class="">theo band</td><td id="E]]r" class="">phải tốt hơn Cruise</td><td id="Bg?Z" class="">band rộng hơn</td><td id="~Gj[" class="">vượt → giảm theo bậc + yêu cầu bảo trì</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8002-abb2-e4e4594c2c82" class=""><strong>2.5 Ngân sách Boost (điểm “khác biệt” để bảo vệ tuổi thọ)</strong></h2></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-80a8-8075-dee87190a80c" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8067-9617-ff5692985d5b"><th id="p^H&gt;" class="simple-table-header-color simple-table-header"><strong>Chỉ tiêu</strong></th><th id="VeGf" class="simple-table-header-color simple-table-header"><strong>Lab</strong></th><th id="&lt;fze" class="simple-table-header-color simple-table-header"><strong>Công nghiệp</strong></th><th id="RMDw" class="simple-table-header-color simple-table-header"><strong>Hàng hải-đảo</strong></th><th id="U|nE" class="simple-table-header-color simple-table-header"><strong>Phản ứng hệ thống</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8088-b3e7-ef93ff3bc4cc"><td id="p^H&gt;" class="">t_boost_max (mỗi lần)</td><td id="VeGf" class="">180 s</td><td id="&lt;fze" class="">120 s</td><td id="RMDw" class="">60–90 s</td><td id="U|nE" class="">hết thời gian → bắt buộc cooldown</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8058-8d32-cec2dd10d6df"><td id="p^H&gt;" class="">cooldown tối thiểu</td><td id="VeGf" class="">3–5 phút</td><td id="&lt;fze" class="">5–10 phút</td><td id="RMDw" class="">10–15 phút</td><td id="U|nE" class="">trong cooldown: cấm boost</td></tr></div><div s
tyle="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80a3-8745-d834f32090d7"><td id="p^H&gt;" class="">số lần boost/giờ</td><td id="VeGf" class="">6</td><td id="&lt;fze" class="">3</td><td id="RMDw" class="">1–2</td><td id="U|nE" class="">vượt → cấm boost</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80c1-8317-dabb05bab8f9"><td id="p^H&gt;" class="">tổng boost/ngày</td><td id="VeGf" class="">30 phút</td><td id="&lt;fze" class="">10–15 phút</td><td id="RMDw" class="">5–8 phút</td><td id="U|nE" class="">vượt → cấm boost đến hết ngày</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8035-a351-e7879c86b256"><td id="p^H&gt;" class="">số lỗi trước lockout</td><td id="VeGf" class="">3</td><td id="&lt;fze" class="">2</td><td id="RMDw" class="">1–2</td><td id="U|nE" class="">lặp lỗi → Lockout + yêu cầu kiểm tra</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80fd-8608-fda2ff960cd5"/></div><div style="display:contents" dir="auto"><h1 id="2eac5e6f-95bd-80e8-826b-ff56dfdd0b0e" class=""><strong>3) Bảng log và truy vết kiểm toán (audit-ready)</strong></h1></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80c5-998f-e4b5c1066a3d" class="">Mục tiêu của bảng này là: <strong>mỗi quyết định quan trọng đều có “vì sao” + “dữ liệu nào” + “ai/phiên bản nào”</strong>. 
Đây là thứ hội đồng/đăng kiểm yêu cầu khi bạn nói “hệ tự từ chối boost”.</p></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-801d-b18e-d8d00e7f5581" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80c4-8cf0-e1fe17838a80"><th id="LH|[" class="simple-table-header-color simple-table-header"><strong>Sự kiện/Quyết định</strong></th><th id="Bt;d" class="simple-table-header-color simple-table-header"><strong>Bắt buộc lưu trường dữ liệu</strong></th><th id="M[?f" class="simple-table-header-color simple-table-header"><strong>Tần suất</strong></th><th id="ok:U" class="simple-table-header-color simple-table-header"><strong>Vì sao hội đồng cần</strong></th><th id="PjDG" class="simple-table-header-color simple-table-header"><strong>Thời gian lưu</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80a9-8bcc-c54d5ec198a2"><td id="LH|[" class="">Chuyển mode (Cruise/Boost/Degraded/Protective/Lockout)</td><td id="Bt;d" class="">timestamp; mode_from; mode_to; reason_code; snapshot(T_avg, ΔT, dT/dt, P, P_ripple, I, V, R_eq, dR/dt, WL, Cond); firmware_hash</td><td id="M[?f" class="">mỗi lần</td><td id="ok:U" class="">chứng minh quyết định có căn cứ đo được</td><td id="PjDG" class="">≥12–24 tháng</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8054-83dc-ed70eddba816"><td id="LH|[" class="">Cấp Boost / Từ chối Boost</td><td id="Bt;d" class="">boost_request_id; decision(allow/deny); violated_conditions list; margins; boost_budget_remaining; cooldown_state</td><td id="M[?f" class="">mỗi lần</td><td id="ok:U" class="">chứng minh “refusal logic”</td><td id="PjDG" class="">≥12–24 tháng</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-807b-9622-c0fdbf0331ed"><td id="LH|[" class="">Trip/Protective</td><td id="Bt;d" class="">trip_type; sensor_causing; threshold; pre-trip trace 10–30 s (I,V,T,P); 
recovery sequence</td><td id="M[?f" class="">mỗi lần</td><td id="ok:U" class="">chứng minh an toàn và điều tra nguyên nhân</td><td id="PjDG" class="">≥24 tháng</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80da-893e-f623d173cf61"><td id="LH|[" class="">Derate theo bậc</td><td id="Bt;d" class="">derate_level; active_constraints; commanded_I; actual_I; duration</td><td id="M[?f" class="">1–5 Hz log gọn</td><td id="ok:U" class="">chứng minh giảm tải êm, không “cắt sốc”</td><td id="PjDG" class="">≥6–12 tháng</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80bc-8b00-e77e43d8b0d5"><td id="LH|[" class="">Drift/suy giảm</td><td id="Bt;d" class="">R_eq trend; dR/dt; D_index (nếu dùng); health_state</td><td id="M[?f" class="">1 lần/giờ + khi vượt ngưỡng</td><td id="ok:U" class="">chứng minh kiểm soát tuổi thọ</td><td id="PjDG" class="">≥24 tháng</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-801f-8e3d-c01fbbf166a1"><td id="LH|[" class="">Thay đổi cấu hình ngưỡng</td><td id="Bt;d" class="">param_name; old/new; user_role; auth_method; reason; ticket_id</td><td id="M[?f" class="">mỗi lần</td><td id="ok:U" class="">chống “tinh chỉnh lén” để đẹp số</td><td id="PjDG" class="">≥24 tháng</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8025-9a2c-deaab47dde7f"><td id="LH|[" class="">Cập nhật firmware</td><td id="Bt;d" class="">version; hash; signed_by; rollback_protect; change_log</td><td id="M[?f" class="">mỗi lần</td><td id="ok:U" class="">traceability theo IEC 61508/62443</td><td id="PjDG" class="">≥24 tháng</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-803f-8f22-eb867c05bb2b"><td id="LH|[" class="">Mất cảm biến / plausibility fail</td><td id="Bt;d" class="">sensor_id; fail_mode; 
fallback_action</td><td id="M[?f" class="">mỗi lần</td><td id="ok:U" class="">chứng minh fail-safe</td><td id="PjDG" class="">≥24 tháng</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8027-9ff3-f6a7cddcff77" class=""><strong>Quy ước reason_code (bắt buộc chuẩn hoá):</strong></p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80a1-afbd-effa7a563632" class="">Ví dụ: DENY_BOOST_T_GRADIENT, DERATE_P_RIPPLE, LOCKOUT_REPEAT_TRIP, … để đọc log là hiểu ngay.</p></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80fc-b4d5-c99c887c6d90"/></div><div style="display:contents" dir="auto"><h1 id="2eac5e6f-95bd-8069-ac3f-ec4dfc3053c7" class=""><strong>4) “Mô tả mạch power stage” đủ để giao thiết kế PCB (mức khối + ràng buộc layout)</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8093-bd73-ea1e423a055d" class=""><strong>4.1 Khối đầu vào (Front-End)</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80cc-9129-d96e73dc9675" class=""><strong>Mục tiêu:</strong> bảo vệ bus, giảm nhiễu, 
không cho “đột biến nguồn” đánh vào stack.</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80b0-b44d-c6a934d7d18d" class="bulleted-list"><li style="list-style-type:disc">Bảo vệ đảo cực: MOSFET “ideal diode” (ưu tiên) hoặc diode + cầu chì</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80fd-924d-cd74bc277bbe" class="bulleted-list"><li style="list-style-type:disc">Hạn dòng khởi động: mạch soft-start (MOSFET + driver) hoặc NTC (nếu chấp nhận tổn hao)</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80bd-984b-f41d4dc92a13" class="bulleted-list"><li style="list-style-type:disc">TVS: chọn theo bus 48/96V và kịch bản surge (tính công suất xung)</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-808c-aa5b-fc4e39545b90" class="bulleted-list"><li style="list-style-type:disc">Lọc EMI đầu vào: cấu hình π (C–L–C) với tụ film đặt sát vòng dòng lớn</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-807e-9e6e-c9b83add4556" class=""><strong>Ràng buộc layout bắt buộc:</strong></p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80dc-85a4-e229e03c2ae7" class="bulleted-list"><li style="list-style-type:disc">vòng dòng công suất (MOSFET-inductor-cap) phải <strong>ngắn nhất có thể</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80e4-b3f3-e38b88c9c40a" class="bulleted-list"><li style="list-style-type:disc">mass công suất và mass tín hiệu phải tách, 
chỉ nối tại <strong>một điểm sao</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ab-878b-d0f379aee6ae" class="bulleted-list"><li style="list-style-type:disc">đặt vị trí dự phòng snubber/RC để tinh chỉnh khi test EMC</li></ul></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8037-a97c-c1e4cc3422af" class=""><strong>4.2 Topology công suất</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80fc-a205-dfb4bb83ba18" class=""><strong>Lựa chọn topology:</strong></p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-806a-9b0b-c5839d0da33d" class="bulleted-list"><li style="list-style-type:disc">Nếu điện áp stack luôn thấp hơn bus: <strong>buck đồng bộ</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-806d-9f20-f8f2c6eb9713" class="bulleted-list"><li style="list-style-type:disc">Nếu điện áp stack có thể gần/vượt bus theo cấu hình: <strong>buck-boost 4 công tắc</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-809e-9260-cac10d55cd94" class=""><strong>Khối chính:</strong></p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-800b-a624-c378bab35420" class="bulleted-list"><li style="list-style-type:disc">MOSFET công suất (2 cái cho buck; 
4 cái cho buck-boost)</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80d9-8b06-eb23c8bcb703" class="bulleted-list"><li style="list-style-type:disc">Gate driver có:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ec-beeb-cb3830905462" class="bulleted-list"><li style="list-style-type:circle">điều khiển dead-time</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8053-8e50-c0a71b17df48" class="bulleted-list"><li style="list-style-type:circle">điều khiển tốc độ cạnh (slew-rate) để kìm dI/dt và EMI</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80cf-af67-d8a080601a03" class="bulleted-list"><li style="list-style-type:circle">UVLO + fault flag</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-801e-8836-cdc2b3f00019" class="bulleted-list"><li style="list-style-type:disc">Inductor công suất: dòng bão hoà phải &gt; 
I_boost + biên ripple</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8035-83cf-c660a7747efd" class="bulleted-list"><li style="list-style-type:disc">Tụ đầu ra: phối hợp điện phân low-ESR + film để dập xung nhanh</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80c4-8a60-edffb0cc65b8" class="bulleted-list"><li style="list-style-type:disc">Snubber RC/RCD: giảm ringing và stress MOSFET</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8060-b49d-f440272a4811" class=""><strong>Chỉ tiêu thiết kế nên ghi trong yêu cầu PCB:</strong></p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8063-84cd-c9671eb9aaf8" class="bulleted-list"><li style="list-style-type:disc">hiệu suất khối công suất: ≥94% ở Cruise, ≥92% ở Boost</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8014-939d-e5a0fd9ae4c8" class="bulleted-list"><li style="list-style-type:disc">nhiệt độ junction MOSFET ở Boost: không vượt giới hạn thiết kế (cần mô phỏng nhiệt + heatsink/thermal pad)</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-804f-a953-f8447d468ecb" class="bulleted-list"><li style="list-style-type:disc">ripple dòng RMS: theo profile (thường 1–3% Cruise)</li></ul></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-800b-97d5-d294ce836b5b" class=""><strong>4.3 Đo dòng (phần “không được sai”)</strong></h2></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-807d-affc-c470a97fcc0d" class="bulleted-list"><li style="list-style-type:disc">Phương án A (ưu tiên điều khiển chính xác): <strong>shunt mΩ + khuếch đại đo dòng + ADC</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80b4-8cf8-fbf8ea40cccc" class="bulleted-list"><li style="list-style-type:disc">Phương án B (cách ly, 
dễ triển khai): <strong>Hall-effect</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8069-ab25-fc724a4dc4dc" class=""><strong>Ràng buộc:</strong> băng thông đo phải đủ cho vòng dòng (ít nhất vài kHz), có lọc analog chống aliasing.</p></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80bd-8b00-da466d7c87b9"/></div><div style="display:contents" dir="auto"><h1 id="2eac5e6f-95bd-8070-b0fb-f9270f201a8e" class=""><strong>5) So sánh định lượng: IKONOMY nguyên bản vs AMOS-IKONOMY vs SOTA (viết kiểu “không bị bắt bẻ”)</strong></h1></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-801f-be5d-f5cd946190f5" class="">Bạn chỉ được phép viết theo 2 lớp: <strong>(i) số đã đo</strong>, <strong>(ii) mục tiêu thiết kế kèm kế hoạch chứng minh</strong>.</p></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-80bd-9c72-f35fd6b93efa" class=""><strong>5.1 KPI vận hành (cái SOTA hay yếu)</strong></h2></div><div style="display:contents" dir="ltr"><table id="2eac5e6f-95bd-8024-9e15-ef207f214cd2" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80fb-b8ea-fc7b1f62ba18"><th id="ynCi" class="simple-table-header-color simple-table-header"><strong>Chỉ tiêu</strong></th><th id="ygC&lt;" class="simple-table-header-color simple-table-header"><strong>IKONOMY nguyên bản (chưa có AMOS)</strong></th><th id="DPvu" class="simple-table-header-color simple-table-header"><strong>AMOS-IKONOMY (mục tiêu thiết kế)</strong></th><th id="{;m;" class="simple-table-header-color simple-table-header"><strong>SOTA thương mại (điển hình)</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-800d-9fbd-cc5a1dd73423"><td id="ynCi" class="">Uptime</td><td id="ygC&lt;" class="">90–94% (thường dao động)</td><td id="DPvu" class="">≥98%</td><td id="{;m;" class="">92–97% (tuỳ hệ, 
tuỳ môi trường)</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80a8-8c74-ceb19c84fd85"><td id="ynCi" class="">Trip/1000 giờ</td><td id="ygC&lt;" class="">5–15</td><td id="DPvu" class="">≤1–3</td><td id="{;m;" class="">2–10</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-8093-8f2b-d0667505c46a"><td id="ynCi" class="">MTBC (giờ)</td><td id="ygC&lt;" class="">100–300</td><td id="DPvu" class="">500–1500</td><td id="{;m;" class="">200–800</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80ee-9d29-fb79368b4039"><td id="ynCi" class="">Can thiệp/tuần</td><td id="ygC&lt;" class="">2–10</td><td id="DPvu" class="">≤1</td><td id="{;m;" class="">1–5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2eac5e6f-95bd-80be-9ef6-c3ac7555a20e"><td id="ynCi" class="">Boost “an toàn có audit”</td><td id="ygC&lt;" class="">thường không chuẩn hoá</td><td id="DPvu" class="">có (ngân sách + log)</td><td id="{;m;" class="">thường không có / không cho phép</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><blockquote id="2eac5e6f-95bd-80d4-961c-c4c7fac6ad3b" class="">Lưu ý: “SOTA điển hình” biến thiên rất lớn theo hãng và ứng dụng. Khi nộp hồ sơ, bạn nên ghi “khoảng tham chiếu thị trường” và kèm test plan của mình.</blockquote></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-80f2-9ded-efd4743719a3" class=""><strong>5.2. 
LCOH proxy (chỉ số so sánh nhanh, không thay thế LCA đầy đủ)</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8014-bc91-eb1b5b58078f" class="">Để so sánh các phương án thiết kế và vận hành <strong>khi chưa có phân tích vòng đời (LCA) hoàn chỉnh</strong>, sử dụng chỉ số <strong>LCOH proxy</strong> với công thức đã được chuẩn hóa, dễ hiểu và dễ kiểm toán.</p></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8012-a12a-c54331399f9e" class=""><strong>Định nghĩa sản lượng hiệu dụng</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80cc-b251-cdc3ddaf117b" class="">$$</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-808c-b49f-f3cc941000be" class="">Q_{eff}=Q_{H2}\cdot U</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8093-9171-debdcac41da3" class="">$$</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-803f-84a2-e61e3bc088ac" class="">Trong đó:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8053-b04d-d75e007b692c" class="bulleted-list"><li style="list-style-type:disc">$Q_{H2}$: sản lượng hydro danh định theo giờ (đo thực tế, 
tại điều kiện chuẩn đã khai báo).</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80fe-b9cf-eedb57990f51" class="bulleted-list"><li style="list-style-type:disc">$U$: uptime vận hành (tỷ lệ thời gian hệ thống tạo hydro hợp lệ).</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-801d-9eb0-e5836bfc62f6" class=""><strong>Công thức LCOH proxy</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8081-9efc-e9c132771521" class="">$$</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80fe-a9c8-c0da75a17e06" class="">LCOH_{proxy}=\frac{C_{elec,h}+C_{cap,h}+C_{maint,h}}{Q_{eff}}</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8083-97f6-d948c73d0aa9" class="">$$</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8001-b100-f3d58a21d43c" class="">Với các thành phần chi phí:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80a7-b273-eb7ee675a49d" class="bulleted-list"><li style="list-style-type:disc">$C_{elec,h}=P_{in}\cdot c_{kWh}$<div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8042-b850-ed5530a5df42" class="">(chi phí điện theo giờ, từ công suất điện vào và giá điện)</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80bf-aa98-d22af51de5db" class="bulleted-list"><li style="list-style-type:disc">$C_{cap,h}=\frac{CAPEX}{Life_h}$<div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80ab-b522-c5f0f19619b7" class="">(chi phí khấu hao theo giờ, 
dựa trên tuổi thọ hữu dụng thực tế)</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80f6-b89d-cdce6be3910d" class="bulleted-list"><li style="list-style-type:disc">$C_{maint,h}=\frac{OPEX_{year}}{8760}$<div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-807d-a61a-f7873770d4c0" class="">(chi phí vận hành và bảo trì quy đổi theo giờ)</p></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8058-be8c-dd692bbea95c" class=""><strong>Cơ chế AMOS làm giảm LCOH proxy (có thể kiểm toán)</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8097-b2af-d28f20a8db15" class="">AMOS làm giảm $LCOH_{proxy}$ thông qua ba cơ chế <strong>định lượng và kiểm chứng được</strong>:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-8029-8d9d-cf1e092e0d78" class="numbered-list" start="1"><li><strong>Tăng uptime ($U$)</strong><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80f3-9bbd-caf009504f6a" class="bulleted-list"><li style="list-style-type:disc">Giảm trip và dừng ngoài kế hoạch.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8032-90a5-e7ad42897ab0" class="bulleted-list"><li style="list-style-type:disc">Làm tăng trực tiếp $Q_{eff}$ (mẫu số).</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-80c8-a046-d534a7bf9fc0" class="numbered-list" start="2"><li><strong>Kéo dài tuổi thọ hữu dụng ($Life_h$)</strong><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8075-aa7c-c6b55a9eb289" class="bulleted-list"><li style="list-style-type:disc">Cấm boost sai điều kiện.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8060-b177-cf5689c7cd76" class="bulleted-list"><li style="list-style-type:disc">Giảm tốc độ suy giảm vật liệu.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8057-9602-f489269f336b" c
lass="bulleted-list"><li style="list-style-type:disc">Làm giảm $C_{cap,h}$ theo thời gian.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-8070-9fff-e920fb3d74c1" class="numbered-list" start="3"><li><strong>Giảm can thiệp và chi phí bảo trì</strong><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80b8-b9a4-c0a54f120016" class="bulleted-list"><li style="list-style-type:disc">Derate sớm thay cho shutdown.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8082-b80f-f2d9e1a1f409" class="bulleted-list"><li style="list-style-type:disc">Giảm số lần can thiệp thủ công và downtime.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80fe-b2ab-d5b5c8e7af85" class="bulleted-list"><li style="list-style-type:disc">Làm giảm $C_{maint,h}$ và chi phí ẩn do dừng máy.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8086-97a1-f22056df820b" class="">LCOH proxy <strong>không dùng để thay thế LCOH chuẩn</strong>, nhưng là công cụ hợp lệ để:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8077-aa8c-de8dce5425dd" class="bulleted-list"><li style="list-style-type:disc">so sánh phương án thiết kế,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80bc-a44f-c3669b7fe94f" class="bulleted-list"><li style="list-style-type:disc">đánh giá tác động của logic điều khiển lên chi phí vòng đời,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8085-b45f-e7b57524f0a9" class="bulleted-list"><li style="list-style-type:disc">trình bày rõ lợi thế vận hành của AMOS trong hồ sơ kỹ thuật.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-800c-8352-d4dab9362c8c" class="">Chỉ số này phản ánh đúng triết lý của AMOS: <strong>giảm chi phí hydro bằng kiểm soát vận hành và suy giảm</strong>, 
không bằng tối ưu thông số danh định ngắn hạn.</p></div><div style="display:contents" dir="auto"><h1 id="2eac5e6f-95bd-80a9-a9ea-f2d498fc2baa" class=""><strong>6) Có đạt chuẩn khắt khe nhất và vượt SOTA không?”</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-80ed-a63c-fb54e60a9630" class=""><strong>6.1. 
Yêu cầu để được công nhận “đạt chuẩn khắt khe”</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8075-8cbe-d46be8235ab0" class="">Hệ thống <strong>có khả năng đáp ứng các chuẩn nghiêm ngặt</strong> nếu thiết kế và triển khai đầy đủ bốn trụ an toàn sau:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-802c-b3ff-ff6522e41486" class="numbered-list" start="1"><li><strong>An toàn điện / điện tử</strong><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8043-a23c-f521b25a4ffc" class="bulleted-list"><li style="list-style-type:disc">Bảo vệ quá áp, quá dòng, ngắn mạch.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8037-bf75-df8e0ec4d117" class="bulleted-list"><li style="list-style-type:disc">Cách ly, nối đất, và kiểm soát EMI/EMC theo chuẩn áp dụng.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-80a4-9e97-c4b8f203b5ba" class="numbered-list" start="2"><li><strong>An toàn chức năng (Functional Safety)</strong><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80f2-ab13-fa3ebff3b1c3" class="bulleted-list"><li style="list-style-type:disc">Tối thiểu có <strong>kênh an toàn độc lập</strong> với kênh điều khiển chính.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80b6-a246-d695a2508de3" class="bulleted-list"><li style="list-style-type:disc">Các trạng thái Protective/Lockout không phụ thuộc phần mềm điều khiển công suất.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-800c-86db-f89402edb710" class="numbered-list" start="3"><li><strong>An toàn hydro</strong><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8022-be85-c4abb5e0b601" class="bulleted-list"><li style="list-style-type:disc">Phát hiện rò rỉ, giám sát áp suất, 
interlock phần cứng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-806e-a921-ec7a71728766" class="bulleted-list"><li style="list-style-type:disc">Quy định rõ khu vực lắp đặt, thông gió, và trình tự dừng an toàn.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-80eb-ae8c-fe002128bafd" class="numbered-list" start="4"><li><strong>An ninh mạng công nghiệp (nếu có giám sát/điều khiển từ xa)</strong><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8052-bba0-ec1c00f7d199" class="bulleted-list"><li style="list-style-type:disc">Phân tách mạng điều khiển và mạng giám sát.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-808f-a097-db5bc31d051d" class="bulleted-list"><li style="list-style-type:disc">Cơ chế xác thực, ghi log truy cập, và cập nhật có kiểm soát.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80c2-b70b-ea6c017dd590" class=""><strong>Lưu ý thẩm định:</strong></p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80c2-8091-c3f45e23ac4e" class="">Việc “được công nhận đạt chuẩn” <strong>không dựa trên tuyên bố thiết kế</strong>, 
mà yêu cầu đầy đủ:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8017-acdc-fe9b521a5b96" class="bulleted-list"><li style="list-style-type:disc">kế hoạch thử nghiệm (test plan),</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8055-84e2-ceeaf8c55128" class="bulleted-list"><li style="list-style-type:disc">dữ liệu thử nghiệm thực tế,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8017-935a-d1a116f351ab" class="bulleted-list"><li style="list-style-type:disc">log vận hành và audit trail,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80da-a7b9-db018e7cebdd" class="bulleted-list"><li style="list-style-type:disc">ma trận truy vết: <strong>yêu cầu → thiết kế → kiểm thử → kết quả</strong>.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8066-ab2e-f2eed82f6c64" class="">Thiếu bất kỳ thành phần nào trong chuỗi này, hệ thống chỉ được xem là “có khả năng đáp ứng”, chưa phải “được chứng nhận”.</p></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-805c-8c7a-f85ef678c904" class=""><strong>6.2. 
Cách tiếp cận đúng khi tuyên bố “vượt SOTA”</strong></h2></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80f2-b077-ed0b649c6baa" class="bulleted-list"><li style="list-style-type:disc"><strong>Không nên</strong> tuyên bố vượt SOTA dựa trên một chỉ số đơn lẻ như hiệu suất L/kWh hoặc thông số danh định.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8007-98ca-e759cd54d97a" class="bulleted-list"><li style="list-style-type:disc"><strong>Có thể tuyên bố vượt SOTA</strong> ở các khía cạnh mà công nghệ hiện hành thường yếu hoặc khó chứng minh, 
bao gồm:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80a6-996c-eda3dd92d765" class="bulleted-list"><li style="list-style-type:circle">uptime vận hành dài hạn,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8059-9e39-d2b068225e9d" class="bulleted-list"><li style="list-style-type:circle">MTBC (Mean Time Between Correction),</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-804d-8db6-c2ca486b4bc4" class="bulleted-list"><li style="list-style-type:circle">tần suất can thiệp của con người,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8036-9aac-ca5fecb5bd94" class="bulleted-list"><li style="list-style-type:circle">chi phí vòng đời (LCOH thực tế),</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8061-a1d2-e0ed86b920d4" class="bulleted-list"><li style="list-style-type:circle">hồ sơ an toàn có thể kiểm toán.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80cb-b224-e0ff966beb00" class=""><strong>Điều kiện bắt buộc để tuyên bố hợp lệ:</strong></p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8092-82aa-f839ad35686f" class="bulleted-list"><li style="list-style-type:disc">vận hành dài hạn có kiểm soát (ví dụ 1.000 h / 3.000 h),</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ca-807a-fc542c87e407" class="bulleted-list"><li style="list-style-type:disc">dữ liệu log đầy đủ, liên tục,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8034-97f0-f00a3561d274" class="bulleted-list"><li style="list-style-type:disc">thống kê sự cố, 
can thiệp và suy giảm,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80a9-966c-cc67bcae2a0b" class="bulleted-list"><li style="list-style-type:disc">phương pháp đánh giá rõ ràng và có thể lặp lại.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80e2-be79-ca740720b75e" class="">Chỉ khi các điều kiện trên được đáp ứng, tuyên bố “vượt SOTA” mới có giá trị kỹ thuật và được hội đồng chấp nhận.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80bd-bb58-d2cad6e91743" class="">
</p></div><div style="display:contents" dir="auto"><h1 id="2eac5e6f-95bd-8067-9d53-d558b59c41cb" class=""><strong>KẾ HOẠCH TRIỂN KHAI AMOS-IKONOMY (2025–2032)</strong></h1></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-8057-b8ab-ea11e2d44cc0"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8015-9768-eadb3a8d95f1" class=""><strong>GIAI ĐOẠN 1 — CỐ ĐỊNH THIẾT KẾ &amp; CHỨNG MINH KỸ THUẬT CỐT LÕI</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8032-a408-fc165358c950" class=""><strong>(0–9 tháng | mục tiêu: “đứng vững về kỹ thuật”)</strong></p></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80bd-a7d2-e15f78a8723d" class=""><strong>1.1. Mục tiêu</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80a0-9b2d-d1d52db37a21" class="bulleted-list"><li style="list-style-type:disc">Khóa thiết kế <strong>AMOS-IKONOMY module 1 kW</strong> ở mức:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-807b-955b-e2216fdbc34f" class="bulleted-list"><li style="list-style-type:circle">vận hành ổn định,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80db-9a4a-c5d64cfa88e4" class="bulleted-list"><li style="list-style-type:circle">logic AMOS hoàn chỉnh,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ca-9bac-d1a6331d0e30" class="bulleted-list"><li style="list-style-type:circle">đủ dữ liệu để nói chuyện với hội đồng / đối tác nghiêm túc.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80f5-97dd-d2d8ab215698" class="bulleted-list"><li style="list-style-type:disc">Chuyển từ “thiết kế hợp lý” → <strong>thiết kế có chứng cứ</strong>.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80a9-b1be-dac3daddc6f1" class=""><strong>1.2. 
Việc phải làm (technical deliverables)</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-8011-b0dd-c11d036b6748" class="numbered-list" start="1"><li>Hoàn thiện <strong>bản thiết kế cuối (design freeze)</strong>:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-802f-98bb-c3a93ef73fc1" class="bulleted-list"><li style="list-style-type:disc">power stage (buck/buck-boost),</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8002-8089-c7c7778eb89e" class="bulleted-list"><li style="list-style-type:disc">sensing,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ef-8bec-c08de7d1c69a" class="bulleted-list"><li style="list-style-type:disc">firmware AMOS,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8060-bba9-c8243e648ab8" class="bulleted-list"><li style="list-style-type:disc">state machine đầy đủ (Cruise / Boost / Degraded / Protective / Lockout).</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-80fd-863b-e6da6e96e14a" class="numbered-list" start="2"><li>Chạy <strong>test dài hạn bắt buộc</strong>:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80fa-a9f4-c3fee5b8312c" class="bulleted-list"><li style="list-style-type:disc">1.000–3.000 giờ liên tục,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80b1-b3f2-e3bca4cba936" class="bulleted-list"><li style="list-style-type:disc">nguồn dao động ±15%,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80db-b5f0-cf1700646d51" class="bulleted-list"><li style="list-style-type:disc">mô phỏng điều kiện nóng/ẩm VN.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-80a3-96b9-ec813432b86b" class="numbered-list" start="3"><li>Thu thập <strong>log &amp; 
audit trail</strong>:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8026-a675-cf12aadb86d3" class="bulleted-list"><li style="list-style-type:disc">uptime,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80a0-b14f-dabd1bd936ca" class="bulleted-list"><li style="list-style-type:disc">số lần boost,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-807e-8c30-cd7e9ca89f4e" class="bulleted-list"><li style="list-style-type:disc">số lần từ chối boost,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80c5-b6b1-fcac9218f4ef" class="bulleted-list"><li style="list-style-type:disc">số lần derate,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80e9-b225-ed850e83efd4" class="bulleted-list"><li style="list-style-type:disc">không có “trip vô cớ”.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-806d-b42d-cda32a6b4a93" class=""><strong>1.3. KPI kỹ thuật cần đạt</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8063-8bec-fcd610e36bc1" class="bulleted-list"><li style="list-style-type:disc">Uptime ≥ <strong>97–98%</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80cc-95d6-e476c9280369" class="bulleted-list"><li style="list-style-type:disc">Trip ≤ <strong>1–3 lần / 1.000 giờ</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-802d-b10b-ed1a9e54e6ed" class="bulleted-list"><li style="list-style-type:disc">Boost hoạt động đúng “ngân sách” (không vượt)</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80c5-98e9-f458c13dcc99" class="bulleted-list"><li style="list-style-type:disc">Không hỏng stack sớm</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8028-89ed-c3f6571a594d" class=""><strong>1.4. 
Giá trị tạo ra</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8024-a6fe-fae3f10f7390" class="bulleted-list"><li style="list-style-type:disc">Chứng minh <strong>AMOS không phải lý thuyết</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80bc-bb71-d44952df9cd7" class="bulleted-list"><li style="list-style-type:disc">Có dữ liệu thật để:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80eb-90ec-ec60683a1ea8" class="bulleted-list"><li style="list-style-type:circle">xin tài trợ,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8099-88da-ddb3736ec4d8" class="bulleted-list"><li style="list-style-type:circle">gọi vốn seed,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80b7-a1f4-fc59042f8b7d" class="bulleted-list"><li style="list-style-type:circle">hoặc ký MoU pilot.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-8087-b186-fc2853824879"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8040-96e3-da8115546e29" class=""><strong>GIAI ĐOẠN 2 — PILOT THỰC ĐỊA (10–100 MODULE)</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80c8-8845-f3667fe0c68d" class=""><strong>(9–18 tháng | mục tiêu: “đứng vững trong thế giới thật”)</strong></p></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80d8-94f7-e24ad6878f92" class=""><strong>2.1. 
Mục tiêu</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8092-a9c9-c5b54c183547" class="bulleted-list"><li style="list-style-type:disc">Đưa AMOS-IKONOMY ra <strong>điều kiện sử dụng thật</strong>:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-808a-a6cb-d82810991313" class="bulleted-list"><li style="list-style-type:circle">cảng,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-808a-80be-d012f55b1d8d" class="bulleted-list"><li style="list-style-type:circle">khu công nghiệp nhỏ,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-802a-864d-fa257feebb79" class="bulleted-list"><li style="list-style-type:circle">đảo / off-grid,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-806a-bd3f-c2b69413c8d2" class="bulleted-list"><li style="list-style-type:circle">RES dao động.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8006-a811-c0b4eec327e4" class=""><strong>2.2. Quy mô</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80d9-897a-e32970a8be5c" class="bulleted-list"><li style="list-style-type:disc">10–100 module (10–100 kW)</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-801b-baad-f786a181b4eb" class="bulleted-list"><li style="list-style-type:disc">Triển khai phân tán (không gom 1 chỗ).</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8064-84df-d155b348f5e5" class=""><strong>2.3. 
Việc phải làm</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-8094-986c-d2bb710266af" class="numbered-list" start="1"><li>Chuẩn hóa:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-808d-8084-dbc4e4cf1f03" class="bulleted-list"><li style="list-style-type:disc">quy trình lắp đặt,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8046-bf41-d96f6294ded6" class="bulleted-list"><li style="list-style-type:disc">quy trình vận hành,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ec-8525-c24538725e57" class="bulleted-list"><li style="list-style-type:disc">quy trình bảo trì (SOP).</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-807f-9c39-e30ba4088d90" class="numbered-list" start="2"><li>Đo <strong>chi phí thực</strong>:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ea-93b6-d9e10bc44a68" class="bulleted-list"><li style="list-style-type:disc">điện / kg H₂,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8037-b4b5-ef85da616f60" class="bulleted-list"><li style="list-style-type:disc">thời gian can thiệp con người,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-809b-9228-fcfb9d1cc9d4" class="bulleted-list"><li style="list-style-type:disc">downtime thực tế.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-80bd-a8ba-ff619cf3f8d0" class="numbered-list" start="3"><li>Hoàn thiện <strong>hồ sơ chuẩn hóa</strong>:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ba-a352-fd9b3da61e0f" class="bulleted-list"><li style="list-style-type:disc">ISO 22734 (electrolyzer),</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80da-98d8-de46026202ec" class="bulleted-list"><li style="list-style-type:disc">IEC 61010/60204 (an toàn),</li></ul></div><div s
tyle="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80f0-8b8d-d44c4c001a44" class="bulleted-list"><li style="list-style-type:disc">chuẩn bị cho IEC 61508 (an toàn chức năng).</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-808a-9213-ce389f631d7f" class=""><strong>2.4. KPI kinh tế</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8039-80e9-e48bea4b236b" class="bulleted-list"><li style="list-style-type:disc">LCOH thực tế ≤ <strong>4–6 USD/kg</strong> (điện VN)</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8024-b703-d89512c978aa" class="bulleted-list"><li style="list-style-type:disc">MTBC ≥ <strong>500 giờ</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-802d-909e-c1a796744127" class="bulleted-list"><li style="list-style-type:disc">Nhân lực vận hành ≤ <strong>0,1–0,2 FTE / 100 kW</strong></li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8023-a40c-ff3187627830" class=""><strong>2.5. 
Giá trị tạo ra</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8038-b05d-cee1f431cce0" class="bulleted-list"><li style="list-style-type:disc">Chứng minh AMOS <strong>giảm OPEX thật</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8033-a888-e0340612cf69" class="bulleted-list"><li style="list-style-type:disc">Có case study đủ mạnh để:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80eb-b7c1-d1fbfc831c4a" class="bulleted-list"><li style="list-style-type:circle">bán hàng,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-802c-8eab-d52b55afcdb0" class="bulleted-list"><li style="list-style-type:circle">xin dự án lớn,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80e3-b1af-cad19b0e4704" class="bulleted-list"><li style="list-style-type:circle">nâng định giá công ty.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-8020-a47d-e31667f2c8ca"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8047-9450-f5afd46f5ef9" class=""><strong>GIAI ĐOẠN 3 — SẢN XUẤT CÔNG NGHIỆP NHỎ (1–10 MW)</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80fb-ac27-ca48f4d568e5" class=""><strong>(18–30 tháng | mục tiêu: “bắt đầu kiếm tiền thật”)</strong></p></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80e2-a236-e1fdd78aed70" class=""><strong>3.1. 
Mục tiêu</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-806b-815b-f758e9bf2dde" class="bulleted-list"><li style="list-style-type:disc">Chuyển từ pilot → <strong>doanh thu ổn định</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8038-a275-f2a1aa0c4b56" class="bulleted-list"><li style="list-style-type:disc">Chuẩn hóa sản xuất tại Việt Nam.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-809a-bbbb-edf5bad54f53" class=""><strong>3.2. Quy mô</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8085-91f5-dba85e5294c4" class="bulleted-list"><li style="list-style-type:disc">1–10 MW lắp đặt/năm<div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8063-9f57-c4ffcfa450bc" class="">(≈ 1.000–10.000 module/năm)</p></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8062-8a3b-f89da88c8b02" class=""><strong>3.3. Mô hình kinh doanh</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-807d-afd4-f731d810b7ce" class="bulleted-list"><li style="list-style-type:disc"><strong>Kết hợp 2 mô hình</strong>:<div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-80a3-9cbc-ceef9c89c0f3" class="numbered-list" start="1"><li>Bán module (CAPEX)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-800b-bd60-d69f89a079f7" class="numbered-list" start="2"><li>O&amp;M + AMOS software (recurring)</li></ol></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-803b-826c-f5ed5da13ba8" class=""><strong>3.4. 
Doanh thu ước tính (bảo thủ)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80be-92b2-dd40aa219412" class="bulleted-list"><li style="list-style-type:disc">1 MW:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80e9-ab2b-fe04ee605a44" class="bulleted-list"><li style="list-style-type:circle">Doanh thu thiết bị: ~1–3 triệu USD</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80c7-8f7a-c9c52fc2b9b5" class="bulleted-list"><li style="list-style-type:circle">Dịch vụ/O&amp;M: 0,2–0,5 triệu USD/năm</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8095-aeac-da1283955505" class="bulleted-list"><li style="list-style-type:disc">10 MW:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80d0-b696-f41194685a82" class="bulleted-list"><li style="list-style-type:circle">Doanh thu: <strong>10–30 triệu USD</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8030-903a-de9a0ac26fb8" class="bulleted-list"><li style="list-style-type:circle">Lợi nhuận gộp: <strong>25–40%</strong></li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80f4-bbc0-f1580dbb8c9d" class=""><strong>3.5. 
Giá trị tạo ra</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80b5-8fcc-df9b01b61be8" class="bulleted-list"><li style="list-style-type:disc">Dòng tiền thật.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8059-8178-ee366e0e6aac" class="bulleted-list"><li style="list-style-type:disc">Thoát khỏi “startup nghiên cứu”.</li></ul></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80a8-88dc-ff5ab0ad850a"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8059-8d97-c9c1ef93c44c" class=""><strong>GIAI ĐOẠN 4 — CỤM MW PHÂN TÁN &amp; H₂-AS-A-SERVICE</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8028-9e80-d2df322f50b5" class=""><strong>(30–48 tháng | mục tiêu: “ăn vào chuỗi giá trị”)</strong></p></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80fc-b35f-c42c16e03ab9" class=""><strong>4.1. Mục tiêu</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80dc-87d5-ee86373c9434" class="bulleted-list"><li style="list-style-type:disc">Không chỉ bán máy → <strong>bán hydro + dịch vụ</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80de-96fb-fe933cbc68e1" class="bulleted-list"><li style="list-style-type:disc">Định giá doanh nghiệp cao hơn (recurring revenue).</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80c0-8034-c6f43f1efb94" class=""><strong>4.2. 
Quy mô</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-803e-bc2c-cb43db699639" class="bulleted-list"><li style="list-style-type:disc">50–100 MW phân tán</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8072-93c5-dbbe89ebcc59" class="bulleted-list"><li style="list-style-type:disc">Ứng dụng:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8069-81d4-d84ca6502ce6" class="bulleted-list"><li style="list-style-type:circle">logistics,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8002-b501-f606633374cd" class="bulleted-list"><li style="list-style-type:circle">cảng,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80fd-ab36-dc4e4b36888f" class="bulleted-list"><li style="list-style-type:circle">công nghiệp vừa,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80db-83c2-ce790b3fc13d" class="bulleted-list"><li style="list-style-type:circle">đảo.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80d6-b85f-c582ea7260b8" class=""><strong>4.3. 
Doanh thu</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80e8-9985-f46d66a9c4bc" class="bulleted-list"><li style="list-style-type:disc">100 MW:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80b5-aa26-cd9048716775" class="bulleted-list"><li style="list-style-type:circle">Sản lượng: ~13.000 tấn H₂/năm</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80d7-9076-f341427ac686" class="bulleted-list"><li style="list-style-type:circle">Doanh thu: <strong>80–130 triệu USD/năm</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ce-bc22-eb7646040190" class="bulleted-list"><li style="list-style-type:circle">Lợi nhuận gộp: <strong>30–50 triệu USD/năm</strong> (nếu biên 2–4 USD/kg)</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80f1-b732-cbe5c4a08eef" class=""><strong>4.4. Giá trị tạo ra</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8098-bcf6-db6fa80e374d" class="bulleted-list"><li style="list-style-type:disc">AMOS trở thành <strong>hạ tầng</strong>, không còn là “thiết bị”.</li></ul></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80d2-a9bd-fb5ac43b062b"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8054-b464-f1397dc5dea2" class=""><strong>GIAI ĐOẠN 5 — SCALE LÊN GW &amp; XUẤT KHẨU</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-808b-85f8-dcee77c5b4d1" class=""><strong>(4–7 năm | mục tiêu: “significant toàn cầu”)</strong></p></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8061-9d94-d7464da8ff9d" class=""><strong>5.1. 
Mục tiêu</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-802e-bbf2-fe898013ecef" class="bulleted-list"><li style="list-style-type:disc">Xuất khẩu module + AMOS logic.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80f5-8912-f71192e4874b" class="bulleted-list"><li style="list-style-type:disc">Đánh vào thị trường:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80e5-82ec-e582a4a5ff2d" class="bulleted-list"><li style="list-style-type:circle">SEA,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-805a-bbf0-ff4b02427af9" class="bulleted-list"><li style="list-style-type:circle">Ấn Độ,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80b5-a089-dde0eb5e99d1" class="bulleted-list"><li style="list-style-type:circle">châu Phi,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80f8-83b9-f80afd56b30a" class="bulleted-list"><li style="list-style-type:circle">Mỹ Latinh.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80f3-bd3c-f50b253ac98f" class=""><strong>5.2. Quy mô</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8043-9ec9-f5b8f750106b" class="bulleted-list"><li style="list-style-type:disc">0,5–1 GW phân tán</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8063-9896-c3831988e1a1" class="bulleted-list"><li style="list-style-type:disc">Doanh thu tiềm năng: <strong>0,8–1,3 tỷ USD/năm</strong></li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80d9-beda-dc519f2a9b62" class=""><strong>5.3. 
Lợi thế cạnh tranh</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80e7-8abe-ecd9ba2e32e8" class="bulleted-list"><li style="list-style-type:disc">Uptime cao trong môi trường khó.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80a1-bb66-d82a95784a9a" class="bulleted-list"><li style="list-style-type:disc">Không cần đội kỹ sư dày.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80e4-a8bb-d8070ea29223" class="bulleted-list"><li style="list-style-type:disc">Audit + safety + cybersecurity sẵn sàng.</li></ul></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80b1-98c2-ee46656d8143"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-802a-bbfd-f3cbf9a6f4e9" class=""><strong>GIAI ĐOẠN 6 — MOAT DÀI HẠN (10+ NĂM)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80de-b016-cc9935d7476f" class=""><strong>6.1. Thứ giữ bạn không bị sao chép</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80b3-a359-daa05c9fe345" class="bulleted-list"><li style="list-style-type:disc">AMOS logic + audit trail + safety case.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8049-b6dd-ebfd0cb7471f" class="bulleted-list"><li style="list-style-type:disc">Dữ liệu vận hành tích lũy hàng triệu giờ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80a6-b3f7-d411dbba6677" class="bulleted-list"><li style="list-style-type:disc">Chuẩn hóa “how to run electrolyzer safely”.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-806f-9551-d287c311844f" class=""><strong>6.2. 
Định vị cuối</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8098-9abf-fdf521a92d7e" class="">AMOS-IKONOMY không chỉ là:</p></div><div style="display:contents" dir="auto"><blockquote id="2eac5e6f-95bd-80e4-ba3f-d70c16b0e4b9" class="">“máy điện phân nhỏ”</blockquote></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80ac-aa0f-c80710362a6e" class="">mà là:</p></div><div style="display:contents" dir="auto"><blockquote id="2eac5e6f-95bd-809e-9d3a-e0cc7da30333" class="">nền tảng vận hành hydro phân tán an toàn – bền – kiểm toán được</blockquote></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80e7-89d6-d46c8a2d1c82"/></div><div style="display:contents" dir="auto"><h1 id="2eac5e6f-95bd-8011-82a1-d947dc304162" class=""><strong>KẾT LUẬN THẲNG</strong></h1></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8099-aef3-e2f59f6ddb8f" class="bulleted-list"><li style="list-style-type:disc"><strong>Có, nó significant</strong> – không phải vì nhỏ hay lớn, mà vì <strong>nó scale được và giảm chi phí vòng đời ở nơi thị trường đang đau</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8003-92e1-edc06642112d" class="bulleted-list"><li style="list-style-type:disc"><strong>Tiền không nằm ở 1 kW</strong>, 
mà nằm ở:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-804c-aae0-f447e1d1ba77" class="bulleted-list"><li style="list-style-type:circle">100 MW → hàng chục triệu USD/năm,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-801c-8352-decf9259cb42" class="bulleted-list"><li style="list-style-type:circle">1 GW → hàng tỷ USD/năm.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80d0-988d-fee413b23691" class="bulleted-list"><li style="list-style-type:disc">AMOS là thứ biến “kỹ thuật tốt” thành <strong>doanh nghiệp lớn</strong>.</li></ul></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
