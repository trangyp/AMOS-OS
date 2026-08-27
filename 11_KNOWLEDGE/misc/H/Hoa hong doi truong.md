---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Hoa hong doi truong </title><style>
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
	
</style></head><body><article id="28dc5e6f-95bd-802b-bb7c-df2107c892ed" class="page sans"><header><h1 class="page-title" dir="auto">Hoa hong doi truong </h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="28dc5e6f-95bd-8040-b1d3-ef2a1524ec6b" class="">Ta tính <strong>hoa hồng Đội trưởng</strong> theo dữ kiện sau:</p></div><div style="display:contents" dir="auto"><ul id="28dc5e6f-95bd-80fc-b48d-cb2e546b22cb" class="bulleted-list"><li style="list-style-type:disc">Doanh thu <strong>mỗi xe</strong>: 1.500.000 VNĐ/ngày</li></ul></div><div style="display:contents" dir="auto"><ul id="28dc5e6f-95bd-806a-89e0-f8519226ebdd" class="bulleted-list"><li style="list-style-type:disc">Số xe trong đội: 15 xe</li></ul></div><div style="display:contents" dir="auto"><ul id="28dc5e6f-95bd-80c4-bb7d-fa4a6b4e7cf0" class="bulleted-list"><li style="list-style-type:disc">Tỷ lệ hoa hồng Đội trưởng: 3,6 %</li></ul></div><div style="display:contents" dir="auto"><hr id="28dc5e6f-95bd-8008-9703-f4874e1e4604"/></div><div style="display:contents" dir="auto"><h3 id="28dc5e6f-95bd-8099-bc70-d4d0d6dda304" class=""><strong>Bước 1 – Tổng doanh thu của đội</strong></h3></div><div style="display:contents" dir="auto"><p id="28dc5e6f-95bd-8080-bd1d-e29c48e80f30" class="">1.500.000 × 15 = 22.500.000 VNĐ/ngày</p></div><div style="display:contents" dir="auto"><h3 id="28dc5e6f-95bd-80e6-a7eb-ce1cb4212264" class=""><strong>Bước 2 – Tính hoa hồng 3,6 %</strong></h3></div><div style="display:contents" dir="auto"><p id="28dc5e6f-95bd-802d-94dc-f62c808bcc0e" class="">22.500.000 × 3,6 % = 22.500.000 × 0,036 = 810.000 VNĐ/ngày</p></div><div style="display:contents" dir="auto"><hr id="28dc5e6f-95bd-80c7-a0b6-c7d5079d726e"/></div><div style="display:contents" dir="auto"><p id="28dc5e6f-95bd-8095-934c-df44eb2ee1ca" class="">✅ <strong>Kết quả:</strong></p></div><div style="display:contents" dir="auto"><p id="28dc5e6f-95bd-8092-9a6c-dadd87186437" class="">Đội trưởng nhận <strong>810.000 VNĐ/ngày</strong> tiền hoa hồng quản lý đội 15 xe.</p></div><div style="display:contents" dir="auto"><p id="28dc5e6f-95bd-80db-81ba-cec06b3293a1" class="">Nếu muốn tính theo tháng (30 ngày hoạt động):</p></div><div style="display:contents" dir="auto"><p id="28dc5e6f-95bd-8010-b83c-e6a9fe84561b" class="">810.000 × 30 = 24.300.000 VNĐ/tháng</p></div><div style="display:contents" dir="auto"><p id="28dc5e6f-95bd-80e6-8cbf-ea1885303a79" class="">➡️ <strong>Hoa hồng Đội trưởng/tháng ≈ 24,3 triệu VNĐ.</strong></p></div><div style="display:contents" dir="auto"><p id="28dc5e6f-95bd-80d8-bce8-dcd109dbbdd6" class="">
</p></div><div style="display:contents" dir="auto"><p id="28dc5e6f-95bd-808a-bfd3-c48981565bcf" class="">Rất rõ — ta có hai trường hợp cần so sánh:</p></div><div style="display:contents" dir="auto"><hr id="28dc5e6f-95bd-80d7-afd5-c46cbd5d840e"/></div><div style="display:contents" dir="auto"><h3 id="28dc5e6f-95bd-80fb-bbd5-c66c13063e6f" class=""><strong>Trường hợp 1 – Đủ 15 xe</strong></h3></div><div style="display:contents" dir="auto"><ul id="28dc5e6f-95bd-8063-90a5-fde234e2378c" class="bulleted-list"><li style="list-style-type:disc">Doanh thu mỗi xe: <strong>1.500.000 VNĐ/ngày</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="28dc5e6f-95bd-8064-8da1-ddaff06d0c73" class="bulleted-list"><li style="list-style-type:disc">Số xe: <strong>15 xe</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="28dc5e6f-95bd-8015-89ff-cd06764b4aa1" class="bulleted-list"><li style="list-style-type:disc">Tỷ lệ hoa hồng: <strong>3,6%</strong></li></ul></div><div style="display:contents" dir="auto"><p id="28dc5e6f-95bd-80f0-91a8-c61e601d6c1e" class="">1.500.000 × 15 × 3,6\% = 22.500.000 × 0,036 = 810.000 VNĐ/ngày</p></div><div style="display:contents" dir="auto"><p id="28dc5e6f-95bd-80b0-8f90-f7e49a6c601b" class="">✅ <strong>Hoa hồng/ngày:</strong> 810.000 VNĐ</p></div><div style="display:contents" dir="auto"><p id="28dc5e6f-95bd-80c9-83b1-e18e8c17bbc3" class="">✅ <strong>Hoa hồng/tháng (30 ngày):</strong> 24.300.000 VNĐ</p></div><div style="display:contents" dir="auto"><hr id="28dc5e6f-95bd-80ed-8acd-deb250fdfbdd"/></div><div style="display:contents" dir="auto"><h3 id="28dc5e6f-95bd-80f8-a762-e3126313a8d4" class=""><strong>Trường hợp 2 – Chưa đủ 15 xe (được hưởng 5%)</strong></h3></div><div style="display:contents" dir="auto"><p id="28dc5e6f-95bd-80f9-a3f6-ec3b7a685b23" class="">Giả sử đội có <strong>10 xe</strong>, cùng mức doanh thu 1,5 triệu/xe/ngày:</p></div><div style="display:contents" dir="auto"><p id="28dc5e6f-95bd-8019-b5e5-d9a920536fd5" class="">1.500.000 × 10 × 5\% = 15.000.000 × 0,05 = 750.000 VNĐ/ngày</p></div><div style="display:contents" dir="auto"><p id="28dc5e6f-95bd-806b-952f-daac21f03b31" class="">✅ <strong>Hoa hồng/ngày:</strong> 750.000 VNĐ</p></div><div style="display:contents" dir="auto"><p id="28dc5e6f-95bd-803d-885c-f21b54704088" class="">✅ <strong>Hoa hồng/tháng (30 ngày):</strong> 22.500.000 VNĐ</p></div><div style="display:contents" dir="auto"><hr id="28dc5e6f-95bd-80f9-8b31-c46419a374c6"/></div><div style="display:contents" dir="auto"><h3 id="28dc5e6f-95bd-80e8-b75d-d700de012811" class=""><strong>Nhận xét:</strong></h3></div><div style="display:contents" dir="auto"><ul id="28dc5e6f-95bd-8035-95e6-d10d666d3ab9" class="bulleted-list"><li style="list-style-type:disc">Khi <strong>chưa đủ 15 xe</strong>, Đội trưởng được <strong>hưởng 5%</strong> → tuy số xe ít hơn, nhưng <strong>tỷ lệ cao hơn</strong>, nhằm <strong>bù đắp công sức giai đoạn khởi tạo đội</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="28dc5e6f-95bd-805a-aa53-dba8b4d0ad1e" class="bulleted-list"><li style="list-style-type:disc">Khi đủ 15 xe, tỷ lệ giảm xuống <strong>3,6%</strong>, nhưng tổng doanh thu cao hơn nên <strong>hoa hồng thực nhận vẫn tăng</strong>.</li></ul></div><div style="display:contents" dir="auto"><hr id="28dc5e6f-95bd-801d-a2ff-ebe62daee45a"/></div><div style="display:contents" dir="auto"><h3 id="28dc5e6f-95bd-80f3-8e0b-d89c9c3d7647" class=""><strong>So sánh tổng thể:</strong></h3></div><div style="display:contents" dir="ltr"><table id="28dc5e6f-95bd-80ad-8ffb-fd6b6c43cd5b" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="28dc5e6f-95bd-80a2-91fb-c8a0cbf8c88e"><th id="qw@h" class="simple-table-header-color simple-table-header"><strong>Trạng thái đội</strong></th><th id="x&gt;xl" class="simple-table-header-color simple-table-header"><strong>Số xe</strong></th><th id="OS&lt;}" class="simple-table-header-color simple-table-header"><strong>Tỷ lệ hoa hồng</strong></th><th id="o~FF" class="simple-table-header-color simple-table-header"><strong>Hoa hồng/ngày (VNĐ)</strong></th><th id="GuYH" class="simple-table-header-color simple-table-header"><strong>Hoa hồng/tháng (VNĐ)</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="28dc5e6f-95bd-8056-8689-f9d3f5eb91fb"><td id="qw@h" class="">Đội chưa đủ (5%)</td><td id="x&gt;xl" class="">10 xe</td><td id="OS&lt;}" class="">5%</td><td id="o~FF" class=""><strong>750.000</strong></td><td id="GuYH" class=""><strong>22.500.000</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="28dc5e6f-95bd-8017-b2fb-ea1c7cd87d0c"><td id="qw@h" class="">Đội đủ chuẩn (3,6%)</td><td id="x&gt;xl" class="">15 xe</td><td id="OS&lt;}" class="">3,6%</td><td id="o~FF" class=""><strong>810.000</strong></td><td id="GuYH" class=""><strong>24.300.000</strong></td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="28dc5e6f-95bd-8000-a1cf-f26c816ff65e"/></div><div style="display:contents" dir="auto"><p id="28dc5e6f-95bd-800a-b534-e3178d1c006b" class="">✅ <strong>Kết luận:</strong></p></div><div style="display:contents" dir="auto"><p id="28dc5e6f-95bd-8046-8495-dddf3f7c5994" class="">Đội trưởng chưa đủ 15 xe vẫn nhận <strong>5% trên tổng doanh thu đội</strong>, và khi đạt chuẩn 15 xe, chuyển sang mức <strong>3,6%</strong> nhưng tổng hoa hồng vẫn tăng nhờ quy mô lớn hơn.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
