---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>MOU</title><style>
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
	
</style></head><body><article id="2b0c5e6f-95bd-80fb-ab01-e53d4fd66922" class="page sans"><header><h1 class="page-title" dir="auto">MOU</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-8073-a86e-e88ccde7228a" class=""><strong>BIÊN BẢN GHI NHỚ HỢP TÁC (MoU)</strong></h1></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80c1-8a06-d71f6c0b6778" class=""><strong>合作备忘录（MoU）</strong></p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80c7-82b6-ec040a1eb52a" class="">Về nhập khẩu – tài trợ – vận hành xe điện Baojun tại Việt Nam</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8095-8021-d0254cf2e462" class="">关于宝骏电动车在越南的进口、融资与运营合作</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8055-aae7-e7589ee030f7" class=""><strong>Ngày / 日期:</strong> …… / …… / 2025</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80e7-b1f2-c074536c18fd" class=""><strong>Địa điểm / 地点:</strong> ……………………………</p></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-806a-b019-dabc4da22df7"/></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8092-9d3c-ed53ced7399f" class=""><strong>I. CÁC BÊN / 当事双方</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-80d6-8f48-f66b059afe4b" class=""><strong>Bên A – UNIPOWER (Việt Nam)</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ce-9826-d08df8feca6a" class="">甲方 – UNIPOWER（越南）</p></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-80dc-889b-f0c467c4aaab" class="bulleted-list"><li style="list-style-type:disc">Đại diện: Ông <strong>Hồ Anh Tuấn</strong> – CEO<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b0-bc4d-e8c8b6f28b44" class="">法定代表人：胡英俊 先生 – 总经理</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-8015-8a98-c91f4dec61e8" class="bulleted-list"><li style="list-style-type:disc">Lĩnh vực: Hệ sinh thái EV, trạm sạc iSac, vận tải Unitaxi, fintech EV<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-800f-8516-e26a1009b5b8" class="">领域：EV 生态系统、iSac 充电、Unitaxi、电动车金融</p></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-8063-aa31-da209623af4b" class=""><strong>Bên B – BAOJUN / SGMW (Trung Quốc)</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-800a-bcdf-df66960504ed" class="">乙方 – 宝骏 / 上汽通用五菱（中国）</p></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-809f-ac13-ef5b443aa300" class="bulleted-list"><li style="list-style-type:disc">Đại diện: ………………………<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-809e-9b9f-e6a32bfc2d13" class="">法定代表人：……………………</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-80fd-b1be-f24860ba475e" class="bulleted-list"><li style="list-style-type:disc">Lĩnh vực: Sản xuất – xuất khẩu xe điện<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ac-8e4e-c8da8b59c1c2" class="">领域：电动车生产与出口</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-8018-89e4-e40244cf8bbe"/></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80a5-b87e-e525fc9e4085" class=""><strong>II. MỤC ĐÍCH &amp; PHẠM VI / 目的与范围</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2b1c5e6f-95bd-80e9-b50c-d4c679a7cc4f" class="numbered-list" start="1"><li>Thiết lập hợp tác dài hạn đưa xe Baojun vào Việt Nam qua hệ sinh thái EV của Unipower.<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8085-b826-eddc147902fa" class="">建立长期合作，将宝骏电动车导入越南并接入 Unipower 生态系统。</p></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b1c5e6f-95bd-80ce-b30b-f6b330389b5d" class="numbered-list" start="2"><li>Áp dụng mô hình <strong>vendor financing 1–2%/năm</strong> và phân phối thương mại.<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a3-a4c5-e8d51428ee91" class="">采用 <strong>1–2% 年利率供应商融资模式</strong>及商业化分销。</p></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b1c5e6f-95bd-80df-94da-dca4a1be01bb" class="numbered-list" start="3"><li>Mẫu xe ưu tiên: <strong>Baojun E6, Baojun Yunduo</strong>.<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ad-96d1-c40b1f4c65c7" class="">优先车型：<strong>宝骏 E6、宝骏云朵</strong>。</p></div></li></ol></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-8075-92a8-db2bd4c0db46"/></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80cc-b407-d3a817f5d344" class=""><strong>III. NGUYÊN TẮC ĐỘC QUYỀN / 独家原则</strong></h2></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-80a4-b393-c1b4648044dc" class="bulleted-list"><li style="list-style-type:disc">Baojun xem xét cấp cho Unipower <strong>quyền độc quyền phân phối</strong> tại Việt Nam khi đạt chỉ tiêu doanh số tối thiểu.<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-804d-8aff-e033aa49babf" class="">宝骏在甲方达成年度销量指标时，考虑授予越南 <strong>独家经销权</strong>。</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-805f-83d1-cacee5949b0c" class="bulleted-list"><li style="list-style-type:disc">Không chỉ định thêm nhà phân phối khác cho các mẫu đã cấp độc quyền.<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8039-ba84-fa53c8bb900c" class="">对已授予独家车型，不再指定其他越南经销商。</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-8022-b52b-eb39b3872905"/></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8091-8906-d3292e5896d7" class=""><strong>IV. THÍ ĐIỂM &amp; ĐÁNH GIÁ / 试点与评估</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2b1c5e6f-95bd-8042-b71b-eb9733231c55" class="numbered-list" start="1"><li>Baojun cung cấp <strong>02 xe thử nghiệm</strong> (E6 + Yunduo).<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-804d-8947-e81a289f87ed" class="">宝骏提供 <strong>2 辆试点车辆</strong>（E6 与云朵）。</p></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b1c5e6f-95bd-800c-ac88-eb83a7305256" class="numbered-list" start="2"><li>Thời gian thử nghiệm: <strong>90–120 ngày</strong>.<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8068-b948-e1326a8d8f37" class="">试点期：<strong>90–120 天</strong>。</p></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b1c5e6f-95bd-80ac-a0d7-fb9a7076e33a" class="numbered-list" start="3"><li>Đánh giá: điện năng tiêu thụ, độ ổn định, độ bền pin, trải nghiệm tài xế &amp; hành khách.<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-801b-94ed-f56e65284f02" class="">评估内容：能耗、稳定性、电池耐久、司机与乘客体验。</p></div></li></ol></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-808f-931e-c8e9692e49c3"/></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8067-b438-d5c45da0eac3" class=""><strong>V. GIÁ, THANH TOÁN &amp; TÀI TRỢ / 价格、支付与融资</strong></h2></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-800a-af1c-c4648153c2e5" class="bulleted-list"><li style="list-style-type:disc">Giá xuất xưởng ưu đãi (Factory Price).<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8032-9998-c03466798c4a" class="">提供优惠出厂价。</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-802e-a2ff-c753f0a9c025" class="bulleted-list"><li style="list-style-type:disc"><strong>FMCG/Vendor Financing:</strong><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-80ad-82bc-ecd8147dba40" class="bulleted-list"><li style="list-style-type:circle">Tài trợ <strong>70–80%</strong> giá trị xe</li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-80c5-82e3-e194b5d5d6f6" class="bulleted-list"><li style="list-style-type:circle">Lãi suất <strong>1–2%/năm</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-80a3-bafa-cd1bbee0bc49" class="bulleted-list"><li style="list-style-type:circle">Kỳ hạn <strong>5 năm</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-800b-901d-decaa742a6b7" class="bulleted-list"><li style="list-style-type:circle">Không yêu cầu tài sản đảm bảo thêm<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8035-97ae-ee6ceecd33ac" class="">供应商融资：</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-80a2-a425-f028b76214b5" class="bulleted-list"><li style="list-style-type:circle">融资 70–80%</li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-8026-8c9d-c6dd490529d8" class="bulleted-list"><li style="list-style-type:circle">年利率 1–2%</li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-8023-a728-e6ef0a491dfe" class="bulleted-list"><li style="list-style-type:circle">期限 5 年</li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-808a-a6ef-e43f7653448d" class="bulleted-list"><li style="list-style-type:circle">无额外抵押要求</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-80a5-b2c3-e5d5e1606dfb" class="bulleted-list"><li style="list-style-type:disc">Lô nhỏ: T/T; Lô lớn: L/C hoặc trả chậm có bảo lãnh.<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-802d-a446-dc554a16f154" class="">小批量：电汇；大批量：信用证或延期支付（附保函）。</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-80d0-af76-c81259b3d226"/></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80dd-990c-da13f7c7c585" class=""><strong>VI. KỸ THUẬT – BẢO HÀNH – LINH KIỆN</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8013-9e9e-cfa9f28daf60" class="">技术 – 质保 – 配件</p></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-803f-8fb1-c596f7b9b4d8" class="bulleted-list"><li style="list-style-type:disc">Bảo hành xe tối thiểu <strong>69 tháng</strong>.<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-806a-b9e4-fa61ff992385" class="">整车质保不少于 <strong>69 个月</strong>。</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-806c-b437-e8f93103898a" class="bulleted-list"><li style="list-style-type:disc">Hỗ trợ linh kiện chính hãng và kho phụ tùng tại Việt Nam.<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80d6-a3ad-c4d42c1005b8" class="">保障原厂配件供应，并在越南设最低库存。</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-808d-a7cf-c43edf014c77" class="bulleted-list"><li style="list-style-type:disc">OTA, telematics, đào tạo kỹ thuật đầy đủ.<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-807e-9d54-eccdeef6d426" class="">提供 OTA、车联网与技术培训。</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-8067-a939-eebd5589868a"/></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80b4-b543-c30e2d5a4e64" class=""><strong>VII. HẠ TẦNG ISAC / iSac 充电网络</strong></h2></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-8028-8115-db4fd9d0c87c" class="bulleted-list"><li style="list-style-type:disc">Baojun đảm bảo tương thích sạc (AC/DC, CCS/GB/T…).<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8089-a86d-c5253b76526e" class="">宝骏确保充电标准兼容。</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-80fb-9e86-e82f641d2902" class="bulleted-list"><li style="list-style-type:disc">Unipower ưu tiên bố trí trạm cho xe Baojun trong hệ sinh thái taxi – logistics – thuê xe.<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80d4-ae17-ddfcdeb3ccf6" class="">Unipower 在出租车、物流、租赁生态中优先保障宝骏车辆的充电资源。</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-8090-9b73-e5a52b9ecdbc"/></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-806b-bc59-dbf7472365c4" class=""><strong>VIII. BẢO MẬT &amp; GIẢI QUYẾT TRANH CHẤP</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8089-8bfe-c591200aa0da" class="">保密与争议解决</p></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-801c-8634-dc5f850b214f" class="bulleted-list"><li style="list-style-type:disc">Hai Bên bảo mật toàn bộ dữ liệu kỹ thuật – thương mại.<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-804f-9af2-fc3f1b9870e0" class="">双方对所有技术与商业信息严格保密。</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-8043-961e-c1c388cbf973" class="bulleted-list"><li style="list-style-type:disc">Luật áp dụng: <strong>Singapore / Hong Kong</strong>.<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-800f-9b6f-f8fd0a787346" class="">适用法律：<strong>新加坡 / 香港</strong>。</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-8092-97fb-e39355111b12" class="bulleted-list"><li style="list-style-type:disc">Tranh chấp: thương lượng trước → nếu không thành, đưa ra <strong>SIAC hoặc HKIAC</strong>.<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ca-95a2-d84f53cfd9fd" class="">争议：先协商 → 不成则提交 <strong>SIAC 或 HKIAC</strong> 仲裁。</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-80d9-8eb9-d32db838884a"/></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8087-b9d1-fedf77b71e08" class=""><strong>IX. HIỆU LỰC</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a1-9bd0-ce78980e7584" class="">效力</p></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-8073-8444-f6616ed49c8d" class="bulleted-list"><li style="list-style-type:disc">MoU có hiệu lực <strong>12 tháng</strong>, dùng để chuẩn bị cho Hợp đồng chính thức.<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-803e-a002-f2afeb922622" class="">本备忘录有效期 <strong>12 个月</strong>，用于准备正式合同。</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-80a0-9c58-cac1d45ada71" class="bulleted-list"><li style="list-style-type:disc">Lập bằng tiếng Việt &amp; tiếng Trung, hiệu lực ngang nhau.<div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8074-9358-f81a4b77ed72" class="">本 MoU 以越南文与中文制作，两种文本效力相同。</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-800b-891d-f91d9ee11e0a"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-8008-851c-e9efd6a04d36" class=""><strong>ĐẠI DIỆN BÊN A / 甲方代表</strong></h1></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80e6-a1e8-ec173ed77910" class="">UNIPOWER</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-807d-b744-d6111dd40997" class="">………………………………</p></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-8047-956c-f836ba153592" class=""><strong>ĐẠI DIỆN BÊN B / 乙方代表</strong></h1></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-805a-ac83-f73d0e2f4c28" class="">BAOJUN / SGMW</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8046-ad0e-e17da254b52e" class="">………………………………</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
