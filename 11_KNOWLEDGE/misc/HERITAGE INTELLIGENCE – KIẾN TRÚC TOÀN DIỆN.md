---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>HERITAGE INTELLIGENCE – KIẾN TRÚC TOÀN DIỆN</title><style>
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
	
</style></head><body><article id="353c5e6f-95bd-8010-b88a-cedba1bbf8ae" class="page sans"><header><h1 class="page-title" dir="auto">HERITAGE INTELLIGENCE – KIẾN TRÚC TOÀN DIỆN</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="353c5e6f-95bd-8089-8289-dccc78a08bba" class="">TỔNG QUAN</h2></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8029-b067-e65590f4b261" class="">Heritage Intelligence là một <strong>hệ thống quản trị quyết định đa tầng</strong>, được xây dựng trên nguyên lý rằng <strong>tri thức sống còn được phân tán vào nhiều lớp tín hiệu và chỉ có thể giải mã khi hội tụ đủ các lớp và đúng ngữ cảnh</strong>.</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80ff-9af2-cf266145a50c" class="">Hệ thống này bao phủ:</p></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-80a5-a70e-fc39011e788d" class="bulleted-list"><li style="list-style-type:disc">Từ entropy vũ trụ đến hành vi vi mô của thị trường</li></ul></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-80cb-bded-deb6eebde141" class="bulleted-list"><li style="list-style-type:disc">Từ sóng não của con người đến dòng chảy văn minh</li></ul></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-8081-8a15-c7f22d672277" class="bulleted-list"><li style="list-style-type:disc">Từ dự báo đến phòng thủ, khai thác, kiến tạo, 
và cuối cùng là <strong>mục đích</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-804c-a89e-c9fe9364f44d"/></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80ac-94b2-e50cc210e7d9"/></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80fe-9dfe-d155be3fd907"/></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80ad-ad14-e3853f46f649"/></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80f2-9547-d0901e2b4044"/></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80d1-83a2-e1c44eb78f5f"/></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-801b-ab7f-c4f5aa2c496d"/></div><div style="display:contents" dir="auto"><h2 id="353c5e6f-95bd-8083-aba4-db20cd49805e" class="">PHẦN 8: CÁC BẤT BIẾN (INVARIANTS)</h2></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-8038-97ac-eccd0a5d9517"/></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-8008-84a1-cc06cf867e51"/></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80bd-833b-d80d1dd78844"/></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80a4-8f49-e0c39f53c403"/></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80dc-95da-d71a2a09b172" class="">Đây là bản mở rộng <strong>tối đa chi tiết</strong> cho <strong>PHẦN 2: KIẾN TRÚC TỔNG THỂ (32 TẦNG + 10 LỚP TÍN HIỆU)</strong>.</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8030-859f-c3233fc498c8" class="">Mỗi tầng được phân tích thành: <strong>định nghĩa, phương trình, biến trạng thái, chế độ thất bại, chế độ phục hồi, 
và kết nối với các tầng khác</strong>.</p></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-8059-9e9a-c4f9d0309a63"/></div><div style="display:contents" dir="auto"><h1 id="353c5e6f-95bd-8025-9487-f79f51cdc68f" class="">HERITAGE INTELLIGENCE – KIẾN TRÚC TỔNG THỂ (BẢN MỞ RỘNG TỐI ĐA)</h1></div><div style="display:contents" dir="auto"><h2 id="353c5e6f-95bd-8002-8e38-cf0680fe2ca7" class="">PHẦN 2.1: CÁC TẦNG NỀN TẢNG (T-4 → T-0.2)</h2></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-800d-833b-f899c83cb2ec"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-80ca-b56f-c6de36d3e5e4" class="">T-4: THERMODYNAMIC CONSTRAINTS</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8052-8e10-d854aa49f7f4" class=""><strong>Định nghĩa:</strong> Các ràng buộc vật lý cơ bản về năng lượng, entropy, và thời gian. 
Đây là tầng sâu nhất mà Heritage có thể tiếp cận (trước đó là triết học/thần học).</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80be-9b78-c3df3295e202" class=""><strong>Phương trình nền tảng:</strong></p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80b6-b8d2-dc42970eadd2" class="">\[<br/>\boxed{\Delta S_{\text{universe}} \geq 0}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-802b-a2f3-c09f04cff2b6" class="">\[<br/>\boxed{\Delta E = Q - W}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8050-9e9c-f90ac78a2c1a" class="">\[<br/>\boxed{dS = \frac{dQ_{\text{rev}}}{T}}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8074-8ba9-e89e542782a2" class=""><strong>Các biến trạng thái:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-802b-9a3a-ca3e85c1be6e" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-801b-b667-cdf3efbd142a"><th id="ccrV" class="simple-table-header-color simple-table-header">Biến</th><th id="&gt;LFx" class="simple-table-header-color simple-table-header">Tên</th><th id="^Mx@" class="simple-table-header-color simple-table-header">Công thức</th><th id="z|Kq" class="simple-table-header-color simple-table-header">Ý nghĩa trong Heritage</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80f0-b688-d7e4ba5102b0"><td id="ccrV" class="">S_entropy</td><td id="&gt;LFx" class="">Entropy thông tin</td><td id="^Mx@" class=""><code>H(X) = -∑ p(x) log p(x)</code></td><td id="z|Kq" class="">Đo độ bất định của tín hiệu</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80c6-9e20-d0501be2d0cd"><td id="ccrV" class="">E_energy</td><td id="&gt;LFx" class="">Năng lượng hệ thống</td><td id="^Mx@" class=""><code>E = E_capital + E_attention + E_compute</code></td><td id="z|Kq" c
lass="">Tài nguyên khả dụng</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-804f-b11e-c70001943f9f"><td id="ccrV" class="">T_temp</td><td id="&gt;LFx" class="">Nhiệt độ thị trường</td><td id="^Mx@" class=""><code>T = volatility × volume</code></td><td id="z|Kq" class="">Độ &quot;nóng&quot; 
của thị trường</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80c5-bd5e-d4dad676abe0"><td id="ccrV" class="">Q_flow</td><td id="&gt;LFx" class="">Dòng năng lượng</td><td id="^Mx@" class=""><code>dE/dt</code></td><td id="z|Kq" class="">Tốc độ tiêu hao/bổ sung tài nguyên</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8048-bf97-f727675b9a59" class=""><strong>Các định luật áp dụng vào Heritage:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-8090-848e-f5f3008360bb" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-803b-9988-fdede1c5e257"><th id="AYF~" class="simple-table-header-color simple-table-header">Định luật</th><th id="]r[^" class="simple-table-header-color simple-table-header">Công thức</th><th id="OJ]|" class="simple-table-header-color simple-table-header">Áp dụng</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-801e-99fb-f68ab64afcd8"><td id="AYF~" class="">Entropy không giảm</td><td id="]r[^" class=""><code>ΔS ≥ 0</code></td><td id="OJ]|" class="">Thông tin càng xử lý càng mất mát (qua τ layers)</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80c3-8fdb-edcfd77716f9"><td id="AYF~" class="">Bảo toàn năng lượng</td><td id="]r[^" class=""><code>E_in = E_out + ΔE_system</code></td><td id="OJ]|" class="">Capital không tự sinh ra</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80aa-8162-d12bc96aac98"><td id="AYF~" class="">Cân bằng nhiệt động</td><td id="]r[^" class="">Hệ thống tiến về cân bằng</td><td id="OJ]|" class="">Thị trường có xu hướng về MEP</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8059-9cb9-e9d22b9fe10f"><td id="AYF~" class="">Chu trình Carnot</td><td id="]r[^" class=""><code>η ≤ 1 - T_c/T_h</code></td><td id="OJ]|" class="">Không thể c
huyển hóa 100% thông tin thành lợi nhuận</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-805d-981a-ffecc4b7d792" class=""><strong>Chế độ thất bại:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-807f-b177-e7adf6a52a86" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80ec-90a3-e433eb053430"><th id="gq?v" class="simple-table-header-color simple-table-header">Failure Mode</th><th id="YckW" class="simple-table-header-color simple-table-header">Điều kiện</th><th id="x`aw" class="simple-table-header-color simple-table-header">Hậu quả</th><th id="ufe^" class="simple-table-header-color simple-table-header">Phục hồi</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-806b-8c0c-d770e41126b2"><td id="gq?v" class="">Entropy exhaustion</td><td id="YckW" class=""><code>S_entropy → 0</code></td><td id="x`aw" class="">Không còn thông tin mới</td><td id="ufe^" class="">Chờ sự kiện mới</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8027-9769-fec7edc83c56"><td id="gq?v" class="">Energy depletion</td><td id="YckW" class=""><code>E_energy &lt; 
E_min</code></td><td id="x`aw" class="">Hết năng lượng để hành động</td><td id="ufe^" class="">Nạp vốn, nghỉ ngơi</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8060-878f-eca4b341d6d4"><td id="gq?v" class="">Thermal death</td><td id="YckW" class="">Thị trường quá phẳng</td><td id="x`aw" class="">Không có edge</td><td id="ufe^" class="">Chuyển sang chế độ khác</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80ce-9872-e618e7e0e6c1" class=""><strong>Kết nối đến tầng khác:</strong></p></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-80c9-85fc-dbbfd3ec8cb6" class="bulleted-list"><li style="list-style-type:disc">T-4 → T-3.8: Entropy là giới hạn của thông tin</li></ul></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-80c9-906c-f417bf5654d7" class="bulleted-list"><li style="list-style-type:disc">T-4 → T-0.5: Randomness là biểu hiện của entropy ở cấp vi mô</li></ul></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-806a-923c-e1da1f66efae"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-8018-8b1b-cfe58a77d54d" class="">T-3.8: INFORMATION-THEORETIC LIMITS</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80be-be82-c18831da0cd0" class=""><strong>Định nghĩa:</strong> Các giới hạn cơ bản của việc truyền tải và xử lý thông tin (Shannon, Kolmogorov, 
Fisher).</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8089-905f-f1b4cf898407" class=""><strong>Phương trình nền tảng:</strong></p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8077-983f-c34917a1dbc3" class="">\[<br/>\boxed{C = B \log_2\left(1 + \frac{S}{N}\right)}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8023-9b28-d1b3ce02b0dc" class="">\[<br/>\boxed{K(x) = \text{độ dài chương trình ngắn nhất sinh ra } x}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-803f-ba55-f59b532cb88b" class="">\[<br/>\boxed{I(X;Y) = H(X) - H(X|Y)}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80e4-964a-f3710cec670c" class=""><strong>Các biến trạng thái:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-803b-9e43-d968cd058851" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80e2-9a15-cc4ac75598bb"><th id="M}&lt;P" class="simple-table-header-color simple-table-header">Biến</th><th id="^d@w" class="simple-table-header-color simple-table-header">Tên</th><th id="&lt;ba^" class="simple-table-header-color simple-table-header">Công thức</th><th id="ZEXi" class="simple-table-header-color simple-table-header">Ý nghĩa</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-804f-b3d2-e0924240bc5a"><td id="M}&lt;P" class="">C_channel</td><td id="^d@w" class="">Dung lượng kênh</td><td id="&lt;ba^" class=""><code>B × log2(1 + SNR)</code></td><td id="ZEXi" class="">Tối đa thông tin có thể nhận</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8053-9af2-f02aa8b3ff87"><td id="M}&lt;P" class="">SNR</td><td id="^d@w" class="">Signal-to-Noise Ratio</td><td id="&lt;ba^" class=""><code>P_signal / P_noise</code></td><td id="ZEXi" class="">Chất lượng tín hiệu</td></tr></div><div style="display:contents" d
ir="ltr"><tr id="353c5e6f-95bd-80d9-91bf-c04846ffc862"><td id="M}&lt;P" class="">I_mutual</td><td id="^d@w" class="">Thông tin tương hỗ</td><td id="&lt;ba^" class="">`H(X) - H(X</td><td id="ZEXi" class="">Y)`</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-805b-afdf-f0cedc2e0e60"><td id="M}&lt;P" class="">K_complexity</td><td id="^d@w" class="">Kolmogorov complexity</td><td id="&lt;ba^" class="">Độ dài chương trình ngắn nhất</td><td id="ZEXi" class="">Độ phức tạp của pattern</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80cc-961f-f843558395e9" class=""><strong>Giới hạn của Heritage:</strong></p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80ad-b65d-c14f4c7aa337" class="">\[<br/>\boxed{I_{\text{processed}}(t) \leq C_{\text{channel}} \times \eta_{\text{efficiency}}}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8087-801e-c18a6bf85f44" class="">\[<br/>\boxed{\text{PredictionError} \geq \frac{1}{2} \ln\left(\frac{1 + \text{SNR}}{\text{SNR}}\right)}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80b6-8297-d49ad491b19d" class=""><strong>Chế độ thất bại:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-8076-83fa-c231c340a5d3" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80f5-974c-d15b37219fd6"><th id="[BCN" class="simple-table-header-color simple-table-header">Failure Mode</th><th id="[jN&gt;" class="simple-table-header-color simple-table-header">Điều kiện</th><th id="=[KS" class="simple-table-header-color simple-table-header">Hậu quả</th><th id="O@^D" class="simple-table-header-color simple-table-header">Phục hồi</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80fa-bd3a-dc32ecfacdff"><td id="[BCN" class="">Channel saturation</td><td id="[jN&gt;" c
lass=""><code>I_signal &gt; C_channel</code></td><td id="=[KS" class="">Mất thông tin</td><td id="O@^D" class="">Giảm rate, tăng B</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8015-8697-f95bbf770607"><td id="[BCN" class="">Noise dominance</td><td id="[jN&gt;" class=""><code>SNR &lt; 1</code></td><td id="=[KS" class="">Không tách được signal</td><td id="O@^D" class="">Lọc nhiễu, tăng công suất</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80a1-9ce5-ce401714cafc"><td id="[BCN" class="">Complexity overflow</td><td id="[jN&gt;" class=""><code>K(x) &gt; 
K_max</code></td><td id="=[KS" class="">Không thể nén/nhận dạng</td><td id="O@^D" class="">Dùng heuristic</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-804e-843f-c5b671ba3408" class=""><strong>Kết nối:</strong></p></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-80a4-b5c4-e76df7984851" class="bulleted-list"><li style="list-style-type:disc">T-3.8 → T1 (địa chất): giới hạn của cảm biến địa chất</li></ul></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-809f-961d-d104e8dda448" class="bulleted-list"><li style="list-style-type:disc">T-3.8 → T0 (macro plumbing): băng thông dữ liệu thị trường</li></ul></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-804d-b405-cba97ec1e687"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-8063-b3b8-e4d4587882db" class="">T-3.6: GAME-THEORETIC DYNAMICS</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8061-863d-fab483be0cbc" class=""><strong>Định nghĩa:</strong> Tương tác chiến lược giữa các tác nhân (trader, institution, AI, government).</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80c7-9837-f39db62e7387" class=""><strong>Phương trình nền tảng:</strong></p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8011-8cdc-e8dd9dd984af" class="">\[<br/>\boxed{\text{NE} = \{\sigma_i^<em>\}_{i=1}^n \mid \forall i, u_i(\sigma_i^</em>, \sigma_{-i}^<em>) \geq u_i(\sigma_i, 
\sigma_{-i}^</em>)}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8010-93c7-d6d95e53fb96" class=""><strong>Các dạng cân bằng:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-80ec-8d02-c393b622a390" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8061-9984-e857c3cf962d"><th id="Gg&gt;p" class="simple-table-header-color simple-table-header">Loại</th><th id="AYxm" class="simple-table-header-color simple-table-header">Công thức</th><th id="hPu_" class="simple-table-header-color simple-table-header">Ví dụ</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80c5-8390-d21c691e9c9f"><td id="Gg&gt;p" class="">Nash Equilibrium (NE)</td><td id="AYxm" class="">Không ai muốn đơn phương đổi chiến lược</td><td id="hPu_" class="">Thị trường cạnh tranh hoàn hảo</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80dc-b01d-e7ffbab1b7ea"><td id="Gg&gt;p" class="">Bayesian NE</td><td id="AYxm" class="">Cân bằng với thông tin không hoàn hảo</td><td id="hPu_" class="">Trading với private signal</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80ff-aa7d-f42ad50dbea3"><td id="Gg&gt;p" class="">Correlated Equilibrium</td><td id="AYxm" class="">Có tín hiệu công cộng</td><td id="hPu_" class="">Fed announcement</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-806c-bab9-e92b4d5239b6"><td id="Gg&gt;p" class="">Evolutionary stable</td><td id="AYxm" class="">Chiến lược chống lại đột biến</td><td id="hPu_" class="">HFT strategies</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8062-9890-ca3c7b34ef8a" class=""><strong>Các biến trạng thái:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-8085-80bc-fef0c1f3affd" class="simple-table"><thead c
lass="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80b3-8090-e6e8a38454f4"><th id="QZL\" class="simple-table-header-color simple-table-header">Biến</th><th id="RDjT" class="simple-table-header-color simple-table-header">Tên</th><th id="Ttux" class="simple-table-header-color simple-table-header">Công thức</th><th id="rlpC" class="simple-table-header-color simple-table-header">Ý nghĩa</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8007-85eb-d0e6705692fd"><td id="QZL\" class="">NE_distance</td><td id="RDjT" class="">Khoảng cách đến cân bằng</td><td id="Ttux" class="">`∑</td><td id="rlpC" class="">π_i - π_i*</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80ff-a6b5-f683e3d1332d"><td id="QZL\" class="">Exploitability</td><td id="RDjT" class="">Mức độ bị khai thác</td><td id="Ttux" class=""><code>max_a u_i(a, σ_{-i}) - u_i(σ_i, σ_{-i})</code></td><td id="rlpC" class="">Edge có thể có</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8091-a5f3-fa3eb6c67914"><td id="QZL\" class="">Regret</td><td id="RDjT" class="">Hối tiếc tích lũy</td><td id="Ttux" class=""><code>∑ max(0, 
u_i(a) - u_i(acted))</code></td><td id="rlpC" class="">Học từ sai lầm</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80b7-ab33-cba9979265f5"><td id="QZL\" class="">Cooperation_level</td><td id="RDjT" class="">Mức độ hợp tác</td><td id="Ttux" class=""><code>P(coordinate action)</code></td><td id="rlpC" class="">Coordination risk (Gap 2)</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80f4-b33f-d4089db86bc1" class=""><strong>Chế độ thất bại:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-8025-a729-fc7d34aa6e9a" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80f0-ae2d-dca18c6a62f5"><th id="pHbZ" class="simple-table-header-color simple-table-header">Failure Mode</th><th id="&gt;]DL" class="simple-table-header-color simple-table-header">Điều kiện</th><th id="oJPy" class="simple-table-header-color simple-table-header">Hậu quả</th><th id="LH&gt;v" class="simple-table-header-color simple-table-header">Phục hồi</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-808b-ad80-d775ac118dff"><td id="pHbZ" class="">Coordination breakdown</td><td id="&gt;]DL" class=""><code>Cooperation_level &lt; 0.3</code></td><td id="oJPy" class="">Market fragmentation</td><td id="LH&gt;v" class="">Reduce size</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8014-8154-c152d6f3bd1f"><td id="pHbZ" class="">Exploitation</td><td id="&gt;]DL" class=""><code>Exploitability &gt; 
0</code> bền vững</td><td id="oJPy" class="">Edge bị khai thác ngược</td><td id="LH&gt;v" class="">Đổi chiến lược</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8094-b900-f7e8575697ae"><td id="pHbZ" class="">Regret spiral</td><td id="&gt;]DL" class=""><code>Regret</code> tăng không dừng</td><td id="oJPy" class="">Không học được</td><td id="LH&gt;v" class="">Reset policy</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-801f-b32e-cd1ec98d587c" class=""><strong>Kết nối:</strong></p></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-80e3-9b1f-d27b1e982f0c" class="bulleted-list"><li style="list-style-type:disc">T-3.6 → T-2.0 (memes): chiến lược lan truyền qua social learning</li></ul></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-8017-b7d5-ffdccce577d6" class="bulleted-list"><li style="list-style-type:disc">T-3.6 → T8 (smart money): institutional players là tác nhân lớn</li></ul></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80e8-b727-d0b006275128"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-8078-9ecb-e69e3bbee293" class="">T-3.5: COMPLEXITY / CHAOS</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80c1-8107-c42b6b76371c" class=""><strong>Định nghĩa:</strong> Hệ phi tuyến, nhạy cảm với điều kiện ban đầu, hiệu ứng cánh bướm.</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8015-a51d-d369cbf550eb" class=""><strong>Phương trình nền tảng:</strong></p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8020-95d0-ee62973e961a" class="">\[<br/>\boxed{\frac{d\mathbf{x}}{dt} = \mathbf{F}(\mathbf{x}, 
\boldsymbol{\mu})}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-808e-a870-c0a39574d5e3" class="">\[<br/>\boxed{\lambda = \lim_{t \to \infty} \frac{1}{t} \ln\left(\frac{|\delta \mathbf{x}(t)|}{|\delta \mathbf{x}(0)|}\right)}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-807b-a23f-e154053f7890" class=""><strong>Các biến trạng thái:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-8070-8ae8-fbf4cd0530fe" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-804d-b16d-ea0567ac417b"><th id="MMxr" class="simple-table-header-color simple-table-header">Biến</th><th id="Q~bV" class="simple-table-header-color simple-table-header">Tên</th><th id="xKBN" class="simple-table-header-color simple-table-header">Công thức</th><th id="QBOq" class="simple-table-header-color simple-table-header">Ý nghĩa</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80f7-b0cf-df8ae3b85df1"><td id="MMxr" class="">λ_lyapunov</td><td id="Q~bV" class="">Lyapunov exponent</td><td id="xKBN" class=""><code>&gt;0</code> = chaotic</td><td id="QBOq" class="">Dự báo được trong bao lâu?</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80e3-bbd7-d5c23feac407"><td id="MMxr" class="">D_corr</td><td id="Q~bV" class="">Thời gian tương quan</td><td id="xKBN" class=""><code>τ = ∫C(τ)dτ</code></td><td id="QBOq" class="">Memory của hệ thống</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8050-833f-c771aa59d18b"><td id="MMxr" class="">Fractal_dim</td><td id="Q~bV" class="">Fractal dimension</td><td id="xKBN" class=""><code>D = log N / log(1/r)</code></td><td id="QBOq" class="">Độ phức tạp của price path</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80fd-bb7c-f33f1aee7367"><td id="MMxr" class="">Predictability_horizon</td><td i
d="Q~bV" class="">Thời gian dự báo được</td><td id="xKBN" class=""><code>≈ 1/λ_max</code></td><td id="QBOq" class="">Khi nào phải dừng dự báo</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8072-8576-f81935018635" class=""><strong>Chế độ thất bại:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-804f-86d2-e8e54652a39b" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8013-94da-ffe650d02899"><th id="baC|" class="simple-table-header-color simple-table-header">Failure Mode</th><th id="EO@A" class="simple-table-header-color simple-table-header">Điều kiện</th><th id="f~Jz" class="simple-table-header-color simple-table-header">Hậu quả</th><th id="_jV&lt;" class="simple-table-header-color simple-table-header">Phục hồi</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-805f-a185-ea3aec4ed666"><td id="baC|" class="">Chaos onset</td><td id="EO@A" class=""><code>λ_lyapunov &gt; 0.1</code></td><td id="f~Jz" class="">Không dự báo được</td><td id="_jV&lt;" class="">Chuyển sang observe only</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8038-9181-fff036c785a4"><td id="baC|" class="">Predictability collapse</td><td id="EO@A" class=""><code>Predictability_horizon &lt; 
Δt</code></td><td id="f~Jz" class="">Mô hình vô dụng</td><td id="_jV&lt;" class="">Dùng hedge thay vì prediction</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8032-bd5c-f5ae87b3bbd5"><td id="baC|" class="">Fractal transition</td><td id="EO@A" class=""><code>Fractal_dim</code> thay đổi đột ngột</td><td id="f~Jz" class="">Regime shift</td><td id="_jV&lt;" class="">Reset model</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80ca-93ea-f2acc90a9337" class=""><strong>Kết nối:</strong></p></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-8067-9350-e7f31f8e9cdb" class="bulleted-list"><li style="list-style-type:disc">T-3.5 → T-0.5 (randomness): chaos khác với randomness (deterministic nhưng không dự báo được)</li></ul></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80b0-ae24-c5e152a74256"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-806e-9ad7-e8c4470e3cfd" class="">T-3.3: ETHICAL CONSTRAINTS</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80b0-b606-f7d8eee6afd2" class=""><strong>Định nghĩa:</strong> Các ràng buộc đạo đức, công lý, trách nhiệm. 
Heritage ∅ sống ở đây.</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8085-9457-d2e3c4836fd9" class=""><strong>Phương trình nền tảng:</strong></p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8041-a6a3-d419b36882d2" class="">\[<br/>\boxed{\text{Permission}<em>{\text{ethical}} = \mathbf{1}[\text{Harm} \leq \text{Harm}</em>{\max}] \times \mathbf{1}[\text{Consent} = 1] \times \mathbf{1}[\text{Fairness} &gt; 
\theta]}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80b5-acbc-f961b8e5ffef" class=""><strong>Các nguyên tắc:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-80d1-8dc8-e58385cadcaf" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80bf-b34b-d0709e5655a3"><th id="fK&gt;c" class="simple-table-header-color simple-table-header">Nguyên tắc</th><th id="&gt;=TL" class="simple-table-header-color simple-table-header">Công thức</th><th id="MfmT" class="simple-table-header-color simple-table-header">Áp dụng</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8088-934d-e1ae6661e018"><td id="fK&gt;c" class="">Non-maleficence</td><td id="&gt;=TL" class=""><code>Harm ≤ θ_harm</code></td><td id="MfmT" class="">Không gây hại có chủ đích</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-808a-b896-dbaa51701dec"><td id="fK&gt;c" class="">Justice</td><td id="&gt;=TL" class=""><code>Asymmetry ≠ 0 ⇒ Justice ≠ 0</code></td><td id="MfmT" class="">Phát hiện bất đối xứng</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80d9-ab29-c638f5a693c8"><td id="fK&gt;c" class="">Transparency</td><td id="&gt;=TL" class=""><code>Decision ⇒ Traceable</code></td><td id="MfmT" class="">Mọi quyết định phải có dấu vết</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80e4-8169-d222c2219b4c"><td id="fK&gt;c" class="">Consent</td><td id="&gt;=TL" class=""><code>User_consent = 1</code></td><td id="MfmT" class="">Không hành động khi chưa được phép</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80bc-8298-c1eb99efb8aa"><td id="fK&gt;c" class="">Accountability</td><td id="&gt;=TL" class=""><code>∃ responsible_entity</code></td><td id="MfmT" class="">Ai chịu trách nhiệm?</td></tr></div></tbody></table></div><div s
tyle="display:contents" dir="auto"><p id="353c5e6f-95bd-8006-98f5-c0ff3e1cd458" class=""><strong>Chế độ thất bại:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-80e9-ae9f-cb8adcdbac02" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80d1-bdc2-fc77b7729cf4"><th id="Dozq" class="simple-table-header-color simple-table-header">Failure Mode</th><th id="PZ`\" class="simple-table-header-color simple-table-header">Điều kiện</th><th id="ovEg" class="simple-table-header-color simple-table-header">Hậu quả</th><th id=":^ox" class="simple-table-header-color simple-table-header">Phục hồi</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80c7-b886-ceddb3bda350"><td id="Dozq" class="">Ethical violation</td><td id="PZ`\" class="">Harm &gt; 
θ_harm</td><td id="ovEg" class="">Lockout</td><td id=":^ox" class="">Human review</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80a3-b2bb-d9a973ecf5f7"><td id="Dozq" class="">Consent missing</td><td id="PZ`\" class="">User_consent = 0</td><td id="ovEg" class="">No action</td><td id=":^ox" class="">Request consent</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80f0-9346-d4a771e46b23"><td id="Dozq" class="">Opaque decision</td><td id="PZ`\" class="">Traceability = 0</td><td id="ovEg" class="">Cannot audit</td><td id=":^ox" class="">Log all decisions</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80c8-9422-f067eec7de77" class=""><strong>Kết nối:</strong></p></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-80c4-80ce-ff5ac235ea25" class="bulleted-list"><li style="list-style-type:disc">T-3.3 → A6 (Purpose): đạo đức là một phần của purpose</li></ul></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-80e6-bc10-f50ebff11a7e" class="bulleted-list"><li style="list-style-type:disc">T-3.3 → M6 (Self-Refutation): tự phát hiện vi phạm</li></ul></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-8045-8b7e-e247de156d08"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-805f-ad5e-c55977c53313" class="">T-3.0: PHENOMENOLOGICAL LAYER</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80d9-9292-f63aedc860e3" class=""><strong>Định nghĩa:</strong> Trải nghiệm chủ quan, ý thức, cảm giác. 
Heritage không thể formalize tầng này, chỉ có thể phát hiện dấu hiệu.</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80ea-9eb0-e3f21d265fbf" class=""><strong>Các biến quan sát được (proxy):</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-8088-a1de-e807b4e64625" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8063-bb5d-d43a9cb3ae31"><th id="^r:v" class="simple-table-header-color simple-table-header">Biến</th><th id="AP\Z" class="simple-table-header-color simple-table-header">Công thức</th><th id=":`ly" class="simple-table-header-color simple-table-header">Ý nghĩa</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8012-baa2-d618a5dd94cd"><td id="^r:v" class="">Subjective_arousal</td><td id="AP\Z" class="">Từ biometrics: HRV, pupil, GSR</td><td id=":`ly" class="">Mức độ hưng phấn/kích thích</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80c6-ae12-cff8932a51cb"><td id="^r:v" class="">Subjective_valence</td><td id="AP\Z" class="">Từ sentiment, facial expression</td><td id=":`ly" class="">Tích cực/tiêu cực</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-809c-8c9c-c406a374c776"><td id="^r:v" class="">Flow_state</td><td id="AP\Z" class=""><code>α_power &gt; θ_α AND γ_power &gt; 
θ_γ</code></td><td id=":`ly" class="">Trạng thái tập trung tối ưu</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80e3-bac2-ff6cb9b8c853"><td id="^r:v" class="">Cognitive_load</td><td id="AP\Z" class=""><code>1 - (performance / baseline)</code></td><td id=":`ly" class="">Mức độ quá tải nhận thức</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-801f-99b6-e23ef6352714" class=""><strong>Chế độ thất bại:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-807b-b04b-fa3bbff60029" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8069-bdcc-ca7c182a83a0"><th id="WXHn" class="simple-table-header-color simple-table-header">Failure Mode</th><th id="p|FO" class="simple-table-header-color simple-table-header">Điều kiện</th><th id="Ro_W" class="simple-table-header-color simple-table-header">Hậu quả</th><th id="Svsd" class="simple-table-header-color simple-table-header">Phục hồi</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-808e-ab7c-d3e676cea38d"><td id="WXHn" class="">Burnout</td><td id="p|FO" class=""><code>Fatigue &gt; 0.8</code></td><td id="Ro_W" class="">Decision quality giảm</td><td id="Svsd" class="">Lock system</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8089-9d02-def94edec25a"><td id="WXHn" class="">Panic</td><td id="p|FO" class=""><code>Subjective_arousal &gt; 0.9 AND valence &lt; 
0</code></td><td id="Ro_W" class="">Hành động phi lý</td><td id="Svsd" class="">Force pause</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-800f-a3c7-c9582619e7a3"><td id="WXHn" class="">Flow loss</td><td id="p|FO" class="">Rời khỏi flow</td><td id="Ro_W" class="">Sáng tạo giảm</td><td id="Svsd" class="">Nghỉ ngơi, thay đổi task</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-807a-bdd3-cb824e665e43"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-8038-8b96-dccebe68a505" class="">T-2.8: NON-DUAL / EMPTINESS</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80e1-8ece-f33643872daa" class=""><strong>Định nghĩa:</strong> Tánh không, bất định căn bản – nơi mọi distinction sụp đổ. 
Đây là tầng mà Heritage không thể đưa ra distinction long/short vì &quot;long&quot; và &quot;short&quot; không còn ý nghĩa.</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80af-9c24-c3a12cc7db4e" class=""><strong>Nguyên lý:</strong><br/>\[<br/>\boxed{\text{All distinctions are conventional, not absolute}}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8069-8921-d250f9f98396" class=""><strong>Áp dụng vào Heritage:</strong></p></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-80a9-ad65-c31a63a3d100" class="bulleted-list"><li style="list-style-type:disc">Khi thị trường ở trạng thái &quot;emptiness&quot; (ví dụ: trước FOMC, không ai biết gì), mọi tín hiệu đều vô nghĩa.</li></ul></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-8019-8dc0-cbc052abc837" class="bulleted-list"><li style="list-style-type:disc">Hành động đúng: Observe only.</li></ul></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-802a-907c-de5fbd9bc4d7" class=""><strong>Dấu hiệu nhận biết:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-8031-99ea-e73d22612602" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-807e-b53e-c00217f4f509"><th id="w}A&lt;" class="simple-table-header-color simple-table-header">Dấu hiệu</th><th id="&lt;TQE" class="simple-table-header-color simple-table-header">Công thức</th><th id="Lay&lt;" class="simple-table-header-color simple-table-header">Ngưỡng</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8009-8d78-d1d13168b0cb"><td id="w}A&lt;" class="">Information entropy max</td><td id="&lt;TQE" class=""><code>H(X) ≈ H_max</code></td><td id="Lay&lt;" class="">&gt; 
0.9 × max</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-801f-ace8-dcc5ca8925a6"><td id="w}A&lt;" class="">Regime entropy cao</td><td id="&lt;TQE" class=""><code>-∑ p_i log p_i &gt; 1.5</code></td><td id="Lay&lt;" class="">(7 regimes → max ~1.95)</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-801b-a9aa-c8a5abd2c000"><td id="w}A&lt;" class="">Cohesion ~ 0</td><td id="&lt;TQE" class=""><code>H ≈ 0</code></td><td id="Lay&lt;" class="">&lt; 0.2</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-807a-a6af-f9907e2c230b"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-8043-b5bc-f963105fa755" class="">T-2.5: META-REFLECTIVE CLOSURE</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80a6-b88e-ceb9294bbd9f" class=""><strong>Định nghĩa:</strong> Biết rằng mình không biết. 
Tầng tự nhận thức về giới hạn của chính mình.</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80ee-8c9a-cb51ddfcfff1" class=""><strong>Phương trình:</strong><br/>\[<br/>\boxed{\text{MetaIgnorance} = 1 - \frac{\text{KnownUnknowns}}{\text{TotalUnknowns}}}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80f1-a3fe-fd8289d09079" class=""><strong>Các câu hỏi meta:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-8054-abb1-cdcf1ee2e3b5" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-801d-8ff7-ca12f426bde6"><th id="aWTz" class="simple-table-header-color simple-table-header">#</th><th id="Zbws" class="simple-table-header-color simple-table-header">Câu hỏi</th><th id="r]gZ" class="simple-table-header-color simple-table-header">Công thức</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8056-bfee-ec129fa23870"><td id="aWTz" class="">1</td><td id="Zbws" class="">Tôi có đang tự lừa mình không?</td><td id="r]gZ" class="">`SelfDeception = 1 if</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80e9-9de9-c9e2ac01a4cd"><td id="aWTz" class="">2</td><td id="Zbws" class="">Mô hình của tôi có đang overfit không?</td><td id="r]gZ" class=""><code>Overfit = 1 if TrainAcc - TestAcc &gt; 0.1</code></td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-809a-a13a-d986481cd246"><td id="aWTz" class="">3</td><td id="Zbws" class="">Tôi có đang bỏ qua bằng chứng nào không?</td><td id="r]gZ" class=""><code>ConfirmationBias = 1 if EvidenceIgnored &gt; θ</code></td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80c0-a595-fc6355cf07d1"><td id="aWTz" class="">4</td><td id="Zbws" class="">Giới hạn của tôi là gì?</td><td id="r]gZ" class=""><code>SelfLimits = {domains where accuracy &lt; 
threshold}</code></td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-800d-88a6-dde346d09518" class=""><strong>Chế độ thất bại:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-803b-bf2c-e25b82dc65c0" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80ec-b9cf-f8d7806c48bc"><th id="QX&gt;~" class="simple-table-header-color simple-table-header">Failure Mode</th><th id="T=PX" class="simple-table-header-color simple-table-header">Điều kiện</th><th id="kFO~" class="simple-table-header-color simple-table-header">Hậu quả</th><th id="@bfA" class="simple-table-header-color simple-table-header">Phục hồi</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8091-af8c-d8864d6eb7d8"><td id="QX&gt;~" class="">Overconfidence</td><td id="T=PX" class=""><code>SelfDeception = 1</code></td><td id="kFO~" class="">Trade khi không nên</td><td id="@bfA" class="">Reduce size, audit</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8053-a0ca-e36676bbb2e2"><td id="QX&gt;~" class="">Meta-blindness</td><td id="T=PX" class=""><code>MetaIgnorance = 0</code></td><td id="kFO~" class="">Không biết mình không biết</td><td id="@bfA" class="">External review</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-8068-9c80-ef60d766391a"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-80da-a3a2-dd2f8199b70d" class="">T-2.3: COSMIC / PLANETARY CONSTRAINTS</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8002-90c0-eef291673dea" class=""><strong>Định nghĩa:</strong> Các ràng buộc từ mặt trời, từ trường Trái Đất, bức xạ vũ trụ, 
thiên văn.</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-803a-be00-eccfd7def3f6" class=""><strong>Các biến:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-80bd-bd7a-f55f840ec9f0" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80d3-bff4-e4ce61c44fea"><th id="_wK_" class="simple-table-header-color simple-table-header">Biến</th><th id="Mo?o" class="simple-table-header-color simple-table-header">Nguồn</th><th id="kFwh" class="simple-table-header-color simple-table-header">Công thức</th><th id="uzkc" class="simple-table-header-color simple-table-header">Ảnh hưởng đến thị trường</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8076-bc9d-e83516d69b76"><td id="_wK_" class="">Solar_flux</td><td id="Mo?o" class="">NOAA</td><td id="kFwh" class=""><code>W/m²</code></td><td id="uzkc" class="">Tâm lý giao dịch (mùa đông → ít risk)</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-806c-a5a9-ce31932a2e5a"><td id="_wK_" class="">Geomagnetic_storm</td><td id="Mo?o" class="">NOAA Kp index</td><td id="kFwh" class=""><code>Kp ∈ [0,9]</code></td><td id="uzkc" class="">Kp &gt; 
7 → lỗi HFT, tăng volatility</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8095-9745-c25e47ea780b"><td id="_wK_" class="">Cosmic_ray_flux</td><td id="Mo?o" class="">Neutron monitors</td><td id="kFwh" class=""><code>counts/min</code></td><td id="uzkc" class="">Tương quan với sáng tạo?</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-806c-9fec-e7efd38b63ba"><td id="_wK_" class="">Lunar_phase</td><td id="Mo?o" class="">Calendar</td><td id="kFwh" class=""><code>0 = new, 0.5 = full, 1 = new</code></td><td id="uzkc" class="">Full moon → tăng volatility nhẹ</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80a9-9539-ccfcfcf2b98a" class=""><strong>Chế độ thất bại:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-8094-9cf7-e42ba41d3e7b" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80fd-af02-e71f358f4e31"><th id="ph|t" class="simple-table-header-color simple-table-header">Failure Mode</th><th id="XnY\" class="simple-table-header-color simple-table-header">Điều kiện</th><th id="QwDw" class="simple-table-header-color simple-table-header">Hậu quả</th><th id="}[ok" class="simple-table-header-color simple-table-header">Phục hồi</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-800d-aec9-e8c9a9e9653f"><td id="ph|t" class="">Solar flare</td><td id="XnY\" class=""><code>Solar_flux đột biến</code></td><td id="QwDw" class="">Communication disruption</td><td id="}[ok" class="">Use backup channels</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8055-b614-da2f63a89265"><td id="ph|t" class="">Geomagnetic storm</td><td id="XnY\" class=""><code>Kp &gt; 
7</code></td><td id="QwDw" class="">HFT lỗi, spread tăng</td><td id="}[ok" class="">Reduce HFT exposure</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80f7-99ac-e077c1721b25"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-80d0-b0f9-f5add7a1bb0a" class="">T-2.0: SOCIAL / CULTURAL MEMES</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8002-b239-f544c7ab2864" class=""><strong>Định nghĩa:</strong> Ý tưởng lan truyền, phong trào đầu tư, narrative kinh tế, 
meme stock.</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80b1-aee2-dfb5d694b5cf" class=""><strong>Phương trình nền tảng:</strong><br/>\[<br/>\boxed{\frac{dM}{dt} = \beta M(1-M) - \gamma M}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8035-bcc3-c733bd0e4d89" class=""><strong>Các biến:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-8073-ace0-de9ce3667e51" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8077-80a5-f3a5f9e38e12"><th id="_ltT" class="simple-table-header-color simple-table-header">Biến</th><th id="?u@S" class="simple-table-header-color simple-table-header">Tên</th><th id="M|lg" class="simple-table-header-color simple-table-header">Công thức</th><th id="LB:p" class="simple-table-header-color simple-table-header">Ý nghĩa</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80c5-bc79-f8f1959874d9"><td id="_ltT" class="">M</td><td id="?u@S" class="">Meme prevalence</td><td id="M|lg" class=""><code>0 → 1</code></td><td id="LB:p" class="">Mức độ lan truyền</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-806b-8edc-f9c2cae4ad11"><td id="_ltT" class="">β</td><td id="?u@S" class="">Transmission rate</td><td id="M|lg" class="">Tốc độ lây lan</td><td id="LB:p" class="">Sức hút của narrative</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8024-864a-ffc9c5c4996e"><td id="_ltT" class="">γ</td><td id="?u@S" class="">Forgetting rate</td><td id="M|lg" class="">Tốc độ chán</td><td id="LB:p" class="">Khi nào meme chết</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8088-8dc2-eab747714ac2"><td id="_ltT" class="">R0</td><td id="?u@S" class="">Basic reproduction</td><td id="M|lg" class=""><code>β/γ</code></td><td id="LB:p" class="">Meme có lan rộng k
hông?</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8086-90d7-f8b369aaa8ca" class=""><strong>Chế độ thất bại:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-8054-9597-e60bb9e2b68c" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8016-943b-d552ba2ab5b6"><th id="ln@I" class="simple-table-header-color simple-table-header">Failure Mode</th><th id="opU{" class="simple-table-header-color simple-table-header">Điều kiện</th><th id="pvtf" class="simple-table-header-color simple-table-header">Hậu quả</th><th id="tA`r" class="simple-table-header-color simple-table-header">Phục hồi</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80d3-b36b-c430d3807c38"><td id="ln@I" class="">Meme bubble</td><td id="opU{" class=""><code>M &gt; 0.8 AND R0 &gt; 2</code></td><td id="pvtf" class="">Overcrowding</td><td id="tA`r" class="">Avoid crowded trades</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8082-8324-db2ab28388e3"><td id="ln@I" class="">Meme death</td><td id="opU{" class=""><code>dM/dt &lt; 
0, M → 0</code></td><td id="pvtf" class="">Edge biến mất</td><td id="tA`r" class="">Exit position</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-808c-9bb6-f37ccf26b4c6"><td id="ln@I" class="">False meme</td><td id="opU{" class=""><code>M cao nhưng không dựa trên thực tế</code></td><td id="pvtf" class="">Speculative bubble</td><td id="tA`r" class="">Hedge</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8061-9511-cc8924a45e5f" class=""><strong>Kết nối:</strong></p></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-80a4-a428-d797e08c5098" class="bulleted-list"><li style="list-style-type:disc">T-2.0 → I-13 (meme propagation)</li></ul></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-80f4-80b6-f59bbb03726e" class="bulleted-list"><li style="list-style-type:disc">T-2.0 → L6 (văn hóa di sản): memes cổ đại</li></ul></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-800b-a191-d7f3d3d076b6"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-8091-a3de-eb19ab0c4596" class="">T-1.8: SPIRITUAL / ANOMALOUS SIGNALS</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80db-bc31-de491dec31ed" class=""><strong>Định nghĩa:</strong> Linh cảm, đồng bộ, trùng hợp kỳ lạ – những tín hiệu không có giải thích khoa học rõ ràng nhưng trader vẫn dùng.</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8096-95e6-c32dcbe4ee88" class=""><strong>Heritage không tin vào siêu nhiên, 
nhưng có thể xử lý như &quot;unknown signals&quot;:</strong></p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80a4-9a96-e42b3f874465" class="">\[<br/>\boxed{\text{AnomalyScore} = 1 - \frac{P(\text{event} \mid \text{model})}{P(\text{event})}}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80fa-927d-dd98025cabd1" class=""><strong>Các loại tín hiệu:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-80b8-a98f-dc155a6f2107" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-806b-868f-c55582841ee1"><th id="nalc" class="simple-table-header-color simple-table-header">Loại</th><th id="^OIk" class="simple-table-header-color simple-table-header">Ví dụ</th><th id="]e&lt;s" class="simple-table-header-color simple-table-header">Xử lý</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-801c-b548-f837e43643bd"><td id="nalc" class="">Coincidence</td><td id="^OIk" class="">&quot;Hôm qua tôi mơ thấy vàng giảm&quot;</td><td id="]e&lt;s" class="">Ignore (no statistical evidence)</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8067-973d-f6dc4bd0002b"><td id="nalc" class="">Synchronicity</td><td id="^OIk" class="">Nhiều tin tức xảy ra cùng lúc</td><td id="]e&lt;s" class="">Cross-check với L7 (quyền lực)</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8063-90a0-d00cff36c7a9"><td id="nalc" class="">Intuition</td><td id="^OIk" class="">&quot;Cảm giác&quot; 
của trader lão làng</td><td id="]e&lt;s" class="">Xem như prior có trọng số thấp (w=0.1)</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80be-ba3a-ea970b0a1c53" class=""><strong>Chế độ thất bại:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-8067-b21e-db81cd3555a2" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80fa-b432-f6f035219e61"><th id="dLK&lt;" class="simple-table-header-color simple-table-header">Failure Mode</th><th id="M?op" class="simple-table-header-color simple-table-header">Điều kiện</th><th id="C;G{" class="simple-table-header-color simple-table-header">Hậu quả</th><th id=":MWo" class="simple-table-header-color simple-table-header">Phục hồi</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8027-ac5b-ffecd6785f5f"><td id="dLK&lt;" class="">Superstition</td><td id="M?op" class="">Dùng tín hiệu không có evidence</td><td id="C;G{" class="">Decision quality giảm</td><td id=":MWo" class="">Force evidence requirement</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8014-96c4-d26bea357e43"><td id="dLK&lt;" class="">Overweight intuition</td><td id="M?op" class=""><code>w_intuition &gt; 
0.3</code></td><td id="C;G{" class="">Overconfidence</td><td id=":MWo" class="">Reduce weight</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80c1-9b3f-eba26c27a824"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-80ad-98c9-fd2de59b88a9" class="">T-1.5: DNA / EVOLUTIONARY PRIORS</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80f8-966d-c949d4bc0060" class=""><strong>Định nghĩa:</strong> Các bias bẩm sinh được mã hóa trong DNA qua hàng triệu năm tiến hóa.</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8073-9504-f9470f5df2b0" class=""><strong>Các bias chính:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-800b-b57b-e817875ef822" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8065-8ee9-d48b784a1b03"><th id="Vca]" class="simple-table-header-color simple-table-header">Bias</th><th id="?FTH" class="simple-table-header-color simple-table-header">Công thức</th><th id="tCXS" class="simple-table-header-color simple-table-header">Nguồn gốc</th><th id="X;U[" class="simple-table-header-color simple-table-header">Ảnh hưởng trading</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80ec-a7d8-c92ab31e0fe2"><td id="Vca]" class="">Loss aversion</td><td id="?FTH" class=""><code>-U(-L) &gt; 
U(L)</code> (≈2.25x)</td><td id="tCXS" class="">Tránh nguy hiểm</td><td id="X;U[" class="">Không chịu cắt lỗ</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80c0-b0ff-c8971b342fb1"><td id="Vca]" class="">Herding</td><td id="?FTH" class=""><code>P(follow) ∝ crowd_size</code></td><td id="tCXS" class="">An toàn theo đám đông</td><td id="X;U[" class="">FOMO, panic selling</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-808b-85f3-feedb75a60dc"><td id="Vca]" class="">Recency</td><td id="?FTH" class=""><code>w(t) ∝ exp(-λt), λ ≈ 0.1</code></td><td id="tCXS" class="">Sự kiện gần đây quan trọng hơn</td><td id="X;U[" class="">Đuổi theo trend</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8022-8f2f-cede6a432b70"><td id="Vca]" class="">Ambiguity aversion</td><td id="?FTH" class=""><code>P(ambiguous) &lt; P(risky)</code></td><td id="tCXS" class="">Tránh không biết</td><td id="X;U[" class="">Không trade khi uncertainty cao</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80a9-b514-f7f875510798"><td id="Vca]" class="">Status quo bias</td><td id="?FTH" class=""><code>P(stay) &gt; 
P(change)</code></td><td id="tCXS" class="">Ổn định an toàn</td><td id="X;U[" class="">Giữ lỗ quá lâu</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-803f-a7ae-f019d29f55d9" class=""><strong>Xử lý trong Heritage:</strong><br/>\[<br/>\boxed{\text{Signal}<em>{\text{corrected}} = \text{Signal}</em>{\text{raw}} - \sum w_{\text{bias}} \times \text{Bias}_{\text{current}}}<br/>\]</p></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80fe-bde8-c07cd2429651"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-804e-bc69-e2bb9f8581de" class="">T-1.2: NEUROSCIENCE KERNEL</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-800e-a021-e226be98ec3d" class=""><strong>Định nghĩa:</strong> Điện sinh học, dopamine, cognitive load, 
default mode network (DMN).</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80d8-bd3a-f1605e89fdc5" class=""><strong>Các biến:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-8003-a3d8-f5fa7aecea8f" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80c8-8371-eb66fdb9c181"><th id="rBia" class="simple-table-header-color simple-table-header">Biến</th><th id="OTLy" class="simple-table-header-color simple-table-header">Tên</th><th id="Q&lt;@O" class="simple-table-header-color simple-table-header">Công thức</th><th id="INZV" class="simple-table-header-color simple-table-header">Ảnh hưởng</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8042-b49e-df39d5aa7b23"><td id="rBia" class="">Dopamine</td><td id="OTLy" class="">Mức độ kỳ vọng phần thưởng</td><td id="Q&lt;@O" class=""><code>DA = P(reward) × magnitude</code></td><td id="INZV" class="">Overconfidence khi thắng</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80b0-9cd4-df4f1ed73f2c"><td id="rBia" class="">Cortisol</td><td id="OTLy" class="">Stress hormone</td><td id="Q&lt;@O" class=""><code>Cortisol ∝ 1/HRV</code></td><td id="INZV" class="">Risk aversion khi stress</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80b9-8e80-c361e52b5e41"><td id="rBia" class="">Cognitive load</td><td id="OTLy" class="">Tải nhận thức</td><td id="Q&lt;@O" class=""><code>Load = tasks / capacity</code></td><td id="INZV" class="">Decision quality ∝ 1/√Load</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-806b-8ad6-d73c817dc71f"><td id="rBia" class="">DMN</td><td id="OTLy" class="">Default mode network</td><td id="Q&lt;@O" class="">Hoạt động khi nghỉ ngơi</td><td id="INZV" class="">Tự kể chuyện, 
narrative bias</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8074-a82b-f45ef202d4e9" class=""><strong>Flow state detection (EEG proxy):</strong><br/>\[<br/>\boxed{\text{Flow} = \mathbf{1}[\alpha_{\text{power}} &gt; \theta_\alpha \land \gamma_{\text{power}} &gt; \theta_\gamma \land \beta_{\text{high}} &lt; \theta_\beta]}<br/>\]</p></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80cf-a643-e4a06d355c57"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-80d5-bd87-cbd84cc7375c" class="">T-0.9: QUANTUM LOGIC</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80c9-a5cb-d6a38fe9c402" class=""><strong>Định nghĩa:</strong> Chồng chập, sụp đổ, vướng víu – áp dụng cho thị trường ở cấp độ vi mô (order book, HFT).</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8088-995c-dc9bad75abb5" class=""><strong>Phương trình nền tảng:</strong><br/>\[<br/>\boxed{|\psi\rangle = \alpha|0\rangle + \beta|1\rangle}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8031-9c1d-f8da3288071a" class="">\[<br/>\boxed{P(\text{measure} = 0) = |\alpha|^2}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8017-9743-ed96f1ae5eb1" class=""><strong>Áp dụng vào market microstructure:</strong></p></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-801a-b2f0-e63ffcffbac0" class="bulleted-list"><li style="list-style-type:disc">Một lệnh có thể vừa là &quot;mua&quot; vừa là &quot;bán&quot; 
cho đến khi khớp (chồng chập)</li></ul></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-806c-a281-cb73c07f5d6e" class="bulleted-list"><li style="list-style-type:disc">Hành động quan sát (market order) làm sụp đổ trạng thái lệnh</li></ul></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-805a-8aa9-d57b2814be55" class="bulleted-list"><li style="list-style-type:disc">Tương quan giữa các lệnh không thể giải thích bằng classical correlation (vướng víu)</li></ul></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8094-8b74-cd626eed6af0" class=""><strong>Chế độ đặc biệt:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-80cb-b6b7-cea667b46fdb" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8019-848b-fdaaf914551b"><th id="bong" class="simple-table-header-color simple-table-header">Khái niệm quantum</th><th id="@=hP" class="simple-table-header-color simple-table-header">Market tương đương</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-802b-ab9b-d0463f3d32df"><td id="bong" class="">Superposition</td><td id="@=hP" class="">Limit order chưa khớp</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-802e-9b1b-c2c078b6ee49"><td id="bong" class="">Collapse</td><td id="@=hP" class="">Market order khớp</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80f3-a33b-db2c8d6b1e54"><td id="bong" class="">Entanglement</td><td id="@=hP" class="">Correlated orders từ cùng một trader</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-805e-b6fd-f5c0223c6a91"><td id="bong" class="">Interference</td><td id="@=hP" class="">Order flow tương tác</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-805c-8073-eea6ce5434f4"/></div><div style="display:contents" dir="auto"><h3 i
d="353c5e6f-95bd-80b5-b433-d60b2a16488a" class="">T-0.5: TRUE RANDOMNESS</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80de-aca3-e181cd9d7e44" class=""><strong>Định nghĩa:</strong> Ngẫu nhiên nội tại không thể dự báo, đến từ cơ học lượng tử.</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8007-8d82-fb686c7a07a3" class=""><strong>Heritage không thể dự báo tầng này, chỉ có thể:</strong></p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80bd-9dc9-f520e0747fd8" class="">\[<br/>\boxed{\text{Recognize} = \mathbf{1}[\text{Signal} \approx \text{Noise}]}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8023-b665-ca1ca8df4021" class=""><strong>Hành động đúng:</strong></p></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-8050-ad80-c4d2474af2e9" class="bulleted-list"><li style="list-style-type:disc">Không dự báo</li></ul></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-80ef-afe6-dfcd37563b1a" class="bulleted-list"><li style="list-style-type:disc">Hedge cho trường hợp xấu nhất</li></ul></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-8061-b13e-fa4914ee34e5" class="bulleted-list"><li style="list-style-type:disc">Chấp nhận uncertainty</li></ul></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80ef-a6de-d60a3d57e034"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-809a-8871-df27654c1263" class="">T-0.2: META-LOGICAL INVARIANTS</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-808d-8c9e-e0f748e7a06d" class=""><strong>Định nghĩa:</strong> Các bất biến logic nền tảng – không mâu thuẫn, phân biệt, 
bền vững.</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80c7-aa9a-cfa8de16bd1f" class=""><strong>Các bất biến:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-80cf-8ab2-eed2c126c567" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-801a-b758-c62dfd21caac"><th id="laB`" class="simple-table-header-color simple-table-header">#</th><th id="B~D&gt;" class="simple-table-header-color simple-table-header">Bất biến</th><th id="S&gt;Gd" class="simple-table-header-color simple-table-header">Công thức</th><th id="?IyR" class="simple-table-header-color simple-table-header">Hậu quả nếu vi phạm</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8036-96e1-fd1e0851b2e7"><td id="laB`" class="">1</td><td id="B~D&gt;" class="">Non-contradiction</td><td id="S&gt;Gd" class=""><code>¬(A ∧ ¬A)</code></td><td id="?IyR" class="">Hệ thống invalid</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-804a-9faf-f3e60d52cada"><td id="laB`" class="">2</td><td id="B~D&gt;" class="">Identity</td><td id="S&gt;Gd" class=""><code>x = x</code></td><td id="?IyR" class="">Không thể phân biệt</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8006-bba4-dfcf8150bcc4"><td id="laB`" class="">3</td><td id="B~D&gt;" class="">Excluded middle</td><td id="S&gt;Gd" class=""><code>A ∨ ¬A</code></td><td id="?IyR" class="">Không thể quyết định</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80b8-8a1c-ca8a1d9267ac"><td id="laB`" class="">4</td><td id="B~D&gt;" class="">Transitivity</td><td id="S&gt;Gd" class=""><code>a ≤ b ∧ b ≤ c ⇒ a ≤ c</code></td><td id="?IyR" class="">Arbitrage vô hạn</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80f7-840c-d8ce7d77ed0c"/></div><div style="display:contents" dir="auto"><h2 i
d="353c5e6f-95bd-8069-94e2-c62461e6de42" class="">PHẦN 2.2: TẦNG THỊ TRƯỜNG (T0 → T15)</h2></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-80d1-b833-cb0cbb16ac90" class="">T0: MACRO PLUMBING CORE</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8017-bfd3-e4640ac148d6" class=""><strong>Định nghĩa:</strong> Các biến vĩ mô cơ bản ảnh hưởng đến mọi tài sản.</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-808b-a0df-c2243c0a7604" class=""><strong>Các biến:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-8004-a9d3-d2c5e153a5c6" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8050-9530-de19136403c2"><th id="IiL=" class="simple-table-header-color simple-table-header">Biến</th><th id=";RjQ" class="simple-table-header-color simple-table-header">Tên</th><th id="BC;{" class="simple-table-header-color simple-table-header">Nguồn</th><th id="AMaT" class="simple-table-header-color simple-table-header">Công thức</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8084-afdd-cf7303d1f126"><td id="IiL=" class="">DXY</td><td id=";RjQ" class="">Dollar Index</td><td id="BC;{" class="">ICE</td><td id="AMaT" class="">Trung bình gia quyền 6 currency</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8032-aa47-f7c356dc2f73"><td id="IiL=" class="">US10Y</td><td id=";RjQ" class="">US 10-year yield</td><td id="BC;{" class="">Treasury</td><td id="AMaT" class="">Lãi suất dài hạn</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80bb-a486-f7f648cfd2fe"><td id="IiL=" class="">US2Y</td><td id=";RjQ" class="">US 2-year yield</td><td id="BC;{" class="">Treasury</td><td id="AMaT" class="">Kỳ vọng Fed</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80ad-8d17-e030562110b9"><td id="IiL=" class="">SOFR</td><td i
d=";RjQ" class="">Secured Overnight Financing Rate</td><td id="BC;{" class="">NY Fed</td><td id="AMaT" class="">Chi phí funding thực</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8009-950c-e2ea44dee5ce"><td id="IiL=" class="">Liquidity_USD</td><td id=";RjQ" class="">Thanh khoản USD</td><td id="BC;{" class="">Reverse repo, 
bank reserves</td><td id="AMaT" class=""><code>Reserves + RRP</code></td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8092-93a0-c60aa740fe59"><td id="IiL=" class="">VIX</td><td id=";RjQ" class="">Volatility index</td><td id="BC;{" class="">CBOE</td><td id="AMaT" class="">Biến động kỳ vọng</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80f2-bbf2-cf8e403ee6e7" class=""><strong>Phương trình tương tác:</strong><br/>\[<br/>\boxed{\Delta \text{Asset} = \beta_1 \Delta \text{DXY} + \beta_2 \Delta \text{US10Y} + \beta_3 \Delta \text{VIX} + \varepsilon}<br/>\]</p></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-8042-a907-f0df7e52299a"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-80ab-88af-ecca8be8e0d1" class="">T1–T10: HERITAGE 10 LỚP TÍN HIỆU (Xem PHẦN 2.3)</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-805a-8350-c16daa8cc998" class="">Đã được chi tiết trong bảng riêng ở trên.</p></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80fd-9194-d6aa873d80b5"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-80d0-8bcf-ef417cc0fdbe" class="">T11: REMAINING INFO</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80bf-8ad7-c05ed5898c7e" class=""><strong>Định nghĩa:</strong> Ngân sách thông tin còn lại sau sự kiện.</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8054-aecf-ee1b0c2ebd1a" class="">\[<br/>\boxed{\text{RI} = \text{InitialShock} - \text{AbsorbedPrice} - \text{NarrativeSaturation}}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8071-a3f3-db9018908a4f" class=""><strong>Các giai đoạn:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-80f0-a17e-c7be4a3ccf8c" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr i
d="353c5e6f-95bd-80a5-bacf-fa79bf9f7371"><th id="FT?:" class="simple-table-header-color simple-table-header">Giai đoạn</th><th id="vNKq" class="simple-table-header-color simple-table-header">RI</th><th id="WpSA" class="simple-table-header-color simple-table-header">Hành động</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8057-8cb4-fa2166b0a347"><td id="FT?:" class="">Chưa hấp thụ</td><td id="vNKq" class="">&gt; 0.7</td><td id="WpSA" class="">Trend following</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-808a-b75d-d64e1096ac50"><td id="FT?:" class="">Đang hấp thụ</td><td id="vNKq" class="">0.3 – 0.7</td><td id="WpSA" class="">Di chuyển stop</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8000-9554-cd6f6873f0bd"><td id="FT?:" class="">Đã hấp thụ</td><td id="vNKq" class="">&lt; 
0.3</td><td id="WpSA" class="">Thoát</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-804d-9a37-de9951e29902"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-80c5-ae98-fada81258b10" class="">T12: INTENTIONAL NOISE</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8062-a16e-fdfee267b471" class=""><strong>Định nghĩa:</strong> Spoofing, layering, quote stuffing, thao túng thị trường.</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80cb-900a-e24bf4cd519b" class="">\[<br/>\boxed{\text{NoiseScore} = \frac{\text{CancelRate} - \text{NormalCancelRate}}{\text{NormalCancelRate}}}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80bc-a2b3-c384528a7c36" class=""><strong>Phát hiện:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-80a4-b429-e78c3e7bca1c" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8075-86bc-cbf5ec7ae3c9"><th id="Nud[" class="simple-table-header-color simple-table-header">Pattern</th><th id="C@oJ" class="simple-table-header-color simple-table-header">Dấu hiệu</th><th id="ir?a" class="simple-table-header-color simple-table-header">Hành động</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80fc-832c-e4953ed82822"><td id="Nud[" class="">Spoofing</td><td id="C@oJ" class="">Lệnh lớn một bên, 
hủy ngay sau khi khớp bên kia</td><td id="ir?a" class="">Block</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-808e-97f9-df39b3c67f12"><td id="Nud[" class="">Layering</td><td id="C@oJ" class="">Nhiều lớp lệnh ảo</td><td id="ir?a" class="">Reduce trust</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8074-b4f7-c17ccd501dbd"><td id="Nud[" class="">Quote stuffing</td><td id="C@oJ" class="">Hàng nghìn lệnh trong 1 giây</td><td id="ir?a" class="">Thoát khỏi venue đó</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-8018-8225-c63a77c945ae"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-804f-9646-d76105acbfdd" class="">T13: MARKET EXPECTATION POINT (MEP)</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8034-a15d-f8e9bd6cdff4" class=""><strong>Định nghĩa:</strong> Điểm giá được coi là hợp lý bởi đa số thị trường.</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8011-8a6b-ca5f27092867" class="">\[<br/>\boxed{\text{MEP} = \text{PivotPoint} + \alpha \cdot \text{ATR} + \beta \cdot \text{FibonacciLevel}}<br/>\]</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8088-b066-cf083584489f" class=""><strong>Cách tính:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-80a7-b2b3-f5f253763992" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80ca-bd1d-c780e042d821"><th id="ls&gt;;" class="simple-table-header-color simple-table-header">Thành phần</th><th id="~{XD" class="simple-table-header-color simple-table-header">Công thức</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8015-ac7d-e8832eeecaa9"><td id="ls&gt;;" class="">Pivot</td><td id="~{XD" class=""><code>(H + L + C)/3</code></td></tr></div><div style="display:contents" dir="ltr"><tr i
d="353c5e6f-95bd-8056-803b-eed664d01b22"><td id="ls&gt;;" class="">ATR</td><td id="~{XD" class="">Average True Range</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80a0-835f-fd6762bbdfef"><td id="ls&gt;;" class="">Fibonacci</td><td id="~{XD" class="">Retracement từ swing gần nhất</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-800e-91a4-f08f1ff44c94" class=""><strong>Trading quanh MEP:</strong></p></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-80fe-b70d-c9fe567ec190" class="bulleted-list"><li style="list-style-type:disc">Giá &gt; MEP + 2*ATR → overextended (sell)</li></ul></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-8080-8fa9-c3a1749ec083" class="bulleted-list"><li style="list-style-type:disc">Giá &lt; 
MEP - 2*ATR → oversold (buy)</li></ul></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80a0-ad43-d8735aebca00"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-80b7-86de-fc0fb883ce70" class="">T14: MICROSTRUCTURE ENGINE</h3></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8045-a462-d6399ea95801" class=""><strong>Định nghĩa:</strong> Volume profile, delta, order book imbalance, 
tick-level patterns.</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-809a-9e07-cd46676c1444" class=""><strong>Các chỉ số:</strong></p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-8014-9e81-e15b70f94981" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80c2-8630-e552edccafa7"><th id="{f[a" class="simple-table-header-color simple-table-header">Chỉ số</th><th id="[gs?" class="simple-table-header-color simple-table-header">Công thức</th><th id="?Lz&gt;" class="simple-table-header-color simple-table-header">Ý nghĩa</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-808f-bbe6-c7dfa9ec0a25"><td id="{f[a" class="">Volume Profile</td><td id="[gs?" class=""><code>V(p) = ∑ volume at price p</code></td><td id="?Lz&gt;" class="">Vùng giá có thanh khoản cao</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80c2-bad5-df4fd75150f9"><td id="{f[a" class="">Delta</td><td id="[gs?" class=""><code>Δ = Volume_buy - Volume_sell</code></td><td id="?Lz&gt;" class="">Áp lực mua/bán</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-807e-b1d8-d5cc4566fc8a"><td id="{f[a" class="">Order book imbalance</td><td id="[gs?" class=""><code>IMB = (Bid_vol - Ask_vol)/(Bid_vol + Ask_vol)</code></td><td id="?Lz&gt;" class="">Sắp tới breakout?</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8039-a0cb-d277422f473c"><td id="{f[a" class="">Tick flow</td><td id="[gs?" class=""><code>Flow(t) = sign(tick) × size</code></td><td id="?Lz&gt;" class="">Hành vi của từng trader</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-8017-9efd-f7efbe27b86c"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-8046-b542-cd05433e7666" class="">T15: REGIME SWITCH ENGINE</h3></div><div style="display:contents" dir="auto"><p i
d="353c5e6f-95bd-8079-8425-f4b17d0bd0e3" class=""><strong>Định nghĩa:</strong> Tự động nhận diện 7 chế độ thị trường.</p></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-80df-9db7-f16d6004ba3e" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-807f-8287-ec98a2c86b25"><th id="zMkY" class="simple-table-header-color simple-table-header">Chế độ</th><th id="{pgu" class="simple-table-header-color simple-table-header">Dấu hiệu</th><th id="R]^T" class="simple-table-header-color simple-table-header">Hành động</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-802f-b895-e71e0ee4caff"><td id="zMkY" class="">Trend</td><td id="{pgu" class=""><code>Ω &gt; 0.6, H &gt; 0.7, slope &gt; 0</code></td><td id="R]^T" class="">Trend-following</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-808c-9eb2-dc77c73a1b1a"><td id="zMkY" class="">Sideway</td><td id="{pgu" class=""><code>Ω &lt; 0.3, H &lt; 0.4, F &gt; 0.5</code></td><td id="R]^T" class="">Mean-reversion</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8067-b380-c16b1e0eb7d6"><td id="zMkY" class="">Panic</td><td id="{pgu" class=""><code>S &gt; 0.7, H &lt; 0.3</code></td><td id="R]^T" class="">Reduce size, hedge</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8069-9775-e98c4dccac10"><td id="zMkY" class="">Transition</td><td id="{pgu" class="">Entropy regimes &gt; 1.5</td><td id="R]^T" class="">Observe only</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8041-bf1a-d58d2f11682c"><td id="zMkY" class="">Manipulation</td><td id="{pgu" class=""><code>NoiseScore &gt; 0.5</code></td><td id="R]^T" class="">Block</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80dd-93f5-f86ad4f0a1af"><td id="zMkY" class="">News shock</td><td id="{pgu" class=""><code>S_news &gt; 0.8, RI &gt; 
0.5</code></td><td id="R]^T" class="">Wait for absorption</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-800b-927d-d0caef3359c0"><td id="zMkY" class="">Policy repricing</td><td id="{pgu" class=""><code>ΔUS2Y &gt; 
0.5% trong 1 tuần</code></td><td id="R]^T" class="">Revalue all assets</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-8032-a775-e9c61e1bb9a4"/></div><div style="display:contents" dir="auto"><h2 id="353c5e6f-95bd-8019-b452-de3bdc96f028" class="">PHẦN 2.3: 10 LỚP TÍN HIỆU HERITAGE (L1–L10) – MỞ RỘNG</h2></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-80ee-b961-ec83c5769808" class="">L1: ĐỊA CHẤT / KHÍ HẬU</h3></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-8021-bcf4-dcfe4562e296" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-801b-b376-e47c42dd29ba"><th id="~np|" class="simple-table-header-color simple-table-header">Thành phần</th><th id="V_tX" class="simple-table-header-color simple-table-header">Nguồn</th><th id="fbk:" class="simple-table-header-color simple-table-header">Phương pháp</th><th id="}_{c" class="simple-table-header-color simple-table-header">Tần suất</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8078-b192-f53f4934235a"><td id="~np|" class="">Đứt gãy, khoáng sản</td><td id="V_tX" class="">USGS, BGS</td><td id="fbk:" class="">GIS, viễn thám</td><td id="}_{c" class="">1 lần</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80f9-875a-c709fad8e663"><td id="~np|" class="">Nước ngầm, bờ biển cổ</td><td id="V_tX" class="">Địa chất thủy văn</td><td id="fbk:" class="">Trầm tích học</td><td id="}_{c" class="">100-1000 năm</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80e0-ba19-f53eea75ed7a"><td id="~np|" class="">Cổ sinh khí hậu</td><td id="V_tX" class="">Lõi băng, 
vòng cây</td><td id="fbk:" class="">Paleoclimatology</td><td id="}_{c" class="">10-1000 năm</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-802c-9c7e-d55372036904" class=""><strong>Công thức:</strong><br/>\[<br/>L1 = \text{SeismicRisk} \times w_s + \text{WaterAvailability} \times w_w + \text{ClimateTrend} \times w_c<br/>\]</p></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80a1-b4f3-f6a115225622"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-8040-8c0d-c41191b281d2" class="">L2: SINH HỌC</h3></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-8056-814e-f102ce0730bf" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80b8-97ea-edffa4151bc4"><th id="puh|" class="simple-table-header-color simple-table-header">Thành phần</th><th id="gy~=" class="simple-table-header-color simple-table-header">Ví dụ</th><th id="y\g&gt;" class="simple-table-header-color simple-table-header">Phương pháp</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80c5-af9f-f01c9ce03583"><td id="puh|" class="">Cây chỉ thị</td><td id="gy~=" class="">Cây bạch đàn → đất nhiễm phèn</td><td id="y\g&gt;" class="">Geobotany</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8014-83ce-e1dd6484d35b"><td id="puh|" class="">Vi sinh</td><td id="gy~=" class="">Vi khuẩn trong đất báo hiệu khoáng sản</td><td id="y\g&gt;" class="">Metagenomics</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8093-bbae-f2727d2c8ba9"><td id="puh|" class="">Bệnh vùng</td><td id="gy~=" class="">Sốt rét ở vùng đầm lầy</td><td id="y\g&gt;" class="">Dịch tễ học</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8012-b487-d276adec2480"><td id="puh|" class="">Động vật tụ/tránh</td><td id="gy~=" class="">Chim tránh khu vực có động đất sắp xảy r
a</td><td id="y\g&gt;" class="">Ethology</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-809a-83a7-e3848cc9a6b3" class=""><strong>Công thức:</strong><br/>\[<br/>L2 = \sum \text{IndicatorSpecies}_i \times \text{Reliability}_i<br/>\]</p></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-8015-871a-cca067ef20a0"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-800c-ba40-e0250e4511ca" class="">L3: CƠ THỂ</h3></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-80e1-b402-ff967aac576d" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80a7-91ce-c420b163feae"><th id=":KWP" class="simple-table-header-color simple-table-header">Thành phần</th><th id="q:BZ" class="simple-table-header-color simple-table-header">Ví dụ</th><th id="xg}m" class="simple-table-header-color simple-table-header">Cơ chế</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-809e-96c4-e1849a735dad"><td id=":KWP" class="">Phản ứng cảm quan</td><td id="q:BZ" class="">Ngửi thấy mùi lưu huỳnh → núi lửa</td><td id="xg}m" class="">Khứu giác</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80cc-bc4c-c679948b91ca"><td id=":KWP" class="">Hành vi tránh/tụ</td><td id="q:BZ" class="">Run rẩy khi lạnh → sắp có bão</td><td id="xg}m" class="">Nhiệt độ cơ thể</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-807b-87c5-d72848c8f542"><td id=":KWP" class="">Bệnh nghề nghiệp</td><td id="q:BZ" class="">Bệnh phổi ở thợ mỏ → có khoáng sản</td><td id="xg}m" class="">Y học cổ truyền</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8020-8ee1-d557e0317e8a"><td id=":KWP" class="">Dinh dưỡng</td><td id="q:BZ" class="">Thiếu iốt → vùng xa biển</td><td id="xg}m" class="">Dinh dưỡng học</td></tr></div></tbody></table></div><div s
tyle="display:contents" dir="auto"><p id="353c5e6f-95bd-80c0-983a-ea2bf2e74f17" class=""><strong>Công thức:</strong><br/>\[<br/>L3 = \text{SensoryResponse} \times w_s + \text{OccupationalDisease} \times w_o<br/>\]</p></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80cb-a036-ece1bab8ee67"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-8004-9e50-d7b77551bede" class="">L4: LOÀI (CROSS-SPECIES)</h3></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-80d3-9f2d-c6fb03bd6193" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80df-b745-f4b50eb878d7"><th id="av;=" class="simple-table-header-color simple-table-header">Thành phần</th><th id="p@oe" class="simple-table-header-color simple-table-header">Ví dụ</th><th id="KUEc" class="simple-table-header-color simple-table-header">Tần suất</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8086-a02d-cdc9a1dbaae2"><td id="av;=" class="">Âm thanh báo động</td><td id="p@oe" class="">Chim kêu to trước động đất</td><td id="KUEc" class="">Giây-phút</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8064-98a8-e929dba0a5db"><td id="av;=" class="">Di cư</td><td id="p@oe" class="">Cá hồi di cư vào mùa sinh sản</td><td id="KUEc" class="">Năm</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-805c-8147-eb0960c13f29"><td id="av;=" class="">Đường đi thay đổi</td><td id="p@oe" class="">Bầy voi tránh vùng có nguy hiểm</td><td id="KUEc" class="">Ngày-tuần</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80f2-a8e7-cdd9048e3bfb" class=""><strong>Công thức:</strong><br/>\[<br/>L4 = \sum \text{Species}_i \times \text{AlertLevel}_i<br/>\]</p></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-8017-b8ed-e2bd727fe2cc"/></div><div style="display:contents" d
ir="auto"><h3 id="353c5e6f-95bd-808e-a86d-f11353c7809f" class="">L5: NGÔN NGỮ / ĐỊA DANH</h3></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-80e6-8651-deb1efc67266" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80cc-aa51-c9374d9c9fed"><th id="o;GB" class="simple-table-header-color simple-table-header">Thành phần</th><th id="@iOu" class="simple-table-header-color simple-table-header">Ví dụ</th><th id="YbDS" class="simple-table-header-color simple-table-header">Phương pháp</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8046-a3d3-cbf1a2eaae71"><td id="o;GB" class="">Từ tượng thanh</td><td id="@iOu" class="">&quot;Rào rào&quot; → mưa to</td><td id="YbDS" class="">Ngữ âm học</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80f6-8ac2-ce8af80d8e83"><td id="o;GB" class="">Ca dao, tục ngữ</td><td id="@iOu" class="">&quot;Chuồn chuồn bay thấp thì mưa&quot;</td><td id="YbDS" class="">Văn học dân gian</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8087-a09a-dee854aedd13"><td id="o;GB" class="">Bài thuốc</td><td id="@iOu" class="">&quot;Lá ổi chữa tiêu chảy&quot;</td><td id="YbDS" class="">Dược học cổ truyền</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80a3-968c-f21273bfedc2"><td id="o;GB" class="">Cách nói gián tiếp</td><td id="@iOu" class="">&quot;Ông trời đang nổi giận&quot; 
→ bão</td><td id="YbDS" class="">Ngôn ngữ học</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8082-bb8a-cdcb27386e90" class=""><strong>Công thức:</strong><br/>\[<br/>L5 = \sum \text{Keywords}_i \times \text{Frequency}<em>i \times \text{Reliability}</em>{\text{folk}}<br/>\]</p></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80f9-a476-fea1407c542e"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-80c8-9db3-ea4607bcf57a" class="">L6: VĂN HÓA / DI SẢN</h3></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-808d-9407-cf23ba5d0282" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8044-a761-c224baa95e3e"><th id="~X=`" class="simple-table-header-color simple-table-header">Thành phần</th><th id="df{e" class="simple-table-header-color simple-table-header">Ví dụ</th><th id="Ygvo" class="simple-table-header-color simple-table-header">Ý nghĩa</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8035-b403-c4d4e9a4d573"><td id="~X=`" class="">Trống đồng</td><td id="df{e" class="">Hoa văn mặt trời, chim, thuyền</td><td id="Ygvo" class="">Lịch, nghi lễ, chiến tranh</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-808f-98cc-e73c7ae878bc"><td id="~X=`" class="">Mộ táng</td><td id="df{e" class="">Hướng mộ, đồ tùy táng</td><td id="Ygvo" class="">Tín ngưỡng, 
địa vị xã hội</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80e2-b55d-cf8ea33de6d7"><td id="~X=`" class="">Lễ hội</td><td id="df{e" class="">Lễ hội đền Hùng</td><td id="Ygvo" class="">Thời điểm quan trọng trong năm</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-800a-a571-ed1ad5865818"><td id="~X=`" class="">Cấm kỵ</td><td id="df{e" class="">Cấm vào rừng thiêng</td><td id="Ygvo" class="">Bảo vệ tài nguyên</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8065-b1b4-fbbdba53501b" class=""><strong>Công thức:</strong><br/>\[<br/>L6 = \text{RitualCalendar} + \text{TabooSpace} + \text{ArtifactPattern}<br/>\]</p></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80d0-9ccd-db31f0d92c08"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-8075-af15-ccf6acbf953f" class="">L7: QUYỀN LỰC / XÃ HỘI</h3></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-808c-a57d-c9836b139ca1" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8073-b22d-d6fcd7acdb80"><th id="=&lt;so" class="simple-table-header-color simple-table-header">Thành phần</th><th id="r?HH" class="simple-table-header-color simple-table-header">Ví dụ</th><th id="sTIX" class="simple-table-header-color simple-table-header">Phương pháp</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80e1-b217-e4762a97cf29"><td id="=&lt;so" class="">Ai giữ nhịp (trống)</td><td id="r?HH" class="">Trưởng làng giữ trống</td><td id="sTIX" class="">Khảo cổ, dân tộc học</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8088-9570-daa48af1b391"><td id="=&lt;so" class="">Ai giữ lịch</td><td id="r?HH" class="">Thầy cúng, 
nhà thiên văn</td><td id="sTIX" class="">Lịch sử tôn giáo</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8005-ad84-ce813ca79fbb"><td id="=&lt;so" class="">Ai giữ nghề</td><td id="r?HH" class="">Gia đình đúc đồng</td><td id="sTIX" class="">Gia phả, truyền nghề</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80de-be13-dc9abd48303e"><td id="=&lt;so" class="">Ai quản lý nước</td><td id="r?HH" class="">Trưởng làng, vua</td><td id="sTIX" class="">Thủy lợi học</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-809e-a748-fa0b46e9ea5f"><td id="=&lt;so" class="">Ai cấm đất</td><td id="r?HH" class="">Nhà vua phong đất</td><td id="sTIX" class="">Sử học</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8081-a75c-f754df026586" class=""><strong>Công thức:</strong><br/>\[<br/>L7 = \log(\text{Power}_{entity}) \times \text{ResourceControl}<br/>\]</p></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80d1-855a-da4c9e4ab7c0"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-809f-84a0-e7b39ce2c79f" class="">L8: DÒNG TIỀN THÔNG MINH</h3></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-80f6-b7f3-da589b3d7519" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8002-adac-e5c402097aea"><th id="mhPH" class="simple-table-header-color simple-table-header">Thành phần</th><th id="kSzL" class="simple-table-header-color simple-table-header">Công thức</th><th id="`e:~" class="simple-table-header-color simple-table-header">Nguồn</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80a4-b59a-dfe0f66b108c"><td id="mhPH" class="">Institutional volume</td><td id="kSzL" class=""><code>V_inst = V_total - V_retail</code></td><td id="`e:~" class="">CFTC COT, OI, 
footprint</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-804d-a652-e6ba5542bb56"><td id="mhPH" class="">Khối lượng bất thường</td><td id="kSzL" class=""><code>Z(V) &gt; 
2</code></td><td id="`e:~" class="">Volume profile</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8082-b2ca-e98631bc12a6"><td id="mhPH" class="">Absorption</td><td id="kSzL" class=""><code>Volume tại vùng kháng cự mà giá không giảm</code></td><td id="`e:~" class="">Delta, order book</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-800d-9e83-d816e88fdca3" class=""><strong>Công thức:</strong><br/>\[<br/>L8 = \frac{\text{SmartVolume}}{\text{TotalVolume}} \times \text{SignalDirection}<br/>\]</p></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80f1-a31b-f116fff157ce"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-80aa-b93b-e3c88228707b" class="">L9: CHI PHÍ CƠ HỘI</h3></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-803a-838d-c542f3bdbbf7" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80cd-a8cf-cf85077c2ce0"><th id="Tz[P" class="simple-table-header-color simple-table-header">Thành phần</th><th id="YBa]" class="simple-table-header-color simple-table-header">Công thức</th><th id="NCod" class="simple-table-header-color simple-table-header">So sánh</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-809f-a65c-ec8c8ba90562"><td id="Tz[P" class="">Lợi suất trái phiếu</td><td id="YBa]" class=""><code>Y_{10y} - Y_{2y}</code></td><td id="NCod" class="">Đường cong lợi suất</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8089-b768-e84e35d65740"><td id="Tz[P" class="">Lãi suất ngân hàng</td><td id="YBa]" class=""><code>SOFR, ESTR</code></td><td id="NCod" class="">Chi phí carry</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-804c-a7f8-fe4b3a6e8194"><td id="Tz[P" class="">Chỉ số thị trường</td><td id="YBa]" class=""><code>S&amp;P500 PE, 
CAPE</code></td><td id="NCod" class="">So với lịch sử</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-805f-98cc-c52348eb9d75" class=""><strong>Công thức:</strong><br/>\[<br/>L9 = r_{\text{asset}} - r_{\text{risk\_free}}<br/>\]</p></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80a0-a62e-e33388dc7df6"/></div><div style="display:contents" dir="auto"><h3 id="353c5e6f-95bd-8012-a658-d89ca30ce8b8" class="">L10: TRÁNH / TỤ VI MÔ</h3></div><div style="display:contents" dir="ltr"><table id="353c5e6f-95bd-8026-af8e-cbd5a7fa4343" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8011-bc02-c637b36ead83"><th id="[jMl" class="simple-table-header-color simple-table-header">Thành phần</th><th id=";kx_" class="simple-table-header-color simple-table-header">Công thức</th><th id="ukeR" class="simple-table-header-color simple-table-header">Ý nghĩa</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-8039-bba5-d804c83feaf4"><td id="[jMl" class="">Mật độ giao dịch</td><td id=";kx_" class=""><code>D(p) = ∑ volume at price p</code></td><td id="ukeR" class="">Vùng có thanh khoản</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80bf-9c8a-d0a39530de21"><td id="[jMl" class="">Order book imbalance</td><td id=";kx_" class=""><code>IMB = (V_bid - V_ask)/(V_bid + V_ask)</code></td><td id="ukeR" class="">Áp lực</td></tr></div><div style="display:contents" dir="ltr"><tr id="353c5e6f-95bd-80cc-9898-eed73a3c2bcb"><td id="[jMl" class="">Volume profile nodes</td><td id=";kx_" class=""><code>POC (point of control)</code></td><td id="ukeR" class="">Giá được giao dịch nhiều nhất</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80c6-9531-cbb1fc0eeaa2" class=""><strong>Công thức:</strong><br/>\[<br/>L10 = D(p) \times (1 - 2|\text{IMB}|) \quad \
text{(liquidity depth)}<br/>\]</p></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-80e4-a2cd-c1b1385e2171"/></div><div style="display:contents" dir="auto"><h2 id="353c5e6f-95bd-805b-8148-dea3d2721e91" class="">TỔNG KẾT PHẦN 2</h2></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8036-b8d4-ecf9af5a02e2" class="">32 tầng + 10 lớp tín hiệu tạo thành <strong>một hệ thống phân cấp hoàn chỉnh</strong> từ vũ trụ (entropy) đến vi cấu trúc thị trường (order book).</p></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80c7-a6df-df9a3a9d9b9c" class="">Mỗi tầng:</p></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-80bb-b6ae-c48057a521a5" class="bulleted-list"><li style="list-style-type:disc">Có <strong>phương trình riêng</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-8048-adac-db76aa10e8a1" class="bulleted-list"><li style="list-style-type:disc">Có <strong>biến trạng thái riêng</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-805e-bfab-fb638e101349" class="bulleted-list"><li style="list-style-type:disc">Có <strong>chế độ thất bại và phục hồi</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="353c5e6f-95bd-8028-bf65-e8f1fc5127a2" class="bulleted-list"><li style="list-style-type:disc"><strong>Kết nối</strong> với các tầng khác qua ma trận tương tác</li></ul></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-80ec-91c1-f35503762e41" class="">Không tầng nào bị bỏ qua. 
Không gap nào không được xử lý (trừ những gap vĩnh viễn đã được formalize).</p></div><div style="display:contents" dir="auto"><hr id="353c5e6f-95bd-8058-b67a-ec345067eea5"/></div><div style="display:contents" dir="auto"><p id="353c5e6f-95bd-8097-bff9-c5dd963f796e" class=""><strong>Heritage ∅ – The only version where every layer is defined, connected, and accountable.</strong></p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
