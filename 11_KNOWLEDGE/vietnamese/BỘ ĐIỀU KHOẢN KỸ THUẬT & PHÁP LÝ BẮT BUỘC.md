---
tags: [vietnamese]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>BỘ ĐIỀU KHOẢN KỸ THUẬT &amp; PHÁP LÝ BẮT BUỘC</title><style>
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
	
</style></head><body><article id="2adc5e6f-95bd-8047-894f-d7bc61c0a316" class="page sans"><header><h1 class="page-title" dir="auto"><strong>BỘ ĐIỀU KHOẢN KỸ THUẬT &amp; PHÁP LÝ BẮT BUỘC</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2adc5e6f-95bd-803f-949a-cb45a2689f6a" class=""><strong>BỘ ĐIỀU KHOẢN KỸ THUẬT &amp; PHÁP LÝ BẮT BUỘC KHI LÀM VIỆC VỚI BAOJUN – ÁP DỤNG CHO THỊ TRƯỜNG VIỆT NAM</strong></p></div><div style="display:contents" dir="auto"><p id="2adc5e6f-95bd-8009-b72f-ea4cab1fd2cd" class="">(Đính kèm Hợp đồng khung và các hợp đồng mua bán; áp dụng cả khi nhập khẩu uỷ thác qua bên thứ ba.)</p></div><div style="display:contents" dir="auto"><hr id="2adc5e6f-95bd-8095-9dd4-ee4d394fb18c"/></div><div style="display:contents" dir="auto"><h2 id="2adc5e6f-95bd-8021-acf8-d659a34b95d1" class=""><strong>I. ĐIỀU KHOẢN VỀ TÌNH TRẠNG XE &amp; XUẤT KHẨU</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-80ba-9547-ebc22ecb9bac" class="numbered-list" start="1"><li><strong>Xe mới 100% – chưa đăng ký, chưa lưu hành nội địa Trung Quốc</strong><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80d5-9017-ded423d40e6e" class="bulleted-list"><li style="list-style-type:disc">Baojun cam kết toàn bộ xe cung cấp cho thị trường Việt Nam là xe mới hoàn toàn, chưa từng:<div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-806a-8275-f5bb55d72912" class="bulleted-list"><li style="list-style-type:circle">Đăng ký lưu hành tại bất kỳ địa phương nào ở Trung Quốc.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80b0-bf89-e197358a88a0" class="bulleted-list"><li style="list-style-type:circle">Sử dụng, cho thuê, chạy thử thương mại nội địa.</li></ul></div></li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-8089-9531-f6340ca2db1b" class="numbered-list" start="2"><li><strong>Không xuất khẩu dưới dạng “xe cũ”</strong><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-802f-a798-c47010cbe299" class="bulleted-list"><li style="list-style-type:disc">Baojun cam kết:<div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8052-b87b-ebb9580b0d93" class="bulleted-list"><li style="list-style-type:circle">Không sử dụng hình thức “đăng ký nội địa rồi huỷ đăng ký để xuất khẩu”.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80b3-9089-d6105da7cb19" class="bulleted-list"><li style="list-style-type:circle">Không xuất khẩu dưới bất kỳ hình thức xe đã qua sử dụng.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80f3-a92c-e94c53242637" class="bulleted-list"><li style="list-style-type:disc">Mọi vi phạm dẫn đến việc xe không được thông quan hoặc phát sinh chi phí bổ sung, Baojun chịu hoàn toàn trách nhiệm.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-8069-ae91-da406c895b68" class="numbered-list" start="3"><li><strong>Mã số nhận dạng xe và chứng thư xuất xưởng</strong><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-808b-a7d5-c024fb3f1b97" class="bulleted-list"><li style="list-style-type:disc">Baojun cung cấp đầy đủ trước khi giao hàng:<div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8068-bd50-f48e19c5a500" class="bulleted-list"><li style="list-style-type:circle">Danh sách số khung, số máy của từng xe.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80b0-824e-c53194f812af" class="bulleted-list"><li style="list-style-type:circle">Giấy chứng nhận xuất xưởng do nhà máy cấp.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8016-8803-d8fa2a89f002" class="bulleted-list"><li style="list-style-type:circle">Hình ảnh xe tại nhà máy trước khi bốc xếp lên tàu.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80de-a6ba-eb963d95c90e" class="bulleted-list"><li style="list-style-type:disc">Đây là điều kiện bắt buộc để cơ quan hải quan Việt Nam không nghi ngờ về trị giá, xuất xứ và tình trạng xe.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="2adc5e6f-95bd-80ef-9c9f-e2423dcf4562"/></div><div style="display:contents" dir="auto"><h2 id="2adc5e6f-95bd-80ab-83d3-ede827a4d75a" class=""><strong>II. ĐIỀU KHOẢN KỸ THUẬT CHO THỊ TRƯỜNG VIỆT NAM</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-808d-8417-fcf03393fd9d" class="numbered-list" start="1"><li><strong>Chuẩn đầu sạc và tiêu chuẩn kỹ thuật trạm sạc</strong><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-804a-871e-dc50a9e9c1f3" class="bulleted-list"><li style="list-style-type:disc">Phiên bản xe cung cấp cho Việt Nam phải sử dụng chuẩn sạc phù hợp với hệ thống trạm sạc đang và sẽ được triển khai tại Việt Nam, cụ thể:<div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-800e-96dd-f9ed3e6b9595" class="bulleted-list"><li style="list-style-type:circle">Đầu sạc xoay chiều loại 2.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80e2-9689-d21703c8a605" class="bulleted-list"><li style="list-style-type:circle">Đầu sạc một chiều tích hợp tiêu chuẩn châu Âu.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80af-87f7-c317bf7ac071" class="bulleted-list"><li style="list-style-type:disc">Không được sử dụng chuẩn đầu sạc độc quyền nội địa Trung Quốc.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-80a4-9e71-d92de6f1b593" class="numbered-list" start="2"><li><strong>Giao thức sạc và khả năng tương thích với trạm</strong><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80bc-be0c-ffd6cf30fa55" class="bulleted-list"><li style="list-style-type:disc">Xe phải hỗ trợ đầy đủ các giao thức trao đổi dữ liệu với trạm sạc theo tiêu chuẩn đang áp dụng tại Việt Nam, bảo đảm:<div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80b7-b235-e58afd324400" class="bulleted-list"><li style="list-style-type:circle">Kết nối, nhận diện, khoá/mở khoá sạc.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8009-ac71-fc964992c50d" class="bulleted-list"><li style="list-style-type:circle">Đo đếm điện năng chính xác.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-807d-869c-d09c115bd621" class="bulleted-list"><li style="list-style-type:circle">Ngắt sạc an toàn khi có sự cố.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80e3-bb1e-ddd585711147" class="bulleted-list"><li style="list-style-type:disc">Mục tiêu: đảm bảo xe hoạt động ổn định với hệ thống trạm sạc của Unipower và các trạm sạc tiêu chuẩn trên thị trường.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-80b2-bc0a-e954dc40f4e7" class="numbered-list" start="3"><li><strong>Bộ hồ sơ kỹ thuật phục vụ đăng kiểm</strong><div style="display:contents" dir="auto"><p id="2adc5e6f-95bd-80e4-958b-f2fb2f640a95" class="">Baojun phải cung cấp đầy đủ bộ hồ sơ kỹ thuật bằng tiếng Việt hoặc tiếng Anh (tuỳ thỏa thuận), gồm tối thiểu:</p></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8057-a481-d20c69547299" class="bulleted-list"><li style="list-style-type:disc">Thông số kỹ thuật chi tiết của xe.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80c4-98ff-e8661791c9b5" class="bulleted-list"><li style="list-style-type:disc">Bản vẽ kỹ thuật.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-801c-b483-e99515918187" class="bulleted-list"><li style="list-style-type:disc">Biên bản thử nghiệm hệ thống phanh, thử nghiệm pin, nhiễu điện từ, an toàn điện áp cao.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80b6-8c35-fe08c3c53aa3" class="bulleted-list"><li style="list-style-type:disc">Chứng nhận phù hợp tiêu chuẩn vận chuyển và sử dụng pin, cell pin.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-804f-8d46-d9d102771b60" class="bulleted-list"><li style="list-style-type:disc">Kết quả thử nghiệm cháy nổ, đo rò rỉ, chống chập điện.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80a3-a543-ee4fc8e6fc66" class="bulleted-list"><li style="list-style-type:disc">Kết quả thử nghiệm va chạm.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80bb-9b6d-d6a664ff6528" class="bulleted-list"><li style="list-style-type:disc">Kết quả thử nghiệm độ kín nước, khả năng chống ngập của cụm pin.</li></ul></div><div style="display:contents" dir="auto"><p id="2adc5e6f-95bd-8097-a0f7-f9430b533fba" class="">Trường hợp hồ sơ không đầy đủ hoặc không đáp ứng yêu cầu của cơ quan đăng kiểm Việt Nam, Baojun có trách nhiệm bổ sung, hiệu chỉnh mà không tính thêm chi phí cho Unipower.</p></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-807b-a324-f05146932fdb" class="numbered-list" start="4"><li><strong>Cam kết tuân thủ các quy chuẩn kỹ thuật quốc gia</strong><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8010-8ca6-fcfde5936699" class="bulleted-list"><li style="list-style-type:disc">Baojun cam kết thiết kế, sản xuất và hoàn thiện xe phù hợp với các quy chuẩn kỹ thuật quốc gia hiện hành liên quan tới ô tô, an toàn điện, hệ thống phanh, hệ thống dây dẫn điện và an toàn pin cho xe điện.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8085-94b0-f171708f3d3f" class="bulleted-list"><li style="list-style-type:disc">Nếu có thay đổi quy chuẩn trong thời gian thực hiện hợp đồng, hai bên sẽ cùng rà soát; phần điều chỉnh về kỹ thuật (nếu có) do Baojun chịu trách nhiệm chính.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="2adc5e6f-95bd-80dc-900a-cafe8809b400"/></div><div style="display:contents" dir="auto"><h2 id="2adc5e6f-95bd-8075-9253-ceacfab1b28d" class=""><strong>III. ĐIỀU KHOẢN BẢO HÀNH CHUYÊN DỤNG CHO TAXI</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-80e3-a6b1-f366d3eec23f" class="numbered-list" start="1"><li><strong>Bảo hành hệ thống điện động lực tối thiểu 8 năm / 600.000 km</strong><div style="display:contents" dir="auto"><p id="2adc5e6f-95bd-8050-9086-f907eb96bc32" class="">Áp dụng cho:</p></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80fc-aff9-cca84f9bf832" class="bulleted-list"><li style="list-style-type:disc">Động cơ điện.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8013-bb80-f29c40c86b42" class="bulleted-list"><li style="list-style-type:disc">Bộ biến tần.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80c3-ada7-ce5ef44e9106" class="bulleted-list"><li style="list-style-type:disc">Bộ điều khiển trung tâm hệ thống truyền động.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80ef-9259-c375a02b27c4" class="bulleted-list"><li style="list-style-type:disc">Cụm pin điện áp cao.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8057-a8e7-f0e8f6e9f2f4" class="bulleted-list"><li style="list-style-type:disc">Hệ thống dây dẫn, giắc nối thuộc mạch điện áp cao.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-80b3-a730-ccf4cc206140" class="numbered-list" start="2"><li><strong>Bảo hành pin theo điều kiện khai thác taxi thương mại</strong><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-801b-b2b7-ee85032f9917" class="bulleted-list"><li style="list-style-type:disc">Baojun cam kết dung lượng pin không suy giảm quá 30% so với dung lượng ban đầu sau 600.000 km vận hành trong điều kiện taxi.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8068-a7e8-e8ee3702a9ee" class="bulleted-list"><li style="list-style-type:disc">Trường hợp:<div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8058-87c6-c4f7296b5010" class="bulleted-list"><li style="list-style-type:circle">Pin phồng, nứt vỡ, rò rỉ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8047-9794-ecd049956e7d" class="bulleted-list"><li style="list-style-type:circle">Hệ thống quản lý pin lỗi.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-807b-9ceb-c8d45989e772" class="bulleted-list"><li style="list-style-type:circle">Dung lượng suy giảm vượt mức cam kết.<div style="display:contents" dir="auto"><p id="2adc5e6f-95bd-8033-a107-f931715da812" class="">→ Baojun có trách nhiệm sửa chữa, thay thế cell hoặc cụm pin mới, không tính chi phí cho Unipower trong thời hạn bảo hành.</p></div></li></ul></div></li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-805e-b225-f3210103cd07" class="numbered-list" start="3"><li><strong>Bảo hành trong điều kiện khai thác khắc nghiệt tại Việt Nam</strong><div style="display:contents" dir="auto"><p id="2adc5e6f-95bd-8057-8fbd-ded6634b4c8f" class="">Baojun xác nhận chế độ bảo hành áp dụng cho điều kiện:</p></div></li></ol></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80d8-aafe-e8cf80144b3a" class="bulleted-list"><li style="list-style-type:disc">Nhiệt độ môi trường thường xuyên từ 35–42°C.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80e6-9274-ceb502d85430" class="bulleted-list"><li style="list-style-type:disc">Thời gian kẹt xe kéo dài 2–4 giờ liên tục.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8015-83d3-cc6865cbaf5e" class="bulleted-list"><li style="list-style-type:disc">Xe vận hành 18–20 giờ/ngày, liên tục nhiều ngày.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8012-8de3-c474cf1c5de2" class="bulleted-list"><li style="list-style-type:disc">Đường xá nhiều ổ gà, gờ giảm tốc, mặt đường kém.</li></ul></div><div style="display:contents" dir="auto"><p id="2adc5e6f-95bd-8032-b222-e3a4973c0552" class="">Cam kết này được hiểu là <strong>bảo hành cho mục đích taxi thương mại</strong>, không áp dụng chuẩn bảo hành xe cá nhân sử dụng nhẹ.</p></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-805c-b1c7-fd83cb849cd8" class="numbered-list" start="1"><li><strong>Cam kết về phụ tùng và thời gian cung ứng</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-800f-8910-e046d7142de3" class="bulleted-list"><li style="list-style-type:disc">Baojun cam kết duy trì khả năng cung ứng phụ tùng cho dòng xe này trong tối thiểu 10 năm kể từ ngày giao xe đầu tiên.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-808b-869e-f1797340d4e6" class="bulleted-list"><li style="list-style-type:disc">Cung cấp bảng giá trần đối với các phụ tùng chủ lực, đảm bảo mức giá ổn định, có lộ trình điều chỉnh hợp lý.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-808a-a986-e4a66160aeaa" class="bulleted-list"><li style="list-style-type:disc">Thời gian cung ứng mỗi đợt phụ tùng thông dụng không vượt quá 7–14 ngày làm việc (tuỳ loại).</li></ul></div><div style="display:contents" dir="auto"><hr id="2adc5e6f-95bd-80dd-8f25-e4d0f0f96b95"/></div><div style="display:contents" dir="auto"><h2 id="2adc5e6f-95bd-8020-8b21-d034a2644f89" class=""><strong>IV. ĐIỀU KHOẢN VỀ DỊCH VỤ, HỖ TRỢ KỸ THUẬT VÀ PHẦN MỀM</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-8077-99f4-e64083f43dcb" class="numbered-list" start="1"><li><strong>Đào tạo kỹ thuật tại Việt Nam</strong><div style="display:contents" dir="auto"><p id="2adc5e6f-95bd-802d-a995-f1e18fdd4012" class="">Baojun có trách nhiệm:</p></div></li></ol></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8022-aa5f-dad7291d227e" class="bulleted-list"><li style="list-style-type:disc">Tổ chức hoặc uỷ quyền đào tạo đội ngũ kỹ thuật của Unipower/Mai Linh về chẩn đoán, sửa chữa, bảo dưỡng xe.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-809c-914d-d406c37d1b26" class="bulleted-list"><li style="list-style-type:disc">Cung cấp đầy đủ tài liệu hướng dẫn sửa chữa, sơ đồ mạch điện, quy trình kiểm tra.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-803d-9dc8-fda74a8f9706" class="bulleted-list"><li style="list-style-type:disc">Cung cấp thiết bị chẩn đoán chuyên dụng và cập nhật phần mềm cho thiết bị này.</li></ul></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-8057-ac2f-cb510afda73f" class="numbered-list" start="1"><li><strong>Cập nhật phần mềm trong suốt vòng đời xe</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80d9-82f7-efb87079db11" class="bulleted-list"><li style="list-style-type:disc">Baojun duy trì việc cập nhật phần mềm cho các hệ thống điều khiển trên xe (quản lý pin, điều khiển động cơ, màn hình trung tâm…) trong suốt vòng đời sản phẩm.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-807f-9185-c6b563e779b2" class="bulleted-list"><li style="list-style-type:disc">Các bản cập nhật nhằm:<div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80f2-b0cd-f9e42a9888cd" class="bulleted-list"><li style="list-style-type:circle">Khắc phục lỗi kỹ thuật phát sinh.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-806c-955f-dc8006c288aa" class="bulleted-list"><li style="list-style-type:circle">Cải thiện độ ổn định trong điều kiện taxi.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8078-ba6d-ffcac40f2023" class="bulleted-list"><li style="list-style-type:circle">Tăng cường an toàn và tối ưu tiêu hao điện năng.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-8000-9ac2-cf54298136cf" class="numbered-list" start="1"><li><strong>Đầu mối hỗ trợ kỹ thuật</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8070-bfb0-cc2ddc900da8" class="bulleted-list"><li style="list-style-type:disc">Baojun bố trí đầu mối kỹ thuật chuyên trách hỗ trợ Unipower:<div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-805e-9bb0-f4541258d810" class="bulleted-list"><li style="list-style-type:circle">Tiếp nhận và xử lý các trường hợp lỗi nghiêm trọng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-800a-aff0-faaf22bebf5b" class="bulleted-list"><li style="list-style-type:circle">Hỗ trợ phân tích nguyên nhân gốc rễ.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8084-aeae-cccaf1def347" class="bulleted-list"><li style="list-style-type:disc">Thời gian phản hồi ban đầu không quá 4 giờ làm việc kể từ khi nhận thông tin.</li></ul></div><div style="display:contents" dir="auto"><hr id="2adc5e6f-95bd-8032-b1c9-f9bc1c193a19"/></div><div style="display:contents" dir="auto"><h2 id="2adc5e6f-95bd-807d-b17a-ce3ad6f3e6ac" class=""><strong>V. ĐIỀU KHOẢN VỀ KIỂM ĐỊNH VÀ PHỐI HỢP PHÁP LÝ TẠI VIỆT NAM</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-8039-a47e-ee126c903aae" class="numbered-list" start="1"><li><strong>Hỗ trợ công tác đăng kiểm và chứng nhận kiểu loại</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80a4-b6f7-db2eeed9c620" class="bulleted-list"><li style="list-style-type:disc">Baojun cung cấp đầy đủ hồ sơ, tài liệu phục vụ đăng kiểm theo yêu cầu của cơ quan chức năng Việt Nam.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8078-a322-ff3c976bca0f" class="bulleted-list"><li style="list-style-type:disc">Trong trường hợp cơ quan đăng kiểm cần giải trình thêm, Baojun bố trí kỹ sư hoặc đầu mối kỹ thuật phối hợp trả lời.</li></ul></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-805c-85f2-ce4ac48d41b9" class="numbered-list" start="1"><li><strong>Chi phí điều chỉnh kỹ thuật theo yêu cầu đăng kiểm</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8083-9394-fd6c0bf69cc7" class="bulleted-list"><li style="list-style-type:disc">Trường hợp cơ quan đăng kiểm Việt Nam yêu cầu điều chỉnh một số chi tiết kỹ thuật (nhãn cảnh báo, ký hiệu, phần mềm điều khiển đèn, cổng sạc, v.v.):<div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80f5-918e-c562e4a7aed6" class="bulleted-list"><li style="list-style-type:circle">Baojun chịu trách nhiệm thực hiện và chịu chi phí hiệu chỉnh đối với những hạng mục thuộc phạm vi thiết kế, sản xuất của hãng.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2adc5e6f-95bd-80d0-a33b-e9b03dc5b6cc"/></div><div style="display:contents" dir="auto"><h2 id="2adc5e6f-95bd-80e7-88ce-cb96ba8d4f02" class=""><strong>VI. ĐIỀU KHOẢN THƯƠNG MẠI – TÀI CHÍNH</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-8008-b5a6-dd184c1a5dbb" class="numbered-list" start="1"><li><strong>Giấy chứng nhận xuất xứ ưu đãi</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-802e-8002-c1107590ec02" class="bulleted-list"><li style="list-style-type:disc">Mỗi lô xe xuất sang Việt Nam đều phải kèm giấy chứng nhận xuất xứ theo hiệp định thương mại giữa hai nước, nhằm hưởng mức thuế nhập khẩu ưu đãi nhất.</li></ul></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-8013-9a62-c73063db3c1d" class="numbered-list" start="1"><li><strong>Giữ ổn định giá bán trong thời hạn hợp đồng</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8036-83c3-f99e7e48f274" class="bulleted-list"><li style="list-style-type:disc">Baojun cam kết không tăng giá bán xe trong thời hạn hiệu lực của hợp đồng khung, trừ trường hợp hai bên có thỏa thuận điều chỉnh bằng văn bản.</li></ul></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-804d-bd02-e2f784ac8929" class="numbered-list" start="1"><li><strong>Chính sách giá cho thị trường chiến lược</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-801b-a07f-e33a4e8c6dd3" class="bulleted-list"><li style="list-style-type:disc">Baojun công nhận Việt Nam là thị trường ưu tiên tại khu vực và áp dụng mức giá đặc biệt cho các lô xe giai đoạn đầu.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-809a-bd03-d8f4207c5cef" class="bulleted-list"><li style="list-style-type:disc">Không tăng giá đột ngột trong ít nhất 12 tháng đầu kể từ khi giao xe lô đầu tiên, trừ trường hợp bất khả kháng đã được hai bên thống nhất trước.</li></ul></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-802c-9942-f965983f7afc" class="numbered-list" start="1"><li><strong>Tiến độ thanh toán rõ ràng, hạn chế rủi ro cho bên mua</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80b5-a586-e5797faf9216" class="bulleted-list"><li style="list-style-type:disc">Tỷ lệ thanh toán được chia thành các đợt, ví dụ:<div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8059-bf5a-d9d630bd976f" class="bulleted-list"><li style="list-style-type:circle">Đợt 1: thanh toán một phần khi mở chứng từ thanh toán qua ngân hàng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8093-b5aa-ec1decb8a6ca" class="bulleted-list"><li style="list-style-type:circle">Đợt 2: thanh toán phần còn lại khi tàu cập cảng, trước khi thông quan.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-804c-8a03-cc8014857b27" class="bulleted-list"><li style="list-style-type:disc">Không áp dụng hình thức thanh toán 100% trước khi giao hàng.</li></ul></div><div style="display:contents" dir="auto"><hr id="2adc5e6f-95bd-8058-b828-ee1a91f204f5"/></div><div style="display:contents" dir="auto"><h2 id="2adc5e6f-95bd-8060-ac37-c232a41ce9a8" class=""><strong>VII. ĐIỀU KHOẢN VỀ RỦI RO VÀ CHẤT LƯỢNG</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-80c7-92af-e9325b753bff" class="numbered-list" start="1"><li><strong>Xử lý khiếm khuyết kỹ thuật nghiêm trọng (thu hồi xe)</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80f1-8118-d60f8f276a18" class="bulleted-list"><li style="list-style-type:disc">Khi phát hiện lỗi có nguy cơ mất an toàn (liên quan pin, hệ thống điều khiển, phanh, lái…), Baojun có trách nhiệm:<div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80fe-8652-e7e796e8e34e" class="bulleted-list"><li style="list-style-type:circle">Xây dựng phương án khắc phục.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-806b-b587-f75b426b468a" class="bulleted-list"><li style="list-style-type:circle">Thực hiện chương trình kiểm tra, sửa chữa hoặc thu hồi, tuỳ mức độ.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8053-9fb6-d5908163a9bc" class="bulleted-list"><li style="list-style-type:disc">Toàn bộ chi phí liên quan đến phần việc của Baojun do Baojun chịu.</li></ul></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-80d3-9027-df73b31eaa4b" class="numbered-list" start="1"><li><strong>Trách nhiệm về rủi ro trong quá trình vận chuyển</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-807e-a15a-e1e415a0125f" class="bulleted-list"><li style="list-style-type:disc">Baojun chịu trách nhiệm về chất lượng, an toàn xe cho đến khi bàn giao cho bên nhập khẩu tại cảng đến, theo điều kiện giao hàng đã thoả thuận trong hợp đồng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80c1-a6a5-e090fd9469cf" class="bulleted-list"><li style="list-style-type:disc">Hàng hoá phải được mua bảo hiểm vật chất đầy đủ trong suốt quá trình vận chuyển.</li></ul></div><div style="display:contents" dir="auto"><hr id="2adc5e6f-95bd-8039-bb4c-fd74e3e9b20b"/></div><div style="display:contents" dir="auto"><h2 id="2adc5e6f-95bd-80b7-a201-d2535f0b3cc6" class=""><strong>VIII. ĐIỀU KHOẢN VỀ NHÃN MÁC, TIÊU CHUẨN VÀ ĐỐI SOÁT TRƯỚC KHI GIAO HÀNG</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-80ab-b899-dc08dacd2c25" class="numbered-list" start="1"><li><strong>Nhãn phụ tiếng Việt</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80bf-8d74-dd20d6848614" class="bulleted-list"><li style="list-style-type:disc">Baojun cung cấp đầy đủ nội dung để dán nhãn phụ tiếng Việt theo đúng quy định pháp luật Việt Nam về ghi nhãn hàng hoá.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80f3-b2d5-d24bc01f97af" class="bulleted-list"><li style="list-style-type:disc">Trường hợp nhãn phụ được dán tại Việt Nam, Baojun phối hợp cung cấp nội dung, Unipower tổ chức dán; việc sai sót về nội dung do bên nào gây ra, bên đó chịu trách nhiệm.</li></ul></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-809e-97d7-c6129fa97da1" class="numbered-list" start="1"><li><strong>Kiểm tra chất lượng trước khi xếp hàng</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80a1-bec2-fedb4cc762db" class="bulleted-list"><li style="list-style-type:disc">Trước khi bốc xếp lên tàu, Baojun:<div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8027-8514-f0efad196a78" class="bulleted-list"><li style="list-style-type:circle">Ghi nhận hình ảnh tổng thể và chi tiết từng xe.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8032-8213-ff4e117b88f7" class="bulleted-list"><li style="list-style-type:circle">Đối soát số khung, số máy, cấu hình theo đơn đặt hàng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80da-88f9-d50bdcc19d33" class="bulleted-list"><li style="list-style-type:circle">Hoàn thiện biên bản kiểm tra chất lượng trước khi giao hàng.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2adc5e6f-95bd-809d-9fb3-c830c5abb7bd"/></div><div style="display:contents" dir="auto"><h2 id="2adc5e6f-95bd-80d7-9a7a-e17c84c1f725" class=""><strong>IX. ĐIỀU KHOẢN ĐẶC BIỆT KHI NHẬP KHẨU UỶ THÁC</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-8066-a36e-ff8401f69dcd" class="numbered-list" start="1"><li><strong>Hợp đồng ba bên là điều kiện bắt buộc</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80d5-bb7e-e0c0f35a7df7" class="bulleted-list"><li style="list-style-type:disc">Mọi hợp đồng mua bán xe cho thị trường Việt Nam đều phải có sự tham gia của:<div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-804e-88f7-ec48de73fb24" class="bulleted-list"><li style="list-style-type:circle">Baojun (bên bán).</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80d6-a532-cd379b080cd8" class="bulleted-list"><li style="list-style-type:circle">Đơn vị nhập khẩu uỷ thác (bên đứng tên hải quan).</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8092-9872-de0321b5fb53" class="bulleted-list"><li style="list-style-type:circle">Unipower (bên sử dụng, thanh toán cuối cùng).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80bc-b31b-e690296c920f" class="bulleted-list"><li style="list-style-type:disc">Mục đích: bảo đảm quyền lợi của Unipower về giá, kỹ thuật, bảo hành.</li></ul></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-8003-8c0a-e49822b7e93c" class="numbered-list" start="1"><li><strong>Không được tự ý thay đổi nội dung hợp đồng mua bán</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-807f-929f-c4203e1a294d" class="bulleted-list"><li style="list-style-type:disc">Bất kỳ điều chỉnh nào về giá, điều kiện thanh toán, thời gian giao hàng, cấu hình xe… đều phải có văn bản chấp thuận của Unipower.</li></ul></div><div style="display:contents" dir="auto"><ol type="1" id="2adc5e6f-95bd-800b-8631-ee3929bd5ffc" class="numbered-list" start="1"><li><strong>Cung cấp chứng từ song song cho Unipower</strong></li></ol></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-805c-a675-c4b7caa03b0e" class="bulleted-list"><li style="list-style-type:disc">Mọi chứng từ liên quan đến từng lô hàng (hợp đồng, hóa đơn, phiếu đóng gói, vận đơn, chứng nhận xuất xứ, chứng thư xuất xưởng…) phải được gửi cho Unipower đồng thời với bên nhập khẩu uỷ thác, để theo dõi và đối chiếu.</li></ul></div><div style="display:contents" dir="auto"><hr id="2adc5e6f-95bd-80a4-9dcc-df0faa157087"/></div><div style="display:contents" dir="auto"><h3 id="2adc5e6f-95bd-80ff-8bc9-c57235925744" class=""><strong>TÓM TẮT CHO LÃNH ĐẠO</strong></h3></div><div style="display:contents" dir="auto"><p id="2adc5e6f-95bd-80e6-9f4f-fe5d66d78c76" class="">Unipower cần khoá chặt <strong>27 điều khoản trên</strong> khi làm việc với Baojun để bảo đảm:</p></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8039-abea-c46b2dbc1aa9" class="bulleted-list"><li style="list-style-type:disc">Xe phù hợp đầy đủ quy chuẩn kỹ thuật tại Việt Nam.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-80d0-abb0-e4c20f05e3b2" class="bulleted-list"><li style="list-style-type:disc">Tận dụng tối đa ưu đãi thuế, không phát sinh chi phí ẩn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8075-a789-d93adf025e30" class="bulleted-list"><li style="list-style-type:disc">Bảo hành đúng theo điều kiện khai thác taxi cường độ cao.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8092-b7f1-faad7d5bb9ae" class="bulleted-list"><li style="list-style-type:disc">Không phụ thuộc hoàn toàn vào bên nhập khẩu uỷ thác.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8094-8a19-e3fd9012e6fe" class="bulleted-list"><li style="list-style-type:disc">Tránh rủi ro từ chính sách xuất khẩu mới của Trung Quốc sau 2026.</li></ul></div><div style="display:contents" dir="auto"><ul id="2adc5e6f-95bd-8044-be89-f5aad8f011fe" class="bulleted-list"><li style="list-style-type:disc">Hạn chế tối đa rủi ro về kỹ thuật, an toàn và chất lượng dịch vụ.</li></ul></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
