---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>📘 BUSINESS REQUIREMENTS DOCUMENT (BRD)</title><style>
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
	
</style></head><body><article id="286c5e6f-95bd-80e7-8a12-d28e2ef6ca45" class="page sans"><header><h1 class="page-title" dir="auto"><strong>📘 BUSINESS REQUIREMENTS DOCUMENT (BRD)</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h1 id="286c5e6f-95bd-8018-926a-d7645a2d97cc" class=""><strong>🚖 Rider App (Khách hàng)</strong></h1></div><div style="display:contents" dir="auto"><h2 id="286c5e6f-95bd-8055-bd79-e92a19ab9594" class=""><strong>1) Chức năng bắt buộc</strong></h2></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8036-a617-fe808018f4d5" class="bulleted-list"><li style="list-style-type:disc"><strong>Đăng ký/Đăng nhập</strong>: OTP qua SMS; lưu hồ sơ cơ bản (tên, SĐT).</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-802e-a43a-c0f99f2d9e7d" class="bulleted-list"><li style="list-style-type:disc"><strong>Định vị &amp; bản đồ</strong>: tự động lấy vị trí hiện tại; chọn điểm đón/trả; gợi ý địa điểm gần.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80f8-b652-e31047bf1ebb" class="bulleted-list"><li style="list-style-type:disc"><strong>Ước tính giá &amp; hiển thị giá cố định</strong>: hiện <em>tổng giá</em> trước khi đặt (km + phút + phụ phí cố định nếu có).</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-801d-b26e-e3e5e8f7ae3a" class="bulleted-list"><li style="list-style-type:disc"><strong>Đặt xe tức thì</strong>: tạo cuốc; nhận trạng thái theo thời gian thực (đang tìm tài xế → tài xế nhận → đang tới → đang chở → hoàn thành).</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-807f-bf7d-d74aa919355e" class="bulleted-list"><li style="list-style-type:disc"><strong>Theo dõi tài xế</strong>: hiển thị biển số, ảnh/ tên tài xế, ETA, vị trí trực tiếp.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80be-9f79-e396b04e4383" class="bulleted-list"><li style="list-style-type:disc"><strong>Thanh toán</strong>: tiền mặt + ví điện tử (VNPay/MoMo/ZaloPay) + thẻ (nếu có); biên lai điện tử.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80e9-8c1d-e9d652119559" class="bulleted-list"><li style="list-style-type:disc"><strong>Hủy cuốc</strong>: hủy trước khi tài xế đến/đón (áp dụng phí hủy rõ ràng nếu vượt ngưỡng).</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8029-861c-ce2b75183527" class="bulleted-list"><li style="list-style-type:disc"><strong>Đánh giá &amp; phản hồi</strong>: chấm sao và góp ý nhanh sau chuyến.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8064-af98-c14eb73996a8" class="bulleted-list"><li style="list-style-type:disc"><strong>Lịch sử chuyến đi</strong>: xem lại chi tiết cuốc và biên lai.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-803b-9a3e-dceebee9f2da" class="bulleted-list"><li style="list-style-type:disc"><strong>Hỗ trợ nhanh</strong>: nút trợ giúp/cuộc gọi ẩn số tới CS.</li></ul></div><div style="display:contents" dir="auto"><h2 id="286c5e6f-95bd-809a-9d04-ef90bbacb00b" class=""><strong>2) Màn hình tối thiểu</strong></h2></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8063-939c-dd5e6c6c0341" class="bulleted-list"><li style="list-style-type:disc">Onboarding/OTP • Trang chính (map) • Chọn điểm đến • Chi tiết giá • Trạng thái cuốc • Thanh toán • Đánh giá • Lịch sử • Hỗ trợ.</li></ul></div><div style="display:contents" dir="auto"><h2 id="286c5e6f-95bd-80e8-afa9-e2fb96f332d4" class=""><strong>3) Tiêu chí chấp nhận (Acceptance)</strong></h2></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80a6-b6ae-c2f75bb45ef7" class="bulleted-list"><li style="list-style-type:disc">Đặt cuốc → ghép tài xế thành công trong ≤60 giây (khi có tài xế gần).</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80c4-8343-c198a7064278" class="bulleted-list"><li style="list-style-type:disc">Giá hiển thị trước = giá thanh toán (sai số tính theo mét/giây &lt; 2%).</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80fc-a0d1-fa0eafb93489" class="bulleted-list"><li style="list-style-type:disc">Đường truyền kém: vẫn thao tác cơ bản, tự đồng bộ khi mạng ổn định.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8036-afcf-d7841af6b95d" class="bulleted-list"><li style="list-style-type:disc">Ứng dụng khởi chạy &lt; 3 giây trên Android tầm trung.</li></ul></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-8017-a599-d6948ef775d2"/></div><div style="display:contents" dir="auto"><h1 id="286c5e6f-95bd-8039-bfcf-e2a3dbde6b5e" class=""><strong>👨‍✈️ Driver App (Tài xế)</strong></h1></div><div style="display:contents" dir="auto"><h2 id="286c5e6f-95bd-80bd-b55c-d620ebf2d8b5" class=""><strong>1) Chức năng bắt buộc</strong></h2></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8085-a980-e03ece3eefaa" class="bulleted-list"><li style="list-style-type:disc"><strong>Đăng nhập</strong>: OTP; kiểm tra trạng thái kích hoạt (đã duyệt hồ sơ).</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80aa-9aa0-f9b196e6dcfd" class="bulleted-list"><li style="list-style-type:disc"><strong>Bật/Tắt nhận cuốc (Trực tuyến/Ngoại tuyến)</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80af-828a-f21cc780d69a" class="bulleted-list"><li style="list-style-type:disc"><strong>Hàng đợi cuốc &amp; nhận cuốc</strong>: xem chi tiết điểm đón/trả, ước tính cước &amp; thời gian; bấm <em>Nhận</em>.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80fe-9e3b-d0c000d834f8" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều hướng</strong>: mở điều hướng (Google/Apple Maps) tới điểm đón &amp; tới điểm trả.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8046-8fd1-e7083ad2b3db" class="bulleted-list"><li style="list-style-type:disc"><strong>Trạng thái chuyến</strong>: <em>Đến điểm đón</em> → <em>Đã đón khách</em> → <em>Kết thúc chuyến</em>.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8099-9d87-e7e99b5bbe29" class="bulleted-list"><li style="list-style-type:disc"><strong>Thu nhập cơ bản</strong>: tổng doanh thu ngày/tuần; số cuốc/giờ; phí/chiết khấu hiển thị rõ.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8080-b8e8-e5d6858859cd" class="bulleted-list"><li style="list-style-type:disc"><strong>Hủy cuốc theo quy định</strong>: chọn lý do; log lại.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80eb-811e-ca6f14281a73" class="bulleted-list"><li style="list-style-type:disc"><strong>Lịch sử chuyến</strong>: chi tiết từng cuốc (km, phút, giá, chia sẻ doanh thu).</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8029-ae57-cba81216467e" class="bulleted-list"><li style="list-style-type:disc"><strong>Hỗ trợ nhanh</strong>: gọi CS; báo cáo sự cố.</li></ul></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-804a-9bf0-dc0f9aacae40" class=""><em>(Nếu là EV: có thể thêm hiển thị % pin và trạm sạc gần nhất — nhưng không bắt buộc cho bản tối thiểu.)</em></p></div><div style="display:contents" dir="auto"><h2 id="286c5e6f-95bd-808a-a4c9-c9f27e2208f2" class=""><strong>2) Màn hình tối thiểu</strong></h2></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80e4-9c85-dccbb275dedf" class="bulleted-list"><li style="list-style-type:disc">OTP/Đăng nhập • Bật/Tắt nhận cuốc • Danh sách/Pop-up cuốc mới • Điều hướng • Trạng thái chuyến • Thu nhập • Lịch sử • Hỗ trợ.</li></ul></div><div style="display:contents" dir="auto"><h2 id="286c5e6f-95bd-80fc-bf19-fcbdeb55034f" class=""><strong>3) Tiêu chí chấp nhận (Acceptance)</strong></h2></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80e1-869b-cdcc2de0285f" class="bulleted-list"><li style="list-style-type:disc">Nhận thông báo cuốc mới trong ≤2 giây từ lúc dispatch gửi.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8029-9097-d44dd781b126" class="bulleted-list"><li style="list-style-type:disc">Quy trình: Nhận cuốc → Điều hướng → Kết thúc → Đồng bộ doanh thu hoàn tất &lt; 5 giây.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8078-9cdd-c14ccdb3ac1f" class="bulleted-list"><li style="list-style-type:disc">App vẫn hiển thị trạng thái và lưu log tạm khi mất mạng ngắn (≤2 phút), tự đồng bộ lại.</li></ul></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-80c4-b459-d863a3832b56"/></div><div style="display:contents" dir="auto"><h1 id="286c5e6f-95bd-80cf-91a6-d128f84c8c2c" class=""><strong>🔗 Nền tảng chung (cho cả 2 app)</strong></h1></div><div style="display:contents" dir="auto"><h2 id="286c5e6f-95bd-80cc-a5d4-d84e4fb330a2" class=""><strong>API bắt buộc (tối thiểu)</strong></h2></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8009-9de4-de62618e7db1" class="bulleted-list"><li style="list-style-type:disc"><strong>Auth</strong>: /otp/send, /auth/verify</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80d8-94c4-e872fa143ba7" class="bulleted-list"><li style="list-style-type:disc"><strong>Rider</strong>: /rides/quote, /rides/create, /rides/status/{id}, /rides/cancel/{id}</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80f9-b019-fe5b61158054" class="bulleted-list"><li style="list-style-type:disc"><strong>Driver</strong>: /driver/status (online/offline), /driver/jobs/next, /driver/jobs/accept/{id}, /driver/jobs/arrive/{id}, /driver/jobs/start/{id}, /driver/jobs/complete/{id}, /driver/job/cancel/{id}</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8098-93cf-fc7ee9c0e656" class="bulleted-list"><li style="list-style-type:disc"><strong>Payments</strong>: /payment/initiate, /payment/callback, /receipt/{rideId}</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80f1-9c30-ebeba16c6508" class="bulleted-list"><li style="list-style-type:disc"><strong>Profiles</strong>: /me, /driver/me, /history/rides</li></ul></div><div style="display:contents" dir="auto"><h2 id="286c5e6f-95bd-80ea-aaff-fd46cc7d9984" class=""><strong>Luồng lõi (happy path)</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="286c5e6f-95bd-8030-a546-e0243e734ae6" class="numbered-list" start="1"><li>Rider: mở app → định vị → nhập điểm đến → xem giá → đặt → ghép driver → theo dõi → thanh toán → đánh giá.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="286c5e6f-95bd-80a7-b2b4-da26622891c0" class="numbered-list" start="2"><li>Driver: online → nhận cuốc → đến điểm đón → đón khách → kết thúc → thu nhập cập nhật.</li></ol></div><div style="display:contents" dir="auto"><h2 id="286c5e6f-95bd-80d0-84e3-edcf2d01c5da" class=""><strong>Edge cases cần xử lý</strong></h2></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-803d-88bd-d2bd8fe28fe6" class="bulleted-list"><li style="list-style-type:disc">Không tìm thấy tài xế: hiển thị <em>thử lại</em> hoặc gợi ý thời gian/điểm đón khác.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-801c-8ab3-c23dc9bb97d6" class="bulleted-list"><li style="list-style-type:disc">Tài xế hủy giữa chừng: tự động gán lại tài xế gần nhất; rider được thông báo.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8093-ac8d-c86c594d5705" class="bulleted-list"><li style="list-style-type:disc">Rider hủy sát giờ: áp dụng phí hủy theo rule (rõ ràng trong biên lai).</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-806f-acfc-d785dca60fce" class="bulleted-list"><li style="list-style-type:disc">Thanh toán ví lỗi: fallback sang tiền mặt; hệ thống auto-đối soát sau.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8090-be32-caed2609f1c7" class="bulleted-list"><li style="list-style-type:disc">Mất GPS/mạng: lưu cục bộ các mốc thời gian; đồng bộ khi có mạng.</li></ul></div><div style="display:contents" dir="auto"><h2 id="286c5e6f-95bd-8057-a777-c8ab9648f702" class=""><strong>Bảo mật &amp; hiệu năng</strong></h2></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8069-9fb5-d7a16f34de56" class="bulleted-list"><li style="list-style-type:disc">OAuth2/JWT; TLS 1.3; mã hóa dữ liệu nhạy cảm.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8039-9e9e-febe4329173b" class="bulleted-list"><li style="list-style-type:disc">Giới hạn tần suất (rate limit) các API đặt/hủy để chống lạm dụng.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-800e-a049-d87a0313342d" class="bulleted-list"><li style="list-style-type:disc">Log/audit tối thiểu cho: tạo cuốc, nhận cuốc, hủy, thanh toán.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8016-8841-f61807f4d297" class="bulleted-list"><li style="list-style-type:disc">Mục tiêu: uptime ≥ 99.9%; phản hồi API &lt; 1.5–2s.</li></ul></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-8068-9638-e43c3bf3eefa"/></div><div style="display:contents" dir="auto"><h1 id="286c5e6f-95bd-8007-b500-f3f9cee85dd5" class=""><strong>🧱 Công nghệ đề xuất (nhẹ, triển khai nhanh)</strong></h1></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-805c-9632-e7e28c440f02" class="bulleted-list"><li style="list-style-type:disc"><strong>Mobile</strong>: Flutter (1 codebase cho Rider &amp; Driver).</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80d9-a5be-cded397d11da" class="bulleted-list"><li style="list-style-type:disc"><strong>Backend</strong>: Node.js (NestJS), PostgreSQL, Redis.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8067-bac5-d576f4bcb41d" class="bulleted-list"><li style="list-style-type:disc"><strong>Realtime</strong>: WebSocket/Socket.IO (trạng thái cuốc, push cuốc mới).</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80b6-ab85-ee9b4ca5162c" class="bulleted-list"><li style="list-style-type:disc"><strong>Maps</strong>: Google Maps SDK (geocode, directions, distance matrix).</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8086-94ad-dc4dea6ab885" class="bulleted-list"><li style="list-style-type:disc"><strong>Payments</strong>: VNPay/MoMo/ZaloPay (server-to-server callback).</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80da-be66-cca4f01c8192" class="bulleted-list"><li style="list-style-type:disc"><strong>Deploy</strong>: Docker + VNPT/AWS; giám sát Prometheus + Grafana.</li></ul></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-8087-8efc-cc6c7962989f"/></div><div style="display:contents" dir="auto"><h1 id="286c5e6f-95bd-8016-b6aa-c8dcaf40f055" class=""><strong>🗓️ Kế hoạch delivery gợi ý (6 tuần “đủ chạy”)</strong></h1></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8043-ad7f-c9c342281f5c" class="bulleted-list"><li style="list-style-type:disc"><strong>Tuần 1–2</strong>: Auth + Map + Quote + Create Ride; Driver online/offline + nhận cuốc cơ bản.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8024-8647-efea9f1eac5e" class="bulleted-list"><li style="list-style-type:disc"><strong>Tuần 3–4</strong>: Trạng thái chuyến trọn vẹn, realtime; lịch sử/biên lai; thu nhập tài xế; hủy &amp; phí hủy.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80e7-bffb-e9ef179c0a5b" class="bulleted-list"><li style="list-style-type:disc"><strong>Tuần 5</strong>: Tích hợp thanh toán ví; hardening hiệu năng; QA end-to-end.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80ee-ac12-d143b7abe43e" class="bulleted-list"><li style="list-style-type:disc"><strong>Tuần 6</strong>: Pilot live 200–500 xe; fix lỗi; chuẩn bị mở rộng.</li></ul></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-809a-8bcc-dce22493587e"/></div><div style="display:contents" dir="auto"><h1 id="286c5e6f-95bd-8069-96a3-ddb464b77d5e" class=""><strong>✅ Tiêu chí “xong” (Definition of Done – bản tối thiểu)</strong></h1></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80be-8d9c-dd00664574f8" class="bulleted-list"><li style="list-style-type:disc">Đặt – nhận – hoàn thành cuốc <strong>ổn định</strong>; tỷ lệ lỗi &lt; 1%/1000 cuốc.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8060-a059-cea7632284a0" class="bulleted-list"><li style="list-style-type:disc">Giá hiển thị trước khớp giá thu tiền; biên lai tự sinh.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8088-9a09-c4ba9851185a" class="bulleted-list"><li style="list-style-type:disc">Tài xế online ≥ 2 giờ mà không crash; pin &amp; dữ liệu nền tối ưu.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-801f-9cee-c83a1cf07269" class="bulleted-list"><li style="list-style-type:disc">Kênh hỗ trợ phản hồi &lt; 5 phút (hotline/in-app call).</li></ul></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-8091-ac9a-c949358402a4"/></div><div style="display:contents" dir="auto"><p id="293c5e6f-95bd-8083-85f7-c4cc35c64ff0" class="">
</p></div><div style="display:contents" dir="auto"><p id="293c5e6f-95bd-8057-9d8c-f6269cf7f0d3" class="">\</p></div><div style="display:contents" dir="auto"><p id="293c5e6f-95bd-80f8-ac27-c2c68804d4da" class="">Tuyệt vời — dưới đây là <strong>bản yêu cầu đã bổ sung</strong> (giữ cấu trúc MVP, thêm các hạng mục pháp lý, an toàn, khả dụng, và hook EV). Phần mới được đánh dấu <strong>[MỚI]</strong> để đội dev/QA nắm rõ phạm vi tăng thêm.</p></div><div style="display:contents" dir="auto"><hr id="293c5e6f-95bd-8013-9460-e7b624bcdb7f"/></div><div style="display:contents" dir="auto"><h1 id="293c5e6f-95bd-8099-a31c-e55f5d5902cb" class=""><strong>🚖 Rider App (Khách hàng)</strong></h1></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-8037-97d0-e7bc3d5284b9" class=""><strong>1) Chức năng bắt buộc</strong></h2></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80dd-a797-d48833ec6efa" class="bulleted-list"><li style="list-style-type:disc"><strong>Đăng ký/Đăng nhập</strong>: OTP qua SMS; lưu hồ sơ cơ bản (tên, SĐT).</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8059-b059-c9ee8cc9a790" class="bulleted-list"><li style="list-style-type:disc"><strong>Định vị &amp; bản đồ</strong>: tự động lấy vị trí hiện tại; chọn điểm đón/trả; gợi ý địa điểm gần.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80ac-a5d9-f1ac27ba8a64" class="bulleted-list"><li style="list-style-type:disc"><strong>Ước tính giá &amp; hiển thị giá cố định</strong>: hiện <em>tổng giá</em> trước khi đặt (km + phút + phụ phí cố định nếu có).<div style="display:contents" dir="auto"><p id="293c5e6f-95bd-808d-b37d-dcec821df9dc" class=""><strong>[MỚI]</strong> Hiển thị <strong>thuế VAT</strong> và tổng thanh toán sau thuế.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-809f-b8f0-d8a000a898f1" class="bulleted-list"><li style="list-style-type:disc"><strong>Đặt xe tức thì</strong>: tạo cuốc; nhận trạng thái theo thời gian thực (đang tìm tài xế → tài xế nhận → đang tới → đang chở → hoàn thành).</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8002-b388-c193304fb31e" class="bulleted-list"><li style="list-style-type:disc"><strong>Theo dõi tài xế</strong>: hiển thị biển số, ảnh/tên tài xế, ETA, vị trí trực tiếp.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-806c-9e06-e6c393cae5ca" class="bulleted-list"><li style="list-style-type:disc"><strong>Thanh toán</strong>: tiền mặt + ví điện tử (VNPay/MoMo/ZaloPay) + thẻ (nếu có); <strong>biên lai điện tử</strong>.<div style="display:contents" dir="auto"><p id="293c5e6f-95bd-8062-a1cc-feabba57c6ce" class=""><strong>[MỚI]</strong> <strong>Yêu cầu xuất Hóa đơn điện tử (HĐĐT)</strong>: toggle “Xuất HĐ công ty”; nhập <strong>MST, Tên Cty, Địa chỉ, Email nhận HĐ</strong>; lưu “hồ sơ người mua” cho lần sau.</p></div><div style="display:contents" dir="auto"><p id="293c5e6f-95bd-8009-ad8c-faa9c952d759" class=""><strong>[MỚI]</strong> Nhận <strong>link tải HĐĐT (PDF/XML)</strong> trong lịch sử chuyến; thông báo “HĐ sẽ gửi sau” nếu đang chờ phát hành.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8095-988c-dccde68f9df8" class="bulleted-list"><li style="list-style-type:disc"><strong>Hủy cuốc</strong>: hủy trước khi tài xế đến/đón (áp dụng phí hủy rõ ràng nếu vượt ngưỡng).</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-806a-b299-f7df920a5564" class="bulleted-list"><li style="list-style-type:disc"><strong>Đánh giá &amp; phản hồi</strong>: chấm sao và góp ý nhanh sau chuyến.<div style="display:contents" dir="auto"><p id="293c5e6f-95bd-8038-a6e8-f6373291f8e2" class=""><strong>[MỚI]</strong> Báo cáo sự cố/đồ thất lạc (lost &amp; found) kèm ảnh.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80eb-b520-f110a871e42b" class="bulleted-list"><li style="list-style-type:disc"><strong>Lịch sử chuyến đi</strong>: xem chi tiết cuốc và biên lai.<div style="display:contents" dir="auto"><p id="293c5e6f-95bd-802b-8e3e-e578a2851ece" class=""><strong>[MỚI]</strong> Tải <strong>HĐĐT</strong>; yêu cầu <strong>điều chỉnh thông tin hóa đơn</strong> trong 24h (nếu nhà cung cấp HĐĐT cho phép).</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8031-b8d2-ff47635fab7e" class="bulleted-list"><li style="list-style-type:disc"><strong>Hỗ trợ nhanh</strong>: nút trợ giúp/cuộc gọi ẩn số tới CS.<div style="display:contents" dir="auto"><p id="293c5e6f-95bd-803e-a8cb-e0fb25fd1891" class=""><strong>[MỚI]</strong> <strong>SOS</strong>: gọi khẩn + gửi vị trí GPS tức thời (ẩn số) tới hotline/bên an ninh.</p></div></li></ul></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-8019-af9f-f98e2dcce0e2" class=""><strong>2) Màn hình tối thiểu</strong></h2></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-807e-98f1-d80b20684dff" class="bulleted-list"><li style="list-style-type:disc">Onboarding/OTP • Trang chính (map) • Chọn điểm đến • Chi tiết giá • Trạng thái cuốc • Thanh toán • Đánh giá • Lịch sử • Hỗ trợ.<div style="display:contents" dir="auto"><p id="293c5e6f-95bd-80d3-b47b-e9a1965414da" class=""><strong>[MỚI]</strong> <strong>Form HĐĐT</strong> (MST/Tên Cty/Địa chỉ/Email) • <strong>Màn Hóa đơn</strong> (xem/tải PDF, XML) • <strong>Màn SOS</strong> (xác nhận gọi khẩn + chia sẻ vị trí).</p></div></li></ul></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-80c0-ade9-e40eb5775d28" class=""><strong>3) Tiêu chí chấp nhận (Acceptance)</strong></h2></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80c5-ac91-cc5b8ed65cd5" class="bulleted-list"><li style="list-style-type:disc">Đặt cuốc → ghép tài xế thành công trong ≤60 giây (khi có tài xế gần).</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8047-bc5c-dd866241ab4f" class="bulleted-list"><li style="list-style-type:disc">Giá hiển thị trước = giá thanh toán (sai số tính theo mét/giây &lt; 2%).<div style="display:contents" dir="auto"><p id="293c5e6f-95bd-8065-bae3-e4d6f7a44bbd" class=""><strong>[MỚI]</strong> VAT hiển thị đúng theo cấu hình thuế hiện hành.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-800f-babb-d775a6f55c90" class="bulleted-list"><li style="list-style-type:disc">Đường truyền kém: vẫn thao tác cơ bản, tự đồng bộ khi mạng ổn định.<div style="display:contents" dir="auto"><p id="293c5e6f-95bd-80eb-b100-da00742577fa" class=""><strong>[MỚI]</strong> <strong>Lưu tạm dữ liệu chuyến &amp; yêu cầu HĐĐT</strong> khi offline ≤2 phút; không mất dữ liệu sau khi kết nối lại.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-804c-8d03-de8328edbcc8" class="bulleted-list"><li style="list-style-type:disc">Ứng dụng khởi chạy &lt; 3 giây trên Android tầm trung.<div style="display:contents" dir="auto"><p id="293c5e6f-95bd-80d3-a2a0-fcc391b06429" class=""><strong>[MỚI]</strong> Bấm “Xuất HĐĐT” → nhận email/SMS link hoặc thấy trạng thái “đang phát hành” trong ≤2 phút.</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="293c5e6f-95bd-805a-8b0f-f029ebc6c044"/></div><div style="display:contents" dir="auto"><h1 id="293c5e6f-95bd-8040-9b76-e16fbe29790a" class=""><strong>👨‍✈️ Driver App (Tài xế)</strong></h1></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-808e-9afd-f0e3d55f6be8" class=""><strong>1) Chức năng bắt buộc</strong></h2></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80ff-ab64-e6323f09384d" class="bulleted-list"><li style="list-style-type:disc"><strong>Đăng nhập</strong>: OTP; kiểm tra trạng thái kích hoạt (đã duyệt hồ sơ).<div style="display:contents" dir="auto"><p id="293c5e6f-95bd-80e7-acb4-fdd62bab7184" class=""><strong>[MỚI]</strong> <strong>Chặn phiên đăng nhập trùng</strong> (không cho 2 thiết bị hoạt động song song).</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80ca-95ec-e0a8c604b855" class="bulleted-list"><li style="list-style-type:disc"><strong>Bật/Tắt nhận cuốc (Trực tuyến/Ngoại tuyến)</strong>.<div style="display:contents" dir="auto"><p id="293c5e6f-95bd-8058-a9b8-ebfbe1b7c63d" class=""><strong>[MỚI]</strong> <strong>Tạm nghỉ ngắn</strong> (break 15’): không nhận cuốc nhưng giữ online cho đối soát.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80a2-95b2-d0ae5022b6c5" class="bulleted-list"><li style="list-style-type:disc"><strong>Hàng đợi cuốc &amp; nhận cuốc</strong>: xem chi tiết điểm đón/trả, ước tính cước &amp; thời gian; bấm <em>Nhận</em>.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-807e-a6fe-e79e2a7b0e51" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều hướng</strong>: mở điều hướng (Google/Apple Maps) tới điểm đón &amp; tới điểm trả.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80aa-b564-c2be6ea1458b" class="bulleted-list"><li style="list-style-type:disc"><strong>Trạng thái chuyến</strong>: <em>Đến điểm đón</em> → <em>Đã đón khách</em> → <em>Kết thúc chuyến</em>.<div style="display:contents" dir="auto"><p id="293c5e6f-95bd-8007-ae88-d382e1de946d" class=""><strong>[MỚI]</strong> Log <strong>bằng chứng đón khách</strong> (1 chạm; tùy chọn ảnh/ghi chú nếu chính sách yêu cầu).</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8003-b73f-dfa75ff29dc8" class="bulleted-list"><li style="list-style-type:disc"><strong>Thu nhập cơ bản</strong>: tổng doanh thu ngày/tuần; số cuốc/giờ; phí/chiết khấu hiển thị rõ.<div style="display:contents" dir="auto"><p id="293c5e6f-95bd-8057-b0bd-f5e75df712fa" class=""><strong>[MỚI]</strong> Tách <strong>doanh thu trước VAT / sau VAT</strong> (nếu tài xế là tổ chức chịu VAT).</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8091-ab2f-d4470173b7e9" class="bulleted-list"><li style="list-style-type:disc"><strong>Hủy cuốc theo quy định</strong>: chọn lý do; log lại.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80b8-b4b9-d84eb8d078f2" class="bulleted-list"><li style="list-style-type:disc"><strong>Lịch sử chuyến</strong>: chi tiết từng cuốc (km, phút, giá, chia sẻ doanh thu).</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8078-af93-dfea3d04bd3f" class="bulleted-list"><li style="list-style-type:disc"><strong>Hỗ trợ nhanh</strong>: gọi CS; báo cáo sự cố.<div style="display:contents" dir="auto"><p id="293c5e6f-95bd-809b-8f99-db6e045afa99" class=""><strong>[MỚI]</strong> <strong>SOS</strong>: gọi khẩn + gửi GPS tới hotline.</p></div><div style="display:contents" dir="auto"><p id="293c5e6f-95bd-8090-b180-e82965f7b7f3" class=""><strong>[MỚI – EV (khuyến nghị)]</strong> Hiển thị <strong>% pin</strong> và <strong>trạm sạc UniPower gần nhất</strong> khi pin &lt; ngưỡng (hook EV, có thể tắt/bật theo khu vực).</p></div></li></ul></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-80a2-ba0d-d1624646eb45" class=""><strong>2) Màn hình tối thiểu</strong></h2></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8040-a642-d15781078b38" class="bulleted-list"><li style="list-style-type:disc">OTP/Đăng nhập • Bật/Tắt nhận cuốc • Danh sách/Pop-up cuốc mới • Điều hướng • Trạng thái chuyến • Thu nhập • Lịch sử • Hỗ trợ.<div style="display:contents" dir="auto"><p id="293c5e6f-95bd-8075-8c0d-cb6efdbbe538" class=""><strong>[MỚI]</strong> <strong>SOS</strong> • <strong>Break Mode</strong> • <strong>Cảnh báo pin thấp/Trạm sạc</strong> (EV – tùy chọn).</p></div></li></ul></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-8010-ac36-ff18fea3c760" class=""><strong>3) Tiêu chí chấp nhận (Acceptance)</strong></h2></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-806f-b0be-f45f06e6f1f6" class="bulleted-list"><li style="list-style-type:disc">Nhận thông báo cuốc mới trong ≤2 giây từ lúc dispatch gửi.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80db-b53c-cbb0a9f32f95" class="bulleted-list"><li style="list-style-type:disc">Quy trình: Nhận cuốc → Điều hướng → Kết thúc → Đồng bộ doanh thu hoàn tất &lt; 5 giây.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-806e-97dd-f0e7e65f2599" class="bulleted-list"><li style="list-style-type:disc">App vẫn hiển thị trạng thái và lưu log tạm khi mất mạng ngắn (≤2 phút), tự đồng bộ lại.<div style="display:contents" dir="auto"><p id="293c5e6f-95bd-8090-be8a-e64a76dbdc0b" class=""><strong>[MỚI]</strong> Không cho đăng nhập đồng thời 2 thiết bị; nếu phát hiện → buộc đăng xuất thiết bị cũ.</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="293c5e6f-95bd-80b1-bb04-d18974a25c93"/></div><div style="display:contents" dir="auto"><h1 id="293c5e6f-95bd-804f-bd8d-f516cb22909d" class=""><strong>🧩 Yêu cầu nền tảng bổ sung (Backend/Compliance) — [MỚI]</strong></h1></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-8086-a0d1-f05ee1f02ead" class=""><strong>A) Hóa đơn điện tử (bắt buộc pháp lý khi UniPower thu tiền)</strong></h2></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-800f-a780-fbc3a08a0c84" class="bulleted-list"><li style="list-style-type:disc">Tích hợp API nhà cung cấp HĐĐT (MISA/Viettel/FPT/VNPT/BKAV…).</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8088-a5ee-db325ec9c854" class="bulleted-list"><li style="list-style-type:disc">Truyền <strong>buyer profile</strong> (MST/Tên/Địa chỉ/Email) nếu khách chọn “Xuất HĐ công ty”.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-801f-a226-d014288b2e6c" class="bulleted-list"><li style="list-style-type:disc">Nhận <strong>invoice_id, số hóa đơn, pdf/xml url, qrcode</strong>; lưu trữ ≥5 năm.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-802b-af2c-d5296749cbf8" class="bulleted-list"><li style="list-style-type:disc"><strong>Đồng bộ Tổng cục Thuế</strong>: theo dõi trạng thái queued/sent/accepted/rejected; tự retry; log mã lỗi.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80b0-9e24-dd448beb3841" class="bulleted-list"><li style="list-style-type:disc">Cho phép <strong>điều chỉnh/huỷ hóa đơn</strong> đúng quy trình khi hoàn tiền/hủy cuốc sau phát hành.</li></ul></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-8093-b13a-f15784bff000" class=""><strong>B) An toàn &amp; pháp lý</strong></h2></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8065-b450-e674df292b71" class="bulleted-list"><li style="list-style-type:disc"><strong>SOS Gateway</strong>: định tuyến cuộc gọi khẩn + đính kèm tọa độ; ghi lại log thời gian thực.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80eb-bdfc-cfe346d09b1f" class="bulleted-list"><li style="list-style-type:disc"><strong>Bảo vệ dữ liệu cá nhân (PII)</strong>: mã hóa at-rest/in-transit; ẩn số khi gọi; xóa/ẩn thông tin nhạy cảm trên màn hình lock.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8036-bda5-d0416d034a16" class="bulleted-list"><li style="list-style-type:disc"><strong>Chống gian lận</strong>: chặn đa phiên, phát hiện vị trí giả (mock location), kiểm tra bất thường dòng cuốc.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-803b-8fe6-e40e9a8dbaef" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều khoản &amp; Chính sách</strong>: màn <strong>Điều khoản sử dụng/Chính sách bảo mật</strong> trước khi sử dụng; checkbox đồng ý.</li></ul></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-807b-9c8f-cd49c33cacee" class=""><strong>C) Khả dụng &amp; vận hành</strong></h2></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8061-885a-ea0206c9153b" class="bulleted-list"><li style="list-style-type:disc"><strong>Offline resilience</strong>: hàng đợi sự kiện (trip state, payment, invoice request) để đồng bộ lại khi có mạng.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-804a-b52c-e29173868d10" class="bulleted-list"><li style="list-style-type:disc"><strong>Observability</strong>: log tập trung, trace giao dịch (trip → payment → invoice) để đối soát 100%.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80e6-8fdd-ffd6d55d2df1" class="bulleted-list"><li style="list-style-type:disc"><strong>UniPortal (ops)</strong>: bảng điều khiển thời gian thực (cuốc đang chạy, heatmap nhu cầu, tình trạng driver); xuất <strong>Báo cáo VAT</strong> hàng tháng.</li></ul></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-80cd-99c2-df1668c11337" class=""><strong>D) Hook EV (khuyến nghị bật theo khu vực)</strong></h2></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-806b-8330-dc875bf8f96a" class="bulleted-list"><li style="list-style-type:disc">API <strong>UniPower Charging</strong>: gợi ý trạm sạc theo SOC, công suất, tình trạng sẵn sàng.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-803b-bbe7-d2633cab333c" class="bulleted-list"><li style="list-style-type:disc">Cảnh báo <strong>SOC thấp</strong> khi nhận cuốc dài vượt phạm vi pin hiện tại.</li></ul></div><div style="display:contents" dir="auto"><hr id="293c5e6f-95bd-80c4-b93f-c1a0ec7928fa"/></div><div style="display:contents" dir="auto"><h1 id="293c5e6f-95bd-80f6-8ff7-e87f1524487f" class=""><strong>📏 Non-Functional &amp; QA — [MỚI]</strong></h1></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8088-af5e-f1012f90ab96" class="bulleted-list"><li style="list-style-type:disc"><strong>Hiệu năng</strong>: P95 API chính ≤ 300 ms; P99 ≤ 800 ms.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80d8-8880-cbfccd229626" class="bulleted-list"><li style="list-style-type:disc"><strong>Độ tin cậy</strong>: Uptime ≥ 99.9% cho Dispatch/Payment/Billing.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80c0-800c-f7ea02049bbd" class="bulleted-list"><li style="list-style-type:disc"><strong>Bảo mật</strong>: Pentest không rò rỉ PII/thuế; rate limit &amp; WAF.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80d1-955a-ede03ea599b6" class="bulleted-list"><li style="list-style-type:disc"><strong>Kiểm thử bắt buộc</strong>:<div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-801b-a410-c147bd3f9f6e" class="bulleted-list"><li style="list-style-type:circle"><strong>Offline &gt;2 phút</strong> không mất dữ liệu chuyến &amp; yêu cầu HĐĐT.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8099-a4e6-ccc5a28bcf87" class="bulleted-list"><li style="list-style-type:circle"><strong>Giao dịch nhiều phương thức</strong> (mixed payments) vẫn phát hành 1 HĐĐT tổng.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80b6-a4fa-cf0f669a2351" class="bulleted-list"><li style="list-style-type:circle"><strong>GDT rejected</strong> → hiển thị pending, retry thành công trong 24h.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="293c5e6f-95bd-806f-9d58-e78074f4c4fa"/></div><div style="display:contents" dir="auto"><h1 id="293c5e6f-95bd-804b-b101-da759ba316d9" class=""><strong>UniPower Referral &amp; Revenue-Sharing System (3% Lifetime Benefit)</strong></h1></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-8080-8eb4-c77cd9dcc75c" class=""><strong>1. Purpose &amp; Overview</strong></h2></div><div style="display:contents" dir="auto"><p id="293c5e6f-95bd-8011-8242-e51f292fc2ba" class="">The referral system is designed to <strong>reward UniPower members</strong> (drivers, riders, or partners) who help expand the UniPower ecosystem.</p></div><div style="display:contents" dir="auto"><p id="293c5e6f-95bd-806d-93f2-f9204646e3f3" class="">Each member receives <strong>3% of the net profit</strong> generated by any user they refer — <strong>for as long as both remain active</strong> in the system.</p></div><div style="display:contents" dir="auto"><p id="293c5e6f-95bd-8065-9a12-cb5029757315" class="">This program incentivises organic growth while keeping full transparency, automation, and legal compliance with Vietnamese tax law.</p></div><div style="display:contents" dir="auto"><hr id="293c5e6f-95bd-807e-ad79-eae9e881e7c5"/></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-80ed-a27d-c4fe13967e94" class=""><strong>2. Core Structure</strong></h2></div><div style="display:contents" dir="auto"><h3 id="293c5e6f-95bd-8040-a92a-f8098ab53473" class=""><strong>Referral Logic</strong></h3></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80b4-baea-eb2aa0bbfece" class="bulleted-list"><li style="list-style-type:disc">Every registered user automatically receives:<div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-802e-a7eb-ea031d226515" class="bulleted-list"><li style="list-style-type:circle">A <strong>unique referral code</strong> (e.g., UNI1234)</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80b5-93d8-fd80950c031e" class="bulleted-list"><li style="list-style-type:circle">A <strong>referral QR code</strong> (e.g., https://unipower.vn/r/UNI1234)</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8087-a79d-f8db45f34f0c" class="bulleted-list"><li style="list-style-type:disc">When a new user registers via <strong>QR scan</strong> or <strong>referral code</strong>, the backend records a <strong>referral link</strong>:</li></ul></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="293c5e6f-95bd-8013-85f5-d4ba6627aa80" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">referrer_id → referee_id</code></pre></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-806c-8e17-ef341749c060" class="bulleted-list"><li style="list-style-type:disc"></li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8042-b704-e760b4a10d2b" class="bulleted-list"><li style="list-style-type:disc">The referral relationship is <strong>one-time and permanent</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8084-89b2-ded8de0ace88" class="bulleted-list"><li style="list-style-type:disc">The referrer earns <strong>3% of UniPower’s net profit</strong> generated by the referred member’s activities (rides, transactions, partnerships) as long as both accounts remain active.</li></ul></div><div style="display:contents" dir="auto"><hr id="293c5e6f-95bd-8083-a5fe-f894fc49bd6b"/></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-8053-9be5-cbed9dcfc2ae" class=""><strong>3. Financial Flow</strong></h2></div><div style="display:contents" dir="auto"><h3 id="293c5e6f-95bd-80eb-8993-fe4ee1488ee5" class=""><strong>Profit Base for Reward Calculation</strong></h3></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8021-adce-ce36d10b6332" class="bulleted-list"><li style="list-style-type:disc">The 3% benefit is calculated from <strong>UniPower’s retained net profit portion</strong>, not from the total transaction amount.<div style="display:contents" dir="auto"><p id="293c5e6f-95bd-8064-a418-ff59cb95d598" class="">Example:</p></div></li></ul></div><div style="display:contents" dir="auto"><pre id="293c5e6f-95bd-8023-a322-ce634bba05ee" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Rider pays 100,000₫
Driver receives 85,000₫
UniPower retains 15,000₫ (net profit portion)
→ Referrer earns 3% × 15,000₫ = 450₫</code></pre></div><div style="display:contents" dir="auto"><h3 id="293c5e6f-95bd-80eb-ae99-dc76e54d4cf3" class=""><strong>Reward Trigger</strong></h3></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8019-92f2-fd4ee49a0f65" class="bulleted-list"><li style="list-style-type:disc">Generated automatically at the time of <strong>trip settlement</strong> (for drivers) or <strong>invoice confirmation</strong> (for riders or partners).</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8056-8df4-c1dd1da0de87" class="bulleted-list"><li style="list-style-type:disc">Stored in the user’s <strong>Referral Wallet</strong> inside the UniPower app.</li></ul></div><div style="display:contents" dir="auto"><h3 id="293c5e6f-95bd-8059-ae32-de9a296d0030" class=""><strong>Payout &amp; Settlement</strong></h3></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80e5-8dae-d7c023d77718" class="bulleted-list"><li style="list-style-type:disc">Minimum withdrawal threshold: e.g., <strong>100,000₫</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80ab-99e6-c60362858ca4" class="bulleted-list"><li style="list-style-type:disc">Payout methods: internal UniWallet → VNPay / MoMo / bank transfer.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8043-b7f2-e2ab6b20442a" class="bulleted-list"><li style="list-style-type:disc">Cycle: <strong>Monthly automatic settlement</strong> or <strong>manual withdrawal</strong> by the user.</li></ul></div><div style="display:contents" dir="auto"><hr id="293c5e6f-95bd-803f-92e7-c3e3323edc62"/></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-809c-9e18-e09990c6d645" class=""><strong>4. Referral Identification Options</strong></h2></div><div style="display:contents" dir="ltr"><table id="293c5e6f-95bd-80a0-a922-def7b4b3f32a" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-802e-a731-e62a4b65e431"><th id="k}\|" class="simple-table-header-color simple-table-header"><strong>Option</strong></th><th id="iVHf" class="simple-table-header-color simple-table-header"><strong>Description</strong></th><th id="KRXE" class="simple-table-header-color simple-table-header"><strong>Pros</strong></th><th id="]ty:" class="simple-table-header-color simple-table-header"><strong>Cons</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-80f9-93e6-c4fd49907e74"><td id="k}\|" class=""><strong>QR-based referral</strong></td><td id="iVHf" class="">Each user shares a QR code for others to scan</td><td id="KRXE" class="">Seamless onboarding, strong offline usability</td><td id="]ty:" class="">Requires camera permissions</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-80ca-b92a-dd38bc84d067"><td id="k}\|" class=""><strong>Referral code</strong></td><td id="iVHf" class="">User manually enters the referrer’s code during signup</td><td id="KRXE" class="">Very easy to implement</td><td id="]ty:" class="">Typing errors possible</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-80b2-9df4-f79fdd38857f"><td id="k}\|" class=""><strong>Hybrid (Recommended)</strong></td><td id="iVHf" class="">QR automatically fills the code; code entry as backup</td><td id="KRXE" class="">Best UX, works both online &amp; offline</td><td id="]ty:" class="">Slightly more backend logic</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="293c5e6f-95bd-8015-ae99-c36abd6f3142" class="">✅ <strong>Recommended for MVP:</strong> Hybrid model — generate both a <strong>code and QR</strong> per user.</p></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80d2-9f6c-d384d413259c" class="bulleted-list"><li style="list-style-type:disc">The referral QR is a short URL (e.g., https://unipower.vn/signup?ref=UNI1234).</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8055-ad93-d31bba228e49" class="bulleted-list"><li style="list-style-type:disc">When the app opens with a referral parameter, the backend links the referrer and referee automatically.</li></ul></div><div style="display:contents" dir="auto"><hr id="293c5e6f-95bd-801e-ae2c-e3d2f29e3674"/></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-8021-9a17-fa5661c0c6fc" class=""><strong>5. Database Schema (Simplified)</strong></h2></div><div style="display:contents" dir="auto"><p id="293c5e6f-95bd-800b-ae81-e8ea3d385d3d" class=""><strong>Table: users</strong></p></div><div style="display:contents" dir="ltr"><table id="293c5e6f-95bd-8058-8342-f278812020a9" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-80a9-8e0c-c5fc35a1078e"><th id="qNIC" class="simple-table-header-color simple-table-header"><strong>Field</strong></th><th id="wyhK" class="simple-table-header-color simple-table-header"><strong>Type</strong></th><th id="?f[s" class="simple-table-header-color simple-table-header"><strong>Description</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-8057-9f5e-f34ca25867e4"><td id="qNIC" class="">id</td><td id="wyhK" class="">INT</td><td id="?f[s" class="">User ID</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-8079-b474-cd2a0e005c37"><td id="qNIC" class="">name</td><td id="wyhK" class="">VARCHAR</td><td id="?f[s" class="">Full name</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-80ca-9bd7-d2f9655a768e"><td id="qNIC" class="">phone</td><td id="wyhK" class="">VARCHAR</td><td id="?f[s" class="">Login ID</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-8002-acfa-fc3a92a855cb"><td id="qNIC" class="">referral_code</td><td id="wyhK" class="">VARCHAR</td><td id="?f[s" class="">Unique referral code</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-806c-a36e-d44bca36e195"><td id="qNIC" class="">referrer_id</td><td id="wyhK" class="">INT</td><td id="?f[s" class="">ID of referring user</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-80e5-998b-ecf3a1614229"><td id="qNIC" class="">role</td><td id="wyhK" class="">ENUM</td><td id="?f[s" class="">Rider / Driver / Partner</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-8081-93a7-f5801187947d"><td id="qNIC" class="">active</td><td id="wyhK" class="">BOOLEAN</td><td id="?f[s" class="">Account status</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="293c5e6f-95bd-8009-9184-e5bea2435086" class=""><strong>Table: referral_rewards</strong></p></div><div style="display:contents" dir="ltr"><table id="293c5e6f-95bd-801a-85ec-cb05b8bbdbce" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-8028-98df-c1c0e56bcb16"><th id="@=Jf" class="simple-table-header-color simple-table-header"><strong>Field</strong></th><th id="ENW[" class="simple-table-header-color simple-table-header"><strong>Type</strong></th><th id="Zl_|" class="simple-table-header-color simple-table-header"><strong>Description</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-80e6-8501-c12971c960c4"><td id="@=Jf" class="">id</td><td id="ENW[" class="">INT</td><td id="Zl_|" class="">Reward record ID</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-803e-83ac-cd3ead5d02c1"><td id="@=Jf" class="">referrer_id</td><td id="ENW[" class="">INT</td><td id="Zl_|" class="">Who earned the reward</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-8041-80c0-c4d40c56c62a"><td id="@=Jf" class="">referee_id</td><td id="ENW[" class="">INT</td><td id="Zl_|" class="">Whose transaction triggered it</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-8056-8e86-fa5e93489f13"><td id="@=Jf" class="">transaction_id</td><td id="ENW[" class="">INT</td><td id="Zl_|" class="">Related trip or order</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-8038-809c-edbd49f431f7"><td id="@=Jf" class="">profit_base</td><td id="ENW[" class="">DECIMAL</td><td id="Zl_|" class="">UniPower profit portion</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-8060-8476-fe08d469c0f5"><td id="@=Jf" class="">reward_amount</td><td id="ENW[" class="">DECIMAL</td><td id="Zl_|" class="">3% of profit base</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-8083-a6ab-d37cd080e317"><td id="@=Jf" class="">created_at</td><td id="ENW[" class="">DATETIME</td><td id="Zl_|" class="">Time of calculation</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-8067-9d5f-f319e9b88953"><td id="@=Jf" class="">status</td><td id="ENW[" class="">ENUM</td><td id="Zl_|" class="">pending / paid / cancelled</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="293c5e6f-95bd-80ba-9146-e7c843689e02" class=""><strong>Table: wallet</strong></p></div><div style="display:contents" dir="ltr"><table id="293c5e6f-95bd-80f7-b29a-cf9dc0c3428d" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-800c-a6a1-dc2620846159"><th id="|bii" class="simple-table-header-color simple-table-header"><strong>Field</strong></th><th id="oj`f" class="simple-table-header-color simple-table-header"><strong>Type</strong></th><th id="{Huv" class="simple-table-header-color simple-table-header"><strong>Description</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-801b-ba37-ed93409cd108"><td id="|bii" class="">id</td><td id="oj`f" class="">INT</td><td id="{Huv" class="">Wallet ID</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-808f-b8c6-d40033fcb3fe"><td id="|bii" class="">user_id</td><td id="oj`f" class="">INT</td><td id="{Huv" class="">Linked user</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-80c5-a477-d021b30b11d8"><td id="|bii" class="">balance</td><td id="oj`f" class="">DECIMAL</td><td id="{Huv" class="">Current wallet balance</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-80ec-90c6-c7ed9e6e8b0e"><td id="|bii" class="">total_earned</td><td id="oj`f" class="">DECIMAL</td><td id="{Huv" class="">Cumulative referral earnings</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-8023-bf8b-d52310c2927a"><td id="|bii" class="">last_withdrawal</td><td id="oj`f" class="">DATETIME</td><td id="{Huv" class="">Last payout date</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="293c5e6f-95bd-8009-b3b9-cd12580b3f78"/></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-8087-be39-eb5fdacaad71" class=""><strong>6. Legal &amp; Tax Compliance (Vietnam)</strong></h2></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-802d-b1d9-cca6d09a69e2" class="bulleted-list"><li style="list-style-type:disc">Referral earnings are classified as <strong>“marketing or referral income”</strong> under Vietnamese law.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80fe-8d0c-dd62535cb046" class="bulleted-list"><li style="list-style-type:disc">UniPower must:<div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8078-83cc-cb5fe9508637" class="bulleted-list"><li style="list-style-type:circle">Record all referral reward transactions.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8095-94f0-d334cc4b1eff" class="bulleted-list"><li style="list-style-type:circle">Deduct <strong>5% PIT (Personal Income Tax)</strong> for individual referrers.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80c8-aff3-e33b112f43ec" class="bulleted-list"><li style="list-style-type:circle">Issue a valid <strong>e-invoice for referral income</strong> under UniPower’s tax ID.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80e8-b32c-df23c21738a3" class="bulleted-list"><li style="list-style-type:circle">Report referral income in the monthly tax declaration.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="293c5e6f-95bd-809e-addb-cb35a9a61e3e" class="">If the referrer is an official business entity or partner with a tax code, UniPower can settle <strong>B2B-style payouts</strong> with standard VAT invoices.</p></div><div style="display:contents" dir="auto"><hr id="293c5e6f-95bd-80e1-b200-c560b780ba1e"/></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-806d-8d36-f8501c72d745" class=""><strong>7. App-Level Functional Requirements</strong></h2></div><div style="display:contents" dir="auto"><h3 id="293c5e6f-95bd-8059-90e2-f3e622fc6072" class=""><strong>Rider / Driver / Partner App</strong></h3></div><div style="display:contents" dir="auto"><p id="293c5e6f-95bd-807e-9dc9-f731bf6780c6" class=""><strong>Referral Page – “Invite Friends”</strong></p></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8083-89fc-e24988701107" class="bulleted-list"><li style="list-style-type:disc">Displays:<div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8083-9956-eb501e1ca7e4" class="bulleted-list"><li style="list-style-type:circle">User’s QR code</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8076-9626-cd94dad1b333" class="bulleted-list"><li style="list-style-type:circle">Referral code</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-809d-bc4a-ce6f2cf69491" class="bulleted-list"><li style="list-style-type:circle">Share button (“Copy link” / “Share via Zalo/Facebook”)</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80e2-90eb-c6f938c7dae0" class="bulleted-list"><li style="list-style-type:circle">Summary of total earned and active referees</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80b9-b190-d0881f26bea7" class="bulleted-list"><li style="list-style-type:circle">Referral Terms &amp; Conditions</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="293c5e6f-95bd-8084-b95d-de1bfe41b515" class=""><strong>Signup Flow</strong></p></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-807e-ae73-f6eab37da1dc" class="bulleted-list"><li style="list-style-type:disc">If QR scanned → app opens with referral param auto-filled.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80a3-8c2b-f50c62e3a830" class="bulleted-list"><li style="list-style-type:disc">If manually entered → validate code and lock-in permanently.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80c8-b5fe-de887c49af7a" class="bulleted-list"><li style="list-style-type:disc">Display referrer name confirmation before finalising.</li></ul></div><div style="display:contents" dir="auto"><p id="293c5e6f-95bd-80cd-bed8-ebefbfe9dfa0" class=""><strong>Referral Wallet</strong></p></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80b0-ac1d-d27894843d4b" class="bulleted-list"><li style="list-style-type:disc">Show:<div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8083-ba51-d1c97fd2be20" class="bulleted-list"><li style="list-style-type:circle">Total earned</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8075-8903-d61588c5d958" class="bulleted-list"><li style="list-style-type:circle">Pending earnings</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-805c-8306-d5f8a84b18cd" class="bulleted-list"><li style="list-style-type:circle">Transaction history</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80c7-ab5e-efb59972ef91" class="bulleted-list"><li style="list-style-type:circle">Withdraw button</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-800a-a1f9-efde7fa165cf" class="bulleted-list"><li style="list-style-type:disc">Real-time balance updates (≤10 seconds after transaction confirmation).</li></ul></div><div style="display:contents" dir="auto"><hr id="293c5e6f-95bd-8046-aeb8-f31201e6b9b6"/></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-80a5-926b-da544fd7ff44" class=""><strong>8. Backend Logic</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="293c5e6f-95bd-802d-92af-f112f5cbc0c4" class="numbered-list" start="1"><li><strong>Registration:</strong><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8074-8967-ff5e9d2d642e" class="bulleted-list"><li style="list-style-type:disc">When referral_code detected, backend resolves to referrer_id and links new user.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="293c5e6f-95bd-80c0-9d14-c7ee422d2ab0" class="numbered-list" start="2"><li><strong>Transaction Processing:</strong><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80c9-a4e2-ccffee2bd11b" class="bulleted-list"><li style="list-style-type:disc">When any transaction with profit occurs, fetch referrer_id.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8061-93ab-ec68be7f03a0" class="bulleted-list"><li style="list-style-type:disc">Compute reward = net_profit × 0.03.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8096-84c6-c6a2cd6a9670" class="bulleted-list"><li style="list-style-type:disc">Create a new record in referral_rewards and update wallet balance.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="293c5e6f-95bd-8010-a1b1-ea5ccf53a340" class="numbered-list" start="3"><li><strong>Payout:</strong><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8044-a62f-d21a1173538e" class="bulleted-list"><li style="list-style-type:disc">When user withdraws or during monthly batch payout, deduct <strong>5% PIT</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-808a-ade7-ed8af96e5483" class="bulleted-list"><li style="list-style-type:disc">Log transaction, issue e-invoice, and send confirmation message.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="293c5e6f-95bd-80ca-b139-eeb9c29144c4"/></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-8031-ae84-ccaa5cadcaef" class=""><strong>9. Anti-Fraud Rules</strong></h2></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80d8-8675-df5a509d92ea" class="bulleted-list"><li style="list-style-type:disc">Only <strong>one referral level</strong> — no multi-level chains.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-804a-b0f6-e95c900b6f0e" class="bulleted-list"><li style="list-style-type:disc">Both referrer and referee must be <strong>active</strong> (last login &lt; 30 days).</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-808e-9087-ca1a73c49c3c" class="bulleted-list"><li style="list-style-type:disc">Referee must have completed at least <strong>one paid trip or transaction</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8064-94b6-e1f5374b4bd0" class="bulleted-list"><li style="list-style-type:disc">No referral reward for self-referrals, duplicate numbers, or same device IDs.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80d6-8bca-e9bb14f66a0a" class="bulleted-list"><li style="list-style-type:disc">Maximum reward per referred user per month: configurable (e.g., ₫200,000).</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80d9-8445-c80f33d97305" class="bulleted-list"><li style="list-style-type:disc">Referral relationship is <strong>immutable</strong> (cannot be changed after signup).</li></ul></div><div style="display:contents" dir="auto"><hr id="293c5e6f-95bd-8007-9956-e2d3e5eb73be"/></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-8014-b2f8-e062fd42815e" class=""><strong>10. Technical Summary</strong></h2></div><div style="display:contents" dir="ltr"><table id="293c5e6f-95bd-8097-a164-d81e4fb05e61" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-80ef-87c7-cd5b4bc7ecd4"><th id="xpyT" class="simple-table-header-color simple-table-header"><strong>Component</strong></th><th id="mEVS" class="simple-table-header-color simple-table-header"><strong>Description</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-807a-9bc8-ec360a9caba2"><td id="xpyT" class="">Referral Code</td><td id="mEVS" class="">Auto-generated alphanumeric (Base36 from userID)</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-8078-84ab-d0c850919006"><td id="xpyT" class="">Referral QR</td><td id="mEVS" class="">Short link encoded with referral param</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-8028-ab1a-ee22243f2177"><td id="xpyT" class="">Tracking</td><td id="mEVS" class="">Relational mapping (referrer_id → referee_id)</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-806a-aa44-d3ff4be3abef"><td id="xpyT" class="">Wallet</td><td id="mEVS" class="">Sub-ledger within UniWallet service</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-8012-9440-ded0e5dfc0d5"><td id="xpyT" class="">Admin Portal</td><td id="mEVS" class="">Dashboard: top referrers, earnings, audit logs, export CSV</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-8073-b98b-d378d43b64a4"><td id="xpyT" class="">Notification</td><td id="mEVS" class="">“You earned 3% from your referral’s activity!” push/email</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-80b9-a56e-e36b65eab9b6"><td id="xpyT" class="">API Exposure</td><td id="mEVS" class="">/api/v1/referrals (link, reward, wallet, withdraw)</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="293c5e6f-95bd-8015-8673-f8eca94d1bea"/></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-80b0-a0eb-d2e67b0a8b56" class=""><strong>11. Acceptance Criteria</strong></h2></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-800d-836d-dd797ee4664e" class="bulleted-list"><li style="list-style-type:disc">Each user receives a <strong>unique code and QR</strong> upon registration.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80a0-908b-cd445e255313" class="bulleted-list"><li style="list-style-type:disc">New signups via code or QR correctly link the referrer.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-801f-aa05-e0638d23edd6" class="bulleted-list"><li style="list-style-type:disc">Rewards automatically calculated as <strong>3% of UniPower’s profit portion</strong> (accuracy &lt; ±1₫).</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-808a-adbe-ee1b9051c383" class="bulleted-list"><li style="list-style-type:disc">Referral wallet updates within <strong>10 seconds</strong> after qualifying transaction.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80d6-8bfc-ec7534027da1" class="bulleted-list"><li style="list-style-type:disc">History and payout records visible in-app and Admin Portal.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8066-b4e9-ff10b6330d48" class="bulleted-list"><li style="list-style-type:disc">Duplicate or fraudulent referrals blocked at registration.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80ad-8564-e70029284f89" class="bulleted-list"><li style="list-style-type:disc">Tax (5% PIT) deducted and logged on every withdrawal.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-805c-a750-f39cd1af4af6" class="bulleted-list"><li style="list-style-type:disc">Monthly summary export for Finance includes:<div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8018-b0fb-f51c701c2783" class="bulleted-list"><li style="list-style-type:circle">Total referrals, total payout, withheld PIT, outstanding balance.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="293c5e6f-95bd-808c-93c3-d303e5a4e92a"/></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-806c-b7fe-ded33c756e25" class=""><strong>12. Example User Flow</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="293c5e6f-95bd-80a8-bf7a-dcb956d9928f" class="numbered-list" start="1"><li>Driver A shares their referral QR with friend B.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="293c5e6f-95bd-808d-a0f7-d2aaf7c02406" class="numbered-list" start="2"><li>B scans and registers → referrer_id = A.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="293c5e6f-95bd-807d-b64e-cc38c2731cbd" class="numbered-list" start="3"><li>B starts driving, generating ₫2,000,000 in UniPower profit that month.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="293c5e6f-95bd-8000-b997-dce4e4253787" class="numbered-list" start="4"><li>A automatically earns ₫60,000 (3% × 2,000,000).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="293c5e6f-95bd-8011-b5d9-c14d296b8f40" class="numbered-list" start="5"><li>A’s Referral Wallet updates instantly.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="293c5e6f-95bd-80ea-bb22-d0419d213b8c" class="numbered-list" start="6"><li>When balance &gt; ₫100,000, A withdraws → UniPower deducts 5% PIT → pays ₫57,000 net.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="293c5e6f-95bd-807c-84ae-d63c2f81053f" class="numbered-list" start="7"><li>Invoice generated and stored for audit.</li></ol></div><div style="display:contents" dir="auto"><hr id="293c5e6f-95bd-80ee-a093-f73550101574"/></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-80ca-93f4-f793877fdbd2" class=""><strong>13. Optional Future Enhancements</strong></h2></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80e4-8055-eb97a4c7a546" class="bulleted-list"><li style="list-style-type:disc"><strong>Tiered rewards</strong> (e.g., 3% first 6 months → 1% thereafter).</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-806f-8fef-c89b90dbed9a" class="bulleted-list"><li style="list-style-type:disc"><strong>Referral leaderboard</strong> (monthly ranking with bonuses).</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-806e-a31b-d8b4452196ed" class="bulleted-list"><li style="list-style-type:disc"><strong>Promo integration</strong> (QR scan triggers ride discounts for new users).</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-801a-b7cf-ed071910991c" class="bulleted-list"><li style="list-style-type:disc"><strong>Geo-restricted campaigns</strong> (target city or driver hub).</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80a1-9350-f3d78b74ee96" class="bulleted-list"><li style="list-style-type:disc"><strong>Blockchain logging (phase 3)</strong> for transparent audit trail of all referral rewards.</li></ul></div><div style="display:contents" dir="auto"><hr id="293c5e6f-95bd-800c-8598-c23abd67f8ff"/></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-805b-aac6-dac9bc60c9c7" class=""><strong>14. Security &amp; Compliance</strong></h2></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8043-b752-dc72f3cf7246" class="bulleted-list"><li style="list-style-type:disc">All referral data encrypted in-transit (TLS 1.2+) and at-rest (AES-256).</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80f5-86fd-ddd4de04b6a1" class="bulleted-list"><li style="list-style-type:disc">Payout actions restricted to verified accounts (KYC).</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-802e-993f-c09b9f18766b" class="bulleted-list"><li style="list-style-type:disc">Session control to prevent device spoofing or shared credentials.</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8075-a602-c18928f91580" class="bulleted-list"><li style="list-style-type:disc">Monthly referral ledger archived for 5 years (tax audit requirement).</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-808a-a320-e3fcccf1e96b" class="bulleted-list"><li style="list-style-type:disc">GDPR-style user consent for marketing and referral participation.</li></ul></div><div style="display:contents" dir="auto"><hr id="293c5e6f-95bd-80be-b071-e70f53e9d333"/></div><div style="display:contents" dir="auto"><h2 id="293c5e6f-95bd-803c-9634-db66dc2514ce" class=""><strong>15. Summary</strong></h2></div><div style="display:contents" dir="ltr"><table id="293c5e6f-95bd-8011-9b7f-fbf8d622d1ea" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-8016-a2fd-ff7e2a609a0a"><th id="VtUF" class="simple-table-header-color simple-table-header"><strong>Category</strong></th><th id="[:&lt;t" class="simple-table-header-color simple-table-header"><strong>Status</strong></th><th id="xn^K" class="simple-table-header-color simple-table-header"><strong>Notes</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-80bc-8aad-eab95eeee066"><td id="VtUF" class="">Legal compliance</td><td id="[:&lt;t" class="">✅</td><td id="xn^K" class="">Follows VN tax &amp; invoice laws</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-80f9-b3d5-d757c3650c64"><td id="VtUF" class="">Technical scalability</td><td id="[:&lt;t" class="">✅</td><td id="xn^K" class="">Single-level model; low complexity</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-80ba-86c9-f8e99d458051"><td id="VtUF" class="">Payout automation</td><td id="[:&lt;t" class="">✅</td><td id="xn^K" class="">Wallet-based, easy reconciliation</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-803d-ab35-e6f40dd0986a"><td id="VtUF" class="">Fraud prevention</td><td id="[:&lt;t" class="">✅</td><td id="xn^K" class="">One-level link, KYC, active check</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-80c1-8ffe-d58e4104af85"><td id="VtUF" class="">UX simplicity</td><td id="[:&lt;t" class="">✅</td><td id="xn^K" class="">QR + code hybrid onboarding</td></tr></div><div style="display:contents" dir="ltr"><tr id="293c5e6f-95bd-805c-b1ef-e5552acb5ca9"><td id="VtUF" class="">Viral potential</td><td id="[:&lt;t" class="">✅</td><td id="xn^K" class="">Encourages organic user growth</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="293c5e6f-95bd-8098-a504-d11c6aafc980"/></div><div style="display:contents" dir="auto"><h3 id="293c5e6f-95bd-8021-a5f6-f3dee38e2e58" class=""><strong>Final Recommendation</strong></h3></div><div style="display:contents" dir="auto"><p id="293c5e6f-95bd-8091-82da-eb57bf13c8e7" class="">Implement the <strong>Hybrid Referral Model (QR + Code)</strong> with:</p></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80f3-aada-f97fd8518210" class="bulleted-list"><li style="list-style-type:disc">3% lifetime profit share,</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-80b7-9cfd-f5ef84a2b51f" class="bulleted-list"><li style="list-style-type:disc">automatic wallet accrual,</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8007-92e5-c61eec65dba8" class="bulleted-list"><li style="list-style-type:disc">5% tax withholding,</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8071-be72-e658c352c7ad" class="bulleted-list"><li style="list-style-type:disc">real-time notifications,</li></ul></div><div style="display:contents" dir="auto"><ul id="293c5e6f-95bd-8093-96d8-f470dd5799b6" class="bulleted-list"><li style="list-style-type:disc">fully auditable payout ledger.</li></ul></div><div style="display:contents" dir="auto"><p id="293c5e6f-95bd-80ce-a250-e7209a8e7198" class="">This achieves <strong>high viral growth</strong>, <strong>legal compliance</strong>, and <strong>financial transparency</strong> — perfectly aligned with UniPower’s ethical and scalable ecosystem.</p></div><div style="display:contents" dir="auto"><hr id="293c5e6f-95bd-804d-a8b9-f81a3d6aa2cf"/></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
