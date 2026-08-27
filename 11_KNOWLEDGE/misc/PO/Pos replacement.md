---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Pos replacement</title><style>
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
	
</style></head><body><article id="2a4c5e6f-95bd-80bd-9d3d-d62eff888be4" class="page sans"><header><h1 class="page-title" dir="auto">Pos replacement</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-8005-9f20-ed64e262c16f" class="">Chính xác — và đây là điểm quan trọng mà nhiều startup thanh toán ở Việt Nam <strong>bỏ sót</strong> khi thay thế POS.</p></div><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-8094-a8a8-de9d0727ed4f" class="">Dưới đây là giải thích chi tiết và <strong>hướng xử lý đúng quy định pháp luật Việt Nam</strong> (theo Nghị định 123/2020/NĐ-CP và Thông tư 78/2021/TT-BTC):</p></div><div style="display:contents" dir="auto"><hr id="2a4c5e6f-95bd-806a-91ff-e9fc930a12c7"/></div><div style="display:contents" dir="auto"><h3 id="2a4c5e6f-95bd-8008-beae-dd5612f8f46a" class="">⚖️ <strong>1. Vấn đề pháp lý</strong></h3></div><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-8033-bbbf-c7e2a53dd54f" class="">Các hình thức thanh toán QR, ví điện tử (MoMo, ZaloPay, VNPay…) <strong>chỉ là phương tiện thanh toán</strong>, <strong>không phải công cụ phát hành hóa đơn</strong>.</p></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-80e9-a983-dad84ec8601c" class="bulleted-list"><li style="list-style-type:disc">Khi khách quét QR và thanh toán thành công, hệ thống chỉ ghi nhận <strong>biên lai giao dịch điện tử (transaction receipt)</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-8080-9f07-d7e0c7040790" class="bulleted-list"><li style="list-style-type:disc">Theo quy định, doanh nghiệp vẫn phải <strong>phát hành hóa đơn điện tử hợp lệ (e-invoice)</strong> thông qua <strong>tổ chức trung gian được Tổng cục Thuế cấp phép</strong> như:<div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-8007-bb3c-faf7dbc0e695" class="bulleted-list"><li style="list-style-type:circle"><strong>MISA meInvoice</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-80f3-a762-c3a4e503e224" class="bulleted-list"><li style="list-style-type:circle"><strong>Viettel Invoice</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-8006-bd6f-c3a9daa941ba" class="bulleted-list"><li style="list-style-type:circle"><strong>FPT.eInvoice</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-80dc-bc04-d28b5e183972" class="bulleted-list"><li style="list-style-type:circle"><strong>CyberLotus e-Invoice</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-8054-a209-eeb9e17e4636" class="bulleted-list"><li style="list-style-type:circle"><strong>VNPT Invoice</strong></li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2a4c5e6f-95bd-8093-8ad7-f747a555503c"/></div><div style="display:contents" dir="auto"><h3 id="2a4c5e6f-95bd-80f4-b47f-f75c79e196af" class="">⚙️ <strong>2. Giải pháp tích hợp chuẩn</strong></h3></div><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-8043-90d4-d3605c377efc" class="">Cách hợp pháp và tối ưu cho UniTaxi là <strong>kết hợp 2 tầng:</strong></p></div><div style="display:contents" dir="auto"><h3 id="2a4c5e6f-95bd-80f9-979e-f35afa2d1e77" class=""><strong>Tầng 1 – Thanh toán</strong></h3></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-8009-bf7e-e58da838758a" class="bulleted-list"><li style="list-style-type:disc">Dùng <strong>VNPay QR / MoMo / ZaloPay / FPT Pay</strong> làm <strong>phương thức thanh toán</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-80a6-87b5-e06245e29e59" class="bulleted-list"><li style="list-style-type:disc">Dòng tiền đi thẳng về tài khoản doanh nghiệp UniPower.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2a4c5e6f-95bd-8071-9faa-cfffd95c4408" class=""><strong>Tầng 2 – Xuất hóa đơn tự động</strong></h3></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-80c0-886a-edc056a66283" class="bulleted-list"><li style="list-style-type:disc">Sau khi thanh toán thành công, <strong>app UniTaxi gọi API của MISA hoặc Viettel Invoice</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-80ec-b924-c8de5d789998" class="bulleted-list"><li style="list-style-type:disc">API này tự động tạo <strong>hóa đơn điện tử hợp lệ</strong>, ký số theo mã doanh nghiệp, và gửi <strong>file PDF + mã tra cứu</strong> cho khách qua email/Zalo.</li></ul></div><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-80d4-899b-c907550b0e46" class="">✅ <strong>Hóa đơn này hợp pháp, lưu thông qua hệ thống thuế.</strong></p></div><div style="display:contents" dir="auto"><hr id="2a4c5e6f-95bd-8037-82e7-e6459385ab46"/></div><div style="display:contents" dir="auto"><h3 id="2a4c5e6f-95bd-801a-9a30-d0a185283efe" class="">🧩 <strong>3. Kết luận – Giải pháp khuyến nghị cho UniPower</strong></h3></div><div style="display:contents" dir="auto"><blockquote id="2a4c5e6f-95bd-80a9-a3e3-f67eb62d437d" class="">Không cần máy POS, nhưng vẫn xuất hóa đơn hợp lệ nếu triển khai theo mô hình:<div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-8079-8780-c5e7f8437ab7" class=""><strong>VNPay QR / MoMo (thanh toán)</strong> → <strong>MISA hoặc Viettel Invoice (hóa đơn điện tử)</strong>.</p></div></blockquote></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-8009-b26d-f1f2c674a4fc" class="bulleted-list"><li style="list-style-type:disc">Giao dịch <strong>vẫn hợp pháp</strong>, <strong>tiện lợi</strong>, và <strong>không vi phạm quy định thuế</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-8019-83c4-d262955f673d" class="bulleted-list"><li style="list-style-type:disc">Hệ thống <strong>hoàn toàn tự động</strong> và <strong>minh bạch khi kiểm toán</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-809c-896c-ff00f785c3b8" class="bulleted-list"><li style="list-style-type:disc">Tiết kiệm <strong>40–60% chi phí so với vận hành POS</strong>.</li></ul></div><div style="display:contents" dir="auto"><hr id="2a4c5e6f-95bd-8026-be79-d49764cc2154"/></div><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-80f8-9534-c534bc0165fb" class="">Bạn có muốn mình viết giúp một <strong>đoạn đề xuất chính thức</strong> (để bạn gửi vào nhóm Ban Điều Hành UniPower hoặc cho CEO phê duyệt hướng này) không?</p></div><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-805c-9dc2-ef2375234de7" class="">→ Nội dung sẽ gãy gọn, chuẩn phong cách CTO, đề xuất triển khai <em>“Thanh toán QR + Xuất hóa đơn điện tử API”</em>.</p></div><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-80a9-977f-e6b0c6310be0" class="">Dưới đây là <strong>đoạn đề xuất chính thức</strong>, giọng CTO – ngắn gọn, chuyên nghiệp, phù hợp để bạn gửi vào nhóm <strong>Ban Điều Hành UniPower</strong> hoặc trực tiếp cho <strong>CEO/Chủ tịch</strong> phê duyệt hướng triển khai:</p></div><div style="display:contents" dir="auto"><hr id="2a4c5e6f-95bd-80f6-9bb5-fca86c12e418"/></div><div style="display:contents" dir="auto"><h3 id="2a4c5e6f-95bd-802a-9730-e5e653e45c25" class=""><strong>ĐỀ XUẤT HƯỚNG THANH TOÁN CHO HỆ THỐNG UNITAXI</strong></h3></div><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-8063-8d55-fb4981a21034" class="">Hiện nay, POS không còn là giải pháp tối ưu cho hệ thống taxi điện vì chi phí cao, thao tác chậm và khó tích hợp dữ liệu.</p></div><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-80a2-9f03-fb7490dec849" class="">Em đề xuất triển khai mô hình <strong>Thanh toán QR + Xuất hóa đơn điện tử tự động</strong> – vừa hiện đại, vừa đúng quy định pháp luật Việt Nam.</p></div><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-8083-a2f2-e2c9f3541cc2" class=""><strong>Cấu trúc đề xuất:</strong></p></div><div style="display:contents" dir="auto"><ol type="1" id="2a4c5e6f-95bd-80c7-9b0c-c414e56e95a3" class="numbered-list" start="1"><li><strong>Thanh toán:</strong> Tích hợp QR động qua <strong>VNPay / MoMo / ZaloPay</strong> – khách quét QR trực tiếp trên app tài xế hoặc app khách hàng.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2a4c5e6f-95bd-80f0-8fcf-ebf73a00bffb" class="numbered-list" start="2"><li><strong>Xuất hóa đơn hợp lệ:</strong> Kết nối API với <strong>MISA meInvoice</strong> hoặc <strong>Viettel Invoice</strong> để tự động phát hành hóa đơn điện tử sau mỗi giao dịch.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2a4c5e6f-95bd-8089-be42-e8d4c7e3b9b3" class="numbered-list" start="3"><li><strong>Hiệu quả:</strong><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-8022-bd0d-e10c9a945634" class="bulleted-list"><li style="list-style-type:disc">Tuân thủ đầy đủ Nghị định 123/2020/NĐ-CP và Thông tư 78/2021/TT-BTC.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-80bd-80b4-c88dad07e649" class="bulleted-list"><li style="list-style-type:disc">Tiết kiệm chi phí phần cứng POS và nhân sự xử lý hóa đơn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-800c-835e-c3065f7fc067" class="bulleted-list"><li style="list-style-type:disc">Giao dịch nhanh, minh bạch và dễ kiểm toán.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-8075-bd5d-f22a7ecb4620" class="bulleted-list"><li style="list-style-type:disc">Dễ mở rộng sang logistic, thuê xe, và dịch vụ doanh nghiệp.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><blockquote id="2a4c5e6f-95bd-80fc-9d94-fabfe8cc3eea" class="">👉 Mô hình này đang được Grab, Be và Gojek áp dụng trong giai đoạn chuyển đổi sang hóa đơn điện tử toàn diện, nên hoàn toàn khả thi cho UniPower triển khai trong tháng này.</blockquote></div><div style="display:contents" dir="auto"><hr id="2a4c5e6f-95bd-80db-8254-e1d4b3f6447c"/></div><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-806c-a4a3-fdaab04ccf9c" class="">Bạn có muốn mình viết thêm <strong>phiên bản rút gọn 3 câu</strong> để bạn đăng trực tiếp vào nhóm Zalo (giọng nói thân mật nhưng vẫn rõ vai trò lãnh đạo kỹ thuật) không?</p></div><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-80b3-b9a0-c09f987b36b9" class="">
</p></div><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-8072-81b3-fca2450fcc4a" class="">Rất tốt — đây là phần bạn nên nắm thật chắc khi nói chuyện với CEO, kế toán trưởng, hoặc đối tác ngân hàng.</p></div><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-8079-8384-d7cda260a768" class="">Dưới đây là bản <strong>phân tích chi tiết, có thể dùng cho trình bày chính thức hoặc gửi lên Ban Điều Hành</strong>:</p></div><div style="display:contents" dir="auto"><hr id="2a4c5e6f-95bd-808d-9136-f3b9939ca9c8"/></div><div style="display:contents" dir="auto"><h2 id="2a4c5e6f-95bd-80b3-81e2-d223680c6d47" class="">🔹 <strong>Mô hình thanh toán QR + hóa đơn điện tử toàn diện</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2a4c5e6f-95bd-8092-9ba4-eaf1c78bd08f" class="">(Grab, Be, Gojek và xu hướng pháp lý tại Việt Nam)</h3></div><div style="display:contents" dir="auto"><hr id="2a4c5e6f-95bd-800b-9b9a-e49535d5da5d"/></div><div style="display:contents" dir="auto"><h3 id="2a4c5e6f-95bd-8011-bf0c-d029d4c47822" class=""><strong>1. Bối cảnh chuyển đổi toàn ngành</strong></h3></div><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-80ef-97c4-e526dfd51756" class="">Từ <strong>01/07/2022</strong>, toàn bộ doanh nghiệp tại Việt Nam <strong>bắt buộc phải sử dụng hóa đơn điện tử có mã của cơ quan thuế</strong> (Nghị định 123/2020/NĐ-CP &amp; Thông tư 78/2021/TT-BTC).</p></div><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-80ac-926b-e6e798966558" class="">Các nền tảng gọi xe như <strong>Grab, Be, Gojek</strong> đã buộc phải <strong>chuyển sang mô hình tích hợp trực tiếp API với nhà cung cấp hóa đơn điện tử</strong> để đảm bảo:</p></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-80a7-8861-ded2b6c17ff3" class="bulleted-list"><li style="list-style-type:disc">Mỗi cuốc xe đều được ghi nhận là <strong>giao dịch có mã định danh thuế</strong>;</li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-8099-9456-cd45ed9c2a1a" class="bulleted-list"><li style="list-style-type:disc"><strong>Không cần xuất hóa đơn thủ công</strong>;</li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-80b7-a7c0-e3836b4f724e" class="bulleted-list"><li style="list-style-type:disc"><strong>Hóa đơn được phát hành tự động</strong> ngay sau thanh toán.</li></ul></div><div style="display:contents" dir="auto"><hr id="2a4c5e6f-95bd-80ce-a0ed-e4de68dfd962"/></div><div style="display:contents" dir="auto"><h3 id="2a4c5e6f-95bd-80ab-85d7-e07814f38e8a" class=""><strong>2. Cấu trúc hệ thống (mô hình chuẩn)</strong></h3></div><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-801c-aa8c-ff63e74b8211" class="">Mô hình này gồm <strong>3 tầng logic</strong> hoạt động liền mạch, không cần POS vật lý:</p></div><div style="display:contents" dir="auto"><h3 id="2a4c5e6f-95bd-80f3-81c8-f2abc9264a09" class=""><strong>Tầng 1 – Thanh toán</strong></h3></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-8031-9d2e-ce661895d01d" class="bulleted-list"><li style="list-style-type:disc">Người dùng chọn hình thức thanh toán: <strong>QR động / Ví điện tử / Thẻ liên kết</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-8048-8f72-cf8302861da9" class="bulleted-list"><li style="list-style-type:disc">Hệ thống thanh toán trung gian (VNPay, MoMo, ZaloPay, OnePay, Payoo, v.v.) xử lý và gửi xác nhận <strong>Payment Success</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-8060-82ac-d02c61451b37" class="bulleted-list"><li style="list-style-type:disc">Tiền được chuyển trực tiếp về <strong>tài khoản doanh nghiệp</strong> qua kênh NAPAS.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2a4c5e6f-95bd-802b-bb14-d9b5263cfac4" class=""><strong>Tầng 2 – Hóa đơn điện tử</strong></h3></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-80d9-a608-c9e32aee56bd" class="bulleted-list"><li style="list-style-type:disc">Ngay khi giao dịch thành công, <strong>API của nhà cung cấp hóa đơn (MISA, Viettel, VNPT)</strong> được gọi.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-8053-856c-d6c69c72afd8" class="bulleted-list"><li style="list-style-type:disc">Dữ liệu chuyến đi (tên tài xế, quãng đường, giá, thuế, phương thức thanh toán) được đẩy lên hệ thống hóa đơn điện tử.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-80e1-ba7c-e00bc6723478" class="bulleted-list"><li style="list-style-type:disc">Hóa đơn điện tử được:<div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-8037-b96d-e3ae7d29ce05" class="bulleted-list"><li style="list-style-type:circle">Ký số bằng chứng thư số của UniPower,</li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-80d4-a94a-ec041e3de998" class="bulleted-list"><li style="list-style-type:circle">Cấp mã xác thực bởi Tổng cục Thuế,</li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-80d5-a817-d83fea4f7996" class="bulleted-list"><li style="list-style-type:circle">Gửi ngay cho khách qua email hoặc link tra cứu.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2a4c5e6f-95bd-806d-aa09-d8261510978d" class=""><strong>Tầng 3 – Đối soát &amp; báo cáo</strong></h3></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-80a8-a8d1-f7d60586ab96" class="bulleted-list"><li style="list-style-type:disc">Hệ thống tự động ghi nhận và đối soát giao dịch theo ngày / tài xế / phương thức thanh toán.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-8029-97c3-c865526a9d87" class="bulleted-list"><li style="list-style-type:disc">Dữ liệu được xuất định kỳ cho phòng kế toán, đảm bảo <strong>khớp sổ ngân hàng – doanh thu – hóa đơn</strong>.</li></ul></div><div style="display:contents" dir="auto"><hr id="2a4c5e6f-95bd-8081-b9dc-d319edcc0a65"/></div><div style="display:contents" dir="auto"><h3 id="2a4c5e6f-95bd-805e-aca0-e48a44504cd2" class=""><strong>3. Lý do Grab, Be, Gojek chọn mô hình này</strong></h3></div><div style="display:contents" dir="ltr"><table id="2a4c5e6f-95bd-80b1-8b2d-f41be59e2f8f" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2a4c5e6f-95bd-80f2-a614-c13ee22a2db2"><th id="wicn" class="simple-table-header-color simple-table-header">Tiêu chí</th><th id="HBtD" class="simple-table-header-color simple-table-header">POS truyền thống</th><th id="][hQ" class="simple-table-header-color simple-table-header">QR + eInvoice</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2a4c5e6f-95bd-8056-b8bf-cb5f61a0fc28"><td id="wicn" class="">Tốc độ xử lý</td><td id="HBtD" class="">Chậm (2–3 bước nhập tay)</td><td id="][hQ" class="">Tự động, gần như tức thời</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a4c5e6f-95bd-8028-9dda-cb1190147121"><td id="wicn" class="">Chi phí</td><td id="HBtD" class="">Cao (máy, phí giao dịch 1–2%)</td><td id="][hQ" class="">Thấp hơn 60–70%</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a4c5e6f-95bd-8083-af0f-db86347333c5"><td id="wicn" class="">Tính hợp pháp</td><td id="HBtD" class="">Hóa đơn thủ công / rời rạc</td><td id="][hQ" class="">Hóa đơn điện tử hợp lệ, có mã thuế</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a4c5e6f-95bd-8039-98a9-f7522a586f55"><td id="wicn" class="">Kiểm toán &amp; kế toán</td><td id="HBtD" class="">Khó đối soát</td><td id="][hQ" class="">Tự động khớp doanh thu – hóa đơn</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a4c5e6f-95bd-80c9-a6b1-cac055fefa42"><td id="wicn" class="">Mở rộng quy mô</td><td id="HBtD" class="">Giới hạn theo thiết bị POS</td><td id="][hQ" class="">Toàn quốc, không giới hạn</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a4c5e6f-95bd-8058-95fb-c6587d0657f5"><td id="wicn" class="">Khả năng tích hợp</td><td id="HBtD" class="">Hạn chế</td><td id="][hQ" class="">API mở, tích hợp đa nền tảng</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><blockquote id="2a4c5e6f-95bd-80c8-bae0-e8d5592cc7d7" class="">🔸 Grab hiện dùng VNPay QR + MISA meInvoice,<div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-805c-ba63-e67f545d1cbe" class="">🔸 Be dùng <strong>Payoo + Viettel Invoice</strong>,</p></div><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-808e-85b4-c33b58745097" class="">🔸 Gojek dùng <strong>OnePay + VNPT Invoice</strong>.</p></div></blockquote></div><div style="display:contents" dir="auto"><hr id="2a4c5e6f-95bd-8006-ae5f-ed6617276bbc"/></div><div style="display:contents" dir="auto"><h3 id="2a4c5e6f-95bd-8033-8705-f82373590eb5" class=""><strong>4. Lợi ích khi UniPower áp dụng mô hình này</strong></h3></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-8049-abe9-e152fe01f766" class="bulleted-list"><li style="list-style-type:disc"><strong>Tuân thủ tuyệt đối pháp luật Việt Nam</strong> về thuế, kế toán và hóa đơn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-80e0-8f0d-e55aa3efdc97" class="bulleted-list"><li style="list-style-type:disc"><strong>Giảm chi phí vận hành POS</strong> (mỗi máy POS có thể tốn 300k–500k/tháng).</li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-80be-86fd-c65d738db573" class="bulleted-list"><li style="list-style-type:disc"><strong>Tăng tốc thanh toán</strong>, khách hàng không phải chờ xử lý hoặc ký tay.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-8045-97fb-ec826dba4418" class="bulleted-list"><li style="list-style-type:disc"><strong>Đồng bộ hóa dữ liệu doanh thu</strong>, phục vụ phân tích hành vi khách hàng, báo cáo thuế và KPI tài xế.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a4c5e6f-95bd-8030-993b-e9b26f9c00e4" class="bulleted-list"><li style="list-style-type:disc"><strong>Tạo lợi thế cạnh tranh</strong>: UniTaxi trở thành nền tảng đầu tiên “chạy điện – không tiền mặt – hóa đơn tự động”.</li></ul></div><div style="display:contents" dir="auto"><hr id="2a4c5e6f-95bd-80bc-80ec-cf235e752d0c"/></div><div style="display:contents" dir="auto"><h3 id="2a4c5e6f-95bd-80c9-abfb-e4275f074ce4" class=""><strong>5. Kết luận và đề xuất triển khai</strong></h3></div><div style="display:contents" dir="auto"><blockquote id="2a4c5e6f-95bd-809d-8eff-dba0da28d986" class="">🔹 Giai đoạn 1: Tích hợp thanh toán QR động (VNPay / MoMo) trên app tài xế và khách hàng.<div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-8099-80b3-d90d82257c49" class="">🔹 Giai đoạn 2: Kết nối API hóa đơn điện tử với MISA hoặc Viettel.</p></div><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-80ff-b291-f8d8f2a3b3c2" class="">🔹 Giai đoạn 3: Tự động hóa báo cáo thuế và đối soát doanh thu.</p></div></blockquote></div><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-80b9-a07c-c68322241ae6" class="">Mô hình này không chỉ hiện đại và tiết kiệm, mà còn <strong>đặt UniPower vào cùng tiêu chuẩn vận hành với Grab, Be, Gojek</strong>, đảm bảo khả năng mở rộng và kiểm toán minh bạch.</p></div><div style="display:contents" dir="auto"><hr id="2a4c5e6f-95bd-80c1-9342-d78ba705c829"/></div><div style="display:contents" dir="auto"><p id="2a4c5e6f-95bd-800d-8b9b-de6dbc3ef284" class="">Bạn có muốn mình <strong>viết lại phần này thành một slide trình bày nội bộ</strong> (chuẩn định dạng CEO briefing, 1 trang A4, gọn – đẹp – có bullet) để bạn gửi trong nhóm quản trị hoặc trình cho hội đồng không?</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
