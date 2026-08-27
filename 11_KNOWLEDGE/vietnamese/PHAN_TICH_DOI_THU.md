---
tags: [vietnamese]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Phân tích đối thủ</title><style>
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
	
</style></head><body><article id="280c5e6f-95bd-80f4-a855-eb85b28da78f" class="page sans"><header><h1 class="page-title" dir="auto">Phân tích đối thủ</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="280c5e6f-95bd-804a-8713-dd2fed24d986" class="">Hiện trạng thị trường xe công nghệ và taxi Việt Nam phản ánh một cấu trúc cạnh tranh phân mảnh nhưng lại đồng quy ở các điểm yếu hệ thống: không hãng nào vừa bảo đảm an sinh dài hạn, vừa tạo thu nhập minh bạch, vừa cho tài xế quyền tự chủ vận hành. Grab thống trị nhờ quy mô khách và hệ sinh thái đa dịch vụ, song thiếu an sinh, thu nhập biến động và kỷ luật zero-tolerance khiến tỷ lệ rời bỏ cao. Be tận dụng thương hiệu nội địa và chi phí gia nhập thấp, nhưng không đạt khối lượng cuốc cần thiết để duy trì thu nhập bền vững. Xanh SM nổi bật với lương cơ bản, BHXH và phương tiện điện cấp sẵn, nhưng lại bù trừ bằng KPI gắt gao, auto-assign và cơ chế truy thu gây áp lực lớn. Các hãng truyền thống (Vinasun, Mai Linh, G7) cung cấp hợp đồng lao động và phúc lợi đầy đủ, song bị giới hạn bởi doanh số cứng, công nghệ yếu và thu nhập thấp, làm họ mất dần tài xế trẻ về phía các nền tảng số.</p></div><div style="display:contents" dir="auto"><p id="280c5e6f-95bd-807e-ba54-fbc3c5d8a37d" class="">Khoảng trống thị trường (white space) xuất hiện chính ở giao điểm chưa được khai thác: <strong>thu nhập minh bạch và dự đoán được, an sinh đầy đủ, kỷ luật hỗ trợ thay vì phạt, và tích hợp B2B để bảo đảm nguồn cuốc ổn định</strong>. Không hãng nào hiện nay hiển thị cho tài xế “P&amp;L theo giờ” (gross, phí nền tảng, chi phí vận hành, net), không hãng nào cung cấp bảo hiểm thu nhập hoặc gói phúc lợi gia đình, và không hãng nào loại bỏ cơ chế truy thu. 
Đây là cơ hội chiến lược cho UniTaxi định vị như nền tảng đầu tiên kết hợp sức mạnh công nghệ (app hiện đại, dữ liệu minh bạch) với giá trị truyền thống (an sinh xã hội, lương cơ bản), đồng thời mở rộng bằng <strong>multi-energy fleet</strong> và <strong>corporate ride contracts</strong>. 
Nếu thực thi đúng, UniTaxi có thể chiếm lợi thế cạnh tranh bền vững, trở thành chuẩn mực mới về hiệu quả vận hành và trải nghiệm tài xế trong ngành.</p></div><div style="display:contents" dir="auto"><h1 id="280c5e6f-95bd-8011-95e5-fa8a8cb5e260" class=""><strong>🚖 Vietnam Ride-Hailing &amp; 
Taxi Competition Matrix (Exhaustive 2.0)</strong></h1></div><div style="display:contents" dir="ltr"><table id="280c5e6f-95bd-806c-89a3-ea7141c72d43" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-807e-9730-ded118c1579f"><th id="DC^M" class="simple-table-header-color simple-table-header" style="width:210px"><strong>Metric</strong></th><th id="f;zY" class="simple-table-header-color simple-table-header" style="width:194px"><strong>Grab</strong></th><th id="&lt;ez;" class="simple-table-header-color simple-table-header" style="width:186px"><strong>Be</strong></th><th id="?uxp" class="simple-table-header-color simple-table-header" style="width:230px"><strong>Xanh SM (GSM)</strong></th><th id="G=jp" class="simple-table-header-color simple-table-header" style="width:168px"><strong>Vinasun</strong></th><th id="?Irk" class="simple-table-header-color simple-table-header" style="width:166px"><strong>Mai Linh</strong></th><th id="CUnr" class="simple-table-header-color simple-table-header" style="width:167px"><strong>G7 (HN)</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-80db-8ee2-e7de9f41db61"><td id="DC^M" class="" style="width:210px"><strong>Tư cách tài xế</strong></td><td id="f;zY" class="" style="width:194px">Đối tác (không HĐLĐ)</td><td id="&lt;ez;" class="" style="width:186px">Đối tác (không HĐLĐ)</td><td id="?uxp" class="" style="width:230px">Nhân viên (HĐLĐ)</td><td id="G=jp" class="" style="width:168px">Nhân viên (HĐLĐ)</td><td id="?Irk" class="" style="width:166px">Nhân viên (HĐLĐ)</td><td id="CUnr" class="" style="width:167px">Nhân viên (HĐLĐ)</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-804f-897f-e3d169e77481"><td id="DC^M" class="" style="width:210px"><strong>BHXH/BHYT/BHTN</strong></td><td id="f;zY" class="" style="width:194px">Không</td><td id="&lt;ez;" class="" style="width:186px">Không</td><td id="?uxp" c
lass="" style="width:230px">Có đầy đủ từ ngày đầu</td><td id="G=jp" class="" style="width:168px">Có đầy đủ</td><td id="?Irk" class="" style="width:166px">Có đầy đủ</td><td id="CUnr" class="" style="width:167px">Có đầy đủ</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-80f5-9c0e-eeab3637313d"><td id="DC^M" class="" style="width:210px"><strong>% đóng BHXH</strong></td><td id="f;zY" class="" style="width:194px">—</td><td id="&lt;ez;" class="" style="width:186px">—</td><td id="?uxp" class="" style="width:230px">21.5% (theo luật VN; công ty + tài xế chia)</td><td id="G=jp" class="" style="width:168px">21.5%</td><td id="?Irk" class="" style="width:166px">21.5%</td><td id="CUnr" class="" style="width:167px">21.5%</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-8026-b053-fd74cae0cde8"><td id="DC^M" class="" style="width:210px"><strong>BH tai nạn chuyến</strong></td><td id="f;zY" class="" style="width:194px">GPA mặc định; 
Ride Cover 2.000đ/chuyến (tối đa 500m)</td><td id="&lt;ez;" class="" style="width:186px">Có, ít chi tiết công khai</td><td id="?uxp" class="" style="width:230px">Bảo hiểm bổ sung, chi tiết nội bộ</td><td id="G=jp" class="" style="width:168px">Theo luật</td><td id="?Irk" class="" style="width:166px">Theo luật</td><td id="CUnr" class="" style="width:167px">Theo luật</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-8063-bcee-f4b57a545461"><td id="DC^M" class="" style="width:210px"><strong>BH gia đình/phụ thuộc</strong></td><td id="f;zY" class="" style="width:194px">Không</td><td id="&lt;ez;" class="" style="width:186px">Không</td><td id="?uxp" class="" style="width:230px">Không</td><td id="G=jp" class="" style="width:168px">Không</td><td id="?Irk" class="" style="width:166px">Không</td><td id="CUnr" class="" style="width:167px">Không</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-803c-88c3-e5205e959935"><td id="DC^M" class="" style="width:210px"><strong>Lương cơ bản</strong></td><td id="f;zY" class="" style="width:194px">Không</td><td id="&lt;ez;" class="" style="width:186px">Không</td><td id="?uxp" class="" style="width:230px">Có (theo vùng) + cam kết thu nhập ban đầu</td><td id="G=jp" class="" style="width:168px">Có</td><td id="?Irk" class="" style="width:166px">Có</td><td id="CUnr" class="" style="width:167px">Có</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-80f2-b855-e9bfed85cc79"><td id="DC^M" class="" style="width:210px"><strong>Hoa hồng nền tảng</strong></td><td id="f;zY" class="" style="width:194px">Bike ~20%, Car ~25%</td><td id="&lt;ez;" class="" style="width:186px">Bike ~18–20%, Car ~25%</td><td id="?uxp" class="" style="width:230px">Car chia %; 
Bike 80% doanh thu 2 năm đầu</td><td id="G=jp" class="" style="width:168px">% chia doanh thu</td><td id="?Irk" class="" style="width:166px">% chia doanh thu</td><td id="CUnr" class="" style="width:167px">% chia doanh thu</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-80b6-bfa5-e6031e780296"><td id="DC^M" class="" style="width:210px"><strong>Thu nhập NET/tháng – Bike FT</strong></td><td id="f;zY" class="" style="width:194px">9–11m (gross 12–15m)</td><td id="&lt;ez;" class="" style="width:186px">7–9m (gross 10–13m)</td><td id="?uxp" class="" style="width:230px">~18m nếu đạt KPI (Bike Platform)</td><td id="G=jp" class="" style="width:168px">—</td><td id="?Irk" class="" style="width:166px">—</td><td id="CUnr" class="" style="width:167px">—</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-804c-8c6d-df0c8f5e3e78"><td id="DC^M" class="" style="width:210px"><strong>Thu nhập NET/tháng – Car FT</strong></td><td id="f;zY" class="" style="width:194px">13–17m (gross 25–30m)</td><td id="&lt;ez;" class="" style="width:186px">11–14m</td><td id="?uxp" class="" style="width:230px">12–20m (tùy KPI)</td><td id="G=jp" class="" style="width:168px">12–16m</td><td id="?Irk" class="" style="width:166px">10–14m</td><td id="CUnr" class="" style="width:167px">9–12m</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-8099-b730-c3d3fc2870fb"><td id="DC^M" class="" style="width:210px"><strong>Thu nhập NET/tháng – Part-time</strong></td><td id="f;zY" class="" style="width:194px">Bike 4–6m; Car 7–9m</td><td id="&lt;ez;" class="" style="width:186px">Bike 3–5m; 
Car 6–8m</td><td id="?uxp" class="" style="width:230px">~8–10m (nếu chạy 4–5h/ngày)</td><td id="G=jp" class="" style="width:168px">5–7m</td><td id="?Irk" class="" style="width:166px">4–6m</td><td id="CUnr" class="" style="width:167px">4–6m</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-8051-9433-d6ff33d383fb"><td id="DC^M" class="" style="width:210px"><strong>Thu nhập ròng theo giờ</strong></td><td id="f;zY" class="" style="width:194px">Bike 40–50k/h; Car 80–100k/h</td><td id="&lt;ez;" class="" style="width:186px">Bike 35–45k/h; Car 70–90k/h</td><td id="?uxp" class="" style="width:230px">70–120k/h (EV tiết kiệm năng lượng)</td><td id="G=jp" class="" style="width:168px">60–80k/h</td><td id="?Irk" class="" style="width:166px">50–70k/h</td><td id="CUnr" class="" style="width:167px">50–65k/h</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-808d-9e71-db7ff855755d"><td id="DC^M" class="" style="width:210px"><strong>Ổn định thu nhập</strong></td><td id="f;zY" class="" style="width:194px">Biến động cao (thưởng thay đổi)</td><td id="&lt;ez;" class="" style="width:186px">Biến động cao</td><td id="?uxp" class="" style="width:230px">Ổn định hơn nhưng bị truy thu</td><td id="G=jp" class="" style="width:168px">Ổn định vừa</td><td id="?Irk" class="" style="width:166px">Ổn định nhưng thấp</td><td id="CUnr" class="" style="width:167px">Ổn định thấp</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-80da-bb41-ec27ac25a392"><td id="DC^M" class="" style="width:210px"><strong>Chi phí gia nhập</strong></td><td id="f;zY" class="" style="width:194px">Bike ~0.5–1m; Car ~2–5m</td><td id="&lt;ez;" class="" style="width:186px">Bike ~0.3–0.5m; Car ~2–3m</td><td id="?uxp" class="" style="width:230px">Gần 0 (xe &amp; 
đồng phục cấp)</td><td id="G=jp" class="" style="width:168px">Thấp</td><td id="?Irk" class="" style="width:166px">Thấp</td><td id="CUnr" class="" style="width:167px">Thấp</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-8088-8985-e97523b6c47e"><td id="DC^M" class="" style="width:210px"><strong>Chi phí vận hành/tháng</strong></td><td id="f;zY" class="" style="width:194px">Bike 5–6m; Car 15–20m</td><td id="&lt;ez;" class="" style="width:186px">Bike 4–6m; 
Car 14–18m</td><td id="?uxp" class="" style="width:230px">Pin 650k/tháng (unlimited km, nếu đạt KPI)</td><td id="G=jp" class="" style="width:168px">10–12m</td><td id="?Irk" class="" style="width:166px">9–11m</td><td id="CUnr" class="" style="width:167px">9–11m</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-80ee-a2d6-f6bfe8daa1fe"><td id="DC^M" class="" style="width:210px"><strong>Khấu hao xe</strong></td><td id="f;zY" class="" style="width:194px">Tài xế chịu (xe cá nhân)</td><td id="&lt;ez;" class="" style="width:186px">Tài xế chịu</td><td id="?uxp" class="" style="width:230px">Công ty chịu (xe VinFast cấp)</td><td id="G=jp" class="" style="width:168px">Công ty chịu</td><td id="?Irk" class="" style="width:166px">Công ty chịu</td><td id="CUnr" class="" style="width:167px">Công ty chịu</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-80d8-92bf-ceadb82f2275"><td id="DC^M" class="" style="width:210px"><strong>Chi phí ẩn</strong></td><td id="f;zY" class="" style="width:194px">Mất thưởng, khóa app</td><td id="&lt;ez;" class="" style="width:186px">Mất thưởng</td><td id="?uxp" class="" style="width:230px">Truy thu doanh số</td><td id="G=jp" class="" style="width:168px">Trừ lương nếu không đạt doanh thu</td><td id="?Irk" class="" style="width:166px">Trừ lương</td><td id="CUnr" class="" style="width:167px">Trừ lương</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-801f-a75d-eefbbc005d9a"><td id="DC^M" class="" style="width:210px"><strong>KPI &amp; kỷ luật</strong></td><td id="f;zY" class="" style="width:194px">Zero-tolerance; 
nhận ≥80%, hủy ≤20%</td><td id="&lt;ez;" class="" style="width:186px">KPI mềm hơn, khóa khi gian lận</td><td id="?uxp" class="" style="width:230px">Nhận ≥70%, auto-assign, doanh thu tối thiểu/ngày</td><td id="G=jp" class="" style="width:168px">Doanh số cứng</td><td id="?Irk" class="" style="width:166px">Doanh số cứng</td><td id="CUnr" class="" style="width:167px">Doanh số cứng</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-8042-a10a-d2622df42834"><td id="DC^M" class="" style="width:210px"><strong>Mức phạt cụ thể</strong></td><td id="f;zY" class="" style="width:194px">Trừ thưởng 100–500k; khóa app 3–7 ngày; gian lận → khóa vĩnh viễn</td><td id="&lt;ez;" class="" style="width:186px">Trừ thưởng, hạn chế cuốc (n/a public)</td><td id="?uxp" class="" style="width:230px">Không đạt doanh số → truy thu; 
vi phạm → chấm dứt HĐLĐ</td><td id="G=jp" class="" style="width:168px">Phạt tiền/kỷ luật</td><td id="?Irk" class="" style="width:166px">Phạt tiền/kỷ luật</td><td id="CUnr" class="" style="width:167px">Phạt tiền/kỷ luật</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-80db-9552-e4702e14b774"><td id="DC^M" class="" style="width:210px"><strong>Thời gian xử lý khiếu nại</strong></td><td id="f;zY" class="" style="width:194px">3–7 ngày</td><td id="&lt;ez;" class="" style="width:186px">5–7 ngày</td><td id="?uxp" class="" style="width:230px">1–3 ngày (có trung tâm)</td><td id="G=jp" class="" style="width:168px">Nội bộ công ty</td><td id="?Irk" class="" style="width:166px">Nội bộ công ty</td><td id="CUnr" class="" style="width:167px">Nội bộ công ty</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-807d-97da-f0bea7b46ad5"><td id="DC^M" class="" style="width:210px"><strong>App quality</strong></td><td id="f;zY" class="" style="width:194px">Ổn định, đa dịch vụ</td><td id="&lt;ez;" class="" style="width:186px">Đôi khi lỗi định vị</td><td id="?uxp" class="" style="width:230px">Ổn định, nhưng phụ thuộc sạc EV</td><td id="G=jp" class="" style="width:168px">Tương đối hạn chế</td><td id="?Irk" class="" style="width:166px">Ứng dụng yếu</td><td id="CUnr" class="" style="width:167px">Ứng dụng yếu</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-806a-9139-ec6df286390e"><td id="DC^M" class="" style="width:210px"><strong>CX – tài xế phàn nàn</strong></td><td id="f;zY" class="" style="width:194px">Hoa hồng cao, khóa app vô cớ, thưởng biến động</td><td id="&lt;ez;" class="" style="width:186px">Ít cuốc, thưởng đổi nhanh, app lỗi</td><td id="?uxp" class="" style="width:230px">KPI cao, auto-assign, 
áp lực sạc</td><td id="G=jp" class="" style="width:168px">Doanh số áp lực</td><td id="?Irk" class="" style="width:166px">Doanh số + chậm trả lương (case)</td><td id="CUnr" class="" style="width:167px">Thu nhập thấp</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-80c8-9747-cbe0f36b0a27"><td id="DC^M" class="" style="width:210px"><strong>CX – khách phàn nàn</strong></td><td id="f;zY" class="" style="width:194px">Hủy phút chót, surge giá cao</td><td id="&lt;ez;" class="" style="width:186px">Khó đặt xe ngoài HN/HCM</td><td id="?uxp" class="" style="width:230px">Thiếu xe giờ cao điểm</td><td id="G=jp" class="" style="width:168px">Giá cao giờ thấp điểm</td><td id="?Irk" class="" style="width:166px">Chờ xe lâu vùng ven</td><td id="CUnr" class="" style="width:167px">Chờ lâu giờ cao điểm</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-8057-af7c-f2100863f697"><td id="DC^M" class="" style="width:210px"><strong>Driver Support SLA</strong></td><td id="f;zY" class="" style="width:194px">App + hotline (chậm)</td><td id="&lt;ez;" class="" style="width:186px">Hotline (chậm)</td><td id="?uxp" class="" style="width:230px">Trung tâm trực tiếp + hotline (nhanh hơn)</td><td id="G=jp" class="" style="width:168px">Phòng nhân sự</td><td id="?Irk" class="" style="width:166px">Phòng nhân sự</td><td id="CUnr" class="" style="width:167px">Phòng nhân sự</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-809b-83da-d94f0c395718"><td id="DC^M" class="" style="width:210px"><strong>Corporate B2B contracts</strong></td><td id="f;zY" class="" style="width:194px">Mạnh (Grab for Business, airport)</td><td id="&lt;ez;" class="" style="width:186px">Yếu</td><td id="?uxp" class="" style="width:230px">Đang phát triển (sân bay, khách sạn Vin)</td><td id="G=jp" class="" style="width:168px">Mạnh (sân bay, 
khách sạn)</td><td id="?Irk" class="" style="width:166px">Mạnh (toàn quốc)</td><td id="CUnr" class="" style="width:167px">Trung bình (Hà Nội)</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-8059-a8a6-d27f3a83ede1"><td id="DC^M" class="" style="width:210px"><strong>Retention lever</strong></td><td id="f;zY" class="" style="width:194px">Missions, referral, nhiều cuốc, hệ sinh thái</td><td id="&lt;ez;" class="" style="width:186px">Incentives khu vực, thương hiệu Việt</td><td id="?uxp" class="" style="width:230px">Lương cơ bản, BHXH, xe cấp, thương hiệu xanh</td><td id="G=jp" class="" style="width:168px">An sinh + B2B</td><td id="?Irk" class="" style="width:166px">An sinh + phủ toàn quốc</td><td id="CUnr" class="" style="width:167px">An sinh + nhận diện Hà Nội</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-80fb-88b7-e0b8eca1a8d7"><td id="DC^M" class="" style="width:210px"><strong>Retention rate (ước tính)</strong></td><td id="f;zY" class="" style="width:194px">70–80% rời trong 1 năm (drop-off cao)</td><td id="&lt;ez;" class="" style="width:186px">60–70% giữ được sau 1 năm</td><td id="?uxp" class="" style="width:230px">70–80% giữ nhờ HĐLĐ, 
nhưng drop khi KPI áp lực</td><td id="G=jp" class="" style="width:168px">80–85% giữ lâu</td><td id="?Irk" class="" style="width:166px">75–80%</td><td id="CUnr" class="" style="width:167px">80%</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-801d-adf2-e38a2aae55ed"><td id="DC^M" class="" style="width:210px"><strong>Referral/Upskilling</strong></td><td id="f;zY" class="" style="width:194px">Referral thưởng giới thiệu</td><td id="&lt;ez;" class="" style="width:186px">Có nhưng nhỏ</td><td id="?uxp" class="" style="width:230px">Không có</td><td id="G=jp" class="" style="width:168px">Không</td><td id="?Irk" class="" style="width:166px">Không</td><td id="CUnr" class="" style="width:167px">Không</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-803a-8129-dc0e718f0221"><td id="DC^M" class="" style="width:210px"><strong>Khung pháp lý</strong></td><td id="f;zY" class="" style="width:194px">ND 158/2024 (taxi điện tử)</td><td id="&lt;ez;" class="" style="width:186px">ND 158/2024</td><td id="?uxp" class="" style="width:230px">ND 158/2024 (taxi chính thức)</td><td id="G=jp" class="" style="width:168px">ND 10/2020, ND 158/2024</td><td id="?Irk" class="" style="width:166px">ND 10/2020, ND 158/2024</td><td id="CUnr" class="" style="width:167px">ND 10/2020, 
ND 158/2024</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-8092-8883-fe74b2ed132e"><td id="DC^M" class="" style="width:210px"><strong>E-invoice compliance</strong></td><td id="f;zY" class="" style="width:194px">Bắt buộc (app)</td><td id="&lt;ez;" class="" style="width:186px">Bắt buộc</td><td id="?uxp" class="" style="width:230px">Bắt buộc</td><td id="G=jp" class="" style="width:168px">Đã có sẵn</td><td id="?Irk" class="" style="width:166px">Đã có sẵn</td><td id="CUnr" class="" style="width:167px">Đã có sẵn</td></tr></div><div style="display:contents" dir="ltr"><tr id="280c5e6f-95bd-8018-bbfa-f4c01c33a9c7"><td id="DC^M" class="" style="width:210px"><strong>Legal disputes</strong></td><td id="f;zY" class="" style="width:194px">Grab vs Vinasun kiện tụng</td><td id="&lt;ez;" class="" style="width:186px">Ít</td><td id="?uxp" class="" style="width:230px">Không</td><td id="G=jp" class="" style="width:168px">Từng kiện Grab</td><td id="?Irk" class="" style="width:166px">Nợ BHXH, khủng hoảng vốn</td><td id="CUnr" class="" style="width:167px">Không đáng kể</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="280c5e6f-95bd-800a-b62f-d51c676794de" class="">Các hãng hiện tại đều để lộ khoảng trống lớn trong việc chăm lo quyền lợi dài hạn và trải nghiệm thực tế của tài xế. Grab và Be thu hút tài xế nhờ số cuốc nhiều và gia nhập dễ, nhưng lại thiếu an sinh, thu nhập biến động và kỷ luật cứng rắn khiến tỷ lệ rời bỏ cao. Xanh SM cung cấp BHXH và lương cơ bản, song áp lực KPI, auto-assign và cơ chế truy thu khiến nhiều tài xế cảm thấy bị “ép”. Taxi truyền thống bảo đảm hợp đồng và phúc lợi đầy đủ, nhưng thu nhập thấp, công nghệ kém và không hấp dẫn với lực lượng lao động trẻ. 
Chính vì thế, không hãng nào kết hợp đồng thời minh bạch thu nhập, an sinh đầy đủ, kỷ luật linh hoạt và nguồn cuốc ổn định — khoảng trống này là cơ hội chiến lược rõ rệt cho UniPower.</p></div><div style="display:contents" dir="auto"><p id="280c5e6f-95bd-808f-9e79-ea3174d5fd3f" class="">Để tận dụng cơ hội này, UniPower có thể thu hút tài xế bằng cơ chế <strong>gia nhập dễ, không phí ban đầu</strong>, minh bạch P&amp;L theo giờ (gross, phí, chi phí, net) và <strong>cam kết thu nhập tối thiểu không truy thu</strong>. Về giữ chân, UniPower nên khác biệt bằng <strong>bảo hiểm thu nhập và gói phúc lợi gia đình</strong>, đồng thời thiết lập <strong>Corporate Ride Engine</strong> để tạo nguồn cuốc sân bay, khách sạn, bệnh viện ổn định cho tài xế kỳ cựu. Thay vì kỷ luật zero-tolerance, UniPower có thể áp dụng mô hình “support-first, penalty-later” — cảnh báo và huấn luyện trước khi phạt. Cách tiếp cận này giúp tạo niềm tin, giảm tỷ lệ rời bỏ và xây dựng một cộng đồng tài xế trung thành, gắn bó lâu dài với thương hiệu.</p></div><div style="display:contents" dir="auto"><h1 id="280c5e6f-95bd-80b5-9999-ffe89d0eb137" class=""><strong>Grab Việt Nam </strong></h1></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-801e-a804-e01d4c893710"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-80bd-814b-c059eec531a3" class=""><strong>1. 
Bảo hiểm &amp; An sinh</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80b7-872a-e323dbeaabc7" class="bulleted-list"><li style="list-style-type:disc"><strong>Không có BHXH/BHYT/BHTN</strong>: Grab phân loại tài xế là đối tác độc lập, không ký HĐLĐ.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-805b-92c9-dd873beef378" class="bulleted-list"><li style="list-style-type:disc"><strong>Group Personal Accident Insurance (miễn phí)</strong>: áp dụng cho tài xế và khách trên mọi chuyến.<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8084-a013-d981535b710f" class="bulleted-list"><li style="list-style-type:circle">Quyền lợi: tử vong/thương tật vĩnh viễn tối đa <strong>500 triệu VND/vụ</strong>.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8086-a28d-d2f37758de90" class="bulleted-list"><li style="list-style-type:disc"><strong>Ride Cover (tùy chọn)</strong>: phí <strong>~2.000 VND/chuyến</strong>, quyền lợi bảo hiểm tử vong/thương tật lên tới <strong>500 triệu VND</strong>, kèm chi trả viện phí.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-803d-98cd-cc8dccfe1c34" class="bulleted-list"><li style="list-style-type:disc"><strong>Hạn chế</strong>: không có bồi thường thu nhập khi tài xế tạm nghỉ vì tai nạn/ốm đau. Phản hồi thực tế cho thấy chi trả y tế có nhưng <strong>mất thu nhập không được bù</strong>.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80d6-9593-dc14f4a30c3f"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-80cd-a6c0-e0fe5c1ebb79" class=""><strong>2. 
Chế độ &amp; Phúc lợi (Compensation &amp; Benefits)</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-803c-8586-fa2d5197978e" class="bulleted-list"><li style="list-style-type:disc"><strong>Không có lương cơ bản</strong>: toàn bộ thu nhập dựa trên cuốc + thưởng.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-801c-b8d5-f168465814d9" class="bulleted-list"><li style="list-style-type:disc"><strong>Thưởng (incentives)</strong>: thay đổi hàng tuần theo khu vực, ví dụ: thưởng <strong>200.000đ/ngày</strong> khi đạt 20 chuyến.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-808c-808f-ea01a37c3906" class="bulleted-list"><li style="list-style-type:disc"><strong>Ưu đãi đối tác</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-803d-a0f5-ec252283b4aa" class="bulleted-list"><li style="list-style-type:circle">Giảm giá xăng/dầu tại cây xăng liên kết (mức giảm 2–5%).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-806e-9c32-e5ffc871dc82" class="bulleted-list"><li style="list-style-type:circle">Gói cước viễn thông rẻ hơn 10–20% cho tài xế.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80c0-a47a-eaa5740100a1" class="bulleted-list"><li style="list-style-type:circle">Ưu đãi bảo dưỡng, kiểm tra xe.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80e2-8437-f488201e3c7e" class="bulleted-list"><li style="list-style-type:disc"><strong>Phúc lợi cộng đồng</strong>: chương trình như “Wishes Behind the Wheel”, hỗ trợ tài xế gặp khó khăn, nhưng không mang tính cam kết an sinh.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8085-94db-f6133b10ae25"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-803b-886a-c7c55a1dac10" class=""><strong>3. 
Tuyển dụng &amp; Đào tạo</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8026-af7d-fa6654dae369" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều kiện</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8057-be35-fa4c59e27f8d" class="bulleted-list"><li style="list-style-type:circle">GrabBike: GPLX A1, CCCD, xe hợp lệ.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8001-aba6-e1f6d2ac0093" class="bulleted-list"><li style="list-style-type:circle">GrabCar: GPLX B2+, đăng kiểm xe, bảo hiểm TNDS.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80dd-a335-d66f5dccac49" class="bulleted-list"><li style="list-style-type:disc"><strong>Chi phí gia nhập</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80f1-aaa4-efe4407dce21" class="bulleted-list"><li style="list-style-type:circle">GrabBike: ~500k–1 triệu (đồng phục, mũ bảo hiểm).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-808d-9247-f16ad7d01ea6" class="bulleted-list"><li style="list-style-type:circle">GrabCar: 2–5 triệu (đăng ký, decal, thiết bị GPS, kiểm định).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80a2-8c23-d0d6239be9a5" class="bulleted-list"><li style="list-style-type:disc"><strong>Quy trình</strong>: đăng ký trực tuyến → đối soát → đào tạo ngắn (1–2h về an toàn, dịch vụ, sử dụng app).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-800e-b344-e56a8cb000e2" class="bulleted-list"><li style="list-style-type:disc"><strong>Không ký HĐLĐ</strong>, không có đào tạo nâng cao dài hạn.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8092-a992-d834ca87a304"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-80af-9b99-ff66659516e4" class=""><strong>4. 
Vận hành ngoài đường</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-803f-8595-ede9677d3219" class="bulleted-list"><li style="list-style-type:disc"><strong>Quy tắc ứng xử (Code of Conduct)</strong>: chính sách zero-tolerance.<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8086-9481-f8a1a9bf30a7" class="bulleted-list"><li style="list-style-type:circle">Gian lận → khóa vĩnh viễn.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80d6-932c-fd86c021bab2" class="bulleted-list"><li style="list-style-type:circle">Thái độ không chuẩn mực → khóa vĩnh viễn.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8042-ab71-fd0f930b81e4" class="bulleted-list"><li style="list-style-type:disc"><strong>KPI ẩn</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80a5-ad29-e18181418946" class="bulleted-list"><li style="list-style-type:circle">Tỷ lệ nhận chuyến &gt;80%.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8094-b399-d83cebd6de41" class="bulleted-list"><li style="list-style-type:circle">Tỷ lệ hủy chuyến &lt;20%.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80bc-8015-c29df8c38963" class="bulleted-list"><li style="list-style-type:disc"><strong>Phạt (nội bộ, 
không công bố)</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80ec-93a2-d396ae96e70c" class="bulleted-list"><li style="list-style-type:circle">Hủy chuyến nhiều → trừ toàn bộ thưởng ngày/tuần.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8009-ac0b-c1dd8a1d42fe" class="bulleted-list"><li style="list-style-type:circle">Dùng phần mềm gian lận → phạt tiền hoặc khóa app.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80a4-a9cb-c6ee8c5be338" class="bulleted-list"><li style="list-style-type:disc"><strong>App kiểm soát</strong>: GPS, AI chống gian lận, phát hiện đa thiết bị.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8095-97bb-d9da7d15fe7a"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-80de-8814-eb1829c0856c" class=""><strong>5. 
Thu nhập Gross vs Net</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8079-ac45-e692a3edbbdc" class="bulleted-list"><li style="list-style-type:disc"><strong>GrabBike (full-time)</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80ec-9e2e-f7d52dca41ff" class="bulleted-list"><li style="list-style-type:circle">Gross: 12–15 triệu VND/tháng.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8016-852b-f209fcb74394" class="bulleted-list"><li style="list-style-type:circle">Net sau chi phí: 9–11 triệu.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8035-a0f2-cbe02e1565c1" class="bulleted-list"><li style="list-style-type:circle">Thu nhập theo giờ: 40–50k VND.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8088-806b-e1e59ae4ea90" class="bulleted-list"><li style="list-style-type:disc"><strong>GrabCar (full-time)</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80e4-b07e-e67e0fb9b8f1" class="bulleted-list"><li style="list-style-type:circle">Gross: 25–30 triệu VND/tháng.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80d8-9939-de1406a0b159" class="bulleted-list"><li style="list-style-type:circle">Net sau chi phí: 13–17 triệu.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-807a-9b4f-d5b649127c0e" class="bulleted-list"><li style="list-style-type:circle">Thu nhập theo giờ: 80–100k VND.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80f0-a9e4-f1ac630106d5" class="bulleted-list"><li style="list-style-type:disc"><strong>Part-time (4–5h/ngày)</strong>: GrabBike net 4–6 triệu/tháng, 
GrabCar net 7–9 triệu/tháng.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8086-96b6-e10f4408196d"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-8039-8992-c7041f1c6b10" class=""><strong>6. Chi phí &amp; Khấu hao</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80e2-bb5b-cc87ce2ad3a7" class="bulleted-list"><li style="list-style-type:disc"><strong>Hoa hồng Grab</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80a5-8cf8-e2e4fafebc88" class="bulleted-list"><li style="list-style-type:circle">GrabBike: 20% mỗi cuốc.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8002-a7d0-e8947e2b7c70" class="bulleted-list"><li style="list-style-type:circle">GrabCar: 25% mỗi cuốc.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8072-aabe-fadaf30b9e8c" class="bulleted-list"><li style="list-style-type:disc"><strong>Chi phí tài xế gánh</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-800f-b1e8-e208b217fee5" class="bulleted-list"><li style="list-style-type:circle">GrabBike: xăng 3–4m, bảo trì 500k, khấu hao 1–2m → tổng 5–6m/tháng.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80ee-9fd5-dd8188db4665" class="bulleted-list"><li style="list-style-type:circle">GrabCar: xăng/dầu 7–10m, bảo trì 2–3m, khấu hao 4–6m, cầu đường 1–2m → tổng 15–20m/tháng.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80e7-b0cd-df93a5876961" class="bulleted-list"><li style="list-style-type:disc"><strong>Chi phí ẩn</strong>: SIM/4G (200–300k), phí app, mất thưởng do KPI không đạt.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80c1-8715-eac562ee1a34"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-8083-98a1-cc9f108db5f7" class=""><strong>7. 
Khiếu nại &amp; Trải nghiệm (CX &amp; 
Driver Complaints)</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-803c-a8db-c6f4254adf91" class="bulleted-list"><li style="list-style-type:disc"><strong>Tài xế phàn nàn</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-803e-ae77-c60809c6711c" class="bulleted-list"><li style="list-style-type:circle">Hoa hồng cao, thưởng thiếu minh bạch.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-807b-a69f-fb9628886d76" class="bulleted-list"><li style="list-style-type:circle">Khóa app đột ngột, khó kháng nghị.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80e7-9833-df0e9f2a8031" class="bulleted-list"><li style="list-style-type:circle">Chậm chi trả bảo hiểm, không bù thu nhập.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8074-8de2-d4275b376fe8" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách hàng phàn nàn</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-808e-b47a-e5c779a8fb85" class="bulleted-list"><li style="list-style-type:circle">Hủy chuyến phút chót.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-807a-9eef-eccd383c2aae" class="bulleted-list"><li style="list-style-type:circle">Giá tăng gấp 2–3 lần giờ cao điểm (surge).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80ad-8589-f11b4b8da545" class="bulleted-list"><li style="list-style-type:circle">Một số trường hợp thái độ phục vụ kém.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80d1-bd96-ee37ae390470" class="bulleted-list"><li style="list-style-type:disc"><strong>CSKH</strong>: hotline phản hồi chậm, 
tài xế chờ 3–7 ngày để xử lý khiếu nại.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80da-9997-c76b63fc072d"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-809a-95aa-f3827b8df275" class=""><strong>8. Thu hút &amp; Giữ chân tài xế</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80a9-99ca-efc7c032104b" class="bulleted-list"><li style="list-style-type:disc"><strong>Nguồn cuốc lớn nhất thị trường</strong>: đảm bảo thu nhập cơ bản.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80c4-82cd-eddbb8bbd7b7" class="bulleted-list"><li style="list-style-type:disc"><strong>Missions &amp; Incentives</strong>: KPI thưởng hàng tuần.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80cd-a686-f88164852bbf" class="bulleted-list"><li style="list-style-type:disc"><strong>Referral Program</strong>: thưởng giới thiệu tài xế mới.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80ae-91f7-c028f58d5a07" class="bulleted-list"><li style="list-style-type:disc"><strong>Hệ sinh thái đa dịch vụ</strong>: Ride + Food + Mart + Express.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80ad-9a77-e84fc3bf68a3" class="bulleted-list"><li style="list-style-type:disc"><strong>Retention issue</strong>: theo ước tính, 20–30% tài xế mới rời bỏ trong 6 tháng do áp lực và thu nhập không ổn định.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80be-bfa9-c05c0e324722"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-80fb-b97f-c10ad42501c3" class=""><strong>9. 
Tuân thủ pháp lý</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8071-8e7a-f37a10e6f797" class="bulleted-list"><li style="list-style-type:disc">Chịu quản lý theo <strong>Nghị định 10/2020</strong> và <strong>Nghị định 158/2024</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8063-a2b9-d2ea95af4ec7" class="bulleted-list"><li style="list-style-type:disc">Bị phân loại gần như doanh nghiệp vận tải → phải xuất hóa đơn điện tử, niêm yết giá, hiển thị thông tin tài xế/xe trên app.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-809d-99ac-fa144884c6f7" class="bulleted-list"><li style="list-style-type:disc">Từng tranh chấp pháp lý với Vinasun về định nghĩa “taxi công nghệ”.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80d1-8d22-d656a30a8ba2" class="bulleted-list"><li style="list-style-type:disc">Hiện nay: pháp lý siết chặt, Grab phải vận hành như taxi điện tử.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8026-a40b-ef553018ccd1"/></div><div style="display:contents" dir="auto"><h2 id="280c5e6f-95bd-8044-ba94-c7307885fa8b" class=""><strong>Đánh giá trung tính</strong></h2></div><div style="display:contents" dir="auto"><p id="280c5e6f-95bd-80ed-8e07-e91660f712c7" class=""><strong>Ưu điểm</strong></p></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8089-a179-cd99b076e83e" class="bulleted-list"><li style="list-style-type:disc">Thị phần lớn, cuốc nhiều, dễ kiếm khách.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80a8-b489-f4a06fd3503f" class="bulleted-list"><li style="list-style-type:disc">Có bảo hiểm tai nạn cơ bản.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-809a-9c1c-fbb851a50c56" class="bulleted-list"><li style="list-style-type:disc">Hệ sinh thái mạnh, 
tạo nhiều nguồn thu nhập khác nhau.</li></ul></div><div style="display:contents" dir="auto"><p id="280c5e6f-95bd-80e6-90eb-ebfe07e85797" class=""><strong>Nhược điểm</strong></p></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80f6-b9d7-f46d31b8b39c" class="bulleted-list"><li style="list-style-type:disc">Không có an sinh chính thức, thu nhập biến động.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-800a-acd5-c6aae068e1f5" class="bulleted-list"><li style="list-style-type:disc">Hoa hồng cao, chi phí ẩn lớn.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-805f-af49-c7416125f703" class="bulleted-list"><li style="list-style-type:disc">Chính sách phạt và thưởng thiếu minh bạch, áp lực KPI.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80db-9f6a-d28387804c37" class="bulleted-list"><li style="list-style-type:disc">CSKH cho tài xế còn yếu, retention kém.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8000-9f44-fb1a7646b393"/></div><div style="display:contents" dir="auto"><h2 id="280c5e6f-95bd-8086-81d3-f6467ca5bc10" class=""><strong>Cơ hội cho UniTaxi (so với Grab)</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-804b-96ac-f34ae23b5f7c" class="numbered-list" start="1"><li><strong>Minh bạch tuyệt đối</strong>: công bố rõ % hoa hồng, bảng phạt, 
công thức thưởng.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-80f0-83e3-f8be9db8d61c" class="numbered-list" start="2"><li><strong>An sinh xã hội</strong>: ký HĐLĐ với BHXH/BHYT/BHTN cho tài xế nòng cốt.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-80af-852a-f52bbaf0e01f" class="numbered-list" start="3"><li><strong>Bảo hiểm nghề nghiệp</strong>: chi trả thu nhập khi tài xế nghỉ do tai nạn/ốm.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-8015-8ef9-ffa42cb47898" class="numbered-list" start="4"><li><strong>Cam kết thu nhập tối thiểu</strong>: 400–500k/ngày cho xe máy, 1–1,2 triệu/ngày cho ô tô.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-80ab-9ae9-e12fa02189b0" class="numbered-list" start="5"><li><strong>Chính sách phạt hỗ trợ</strong>: cảnh báo + đào tạo trước khi khóa app.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-8096-b04e-e9269c6302aa" class="numbered-list" start="6"><li><strong>Tối ưu chi phí</strong>: thẻ xăng/sạc ưu đãi, bảo trì định kỳ “trọn gói theo km”.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-80fa-9417-c3a785e26359" class="numbered-list" start="7"><li><strong>Đào tạo &amp; 
thăng hạng</strong>: hệ thống Bronze–Platinum gắn với thưởng + quyền lợi.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-8059-830f-e94853f29b52" class="numbered-list" start="8"><li><strong>Retention mạnh hơn</strong>: xây dựng gói phúc lợi gia đình (học phí, y tế), tạo lý do tài xế gắn bó lâu dài.</li></ol></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8043-ab89-eb66c4b13eb2"/></div><div style="display:contents" dir="auto"><h1 id="280c5e6f-95bd-809b-984d-e56f65031355" class=""><strong>Be Group</strong></h1></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8054-97dc-f12da2fad9c0"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-808e-b621-d7fa06923bad" class=""><strong>1. 
Bảo hiểm &amp; An sinh</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8040-86d9-c006796ac549" class="bulleted-list"><li style="list-style-type:disc"><strong>Không có BHXH/BHYT/BHTN</strong>: tài xế được phân loại là đối tác, không ký HĐLĐ.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8018-883b-ee7d6412c40b" class="bulleted-list"><li style="list-style-type:disc"><strong>Bảo hiểm tai nạn chuyến đi</strong>: Be công bố có hợp tác với các công ty bảo hiểm, nhưng mức quyền lợi không rõ ràng bằng Grab.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-808e-a56c-fb95521f10d1" class="bulleted-list"><li style="list-style-type:disc"><strong>Không có bảo hiểm mất thu nhập</strong>: tài xế bị tai nạn/ốm đau vẫn tự gánh chi phí cơ hội.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80c0-b626-d8cddf4bf31e" class="bulleted-list"><li style="list-style-type:disc"><strong>Hạn chế</strong>: bảo hiểm hiện tại chủ yếu bảo vệ khách hơn là tài xế.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8073-be5c-e7b3c15cbdb6"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-8011-9d27-fbafa1bc08c4" class=""><strong>2. 
Chế độ &amp; Phúc lợi (Compensation &amp; Benefits)</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8074-b6ce-f6d5de472452" class="bulleted-list"><li style="list-style-type:disc"><strong>Không có lương cơ bản</strong>: toàn bộ thu nhập từ cước + thưởng.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80dd-b3a5-c27392657a4a" class="bulleted-list"><li style="list-style-type:disc"><strong>Incentives</strong>: thường xuyên có thưởng theo khu vực/khung giờ (ví dụ: thêm 20–40k/chuyến trong giờ cao điểm HN/HCM).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-805c-9a93-c9dad9a8872e" class="bulleted-list"><li style="list-style-type:disc"><strong>Chương trình hạng thẻ</strong>: Đồng, Bạc, Vàng, Kim cương. Tài xế hạng cao được ưu tiên cuốc và thêm thưởng.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-800f-9c8b-c0dd2fc08327" class="bulleted-list"><li style="list-style-type:disc"><strong>Ưu đãi đối tác</strong>: hỗ trợ mua xe trả góp, giảm giá xăng/dầu (2–5%), gói điện thoại.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80b0-b570-e5db4495a14c" class="bulleted-list"><li style="list-style-type:disc"><strong>Không có ngày nghỉ có lương, không hỗ trợ y tế định kỳ</strong>.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8058-ba32-fc171f22b872"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-8066-b4a3-eefb60eb7659" class=""><strong>3. 
Tuyển dụng &amp; Đào tạo</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-802d-ac30-eec03a692fb6" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều kiện</strong>: GPLX hợp lệ, CCCD, hồ sơ phương tiện.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80bb-ba5d-ea1e9216d290" class="bulleted-list"><li style="list-style-type:disc"><strong>Chi phí gia nhập</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80cc-8c38-cad531275280" class="bulleted-list"><li style="list-style-type:circle">BeBike: ~300k–500k (đồng phục, nón bảo hiểm).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-809c-b069-f70012a89f32" class="bulleted-list"><li style="list-style-type:circle">BeCar: 2–3 triệu (tem, đăng ký, thủ tục ban đầu).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80b3-a359-e26c44e451ef" class="bulleted-list"><li style="list-style-type:disc"><strong>Đào tạo</strong>: qua <strong>BeAcademy</strong> (online/offline), nội dung: kỹ năng dịch vụ, an toàn, chống gian lận.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80d5-a88b-f04fe6262a9e" class="bulleted-list"><li style="list-style-type:disc"><strong>Tốc độ gia nhập</strong>: 1–3 ngày có thể chạy.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8015-9101-fb28dc8a47a3" class="bulleted-list"><li style="list-style-type:disc"><strong>Không ký HĐLĐ</strong>: quan hệ cộng tác.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80e9-a519-f14010419298"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-8081-8610-d509972e1f1d" class=""><strong>4. 
Vận hành ngoài đường</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-808b-bd7c-eca4874b316c" class="bulleted-list"><li style="list-style-type:disc"><strong>Yêu cầu</strong>: tỷ lệ nhận chuyến &gt;70%, tỷ lệ hủy &lt;20%.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-806e-b501-c56fc6c7fde9" class="bulleted-list"><li style="list-style-type:disc"><strong>Đồng phục</strong>: bắt buộc (áo vàng Be).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8038-a9ea-d581a408a4d3" class="bulleted-list"><li style="list-style-type:disc"><strong>Quy định kỷ luật</strong>: hủy chuyến quá nhiều hoặc gian lận (dùng phần mềm) sẽ bị khóa app.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80e7-b8ea-c12f98a4cd7b" class="bulleted-list"><li style="list-style-type:disc"><strong>Mềm hơn Grab</strong>: Be ít khi khóa vĩnh viễn ngay, thường phạt bằng hạn chế cuốc trước.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80e1-b922-dc9328590e2b"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-8093-85ce-e2196233e55c" class=""><strong>5. 
Thu nhập Gross vs Net</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-804b-94b3-f6373fb3f259" class="bulleted-list"><li style="list-style-type:disc"><strong>BeBike (full-time)</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80d7-9f22-f58954d4c2b9" class="bulleted-list"><li style="list-style-type:circle">Gross: 10–13 triệu VND/tháng.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8022-949d-e298b04a56a9" class="bulleted-list"><li style="list-style-type:circle">Net: 7–9 triệu (sau xăng 3–4m, hoa hồng 18–20%).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80d1-a170-d908e4471a16" class="bulleted-list"><li style="list-style-type:circle">Thu nhập theo giờ: 35–45k VND.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-802c-b0d1-f681229360a7" class="bulleted-list"><li style="list-style-type:disc"><strong>BeCar (full-time)</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-807c-bb73-ebc351654f40" class="bulleted-list"><li style="list-style-type:circle">Gross: 20–25 triệu VND/tháng.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80bf-a8dc-eb66b689d4bc" class="bulleted-list"><li style="list-style-type:circle">Net: 11–14 triệu (sau hoa hồng 25%, xăng/dầu 7–9m, bảo trì 2–3m).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8006-bf0a-e835022b3984" class="bulleted-list"><li style="list-style-type:circle">Thu nhập theo giờ: 70–90k VND.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8070-b6a0-c91777bbc61a" class="bulleted-list"><li style="list-style-type:disc"><strong>Part-time</strong>: 4–6 triệu (Bike), 
6–8 triệu (Car).</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8042-b461-c34f7082cb3a"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-8014-a098-d0f46b5f80b7" class=""><strong>6. Chi phí &amp; Khấu hao</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8049-9158-f44eca9e711b" class="bulleted-list"><li style="list-style-type:disc"><strong>Hoa hồng Be</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8020-ac16-da9f3a4a8810" class="bulleted-list"><li style="list-style-type:circle">BeBike: 18–20%.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-809a-875b-d00a2d950ef4" class="bulleted-list"><li style="list-style-type:circle">BeCar: 25%.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8022-8b66-cd52ddd1ad23" class="bulleted-list"><li style="list-style-type:disc"><strong>Chi phí vận hành</strong>: gần tương tự Grab (xăng, bảo trì, khấu hao).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80ac-af08-d5a7a1f2a0df" class="bulleted-list"><li style="list-style-type:disc"><strong>Chi phí gia nhập</strong> thấp hơn Grab, nhất là BeBike.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8072-9e71-eb1a033b1628" class="bulleted-list"><li style="list-style-type:disc"><strong>Chi phí ẩn</strong>: mất thưởng nếu không đạt KPI, chi phí tự trang bị bảo hiểm.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-808f-8fda-e5aa2af4b17a"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-808e-b8dc-d31adf462326" class=""><strong>7. 
Khiếu nại &amp; Trải nghiệm (CX &amp; Driver Complaints)</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8027-91c0-ded0fe01f1ec" class="bulleted-list"><li style="list-style-type:disc"><strong>Tài xế phàn nàn</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-802f-aef4-dcc957b1b122" class="bulleted-list"><li style="list-style-type:circle">Số lượng cuốc ít hơn Grab, nhất là ở tỉnh.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8003-b804-f1fd8af2b9b4" class="bulleted-list"><li style="list-style-type:circle">Thưởng thay đổi nhanh, khó dự đoán thu nhập.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80d1-9a72-f936db12a209" class="bulleted-list"><li style="list-style-type:circle">App đôi khi lỗi định vị hoặc thanh toán chậm.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80fc-960f-e9e9d5d15c62" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách hàng phàn nàn</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80f7-9ce6-fe5fb3daab1d" class="bulleted-list"><li style="list-style-type:circle">Thường khó đặt được xe ngoài HN/HCM.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-804c-b851-ed1c20a6fe95" class="bulleted-list"><li style="list-style-type:circle">Một số phản ánh dịch vụ không đồng đều (chất lượng xe, thái độ).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80a8-a58e-dea6f99b051d" class="bulleted-list"><li style="list-style-type:disc"><strong>CSKH</strong>: hotline hoạt động nhưng phản hồi chậm hơn Grab.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8099-a4e7-dc715e612808"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-8051-ab51-c85bbd52eb97" class=""><strong>8. 
Thu hút &amp; Giữ chân tài xế</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8046-b208-e7a78c7111b9" class="bulleted-list"><li style="list-style-type:disc"><strong>Chiến lược nội địa</strong>: truyền thông “ứng dụng Việt, hỗ trợ tài xế Việt”.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8044-ab21-e614cf382402" class="bulleted-list"><li style="list-style-type:disc"><strong>Thưởng gia nhập</strong>: từng có chính sách thưởng khi tài xế mới đạt số chuyến đầu tiên.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8061-8966-e5f62f2370b2" class="bulleted-list"><li style="list-style-type:disc"><strong>Chương trình hạng thẻ</strong>: giữ chân tài xế bằng hệ thống thứ bậc.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8025-a82e-d2bebd885d31" class="bulleted-list"><li style="list-style-type:disc"><strong>Ưu đãi đầu vào</strong>: mua xe trả góp, gói điện thoại giá rẻ.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8090-8a7c-f253543e1492" class="bulleted-list"><li style="list-style-type:disc"><strong>Điểm yếu</strong>: thiếu cam kết thu nhập → tài xế giỏi dễ chuyển sang Grab hoặc Xanh SM.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80c9-b17a-d628ab11e4c7"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-8070-bd72-c2fd57a9664a" class=""><strong>9. 
Tuân thủ pháp lý</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80d7-a0f1-d5e33319994c" class="bulleted-list"><li style="list-style-type:disc">Hoạt động dưới khung <strong>Nghị định 10/2020</strong> và <strong>Nghị định 158/2024</strong>, giống Grab.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8009-be68-c674fda83bd2" class="bulleted-list"><li style="list-style-type:disc">Bị quản lý như taxi điện tử → phải xuất hóa đơn điện tử, niêm yết cước, cung cấp thông tin minh bạch cho khách.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8081-b31f-f9a2adfc2dbe" class="bulleted-list"><li style="list-style-type:disc">Không gặp tranh chấp pháp lý lớn như Grab, nhưng chịu áp lực khi cạnh tranh thị phần với Xanh SM.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80c8-8d83-c7e9046459dd"/></div><div style="display:contents" dir="auto"><h2 id="280c5e6f-95bd-8094-9ee4-e872863b5245" class=""><strong>Đánh giá trung tính</strong></h2></div><div style="display:contents" dir="auto"><p id="280c5e6f-95bd-80a8-87aa-e28af1c16e0b" class=""><strong>Ưu điểm</strong></p></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8069-8c75-d1ded6f5abd3" class="bulleted-list"><li style="list-style-type:disc">Linh hoạt hơn Grab trong chính sách vận hành.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-805d-853c-d3dd8eaf4342" class="bulleted-list"><li style="list-style-type:disc">Hoa hồng thấp hơn GrabBike một chút (~18–20%).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8071-ac3f-d01e8de9aeb2" class="bulleted-list"><li style="list-style-type:disc">Chi phí gia nhập thấp, dễ thu hút tài xế mới.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8096-983c-f9d9d4e9d28a" class="bulleted-list"><li style="list-style-type:disc">Thương hiệu nội địa, 
có thể tùy biến chính sách.</li></ul></div><div style="display:contents" dir="auto"><p id="280c5e6f-95bd-80e2-98e1-c594681dd8d1" class=""><strong>Nhược điểm</strong></p></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80b8-9507-f6992eaef0a8" class="bulleted-list"><li style="list-style-type:disc">Thị phần nhỏ hơn, ít cuốc hơn Grab và Xanh SM.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80eb-8d84-d16e54dbaf4b" class="bulleted-list"><li style="list-style-type:disc">Không có an sinh bắt buộc, thu nhập biến động.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80a2-b1d0-c673e991e805" class="bulleted-list"><li style="list-style-type:disc">Thưởng thay đổi liên tục, thiếu ổn định.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-805a-9ded-e77b558198e1" class="bulleted-list"><li style="list-style-type:disc">CSKH chưa hiệu quả, khách phàn nàn dịch vụ không đồng đều.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-800a-940e-cfb23678bb83"/></div><div style="display:contents" dir="auto"><h2 id="280c5e6f-95bd-8081-bcf6-d07d3618a459" class=""><strong>Cơ hội cho UniTaxi (so với Be Group)</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-80f2-a3ab-eb5e60be34f1" class="numbered-list" start="1"><li><strong>Khắc phục điểm yếu thu nhập</strong>: công bố cam kết thu nhập tối thiểu/ca để tạo niềm tin.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-8022-976f-f76b268c7e5a" class="numbered-list" start="2"><li><strong>An sinh chính thức</strong>: ký HĐLĐ cho tài xế nòng cốt, 
đóng BHXH/BHYT/BHTN.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-8092-ac46-e70a26cf1b5e" class="numbered-list" start="3"><li><strong>Bảo hiểm thu nhập</strong>: hỗ trợ khi tài xế nghỉ do tai nạn/ốm đau.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-80fc-aaef-f36ee1ca3e88" class="numbered-list" start="4"><li><strong>Đảm bảo số cuốc</strong>: hợp tác với doanh nghiệp, sân bay, khách sạn để tạo cuốc ổn định (B2B).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-806d-b603-c70149957756" class="numbered-list" start="5"><li><strong>Ứng dụng ổn định hơn</strong>: tập trung vào hạ tầng công nghệ mượt mà.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-80d2-83ae-c24480a088ca" class="numbered-list" start="6"><li><strong>Retention</strong>: xây dựng gói phúc lợi gia đình (y tế, học phí), hệ thống thăng hạng minh bạch.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-804f-91fa-ed44fa7d7343" class="numbered-list" start="7"><li><strong>Thương hiệu mạnh</strong>: định vị UniTaxi là “ứng dụng Việt có an sinh &amp; thu nhập ổn định” → khác biệt với cả Be và Grab.</li></ol></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80ab-b2de-f76b02d0535d"/></div><div style="display:contents" dir="auto"><h1 id="280c5e6f-95bd-8033-8bbd-cc7456af5871" class=""><strong>Xanh SM (GSM) </strong></h1></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8010-aa09-d2e0afc67787"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-8047-8994-de0b1cd45e1a" class=""><strong>1. 
Bảo hiểm &amp; An sinh</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80fb-b488-de382863acb1" class="bulleted-list"><li style="list-style-type:disc"><strong>Có HĐLĐ chính thức</strong>: tài xế là nhân viên, được đóng <strong>BHXH, BHYT, BHTN từ ngày đầu</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-806b-bb32-d0a7b1e2cf9e" class="bulleted-list"><li style="list-style-type:disc"><strong>Bảo hiểm tai nạn bổ sung</strong>: áp dụng cho lái xe và hành khách, chi tiết theo hợp đồng với công ty bảo hiểm (chưa công bố mức cụ thể).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80d2-be01-f436327de8ed" class="bulleted-list"><li style="list-style-type:disc"><strong>Ưu thế</strong>: là hãng duy nhất hiện tại ở VN cung cấp <strong>bảo hiểm xã hội bắt buộc + an sinh dài hạn</strong> cho tài xế.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80b6-9511-c195d0d18dfc"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-80bf-9574-ee3041f9dc2e" class=""><strong>2. 
Chế độ &amp; Phúc lợi (Compensation &amp; Benefits)</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80a3-8c1c-d14381c996ab" class="bulleted-list"><li style="list-style-type:disc"><strong>Có lương cơ bản</strong>: trả theo vùng (tối thiểu vùng).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80d2-a004-ca1c4416c1fb" class="bulleted-list"><li style="list-style-type:disc"><strong>Cam kết thu nhập tối thiểu</strong>: ví dụ ~600.000đ/ngày trong 60 ngày đầu ở HN/HCM.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8066-8047-c00e8ebbe313" class="bulleted-list"><li style="list-style-type:disc"><strong>Thưởng</strong>: theo doanh số, chất lượng dịch vụ, thâm niên.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80ad-8f0b-dd87c22e7044" class="bulleted-list"><li style="list-style-type:disc"><strong>Xe &amp; đồng phục</strong>: VinFast cung cấp (xe máy điện/ô tô điện).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80d7-805f-c2a12fedd4d2" class="bulleted-list"><li style="list-style-type:disc"><strong>Ưu đãi tài chính</strong>: mua xe trả góp, hỗ trợ thuê pin (ví dụ: 650.000đ/tháng cho pin không giới hạn km nếu đạt 180 chuyến/tháng).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80c6-893a-fbcece15b0fe" class="bulleted-list"><li style="list-style-type:disc"><strong>Hạn chế</strong>: thu nhập phụ thuộc KPI doanh số → nếu không đạt sẽ bị truy thu phần thiếu.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8095-b7a3-c4aeb0d7b423"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-80b4-8c90-dad1cbb1ca34" class=""><strong>3. 
Tuyển dụng &amp; Đào tạo</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8057-9e58-d86882c41e43" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều kiện</strong>: GPLX hợp lệ (A1 cho xe máy, B2+ cho ô tô), lý lịch tư pháp, giấy khám sức khỏe.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80c7-925a-da64e0302a83" class="bulleted-list"><li style="list-style-type:disc"><strong>Quy trình</strong>: phỏng vấn, ký HĐLĐ, đào tạo tập trung.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8079-85b3-f722a016131d" class="bulleted-list"><li style="list-style-type:disc"><strong>Đào tạo</strong>: chuyên sâu hơn Grab/Be → kỹ năng vận hành xe điện, quy trình sạc, dịch vụ khách hàng, đồng phục.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8027-9df3-c4cf9199cd39" class="bulleted-list"><li style="list-style-type:disc"><strong>Chi phí gia nhập</strong>: gần như bằng 0 (xe, đồng phục do công ty cấp).</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8040-a8c5-cf7d46b37f06"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-80b9-818f-d50970974d9f" class=""><strong>4. 
Vận hành ngoài đường</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8048-90f5-cc44a28bb86f" class="bulleted-list"><li style="list-style-type:disc"><strong>Quy định nghiêm ngặt</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-806b-a1e3-c65fbae86fc1" class="bulleted-list"><li style="list-style-type:circle">Tỷ lệ nhận chuyến &gt;70%.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80c4-b9e4-d2f6ea61327c" class="bulleted-list"><li style="list-style-type:circle">Doanh số tối thiểu/ngày (HN: ~280.000đ), nếu không đạt sẽ bị truy thu.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-807d-af42-d6d2c98b9589" class="bulleted-list"><li style="list-style-type:disc"><strong>Auto-assign</strong>: nếu tỷ lệ nhận thấp, hệ thống tự động phân cuốc đến hết ngày.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8091-a0fa-cf566976a602" class="bulleted-list"><li style="list-style-type:disc"><strong>Quản lý chặt</strong>: đồng phục, vệ sinh xe, thái độ phục vụ.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8000-b6a2-d8b1288a728d" class="bulleted-list"><li style="list-style-type:disc"><strong>Kỷ luật</strong>: vi phạm nhiều lần → thu hồi xe, chấm dứt hợp đồng.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80c9-ac09-ebd87f21d931"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-803c-b230-c6208962d72a" class=""><strong>5. 
Thu nhập Gross vs Net</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80dd-99d0-d7abfcd3da1e" class="bulleted-list"><li style="list-style-type:disc"><strong>Xanh SM Car (full-time)</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8071-aa21-c5feed259bc3" class="bulleted-list"><li style="list-style-type:circle">Gross: 15–30 triệu VND/tháng (theo quảng bá).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-805f-a005-e99787ed2281" class="bulleted-list"><li style="list-style-type:circle">Net: 12–20 triệu (sau khi trừ truy thu, bảo hiểm, thuế TNCN).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8080-bada-e245fb6a2298" class="bulleted-list"><li style="list-style-type:disc"><strong>Xanh SM Bike Platform</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8075-92a3-d2edd9b807ff" class="bulleted-list"><li style="list-style-type:circle">Chia sẻ doanh số 80% trong 2 năm đầu.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8069-ab18-f3ffc4fc3998" class="bulleted-list"><li style="list-style-type:circle">Ước tính thu nhập ~18 triệu VND/tháng nếu đạt KPI (180+ chuyến/tháng).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8065-851a-cd079446afc4" class="bulleted-list"><li style="list-style-type:disc"><strong>Ưu thế</strong>: chi phí nhiên liệu gần như 0 (điện rẻ hơn xăng 40–50%).</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8009-8960-d732dd4031a0"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-80a6-8152-ea6f34dfb952" class=""><strong>6. 
Chi phí &amp; Khấu hao</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80fd-8969-e3d0cec452b3" class="bulleted-list"><li style="list-style-type:disc"><strong>Xe VinFast</strong>: cấp cho tài xế, không phải tự mua (giảm rủi ro đầu tư ban đầu).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80af-8ab0-d1a30f5afe9f" class="bulleted-list"><li style="list-style-type:disc"><strong>Pin xe máy điện</strong>: hỗ trợ thuê pin hoặc miễn phí nếu đạt KPI.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8002-bb9b-f608a35b61f9" class="bulleted-list"><li style="list-style-type:disc"><strong>Chi phí cá nhân</strong>: ăn uống, SIM/4G (~200–300k/tháng).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-804a-8906-e9fa8895d65f" class="bulleted-list"><li style="list-style-type:disc"><strong>Chi phí ẩn</strong>: nếu không đạt doanh số → bị truy thu, làm thu nhập thực giảm.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-802c-8270-e220adf80e60"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-806f-ada8-d13a1485fe70" class=""><strong>7. 
Khiếu nại &amp; Trải nghiệm (CX &amp; Driver Complaints)</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8094-a637-f37279a4f6ed" class="bulleted-list"><li style="list-style-type:disc"><strong>Tài xế phàn nàn</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80be-8df9-dcb2137e6d94" class="bulleted-list"><li style="list-style-type:circle">Áp lực KPI cao, bị truy thu khi không đạt doanh số.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80dd-8d70-c46076b011b1" class="bulleted-list"><li style="list-style-type:circle">Auto-assign gây khó chịu vì thiếu linh hoạt.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80e5-a1d8-d27dea60f43e" class="bulleted-list"><li style="list-style-type:circle">Phụ thuộc vào hạ tầng sạc → mất thời gian, giảm số chuyến/ngày.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-807d-9342-c33b5d2c33af" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách hàng</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80f6-a2d1-d94b26beeb23" class="bulleted-list"><li style="list-style-type:circle">Đánh giá cao dịch vụ (xe mới, sạch, đồng phục, thái độ).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8091-ab57-d58e83a5a02c" class="bulleted-list"><li style="list-style-type:circle">Phàn nàn nhỏ về thiếu xe ở một số khu vực giờ cao điểm.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80c5-98ef-fbabf82f23c1" class="bulleted-list"><li style="list-style-type:disc"><strong>CSKH</strong>: có hotline riêng cho khách &amp; tài xế, xử lý nhanh hơn Be.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8060-a3fb-eed0b08a25d8"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-80bf-81d8-fdaf0cc2eb16" class=""><strong>8. 
Thu hút &amp; Giữ chân tài xế</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-803b-82ad-c9cafd32d9f5" class="bulleted-list"><li style="list-style-type:disc"><strong>Lương cơ bản + BHXH</strong>: điểm mạnh nhất để thu hút tài xế so với Grab/Be.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8026-8b87-ff2c0dbcd877" class="bulleted-list"><li style="list-style-type:disc"><strong>Xe VinFast cấp sẵn</strong>: giảm chi phí gia nhập.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80e9-bf3d-f25a8c42fe40" class="bulleted-list"><li style="list-style-type:disc"><strong>Chính sách chia sẻ doanh số (80%)</strong>: hấp dẫn tài xế bike trong 2 năm đầu.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80ef-8000-cec347792096" class="bulleted-list"><li style="list-style-type:disc"><strong>Retention</strong>: tạo thương hiệu “Taxi xanh, an sinh đầy đủ” → giữ chân nhóm tài xế ưa ổn định.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80a9-9edc-d0a9056eb93a" class="bulleted-list"><li style="list-style-type:disc"><strong>Điểm yếu</strong>: kỷ luật gắt gao, áp lực doanh số có thể làm tài xế rời bỏ sau 3–6 tháng.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-803b-9faf-ffc86ea44fb4"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-800a-a91b-e4dd7f7de804" class=""><strong>9. 
Tuân thủ pháp lý</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-800d-902d-d077d176deb0" class="bulleted-list"><li style="list-style-type:disc">Xanh SM đăng ký là <strong>doanh nghiệp taxi chính thức</strong> → chịu quản lý hoàn toàn như taxi (Nghị định 10/2020, 158/2024).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-801b-800f-c9fda2cdca0e" class="bulleted-list"><li style="list-style-type:disc">Minh bạch hóa đơn, hiển thị tài xế, biển số, hành trình, giá cước.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8035-abfe-e66fc2761a1f" class="bulleted-list"><li style="list-style-type:disc">Có lợi thế <strong>được nhà nước ủng hộ</strong> vì thúc đẩy phương tiện xanh, giảm phát thải.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80c4-a07a-e4a2d5f36554"/></div><div style="display:contents" dir="auto"><h2 id="280c5e6f-95bd-80c2-8ea4-e0bb597a3a95" class=""><strong>Đánh giá trung tính</strong></h2></div><div style="display:contents" dir="auto"><p id="280c5e6f-95bd-8071-9bb3-d8a0bcd9d8e0" class=""><strong>Ưu điểm</strong></p></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80c2-bf3c-e390c141b8fd" class="bulleted-list"><li style="list-style-type:disc">An sinh xã hội đầy đủ (BHXH, BHYT, BHTN).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-800b-965f-fafedc921c9f" class="bulleted-list"><li style="list-style-type:disc">Có lương cơ bản, cam kết thu nhập.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8009-8723-f2b3c0a74eb6" class="bulleted-list"><li style="list-style-type:disc">Xe &amp; 
đồng phục cấp sẵn, chi phí đầu tư gần như bằng 0.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-800d-a019-d30bc99f137c" class="bulleted-list"><li style="list-style-type:disc">Thương hiệu xanh, dịch vụ cao cấp, được chính quyền ủng hộ.</li></ul></div><div style="display:contents" dir="auto"><p id="280c5e6f-95bd-8061-88fa-ded781c6b3ec" class=""><strong>Nhược điểm</strong></p></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80d8-a651-d0aa8563d270" class="bulleted-list"><li style="list-style-type:disc">Áp lực KPI và truy thu cao.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-807b-90f1-ce2460f3cd90" class="bulleted-list"><li style="list-style-type:disc">Auto-assign gây mất linh hoạt.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8057-b4c6-f457685c1578" class="bulleted-list"><li style="list-style-type:disc">Phụ thuộc hạ tầng sạc điện, rủi ro downtime.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8062-808c-d78968fc538f" class="bulleted-list"><li style="list-style-type:disc">Thu nhập thực tế bị giảm nếu không đạt doanh số.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8033-890b-eb97e55d98d1"/></div><div style="display:contents" dir="auto"><h2 id="280c5e6f-95bd-80d7-9135-c4822a1241a7" class=""><strong>Cơ hội cho UniTaxi (so với Xanh SM)</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-80ce-aff8-e6676cecd71e" class="numbered-list" start="1"><li><strong>Cam kết thu nhập linh hoạt</strong>: giữ mức tối thiểu nhưng không truy thu, thay bằng hỗ trợ đào tạo và phân tích dữ liệu cho tài xế.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-808f-b196-d1a6dc8372d9" class="numbered-list" start="2"><li><strong>Hỗ trợ đa dạng năng lượng</strong>: không chỉ xe điện, 
mà cả hybrid/xăng → giảm rủi ro hạ tầng.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-80bb-ac86-c06122e2594d" class="numbered-list" start="3"><li><strong>Bảo hiểm thu nhập</strong>: chi trả ngày công khi tài xế nghỉ vì ốm/ tai nạn.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-806c-bda1-f059c7ca6bfd" class="numbered-list" start="4"><li><strong>Retention mềm</strong>: giảm KPI cứng, thay bằng cơ chế thưởng linh hoạt → ít áp lực hơn GSM.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-808b-9275-f68a431742a6" class="numbered-list" start="5"><li><strong>Dịch vụ cao cấp + linh hoạt</strong>: tạo kênh “corporate ride” cho doanh nghiệp, khách sạn, sân bay.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-8017-b6e1-da73f5ad06c4" class="numbered-list" start="6"><li><strong>Khác biệt thương hiệu</strong>: UniTaxi có thể định vị là “ứng dụng công nghệ Việt với an sinh đầy đủ + linh hoạt hơn GSM”.</li></ol></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80eb-bb4b-c9e1afdff8ab"/></div><div style="display:contents" dir="auto"><h1 id="280c5e6f-95bd-809d-81bc-ee638ed145c9" class=""><strong>Vinasun Taxi</strong></h1></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80f5-b90b-c062d4c2357c"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-807e-a970-dd6dfd606e42" class=""><strong>1. 
Bảo hiểm &amp; An sinh</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-807e-a5cf-c5ace5d867c6" class="bulleted-list"><li style="list-style-type:disc"><strong>Có HĐLĐ chính thức</strong>: tài xế là nhân viên, hưởng đầy đủ <strong>BHXH, BHYT, BHTN</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80dc-9567-d4bac4119fcb" class="bulleted-list"><li style="list-style-type:disc"><strong>Bảo hiểm tai nạn nghề nghiệp</strong>: theo quy định pháp luật và hợp đồng lao động.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80fb-9ffb-e77077368ecf" class="bulleted-list"><li style="list-style-type:disc"><strong>Ưu thế</strong>: giống Xanh SM, Vinasun cung cấp <strong>an sinh xã hội đầy đủ</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80ca-b6ad-cd8776f39336" class="bulleted-list"><li style="list-style-type:disc"><strong>Hạn chế</strong>: không có bảo hiểm mất thu nhập bổ sung; phúc lợi hạn chế so với chuẩn ngành logistics/aviation.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8044-8aca-e20a51f8ce01"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-8060-bef3-d38c9f009abb" class=""><strong>2. 
Chế độ &amp; Phúc lợi (Compensation &amp; Benefits)</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-802d-890e-e1b08da0913f" class="bulleted-list"><li style="list-style-type:disc"><strong>Lương cơ bản</strong>: theo vùng (mức tối thiểu vùng).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8023-9a2e-dbbb3c2dd3ca" class="bulleted-list"><li style="list-style-type:disc"><strong>Thu nhập</strong> = lương cơ bản + % doanh thu (thường ~35–40% doanh thu cuốc xe).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80df-b05b-c296d5eb0b04" class="bulleted-list"><li style="list-style-type:disc"><strong>Thưởng</strong>: theo doanh số tháng, thái độ phục vụ, thành tích không vi phạm.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8056-8982-eef563a96c28" class="bulleted-list"><li style="list-style-type:disc"><strong>Đồng phục &amp; taxi</strong>: xe gắn logo Vinasun, tài xế được cấp đồng phục.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8067-ac76-e3dbcac60e28" class="bulleted-list"><li style="list-style-type:disc"><strong>Phúc lợi bổ sung</strong>: nghỉ phép có lương, thưởng lễ Tết.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-805c-a44e-d3d5619d2b48"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-80b7-9df8-d3e0edd5f912" class=""><strong>3. 
Tuyển dụng &amp; Đào tạo</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80b3-b73b-e4f4fbf2d173" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều kiện</strong>: GPLX B2 trở lên, lý lịch rõ ràng, sức khỏe tốt.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8025-ae09-e616f43e9e61" class="bulleted-list"><li style="list-style-type:disc"><strong>Quy trình</strong>: nộp hồ sơ → phỏng vấn → ký HĐLĐ → đào tạo.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8037-8a15-c66bde96e8b7" class="bulleted-list"><li style="list-style-type:disc"><strong>Đào tạo</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8027-8037-c90d63550440" class="bulleted-list"><li style="list-style-type:circle">Kỹ năng lái xe, dịch vụ khách hàng.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8030-827a-f6f6bfa3301a" class="bulleted-list"><li style="list-style-type:circle">Quy trình an toàn, ứng xử chuyên nghiệp.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-802d-be7d-f0b015aef61d" class="bulleted-list"><li style="list-style-type:disc"><strong>Chi phí gia nhập</strong>: thấp, chủ yếu chi phí hồ sơ.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-807a-b5e7-d8750b00f8e9"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-8064-b8ce-f44cd7970cbe" class=""><strong>4. 
Vận hành ngoài đường</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8030-b7b6-da4def3bd067" class="bulleted-list"><li style="list-style-type:disc"><strong>Quy định vận hành</strong>: tài xế phải trực tại bến đỗ, khu vực quy định hoặc nhận cuốc qua tổng đài/app Vinasun.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80d2-bd55-e755d60bc531" class="bulleted-list"><li style="list-style-type:disc"><strong>Doanh số tối thiểu</strong>: có yêu cầu mức doanh thu/ngày để đảm bảo lương cơ bản + % doanh thu.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8068-aa75-c4359a4ba582" class="bulleted-list"><li style="list-style-type:disc"><strong>Quản lý chặt</strong>: xe phải bảo dưỡng định kỳ, vệ sinh sạch sẽ, đồng phục chuẩn.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80c2-b7f2-ead23f12dbe8" class="bulleted-list"><li style="list-style-type:disc"><strong>Phạt nội bộ</strong>: vi phạm doanh thu, thái độ, hoặc gây sự cố sẽ bị phạt tiền hoặc kỷ luật.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80b0-a4ec-f62f090f4491"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-800f-86c6-d60284764193" class=""><strong>5. 
Thu nhập Gross vs Net</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-800a-b03e-dde91ca20822" class="bulleted-list"><li style="list-style-type:disc"><strong>Gross (toàn bộ doanh thu xe)</strong>: 30–40 triệu VND/tháng (taxi 4 chỗ, chạy full-time).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80f8-b015-ca3a1c98c364" class="bulleted-list"><li style="list-style-type:disc"><strong>Net (tài xế nhận)</strong>: 12–16 triệu VND/tháng sau khi trừ chi phí nộp lại công ty và khấu hao.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8020-82ee-cb63a1fcbc73" class="bulleted-list"><li style="list-style-type:disc"><strong>Thu nhập theo giờ</strong>: ~70–90k VND.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8069-98ae-f058a9b70b02" class="bulleted-list"><li style="list-style-type:disc"><strong>So sánh</strong>: thấp hơn GrabCar full-time (net 13–17 triệu), nhưng ổn định hơn do có lương cơ bản + BHXH.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8040-948d-f66e650d1072"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-80c3-b0c5-d88e6be84902" class=""><strong>6. 
Chi phí &amp; Khấu hao</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-802d-b861-c8a0144cad2f" class="bulleted-list"><li style="list-style-type:disc"><strong>Xe thuộc công ty</strong>: tài xế không phải mua xe riêng.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8019-9b15-d3b589d3fabf" class="bulleted-list"><li style="list-style-type:disc"><strong>Chi phí tài xế gánh</strong>: xăng/dầu, cầu đường, vệ sinh, đôi khi chia với công ty (tuỳ hợp đồng).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-804e-b25c-eea47c04cfd7" class="bulleted-list"><li style="list-style-type:disc"><strong>Khấu hao</strong>: công ty chịu, không đổ dồn lên tài xế.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8077-8fc1-d4f47bf63556" class="bulleted-list"><li style="list-style-type:disc"><strong>Chi phí ẩn</strong>: nộp doanh số không đủ → bị trừ lương, giảm thưởng.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80bf-a0f7-c772138f1353"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-806c-92ca-f80faa4bdfc8" class=""><strong>7. 
Khiếu nại &amp; Trải nghiệm (CX &amp; Driver Complaints)</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80da-943d-fab8d6256608" class="bulleted-list"><li style="list-style-type:disc"><strong>Tài xế phàn nàn</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80c9-8847-de98857652b9" class="bulleted-list"><li style="list-style-type:circle">Áp lực doanh số cao, phải chạy đủ chuyến để đạt mức lương ổn định.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8088-ba30-e11946c58d00" class="bulleted-list"><li style="list-style-type:circle">Cạnh tranh khốc liệt với Grab/Xanh SM.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80c7-a057-cbe1e44f306c" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách hàng phàn nàn</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8020-ad20-c92d8e350407" class="bulleted-list"><li style="list-style-type:circle">Giá cước taxi truyền thống thường cao hơn Grab/Xanh SM trong giờ thấp điểm.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80fe-8e78-f1efbb7269b5" class="bulleted-list"><li style="list-style-type:circle">Thỉnh thoảng tài xế từ chối cuốc ngắn.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-808f-b55e-c862bbc5237b" class="bulleted-list"><li style="list-style-type:disc"><strong>Điểm mạnh</strong>: khách quen đánh giá cao độ tin cậy, thương hiệu lâu đời.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-805a-b953-c8f50c1bd954"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-8040-a0f1-f973aefebba0" class=""><strong>8. 
Thu hút &amp; Giữ chân tài xế</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8017-8dc2-cccc54421f1a" class="bulleted-list"><li style="list-style-type:disc"><strong>An sinh xã hội + lương cơ bản</strong>: yếu tố giữ chân nhóm tài xế truyền thống.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8099-a1b9-df62a6c9070e" class="bulleted-list"><li style="list-style-type:disc"><strong>Đồng phục + xe công ty cấp</strong>: giảm rủi ro đầu tư.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80d8-9af1-ca8f2e47d37f" class="bulleted-list"><li style="list-style-type:disc"><strong>Thương hiệu lâu năm</strong>: tạo sự tin cậy với khách hàng doanh nghiệp (hợp đồng sân bay, khách sạn).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80c0-a19a-c16c3dd10860" class="bulleted-list"><li style="list-style-type:disc"><strong>Điểm yếu</strong>: thu nhập thấp hơn so với GrabCar/Xanh SM, khiến tài xế trẻ thường bỏ sang ứng dụng công nghệ.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80ea-9364-fefe88e1599f"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-804d-a4d0-f5657e306c9d" class=""><strong>9. 
Tuân thủ pháp lý</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8086-810a-e949e788b6cd" class="bulleted-list"><li style="list-style-type:disc">Hoạt động như taxi truyền thống, hoàn toàn trong khung <strong>Nghị định 10/2020</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8099-90da-c35987bcf702" class="bulleted-list"><li style="list-style-type:disc">Tuân thủ chặt về niêm yết giá, đồng hồ tính cước, hợp đồng lao động, an toàn.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-808a-8fe1-f901d010548e" class="bulleted-list"><li style="list-style-type:disc">Lợi thế pháp lý: ít tranh chấp như Grab, không bị “gọi là công nghệ hay taxi”.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8072-804e-d0acec4543c1"/></div><div style="display:contents" dir="auto"><h2 id="280c5e6f-95bd-80d7-90ae-d6adffc5b8f7" class=""><strong>Đánh giá trung tính</strong></h2></div><div style="display:contents" dir="auto"><p id="280c5e6f-95bd-80fb-8a49-d123d7428d46" class=""><strong>Ưu điểm</strong></p></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80e7-ac16-d4ff8bc5a1c4" class="bulleted-list"><li style="list-style-type:disc">Có HĐLĐ, BHXH đầy đủ, thu nhập ổn định.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80e5-8324-c9e9d041a9c6" class="bulleted-list"><li style="list-style-type:disc">Xe công ty cấp, không cần đầu tư ban đầu.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80c4-bd1c-caf93effbfa2" class="bulleted-list"><li style="list-style-type:disc">Thương hiệu lâu năm, 
uy tín với khách hàng doanh nghiệp.</li></ul></div><div style="display:contents" dir="auto"><p id="280c5e6f-95bd-807c-b7b9-ca18634712f0" class=""><strong>Nhược điểm</strong></p></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-802b-a476-fd3e893fdc03" class="bulleted-list"><li style="list-style-type:disc">Thu nhập thấp hơn so với GrabCar/Xanh SM.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-800d-9c29-e6f7e8c628fe" class="bulleted-list"><li style="list-style-type:disc">Áp lực doanh số, ít linh hoạt.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80ce-b2ef-dcc572f6b349" class="bulleted-list"><li style="list-style-type:disc">Cạnh tranh gay gắt với taxi công nghệ, thị phần suy giảm.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8067-a4bc-c50f2559676e"/></div><div style="display:contents" dir="auto"><h2 id="280c5e6f-95bd-8065-83c1-eeefe17f0063" class=""><strong>Cơ hội cho UniTaxi (so với Vinasun)</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-801c-a2ca-ef86a588fbe1" class="numbered-list" start="1"><li><strong>Kết hợp điểm mạnh truyền thống + công nghệ</strong>: có an sinh &amp; 
lương cơ bản như Vinasun, nhưng vận hành công nghệ như Grab/Xanh SM.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-803a-8eb9-d459307bf72d" class="numbered-list" start="2"><li><strong>Thu nhập cạnh tranh hơn</strong>: đặt ngưỡng cam kết tối thiểu cao hơn (15–18 triệu net/tháng cho tài xế full-time).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-8027-a673-c38bb99fae48" class="numbered-list" start="3"><li><strong>Linh hoạt hơn</strong>: không ép doanh số cứng, cho phép chọn ca làm việc linh hoạt.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-805c-b6a1-ceb10f3460c2" class="numbered-list" start="4"><li><strong>Ứng dụng mạnh</strong>: app thông minh, gắn KPI minh bạch thay vì chỉ áp lực doanh thu.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-802d-b345-e998b61c3dd2" class="numbered-list" start="5"><li><strong>Hợp đồng doanh nghiệp</strong>: giữ ưu thế khách sạn, sân bay nhưng bằng nền tảng công nghệ, tăng ổn định cuốc.</li></ol></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-805e-8619-c46bf9c558d2"/></div><div style="display:contents" dir="auto"><h1 id="280c5e6f-95bd-80a8-99e4-efc1e57a961c" class=""><strong>Mai Linh Taxi — Competition Benchmark</strong></h1></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80af-a164-e508760e35cf"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-8038-bd34-ccc862a77547" class=""><strong>1. 
Bảo hiểm &amp; An sinh</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8015-9504-c4708b7114cf" class="bulleted-list"><li style="list-style-type:disc"><strong>Có HĐLĐ chính thức</strong>: tài xế là nhân viên, được đóng <strong>BHXH, BHYT, BHTN</strong> đầy đủ.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8089-a167-f8de3649cb13" class="bulleted-list"><li style="list-style-type:disc"><strong>Bảo hiểm tai nạn nghề nghiệp</strong>: áp dụng theo luật lao động VN.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80ef-9d98-d35316df5a4b" class="bulleted-list"><li style="list-style-type:disc"><strong>Điểm cộng</strong>: cam kết an sinh giống Vinasun.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-800c-bd9e-eee99725fe94" class="bulleted-list"><li style="list-style-type:disc"><strong>Hạn chế</strong>: ít có gói bảo hiểm bổ sung (mất thu nhập, gia đình).</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8091-ab1e-fddcada7ec85"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-80f1-bd75-d8023445a4cb" class=""><strong>2. 
Chế độ &amp; Phúc lợi (Compensation &amp; Benefits)</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8055-a311-dbed931b18e4" class="bulleted-list"><li style="list-style-type:disc"><strong>Lương cơ bản</strong>: theo vùng, bằng hoặc cao hơn mức tối thiểu vùng.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-803d-a839-c8154dbca299" class="bulleted-list"><li style="list-style-type:disc"><strong>Thu nhập</strong> = lương cơ bản + % doanh thu (khoảng 30–35% doanh thu xe).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80f5-978e-d0a91ee52a74" class="bulleted-list"><li style="list-style-type:disc"><strong>Thưởng</strong>: doanh số, phục vụ tốt, dịp lễ/Tết.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80fb-a9e8-ea41ce4d14c9" class="bulleted-list"><li style="list-style-type:disc"><strong>Xe &amp; đồng phục</strong>: công ty cấp, đồng phục xanh đặc trưng.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-804c-82ab-d63617ec311c" class="bulleted-list"><li style="list-style-type:disc"><strong>Phúc lợi bổ sung</strong>: nghỉ phép có lương, bảo hiểm y tế, hỗ trợ khó khăn.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8043-b1da-e519e351bb63"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-80b2-bfdb-f47179ee8c96" class=""><strong>3. 
Tuyển dụng &amp; Đào tạo</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8064-ad91-e7c1069842af" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều kiện</strong>: GPLX B2+, hồ sơ pháp lý, sức khỏe đạt chuẩn.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80a1-8bd8-e27fd4afe595" class="bulleted-list"><li style="list-style-type:disc"><strong>Quy trình</strong>: nộp hồ sơ → phỏng vấn → ký HĐLĐ → đào tạo.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8066-bba0-fe0fdaab8b11" class="bulleted-list"><li style="list-style-type:disc"><strong>Đào tạo</strong>: lái xe an toàn, dịch vụ khách hàng, kỹ năng ứng xử.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8092-bdfd-d41236337c32" class="bulleted-list"><li style="list-style-type:disc"><strong>Chi phí gia nhập</strong>: công ty chịu phần lớn, tài xế chủ yếu tốn chi phí hồ sơ.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-801f-9ac2-fee731436b11"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-8051-8fb0-e0668724e62e" class=""><strong>4. 
Vận hành ngoài đường</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80f9-b026-e0565144ffee" class="bulleted-list"><li style="list-style-type:disc"><strong>Mô hình truyền thống</strong>: tài xế chạy theo tổng đài hoặc app Mai Linh (ra mắt từ 2017).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-800d-bdfa-c304896478b3" class="bulleted-list"><li style="list-style-type:disc"><strong>Doanh số tối thiểu</strong>: quy định mức doanh thu/ngày để giữ lương ổn định.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8079-8eb8-cdcc843c075c" class="bulleted-list"><li style="list-style-type:disc"><strong>Quản lý</strong>: xe vệ sinh sạch, đồng phục chuẩn, thái độ lịch sự.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8042-977b-f0b07d23347c" class="bulleted-list"><li style="list-style-type:disc"><strong>Phạt</strong>: vi phạm doanh số, từ chối khách, thái độ kém → phạt tiền hoặc kỷ luật.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80b0-9605-f75f64ee332e"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-808a-980f-f629bfbfa3d7" class=""><strong>5. 
Thu nhập Gross vs Net</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80d8-8f02-e723854868bc" class="bulleted-list"><li style="list-style-type:disc"><strong>Gross (doanh thu xe)</strong>: 25–35 triệu VND/tháng (xe 4 chỗ, chạy full-time).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80a2-a431-e18970d7153f" class="bulleted-list"><li style="list-style-type:disc"><strong>Net (tài xế nhận)</strong>: 10–14 triệu/tháng (sau chia doanh thu + khấu trừ công ty).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80c0-bc60-fc3f96a44796" class="bulleted-list"><li style="list-style-type:disc"><strong>Thu nhập theo giờ</strong>: ~60–80k VND.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80d6-a973-c23a94f533e1" class="bulleted-list"><li style="list-style-type:disc"><strong>So sánh</strong>: thấp hơn GrabCar (13–17m net) và Xanh SM (12–20m net).</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8055-871a-dea39bed5ea4"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-80f8-b23f-c0243da3f475" class=""><strong>6. 
Chi phí &amp; Khấu hao</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8073-8f52-c9c6b4634ce0" class="bulleted-list"><li style="list-style-type:disc"><strong>Xe công ty cấp</strong>: tài xế không phải đầu tư ban đầu.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8036-a94e-f2ae85a2c5d4" class="bulleted-list"><li style="list-style-type:disc"><strong>Chi phí tài xế gánh</strong>: nhiên liệu, cầu đường, vệ sinh xe (chia sẻ với công ty).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8023-86ff-f094640dfe18" class="bulleted-list"><li style="list-style-type:disc"><strong>Khấu hao</strong>: công ty chịu.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8093-8c07-f702c91b8335" class="bulleted-list"><li style="list-style-type:disc"><strong>Chi phí ẩn</strong>: nếu không đạt doanh số tối thiểu → bị giảm lương hoặc cắt thưởng.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8097-a5f2-d1a3ac26842d"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-80ed-97df-d13036f5c986" class=""><strong>7. 
Khiếu nại &amp; Trải nghiệm (CX &amp; Driver Complaints)</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80dd-91c4-dd3a2c8b0474" class="bulleted-list"><li style="list-style-type:disc"><strong>Tài xế phàn nàn</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-804c-8534-f7f818a841c1" class="bulleted-list"><li style="list-style-type:circle">Doanh thu thực giảm do cạnh tranh từ Grab, Be, Xanh SM.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8037-ab8d-cc54f8549700" class="bulleted-list"><li style="list-style-type:circle">Áp lực doanh số, ít linh hoạt giờ làm.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-806f-8beb-f5b4cb03e0d7" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách hàng phàn nàn</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80d8-a3db-f558d45556cc" class="bulleted-list"><li style="list-style-type:circle">Giá cước cao hơn ứng dụng công nghệ trong giờ thấp điểm.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8020-9dce-f728beab0d05" class="bulleted-list"><li style="list-style-type:circle">Chờ xe lâu hơn ở vùng ven so với Grab/Xanh SM.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8096-bb8c-e644ad398be4" class="bulleted-list"><li style="list-style-type:disc"><strong>Điểm mạnh</strong>: thương hiệu truyền thống, khách hàng trung thành, đặc biệt nhóm lớn tuổi và doanh nghiệp.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8033-9005-c1dd814ea4ec"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-80ea-bd11-ef55c9852e96" class=""><strong>8. 
Thu hút &amp; Giữ chân tài xế</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80de-9d9b-e183fc36d40c" class="bulleted-list"><li style="list-style-type:disc"><strong>An sinh đầy đủ + lương cơ bản</strong>: yếu tố giữ chân tài xế truyền thống.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80e2-bf54-cce5a38d810f" class="bulleted-list"><li style="list-style-type:disc"><strong>Thương hiệu lâu đời (30 năm)</strong>: tạo sự tin cậy.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8070-8757-f1ea70d21e3f" class="bulleted-list"><li style="list-style-type:disc"><strong>Xe công ty cấp</strong>: giảm rủi ro đầu tư.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80bb-942c-d9ca68ddc220" class="bulleted-list"><li style="list-style-type:disc"><strong>Điểm yếu</strong>: thu nhập thấp hơn taxi công nghệ, ít hấp dẫn với tài xế trẻ.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80a7-99a7-c5ef6e22e57b" class="bulleted-list"><li style="list-style-type:disc"><strong>Ứng dụng Mai Linh</strong>: giúp hiện đại hóa, nhưng thị phần nhỏ hơn Grab/Xanh SM.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8045-b6ee-f6dca5bc003d"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-80b1-b391-df989780b2e4" class=""><strong>9. 
Tuân thủ pháp lý</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8082-a8af-df2552567809" class="bulleted-list"><li style="list-style-type:disc">Hoạt động đúng khung taxi truyền thống (Nghị định 10/2020).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80c6-b13d-deb9ccccc77a" class="bulleted-list"><li style="list-style-type:disc">Tuân thủ đầy đủ về đồng hồ tính cước, hóa đơn VAT, hợp đồng lao động.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8074-a4d6-dffd3c980aee" class="bulleted-list"><li style="list-style-type:disc">Không gặp tranh cãi pháp lý như Grab.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8019-b55e-c3bc65f0f3ae" class="bulleted-list"><li style="list-style-type:disc">Có lợi thế pháp lý ổn định, nhưng bị bất lợi cạnh tranh với nền tảng công nghệ.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8091-aeb6-f7ab171c0641"/></div><div style="display:contents" dir="auto"><h2 id="280c5e6f-95bd-80d6-baaf-cfb8d690240b" class=""><strong>Đánh giá trung tính</strong></h2></div><div style="display:contents" dir="auto"><p id="280c5e6f-95bd-8028-9da0-d0dcd4c4f40c" class=""><strong>Ưu điểm</strong></p></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-803c-8334-f14ccad0c44e" class="bulleted-list"><li style="list-style-type:disc">Có an sinh, lương cơ bản, chế độ lao động đầy đủ.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80ad-aa6a-feae21457994" class="bulleted-list"><li style="list-style-type:disc">Xe và đồng phục do công ty cấp.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8029-9372-d12f2786c5fa" class="bulleted-list"><li style="list-style-type:disc">Thương hiệu uy tín, 
quen thuộc.</li></ul></div><div style="display:contents" dir="auto"><p id="280c5e6f-95bd-80e9-a619-cab7ee76119c" class=""><strong>Nhược điểm</strong></p></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80f7-874a-d7503f88b506" class="bulleted-list"><li style="list-style-type:disc">Thu nhập thực thấp hơn GrabCar/Xanh SM.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8001-bff5-c978a4ca2f30" class="bulleted-list"><li style="list-style-type:disc">Doanh số ép buộc, ít linh hoạt.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8044-820e-dcd376cb0027" class="bulleted-list"><li style="list-style-type:disc">Dịch vụ công nghệ chưa mạnh, khó cạnh tranh ở thành phố lớn.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8078-9cf5-da7d0a868894"/></div><div style="display:contents" dir="auto"><h2 id="280c5e6f-95bd-8025-81f5-cb709ef60ad6" class=""><strong>Cơ hội cho UniTaxi (so với Mai Linh)</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-8046-bc5f-c959c7ab2a9c" class="numbered-list" start="1"><li><strong>Giữ điểm mạnh an sinh xã hội</strong>, nhưng nâng <strong>mức thu nhập tối thiểu</strong> cạnh tranh với Grab/Xanh SM.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-8026-955c-ff0ca54abf48" class="numbered-list" start="2"><li><strong>Không áp doanh số cứng</strong>: thay bằng KPI minh bạch và linh hoạt (chuyến/giờ).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-8043-a15c-cd7403ef80dd" class="numbered-list" start="3"><li><strong>Tích hợp công nghệ mạnh</strong>: app hiện đại, cuốc ổn định, dữ liệu minh bạch.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-8001-b8a6-dbccba53e6f5" class="numbered-list" start="4"><li><strong>Retention</strong>: thêm phúc lợi gia đình (y tế, 
học phí) để giữ tài xế lâu dài.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-8036-a1ea-f0a917b8bc59" class="numbered-list" start="5"><li><strong>Định vị thương hiệu</strong>: “Taxi công nghệ Việt có an sinh như Mai Linh nhưng thu nhập cao hơn Grab/Xanh SM.”</li></ol></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8044-89fb-f3392036c879"/></div><div style="display:contents" dir="auto"><h1 id="280c5e6f-95bd-8004-97d6-fb665dc6acab" class=""><strong>G7 Taxi — Competition Benchmark</strong></h1></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8016-ad5f-d2554e182649"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-8003-a40e-d2cf7392a19a" class=""><strong>1. 
Bảo hiểm &amp; An sinh</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80c0-b72b-e191cc92bf16" class="bulleted-list"><li style="list-style-type:disc"><strong>Có HĐLĐ chính thức</strong>: tài xế là nhân viên, được đóng <strong>BHXH, BHYT, BHTN</strong> theo luật lao động.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-802c-9f42-e959ced02518" class="bulleted-list"><li style="list-style-type:disc"><strong>Bảo hiểm tai nạn nghề nghiệp</strong>: áp dụng theo quy định pháp luật và chính sách nội bộ.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80c3-b67e-f3c04c92b0bb" class="bulleted-list"><li style="list-style-type:disc"><strong>Điểm mạnh</strong>: an sinh đầy đủ tương tự Vinasun và Mai Linh.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8052-b7a6-ef784f78b393" class="bulleted-list"><li style="list-style-type:disc"><strong>Điểm yếu</strong>: ít gói phúc lợi bổ sung, chưa có bảo hiểm thu nhập hoặc gia đình.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8011-9682-f79428b432aa"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-80eb-a367-dc2a4073b35f" class=""><strong>2. 
Chế độ &amp; Phúc lợi (Compensation &amp; Benefits)</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8011-b273-c4d5623a1798" class="bulleted-list"><li style="list-style-type:disc"><strong>Lương cơ bản</strong>: trả theo vùng (mức tối thiểu vùng).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8033-9914-cdc234376ad8" class="bulleted-list"><li style="list-style-type:disc"><strong>Thu nhập</strong> = lương cơ bản + % doanh thu (thường 30–40%).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80f2-813e-dc531530d3b5" class="bulleted-list"><li style="list-style-type:disc"><strong>Thưởng</strong>: theo doanh số, hiệu quả phục vụ, ngày lễ Tết.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-803c-b28e-cd850134cb2b" class="bulleted-list"><li style="list-style-type:disc"><strong>Xe &amp; đồng phục</strong>: công ty cấp xe taxi gắn thương hiệu G7, tài xế được cấp đồng phục.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-802a-b7ff-c3bb3e7dac14" class="bulleted-list"><li style="list-style-type:disc"><strong>Phúc lợi bổ sung</strong>: nghỉ phép năm, hỗ trợ khó khăn, các chế độ xã hội cơ bản.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-804c-863f-d608f506288c"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-8010-bc0f-fad53e86a45e" class=""><strong>3. 
Tuyển dụng &amp; Đào tạo</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8076-aab0-d9752ee26db9" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều kiện</strong>: GPLX B2+, sức khỏe đạt chuẩn, lý lịch rõ ràng.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-806b-98d6-d72bd930d826" class="bulleted-list"><li style="list-style-type:disc"><strong>Quy trình</strong>: nộp hồ sơ → phỏng vấn → ký HĐLĐ → đào tạo.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80ba-8154-e05dd85110ff" class="bulleted-list"><li style="list-style-type:disc"><strong>Đào tạo</strong>: lái xe an toàn, kỹ năng phục vụ khách, sử dụng app G7.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8054-84b4-eb7ce1a6b247" class="bulleted-list"><li style="list-style-type:disc"><strong>Chi phí gia nhập</strong>: thấp, tài xế chủ yếu cần hồ sơ và sức khỏe.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80d0-b9ec-cce47dbb9b99"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-804f-bacf-e431dbeee7eb" class=""><strong>4. 
Vận hành ngoài đường</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80a5-bcb7-f1aa24ce3b54" class="bulleted-list"><li style="list-style-type:disc"><strong>Mô hình vận hành</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80ed-bf6e-fba79d5b6b4c" class="bulleted-list"><li style="list-style-type:circle">Đón khách qua tổng đài 24/7 hoặc app G7.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8018-9f3e-e70795984aa7" class="bulleted-list"><li style="list-style-type:circle">Tài xế phải trực bến/khu vực được phân bổ.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8086-acda-c302513098c1" class="bulleted-list"><li style="list-style-type:disc"><strong>Doanh số tối thiểu</strong>: có chỉ tiêu doanh thu/ngày hoặc tháng.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80af-87ae-c4de9d577f2e" class="bulleted-list"><li style="list-style-type:disc"><strong>Quản lý</strong>: bắt buộc đồng phục, giữ vệ sinh xe, tuân thủ thái độ phục vụ.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-807b-aed7-f5598eec5ab3" class="bulleted-list"><li style="list-style-type:disc"><strong>Phạt</strong>: từ cảnh cáo → phạt tiền → kỷ luật khi không đạt doanh số hoặc vi phạm dịch vụ.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80f4-b1ed-ee066a67d566"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-8019-be9d-c7bf1607577d" class=""><strong>5. 
Thu nhập Gross vs Net</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-809b-bca2-d20eaed19d50" class="bulleted-list"><li style="list-style-type:disc"><strong>Gross (doanh thu xe)</strong>: 20–30 triệu VND/tháng (taxi 4–7 chỗ chạy full-time).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80ea-a6ed-f13a92c4aa00" class="bulleted-list"><li style="list-style-type:disc"><strong>Net (tài xế nhận)</strong>: 9–12 triệu VND/tháng sau khi chia doanh thu.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80a9-b910-e6cef091c0b7" class="bulleted-list"><li style="list-style-type:disc"><strong>Thu nhập theo giờ</strong>: ~50–70k VND.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80d3-a49a-c7ccd02353b5" class="bulleted-list"><li style="list-style-type:disc"><strong>So sánh</strong>: thấp hơn GrabCar (13–17m net) và Xanh SM (12–20m net), gần tương tự Mai Linh.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8048-b1f1-f2a182adb2fd"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-80f2-8a9c-de303b4c58cb" class=""><strong>6. 
Chi phí &amp; Khấu hao</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8087-b772-e321d0b48824" class="bulleted-list"><li style="list-style-type:disc"><strong>Xe công ty cấp</strong>: tài xế không phải đầu tư xe.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8038-8832-f657cff6f9a4" class="bulleted-list"><li style="list-style-type:disc"><strong>Chi phí tài xế gánh</strong>: nhiên liệu, cầu đường, vệ sinh xe, một phần bảo trì.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-807c-8c39-ea648ba1cac9" class="bulleted-list"><li style="list-style-type:disc"><strong>Khấu hao</strong>: công ty chịu.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80c3-bed5-ce96afcb3c3e" class="bulleted-list"><li style="list-style-type:disc"><strong>Chi phí ẩn</strong>: doanh số không đạt → bị trừ thưởng hoặc giảm lương.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80b1-b1dc-d1393e9da200"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-802f-b277-e1453f9a0e10" class=""><strong>7. 
Khiếu nại &amp; Trải nghiệm (CX &amp; Driver Complaints)</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8036-9b07-e5e6f6129e0b" class="bulleted-list"><li style="list-style-type:disc"><strong>Tài xế phàn nàn</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80a8-a316-eeccaafa4daf" class="bulleted-list"><li style="list-style-type:circle">Thu nhập thấp hơn taxi công nghệ.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-804e-b578-c91b9020d9da" class="bulleted-list"><li style="list-style-type:circle">Áp lực doanh số, ít linh hoạt ca làm.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80bf-9210-ded3ddcdee5e" class="bulleted-list"><li style="list-style-type:circle">Cạnh tranh gay gắt tại Hà Nội với Grab, Be, Xanh SM.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80b8-ad7c-f2a66c7be9a0" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách hàng phàn nàn</strong>:<div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8084-89b2-c8a5b5d60ede" class="bulleted-list"><li style="list-style-type:circle">Chờ xe lâu giờ cao điểm.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-801a-b8ba-d52e7a2b15a8" class="bulleted-list"><li style="list-style-type:circle">Một số tài xế từ chối cuốc ngắn.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-802d-b13c-c770e6c3c5b1" class="bulleted-list"><li style="list-style-type:disc"><strong>Điểm mạnh</strong>: thương hiệu quen thuộc tại Hà Nội, giá niêm yết rõ ràng, dễ tin cậy với khách lớn tuổi/doanh nghiệp.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8020-a43d-c3ce121dd9d3"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-806a-a773-d07d40394b92" class=""><strong>8. 
Thu hút &amp; Giữ chân tài xế</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8084-a569-ed9d58901925" class="bulleted-list"><li style="list-style-type:disc"><strong>An sinh xã hội đầy đủ</strong>: BHXH, BHYT, BHTN.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80f5-a788-e18d7cacf88c" class="bulleted-list"><li style="list-style-type:disc"><strong>Xe công ty cấp</strong>: không yêu cầu tài xế đầu tư ban đầu.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8071-babc-c6cf0a50a37c" class="bulleted-list"><li style="list-style-type:disc"><strong>Thương hiệu Hà Nội</strong>: tạo sự quen thuộc, được nhiều khách quen sử dụng.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80d5-bbee-df31598b9c7c" class="bulleted-list"><li style="list-style-type:disc"><strong>Điểm yếu</strong>: thu nhập thấp, thiếu linh hoạt, không có chính sách retention mạnh như ứng dụng công nghệ (incentive, referral).</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-8079-9f57-e21746e2822f"/></div><div style="display:contents" dir="auto"><h3 id="280c5e6f-95bd-8023-a02e-c8a589bfdea6" class=""><strong>9. 
Tuân thủ pháp lý</strong></h3></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8042-9e00-f32c0b7058af" class="bulleted-list"><li style="list-style-type:disc">Hoạt động hoàn toàn trong khung taxi truyền thống (Nghị định 10/2020).</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-802a-9e19-d3a04f65dd9e" class="bulleted-list"><li style="list-style-type:disc">Tuân thủ về đồng hồ tính cước, hợp đồng lao động, hóa đơn VAT.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8003-b3a0-ca94b1250230" class="bulleted-list"><li style="list-style-type:disc">Có lợi thế pháp lý ổn định, nhưng khó cạnh tranh với taxi công nghệ về giá và sự linh hoạt.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80b5-b181-de8f858f4fe7"/></div><div style="display:contents" dir="auto"><h2 id="280c5e6f-95bd-80c5-9f34-f4cb9d276d79" class=""><strong>Đánh giá trung tính</strong></h2></div><div style="display:contents" dir="auto"><p id="280c5e6f-95bd-80c4-8237-efdd514c7f74" class=""><strong>Ưu điểm</strong></p></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8043-b94e-c39924879133" class="bulleted-list"><li style="list-style-type:disc">An sinh xã hội đầy đủ.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80c9-abbb-d7a9dc654a9e" class="bulleted-list"><li style="list-style-type:disc">Xe công ty cấp, không yêu cầu vốn đầu tư.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8035-ac06-e6524e636030" class="bulleted-list"><li style="list-style-type:disc">Thương hiệu uy tín tại Hà Nội.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80c7-9332-ec2482857a0c" class="bulleted-list"><li style="list-style-type:disc">Giá niêm yết rõ ràng, 
khách quen tin cậy.</li></ul></div><div style="display:contents" dir="auto"><p id="280c5e6f-95bd-8025-82d9-fda7bcb6826b" class=""><strong>Nhược điểm</strong></p></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8090-826a-f5f762741f4b" class="bulleted-list"><li style="list-style-type:disc">Thu nhập thấp hơn GrabCar, Xanh SM.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-80b4-8472-db8a8b7d92e0" class="bulleted-list"><li style="list-style-type:disc">Doanh số ép buộc, ít linh hoạt.</li></ul></div><div style="display:contents" dir="auto"><ul id="280c5e6f-95bd-8033-bbcd-d6e62349e9d5" class="bulleted-list"><li style="list-style-type:disc">Dịch vụ công nghệ chưa mạnh, khó mở rộng ngoài Hà Nội.</li></ul></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80fd-9c61-c76098098878"/></div><div style="display:contents" dir="auto"><h2 id="280c5e6f-95bd-800c-ae3f-c218a14a6ab9" class=""><strong>Cơ hội cho UniTaxi (so với G7)</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-80c9-8caa-efc475e2f896" class="numbered-list" start="1"><li><strong>Giữ điểm mạnh an sinh</strong>, nhưng nâng <strong>thu nhập tối thiểu</strong> để cạnh tranh.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-80e6-848d-c969a03e7d2a" class="numbered-list" start="2"><li><strong>Không ép doanh số cứng</strong>: cho phép tài xế chọn ca linh hoạt.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-8017-aaf6-c2366cdbe30a" class="numbered-list" start="3"><li><strong>Ứng dụng công nghệ mạnh mẽ hơn</strong>: so với app G7 còn hạn chế.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-80dc-81ba-c3bd4d85798f" class="numbered-list" start="4"><li><strong>Hợp đồng doanh nghiệp</strong>: mở rộng B2B (sân bay, khách sạn), 
tạo cuốc ổn định.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-8023-bb11-d4ec1e97454b" class="numbered-list" start="5"><li><strong>Retention mới</strong>: bổ sung bảo hiểm thu nhập, gói hỗ trợ gia đình để giữ chân lâu dài.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="280c5e6f-95bd-808c-bb94-e3aecf977f49" class="numbered-list" start="6"><li><strong>Khác biệt thương hiệu</strong>: UniTaxi có thể định vị “ứng dụng Việt toàn quốc, an sinh như G7 nhưng thu nhập cao và linh hoạt hơn”.</li></ol></div><div style="display:contents" dir="auto"><hr id="280c5e6f-95bd-80f5-9c65-ed9c9baae966"/></div><div style="display:contents" dir="auto"><p id="280c5e6f-95bd-80b5-8cb7-ef4b09522606" class="">
</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
