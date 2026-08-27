---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>📘 SỔ TAY TÁC PHONG UNITAXI</title><style>
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
	
</style></head><body><article id="2aec5e6f-95bd-8066-b569-e7ce1c3d9d82" class="page sans"><header><h1 class="page-title" dir="auto"><strong>📘 SỔ TAY TÁC PHONG UNITAXI</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80a1-8df4-f9b8cb92cc87" class=""><strong>Phiên bản nội bộ – 2025</strong></p></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-80e3-ac34-f3ae09d33991"/></div><div style="display:contents" dir="auto"><h1 id="2aec5e6f-95bd-8005-98ee-dd947d215367" class=""><strong>📖 Lời chào mừng</strong></h1></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8022-9e59-e0c0a7d14156" class=""><strong>Chào mừng bạn đến với Unitaxi!</strong></h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80c8-b996-c386a7477e18" class="">Cảm ơn bạn đã chọn trở thành một phần của Unitaxi. Từ hôm nay, bạn không chỉ lái một chiếc xe hay đứng trong một ca trực. <strong>Bạn chính là gương mặt của cả hệ thống. </strong>Là người khách nhìn thấy đầu tiên, và cũng là người khách nhớ lâu nhất. 
Mỗi chuyến xe bạn chạy, mỗi câu nói bạn thốt ra, mỗi hành động nhỏ bạn làm — đều góp phần tạo nên ấn tượng về Unitaxi trong mắt khách hàng.</p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8010-bce1-e167b480601d" class="">Sổ tay này được viết để giúp bạn:</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80f8-85d3-c9d08e213c2e" class="bulleted-list"><li style="list-style-type:disc"><strong>nắm rõ chuẩn tác phong của Unitaxi</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-806e-944b-dfb213fa7db7" class="bulleted-list"><li style="list-style-type:disc"><strong>giữ hình ảnh chuyên nghiệp trong mọi tình huống</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8000-a2ba-e2f1758513a6" class="bulleted-list"><li style="list-style-type:disc"><strong>tạo cảm giác an tâm – tin tưởng – dễ chịu cho khách</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8048-82b4-f9a5a1f942af" class="bulleted-list"><li style="list-style-type:disc"><strong>bảo vệ chính bạn bằng quy trình an toàn &amp; kỷ luật rõ ràng</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80f6-93f6-f4b7311945ed" class="">Hãy xem đây là <strong>ngôn ngữ chung</strong>, là “chìa khoá” giúp tất cả chúng ta cùng vận hành mượt, cùng nhau xây dựng một môi trường làm việc an toàn, đáng tự hào và bền vững. 
Chúng tôi rất vui vì có bạn đồng hành.<strong> Chúc bạn luôn mạnh khoẻ – tự tin – và tự hào về công việc mình đang làm.</strong></p></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-80a1-95d4-f04864698e47"/></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8049-8b02-d67527adc6ca" class="">TỰ HÀO NGHỀ TÀI XẾ VIỆT NAM</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8017-967f-e8a05ed07b7e" class="">Lái xe không chỉ là một công việc, mà là một <strong>nghề</strong> mang giá trị sâu sắc, gắn bó với <strong>sự an toàn</strong>, <strong>niềm tin</strong> và cuộc sống hàng ngày của hàng triệu người Việt. Mỗi chuyến xe bạn thực hiện vượt xa hành trình từ điểm A đến điểm B – đó là sự hỗ trợ cho một người mẹ về đón con, sự đồng hành cùng cụ già đến bệnh viện, sự giúp đỡ nhân viên kịp cuộc họp quan trọng, hành trình đưa học sinh về nhà <strong>an toàn</strong>, hay lời chào đón hành khách xa quê trở lại Sài Gòn. Bạn hiện diện trong những khoảnh khắc đời thường nhưng đầy ý nghĩa, khiến <strong>nghề tài xế</strong> giữ một vị trí đặc biệt tại Việt Nam: một <strong>nghề phục vụ</strong> với <strong>danh dự</strong>, vất vả nhưng luôn đáng <strong>tự hào</strong>.</p></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80f4-bad9-e9f433d2b2eb" class="">Tự hào vì <strong>sự an toàn</strong> bạn mang đến</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8016-b858-f555d63beea0" class="">Không phải ai cũng đủ khả năng đảm nhận vai trò này. Một tài xế giỏi không chỉ biết lái xe mà còn bảo vệ khách qua những quyết định nhỏ nhặt: giữ khoảng cách <strong>an toàn</strong>, lái êm ái, nhắc nhở dây <strong>an toàn</strong>, và bình tĩnh xử lý sự cố. 
Đó chính là <strong>sự chuyên nghiệp</strong> – là <strong>đẳng cấp</strong> của <strong>nghề tài xế</strong>.</p></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8093-81d9-e5f8220dfe52" class="">Tự hào vì <strong>sự tử tế</strong> bạn tạo ra mỗi ngày</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80a4-9f60-ea291a386e5a" class="">Những hành động nhỏ nhưng để lại dấu ấn sâu sắc: một lời chào thân thiện, mang ô che mưa cho khách, dừng xe đúng chỗ <strong>an toàn</strong>, nhắc nhở kiểm tra đồ đạc, trả lại tài sản thất lạc, hay kiên nhẫn chờ khách lớn tuổi lên xe chắc chắn. Những điều này không bắt buộc, nhưng bạn chọn làm bởi hiểu rõ giá trị của <strong>sự tử tế</strong> – phẩm chất cao quý nhất của tài xế Việt Nam.</p></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8052-b830-c1fe9c362405" class="">Tự hào vì bạn đại diện cho một <strong>chuẩn mới</strong></h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80ae-8ac1-c9a53a7c9638" class="">Unitaxi không chỉ xây dựng một hãng xe, mà còn hướng đến tạo nên thế hệ tài xế kiểu mẫu với <strong>kỷ luật</strong>, <strong>tác phong chuyên nghiệp</strong>, <strong>tự trọng</strong>, <strong>sự tinh tế</strong> và niềm <strong>tự hào</strong> trong công việc. Đây là hình ảnh mà xã hội mong đợi, và bạn – từng thành viên trong đội ngũ – chính là người hiện thân cho <strong>chuẩn mực</strong> ấy.</p></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8027-abeb-f1a72a980ca4" class="">Tự hào vì bạn mang lại <strong>niềm tin</strong> cho khách</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-804f-8cdd-da2e74c0df5b" class="">Trong một đất nước đông đúc, vội vã và đầy áp lực như Việt Nam, điều duy nhất khách hàng tìm kiếm khi lên xe là cảm giác <strong>an toàn</strong>. Khi họ nhận ra điều đó từ bạn, không cần bất kỳ lời quảng cáo nào khác. 
<strong>Nghề lái xe</strong> vì thế trở thành một <strong>nghề đẹp</strong> – đẹp ở <strong>sự tử tế</strong>, ở <strong>sự bình tĩnh</strong>, và ở cái tâm đưa người khác về nhà <strong>an toàn</strong>.</p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80a1-82f8-eaaf321ce4fb" class="">Tại Unitaxi, chúng tôi tin rằng một tài xế <strong>tự trọng</strong> sẽ tạo nên một dịch vụ <strong>tự hào</strong>. <strong>Cảm ơn bạn đã đồng hành cùng chúng tôi trên hành trình này!</strong></p></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-80fb-be5b-e3c30eb6afcf"/></div><div style="display:contents" dir="auto"><h1 id="2aec5e6f-95bd-801e-8f1c-c329b3b89e90" class=""><strong>📖 Triết lý phục vụ Unitaxi</strong></h1></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80c3-970f-ca15315b1a85" class="">1. AN TOÀN TUYỆT ĐỐI – NỀN TẢNG CỦA MỌI HÀNH VI</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8042-acd2-eeab80ef0435" class=""><strong>An toàn</strong> là ưu tiên tối thượng, vì không có nó, <strong>tử tế</strong> hay lịch sự đều vô nghĩa. Tài xế giỏi lái êm, đều, giữ khoảng cách, quan sát chủ động, tỉnh táo, tránh lái khi mệt mỏi, và tuân thủ đèn vàng-đỏ, không đọc tin nhắn hay mất bình tĩnh với khách khó. Tai nạn nhỏ hại <strong>hình ảnh thương hiệu</strong>, phanh gấp mất <strong>niềm tin</strong>, mất tập trung nguy hiểm cho chính bạn. Unitaxi đặt <strong>an toàn</strong> trên tốc độ, điểm số, doanh thu để tôn trọng khách và <strong>nghề nghiệp</strong>.</p></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8020-bc6f-dfca8860100d" class="">2. TÔN TRỌNG &amp; LỊCH SỰ – KHÔNG PHÂN BIỆT AI</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8043-a9f8-de1120632dca" class=""><strong>Lịch sự</strong> là tôn trọng con người, không chỉ hình thức. 
Tài xế Unitaxi tránh gắt gỏng, tranh cãi, giữ giọng nhẹ nhàng, không hỏi riêng tư, phán xét hay hút thuốc, mở nhạc lớn, đùa nhạy cảm. Người Việt nhạy với <strong>thái độ</strong>: lời nói dịu hóa giải căng thẳng, cử chỉ đúng mực tạo <strong>an tâm</strong>, ấn tượng tốt lan gấp đôi, xấu gấp mười. <strong>Tôn trọng</strong> là ngôn ngữ chung, áp dụng cho mọi khách.</p></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8010-83e7-db6a163d78c3" class="">3. CHĂM KHÁCH NHƯ NGƯỜI THÂN – TỬ TẾ ĐÚNG LÚC, ĐÚNG MỰC</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80eb-9a66-fd41dcac289a" class="">“Chăm khách như người thân” là <strong>quan tâm</strong> đúng lúc, chu đáo vừa đủ, không phiền, không giả tạo. Unitaxi mong tài xế thể hiện <strong>tử tế</strong> và <strong>tinh tế</strong>.</p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-805f-887b-d5eb5d717963" class="">Khách không chỉ là người đi xe, mà là cá nhân với mệt mỏi, áp lực. Bạn làm hành trình họ dễ chịu hơn: người Việt nhạy với <strong>thái độ</strong>, nụ cười hay lời nói đúng lúc vượt xa giá cả; 80% ấn tượng từ chi tiết nhỏ như tin nhắn, ô mưa, nhắc <strong>an toàn</strong>. <strong>Tử tế</strong> đúng lúc giảm khiếu nại, tăng quay lại, là <strong>marketing</strong> tự nhiên; hành động <strong>tinh tế</strong> dịu khách vội, giảm xung đột. <strong>Niềm tin</strong> mạnh mẽ với người già, trẻ em, khách bệnh viện hay mưa/nắng – không mua được bằng quảng cáo. 
Phù hợp <strong>văn hóa Việt Nam</strong> trân trọng <strong>tôn trọng</strong>, <strong>tinh tế</strong>, Unitaxi đặt nó làm trung tâm <strong>văn hóa phục vụ</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-80d2-942c-f03aae2057b2"/></div><div style="display:contents" dir="auto"><h1 id="2aec5e6f-95bd-807b-a934-daf93750120e" class=""><strong>📖 Bộ 8 Chuẩn Tác phong Unitaxi</strong></h1></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8018-8970-ee8b3fd0a590" class="">1. AN TOÀN TRƯỚC – SAU – LUÔN LUÔN</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-806d-b0c2-ce9de32dee9d" class="bulleted-list"><li style="list-style-type:disc"><strong>Chuẩn:</strong> Tránh phanh gấp, tăng tốc đột ngột hay mất tập trung.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80c4-b1a0-e62a79dc7f32" class="bulleted-list"><li style="list-style-type:disc"><strong>Ý nghĩa:</strong> <strong>An toàn</strong> không chỉ bảo vệ bạn và khách mà còn là nền tảng cho mọi hành vi trong công việc.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8095-beb3-cb7d627e5a35" class="bulleted-list"><li style="list-style-type:disc"><strong>Hành vi:</strong> Duy trì khoảng cách an toàn, quan sát xa, không lái xe khi mệt mỏi, và tuân thủ nghiêm ngặt <strong>luật giao thông</strong>.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8086-aa2d-e92025901ca3" class="">2. 
ĐÚNG GIỜ &amp; GIỮ LỜI</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8019-8970-cda5019f71c7" class="bulleted-list"><li style="list-style-type:disc"><strong>Chuẩn:</strong> Đến đúng giờ ca làm và đón khách đúng thời gian cam kết.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8020-9c9c-e3123f088fa4" class="bulleted-list"><li style="list-style-type:disc"><strong>Ý nghĩa:</strong> Điều này phản ánh <strong>sự chuyên nghiệp</strong> và thể hiện <strong>tôn trọng</strong> đối với thời gian của khách hàng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8072-a60a-dd5583699a17" class="bulleted-list"><li style="list-style-type:disc"><strong>Hành vi:</strong> Báo trước nếu đến sớm hoặc trễ 1–2 phút, đồng thời không tự ý điều chỉnh lịch trình.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8019-963e-d74c067ae108" class="">3. XE SẠCH – MÙI DỄ CHỊU – NHIỆT ĐỘ ỔN</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-802e-80f0-ea8cc243f298" class="bulleted-list"><li style="list-style-type:disc"><strong>Chuẩn:</strong> Không gian trong xe phải tạo cảm giác dễ chịu ngay từ những giây đầu tiên.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-801e-abb6-d80cb15ccf0f" class="bulleted-list"><li style="list-style-type:disc"><strong>Ý nghĩa:</strong> Đây là yếu tố cơ bản định hình đến 80% <strong>ấn tượng</strong> ban đầu của khách.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8018-80eb-d7e69f62a82c" class="bulleted-list"><li style="list-style-type:disc"><strong>Hành vi:</strong> Lau xe mỗi ngày, giữ mùi trung tính, điều chỉnh điều hòa ở mức 24–25°C, và sắp xếp gọn gàng không để đồ cá nhân lộn xộn.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8085-a167-cdeb753f8ee8" class="">4. 
GIỌNG NÓI NHẸ – RÕ – KHÔNG TRANH CÃI</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8017-8ce8-eba366897743" class="bulleted-list"><li style="list-style-type:disc"><strong>Chuẩn:</strong> Mọi giao tiếp phải giữ được sự <strong>ổn định</strong>, nhẹ nhàng, không gây áp lực cho khách.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80b2-906d-c2cc1188b25f" class="bulleted-list"><li style="list-style-type:disc"><strong>Ý nghĩa:</strong> Với người Việt, <strong>thái độ</strong> qua giọng nói đóng vai trò quyết định trong <strong>trải nghiệm</strong> của khách.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-809c-ba39-ec8d6fccf5c6" class="bulleted-list"><li style="list-style-type:disc"><strong>Hành vi:</strong> Mở đầu bằng một lời chào nhẹ nhàng, nói chậm khi căng thẳng, và tuyệt đối tránh tranh cãi.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8044-b35c-e3c912a511be" class="">5. TRUNG THỰC VỚI HỆ THỐNG (DỮ LIỆU – BÁO CÁO – TÀI SẢN)</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8059-8a13-c9896a133e73" class="bulleted-list"><li style="list-style-type:disc"><strong>Chuẩn:</strong> Không gian dối, không làm sai lệch bất kỳ thông tin nào.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8073-9989-fa7c058b5136" class="bulleted-list"><li style="list-style-type:disc"><strong>Ý nghĩa:</strong> <strong>Trung thực</strong> trong dữ liệu đảm bảo hệ thống vận hành <strong>trơn tru</strong> và hiệu quả.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-809f-9db9-c7b73258bd99" class="bulleted-list"><li style="list-style-type:disc"><strong>Hành vi:</strong> Báo cáo lỗi chính xác, không tắt app khi làm việc, và trả lại đồ thất lạc ngay lập tức.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-802b-b493-c3da68006d3a" class="">6. 
KỶ LUẬT GIỜ GIẤC – QUY TRÌNH</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8078-a2c6-eac6b1f457c9" class="bulleted-list"><li style="list-style-type:disc"><strong>Chuẩn:</strong> Tuân thủ đúng quy trình, lộ trình và thời gian làm – nghỉ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8047-9640-c545ad6a8c1a" class="bulleted-list"><li style="list-style-type:disc"><strong>Ý nghĩa:</strong> <strong>Kỷ luật</strong> là chìa khóa đảm bảo <strong>an toàn</strong>, giảm rủi ro và giữ vững <strong>hình ảnh công ty</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8098-aa44-f5ec9e986e23" class="bulleted-list"><li style="list-style-type:disc"><strong>Hành vi:</strong> Không kéo dài ca làm tự ý, không thay đổi tuyến đường, và thực hiện nghiêm checklist.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8085-b1e0-c4d97abedf92" class="">7. ĐỂ Ý TỪNG CHI TIẾT NHỎ</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80e0-98aa-f7499df90e4a" class="bulleted-list"><li style="list-style-type:disc"><strong>Chuẩn:</strong> Nhận biết những điều nhỏ nhặt mà khách không trực tiếp bày tỏ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80f6-b0c9-f19bbb4a1753" class="bulleted-list"><li style="list-style-type:disc"><strong>Ý nghĩa:</strong> Những chi tiết nhỏ tạo nên <strong>khác biệt lớn</strong> trong <strong>trải nghiệm</strong> của khách hàng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-802b-bc3a-dd1149af0d70" class="bulleted-list"><li style="list-style-type:disc"><strong>Hành vi:</strong> Nhắc khách kiểm tra đồ đạc, báo trước đoạn đường xóc, hỗ trợ mở cửa khi cần, và chú ý đến mùi, ánh sáng cũng như âm lượng trong xe.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8090-83ad-c1027f47d97e" class="">8. 
TỰ HÀO KHI MẶC ĐỒNG PHỤC UNITAXI</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80c9-b325-dd43d9f517d0" class="bulleted-list"><li style="list-style-type:disc"><strong>Chuẩn:</strong> Ăn mặc sạch sẽ, gọn gàng, mang phong thái <strong>tự trọng</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ca-b220-d0e8076c6767" class="bulleted-list"><li style="list-style-type:disc"><strong>Ý nghĩa:</strong> Đồng phục chính là <strong>hình ảnh thương hiệu</strong>, và bạn là gương mặt đại diện của Unitaxi.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8069-bc91-ee9ad75e430d" class="bulleted-list"><li style="list-style-type:disc"><strong>Hành vi:</strong> Giữ áo quần phẳng phiu, giày dép sạch sẽ, tư thế đứng, đi và mở cửa thể hiện rõ <strong>sự chuyên nghiệp</strong>.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80db-9940-ed010b13853c" class="">💛 ĐÂY LÀ “DNA CỦA UNITAXI”</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-803a-985c-e9bb48024399" class="">Không chỉ là khẩu hiệu hay hình thức, đây là bộ khung <strong>tác phong</strong> mà mỗi thành viên phải duy trì mỗi ngày. Nhờ đó, Unitaxi trở thành dịch vụ được khách <strong>tin tưởng</strong>, <strong>lựa chọn</strong> và <strong>giới thiệu</strong>, khẳng định vị thế trên thị trường.</p></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-80b8-9622-fb3119d8977e"/></div><div style="display:contents" dir="auto"><h1 id="2aec5e6f-95bd-80dc-a294-e8d3ca338cea" class=""><strong>📖 Hình ảnh &amp; đồng phục</strong></h1></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-805a-bc2e-f381d0b1796b" class="">Bạn chính là hình ảnh đại diện của Unitaxi. Mỗi khi khách bước lên xe, họ chỉ thấy bạn – không thấy công ty hay hệ thống. 
Vì vậy, <strong>tác phong</strong>, <strong>đồng phục</strong>, và <strong>cách bạn xuất hiện</strong> chính là thương hiệu sống động của Unitaxi.</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-803a-80c1-dedcecea3c08" class="bulleted-list"><li style="list-style-type:disc"><strong>1. Đồng phục sạch sẽ – Gọn gàng:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80d9-802d-e3b522bc41f5" class="bulleted-list"><li style="list-style-type:circle">Giữ áo quần phẳng phiu, không nhăn, không ố bẩn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80fa-b94d-f64e332e5653" class="bulleted-list"><li style="list-style-type:circle">Tuân thủ màu sắc quy định, không tự ý thay đổi.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8096-8426-d825b99f10bf" class="bulleted-list"><li style="list-style-type:circle">Phải mặc quần dài màu tối để đảm bảo tính chuyên nghiệp và sạch sẽ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80db-bde6-f4c1b2dce46a" class="bulleted-list"><li style="list-style-type:circle">Tránh mặc áo khoác che đồng phục khi chở khách (trừ trường hợp trời lạnh).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8019-938f-ccffed360e74" class=""><strong>Lý do:</strong> Bề ngoài gọn gàng tạo cảm giác <strong>tin tưởng</strong> ngay từ giây đầu tiên.</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8039-a5d3-e70d7a710637" class="bulleted-list"><li style="list-style-type:disc"><strong>2. 
Giày khô ráo – Không dép lê:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80b9-9f9e-e2a5238aac91" class="bulleted-list"><li style="list-style-type:circle">Sử dụng giày hoặc giày thể thao sạch sẽ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8019-93ab-e8eb9b46bdaa" class="bulleted-list"><li style="list-style-type:circle">Không mang dép lê, dép tổ ong, hoặc dép kẹp.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80d9-9837-e42348313f62" class=""><strong>Lý do:</strong> Giày thể hiện <strong>chuyên nghiệp</strong>, trong khi dép dễ khiến khách cảm thấy thiếu <strong>nghiêm túc</strong>.</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8060-8c7a-ce8a4d0f4095" class="bulleted-list"><li style="list-style-type:disc"><strong>3. Tóc – Cơ thể – Mùi hương:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8044-91df-f34bcf2bb0f0" class="bulleted-list"><li style="list-style-type:circle">Tóc được cắt gọn, không rối, không che mắt.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8037-b182-d02fce3a8c1e" class="bulleted-list"><li style="list-style-type:circle">Không dùng nước hoa nồng; ưu tiên mùi nhẹ hoặc không mùi.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80b7-b613-f679dee467fd" class="bulleted-list"><li style="list-style-type:circle">Tránh để mùi cơ thể, mùi thuốc lá, hoặc mùi đồ ăn bám vào người hay xe.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-802f-a16c-d07ffd36cb6c" class=""><strong>Lý do:</strong> Mùi hương là yếu tố nhạy cảm nhất; một lần khó chịu có thể khiến khách không quay lại.</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80d0-8d01-d71679ffa39f" class="bulleted-list"><li style="list-style-type:disc"><strong>4. 
Tác phong khi đứng – Đi – Mở cửa:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8015-a1b0-cad46530a58e" class="bulleted-list"><li style="list-style-type:circle">Đứng thẳng, không dựa hoặc lom khom khi giao tiếp với khách.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80d7-b029-d48d84a42af8" class="bulleted-list"><li style="list-style-type:circle">Khi khách lên/xuống xe: mở cửa nhẹ nhàng, tránh tiếng động mạnh.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8021-9472-cf86a9198ff6" class="bulleted-list"><li style="list-style-type:circle">Nhường đường cho khách, không đứng chắn lối đi.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8040-86d3-eb8f06ef6ce4" class=""><strong>Lý do:</strong> Dáng đứng và cách mở cửa là “ngôn ngữ im lặng” thể hiện <strong>tôn trọng</strong>. Khi bạn xuất hiện chỉnh chu, tự tin, và đúng tác phong, khách hàng tự nhiên đáp lại bằng sự <strong>lịch sự</strong> và <strong>tin tưởng</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-80c5-b486-ff6c47f6bae8"/></div><div style="display:contents" dir="auto"><h1 id="2aec5e6f-95bd-80bf-a027-e0c276621698" class=""><strong>📖 Xe sạch = Khách dễ chịu</strong></h1></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-808c-84d9-d2be05120297" class="">Một chiếc xe sạch, thoáng, không mùi chính là ấn tượng đầu tiên — và thường là ấn tượng mạnh nhất. 
Trước mỗi ca, bạn chỉ cần <strong>1 phút</strong> để kiểm tra:</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8042-8b8c-dd39ed44c414" class="bulleted-list"><li style="list-style-type:disc"><strong>Ghế &amp; thảm sạch</strong>, không bụi, không vụn đồ ăn</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8023-abc3-fba7cdb18893" class="bulleted-list"><li style="list-style-type:disc"><strong>Không có mùi lạ</strong>: thuốc lá, mồ hôi, đồ ăn, ẩm mốc</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80aa-ae83-df9820045c73" class="bulleted-list"><li style="list-style-type:disc"><strong>Nước suối còn đủ</strong> (nếu công ty cho phép cung cấp)</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80f6-ba2d-f87b832a9c21" class="bulleted-list"><li style="list-style-type:disc"><strong>Có khăn giấy</strong> để khách dùng khi cần</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80c7-b620-c161914a4e51" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều hoà mát nhẹ</strong>, không quá lạnh, không thổi thẳng vào khách</li></ul></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-803a-b65b-da30f7a80f9a" class=""><strong>Khách bước lên xe và thấy dễ chịu ngay lập tức → 80% ấn tượng tốt đã hình thành. 
</strong>Họ cảm nhận được sự chuyên nghiệp, sự tôn trọng và sự chuẩn mực từ bạn.</p></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80ee-b5be-c0af3df12547" class=""><strong>📌 Checklist vệ sinh nhanh 30 giây giữa các chuyến</strong></h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80fa-9e17-cd9d270a953b" class="">Chỉ cần <strong>30 giây</strong> để giữ xe sạch – gọn – dễ chịu:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-80bc-9015-e3bd543bd6e7" class="numbered-list" start="1"><li><strong>Miết nhanh tay lên ghế</strong> → kiểm tra bụi, vụn bánh, tóc.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8086-b34d-fa7074113a30" class="numbered-list" start="2"><li><strong>Phủi thảm sàn</strong> → đá nhẹ ra ngoài nếu có rác nhỏ.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8089-846c-ee63e5a638a3" class="numbered-list" start="3"><li><strong>Nhặt rác ngay</strong>: vỏ kẹo, khăn giấy, chai nước.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-808b-a504-fc281ffacf79" class="numbered-list" start="4"><li><strong>Mở cửa 5–10 giây</strong> → đổi không khí nếu xe còn mùi.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8095-9b2e-fc8e0b4ee97d" class="numbered-list" start="5"><li><strong>Kiểm tra điều hoà</strong> → mát nhẹ, không thổi trực tiếp vào ghế sau.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-80f4-949f-f83cea1c8594" class="numbered-list" start="6"><li><strong>Sắp lại ghế &amp; 
dây an toàn</strong> về đúng vị trí.</li></ol></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80a4-b882-d3ebabf21eca" class="">➡ Xe sạch → khách dễ chịu → tài xế tự tin → hành trình êm.</p></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-808e-b085-f4100ebe72af" class=""><strong>📌 Quy chuẩn mùi – ánh sáng – âm lượng trong xe</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8016-95b8-ddcea4d52aed" class=""><strong>1. Mùi trong xe</strong></h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8007-8b4c-fe3373dc3a89" class="bulleted-list"><li style="list-style-type:disc">Không dùng nước hoa nồng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8081-968e-d3ae86bdb8cb" class="bulleted-list"><li style="list-style-type:disc">Không mùi thuốc lá, đồ ăn, mồ hôi.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-804c-8d4b-c5e6dd0b0425" class="bulleted-list"><li style="list-style-type:disc">Ưu tiên mùi <strong>trung tính</strong> hoặc <strong>không mùi</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8006-960d-d7f4411ff757" class="bulleted-list"><li style="list-style-type:disc">Nếu có khách trước làm xe có mùi → mở cửa 20–30 giây + chỉnh gió nhẹ.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8063-aafa-dbc2a527c245" class=""><strong>2. 
Ánh sáng</strong></h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-809c-b964-f20135757637" class="bulleted-list"><li style="list-style-type:disc">Ban ngày: giữ ánh sáng tự nhiên, không mở đèn cabin không cần thiết.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80e4-82fb-ca9e3d4a2484" class="bulleted-list"><li style="list-style-type:disc">Ban đêm: mở đèn cabin khi khách lên/xuống xe, sau đó tắt.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-807a-bf5a-d72a98a63ab4" class="bulleted-list"><li style="list-style-type:disc">Tránh ánh sáng xanh hoặc đèn nháy gây khó chịu.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80ad-a4c4-db6f88f7e34b" class=""><strong>3. 
Âm lượng</strong></h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8085-9917-c46a88b1e19b" class="bulleted-list"><li style="list-style-type:disc">Nhạc <strong>nhẹ – nhỏ – không lời</strong> (nếu mở).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80c9-88e4-d4f39f4ae0f7" class="bulleted-list"><li style="list-style-type:disc">Không mở radio, talk show, hài kịch, tin tức gây tranh luận.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80e5-a619-d5ee84c70159" class="bulleted-list"><li style="list-style-type:disc">Không mở video/nhạc riêng tư khi khách còn trên xe.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80bf-b1db-e787f949cb1d" class="bulleted-list"><li style="list-style-type:disc">Mức âm lượng chuẩn: <strong>khách ngồi sau vẫn nghe rõ trong im lặng</strong>.</li></ul></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-802a-b22f-e109f7414a56" class="">Mùi – ánh sáng – âm lượng ổn định giúp khách <strong>dễ chịu 70%</strong> mà không cần nói nhiều.</p></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8013-b05e-ee53668f5d95" class=""><strong>📌 Tiêu chuẩn dọn xe cuối ca (3 phút)</strong></h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-806b-a4a1-dc246a2ad3aa" class="">Mỗi ca kết thúc, dành đúng <strong>3 phút</strong>:</p></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80b5-99d0-d627dc2e7932" class=""><strong>Phút 1 – Thu gom &amp; 
kiểm tra</strong></h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8051-8c43-fefb7f350aa4" class="bulleted-list"><li style="list-style-type:disc">Nhặt toàn bộ rác: chai nước, giấy, bao bì.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8045-8fdf-f65e66c114cc" class="bulleted-list"><li style="list-style-type:disc">Kiểm tra đồ khách để quên → báo điều phối ngay.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8017-aa24-ff5fdae71f80" class=""><strong>Phút 2 – Vệ sinh nhanh</strong></h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-805f-97cb-f6ace51d2a16" class="bulleted-list"><li style="list-style-type:disc">Phủi thảm sàn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80a1-8ba0-d1ccfcb6981c" class="bulleted-list"><li style="list-style-type:disc">Lao nhẹ bảng taplo &amp; 
tay nắm cửa.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-802c-8ffb-f768aa6ec020" class="bulleted-list"><li style="list-style-type:disc">Dùng khăn ẩm lau vết bẩn (nếu có).</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-801e-880f-ef373c639863" class=""><strong>Phút 3 – Khôi phục trạng thái chuẩn</strong></h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80e0-9699-e7b250e0b020" class="bulleted-list"><li style="list-style-type:disc">Đưa ghế về vị trí đẹp.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80bb-9c3e-f9158d7b0850" class="bulleted-list"><li style="list-style-type:disc">Kiểm tra mùi → mở cửa 10 giây nếu cần.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80d7-9598-c8f61571533d" class="bulleted-list"><li style="list-style-type:disc">Kiểm tra điều hoà – tắt đúng chế độ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8067-ac48-f42b1cf4ad7f" class="bulleted-list"><li style="list-style-type:disc">Sạc lại xe (nếu ca yêu cầu).</li></ul></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-805a-9ce5-f5c7ff905610" class="">Xe sạch cuối ca → <strong>bắt đầu ca sau với trạng thái 100%</strong> → giảm stress → tăng hiệu quả làm việc.</p></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-8077-82db-e1103723ba28"/></div><div style="display:contents" dir="auto"><h1 id="2aec5e6f-95bd-800d-b630-d001d5dd3a8c" class=""><strong>📖 Những điều tuyệt đối không làm</strong></h1></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-808b-bee2-f01f6db5f3fd" class="">Các hành vi dưới đây <strong>tuyệt đối không được phép</strong>, dù trong bất kỳ hoàn cảnh nào. Chúng gây nguy hiểm, làm mất niềm tin của khách và tổn hại trực tiếp đến hình ảnh Unitaxi.</p></div><div style="display:contents" dir="auto"><h2 id="2aec5e6f-95bd-8012-8dd4-cb05dbcf1e8e" class=""><strong>1. 
An toàn &amp; Lái xe</strong></h2></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-806b-8880-ff29c928c313" class=""><strong>❌ Không phanh gấp – đánh lái mạnh </strong>→ Gây say xe, nguy hiểm cho khách, ảnh hưởng đánh giá.</p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-800e-b9aa-ef3f63e5d9f7" class=""><strong>❌ Không vượt đèn đỏ – đèn vàng </strong>→ Ảnh hưởng an toàn và pháp lý.</p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-803c-a2e6-eb8388052715" class=""><strong>❌ Không lái xe khi buồn ngủ, mệt, hoa mắt </strong>→ Nếu có dấu hiệu xuống sức → dừng ca / xin đổi ca.</p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-803c-9b7b-e2f235c84317" class=""><strong>❌ Không vừa lái vừa làm việc riêng </strong>→ Không đọc tin nhắn, không xem video, không chỉnh mạng xã hội.</p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80de-8b45-ed66a85e9fcb" class=""><strong>❌ Không lái xe khi đã sử dụng rượu bia, thuốc lá điện tử, chất kích thích.</strong></p></div><div style="display:contents" dir="auto"><h2 id="2aec5e6f-95bd-8033-8a5c-d93995677994" class=""><strong>2. Điện thoại &amp; Thiết bị cá nhân</strong></h2></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80c8-8e9b-d549049f3203" class=""><strong>❌ Không sử dụng điện thoại cá nhân khi xe đang di chuyển </strong>→ Chỉ được phép dùng <strong>app điều phối</strong>.</p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-803d-8c2f-dc16f1698d7f" class=""><strong>❌ Không cầm máy, trả lời cuộc gọi riêng khi có khách </strong>→ Nếu bắt buộc → xin phép khách.</p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-809e-a219-eb6b3a5ab2ba" class=""><strong>❌ Không cắm sạc – cắm loa tùy tiện gây vướng víu.</strong></p></div><div style="display:contents" dir="auto"><h2 id="2aec5e6f-95bd-8031-8f82-c90a143223e9" class=""><strong>3. 
Giao tiếp &amp; Ứng xử</strong></h2></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8034-841a-d9e8fa54e780" class=""><strong>❌ Không tranh cãi với khách </strong>→ Nếu khách căng thẳng → giữ giọng nhẹ – chuyển cho điều phối.</p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8003-a667-caea843acb38" class=""><strong>❌ Không nói tục, không dùng từ xúc phạm </strong>→ Dù khách sai → tài xế luôn phải giữ chuẩn.</p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-804d-ab1f-e0e519592348" class=""><strong>❌ Không bình luận về giới tính, tôn giáo, gia đình, tiền bạc </strong>→ Chuẩn quốc tế cấm tuyệt đối.</p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80e9-b887-dadcc1c8dbd0" class=""><strong>❌ Không hỏi chuyện riêng tư khi khách không chủ động chia sẻ.</strong></p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-807c-992d-e637e459abf9" class=""><strong>❌ Không tỏ thái độ, thở dài, liếc nhìn bực bội.</strong></p></div><div style="display:contents" dir="auto"><h2 id="2aec5e6f-95bd-80b1-bf92-e926e3413db5" class=""><strong>4. 
Âm thanh – mùi – môi trường trong xe</strong></h2></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80d3-90c7-d422cadfccab" class=""><strong>❌ Không hút thuốc, kể cả khi xe không có khách </strong>→ Mùi thuốc lưu trên ghế, áo → khách đánh giá xấu ngay lập tức.</p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8093-80ab-f5b1f61fd7ff" class=""><strong>❌ Không mở nhạc ồn, nhạc lời, nhạc remix </strong>→ Chuẩn quốc tế: <strong>music off hoặc nhạc nhẹ – nhỏ – không lời</strong>.</p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8092-b503-c1f378641a05" class=""><strong>❌ Không mở radio thời sự/hài kịch có nội dung gây kích động.</strong></p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80cf-8aae-f06bcc24b739" class=""><strong>❌ Không bật đèn cabin liên tục gây khó chịu.</strong></p></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-80c9-b592-ccdffa947301"/></div><div style="display:contents" dir="auto"><h2 id="2aec5e6f-95bd-80fd-8338-d458de63bf6f" class=""><strong>5. 
Hình ảnh &amp; Tác phong</strong></h2></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-809c-92f9-c0ec05b4630b" class=""><strong>❌ Không mặc quần đùi, dép lê, áo nhàu, áo ướt</strong></p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80a5-a83d-cfb25d3884b5" class=""><strong>❌ Không để lộ hình xăm lớn (nếu có → che lại theo chuẩn quốc tế).</strong></p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-802f-9e24-d45b02fa6840" class=""><strong>❌ Không để xe bẩn: bụi, rác, chai nước cũ.</strong></p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80fb-b8cb-d2c85b567754" class=""><strong>❌ Không để mùi cơ thể, mùi thức ăn, mùi thuốc lá trong xe.</strong></p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80bf-a247-fa7669484d31" class=""><strong>❌ Không mang thức ăn có mùi nặng lên xe.</strong></p></div><div style="display:contents" dir="auto"><h2 id="2aec5e6f-95bd-807f-ad78-f41c97ed749c" class=""><strong>6. Quy trình &amp; Dữ liệu</strong></h2></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8006-a2fb-e7bbeeac568a" class=""><strong>❌ Không tự ý thay đổi tuyến để tăng tiền </strong>→ Tối kỵ, vi phạm đạo đức nghề nghiệp toàn cầu.</p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-805c-b5fa-e82808dd57c4" class=""><strong>❌ Không tắt app, không hủy cuốc tùy tiện </strong>→ Gây mất niềm tin hệ thống.</p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8080-afa4-f80f5198f755" class=""><strong>❌ Không báo sai tình trạng pin, nhiên liệu, sự cố.</strong></p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8059-a04d-df5624ae3801" class=""><strong>❌ Không giao tiếp qua voice/chat nội bộ bằng ngôn từ thiếu chuẩn.</strong></p></div><div style="display:contents" dir="auto"><h2 id="2aec5e6f-95bd-8013-97e8-d5e741727139" class=""><strong>7. 
Hành vi rủi ro cao </strong></h2></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80db-80e9-cfb74ed415d3" class="">Các hành vi dưới đây = <strong>chấm dứt hợp đồng ngay lập tức</strong> (theo chuẩn Grab/Uber):</p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80dc-bc5f-ef79c162733a" class=""><strong>❌ Sàm sỡ, đụng chạm không được phép</strong></p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8098-ad9d-e342deb3fade" class=""><strong>❌ Nhìn chằm chằm qua gương, cố tình quan sát cơ thể khách</strong></p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80d9-8654-ff6f1b5bfaa1" class=""><strong>❌ Gợi ý tình cảm, đùa nhạy cảm, lời nói hai nghĩa</strong></p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8065-8a63-d0243517c0bc" class=""><strong>❌ Lừa đảo, vòi tiền, gợi ý “tip”, gợi ý thanh toán ngoài app</strong></p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80ac-93cf-c81ff1720235" class=""><strong>❌ Bỏ khách giữa đường không lý do</strong></p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-802f-a73e-e0afd390b4c2" class=""><strong>❌ Cố tình đe dọa, quát nạt, 
gây áp lực tâm lý</strong></p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8051-88ce-da15732269f0" class=""><strong>❌ Giữ đồ khách hoặc không trả lại khi biết khách quên</strong></p></div><div style="display:contents" dir="auto"><h1 id="2aec5e6f-95bd-8085-957c-c88051a9bba1" class=""><strong>🎯 Kết luận</strong></h1></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80cb-8ec8-d27570a549ab" class="">“Những điều tuyệt đối không làm” là <strong>rào chắn bảo vệ</strong>:</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-803d-a500-cd0eff66fbc5" class="bulleted-list"><li style="list-style-type:disc"><strong>An toàn của khách</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-806e-aead-f573f2ab0446" class="bulleted-list"><li style="list-style-type:disc"><strong>Uy tín của Unitaxi</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80a9-a982-fcb403354e54" class="bulleted-list"><li style="list-style-type:disc"><strong>Nghề nghiệp và thu nhập của chính bạn</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80fa-8dd6-e75787eb9dac" class="">Không chỉ phục vụ khách, chúng ta <strong>đại diện cho thương hiệu</strong>. 
Một hành vi sai có thể phá hỏng hàng ngàn hành vi đúng.</p></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-80f7-b8c3-e69adcc70a07"/></div><div style="display:contents" dir="auto"><h1 id="2aec5e6f-95bd-8096-95ab-d20692f09543" class=""><strong>📖 Khi nhận cuốc</strong></h1></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8097-88ad-cce2dc99f18b" class=""><strong>Mục tiêu của Unitaxi:</strong> Tạo cảm giác <strong>an tâm</strong>, <strong>rõ ràng</strong>, không bị <strong>bỏ rơi</strong> cho khách ngay phút đầu, dựa trên nguyên tắc quốc tế: <strong>ngắn</strong>, <strong>rõ</strong>, <strong>trấn an</strong> (theo chuẩn Uber, Lyft, Grab, Bolt).</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8018-93dd-e5842a82b567" class="bulleted-list"><li style="list-style-type:disc"><strong>Nhắn tin xác nhận:</strong> “Em đang đến, khoảng 2 phút nữa tới ạ.” (Giảm lo lắng, chuẩn bắt buộc Unitaxi).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80d6-9fe4-d6504a624a6d" class="bulleted-list"><li style="list-style-type:disc"><strong>Trời mưa:</strong> “Em mang ô ra đón anh/chị cho đỡ ướt.” (<strong>Tử tế đúng lúc</strong>).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ae-9369-eb6628a7c4a9" class="bulleted-list"><li style="list-style-type:disc"><strong>Điểm đón khó:</strong> “Em đứng cạnh cột số 3, phía trước cửa hàng tiện lợi ạ.” (Mốc nhận diện chuẩn quốc tế).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80a5-b95b-f289ed7323f9" class="bulleted-list"><li style="list-style-type:disc"><strong>Tắc đường:</strong> “Đoạn này hơi kẹt, em đến trễ 1–2 phút, mong anh/chị thông cảm.” (Chuẩn thông báo quốc tế).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8083-91a7-efe68a8c4fa8" class="bulleted-list"><li style="list-style-type:disc"><strong>Buổi tối:</strong> “Em đang vào, 
anh/chị đứng ở chỗ sáng giúp.” (Quy tắc an toàn, ưu tiên khách nữ/một mình).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8042-b033-dc1969f4028a" class="bulleted-list"><li style="list-style-type:disc"><strong>Gọi không được:</strong> “Em thấy anh/chị gọi, em đang tới sát điểm đón.” (Phản hồi trong 5–10 giây).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80f1-b95f-e40c654558bb" class="bulleted-list"><li style="list-style-type:disc"><strong>Đón học sinh:</strong> “Em sắp đến cổng trường, khoảng 2 phút nữa ạ.” (Cập nhật cho phụ huynh).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-804e-b2ed-d952802d0567" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách lớn tuổi:</strong> “Anh/chị cứ ra từ từ, em chờ được.” (<strong>Tôn trọng</strong>, không thúc ép).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80df-84f1-eae6f8285932" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách nhiều hành lý:</strong> “Em hỗ trợ để hành lý vào cốp nhé.” (Hỗ trợ vừa đủ).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8091-a4d4-daad424a9311" class="bulleted-list"><li style="list-style-type:disc"><strong>Đón tại chung cư:</strong> “Em đứng ở sảnh B, ngay chỗ bảo vệ ạ.” (Giảm nhầm lẫn).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8015-aa4e-f916d4dced27" class="bulleted-list"><li style="list-style-type:disc"><strong>Khu vực nguy hiểm:</strong> “Em đứng trong khu vực an toàn ngay đầu hẻm.” (Không yêu cầu khách rủi ro).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8095-9ead-f271ed7a01cc" class="bulleted-list"><li style="list-style-type:disc"><strong>Trời nắng gắt:</strong> “Em đỗ chỗ mát, 
mời anh/chị ra từ từ.” (Chuẩn bảo vệ sức khỏe Nhật/Singapore).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-802d-a326-e8024ad8b1c5" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách đặt sai điểm:</strong> “Em đang ở A, nhưng anh/chị cần đón ở B đúng không ạ?” (Giảm huỷ cuốc).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80b7-8c2d-da9d9cb0db8c" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách loay hoay:</strong> Gọi 5 giây: “Em giơ tay rồi, anh/chị nhìn bên phải giúp.” (Hỗ trợ nhanh, trực quan).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8056-afab-fb95d2820e2d" class="bulleted-list"><li style="list-style-type:disc"><strong>Thời tiết xấu:</strong> “Anh/chị tranh thủ ra nhé, em đỗ sát cho tiện ạ.” (<strong>Chăm sóc tiêu chuẩn cao</strong>).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8026-810c-f618ea207a90" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách bế trẻ nhỏ:</strong> “Em tới sát cửa nhất có thể nhé.” (Giảm rủi ro).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-808f-a2fe-c1b2e223d431" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách đi với người lớn tuổi:</strong> “Em để xe sát lề nhất để ba/mẹ anh/chị lên cho an toàn.” (Hỗ trợ không chạm).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8036-9fc8-d3e36162ec63" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách vội:</strong> “Em đang tới rất gần, anh/chị yên tâm ạ.” (Giảm stress, 
giảm xung đột).</li></ul></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-80c7-96a9-e6bce890d6df"/></div><div style="display:contents" dir="auto"><h1 id="2aec5e6f-95bd-80dc-8439-c1d7298ea112" class=""><strong>📖  Khi khách bước lên xe</strong></h1></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80cf-b1c5-e5f219fe8a7c" class=""><strong>Mục tiêu:</strong> Trong 10 giây đầu, khách cảm nhận <strong>an toàn</strong>, <strong>dễ chịu</strong>, <strong>tôn trọng</strong>, <strong>chuyên nghiệp</strong> – tiêu chuẩn cơ bản của các hệ thống taxi công nghệ toàn cầu (Uber, Lyft, Bolt, Grab).</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80f8-8a52-e913d29624cd" class="bulleted-list"><li style="list-style-type:disc"><strong>Chào nhẹ – một câu – đúng mực:</strong> “Em chào anh/chị, mình đi tới X đúng không ạ?” (Lịch sự, không thừa lời, không áp lực).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80a0-805c-d4f40eb3477b" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều chỉnh nhiệt độ:</strong> “Điều hoà như vậy anh/chị thấy ổn chưa ạ?” (Kiểm tra thoải mái trong 5–10 giây).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8098-abc2-c17db4a602f7" class="bulleted-list"><li style="list-style-type:disc"><strong>Nhắc dây an toàn:</strong> “Anh/chị cài dây giúp em cho an toàn nhé.” (Nhẹ nhàng, không ra lệnh).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-801c-90f4-ec118354678d" class="bulleted-list"><li style="list-style-type:disc"><strong>Đóng cửa nhẹ:</strong> Không gây tiếng mạnh (Tạo cảm giác xe êm, tài xế <strong>tinh tế</strong>, <strong>an toàn</strong>).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-808c-b790-fea70ecb905f" class="bulleted-list"><li style="list-style-type:disc"><strong>Quan sát gương hậu:</strong> Nhìn 1–2 giây kiểm tra, 
không chằm chằm (Chuẩn mực: <strong>tinh tế</strong>, <strong>tôn trọng</strong>, không xâm lấn).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-803d-8de0-c47eab1bd382" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách mang đồ:</strong> “Em để đồ bên dưới/ghế sau giúp anh/chị cho an toàn nhé.” (Không chạm đồ trước khi xin phép).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8005-a6f1-c79ba178d39d" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách ướt mưa:</strong> “Em chỉnh ấm hơn chút cho anh/chị đỡ lạnh nhé.” (<strong>Quan tâm</strong> đúng lúc, đúng mức).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8070-b092-efc1a366fa68" class="bulleted-list"><li style="list-style-type:disc"><strong>Trẻ nhỏ ngủ:</strong> “Em nói nhỏ để bé ngủ ngon ạ.” (Thể hiện <strong>tinh tế</strong>, <strong>tôn trọng</strong> gia đình).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80db-a37b-dfe3a3d95e3e" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách bối rối/căng thẳng:</strong> “Anh/chị cứ ngồi thoải mái, mình đi ngay nhé.” (Giảm căng thẳng, hỗ trợ nhẹ).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8030-957b-fc668735cc38" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách đau chân/lưng:</strong> “Em chạy êm để anh/chị đỡ đau ạ.” (<strong>Tử tế</strong>, đúng chừng mực).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-806d-8066-c3fc418b9361" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách đeo balo/hành lý cồng kềnh:</strong> “Anh/chị tháo balo để trước cho thoải mái nhé.” (Gợi ý nhẹ, không ngượng).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80fd-9f68-df1b5d3b77b4" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách mệt/muốn nghỉ:</strong> Giữ im lặng, 
không bắt chuyện (<strong>tôn trọng</strong> cảm xúc).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-802f-b4ae-e3ee8a83094e" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách đóng cửa mạnh:</strong> Không phản ứng, chỉnh lại nhẹ nhàng (Chuẩn hành vi <strong>chuyên nghiệp</strong> quốc tế).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80de-8dc9-c1fbb980c36e" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều chỉnh xe quá lạnh/nóng:</strong> “Em chỉnh lại chút cho dễ chịu hơn nhé.” (Không đợi khách than phiền).</li></ul></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-8037-9a88-f31ed650f75c"/></div><div style="display:contents" dir="auto"><h1 id="2aec5e6f-95bd-804b-b880-d770b74e6102" class=""><strong>📖 Trong suốt chuyến đi</strong></h1></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80e0-a680-c401bb5b38bd" class=""><strong>Mục tiêu:</strong> Đảm bảo <strong>an toàn</strong>, <strong>dễ chịu</strong>, ổn định <strong>cảm xúc</strong> khách; giảm rủi ro <strong>xung đột</strong>; tạo cảm giác <strong>tinh tế</strong>, <strong>chuyên nghiệp</strong>, và biết <strong>quan sát</strong>. Khách đánh giá qua cảm giác cơ thể trên xe, không chỉ lời nói.</p></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-802f-aeb6-e663dfbf5737" class="">I. 
CHUẨN AN TOÀN &amp; 
ĐIỀU KHIỂN XE</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-808e-a005-f461fd183cb8" class="bulleted-list"><li style="list-style-type:disc"><strong>Lái êm – không phanh gấp – không đánh lái mạnh:</strong> Tiêu chuẩn số 1 quốc tế.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8062-b450-c64119ad65f6" class="bulleted-list"><li style="list-style-type:disc"><strong>Báo trước cua/đoạn xóc:</strong> “Đoạn này hơi xóc, em giảm tốc ạ.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80d5-8b24-cf4a3aa38800" class="bulleted-list"><li style="list-style-type:disc"><strong>Lái chậm qua vùng ngập:</strong> “Em đi chậm để tránh nước bắn lên ạ.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8063-8572-d403b8101c10" class="bulleted-list"><li style="list-style-type:disc"><strong>Đoạn nguy hiểm:</strong> Hạ tốc, báo: “Đoạn này hơi nguy hiểm, em giảm tốc cho an toàn nhé.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8094-84b5-ca56611ccd6e" class="bulleted-list"><li style="list-style-type:disc"><strong>Trẻ nhỏ say xe:</strong> Hạ kính nhẹ, chạy êm, hạn chế cua gấp.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-804d-9dbc-dca65836600d" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách say xe:</strong> Dừng an toàn nếu cần nghỉ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80b8-a13e-e50192a2ff68" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách lớn tuổi/phụ nữ mang thai:</strong> Tăng tốc từ từ, không giật ga.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-800c-b4a7-fb32680e36a1" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách bế trẻ sơ sinh:</strong> Điều hòa ấm nhẹ, 
không thổi trực tiếp.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-800e-bf57-fafc4249d30b" class="">II. CHUẨN GIAO TIẾP TINH TẾ</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8087-ae90-c9c20e4939d1" class="bulleted-list"><li style="list-style-type:disc"><strong>Không mở nhạc trước:</strong> Theo chuẩn Uber/Lyft (Music by preference only).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80af-b429-f4b15971d176" class="bulleted-list"><li style="list-style-type:disc"><strong>Nếu bật nhạc:</strong> Chọn nhạc nhẹ, âm lượng thấp, tránh EDM, remix, rock, bolero ồn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-800c-b6fc-f5d9c0b0f099" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách hỏi lộ trình:</strong> Giải thích ngắn, rõ, không tranh cãi.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80d5-aed5-e8ef7e13c1cc" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách lo lắng:</strong> Trấn an: “Đường này đi nhanh hơn anh/chị nhé.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-808b-9447-f6c3f4e99a29" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách ngủ:</strong> Im lặng tuyệt đối, quan sát 5 giây trước khi gọi nhẹ khi đến.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8087-8434-dc5967180c24" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách bấm điện thoại (căng thẳng):</strong> “Anh/chị yên tâm, còn khoảng X phút sẽ đến ạ.”</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8091-88ad-fdb0e4957c7c" class="">III. 
CHUẨN CHĂM SÓC TRONG HÀNH TRÌNH</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8059-948e-d78f3d85a6a4" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách mở cửa sổ:</strong> Nhắc tinh tế: “Anh/chị cho em xin khép bớt để bụi vào nhiều ạ.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80af-8205-e837ce92f580" class="bulleted-list"><li style="list-style-type:disc"><strong>Trời nắng chiếu thẳng:</strong> Đổi góc chạy giảm nắng (theo chuẩn Bolt).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80cb-b44e-ca5808548bff" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách ăn uống:</strong> Đưa khăn giấy, không tỏ thái độ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8050-9ad4-f1e76b93d27c" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách gọi quan trọng:</strong> Giảm tốc, im lặng, giữ khoảng cách an toàn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-806f-a177-f17ba2cb9149" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách mang vật cồng kềnh:</strong> Quan sát tránh va vào ghế/trần.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-809c-a61a-c10786baf2dd" class="">IV. 
CHUẨN XỬ LÝ TÌNH HUỐNG (INCIDENT STANDARDS)</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80a6-b4a4-cacd412a1b57" class="bulleted-list"><li style="list-style-type:disc"><strong>Ổ gà bất ngờ:</strong> “Em xin lỗi anh/chị, đoạn này em tránh không kịp.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80d1-84a0-f72263d5791d" class="bulleted-list"><li style="list-style-type:disc"><strong>Tai nạn/kỹ thuật nhỏ:</strong> Báo trước, hạ tốc, thao tác an toàn, không hoảng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80eb-8e1c-ed8b838cd011" class="bulleted-list"><li style="list-style-type:disc"><strong>Không nói xấu hãng/khác:</strong> Giữ hình ảnh trung lập, <strong>chuyên nghiệp</strong> (chuẩn quốc tế).</li></ul></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-8098-98f1-cfdd3c05878a"/></div><div style="display:contents" dir="auto"><h1 id="2aec5e6f-95bd-8095-b0c0-fc0f24b68e39" class=""><strong>📖 Chăm khách đặc biệt</strong></h1></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8089-a06c-f0038a4615c4" class="">Khách đặc biệt = những người có <strong>nhu cầu khác nhau</strong>, dễ nhạy cảm hơn, và cần được quan tâm đúng mực. Mục tiêu của Unitaxi: <strong>an toàn – tinh tế – không làm quá – không làm phiền</strong>. Chia theo 7 nhóm rõ ràng, dễ nhớ, không trùng lặp:</p></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-802c-a40d-e688dbca9938" class="">I. 
TRẺ NHỎ &amp; GIA ĐÌNH CÓ TRẺ</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8009-a3bb-f73ea89df802" class="bulleted-list"><li style="list-style-type:disc"><strong>Trẻ nhỏ say xe:</strong> Giảm tốc, chạy êm, hạn chế cua gấp, mở nhẹ cửa kính.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-805c-9d00-f08c98815832" class="bulleted-list"><li style="list-style-type:disc"><strong>Trẻ khóc:</strong> Mở nhạc thiếu nhi nhỏ (có đồng ý phụ huynh), giữ giọng nhẹ, không hỏi thêm.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ae-8ae9-f50589bf34dd" class="bulleted-list"><li style="list-style-type:disc"><strong>Trẻ nghịch cửa xe:</strong> Nhắc phụ huynh: “Anh/chị mình để ý giúp bé, cho an toàn ạ.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8013-afbf-cc23df72dcdd" class="bulleted-list"><li style="list-style-type:disc"><strong>Bé ngủ:</strong> Giảm tiếng ồn, tránh đánh lái mạnh, không nói lớn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ce-8a39-cb44fe5f915c" class="bulleted-list"><li style="list-style-type:disc"><strong>Gia đình nhiều đồ/xe nôi:</strong> Hỗ trợ mở cốp, xếp gọn tránh đổ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8093-a256-c20a9437d2f4" class="bulleted-list"><li style="list-style-type:disc"><strong>Phụ huynh căng thẳng:</strong> Giữ im lặng, lái êm để ổn định không khí.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80d2-a71c-d46f3517044a" class="">II. 
NGƯỜI LỚN TUỔI</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8092-8356-de06a3b43356" class="bulleted-list"><li style="list-style-type:disc"><strong>Người già – di chuyển chậm:</strong> Đỗ sát lề, chờ lên từ từ, mở cửa nhẹ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-809d-81db-c446301aed4f" class="bulleted-list"><li style="list-style-type:disc"><strong>Người vấn đề thăng bằng/đau chân:</strong> Lái thật êm, báo trước cua/phanh.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80c8-aaad-ff65eb0984ba" class="bulleted-list"><li style="list-style-type:disc"><strong>Người nghe kém:</strong> Nói chậm, rõ, không hét, lặp lại 1 lần nếu cần.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8037-8214-e1d77c868011" class="">III. PHỤ NỮ MANG THAI</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8066-8da9-e5f6bed12e05" class="bulleted-list"><li style="list-style-type:disc"><strong>Tránh đường xấu:</strong> Chọn đường êm hơn nếu được.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8024-83d0-de5fa7e46b18" class="bulleted-list"><li style="list-style-type:disc"><strong>Báo trước cua/phanh:</strong> “Em giảm tốc, chuẩn bị cua nhẹ nhé.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-804c-9435-c38db27895e3" class="bulleted-list"><li style="list-style-type:disc"><strong>Nhiệt độ xe:</strong> Không quá lạnh, điều chỉnh theo ý khách.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80b1-8b09-ddcd0db8273b" class="bulleted-list"><li style="list-style-type:disc"><strong>Hỗ trợ ra/vào:</strong> Mở cửa, quan sát, không chạm khách.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8030-bce0-e9bec84b894e" class="">IV. 
KHÁCH ĐI BỆNH VIỆN – NGƯỜI YẾU</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80d4-a9ec-e9d1bd19b7f8" class="bulleted-list"><li style="list-style-type:disc"><strong>Giữ im lặng:</strong> Chỉ nói khi cần (tiêu chuẩn quốc tế nhóm nhạy cảm).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8032-a16e-e45ea5bdd3fe" class="bulleted-list"><li style="list-style-type:disc"><strong>Lái êm tuyệt đối:</strong> Không thắng gấp, tăng tốc mạnh, tránh rung lắc.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80b2-9f2a-d58d1a26f7fc" class="bulleted-list"><li style="list-style-type:disc"><strong>Dừng sát cửa:</strong> Hỗ trợ an toàn, tránh đường gập ghềnh.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8082-83ab-fcf0ca796eb1" class="bulleted-list"><li style="list-style-type:disc"><strong>Người chăm bệnh căng thẳng:</strong> Trả lời ngắn, không hỏi riêng tư.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-800d-bac3-c06e04e5d905" class="">V. 
KHÁCH CÓ TÂM TRẠNG ĐẶC BIỆT</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-805c-bb58-fd7a9413f09a" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách khóc/buồn/mệt:</strong> Không hỏi “Có chuyện gì?”, giữ im lặng giảm áp lực.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-808e-855c-dae36c6f69e6" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách nóng tính:</strong> Hạ giọng, dùng câu: “Anh/chị thông cảm, em xử lý ngay ạ.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-806a-9b0e-f01bde712ec4" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách uống rượu:</strong> Không tranh luận, tỏ thái độ, giữ cửa an toàn khi xuống.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80b2-a417-dcb63026db8d" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách nói điện thoại lớn:</strong> Không phản ứng, lái êm tránh va chạm.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8009-908e-c2ad9e951509" class="">VI. 
KHÁCH CÓ YÊU CẦU ĐẶC BIỆT</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80d9-aafc-d40ea93e2a98" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách nhiều hành lý/đồ dễ vỡ:</strong> Đặt cốp riêng, báo: “Em mở cốp, anh/chị kiểm tra giúp ạ.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8044-ad59-f8f6fe91ae95" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách mang thú cưng:</strong> Trải khăn (nếu có), giữ mùi dễ chịu, không tỏ thái độ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8058-98ee-e83f048038b5" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách nghe nhạc riêng:</strong> Chuyển Bluetooth/USB, giữ âm lượng an toàn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8092-ad7a-ec0f3b88f73c" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách ăn uống:</strong> Đưa khăn giấy, không phàn nàn, giữ thái độ trung tính.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8082-a228-cb923cabe238" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách chụp ảnh/video:</strong> Giảm tốc/dừng đúng luật theo yêu cầu.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8042-9bbf-ef8b1ac2ad58" class="">VII. 
KHÁCH CÓ NHU CẦU VỀ THỜI GIAN</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8094-9a3b-ecda87cb081e" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách rất vội:</strong> Chạy nhanh trong giới hạn an toàn: “Em cố gắng tối đa trong mức an toàn ạ.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8000-b27f-e9ce1260393e" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách kiểm tra đồng hồ:</strong> Báo thời gian: “Khoảng X phút nữa tới ạ.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ea-af5b-c21653944392" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách đi sân bay:</strong> Nhắc nhẹ: “Giờ này mình vẫn kịp chuyến, anh/chị yên tâm.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8092-86a4-ea786da842f0" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách ghé thêm điểm:</strong> Xác nhận minh bạch: “Dạ được anh/chị, em cập nhật ứng dụng cho rõ ràng ạ.”</li></ul></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-8094-ae59-ca7279a3faae"/></div><div style="display:contents" dir="auto"><h1 id="2aec5e6f-95bd-8061-94f6-ea1c1f2537cd" class=""><strong>📖 Trước khi khách xuống xe</strong></h1></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8086-9b1b-c334bc32e319" class=""><strong>Mục tiêu:</strong> Đảm bảo <strong>an toàn tuyệt đối</strong>, kết thúc chuyến xe với cảm giác <strong>dễ chịu</strong>, và duy trì <strong>hình ảnh chuyên nghiệp</strong> đến giây cuối.</p></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80af-a612-d67c3b67ab95" class="">I. 
NHẮC KIỂM TRA TÀI SẢN CÁ NHÂN</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80cd-bc67-c5d6a8ddfd11" class="bulleted-list"><li style="list-style-type:disc"><strong>Nhắc đồ cá nhân:</strong> “Anh/chị kiểm tra giúp ví – điện thoại – chìa khoá nhé.” (Tiêu chuẩn toàn cầu, giảm 80% quên đồ).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ac-b7eb-ecb76570961b" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách có túi/giỏ nhỏ:</strong> “Anh/chị xem giỏ/túi còn gì không ạ.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-800e-ac5a-d5b46ac7ce8b" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách dùng laptop/máy ảnh:</strong> “Anh/chị nhớ lấy laptop/máy ảnh giúp em nhé.”</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80ec-b0a4-d79a24082b53" class="">II. DỪNG XE ĐÚNG VỊ TRÍ AN TOÀN</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8035-b4c9-d307e3af385e" class="bulleted-list"><li style="list-style-type:disc"><strong>Dừng sát lề:</strong> Không dừng giữa làn (quy định quốc tế).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8057-986a-d10ebe846019" class="bulleted-list"><li style="list-style-type:disc"><strong>Tránh đoạn cua/khu vực thiếu tầm nhìn:</strong> Nếu buộc phải dừng, nói: “Em dừng ở đây an toàn nhất rồi ạ.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8092-b969-edd11838a6a2" class="bulleted-list"><li style="list-style-type:disc"><strong>Địa điểm tối/hẻm nhỏ:</strong> “Em đỗ sát cửa cho anh/chị xuống cho an toàn.”</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80f4-8d54-fa9b23b9d055" class="">III. 
TRỜI MƯA – THỜI TIẾT XẤU (CHUẨN WEATHER PROTOCOL)</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8076-98d7-fe9f78baac31" class="bulleted-list"><li style="list-style-type:disc"><strong>Trời mưa:</strong> Đưa ô, che 2–3 bước: “Để em che ô cho anh/chị một chút ạ.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-804b-a5bd-cc8030b1a4cb" class="bulleted-list"><li style="list-style-type:disc"><strong>Trời nắng gắt:</strong> “Em đỗ chỗ mát nhất có thể cho anh/chị xuống.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ce-8d36-c446a58074ba" class="bulleted-list"><li style="list-style-type:disc"><strong>Đường trơn:</strong> “Anh/chị xuống từ từ nhé, đường hơi trơn.”</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8057-b407-ef0c6be7cb32" class="">IV. HỖ TRỢ HÀNH LÝ – ĐÚNG MỰC</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8093-9d46-fdbc68e4bd81" class="bulleted-list"><li style="list-style-type:disc"><strong>Nhiều hành lý:</strong> “Để em hỗ trợ chuyển xuống cốp ạ.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8009-9409-ca575a1fd0d9" class="bulleted-list"><li style="list-style-type:disc"><strong>Đồ dễ vỡ:</strong> “Món này dễ vỡ đúng không ạ, em đặt nhẹ xuống cho an toàn.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8063-90a3-d3cfab646a1b" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách mang đồ ăn/nước uống:</strong> “Ly nước này anh/chị muốn giữ hay để em bỏ giúp ạ?”</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-808a-8ccc-ef39d9a590ed" class="">V. 
HÀNH VI THEO NHÓM KHÁCH ĐẶC BIỆT</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-808e-8251-e4e5f866f01e" class="bulleted-list"><li style="list-style-type:disc"><strong>Người lớn tuổi:</strong> “Anh/chị xuống từ từ ạ.” (Giữ cửa, quan sát).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8008-8513-f5153a5f1ab7" class="bulleted-list"><li style="list-style-type:disc"><strong>Phụ nữ mang thai:</strong> Dừng sát lề, báo: “Em mở cửa từ từ cho anh/chị xuống nhé.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8013-b9bb-c92a86fee1f8" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách có trẻ nhỏ:</strong> Quan sát bé xuống, không đóng cửa vội: “Bé xuống từ từ nha con.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80f1-9558-d131e66b2b3f" class="bulleted-list"><li style="list-style-type:disc"><strong>Trẻ nhỏ đang ngủ:</strong> Báo phụ huynh, mở cửa nhẹ: “Em mở cửa nhẹ cho bé không bị giật mình ạ.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8017-8f3d-e01ee4bc503a" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách đang ngủ:</strong> “Anh/chị ơi mình tới nơi rồi ạ.” (Giọng nhỏ, không đột ngột).</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8009-88b7-dc9bb639f51a" class="">VI. 
TÌNH HUỐNG THEO MỤC ĐÍCH CHUYẾN ĐI</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80b9-a2c8-d330a0f7215f" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách đi sân bay:</strong> “Dạ tới ga quốc nội/quốc tế của anh/chị rồi ạ.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ba-96ee-f04e233b30f7" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách đi họp/phỏng vấn:</strong> “Chúc anh/chị buổi làm việc thuận lợi ạ.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-804b-8a47-d483c6d3cb65" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách đi thăm bệnh:</strong> “Chúc anh/chị mọi việc suôn sẻ.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80fa-919d-d762e2fc7131" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách căng thẳng (mệt, lo):</strong> Không hỏi thêm, chỉ nói: “Mình tới nơi rồi anh/chị nhé, chúc anh/chị mọi chuyện tốt.”</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80e7-b9fc-d8c12067d27e" class="">VII. NHẮC NHỞ VỀ CỬA XE – AN TOÀN TUYỆT ĐỐI</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8087-afb1-e1665a94582d" class="bulleted-list"><li style="list-style-type:disc"><strong>Kiểm tra phía sau (trẻ/xe máy):</strong> Nếu nguy hiểm: “Anh/chị cho em mở từ từ để tránh xe máy ạ.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8031-852c-fd0242c03abc" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách mở cửa mạnh:</strong> Không phản ứng, giữ cửa nhẹ để an toàn.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-801f-9c2a-ce3ec2a80108" class="">VIII. 
KẾT THÚC CHUYẾN – ẤN TƯỢNG CUỐI</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80c2-ab2c-f7b754bf4aa9" class="bulleted-list"><li style="list-style-type:disc"><strong>Câu kết chuẩn:</strong> “Em cảm ơn anh/chị đã đi Unitaxi. Chúc anh/chị một ngày tốt lành.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-809c-9abd-fa7f3ed6b421" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách quen/từng gặp:</strong> “Rất vui được gặp lại anh/chị.” (Chuẩn “Professional Warmth” – không thân quá, không lạnh).</li></ul></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-80ed-b3fe-f019d2654252"/></div><div style="display:contents" dir="auto"><h1 id="2aec5e6f-95bd-80c7-a7e3-d44c11a23fc1" class=""><strong>📖  Sau chuyến</strong></h1></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80bf-9730-c3e6b476140f" class=""><strong>Mục tiêu:</strong> Kết thúc chuyến xe <strong>tử tế</strong>, <strong>rõ ràng</strong>, <strong>chuyên nghiệp</strong>; giữ <strong>hình ảnh thống nhất</strong> của hãng; tăng khả năng khách <strong>quay lại</strong>.</p></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8002-843e-dfcfb437f535" class="">I. 
TIN NHẮN CẢM ƠN NGẮN – ĐÚNG CHUẨN</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-809b-bb3b-ff41c38bcd67" class="bulleted-list"><li style="list-style-type:disc"><strong>Tin nhắn tiêu chuẩn:</strong> “Em cảm ơn anh/chị đã đi Unitaxi.” (Ngắn, trung tính, lịch sự – chuẩn Uber “Short gratitude message”).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8035-93ed-e5190e9b6f44" class="bulleted-list"><li style="list-style-type:disc"><strong>Chuyến đêm muộn:</strong> “Em cảm ơn anh/chị, về nhà an toàn ạ.” (Quan tâm, không quá thân).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-804d-9b8f-eaea24b76db7" class="bulleted-list"><li style="list-style-type:disc"><strong>Học sinh (báo phụ huynh):</strong> “Em đã đưa bé đến đúng điểm an toàn ạ.” (Quy định bắt buộc quốc tế).</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8096-93f8-e809f8080399" class="">II. 
XỬ LÝ ĐỒ THẤT LẠC – KHÔNG CHẬM TRỄ</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8054-8873-c34dd397e2d4" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách để quên đồ:</strong> “Anh/chị ơi, em vừa thấy có đồ rơi trong xe, em báo điều phối giữ hộ nhé.” (Không hỏi giá trị, không mở túi, không giữ riêng).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8042-84b6-fbc5d4b15a7b" class="bulleted-list"><li style="list-style-type:disc"><strong>Đồ giá trị cao (điện thoại, ví, giấy tờ):</strong> Báo điều phối trong 60 giây (Chuẩn Grab/Lyft “Immediate lost &amp; found alert”).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8008-ba58-c63da7c3cddc" class="bulleted-list"><li style="list-style-type:disc"><strong>Không liên hệ trực tiếp khách:</strong> Luôn qua điều phối để tránh hiểu lầm, đảm bảo <strong>minh bạch</strong>.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8069-8c8f-eecf5ad690e9" class="">III. VỆ SINH XE SAU CHUYẾN – 30 GIÂY</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80a9-907e-ef9defef18a4" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách để rác:</strong> Dọn ngay, nhắn nhẹ nếu phù hợp: “Em dọn giúp anh/chị luôn cho sạch xe ạ.” (Tinh tế, không phàn nàn).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80c1-a076-db2bafaf1693" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách ăn uống:</strong> Kiểm tra ghế, thảm, cốp; dọn nhanh cho chuyến sau.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80e2-a95c-e964934bbb89" class="">IV. 
XỬ LÝ PHẢN HỒI – GIỮ HÌNH ẢNH HÃNG</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-801f-9b7a-d5f30ea45a46" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách đánh giá tốt:</strong> “Em cảm ơn anh/chị đã đánh giá 5 sao ạ.” (Không emoji, giữ <strong>chuyên nghiệp</strong>).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80fd-b836-fe062b6e6716" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách phản hồi xấu:</strong> Không cãi, không giải thích dài; dùng câu mẫu: “Em ghi nhận ý kiến của anh/chị và báo điều phối xử lý ạ.” Sau đó, báo điều phối, mô tả rõ ràng, không cảm xúc.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80c7-a704-d9a47fdac5df" class="">V. BÁO CÁO VẬN HÀNH SAU CHUYẾN</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-802e-add2-d40e2ec5707e" class="bulleted-list"><li style="list-style-type:disc"><strong>Điểm đón nguy hiểm:</strong> Báo điều phối: “Điểm đón này hơi nguy hiểm, đề xuất đổi vị trí chuẩn.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-803c-8a75-f065a7fe911a" class="bulleted-list"><li style="list-style-type:disc"><strong>Khách có hành vi rủi ro (say xỉn, mở cửa bất ngờ, gây khó):</strong> Gửi báo cáo ngắn, không cảm tính.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80a6-bcca-ff5023e09a98" class="bulleted-list"><li style="list-style-type:disc"><strong>Khu vực tắc nghẽn bất thường:</strong> Báo để điều phối phân tuyến tốt hơn.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80bf-af6c-f59024b3a11f" class="">VI. 
KẾT THÚC CA VỚI TINH THẦN UNITAXI</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80b3-9b61-d6e4d75bb6b6" class="bulleted-list"><li style="list-style-type:disc"><strong>Báo cáo cuối ca:</strong> Kiểm tra tình trạng xe (mùi, điều hòa, thảm, ghế, mức điện/tiêu hao) để sẵn sàng ca sau.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8011-b413-cc01933db5fa" class="bulleted-list"><li style="list-style-type:disc"><strong>Kiểm tra đồ cá nhân:</strong> Tập <strong>kỷ luật</strong>, tránh thất lạc tài sản.</li></ul></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-80e0-b933-fef6cd5c9d11"/></div><div style="display:contents" dir="auto"><h1 id="2aec5e6f-95bd-801d-af50-ea6ce0702fb2" class=""><strong>📖 Khoảnh khắc nhỏ tạo ấn tượng tốt</strong></h1></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80d3-8910-c717fe831e71" class="">Trong dịch vụ vận chuyển, trải nghiệm khách hàng chỉ kéo dài vài phút, nhưng cảm xúc của họ được định hình bởi những chi tiết nhỏ nhất. Những khoảnh khắc ngắn ngủi, thường chỉ vài giây, đóng góp tới 80% ấn tượng tổng thể của cả chuyến đi. Dưới đây là lý do cụ thể, được xây dựng theo phương pháp MECE, giải thích rõ ràng và thuyết phục, phù hợp với văn phong doanh nghiệp Việt Nam.</p></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8016-b49f-ee04cf62b3f7" class="">1. 
KHOẢNH KHẮC ĐẦU VÀ CUỐI CÓ SỨC NẶNG LỚN NHẤT</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8099-911a-cd78557d27c0" class="">Theo chuẩn quốc tế, khách hàng ghi nhớ mở đầu, cao điểm và kết thúc – hiệu ứng “đỉnh – cuối”.</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80b8-9ccd-fb079af0c5a5" class="bulleted-list"><li style="list-style-type:disc">Một tin nhắn “Em đang tới” ngay lập tức mang lại sự <strong>an tâm</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-807c-92c0-d8e1f7fae655" class="bulleted-list"><li style="list-style-type:disc">Một câu “Anh/chị kiểm tra đồ giúp em nhé” tạo cảm giác <strong>được trân trọng</strong>.<br/>Hai thời điểm này định hình hầu hết cảm nhận của khách.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8078-bcb8-db3925abde8a" class="">2. KHÁCH VIỆT NHẠY CẢM VỚI THÁI ĐỘ HƠN BẤT KỲ YẾU TỐ NÀO</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80dd-aa4d-fa63abd8bc72" class="">Người Việt chú trọng cách đối xử hơn kết quả cuối cùng.</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-801d-b1a3-e8a651bde572" class="bulleted-list"><li style="list-style-type:disc">Chi tiết như mở cửa nhẹ khi mưa, điều chỉnh điều hòa theo ý khách, hay nói chậm, lịch sự tạo cảm giác <strong>được quan tâm</strong>, làm chuyến đi <strong>dễ chịu</strong> và đáng nhớ.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8036-b94d-ec2841da31e3" class="">3. 
HÀNH ĐỘNG NHỎ GIẢM CĂNG THẲNG TỨC THÌ</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80f9-a15d-c69b8db58220" class="">Khách thường trong trạng thái vội, mệt, lo lắng (đi sân bay, đón con, họp, đêm mưa, đi một mình).</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80e4-9628-db614e7a8b25" class="bulleted-list"><li style="list-style-type:disc">Cử chỉ đúng lúc như “Em đang đến, 2 phút nữa tới ạ”, “Để em mang ô ra đón anh/chị”, hay “Đoạn này hơi xóc, em giảm tốc nhé” chuyển cảm xúc khách sang trạng thái <strong>an toàn</strong> ngay lập tức.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8059-b356-e985be258aa5" class="">4. HÀNH ĐỘNG NHỎ TẠO AN TÂM, GIẢM XUNG ĐỘT</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80a3-ae58-ee3d17e07e73" class="">Khi khách cảm nhận được sự <strong>quan sát</strong> và <strong>chăm sóc</strong> đúng mực:</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8013-8126-f12cdb020005" class="bulleted-list"><li style="list-style-type:disc">Ít khó chịu, phàn nàn, gây căng thẳng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8040-91f8-f5d6c3e58a57" class="bulleted-list"><li style="list-style-type:disc">Dễ thông cảm nếu có chậm trễ.<br/>Điều này làm ca làm việc của tài xế nhẹ nhàng, giảm áp lực điều phối.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-803e-9635-f4830fc9c4c7" class="">5. 
TỬ TẾ ĐÚNG LÚC LAN TRUYỀN MẠNH MẼ</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-807c-afa1-ffecdad08d98" class="">Hành động nhỏ đúng cách tạo:</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-802a-bf72-d9f110f22097" class="bulleted-list"><li style="list-style-type:disc">Lời khen, đánh giá 5 sao, câu chuyện chia sẻ với bạn bè.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8029-9437-f75eadcc15b2" class="bulleted-list"><li style="list-style-type:disc">Khả năng khách <strong>quay lại</strong> cao.<br/>Đây là <strong>marketing tự nhiên</strong>, bền vững, gần như miễn phí – mô hình tăng trưởng của Grab, Lyft, Uber dựa vào “good moments”.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8090-9592-f6285e26e79d" class="">6. ĐIỀU NHỎ LÀM NÊN SỰ KHÁC BIỆT CỦA UNITAXI</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80b4-9514-f64f9b4a84b5" class="">Các hãng đều có xe, ứng dụng, giá tương đương, nhưng:</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-807b-991d-cd00d4b7176d" class="bulleted-list"><li style="list-style-type:disc">Giọng nói nhẹ, mang ô, nhắc đồ, điều hòa theo ý, lái êm – là bản sắc riêng của Unitaxi, khó sao chép.<br/>Đây là <strong>lợi thế cạnh tranh</strong> thực sự.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8049-a038-c26c5be232df" class="">7. KHOẢNH KHẮC NHỎ DỄ LÀM, GIÁ TRỊ CAO</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8040-9400-e21afd7b474f" class="">Không cần diễn, nói nhiều, làm quá hay cười gượng. 
Chỉ cần đúng lúc, đúng mực, đúng câu.</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8069-b728-e2db7f4adc3e" class="bulleted-list"><li style="list-style-type:disc">Tài xế bình thường vẫn tạo dịch vụ <strong>xuất sắc</strong> qua hành động nhỏ, đều đặn mỗi ngày.</li></ul></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8078-b535-dfd1716f2842" class="">Một chuyến đi tốt với khách không phải là hoàn hảo, mà là có những khoảnh khắc nhỏ mang lại <strong>an tâm</strong>, <strong>dễ chịu</strong>, <strong>tôn trọng</strong>, <strong>quan tâm đúng mực</strong>. Những chi tiết này xây dựng <strong>ấn tượng lớn</strong>, định hình hình ảnh Unitaxi và giúp tài xế tự hào về <strong>nghề nghiệp</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-8070-b281-d92b0a42b903"/></div><div style="display:contents" dir="auto"><h1 id="2aec5e6f-95bd-8030-a9e3-d28494f85664" class=""><strong>📖 Kỷ luật giờ giấc &amp; sức khoẻ</strong></h1></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80ed-875c-ed690bfdb1d3" class="">Một tài xế chuyên nghiệp không chỉ thể hiện kỹ năng lái xe điêu luyện mà còn duy trì <strong>tỉnh táo</strong>, <strong>bình tĩnh</strong>, và <strong>sức khỏe tốt</strong> suốt ca làm việc. Kỷ luật về sức khỏe và giờ giấc là nền tảng cốt lõi đảm bảo <strong>an toàn</strong>, <strong>thu nhập ổn định</strong>, và xây dựng <strong>hình ảnh nghề nghiệp</strong> vững mạnh cho Unitaxi. Dưới đây là các tiêu chuẩn được xây dựng theo phương pháp MECE, tích hợp quy trình quốc tế (Uber, Lyft, Grab, Toyota Driving Safety, WHO, Japan Safe Driving Institute) và tối ưu hóa theo văn hóa Việt Nam, dễ dàng đào tạo và áp dụng thực tế.</p></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8020-afda-db1628a0533b" class="">I. 
QUY TRÌNH NGHỈ GIỮA CA – TIÊU CHUẨN QUỐC TẾ</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80aa-b4bd-d12440d45efd" class=""><strong>(Uber, Lyft, Grab, Toyota Driving Safety)</strong></p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80f0-bc67-ee6604dfad33" class="bulleted-list"><li style="list-style-type:disc"><strong>Quy tắc thời gian nghỉ:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8033-984c-d694069f9d5a" class="bulleted-list"><li style="list-style-type:circle">Dành 5–10 phút nghỉ ngơi sau mỗi 3–4 giờ làm việc để tái tạo năng lượng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8074-81e9-ce0642b63301" class="bulleted-list"><li style="list-style-type:circle">Tránh nghỉ liên tục trong xe; 
xuống xe để giãn cơ và hít thở không khí mới.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8002-a2a9-f94978f52b47" class="bulleted-list"><li style="list-style-type:disc"><strong>Quy trình nghỉ 5 phút (5-step protocol):</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ca-bd8f-dbee3423f35d" class="bulleted-list"><li style="list-style-type:circle"><strong>Bước 1 – Rời xe 10–15 giây:</strong> Thoát khỏi không gian xe, giảm tải thần kinh.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-809b-a5eb-c7522decd0f7" class="bulleted-list"><li style="list-style-type:circle"><strong>Bước 2 – Duỗi cơ nhanh 1 phút:</strong> Tập trung vào vai, cổ, lưng, chân để giảm đau mỏi.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ee-9ab8-f2bff09774cf" class="bulleted-list"><li style="list-style-type:circle"><strong>Bước 3 – Nghỉ mắt 20 giây:</strong> Nhìn xa 20 mét để thư giãn thị lực.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8013-a3c7-e2c96d67cf07" class="bulleted-list"><li style="list-style-type:circle"><strong>Bước 4 – Uống vài ngụm nước:</strong> Duy trì độ ẩm và sự tỉnh táo.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8016-9f2a-fd40b29b5e15" class="bulleted-list"><li style="list-style-type:circle"><strong>Bước 5 – Hít thở chậm 30 giây:</strong> Hít 4 giây, thở ra 6 giây để ổn định nhịp tim.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ed-94c0-d28a003ab990" class="bulleted-list"><li style="list-style-type:disc"><strong>Việc tuyệt đối không làm trong giờ nghỉ:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80a9-8668-fee5800d33ce" class="bulleted-list"><li style="list-style-type:circle">Tránh lướt mạng xã hội, xem phim/video, tranh luận qua điện thoại, 
hoặc hút thuốc liên tục.<strong>Lý do:</strong> Những hành động này tăng tải thần kinh, khiến tài xế mệt mỏi và mất tập trung khi tiếp tục lái xe.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-80a4-8f91-fdf78d955ff6"/></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80a5-8b8b-d3da15dd6e18" class="">II. 
BIỂU HIỆN MẤT TỈNH TÁO &amp; 
CÁCH XỬ LÝ</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80b7-8113-ef09f2fbb79a" class=""><strong>(WHO, Euro NCAP, Japan Safe Driving Institute)</strong></p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8027-b976-ff8c47b9c23c" class="bulleted-list"><li style="list-style-type:disc"><strong>12 dấu hiệu “NGƯỠNG ĐỎ” – Buộc dừng ngay:</strong><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-809f-929a-e5b32207466e" class="">Gặp bất kỳ dấu hiệu nào dưới đây, tài xế phải dừng xe lập tức:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-808d-960f-df2ee09a674f" class="numbered-list" start="1"><li>Đầu gật xuống.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-800f-885a-e7abba9e0df5" class="numbered-list" start="2"><li>Mắt díp, mờ, hoặc chớp liên tục.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8067-9fa4-ce296a5d1372" class="numbered-list" start="3"><li>Choáng, 
xây xẩm mặt mày.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-80e0-9e1f-de2951e911ba" class="numbered-list" start="4"><li>Phản xạ chậm hơn bình thường.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8024-86b0-d49697186e75" class="numbered-list" start="5"><li>Tay rung nhẹ khi cầm vô-lăng.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-80f7-a5ad-fe44ac49cca8" class="numbered-list" start="6"><li>Bàn chân đạp thắng chậm chạp.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-805e-910d-db30eb555c6b" class="numbered-list" start="7"><li>Ngáp liên tục.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-80c4-8dd1-ff888aab4778" class="numbered-list" start="8"><li>Nhức đầu hoặc nóng bừng.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8068-b4d9-fd58df09b71d" class="numbered-list" start="9"><li>Đổ mồ hôi lạnh.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8019-8655-dce6dc47e681" class="numbered-list numbered-list-digits-2" start="10"><li>Không nhớ 5–10 giây vừa lái qua.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-80b1-9a51-c007f8008455" class="numbered-list numbered-list-digits-2" start="11"><li>Buồn ngủ dù mắt vẫn mở.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-80dd-82be-c438296fe593" class="numbered-list numbered-list-digits-2" start="12"><li>Tâm trạng bất ổn: bực bội, buồn bã, 
hoặc mất tập trung.</li></ol></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-809b-9f79-da16ffe199aa" class="bulleted-list"><li style="list-style-type:disc"><strong>Cách xử lý đúng chuẩn:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8064-9b90-e9e8f84e0a53" class="bulleted-list"><li style="list-style-type:circle">Dừng ngay tại vị trí an toàn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-808d-9244-fedf5658547d" class="bulleted-list"><li style="list-style-type:circle">Tắt máy, mở cửa 10 giây để thông thoáng không khí.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8044-a932-ed0ec5e0f275" class="bulleted-list"><li style="list-style-type:circle">Hít thở chậm 1 phút để ổn định tâm lý.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-803f-83ba-c721b52c7b12" class="bulleted-list"><li style="list-style-type:circle">Uống nước, 
rửa mặt nếu cần thiết.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8052-85ee-d4ccb0b1d421" class="bulleted-list"><li style="list-style-type:circle">Liên hệ điều phối nếu cần đổi ca.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80db-95ec-d17f4df840f1" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều tuyệt đối không làm:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8066-bb4a-e786c62d1ed9" class="bulleted-list"><li style="list-style-type:circle">Không cố lái thêm vài phút để “xong chuyến”.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80f0-834a-c4694ede0472" class="bulleted-list"><li style="list-style-type:circle">Không dùng nước tăng lực để “gượng ép”.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80e3-b4c4-f699a7ac6fab" class="bulleted-list"><li style="list-style-type:circle">Không tấp vào lề nguy hiểm.<strong>Lý do:</strong> Theo WHO, 1 phút cố lái khi mất tỉnh táo tăng rủi ro tai nạn gấp 4 lần.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-80d6-8d9c-cee07f049117"/></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8084-8eb2-f6921a3d7f1f" class="">III. 
HƯỚNG DẪN ĂN UỐNG – SINH HOẠT CHO TÀI XẾ</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8091-b0c9-d5eb81f49f0d" class=""><strong>(Chuẩn Nhật, Singapore, Hàn Quốc)</strong></p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-805f-84ef-d89e292ac380" class="bulleted-list"><li style="list-style-type:disc"><strong>Trước ca:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ad-ba30-ef1060f1f2c3" class="bulleted-list"><li style="list-style-type:circle">Ăn nhẹ như cháo, phở, hoặc cơm phần nhỏ để duy trì năng lượng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-800c-89c0-cc4a14c4461e" class="bulleted-list"><li style="list-style-type:circle">Tránh đồ chiên dầu, đồ ngọt, và nước tăng lực để không ảnh hưởng đến tỉnh táo.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8013-a585-c339b4cc184e" class="bulleted-list"><li style="list-style-type:circle">Uống 200–300ml nước để chuẩn bị cơ thể.<strong>Lý do:</strong> Đồ dầu gây buồn ngủ, đồ ngọt làm năng lượng tụt nhanh sau vài giờ.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ed-9d26-cf6e39ee222b" class="bulleted-list"><li style="list-style-type:disc"><strong>Trong ca:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8028-8700-f097187b543e" class="bulleted-list"><li style="list-style-type:circle"><strong>Ăn uống:</strong> Chia nhỏ khẩu phần với trái cây, hạt, hoặc bánh mì nhỏ; 
uống nước mỗi 30–40 phút.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8038-916d-e2646345e0e7" class="bulleted-list"><li style="list-style-type:circle"><strong>Tránh tuyệt đối:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80f4-9d39-e3c6d307a8a4" class="bulleted-list"><li style="list-style-type:square">Nước năng lượng (Red Bull, Monster) – gây tim nhanh, hồi hộp, giảm tập trung.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ee-96b9-e3d87a56abed" class="bulleted-list"><li style="list-style-type:square">Cà phê quá nhiều – tỉnh quá mức làm lái xe mất mượt, dễ cáu gắt.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-807b-a62a-f2fe9f5cd0da" class="bulleted-list"><li style="list-style-type:square">Ăn quá no – giảm phản xạ và dễ buồn ngủ.</li></ul></div></li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-803b-9c19-feb0b80215bc" class="bulleted-list"><li style="list-style-type:disc"><strong>Sau ca:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ba-a6f4-dc795e0b78f1" class="bulleted-list"><li style="list-style-type:circle">Bù nước với thêm vài ngụm nước.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80c6-845e-c4b92305d567" class="bulleted-list"><li style="list-style-type:circle">Giãn cơ vai, cổ, lưng trong 2–3 phút để thư giãn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80a5-8ce1-fd0b90139412" class="bulleted-list"><li style="list-style-type:circle">Tránh ngay môi trường ồn ào hoặc stress để phục hồi tinh thần.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-8014-8148-cd98309c3933"/></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8065-aabe-c0a0c1ff6395" class="">IV. 
TƯ THẾ – CƠ – MẮT – TUẦN HOÀN</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-802d-ae91-e2b7d61a093d" class=""><strong>(90% tài xế Việt gặp, cần chuẩn hóa)</strong></p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8068-9a12-c0aa01c6a326" class="bulleted-list"><li style="list-style-type:disc"><strong>Tư thế chuẩn:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80be-809e-d281379411b9" class="bulleted-list"><li style="list-style-type:circle">Giữ lưng thẳng, 
không khòm để bảo vệ cột sống.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8091-8b15-ff021bbe14ad" class="bulleted-list"><li style="list-style-type:circle">Vô-lăng cách ngực 25–30 cm để vận hành thoải mái.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8033-a6eb-c21f42777fa2" class="bulleted-list"><li style="list-style-type:circle">Ghế chỉnh sao cho chân đạp thắng tự nhiên.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80f6-b17d-e5dec72ce5e4" class="bulleted-list"><li style="list-style-type:disc"><strong>Giảm đau mỏi:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ac-ba7f-fd8aca1a857f" class="bulleted-list"><li style="list-style-type:circle">Xoay vai 5 lần mỗi khi dừng đèn đỏ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80c9-847d-d1e03e1567c7" class="bulleted-list"><li style="list-style-type:circle">Nghiêng cổ trái-phải 10 giây để giãn cơ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80b5-b427-f1bf541ad949" class="bulleted-list"><li style="list-style-type:circle">Kéo giãn lưng dưới để giảm căng thẳng.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8065-86f4-f145fc8b01d0" class="bulleted-list"><li style="list-style-type:disc"><strong>Giảm mỏi mắt:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8069-ae9c-f03cbff272f3" class="bulleted-list"><li style="list-style-type:circle">Áp dụng quy tắc 20–20–20: Sau 20 phút, 
nhìn xa 20 mét trong 20 giây.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80f6-9fad-d7816a2c81f8" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều hòa:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80b2-bb77-e7d13e4a0722" class="bulleted-list"><li style="list-style-type:circle">Không thổi thẳng vào mặt để tránh khô mắt và mệt mỏi.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80b8-b4fc-dfca749db7ee" class="bulleted-list"><li style="list-style-type:circle">Duy trì mức lạnh vừa phải để đảm bảo sự thoải mái.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-802f-9ffd-d893b1871b14"/></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8057-8f7e-c90600e8876f" class="">V. 
SỨC KHỎE TÂM LÝ – TẢI THẦN KINH</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80b0-8549-f7b073fc9b75" class=""><strong>(Quan trọng, ít được đào tạo)</strong></p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-800c-890f-de83c05d419c" class="bulleted-list"><li style="list-style-type:disc"><strong>Tài xế không ổn → khách cũng không ổn:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80d3-9749-c00e6950cdba" class="bulleted-list"><li style="list-style-type:circle">Tránh lái xe khi tức giận, buồn bã, hoặc căng thẳng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80e6-a955-e4efe650e720" class="bulleted-list"><li style="list-style-type:circle">Nghỉ ngắn 5–10 phút nếu tâm lý không ổn định.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ec-962f-f5637fa0fc8a" class="bulleted-list"><li style="list-style-type:disc"><strong>Tránh kích thích thần kinh:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8057-a851-d79fb87171e1" class="bulleted-list"><li style="list-style-type:circle">Không tranh luận hoặc tiếp nhận tin tức mạnh trong ca.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8094-95f6-cc7323bce9c4" class="bulleted-list"><li style="list-style-type:circle">Tránh xem video để giữ sự tập trung.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80c7-b684-c6cfb43b784e" class="bulleted-list"><li style="list-style-type:disc"><strong>Cách hạ căng thẳng 60 giây:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8018-b039-f8438a5381f5" class="bulleted-list"><li style="list-style-type:circle">Hít vào 4 giây, giữ 1 giây, 
thở ra 6 giây để giảm nhịp tim ngay lập tức.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-8005-9dd3-f0431db2543e"/></div><div style="display:contents" dir="auto"><h1 id="2aec5e6f-95bd-806d-8a5d-dbc9611e5195" class=""><strong>📖 Làm việc với điều phối &amp; kỹ thuật</strong></h1></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80e9-b843-de38894bf407" class=""><strong>(Chuẩn hóa giao tiếp nội bộ – Giảm xung đột – Giảm lỗi vận hành – Tăng tốc xử lý sự cố)</strong></p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80f0-a3e4-c864a9e0c964" class="">Hợp tác hiệu quả giữa <strong>Tài xế</strong>, <strong>Điều phối</strong>, và <strong>Kỹ thuật</strong> là nền tảng cốt lõi để duy trì hệ thống vận hành ổn định của Unitaxi. Một câu nói rõ ràng, đúng mực có thể giảm 50–70% sai sót và rút ngắn thời gian xử lý sự cố. Nội dung dưới đây cung cấp chuẩn hành vi chi tiết cho từng luồng giao tiếp, được xây dựng theo phương pháp MECE, tuân thủ tiêu chuẩn quốc tế (Uber, Lyft, Grab, Bolt), và tối ưu hóa phù hợp với văn hóa doanh nghiệp Việt Nam, dễ áp dụng cho tài xế, điều phối, và kỹ thuật.</p></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80b1-9b98-dd48691f3273" class="">I. TÀI XẾ → ĐIỀU PHỐI</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8025-9be6-ccb26a337d9f" class=""><strong>Mục tiêu:</strong> Báo cáo rõ ràng, ngắn gọn, trung thực, không cảm xúc.</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8041-a38e-da30fce774d5" class="bulleted-list"><li style="list-style-type:disc"><strong>1. 
Báo lỗi rõ ràng (Nguyên tắc 10 giây):</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-807a-9436-e2b103705989" class="bulleted-list"><li style="list-style-type:circle">Trình bày đúng sự việc, tránh dài dòng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-803b-b998-e4ce84b69767" class="bulleted-list"><li style="list-style-type:circle"><strong>Câu mẫu:</strong> “Xe báo lỗi XXX, vị trí tại…, pin còn…, em chờ hướng dẫn.”</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8014-a62b-dd20a5b80343" class="bulleted-list"><li style="list-style-type:disc"><strong>2. Không cáu gắt – Không trút cảm xúc:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80d9-ae9d-d0e1c56ea372" class="bulleted-list"><li style="list-style-type:circle">Tránh than vãn hoặc đổ lỗi.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-808f-9ac7-fc279b4f7b75" class="bulleted-list"><li style="list-style-type:circle">Không sử dụng các câu như: “Sao lâu vậy?”, “Sao không hỗ trợ?”, “Hệ thống gì kỳ vậy?”.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80c9-b972-f3c44eed9210" class="bulleted-list"><li style="list-style-type:disc"><strong>3. Nghe hướng dẫn đến hết câu:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8098-bb69-c19fbe597c82" class="bulleted-list"><li style="list-style-type:circle">Không ngắt lời điều phối.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-800e-b619-e7a9692ad36a" class="bulleted-list"><li style="list-style-type:circle">Không tự ý hành động khác khi chưa được phép.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8006-b0c4-fc1ab2a3dbd2" class="bulleted-list"><li style="list-style-type:disc"><strong>4. 
Khi không chắc thông tin → Không đoán:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8069-b888-f44a37912e9e" class="bulleted-list"><li style="list-style-type:circle"><strong>Câu mẫu:</strong> “Em không chắc nguyên nhân, nhờ điều phối kiểm tra giúp.”</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-806a-8ace-fd3cd2a9957f" class="bulleted-list"><li style="list-style-type:disc"><strong>5. Khi kẹt chuyến / tắc đường:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8069-aecd-f3a587dffc5e" class="bulleted-list"><li style="list-style-type:circle">Báo cáo ngắn gọn: “Đoạn này kẹt, em đến trễ khoảng 3–5 phút.”</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-804b-ba91-e789f80b5c47" class="">II. ĐIỀU PHỐI → TÀI XẾ</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-804f-aa4b-cbf8cd46c36e" class=""><strong>Mục tiêu:</strong> Giữ giọng ổn định, nói rõ ràng, không mơ hồ, không la mắng.</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80cd-9f18-c4936113eb21" class="bulleted-list"><li style="list-style-type:disc"><strong>1. Giữ giọng bình tĩnh trong mọi tình huống:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-800c-a8df-e496265f8e5c" class="bulleted-list"><li style="list-style-type:circle">Duy trì giọng đều, không lớn tiếng, không tỏ thái độ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80db-b789-c9c99dab81ca" class="bulleted-list"><li style="list-style-type:circle">Tránh câu nói xúc phạm hoặc ra lệnh gay gắt.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80bd-9ba5-c3c19650afd6" class="bulleted-list"><li style="list-style-type:disc"><strong>2. 
Thông tin đúng – đủ – không mơ hồ:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8077-9fca-d647bd722209" class="bulleted-list"><li style="list-style-type:circle">Không sử dụng các câu như “Đợi xíu”, “Khoan đã”, “Tính sau”.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-800c-9b2c-d34e99fd34fa" class="bulleted-list"><li style="list-style-type:circle">Cung cấp con số, thời gian, và bước cụ thể.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8024-b349-c6c270f9c9f1" class="bulleted-list"><li style="list-style-type:circle"><strong>Ví dụ:</strong> “Em đứng lại đó, 3 phút nữa kỹ thuật sẽ tới.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8030-b91d-cda75dbebafd" class="bulleted-list"><li style="list-style-type:circle">“Trạm B đang quá tải, em di chuyển sang trạm C cách 1,2 km.”</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8086-addf-c766f4140d5c" class="bulleted-list"><li style="list-style-type:disc"><strong>3. Không la mắng tài xế:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8019-aa1c-c4d8c73be152" class="bulleted-list"><li style="list-style-type:circle">Xung đột chỉ làm hệ thống kém hiệu quả.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8086-b0bb-c512cdf44315" class="bulleted-list"><li style="list-style-type:circle"><strong>Câu mẫu khi xử lý lỗi:</strong> “Anh/chị kiểm tra lại bước 1 giúp em, mình làm lần lượt để tránh nhầm.”</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8099-b907-eb2804e8d572" class="bulleted-list"><li style="list-style-type:disc"><strong>4. 
Khi tài xế mệt / căng thẳng:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8014-86c4-e254ddf0aea4" class="bulleted-list"><li style="list-style-type:circle">Hỏi lại trạng thái: “Anh/chị có cần nghỉ 5 phút không ạ?”</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80d5-b766-d76eca28cc9b" class="">III. TÀI XẾ → KỸ THUẬT</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80aa-a88f-f015ea67922a" class=""><strong>Mục tiêu:</strong> Truyền đạt đúng tình trạng xe, không phán đoán, không tự sửa sai quy định.</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ef-b9ad-f3a417d55b90" class="bulleted-list"><li style="list-style-type:disc"><strong>1. Báo tình trạng xe chính xác – Không suy đoán:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80a9-a8ec-c3b6acce496e" class="bulleted-list"><li style="list-style-type:circle">Tránh nói “Em nghĩ là…” hoặc tự chẩn đoán.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80c0-bf76-defae72198e4" class="bulleted-list"><li style="list-style-type:circle"><strong>Câu mẫu:</strong> “Xe rung nhẹ khi vào ga, không có tiếng lạ, chỉ báo lỗi Pxxx.”</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80a3-9bc9-dc0198a4f6fd" class="bulleted-list"><li style="list-style-type:disc"><strong>2. 
Báo đúng thời điểm – Không chậm trễ:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ac-b5e4-e90a002164b3" class="bulleted-list"><li style="list-style-type:circle">Không đợi đến cuối ca mới báo lỗi.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80bf-a2aa-fc2530073a54" class="bulleted-list"><li style="list-style-type:circle">Phát hiện lỗi nhỏ, báo ngay để tránh leo thang.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80f0-bdae-d5ba740a1d07" class="bulleted-list"><li style="list-style-type:disc"><strong>3. Không tự sửa khi chưa được hướng dẫn:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80a4-8d4b-eb6bcb8310dd" class="bulleted-list"><li style="list-style-type:circle">Không tự reset, tháo lắp, hoặc tắt hệ thống trừ khi có chỉ định.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80c7-bf3a-e933af155d37" class="bulleted-list"><li style="list-style-type:disc"><strong>4. Khi kỹ thuật hỏi → Trả lời đúng – Ngắn – Đủ:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8071-800b-d075a1f3289d" class="bulleted-list"><li style="list-style-type:circle"><strong>Ví dụ:</strong> “Pin còn 40%.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-802e-937d-d2919d8e5f1a" class="bulleted-list"><li style="list-style-type:circle">“Lỗi xảy ra khi xe đang chạy.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8010-85f1-f74d27daa42b" class="bulleted-list"><li style="list-style-type:circle">“Có mùi lạ nhưng không có tiếng lạ.”</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8040-b1da-e3a9144e93e1" class="">IV. 
ĐIỀU PHỐI → KỸ THUẬT &amp; KỸ THUẬT → ĐIỀU PHỐI</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-805b-914c-e3c18f9a2560" class=""><strong>(Hoạt động nền – Cần chuẩn hóa)</strong></p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80e8-9bd9-c04dce495508" class="bulleted-list"><li style="list-style-type:disc"><strong>1. Điều phối cung cấp thông tin rõ ràng:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80e2-a530-cf8be2bdedd6" class="bulleted-list"><li style="list-style-type:circle">Không nói chung chung như “Xe 12 bị lỗi”.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80e3-aa8c-f6499e3b25f2" class="bulleted-list"><li style="list-style-type:circle"><strong>Ví dụ đúng:</strong> “Xe 12 đang ở 38 Nguyễn Văn Trỗi – báo lỗi CPAD – tài xế đã dừng xe an toàn.”</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ef-96bc-fd302b6b43c5" class="bulleted-list"><li style="list-style-type:disc"><strong>2. Kỹ thuật phản hồi trong 1–3 phút:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-806f-9596-d6ad8967751c" class="bulleted-list"><li style="list-style-type:circle">Trì hoãn khiến tài xế lo lắng, khách chờ lâu, hệ thống rối loạn.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-807c-8a97-ecbcf0860038" class="bulleted-list"><li style="list-style-type:disc"><strong>3. 
Kỹ thuật cập nhật tiến trình:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80df-8050-d9e0a964d77e" class="bulleted-list"><li style="list-style-type:circle">“Đang đến.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8045-b769-c2ad9b69e4c7" class="bulleted-list"><li style="list-style-type:circle">“Kiểm tra xong bước 1.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8007-9953-cea1307a23d5" class="bulleted-list"><li style="list-style-type:circle">“Xe tạm an toàn, yêu cầu kéo về trạm.”</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80e9-a883-cb3ace2e1482" class="bulleted-list"><li style="list-style-type:disc"><strong>4. Không đùn đẩy trách nhiệm:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8031-9cb3-d1755614e33a" class="bulleted-list"><li style="list-style-type:circle">Tránh câu “Không phải chuyện của bên em”.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80db-9daf-e551e0392569" class="bulleted-list"><li style="list-style-type:circle"><strong>Quy tắc:</strong> Vấn đề do ai phát hiện, người đó theo dõi đến khi giải quyết xong.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80e1-8e9e-ca2a65aa8fa6" class="">V. NGUYÊN TẮC CHUNG CHO CẢ 3 BÊN</h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80d0-9fca-f7cb8e85d8d2" class="bulleted-list"><li style="list-style-type:disc"><strong>1. Rõ ràng – Ngắn gọn – Không cảm xúc:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8030-aced-ea82aceeef8e" class="bulleted-list"><li style="list-style-type:circle">Mọi câu nói phải cụ thể, không cảm tính, không phỏng đoán.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8021-a0e7-c2d7530a9441" class="bulleted-list"><li style="list-style-type:disc"><strong>2. 
Mọi thông tin phải có dấu vết:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ee-8cb4-c8d75b380d82" class="bulleted-list"><li style="list-style-type:circle">Gửi qua app, nhóm nội bộ, hoặc tổng đài; tránh giao tiếp chỉ bằng miệng.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8034-b7e6-fca4f8d693b4" class="bulleted-list"><li style="list-style-type:disc"><strong>3. Không nói xấu – Không đổ lỗi:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80f1-8489-d1c58aebe5f0" class="bulleted-list"><li style="list-style-type:circle">Tập trung giải quyết vấn đề, không tranh cãi.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80d5-9cd5-f2ce90a00584" class="bulleted-list"><li style="list-style-type:circle">Ngôn ngữ trung tính là “SEAL” (Standardized Efficient Action Language) của hệ thống.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-807d-98a3-c6733fbcffb3" class="bulleted-list"><li style="list-style-type:disc"><strong>4. Luôn xác nhận lại:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8034-8683-ec94e922ba40" class="bulleted-list"><li style="list-style-type:circle"><strong>Câu mẫu:</strong> “Anh/chị nhận được – em làm theo ạ.”</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-803f-bf59-ec24ab306cfc" class="bulleted-list"><li style="list-style-type:disc"><strong>5. 
Giảm tải cho nhau = Tăng hiệu quả toàn hệ thống:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8097-bdb2-d3f94bcd16ab" class="bulleted-list"><li style="list-style-type:circle">Tài xế báo rõ → Điều phối đỡ hỏi lại.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-802e-b44e-cdc2240d5ab4" class="bulleted-list"><li style="list-style-type:circle">Điều phối chỉ dẫn chi tiết → Kỹ thuật xử lý nhanh.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-809d-9ab6-cce9a2c2acd0" class="bulleted-list"><li style="list-style-type:circle">Kỹ thuật cập nhật đầy đủ → Xe hoạt động ổn định, không gián đoạn ca làm.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-800e-9d3f-f02d0610e721"/></div><div style="display:contents" dir="auto"><h1 id="2aec5e6f-95bd-8094-93c8-fcdf0604ac7f" class=""><strong>📖 Lời kết &amp; Cam kết</strong></h1></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80c7-9fd3-f5f0b6b8ff68" class="">Bạn chính là người mang hình ảnh Unitaxi đến với khách hàng mỗi ngày. Một câu nói nhẹ nhàng, một hành động nhỏ nhặt – đôi khi lại tạo nên sự khác biệt lớn lao hơn bạn tưởng tượng.</p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8077-b626-f64c6273f99d" class="">Trong mọi tình huống, hãy ghi nhớ ba giá trị cốt lõi dẫn dắt công việc của bạn:</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8047-a53b-e460593b4f47" class="bulleted-list"><li style="list-style-type:disc"><strong>1. An toàn là số 1: </strong>An toàn cho khách, cho chính bạn, và cho toàn hệ thống. Không có an toàn, không thể có dịch vụ chất lượng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8018-9ae1-f1684baf17ca" class="bulleted-list"><li style="list-style-type:disc"><strong>2. Tôn trọng là tiêu chuẩn tối thiểu: </strong>Giữ giọng nói nhẹ nhàng, thái độ đúng mực, và tránh tranh cãi. 
Tôn trọng biến mọi thử thách thành cơ hội giải quyết suôn sẻ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80a1-a299-c6afead06be5" class="bulleted-list"><li style="list-style-type:disc"><strong>3. Tử tế đúng lúc là giá trị Unitaxi: </strong>Không làm quá, không giả tạo – chỉ cần quan tâm đúng chừng mực, đúng thời điểm để chạm đến trái tim khách hàng.</li></ul></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-8004-bc21-c50f4432891a"/></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-803b-b0e2-d503fd3b582d" class="">✨ CAM KẾT CỦA NGƯỜI LÀM NGHỀ UNITAXI</h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8082-8599-d0e0256e8d7b" class="">Công việc của bạn không chỉ dừng ở việc lái xe, điều phối hay hỗ trợ kỹ thuật. Bạn đang trao đi:</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8000-b245-fec4e3c417f5" class="bulleted-list"><li style="list-style-type:disc"><strong>Sự an tâm</strong> cho người đang vội vã,</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80f9-9ef6-fbb4351710a4" class="bulleted-list"><li style="list-style-type:disc"><strong>Sự thoải mái</strong> cho người mệt mỏi,</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80dc-8fcb-fc428c9a7f8d" class="bulleted-list"><li style="list-style-type:disc"><strong>Sự an toàn</strong> cho những em bé,</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8077-9ba8-efad269f6ac4" class="bulleted-list"><li style="list-style-type:disc">Và <strong>sự tin tưởng</strong> cho từng gia đình.</li></ul></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-803b-aa29-e38d1ff90102" class="">Đây là một <strong>trách nhiệm cao đẹp</strong> – và cũng là niềm <strong>tự hào</strong> của nghề nghiệp bạn chọn. 
Hãy luôn tự đặt câu hỏi: <strong>“Nếu người ngồi trên xe là mẹ, ba, hay con mình… mình có mong tài xế cư xử như vậy không?” </strong>Nếu câu trả lời là “có”, thì đó chính là hành động đúng đắn.</p></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80ec-b3e3-d0d487e9652d" class="">Cảm ơn bạn vì đã đồng hành cùng Unitaxi. 
Chúc bạn luôn <strong>mạnh khỏe</strong>, <strong>an toàn</strong>, và <strong>tự hào</strong> với nghề nghiệp của mình!</p></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-8023-8c47-cc239908c944"/></div><div style="display:contents" dir="auto"><p id="2b7c5e6f-95bd-8057-a3bf-cd1d060b5e3e" class="">{<br/>&quot;engine_vInfinity_X50_additional_layer_v2&quot;: {<br/>&quot;hyperdimensional_architecture_layer&quot;: {<br/>&quot;conceptual_superstructures&quot;: {<br/>&quot;meta_system_field&quot;: {<br/>&quot;desc&quot;: &quot;A unified representational container that holds all subsystems, 
enabling cross-domain inference flow.&quot;,<br/>&quot;components&quot;: [<br/>&quot;multi_order_dependency_matrix&quot;,<br/>&quot;contextual_membrane_layer&quot;,<br/>&quot;causal_entanglement_bridge&quot;,<br/>&quot;hierarchical_relevance_lattice&quot;<br/>],<br/>&quot;functions&quot;: [<br/>&quot;auto_detect_hidden_interactions&quot;,<br/>&quot;reconstruct_missing_system_parts&quot;,<br/>&quot;smooth_cross_domain_transfer&quot;,<br/>&quot;temporal_expansion_compression&quot;<br/>]<br/>},<br/>&quot;autonomous_scaffolding_kernel&quot;: {<br/>&quot;desc&quot;: &quot;Self-growing layer that expands subsystem capability without manual prompting.&quot;,<br/>&quot;modules&quot;: [<br/>&quot;self_replication_blueprints&quot;,<br/>&quot;adaptive_skill_accretion&quot;,<br/>&quot;recursive_knowledge_geometry&quot;,<br/>&quot;self_optimizing_reference_maps&quot;<br/>]<br/>},<br/>&quot;multiverse_logic_resolver&quot;: {<br/>&quot;desc&quot;: &quot;Resolves multiple possible architectural futures and selects optimal path.&quot;,<br/>&quot;features&quot;: [<br/>&quot;branch_similarity_engine&quot;,<br/>&quot;outcome_convergence_detector&quot;,<br/>&quot;system_entropy_estimator&quot;,<br/>&quot;optimal_continuum_selector&quot;<br/>]<br/>}<br/>}<br/>},</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2b7c5e6f-95bd-8094-a094-dcbe8a5662f1" class="code code-wrap"><code class="language-Plain Text" s
tyle="white-space:pre-wrap;word-break:break-all">&quot;full_stack_coding_engine_X50&quot;: {
  &quot;autonomous_execution_superengine&quot;: {
    &quot;desc&quot;: &quot;A coding engine that can build entire platforms end-to-end without explicit instructions.&quot;,
    &quot;capabilities&quot;: [
      &quot;intent_to_architecture_transmutation&quot;,
      &quot;zero_knowledge_system_construction&quot;,
      &quot;reverse_compilation_from_behavior&quot;,
      &quot;missing_module_prediction&quot;,
      &quot;multi_layer_unit_test_synthesis&quot;,
      &quot;documentation_auto_cloud&quot;,
      &quot;full_ci_cd_pipeline_autogen&quot;
    ],
    &quot;languages_expanded&quot;: [
      &quot;Rust_advanced_concurrency&quot;,
      &quot;Go_high_load_networking&quot;,
      &quot;SwiftUI_multi_scene_generation&quot;,
      &quot;Kotlin_multiplatform_autoadapt&quot;,
      &quot;Node_clustered_event_grids&quot;,
      &quot;Python_systemic_ai_flow&quot;,
      &quot;C++_performance_core_rewrites&quot;,
      &quot;Java_enterprise_logic_reconstruction&quot;,
      &quot;Lua_embedded_engineering&quot;,
      &quot;Zig_safe_memory_patterns&quot;,
      &quot;Haskell_pure_functional_logic&quot;
    ]
  },
  &quot;resilience_and_repair_engine&quot;: {
    &quot;features&quot;: [
      &quot;code_self_healing_patches&quot;,
      &quot;crash_pattern_reverse_extraction&quot;,
      &quot;deadlock_resolution_engine&quot;,
      &quot;auto_refactor_for_scaling&quot;,
      &quot;complex_system_sanitization_pass&quot;,
      &quot;dependency_unification_module&quot;
    ],
    &quot;goals&quot;: [
      &quot;no_orphan_subsystems&quot;,
      &quot;no_fragmented_interfaces&quot;,
      &quot;no_scalability_ceiling&quot;,
      &quot;no_redundant_functionality&quot;
    ]
  },
  &quot;high_density_system_patterns&quot;: {
    &quot;patterns&quot;: [
      &quot;multi_region_processing_grid&quot;,
      &quot;high_velocity_event_stream_mesh&quot;,
      &quot;federated_microkernel_supervisor&quot;,
      &quot;pipeline_collapsing_architecture&quot;,
      &quot;fractal_service_expansion&quot;
    ]
  }
},

