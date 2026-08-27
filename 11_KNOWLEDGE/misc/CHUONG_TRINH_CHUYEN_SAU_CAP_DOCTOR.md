---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>CHƯƠNG TRÌNH CHUYÊN SÂU CẤP DOCTOR</title><style>
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
	
</style></head><body><article id="36bc5e6f-95bd-80c4-9ef5-d10406543908" class="page sans"><header><h1 class="page-title" dir="auto">CHƯƠNG TRÌNH CHUYÊN SÂU CẤP DOCTOR</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="36bc5e6f-95bd-8034-9975-f49ae68c9d47" class="">Học — Đọc trường — Sống trong trường — Điều hướng hệ</h2></div><div style="display:contents" dir="auto"><h1 id="36bc5e6f-95bd-80fb-a790-d399b232b41c" class="">LỜI MỞ ĐẦU VỀ TÍNH THỰC CHỨNG</h1></div><div style="display:contents" dir="auto"><hr id="36bc5e6f-95bd-8045-82cc-f3dbc7de582d"/></div><div style="display:contents" dir="auto"><h3 id="36bc5e6f-95bd-80b3-9708-d2b3b3e3fdff" class="">1. Tuyên bố nền tảng</h3></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-80d3-a061-f6671e37d46a" class="">Chương trình này được xây dựng trên sự tích hợp giữa:</p></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-8059-99c6-f826f3760662" class=""><strong>A. Thực hành gia hệ</strong></p></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-80cd-8256-de8c557000be" class="bulleted-list"><li style="list-style-type:disc">Hàng triệu ca lâm sàng trên toàn thế giới từ những năm 1990</li></ul></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-80d4-a93e-dd10fcc4d635" class="bulleted-list"><li style="list-style-type:disc">Được phát triển bởi Bert Hellinger và các cộng sự, dựa trên quan sát hệ thống</li></ul></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-80f4-8a76-c1d0df13bbcb" class=""><strong>B. Khoa học thần kinh và tâm sinh lý</strong> (dẫn chứng cụ thể bên dưới)</p></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-80f7-b8a1-caa80a3ae658" class="bulleted-list"><li style="list-style-type:disc">Interoception và cảm nhận cơ thể</li></ul></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-8043-adb6-d3038d9b854c" class="bulleted-list"><li style="list-style-type:disc">Hệ thần kinh tự chủ và phản ứng sinh lý</li></ul></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-8097-b75c-c5790c08a404" class="bulleted-list"><li style="list-style-type:disc">Tế bào gương và cảm nhận quan hệ</li></ul></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-802d-958d-fb3df5960f1f" class="bulleted-list"><li style="list-style-type:disc">Ký ức cơ thể và học tập hàm ẩn</li></ul></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-808a-a33a-d5c5b839524e" class=""><strong>C. Khoa học thực chứng từ các lĩnh vực</strong></p></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-80c3-8cd1-c7f03b43a45d" class="bulleted-list"><li style="list-style-type:disc">Lý thuyết hệ thống phức hợp</li></ul></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-80b4-b454-c9e9c290fd20" class="bulleted-list"><li style="list-style-type:disc">Suy luận nhân quả (causal inference)</li></ul></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-80f7-8c54-f7df4be33387" class="bulleted-list"><li style="list-style-type:disc">Xử lý dữ liệu thiếu (missing data theory)</li></ul></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-8095-a003-d6a7c2859443" class="bulleted-list"><li style="list-style-type:disc">Lý thuyết điều khiển tối ưu</li></ul></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-807a-8eaa-e3caf0e5c562" class="bulleted-list"><li style="list-style-type:disc">Di truyền học biểu sinh (transgenerational epigenetics)</li></ul></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-80cb-b049-e94d4e312324" class="bulleted-list"><li style="list-style-type:disc">Đạo đức y sinh</li></ul></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-8073-a49e-c5967ea8b5e4" class=""><strong>D. Bản thể học thực tại</strong> từ Trang Reality Architecture</p></div><div style="display:contents" dir="auto"><hr id="36bc5e6f-95bd-8037-a309-ccbdca26af18"/></div><div style="display:contents" dir="auto"><h3 id="36bc5e6f-95bd-80c6-996d-e255dbe15807" class="">2. Định nghĩa &quot;trường&quot; trong khuôn khổ khoa học</h3></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-80d6-8741-fa37df40129f" class=""><strong>Tuyên bố minh bạch:</strong></p></div><div style="display:contents" dir="auto"><blockquote id="36bc5e6f-95bd-80e1-9a20-d2310678ffbd" class=""><strong>&quot;Trường&quot; trong chương trình này KHÔNG được khẳng định là một thực thể vật lý đã được khoa học chứng minh (như trường điện từ hay trường hấp dẫn). Nó là một MÔ HÌNH CẤU TRÚC để mô tả và điều hướng các quan hệ, ký ức, ràng buộc, và tín hiệu phản hồi trong hệ thống.</strong></blockquote></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-8067-9495-c4911a26ddaa" class=""><strong>Cơ sở khoa học của mô hình &quot;trường&quot;:</strong></p></div><div style="display:contents" dir="ltr"><table id="36bc5e6f-95bd-80ea-b666-dd2efa050ca8" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80f2-aa35-ecd14242318c"><th id="@hEO" class="simple-table-header-color simple-table-header">Thành phần của &quot;trường&quot;</th><th id="x[pf" class="simple-table-header-color simple-table-header">Tương ứng khoa học</th><th id="dXZy" class="simple-table-header-color simple-table-header">Dẫn chứng</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8080-abb9-d306758cebab"><td id="@hEO" class="">Quan hệ</td><td id="x[pf" class="">Mạng lưới xã hội, lý thuyết gắn bó</td><td id="dXZy" class="">Bowlby (1969); Christakis &amp; Fowler (2009)</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80b9-82de-f8275fba5872"><td id="@hEO" class="">Ký ức</td><td id="x[pf" class="">Ký ức hàm ẩn, ký ức cơ thể, ký ức biểu sinh</td><td id="dXZy" class="">Squire (2004); Meaney (2010); Yehuda (2016)</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80f0-bef9-c1ab09a19f58"><td id="@hEO" class="">Ràng buộc</td><td id="x[pf" class="">Luật hệ thống, ràng buộc tiến hóa</td><td id="dXZy" class="">Meadows (2008); Gintis (2007)</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-809d-82e8-e0131bcf2c83"><td id="@hEO" class="">Tín hiệu</td><td id="x[pf" class="">Interoception, cảm nhận bản thể, tế bào gương</td><td id="dXZy" class="">Craig (2009); Damasio (1994); Rizzolatti (2004)</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8075-8727-c5e982c58f58"><td id="@hEO" class="">Phản hồi</td><td id="x[pf" class="">Vòng lặp phản hồi trong hệ thần kinh và xã hội</td><td id="dXZy" class="">Wiener (1948); Carver &amp; Scheier (1982)</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80b3-aaa5-d389352fcac6"><td id="@hEO" class="">Sửa sai</td><td id="x[pf" class="">Neuroplasticity, homeostatic regulation</td><td id="dXZy" class="">Doidge (2007); Sterling (2012)</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="36bc5e6f-95bd-8056-80ef-cc2ca62a2095"/></div><div style="display:contents" dir="auto"><h3 id="36bc5e6f-95bd-80ef-bdfe-c30a5ea6147f" class="">3. Dẫn chứng khoa học thần kinh cụ thể cho từng kênh biểu hiện của &quot;trường&quot;</h3></div><div style="display:contents" dir="auto"><h3 id="36bc5e6f-95bd-80ba-ac61-f942568430d4" class="">3.1. Cảm giác cơ thể (nặng, nhẹ, nóng, lạnh, thắt, giãn)</h3></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-8026-9ee6-faadda57a2b6" class=""><strong>Cơ sở khoa học thần kinh:</strong></p></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-80d2-962b-d9cb7935ef99" class="">Interoception là khả năng cảm nhận các tín hiệu từ bên trong cơ thể, được xử lý bởi:</p></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-80c9-aad0-f120e2bafd60" class="bulleted-list"><li style="list-style-type:disc"><strong>Insula</strong> (thùy đảo) — trung tâm xử lý interoception chính</li></ul></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-80c3-adee-c27142d3f7e1" class="bulleted-list"><li style="list-style-type:disc"><strong>Cortex somatosensory</strong> — xử lý cảm giác cơ thể</li></ul></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-8044-a3e2-f62eb5d8d2b1" class="bulleted-list"><li style="list-style-type:disc"><strong>Hệ thần kinh tự chủ</strong> (giao cảm và phó giao cảm)</li></ul></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-808b-bae7-ed2af4a4a49c" class=""><strong>Dẫn chứng nghiên cứu:</strong></p></div><div style="display:contents" dir="ltr"><table id="36bc5e6f-95bd-8070-a813-f0bad90e1cb7" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80a2-babf-d8dc7d5ef7a1"><th id="@ggB" class="simple-table-header-color simple-table-header">Nghiên cứu</th><th id="IRBC" class="simple-table-header-color simple-table-header">Phát hiện</th><th id="Wk^t" class="simple-table-header-color simple-table-header">Liên hệ thực hành</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8012-a85f-f46e3bd7a809"><td id="@ggB" class="">Craig (2002, 2009)</td><td id="IRBC" class="">Insula là trung tâm tích hợp cảm giác cơ thể và cảm xúc; con người có khả năng cảm nhận nhịp tim, hơi thở, nhiệt độ cơ thể</td><td id="Wk^t" class="">Khi đặt đại diện, insula người dẫn có thể phản ánh trạng thái của hệ</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8033-8fdf-dc1d07b4ef6b"><td id="@ggB" class="">Damasio (1994, 2018)</td><td id="IRBC" class="">&quot;Somatic markers&quot; — cơ thể lưu trữ dấu ấn của các quyết định và trải nghiệm cảm xúc trong quá khứ; những dấu ấn này ảnh hưởng đến hành vi hiện tại</td><td id="Wk^t" class="">Cảm giác nặng/nhẹ có thể là dấu ấn cơ thể của một quan hệ hoặc sự kiện trong gia hệ</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80bc-8686-ce0e2bc06134"><td id="@ggB" class="">Herbert &amp; Pollatos (2012)</td><td id="IRBC" class="">Meta-analysis cho thấy interoceptive accuracy có thể đo được và khác biệt giữa cá nhân; có tương quan với xử lý cảm xúc</td><td id="Wk^t" class="">Người dẫn cần luyện interoception để đọc tín hiệu chính xác</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8022-9ccc-c9182f6eada8"><td id="@ggB" class="">Critchley &amp; Garfinkel (2017)</td><td id="IRBC" class="">Interoception có 3 thành phần: accuracy (độ chính xác), sensibility (độ nhạy), awareness (nhận thức)</td><td id="Wk^t" class="">Phân biệt được: cảm thấy có tín hiệu (sensibility) ≠ tín hiệu đúng với trường (accuracy)</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h3 id="36bc5e6f-95bd-8025-97b9-d18891221b50" class="">3.2. Phản ứng cơ thể khi nghĩ về người thân, người mâu thuẫn</h3></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-80b4-a72d-d6b320899699" class=""><strong>Cơ sở khoa học thần kinh:</strong></p></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-8024-9956-fffda4ed7ee7" class="">Hệ thống gắn bó (attachment system) và mạng lưới thần kinh xã hội:</p></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-8016-a3c5-f1fae29fb263" class="bulleted-list"><li style="list-style-type:disc"><strong>Amygdala</strong> — xử lý nguy hiểm và đe dọa xã hội</li></ul></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-80c6-bfe3-c5f74feaf506" class="bulleted-list"><li style="list-style-type:disc"><strong>Cortex prefrontal ventromedial</strong> — xử lý giá trị xã hội và quan hệ</li></ul></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-80be-9ef0-dbb944c8392b" class="bulleted-list"><li style="list-style-type:disc"><strong>Hệ thống tế bào gương</strong> — cảm nhận trạng thái của người khác</li></ul></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-8065-be9d-df00412f1012" class=""><strong>Dẫn chứng nghiên cứu:</strong></p></div><div style="display:contents" dir="ltr"><table id="36bc5e6f-95bd-80af-887a-f96ec715ee30" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80c1-88db-cfcaef8e5e21"><th id="ju=b" class="simple-table-header-color simple-table-header">Nghiên cứu</th><th id="`V\b" class="simple-table-header-color simple-table-header">Phát hiện</th><th id="w=yS" class="simple-table-header-color simple-table-header">Liên hệ thực hành</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80cd-96a0-cdfe0f77a2a9"><td id="ju=b" class="">Eisenberger &amp; Lieberman (2004)</td><td id="`V\b" class="">Đau do loại trừ xã hội kích hoạt cùng vùng não với đau thể chất (dorsal anterior cingulate cortex)</td><td id="w=yS" class="">&quot;Trường&quot; loại trừ có thể cảm nhận như đau thể chất</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8064-b2ff-f561973bfe60"><td id="ju=b" class="">Rizzolatti &amp; Sinigaglia (2010)</td><td id="`V\b" class="">Tế bào gương kích hoạt khi quan sát người khác, tạo ra mô phỏng nội bộ trạng thái của họ</td><td id="w=yS" class="">Khi đặt đại diện, não người dẫn mô phỏng trạng thái của người được đặt</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80c8-8fc2-e02c4a536425"><td id="ju=b" class="">Coan (2011)</td><td id="`V\b" class="">Lý thuyết &quot;Social Baseline&quot; — não người sử dụng người thân như nguồn lực điều chỉnh; sự hiện diện/vắng mặt của người thân thay đổi phản ứng thần kinh</td><td id="w=yS" class="">Khoảng cách và hướng nhìn trong topology ảnh hưởng đến cảm nhận cơ thể</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-808a-84a9-ee5c15b3aa19"><td id="ju=b" class="">Beckes &amp; Coan (2011)</td><td id="`V\b" class="">Khi nhắc đến người gắn bó an toàn, phản ứng amygdala với đe dọa giảm</td><td id="w=yS" class="">Đặt &quot;mẹ&quot; vào đúng vị trí có thể làm dịu hệ thần kinh</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h3 id="36bc5e6f-95bd-8062-a28c-d41f4689121b" class="">3.3. Khoảng cách, hướng nhìn, và vị trí tương đối</h3></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-80d5-8ffa-d929bef3c7c7" class=""><strong>Cơ sở khoa học thần kinh:</strong></p></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-806d-8cb7-c9db64481f14" class="">Không gian xã hội được xử lý bởi các mạch thần kinh chồng lấn với không gian vật lý:</p></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-802f-8fb6-e433df2f0a59" class="bulleted-list"><li style="list-style-type:disc"><strong>Hippocampus</strong> — bản đồ không gian và bản đồ xã hội</li></ul></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-80a1-8ef3-c1f9f19a850c" class="bulleted-list"><li style="list-style-type:disc"><strong>Cortex parietal</strong> — xử lý khoảng cách và vị trí</li></ul></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-80cf-96a7-c7ede4af3693" class="bulleted-list"><li style="list-style-type:disc"><strong>Cortex prefrontal</strong> — ước lượng khoảng cách xã hội</li></ul></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-8010-aac1-de02cd13b24a" class=""><strong>Dẫn chứng nghiên cứu:</strong></p></div><div style="display:contents" dir="ltr"><table id="36bc5e6f-95bd-804b-a93a-d10ee6d0c708" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8040-92d7-cae3243c2b8e"><th id="jc&gt;w" class="simple-table-header-color simple-table-header">Nghiên cứu</th><th id="oJsZ" class="simple-table-header-color simple-table-header">Phát hiện</th><th id="Zi&gt;U" class="simple-table-header-color simple-table-header">Liên hệ thực hành</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80e8-a2ce-e594b008197c"><td id="jc&gt;w" class="">Parkinson &amp; Wheatley (2014)</td><td id="oJsZ" class="">&quot;Social space&quot; được mã hóa trong hippocampus giống như physical space; khoảng cách xã hội và khoảng cách vật lý dùng chung cơ chế thần kinh</td><td id="Zi&gt;U" class="">Thay đổi vị trí vật lý của đại diện thay đổi cảm nhận về khoảng cách xã hội</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-805e-bf74-c41420a58372"><td id="jc&gt;w" class="">Hall (1966) — dù cũ nhưng nền tảng</td><td id="oJsZ" class="">Khoảng cách giao tiếp (intimate, personal, social, public) có cơ sở sinh học và văn hóa</td><td id="Zi&gt;U" class="">Đọc topology: ai trong intimate distance, ai ngoài rìa</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80f1-b7e4-d9dea8501e75"><td id="jc&gt;w" class="">Kennedy &amp; Adolphs (2012)</td><td id="oJsZ" class="">Các vùng não xử lý social distance (khoảng cách xã hội) chồng lấn với vùng xử lý physical distance</td><td id="Zi&gt;U" class="">&quot;Gần&quot; trong topology không chỉ nghĩa bóng mà có cơ sở thần kinh</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8037-9399-fbace85539b7"><td id="jc&gt;w" class="">Todorov (2017)</td><td id="oJsZ" class="">Con người đánh giá social hierarchy (cao/thấp, trước/sau) trong vòng vài trăm mili giây</td><td id="Zi&gt;U" class="">Hướng nhìn và vị trí cao/thấp ảnh hưởng đến cảm nhận quyền lực</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h3 id="36bc5e6f-95bd-802d-b4d4-e138d1067e30" class="">3.4. Tín hiệu khi nói câu ghi nhận / giải pháp</h3></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-80a5-9730-e7cb1e67601d" class=""><strong>Cơ sở khoa học thần kinh:</strong></p></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-807e-ad70-c344956bfdd3" class="">Ngôn ngữ ảnh hưởng đến trạng thái cơ thể qua:</p></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-8032-99ce-d517f6fd70b2" class="bulleted-list"><li style="list-style-type:disc"><strong>Hiệu ứng nội tại</strong> (embodied language comprehension)</li></ul></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-8087-b41e-ec3aac298644" class="bulleted-list"><li style="list-style-type:disc"><strong>Hệ thống tế bào gương ngữ nghĩa</strong></li></ul></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-80ea-ba64-c86c5a9bbcea" class=""><strong>Dẫn chứng nghiên cứu:</strong></p></div><div style="display:contents" dir="ltr"><table id="36bc5e6f-95bd-80f8-8213-e13715110dea" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8007-9d2d-d1cddfb37b64"><th id="Xh~A" class="simple-table-header-color simple-table-header">Nghiên cứu</th><th id="V[mo" class="simple-table-header-color simple-table-header">Phát hiện</th><th id="hb^L" class="simple-table-header-color simple-table-header">Liên hệ thực hành</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8064-a0c0-e8b4fbadabb7"><td id="Xh~A" class="">Pulvermüller (2013)</td><td id="V[mo" class="">Hiểu từ chỉ hành động (chạy, nắm) kích hoạt vùng vận động tương ứng</td><td id="hb^L" class="">Nói &quot;con xin trả lại&quot; có thể kích hoạt cảm giác nhẹ ở vai — có cơ sở thần kinh</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8084-9491-f9de96ef7290"><td id="Xh~A" class="">Glenberg (2015)</td><td id="V[mo" class="">Ngôn ngữ được &quot;nhúng cơ thể&quot; (embodied); câu phù hợp với trạng thái cơ thể xử lý dễ hơn</td><td id="hb^L" class="">Câu đúng với trường tạo cảm giác &quot;đúng&quot; ở cơ thể; câu sai tạo cảm giác &quot;vướng&quot;</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80c0-82f7-f9e3c59e04f6"><td id="Xh~A" class="">Nook &amp; đồng nghiệp (2017)</td><td id="V[mo" class="">&quot;Affective labeling&quot; — gọi tên cảm xúc làm giảm phản ứng amygdala</td><td id="hb^L" class="">Gọi tên cái chưa được nói có tác dụng điều hòa hệ thần kinh</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8065-ba41-d5ea963849c5"><td id="Xh~A" class="">Lieberman (2007)</td><td id="V[mo" class="">Gọi tên cảm xúc chuyển hoạt động từ amygdala sang prefrontal cortex, giảm đau khổ chủ quan</td><td id="hb^L" class="">Đây là cơ sở khoa học cho hiệu ứng của &quot;câu ghi nhận&quot;</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="36bc5e6f-95bd-80c0-9686-ca5f21a93c6e"/></div><div style="display:contents" dir="auto"><h3 id="36bc5e6f-95bd-809e-8fe8-efd0d1e763e6" class="">4. Khoa học về trường xuyên thế hệ (Transgenerational)</h3></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-807d-8eed-c7c00c2d6a55" class=""><strong>Tuyên bố minh bạch:</strong></p></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-803e-a66b-c7b5e60cf087" class="">Khoa học <strong>CHƯA</strong> chứng minh &quot;trường xuyên thế hệ&quot; là một trường vật lý. Tuy nhiên, có bằng chứng về <strong>cơ chế sinh học</strong> cho phép ảnh hưởng từ thế hệ trước sang thế hệ sau:</p></div><div style="display:contents" dir="auto"><h3 id="36bc5e6f-95bd-80d3-a509-dbdf268bb6e5" class="">4.1. Di truyền biểu sinh (Epigenetics)</h3></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-80bd-9685-e444d83dddea" class=""><strong>Dẫn chứng nghiên cứu:</strong></p></div><div style="display:contents" dir="ltr"><table id="36bc5e6f-95bd-80ed-80ba-de104fde35d4" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80b1-ae90-e99261ebe50d"><th id="cN@h" class="simple-table-header-color simple-table-header">Nghiên cứu</th><th id="tPu~" class="simple-table-header-color simple-table-header">Phát hiện</th><th id="CGHG" class="simple-table-header-color simple-table-header">Ý nghĩa</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-804d-90e5-f3bb5478eb08"><td id="cN@h" class="">Meaney (2001, 2010)</td><td id="tPu~" class="">Chuột con được mẹ chăm sóc nhiều có biểu hiện gene khác với chuột bị bỏ mặc; khác biệt này kéo dài sang thế hệ sau</td><td id="CGHG" class="">Chăm sóc (hay sang chấn) có thể &quot;ghi&quot; vào hệ biểu sinh</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80a3-90d5-c159d608da14"><td id="cN@h" class="">Yehuda &amp; đồng nghiệp (2014, 2016)</td><td id="tPu~" class="">Con cái của người sống sót sau Holocaust có mức cortisol và biểu hiện gene liên quan đến stress khác biệt so với nhóm chứng</td><td id="CGHG" class="">Sang chấn có thể ảnh hưởng đến thế hệ sau qua cơ chế biểu sinh</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80f3-ad09-e2c974fa06f1"><td id="cN@h" class="">Dias &amp; Ressler (2014)</td><td id="tPu~" class="">Chuột được huấn luyện sợ mùi acetophenone; con cháu của chúng cũng sợ mùi đó mà không cần tiếp xúc trực tiếp</td><td id="CGHG" class="">Ký ức sợ có thể truyền qua biểu sinh qua vài thế hệ</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-804b-8518-c3f933e4cfb1" class=""><strong>Giới hạn:</strong> Các nghiên cứu trên người còn hạn chế và đang tranh luận. Không khẳng định &quot;mọi thứ đều di truyền biểu sinh&quot;.</p></div><div style="display:contents" dir="auto"><h3 id="36bc5e6f-95bd-8011-b1db-eba577cfaff8" class="">4.2. Ký ức hàm ẩn (Implicit memory) và mô thức lặp</h3></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-80a0-9c6c-e9c7cee8d9ff" class=""><strong>Dẫn chứng nghiên cứu:</strong></p></div><div style="display:contents" dir="ltr"><table id="36bc5e6f-95bd-8053-8f47-c2a6c6e399e4" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80d6-8828-f66c5f3856cb"><th id="OkD\" class="simple-table-header-color simple-table-header">Nghiên cứu</th><th id="S{ss" class="simple-table-header-color simple-table-header">Phát hiện</th><th id="qW\L" class="simple-table-header-color simple-table-header">Ý nghĩa</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8097-9e82-e638f926a3b8"><td id="OkD\" class="">Schacter (1987)</td><td id="S{ss" class="">Ký ức hàm ẩn ảnh hưởng đến hành vi mà không cần nhận thức có chủ ý</td><td id="qW\L" class="">Mô thức lặp trong gia hệ có thể là ký ức hàm ẩn được truyền qua hành vi và ngôn ngữ</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80ce-8ae4-cc018ed00fe1"><td id="OkD\" class="">Fraiberg (1975)</td><td id="S{ss" class="">&quot;Ghosts in the nursery&quot; — cha mẹ vô thức tái diễn với con cái những trải nghiệm từ thời thơ ấu của chính họ</td><td id="qW\L" class="">Không cần &quot;trường siêu hình&quot; để giải thích mô thức lặp</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8003-8f35-edc77b3fc573"><td id="OkD\" class="">Siegel (2012)</td><td id="S{ss" class="">Interpersonal neurobiology — não người phát triển trong quan hệ; mô hình quan hệ thời thơ ấu trở thành cấu trúc bên trong</td><td id="qW\L" class="">Mô thức gia hệ không phải &quot;di truyền kỳ bí&quot; mà là cấu trúc thần kinh được hình thành từ quan hệ</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="36bc5e6f-95bd-8080-9754-eed7616e60a7"/></div><div style="display:contents" dir="auto"><h3 id="36bc5e6f-95bd-802f-be9e-ccdbfcf8283a" class="">5. Khoa học về tác động của can thiệp (điều hướng trường)</h3></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-8042-9139-d9d2b52110fe" class=""><strong>Dẫn chứng nghiên cứu về hiệu quả của các can thiệp tương tự gia hệ:</strong></p></div><div style="display:contents" dir="ltr"><table id="36bc5e6f-95bd-80ff-9bd9-d692620fda7b" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80ab-bb7d-c21f26fa0d51"><th id="^JPw" class="simple-table-header-color simple-table-header">Phương pháp</th><th id="ydUL" class="simple-table-header-color simple-table-header">Nghiên cứu</th><th id="]IpF" class="simple-table-header-color simple-table-header">Phát hiện</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80ac-94e5-c998cfb4278e"><td id="^JPw" class="">Family constellations (nghiên cứu đầu tiên)</td><td id="ydUL" class="">Weber &amp; đồng nghiệp (2005) — nghiên cứu tại Đức</td><td id="]IpF" class="">Cải thiện triệu chứng sau 1 năm ở nhiều lĩnh vực; cần thêm RCT</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8080-9ff1-cb0043fcf812"><td id="^JPw" class="">Systemic therapy (nói chung)</td><td id="ydUL" class="">Von Sydow &amp; đồng nghiệp (2010) — meta-analysis</td><td id="]IpF" class="">Hiệu quả cho nhiều rối loạn (trầm cảm, lo âu, rối loạn ăn uống)</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8097-a0fd-e235641dc593"><td id="^JPw" class="">Attachment-based family therapy</td><td id="ydUL" class="">Diamond &amp; đồng nghiệp (2016) — RCT</td><td id="]IpF" class="">Giảm trầm cảm và ý định tự tử ở thanh thiếu niên</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-800f-92eb-f2af2c26e6e6"><td id="^JPw" class="">Interpersonal psychotherapy (IPT)</td><td id="ydUL" class="">Cuijpers &amp; đồng nghiệp (2011) — meta-analysis</td><td id="]IpF" class="">Hiệu quả cho trầm cảm, cơ chế qua cải thiện quan hệ</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-8048-b587-c49b5f833351" class=""><strong>Giới hạn:</strong> Chưa có RCT lớn cho riêng &quot;family constellations&quot; với nhóm đối chứng chặt chẽ. Do đó, không khẳng định &quot;đã được khoa học chứng minh tuyệt đối&quot;.</p></div><div style="display:contents" dir="auto"><hr id="36bc5e6f-95bd-807e-a407-ec41df25f5c2"/></div><div style="display:contents" dir="auto"><h3 id="36bc5e6f-95bd-80da-aa37-f14daec31add" class="">6. Tổng kết: Cái gì CÓ và KHÔNG CÓ cơ sở khoa học</h3></div><div style="display:contents" dir="ltr"><table id="36bc5e6f-95bd-8040-98fb-c563a30528d9" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8082-9658-f0085b688210"><th id="P\@c" class="simple-table-header-color simple-table-header">Khẳng định</th><th id="[M]W" class="simple-table-header-color simple-table-header">Cơ sở khoa học</th><th id="O\E_" class="simple-table-header-color simple-table-header">Mức độ bằng chứng</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8007-b40b-f5c704cc39aa"><td id="P\@c" class="">Con người có thể cảm nhận tín hiệu từ cơ thể</td><td id="[M]W" class="">Có — interoception</td><td id="O\E_" class="">Cao (nhiều RCT, meta-analysis)</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80ce-aca9-dc883889f7fa"><td id="P\@c" class="">Tín hiệu cơ thể thay đổi theo trạng thái cảm xúc và quan hệ</td><td id="[M]W" class="">Có — somatic markers, social neuroscience</td><td id="O\E_" class="">Cao</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8049-b476-cefa28ea026f"><td id="P\@c" class="">Khoảng cách và hướng nhìn ảnh hưởng đến cảm nhận</td><td id="[M]W" class="">Có — social space, proxemics</td><td id="O\E_" class="">Cao</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8033-b0c5-c01fd410f88b"><td id="P\@c" class="">Gọi tên cảm xúc làm giảm phản ứng căng thẳng</td><td id="[M]W" class="">Có — affective labeling</td><td id="O\E_" class="">Cao</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-807a-94cc-c3218e0ca12f"><td id="P\@c" class="">Có mô thức lặp trong gia hệ</td><td id="[M]W" class="">Có — implicit memory, attachment theory</td><td id="O\E_" class="">Cao</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8076-b0c0-e921acc59deb"><td id="P\@c" class="">Sang chấn có thể ảnh hưởng đến thế hệ sau</td><td id="[M]W" class="">Có — epigenetics (ở động vật), nghiên cứu quan sát ở người</td><td id="O\E_" class="">Trung bình - Cao (động vật); Trung bình (người)</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80c9-9879-e039fb6e78ee"><td id="P\@c" class="">&quot;Trường gia hệ&quot; là một trường vật lý</td><td id="[M]W" class="">Không — chưa có bằng chứng</td><td id="O\E_" class="">Rất thấp (chưa có)</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80c1-8669-ed57c9e47197"><td id="P\@c" class="">Family constellations có hiệu quả chữa bệnh</td><td id="[M]W" class="">Có nghiên cứu ban đầu, cần thêm RCT</td><td id="O\E_" class="">Thấp - Trung bình</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="36bc5e6f-95bd-801d-8b03-e8403837daa6"/></div><div style="display:contents" dir="auto"><h3 id="36bc5e6f-95bd-8078-b2a1-e4d79d4a2831" class="">7. Kết luận mở đầu</h3></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-80f7-8e23-fc05f967d5cc" class="">Chương trình này sử dụng <strong>ngôn ngữ &quot;trường&quot; như một mô hình làm việc (working model)</strong> để mô tả các hiện tượng có cơ sở trong:</p></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-809f-8178-d1dda5a59c43" class="bulleted-list"><li style="list-style-type:disc">Khoa học thần kinh (interoception, tế bào gương, social space)</li></ul></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-80b8-a9df-cf0e7c47ad24" class="bulleted-list"><li style="list-style-type:disc">Tâm lý học (gắn bó, ký ức hàm ẩn, mô thức lặp)</li></ul></div><div style="display:contents" dir="auto"><ul id="36bc5e6f-95bd-8038-9770-d8fa80858282" class="bulleted-list"><li style="list-style-type:disc">Sinh học (biểu sinh, hệ thần kinh tự chủ)</li></ul></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-8014-8c10-c8356792f979" class=""><strong>Không có khẳng định siêu hình.</strong> Mọi &quot;tín hiệu trường&quot; đều được hiểu là tín hiệu sinh lý - thần kinh có thể đo lường bằng các phương pháp khoa học (nhịp tim, độ dẫn da, hoạt động não, hormone).</p></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-80f9-ac6c-ee3a6a0a0d07" class="">Người học được khuyến khích:</p></div><div style="display:contents" dir="auto"><ol type="1" id="36bc5e6f-95bd-806d-9054-c84c17ccb0aa" class="numbered-list" start="1"><li><strong>Đọc các nghiên cứu gốc</strong> được trích dẫn</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="36bc5e6f-95bd-8054-b1fa-cfdbe324c286" class="numbered-list" start="2"><li><strong>Cập nhật bằng chứng mới</strong> vì khoa học thay đổi</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="36bc5e6f-95bd-806d-aec1-c7497f5cb948" class="numbered-list" start="3"><li><strong>Phân biệt giữa mô hình làm việc và sự thật đã được chứng minh</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="36bc5e6f-95bd-8033-943d-d8ff0613a947" class="numbered-list" start="4"><li><strong>Không tuyên bố quá mức</strong> với thân chủ (ví dụ: &quot;khoa học đã chứng minh trường gia hệ&quot;)</li></ol></div><div style="display:contents" dir="auto"><hr id="36bc5e6f-95bd-8077-bbc9-e0142b92fe81"/></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-803b-b265-d83adeb366f6" class=""><strong>Tài liệu tham khảo chính cho phần mở đầu:</strong></p></div><div style="display:contents" dir="ltr"><table id="36bc5e6f-95bd-80a7-9b12-ee1ed87a37d8" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8044-aaa5-dec7c5590517"><th id="S{U;" class="simple-table-header-color simple-table-header">Lĩnh vực</th><th id="Z`Vu" class="simple-table-header-color simple-table-header">Tài liệu</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80d6-b1e7-f4c2d7d7ecaa"><td id="S{U;" class="">Interoception</td><td id="Z`Vu" class="">Craig (2009); Critchley &amp; Garfinkel (2017)</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8034-955c-cfe8a5621a04"><td id="S{U;" class="">Somatic markers</td><td id="Z`Vu" class="">Damasio (1994, 2018)</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80d4-b1bd-d786a904c82f"><td id="S{U;" class="">Tế bào gương</td><td id="Z`Vu" class="">Rizzolatti &amp; Sinigaglia (2010)</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8057-b1e0-d41012ec4716"><td id="S{U;" class="">Khoảng cách xã hội</td><td id="Z`Vu" class="">Hall (1966); Parkinson &amp; Wheatley (2014)</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80a1-b2bd-fbe5f004cded"><td id="S{U;" class="">Gắn bó</td><td id="Z`Vu" class="">Bowlby (1969); Coan (2011)</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-8062-acf1-ce6ce8359e10"><td id="S{U;" class="">Affective labeling</td><td id="Z`Vu" class="">Lieberman (2007); Nook &amp; cs (2017)</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80c9-b5ff-cba4556154a2"><td id="S{U;" class="">Ký ức hàm ẩn</td><td id="Z`Vu" class="">Schacter (1987); Squire (2004)</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80f3-a616-c6bca3bafc78"><td id="S{U;" class="">Epigenetics (sang chấn)</td><td id="Z`Vu" class="">Meaney (2010); Yehuda (2016)</td></tr></div><div style="display:contents" dir="ltr"><tr id="36bc5e6f-95bd-80d0-b01f-ee06c3fd4f55"><td id="S{U;" class="">Hiệu quả systemic therapy</td><td id="Z`Vu" class="">Von Sydow &amp; cs (2010)</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="36bc5e6f-95bd-806b-a4fe-d84e45e516af" class="">
</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
