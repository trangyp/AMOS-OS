---
tags: [tech-coding]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Tech Partner Audit</title><style>
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
	
</style></head><body><article id="285c5e6f-95bd-805a-9893-f59831153ae5" class="page sans"><header><h1 class="page-title" dir="auto">Tech Partner Audit</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="285c5e6f-95bd-807f-a162-cb0210501ea8" class=""><strong>I. KẾT LUẬN CHUNG</strong></h2></div><div style="display:contents" dir="auto"><p id="285c5e6f-95bd-80e3-b040-c84780e22b45" class=""><strong>Đối tác này không đạt chuẩn để trở thành nhà phát triển công nghệ lõi (Core Tech Partner)</strong> cho hệ sinh thái UniTaxi – UniLogistic – UniPower.</p></div><div style="display:contents" dir="auto"><p id="285c5e6f-95bd-8000-bd0e-d1f17bf9ce3e" class="">Tuy có kinh nghiệm trong fintech và nền tảng thanh toán, nhưng <strong>chưa đáp ứng tiêu chuẩn về pháp lý, an ninh mạng, năng lực hệ thống, và khả năng mở rộng thương mại.</strong></p></div><div style="display:contents" dir="auto"><p id="285c5e6f-95bd-806b-a974-f5468860d4b6" class="">Mức độ rủi ro tổng hợp: <strong>Cao (Level 4/5)</strong></p></div><div style="display:contents" dir="auto"><p id="285c5e6f-95bd-808d-bf1d-c9f985d8188b" class="">→ Chỉ nên sử dụng làm <strong>nhà tư vấn công nghệ phụ trợ</strong>, <em>không giao vai trò phát triển lõi hoặc quản trị dữ liệu người dùng</em>.</p></div><div style="display:contents" dir="auto"><hr id="285c5e6f-95bd-8003-8035-c0138311b1d5"/></div><div style="display:contents" dir="auto"><h2 id="285c5e6f-95bd-80c6-8639-f9b132e77b2d" class=""><strong>II. PHÂN TÍCH THEO TRỤC CÔNG NGHỆ</strong></h2></div><div style="display:contents" dir="ltr"><table id="285c5e6f-95bd-80a2-8b33-e799d9a1828d" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-80e0-91f8-d3cdbee2a7b0"><th id="zot@" class="simple-table-header-color simple-table-header"><strong>Hạng mục</strong></th><th id="k{~f" class="simple-table-header-color simple-table-header" style="width:156px"><strong>Đánh giá</strong></th><th id="z=Gj" class="simple-table-header-color simple-table-header" style="width:335px"><strong>Ghi chú</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-806c-92b3-f5c3a35593dd"><td id="zot@" class=""><strong>Hạ tầng bản đồ (Mapping Engine)</strong></td><td id="k{~f" class="" style="width:156px">⚠️ Không đạt</td><td id="z=Gj" class="" style="width:335px">Dựa hoàn toàn vào Google Maps API, chưa có bản đồ nội địa. Không có license riêng, không được Google cho phép thanh toán tại VN → rủi ro cao về license.</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-80e9-a747-ec8fbb0c03cf"><td id="zot@" class=""><strong>Độ chính xác định vị (GPS Accuracy)</strong></td><td id="k{~f" class="" style="width:156px">⚠️ Trung bình</td><td id="z=Gj" class="" style="width:335px">Độ sai số 5–10 m, chưa chứng minh khả năng vận hành ổn định với 10.000+ phương tiện.</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-80cc-9e4e-f3bdfd8b92d0"><td id="zot@" class=""><strong>Kiến trúc server &amp; dữ liệu</strong></td><td id="k{~f" class="" style="width:156px">❌ Không đạt</td><td id="z=Gj" class="" style="width:335px">Chưa có hạ tầng máy chủ độc lập; hiện đang thuê tạm hoặc “test lab”, không đảm bảo chuẩn ISO 27001 hay Luật An ninh mạng.</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-8067-8a83-ea7a9d009851"><td id="zot@" class=""><strong>Khả năng xử lý song song (Scalability)</strong></td><td id="k{~f" class="" style="width:156px">⚠️ Yếu</td><td id="z=Gj" class="" style="width:335px">Chưa test tải thực tế; năng lực chịu tải dưới 1 triệu user chỉ là tuyên bố miệng, không có benchmark.</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-8045-9751-d2154cb65577"><td id="zot@" class=""><strong>Fintech Integration (Thanh toán)</strong></td><td id="k{~f" class="" style="width:156px">⚠️ Nguy cơ cao</td><td id="z=Gj" class="" style="width:335px">Có kinh nghiệm kết nối ngân hàng, nhưng chưa có giấy phép trung gian thanh toán (Payment Gateway License). Giao dịch “membership” tiềm ẩn rủi ro vi phạm Nghị định 40 (bán hàng đa cấp).</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-8026-97ff-d7b4e5116fc3"><td id="zot@" class=""><strong>An ninh mạng (Cybersecurity)</strong></td><td id="k{~f" class="" style="width:156px">❌ Không đạt</td><td id="z=Gj" class="" style="width:335px">Không có hệ thống bảo mật hoặc SOC. Nhiều mô tả cho thấy logic xử lý giao dịch chưa đạt yêu cầu NĐ 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân.</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-80d7-9c2b-d60b9037b24f"><td id="zot@" class=""><strong>Hạ tầng vận hành AI/Logistics</strong></td><td id="k{~f" class="" style="width:156px">⚠️ Thô sơ</td><td id="z=Gj" class="" style="width:335px">Chỉ mới xử lý tuyến bằng thuật toán khoảng cách, chưa có Dynamic Routing hoặc Energy-Aware Scheduling. Không có năng lực AI nội bộ.</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="285c5e6f-95bd-80fa-a777-def49d804611" class=""><strong>Tổng kết công nghệ:</strong></p></div><div style="display:contents" dir="auto"><p id="285c5e6f-95bd-8077-98f5-e48fee289547" class="">Mức độ sẵn sàng thực tế (Technology Readiness Level – TRL): <strong>4/9 (Prototype Phase)</strong></p></div><div style="display:contents" dir="auto"><p id="285c5e6f-95bd-80d1-800d-c0e9bc67a433" class="">→ Cần 6–12 tháng tái cấu trúc toàn bộ nếu muốn thương mại hóa trong UniTaxi.</p></div><div style="display:contents" dir="auto"><hr id="285c5e6f-95bd-8044-9ce4-ca598ff7dc1c"/></div><div style="display:contents" dir="auto"><h2 id="285c5e6f-95bd-80d4-a366-fc3d3b44f8dd" class=""><strong>III. PHÁP LÝ &amp; TUÂN THỦ</strong></h2></div><div style="display:contents" dir="ltr"><table id="285c5e6f-95bd-803a-9b90-d6c4badc7c4e" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-806f-878b-d1534b450061"><th id="KO?O" class="simple-table-header-color simple-table-header"><strong>Mảng</strong></th><th id=":YcY" class="simple-table-header-color simple-table-header" style="width:375px"><strong>Phân tích</strong></th><th id="W?ou" class="simple-table-header-color simple-table-header" style="width:93px"><strong>Trạng thái</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-804b-8825-f6aab4057eed"><td id="KO?O" class=""><strong>Giấy phép trung gian thanh toán</strong></td><td id=":YcY" class="" style="width:375px">Không có. Đang “xin” qua ngân hàng đối tác → không đủ điều kiện hoạt động fintech thương mại.</td><td id="W?ou" class="" style="width:93px">❌</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-8054-b746-c496551ef141"><td id="KO?O" class=""><strong>Giấy phép kinh doanh năng lượng (EaaS)</strong></td><td id=":YcY" class="" style="width:375px">Không có. Dễ vi phạm Luật Điện lực nếu thu tiền điện trực tiếp.</td><td id="W?ou" class="" style="width:93px">❌</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-802d-a9ea-fa70168b53ad"><td id="KO?O" class=""><strong>Giấy phép thương mại đa cấp (F1–F2)</strong></td><td id=":YcY" class="" style="width:375px">Cấu trúc chia % doanh thu F1/F2 tiềm ẩn rủi ro bị xếp vào mô hình “đa cấp tài chính”.</td><td id="W?ou" class="" style="width:93px">⚠️</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-807e-bbe2-d17b7d80f884"><td id="KO?O" class=""><strong>Quản lý dữ liệu cá nhân</strong></td><td id=":YcY" class="" style="width:375px">Không có biện pháp lưu trữ an toàn hoặc cơ chế xóa dữ liệu. Vi phạm tiềm tàng NĐ 13/2023.</td><td id="W?ou" class="" style="width:93px">❌</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-8001-8f56-e85bef1ae677"><td id="KO?O" class=""><strong>Thuế &amp; hóa đơn điện tử</strong></td><td id=":YcY" class="" style="width:375px">Không có cơ chế xuất hóa đơn tự động; chưa tuân NĐ 123/2020/TT-BTC.</td><td id="W?ou" class="" style="width:93px">⚠️</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-8030-8cee-c4129a2f8d81"><td id="KO?O" class=""><strong>Hợp đồng pháp nhân / cấu trúc BCC</strong></td><td id=":YcY" class="" style="width:375px">Mô hình hợp tác lỏng, không rõ ranh giới giữa tư vấn và chủ sở hữu IP.</td><td id="W?ou" class="" style="width:93px">⚠️</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="285c5e6f-95bd-80b6-8f02-d01c098f0794" class=""><strong>Kết luận pháp lý:</strong></p></div><div style="display:contents" dir="auto"><p id="285c5e6f-95bd-8039-9757-dc1adab98518" class="">→ <strong>Nguy cơ pháp lý cao</strong>, có thể dẫn tới <strong>tạm đình chỉ hoặc bị thanh tra</strong> nếu vận hành quy mô lớn mà không có giấy phép fintech chính thức.</p></div><div style="display:contents" dir="auto"><hr id="285c5e6f-95bd-802a-a6c8-ea2238dcd80c"/></div><div style="display:contents" dir="auto"><h2 id="285c5e6f-95bd-809e-a72c-d6936c9ba720" class=""><strong>IV. VẬN HÀNH &amp; NĂNG LỰC TRIỂN KHAI</strong></h2></div><div style="display:contents" dir="ltr"><table id="285c5e6f-95bd-80a9-bde0-fd018023e28b" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-80fd-a73e-df8ff08dff3c"><th id="_\Un" class="simple-table-header-color simple-table-header"><strong>Hạng mục</strong></th><th id="K^=Z" class="simple-table-header-color simple-table-header"><strong>Đánh giá</strong></th><th id="t:Jr" class="simple-table-header-color simple-table-header"><strong>Ghi chú</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-80dd-bf96-fe86a5a6a1c1"><td id="_\Un" class=""><strong>Kinh nghiệm triển khai thực tế</strong></td><td id="K^=Z" class="">⚠️ Chưa rõ ràng</td><td id="t:Jr" class="">Có kinh nghiệm với Mai Linh và Morabay, nhưng chưa có case thương mại quy mô.</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-80ab-9cd9-eb5b357b20ee"><td id="_\Un" class=""><strong>Đội ngũ kỹ thuật</strong></td><td id="K^=Z" class="">⚠️ Giới hạn</td><td id="t:Jr" class="">6 lập trình viên, làm việc thời vụ. Không có DevOps hoặc QA chuyên biệt.</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-809a-85db-f5ead3d9f73a"><td id="_\Un" class=""><strong>Khả năng vận hành 200–1.000 xe (Q4/2025)</strong></td><td id="K^=Z" class="">❌ Không đạt</td><td id="t:Jr" class="">Chưa có hệ thống real-time dispatch, load test hoặc tích hợp OBD-II.</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-8029-abf3-d21575d5b539"><td id="_\Un" class=""><strong>Giao diện App (UI/UX)</strong></td><td id="K^=Z" class="">⚠️ Mức cơ bản</td><td id="t:Jr" class="">Giao diện chỉ mới ở mức beta, chưa có hệ thống khách–tài–admin đồng bộ.</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-809d-91ef-d5d7e439a50b"><td id="_\Un" class=""><strong>Hỗ trợ vận hành / bảo trì</strong></td><td id="K^=Z" class="">❌ Không có mô hình SLA (Service Level Agreement).</td><td id="t:Jr" class="">❌</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="285c5e6f-95bd-8085-8120-db027726c711"/></div><div style="display:contents" dir="auto"><h2 id="285c5e6f-95bd-80d1-8653-fd4899fe2401" class=""><strong>V. RỦI RO &amp; ĐỀ XUẤT BIỆN PHÁP</strong></h2></div><div style="display:contents" dir="ltr"><table id="285c5e6f-95bd-8074-878f-c5df0737919d" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-8038-9ed1-edc834414912"><th id="ol`:" class="simple-table-header-color simple-table-header"><strong>Nhóm rủi ro</strong></th><th id="[Eck" class="simple-table-header-color simple-table-header"><strong>Mức độ</strong></th><th id="j}u`" class="simple-table-header-color simple-table-header"><strong>Mô tả</strong></th><th id="wz&lt;s" class="simple-table-header-color simple-table-header"><strong>Giải pháp đề xuất</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-8012-8f0f-d7bfe32d520f"><td id="ol`:" class=""><strong>Pháp lý</strong></td><td id="[Eck" class="">🔴 Cao</td><td id="j}u`" class="">Không có giấy phép thanh toán hoặc bán hàng đa cấp → nguy cơ bị dừng hoạt động.</td><td id="wz&lt;s" class="">Không dùng cấu trúc F1/F2 trong giai đoạn 1; hợp đồng hợp tác BCC rõ ràng; tách Fintech ra thành công ty con có license.</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-80f7-92db-c0953e4dab18"><td id="ol`:" class=""><strong>Công nghệ</strong></td><td id="[Eck" class="">🔴 Cao</td><td id="j}u`" class="">Không có hạ tầng cloud bảo mật; phụ thuộc Google Maps và Amazon.</td><td id="wz&lt;s" class="">Chuyển sang kiến trúc độc lập (VNPT/AWS VN region); thuê audit SOC 2.</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-80c7-80e3-c6e3bfed5159"><td id="ol`:" class=""><strong>Tài chính</strong></td><td id="[Eck" class="">🟠 Trung bình</td><td id="j}u`" class="">Vốn vận hành không rõ, dự án phụ thuộc chủ cá nhân.</td><td id="wz&lt;s" class="">Chỉ dùng theo hợp đồng dự án cụ thể; không giao quyền lưu trữ dữ liệu tài chính.</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-80f3-907b-c58654f9fb2c"><td id="ol`:" class=""><strong>Đạo đức nghề nghiệp / dữ liệu</strong></td><td id="[Eck" class="">🔴 Cao</td><td id="j}u`" class="">Ghi âm buổi họp cho thấy chưa tách dữ liệu người dùng khỏi dữ liệu vận hành.</td><td id="wz&lt;s" class="">Ràng buộc NDAs &amp; DPIA (Data Protection Impact Assessment).</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-8045-9ea5-e9d6a92a0438"><td id="ol`:" class=""><strong>Vận hành thực tế</strong></td><td id="[Eck" class="">🟠 Trung bình</td><td id="j}u`" class="">Thiếu năng lực triển khai 24/7, không có trung tâm hỗ trợ.</td><td id="wz&lt;s" class="">Phải phối hợp với đội vận hành UniTaxi hoặc Viettel Tech.</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="285c5e6f-95bd-8049-9f05-e5477f9904cc"/></div><div style="display:contents" dir="auto"><h2 id="285c5e6f-95bd-80da-bf52-deba3e7050e5" class=""><strong>VI. ĐÁNH GIÁ PHÙ HỢP VỚI UNIPOWER – UNITAXI</strong></h2></div><div style="display:contents" dir="ltr"><table id="285c5e6f-95bd-80b4-a405-e77747e71e4b" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-807b-a3aa-ce972140b13c"><th id="n]da" class="simple-table-header-color simple-table-header"><strong>Trục so sánh</strong></th><th id="jCHo" class="simple-table-header-color simple-table-header"><strong>Mức độ tương thích</strong></th><th id="zyUv" class="simple-table-header-color simple-table-header" style="width:289.0078125px"><strong>Ghi chú</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-8003-b8ac-c7567f0e5f9f"><td id="n]da" class=""><strong>Fintech Core (Unipay)</strong></td><td id="jCHo" class="">⚠️ Một phần</td><td id="zyUv" class="" style="width:289.0078125px">Có khả năng gắn API, nhưng không đạt chuẩn bảo mật.</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-809b-b8e7-e910656e7cb3"><td id="n]da" class=""><strong>SuperApp Integration (Unitaxi)</strong></td><td id="jCHo" class="">❌ Không đạt</td><td id="zyUv" class="" style="width:289.0078125px">Không có SDK hoặc API chuẩn hóa để tích hợp.</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-807b-a2ff-d51c8ef10f4f"><td id="n]da" class=""><strong>Energy Billing (Unipower)</strong></td><td id="jCHo" class="">❌ Không đạt</td><td id="zyUv" class="" style="width:289.0078125px">Thanh toán điện chưa có khung pháp lý hoặc kỹ thuật.</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-80f0-9024-f0f12f712450"><td id="n]da" class=""><strong>Fleet Management &amp; IoT</strong></td><td id="jCHo" class="">⚠️ Hạn chế</td><td id="zyUv" class="" style="width:289.0078125px">Mới ở mức API Google, chưa có backend IoT.</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-8010-add1-e21564535aa4"><td id="n]da" class=""><strong>Legal Alignment (ESG, MOIT, MOT)</strong></td><td id="jCHo" class="">⚠️ Không đầy đủ</td><td id="zyUv" class="" style="width:289.0078125px">Không đáp ứng yêu cầu Luật Điện lực và NĐ 13.</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="285c5e6f-95bd-803b-8223-cd174c115683"/></div><div style="display:contents" dir="auto"><h2 id="285c5e6f-95bd-80ed-a6eb-e94b771fff6c" class=""><strong>VII. KẾT LUẬN TỔNG THỂ </strong></h2></div><div style="display:contents" dir="ltr"><table id="285c5e6f-95bd-800b-abc8-d9d33bdf62b0" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-8094-86c0-c05caa4914b6"><th id="lEbL" class="simple-table-header-color simple-table-header"><strong>Tiêu chí</strong></th><th id="t_rJ" class="simple-table-header-color simple-table-header"><strong>Điểm (thang 10)</strong></th><th id="y_LO" class="simple-table-header-color simple-table-header"><strong>Đánh giá</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-801f-8d9d-e6f57fd60f21"><td id="lEbL" class="">Công nghệ lõi</td><td id="t_rJ" class="">4.5</td><td id="y_LO" class="">Prototype, chưa thể thương mại hóa</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-8021-9b9e-fc5237f70f09"><td id="lEbL" class="">An toàn &amp; bảo mật</td><td id="t_rJ" class="">3.0</td><td id="y_LO" class="">Không đạt chuẩn</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-80d7-ba4a-c346d21fd09d"><td id="lEbL" class="">Pháp lý &amp; cấp phép</td><td id="t_rJ" class="">2.5</td><td id="y_LO" class="">Rủi ro cao</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-8092-9cd3-f8c5ab03b942"><td id="lEbL" class="">Vận hành &amp; mở rộng</td><td id="t_rJ" class="">4.0</td><td id="y_LO" class="">Năng lực yếu</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-80c4-b505-eadf70456de5"><td id="lEbL" class="">Tương thích hệ sinh thái UniPower</td><td id="t_rJ" class="">5.0</td><td id="y_LO" class="">Cần tái cấu trúc sâu</td></tr></div><div style="display:contents" dir="ltr"><tr id="285c5e6f-95bd-809c-9096-d0e1b9527fe3"><td id="lEbL" class="">Tổng hợp</td><td id="t_rJ" class=""><strong>3.8 / 10</strong></td><td id="y_LO" class=""><strong>Không đạt chuẩn đối tác lõi</strong></td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="285c5e6f-95bd-802d-a656-f7f15c2e330d"/></div><div style="display:contents" dir="auto"><h2 id="285c5e6f-95bd-80ab-a65d-ca13c83527ec" class=""><strong>VIII. KHUYẾN NGHỊ HÀNH ĐỘNG</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="285c5e6f-95bd-80ca-bccc-f633d48685ed" class="numbered-list" start="1"><li>❌ <strong>Không giao quyền phát triển lõi (Core System) cho OneTech/OneSearch Việt.</strong><div style="display:contents" dir="auto"><p id="285c5e6f-95bd-8040-b247-f3d3eab6d8cd" class="">→ Chỉ giữ họ ở vai trò <strong>tư vấn kỹ thuật phụ</strong> trong giai đoạn thử nghiệm.</p></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="285c5e6f-95bd-80c1-841e-e38591df34ed" class="numbered-list" start="2"><li>✅ <strong>Tách hạ tầng thanh toán ra khỏi app</strong> (dựng Unipay riêng, đăng ký license trung gian thanh toán).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="285c5e6f-95bd-8093-90c7-f7754ae24cd3" class="numbered-list" start="3"><li>✅ <strong>Chuyển hạ tầng bản đồ sang GrabMaps / Viettel Maps / VinBigData Map</strong> để tránh phụ thuộc Google.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="285c5e6f-95bd-80fa-b025-e02dac41c094" class="numbered-list" start="4"><li>✅ <strong>Ký NDA, Hợp đồng bảo mật dữ liệu &amp; giới hạn truy cập codebase.</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="285c5e6f-95bd-809f-9901-fc86ff9d71c4" class="numbered-list" start="5"><li>✅ <strong>Nếu tiếp tục hợp tác</strong>, yêu cầu họ đạt các tiêu chuẩn sau trước Q2/2026:<div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80b4-bde1-f9279a3f6a09" class="bulleted-list"><li style="list-style-type:disc">ISO 27001:2022</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80c4-af07-c4c7f4d06e9d" class="bulleted-list"><li style="list-style-type:disc">Giấy phép trung gian thanh toán của NHNN</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80ce-89a9-eefd060a0488" class="bulleted-list"><li style="list-style-type:disc">Audit bảo mật độc lập (VNISA hoặc PwC Việt Nam)</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80b2-94e3-f065f7f2dd78" class="bulleted-list"><li style="list-style-type:disc">Kiểm chứng stress-test 1.000 xe thực tế</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><p id="285c5e6f-95bd-805f-aeab-e3ff2667e58b" class="">
</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