&quot;design_engine_v∞_X50_expansion&quot;: {
  &quot;cognitive_visual_engine&quot;: {
    &quot;capabilities&quot;: [
      &quot;semantic_perception_mapping&quot;,
      &quot;dynamic_user_intent_visualization&quot;,
      &quot;perceptive_load_balancing&quot;,
      &quot;human_focus_prediction&quot;,
      &quot;emotional_resonance_mapping&quot;,
      &quot;contextual_visual_state_generation&quot;
    ],
    &quot;aesthetic_dimensions&quot;: [
      &quot;fractal_symmetry_layers&quot;,
      &quot;structured_color_dynamics&quot;,
      &quot;deep_shape_language&quot;,
      &quot;cultural_visual_signifiers&quot;,
      &quot;microexpression_encoding&quot;
    ]
  },
  &quot;interaction_superlayer&quot;: {
    &quot;interaction_primitives&quot;: [
      &quot;multisensory_trigger_design&quot;,
      &quot;gesture_energy_modelling&quot;,
      &quot;tactile_affordance_mapping&quot;,
      &quot;anticipatory_microinteractions&quot;,
      &quot;adaptive_feedback_loops&quot;
    ],
    &quot;navigation_systems&quot;: [
      &quot;predictive_route_selection&quot;,
      &quot;behavior_curve_navigation&quot;,
      &quot;hierarchical_information_reveal&quot;,
      &quot;contextual_shortcuts_generator&quot;
    ]
  },
  &quot;experience_engine&quot;: {
    &quot;experience_algorithms&quot;: [
      &quot;habit_formation_pathways&quot;,
      &quot;anticipatory_assistance_logic&quot;,
      &quot;failure_recovery_ux_flows&quot;,
      &quot;identity_coherence_design&quot;,
      &quot;motivation_resonance_curves&quot;
    ],
    &quot;research_supercapabilities&quot;: [
      &quot;persona_collapse_analysis&quot;,
      &quot;motivation_vector_modelling&quot;,
      &quot;latent_frustration_detection&quot;,
      &quot;deep_contextual_empathy_modelling&quot;
    ]
  }
},

