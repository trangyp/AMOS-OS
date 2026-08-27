---
tags: [vietnamese]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Khung Giáo trình 48 giờ cho tài xế – điều phối – kỹ thuật.</title><style>
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
	
</style></head><body><article id="2aec5e6f-95bd-805a-b7a8-f3280934c901" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Khung Giáo trình 48 giờ cho tài xế – điều phối – kỹ thuật.</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-802b-85fb-d9b17b4f07eb" class="">Toàn bộ cấu trúc đi từ: <strong>Chọn đúng người → xây đúng quy trình → ổn định nội bộ → trải nghiệm khách tốt → tự hào nghề nghiệp → thương hiệu tự khuếch đại.</strong></p></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-8008-968e-df54bc4a3b51"/></div><div style="display:contents" dir="auto"><h2 id="2aec5e6f-95bd-807d-bc43-c4663264ef1f" class=""><strong>I. Mục tiêu chương trình 48 giờ</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8069-a805-ced9cdff64c9" class="numbered-list" start="1"><li><strong>Đối với tài xế</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-806d-9da5-dd7ae99065d7" class="bulleted-list"><li style="list-style-type:disc">Lái an toàn tuyệt đối, không có vi phạm lớn trong 12 tháng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80d0-8aaa-d98ba4dab771" class="bulleted-list"><li style="list-style-type:disc">Hiểu và vận hành tốt xe điện, sạc, tối ưu pin.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-808c-8152-ec5910e11560" class="bulleted-list"><li style="list-style-type:disc">Giữ sức khoẻ – tỉnh táo – tập trung suốt ca.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80a9-9802-cecdac8a1260" class="bulleted-list"><li style="list-style-type:disc">Có <strong>kỷ luật giờ giấc và quy trình</strong>, không tự ý phá chuẩn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8013-b0cf-e1ad21759ffd" class="bulleted-list"><li style="list-style-type:disc">Giao tiếp chuẩn, tạo cảm giác <strong>“dễ chịu – an toàn – chuyên nghiệp”</strong> cho khách.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-806b-9e59-ea244b99537b" class="bulleted-list"><li style="list-style-type:disc"><strong>Ăn mặc gọn gàng, tác phong tự trọng, tự hào khi mặc đồng phục Unitaxi.</strong></li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-80b7-a30e-fbbc7f8a5105" class="numbered-list" start="2"><li><strong>Đối với điều phối</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-809c-8523-e03feb7f9519" class="bulleted-list"><li style="list-style-type:disc">Điều xe tối ưu (giảm km rỗng, giảm thời gian chờ).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-809c-83bf-e363f4a5b819" class="bulleted-list"><li style="list-style-type:disc">Xử lý sự cố bình tĩnh, giọng nói ổn định, không đổ lỗi.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80fe-a2c2-c514dea0d44f" class="bulleted-list"><li style="list-style-type:disc">Thống nhất cách nói chuyện với tài xế &amp; khách.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-809a-9b70-f03c12c3c0db" class="bulleted-list"><li style="list-style-type:disc">Biết cách phân ca, nhắc nghỉ để tránh quá tải cho tài xế.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8083-90b4-ed87ff00461c" class="bulleted-list"><li style="list-style-type:disc">Giữ kỷ luật thông tin: <strong>không sai số, không nói mơ hồ.</strong></li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-80ad-bfc7-cc0073c9071f" class="numbered-list" start="3"><li><strong>Đối với kỹ thuật (xe + trạm sạc)</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ed-bff2-e9db7c37f09a" class="bulleted-list"><li style="list-style-type:disc">Bảo trì chủ động, không để xe/trạm chết bất ngờ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-801d-bf90-ea815c15c970" class="bulleted-list"><li style="list-style-type:disc">Hiểu và sử dụng được hệ thống giám sát, báo lỗi, dữ liệu.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80c0-a4a3-e42fe2057a5e" class="bulleted-list"><li style="list-style-type:disc">Làm việc an toàn với điện, nhiệt, pin, môi trường trạm.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8005-877d-de869806300d" class="bulleted-list"><li style="list-style-type:disc">Tác phong kỹ thuật viên: <strong>sạch – gọn – chính xác – đúng hẹn.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80a0-a5cf-d9575f6a449e" class="bulleted-list"><li style="list-style-type:disc">Giao tiếp được với tài xế và điều phối bằng ngôn ngữ đơn giản, dễ hiểu.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-804e-85fa-c1564ff174a9" class="numbered-list" start="4"><li><strong>Đối với toàn hệ thống</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8009-bb91-db0fbdccd204" class="bulleted-list"><li style="list-style-type:disc">Chuẩn hoá <strong>văn hoá – tác phong Unitaxi</strong> (1 bộ chuẩn duy nhất).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80e4-aebf-e9c6c2d284f0" class="bulleted-list"><li style="list-style-type:disc">Duy trì <strong>môi trường làm việc an toàn, ổn định, ít stress.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80f9-af10-ddbb363478ed" class="bulleted-list"><li style="list-style-type:disc">Xây <strong>niềm tự hào và gắn bó</strong> với Unitaxi như “ngôi nhà nghề nghiệp”.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8025-96b2-eb7e14ec66e4" class="bulleted-list"><li style="list-style-type:disc">Đủ cấu trúc để <strong>đào tạo lại (re-training) 30% lực lượng/tháng</strong> mà không làm vỡ vận hành.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-8053-abf0-c26f26b5f9b4"/></div><div style="display:contents" dir="auto"><h2 id="2aec5e6f-95bd-800f-9252-ef68fc6b1437" class=""><strong>II. Mô hình phân bổ 48 giờ (lý thuyết)</strong></h2></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-801d-85fb-d7ee6470fcc9" class="bulleted-list"><li style="list-style-type:disc"><strong>Nền tảng chung (16 giờ)</strong> – tất cả các nhóm cùng học.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8016-966a-eb34093c6058" class="bulleted-list"><li style="list-style-type:disc"><strong>Chuyên môn theo vị trí (20 giờ)</strong> – tách 3 nhóm: Tài xế / Điều phối / Kỹ thuật.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8072-be1d-ff17c549e601" class="bulleted-list"><li style="list-style-type:disc"><strong>Tình huống &amp; ôn tập lý thuyết (8 giờ)</strong> – dùng tình huống giấy, thảo luận, không mô phỏng thực tế.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80d4-b824-e64e737035a2" class="bulleted-list"><li style="list-style-type:disc"><strong>Đánh giá – phản hồi – cam kết (4 giờ)</strong> – test lý thuyết và trao đổi cá nhân.</li></ul></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8093-8f74-c644ff49ce57" class="">Tổng: <strong>16 + 20 + 8 + 4 = 48 giờ</strong> cho mỗi học viên.</p></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-8021-93da-f94703f5d7c4"/></div><div style="display:contents" dir="auto"><h2 id="2aec5e6f-95bd-8041-8ac6-e30b898ff700" class=""><strong>III. Nội dung nền tảng chung (16 giờ)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80a6-ac07-ce785b677453" class=""><strong>1. Bối cảnh &amp; sứ mệnh Unitaxi (2 giờ)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80bf-9570-dfae26838ae4" class="bulleted-list"><li style="list-style-type:disc">Vì sao Unitaxi chọn xe điện.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-805c-a64d-f7f87f831305" class="bulleted-list"><li style="list-style-type:disc">Vai trò của giao thông xanh trong đô thị.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8033-9933-e201bb0d88f6" class="bulleted-list"><li style="list-style-type:disc">Mối liên kết giữa tài xế – điều phối – kỹ thuật.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80be-b168-c95c274f220e" class="bulleted-list"><li style="list-style-type:disc">Mỗi người là <strong>“gương mặt của Unitaxi”</strong> trước khách và cộng đồng.</li></ul></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-808b-a6db-f0423d76d6f4"/></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80c3-962c-e087ec62ccde" class=""><strong>2. Văn hoá – tác phong Unitaxi (4 giờ)</strong></h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-8088-b19e-c9b42340e46f" class=""><strong>8 chuẩn văn hoá – tác phong cốt lõi:</strong></p></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8041-a06f-f47f32b5c83a" class="numbered-list" start="1"><li><strong>An toàn trước – sau – luôn luôn.</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8075-98af-fc08cf449ae7" class="numbered-list" start="2"><li><strong>Đúng giờ &amp; tôn trọng cam kết.</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-808b-a820-eb7f6a399d48" class="numbered-list" start="3"><li><strong>Không gian dễ chịu cho cơ thể khách:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ff-8392-f256b872807d" class="bulleted-list"><li style="list-style-type:disc">xe sạch, không mùi khó chịu</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8040-88e5-f459a95dc7b1" class="bulleted-list"><li style="list-style-type:disc">nhiệt độ ổn, âm lượng vừa phải.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8013-8c2e-dbc09978d151" class="numbered-list" start="4"><li><strong>Tôn trọng trong giao tiếp:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ca-8a48-c469cd30f9a5" class="bulleted-list"><li style="list-style-type:disc">giọng nói đều, không quát, không tranh cãi, không phán xét.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-809f-ae2d-c4fceb1f0894" class="numbered-list" start="5"><li><strong>Trung thực với hệ thống</strong> (dữ liệu, báo cáo, tài sản).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8022-8ec6-edd62e359685" class="numbered-list" start="6"><li><strong>Kỷ luật giờ giấc &amp; quy trình:</strong> đến đúng giờ, làm đúng quy trình, không “lách”.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8021-9fb4-ffec66af33d4" class="numbered-list" start="7"><li><strong>Chú ý chi tiết:</strong> để ý từng chi tiết nhỏ (mùi xe, thảm, ghế, cửa, ánh sáng, ứng dụng).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-809e-8ecb-cf04f78d1716" class="numbered-list" start="8"><li><strong>Tự hào khi mặc đồng phục Unitaxi:</strong> ăn mặc gọn gàng, sạch sẽ, tư thế đứng – đi – mở cửa toát lên sự tự trọng.</li></ol></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-800e-8f93-f5c26d893348"/></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8096-9059-f9f54bd3fdfe" class=""><strong>3. An toàn &amp; pháp lý (4 giờ)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8074-962f-cf9eb46085e5" class="bulleted-list"><li style="list-style-type:disc">Luật giao thông đường bộ liên quan trực tiếp.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80b2-a86b-dc9c54bcda41" class="bulleted-list"><li style="list-style-type:disc">Quy định về xe điện, cháy nổ, sạc.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8038-832a-ddb3f0461fc4" class="bulleted-list"><li style="list-style-type:disc">Quy định về bảo vệ trẻ em (đưa đón học sinh).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-804b-ad2f-f900ee364df2" class="bulleted-list"><li style="list-style-type:disc">Quy định về rượu bia, ma tuý, camera, ghi âm.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80e9-a246-fc129a7801db" class="bulleted-list"><li style="list-style-type:disc">Quy tắc tuyệt đối:<div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8075-9fc0-e361c74cc6e7" class="bulleted-list"><li style="list-style-type:circle">không lái khi thiếu ngủ, có chất kích thích</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80b7-8b16-fae72faec197" class="bulleted-list"><li style="list-style-type:circle">không làm thêm ca khi đã chạm giới hạn giờ lái an toàn của công ty.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-806e-9b33-e98d36b7b86d" class=""><strong>Đánh giá:</strong></p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80c6-a717-c96859a56173" class="bulleted-list"><li style="list-style-type:disc">Bài test tình huống trên giấy, phân tích tình huống thực tế.</li></ul></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-80a7-b6a3-eee032f23bd1"/></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80d2-a9c6-f9e2b3f2c8d9" class=""><strong>4. Giao tiếp &amp; xử lý xung đột (3 giờ)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-809b-8067-e841a5d8a110" class="bulleted-list"><li style="list-style-type:disc">Cách lắng nghe, cách xin lỗi, cách giải thích ngắn – rõ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80d0-8a9d-c99116bb1259" class="bulleted-list"><li style="list-style-type:disc">Xử lý khách say, khách nóng tính, khách phàn nàn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8077-a930-d7013cd7994f" class="bulleted-list"><li style="list-style-type:disc">Khi nào phải gọi điều phối / an ninh / công an.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8010-b142-cda60923a06b" class="bulleted-list"><li style="list-style-type:disc"><strong>Giọng nói &amp; nhịp nói an toàn:</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80d8-900c-c62f97ceb530" class="bulleted-list"><li style="list-style-type:circle">nói chậm hơn khi tình huống căng thẳng</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-806e-b67b-e3a657e5c8d5" class="bulleted-list"><li style="list-style-type:circle">không cắt lời, không nâng tông.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8060-923a-c06d3d9e17e5" class="bulleted-list"><li style="list-style-type:disc"><strong>Kỷ luật ngôn từ:</strong> không nói tục, không đùa nhạy cảm, không “dạy đời” khách.</li></ul></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-803b-a485-fe83abb4d39d" class=""><strong>Mục tiêu:</strong> mỗi người có <strong>3–5 câu mẫu</strong> an toàn, dùng được ngay (học thuộc và làm bài test).</p></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-8000-8c2d-e1681027e1f4"/></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-8098-b563-f8041b3d975c" class=""><strong>5. Giới thiệu hệ thống công nghệ Unitaxi (3 giờ)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80fd-9ab4-f39d98562546" class="bulleted-list"><li style="list-style-type:disc">Ứng dụng dành cho tài xế, màn hình điều phối, hệ thống giám sát xe &amp; trạm (giới thiệu khái niệm, luồng chính).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80b3-88c8-c93ca35c9b93" class="bulleted-list"><li style="list-style-type:disc">Cách báo lỗi, cách gửi phản hồi qua hệ thống.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-801a-beb4-c173a6ac2ad8" class="bulleted-list"><li style="list-style-type:disc">Nguyên tắc: <strong>“Không nói miệng – mọi thứ chỉ được ghi nhận trên báo cáo và dữ liệu.”</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-80b4-87de-f891c49ac7d6"/></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80d7-9971-e4e198847c27" class=""><strong>6. Sức khoẻ – năng lượng – tập trung trong ca làm việc (4 giờ)</strong></h3></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80c2-82ab-d047887170a4" class="">Áp dụng cho <strong>cả 3 nhóm</strong>.</p></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-806c-b25b-c17775957992" class="bulleted-list"><li style="list-style-type:disc">Tư thế ngồi – đứng chuẩn để tránh mỏi, đau lưng, tê tay.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-801e-89fc-e67d5104b030" class="bulleted-list"><li style="list-style-type:disc">Thói quen khởi động 5 phút trước ca.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80a2-8b59-ed0a75ccec8f" class="bulleted-list"><li style="list-style-type:disc">Quy tắc <strong>nghỉ ngắn 5–10 phút</strong> sau mỗi 3–4 giờ làm việc liên tục.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8080-83b3-d32f0c8c5493" class="bulleted-list"><li style="list-style-type:disc">Cách giữ tỉnh táo:<div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ff-b48f-e7f74d368716" class="bulleted-list"><li style="list-style-type:circle">uống nước chia nhỏ</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80a3-b38e-ec62b32bda6b" class="bulleted-list"><li style="list-style-type:circle">tránh ăn quá no trước khi lái</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80a4-8192-f21eae7f1388" class="bulleted-list"><li style="list-style-type:circle">không dùng điện thoại giải trí liên tục giữa ca.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8054-b107-f832b1d058e5" class="bulleted-list"><li style="list-style-type:disc">3–4 bài tập thở đơn giản giúp hạ căng thẳng trong 1–2 phút (giới thiệu lý thuyết, hướng dẫn miệng).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80f7-8e6b-dd632265f593" class="bulleted-list"><li style="list-style-type:disc">Cách tự nhận biết khi mình mất tập trung và quy trình báo điều phối để đổi ca / nghỉ.</li></ul></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-8053-bcc7-ef82b501c88e"/></div><div style="display:contents" dir="auto"><h2 id="2aec5e6f-95bd-8067-8477-ef407b8bcddf" class=""><strong>IV. Nội dung chuyên môn theo vị trí (20 giờ)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-80d6-b943-d7d8f9faba64" class=""><strong>1. Nội dung cho Tài xế (20 giờ)</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-80b4-9265-ddeb8fbd10f7" class="numbered-list" start="1"><li><strong>Vận hành xe điện chuyên sâu (6 giờ)</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8019-b60a-ecc56c4408b1" class="bulleted-list"><li style="list-style-type:disc">Cấu tạo cơ bản, pin, phanh tái sinh.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80b3-a8ea-c5799b857118" class="bulleted-list"><li style="list-style-type:disc">Cách đọc cảnh báo, quy trình dừng xe an toàn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8054-b1bf-d970c7bdf772" class="bulleted-list"><li style="list-style-type:disc">Quy trình trước – trong – sau ca.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-807e-ae88-e6dacbb35fa0" class="bulleted-list"><li style="list-style-type:disc">Tiêu chuẩn vệ sinh &amp; mùi trong xe, kiểm tra nhanh trước mỗi chuyến.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-800f-8c8e-c64d6eb5abad" class="numbered-list" start="2"><li><strong>Lái xe an toàn nâng cao &amp; chống mệt mỏi (6 giờ)</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-805e-8b51-d3a8f874796f" class="bulleted-list"><li style="list-style-type:disc">Kỹ thuật phòng vệ, khoảng cách an toàn, phản xạ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8068-9905-d2ed7885de02" class="bulleted-list"><li style="list-style-type:disc">Lái trong mưa, ngập, tầm nhìn kém; lái đêm, gần trường học/bệnh viện.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-802b-9459-cc961be64d80" class="bulleted-list"><li style="list-style-type:disc">Quy tắc:<div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-803d-99d5-de22e6c07f38" class="bulleted-list"><li style="list-style-type:circle">không lái liên tục quá số giờ quy định</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8064-ae5f-e0350b46c944" class="bulleted-list"><li style="list-style-type:circle">cách xử lý khi thấy buồn ngủ, hoa mắt, chóng mặt.</li></ul></div></li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8037-a708-f3fe955f1769" class="numbered-list" start="3"><li><strong>Quản lý hành trình, thu nhập &amp; năng lượng (4 giờ)</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8027-92d0-fd2de2f6066c" class="bulleted-list"><li style="list-style-type:disc">Đọc bản đồ, tránh đường kẹt, tránh đi vòng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80cc-ad93-e2f162d575de" class="bulleted-list"><li style="list-style-type:disc">Quản lý giờ cao điểm – thấp điểm.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80e8-a778-ef7bdd00e923" class="bulleted-list"><li style="list-style-type:disc">Cách tối ưu thu nhập mà không gian dối (tránh “vòng vo”, huỷ cuốc…).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80e4-a39a-c750ff00023d" class="bulleted-list"><li style="list-style-type:disc">Cách phân bổ ca để không kiệt sức cuối ngày.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8056-b381-d4672556d35c" class="numbered-list" start="4"><li><strong>Chăm sóc học sinh &amp; khách đặc biệt (4 giờ)</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-803b-962f-cc65fd830188" class="bulleted-list"><li style="list-style-type:disc">Quy trình điểm danh, bàn giao, xử lý trẻ khóc, trễ giờ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ae-a782-df64d2eeb21c" class="bulleted-list"><li style="list-style-type:disc">Chăm sóc người già, người khuyết tật, phụ nữ mang thai.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ae-9d45-eb9978d197eb" class="bulleted-list"><li style="list-style-type:disc">Cách trấn an khi khách lo lắng / say xe:<div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80c3-9192-cfab1eacba30" class="bulleted-list"><li style="list-style-type:circle">giọng nói chậm</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80b4-b7d7-ce855302f951" class="bulleted-list"><li style="list-style-type:circle">thông báo quãng đường &amp; thời gian còn lại</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8062-80b4-fa7f315b446e" class="bulleted-list"><li style="list-style-type:circle">điều chỉnh nhiệt độ, mở/đóng cửa sổ phù hợp.</li></ul></div></li></ul></div></li></ol></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-80f6-8d46-dc18f2fdec1e" class=""><em>(Tất cả ở mức giảng giải lý thuyết, hỏi – đáp; không mô phỏng lái thử.)</em></p></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-8081-8689-dd5661cadd1f"/></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-801b-a2e6-dd79aae4765f" class=""><strong>2. Nội dung cho Điều phối (20 giờ)</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8022-a5d8-df8eb9e173f8" class="numbered-list" start="1"><li><strong>Tư duy điều phối – tài xế là khách hàng nội bộ (4 giờ)</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-805b-8dd2-d284bc2e0c6c" class="bulleted-list"><li style="list-style-type:disc">Điều phối là người <strong>giải bài toán</strong>, không phải “ra lệnh”.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80b0-8d18-df0c1ead8ed4" class="bulleted-list"><li style="list-style-type:disc">Nguyên tắc giao tiếp: rõ – ngắn – tôn trọng – bình tĩnh.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-801f-9d40-f30988462667" class="numbered-list" start="2"><li><strong>Sử dụng hệ thống điều phối Unitaxi (6 giờ)</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80f1-8976-e0664742b61b" class="bulleted-list"><li style="list-style-type:disc">Màn hình điều phối, bản đồ, ưu tiên chuyến, gán xe (mô tả luồng công việc).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80c0-be54-d2587f334c64" class="bulleted-list"><li style="list-style-type:disc">Đọc cảnh báo: xe sắp hết pin, trạm quá tải, khu vực rủi ro.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8095-a51c-f05811d7dc5c" class="numbered-list" start="3"><li><strong>Quản lý ca, giờ, km rỗng &amp; tải thần kinh (4 giờ)</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-802c-b18c-f579464c9082" class="bulleted-list"><li style="list-style-type:disc">Nguyên tắc phân ca công bằng, an toàn.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8040-8985-e2d5c9cf68e3" class="bulleted-list"><li style="list-style-type:disc">Giảm km rỗng bằng bố trí khu vực, trạm sạc, điểm đón.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80f1-b7b8-ff5e22581a47" class="bulleted-list"><li style="list-style-type:disc">Theo dõi giờ lái để nhắc tài xế nghỉ ngắn, đổi ca khi cần.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8005-8951-e2511d054a19" class="numbered-list" start="4"><li><strong>Xử lý sự cố &amp; khủng hoảng (4 giờ)</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80fd-aaeb-c5de59e3e104" class="bulleted-list"><li style="list-style-type:disc">Tai nạn, khách khiếu nại, phương tiện hỏng, tắc đường diện rộng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80a4-a0af-f656e1a89c42" class="bulleted-list"><li style="list-style-type:disc">Kịch bản từng bước, ai gọi ai, ghi nhận ra sao.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ae-a9af-e6cd4ad6960c" class="bulleted-list"><li style="list-style-type:disc">Giữ giọng nói ổn định, không đổ lỗi, không kích động.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-800a-9b4b-dae47101072c" class="numbered-list" start="5"><li><strong>Báo cáo &amp; học từ dữ liệu (2 giờ)</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8038-9283-d42b5e38ab78" class="bulleted-list"><li style="list-style-type:disc">Báo cáo cuối ca / cuối ngày.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ea-b503-d5ee04420908" class="bulleted-list"><li style="list-style-type:disc">Đọc số liệu: tỉ lệ hoàn thành chuyến, tỉ lệ huỷ, thời gian chờ, số giờ lái, lỗi an toàn.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-80ff-aa16-c85b7bede4e1"/></div><div style="display:contents" dir="auto"><h3 id="2aec5e6f-95bd-807c-825b-ec0da259ab69" class=""><strong>3. Nội dung cho Kỹ thuật (xe + trạm sạc) (20 giờ)</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8004-9895-f84e2e9983b9" class="numbered-list" start="1"><li><strong>Nguyên lý hệ thống xe điện &amp; trạm sạc (6 giờ)</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8007-b709-fbbcb7b68495" class="bulleted-list"><li style="list-style-type:disc">Cấu trúc trạm, kết nối điện lực, hệ thống bảo vệ.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80b6-a4e4-c0c42b5dcd23" class="bulleted-list"><li style="list-style-type:disc">Lỗi thường gặp và mức độ nghiêm trọng.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8088-be52-e7cb43a55c50" class="numbered-list" start="2"><li><strong>Bảo trì định kỳ &amp; bảo trì chủ động (6 giờ)</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-807e-b477-d2cef302212c" class="bulleted-list"><li style="list-style-type:disc">Lịch bảo dưỡng theo km, theo thời gian.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8094-b537-e30593e56c35" class="bulleted-list"><li style="list-style-type:disc">Danh mục kiểm tra trước khi giao xe / bàn giao trạm.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80c7-b286-f8499c8493c1" class="bulleted-list"><li style="list-style-type:disc">Sử dụng hệ thống cảnh báo từ xa (ở mức hiểu khái niệm).</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-80be-9e68-e1d18d99d884" class="numbered-list" start="3"><li><strong>An toàn điện &amp; xử lý sự cố (4 giờ)</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8018-9fef-de07dce25a8b" class="bulleted-list"><li style="list-style-type:disc">Cháy nổ, chập điện, nước ngập trạm, tai nạn khi sạc.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-809b-b804-dcd506b45742" class="bulleted-list"><li style="list-style-type:disc">Phong toả khu vực, báo lực lượng chức năng, báo điều phối.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80d0-9b5c-e1d0ddf152fb" class="bulleted-list"><li style="list-style-type:disc">Quy định về bảo hộ khi làm việc với điện, nhiệt, pin.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8045-9b31-d69bb97e3bc6" class="numbered-list" start="4"><li><strong>Giao tiếp với tài xế &amp; điều phối (4 giờ)</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-809b-a39f-ced6b6c3bcb8" class="bulleted-list"><li style="list-style-type:disc">Giải thích lỗi bằng ngôn ngữ dễ hiểu, không kỹ thuật hoá quá mức.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8051-8126-c8d9a31946ac" class="bulleted-list"><li style="list-style-type:disc">Nhận thông tin từ điều phối, phản hồi rõ – ngắn – đúng thời gian.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8079-93f5-d689aecf2130" class="bulleted-list"><li style="list-style-type:disc">Không để tài xế/khách chờ lâu mà không có thông tin.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-80a2-b0aa-cb6d965cd86f"/></div><div style="display:contents" dir="auto"><h2 id="2aec5e6f-95bd-809e-83b0-f3d928226bfb" class=""><strong>V. Tình huống &amp; ôn tập lý thuyết (8 giờ)</strong></h2></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80d1-a2b6-f69a81cc25b6" class="bulleted-list"><li style="list-style-type:disc">Phân tích chuỗi tình huống tai nạn thường gặp.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-800b-a73a-c624ac2b0396" class="bulleted-list"><li style="list-style-type:disc">Phân tích các tình huống giao tiếp khó với khách.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80da-9c89-fd45ead9f63b" class="bulleted-list"><li style="list-style-type:disc">Phân tích các tình huống kỹ thuật – sạc – pin.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8089-bc37-fdaa84abdffa" class="bulleted-list"><li style="list-style-type:disc">Phân tích các tình huống điều phối: thừa xe, thiếu xe, trễ giờ, khách phàn nàn.</li></ul></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-8029-a545-ca70be8eca11"/></div><div style="display:contents" dir="auto"><h2 id="2aec5e6f-95bd-8089-890a-f0187a5a588e" class=""><strong>VI. Đánh giá – phản hồi – cam kết (4 giờ)</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-803b-b149-f5a0eada3ef0" class="numbered-list" start="1"><li><strong>Bài test lý thuyết (1 giờ)</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8013-8631-cd476179a1c1" class="bulleted-list"><li style="list-style-type:disc">An toàn, pháp lý, quy trình, văn hoá, quy tắc giờ làm – nghỉ.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-807a-8d52-f5a5b315bfa7" class="numbered-list" start="2"><li><strong>Đánh giá qua câu hỏi tình huống (1 giờ)</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8073-a7a4-fd21f8e7d0d0" class="bulleted-list"><li style="list-style-type:disc">Tài xế / điều phối / kỹ thuật trả lời cách xử lý theo từng kịch bản.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8009-9e13-ef345e240fe3" class="numbered-list" start="3"><li><strong>Phản hồi 1–1 (1 giờ)</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ae-a52d-d83822a631de" class="bulleted-list"><li style="list-style-type:disc">Trainer trao đổi: điểm mạnh, điểm cần cải thiện, kế hoạch 1 tháng.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8038-a442-d6dcc22fb14c" class="numbered-list" start="4"><li><strong>Cam kết &amp; xếp hạng nội bộ (1 giờ)</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80a1-9fa1-db3cfa4ce1e0" class="bulleted-list"><li style="list-style-type:disc">Ký cam kết chuẩn văn hoá – an toàn – giờ làm việc lành mạnh.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80e5-9fac-e139fbec742b" class="bulleted-list"><li style="list-style-type:disc">Xếp hạng: Đạt / Đạt có điều kiện / Cần đào tạo lại.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-80f2-9eb6-dc1e7305f626"/></div><div style="display:contents" dir="auto"><h2 id="2aec5e6f-95bd-8097-ab82-f9bcd0497a97" class=""><strong>VII. Cơ chế đào tạo lại 30% lực lượng / tháng</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-80eb-9307-d5e3e06e70f6" class="numbered-list" start="1"><li><strong>Cách chọn 30%</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-805d-ba47-d6630c70a52f" class="bulleted-list"><li style="list-style-type:disc">10%: nhân sự mới &lt; 6 tháng.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80ab-9ce7-e181dfe365a9" class="bulleted-list"><li style="list-style-type:disc">10%: chỉ số thấp (khách phàn nàn, tai nạn nhỏ, vi phạm quy trình).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-805a-91e4-e3e838e020ab" class="bulleted-list"><li style="list-style-type:disc">10%: chọn ngẫu nhiên.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-80e3-afb5-fbdaec02028d" class="numbered-list" start="2"><li><strong>Nội dung đào tạo lại (~6–8 giờ/người/tháng)</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8068-9ee7-c017b91184fb" class="bulleted-list"><li style="list-style-type:disc">Cập nhật quy định &amp; thay đổi vận hành (2 giờ).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-801e-b67e-cf994c0a6b2c" class="bulleted-list"><li style="list-style-type:disc">Ôn lại 8 chuẩn văn hoá – tác phong qua tình huống thực tế (2 giờ).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80e3-9c2c-f721834faf7d" class="bulleted-list"><li style="list-style-type:disc">Ôn 1–2 kịch bản sự cố trên giấy, tập trung vào giữ bình tĩnh, giọng nói, an toàn (2 giờ).</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-80e4-bc19-e8bc917f428e" class="bulleted-list"><li style="list-style-type:disc">Phản hồi cá nhân từ dữ liệu 30 ngày (1–2 giờ):<div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-801a-ba17-e2f188221bf5" class="bulleted-list"><li style="list-style-type:circle">điểm khách, tỉ lệ huỷ, thời gian chờ, lỗi an toàn, giờ làm việc.</li></ul></div></li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8054-aead-debfc1c5ae8b" class="numbered-list" start="3"><li><strong>Công cụ hỗ trợ</strong><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-8031-9b57-cbe896e19507" class="bulleted-list"><li style="list-style-type:disc">Nhóm trao đổi nội bộ (ví dụ: Zalo) để chia sẻ tình huống hay, kinh nghiệm tốt.</li></ul></div><div style="display:contents" dir="auto"><ul id="2aec5e6f-95bd-808a-b69f-d851a350d629" class="bulleted-list"><li style="list-style-type:disc">Cơ chế <strong>“tài xế hướng dẫn tài xế”</strong>: tài xế tốt kèm 1–2 tài xế mới.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-806e-9231-f03d81dbc3e1"/></div><div style="display:contents" dir="auto"><h2 id="2aec5e6f-95bd-80d4-8b13-f3f9aca2ad53" class=""><strong>VIII. Chuẩn hoá văn hoá – tác phong Unitaxi trong mọi lớp</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8035-acaa-f028cd810d41" class="numbered-list" start="1"><li>Mọi phần nội dung đều gắn về <strong>8 chuẩn văn hoá – tác phong</strong>.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8063-91f3-cc6a0a5808e1" class="numbered-list" start="2"><li>Trainer là người sống đúng chuẩn, không chỉ dạy bằng lời.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8074-9704-cee3e08a8a02" class="numbered-list" start="3"><li>Mọi vi phạm được ghi nhận bằng dữ liệu, không xử lý theo cảm tính.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8005-9b3d-cfe5f5a7a2e6" class="numbered-list" start="4"><li>Khen thưởng gắn với <strong>an toàn – văn hoá – kỷ luật – chú ý chi tiết</strong>, không chỉ doanh thu.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2aec5e6f-95bd-8055-8c88-ee70c43e5db5" class="numbered-list" start="5"><li>Câu chuyện tích cực được kể lại định kỳ (tài xế trả lại đồ, xử lý sự cố, chăm sóc học sinh tốt…) để xây <strong>niềm tự hào và lòng trung thành</strong> với Unitaxi.</li></ol></div><div style="display:contents" dir="auto"><p id="2aec5e6f-95bd-807f-a3fa-cbd082494e47" class="">
</p></div><div style="display:contents" dir="auto"><hr id="2aec5e6f-95bd-80ab-b2dd-ced13fae02a6"/></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
