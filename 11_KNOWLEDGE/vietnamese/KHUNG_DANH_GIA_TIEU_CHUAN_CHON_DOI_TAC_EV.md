---
tags: [vietnamese]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>KHUNG ĐÁNH GIÁ TIÊU CHUẨN CHỌN ĐỐI TÁC EV </title><style>
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
	
</style></head><body><article id="2afc5e6f-95bd-803b-a188-e918a3bcd69e" class="page sans"><header><h1 class="page-title" dir="auto"><strong>KHUNG ĐÁNH GIÁ TIÊU CHUẨN CHỌN ĐỐI TÁC EV </strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-80e6-a1dd-d4d8876c3514"/></div><div style="display:contents" dir="auto"><h1 id="2afc5e6f-95bd-805c-8aba-e4fa55181ab3" class=""><strong>I. NĂNG LỰC TÀI CHÍNH &amp; ỔN ĐỊNH DOANH NGHIỆP (8 tiêu chí)</strong></h1></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-8014-a809-d2704dce5753"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-80b0-b91a-d7bbf2c8c5d1" class=""><strong>1. Doanh số EV tại Trung Quốc (tháng/quý)</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-80b8-b561-e658c4fddb10" class=""><strong>Ý nghĩa:</strong> doanh số cao cho thấy hãng có <strong>thị phần – nhu cầu thật – mô hình kinh doanh bền</strong>, đồng thời đảm bảo khả năng tồn tại 5–10 năm → cực kỳ quan trọng với fleet tại Việt Nam.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8070-8c0e-ebee398277d8" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> &gt; <strong>30.000 xe/tháng</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80c6-bdb3-fd9e52b01ae7" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> <strong>10.000–30.000</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-804a-8e49-ec7e28cc53bb" class="bulleted-list"><li style="list-style-type:disc"><strong>Nguy cơ:</strong> <strong>3.000–10.000</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-801c-9895-ca72e60b49ee" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>&lt; 3.000</strong> → rủi ro biến mất, không hỗ t
rợ hậu mãi</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-8021-a56d-fedd5a862a79"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-806f-b351-f1da3a3ae02e" class=""><strong>2. Doanh thu hàng năm (NEV Revenue)</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-80ce-b834-d060dfd3149c" class=""><strong>Ý nghĩa:</strong> doanh thu lớn chứng minh hãng có <strong>đủ năng lực tài chính</strong> để duy trì R&amp;D, linh kiện, bảo hành, OTA và phát triển thị trường quốc tế.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80d1-8aeb-e1e164d2778e" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> &gt; <strong>5 tỷ USD/năm</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-803b-9bb9-d2de5b9c8882" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>&lt; 500 triệu USD</strong> → không đủ năng lực duy trì lâu dài</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-80fa-848f-ed84c91d5bdd"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-802d-ab14-db3a06a4500e" class=""><strong>3. Quy mô vốn hoá hoặc tổng tài sản</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-8089-9f52-ea086cf5a784" class=""><strong>Ý nghĩa:</strong> vốn hóa/tài sản càng lớn → khả năng chịu biến động thị trường càng cao → ít nguy cơ phá sản, đảm bảo hợp tác dài hạn.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80a6-a0c7-f65860e586ff" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> Top <strong>10–15</strong> Trung Quốc</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-804b-8d31-dc3bc324f8f3" class="bulleted-list"><li style="list-style-type:disc"><strong>Nguy cơ:</strong> Top <strong>30–50</strong></li></ul></div><div style="display:contents" d
ir="auto"><ul id="2afc5e6f-95bd-80b5-af1d-f5f82f768eaf" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>Ngoài top 50</strong> → rủi ro rất cao</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-8000-ad4e-d656ee21cd48"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-800e-8f3e-c5c9c254dd98" class=""><strong>4. Dòng tiền hoạt động (Operating Cash Flow)</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-8089-92ed-d358f375b31b" class=""><strong>Ý nghĩa:</strong> hãng EV đốt tiền quá nhiều sẽ không đủ nguồn lực duy trì bảo hành, recall, nâng cấp và hỗ trợ quốc tế.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8069-96ca-d72e2f29b0f7" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> Dòng tiền <strong>dương ≥ 3 năm liên tục</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80dc-9b52-f8c2db1db6f6" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>Âm liên tục</strong> → rủi ro phá sản cao</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-8057-b440-cc5438cf7b1e"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-80fd-a71f-dd4e6ae34ddf" class=""><strong>5. Tỷ lệ nợ/vốn chủ (Debt-to-Equity)</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-8043-8df6-e04128b8b9e4" class=""><strong>Ý nghĩa:</strong> nợ lớn khiến hãng khó duy trì hậu mãi &amp; R&amp;D → rủi ro đổ vỡ cao.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8046-bcdd-ed965af35144" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> &lt; <strong>1.5</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80a8-8f45-ffbd9652244d" class="bulleted-list"><li style="list-style-type:disc"><strong>Nguy cơ:</strong> <
strong>1.5–3.0</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80d2-ac98-de72b195d4fd" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> &gt; <strong>3.0</strong> → cảnh báo rủi ro nghiêm trọng</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-80f9-bcd1-d0c403af9264"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-8067-b403-dcdc25291cf2" class=""><strong>6. Lợi nhuận ròng (Net Profit Margin)</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-8021-8a4a-ccfe56e1b66f" class=""><strong>Ý nghĩa:</strong> chỉ các hãng có <strong>lợi nhuận ổn định</strong> mới duy trì bảo hành – phụ tùng – nâng cấp phần mềm quốc tế.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80a3-99fc-e595380ea73b" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> <strong>Đang có lãi</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8026-bd60-c7d6d4705f50" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>Lỗ sâu và kéo dài</strong> (&gt; 3 năm)</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-80cf-9631-f987e6da7fac"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-804e-b856-e48a63ab1170" class=""><strong>7. Mức đầu tư R&amp;D hàng năm (% doanh thu)</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-80ae-bc6a-c5e8d948b38c" class=""><strong>Ý nghĩa:</strong> EV phụ thuộc cực lớn vào phần mềm, pin, ADAS – hãng nào không đầu tư R&amp;D sẽ tụt lại và sụp.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8092-a7a1-db074cb78b63" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> &gt; <strong>8% doanh thu</strong></li></ul></div><div style="display:contents" dir="auto"><ul i
d="2afc5e6f-95bd-800e-9ce1-f287865b4947" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> 5–8%</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80b2-a3e3-ff7e38b77380" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> &lt; <strong>3%</strong> → công nghệ lỗi thời, rủi ro lâu dài</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-80ba-bbe5-f3a85db5ab2f"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-806c-85eb-d099920467ab" class=""><strong>8. Lịch sử ngành (năm hoạt động)</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-803f-90d5-f4f956654d5d" class=""><strong>Ý nghĩa:</strong> kinh nghiệm ngành quyết định khả năng bảo hành – linh kiện – vòng đời sản phẩm.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8016-af59-dec76b07acad" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> ≥ <strong>10 năm</strong> hoạt động EV/automotive</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80c2-b788-dfe0697b3225" class="bulleted-list"><li style="list-style-type:disc"><strong>Nguy cơ:</strong> <strong>5–10 năm</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80b0-97d4-d9d2bca7ead2" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> &lt; <strong>5 năm</strong> → kinh nghiệm quá ít, rủi ro cao</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-80f3-9d2b-fa0e58b27c3d"/></div><div style="display:contents" dir="auto"><h1 id="2afc5e6f-95bd-8015-940c-d2f54b126fd5" class=""><strong>II. NĂNG LỰC SẢN XUẤT &amp; XUẤT KHẨU (5 tiêu chí)</strong></h1></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-80ef-82a2-e4670688b4c4" class=""><strong>9. Giấy phép xuất khẩu (China Export License)</strong></h3></div><div s
tyle="display:contents" dir="auto"><p id="2afc5e6f-95bd-80ad-a3d8-cf9823f69753" class=""><strong>Giải thích: </strong>Từ năm 2023, Trung Quốc siết chặt giấy phép xuất khẩu xe điện. Chỉ các <strong>nhà máy đủ chuẩn an toàn – dữ liệu – phần mềm – chất lượng</strong> mới được cấp phép. Nếu không có giấy này, <strong>xe không thể thông quan hợp pháp</strong> vào Việt Nam và không thể làm hồ sơ bảo hành/recall.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80bb-9f5b-c0f156b1e984" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> Có giấy phép xuất khẩu chính thức</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80e1-8882-dcbd11534f53" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> Công ty con của tập đoàn lớn, có LOA/ủy quyền đầy đủ</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-806b-8033-ce1792bcb8f1" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>Thiếu giấy phép hoặc giấy giả</strong> → không thể làm dự án</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-80ea-957e-f84cf5b40e83"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-80c6-bb08-c681431294ee" class=""><strong>10. Nhà máy đạt tiêu chuẩn EU/ASEAN</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-80d7-b468-c7a622a0cd63" class=""><strong>Giải thích: </strong>Việt Nam áp dụng quy chuẩn <strong>EU</strong> cho kiểm định xe nhập khẩu (an toàn – khí thải – tính năng). Nếu nhà máy chỉ đạt tiêu chuẩn nội địa Trung Quốc, xe <strong>không đạt kiểm định – không được cấp giấy đăng kiểm – không lưu hành được</strong>.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80cf-bf18-faaee83688a1" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> Nhà máy đạt <strong>đầy đủ tiêu chuẩn E
U</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80c6-a19b-c93c9bdbbfc6" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> Đạt tiêu chuẩn ASEAN + có hồ sơ kiểm định bổ sung</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80db-b6fe-c63bd6d54ce5" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>Chỉ đạt chuẩn nội địa</strong> → rủi ro loại ngay từ vòng pháp lý</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-80e7-8605-c93f979c5c92"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-8047-a78b-e62199d1f723" class=""><strong>11. Công suất nhà máy (sản lượng/năm)</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-8039-a495-e3213f7738e4" class=""><strong>Giải thích: </strong>Các dự án fleet 200–3.000 xe cần <strong>nguồn cung ổn định</strong>. Nhà máy sản lượng thấp thường thiếu hàng, thiếu linh kiện hoặc ngưng sản xuất mẫu xe sau 1–2 năm → phá vỡ toàn bộ kế hoạch đội xe và bảo hành.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80b1-912f-ca8952df7b36" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> <strong>&gt; 100.000 xe/năm</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-801b-afb5-d054cb46a94c" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> 50.000–100.000 xe/năm</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80fd-83a9-db749437f9a5" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>&lt; 20.000 xe/năm</strong> → rủi ro cao về nguồn cung &amp; linh kiện</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-80a7-beae-dd882ab63b16"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-8028-829f-d853a2afb9b8" c
lass=""><strong>12. Tỷ lệ tự động hóa dây chuyền</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-80cc-a516-de00c7d171d9" class=""><strong>Giải thích: </strong>Tự động hoá cao → chất lượng đồng đều → giảm lỗi sản xuất → giảm tỷ lệ hỏng hóc khi vận hành &gt; 12 giờ/ngày (mô hình taxi/lease). Dây chuyền thủ công thường gây lỗi vặt, nghiêm trọng hơn đối với EV do độ phức tạp của pin – điện – phần mềm.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8018-90e7-ea87e7c7ac21" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> <strong>&gt; 70% tự động hoá</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8089-b655-feb2054916b7" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> 50–70%</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80cd-85ab-fbfeb22b8b0b" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>&lt; 40%</strong> → lỗi sản xuất cao, rủi ro nằm bãi</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-8044-ac41-d61cd04030b1"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-8063-89f9-f9ea3521b9bd" class=""><strong>13. Bộ hồ sơ nhập khẩu (LOA, LOC, COP)</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-80cd-aa10-f5cfa8a890c9" class=""><strong>Giải thích: </strong>Xe EV vào Việt Nam bắt buộc phải có bộ hồ sơ tiêu chuẩn gồm:</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-804f-92f2-d8274e223757" class="bulleted-list"><li style="list-style-type:disc"><strong>LOA</strong>: Ủy quyền bảo hành / recall</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-801a-8c7d-e23df04211b1" class="bulleted-list"><li style="list-style-type:disc"><strong>LOC</strong>: Xác nhận xuất xưởng đúng chuẩn quốc tế</li></ul></div><div s
tyle="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8018-9338-df6d37082ca0" class="bulleted-list"><li style="list-style-type:disc"><strong>COP</strong>: Chứng nhận phù hợp sản xuất (có giá trị 3 năm)</li></ul></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-8084-8526-da30c8cb0e32" class="">Thiếu các giấy tờ này, xe <strong>không được đăng kiểm – không được lưu hành – không được bảo hành chính hãng</strong>.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80b1-b00e-f71c6f84dc7f" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> Cung cấp đầy đủ LOA – LOC – COP có xác nhận lãnh sự</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80b9-be36-d39be24584fe" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>Không cung cấp / không công chứng</strong> → không thể triển khai dự án</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-80f8-9a10-f98a2c320de5"/></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-80e0-a66f-d9d6fcec0a04" class="">5 tiêu chí về năng lực sản xuất – xuất khẩu là <strong>hàng rào pháp lý và chất lượng bắt buộc</strong>:</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80a4-bfaf-e5a52bcdec85" class="bulleted-list"><li style="list-style-type:disc">Có giấy phép xuất khẩu → đảm bảo hợp pháp &amp; an toàn</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80b9-bc97-d4f7d717e523" class="bulleted-list"><li style="list-style-type:disc">Nhà máy đạt EU → chắc chắn qua kiểm định VN</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8079-9f30-cadcf18c6e8a" class="bulleted-list"><li style="list-style-type:disc">Công suất lớn → bảo đảm nguồn cung &amp; linh kiện</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-808d-b8b7-c44a15ec2736" class="bulleted-list"><li s
tyle="list-style-type:disc">Tự động hóa cao → giảm lỗi – giảm downtime</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80d7-8b4a-cc990469260f" class="bulleted-list"><li style="list-style-type:disc">Bộ hồ sơ đầy đủ → thông quan nhanh – bảo hành chuẩn</li></ul></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-8098-b497-d87f8248a449" class="">⟶ Đây là <strong>bộ tiêu chuẩn bắt buộc</strong> trước khi Unipower ký hợp tác nhập khẩu – không đạt thì loại ngay.</p></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-80d2-82f1-e4291f3f7651"/></div><div style="display:contents" dir="auto"><h1 id="2afc5e6f-95bd-80d1-9aaf-eee2e9fbc272" class=""><strong>III. PIN – AN TOÀN – CÔNG NGHỆ (6 tiêu chí)</strong></h1></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-8097-a4fb-f99caa20b51a" class=""><strong>14. Nhà cung cấp pin (CATL / BYD / CALB / EVE / Gotion)</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-808a-9a24-e68e7f2abc59" class=""><strong>Giải thích: </strong>Nhà cung cấp pin quyết định <strong>tuổi thọ, độ ổn định, rủi ro cháy nổ và chi phí vận hành</strong>. Các dự án fleet lớn phải dùng pin từ top 5 toàn cầu vì họ có chuỗi cung ứng ổn định, tiêu chuẩn an toàn cao và khả năng hỗ trợ bảo hành quốc tế.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-804f-b247-c1855e481cc6" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> Thuộc <strong>top 5 thế giới</strong> (CATL, BYD, EVE, CALB, Gotion)</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8057-9dd6-c225c03eecb6" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> Hãng xếp hạng trung bình nhưng có chứng nhận đầy đủ</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80f2-a78a-c23001324958" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <
strong>Pin vô danh / pin xe tốc độ thấp</strong> → rủi ro rất cao</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-8035-a564-fc11e41d3970"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-8036-a7f0-fb4a0e0af57e" class=""><strong>15. Chứng nhận an toàn pin (UL, IEC, GB tiêu chuẩn mới)</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-80bf-aa9b-eeb2b89bd956" class=""><strong>Giải thích: </strong>Pin EV phải đạt <strong>quy chuẩn an toàn quốc tế</strong> để được nhập khẩu chính ngạch và bảo đảm an toàn khi vận hành liên tục 24/7. Nếu không đạt chuẩn UL/IEC/GB mới, pin có thể gặp lỗi quá nhiệt, phồng cell, cháy nổ trong quá trình sạc nhanh.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-807b-ab2f-d690fcb8eb67" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> Đầy đủ chứng nhận UL/IEC/GB</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80bf-951d-da73a9b4be92" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> Chỉ đủ GB nhưng có hồ sơ kiểm định mạnh</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80fd-bb8b-cd9b5318ed16" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>Không đạt chuẩn quốc tế</strong> → không thể dùng cho fleet</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-80b8-8a9d-d774626e37e3"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-8091-9449-ce4105773ce6" class=""><strong>16. Tỷ lệ suy giảm pin (Degradation Rate)</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-807a-a5db-d5e2b8e57e30" class=""><strong>Giải thích: </strong>Xe taxi chạy 60.000–90.000 km/năm. Nếu pin suy giảm nhanh, chi phí thay pin sẽ phá vỡ toàn bộ P&amp;L của đội xe. Tỷ lệ xuống cấp phản ánh chất lượng cell, BMS và công nghệ tản n
hiệt.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80d1-a169-c2349b175a38" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> <strong>&lt; 8% sau 2 năm</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8043-be15-de60de6cbb87" class="bulleted-list"><li style="list-style-type:disc"><strong>Nguy cơ:</strong> 12–18% → chi phí/km tăng rõ</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8015-82b9-c0530fab3fd3" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>&gt; 20%</strong> → đội xe lỗ sau 2–3 năm</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-808f-a8f3-f5e38a2db6bc"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-8064-aa0e-f920e89f39c8" class=""><strong>17. Tốc độ sạc (Max DC Charging Speed)</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-8062-905a-ddb4841066e3" class=""><strong>Giải thích: </strong>Tốc độ sạc quyết định <strong>vòng quay xe, số cuốc/ngày và hiệu suất tài sản</strong>. Xe sạc chậm làm giảm doanh thu ~15–25% vì mất thời gian chờ sạc.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80b2-8aee-e4f267cd622f" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> <strong>≥ 60–80 kW</strong> (phù hợp taxi &amp; fleet)</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80f6-9c61-dc438ff00408" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> 40–60 kW</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-803b-8681-d4ad29054f02" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>&lt; 30 kW</strong> → không đáp ứng vận hành thương mại</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-80bc-9ca8-d1fb65b25e3a"/></div><div s
tyle="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-8020-b7db-d110b1dde242" class=""><strong>18. Công nghệ BMS &amp; tản nhiệt pin</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-80bd-9f38-e920b947c8e5" class=""><strong>Giải thích: </strong>Pin EV cần hệ thống <strong>quản lý nhiệt độ (liquid cooling)</strong> để duy trì tuổi thọ, tránh quá nhiệt và đảm bảo an toàn khi sạc nhanh. Xe không có tản nhiệt tốt sẽ giảm SOH nhanh và nguy cơ cháy nổ cao.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-802b-8823-c65bbeaa6517" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> Liquid cooling + BMS cấp độ cao</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8039-87cf-d4ec56501277" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> Air cooling nhưng có BMS mạnh</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80cc-84c6-e237ac872a07" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>Không có kiểm soát nhiệt tốt</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-8048-bfe1-c1435c04b4b4"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-800e-af45-e6f7b74086b4" class=""><strong>19. Hệ thống an toàn (ESP, ABS, ADAS)</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-8017-9b27-d273b959fd31" class=""><strong>Giải thích: </strong>Hệ thống phanh – cân bằng – hỗ trợ lái trực tiếp ảnh hưởng đến <strong>an toàn pháp lý</strong> khi vận hành taxi, đặc biệt trong đô thị đông đúc. Xe thiếu tính năng cơ bản dễ gây tai nạn và tăng chi phí bảo hiểm.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80aa-a7fd-cfb05698eae4" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> ESP + ABS + ADAS đầy đủ</li></ul></div><div style="display:contents" d
ir="auto"><ul id="2afc5e6f-95bd-8075-abdf-ea9e94579cc5" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> ESP + ABS</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80af-b652-c110d165222e" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>Thiếu tính năng an toàn cơ bản</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-8042-be20-ddda67c6fe41"/></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-8071-aec5-fdb835079f2d" class="">6 tiêu chí về pin – an toàn – công nghệ là <strong>tuyến phòng thủ sống còn</strong> của đội xe Unipower:</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80ec-b91c-ca1ca2e307a8" class="bulleted-list"><li style="list-style-type:disc">Pin top 5 → ổn định – an toàn – dễ bảo hành</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80fc-8a7d-e8de268bcabd" class="bulleted-list"><li style="list-style-type:disc">Chứng nhận đầy đủ → thông quan nhanh – không rủi ro pháp lý</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8089-b2f0-dcbdc8cd6ddb" class="bulleted-list"><li style="list-style-type:disc">Degradation thấp → bảo toàn P&amp;L trong 3–5 năm</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8072-9a1c-e5c3e12b18a1" class="bulleted-list"><li style="list-style-type:disc">Sạc nhanh → tăng số cuốc/ngày → tăng doanh thu</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80e7-a6a3-d22762a3763c" class="bulleted-list"><li style="list-style-type:disc">Tản nhiệt tốt → tăng tuổi thọ pin</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8079-9b52-d4c30ddf10d5" class="bulleted-list"><li style="list-style-type:disc">An toàn cao → giảm tai nạn – giảm downtime – giảm chi phí bảo hiểm</li></ul></div><div style="display:contents" dir="auto"><p i
d="2afc5e6f-95bd-8004-aa81-e5b8c52d431f" class="">⟶ <strong>Nếu hãng xe không đạt tiêu chuẩn, tuyệt đối không chọn cho mô hình 200–3.000 xe.</strong></p></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-80bb-b2e0-f3a64d3f008f"/></div><div style="display:contents" dir="auto"><h1 id="2afc5e6f-95bd-804d-90fe-f51b7a965e21" class=""><strong>IV. PHẦN MỀM – DỮ LIỆU – TELEMATICS (5 tiêu chí)</strong></h1></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-80f5-95be-cd0c0adea26c" class=""><strong>20. API tích hợp fleet</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-800f-a66a-cdb0fe842988" class=""><strong>Giải thích: </strong>Đội xe lớn cần <strong>dữ liệu real-time</strong> (vị trí, SOC, lỗi hệ thống, hành vi lái…) để tối ưu điều phối, bảo trì dự báo và kiểm soát chi phí. Nếu hãng xe không mở API, Unipower <strong>không thể vận hành quy mô lớn</strong>.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8025-af94-ca34cebf512f" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> API mở đầy đủ (SOC/SOH, nhiệt độ pin, lỗi hệ thống, vị trí…)</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-804a-b1d5-c253efcb67f9" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> API giới hạn</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80ee-9016-eb02d6f1c733" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>Không có API</strong> → không thể quản lý đội xe</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-80f4-8a36-fd405ee93302"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-80d3-8272-f6982edee28e" class=""><strong>21. OTA – cập nhật phần mềm từ xa</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-808f-abaa-e73120a846d0" class=""><strong>Giải thích: </strong>90% l
ỗi EV hiện đại đến từ phần mềm (battery BMS, cabin ECU, ADAS, gateway…). Nếu không OTA, mỗi lỗi phải đưa xe vào xưởng → tê liệt đội xe, tăng downtime, tăng chi phí.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8096-bcf7-cf05fc7d2364" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> OTA toàn bộ hệ thống</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80ac-8c4c-e9fdb1b14443" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> OTA một phần</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8028-933a-ee7fb821d353" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>Không OTA</strong> → rủi ro “chết xe hàng loạt”</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-8077-a7c1-d679f76e6875"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-80e8-862f-d2765b7a4cef" class=""><strong>22. Telematics (SOC, SOH, lỗi pin, hành vi lái)</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-8013-8868-c8cc19f5ddf0" class=""><strong>Giải thích: </strong>Taxi EV cần theo dõi <strong>tình trạng pin (SOC/SOH), nhiệt độ, dòng sạc/xả, lỗi cell, lỗi motor, thói quen tăng tốc – phanh</strong>. Nếu chỉ có GPS, gần như <strong>không thể kiểm soát chi phí/km</strong>.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8032-90eb-e6aca29a2ade" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> telematics đầy đủ cấp độ pin – motor – BMS</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-808a-9638-df4e28167936" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> telematics giới hạn</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8063-acb4-e29ecdbcb6d3" class="bulleted-list"><li s
tyle="list-style-type:disc"><strong>Red flag:</strong> <strong>Chỉ có GPS</strong> → quản lý đội xe mù thông tin</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-8029-b40f-e79f15a5f400"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-80b7-9ca5-eeb4d81be473" class=""><strong>23. Ổn định phần mềm (tỷ lệ crash)</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-80d1-b258-cde6a45f3d86" class=""><strong>Giải thích: </strong>Lỗi phần mềm gây đứng xe, tắt màn hình, treo BMS hoặc mất kết nối — cực kỳ nguy hiểm khi vận hành taxi 24/7.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8009-a7cc-f7721fbee65e" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> tỷ lệ crash <strong>&lt; 1%</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8074-823e-db2462c9eb9a" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> 1–3%</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80cb-9cd6-fc69bcd61726" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>Lỗi liên tục / treo hệ thống</strong> → không dùng cho fleet</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-809a-947f-f05d82e3bfa8"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-80d4-a013-d190f5d15b2a" class=""><strong>24. Tuân thủ luật dữ liệu Trung Quốc (Data Compliance)</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-80b8-a5d7-d0acb3342dd6" class=""><strong>Giải thích: </strong>Luật Trung Quốc (Data Export Security Law) cấm xuất dữ liệu ra khỏi lãnh thổ nếu hãng xe <strong>không được cấp phép xuất khẩu chính ngạch</strong>. Những hãng nhỏ, xe tốc độ thấp, hoặc chưa đạt tiêu chuẩn an toàn dữ liệu <strong>không được phép xuất khẩu</strong> → không thể cấp LOA/LOC/ủy quyền bảo h
ành.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8019-9597-ec6a0a8e3857" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> hãng có giấy phép xuất khẩu + tuân thủ đầy đủ</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-801d-9b5b-c9cb77c336b3" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> đang tiến hành thủ tục</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80f8-a409-ff23f8fb8894" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>Không tuân thủ → không thể nhập khẩu chính ngạch</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-80b4-926b-fc0bdc75bb08"/></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-80fa-a157-e0da8be7b86d" class="">5 tiêu chí phần mềm – dữ liệu – telematics là nền tảng sống còn cho đội xe lớn:</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80d9-b448-dbbc0fb48255" class="bulleted-list"><li style="list-style-type:disc">Không API → không quản lý được.</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80eb-9f30-e019801074f5" class="bulleted-list"><li style="list-style-type:disc">Không OTA → không xử lý lỗi nhanh.</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80c6-b8d3-e014c6df456d" class="bulleted-list"><li style="list-style-type:disc">Không telematics → không tối ưu chi phí/km.</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-801a-b888-ffdf0544556d" class="bulleted-list"><li style="list-style-type:disc">Phần mềm không ổn định → đội xe tê liệt.</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80ea-8d95-c1607f908737" class="bulleted-list"><li style="list-style-type:disc">Không compliance dữ liệu → không thể nhập khẩu hợp pháp.</li></ul></div><div s
tyle="display:contents" dir="auto"><p id="2afc5e6f-95bd-805f-a9ac-d46bda0f6704" class="">⟶ <strong>Nếu hãng xe không đạt các tiêu chuẩn này, tuyệt đối không được chọn làm đối tác fleet.</strong></p></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-8021-942e-c476d2066db7"/></div><div style="display:contents" dir="auto"><h1 id="2afc5e6f-95bd-8026-b999-d01ac0d454ab" class=""><strong>V. HẬU MÃI – BẢO HÀNH – LINH KIỆN </strong></h1></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-80ec-bc41-d6e545965585" class=""><strong>25. Bảo hành pin &amp; motor</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-8091-97ac-ff6966357731" class=""><strong>Ý nghĩa:</strong> Pin và motor chiếm 45–55% giá trị xe. Đây là hai bộ phận quyết định tuổi thọ, chi phí vận hành và khả năng khai thác xe trong mô hình taxi/thuê xe.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8003-ab43-c4f5f06e455c" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> ≥ <strong>5 năm</strong> (đảm bảo an toàn tài chính và kỹ thuật cho fleet vận hành cường độ cao)</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80f0-b1a4-eae4e006ace1" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> 3–5 năm</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8068-9da9-d877592bb8cd" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> &lt; <strong>3 năm</strong> → rủi ro chi phí bảo trì tăng mạnh sau 18–24 tháng</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-8093-8849-e705112b0026"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-8079-9df9-cbedb949f40f" class=""><strong>26. Thời gian phản hồi bảo hành</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-80ca-8915-f50286ddfb10" class=""><strong>Ý nghĩa:</strong> Trong mô 
ình vận tải và fleet, thời gian phản hồi quyết định trực tiếp doanh thu. Xe chết nằm bãi = mất tiền.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-807b-b2fd-c2015ad8920d" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> &lt; <strong>24 giờ</strong> (chuẩn của BYD, Geely, Changan khi hỗ trợ fleet quốc tế)</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8046-a0ec-f8807747cf00" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> 24–72 giờ</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8068-8323-c3cce3a523e6" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> &gt; <strong>7 ngày</strong> → đội xe mất vòng quay, thiệt hại doanh thu rất lớn</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-806c-ac89-cecda314d75d"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-801e-9429-c1d07011ce5f" class=""><strong>27. Thời gian cung cấp linh kiện</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-805e-ab07-d7859654c75a" class=""><strong>Ý nghĩa:</strong> Linh kiện chậm = xe nằm bãi = thiệt hại kép (doanh thu + tài xế). Đây là rủi ro lớn nhất với hãng nhỏ.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80d5-a27c-e163a5228143" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> <strong>3–5 ngày</strong> (có kho linh kiện tại VN hoặc xuất kho nhanh từ Trung Quốc)</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80a9-909c-f35bb51bbd4b" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> 7–14 ngày</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-802c-8f53-ed5f1917456d" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> &gt; <strong>30 ngày</strong> → không thể vận h
ành fleet lớn</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-8029-ab37-d4a5c2262641"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-80fe-bf66-d5a50fd30ab0" class=""><strong>28. Số trung tâm bảo dưỡng uỷ quyền tại Việt Nam</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-803d-afc6-c431d9e292e1" class=""><strong>Ý nghĩa:</strong> Mạng lưới bảo dưỡng thể hiện cam kết thị trường, khả năng bảo hành và hỗ trợ vận hành dài hạn.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-808e-b6f1-e7145de20df0" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> ≥ <strong>5 trung tâm</strong> (HCM – HN – Đà Nẵng – Cần Thơ – Hải Phòng)</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80b1-bc3d-f7d18d9f189e" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> 2–4</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8089-aa8d-d5551c8a8c3e" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>0–1</strong> → rủi ro cao: thiếu nhân lực, thiếu năng lực hỗ trợ</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-80a4-bf8d-f5d25ae65ec1"/></div><div style="display:contents" dir="auto"><h1 id="2afc5e6f-95bd-80a4-ae95-efe842ad6e96" class=""><strong>VI. PHÙ HỢP VỚI VIỆT NAM – FLEET – ĐỘI XE (3 tiêu chí)</strong></h1></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-8040-a60d-dfa0b1a20424" class=""><strong>29. Khả năng chịu tải taxi – điều kiện đường Việt Nam</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-804f-bda6-c596ad214e51" class=""><strong>Giải thích:</strong></p></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-80c1-8137-c41d70170d89" class="">Xe EV làm taxi ở Việt Nam phải chịu tải trọng cao, đường xấu, tần suất phanh – tăng tốc liên tục và k
hí hậu nóng ẩm. Các mẫu xe giá rẻ hoặc xe nội địa Trung Quốc không thiết kế cho cường độ vận hành 12–16 giờ/ngày sẽ xuống cấp nhanh (giảm tuổi thọ pin, hệ thống treo, điều hoà).</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8075-b0bd-c93bf405318e" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> Có dữ liệu kiểm thử thực tế <strong>50.000–80.000 km</strong> trong điều kiện vận tải hoặc fleet</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8090-99ce-e562411cc5a0" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> Có dữ liệu kiểm thử kỹ thuật nhưng chưa có dữ liệu fleet</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-800f-aa28-e8b94ed47cad" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>Không có dữ liệu</strong> → rủi ro hao mòn cao, chi phí bảo trì tăng mạnh sau 12–18 tháng</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-80da-b6b5-f7bfe8f55e9e"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-80a1-ac25-e5ffec02d19e" class=""><strong>30. Chi phí vận hành/km (OPEX/km)</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-8047-a45c-d15ebc0b945f" class=""><strong>Giải thích: </strong>OPEX/km quyết định trực tiếp <strong>lợi nhuận taxi, leasing và hợp đồng doanh nghiệp</strong>. Khác biệt 200–300đ/km là chênh lệch hàng tỷ đồng/năm với đội xe lớn. Xe pin kém, điều hoà yếu hoặc tiêu hao điện cao sẽ làm mô hình fleet mất hiệu quả.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80d1-b081-ff1a47270e4a" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> <strong>&lt; 400đ/km</strong> (chuẩn BYD, SGMW, Changan dùng fleet tại TQ &amp; SEA)</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8088-83f0-c378461ff554" c
lass="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> 400–700đ/km</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80ec-a9f9-c545b11ccb5e" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>&gt; 800đ/km</strong> → mô hình taxi hoặc leasing gần như không có lợi nhuận</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-8005-be04-e75e00e06a3e"/></div><div style="display:contents" dir="auto"><h3 id="2afc5e6f-95bd-80c6-80b7-dca8c8679f57" class=""><strong>31. Hỗ trợ mở rộng quy mô (fleet support)</strong></h3></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-8030-9e02-e0edb3dec4ea" class=""><strong>Giải thích: </strong>Để Unipower triển khai 500–3.000 xe trong 3 năm, hãng xe phải đủ năng lực về sản lượng, hậu mãi, linh kiện, đào tạo kỹ thuật và phần mềm. Nếu chỉ bán lẻ hoặc không có chương trình hỗ trợ fleet, Unipower sẽ bị đứt gãy vận hành ngay từ năm 1.</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80e1-8cf7-e56d6fef63fd" class="bulleted-list"><li style="list-style-type:disc"><strong>Tối ưu:</strong> Có <strong>fleet program</strong> chính thức: ưu đãi số lượng, hotline kỹ thuật, hỗ trợ bảo hành nhanh, tài liệu kỹ thuật, kho linh kiện riêng</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8009-800c-f5cfa9c3604a" class="bulleted-list"><li style="list-style-type:disc"><strong>Chấp nhận:</strong> Có hỗ trợ cơ bản nhưng không đầy đủ</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80d6-89d4-c44041babf8d" class="bulleted-list"><li style="list-style-type:disc"><strong>Red flag:</strong> <strong>Chỉ bán lẻ, không hỗ trợ fleet</strong> → không thể mở rộng mô hình đội xe lớn</li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-8007-a667-c5decb2a4ba0"/></div><div style="display:contents" dir="auto"><p i
d="2afc5e6f-95bd-8048-8644-d9ea5ea3b559" class="">Bộ 3 tiêu chí này xác định mức <strong>phù hợp thực tế với thị trường Việt Nam</strong>, nơi:</p></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8014-9f49-feb4e6d76fb4" class="bulleted-list"><li style="list-style-type:disc">đường xấu hơn Trung Quốc/EU,</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8086-8126-ced1307c29a5" class="bulleted-list"><li style="list-style-type:disc">khí hậu khắc nghiệt hơn,</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-808f-98dd-c864a4204076" class="bulleted-list"><li style="list-style-type:disc">tần suất vận hành taxi cao hơn,</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-809a-80b7-c149f391ff44" class="bulleted-list"><li style="list-style-type:disc">yêu cầu chi phí/km thấp hơn,</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80f8-a94a-f9f7a3184356" class="bulleted-list"><li style="list-style-type:disc">và cần hỗ trợ fleet mạnh ⟶ <strong>Nếu hãng xe không đạt chuẩn mục này, mô hình đội xe 200–3.000 chiếc gần như không khả thi.</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="2afc5e6f-95bd-8091-bc98-eeef76edf881"/></div><div style="display:contents" dir="auto"><h1 id="2afc5e6f-95bd-8008-ac92-c2bb0c6ed2dd" class=""><strong>🟩 KẾT LUẬN – BẢN 31 TIÊU CHÍ ĐÃ ĐẦY ĐỦ &amp; KHÔNG CÒN LỖ HỔNG</strong></h1></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80e9-b888-fa45cfa5979d" class="bulleted-list"><li style="list-style-type:disc">Bao trùm toàn bộ các rủi ro có thể xảy ra trong <strong>nhập khẩu – vận hành – bảo hành – mở rộng đội xe</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-80bb-965e-e053efdf4947" class="bulleted-list"><li style="list-style-type:disc">Dùng được cho tất cả hãng EV Trung Quốc trong việc chọn đối tác chiến lược.</li></ul></div><div s
tyle="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8084-ad44-ee27712c0036" class="bulleted-list"><li style="list-style-type:disc">Đảm bảo Unipower tránh được <strong>rủi ro pháp lý – vận hành – tài chính – kỹ thuật – pin – dữ liệu</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2afc5e6f-95bd-8084-8aa9-e6348b6b4a00" class="bulleted-list"><li style="list-style-type:disc">Đủ tiêu chuẩn để chọn đối tác cho quy mô <strong>200 → 1.000 → 3.000 xe</strong>.</li></ul></div><div style="display:contents" dir="auto"><p id="2afc5e6f-95bd-8079-95c2-f1bc2197fd2a" class="">
</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