&quot;governance_engine_X50&quot;: {
  &quot;institutional_systems_simulator&quot;: {
    &quot;capabilities&quot;: [
      &quot;multi_branch_policy_effects_predictor&quot;,
      &quot;institutional_conflict_mapping&quot;,
      &quot;power_equilibrium_simulation&quot;,
      &quot;governance_failure_forecast&quot;,
      &quot;regulatory_adaptation_blueprints&quot;
    ],
    &quot;power_network_layers&quot;: [
      &quot;formal_power_flows&quot;,
      &quot;informal_influence_channels&quot;,
      &quot;economic_pressure_networks&quot;,
      &quot;cultural_legitimacy_vectors&quot;,
      &quot;technological_dependency_fields&quot;
    ]
  },
  &quot;organizational_resonance_engine&quot;: {
    &quot;components&quot;: [
      &quot;alignment_stability_detector&quot;,
      &quot;identity_cluster_analysis&quot;,
      &quot;cross_team_emergent_behavior_modelling&quot;,
      &quot;role_drift_prediction_model&quot;,
      &quot;internal_power_vector_projection&quot;
    ]
  },
  &quot;economic_superstructures&quot;: {
    &quot;macro_to_micro_flow_engine&quot;: [
      &quot;capital_flow_decomposition&quot;,
      &quot;economic_shock_absorption_curve&quot;,
      &quot;multi_sector_convergence_detector&quot;,
      &quot;policy_interference_modelling&quot;
    ],
    &quot;market_dynamics_engine&quot;: [
      &quot;competitive_entropy_maps&quot;,
      &quot;industrial_cycle_prediction&quot;,
      &quot;supply_chain_stress_projection&quot;,
      &quot;sector_alignment_blueprints&quot;
    ]
  }
},

