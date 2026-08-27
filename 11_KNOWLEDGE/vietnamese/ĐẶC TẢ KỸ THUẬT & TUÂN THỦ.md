---
tags: [vietnamese]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>ĐẶC TẢ KỸ THUẬT &amp; TUÂN THỦ</title><style>
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
	
</style></head><body><article id="2c0c5e6f-95bd-8087-b89c-e8856ff1ba4d" class="page sans"><header><h1 class="page-title" dir="auto"><strong>ĐẶC TẢ KỸ THUẬT &amp; TUÂN THỦ</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-80e8-b364-c0d02e762d5a" class=""><strong>TÍCH HỢP CỔNG THANH TOÁN &amp; HÓA ĐƠN ĐIỆN TỬ MISA – NỀN TẢNG UNITAXI CỦA UNIPOWER</strong></h2></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-8050-b417-e670dc3aad1f"/></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-8049-94a0-d4d6ab755f35" class=""><strong>0. Khung pháp lý và nguyên tắc thiết kế</strong></h2></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80ea-b2b7-cfb7285886cc" class="">Hệ thống thanh toán và hóa đơn điện tử trên nền tảng UniTaxi của UNIPOWER phải tuân thủ các nhóm quy định về thanh toán không dùng tiền mặt (nghị định và quy định của Ngân hàng Nhà nước về trung gian thanh toán, ví điện tử, cổng thanh toán), hoạt động thẻ ngân hàng và trung gian thanh toán (NAPAS, VNPAY, MoMo, ViettelPay…), hóa đơn điện tử (hệ thống của MISA đã được Tổng cục Thuế cấp phép), bảo vệ dữ liệu cá nhân (PDPD – coi dữ liệu thanh toán và dữ liệu thuế là dữ liệu nhạy cảm, yêu cầu hạn chế truy cập, mã hóa, log truy cập) và an toàn thông tin/an ninh mạng (máy chủ, log và xử lý sự cố phải tuân thủ luật liên quan, dữ liệu đặt tại hoặc có bản sao tại Việt Nam).</p></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8021-a35a-faa66766dcd3" class="">Nguyên tắc thiết kế: UNIPOWER không được coi là trung gian thanh toán, không vận hành ví điện tử, không giữ số dư, không cho phép chuyển tiền giữa người dùng trong ứng dụng và không tự cung cấp sản phẩm tài chính (BNPL, cho vay, tín dụng…). Việc xử lý dòng tiền và lưu trữ thông tin thanh toán nhạy cảm phải do các đơn vị đã được cấp phép đảm nhiệm (MoMo, VNPAY, ViettelPay, cổng thanh toán ngân hàng/NAPAS; MISA cho hóa đơn điện tử). Hệ thống UniTaxi chỉ lưu trữ tối thiểu dữ liệu cần thiết, không lưu số thẻ đầy đủ, không lưu OTP/PIN/CVV, chủ yếu lưu token/mã tham chiếu giao dịch để phục vụ đối soát. Mọi thay đổi trạng thái giao dịch và hóa đơn đều phải có audit đầy đủ (trước/sau, thời điểm, tác nhân, nguồn thay đổi).</p></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-80c7-bc08-f8a89b8658c7"/></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-80d8-b63e-e1be8cfadab9" class=""><strong>1. Kiến trúc tổng – Payment + Invoice trên UniTaxi</strong></h2></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8046-9e57-cbb26f1039f8" class="">Kiến trúc UniTaxi liên quan đến thanh toán và hóa đơn gồm: ứng dụng UniTaxi phía khách, ứng dụng UniTaxi phía tài xế, backend nghiệp vụ UniTaxi (API), một dịch vụ thanh toán nội bộ (Payment Service) làm “cổng thanh toán nội bộ” trừu tượng toàn bộ MoMo/VNPAY/ViettelPay/NAPAS, các cổng thanh toán bên ngoài (MoMo, VNPAY, ViettelPay, cổng ngân hàng) và kết nối đến MISA eInvoice cho hóa đơn điện tử. Tầng dữ liệu nội bộ có sổ cái thanh toán (payment ledger) lưu PaymentIntent, PaymentTransaction và ReconciliationBatch phục vụ đối soát.</p></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8063-b64e-c5cbadf390d0" class="">Các đối tượng chính:</p></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8063-b155-f74436bffbf2" class="bulleted-list"><li style="list-style-type:disc"><strong>Ride (chuyến UniTaxi)</strong> – mã chuyến, khách, tài xế, số tiền, phương thức thanh toán, trạng thái thanh toán (UNPAID, PENDING, PAID_NONCASH, PAID_CASH, REFUNDED).</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8039-a129-c2ad02f3646b" class="bulleted-list"><li style="list-style-type:disc"><strong>PaymentIntent</strong> – một “ý định thanh toán” với số tiền và phương thức (CASH, MOMO, VNPAY, VIETTELPAY, CARD_BANK), trạng thái PENDING/IN_PROGRESS/SUCCEEDED/FAILED/CANCELED, gắn với ride_id.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-806f-9c36-f74d5430e3fe" class="bulleted-list"><li style="list-style-type:disc"><strong>PaymentTransaction</strong> – một giao dịch thực tế với nhà cung cấp, chứa nhà cung cấp (MOMO/VNPAY/VIETTELPAY/BANK), provider_order_id/txnRef/transId, amount, status CREATED/PENDING_GATEWAY/SUCCESS/FAILURE/REFUNDED, payload yêu cầu/phản hồi, ipn_payload, mã lỗi.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8036-8d6a-d17dcc91d725" class="bulleted-list"><li style="list-style-type:disc"><strong>InvoiceRequest/Invoice</strong> – yêu cầu và kết quả phát hành hóa đơn điện tử cho một ride, gắn với payment_transaction_id (đặc biệt với non-cash), thông tin bên mua (cá nhân/công ty), số tiền, VAT, trạng thái PENDING/SENDING_TO_MISA/ISSUED/FAILED/CANCELED, thông tin hóa đơn MISA (số, ký hiệu, ngày phát hành, PDF).</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-800e-b624-e2d45e82ae25" class="bulleted-list"><li style="list-style-type:disc"><strong>ReconciliationBatch</strong> – một lô đối soát hằng ngày với từng nhà cung cấp, bao gồm tổng số giao dịch, tổng tiền, tổng phí, trạng thái và mapping từng dòng provider_txn_id → PaymentTransaction.</li></ul></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-805c-9561-e37a42e2afd8"/></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-8044-8cb9-e0c061756bd8" class=""><strong>2. UI/UX trên UniTaxi – tương đương Grab / Xanh SM</strong></h2></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80bb-8e2d-f1d17268ea5c" class="">Trước khi đặt xe, màn hình “Xác nhận đặt xe” của UniTaxi hiển thị rõ thông tin chuyến (điểm đón/trả, loại xe, thời gian dự kiến), giá cước ước tính (kèm ghi chú về khả năng thay đổi do phí đường/bãi…) và một khối “Phương thức thanh toán” thể hiện phương thức hiện tại (Tiền mặt, MoMo, VNPAY QR, ViettelPay, Thẻ ngân hàng…) với icon chuẩn và nút “Thay đổi”. Khi người dùng mở màn hình “Phương thức thanh toán”, họ thấy danh sách các lựa chọn với logo nhà cung cấp, mô tả ngắn (“Thanh toán bằng tiền mặt cho tài xế”, “Ví MoMo – thanh toán trong ứng dụng”, “VNPAY QR – quét QR / chọn ngân hàng”…), trạng thái lựa chọn (tick) và có thể gắn nhãn “Khuyên dùng” cho một số phương thức nội địa. Người dùng luôn phải thấy rõ phương thức đang chọn trước khi bấm “Đặt xe”. Nếu người dùng đổi từ ví sang tiền mặt khi chuyến chưa thanh toán, backend UniTaxi chỉ cập nhật PaymentIntent tương ứng (nếu chưa tạo) và hiển thị thông báo rõ ràng “Chuyến này sẽ thanh toán bằng tiền mặt cho tài xế”.</p></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-808c-a26b-ff6f7a262d37" class="">Sau khi tài xế UniTaxi bấm kết thúc chuyến, ứng dụng hiển thị màn hình tóm tắt gồm quãng đường, thời gian, tổng tiền và chi tiết thành phần cước (cơ bản, phụ phí, khuyến mãi). Nếu phương thức là tiền mặt, UniTaxi nhắc khách thanh toán trực tiếp cho tài xế, và phía tài xế có nút xác nhận “Đã nhận đủ tiền”. Nếu phương thức là non-cash, backend UniTaxi tự động tạo PaymentIntent và khởi tạo luồng thanh toán qua cổng thanh toán; ứng dụng hiển thị trạng thái “Đang chuyển đến MoMo/VNPAY/ViettelPay…”, chip “Đang xác nhận thanh toán…” khi chưa có IPN, chuyển sang “Đã thanh toán thành công qua [tên nhà cung cấp]” khi IPN báo thành công, hoặc “Thanh toán thất bại” kèm hai lựa chọn “Thử lại phương thức này” và “Đổi sang thanh toán tiền mặt” khi IPN hoặc returnUrl báo lỗi.</p></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-807c-a5a5-e45348030bc9" class="">Màn hình lịch sử chuyến của UniTaxi hiển thị danh sách các chuyến với thời gian, tuyến đường tóm tắt, số tiền và tag phương thức (“Tiền mặt”, “MoMo”, “VNPAY QR”, “ViettelPay”) được đánh dấu bằng màu sắc cho trạng thái đã thanh toán. Khi mở chi tiết chuyến, người dùng phải thấy đầy đủ thông tin pháp nhân: “Đơn vị cung cấp dịch vụ: CÔNG TY CỔ PHẦN UNIPOWER”, mã số thuế, địa chỉ, số hotline. Phần thanh toán hiển thị phương thức, mã giao dịch nội bộ (payment_transaction_id), mã giao dịch từ cổng thanh toán (orderId/vnp_TxnRef/transId), trạng thái. Phần hóa đơn trong chi tiết chuyến cho phép người dùng yêu cầu hóa đơn nếu chưa tạo (nút “Yêu cầu hóa đơn”), theo dõi trạng thái “Đang phát hành hóa đơn…” khi hệ thống đang gửi MISA và ở trạng thái ISSUED hiển thị chip “Đã phát hành hóa đơn” cùng nút “Xem/Tải hóa đơn PDF”. Từ bất kỳ màn hình thanh toán liên quan nào trên UniTaxi, người dùng phải truy cập được “Điều khoản sử dụng” và “Chính sách bảo vệ dữ liệu cá nhân”, với bước tick đồng ý bắt buộc ở lần đầu.</p></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-808e-90eb-ea56438fdfb5"/></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-800b-8426-c20cd5c0e463" class=""><strong>3. Tích hợp MISA – Hóa đơn điện tử cho UniTaxi</strong></h2></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8017-9336-fdac922a6b87" class="">UNIPOWER là bên bán, phát hành hóa đơn VAT cho dịch vụ vận tải qua UniTaxi, MISA là nhà cung cấp dịch vụ hóa đơn điện tử. Backend UniTaxi không tự ký số trên hóa đơn mà chỉ truyền dữ liệu lên hệ thống MISA và nhận lại thông tin hóa đơn đã phát hành (số, ký hiệu, ngày phát hành, đường dẫn/file PDF).</p></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80d2-bb00-fed6827481b3" class="">Mô hình dữ liệu InvoiceRequest trên UniTaxi phải bao gồm: invoice_request_id (UUID), ride_id, payment_transaction_id (bắt buộc với thanh toán non-cash), buyer_type (INDIVIDUAL/COMPANY), thông tin bên mua (buyer_name, company_name, tax_code, address, phone, email), thông tin tài chính (subtotal, tax_rate, tax_amount, total_amount, currency), danh sách dòng hàng (mã, mô tả “Cước vận chuyển hành khách bằng taxi công nghệ”, đơn vị tính “Chuyến” hoặc “Lượt”, số lượng, đơn giá, thành tiền), phương thức thanh toán (payment_method), mã tham chiếu giao dịch (payment_reference), trạng thái (PENDING, SENDING_TO_MISA, ISSUED, FAILED, CANCELED), misa_template_id nếu MISA có nhiều mẫu hóa đơn, thông tin từ MISA trả về (misa_invoice_no, misa_series, misa_issue_date, misa_pdf_url hoặc blob PDF), trường lỗi nếu có (error_code, error_message) và thời gian tạo/cập nhật.</p></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-809c-9c53-d8eda21b9404" class="">Luồng nghiệp vụ: từ ứng dụng UniTaxi, người dùng mở chi tiết chuyến, bấm “Yêu cầu hóa đơn”, chọn loại cá nhân hoặc công ty và điền dữ liệu (cá nhân: họ tên, email; công ty: tên, mã số thuế, địa chỉ, email, số điện thoại). Ứng dụng gửi POST /api/invoices/request lên backend UniTaxi. Backend kiểm tra chuyến tồn tại, trạng thái thanh toán là đã trả (PAID_NONCASH hoặc PAID_CASH), chưa từng phát hành hóa đơn cho chuyến đó; sau đó tạo một bản ghi InvoiceRequest trạng thái PENDING, tính lại số tiền và VAT từ dữ liệu hệ thống. Một service nền (cron hoặc event-driven) trên backend UniTaxi định kỳ duyệt các InvoiceRequest có trạng thái PENDING, map sang schema MISA, gọi API createInvoice/issueInvoice và cập nhật trạng thái: nếu thành công thì chuyển ISSUED, lưu đầy đủ số/ký hiệu/ngày/pdf; nếu lỗi thì chuyển FAILED, lưu mã lỗi và thông điệp để kế toán của UNIPOWER xử lý lại.</p></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80a3-b4fa-c26068c141fa" class="">Người dùng UniTaxi xem/tải hóa đơn qua endpoint GET /api/invoices/by-ride/{ride_id}, nhận được trạng thái (NONE, PENDING, ISSUED, FAILED); nếu ISSUED thì có link tải PDF (proxy qua backend UniTaxi). Giao diện quản trị nội bộ của UniTaxi dành cho kế toán/pháp chế UNIPOWER phải có danh sách yêu cầu hóa đơn với bộ lọc theo ngày, trạng thái, loại buyer, số tiền; cho phép “Gửi lại MISA” với bản ghi FAILED và “Hủy yêu cầu” khi chưa phát hành; màn chi tiết hiển thị đầy đủ thông tin đầu vào, thông tin chuyến và thanh toán, log lời gọi MISA và lỗi nếu có. Hệ thống cần chức năng xuất CSV danh sách hóa đơn đã phát hành theo ngày/tháng phục vụ kê khai thuế. Quyền truy cập phải giới hạn cho nhóm kế toán/pháp chế; file PDF nếu lưu nội bộ cần mã hóa; mọi lần xem/tải hóa đơn đều được log với người dùng nội bộ, thời gian, IP.</p></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-8006-9d81-fe3c60102b7d"/></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-8022-a340-e18392735904" class=""><strong>4. Tích hợp MoMo / VNPAY / ViettelPay / Ngân hàng cho UniTaxi</strong></h2></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80f6-a520-d83c17544ade" class="">Trong dịch vụ thanh toán nội bộ của UniTaxi, cần định nghĩa một interface trừu tượng cho mỗi cổng thanh toán:</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2c0c5e6f-95bd-807f-95a5-e80894bf8aa1" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">interface PaymentProvider {
  createPayment(intent: PaymentIntent): Promise&lt;CreatePaymentResult&gt;;
  handleReturn(queryOrBody: any): PaymentResult;
  handleIpn(queryOrBody: any): PaymentResult;
}</code></pre></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8086-8cb2-cca9fb427f35" class="">CreatePaymentResult gồm payment_transaction_id, redirect_url, provider_metadata; PaymentResult gồm payment_transaction_id, status (SUCCESS/FAILURE), provider_txn_id nếu có, error_code nếu có và raw_payload. Các adapter cụ thể (MoMo, VNPAY, ViettelPay, cổng ngân hàng) triển khai interface này, đảm bảo logic nội bộ thống nhất cho UniTaxi.</p></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80e6-a1aa-d14ef3cceefc" class="">Với MoMo: ứng dụng UniTaxi gọi POST /payments/momo/create với ride_id, amount, description; backend UniTaxi xác nhận chuyến đã kết thúc và chưa thanh toán, tạo PaymentIntent (PENDING) và PaymentTransaction (CREATED). Adapter MoMo sinh orderId (ví dụ UTX-{ride_id}-{timestamp}) và requestId (UUID), xây payload theo tài liệu MoMo (partnerCode, accessKey, secretKey, amount, orderInfo, redirectUrl, ipnUrl, extraData…), tính signature HMAC SHA256, gửi yêu cầu HTTPS. MoMo trả payUrl hoặc deeplink; backend UniTaxi cập nhật PaymentTransaction sang PENDING_GATEWAY, lưu orderId/requestId, trả redirect_url cho ứng dụng; UniTaxi mở MoMo bằng deep link hoặc webview. Sau khi thanh toán, MoMo redirect tới redirectUrl với query; backend kiểm tra chữ ký, cập nhật tạm và render trang HTML nhẹ để UniTaxi nhận biết “Thành công/Thất bại”. IPN là nguồn xác nhận cuối: MoMo gửi POST tới ipnUrl, backend UniTaxi xác thực chữ ký/số tiền, tìm PaymentTransaction theo orderId; nếu resultCode = 0 thì đánh dấu SUCCESS cho PaymentTransaction, SUCCEEDED cho PaymentIntent và PAID_NONCASH cho Ride; nếu khác thì FAILURE, lưu error_code. Luồng phải idempotent, bỏ qua IPN trùng lặp sau khi đã SUCCESS.</p></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8084-8098-efa48d6d56e5" class="">Với VNPAY: luồng tương tự, dùng các tham số vnp_* (vnp_Version, vnp_TmnCode, vnp_Amount, vnp_Command, vnp_CreateDate, vnp_CurrCode, vnp_IpAddr, vnp_Locale, vnp_OrderInfo, vnp_OrderType, vnp_ReturnUrl, vnp_TxnRef, vnp_SecureHash). Ứng dụng UniTaxi gọi POST /payments/vnpay/create, backend tạo PaymentIntent và PaymentTransaction; adapter VNPAY tạo vnp_TxnRef (ví dụ UTX-{ride_id}-{timestamp}), chuẩn bị đầy đủ trường vnp_*, sắp xếp và nối query string, tính vnp_SecureHash, tạo paymentUrl. UniTaxi mở paymentUrl trong webview; người dùng chọn ngân hàng, quét QR hoặc nhập thông tin thẻ. Sau thanh toán, VNPAY redirect tới vnp_ReturnUrl và đồng thời gửi IPN tới backend UniTaxi. handleReturn chỉ phục vụ hiển thị cho ứng dụng, còn handleIpn xác thực chữ ký, kiểm tra amount, map vnp_ResponseCode (00 = thành công) và cập nhật PaymentTransaction, PaymentIntent, Ride giống MoMo.</p></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8016-8afd-f8166d15887a" class="">Với ViettelPay/Viettel Money: sử dụng pattern tương tự – backend UniTaxi tạo orderCode, ký request với cặp khóa do ViettelPay cấp (appId/merchantCode, secret), gửi tới API, nhận lại paymentUrl; UniTaxi mở paymentUrl (app-to-app hoặc web); ViettelPay gọi callback tới backend UniTaxi, backend xác thực chữ ký và cập nhật trạng thái giao dịch. Thanh toán ngân hàng/thẻ (Napas, Internet Banking) thường đi qua một sản phẩm của VNPAY hoặc PGW khác; với UniTaxi, luồng vẫn là createPayment → redirect → IPN với chữ ký tương tự VNPAY, phương thức nội bộ là CARD_BANK.</p></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80b7-86d5-d3ca2f6495ca" class="">Đối soát và settlement: mỗi ngày (T+0/T+1) cho từng nhà cung cấp, backend UniTaxi tải file đối soát (SFTP/portal/API), import vào bảng ReconciliationBatch, mapping provider_txn_id và provider_order_id vào PaymentTransaction; đánh dấu RECONCILED nếu khớp, MISMATCH nếu lệch số tiền/trạng thái; sinh báo cáo tổng hợp (tổng thu, tổng phí, tiền ròng UNIPOWER nhận cho nền tảng UniTaxi). Các sai lệch được đánh dấu: PaymentTransaction SUCCESS nhưng file không có → SUSPECT_MISSING_SETTLEMENT; file báo FAILED nhưng nội bộ SUCCESS → DISPUTE, cần xử lý với nhà cung cấp.</p></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-8052-9802-cda63be20390"/></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-80e0-b632-c8a0ae3be48a" class=""><strong>5. Bảo mật, nhật ký và kiểm soát</strong></h2></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8027-b0ea-d3bd6b09dcb7" class="">Thông số nhạy cảm của đối tác (partnerCode, accessKey, secretKey, merchantCode, certificate…) phải được lưu trong hệ thống quản lý bí mật (Vault, KMS…) của UNIPOWER, không đặt trong mã nguồn UniTaxi; chỉ nhóm rất nhỏ (CTO, DevOps được ủy quyền) có quyền xem/rotate. UniTaxi tuyệt đối không lưu số thẻ đầy đủ, CVV, PIN, OTP; chỉ lưu 4 số cuối thẻ nếu cần hiển thị và mã tham chiếu giao dịch từ cổng thanh toán. Hệ thống cần log lại tất cả lời gọi tới gateway, tất cả IPN nhận được và mọi thay đổi trạng thái PaymentTransaction/PaymentIntent với đầy đủ thông tin ai/thời điểm/nguồn; giám sát tỉ lệ thất bại theo nhà cung cấp, phát hiện pattern bất thường (chuỗi giao dịch nhỏ liên tiếp, retry nhiều, refund bất thường).</p></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-8067-b0d5-ce84c669dd8e"/></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-809b-9037-d15b13524de4" class=""><strong>6. Mapping vào mã nguồn Wooberly cho UniTaxi</strong></h2></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-806e-9f29-f40bdac9116e" class="">Trên front-end (ứng dụng UniTaxi phía khách và phía tài xế), lớp Payment mặc định của Wooberly phải được thay bằng luồng Payment của UniTaxi như mô tả: màn hình chọn phương thức thanh toán, màn hình hậu chuyến, lịch sử chuyến và chi tiết chuyến đều bám theo pattern nói trên, còn các gọi API thanh toán phải đi qua Payment Service của UniTaxi, không gọi trực tiếp gateway. Phía backend, cần tách rõ logic tính cước và lưu chuyến (giữ lại từ Wooberly) khỏi logic thanh toán (chuyển hoàn toàn sang Payment Service của UniTaxi); bổ sung endpoint cho IPN (MoMo, VNPAY, ViettelPay, ngân hàng…) và các bảng sổ cái thanh toán nội bộ (PaymentIntent, PaymentTransaction, ReconciliationBatch). Module hóa đơn MISA hoạt động độc lập với module thanh toán mặc định của Wooberly: khi ride.payment_status đã là PAID_NONCASH hoặc PAID_CASH thì backend UniTaxi cho phép tạo InvoiceRequest, và luồng MISA chỉ sử dụng dữ liệu của ride và thanh toán làm đầu vào, không phụ thuộc bất kỳ logic thanh toán cũ nào.</p></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80e4-af79-d130886b066f" class="">Tài liệu này là chuẩn chung để đội phát triển (Wooberly/RadicalStart khi triển khai UniTaxi cho UNIPOWER), đội pháp chế/tuân thủ và các đối tác tích hợp (MISA, MoMo, VNPAY, ViettelPay, cổng ngân hàng) cùng dựa vào khi thiết kế – triển khai, nhằm đảm bảo trải nghiệm người dùng UniTaxi tương đương các nền tảng lớn, tuân thủ pháp luật Việt Nam và đáp ứng yêu cầu an toàn thông tin, bảo vệ dữ liệu, kiểm toán – đối soát ở mức doanh nghiệp cho UNIPOWER.</p></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8051-8a1a-e5753c1473e6" class="">
</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
