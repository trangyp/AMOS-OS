---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Hop dong</title><style>
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
	
</style></head><body><article id="2cfc5e6f-95bd-80e9-be8f-ce40be0b6995" class="page sans"><header><h1 class="page-title" dir="auto">Hop dong</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80c6-ace6-d76dc6b9cdf8" class="">Dưới đây là <strong>phân tích pháp lý toàn diện – exhaustively, 0 gaps</strong> dựa <strong>trực tiếp trên 03 tài liệu</strong> bạn đã cung cấp (Proforma Invoice + Contract HH2025121902), theo <strong>chuẩn audit pháp lý quốc tế (Big4 / McKinsey Legal Due Diligence)</strong>, tập trung vào <strong>rủi ro thực tế nếu UNIPOWER ký và thực thi hợp đồng này</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-8066-bcac-d8377967ee8b"/></div><div style="display:contents" dir="auto"><h1 id="2cfc5e6f-95bd-8093-b37b-c5312161deef" class=""><strong>I. TỔNG QUAN NHANH (EXECUTIVE SUMMARY)</strong></h1></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80a1-8b4e-f96a2298ae5d" class=""><strong>Kết luận ngắn gọn:</strong></p></div><div style="display:contents" dir="auto"><blockquote id="2cfc5e6f-95bd-806a-b6b1-e47944862128" class="">❌ <strong>Hợp đồng hiện tại có rủi ro pháp lý rất cao cho UNIPOWER</strong></blockquote></div><div style="display:contents" dir="auto"><ol type="1" id="2cfc5e6f-95bd-805d-bf13-d5c1928364f5" class="numbered-list" start="1"><li>Điều khoản xác nhận <strong>xe là “USED VEHICLES”</strong> (xe đã qua sử dụng)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2cfc5e6f-95bd-8083-a7b0-ce35bc803fdc" class="numbered-list" start="2"><li><strong>Miễn trừ hoàn toàn trách nhiệm chất lượng &amp; hậu mãi của Seller</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2cfc5e6f-95bd-80d4-aeb1-f08d8255ad67" class="numbered-list" start="3"><li>Thanh toán <strong>100% trước khi giao hàng (FOB)</strong> – mất toàn bộ đòn bẩy</li></ol></div><div style="display:contents" d
ir="auto"><ol type="1" id="2cfc5e6f-95bd-8048-9d98-dd575fdaee24" class="numbered-list" start="4"><li>Luật áp dụng + tài phán <strong>hoàn toàn bất lợi</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2cfc5e6f-95bd-8061-9ad6-da93300a400a" class="numbered-list" start="5"><li>Không có bất kỳ điều khoản nào bảo vệ việc <strong>đăng kiểm – homologation tại Việt Nam</strong></li></ol></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80ee-8738-e8f9a31c3ed7" class="">➡️ <strong>Ở trạng thái hiện tại: KHÔNG NÊN KÝ.</strong></p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8065-a2cd-d775f0aebcaf" class="">➡️ Cần <strong>bổ sung / sửa tối thiểu 14 nhóm điều khoản bắt buộc</strong> trước khi ký.</p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-80a7-849c-c2fb0fa02ba0"/></div><div style="display:contents" dir="auto"><h1 id="2cfc5e6f-95bd-80dd-9404-cc2f5a2ee614" class=""><strong>II. PHÂN TÍCH CHI TIẾT THEO TỪNG NHÓM RỦI RO PHÁP LÝ</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-80d4-b188-c0c8a91f7aeb" class=""><strong>1. RỦI RO NGHIÊM TRỌNG NHẤT: XE BỊ XÁC ĐỊNH LÀ “USED VEHICLES”</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2cfc5e6f-95bd-8083-b0f8-c8f3d38c43d8" class=""><strong>Căn cứ hợp đồng</strong></h3></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8068-8174-f10ad836a7f9" class="">Tại <strong>GENERAL TERMS – Article 1.1</strong> ghi rõ:</p></div><div style="display:contents" dir="auto"><blockquote id="2cfc5e6f-95bd-802d-8313-cd333ed09cbf" class="">“the Buyer knows that all the goods delivered by the Seller are<div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8036-9419-cb45af4fbef6" class=""><em><strong>used vehicles</strong></em></p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8098-96e9-cc9f60adba95" class=""><em>… Buyer agrees to accept all defects … and shall exempt t
he Seller from all quality assurance obligations.”</em></p></div></blockquote></div><div style="display:contents" dir="auto"><h3 id="2cfc5e6f-95bd-8060-bd69-f1535ce32dfa" class=""><strong>Hệ quả pháp lý tại Việt Nam</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="2cfc5e6f-95bd-8090-9c9b-d3e5e0507e7b" class="numbered-list" start="1"><li><strong>Xe đã qua sử dụng KHÔNG ĐỦ ĐIỀU KIỆN</strong>:<div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80cf-a04a-d9a9ae9a1691" class="bulleted-list"><li style="list-style-type:disc">Xin <strong>chứng nhận kiểu loại</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8064-9978-db907f54339e" class="bulleted-list"><li style="list-style-type:disc">Đăng kiểm xe mới</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-805e-98ba-faeb4c97a69e" class="bulleted-list"><li style="list-style-type:disc">Nhập khẩu xe điện để thương mại / thử nghiệm</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2cfc5e6f-95bd-8030-9f11-d6f9df0abb75" class="numbered-list" start="2"><li>Trực tiếp vi phạm:<div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-802f-a383-e772fd270bec" class="bulleted-list"><li style="list-style-type:disc">Nghị định 116/2017/NĐ-CP</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8081-a7a0-e040f6b84be9" class="bulleted-list"><li style="list-style-type:disc">Thông tư 30/2011/TT-BGTVT (nhập khẩu ô tô)</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8019-8019-eae341ed2889" class="bulleted-list"><li style="list-style-type:disc">Quy định Đăng kiểm về xe mẫu</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8075-8f9f-ded4d2835776" class="">📌 <strong>Đây là điều khoản “kill deal”</strong></p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80d6-84a2-c3304be29cb0" class="">→ Nếu 
ý, <strong>UNIPOWER tự xác nhận xe là xe cũ</strong>, dù thực tế có thể là xe mới.</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8085-a6f7-e6ebad07dfbb" class=""><strong>MỨC ĐỘ RỦI RO: CỰC KỲ NGHIÊM TRỌNG (RED FLAG – STOP DEAL)</strong></p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-805f-8499-c6448f458335"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-80df-a872-de3df7ed5e9b" class=""><strong>2. MIỄN TRỪ HOÀN TOÀN TRÁCH NHIỆM CHẤT LƯỢNG &amp; HẬU MÃI</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2cfc5e6f-95bd-80f2-802b-d1fccc314c6b" class=""><strong>Điều khoản</strong></h3></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-803f-8110-d5940d4cd6ee" class="bulleted-list"><li style="list-style-type:disc">Seller:<div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8020-9fc8-e7cc3075dded" class="bulleted-list"><li style="list-style-type:circle">Không chịu <strong>bất kỳ trách nhiệm bảo hành nào</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8084-a1a2-c73dda8bdfaf" class="bulleted-list"><li style="list-style-type:circle">Không chịu <strong>after-sales service</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80a1-8c3e-fe15c6eeecbc" class="bulleted-list"><li style="list-style-type:circle">Buyer tự chịu toàn bộ rủi ro kỹ thuật</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2cfc5e6f-95bd-8094-8dff-fb86f3a2733e" class=""><strong>Hệ quả</strong></h3></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8006-9a62-f183ad70602c" class="bulleted-list"><li style="list-style-type:disc">Nếu:<div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8012-b5c7-c4427eff6543" class="bulleted-list"><li style="list-style-type:circle">Pin lỗi</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80e1-86ea-f42bb7b2866b" c
lass="bulleted-list"><li style="list-style-type:circle">ECU lỗi</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80cc-9ffa-f6efdf8b49f2" class="bulleted-list"><li style="list-style-type:circle">Không đạt test an toàn điện / EMC / braking<div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80d7-b089-cbc572093afc" class="">→ <strong>UNIPOWER không có quyền khiếu nại hợp đồng</strong></p></div></li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80af-85e8-c5eb2e119696" class="">📌 Trong EV, <strong>pin chiếm 30–40% giá trị xe</strong> → rủi ro tài chính cực lớn.</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80fc-ad60-d070649c0fd2" class=""><strong>MỨC ĐỘ RỦI RO: RẤT CAO</strong></p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-807d-96a4-e214d4c15130"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-80f2-8451-e48edb384b4e" class=""><strong>3. THANH TOÁN 100% TRƯỚC – FOB (MẤT TOÀN BỘ ĐÒN BẨY)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2cfc5e6f-95bd-8006-8ae9-d7674e1b51d9" class=""><strong>Điều khoản thanh toán</strong></h3></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8093-8ce9-eebd52ef17e8" class="bulleted-list"><li style="list-style-type:disc">Article 2:<div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80ec-b9e8-fd743810fbd9" class="bulleted-list"><li style="list-style-type:circle">T/T <strong>100% trong 3 ngày sau ký</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-802b-9970-e741b977262f" class="bulleted-list"><li style="list-style-type:circle">Trước khi giao hàng</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8033-a799-f74c7595027a" class="bulleted-list"><li style="list-style-type:disc">Điều kiện giao: <strong>FOB Nansha</strong></li></ul></div><div style="display:contents" d
ir="auto"><h3 id="2cfc5e6f-95bd-80a3-bca5-e1fddfc7c7ee" class=""><strong>Rủi ro thực tế</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="2cfc5e6f-95bd-8094-9744-d64cb3fbeb70" class="numbered-list" start="1"><li>Sau khi chuyển tiền:<div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80a5-b167-e652bb564b2e" class="bulleted-list"><li style="list-style-type:disc">Seller <strong>không còn nghĩa vụ tài chính</strong></li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2cfc5e6f-95bd-80c3-afcc-ecb2ce7aaf2e" class="numbered-list" start="2"><li>Mọi rủi ro:<div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80cb-b7c4-f54b3ad09b9b" class="bulleted-list"><li style="list-style-type:disc">Hư hỏng</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80be-aeac-fa1c80a79f85" class="bulleted-list"><li style="list-style-type:disc">Chậm tàu</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80d8-8215-e100706c7900" class="bulleted-list"><li style="list-style-type:disc">Hồ sơ sai<div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-803e-86c6-d047f9f8107a" class="">→ <strong>Buyer gánh 100%</strong></p></div></li></ul></div></li></ol></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8031-ac47-f3d5f98f9b8f" class="">📌 Chuẩn quốc tế cho xe mẫu:</p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8056-8a65-ff272acb8fad" class="bulleted-list"><li style="list-style-type:disc">30% deposit</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80b9-bbb2-f963453dad70" class="bulleted-list"><li style="list-style-type:disc">70% sau inspection / B/L draft</li></ul></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8061-b251-feb9b00c4498" class=""><strong>MỨC ĐỘ RỦI RO: CAO</strong></p></div><div style="display:contents" dir="auto"><hr i
d="2cfc5e6f-95bd-80ce-ba42-e2889d5ee165"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-8068-be2d-d955e601b608" class=""><strong>4. LUẬT ÁP DỤNG &amp; TÀI PHÁN – BẤT LỢI TOÀN DIỆN</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2cfc5e6f-95bd-80b5-9be3-f3338af7b849" class=""><strong>Điều khoản</strong></h3></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8047-8bf8-d0c7292a6ed6" class="bulleted-list"><li style="list-style-type:disc">Luật áp dụng: <strong>Luật Trung Quốc</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80bd-ba43-f77cb9d5d8cd" class="bulleted-list"><li style="list-style-type:disc">Tòa án:<div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80a7-91ae-cb52b4f94d15" class="bulleted-list"><li style="list-style-type:circle"><strong>Tòa nơi Seller đặt trụ sở</strong></li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8024-a2c2-e7a9fb7ba637" class="bulleted-list"><li style="list-style-type:disc">Ngôn ngữ:<div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-805f-8aad-fb42ce4cf8c6" class="bulleted-list"><li style="list-style-type:circle">Nếu khác nhau → <strong>tiếng Trung ưu tiên</strong></li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2cfc5e6f-95bd-809e-b8a9-dca43ee39495" class=""><strong>Hệ quả</strong></h3></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-800d-9588-f99eeba4c962" class="bulleted-list"><li style="list-style-type:disc">UNIPOWER:<div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-807c-9617-cebe0aac2221" class="bulleted-list"><li style="list-style-type:circle">Phải kiện tại Trung Quốc</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-809a-96a3-ece2c96dc360" class="bulleted-list"><li style="list-style-type:circle">Chi phí luật sư, dịch thuật, thời gian rất lớn</li></ul></div><div s
tyle="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8072-8c06-c4914a66cbfb" class="bulleted-list"><li style="list-style-type:circle">Gần như <strong>không khả thi cho tranh chấp nhỏ / trung bình</strong></li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80a5-97df-d270b8028893" class=""><strong>MỨC ĐỘ RỦI RO: CAO</strong></p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-8070-92f3-f28aeb47a2a7"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-803a-ac5e-fc0362d33de7" class=""><strong>5. KHÔNG CÓ ĐIỀU KHOẢN CAM KẾT PHÙ HỢP ĐĂNG KIỂM VIỆT NAM</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2cfc5e6f-95bd-8091-b40c-c65c149c3c97" class=""><strong>Thiếu hoàn toàn các cam kết bắt buộc:</strong></h3></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8042-829e-dec1b03b0ae0" class="">❌ Không có:</p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8070-a272-f4575441ea86" class="bulleted-list"><li style="list-style-type:disc">Cam kết <strong>đạt QCVN Việt Nam</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8019-807d-fd0d3135cd9b" class="bulleted-list"><li style="list-style-type:disc">Cam kết hỗ trợ <strong>homologation</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-807c-b102-cf9ae5f6fff5" class="bulleted-list"><li style="list-style-type:disc">Nghĩa vụ cung cấp test report theo yêu cầu VR</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80f4-81b2-c4060954c60b" class="bulleted-list"><li style="list-style-type:disc">Trách nhiệm nếu <strong>xe không được cấp chứng nhận</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8042-98a2-c779b75ec3d4" class="">📌 Nếu đăng kiểm từ chối → <strong>xe thành tài sản chết</strong></p></div><div style="display:contents" dir="auto"><p i
d="2cfc5e6f-95bd-80e0-8ba8-d00bea41ad0e" class=""><strong>MỨC ĐỘ RỦI RO: CAO</strong></p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-80d4-bf3e-f24254d7dada"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-8066-9518-f99c1c17b3ad" class=""><strong>6. MÂU THUẪN NGUY HIỂM: “BAO JUN E6 2026” NHƯNG LẠI LÀ “USED VEHICLE”</strong></h2></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8056-bca5-c3f7a91a5962" class="bulleted-list"><li style="list-style-type:disc">Invoice: xe <strong>2026</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-806e-8978-f00b11168b06" class="bulleted-list"><li style="list-style-type:disc">Contract: <strong>used vehicles</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-804a-af03-d07b0fdf1c30" class="">📌 Đây là <strong>mâu thuẫn pháp lý nghiêm trọng</strong>, cho phép:</p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8025-a4b1-d87eaf0f1669" class="bulleted-list"><li style="list-style-type:disc">Hải quan nghi ngờ gian lận</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8032-8d2a-fddd73b5ca1c" class="bulleted-list"><li style="list-style-type:disc">Đăng kiểm từ chối hồ sơ</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-803b-94e0-fe10e8340017" class="bulleted-list"><li style="list-style-type:disc">Seller phủ nhận trách nhiệm</li></ul></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-80eb-92c7-d0624bc9cee3"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-8093-86e1-fb74c792ec41" class=""><strong>7. RỦI RO HẢI QUAN &amp; THUẾ</strong></h2></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80b5-ab7e-cf3cac2c8361" class="bulleted-list"><li style="list-style-type:disc">Giá FOB: <strong>12,570 USD/xe</strong></li></ul></div><div style="display:contents" dir="auto"><ul i
d="2cfc5e6f-95bd-8090-9982-f482ba287fb8" class="bulleted-list"><li style="list-style-type:disc">Rất dễ bị:<div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-800c-afa1-db9e0fd73d3f" class="bulleted-list"><li style="list-style-type:circle">Hải quan VN <strong>tham vấn giá</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8073-a821-c97fbeebce0c" class="bulleted-list"><li style="list-style-type:circle">Yêu cầu chứng minh không chuyển giá</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80c7-b6ac-e0308d09cef6" class="bulleted-list"><li style="list-style-type:disc">Không có điều khoản:<div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80ae-8c8f-fc62f3edcac6" class="bulleted-list"><li style="list-style-type:circle">Seller hỗ trợ giải trình giá</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-8084-a90e-e5d42322f7fd"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-805f-89d0-da18d4ca2e06" class=""><strong>8. RỦI RO VỀ NGÂN HÀNG &amp; THANH TOÁN</strong></h2></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-803a-98a4-f9ec9b3c3e7f" class="bulleted-list"><li style="list-style-type:disc">Thanh toán qua:<div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-809a-86fe-f13fc0b4ef1b" class="bulleted-list"><li style="list-style-type:circle">Hong Kong entity</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8053-b10c-f67c5c41c1c2" class="bulleted-list"><li style="list-style-type:circle">Ngân hàng Trung Quốc</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8077-a0e0-fbe905e63694" class="bulleted-list"><li style="list-style-type:disc">Cần kiểm tra:<div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80d0-be44-fd85c3333819" class="bulleted-list"><li style="list-style-type:circle">AML</li></ul></div><div s
tyle="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80d8-9c32-d33937731171" class="bulleted-list"><li style="list-style-type:circle">KYC</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80db-bdb3-fd2fe6b59f7e" class="bulleted-list"><li style="list-style-type:circle">Chủ sở hữu thực (UBO)</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-80b2-a89e-c612f489a171"/></div><div style="display:contents" dir="auto"><h1 id="2cfc5e6f-95bd-80e1-a443-d7291351d439" class=""><strong>III. DANH SÁCH ĐIỀU KHOẢN BẮT BUỘC PHẢI BỔ SUNG (CHECKLIST)</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-80d2-acc4-fcbebf4b8649" class=""><strong>A. Điều khoản bắt buộc thêm mới</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2cfc5e6f-95bd-8001-a437-fa51955b117e" class="numbered-list" start="1"><li>Xác nhận <strong>xe mới 100%, chưa đăng ký, chưa sử dụng</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2cfc5e6f-95bd-808c-96a5-d5bf661913cb" class="numbered-list" start="2"><li>Cam kết <strong>đủ điều kiện đăng kiểm &amp; homologation tại Việt Nam</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2cfc5e6f-95bd-804a-9d01-ea70146bcac1" class="numbered-list" start="3"><li>Nghĩa vụ cung cấp <strong>test reports theo yêu cầu VR</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2cfc5e6f-95bd-8050-beea-d4d893c95870" class="numbered-list" start="4"><li>Điều khoản <strong>hủy hợp đồng / hoàn tiền</strong> nếu không đạt đăng kiểm</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2cfc5e6f-95bd-808e-be08-ec8ebae46108" class="numbered-list" start="5"><li>Bảo hành pin tối thiểu 5–8 năm (hoặc X chu kỳ)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2cfc5e6f-95bd-8053-b699-d47678a3d3a8" class="numbered-list" start="6"><li>Chia nhỏ t
hanh toán (30/70 hoặc 40/60)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2cfc5e6f-95bd-80a9-9009-c5abe168eb6e" class="numbered-list" start="7"><li>Điều khoản <strong>inspection trước khi giao</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2cfc5e6f-95bd-8078-a773-d87908f24c43" class="numbered-list" start="8"><li>Nghĩa vụ hỗ trợ kỹ thuật sau bán</li></ol></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-8024-8498-fde7e226eef8" class=""><strong>B. Điều khoản cần sửa / loại bỏ</strong></h2></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80e9-824b-de8cb5803049" class="bulleted-list"><li style="list-style-type:disc">❌ Toàn bộ clause “USED VEHICLES”</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8019-a790-ca1afc0d644d" class="bulleted-list"><li style="list-style-type:disc">❌ Miễn trừ toàn bộ trách nhiệm chất lượng</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-808e-a67b-d54ab66dc482" class="bulleted-list"><li style="list-style-type:disc">❌ Luật áp dụng độc quyền Trung Quốc (cần trung lập hoặc VN/SG)</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-800f-841a-e4a82d3612ac" class="bulleted-list"><li style="list-style-type:disc">❌ Tài phán tại nơi Seller</li></ul></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-80f1-a433-d8a8572877ba"/></div><div style="display:contents" dir="auto"><h1 id="2cfc5e6f-95bd-800d-a1f2-e37766c5faf6" class=""><strong>IV. KẾT LUẬN CUỐI CÙNG (AUDITOR VERDICT)</strong></h1></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80bd-941a-fea5cf2291da" class=""><strong>Ở trạng thái hiện tại:</strong></p></div><div style="display:contents" dir="auto"><blockquote id="2cfc5e6f-95bd-801f-8129-fb11feb518eb" class="">🔴 <strong>KHÔNG ĐƯỢC KÝ</strong></blockquote></div><div style="display:contents" dir="auto"><blockquote i
d="2cfc5e6f-95bd-8008-a919-d018178bfce9" class="">🔴 <strong>RỦI RO PHÁP LÝ CẤP ĐỘ DỰ ÁN</strong></blockquote></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-802a-973b-f7c7ec4cbc1c" class="">Hợp đồng này:</p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8072-aa9d-cd7ac2ad6266" class="bulleted-list"><li style="list-style-type:disc">Phù hợp <strong>mua xe cũ giá rẻ</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8027-a10b-cc62d4cf7eff" class="bulleted-list"><li style="list-style-type:disc">❌ Không phù hợp <strong>nhập xe mẫu EV cho đăng kiểm Việt Nam</strong><br/><br/>Dưới đây là danh sách <strong>rủi ro pháp lý “còn thiếu” cần bổ sung</strong> vào quy trình nhập <strong>02 xe Baojun mẫu theo hình thức nhập khẩu ủy thác</strong>, theo cấu trúc <strong>MECE, không hở khe</strong> (kèm gợi ý “điều khoản/phương án khóa rủi ro” để đưa thẳng vào hợp đồng và quy chế nội bộ).</li></ul></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-8064-9c9e-e257ab9a5e95"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-8046-a442-cc1d842198e2" class=""><strong>1) Rủi ro “đúng tư cách nhập khẩu” và phạm vi ủy thác</strong></h2></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-803d-ab48-fe4e8d0ca6b9" class=""><strong>Rủi ro</strong></p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8040-9dad-c8081f5eb2a2" class="bulleted-list"><li style="list-style-type:disc">Bên nhận ủy thác <strong>đứng tên tờ khai</strong> nhưng thực tế “mua – bán – sở hữu” không tách bạch rõ → phát sinh tranh chấp quyền sở hữu xe, quyền nhận hồ sơ gốc, quyền quyết định xử lý khi bị giữ hàng/kiểm hóa.</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8017-8100-cfe71c758381" class="bulleted-list"><li style="list-style-type:disc">Bên ủy thác tự ý thay đổi điều kiện giao hàng/giá/thuế suất/mã HS → kéo UNIPOWER vào rủi ro truy thu, p
hạt.</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80bf-a897-d5e14c7ce78a" class="bulleted-list"><li style="list-style-type:disc">“Ủy thác” nhưng lại vận hành như “đại lý/nhà phân phối” không có điều kiện pháp lý tương ứng (đặc biệt khi bước sang lô 20–50–200).</li></ul></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-803b-8076-d7581074a013" class=""><strong>Bổ sung cần có</strong></p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80b4-9055-f4ca94a89d9f" class="bulleted-list"><li style="list-style-type:disc"><strong>Hợp đồng ủy thác</strong>: điều khoản “không được thay đổi” (giá, điều kiện giao hàng, mã HS, mô tả hàng hóa, trị giá tính thuế) nếu không có phê duyệt bằng văn bản của UNIPOWER.</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80aa-999e-f0b8d491b177" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều khoản quyền sở hữu &amp; quyền kiểm soát hồ sơ gốc</strong>: hồ sơ gốc (invoice/packing list/B/L/C/O/giấy xuất xưởng/hồ sơ kỹ thuật) <strong>phải bàn giao vô điều kiện</strong> cho UNIPOWER trong X ngày sau thông quan.</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8015-929b-e314af995b6d" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều khoản xử lý sự cố hải quan</strong>: ai quyết định “mở kiểm hóa/giải trình/thuê giám định/kháng nghị” + trần ngân sách phát sinh + cơ chế phê duyệt.</li></ul></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-805f-b701-e62d6cbbff3d" class=""><strong>2) Rủi ro điều kiện nhập khẩu ô tô và yêu cầu chất lượng/kiểu loại</strong></h2></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8068-a668-d397d93f854d" class=""><strong>Rủi ro</strong></p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8023-99fd-f332d90ab923" class="bulleted-list"><li style="list-style-type:disc">Ô tô nhập khẩu chịu cơ chế điều kiện/kiểm t
ra chuyên ngành; hồ sơ kỹ thuật không đạt yêu cầu → bị kéo dài thông quan, bị yêu cầu thử nghiệm bổ sung, đội chi phí.</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-800c-bbd7-c938432a9b87" class="bulleted-list"><li style="list-style-type:disc">Nhầm kỳ vọng “xe mẫu” sẽ được miễn các nghĩa vụ kiểm tra như xe thương mại → dễ sai; thực tế miễn/giảm chỉ áp dụng khi <strong>được cơ quan có thẩm quyền chấp nhận</strong> theo hồ sơ/đối tượng cụ thể (không nên ghi “đương nhiên được miễn”).</li></ul></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8055-9fe9-f33e16e98e7a" class=""><strong>Bổ sung cần có</strong></p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8013-8bb4-d21c05224552" class="bulleted-list"><li style="list-style-type:disc"><strong>Phòng Pháp chế + Kỹ thuật</strong> phải thêm mục: “ma trận yêu cầu hồ sơ/kiểm tra theo quy định hiện hành” (danh mục giấy tờ tối thiểu + bản dịch + hợp pháp hóa/lãnh sự nếu cần).</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-807b-98e8-d0ce0dfdc8b4" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều khoản trách nhiệm hồ sơ của Baojun</strong>: nếu hồ sơ không đáp ứng khiến phải thử nghiệm lại/chi phí phát sinh → <strong>Baojun chịu</strong> (hoặc chia sẻ theo tỷ lệ, nhưng phải ghi rõ).</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8032-a377-f8d0209d18b5" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều khoản “mốc chấp nhận trước”</strong>: chỉ cho phép xe rời nhà máy sau khi UNIPOWER xác nhận “bộ hồ sơ nộp trước” đạt chuẩn nội bộ để nộp/trao đổi trước với cơ quan đăng kiểm.</li></ul></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-8048-92ee-d5ff57854f65" class=""><strong>3) Rủi ro “khai báo trị giá – xuất xứ – mã hàng” dẫn tới truy thu/phạt</strong></h2></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-804f-9703-dea27b50d337" c
lass=""><strong>Rủi ro</strong></p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-809b-8ee6-f1e92ad200e2" class="bulleted-list"><li style="list-style-type:disc">Trị giá tính thuế bị nghi ngờ (giá thấp do xe mẫu, hỗ trợ thị trường…) → bị tham vấn giá, ấn định thuế, phạt chậm nộp.</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80ff-8761-e71ff02d66ba" class="bulleted-list"><li style="list-style-type:disc">C/O không phù hợp form/tiêu chí xuất xứ → mất ưu đãi (nếu có), bị truy thu.</li></ul></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8084-b162-cb05d913fb40" class=""><strong>Bổ sung cần có</strong></p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8063-9222-ef6ee1310163" class="bulleted-list"><li style="list-style-type:disc">Bộ “hồ sơ giải trình giá” chuẩn: thư xác nhận xe mẫu + mục đích thử nghiệm + điều kiện hạn chế chuyển nhượng (nếu áp dụng) + cấu phần giá.</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80f9-a3d8-ef2cac4ef78c" class="bulleted-list"><li style="list-style-type:disc">Điều khoản bắt buộc Baojun cung cấp <strong>bằng chứng cấu phần giá</strong> và tài liệu hỗ trợ xuất xứ.</li></ul></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-8045-8cb4-cea3ad012454" class=""><strong>4) Rủi ro trách nhiệm sản phẩm, triệu hồi, bảo hành và hậu mãi tại Việt Nam</strong></h2></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80b6-b384-dfa152963366" class=""><strong>Rủi ro</strong></p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8096-8317-d0f642277410" class="bulleted-list"><li style="list-style-type:disc">Khi xe chạy thử thực tế (đặc biệt vận hành dịch vụ), nếu xảy ra lỗi an toàn → rủi ro trách nhiệm sản phẩm, thu hồi/sửa chữa, khiếu nại khách hàng, ảnh hưởng thương hiệu.</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8014-84c2-c31eadac3fdd" c
lass="bulleted-list"><li style="list-style-type:disc">Nghĩa vụ bảo hành/triệu hồi liên quan đến xe nhập khẩu thường bị cơ quan quản lý và người dùng soi rất kỹ.</li></ul></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8010-888d-eab8653e909a" class=""><strong>Bổ sung cần có</strong></p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8031-a1fd-f01546b396bf" class="bulleted-list"><li style="list-style-type:disc">Phụ lục “<strong>bảo hành – phụ tùng – quy trình xử lý sự cố</strong>” (SLA thời gian phản hồi, phụ tùng tối thiểu, kỹ sư hỗ trợ, chi phí ai chịu).</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8088-b9c3-e4768b8ae1f5" class="bulleted-list"><li style="list-style-type:disc">Điều khoản “<strong>triệu hồi &amp; an toàn</strong>”: cơ chế phối hợp, quyền dừng vận hành, nghĩa vụ cung cấp bản cập nhật kỹ thuật/phần mềm, nghĩa vụ báo cáo sự cố nghiêm trọng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80d3-93c2-c4f6235c3e04" class="bulleted-list"><li style="list-style-type:disc">Bảo hiểm: yêu cầu tối thiểu về <strong>bảo hiểm trách nhiệm</strong> trong giai đoạn thử nghiệm.</li></ul></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-8093-b5c1-d951e2c19296" class=""><strong>5) Rủi ro dữ liệu cá nhân và dữ liệu camera/telematics</strong></h2></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-801b-9149-d843c5b1ae7c" class=""><strong>Rủi ro</strong></p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80fb-a575-d3d28bb02697" class="bulleted-list"><li style="list-style-type:disc">Nếu gắn telematics/camera/hệ thống giám sát người lái/định vị… sẽ phát sinh nghĩa vụ theo quy định bảo vệ dữ liệu cá nhân: mục đích xử lý, thông báo/đồng ý, lưu trữ, chuyển dữ liệu ra nước ngoài, phân quyền truy cập, thời hạn lưu…</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80ef-bcea-c09808df418b" c
lass="bulleted-list"><li style="list-style-type:disc">Dữ liệu có thể đi qua hạ tầng/đám mây của nhà sản xuất hoặc bên thứ ba → rủi ro chuyển dữ liệu xuyên biên giới và rò rỉ.</li></ul></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-801d-96cf-d306874c286d" class=""><strong>Bổ sung cần có</strong></p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8034-a269-cc3af8626126" class="bulleted-list"><li style="list-style-type:disc">Chính sách “<strong>quản trị dữ liệu thử nghiệm</strong>”: loại dữ liệu thu, mục đích, thời hạn lưu, ai truy cập, quy trình xóa, nhật ký truy cập.</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8088-bd4e-ce6da9936b0c" class="bulleted-list"><li style="list-style-type:disc">Điều khoản với Baojun/nhà cung cấp thiết bị: <strong>không tự ý thu/đẩy dữ liệu ra ngoài</strong> khi chưa có phê duyệt; quy định nơi lưu trữ; cơ chế xử lý sự cố an ninh.</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8079-b19d-d4c304664eb2" class="bulleted-list"><li style="list-style-type:disc">Mẫu <strong>thông báo/đồng ý</strong> cho tài xế vận hành thử (vì có dữ liệu định danh/giọng nói/hình ảnh).</li></ul></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-8087-8f28-f699ea2346d1" class=""><strong>6) Rủi ro môi trường: pin, ắc quy, tái chế và chất thải nguy hại</strong></h2></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-809f-bc52-f5a30c23cea0" class=""><strong>Rủi ro</strong></p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8022-b92b-d43f50f62d7a" class="bulleted-list"><li style="list-style-type:disc">Pin lithium và linh kiện liên quan có nghĩa vụ quản lý môi trường (thu hồi, tái chế, xử lý) theo cơ chế trách nhiệm mở rộng của nhà sản xuất/nhập khẩu (tùy vai trò pháp lý của UNIPOWER/bên ủy thác ở giai đoạn sau).</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-804f-b562-d01f57304c51" c
lass="bulleted-list"><li style="list-style-type:disc">Nếu chưa thiết kế kênh thu hồi pin/hỏng pin trong thử nghiệm → rủi ro vi phạm môi trường và rủi ro chi phí “bất ngờ”.</li></ul></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80b2-9f01-f58cb2e845bf" class=""><strong>Bổ sung cần có</strong></p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-809d-80d9-ce72f8828932" class="bulleted-list"><li style="list-style-type:disc">Điều khoản “<strong>xử lý pin/linh kiện sau thử nghiệm</strong>”: ai chịu trách nhiệm, kênh xử lý, chi phí, nhà thầu đủ điều kiện.</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8073-a658-ef89f324cce7" class="bulleted-list"><li style="list-style-type:disc">Checklist tuân thủ môi trường trong giai đoạn thử nghiệm (lưu giữ, vận chuyển, xử lý).</li></ul></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-80ce-994d-f7fb7c47b1d9" class=""><strong>7) Rủi ro tiêu chuẩn sạc, tương thích hạ tầng, an toàn điện/PCCC</strong></h2></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-807a-879f-d7e01aa9ccfa" class=""><strong>Rủi ro</strong></p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80d3-a7b3-f9fdd8bc1983" class="bulleted-list"><li style="list-style-type:disc">Nếu chuẩn sạc/đầu nối/điện áp không tương thích hạ tầng dự kiến → rủi ro phải thay đổi thiết kế trạm sạc hoặc mua bộ chuyển đổi, kéo dài pilot.</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-802e-ad5c-fa055c3abca5" class="bulleted-list"><li style="list-style-type:disc">Yêu cầu an toàn điện và PCCC tại điểm sạc (đặc biệt nếu đặt trạm thử nghiệm tại bãi/depot). (Quy định/tiêu chuẩn có thể thay đổi theo địa phương và theo từng loại công trình.)</li></ul></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-800f-a8d1-e86ab1fd0b3a" class=""><strong>Bổ sung cần có</strong></p></div><div style="display:contents" dir="auto"><ul i
d="2cfc5e6f-95bd-80ef-b10c-ca0d3d6911c0" class="bulleted-list"><li style="list-style-type:disc">Phụ lục “<strong>chuẩn sạc &amp; thông số tương thích</strong>” khóa cứng trước khi xuất xưởng (không để “gửi xe bất kỳ rồi tính sau”).</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80b2-94af-f7956d8e6b9e" class="bulleted-list"><li style="list-style-type:disc">Kế hoạch nghiệm thu an toàn điện/PCCC theo từng điểm thử nghiệm (chủ điểm chịu trách nhiệm, hồ sơ, bản vẽ, nghiệm thu).</li></ul></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-8012-9b4d-e6ea75619abd" class=""><strong>8) Rủi ro pháp lý vận hành thử nghiệm (lưu hành, đăng ký, bảo hiểm, phạm vi sử dụng)</strong></h2></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80eb-a81d-f6c6b43f37c5" class=""><strong>Rủi ro</strong></p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8057-956c-c7aafd32f1da" class="bulleted-list"><li style="list-style-type:disc">Xe chưa hoàn tất thủ tục lưu hành mà chạy thử ngoài phạm vi cho phép → rủi ro xử phạt, tạm giữ phương tiện.</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-808f-84b2-e93ca4b38fe1" class="bulleted-list"><li style="list-style-type:disc">Thiếu bảo hiểm bắt buộc/không rõ phạm vi sử dụng thử nghiệm (nội bộ vs cung cấp dịch vụ).</li></ul></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8034-a2fe-f3b1104a7669" class=""><strong>Bổ sung cần có</strong></p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80dd-ba4b-d6969ac22f10" class="bulleted-list"><li style="list-style-type:disc">Quy định nội bộ: “xe chỉ được chạy thử theo <strong>phạm vi – tuyến – mục đích</strong> đã phê duyệt”, có lệnh điều xe/nhật ký.</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8087-b1f7-d5e80e30a89a" class="bulleted-list"><li style="list-style-type:disc">Gói bảo hiểm tối thiểu bắt buộc trước khi lăn bánh (trách nhiệm d
ân sự, vật chất, người ngồi trên xe…).</li></ul></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-805a-bfab-cb7585193f95" class=""><strong>9) Rủi ro hợp đồng quốc tế: luật áp dụng, giải quyết tranh chấp, chế tài giao hàng</strong></h2></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-800d-bba2-dec8ac59c1db" class=""><strong>Rủi ro</strong></p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8096-a00e-fd266fe54d2d" class="bulleted-list"><li style="list-style-type:disc">Hợp đồng 3 bên nếu không khóa: luật áp dụng, cơ quan giải quyết tranh chấp, ngôn ngữ ưu tiên, điều kiện phạt chậm giao/không đạt spec → khi phát sinh sự cố sẽ rất khó “ép” nhà sản xuất.</li></ul></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-800a-b595-e6191866f42f" class=""><strong>Bổ sung cần có</strong></p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80fe-b0cc-fcb2e1199a74" class="bulleted-list"><li style="list-style-type:disc">Điều khoản: luật áp dụng + cơ chế giải quyết tranh chấp + ngôn ngữ ưu tiên.</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80a3-9f09-eaffeb27a300" class="bulleted-list"><li style="list-style-type:disc">Điều khoản “<strong>chấp nhận chất lượng</strong>” tại Việt Nam: tiêu chí nghiệm thu, quyền từ chối nhận/giữ lại thanh toán, phạt chậm, bồi thường.</li></ul></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-8017-9e59-e8ef16dbba23" class=""><strong>10) Rủi ro “chuyển pha” từ 2 xe mẫu sang lô thương mại</strong></h2></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-801b-a671-ccdda10ae6e6" class=""><strong>Rủi ro</strong></p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80c8-9b5c-c7d3ea2d64b3" class="bulleted-list"><li style="list-style-type:disc">Nhiều dự án EV chết ở điểm chuyển pha vì: hồ sơ kiểu loại/kiểm tra chất lượng/điều kiện kinh doanh/after-sales chưa sẵn sàng.</li></ul></div><div s
tyle="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8030-a7d3-d4fd41977831" class=""><strong>Bổ sung cần có</strong></p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8090-87e0-d8afae26601c" class="bulleted-list"><li style="list-style-type:disc">Ngay trong pilot 2 xe: tạo “<strong>hồ sơ nền cho lô 20–50</strong>” (bản đồ yêu cầu pháp lý, danh mục giấy phép/điều kiện, kế hoạch bảo hành – phụ tùng – đào tạo – dịch vụ).</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8075-baf4-c2c3d440f0d7" class="bulleted-list"><li style="list-style-type:disc">Cơ chế “cổng quyết định”: chỉ mở lô tiếp theo nếu đạt KPI pháp lý (thời gian thông quan, đạt thử nghiệm, chi phí tuân thủ, khả năng hậu mãi).</li></ul></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-8039-aac1-ec5ebdf6d619"/></div><div style="display:contents" dir="auto"><h3 id="2cfc5e6f-95bd-804d-ad91-e9c48369826a" class=""><strong>Các điểm cần sửa ngay trong đoạn bạn đang dùng (để tránh rủi ro câu chữ)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-805c-8a25-c1d3e36f2019" class="bulleted-list"><li style="list-style-type:disc">Thay câu “<strong>Xe mẫu không áp tiêu chuẩn thương mại / miễn thử nghiệm nhờ hồ sơ Trung Quốc</strong>” bằng:<div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-801c-908c-ec4fcf1fc111" class=""><strong>“Xem xét khả năng được giảm/miễn một số hạng mục theo quy định hiện hành trên cơ sở hồ sơ kỹ thuật và chấp thuận của cơ quan có thẩm quyền; không mặc định.”</strong></p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-808b-b0f4-dd1e7f27341c" class="bulleted-list"><li style="list-style-type:disc">Bổ sung hẳn một tiểu mục trong <strong>PHÒNG PHÁP CHẾ</strong>: “dữ liệu cá nhân &amp; an ninh thông tin” (vì xe điện + telematics gần như chắc chắn dính Nghị định 13/2023).</li></ul></div><div style="display:contents" dir="auto"><ul i
d="2cfc5e6f-95bd-806b-8205-d67d9e7cfc1f" class="bulleted-list"><li style="list-style-type:disc">Bổ sung trong <strong>PHÒNG KỸ THUẬT – VẬN HÀNH</strong>: “chuẩn sạc/tương thích, an toàn điện/PCCC điểm sạc, quy trình xử lý pin &amp; linh kiện”.</li></ul></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8077-9303-d9505c63418a" class="">
</p></div><div style="display:contents" dir="ltr"><figure id="2ddc5e6f-95bd-80e9-ace6-df548e2d0066" class="link-to-page"><a href="A)%20Account%20+%20Infrastructure%20Setup%20(Execution-only)%202ddc5e6f95bd80e9ace6df548e2d0066.html">A) Account + Infrastructure Setup (Execution-only)</a></figure></div><div style="display:contents" dir="ltr"><figure id="2cfc5e6f-95bd-80b2-b60c-d3e79afa4842" class="link-to-page"><a href="H%E1%BB%A2P%20%C4%90%E1%BB%92NG%20MUA%20B%C3%81N%202cfc5e6f95bd80b2b60cd3e79afa4842.html">HỢP ĐỒNG MUA BÁN</a></figure></div><div style="display:contents" dir="ltr"><figure id="2cfc5e6f-95bd-80b9-be2e-c466d9e3aea8" class="link-to-page"><a href="H%C3%93A%20%C4%90%C6%A0N%20CHI%E1%BA%BEU%20L%E1%BB%86%20(PROFORMA%20INVOICE)%202cfc5e6f95bd80b9be2ec466d9e3aea8.html">HÓA ĐƠN CHIẾU LỆ (PROFORMA INVOICE)</a></figure></div><div style="display:contents" dir="ltr"><figure id="2cfc5e6f-95bd-801c-bcea-dcb40b593fa0" class="link-to-page"><a href="%C4%90%E1%BB%80%20XU%E1%BA%A4T%20CH%E1%BB%88NH%20S%E1%BB%ACA%20H%E1%BB%A2P%20%C4%90%E1%BB%92NG%20%E2%80%93%20B%E1%BA%A2O%20V%E1%BB%86%20B%C3%8AN%20MUA%20(UNIPO%202cfc5e6f95bd801cbceadcb40b593fa0.html">ĐỀ XUẤT CHỈNH SỬA HỢP ĐỒNG – BẢO VỆ BÊN MUA (UNIPOWER)</a></figure></div><div style="display:contents" dir="ltr"><figure id="2ddc5e6f-95bd-80d7-8354-c425f2b2fd4c" class="link-to-page"><a href="V%C4%82N%20B%E1%BA%A2N%20TH%E1%BA%A8M%20%C4%90%E1%BB%8ANH%20CHI%E1%BA%BEN%20L%C6%AF%E1%BB%A2C%202ddc5e6f95bd80d78354c425f2b2fd4c.html">VĂN BẢN THẨM ĐỊNH CHIẾN LƯỢC </a></figure></div><div style="display:contents" dir="ltr"><figure id="2ddc5e6f-95bd-8075-804a-d2c4529daebd" class="link-to-page"><a href="Untitled%202ddc5e6f95bd8075804ad2c4529daebd.html">Untitled</a></figure></div><div style="display:contents" dir="ltr"><figure id="2dfc5e6f-95bd-803a-bed3-d88fb9daf85d" class="link-to-page"><a href="T%E1%BB%9C%20TR%C3%8CNH%20TH%C6%AF%20B%C3%80Y%20T%E1%BB%8E%20NGUY%E1%BB%86N%20V%E1%BB%8CNG%202dfc5e6f95bd803abed3d88fb9daf85d.html">TỜ TRÌNH / THƯ B
ÀY TỎ NGUYỆN VỌNG</a></figure></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