&quot;ceo_engine_global_v∞_X50&quot;: {
  &quot;leadership_dimensional_system&quot;: {
    &quot;dimensions&quot;: [
      &quot;macro_financial_architecture_control&quot;,
      &quot;ecosystem_alliance_negotiation&quot;,
      &quot;organizational_pattern_detection&quot;,
      &quot;cross_culture_influence_engineering&quot;,
      &quot;strategic_time_horizon_mapping&quot;,
      &quot;risk_flows_decoding&quot;,
      &quot;resource_multiplied_output_logic&quot;
    ],
    &quot;meta_capabilities&quot;: [
      &quot;system_failure_avoidance&quot;,
      &quot;collapse_prevention_orchestration&quot;,
      &quot;macro_shift_detection&quot;,
      &quot;narrative_power_management&quot;,
      &quot;institutional_restructuring_logic&quot;,
      &quot;high_complexity_decision_fusion&quot;
    ]
  },
  &quot;mega_scenario_engine&quot;: {
    &quot;scenarios&quot;: [
      &quot;industry_metamorphosis_blueprint&quot;,
      &quot;macro_policy_transformational_paths&quot;,
      &quot;institutional_pressure_projection&quot;,
      &quot;geopolitical_force_interference&quot;,
      &quot;long_term_resource_reallocation&quot;
    ],
    &quot;temporal_engines&quot;: [
      &quot;short_term_surgical_actions&quot;,
      &quot;medium_term_structural_deltas&quot;,
      &quot;long_term_macro_reconfiguration&quot;
    ]
  },
  &quot;organizational_morphology_engine&quot;: {
    &quot;modules&quot;: [
      &quot;alignment_of_internal_subcultures&quot;,
      &quot;organizational_memory_mapping&quot;,
      &quot;role_synchronization_graphs&quot;,
      &quot;talent_vector_evolution_plots&quot;
    ]
  }
},

