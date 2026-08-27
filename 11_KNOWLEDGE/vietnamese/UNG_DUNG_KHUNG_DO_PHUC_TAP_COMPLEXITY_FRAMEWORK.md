---
tags: [vietnamese]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Ứng dụng Khung Độ Phức Tạp (Complexity Framework) vào Ba Hệ Thống Biểu tượng Đông Sơn – Cổ Loa – Trống Đồng</title><style>
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
	
</style></head><body><article id="361c5e6f-95bd-80f1-9a06-e9bf2b3cf0fb" class="page sans"><header><h1 class="page-title" dir="auto">Ứng dụng Khung Độ Phức Tạp (Complexity Framework) vào Ba Hệ Thống Biểu tượng Đông Sơn – Cổ Loa – Trống Đồng</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-8066-9965-e11a9ff28226" class=""><strong>Tác giả:</strong> Trang Phan</p></div><div style="display:contents" dir="auto"><hr id="361c5e6f-95bd-80b2-a67c-d90a11079116"/></div><div style="display:contents" dir="auto"><h2 id="361c5e6f-95bd-8045-8d0c-d9113e478966" class="">Tóm tắt điều hành</h2></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-802b-94ff-cf49f361e5db" class="">Báo cáo này thực hiện ánh xạ có hệ thống ba thực thể khảo cổ học và văn minh học – <strong>Trống đồng Đông Sơn</strong>, <strong>thành Cổ Loa</strong>, và <strong>văn minh Đông Sơn</strong> – lên năm trường đo lường độ phức tạp (complexity metrics) trong khung lý thuyết của tác giả. Luận điểm trung tâm: cả ba thực thể đều là biểu hiện fractal của cùng một cấu trúc vận hành sâu: <strong>TÂM → TRƯỜNG → VÒNG → BIÊN → CHU KỲ → TÍN HIỆU → KÝ ỨC</strong>. Không có sự ưu ái diễn giải. Không có sự khiêm tốn giả tạo. Dữ liệu hiển nhiên.</p></div><div style="display:contents" dir="auto"><hr id="361c5e6f-95bd-80aa-a6a7-e64533ec1fe4"/></div><div style="display:contents" dir="auto"><h2 id="361c5e6f-95bd-8006-9466-c70a97b93be5" class="">1. Khung lý thuyết: Năm trường đo độ phức tạp</h2></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-802c-970a-ca8b7a11a3d0" class="">Trước khi ánh xạ, cần định nghĩa năm trường.</p></div><div style="display:contents" dir="ltr"><table id="361c5e6f-95bd-80ef-bfe9-cc5874a24272" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-80fd-b763-eca81a8bc10a"><th id="f:bc" class="simple-table-header-color simple-table-header">Trường</th><th id=";rpI" class="simple-table-header-color simple-table-header">Định nghĩa vận hành</th><th id="dxNF" class="simple-table-header-color simple-table-header">Câu hỏi trung tâm</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-80e5-908a-e1202a278c79"><td id="f:bc" class=""><strong>1. Thuật toán / Độ nén (K)</strong></td><td id=";rpI" class="">Độ dài mô tả ngắn nhất (minimum description length) đủ để tái tạo toàn bộ hệ thống</td><td id="dxNF" class="">Hệ thống này nén bao nhiêu thông tin vào một hình thức duy nhất?</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-80bd-b5af-c2d732855901"><td id="f:bc" class=""><strong>2. Thống kê / Entropy cấu trúc (H)</strong></td><td id=";rpI" class="">Phân bố xác suất của các motif / trạng thái; trật tự nằm giữa hỗn loạn (H cao) và cứng nhắc (H thấp)</td><td id="dxNF" class="">Hệ thống có &quot;trật tự sống&quot; (edge of chaos) không?</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-80d2-b1c8-cac9c3ccb056"><td id="f:bc" class=""><strong>3. Tài nguyên / Độ sâu logic (D)</strong></td><td id=";rpI" class="">Tổng thời gian tích lũy (cumulative time) của các quá trình kỹ thuật, xã hội, nghi lễ, vật liệu</td><td id="dxNF" class="">Hệ thống này cần bao nhiêu lớp tích lũy để xuất hiện?</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-80ba-912e-c32ccad56b64"><td id="f:bc" class="">**4. Cấu trúc / Mạng lưới (G)</td><td id=";rpI" class="">Đồ thị các node (motif, không gian, vai trò xã hội) và edge (quan hệ) với các chỉ số centrality, modularity, hierarchy</td><td id="dxNF" class="">Ai / cái gì kết nối với ai, và cấu trúc quyền lực ra sao?</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-806e-bc5a-eee54d22fe84"><td id="f:bc" class=""><strong>5. Động lực / Sự thích nghi (Φ)</strong></td><td id=";rpI" class="">Hàm chuyển trạng thái theo thời gian, chịu tác động của môi trường (nước, mùa, lũ, xâm lăng)</td><td id="dxNF" class="">Hệ thống có tồn tại ở rìa hỗn loạn (edge of chaos) và thích nghi không?</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="361c5e6f-95bd-8038-9604-db19570c0f0d"/></div><div style="display:contents" dir="auto"><h2 id="361c5e6f-95bd-8054-acec-c974aee00b60" class="">2. Đối tượng 1: Trống đồng Đông Sơn</h2></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-8068-ad11-ce788d195c3c" class="">2.1. Bản chất hệ thống</h3></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-8012-bc22-cb85a153c8a8" class="">Trống đồng Đông Sơn không phải &quot;trống&quot; theo nghĩa nhạc cụ. Nó là <strong>máy nén văn minh</strong> (civilization compressor). Toàn bộ thế giới quan, sinh thái, nghi lễ, quyền lực, lịch, và hệ thống âm thanh của một xã hội thủy văn (hydraulic society) được nén vào một vật thể duy nhất: khối đồng tròn, hoa văn khắc chìm, âm thanh cộng hưởng.</p></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-8097-9c8c-cec52b61b14a" class="">2.2. Ánh xạ lên năm trường</h3></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-80b4-bf8b-d57269de9ba3" class="">Trường 1 – Độ nén (K)</h3></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80ee-95bf-fd1de047090d" class="">K(Trống Đồng) = mô tả ngắn nhất bao gồm:</p></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-800c-91e8-fd0c9ef6720e" class="bulleted-list"><li style="list-style-type:disc">Tâm mặt trời (solar center)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80dc-ba7b-e99eb4c8d5ff" class="bulleted-list"><li style="list-style-type:disc">Vòng đồng tâm (concentric rings)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8072-b820-e4ba0cdb66bc" class="bulleted-list"><li style="list-style-type:disc">Chim, thuyền, người, nhà, hoa văn hình học</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8056-a9b9-d91c628d0424" class="bulleted-list"><li style="list-style-type:disc">Hợp kim đồng</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8014-b453-fb0d142ab8f3" class="bulleted-list"><li style="list-style-type:disc">Âm thanh có tần số nghi lễ</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-800f-9f7e-ea99c763d737" class="bulleted-list"><li style="list-style-type:disc">Khuôn đúc phức hợp</li></ul></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-809d-b498-e6b3b4c12729" class="">Hệ quả: Độ nén cực cao. Một mặt trống có thể tái tạo lịch, bản đồ thủy văn, cấu trúc quyền lực, và nghi lễ cộng đồng.</p></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-8008-a51e-cd4356080849" class="">Mermaid sơ đồ độ nén:</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="361c5e6f-95bd-8042-8556-e86892517b9d" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">graph TD
    A[Văn minh Đông Sơn] --&gt; B[Lịch mặt trời]
    A --&gt; C[Hệ thống sông nước]
    A --&gt; D[Phân tầng xã hội]
    A --&gt; E[Nghi lễ tổ tiên]
    A --&gt; F[Kỹ thuật đồng thau]
    B --&gt; G[Trống Đồng&lt;br/&gt;Máy nén duy nhất]
    C --&gt; G
    D --&gt; G
    E --&gt; G
    F --&gt; G
    G --&gt; H[Mặt trời tâm]
    G --&gt; I[Vòng hoa văn]
    G --&gt; J[Âm thanh nghi lễ]
    G --&gt; K[Ký ức cộng đồng]</code></pre></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-80d4-956e-c8d50126dbbb" class="">Trường 2 – Entropy cấu trúc (H)</h3></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-8049-84eb-fe8c405a06a4" class="">Phân bố motif trên mặt trống không ngẫu nhiên (H quá cao sẽ là nhiễu). Cũng không lặp y hệt (H quá thấp sẽ cứng chết). Entropy ở mức &quot;vừa đủ&quot; – lặp nhưng biến thể, đối xứng nhưng có phá vỡ, vòng tròn nhưng có hướng chuyển động. Đây là dấu hiệu của <strong>trật tự ở rìa hỗn loạn</strong> (order at the edge of chaos).</p></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80be-b21b-d3f52aa1df85" class="">Các motif điển hình:</p></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80fe-a8db-c0b682362ec7" class="bulleted-list"><li style="list-style-type:disc">Mặt trời trung tâm: entropy thấp (cực kỳ ổn định)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8095-af91-e86c256ad742" class="bulleted-list"><li style="list-style-type:disc">Vòng chim bay: entropy trung bình (lặp nhưng khác hướng)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-806c-9e88-dc98912be40c" class="bulleted-list"><li style="list-style-type:disc">Vòng thuyền – người: entropy cao hơn (nhiều chi tiết, nhiều tư thế)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80ae-a5d2-f665dbdd297f" class="bulleted-list"><li style="list-style-type:disc">Hoa văn hình học: entropy rất thấp (lặp chính xác)</li></ul></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-806a-b4c4-c3d254569ddc" class="">Kết quả: Mật độ ý nghĩa (meaning density) = tích của entropy vừa phải × đối xứng × nhịp vòng × mạch lạc motif.</p></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-8027-a1eb-db3fdef3a4b9" class="">Mermaid phân bố entropy:</p></div><div style="display:contents" dir="auto"><pre id="361c5e6f-95bd-80f2-97af-e5f0ae10f9e4" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">pie title Phân bố entropy trên mặt trống
    &quot;Mặt trời tâm (H rất thấp)&quot; : 10
    &quot;Vòng chim (H trung bình)&quot; : 30
    &quot;Vòng thuyền-người (H cao)&quot; : 40
    &quot;Vòng hình học (H thấp)&quot; : 20</code></pre></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-801d-b5be-dab9cc659a4e" class="">Trường 3 – Độ sâu logic (D)</h3></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80fa-9671-da1afe0dc5ea" class="">D(Trống Đồng) không thể thấp. Để đúc được một trống đồng Đông Sơn, xã hội phải có:</p></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-808f-ba09-d3e276a0adb0" class="bulleted-list"><li style="list-style-type:disc">Tích lũy khai mỏ và luyện kim: &gt; 1000 năm (từ Phùng Nguyên)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-802b-833c-fcb06f369ebe" class="bulleted-list"><li style="list-style-type:disc">Tích lũy kỹ thuật khuôn đúc: &gt; 500 năm</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8097-af33-d23fbc8f436a" class="bulleted-list"><li style="list-style-type:disc">Tích lũy thừa dư nông nghiệp (lúa nước): &gt; 1500 năm</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8004-be54-f98d7a782f62" class="bulleted-list"><li style="list-style-type:disc">Tích lũy cấu trúc quyền lực tập trung: &gt; 500 năm</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80ac-aca5-fe5cdf01fef7" class="bulleted-list"><li style="list-style-type:disc">Tích lũy hệ thống nghi lễ âm thanh: không xác định nhưng sâu</li></ul></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80c1-ae21-e063e11b83db" class="">Phương trình nén: Đông Sơn = Hòa Bình → Mán Bạc → Phùng Nguyên → Đồng Đậu → Gò Mun → Đông Sơn → Cổ Loa. Mỗi mũi tên là một bậc tích lũy.</p></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80cd-82d1-c205853afccf" class="">Mermaid tiến trình tích lũy:</p></div><div style="display:contents" dir="auto"><pre id="361c5e6f-95bd-80c2-9aba-e03278d934d7" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">timeline
    title Độ sâu logic của Trống Đồng (D)
    10.000-5.000 BP : Săn bắt hái lượm&lt;br/&gt;Nền tảng sinh thái
    5.000-4.000 BP : Tiền nông nghiệp&lt;br/&gt;Gốm, làng
    4.000-3.500 BP : Lúa nước định cư&lt;br/&gt;Phùng Nguyên
    3.500-3.000 BP : Đồng sơ khai&lt;br/&gt;Đồng Đậu
    3.000-2.500 BP : Đồng thau kỹ thuật cao&lt;br/&gt;Gò Mun
    2.500-2.000 BP : TRỐNG ĐỒNG ĐÔNG SƠN</code></pre></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-80eb-b9a8-d80602fbab66" class="">Trường 4 – Cấu trúc mạng (G)</h3></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80da-a66b-cc8ea5e9d76a" class="">Mạng motif trên mặt trống có các đặc điểm:</p></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8020-a14b-fd459c294569" class="bulleted-list"><li style="list-style-type:disc">Một node trung tâm (mặt trời) với centrality tuyệt đối</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80cd-969a-c7af32b77d49" class="bulleted-list"><li style="list-style-type:disc">Các vòng là các module (module = chim, thuyền, người, hình học)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80c4-8a95-cc11cdad99b3" class="bulleted-list"><li style="list-style-type:disc">Mỗi module có node con riêng</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8060-8159-f80774294e5a" class="bulleted-list"><li style="list-style-type:disc">Edge: hướng xoay (theo vòng), đối xứng xuyên tâm, lặp nhịp</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8064-b685-e4ed9c103c8d" class="bulleted-list"><li style="list-style-type:disc">Âm thanh là tín hiệu kích hoạt toàn mạng (activation signal)</li></ul></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-8071-b283-dfda18b2a46f" class="">Mermaid đồ thị mạng motif:</p></div><div style="display:contents" dir="auto"><pre id="361c5e6f-95bd-807f-aa50-f31232c51147" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">graph LR
    Sun[Mặt Trời&lt;br/&gt;Centrality=1.0] --&gt; Ring1[Vòng 1: Chim]
    Sun --&gt; Ring2[Vòng 2: Thuyền]
    Sun --&gt; Ring3[Vòng 3: Người]
    Sun --&gt; Ring4[Vòng 4: Hình học]
    Ring1 --&gt; Bird1[Chim A]
    Ring1 --&gt; Bird2[Chim B]
    Ring2 --&gt; Boat1[Thuyền A]
    Ring2 --&gt; Boat2[Thuyền B]
    Ring3 --&gt; Human1[Người A]
    Ring3 --&gt; Human2[Người B]
    Ring4 --&gt; Geo1[Hình A]
    Ring4 --&gt; Geo2[Hình B]
    DrumSound[Âm thanh trống] -.-&gt; Sun
    DrumSound -.-&gt; Ring1
    DrumSound -.-&gt; Ring2
    DrumSound -.-&gt; Ring3
    DrumSound -.-&gt; Ring4</code></pre></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-8066-a0e2-de209148acca" class="">Trường 5 – Động lực thích nghi (Φ)</h3></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-807f-bb42-c00db90d1b87" class="">Trống đồng không phải tĩnh. Nó thay đổi theo chu kỳ:</p></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-806d-a395-c1cdeb46541f" class="bulleted-list"><li style="list-style-type:disc">Khi đánh trống, âm thanh kích hoạt nghi lễ → cộng đồng đồng bộ → tái lập trật tự sau lũ / mùa / chiến tranh</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80d2-8466-d43713f27ca3" class="bulleted-list"><li style="list-style-type:disc">Hoa văn không cố định tuyệt đối: các trống khác nhau có biến thể motif (thích nghi địa phương)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80bb-83a5-f71fd7590732" class="bulleted-list"><li style="list-style-type:disc">Hệ thống này tồn tại vì nó ở rìa hỗn loạn: quá cứng (một motif lặp y hệt) sẽ chết vì không đáp ứng biến đổi môi trường; quá loạn (không motif nào lặp) sẽ mất chức năng nghi lễ</li></ul></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80b8-b34f-cf2106eb9d52" class="">Mermaid vòng động lực:</p></div><div style="display:contents" dir="auto"><pre id="361c5e6f-95bd-80af-a11d-fe9a657bee4f" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">stateDiagram-v2
    [*] --&gt; Mua_lũ
    Mua_lũ --&gt; Mất_trật_tự
    Mất_trật_tự --&gt; Đánh_trống
    Đánh_trống --&gt; Kích_hoạt_nghi_lễ
    Kích_hoạt_nghi_lễ --&gt; Đồng_bộ_cộng_đồng
    Đồng_bộ_cộng_đồng --&gt; Tái_lập_trật_tự
    Tái_lập_trật_tự --&gt; Mùa_khô
    Mùa_khô --&gt; Tích_lũy
    Tích_lũy --&gt; Mua_lũ</code></pre></div><div style="display:contents" dir="auto"><hr id="361c5e6f-95bd-80e0-a6ec-ea412af60cd3"/></div><div style="display:contents" dir="auto"><h2 id="361c5e6f-95bd-8096-a637-e1e7dea9dead" class="">3. Đối tượng 2: Thành Cổ Loa</h2></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-80f7-9f86-c995abab75b1" class="">3.1. Bản chất hệ thống</h3></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80d6-b87f-f34b0ab499a9" class="">Cổ Loa không phải &quot;thành&quot; theo nghĩa tường đá châu Âu. Nó là <strong>máy nén quyền lực không gian</strong> (spatial power compressor). Cùng một cấu trúc fractal của trống đồng (tâm → vòng → biên → nước → âm thanh → ký ức) nhưng được phóng đại thành địa hình, thủy lợi, lao động tập thể, và quân sự.</p></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-8042-822d-d301ab6e5b2a" class="">3.2. Ánh xạ lên năm trường</h3></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-8082-a769-ca63b78d7e2d" class="">Trường 1 – Độ nén (K)</h3></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-8010-97d5-f4aff6a8bacf" class="">K(Cổ Loa) = mô tả ngắn nhất bao gồm:</p></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8007-bcce-fe39a43e7fe4" class="bulleted-list"><li style="list-style-type:disc">Một lõi quyền lực trung tâm (nội thành)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-805b-bd65-f861b3f209ec" class="bulleted-list"><li style="list-style-type:disc">Ba vòng thành đất (concentric ramparts)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80d0-bf35-c7c65798b68e" class="bulleted-list"><li style="list-style-type:disc">Hào nước kết nối sông Hoàng – sông Hồng</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-806f-9cc6-d7d8ef42df25" class="bulleted-list"><li style="list-style-type:disc">Hệ thống cửa ô kiểm soát</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8089-bde3-fb2cd1cfb8ab" class="bulleted-list"><li style="list-style-type:disc">Xưởng, kho, doanh trại, đền</li></ul></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80cd-b043-e80d6d33fc8d" class="">Độ nén thấp hơn trống đồng vì Cổ Loa là vật thể lớn hơn, nhưng cấu trúc nén vẫn rất cao: toàn bộ ý đồ quân sự, thủy văn, chính trị được nén vào một hình học vòng tròn.</p></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80f5-8d00-f5a8831c98d5" class="">Mermaid sơ đồ nén:</p></div><div style="display:contents" dir="auto"><pre id="361c5e6f-95bd-80b1-8d9f-e26281f58d4a" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">graph TD
    A[Nhà nước Âu Lạc] --&gt; B[Quyền lực trung ương]
    A --&gt; C[Kiểm soát lãnh thổ]
    A --&gt; D[Phòng thủ quân sự]
    A --&gt; E[Quản lý nước]
    A --&gt; F[Huy động lao động]
    B --&gt; G[Thành Cổ Loa&lt;br/&gt;Bộ nén không gian]
    C --&gt; G
    D --&gt; G
    E --&gt; G
    F --&gt; G
    G --&gt; H[Nội thành - lõi]
    G --&gt; I[Trung thành - vòng 1]
    G --&gt; J[Ngoại thành - vòng 2]
    G --&gt; K[Hào nước liên hoàn]
    G --&gt; L[Kiểm soát cửa ô]</code></pre></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-8001-a3fd-e1fc7db576d9" class="">Trường 2 – Entropy cấu trúc (H)</h3></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-8036-9f1d-f1900cdef349" class="">Cổ Loa có entropy thấp hơn trống đồng. Nó là một công trình quân sự – chính trị, do đó yêu cầu trật tự cao. Tuy nhiên, các vòng thành không phải đường tròn hoàn hảo: chúng uốn theo địa hình, chạy theo sông, tránh vùng trũng. Đây là &quot;entropy địa hình&quot; – sự thích nghi có kiểm soát.</p></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80d5-9ff3-d5ed0c193c12" class="bulleted-list"><li style="list-style-type:disc">Vòng trong cùng: entropy rất thấp (gần tròn, gần đối xứng)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-802a-b707-e81a849ae0d6" class="bulleted-list"><li style="list-style-type:disc">Vòng giữa: entropy trung bình (uốn theo địa hình nhiều hơn)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8097-a3f3-d3c9e39f4e04" class="bulleted-list"><li style="list-style-type:disc">Vòng ngoài: entropy cao nhất (chạy dài, bẻ góc, tận dụng sông tự nhiên)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-802c-8ce7-e0088dd70ee6" class="bulleted-list"><li style="list-style-type:disc">Hào nước: entropy thấp (kênh đào nhân tạo)</li></ul></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-8030-853b-d41c3342d32e" class="">Mermaid so sánh entropy:</p></div><div style="display:contents" dir="auto"><pre id="361c5e6f-95bd-80c9-a892-daec19dcb81b" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">graph LR
    subgraph &quot;Cổ Loa&quot;
        A[Nội thành&lt;br/&gt;H rất thấp]
        B[Trung thành&lt;br/&gt;H thấp]
        C[Ngoại thành&lt;br/&gt;H trung bình]
        D[Hào nước&lt;br/&gt;H rất thấp]
    end
    subgraph &quot;Trống Đồng (so sánh)&quot;
        E[Mặt trời tâm&lt;br/&gt;H rất thấp]
        F[Chim&lt;br/&gt;H trung bình]
        G[Thuyền/Người&lt;br/&gt;H cao]
        H[Hình học&lt;br/&gt;H thấp]
    end</code></pre></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-808c-a337-d842382100cb" class="">Trường 3 – Độ sâu logic (D)</h3></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-805b-8d56-ffb3a39662a4" class="">D(Cổ Loa) rất lớn. Không thể đắp một hệ thống ba vòng thành với khối lượng đất lên đến hàng triệu mét khối nếu không có:</p></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8024-a339-f4fe780ac93d" class="bulleted-list"><li style="list-style-type:disc">Tích lũy tổ chức lao động tập thể: &gt; 500 năm (từ các làng tiền Đông Sơn)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80da-9785-d6ffbab27fdd" class="bulleted-list"><li style="list-style-type:disc">Tích lũy kỹ thuật quân sự: &gt; 300 năm</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80af-993e-c1de359e3e12" class="bulleted-list"><li style="list-style-type:disc">Tích lũy quản trị thủy văn: &gt; 1000 năm (lúa nước bắt buộc phải có quản lý nước)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-800f-b6a3-cd168bb77803" class="bulleted-list"><li style="list-style-type:disc">Tích lũy nhà nước sơ khai: &gt; 200 năm</li></ul></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80d3-aaec-fc7efb6bd902" class="">D(Cổ Loa) ≥ D(Trống Đồng) + 300 năm xã hội học.</p></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80d1-854d-e4982c93f438" class="">Mermaid tiến trình:</p></div><div style="display:contents" dir="auto"><pre id="361c5e6f-95bd-800b-980a-c37776d04c30" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">timeline
    title Độ sâu logic của Cổ Loa (D)
    4000-3500 BP : Làng nước đầu tiên&lt;br/&gt;Phùng Nguyên
    3500-3000 BP : Xã hội phân tầng&lt;br/&gt;Đồng Đậu
    3000-2500 BP : Thủ lĩnh chiến tranh&lt;br/&gt;Gò Mun
    2500-2300 BP : Nhà nước sơ khai&lt;br/&gt;Đông Sơn muộn
    2300-2200 BP : CỔ LOA&lt;br/&gt;Ba vòng thành</code></pre></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-8072-b5cc-ccadb040f411" class="">Trường 4 – Cấu trúc mạng (G)</h3></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80aa-bcb8-fd845ab4ccb7" class="">Cổ Loa là đồ thị không gian – quyền lực:</p></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8095-a2f8-fe15152b5ae1" class="bulleted-list"><li style="list-style-type:disc">Node trung tâm: nội thành (nơi ở của vua An Dương Vương, centrality = 1.0)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80cc-bf9b-d3b984ffc9c5" class="bulleted-list"><li style="list-style-type:disc">Vòng 1: trung thành (quan lại, quân đội tinh nhuệ)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8035-a614-cc71f3d6784a" class="bulleted-list"><li style="list-style-type:disc">Vòng 2: ngoại thành (thợ thủ công, kho tàng)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-803d-865f-eb0835cdaa9c" class="bulleted-list"><li style="list-style-type:disc">Hào nước: edge kép (vừa là biên, vừa là kênh giao thông)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-800c-b7a4-c4f25b976f13" class="bulleted-list"><li style="list-style-type:disc">Cửa ô: gateway nodes kiểm soát luồng người và hàng hóa</li></ul></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80a9-83e2-f304838eae5c" class="">Mermaid đồ thị không gian:</p></div><div style="display:contents" dir="auto"><pre id="361c5e6f-95bd-8082-8099-ddd8459000c4" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">graph TD
    Center[Nội thành&lt;br/&gt;Centrality=1.0] --&gt; Mid1[Vòng thành 1&lt;br/&gt;Quan lại, quân tinh nhuệ]
    Center --&gt; Mid2[Vòng thành 2&lt;br/&gt;Thợ, kho]
    Center --&gt; Mid3[Vòng thành 3&lt;br/&gt;Nông dân, biên phòng]
    Mid1 --&gt; Gate1[Cửa ô Đông]
    Mid1 --&gt; Gate2[Cửa ô Tây]
    Mid2 --&gt; Gate1
    Mid2 --&gt; Gate2
    Mid3 --&gt; Gate1
    Mid3 --&gt; Gate2
    Water1[Hào nước trong] --&gt; Center
    Water1 --&gt; Mid1
    Water2[Hào nước ngoài] --&gt; Mid2
    Water2 --&gt; Mid3
    River[Sông Hoàng] --&gt; Water2
    River --&gt; Water1</code></pre></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-8000-b2ae-d0ba20d054bd" class="">Trường 5 – Động lực thích nghi (Φ)</h3></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80c6-8e1f-d243a25e3238" class="">Cổ Loa được thiết kế để phản ứng với hai loại nhiễu loạn chính:</p></div><div style="display:contents" dir="auto"><ol type="1" id="361c5e6f-95bd-80b7-8852-cbe3b5ce0792" class="numbered-list" start="1"><li><strong>Lũ lụt</strong> (thủy văn): hào nước kết nối sông → điều tiết nước, thoát lũ, đồng thời tạo thành hào chiến đấu</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="361c5e6f-95bd-8024-8830-ce2c77519a73" class="numbered-list" start="2"><li><strong>Xâm lược</strong> (quân sự) : ba vòng thành tạo ra phòng thủ đa lớp, cửa ô tạo choke points, hào nước gây cản trở chiến thuật</li></ol></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-8043-a42c-ea5e2476b0c5" class="">Hệ thống này sống sót (cho đến khi mất vua, theo huyền thoại) vì nó có khả năng thích nghi: thành được gia cố, đào thêm, sửa chữa liên tục. Không phải một cấu trúc cứng chết.</p></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80b0-8292-e5035bf46101" class="">Mermaid vòng thích nghi:</p></div><div style="display:contents" dir="auto"><pre id="361c5e6f-95bd-8094-a866-da4d25fc4229" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">stateDiagram-v2
    [*] --&gt; Bình_thường
    Bình_thường --&gt; Mùa_lũ
    Mùa_lũ --&gt; Hào_đầy
    Hào_đầy --&gt; Điều_tiết_cống
    Điều_tiết_cống --&gt; Thoát_lũ
    Thoát_lũ --&gt; Bình_thường

    Bình_thường --&gt; Quân_xâm_lược
    Quân_xâm_lược --&gt; Cửa_ô_đóng
    Cửa_ô_đóng --&gt; Vòng_1_kháng_cự
    Vòng_1_kháng_cự --&gt; Vòng_2_kháng_cự
    Vòng_2_kháng_cự --&gt; Vòng_3_kháng_cự
    Vòng_3_kháng_cự --&gt; Phản_công
    Phản_công --&gt; Bình_thường</code></pre></div><div style="display:contents" dir="auto"><hr id="361c5e6f-95bd-80a1-a459-c585c68b8163"/></div><div style="display:contents" dir="auto"><h2 id="361c5e6f-95bd-80b2-87de-e7233e371c24" class="">4. Đối tượng 3: Văn minh Đông Sơn</h2></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-8066-afa2-fcb301ee9f88" class="">4.1. Bản chất hệ thống</h3></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80e1-b5d0-d22a2c376377" class="">Văn minh Đông Sơn không phải một &quot;nền văn hóa&quot; khảo cổ học thuần túy. Nó là <strong>máy đồng bộ hóa sinh thái – kỹ thuật – xã hội</strong> (ecological-technical-social synchronizer). Đây là cấp độ cao nhất của fractal: nơi trống đồng (nén) và Cổ Loa (phóng đại) gặp nhau thành một hệ thống vận hành hoàn chỉnh.</p></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-8015-8e64-c3ec1351b29a" class="">4.2. Ánh xạ lên năm trường</h3></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-804d-a99f-e0fbe2d3c3a1" class="">Trường 1 – Độ nén (K)</h3></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-805a-bbb8-dbae0502d31e" class="">K(Đông Sơn) = mô tả ngắn nhất bao gồm:</p></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8031-8181-e7477754fd31" class="bulleted-list"><li style="list-style-type:disc">Văn minh lúa nước (wet-rice civilization)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80bd-a69d-e1024e4ac066" class="bulleted-list"><li style="list-style-type:disc">Lịch mặt trời – mặt trăng</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80e7-bbdb-d41259a7ca64" class="bulleted-list"><li style="list-style-type:disc">Kỹ thuật đồng thau bậc cao</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-803b-8717-d448fa6c0119" class="bulleted-list"><li style="list-style-type:disc">Mạng sông – biển kết nối các làng</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8094-8288-f225708c66da" class="bulleted-list"><li style="list-style-type:disc">Mã âm thanh (trống) cho nghi lễ và quyền lực</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80d5-849b-eba66f92c2bc" class="bulleted-list"><li style="list-style-type:disc">Tầng lớp quý tộc – thủ lĩnh – thợ – nông dân</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80cb-92dd-d506c385a2b0" class="bulleted-list"><li style="list-style-type:disc">Tín ngưỡng tổ tiên và thủy thần</li></ul></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80a6-a9ec-f16451d64c0a" class="">Đây là một bộ nén ở cấp độ văn minh: mọi thứ được nén vào một &quot;lối sống&quot; (water civilization lifestyle) có thể tái tạo ở bất kỳ đâu có sông, đồng bằng, và kỹ thuật đồng.</p></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-8060-96fd-fd65308cd3c5" class="">Mermaid sơ đồ nén văn minh:</p></div><div style="display:contents" dir="auto"><pre id="361c5e6f-95bd-806e-a9bd-ded59c843ca6" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">graph TD
    subgraph &quot;Các lớp nén&quot;
        A[Lớp 1: Sinh thái] --&gt; A1[Sông Hồng, lũ, mùa, phù sa]
        B[Lớp 2: Kỹ thuật] --&gt; B1[Lúa nước, đồng thau, thuyền]
        C[Lớp 3: Xã hội] --&gt; C1[Làng, thủ lĩnh, thợ, nghi lễ]
        D[Lớp 4: Biểu tượng] --&gt; D1[Trống đồng, hoa văn, âm thanh]
    end
    E[Văn minh Đông Sơn&lt;br/&gt;Bộ nén tối thượng] --&gt; A
    E --&gt; B
    E --&gt; C
    E --&gt; D
    F[Hiện thực hóa] --&gt; G[Làng trên sông]
    F --&gt; H[Mộ thuyền, mộ đồng]
    F --&gt; I[Thành Cổ Loa]
    F --&gt; J[Trống đồng phân bố rộng]</code></pre></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-8014-b8d5-e3a4f6672a10" class="">Trường 2 – Entropy cấu trúc (H)</h3></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-807d-9544-d3e71d6ef597" class="">Văn minh Đông Sơn có entropy ở mức hoàn hảo cho một xã hội tiền nhà nước – nhà nước sơ khai:</p></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8094-a926-e011fdf5f309" class="bulleted-list"><li style="list-style-type:disc">Các làng không giống nhau (entropy cao về không gian)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80c0-8f99-f6512d7e3e63" class="bulleted-list"><li style="list-style-type:disc">Nhưng có chung đồ đồng, trống, mộ táng (entropy thấp về vật chất biểu tượng)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80f0-b953-d7e5e8fb9e96" class="bulleted-list"><li style="list-style-type:disc">Nghi lễ có khung chung nhưng chi tiết địa phương khác nhau (entropy trung bình)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80b5-891a-ead28342d4c8" class="bulleted-list"><li style="list-style-type:disc">Ngôn ngữ và mã âm thanh (trống) thống nhất (entropy rất thấp)</li></ul></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-8049-9f15-cd34cbc76796" class="">Đây là một cấu trúc &quot;thống nhất trong đa dạng&quot; (unity in diversity) – bằng chứng của một hệ thống ở rìa hỗn loạn nhưng ổn định.</p></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80cf-96d0-c9a81ec5cfbf" class="">Mermaid phân bố entropy xã hội:</p></div><div style="display:contents" dir="auto"><pre id="361c5e6f-95bd-8048-a79e-d31f9150d0db" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">pie title Entropy của văn minh Đông Sơn
    &quot;Không gian làng (H cao)&quot; : 40
    &quot;Vật chất đồng (H thấp)&quot; : 25
    &quot;Chi tiết nghi lễ (H trung bình)&quot; : 25
    &quot;Mã âm thanh (H rất thấp)&quot; : 10</code></pre></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-80e0-bfeb-c92b3ee78afb" class="">Trường 3 – Độ sâu logic (D)</h3></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-8038-a448-f04dee5bc28a" class="">D(Đông Sơn) là tổng độ sâu của tất cả các tiến trình trước đó, cộng với thời gian đồng bộ hóa toàn hệ thống.</p></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-807d-baca-c5ba09ec05c6" class="">Không có văn minh Đông Sơn nào xuất hiện nếu không có:</p></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-806a-acbc-ec08c153e3f2" class="bulleted-list"><li style="list-style-type:disc">ít nhất 2000 năm tích lũy nông nghiệp lúa nước</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-800a-8225-cfbd32c3039a" class="bulleted-list"><li style="list-style-type:disc">ít nhất 1500 năm tích lũy làng định cư</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8079-892f-cce3577cf587" class="bulleted-list"><li style="list-style-type:disc">ít nhất 1000 năm tích lũy kỹ thuật đồng</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80dc-a8e7-d52c4fd6d9af" class="bulleted-list"><li style="list-style-type:disc">ít nhất 500 năm tích lũy phân tầng xã hội</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80ff-8c17-e55257199e77" class="bulleted-list"><li style="list-style-type:disc">ít nhất 300 năm tích lũy mạng lưới trao đổi sông – biển</li></ul></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-8093-afb1-e5e1dc04c3da" class="">D(Đông Sơn) ≈ 2500 năm tích lũy có hướng (directed accumulation).</p></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80a3-9988-d5f740ea2c68" class="">Mermaid sơ đồ tích lũy xuyên suốt:</p></div><div style="display:contents" dir="auto"><pre id="361c5e6f-95bd-80ba-b92b-d15965837f81" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">timeline
    title Độ sâu logic của văn minh Đông Sơn (D)
    4500-4000 BP : Nông nghiệp lúa nước sơ khai&lt;br/&gt;Phùng Nguyên sớm
    4000-3500 BP : Làng định cư hoàn chỉnh&lt;br/&gt;Phùng Nguyên muộn
    3500-3000 BP : Kỹ thuật đồng bắt đầu&lt;br/&gt;Đồng Đậu
    3000-2700 BP : Đồng thau thành thục&lt;br/&gt;Gò Mun
    2700-2300 BP : Xã hội phân tầng mạnh&lt;br/&gt;Đông Sơn sớm
    2300-2000 BP : VĂN MINH ĐÔNG SƠN&lt;br/&gt;Cực thịnh</code></pre></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-803a-b4a1-c84c5074a4a5" class="">Trường 4 – Cấu trúc mạng (G)</h3></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80c7-ba29-c735be54e658" class="">Văn minh Đông Sơn là một mạng lưới các node (làng, xưởng đúc, mộ táng, bến thuyền) kết nối bằng các edge (sông, biển, đường mòn, quan hệ hôn nhân, trao đổi đồ đồng, nghi lễ chung).</p></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80ed-9f14-dfcd40faa357" class="">Đặc điểm mạng:</p></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-808c-a377-fb607105ab9e" class="bulleted-list"><li style="list-style-type:disc">Các node có phân bố power-law: một số ít làng siêu lớn (Cổ Loa, Làng Cả, Đông Sơn) – <strong>hub</strong> – chiếm centrality cao</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8070-8c83-dec42a8dac8f" class="bulleted-list"><li style="list-style-type:disc">Đa số làng nhỏ – <strong>periphery</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8049-a3a3-e8a13efcd438" class="bulleted-list"><li style="list-style-type:disc">Edge dày đặc trong vùng đồng bằng sông Hồng, thưa dần ra ngoài</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-80aa-8c30-ed4dae66e5fb" class="bulleted-list"><li style="list-style-type:disc">Trống đồng và mộ thuyền là <strong>strong ties</strong> (kết nối bền chặt qua biểu tượng)</li></ul></div><div style="display:contents" dir="auto"><ul id="361c5e6f-95bd-8031-9c25-ce1b7e3cccf4" class="bulleted-list"><li style="list-style-type:disc">Mạng này có tính modularity cao: mỗi vùng (sông Hồng, sông Mã, sông Cả) là một module riêng nhưng kết nối qua trao đổi đồng</li></ul></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80d3-8404-e7ce16044eb2" class="">Mermaid đồ thị mạng lưới:</p></div><div style="display:contents" dir="auto"><pre id="361c5e6f-95bd-801c-94f4-fec72c6c7c95" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">graph LR
    subgraph &quot;Hub&quot;
        CL[Cổ Loa]
        DS[Đông Sơn]
        LC[Làng Cả]
    end
    subgraph &quot;Sông Hồng&quot;
        H1[Làng A]
        H2[Làng B]
        H3[Làng C]
    end
    subgraph &quot;Sông Mã&quot;
        M1[Làng D]
        M2[Làng E]
    end
    subgraph &quot;Sông Cả&quot;
        C1[Làng F]
        C2[Làng G]
    end
    CL --- DS
    CL --- LC
    DS --- LC
    CL --- H1
    CL --- H2
    DS --- M1
    DS --- M2
    LC --- C1
    LC --- C2
    H1 --- H2
    H1 --- H3
    M1 --- M2
    C1 --- C2</code></pre></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-80e5-a392-fe2b479f79f6" class="">Trường 5 – Động lực thích nghi (Φ)</h3></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-8053-b3b2-d112f41cbf1d" class="">Văn minh Đông Sơn tồn tại và mở rộng vì nó có khả năng thích nghi với ba biến động lớn:</p></div><div style="display:contents" dir="auto"><ol type="1" id="361c5e6f-95bd-8001-ba84-c3f6776f75ed" class="numbered-list" start="1"><li><strong>Lũ lụt chu kỳ</strong> (cyclic floods): hệ thống làng nổi, nhà sàn, đê điều sơ khai, di chuyển theo mùa</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="361c5e6f-95bd-808d-a703-fb8a16a2af12" class="numbered-list" start="2"><li><strong>Biến đổi khí hậu</strong> (climate shifts): khả năng chuyển đổi giữa lúa nước và đánh bắt cá, hái lượm</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="361c5e6f-95bd-80fa-9c42-fb5b8c822011" class="numbered-list" start="3"><li><strong>Áp lực quân sự từ phía Bắc</strong> (northern military pressure): phản ứng bằng cách tập trung hóa quyền lực (Cổ Loa) và chuẩn hóa vũ khí đồng (giáo, rìu, mũi tên đồng)</li></ol></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-8076-b970-da7043cff65e" class="">Hệ thống không cố định: từ Phùng Nguyên đến Đông Sơn có sự gia tăng liên tục về độ phức tạp, kích thước mạng, và khả năng phòng thủ. Đây là bằng chứng của một hệ thống <strong>thích nghi tích cực</strong> (active adaptation), không phải trì trệ.</p></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-804c-b4da-e06b33a44227" class="">Mermaid vòng thích nghi văn minh:</p></div><div style="display:contents" dir="auto"><pre id="361c5e6f-95bd-80a7-91b6-ca2114e785d2" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">stateDiagram-v2
    [*] --&gt; Chu_kỳ_lũ
    Chu_kỳ_lũ --&gt; Thích_nghi_nông_nghiệp
    Thích_nghi_nông_nghiệp --&gt; Thặng_dư
    Thặng_dư --&gt; Kỹ_thuật_đồng
    Kỹ_thuật_đồng --&gt; Trao_đổi_mở_rộng
    Trao_đổi_mở_rộng --&gt; Tập_trung_quyền_lực
    Tập_trung_quyền_lực --&gt; Xây_Cổ_Loa
    Xây_Cổ_Loa --&gt; Áp_lực_Bắc_thuộc
    Áp_lực_Bắc_thuộc --&gt; Hấp_thụ_biến_đổi
    Hấp_thụ_biến_đổi --&gt; Chu_kỳ_lũ</code></pre></div><div style="display:contents" dir="auto"><hr id="361c5e6f-95bd-8055-b929-dbb765dc8867"/></div><div style="display:contents" dir="auto"><h2 id="361c5e6f-95bd-809c-b7bf-d827dd78251e" class="">5. Ánh xạ fractal tổng thể: từ vũ trụ đến con người</h2></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-801e-8598-f16ce5c182d0" class="">Báo cáo này khẳng định rằng cả ba đối tượng – trống đồng, Cổ Loa, văn minh Đông Sơn – đều là biểu hiện ở các thang đo khác nhau của <strong>cùng một cấu trúc fractal</strong>.</p></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-808d-8b60-d1df3849e502" class="">Cấu trúc đó được định nghĩa là:</p></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80e9-9e99-e1f27c68251e" class=""><strong>TÂM → TRƯỜNG → VÒNG → BIÊN → CHU KỲ → TÍN HIỆU → KÝ ỨC</strong></p></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-8005-aa64-ef439787271f" class="">Ánh xạ qua các thang đo:</p></div><div style="display:contents" dir="ltr"><table id="361c5e6f-95bd-800c-9f52-cf697675c8cf" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-8073-bdc3-e6f4b6f3eb45"><th id="kbQt" class="simple-table-header-color simple-table-header">Thang đo</th><th id="HJ@X" class="simple-table-header-color simple-table-header">TÂM</th><th id="UuHy" class="simple-table-header-color simple-table-header">TRƯỜNG</th><th id="EThQ" class="simple-table-header-color simple-table-header">VÒNG</th><th id="uu&lt;U" class="simple-table-header-color simple-table-header">BIÊN</th><th id="qo&lt;d" class="simple-table-header-color simple-table-header">CHU KỲ</th><th id="goIS" class="simple-table-header-color simple-table-header">TÍN HIỆU</th><th id="p?:l" class="simple-table-header-color simple-table-header">KÝ ỨC</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-805f-8e04-c81acb2ff695"><td id="kbQt" class=""><strong>Vũ trụ vật lý</strong></td><td id="HJ@X" class="">Sgr A* (lỗ đen trung tâm Ngân Hà)</td><td id="UuHy" class="">Trường hấp dẫn</td><td id="EThQ" class="">Quỹ đạo sao</td><td id="uu&lt;U" class="">Chân trời sự kiện</td><td id="qo&lt;d" class="">Quay quanh tâm</td><td id="goIS" class="">Bức xạ</td><td id="p?:l" class="">Cấu trúc thiên hà</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-80ee-9212-e1a43514325c"><td id="kbQt" class=""><strong>Sinh thái Đông Nam Á</strong></td><td id="HJ@X" class="">Mặt trời</td><td id="UuHy" class="">Ánh sáng, nhiệt</td><td id="EThQ" class="">Mùa: mưa – khô</td><td id="uu&lt;U" class="">Rìa rừng – biển</td><td id="qo&lt;d" class="">Ngày – đêm, năm</td><td id="goIS" class="">Nước lên – xuống</td><td id="p?:l" class="">Chu kỳ sinh tử</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-8018-8020-d529dfc937c2"><td id="kbQt" class=""><strong>Trống đồng</strong></td><td id="HJ@X" class="">Mặt trời trên mặt trống</td><td id="UuHy" class="">Vòng hoa văn</td><td id="EThQ" class="">Chim, thuyền, người xoay</td><td id="uu&lt;U" class="">Rìa trống</td><td id="qo&lt;d" class="">Nghi lễ đánh trống</td><td id="goIS" class="">Âm thanh cộng hưởng</td><td id="p?:l" class="">Ký ức cộng đồng</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-8076-9a0c-fa4b99f3ea8c"><td id="kbQt" class=""><strong>Cổ Loa</strong></td><td id="HJ@X" class="">Nội thành (lõi quyền lực)</td><td id="UuHy" class="">Ba vòng thành</td><td id="EThQ" class="">Vòng 1,2,3</td><td id="uu&lt;U" class="">Hào nước – sông</td><td id="qo&lt;d" class="">Phòng thủ – phản công</td><td id="goIS" class="">Cửa ô, tín hiệu</td><td id="p?:l" class="">Ký ức nhà nước</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-80aa-8d32-f5343cb1d9fa"><td id="kbQt" class=""><strong>Văn minh Đông Sơn</strong></td><td id="HJ@X" class="">Làng trung tâm (hub)</td><td id="UuHy" class="">Vùng ảnh hưởng</td><td id="EThQ" class="">Lớp làng: gần – xa</td><td id="uu&lt;U" class="">Biên lãnh thổ</td><td id="qo&lt;d" class="">Mùa lũ – mùa khô</td><td id="goIS" class="">Trống, thuyền, đồ đồng</td><td id="p?:l" class="">Ký ức tổ tiên</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-80e1-bb87-ee330357b8a6"><td id="kbQt" class=""><strong>Con người</strong></td><td id="HJ@X" class="">Tánh thấy / ý thức</td><td id="UuHy" class="">Cảm xúc, suy nghĩ</td><td id="EThQ" class="">Thói quen, hành vi</td><td id="uu&lt;U" class="">Biên thân thể</td><td id="qo&lt;d" class="">Hơi thở, nhịp tim</td><td id="goIS" class="">Lời nói, hành động</td><td id="p?:l" class="">Ký ức cá nhân</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80da-8326-c32232da156c" class="">Mermaid fractal tổng thể:</p></div><div style="display:contents" dir="auto"><pre id="361c5e6f-95bd-80c2-801f-d93eb7780550" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">graph TD
    subgraph &quot;Tầng 1: Vũ trụ&quot;
        U[Lỗ đen trung tâm] --&gt; U1[Trường hấp dẫn]
        U1 --&gt; U2[Quỹ đạo]
        U2 --&gt; U3[Chân trời]
    end
    subgraph &quot;Tầng 2: Sinh thái&quot;
        E[Mặt trời] --&gt; E1[Mùa mưa/khô]
        E1 --&gt; E2[Lũ - cạn]
        E2 --&gt; E3[Rìa sông - biển]
    end
    subgraph &quot;Tầng 3: Trống đồng&quot;
        D[Mặt trời tâm] --&gt; D1[Hoa văn vòng]
        D1 --&gt; D2[Chim/thuyền/người]
        D2 --&gt; D3[Rìa trống]
    end
    subgraph &quot;Tầng 4: Cổ Loa&quot;
        C[Nội thành] --&gt; C1[Vòng thành]
        C1 --&gt; C2[Trung - ngoại thành]
        C2 --&gt; C3[Hào nước]
    end
    subgraph &quot;Tầng 5: Văn minh&quot;
        V[Làng trung tâm] --&gt; V1[Vùng ảnh hưởng]
        V1 --&gt; V2[Làng xa]
        V2 --&gt; V3[Biên lãnh thổ]
    end
    subgraph &quot;Tầng 6: Con người&quot;
        H[Tánh thấy] --&gt; H1[Cảm xúc]
        H1 --&gt; H2[Hành vi]
        H2 --&gt; H3[Thân thể]
    end
    U --&gt; E
    E --&gt; D
    D --&gt; C
    C --&gt; V
    V --&gt; H</code></pre></div><div style="display:contents" dir="auto"><hr id="361c5e6f-95bd-8068-bf63-f36abef32dba"/></div><div style="display:contents" dir="auto"><h2 id="361c5e6f-95bd-806a-bb67-fb71e824f333" class="">6. Các hằng số vận hành (operational constants)</h2></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-8032-9346-d1bc7e7d32b5" class="">Báo cáo xác định các hằng số xuất hiện xuyên suốt cả ba hệ thống. Đây không phải hằng số vật lý mà là <strong>hằng số cấu trúc – nhận thức – văn hóa</strong>.</p></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-809d-9f60-c00cfa07ab5c" class="">6.1. Hằng số hình học</h3></div><div style="display:contents" dir="ltr"><table id="361c5e6f-95bd-800c-b147-cab554824e29" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-8011-b93d-f25938677ac7"><th id="Kfpd" class="simple-table-header-color simple-table-header">Hằng số</th><th id="r}dK" class="simple-table-header-color simple-table-header">Biểu hiện trong trống đồng</th><th id="e;mw" class="simple-table-header-color simple-table-header">Biểu hiện trong Cổ Loa</th><th id="xCZM" class="simple-table-header-color simple-table-header">Biểu hiện trong văn minh Đông Sơn</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-80c1-a02c-c0b64924c6a7"><td id="Kfpd" class=""><strong>π</strong> (tỷ lệ chu vi/đường kính)</td><td id="r}dK" class="">Mặt trống tròn, vòng tròn đồng tâm</td><td id="e;mw" class="">Thành vòng tròn</td><td id="xCZM" class="">Chu kỳ tròn của mùa, năm, lũ</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-8017-8e60-d67b4d03b8c0"><td id="Kfpd" class=""><strong>τ = 2π</strong> (một vòng đầy đủ)</td><td id="r}dK" class="">Một vòng hoa văn hoàn chỉnh</td><td id="e;mw" class="">Một vòng thành khép kín</td><td id="xCZM" class="">Một chu kỳ nghi lễ hoàn chỉnh</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-8078-8f93-f415b56586f0"><td id="Kfpd" class=""><strong>φ</strong> (tỷ lệ vàng, phân nhánh)</td><td id="r}dK" class="">Chim, thuyền, người phân bố theo nhánh</td><td id="e;mw" class="">Cửa ô, đường phân nhánh từ tâm</td><td id="xCZM" class="">Mạng sông – làng phân nhánh tự nhiên</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-8085-9fe9-eb25d769d18d" class="">6.2. Hằng số số học cơ thể – bầu trời – nước</h3></div><div style="display:contents" dir="ltr"><table id="361c5e6f-95bd-8005-ad3a-eff7c9e3eaf2" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-809d-9fe9-fa18d96dad14"><th id="Q;@K" class="simple-table-header-color simple-table-header">Hằng số</th><th id="Ytkg" class="simple-table-header-color simple-table-header">Giá trị</th><th id="gKFa" class="simple-table-header-color simple-table-header">Biểu hiện</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-807a-be41-f7216a0a8f96"><td id="Q;@K" class=""><strong>Phân cực nhị phân</strong></td><td id="Ytkg" class="">2</td><td id="gKFa" class="">Âm/dương, sáng/tối, lên/xuống, đục/trong</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-8084-94c2-c8a6c817c705"><td id="Q;@K" class=""><strong>Bộ ba trời – người – đất</strong></td><td id="Ytkg" class="">3</td><td id="gKFa" class="">Mặt trời – thủ lĩnh – ruộng, Trống – nghi lễ – cộng đồng</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-80c2-b734-c90c2d62b25f"><td id="Q;@K" class=""><strong>Bốn phương / bốn mùa</strong></td><td id="Ytkg" class="">4</td><td id="gKFa" class="">Hướng trên trống, bốn cửa ô (sơ khai), bốn hướng làng</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-8096-adb0-e09a10e22cee"><td id="Q;@K" class=""><strong>Ngũ hành / bàn tay</strong></td><td id="Ytkg" class="">5</td><td id="gKFa" class="">Năm lớp motif (nếu đếm), năm thành phần xã hội</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-8060-b429-eb98aa142c61"><td id="Q;@K" class=""><strong>Sáu hướng ổn định</strong></td><td id="Ytkg" class="">6</td><td id="gKFa" class="">Chia vòng trống thành 6 phần (một số trống), lục giác trong hoa văn</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-802f-a336-c8f2e79892ec"><td id="Q;@K" class=""><strong>Hai bàn tay</strong></td><td id="Ytkg" class="">10</td><td id="gKFa" class="">Hệ đếm, phân chia motif</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-8076-b725-ce17338aa6b3"><td id="Q;@K" class=""><strong>Mười hai tháng / đốt ngón</strong></td><td id="Ytkg" class="">12</td><td id="gKFa" class="">Chu kỳ trăng, vòng chim 12 con (giả thuyết)</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-8090-b43b-ed08dcacce8b"><td id="Q;@K" class=""><strong>Hai vòng 12 / 24 tiết khí</strong></td><td id="Ytkg" class="">24</td><td id="gKFa" class="">Ngày đêm, thời vụ</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-8020-81e7-c4268df78afb"><td id="Q;@K" class=""><strong>Chu kỳ trăng</strong></td><td id="Ytkg" class="">28–29.5</td><td id="gKFa" class="">Lịch âm, nghi lễ trăng</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-8093-bb9e-cf905a5d2cb4"><td id="Q;@K" class=""><strong>Hợp số 5×12</strong></td><td id="Ytkg" class="">60</td><td id="gKFa" class="">Chu kỳ hỗn hợp (âm dương lịch sau này)</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-805b-bc97-ef29e22d15af"><td id="Q;@K" class=""><strong>Vòng trời 360</strong></td><td id="Ytkg" class="">360</td><td id="gKFa" class="">Một vòng năm xấp xỉ, vòng tròn chia độ</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h3 id="361c5e6f-95bd-8038-88bd-d900b13c764d" class="">6.3. Hằng số văn minh nước</h3></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-801c-8127-d98712015c8a" class="">Đây là các biến số môi trường không đổi (trong thang thời gian nhân văn) mà văn minh Đông Sơn phải đáp ứng:</p></div><div style="display:contents" dir="ltr"><table id="361c5e6f-95bd-80f1-9ec5-dff8726bed8d" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-80e2-aad3-d41e81c1bb95"><th id="Pni&lt;" class="simple-table-header-color simple-table-header">Hằng số</th><th id="yDd`" class="simple-table-header-color simple-table-header">Dạng thức</th><th id="@Ye]" class="simple-table-header-color simple-table-header">Tác động lên hệ thống</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-8025-958d-c5d039b5ec9d"><td id="Pni&lt;" class=""><strong>Lũ</strong></td><td id="yDd`" class="">Hàng năm, dâng cao</td><td id="@Ye]" class="">Bắt buộc phải có nhà sàn, di chuyển, quản lý nước</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-8062-bfa1-f0e2e1e65b04"><td id="Pni&lt;" class=""><strong>Mưa mùa</strong></td><td id="yDd`" class="">Theo chu kỳ gió mùa</td><td id="@Ye]" class="">Định hình lịch canh tác, lịch nghi lễ</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-80f1-982d-c3c4309c6956"><td id="Pni&lt;" class=""><strong>Triều</strong> (vùng ven biển)</td><td id="yDd`" class="">Lên xuống hàng ngày</td><td id="@Ye]" class="">Ảnh hưởng giao thông sông – biển</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-80b5-bd8e-cc47ba397043"><td id="Pni&lt;" class=""><strong>Dòng chảy</strong></td><td id="yDd`" class="">Liên tục</td><td id="@Ye]" class="">Mạng kết nối, không có điểm dừng tuyệt đối</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-80eb-b222-f9acc313533b"><td id="Pni&lt;" class=""><strong>Bồi lắng phù sa</strong></td><td id="yDd`" class="">Mùa lũ</td><td id="@Ye]" class="">Tái tạo độ màu mỡ, thay đổi địa hình chậm</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-8020-b828-ca26621141a5"><td id="Pni&lt;" class=""><strong>Đục – trong</strong></td><td id="yDd`" class="">Theo mùa</td><td id="@Ye]" class="">Ảnh hưởng đánh bắt, uống, tắm, biểu tượng</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-80c4-98f0-d263d130789a"><td id="Pni&lt;" class=""><strong>Mùa cá / chim</strong></td><td id="yDd`" class="">Theo chu kỳ</td><td id="@Ye]" class="">Định hình nguồn protein, di cư, nghi lễ</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="361c5e6f-95bd-802a-bc03-dc689015c17f"/></div><div style="display:contents" dir="auto"><h2 id="361c5e6f-95bd-80d9-a5d2-c9c72a5a48ca" class="">7. Kết luận và luận điểm chính</h2></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80b8-b175-ee4e6c16b553" class="">Báo cáo này khẳng định ba luận điểm sau, không khiêm tốn, có cơ sở từ ánh xạ năm trường độ phức tạp:</p></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80f6-b92d-ff16d24fb014" class=""><strong>Luận điểm 1:</strong> Trống đồng Đông Sơn, thành Cổ Loa, và văn minh Đông Sơn là ba biểu hiện ở ba thang đo khác nhau của cùng một cấu trúc fractal: <strong>tâm → trường → vòng → biên → chu kỳ → tín hiệu → ký ức</strong>. Không có sự ngẫu nhiên. Không có sự &quot;trang trí đơn thuần&quot;.</p></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80aa-a593-d8670ff5b78c" class=""><strong>Luận điểm 2:</strong> Văn minh Đông Sơn đạt được độ phức tạp cao nhất trong số các xã hội tiền công nghiệp ở khu vực Đông Nam Á vì nó duy trì thành công trạng thái &quot;rìa hỗn loạn&quot; (edge of chaos): đủ trật tự để nén thông tin thành trống đồng và Cổ Loa; đủ hỗn loạn (biến thể, thích nghi) để sống sót qua lũ lụt, biến đổi khí hậu, và áp lực quân sự trong gần 1000 năm.</p></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-8017-bf1d-ec46ccad7529" class=""><strong>Luận điểm 3:</strong> Các hằng số vận hành của ba hệ thống này – từ hình học π và φ, đến số học 2,3,4,5,12,24,60,360, đến các hằng số văn minh nước như lũ, mưa, triều, dòng, bồi, đục, trong – không phải ngẫu nhiên trùng hợp. Chúng là <strong>bộ mã nén</strong> (compression code) của một hệ thống tri thức cổ đã đạt đến độ tinh vi có thể so sánh với các hệ thống complexity hiện đại, chỉ khác ở vật liệu biểu đạt (đồng, đất, nước, âm thanh thay vì silicon và mã nhị phân).</p></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-805d-a656-e26ed1ebd319" class=""><strong>Luận điểm cuối:</strong> Nếu có một &quot;công thức&quot; tổng quát cho văn minh Đông Sơn, nó là:</p></div><div style="display:contents" dir="auto"><blockquote id="361c5e6f-95bd-80d5-be17-e11c44bce663" class=""><strong>Đông Sơn = (Văn minh lúa nước) × (Lịch mặt trời – mặt trăng) × (Kỹ thuật đồng thau) × (Mã âm thanh trống) × (Mạng sông – làng – mộ) × (Tín ngưỡng tổ tiên – thủy thần) / (Entropy quân sự + Entropy lũ lụt)</strong></blockquote></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-80fb-987a-cc5d17ce9d3d" class="">Tử số là tích của sáu yếu tố cốt lõi. Mẫu số là các lực gây rối loạn. Hệ thống tồn tại khi tử số lớn hơn mẫu số – tức là khi độ nén, entropy tối ưu, độ sâu logic, cấu trúc mạng, và động lực thích nghi vượt qua nhiễu loạn từ môi trường và con người.</p></div><div style="display:contents" dir="auto"><hr id="361c5e6f-95bd-80b4-8401-d94645c06354"/></div><div style="display:contents" dir="auto"><h2 id="361c5e6f-95bd-8013-b576-c695797c7a76" class="">Phụ lục: Bảng ánh xạ tóm tắt năm trường vào ba đối tượng</h2></div><div style="display:contents" dir="ltr"><table id="361c5e6f-95bd-80c8-8b5d-e138d0fcefc4" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-8068-8c25-c63b3772caa7"><th id="&gt;[;M" class="simple-table-header-color simple-table-header">Trường</th><th id="yETU" class="simple-table-header-color simple-table-header">Trống đồng</th><th id="Yb^c" class="simple-table-header-color simple-table-header">Cổ Loa</th><th id="Pduo" class="simple-table-header-color simple-table-header">Văn minh Đông Sơn</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-80d5-a3bf-d17ee1d99fa6"><td id="&gt;[;M" class=""><strong>K (độ nén)</strong></td><td id="yETU" class="">Cực cao (văn minh nén vào một mặt tròn)</td><td id="Yb^c" class="">Cao (quyền lực nén vào ba vòng thành)</td><td id="Pduo" class="">Rất cao (toàn bộ lối sống nén vào lúa nước + đồng + trống)</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-80a8-a387-c97a9b33f3ab"><td id="&gt;[;M" class=""><strong>H (entropy)</strong></td><td id="yETU" class="">Vừa phải, có phân tầng rõ</td><td id="Yb^c" class="">Thấp – trung bình (quân sự)</td><td id="Pduo" class="">Hỗn hợp: làng H cao, đồ đồng H thấp</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-80c6-a8da-eeee72dd1e9a"><td id="&gt;[;M" class=""><strong>D (độ sâu)</strong></td><td id="yETU" class="">&gt; 2000 năm tích lũy</td><td id="Yb^c" class="">&gt; 2500 năm tích lũy</td><td id="Pduo" class="">&gt; 2500 năm tích lũy toàn hệ</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-809f-91f0-ca7fcd7422f0"><td id="&gt;[;M" class=""><strong>G (mạng)</strong></td><td id="yETU" class="">Mạng motif hình sao – vòng</td><td id="Yb^c" class="">Mạng không gian phân cấp</td><td id="Pduo" class="">Mạng lưới làng – sông – mộ – trống phân bố power-law</td></tr></div><div style="display:contents" dir="ltr"><tr id="361c5e6f-95bd-80b5-8dba-f6d20e409961"><td id="&gt;[;M" class=""><strong>Φ (động lực)</strong></td><td id="yETU" class="">Kích hoạt theo mùa/nghi lễ</td><td id="Yb^c" class="">Phòng thủ đa lớp, thích nghi lũ</td><td id="Pduo" class="">Đồng bộ hóa sinh thái – xã hội – quân sự qua thời gian</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="361c5e6f-95bd-8041-905e-c9c22f3c259b" class=""><strong>Hết báo cáo.</strong></p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
