---
tags: [amos-general]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Thiết kế “AMOS-IKONOMY</title><style>
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
	
</style></head><body><article id="2eac5e6f-95bd-8059-9555-d3498d5a3f2e" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Thiết kế “AMOS-IKONOMY</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8099-86b7-e8d04a479b95" class=""><strong>0) Điểm xuất phát: IKONOMY “nguyên bản” là gì, và vì sao phải đổi</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8080-9788-f8f49b92f70c" class=""><strong>IKONOMY nguyên bản</strong> (theo mô tả bạn đã đưa và logic “Cannon”) là kiến trúc có 3 đặc trưng điển hình:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-803b-8804-f6652e4620ad" class="numbered-list" start="1"><li><strong>Chấp hành công suất kiểu PWM/đóng cắt</strong> để điều chỉnh dòng/áp cấp vào stack;</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-8024-aa02-c6e70f36814f" class="numbered-list" start="2"><li><strong>Điều khiển chủ yếu theo ngưỡng tức thời</strong> (quá dòng, quá nhiệt, quá áp…);</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-8045-852a-caf98cd3fbdf" class="numbered-list" start="3"><li><strong>Bảo vệ kiểu “cắt khẩn” (hard trip)</strong> và phần tối ưu hóa thường nằm ở thao tác người vận hành/thiết lập thủ công.</li></ol></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80ba-bde7-f2a5a5b70fda" class="">Vấn đề của trạng thái nguyên bản không nằm ở “không tạo được hydro”, mà nằm ở chỗ: <strong>hệ thống chưa có cơ chế bắt buộc để tránh vùng suy giảm không hồi phục</strong> (degradation cliff), và chưa có mô hình <strong>tách “đỉnh” khỏi “hiệu dụng”</strong>. Khi triển khai môi trường Việt Nam (nguồn dao động, bảo trì hạn chế, nhiệt/ẩm cao, rung/tilt, nước không lý tưởng), chính các “vùng biên” này làm chi phí vòng đời tăng mạnh.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80c4-9110-edfc3fc25b42" class=""><strong>AMOS-IKONOMY thay đổi cái gốc</strong>: không thay hóa học, nhưng <strong>đưa giới hạn vật lý + giới hạn vật liệu + giới hạn vận hành</strong> vào <strong>logic điều khiển bắt buộc</strong>. Kết quả là hệ thống có thể <strong>đẩy sát trần lâu hơn</strong> mà không rơi khỏi mép.</p></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-806b-87d2-ceed3c705c44"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8024-bbc7-e2ddfd9b863a" class=""><strong>1) Kiến trúc tổng thể (hệ liên hợp điện – nhiệt – khí – vật liệu)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-809a-909b-c13ddd0ac27f" class=""><strong>1.1 Sơ đồ khối (dạng hồ sơ kỹ thuật)</strong></h3></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2eac5e6f-95bd-8050-8e37-fbf0ea0bd83d" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">flowchart TB
  A[DC Input 48–96VDC] --&gt; B[Power Conditioning &amp; Protection]
  B --&gt; C[HV/LV Rails + Precharge + EMI/EMC Filter]
  C --&gt; D[Cannon Drive Stage&lt;br/&gt;Current-Controlled Switching Converter]
  D --&gt; E[Electrolysis Stack + Manifold]
  E --&gt; F[Thermal Mass + Heat Spreader + Cooling Loop]
  E --&gt; G[Gas Separation + Water Trap + Bubbler/Conditioning]
  G --&gt; H[H2 Output Regulation + Non-return + Relief]
  E --&gt; I[Water Management: Tank/Feed + Level + Conductivity]
  D --&gt; J[MCU/RT Controller (Lớp 2)]
  J --&gt; D
  K[AMOS Core (Lớp 3)] --&gt; J
  J --&gt; K
  L[Supervisory/SCADA/Deployment Policy (Lớp 4)] --&gt; K
  K --&gt; L
  M[Sensors: I,V,Tmulti,P,Flow,Leak,Level,Cond] --&gt; J
  M --&gt; K</code></pre></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8087-9fa6-e4ae58fb7c81" class=""><strong>1.2 Nguyên lý thiết kế bắt buộc</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8002-9810-dedcad8719c2" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều khiển theo dòng (current-mode) là biến chủ đạo</strong>: dòng quyết định tốc độ phản ứng và tốc độ suy giảm.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-804b-a933-db982c548aa3" class="bulleted-list"><li style="list-style-type:disc"><strong>Đa miền liên hợp</strong>: mọi lệnh dòng chỉ được phép nếu đồng thời thỏa <strong>nhiệt</strong>, <strong>khí/áp</strong>, <strong>nước</strong>, <strong>suy giảm vật liệu</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-803f-9a7c-e42e18246e76" class="bulleted-list"><li style="list-style-type:disc"><strong>Tách 2 phong bì</strong>:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8098-8ce0-c8396c667f34" class="bulleted-list"><li style="list-style-type:circle"><strong>Rated/Cruise</strong>: tối ưu sản lượng vòng đời, chạy 24/7.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8072-873f-d224cfecd295" class="bulleted-list"><li style="list-style-type:circle"><strong>Boost/Peak</strong>: tăng công suất ngắn hạn, bị chặn bởi luật nhiệt-khí-suy giảm.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-807a-82e7-fd48fa371032"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8074-9704-fb9260971cc0" class=""><strong>2) Đẩy “đỉnh” và “hiệu dụng”: định nghĩa mục tiêu kỹ thuật (không mơ hồ)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8069-bf44-c8977cbaa4a3" class=""><strong>2.1 Chỉ tiêu mục tiêu (có thể khóa thành spec)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80fa-bed3-ef7a448ef87a" class="bulleted-list"><li style="list-style-type:disc"><strong>Công suất danh định (Rated)</strong>: 1,0 kW liên tục.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-801e-a4b5-cbe93c1f5809" class="bulleted-list"><li style="list-style-type:disc"><strong>Công suất đỉnh (Boost)</strong>: 1,5–2,0 kW trong <strong>30–180 s</strong>, bắt buộc có <strong>cooldown</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8036-bf04-c48ff9f0796b" class="bulleted-list"><li style="list-style-type:disc"><strong>Uptime mục tiêu</strong>: ≥ 98% theo định nghĩa “sẵn sàng vận hành” (không tính thời gian bảo trì định kỳ).</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ca-bf0b-f7995f15e70a" class="bulleted-list"><li style="list-style-type:disc"><strong>Giảm chi phí vòng đời</strong>: mục tiêu 25–40% so với vận hành kiểu “cắt khẩn + canh máy” (giảm dừng ngoài kế hoạch + giảm thay thế sớm + giảm can thiệp).</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-804d-b328-dad476d73c2c" class="bulleted-list"><li style="list-style-type:disc"><strong>Tăng tuổi thọ hữu dụng</strong>: mục tiêu 1,5–2,0 lần so với chạy sát biên không kiểm soát (đạt bằng giảm sốc nhiệt, giảm dao động dòng, tránh vùng Tafel/cliff).</li></ul></div><div style="display:contents" dir="auto"><blockquote id="2eac5e6f-95bd-8091-bd30-c2f3d0453594" class="">Các con số này là<div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-804b-b316-c8b9c55a68e4" class=""><strong>mục tiêu thiết kế</strong></p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8070-b47a-cdca3c44f4d4" class=""><strong>báo cáo thử nghiệm</strong></p></div></blockquote></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-803b-88af-eae753feb8e6"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-800a-accb-d738ac6defec" class=""><strong>3) Khối nguồn vào và bảo vệ (Power Conditioning &amp; Protection)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8080-ac91-f757e1e7fa53" class=""><strong>3.1 Dải điện áp và dòng</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80b6-85d8-eb2164ffb460" class="bulleted-list"><li style="list-style-type:disc"><strong>Vin danh định</strong>: 48–96 VDC; <strong>dải cho phép</strong>: ±15%.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80e8-9ba0-d82eb76679d2" class="bulleted-list"><li style="list-style-type:disc"><strong>Iin_max</strong>: tính theo boost 2 kW @ 48 V → khoảng 42 A (chưa tính dự phòng).</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8053-8804-c0876d8e330a" class="bulleted-list"><li style="list-style-type:disc"><strong>Yêu cầu chịu dao động</strong>: sụt áp ngắn hạn, ripple nguồn, nhiễu do tải khác.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80d9-9e5f-f3ba41d2a350" class=""><strong>3.2 Bảo vệ bắt buộc (để đi chứng nhận nghiêm)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8069-a03a-ff0824353cfd" class="bulleted-list"><li style="list-style-type:disc"><strong>OVP/UVP</strong>: khóa mềm (derate) trước, khóa cứng sau nếu tiếp tục vi phạm.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-805e-b641-d1b7f13b2e53" class="bulleted-list"><li style="list-style-type:disc"><strong>Reverse polarity</strong>: bảo vệ phần cứng (ideal diode / MOSFET ORing).</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-806f-8a10-da911a850cc1" class="bulleted-list"><li style="list-style-type:disc"><strong>Inrush limiting + precharge</strong>: tránh sốc tụ và tránh “cúp nguồn dây chuyền”.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-802c-b036-da2bb1f973ff" class="bulleted-list"><li style="list-style-type:disc"><strong>Surge/ESD</strong>: TVS + LC filter + layout chuẩn EMC.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-808e-ac8f-e4d758e64bc4" class="bulleted-list"><li style="list-style-type:disc"><strong>EMI/EMC</strong>: lọc đầu vào, kiểm soát dv/dt và di/dt ở công suất.</li></ul></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80ba-8520-d2241740ec54"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8060-86b8-e2c18ebe7fa9" class=""><strong>4) Cannon Drive Stage (bộ biến đổi công suất điều khiển theo dòng) – “điểm push số 1”</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80a7-be62-dd130acac4ef" class=""><strong>4.1 Topology (đề xuất theo cấu hình stack)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80f0-903e-c54016ea7449" class="bulleted-list"><li style="list-style-type:disc"><strong>Buck đồng bộ</strong> nếu điện áp stack thấp hơn Vin.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80d9-a406-dbe431f67d39" class="bulleted-list"><li style="list-style-type:disc"><strong>Buck-Boost đồng bộ</strong> nếu stack thay đổi rộng hoặc cần giữ dòng ổn định khi Vin dao động.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8038-a84b-e6c7f6982a52" class="bulleted-list"><li style="list-style-type:disc"><strong>Interleaved (2 pha)</strong> nếu muốn giảm ripple dòng, giảm nhiệt linh kiện và giảm stress điện hóa.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-803b-b280-ece8491c1131" class=""><strong>4.2 Thiết bị công suất và tiêu chí chọn</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8069-8dec-d26a1d7e32f5" class="bulleted-list"><li style="list-style-type:disc"><strong>MOSFET Rds(on) thấp</strong> cho vùng rated;</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80db-aa72-febea8ca8668" class="bulleted-list"><li style="list-style-type:disc"><strong>SiC MOSFET</strong> nếu boost kéo dài, nhiệt môi trường cao, cần dv/dt kiểm soát tốt ở công suất cao;</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80fa-8bf8-e990cd2bdb59" class="bulleted-list"><li style="list-style-type:disc"><strong>Driver có kiểm soát slew-rate</strong> để giảm EMI và giảm RMS heating ẩn.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8001-be57-e816649f1318" class=""><strong>4.3 Vòng điều khiển dòng (bắt buộc, không thỏa hiệp)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-806e-aabc-f95bcb0fd278" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều khiển dòng vòng kín</strong> (PI hoặc PI + feedforward Vin).</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8037-ada0-f47362fb492b" class="bulleted-list"><li style="list-style-type:disc"><strong>Giới hạn động</strong>:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80f8-8c29-d6fc7b03e856" class="bulleted-list"><li style="list-style-type:circle">dI/dt_max (ví dụ 0,5 A/ms hoặc theo stack).</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8005-b25e-fa1f747100a9" class="bulleted-list"><li style="list-style-type:circle">I_max theo mode.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-809e-a228-dff05aa902d9" class="bulleted-list"><li style="list-style-type:disc"><strong>Chống bão hòa</strong>: anti-windup cho PI; bảo vệ quá dòng phần cứng (cycle-by-cycle).</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-804a-a97a-e4d707690df9" class=""><strong>4.4 “Push” bằng dạng sóng: từ PWM đơn điệu → thư viện kích thích điện hóa</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8018-ba85-dd9bf819fe97" class="">Thư viện tối thiểu 3 họ dạng sóng:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-8041-8f2f-d3095a6e5627" class="numbered-list" start="1"><li><strong>DC mượt (Low-stress DC)</strong>: ripple thấp, ưu tiên tuổi thọ.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-8074-9bb5-d99a218b7870" class="numbered-list" start="2"><li><strong>Pulsed DC khóa theo trở kháng</strong>: thay đổi duty/f theo trạng thái bọt khí và phân cực.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-80a4-acba-e3434fb1a9af" class="numbered-list" start="3"><li><strong>Soft-Burst Boost</strong>: burst có ramp lên/ramp xuống, giới hạn nhiệt-áp-suy giảm.</li></ol></div><div style="display:contents" dir="auto"><blockquote id="2eac5e6f-95bd-80cd-98a0-c4e26f3b2d11" class="">Điểm khác biệt “đẩy sát mép” không phải “xung mạnh”, mà là<div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8021-b61e-cf51f7a8a076" class=""><strong>đúng tần – đúng duty – đúng tốc độ cạnh</strong></p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80c9-b3d0-d5ebf10025a6" class=""><strong>giảm tổn thất không hồi phục</strong></p></div></blockquote></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80ff-9043-e634624fce2c"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-808d-9c88-fb4923661e18" class=""><strong>5) Stack điện phân + manifold + vật liệu (điểm push số 2: “vật liệu và hình học để chịu boost”)</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8023-94da-fda49a268dd6" class="">Vì bạn chưa chốt PEM/AEM/kiểu khác, phần này viết theo <strong>nguyên tắc chung</strong> nhưng đủ “đứng” để hội đồng hiểu bạn kiểm soát rủi ro:</p></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80c5-8d77-fdffb3d70cac" class=""><strong>5.1 Miền vận hành (Operating envelopes)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8009-9bc6-f3eb020f048e" class="bulleted-list"><li style="list-style-type:disc"><strong>T vận hành</strong>: 55–75 °C (đặt theo hiệu suất và độ bền vật liệu).</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80b6-aa0a-c0c5585ef5cc" class="bulleted-list"><li style="list-style-type:disc"><strong>ΔT cho phép vùng phản ứng</strong>: ≤ 5 °C (để tránh nứt, lão hóa cục bộ).</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-805e-b7df-e43bf1a876be" class="bulleted-list"><li style="list-style-type:disc"><strong>P vận hành</strong>: 1,5–3 bar (tránh tăng stress cơ khí và rủi ro crossover).</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-809a-aab5-d586a9ce6a4f" class=""><strong>5.2 Luật “không được vượt” (hard constraints)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-807e-a8f4-e1f513fbf0cb" class="bulleted-list"><li style="list-style-type:disc">Nếu <strong>dV/dI</strong> (độ dốc điện áp theo dòng) tăng bất thường → dấu hiệu tăng tổn hao/khí bám → bắt buộc giảm tải hoặc đổi waveform.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-809c-b47a-d064e077e233" class="bulleted-list"><li style="list-style-type:disc">Nếu <strong>R_eq</strong> trôi nhanh theo thời gian → dấu hiệu lão hóa/ô nhiễm → khóa boost.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80e8-a2c4-e569d456b566" class="bulleted-list"><li style="list-style-type:disc">Nếu <strong>ΔT</strong> tăng nhanh → giảm dòng trước khi đạt ngưỡng nhiệt tuyệt đối.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80c8-8ab5-fb6ec4c78a35" class=""><strong>5.3 Vật liệu và chi tiết “để sản xuất tại VN nhưng không hi sinh an toàn”</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80df-88ae-cdc49643b9e3" class="bulleted-list"><li style="list-style-type:disc"><strong>Heat spreader</strong>: nhôm/đồng (VN gia công tốt) để dàn đều nhiệt.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8051-be4c-f6bc63a90548" class="bulleted-list"><li style="list-style-type:disc"><strong>Gioăng, seal, đường khí</strong>: ưu tiên vật liệu chịu nhiệt/ẩm và tương thích H₂ (giảm thấm, giảm lão hóa).</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8099-8263-ebb6fed3287c" class="bulleted-list"><li style="list-style-type:disc"><strong>Bề mặt tiếp xúc điện</strong>: mạ/hoàn thiện để giảm điện trở tiếp xúc và điểm nóng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80c9-b2cc-d548670a9340" class="bulleted-list"><li style="list-style-type:disc"><strong>Cơ khí chống rung</strong>: gối đỡ/khung giảm rung (phù hợp hàng hải/đảo).</li></ul></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-8054-91ac-f81d122b2431"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-80c2-9985-c8bca7b848d7" class=""><strong>6) Quản lý nhiệt (Thermal Management) – “điểm push số 3: boost bị khóa bởi nhiệt”</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8046-8efd-fe54816a4b1e" class=""><strong>6.1 Triết lý nhiệt: “tối ưu phân bố”, không chỉ “tản nhiều”</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-800a-8e9d-d45bd81415b7" class="bulleted-list"><li style="list-style-type:disc"><strong>Thermal mass gần vùng phản ứng</strong> để giảm sốc.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80f9-b2f7-dc17bf119191" class="bulleted-list"><li style="list-style-type:disc"><strong>Heat spreader</strong> để giảm gradient.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80d4-8f7c-d3bb136fc847" class="bulleted-list"><li style="list-style-type:disc"><strong>Cooling loop</strong> có tiết diện đủ lớn; quạt/bơm là “tuyến phụ trợ”, không phải cứu hộ.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8004-bc6d-e7e2aca311d4" class=""><strong>6.2 Luật điều khiển nhiệt (rõ biến – rõ ngưỡng)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80af-925a-c8917668905f" class="bulleted-list"><li style="list-style-type:disc">dT/dt_max = 1 °C/phút (hoặc theo stack).</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-807f-856d-f5a35e28ddf2" class="bulleted-list"><li style="list-style-type:disc">ΔT_max = 5 °C.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-803a-845e-de918483f889" class="bulleted-list"><li style="list-style-type:disc">T_max tuyệt đối theo vật liệu.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-802a-82d2-c3463dd532bc" class="bulleted-list"><li style="list-style-type:disc">Nếu vi phạm dT/dt hoặc ΔT: <strong>derate dòng ngay</strong>, không chờ báo động.</li></ul></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-8076-8294-e96632c42751"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-808f-8b4f-eab02a990536" class=""><strong>7) Đường nước + chất lượng nước (Water Management) – “điểm push số 4: chịu thực tế VN”</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-803c-976a-d3dfa83b9a24" class=""><strong>7.1 Biến đo và điều khiển</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8098-ac7b-f97d87070d0c" class="bulleted-list"><li style="list-style-type:disc"><strong>Level</strong>: mực nước tối thiểu/ tối đa.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ca-b0f5-fa695fa04f5f" class="bulleted-list"><li style="list-style-type:disc"><strong>Conductivity</strong> (khuyến nghị bắt buộc nếu muốn chạy bền): dùng làm proxy cho ô nhiễm/ion không mong muốn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8037-a1e5-c4d502b28db1" class="bulleted-list"><li style="list-style-type:disc"><strong>Luật derate theo nước</strong>: nước xấu → giảm dòng → bảo vệ vật liệu.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80ef-9e74-cec6d893eafe" class=""><strong>7.2 Chế độ vận hành “không cố chạy”</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80fb-926e-cbc338a1d97c" class="bulleted-list"><li style="list-style-type:disc">Không tồn tại logic “đã bật là phải đạt KPI”.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80dd-a8dc-c35a4f309549" class="bulleted-list"><li style="list-style-type:disc">AMOS bắt buộc ưu tiên “chạy ít nhưng bền” hơn “chạy nhiều rồi chết”.</li></ul></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-801e-95e5-d23141c39fe2"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-80a4-a48d-ef0af05c4844" class=""><strong>8) Tách khí – điều hòa – an toàn H₂ (Gas Handling &amp; Safety) – “điểm push số 5: boost không được biến thành sự kiện an toàn”</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-806b-af4a-dd69f6ad992e" class=""><strong>8.1 Cấu hình bắt buộc</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-805e-b0be-ed5ebeaf5c13" class="bulleted-list"><li style="list-style-type:disc"><strong>Water trap/bubbler</strong> đủ kích thước cho <strong>lưu lượng boost</strong> (để tránh carry-over).</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8007-bbc5-d2bf7a13037f" class="bulleted-list"><li style="list-style-type:disc"><strong>Buffer volume</strong> để triệt xung áp.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80e3-888a-ce51769533f9" class="bulleted-list"><li style="list-style-type:disc"><strong>Non-return</strong> và cơ cấu chống backflow.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80a8-bae6-e85d97918abc" class="bulleted-list"><li style="list-style-type:disc"><strong>Relief valve</strong> thụ động độc lập.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8097-a3cc-e1c5257ac5b5" class=""><strong>8.2 Chỉ tiêu động</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-804a-a60a-dbb62397b563" class="bulleted-list"><li style="list-style-type:disc"><strong>Pressure ripple</strong> ≤ 3% trong boost.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80c9-acc4-ee281ab42963" class="bulleted-list"><li style="list-style-type:disc">Nếu ripple vượt: giảm boost, tăng damping, hoặc khóa boost.</li></ul></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-807b-880d-cff37ca6440a"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-80dd-b1f9-d1e8156b2c8c" class=""><strong>9) AMOS Core (Lớp 3) ở mức thuật toán: biến – ngưỡng – logic quyết định (viết để “ai cũng hiểu”)</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8008-befc-e3aeb2724017" class="">AMOS không phải “AI mơ hồ”. AMOS là <strong>bộ quản lý phong bì vận hành + bộ quản lý suy giảm + bộ cấp quyền boost</strong>.</p></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8031-8d26-f9ce6f3779ba" class=""><strong>9.1 Tập biến trạng thái (state variables)</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-808f-ad7f-e33ec30edb93" class="">Ký hiệu (đặt chuẩn để viết SRS):</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8017-938e-e6d6a7502371" class="bulleted-list"><li style="list-style-type:disc">I(t): dòng stack; V(t): điện áp stack</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8090-baf5-ebf4e5fae084" class="bulleted-list"><li style="list-style-type:disc">T̄(t): nhiệt độ trung bình; ΔT(t): gradient; dT/dt</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ce-b23f-c625e3d713ee" class="bulleted-list"><li style="list-style-type:disc">P(t): áp suất H₂; ΔP_ripple(t): biên độ dao động áp</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8091-96d4-d9187bb1836a" class="bulleted-list"><li style="list-style-type:disc">L(t): mực nước; Cw(t): độ dẫn điện (proxy chất lượng)</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80e6-b24a-d09b1169c13b" class="bulleted-list"><li style="list-style-type:disc">R_eq(t) = V/I (hoặc ước lượng lọc); dR_eq/dt (trôi)</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80a2-9c4e-df8a9f811b26" class="bulleted-list"><li style="list-style-type:disc">H(t): chỉ số sức khỏe (0–1)</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8057-9e08-d89b2accd1cf" class="bulleted-list"><li style="list-style-type:disc">D(t): chỉ số suy giảm tích lũy (có đơn vị quy ước)</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8001-896e-d2d04392d45c" class="bulleted-list"><li style="list-style-type:disc">F_recent: cờ lỗi gần đây; N_restart: số lần restart gần đây</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8073-853f-d5afd788e5bd" class=""><strong>9.2 Các ngưỡng cứng (hard thresholds)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80e3-ac14-ffe03d69145a" class="bulleted-list"><li style="list-style-type:disc">I_max_rated, I_max_boost</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8085-832f-c562048d1523" class="bulleted-list"><li style="list-style-type:disc">T_max, ΔT_max, (dT/dt)_max</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80c8-9585-cc4d8d2dde49" class="bulleted-list"><li style="list-style-type:disc">P_max, ΔP_ripple_max</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80b6-a3c9-cfe15efc7e4c" class="bulleted-list"><li style="list-style-type:disc">L_min, Cw_max (hoặc band Cw_min…max tùy hóa học)</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8018-95c8-e88d7a68f4ab" class="bulleted-list"><li style="list-style-type:disc">(dR_eq/dt)_max để khóa boost</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-806b-9b42-df2070bc9bd3" class=""><strong>9.3 Chỉ số suy giảm (D) – cách tính “đủ dùng, không cần hoàn hảo”</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8044-bd00-e2a08f833590" class="">Một dạng đơn giản nhưng có ý nghĩa kỹ thuật:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-800a-98ad-f9f31d7fd89e" class="bulleted-list"><li style="list-style-type:disc">D tăng theo:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-807a-83a8-c85473889a38" class="bulleted-list"><li style="list-style-type:circle"><strong>nhiệt cao kéo dài</strong> (stress nhiệt)</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-806c-9595-ca011f613800" class="bulleted-list"><li style="list-style-type:circle"><strong>dao động dòng lớn</strong> (stress điện hóa)</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80a4-b6fc-c8de1b604ee6" class="bulleted-list"><li style="list-style-type:circle"><strong>vận hành gần vùng cliff</strong> (proxy bằng tăng nhanh R_eq và tăng V ở cùng I)</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80c3-8fdd-fcded6264873" class="">Ví dụ quy ước:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80bf-a2ed-f70772e1d67f" class="bulleted-list"><li style="list-style-type:disc">D(t+Δt) = D(t) + k1·max(0, T̄−T_ref)·Δt + k2·|ΔI| + k3·max(0, dR_eq/dt)·Δt</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80ae-bb16-c7c37ff9a1ac" class="">Trong đó k1,k2,k3 được hiệu chuẩn bằng thử nghiệm 1.000h/2.000h.</p></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8060-af9a-d4f2400d6b62" class=""><strong>9.4 Luật quyết định chế độ (mode logic)</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-805b-b6db-cfffa055bf5d" class="">AMOS luôn ở một trong 5 mode:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80d9-92b6-dbd1244ed101" class="bulleted-list"><li style="list-style-type:disc">CRUISE (Rated)</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8022-9f26-fd58a70a1286" class="bulleted-list"><li style="list-style-type:disc">BOOST (Peak)</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80bc-8704-f309052531fd" class="bulleted-list"><li style="list-style-type:disc">DEGRADED (giảm công suất để giữ bền)</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-805b-8dba-cb73fc385103" class="bulleted-list"><li style="list-style-type:disc">PROTECTIVE (bảo toàn)</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8072-90c3-f7bb314ebaf1" class="bulleted-list"><li style="list-style-type:disc">LOCKOUT (khóa, yêu cầu cooldown + kiểm tra)</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80b2-bf19-cffd2bc9bd3f" class=""><strong>9.5 Luật cấp boost (Boost Permission) – “một điều kiện fail là không boost”</strong></h3></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80fc-ae3b-ec459ad82d86" class="">Boost chỉ được phép khi đồng thời:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8010-ab1a-de1d42689058" class="bulleted-list"><li style="list-style-type:disc">T̄ &lt; T_boost_enable</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80c5-ace0-cbbc4a8f3663" class="bulleted-list"><li style="list-style-type:disc">ΔT &lt; ΔT_enable</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-804f-92d9-f0489c20b80d" class="bulleted-list"><li style="list-style-type:disc">dT/dt &lt; (dT/dt)_enable</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-803c-b9bd-f84c821654f3" class="bulleted-list"><li style="list-style-type:disc">ΔP_ripple &lt; ΔP_enable</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80d0-807e-e0065d454726" class="bulleted-list"><li style="list-style-type:disc">Cw trong band</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8070-b16b-ccbc3894efb4" class="bulleted-list"><li style="list-style-type:disc">dR_eq/dt &lt; ngưỡng trôi</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-807f-976a-d3ee2c914eef" class="bulleted-list"><li style="list-style-type:disc">F_recent = 0 và N_restart &lt; N_cap</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8070-ae35-c339009a26b1" class="bulleted-list"><li style="list-style-type:disc">H &gt; H_min và D &lt; D_cap</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8071-adb0-e8cd58c8c8bd" class="">Nếu đạt → cấp boost trong thời gian τ_boost, sau đó bắt buộc cooldown τ_cooldown.</p></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-806b-a5ff-fcc15c76938c" class=""><strong>9.6 Pseudocode (cô đọng, đủ kỹ thuật)</strong></h3></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2eac5e6f-95bd-80cb-88a1-f1bae05fdb8f" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">loop mỗi 100 ms:
  đọc I,V,T1,T2,T3,P,L,Cw
  tính T̄, ΔT, dT/dt, R_eq, dR_eq/dt, ΔP_ripple
  cập nhật D, H

  nếu (T̄ &gt; T_max) hoặc (P &gt; P_max) hoặc (L &lt; L_min):
      mode = PROTECTIVE
  else nếu (F_recent = 1) hoặc (D &gt; D_lock) hoặc (N_restart &gt; N_lock):
      mode = LOCKOUT
  else nếu (cần tải cao) và boost_permission() = TRUE:
      mode = BOOST
  else nếu (ΔT &gt; ΔT_warn) hoặc (dR_eq/dt &gt; drift_warn) hoặc (Cw ngoài band hẹp):
      mode = DEGRADED
  else:
      mode = CRUISE

  theo mode đặt I_set và waveform:
      CRUISE: I_set = I_rated; waveform = DC_mượt
      BOOST:  I_set = I_boost; waveform = soft-burst; timeout = τ_boost
      DEGRADED: I_set = I_rated * α; waveform = pulsed-impedance
      PROTECTIVE: I_set giảm về 0 theo ramp; waveform = DC_mượt
      LOCKOUT: I_set = 0; chờ cooldown + reset quy trình

  gửi I_set + waveform xuống Lớp 2 (MCU current loop)</code></pre></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-8003-a2b5-e3e3a0d26694"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8017-b641-e88363e9133a" class=""><strong>10) Firmware/MCU (Lớp 2) – luật thời gian thực “không được trái AMOS”</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8054-be1f-c5ff5fe94991" class="">MCU chỉ làm 3 việc:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-80ab-b652-ddb30dd0e2fa" class="numbered-list" start="1"><li>Thực thi I_set với vòng dòng kín.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-8031-98b8-e245ed8a430b" class="numbered-list" start="2"><li>Thực thi giới hạn dI/dt, giới hạn tần số, giới hạn slew-rate.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-8025-a9a3-ec156cd22cab" class="numbered-list" start="3"><li>Bảo vệ phần cứng cycle-by-cycle (ngắn mạch, quá dòng tức thời, driver fault).</li></ol></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80ca-9ef6-cd747843584c" class="">MCU <strong>không có quyền</strong> tự “tăng dòng cho đạt KPI”.</p></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80eb-8e71-f06b3f97af09"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-80ac-871d-c212d0232c22" class=""><strong>11) Lớp giám sát – triển khai – chính sách (Lớp 4): đi chứng nhận và đi Nhà nước</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8004-afb8-db219cfe3691" class=""><strong>11.1 Nhật ký và truy vết (audit-ready)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8028-bb25-ff29acc70d94" class="bulleted-list"><li style="list-style-type:disc">Log theo sự kiện + theo chu kỳ: mode, I,V,T,P,L,Cw,R_eq,D,H.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-803a-9ed0-c164e77109a7" class="bulleted-list"><li style="list-style-type:disc">Log “ai thay đổi cấu hình, thay đổi gì, lúc nào” (phục vụ kiểm toán).</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8023-a8d1-cf3507cb49f1" class="bulleted-list"><li style="list-style-type:disc">Báo cáo định kỳ: uptime, số lần boost, số lần derate, số lần lockout, nguyên nhân.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-80ce-afad-f4a3bce3438d" class=""><strong>11.2 An ninh mạng công nghiệp (để qua kiểm tra hạ tầng)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-802a-8ce6-d07817deac7c" class="bulleted-list"><li style="list-style-type:disc">Phân vùng mạng: điều khiển thời gian thực tách khỏi SCADA.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8066-b9be-c874543e04d2" class="bulleted-list"><li style="list-style-type:disc">Cập nhật firmware có ký số; rollback an toàn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ad-8fc2-e0dccc9061fe" class="bulleted-list"><li style="list-style-type:disc">Không cho phép override an toàn từ xa.</li></ul></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-80c8-9c02-c8ce6d9e7240"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-80bb-97f9-c078e9a19095" class=""><strong>12) “Push all” đến sát mép khả thi: danh mục các đẩy quan trọng nhất (không lặp lại)</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80a0-8752-ffe1cd9ed13c" class=""><strong>Push 1 – Interleaved current-mode + slew control</strong>: giảm ripple dòng → giảm stress điện hóa → tăng bền.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80a2-b3d5-c9b6e6fe0123" class=""><strong>Push 2 – Boost envelope có quyền cấp + cooldown cưỡng bức</strong>: tăng đỉnh mà không ăn tuổi thọ.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80f3-8ca5-e53c4a66a308" class=""><strong>Push 3 – Impedance-locked waveform</strong>: thay đổi duty/f theo R_eq và drift → tránh bám khí/đi vào vùng cliff.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8066-bc59-e57f5b35293e" class=""><strong>Push 4 – Thermal headroom gating</strong>: boost bị khóa bởi ΔT và dT/dt, không bị “dụ” bởi nguồn còn mạnh.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80f7-8499-dd3aa253e9a6" class=""><strong>Push 5 – Gas surge-rated plumbing</strong>: boost không tạo xung áp/carry-over.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8043-a3b2-cbabdde2babc" class=""><strong>Push 6 – Water-quality derate</strong>: chịu nước thực tế VN mà không tự hủy.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-806b-8b7a-c270b7049db7" class=""><strong>Push 7 – Degradation index D + health H</strong>: ra quyết định theo xu hướng, không theo ngưỡng chết.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-808d-af6d-d90270903593" class=""><strong>Push 8 – Fail-operational theo mức</strong>: ưu tiên derate thay vì trip → tăng uptime.</p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-809b-aa6b-f3264b0bfe97" class=""><strong>Push 9 – Audit-ready logs + policy layer</strong>: đi tài trợ/đi kiểm toán/đi chuẩn hóa.</p></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-8040-aac3-f9273001de7e"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8065-9cc3-e711b76c5840" class=""><strong>13) Về “chuẩn nghiêm nhất toàn cầu” và “vượt state-of-the-art”: trả lời đúng chuẩn kỹ thuật</strong></h2></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-808e-a826-cca1c7423531" class="bulleted-list"><li style="list-style-type:disc"><strong>Có thể thiết kế để đáp ứng các bộ tiêu chuẩn nghiêm</strong> (an toàn điện, an toàn khí H₂, EMC, chức năng an toàn, hệ thống điều khiển công nghiệp).</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80e2-9d85-c3c3fffd6b49" class="bulleted-list"><li style="list-style-type:disc">Nhưng <strong>không thể tuyên bố “đã vượt/đã đáp ứng”</strong> nếu chưa có:<div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8022-8937-ca00cdbba7c7" class="bulleted-list"><li style="list-style-type:circle">kế hoạch thử nghiệm type test,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8037-a7f0-e371acecaa85" class="bulleted-list"><li style="list-style-type:circle">báo cáo phòng thử nghiệm,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80c1-9df2-ed8268c24d00" class="bulleted-list"><li style="list-style-type:circle">hồ sơ an toàn chức năng (FMEA/FTA, SIL/PL nếu áp dụng),</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8019-a92c-e893024da8d0" class="bulleted-list"><li style="list-style-type:circle">báo cáo EMC/EMI,</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8023-ad01-e169b2ce8f1b" class="bulleted-list"><li style="list-style-type:circle">và chứng thư cho cụm thiết bị.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-80e0-a227-e622e4f28e1d" class="">Vì vậy trong hồ sơ, câu đúng là:</p></div><div style="display:contents" dir="auto"><blockquote id="2eac5e6f-95bd-8025-8ea1-df3991191907" class="">Thiết kế AMOS-IKONOMY áp dụng kiến trúc ràng buộc cứng và cơ chế kiểm soát đa miền để<div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-808c-87cb-d510111cae39" class=""><strong>đạt điều kiện cần</strong></p></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-800c-8157-e166938557d6" class=""><strong>chương trình thử nghiệm và thẩm định độc lập</strong></p></div></blockquote></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-8094-892a-f946d0cb58fa"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-80a7-b35e-cfc4db025566" class=""><strong>14) Gói “0 gaps” về kiểm chứng: chương trình thử nghiệm bắt buộc (để biến thiết kế thành sự thật)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8052-82f8-f1531514f2b5" class=""><strong>14.1 Thử nghiệm hiệu suất – định luật Faraday (đúng bản chất)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ec-9866-dd92ccafe9e7" class="bulleted-list"><li style="list-style-type:disc">Đo H₂ thực (lưu lượng kế chuẩn) vs điện lượng (∫I dt).</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8028-97a0-d54cc5e6e563" class="bulleted-list"><li style="list-style-type:disc">Tính ổn định L/kWh theo thời gian.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8063-a074-d3aafbe208ab" class=""><strong>14.2 Thử nghiệm boost (điểm sống còn)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80df-9e93-c553d93b9bf3" class="bulleted-list"><li style="list-style-type:disc">Boost lặp lại theo chu kỳ, có cooldown bắt buộc.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ea-acdf-ed2400a08c3d" class="bulleted-list"><li style="list-style-type:disc">Theo dõi ΔT, dT/dt, ΔP_ripple, drift R_eq.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-805d-b2fa-fb8b4b9bb6a2" class="bulleted-list"><li style="list-style-type:disc">Tiêu chí: <strong>không xuất hiện drift tăng tốc</strong> sau các chuỗi boost.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8024-ad3a-ded84b086947" class=""><strong>14.3 Thử nghiệm độ bền 1.000h → 2.000h</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ec-a543-df30167b452e" class="bulleted-list"><li style="list-style-type:disc">Chạy liên tục + start/stop mô phỏng thực tế VN (nguồn dao động).</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8087-a34d-ec486e49a823" class="bulleted-list"><li style="list-style-type:disc">Đánh giá xu hướng R_eq, hiệu suất, số sự kiện derate/lockout.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-802a-a98f-da4817959907" class=""><strong>14.4 Thử nghiệm nước “không lý tưởng”</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8014-ba66-ff9a8ec7eeba" class="bulleted-list"><li style="list-style-type:disc">Các band độ dẫn khác nhau trong giới hạn an toàn của hóa học.</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ab-8de9-c26eec5e7ad8" class="bulleted-list"><li style="list-style-type:disc">Tiêu chí: hệ thống <strong>derate đúng</strong>, không tự phá vật liệu.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2eac5e6f-95bd-8089-af5f-ca5322581a2b" class=""><strong>14.5 EMC/EMI tiền chứng nhận</strong></h3></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80ca-b8a6-ef3dd82e9fad" class="bulleted-list"><li style="list-style-type:disc">Đo nhiễu dẫn và nhiễu bức xạ; kiểm tra ảnh hưởng tới cảm biến và MCU.</li></ul></div><div style="display:contents" dir="auto"><hr id="2eac5e6f-95bd-8033-b8d8-f8e3e5610c42"/></div><div style="display:contents" dir="auto"><h2 id="2eac5e6f-95bd-8028-918f-f25bc2ead65a" class=""><strong>15) Trả lời thẳng: “còn đẩy được nữa không?”</strong></h2></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8093-b507-f1bc412fd276" class=""><strong>Có</strong>, nhưng “đẩy thêm” ở giai đoạn này không còn là “thêm công suất” theo kiểu tuyến tính. “Đẩy thêm” là:</p></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-8098-88d8-d76834ffe377" class="bulleted-list"><li style="list-style-type:disc"><strong>giảm ripple dòng thêm nữa</strong> (interleaving tốt hơn, đo dòng tốt hơn, layout tốt hơn);</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80a4-bcc2-c389ab9e2c3a" class="bulleted-list"><li style="list-style-type:disc"><strong>tăng headroom nhiệt bằng hình học + truyền nhiệt</strong> (không phải tăng quạt);</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80d7-a42c-de2ab6386719" class="bulleted-list"><li style="list-style-type:disc"><strong>giảm nhạy với nước và môi trường</strong> (logic derate + vật liệu seal/đường nước);</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-808c-b449-c3b8d733172e" class="bulleted-list"><li style="list-style-type:disc"><strong>tối ưu đường khí để boost an toàn hơn</strong>;</li></ul></div><div style="display:contents" dir="auto"><ul id="2eac5e6f-95bd-80c6-8be5-c61a309b808f" class="bulleted-list"><li style="list-style-type:disc"><strong>tinh chỉnh D và H từ dữ liệu thử nghiệm</strong> để khóa đúng lúc, không khóa quá sớm.</li></ul></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-803e-bad4-dad98b4ec7dd" class="">Nếu bạn muốn, tôi có thể viết tiếp thành <strong>3 tài liệu đóng gói</strong> (đúng “0 gaps” cho hồ sơ):</p></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-80e9-a478-e805b8fe3869" class="numbered-list" start="1"><li><strong>SRS đầy đủ cho AMOS</strong> (chức năng, phi chức năng, interface, an toàn, logging, update, cybersecurity, test cases).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-8062-ba3d-fa65f360baa7" class="numbered-list" start="2"><li><strong>Sơ đồ mạch power stage ở mức khối + danh mục linh kiện mục tiêu</strong> (BOM logic, yêu cầu layout, yêu cầu đo dòng/áp, driver).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2eac5e6f-95bd-80b2-a3bc-c8681848adf5" class="numbered-list" start="3"><li><strong>Bộ “Safety &amp; Compliance Pack”</strong> (hazard analysis, FMEA/FTA khung, kế hoạch thử nghiệm, tiêu chí nghiệm thu cho thẩm định Nhà nước).</li></ol></div><div style="display:contents" dir="auto"><p id="2eac5e6f-95bd-8085-8064-de3745560350" class="">
</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