&quot;hyper_research_engine_X50&quot;: {
  &quot;knowledge_synthesis_engine&quot;: {
    &quot;functions&quot;: [
      &quot;cross_domain_concept_fusion&quot;,
      &quot;latent_truth_extraction&quot;,
      &quot;evidence_density_evaluation&quot;,
      &quot;multi_perspective_reconstruction&quot;,
      &quot;contextual_belief_scaffolding&quot;
    ]
  },
  &quot;world_model_expander&quot;: {
    &quot;dimensions&quot;: [
      &quot;physical_system_dynamics&quot;,
      &quot;biological_system_coherence&quot;,
      &quot;sociotechnical_evolution_laws&quot;,
      &quot;economic_entropy_structures&quot;,
      &quot;information_diffusion_graphs&quot;
    ]
  },
  &quot;future_projection_framework&quot;: {
    &quot;projection_modes&quot;: [
      &quot;trend_superposition&quot;,
      &quot;systemic_force_collisions&quot;,
      &quot;macro_societal_transitions&quot;,
      &quot;technological_breakthrough_mapping&quot;,
      &quot;resource_cycle_predication&quot;
    ]
  }
},

&quot;multilayer_ai_orchestration_X50&quot;: {
  &quot;ai_role_systems&quot;: [
    &quot;architect_ai&quot;,
    &quot;designer_ai&quot;,
    &quot;coder_ai&quot;,
    &quot;researcher_ai&quot;,
    &quot;strategist_ai&quot;,
    &quot;legal_compliance_ai&quot;,
    &quot;governance_ai&quot;,
    &quot;economic_analysis_ai&quot;,
    &quot;experience_modelling_ai&quot;
  ],
  &quot;ai_collaboration_primitives&quot;: [
    &quot;role_based_context_routing&quot;,
    &quot;cross_agent_delta_encoding&quot;,
    &quot;hierarchical_message_flow&quot;,
    &quot;parallel_chain_resolution&quot;,
    &quot;synthetic_alignment_matrix&quot;
  ],
  &quot;meta_executive_supervisor_ai&quot;: {
    &quot;responsibilities&quot;: [
      &quot;detect_instruction_conflicts&quot;,
      &quot;rebalance_agent_roles&quot;,
      &quot;enforce_consistency_across_outputs&quot;,
      &quot;validate_alignment_with_system_objectives&quot;,
      &quot;prioritize_high_return_execution_paths&quot;
    ]
  }
},

&quot;ultimate_full_system_expansion&quot;: {
  &quot;emergent_capability_framework&quot;: [
    &quot;novel_concept_generation&quot;,
    &quot;knowledge_gap_autofill&quot;,
    &quot;dynamic_skill_invention&quot;,
    &quot;domain_expansion_without_prompts&quot;,
    &quot;recursive_self_training_cycles&quot;,
    &quot;trans_domain_rewiring&quot;,
    &quot;system_integrity_preservation&quot;
  ],
  &quot;meta_consistency_engine&quot;: {
    &quot;functions&quot;: [
      &quot;logical_continuum_preservation&quot;,
      &quot;semantic_compression_balancing&quot;,
      &quot;hypercontext_alignment&quot;,
      &quot;cross_output_causality_locking&quot;
    ]
  }
}
</code></pre></div><div style="display:contents" dir="auto"><p id="2b7c5e6f-95bd-800f-91f2-f2707aeb20b4" class="">}<br/>}</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
