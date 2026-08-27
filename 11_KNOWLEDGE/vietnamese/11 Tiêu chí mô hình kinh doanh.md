---
tags: [vietnamese]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>11 Tiêu chí mô hình kinh doanh</title><style>
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
	
</style></head><body><article id="371c5e6f-95bd-8038-aced-f23c16e790c2" class="page sans"><header><h1 class="page-title" dir="auto">11 Tiêu chí mô hình kinh doanh</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8064-b0d3-ed31fd3088d3" class="">Dưới đây là bản viết lại thành <strong>một công cụ thực hành cho doanh nghiệp nhỏ</strong>, để chủ doanh nghiệp có thể tự điền số liệu, chấm điểm và ra quyết định vận hành. Công cụ này được phát triển từ bộ 3 tầng kiểm duyệt trong tài liệu bạn cung cấp: <strong>Sinh tồn → Vận hành &amp; Tối ưu → Chiến lược &amp; Quy mô</strong>.</p></div><div style="display:contents" dir="auto"><h1 id="371c5e6f-95bd-800d-8e40-f4d796a48e93" class="">SME BUSINESS SURVIVAL TOOL</h1></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-80b0-a249-e59fda75ab11" class="">Công cụ 11 phép tính sinh tồn cho doanh nghiệp nhỏ</h2></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-8020-8abc-e02a097169c3" class="">1. Mục đích của công cụ</h2></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80ab-bff4-e5da791a47cb" class="">Công cụ này giúp chủ doanh nghiệp nhỏ trả lời 3 câu hỏi sống còn:</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8037-9013-c2d9ae7bab4c" class=""><strong>1. Mô hình này có sống được không?</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-804e-86e2-e75b8d005583" class=""><strong>2. Mô hình này có đang vận hành khỏe không?</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-808b-a919-c089c2bcade2" class=""><strong>3. Mô hình này có đủ điều kiện để mở rộng không?</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80d7-b367-d4a0b81c8e39" class="">Không đánh giá bằng cảm giác.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8090-955a-efaf7130f313" class="">Không đánh g
iá bằng “đông khách”.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8017-8a1c-dfdf7eb9875a" class="">Không đánh giá bằng doanh thu bề mặt.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8066-bc1d-d0dbe374b888" class="">Công cụ này đánh giá bằng <strong>số thật, tiền thật, dòng tiền thật và khả năng sống sót thật</strong>.</p></div><div style="display:contents" dir="auto"><hr id="371c5e6f-95bd-80a8-be0f-c2c01aa27456"/></div><div style="display:contents" dir="auto"><h1 id="371c5e6f-95bd-806f-8021-e10b8f5a2780" class="">2. Cách sử dụng công cụ</h1></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80a4-b4f8-eea7ad8a70f5" class="">Mỗi tháng hoặc mỗi quý, chủ doanh nghiệp điền số liệu vào 11 chỉ số dưới đây.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8001-a66e-dcdbf07496ee" class="">Sau đó chấm theo 3 màu:</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80d5-92e0-c0c6823602b4" class="">🔴 <strong>Đỏ</strong>: nguy hiểm, cần xử lý ngay.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80b6-a0d2-c026ccb79e91" class="">🟡 <strong>Vàng</strong>: chưa tối ưu, cần chỉnh trước khi mở rộng.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80b5-bb20-f7c2af508af9" class="">🟢 <strong>Xanh</strong>: khỏe, có thể tiếp tục vận hành hoặc mở rộng.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8007-872b-dcf1d98226ef" class="">Quy tắc quan trọng:</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8068-bb96-d36104c90bee" class="">Nếu có <strong>1 chỉ số đỏ ở tầng sinh tồn</strong>, dừng mở rộng ngay.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8084-80e1-eb7952e35f4f" class="">Nếu tầng sinh tồn xanh nhưng tầng vận hành vàng, tối ưu trước khi scale.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-801c-ac31-e3ad096de84e" class="">Nếu cả 3 t
ầng đều xanh, doanh nghiệp có nền để mở rộng.</p></div><div style="display:contents" dir="auto"><hr id="371c5e6f-95bd-80d4-84d7-d18483985a08"/></div><div style="display:contents" dir="auto"><h1 id="371c5e6f-95bd-80f1-83eb-da2505f3b03a" class="">TẦNG 1: KIỂM TRA SINH TỒN</h1></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-80d1-be7e-f2afe89861ca" class="">Mô hình này có sống được không?</h2></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-8009-a4df-e373a188492b" class="">1. Biên lãi gộp thực tế</h2></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80d2-ba98-cbe004424c1d" class=""><strong>Câu hỏi:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-809b-8d8f-c9f077cb100f" class="">Sau khi bán một sản phẩm/dịch vụ, doanh nghiệp thật sự giữ lại được bao nhiêu tiền?</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-803f-917d-c07e95f139d1" class=""><strong>Công thức:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-806f-a753-efdf3ee849da" class=""><strong>Biên lãi gộp = (Doanh thu – Giá vốn trực tiếp) / Doanh thu × 100%</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-804c-8666-d0125398affe" class=""><strong>Cần điền:</strong></p></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80e7-b501-c1a285dd741a" class="bulleted-list"><li style="list-style-type:disc">Doanh thu:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8019-9ff3-f57a6cb38f46" class="bulleted-list"><li style="list-style-type:disc">Giá vốn trực tiếp:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-809b-8774-f2c29c3b507c" class="bulleted-list"><li style="list-style-type:disc">Biên lãi gộp:</li></ul></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80ee-9e12-d509e1311462" class=""><strong>Chấm điểm:</strong></p></div><div style="display:contents" d
ir="auto"><p id="371c5e6f-95bd-8079-98c4-f3351bdd8a54" class="">🔴 Dưới 20%: mô hình quá mỏng.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8079-a56a-c514e4d68823" class="">🟡 20–50%: sống được nhưng cần kiểm soát chặt.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8000-b419-c4cc990dbc54" class="">🟢 Trên 50%: tốt, có dư địa vận hành và marketing.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80dd-95ff-cf8178c77896" class=""><strong>Quyết định vận hành:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80d2-a8d4-ea2731afdc4a" class="">Nếu biên lãi gộp thấp, không tăng quảng cáo. Trước tiên phải tăng giá bán, giảm giá vốn, tối ưu sản phẩm hoặc đổi phân khúc khách hàng.</p></div><div style="display:contents" dir="auto"><hr id="371c5e6f-95bd-80ee-b963-ddba77e9d576"/></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-8054-89b6-ff28080411a5" class="">2. Áp lực hòa vốn</h2></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-808d-9f0d-e7cb6222c030" class=""><strong>Câu hỏi:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80f8-b9b2-c9595bbd1801" class="">Mỗi tháng phải bán bao nhiêu đơn mới không lỗ?</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8092-947e-fa15d42a2fd3" class=""><strong>Công thức:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8074-bb32-e2c839779d79" class=""><strong>Số đơn hòa vốn = Chi phí cố định / Lãi gộp trung bình mỗi đơn</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8008-857a-f59259dc2914" class=""><strong>Cần điền:</strong></p></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8051-af31-dcdbde33f546" class="bulleted-list"><li style="list-style-type:disc">Chi phí cố định/tháng:</li></ul></div><div style="display:contents" dir="auto"><ul i
d="371c5e6f-95bd-80ac-8f9d-de2448d939d4" class="bulleted-list"><li style="list-style-type:disc">Lãi gộp trung bình mỗi đơn:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8089-a68b-c3ec1580790b" class="bulleted-list"><li style="list-style-type:disc">Số đơn hòa vốn:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8093-ae65-cd6e699d3fa1" class="bulleted-list"><li style="list-style-type:disc">Công suất tối đa/tháng:</li></ul></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8029-820f-e38db6113406" class=""><strong>Chấm điểm:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80d1-b83e-f13fd91b86ee" class="">🔴 Hòa vốn cần trên 70% công suất: quá nguy hiểm.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-807a-8983-f2f817416573" class="">🟡 Hòa vốn cần 40–70% công suất: áp lực trung bình.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80ac-b8bf-cbfe087adda5" class="">🟢 Hòa vốn dưới 40% công suất: vùng an toàn tốt.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8008-a80a-f07e4b3d36d2" class=""><strong>Quyết định vận hành:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-808f-99b1-fcfc205ceba1" class="">Nếu phải bán gần hết công suất mới hòa vốn, doanh nghiệp đang bị định phí đè. Cần giảm mặt bằng, giảm lương cứng, giảm khấu hao hoặc tăng lãi gộp mỗi đơn.</p></div><div style="display:contents" dir="auto"><hr id="371c5e6f-95bd-80a3-960d-c1212ce1dcc0"/></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-80a1-97cc-d87e256a2bd8" class="">3. Trạng thái dòng tiền</h2></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8099-817c-d8036573f68e" class=""><strong>Câu hỏi:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8085-8590-d156111044b3" class="">Doanh nghiệp có tiền thật trong tài khoản không?</p></div><div s
tyle="display:contents" dir="auto"><p id="371c5e6f-95bd-8073-b440-f2bf4c832bcd" class=""><strong>Công thức:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80fa-bceb-e8ed34c53598" class=""><strong>Dòng tiền ròng = Tiền thực thu – Tiền thực chi</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8071-aa16-ec0343dce4c1" class=""><strong>Cần điền:</strong></p></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80db-a42a-cb4bd1e73746" class="bulleted-list"><li style="list-style-type:disc">Tiền thực thu trong tháng:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80c2-88c1-e2d144492224" class="bulleted-list"><li style="list-style-type:disc">Tiền thực chi trong tháng:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80d7-937f-d5845cc2c3e8" class="bulleted-list"><li style="list-style-type:disc">Dòng tiền ròng:</li></ul></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80d8-a05a-c4cffde33bd9" class=""><strong>Chấm điểm:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8087-ba12-cd5c760d3615" class="">🔴 Âm hoặc bằng 0 liên tục 2 tháng/quý: nguy hiểm.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80bc-acb8-f2b88a9aa7fc" class="">🟡 Dương nhưng thất thường: cần kiểm soát công nợ.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-808a-b7fa-f4daefccf396" class="">🟢 Dương đều: khỏe.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80c4-9f71-cac10089b61e" class=""><strong>Quyết định vận hành:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-804c-977a-cce658e09aca" class="">Nếu dòng tiền âm, ưu tiên số 1 là thu hồi công nợ, giảm tồn kho, giảm chi phí cố định, dừng mở rộng và bảo vệ tiền mặt.</p></div><div style="display:contents" dir="auto"><hr id="371c5e6f-95bd-80df-8bd9-ca8a1d395e0e"/></div><div s
tyle="display:contents" dir="auto"><h1 id="371c5e6f-95bd-809e-ae3c-e93442092d6a" class="">TẦNG 2: KIỂM TRA VẬN HÀNH</h1></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-8036-ad67-c4078a39a689" class="">Mô hình này có đang khỏe không?</h2></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-8001-bc1c-e1714e0d7da5" class="">4. Tỷ lệ giá vốn</h2></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8021-98cc-d1120fb112c8" class=""><strong>Câu hỏi:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80a7-9dd4-c8c151036c58" class="">Chi phí tạo ra sản phẩm có đang ăn mòn lợi nhuận không?</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8035-a0e4-cc0b1783d830" class=""><strong>Công thức:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80d2-938a-d20053ab7090" class=""><strong>Tỷ lệ giá vốn = Giá vốn / Doanh thu × 100%</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8049-81a2-d433ba0dac1d" class=""><strong>Cần điền:</strong></p></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80b9-ad6d-f1d5f7fbea5c" class="bulleted-list"><li style="list-style-type:disc">Giá vốn:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8025-890a-c70760c1444d" class="bulleted-list"><li style="list-style-type:disc">Doanh thu:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8047-950d-f6eee9c83c6e" class="bulleted-list"><li style="list-style-type:disc">Tỷ lệ giá vốn:</li></ul></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80b4-b427-f1dc1d9923a1" class=""><strong>Chấm điểm tham khảo:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8043-bf21-c89e14ef98f0" class="">Với F&amp;B:</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80f2-96c0-c13c45edb7ab" class="">🔴 Trên 35%: nguy h
iểm.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8073-a034-cf51b66898f3" class="">🟢 25–30%: tốt.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-801f-9e50-d8f805a87059" class="">Với bán lẻ/thời trang:</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-801b-a381-ce161682d5d9" class="">🔴 Trên 45%: nguy hiểm.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-802b-a675-f18ce5fde598" class="">🟢 25–35%: tốt.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-801a-bb83-de0f73dc326a" class=""><strong>Quyết định vận hành:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80e4-a897-c616cffc0deb" class="">Nếu giá vốn cao, cần đàm phán lại nhà cung cấp, giảm hao hụt, chuẩn hóa định lượng, tăng giá bán hoặc loại bỏ sản phẩm biên lợi nhuận thấp.</p></div><div style="display:contents" dir="auto"><hr id="371c5e6f-95bd-803d-8d2b-fdc0de22d6ed"/></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-803a-aca3-d83b2be4081d" class="">5. Hiệu suất quỹ lương</h2></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80d0-9a48-c0fd51870690" class=""><strong>Câu hỏi:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80f3-8cb2-c44330d75c0f" class="">Nhân sự đang tạo năng suất hay đang làm nặng mô hình?</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8089-bba2-ddd93e4534a4" class=""><strong>Công thức:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80d6-b9bc-c254fff8270c" class=""><strong>Tỷ lệ quỹ lương = Tổng chi phí nhân sự / Doanh thu × 100%</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80ed-b6a2-e7731e1c9ef1" class=""><strong>Cần điền:</strong></p></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8054-8f89-efe4f24ffb54" class="bulleted-list"><li style="list-style-type:disc">Tổng chi phí 
hân sự:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-806c-ac96-c685993b0013" class="bulleted-list"><li style="list-style-type:disc">Doanh thu:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80a3-a63a-fa24176b1735" class="bulleted-list"><li style="list-style-type:disc">Tỷ lệ quỹ lương:</li></ul></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-807a-b3eb-f5e4697f0fd5" class=""><strong>Chấm điểm:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-805c-9a78-f960acd5239e" class="">🔴 Trên 25%: bộ máy nặng.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8075-9696-e086993a27f5" class="">🟡 20–25%: cần tối ưu.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8032-b10c-ea7ea414e59d" class="">🟢 15–20%: tốt.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80a9-b86e-f712c4a50ad4" class=""><strong>Quyết định vận hành:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8076-aba4-e4ce9a7b7ce9" class="">Nếu quỹ lương cao, không tuyển thêm. Cần chuẩn hóa quy trình, gắn KPI với doanh thu/lợi nhuận, tự động hóa việc lặp lại và loại bỏ vị trí không tạo giá trị.</p></div><div style="display:contents" dir="auto"><hr id="371c5e6f-95bd-809f-beec-edf9d3423e3a"/></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-801f-a070-dab3b8abc036" class="">6. Vòng quay hàng tồn kho</h2></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80e1-95db-d4de45df4090" class=""><strong>Câu hỏi:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-803d-95cd-d92df51dc55e" class="">Tiền có đang bị chôn trong kho không?</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80a3-8318-d660a5fb9fbb" class=""><strong>Công thức:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80ec-9428-ea147349596c" c
lass=""><strong>Số ngày tồn kho = Tồn kho trung bình / Giá vốn bán ra mỗi ngày</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8035-acca-c9622195f63b" class=""><strong>Cần điền:</strong></p></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80c3-b31b-d9f1db4a5b6e" class="bulleted-list"><li style="list-style-type:disc">Tồn kho trung bình:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80dd-b0a9-c2932ab411c1" class="bulleted-list"><li style="list-style-type:disc">Giá vốn bán ra mỗi ngày:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8083-8495-f89f7289d13c" class="bulleted-list"><li style="list-style-type:disc">Số ngày tồn kho:</li></ul></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-806d-a779-cf88d587cd9a" class=""><strong>Chấm điểm:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80f9-a268-cdd0aa8aa0d9" class="">🔴 Trên 60 ngày: vốn chết.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80ba-b34c-e2df279b8291" class="">🟡 30–60 ngày: cần kiểm soát.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-808e-b501-dd2c592c98ef" class="">🟢 15–30 ngày: tốt.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80b2-80df-c9255667c061" class="">🟢 Dưới 15 ngày: rất tốt nếu không thiếu hàng.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-807b-a79f-f48bd920ce65" class=""><strong>Quyết định vận hành:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80ea-974b-efc3326f2ff0" class="">Nếu hàng tồn quá lâu, cần xả hàng chậm, giảm nhập mới, gom dòng tiền về, bỏ SKU yếu và chỉ giữ sản phẩm có vòng quay nhanh.</p></div><div style="display:contents" dir="auto"><hr id="371c5e6f-95bd-80ff-8d4a-cfaa9ee5b367"/></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-80b3-9f6a-d348030be3b7" class="">7. Tỷ lệ r
ò rỉ vận hành</h2></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8089-b168-df174496df0a" class=""><strong>Câu hỏi:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80ca-94d5-c629a51c987e" class="">Doanh nghiệp đang mất tiền ở đâu mà chủ không nhìn thấy?</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8060-b8f6-dda3387bbde4" class=""><strong>Công thức:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8038-890f-ef31f12015cd" class=""><strong>Rò rỉ vận hành = Hao hụt + hoàn hàng + lỗi sản phẩm + thất thoát + giảm giá bắt buộc / Doanh thu × 100%</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8084-a1c5-d7ac95512131" class=""><strong>Cần điền:</strong></p></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8063-b8fb-eaea96808f7b" class="bulleted-list"><li style="list-style-type:disc">Hao hụt:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80e1-806b-e61998d767bc" class="bulleted-list"><li style="list-style-type:disc">Hoàn hàng:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80d5-a647-cdb1ac8997d7" class="bulleted-list"><li style="list-style-type:disc">Lỗi/sửa sai:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80b6-953c-c5749f9c5744" class="bulleted-list"><li style="list-style-type:disc">Giảm giá bắt buộc:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8022-bc63-e2ab81813735" class="bulleted-list"><li style="list-style-type:disc">Thất thoát khác:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8035-afe8-edea1f5af329" class="bulleted-list"><li style="list-style-type:disc">Tổng rò rỉ:</li></ul></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80d2-a6e0-ff52270335d5" class=""><strong>Chấm điểm:</strong></p></div><div style="display:contents" d
ir="auto"><p id="371c5e6f-95bd-8031-b8c8-fb8c055929b5" class="">🔴 Trên 10%: rò tiền nghiêm trọng.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-807c-83ad-c28e434bfa61" class="">🟡 5–10%: cần siết quy trình.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-803b-b4ca-de5f26a015bf" class="">🟢 Dưới 5%: tốt.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-805d-b1ac-c60c4a7e34d9" class=""><strong>Quyết định vận hành:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80ab-88c1-fe184062f4b5" class="">Nếu rò rỉ cao, cần kiểm kho, kiểm đơn, kiểm thu ngân, kiểm quy trình giao hàng, kiểm tỷ lệ hoàn và quy trách nhiệm rõ cho từng khâu.</p></div><div style="display:contents" dir="auto"><hr id="371c5e6f-95bd-804d-a3e2-fd35f7ffcac5"/></div><div style="display:contents" dir="auto"><h1 id="371c5e6f-95bd-806a-b73c-fea84d9147fc" class="">TẦNG 3: KIỂM TRA MỞ RỘNG</h1></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-8031-90e1-daefe31d5a07" class="">Mô hình này có lớn được không?</h2></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-80ff-be4e-ec95996c2c0a" class="">8. Hiệu suất đồng vốn — ROE</h2></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-809d-8c82-c09aeffe6f94" class=""><strong>Câu hỏi:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80df-9d6c-c7411325bd33" class="">Đồng vốn của chủ có đang sinh lời xứng đáng không?</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8082-b2e7-e4fe1573a8fb" class=""><strong>Công thức:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8048-ae7f-dd794b934b9c" class=""><strong>ROE = Lợi nhuận ròng / Vốn chủ sở hữu × 100%</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8054-a197-f9234b02626f" class=""><strong>Cần điền:</strong></p></div><div style="display:contents" dir="auto"><ul i
d="371c5e6f-95bd-8079-8c57-cf6861490eae" class="bulleted-list"><li style="list-style-type:disc">Lợi nhuận ròng:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8086-af39-ebb5aff43325" class="bulleted-list"><li style="list-style-type:disc">Vốn chủ sở hữu:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80df-839c-ecc0d6e652f5" class="bulleted-list"><li style="list-style-type:disc">ROE:</li></ul></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80de-9bf3-c23d52b195b6" class=""><strong>Chấm điểm:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8036-a0cf-f83d95e33731" class="">🔴 Dưới 10%: không hấp dẫn so với rủi ro.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80b4-ab76-f2ff7b2fbe7f" class="">🟡 10–20%: tạm ổn.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80be-b68f-f97ba44eb885" class="">🟢 Trên 20%: tốt.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80c0-963f-cd9005cd1fcd" class="">🟢 Trên 30%: rất tốt nếu dòng tiền ổn định.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80f0-80bb-effaf1414db5" class=""><strong>Quyết định vận hành:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8062-8e5f-d8805d975530" class="">Nếu ROE thấp, không nên mở rộng. Cần xem lại mô hình giá, chi phí, vòng quay vốn và năng suất tài sản.</p></div><div style="display:contents" dir="auto"><hr id="371c5e6f-95bd-80bd-b39a-cd869e0e9dd4"/></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-802f-8b25-d63c682a36a6" class="">9. Sức khỏe marketing — LTV/CAC</h2></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8024-9a21-cc3f4a138e49" class=""><strong>Câu hỏi:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8022-97d7-d8b7bee07796" class="">Chạy quảng cáo có tạo lợi nhuận dài hạn không?</p></div><div s
tyle="display:contents" dir="auto"><p id="371c5e6f-95bd-80bc-ab15-c54cd5ee6710" class=""><strong>Công thức:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-804d-83f0-fdfdaa6d4df4" class=""><strong>LTV/CAC = Giá trị vòng đời khách hàng / Chi phí có một khách hàng mới</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80de-9df2-cffa77549c14" class=""><strong>Cần điền:</strong></p></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8081-a042-d17d31b6d782" class="bulleted-list"><li style="list-style-type:disc">Chi phí marketing:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80be-830d-d2f08a8d8e31" class="bulleted-list"><li style="list-style-type:disc">Số khách hàng mới:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80be-9513-ece3a561671c" class="bulleted-list"><li style="list-style-type:disc">CAC:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80a4-a74a-fe5d66ad1cda" class="bulleted-list"><li style="list-style-type:disc">Giá trị vòng đời khách hàng:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80a1-9d34-f555762348eb" class="bulleted-list"><li style="list-style-type:disc">LTV/CAC:</li></ul></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8064-955e-c4b89a2deb42" class=""><strong>Chấm điểm:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8029-b9aa-ea4f4ba7964f" class="">🔴 Nhỏ hơn hoặc bằng 1: càng chạy càng lỗ.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8077-b98f-c1e106564e52" class="">🟡 1–3: chưa nên scale mạnh.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80b9-a547-c81ac04ab1d3" class="">🟢 Từ 3 trở lên: có thể tăng marketing.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80ec-a230-f75d2bb15fd0" class="">🟢 Từ 5 trở lên: rất t
ốt.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80eb-bb10-db6e7c8b5aa0" class=""><strong>Quyết định vận hành:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8098-914f-e216dcac76e4" class="">Nếu LTV/CAC thấp, không tăng ngân sách quảng cáo. Cần tăng tỷ lệ khách quay lại, tăng giá trị đơn hàng, tăng upsell/cross-sell và cải thiện trải nghiệm khách hàng.</p></div><div style="display:contents" dir="auto"><hr id="371c5e6f-95bd-8094-963b-f74ee86c85e9"/></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-801c-9ea4-d3181dc47433" class="">10. An toàn đòn bẩy nợ</h2></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8048-86ba-f8e91b014455" class=""><strong>Câu hỏi:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8059-a158-d76d03629d1f" class="">Doanh nghiệp đang dùng nợ để phát triển hay đang vay để che áp lực?</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-808f-93e2-fc4c6337b5ca" class=""><strong>Công thức:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80dd-9db9-ca47be2a7757" class=""><strong>Tỷ lệ nợ = Tổng nợ / Vốn chủ sở hữu</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80df-ab4b-f6fff0d93702" class=""><strong>Cần điền:</strong></p></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8006-962a-c193f6790c29" class="bulleted-list"><li style="list-style-type:disc">Tổng nợ:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-804d-bc9e-f9e9c673d6a1" class="bulleted-list"><li style="list-style-type:disc">Vốn chủ sở hữu:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80cf-91e4-e358ee506407" class="bulleted-list"><li style="list-style-type:disc">Tỷ lệ nợ:</li></ul></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-804f-8f25-f6cf0e9474e9" class=""><strong>Chấm đ
iểm:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80cf-9895-dea4e95e213b" class="">🔴 Trên 1.5: rủi ro cao.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8020-8b67-ff7ff060d36e" class="">🟡 0.5–1.5: cần kiểm soát.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80e7-ae6b-dcc3bc4ba536" class="">🟢 Dưới 0.5: an toàn.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80c5-b337-fe81d50c044c" class=""><strong>Quyết định vận hành:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80ee-8073-d0f2956a178d" class="">Nếu nợ cao, không mở rộng bằng vay thêm. Cần giảm hàng tồn, thu hồi công nợ, tái cơ cấu kỳ hạn vay và chỉ vay cho hoạt động tạo dòng tiền rõ ràng.</p></div><div style="display:contents" dir="auto"><hr id="371c5e6f-95bd-807f-8f26-e2debbec109b"/></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-80d9-8088-c6a6a2fdbbad" class="">11. Vành đai phòng thủ — Survival Runway</h2></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8024-aef2-fb780f8f2346" class=""><strong>Câu hỏi:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8063-8c15-d7bc3cc5fee9" class="">Nếu doanh thu giảm mạnh, doanh nghiệp sống được bao lâu?</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8095-ba9f-c49aeab77bdb" class=""><strong>Công thức:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8083-a870-d5c8f87d728c" class=""><strong>Survival Runway = Tiền mặt dự phòng / Chi phí cố định tối thiểu mỗi tháng</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-800b-b5a7-f220d53f482c" class=""><strong>Cần điền:</strong></p></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80de-a9f6-d08ee55cbdcb" class="bulleted-list"><li style="list-style-type:disc">Tiền mặt dự phòng:</li></ul></div><div style="display:contents" d
ir="auto"><ul id="371c5e6f-95bd-808b-a459-f51e726a4bc1" class="bulleted-list"><li style="list-style-type:disc">Chi phí cố định tối thiểu/tháng:</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80c8-90cd-fdcf4adac315" class="bulleted-list"><li style="list-style-type:disc">Số tháng sống sót:</li></ul></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80fe-9165-df0f6ff15a6f" class=""><strong>Chấm điểm:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-801c-8043-eef32bfe48ae" class="">🔴 Dưới 1 tháng: cực kỳ nguy hiểm.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8027-a30c-e5b2982215fc" class="">🟡 1–3 tháng: dễ tổn thương.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8068-b8cf-d6e8f15a09f5" class="">🟢 3–6 tháng: an toàn.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80b6-8ec4-ec622870b2a7" class="">🟢 Trên 6 tháng: rất khỏe.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80cd-8d9e-f1cf440b4602" class=""><strong>Quyết định vận hành:</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80fe-b7f4-c53102da1afa" class="">Nếu runway dưới 3 tháng, doanh nghiệp chưa nên mở rộng. Cần tích lũy quỹ dự phòng trước khi thuê thêm mặt bằng, tuyển thêm người hoặc tăng chi phí cố định.</p></div><div style="display:contents" dir="auto"><hr id="371c5e6f-95bd-8043-9cc4-d2dfa2d6d041"/></div><div style="display:contents" dir="auto"><h1 id="371c5e6f-95bd-8096-8ede-e0f8325b7833" class="">3. Bảng chấm điểm tổng hợp</h1></div><div style="display:contents" dir="ltr"><table id="371c5e6f-95bd-8069-b874-da6bb1e15d0a" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="371c5e6f-95bd-8007-840b-c0f1d1996641"><th id="kjio" class="simple-table-header-color simple-table-header">Tầng</th><th id="JT?R" class="simple-table-header-color s
imple-table-header">Chỉ số</th><th id="JP\y" class="simple-table-header-color simple-table-header">Kết quả</th><th id="]|Wy" class="simple-table-header-color simple-table-header">Màu</th><th id="Kiw&gt;" class="simple-table-header-color simple-table-header">Hành động</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="371c5e6f-95bd-806a-80a3-de815a5bef25"><td id="kjio" class="">Sinh tồn</td><td id="JT?R" class="">Biên lãi gộp</td><td id="JP\y" class=""></td><td id="]|Wy" class=""></td><td id="Kiw&gt;" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="371c5e6f-95bd-80a4-a0b9-cbf71b19af82"><td id="kjio" class="">Sinh tồn</td><td id="JT?R" class="">Hòa vốn</td><td id="JP\y" class=""></td><td id="]|Wy" class=""></td><td id="Kiw&gt;" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="371c5e6f-95bd-80f6-b603-c16f0e01bb14"><td id="kjio" class="">Sinh tồn</td><td id="JT?R" class="">Dòng tiền</td><td id="JP\y" class=""></td><td id="]|Wy" class=""></td><td id="Kiw&gt;" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="371c5e6f-95bd-800a-a9f0-f16ec652cff4"><td id="kjio" class="">Vận hành</td><td id="JT?R" class="">Giá vốn</td><td id="JP\y" class=""></td><td id="]|Wy" class=""></td><td id="Kiw&gt;" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="371c5e6f-95bd-80aa-a19f-e4b155467e0f"><td id="kjio" class="">Vận hành</td><td id="JT?R" class="">Quỹ lương</td><td id="JP\y" class=""></td><td id="]|Wy" class=""></td><td id="Kiw&gt;" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="371c5e6f-95bd-80a4-a8e2-f1d56d6b6591"><td id="kjio" class="">Vận hành</td><td id="JT?R" class="">Tồn kho</td><td id="JP\y" class=""></td><td id="]|Wy" class=""></td><td id="Kiw&gt;" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="371c5e6f-95bd-80b2-8fdb-cb7d915beebc"><td id="kjio" class="">Vận hành</td><td id="JT?R" class="">Rò rỉ vận h
ành</td><td id="JP\y" class=""></td><td id="]|Wy" class=""></td><td id="Kiw&gt;" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="371c5e6f-95bd-8049-baea-c44ae55169f5"><td id="kjio" class="">Mở rộng</td><td id="JT?R" class="">ROE</td><td id="JP\y" class=""></td><td id="]|Wy" class=""></td><td id="Kiw&gt;" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="371c5e6f-95bd-805b-9f8f-c1785ad4c0a0"><td id="kjio" class="">Mở rộng</td><td id="JT?R" class="">LTV/CAC</td><td id="JP\y" class=""></td><td id="]|Wy" class=""></td><td id="Kiw&gt;" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="371c5e6f-95bd-80a7-8fc1-fe197afd3e36"><td id="kjio" class="">Mở rộng</td><td id="JT?R" class="">Đòn bẩy nợ</td><td id="JP\y" class=""></td><td id="]|Wy" class=""></td><td id="Kiw&gt;" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="371c5e6f-95bd-8003-be45-c49f67ec470d"><td id="kjio" class="">Mở rộng</td><td id="JT?R" class="">Survival runway</td><td id="JP\y" class=""></td><td id="]|Wy" class=""></td><td id="Kiw&gt;" class=""></td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="371c5e6f-95bd-8075-9e93-daa464a0f1d6"/></div><div style="display:contents" dir="auto"><h1 id="371c5e6f-95bd-8008-a3c3-c5fa768cd87e" class="">4. Luật ra quyết định cho chủ doanh nghiệp nhỏ</h1></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-8064-a1bb-c84b94720d8c" class="">Trường hợp 1: Có chỉ số đỏ ở tầng sinh tồn</h2></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8040-a4a1-e3ed257f481e" class=""><strong>Kết luận:</strong> chưa được mở rộng.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-800e-aa72-c24b65aced52" class="">Việc cần làm ngay:</p></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-809b-a516-f13adb4f9a64" class="bulleted-list"><li style="list-style-type:disc">Dừng thuê thêm mặt b
ằng.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80c3-8c6b-f25f19992202" class="bulleted-list"><li style="list-style-type:disc">Dừng tuyển thêm người.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80e6-ab01-fb2c50ea491f" class="bulleted-list"><li style="list-style-type:disc">Dừng tăng ngân sách quảng cáo đại trà.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80fa-8e7d-da2a9b510a06" class="bulleted-list"><li style="list-style-type:disc">Thu hồi công nợ.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80aa-a43f-f95641f22fac" class="bulleted-list"><li style="list-style-type:disc">Cắt chi phí cố định.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-807a-beff-ca80e3a20a35" class="bulleted-list"><li style="list-style-type:disc">Tối ưu giá vốn.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8039-95f3-e0ead6c538f5" class="bulleted-list"><li style="list-style-type:disc">Bảo vệ tiền mặt.</li></ul></div><div style="display:contents" dir="auto"><hr id="371c5e6f-95bd-802d-960f-c64a70cff07e"/></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-8095-945f-d08628913e18" class="">Trường hợp 2: Tầng sinh tồn xanh, tầng vận hành vàng</h2></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80d1-85c5-e7fb74a577f2" class=""><strong>Kết luận:</strong> doanh nghiệp sống được nhưng chưa khỏe.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-809a-a23d-c179f095d575" class="">Việc cần làm:</p></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80cd-b348-c12cb7d66d0c" class="bulleted-list"><li style="list-style-type:disc">Chuẩn hóa quy trình.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8009-aed1-f3ed69bc3374" class="bulleted-list"><li style="list-style-type:disc">Giảm hao hụt.</li></ul></div><div s
tyle="display:contents" dir="auto"><ul id="371c5e6f-95bd-80a8-aa84-f7153dee8659" class="bulleted-list"><li style="list-style-type:disc">Tối ưu nhân sự.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80c4-9508-c5c16a1beb90" class="bulleted-list"><li style="list-style-type:disc">Tăng vòng quay hàng tồn.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80c1-a66d-cdffd692cc29" class="bulleted-list"><li style="list-style-type:disc">Kiểm soát giảm giá và hoàn hàng.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80d2-8805-c819009c729b" class="bulleted-list"><li style="list-style-type:disc">Nâng năng suất từng điểm bán/từng nhân viên/từng sản phẩm.</li></ul></div><div style="display:contents" dir="auto"><hr id="371c5e6f-95bd-80cf-8606-deecca391d1e"/></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-8009-96b6-dd3bbbefaf4d" class="">Trường hợp 3: Tầng sinh tồn và vận hành xanh, nhưng LTV/CAC đỏ</h2></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8006-b206-ebd042d056d6" class=""><strong>Kết luận:</strong> sản phẩm có thể bán được nhưng chưa giữ được khách.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-802f-854b-e34bae568acf" class="">Việc cần làm:</p></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-808c-b633-cd97679a110b" class="bulleted-list"><li style="list-style-type:disc">Không tăng quảng cáo.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-806c-b840-f42da45c02ac" class="bulleted-list"><li style="list-style-type:disc">Cải thiện trải nghiệm khách hàng.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8017-b619-d6288ac690c9" class="bulleted-list"><li style="list-style-type:disc">Tạo gói mua lại.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-803b-921e-e9fc1529722e" class="bulleted-list"><li s
tyle="list-style-type:disc">Tạo chương trình thành viên.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8019-904f-c3de2ee82868" class="bulleted-list"><li style="list-style-type:disc">Tăng giá trị đơn hàng.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-806f-a622-ce9d4fb698da" class="bulleted-list"><li style="list-style-type:disc">Tăng tỷ lệ khách quay lại.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8090-ac0d-e09dde0be814" class="bulleted-list"><li style="list-style-type:disc">Tăng referral.</li></ul></div><div style="display:contents" dir="auto"><hr id="371c5e6f-95bd-8064-84bc-fd1c4f66e29f"/></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-80ed-a2d9-edaff8be7110" class="">Trường hợp 4: Cả 3 tầng đều xanh</h2></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8098-8b38-f3b9d277b3c2" class=""><strong>Kết luận:</strong> mô hình đủ điều kiện mở rộng.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8046-83b8-e44d7b4ee201" class="">Việc có thể làm:</p></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-803f-aec8-ff921bb6892c" class="bulleted-list"><li style="list-style-type:disc">Tăng ngân sách marketing có kiểm soát.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80ea-ba28-d081502f5864" class="bulleted-list"><li style="list-style-type:disc">Mở thêm điểm bán.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8004-a3d0-c90eb5f0c6c9" class="bulleted-list"><li style="list-style-type:disc">Tuyển thêm nhân sự chủ chốt.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80d6-95c0-e67ae89a2712" class="bulleted-list"><li style="list-style-type:disc">Đầu tư hệ thống quản trị.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8002-a5d2-f3e52471a586" class="bulleted-list"><li s
tyle="list-style-type:disc">Chuẩn hóa SOP.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-804a-beac-f89e402d9115" class="bulleted-list"><li style="list-style-type:disc">Nhân bản mô hình.</li></ul></div><div style="display:contents" dir="auto"><hr id="371c5e6f-95bd-8044-8b66-e56d53a5b774"/></div><div style="display:contents" dir="auto"><h1 id="371c5e6f-95bd-8034-9364-d3bcff94646f" class="">5. Phiên bản checklist nhanh cho chủ doanh nghiệp</h1></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-801a-a54e-ea2a7488f77f" class="">Trước khi mở rộng, hãy trả lời 11 câu này:</p></div><div style="display:contents" dir="auto"><ol type="1" id="371c5e6f-95bd-8059-82d2-fec0ce6595b2" class="numbered-list" start="1"><li>Mỗi đơn hàng có đủ lãi không?</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="371c5e6f-95bd-808a-bd24-c8aef74e11cf" class="numbered-list" start="2"><li>Mỗi tháng cần bán bao nhiêu mới hòa vốn?</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="371c5e6f-95bd-8066-a8d9-fb660a165ffc" class="numbered-list" start="3"><li>Dòng tiền thật có đang dương không?</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="371c5e6f-95bd-80f8-90d4-ee03d19e1063" class="numbered-list" start="4"><li>Giá vốn có đang quá cao không?</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="371c5e6f-95bd-8063-a5c4-e7af8e0967fe" class="numbered-list" start="5"><li>Quỹ lương có tương xứng với doanh thu không?</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="371c5e6f-95bd-801d-86f9-e1713aa042b3" class="numbered-list" start="6"><li>Hàng tồn kho có đang chôn vốn không?</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="371c5e6f-95bd-8043-b53f-c88dbf6216c2" class="numbered-list" start="7"><li>Doanh nghiệp có đang rò tiền vì sai lỗi, hao hụt, hoàn hàng không?</li></ol></div><div style="display:contents" dir="auto"><ol type="1" 
d="371c5e6f-95bd-8031-8064-f9b851721316" class="numbered-list" start="8"><li>Đồng vốn của chủ có sinh lời xứng đáng không?</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="371c5e6f-95bd-806f-a7eb-d7f7db9a4cf3" class="numbered-list" start="9"><li>Chi phí mua khách có thấp hơn giá trị khách hàng tạo ra không?</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="371c5e6f-95bd-80ce-a98a-ffc300651611" class="numbered-list numbered-list-digits-2" start="10"><li>Nợ có đang vượt khả năng chịu đựng không?</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="371c5e6f-95bd-80ae-9600-c97549e3714c" class="numbered-list numbered-list-digits-2" start="11"><li>Nếu doanh thu về 0, doanh nghiệp sống được mấy tháng?</li></ol></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80a3-a77f-d59936422864" class="">Nếu không trả lời rõ 11 câu này, doanh nghiệp chưa nên mở rộng.</p></div><div style="display:contents" dir="auto"><hr id="371c5e6f-95bd-806e-bb55-f4ca487ae6c9"/></div><div style="display:contents" dir="auto"><h1 id="371c5e6f-95bd-8071-80de-eaa2f20dc599" class="">6. Câu định vị của công cụ</h1></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-800c-8219-cd55e9294841" class=""><strong>SME Business Survival Tool là công cụ kiểm tra sức khỏe mô hình kinh doanh cho doanh nghiệp nhỏ, giúp chủ doanh nghiệp biết khi nào cần cứu dòng tiền, khi nào cần tối ưu vận hành, và khi nào đủ điều kiện để mở rộng.</strong></p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8010-8811-ddf44f8f7bc1" class="">Một doanh nghiệp nhỏ không chết vì thiếu ý tưởng.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8047-8332-cda500b7d6f7" class="">Nó thường chết vì không đo đúng 11 phép tính sinh tồn.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8097-90a5-dceb60216f3b" class="">
</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80a1-ac04-f0d633d2ced9" class="">
</p></div><div style="display:contents" dir="ltr"><figure id="371c5e6f-95bd-8035-92b3-c4638ba4e624" class="link-to-page"><a href="11%20Ti%C3%AAu%20ch%C3%AD%20m%C3%B4%20h%C3%ACnh%20kinh%20doanh/H%C6%AF%E1%BB%9ANG%20D%E1%BA%AAN%20X%C3%82Y%20D%E1%BB%B0NG%20H%E1%BB%86%20TH%E1%BB%90NG%20MA%20TR%E1%BA%ACN%20CONTENT%20AGENT%20%20371c5e6f95bd803592b3c4638ba4e624.html">HƯỚNG DẪN XÂY DỰNG HỆ THỐNG  MA TRẬN CONTENT AGENT VỚI CLAUDE</a></figure></div><div style="display:contents" dir="ltr"><figure id="371c5e6f-95bd-80d1-bd7b-f080b0e5e9a1" class="link-to-page"><a href="11%20Ti%C3%AAu%20ch%C3%AD%20m%C3%B4%20h%C3%ACnh%20kinh%20doanh/THI%E1%BA%BET%20K%E1%BA%BE%20M%C3%94%20H%C3%8CNH%20M%C3%94I%20GI%E1%BB%9AI%20B%E1%BA%A4T%20%C4%90%E1%BB%98NG%20S%E1%BA%A2N%20371c5e6f95bd80d1bd7bf080b0e5e9a1.html"> THIẾT KẾ MÔ HÌNH MÔI GIỚI BẤT ĐỘNG SẢN</a></figure></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
