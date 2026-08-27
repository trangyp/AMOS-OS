---
tags: [energy]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Energy OS</title><style>
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
	
</style></head><body><article id="2e2c5e6f-95bd-80d9-b859-d13d2adb51b5" class="page sans"><header><h1 class="page-title" dir="auto">Energy OS</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8059-a1f0-ec107b02685c" class=""><strong>Hệ năng lượng nhà ở thực chất là một bài toán điều phối bốn dòng năng lượng</strong>, không phải là câu chuyện “lắp thêm thiết bị”. Mục tiêu cốt lõi là quyết định mỗi kWh nên đi qua con đường nào để đạt đồng thời ba tiêu chí: rẻ nhất về chi phí vòng đời, bền nhất cho thiết bị, và an toàn nhất cho vận hành dài hạn.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8094-abd0-d97bb62d525e" class=""><strong>Điện dùng ngay (instant consumption)</strong> là dòng năng lượng rẻ nhất tuyệt đối. Điện từ PV hoặc gió đi thẳng vào tải mà không qua bất kỳ tầng lưu trữ nào thì không có tổn hao chuyển đổi, không gây hao mòn pin, và không đòi hỏi hạ tầng lưu trữ bổ sung. Đây là “kWh vàng” của hệ thống, và mọi kiến trúc “max energy – min cost” đều phải ưu tiên tối đa tự tiêu thụ tức thời. Nguyên tắc thiết kế rất đơn giản nhưng mang tính quyết định: inverter và MARINA luôn phải kiểm tra tải trước tiên; nếu đang có tải, điện phải đi thẳng vào tải, không vòng qua pin và tuyệt đối không vòng qua hydrogen.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8059-8b71-f5b7b2408210" class=""><strong>Pin (daily storage)</strong> là động cơ kinh tế của toàn hệ thống. Pin xử lý bài toán chuyển điện từ ban ngày sang ban đêm, xử lý peak tải và cung cấp khả năng phản ứng cực nhanh ở thang thời gian mili-giây đến giây, giúp ổn định điện áp và bảo vệ thiết bị. Với chu kỳ ngày–đêm, pin có chi phí trên mỗi kWh hữu dụng thấp nhất và hiệu suất cao. Tuy nhiên pin không phù hợp cho lưu trữ nhiều ngày do chi phí tăng nhanh và hao mòn theo chu kỳ sâu. Vì vậy pin không phải là bảo hiểm dài ngày mà là công cụ kinh tế ngắn hạn, và phải được vận hành t
rong một dải SOC hợp lý (ví dụ 25–85%), luôn được ưu tiên hơn hydrogen và không bao giờ được dùng như một bể tích dư vô hạn.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8049-8a1f-e17c93e8ec98" class=""><strong>Hydrogen (long-duration storage)</strong> tồn tại để giải quyết bài toán mà pin không kinh tế: lưu trữ nhiều ngày hoặc nhiều tuần, và hấp thụ phần điện dư khi pin đã “đủ”. Hydrogen có hiệu suất vòng đời thấp hơn pin, nhưng lại trở nên rẻ hơn khi quy đổi theo số ngày tự chủ, không bị hao mòn chu kỳ như pin, và scale theo thời gian lưu trữ tốt hơn so với pin. Vì vậy hydrogen không cạnh tranh với pin mà bổ sung cho pin. Vai trò đúng của S-1000 không phải là chạy hằng ngày hay thay thế pin, mà là bể ăn điện dư và lớp bảo hiểm năng lượng dài ngày. Nguyên tắc vận hành cứng là hydrogen chỉ được kích hoạt khi pin đã đạt SOC cao và nguồn điện dư ổn định; hydrogen không bao giờ được phép giành điện với pin.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-803f-a5b4-ce7a02d37578" class=""><strong>Lưới điện (grid fallback)</strong> không phải là trung tâm của hệ, cũng không phải là đối tượng đối đầu. Lưới là điểm tựa an toàn, dùng để bù khi thiếu hoặc làm tham chiếu chi phí nếu có biểu giá theo thời gian. Trong một hệ tối ưu, lưới chỉ cấp điện khi pin xuống dưới ngưỡng an toàn hoặc khi chi phí lưới rẻ hơn các lựa chọn khác, và không được dùng để chạy electrolyzer trong các gói nhà ở đại trà.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8028-bd4a-e2f025ff0ec5" class=""><strong>KP</strong>in là động cơ kinh tế xử lý chu kỳ ngắn hạn, hydrogen là bảo hiểm dài ngày và bể hấp thụ điện dư, lưới là điểm tựa cuối cùng, còn MARINA là não điều phối đảm bảo mỗi kWh tại mọi thời điểm luôn đi qua con đường rẻ nhất, bền nhất và an toàn nhất.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-805e-90f4-e5367f83e9f5" class="">
</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80a7-9f15-d37050d8414f" class="">
</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8025-81da-c3c8effb8aaf" class="">
</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-806e-ad3a-d43d8417cafd" class="">
</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8062-9a40-c6e35ed97749" class="">
</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8076-a131-d9d7179679b3" class="">
</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8084-85ae-f7ed50104638" class=""><strong>Chân lý kinh tế </strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8027-8f5e-f695ddbaebe4" class="bulleted-list"><li style="list-style-type:disc"><strong>PV + Battery</strong> luôn là “xương sống” rẻ nhất cho hộ gia đình.</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80cd-92ed-ed2117a15b58" class="bulleted-list"><li style="list-style-type:disc"><strong>Wind nhỏ (home turbine)</strong> chỉ hiệu quả khi <strong>địa điểm có gió sạch</strong>; nếu không, nó thành “máy tạo chi phí bảo trì”.</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b5-a515-e37b94f5591a" class="bulleted-list"><li style="list-style-type:disc"><strong>Hydrogen (electrolyzer S-1000)</strong> nên dùng như:<div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8040-a0c6-f351429cac66" class="numbered-list" start="1"><li><strong>bể chứa dư năng lượng</strong> (surplus sink) khi pin đã đầy</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8029-bc62-dfdacb8c012d" class="numbered-list" start="2"><li><strong>dự phòng dài ngày</strong> (long-duration backup)<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80e7-aa99-d0284d94b3bc" class="">❌ không nên dùng để “chạy hằng ngày thay pin” (vì hiệu suất vòng đời thấp hơn pin).</p></div></li></ol></div></li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-800b-9f15-fe06a660bc83" class="">=&gt; Hệ tối ưu chi phí sẽ là <strong>Hybrid 2 tầng lưu trữ</strong>:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-808c-ba6a-c943c10f1fe9" class="bulleted-list"><li style="list-style-type:disc"><strong>Battery = ngắn hạn / daily</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b2-9da9-c495303f555e" class="bulleted-list"><li 
tyle="list-style-type:disc"><strong>H₂ = dài hạn / khi dư hoặc khi mất điện kéo dài</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8045-ba57-dcf4cc2f390a"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-8044-a405-c4f109c6e780" class=""><strong>2) Hai gói sản phẩm (SKU) – chốt lại thành “đóng gói được”</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-805c-a547-fdd21dd2d4c8" class=""><strong>SKU A — MASS (Rẻ nhất, đại trà)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80b9-aebc-fe7f6ed4dcfe" class=""><strong>Mục tiêu:</strong> giảm tiền điện + backup nhẹ (grid-tied là chuẩn)</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80a5-8c14-e1df2b5c1213" class=""><strong>Thành phần:</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a4-8ad4-c59530f8971a" class="bulleted-list"><li style="list-style-type:disc">PV (mái nhà)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b2-8ff1-c1156a18fbff" class="bulleted-list"><li style="list-style-type:disc">Battery (daily shift)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8028-b8ff-d65711eb16cf" class="bulleted-list"><li style="list-style-type:disc"><strong>S-1000 (1 máy)</strong> chỉ chạy khi dư</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80df-be85-c8ea1fd33a7e" class="bulleted-list"><li style="list-style-type:disc"><strong>MARINA IoT + App</strong> điều phối + giám sát + cảnh báo</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8061-a1e2-f729aedc0e04" class="bulleted-list"><li style="list-style-type:disc">(Tuỳ chọn wind nếu “đủ chuẩn gió” – xem mục 3)</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80e4-a128-c3b8e290ab86" class=""><strong>Lời hứa bán hàng đúng:</strong></p></div><div s
tyle="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8063-b357-d482c0353d36" class="bulleted-list"><li style="list-style-type:disc">“Giảm hoá đơn + có lớp dự phòng thêm.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80be-a441-e447cf5a59e4" class="bulleted-list"><li style="list-style-type:disc">“Hydrogen dùng để tích phần dư và dự phòng, không phải thay pin.”</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80ba-b6e2-f99449318c05"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80b5-8209-ce93e3dff60a" class=""><strong>SKU B — RESILIENCE / COASTAL (Premium, off-grid / chịu mất điện dài)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8020-ad88-fae0e59e8a0e" class=""><strong>Mục tiêu:</strong> tự chủ nhiều ngày (đặc biệt vùng biển/đảo/xa)</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80fa-9c1e-cc2b32d0dfab" class=""><strong>Thành phần:</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8031-b95f-d4f0042a5116" class="bulleted-list"><li style="list-style-type:disc">PV lớn hơn</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80eb-b717-dd549626e4fb" class="bulleted-list"><li style="list-style-type:disc">Wind <strong>bắt buộc phải site-qualify</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8056-a476-d419672aedda" class="bulleted-list"><li style="list-style-type:disc">Battery lớn hơn (đỡ shock tải, phản ứng nhanh)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ce-84a5-c8a7a4abf06d" class="bulleted-list"><li style="list-style-type:disc"><strong>Nhiều S-1000</strong> (mô-đun hoá theo nhu cầu)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ae-a174-f74d0e39d217" class="bulleted-list"><li style="list-style-type:disc">H₂ storage “tính theo ngày”</li></ul></div><div s
tyle="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ed-bcb2-c55eef38a8df" class="bulleted-list"><li style="list-style-type:disc">MARINA + app/cloud để điều phối toàn bộ (đây là “não”)</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-809f-b81f-ff78b8caac4f" class=""><strong>Lời hứa bán hàng đúng:</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8077-9526-c33d84e41293" class="bulleted-list"><li style="list-style-type:disc">“Hybrid generation + dual storage (battery + hydrogen) cho tự chủ dài ngày.”</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8037-a645-eca69bcc5d0d"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-80f3-aa45-ddcb4f38f3dc" class=""><strong>3) Quy tắc chọn Wind (nếu không có dữ liệu thì phải có “gate”)</strong></h1></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8087-b952-fff52c2f88a9" class="">Bạn muốn mass market → phải có <strong>điều kiện vào cửa</strong> rất cứng. Nếu không, tỉ lệ fail cao.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8090-9e6d-ea993b78eb17" class=""><strong>Wind “được phép vào hệ”</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80cf-a18c-c0c956411dd1" class="">Chỉ đưa turbine vào nếu <strong>tối thiểu</strong> đạt 2/3 điều kiện:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80e6-b8e9-d55e3a233a6c" class="numbered-list" start="1"><li>Nhà ở <strong>vùng biển / trống trải / đồi cao</strong>, ít vật cản</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-806f-a4fe-ff72c41f4427" class="numbered-list" start="2"><li>Có khả năng lắp turbine đủ cao để “thoát nhiễu” (không bị cây/nhà quật gió)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-801b-ac6d-de10edf0fcf6" class="numbered-list" start="3"><li>Chấp nhận tiếng ồn / rung / bảo trì đ
ịnh kỳ</li></ol></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8038-8012-d83069aeb039" class="">Nếu không đạt → <strong>SKU A bỏ turbine</strong>, chỉ PV + battery + S-1000.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-806f-af3c-cdbacba58cb4"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-800f-a8fb-f9d6a48dba90" class=""><strong>4) Tech stack bạn đang có: S-1000 + MARINA (đặt đúng vai)</strong></h1></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-807b-a266-f693334c1885" class="">Theo bộ spec/pitch:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-806a-b501-e04666ddc745" class="bulleted-list"><li style="list-style-type:disc"><strong>S-1000 / W-1000</strong> là electrolyzer công suất khoảng 1kW, mô-đun hoá, có lớp bảo vệ/giám sát vận hành; hệ thống đi kèm các thành phần lọc/sấy và bảo vệ vận hành.</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-802a-86d6-d4b882ab379a" class="bulleted-list"><li style="list-style-type:disc"><strong>MARINA IoT</strong> + app là lớp điều khiển/giám sát thiết bị và trạng thái vận hành (hướng “device management”).</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-802c-972d-cd5f07637d49" class="">=&gt; Trong “nhà ở”, vai của MARINA phải nâng cấp thành:</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80a1-8bbd-d9ec8808a94e" class=""><strong>Energy Dispatch Controller</strong> (điều phối nguồn–pin–electrolyzer), không chỉ “monitor máy”.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-805b-a71e-d0e65f066152"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-8008-b573-c51612c44f72" class=""><strong>5) Logic điều phối (đây là phần làm hệ “min cost”)</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80d2-9ac1-f9eb7823ec8f" class=""><strong>Logic cho SKU A (Mass – min c
ost)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8084-b699-c131e7715958" class=""><strong>Mục tiêu:</strong> dùng năng lượng rẻ nhất trước, kéo dài tuổi pin, hydrogen chỉ ăn phần dư.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-800f-aa83-d8e3ba609cb5" class=""><strong>Ưu tiên:</strong></p></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80ec-ba59-c4386d9760e7" class="numbered-list" start="1"><li>PV → tải nhà (instant self-consumption)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8007-9701-c103b33b37df" class="numbered-list" start="2"><li>PV → sạc pin tới SOC mục tiêu</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80af-b133-c09ad62233a1" class="numbered-list" start="3"><li>Nếu pin đủ cao + PV còn dư → bật S-1000 (ăn surplus)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8093-9cf7-cbde9b4b9095" class="numbered-list" start="4"><li>Nếu PV yếu / tối → pin cấp tải</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8092-88ac-c76a5b81b758" class="numbered-list" start="5"><li>Grid chỉ bù khi pin xuống ngưỡng thấp (tuỳ cấu hình)</li></ol></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80e1-982a-fb349d10a465" class=""><strong>Ngưỡng SOC gợi ý (để pin bền và vẫn có backup):</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8022-af22-e3550cc68bd3" class="bulleted-list"><li style="list-style-type:disc">SOC_MIN: 20–30%</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-804c-a48f-dd83d82bc445" class="bulleted-list"><li style="list-style-type:disc">SOC_TARGET: 70–90% (tuỳ chiến lược)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8054-80f2-da6b4466bdbe" class="bulleted-list"><li style="list-style-type:disc">Chỉ chạy electrolyzer 
hi SOC &gt; 85–90% và PV dư ổn định X phút.</li></ul></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8028-b70b-d17b9f911cc4" class=""><strong>Logic cho SKU B (Resilience – chịu dài ngày)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8066-a541-df2a31970155" class=""><strong>Mục tiêu:</strong> luôn giữ “response reserve” trên pin, dùng H₂ cho dài hơi.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8085-8f3b-ffe1ed98414e" class=""><strong>Ưu tiên:</strong></p></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80e9-90bf-df2f59e881c0" class="numbered-list" start="1"><li>PV/Wind → tải</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80a9-b927-fde8211c5650" class="numbered-list" start="2"><li>Duy trì pin trong “band” (ví dụ 40–80%) để pin không bị kiệt + sẵn phản ứng tải đột biến</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8097-ae84-d7ab5cb7acdc" class="numbered-list" start="3"><li>Khi dư → chạy nhiều S-1000 theo bậc (1 máy → 2 máy → …)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8035-9140-eff40eb3b715" class="numbered-list" start="4"><li>Khi thiếu kéo dài → ưu tiên pin cho tải nhạy (đèn, internet, lạnh), H₂ dùng cho tải dài/hệ thống dự phòng</li></ol></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8090-8748-e333a296bea0"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-80f7-bdeb-d61d5e646260" class=""><strong>6) Sizing “không cần dữ liệu vẫn triển khai được” (template)</strong></h1></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80cb-981f-e7717ee1aecf" class="">Vì bạn chưa có số liệu nhà, mình đưa ra 3 profile phổ biến để bạn chọn làm baseline:</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-800b-813e-d35a1592c87d" class=""><strong>Profile P1 — Nhà nhỏ / tiết k
iệm</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e1-8c59-d1a3d13474a4" class="bulleted-list"><li style="list-style-type:disc">10–15 kWh/ngày, peak 3–5 kW<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80c8-8f1d-c2c178badf0a" class=""><strong>Gợi ý:</strong> PV 3–5 kW | Battery 5–10 kWh | S-1000 x1</p></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80a4-bbce-d12a8e69202a" class=""><strong>Profile P2 — Nhà trung bình (phổ biến nhất)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a4-b679-eef7eea1c485" class="bulleted-list"><li style="list-style-type:disc">20–35 kWh/ngày, peak 5–10 kW<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-800d-8f45-ef19d0ca7dcf" class=""><strong>Gợi ý:</strong> PV 6–10 kW | Battery 10–20 kWh | S-1000 x1 (SKU A) / x2–4 (SKU B)</p></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80c1-b0b6-d72e93b65c86" class=""><strong>Profile P3 — Nhà lớn / nhiều thiết bị</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8022-9104-e5969aab61ea" class="bulleted-list"><li style="list-style-type:disc">40–70+ kWh/ngày, peak 10–20 kW<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80aa-980b-e3f297276ce8" class=""><strong>Gợi ý:</strong> PV 10–15+ kW | Battery 20–40 kWh | S-1000 x2–8 (tuỳ autonomy)</p></div></li></ul></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-80b1-8723-d19489780bb6" class="">Điểm mấu chốt:<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80d3-bb3d-faadfe377355" class=""><strong>Battery sizing theo “ngày/đêm”</strong></p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80fd-b884-c990530ee3db" class=""><strong>H₂ sizing theo “ngày mất điện”</strong></p></div></blockquote></div><div style="display:contents" dir="auto"><hr i
d="2e2c5e6f-95bd-80f4-84b1-e7380daba9ea"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-8078-aea1-fdb02f61045a" class=""><strong>7) BOM dạng module (để bạn biến thành sản phẩm bán được)</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8060-b0b6-f7b35da5796d" class=""><strong>Module 1 — Generation</strong></h2></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-807d-932c-dd66981f41ea" class="bulleted-list"><li style="list-style-type:disc">PV array + inverter (hybrid inverter ưu tiên)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b7-aed7-f88d5dc8cdca" class="bulleted-list"><li style="list-style-type:disc">(Optional) wind turbine + controller</li></ul></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8004-b8ed-d07149f83838" class=""><strong>Module 2 — Daily Storage</strong></h2></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d7-8fc4-cb16c057acc7" class="bulleted-list"><li style="list-style-type:disc">Battery pack + BMS + inverter/charger (nếu không chung inverter)</li></ul></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-807f-a6d1-c747787829a2" class=""><strong>Module 3 — Hydrogen Layer (theo spec IKONOMY)</strong></h2></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80de-95a1-ca5978ebcb25" class="bulleted-list"><li style="list-style-type:disc">S-1000 electrolyzer (1…n)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f9-ad6b-d629ce298377" class="bulleted-list"><li style="list-style-type:disc">H₂ drying/filtration (nếu đã tích hợp theo cấu hình)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80fd-88a7-d3eb0f6235da" class="bulleted-list"><li style="list-style-type:disc">Storage + regulator + safety valves (đây là phần cần thiết kế chuẩn hoá theo thị trường)</li></ul></div><div style="display:contents" dir="auto"><ul i
d="2e2c5e6f-95bd-8047-94ee-c6dd5dd298d6" class="bulleted-list"><li style="list-style-type:disc">Option: fuel cell / generator (tuỳ gói)</li></ul></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8098-a103-c2de21ec1e14" class=""><strong>Module 4 — Brain (MARINA)</strong></h2></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8046-b600-cb5baa41a781" class="bulleted-list"><li style="list-style-type:disc">MARINA gateway</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-804c-b66b-f96485da6ba0" class="bulleted-list"><li style="list-style-type:disc">App control + logging + alarms</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d9-92e1-fcecc93136f6" class="bulleted-list"><li style="list-style-type:disc">Cloud (nếu có)</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-807e-8741-e6f9f3c913bd"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-806c-b3a5-ff2328fda6b3" class=""><strong>8) Điểm rủi ro lớn nhất (và cách “min cost” đúng nghĩa)</strong></h1></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8035-8055-fcbde695be15" class=""><strong>Rủi ro #1:</strong> bán wind cho sai địa điểm → fail, bảo trì, tiếng ồn, khách quay xe.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8081-b405-f2a5ec6f13b9" class="">→ Giải pháp: <strong>Wind gate</strong> cực cứng + chỉ bán wind ở SKU B hoặc “đủ chuẩn”.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80ec-831a-c55e8092d001" class=""><strong>Rủi ro #2:</strong> nói hydrogen “thay pin” → sai kinh tế, sai kỳ vọng.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80d2-b299-c8c1cc75838b" class="">→ Giải pháp: định vị hydrogen là <strong>surplus + multi-day backup</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8002-bf5b-f92b8c804be6" class=""><strong>Rủi ro #3:</strong> thiếu d
ispatch logic → hệ chạy ngu, tốn điện, pin mau hỏng.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80d9-8b01-d91c420d2cfb" class="">→ Giải pháp: MARINA phải có <strong>rule-set điều phối</strong> như mục 5.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80f2-98d6-ef13fc64ae2b"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-8047-9481-c6f811d100f6" class=""><strong>9) Bạn muốn “đi sâu” tiếp theo hướng nào?</strong></h1></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8050-9991-f4d9d66e84ae" class="">Chọn 1 (mình sẽ làm ngay theo hướng đó):</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8068-867d-ee10e2b2a08b" class="numbered-list" start="1"><li><strong>Thiết kế SKU A hoàn chỉnh</strong>: cấu hình, logic, câu chữ bán hàng, scope lắp đặt, checklist nghiệm thu</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-802c-b065-f58fd4ade815" class="numbered-list" start="2"><li><strong>Thiết kế SKU B hoàn chỉnh</strong>: autonomy theo ngày, bậc scale S-1000, kịch bản outage</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-805b-b1ff-e924e32dc234" class="numbered-list" start="3"><li><strong>Thiết kế “Energy OS” cho MARINA</strong>: state machine + ngưỡng + alarms + dashboard</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8097-afcc-e3adba231366" class="numbered-list" start="4"><li><strong>Cost model khung</strong>: CAPEX/OPEX, điểm hoà vốn, khi nào H₂ đáng tiền</li></ol></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80e2-bc69-e1ae20d07e78" class="">Nếu bạn không chọn, mình sẽ mặc định làm <strong>(1) + (3)</strong> vì đó là “mass market + hệ điều phối” = leverage lớn nhất.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-800d-90cb-cd97c5885bd5" class="">Ok. Mình sẽ “đi sâu” theo đúng nghĩa <strong>thiết k
ế hệ thành sản phẩm có thể bán/triển khai</strong>: <strong>Energy OS (logic điều phối)</strong> + <strong>chuẩn hoá module</strong> + <strong>sizing không cần dữ liệu</strong> + <strong>các chế độ vận hành</strong> + <strong>gate gió</strong> + <strong>cơ chế an toàn</strong> — và tất cả vẫn bám vào stack bạn đã có: <strong>S-1000 + MARINA + app/cloud</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80bf-b0b9-efbb2881f106"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80c6-8aba-cba6c2292ccb" class=""><strong>1) “Max energy – Min cost” thực ra là bài toán tối ưu dòng năng lượng</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-806d-abb0-fc8c2be5287d" class="">Hệ nhà ở có 4 dòng năng lượng cần điều phối:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8002-bfb8-e1654543ecbb" class="numbered-list" start="1"><li><strong>Instant consumption</strong> (điện dùng ngay) – rẻ nhất, không thất thoát</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-804c-ab21-c4392771f287" class="numbered-list" start="2"><li><strong>Daily storage</strong> (Battery) – chi phí/kWh tốt nhất cho chu kỳ ngày/đêm</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80b4-b052-d48a391fce7c" class="numbered-list" start="3"><li><strong>Long-duration storage</strong> (Hydrogen) – đắt hơn theo hiệu suất, nhưng rẻ hơn nếu bạn cần <strong>nhiều ngày dự phòng</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80de-ba4f-e6e3ea023b74" class="numbered-list" start="4"><li><strong>Grid fallback</strong> – rẻ hay đắt tùy biểu giá, nhưng là “điểm tựa”</li></ol></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80eb-a2d1-ca53861f091c" class=""><strong>Kết luận kiến trúc:</strong></p></div><div style="display:contents" dir="auto"><ul i
d="2e2c5e6f-95bd-8063-a0ad-fbbd0fe8b0d3" class="bulleted-list"><li style="list-style-type:disc">Battery là “động cơ kinh tế”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8065-83b8-e2598c1b5492" class="bulleted-list"><li style="list-style-type:disc">Hydrogen là “bảo hiểm dài ngày + bể ăn dư”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f0-9cbf-f0affad4b67f" class="bulleted-list"><li style="list-style-type:disc">MARINA là “não điều phối”</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80af-a921-cbd57d05825d"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80a5-af3e-f147597afe56" class=""><strong>2) Thiết kế “Energy OS” cho MARINA: State machine (cực quan trọng)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-805c-945f-de71ea569d8f" class="">Nếu không có state machine, hệ sẽ chạy ngu → tốn tiền, pin mau hỏng, hydro sai thời điểm.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80d9-bc16-f46d715ddbf1" class=""><strong>Các biến trạng thái tối thiểu (MARINA phải đọc/nhận)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80db-b629-da300a90ba07" class="bulleted-list"><li style="list-style-type:disc">PV power (P_pv), Wind power (P_wind – nếu có)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8016-a759-d1809f26d7ee" class="bulleted-list"><li style="list-style-type:disc">Load power (P_load)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8009-8d18-e5310f7fd07c" class="bulleted-list"><li style="list-style-type:disc">Battery SOC, Battery charge/discharge power, nhiệt độ pin</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f7-8f3a-d2bcaa4d8c12" class="bulleted-list"><li style="list-style-type:disc">Grid status (on/off), grid price mode (optional)</li></ul></div><div s
tyle="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80eb-97cd-f5f4a0692a7f" class="bulleted-list"><li style="list-style-type:disc">Electrolyzer status: on/off, input power, H₂ flow/production, lỗi (OV/UV/OC/OT/pressure…)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80db-8241-f63b40532eba" class="bulleted-list"><li style="list-style-type:disc">Hydrogen tank pressure/level (bắt buộc nếu muốn bán “resilience”)</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8047-8da8-d1b9efbebf14" class=""><strong>Các trạng thái vận hành cốt lõi</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80fd-8a3c-f91c92995290" class=""><strong>S0 – SAFE/IDLE</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ad-8795-d7ffe909150f" class="bulleted-list"><li style="list-style-type:disc">mặc định khi không có dư năng lượng, hoặc hệ đang lỗi/safety hold</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8072-b173-c9d902ca878d" class=""><strong>S1 – SELF-CONSUME</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8024-98bb-fea3d8cb3b31" class="bulleted-list"><li style="list-style-type:disc">PV/Wind cấp tải trực tiếp (ưu tiên số 1)</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8009-9098-d861f73eb74a" class=""><strong>S2 – BATTERY CHARGE</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ff-894d-e85171a8cab7" class="bulleted-list"><li style="list-style-type:disc">khi còn dư: sạc pin đến SOC_target</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-803f-afa2-da47ba923574" class=""><strong>S3 – SURPLUS→H2</strong> (đây là nơi S-1000 phát huy)</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80aa-a67f-d3af8eb7a7fa" class="bulleted-list"><li style="list-style-type:disc">chỉ kích hoạt khi: SOC &gt; SOC_H2_START và 
ư ổn định (không “nhấp nháy”)</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8040-b343-f80ea465b4f4" class=""><strong>S4 – BATTERY DISCHARGE</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e1-b7b1-c76d966ba5f2" class="bulleted-list"><li style="list-style-type:disc">khi thiếu: pin cấp tải đến SOC_min</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-807b-b4cf-fa3d89aee0e6" class=""><strong>S5 – OUTAGE MODE (GRID OFF)</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e9-a0f0-d8747bc0621a" class="bulleted-list"><li style="list-style-type:disc">ưu tiên tải thiết yếu + giữ SOC “response reserve”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c1-b5d7-e6d7cece1573" class="bulleted-list"><li style="list-style-type:disc">hydro chỉ dùng cho dài ngày (đúng cách)</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-802c-ae43-d0ec0d46521f" class=""><strong>S6 – FAULT / SAFETY HOLD</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8090-be88-e492bc70fece" class="bulleted-list"><li style="list-style-type:disc">nếu có bất kỳ lỗi safety → ngắt electrolyzer, đưa về safe, cảnh báo</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-802f-91c6-ee0b7c04a374" class=""><strong>Điều kiện chuyển trạng thái (logic “min cost”)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-803e-af94-fc60a2e48928" class="bulleted-list"><li style="list-style-type:disc">Nếu <strong>P_gen = P_pv + P_wind</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8085-82df-efec0b4be73d" class="bulleted-list"><li style="list-style-type:disc">Nếu <strong>Surplus = P_gen – P_load</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8004-a5f5-cdbf48d0bf57" class=""><strong>Rule 1 (luôn đ
úng):</strong> phục vụ tải trước</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8078-84b9-e9ac44a907f9" class=""><strong>Rule 2:</strong> sạc pin trong band để tối ưu tuổi thọ</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80d5-ac5f-f99b297f4d75" class=""><strong>Rule 3:</strong> chỉ chạy electrolyzer khi pin đã “đủ đầy” + dư ổn định</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-808e-9163-cfb192b7cd98" class=""><strong>Rule 4:</strong> không cho electrolyzer “giành” điện với pin trong giờ thiếu</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80c8-8bdf-c4a906a91281"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-805e-87d4-de3157c8325e" class=""><strong>3) Bộ ngưỡng chuẩn hoá (không cần biết nhà cụ thể vẫn dùng được)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80d4-8899-db56aaea4cf9" class="">Bạn cần ngưỡng default để triển khai mass market.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8063-bb41-ee39fdfe391a" class=""><strong>Ngưỡng SOC gợi ý (Package A – mass)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8028-b04c-cb971d8040c1" class="bulleted-list"><li style="list-style-type:disc">SOC_min = 25% (bảo vệ pin + giữ backup)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e6-bc72-ebc5120e8b68" class="bulleted-list"><li style="list-style-type:disc">SOC_target = 85% (đủ cho tối + peak)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8029-ac3c-d26a5bb86aa6" class="bulleted-list"><li style="list-style-type:disc">SOC_H2_START = 90% (chỉ khi pin gần đầy mới chạy H2)</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80e1-acf3-e8847b9e6cd2" class=""><strong>Anti-flicker (tránh bật/tắt liên tục làm hại hệ)</strong></h3></div><div style="display:contents" dir="auto"><ul i
d="2e2c5e6f-95bd-8006-a565-f35c51f70122" class="bulleted-list"><li style="list-style-type:disc">Điều kiện “dư ổn định”: Surplus &gt; P_electrolyzer + margin trong <strong>5–10 phút</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80cc-8b1e-dce3d61176d4" class="bulleted-list"><li style="list-style-type:disc">Cooldown sau khi tắt: 3–5 phút mới cho bật lại</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8095-ba3f-d72d19ff22ca" class="bulleted-list"><li style="list-style-type:disc">Ramp electrolyzer theo bậc (Package B): 1 máy → 2 máy → 3 máy…</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8046-bd94-fcd3c61e07c8"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80ff-ae13-d480867d8b18" class=""><strong>4) Sizing sâu hơn: cách ra cấu hình mà không cần dữ liệu khách</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-807c-9deb-ded8005e9d4a" class="">Ta dùng 3 “profile tiêu chuẩn” để đóng gói sản phẩm.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8049-bf18-e4a5f6470b43" class=""><strong>Profile P1 (nhỏ)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8083-a8ae-fc8bad46476f" class="bulleted-list"><li style="list-style-type:disc">PV: 3–5 kW</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d4-97f0-c05f2fa8ff7f" class="bulleted-list"><li style="list-style-type:disc">Battery: 5–10 kWh</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8091-a43b-d9f27a2e0fdd" class="bulleted-list"><li style="list-style-type:disc">S-1000: 1 unit (surplus + backup nhẹ)</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80f6-a13a-cbd6103e9d78" class=""><strong>Profile P2 (trung bình – đại trà)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a0-bf8a-e83fe02cb449" c
lass="bulleted-list"><li style="list-style-type:disc">PV: 6–10 kW</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-801a-9904-e76c24c02739" class="bulleted-list"><li style="list-style-type:disc">Battery: 10–20 kWh</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-805d-8da1-cacef4779493" class="bulleted-list"><li style="list-style-type:disc">S-1000: 1 unit (Package A) hoặc 2–4 (Package B)</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80e4-9453-c71d24340b46" class=""><strong>Profile P3 (lớn)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e0-8536-fa84dd4537f9" class="bulleted-list"><li style="list-style-type:disc">PV: 10–15+ kW</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8031-b201-e24ee0a6338a" class="bulleted-list"><li style="list-style-type:disc">Battery: 20–40 kWh</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-803e-a428-fce154f1bf3f" class="bulleted-list"><li style="list-style-type:disc">S-1000: 2–8 units (tùy số ngày autonomy)</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8039-bfc2-c5ae190e72fe" class=""><strong>Quy tắc sizing đúng bản chất:</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b2-a607-ffd28e6a58e8" class="bulleted-list"><li style="list-style-type:disc">Battery (kWh) ~ 0.3–0.8 × điện tiêu thụ/ngày (tuỳ mục tiêu)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8034-8af8-d6e6ca83f824" class="bulleted-list"><li style="list-style-type:disc">Hydrogen storage = “số ngày muốn sống” × “mức tải thiết yếu mỗi ngày”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80bd-9013-c8884845df96" class="bulleted-list"><li style="list-style-type:disc">Electrolyzer count = tốc độ bạn muốn nạp hydro trong điều kiện dư điện thực tế (phụ thuộc P
V/wind)</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80f6-a1ef-c85dd28e248f"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80d6-b4ed-c9b16c661af3" class=""><strong>5) Gate gió (đi sâu hơn để giảm fail rate)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-801d-9c4d-ff43e70b093b" class="">Turbine nhỏ mà lắp sai chỗ là chết sản phẩm.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80ad-a8f8-fe2f57d433e3" class=""><strong>Wind qualification cấp độ sản phẩm (3 lớp)</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8058-ad1b-fdd12fc2ea4b" class=""><strong>W0 – Không đạt (default):</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-805b-8e07-c9192eec1338" class="bulleted-list"><li style="list-style-type:disc">đô thị/suburban nhiều vật cản → không bán wind</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8002-bf47-d13c050f4f46" class=""><strong>W1 – Có thể (có điều kiện):</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8087-8e44-d203ed2bb96f" class="bulleted-list"><li style="list-style-type:disc">khu trống, ít cản, có chỗ nâng hub height</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8000-8a72-ec677cafb402" class="bulleted-list"><li style="list-style-type:disc">vẫn phải ký cam kết tiếng ồn/bảo trì</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80cb-936a-f6a20882f7cf" class=""><strong>W2 – Lý tưởng (đáng tiền):</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-805f-8a5e-f7ac5acf5ee2" class="bulleted-list"><li style="list-style-type:disc">ven biển/đảo/đồi, gió đêm đều</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8070-ac79-da1e37aad2a9" class="bulleted-list"><li style="list-style-type:disc">đây là nơi Package B tạo khác b
iệt thật</li></ul></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-80ec-8249-c7e6de8a3198" class="">Nếu bạn muốn mass market, hãy coi wind là<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80d9-a8d0-d1574b648241" class=""><strong>option hiếm</strong></p></div></blockquote></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80f0-858f-c3ae238532c1"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8097-a3d4-f28f45f38bd3" class=""><strong>6) Thiết kế lớp Hydrogen cho HOME (đúng, an toàn, bán được)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-805f-9b37-f108bdc6c5d9" class="">Trong nhà ở, hydro không được “mơ hồ”. Phải đóng thành module rõ ràng.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8026-92cb-c56c785e883f" class=""><strong>Module H2 tối thiểu gồm:</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8061-b9f5-cd4233e06264" class="numbered-list" start="1"><li><strong>S-1000 electrolyzer</strong> (1…n)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-809e-98f2-c156acedacb9" class="numbered-list" start="2"><li><strong>Drying/filtration + safety chain</strong> (theo cấu hình đi kèm thiết bị)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80b4-a718-cc0205521cbf" class="numbered-list" start="3"><li><strong>Storage</strong> (bình/giải pháp lưu trữ) + cảm biến áp suất</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80a2-82b3-c55f839c989a" class="numbered-list" start="4"><li><strong>Regulator + relief + shutoff valve</strong> (tự động)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-801f-b120-de9b69dc2113" class="numbered-list" start="5"><li><strong>H2 detector + ventilation requirement</strong> (đây là điều kiện để hệ được phép tồn tại trong 
hà)</li></ol></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8047-b000-d2b126eb9736" class=""><strong>Cách dùng hydro đúng (không đốt hiệu suất)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8052-bb58-d41f13db8b86" class="bulleted-list"><li style="list-style-type:disc">Không dùng hydro để “tối nào cũng chạy”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a6-a59e-e9cd952a6560" class="bulleted-list"><li style="list-style-type:disc">Dùng hydro khi:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-804b-8f17-d660aae06412" class="bulleted-list"><li style="list-style-type:circle">pin xuống dưới band nhưng dự báo thời tiết xấu nhiều ngày</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8015-806d-d494172b543c" class="bulleted-list"><li style="list-style-type:circle">mất điện dài</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80cb-b5e1-ca49d302850b" class="bulleted-list"><li style="list-style-type:circle">có dư điện lớn kéo dài (PV nhiều, tải thấp)</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80c6-8f67-f37d34cf3edc"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-806b-863f-ccc95869785b" class=""><strong>7) Package A &amp; B: đóng gói thành “cam kết vận hành” (cực quan trọng để bán)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8053-8180-fab45989da2a" class=""><strong>Package A (Mass) – Cam kết</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8025-bf23-d678e24dbcf8" class="bulleted-list"><li style="list-style-type:disc">Giảm tiền điện nhờ tự tiêu thụ + pin</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80cc-84af-eb27a1a645af" class="bulleted-list"><li style="list-style-type:disc">H2 chỉ là “bể ăn dư_toggle” + dự phòng hạn chế</li></ul></div><div s
tyle="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f0-a96b-c504ea2c7567" class="bulleted-list"><li style="list-style-type:disc">Ít bảo trì (vì wind thường không bán)</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8016-a90b-f37ab1d0f234" class=""><strong>Package B (Resilience) – Cam kết</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8031-8895-e68a47997d71" class="bulleted-list"><li style="list-style-type:disc">Vận hành trong mất điện dài ngày theo “load tiering”:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-800f-9c81-f4ebd10c2da8" class="bulleted-list"><li style="list-style-type:circle">Tier 1: thiết yếu (đèn, mạng, tủ lạnh, bơm nhỏ)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8000-ac53-f8ddaee8e9f3" class="bulleted-list"><li style="list-style-type:circle">Tier 2: tiện nghi (điều hoà hạn chế)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d2-a9ac-f623193f472c" class="bulleted-list"><li style="list-style-type:circle">Tier 3: xa xỉ (cắt)</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8027-9b18-dcd74abc7c5b"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-808c-a2c2-e4b0963ed314" class=""><strong>8) Bộ dashboard (app) cần có để system “đáng tiền”</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80c9-a17e-ee8dfe7f9789" class="">App không chỉ show số. Phải show “quyết định của não”.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-808d-ada0-d5d006d6153a" class=""><strong>4 màn hình bắt buộc:</strong></p></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8089-b4a8-e3fbf841bcf3" class="numbered-list" start="1"><li>Energy Flow realtime (PV/Wind → Load/Battery/H2/Grid)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" i
d="2e2c5e6f-95bd-8048-a25b-d165feab3bda" class="numbered-list" start="2"><li>Storage status (SOC + H2 pressure/level + autonomy estimate)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-802a-8c94-d08bc3805c7e" class="numbered-list" start="3"><li>Mode state (S1/S2/S3/Outage…) + lý do chuyển mode</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-803f-be32-d352b73954a2" class="numbered-list" start="4"><li>Alerts + recommended action (bảo trì, safety, lỗi)</li></ol></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80eb-a876-fb2ef1acf6e1" class="">MARINA chính là lớp thu thập + điều phối để làm điều này.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8008-a6f5-e723630c45b2"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80ea-baf3-f90b10e0fc79" class=""><strong>9) Nếu bạn muốn “đi sâu hơn nữa”: mình cần chọn một trục</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-803c-8147-e740d4575b72" class="">Mình có thể đi tiếp theo 1 trong 3 hướng sâu nhất (bạn chỉ cần chọn số):</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8047-97dc-c41516be7ee2" class=""><strong>A) Thiết kế Energy OS chi tiết:</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f1-aaa9-d145016bee2b" class="bulleted-list"><li style="list-style-type:disc">bảng transition đầy đủ, ngưỡng, timers, anti-flicker, ưu tiên tải, outage playbook</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-801c-98f7-c1b04ef72e5a" class=""><strong>B) Thiết kế sản phẩm thương mại:</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8039-82f7-d0a7d8d4086c" class="bulleted-list"><li style="list-style-type:disc">3 profile × 2 packages = 6 cấu hình SKU</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ad-8003-eadde795ae4a" c
lass="bulleted-list"><li style="list-style-type:disc">scope lắp đặt, tiêu chuẩn nghiệm thu, gói bảo trì, điều khoản “wind gate”</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-809a-8f58-df25fa9cdb11" class=""><strong>C) Thiết kế H2 module cho home chuẩn hoá:</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-807f-9c80-c5e15c53e4ec" class="bulleted-list"><li style="list-style-type:disc">kiến trúc an toàn, yêu cầu lắp đặt, điều kiện thông gió/cảm biến, logic shutdown</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80ae-bf14-c2b45ec28ec1" class="">Nếu bạn không chọn, mình sẽ mặc định làm <strong>A (Energy OS)</strong> vì đó là “lõi min cost” và là thứ giúp bạn khác biệt thật.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
