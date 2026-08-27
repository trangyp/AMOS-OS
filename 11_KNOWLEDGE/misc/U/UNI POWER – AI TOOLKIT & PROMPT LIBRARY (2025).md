---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>UNI POWER – AI TOOLKIT &amp; PROMPT LIBRARY (2025)</title><style>
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
	
</style></head><body><article id="291c5e6f-95bd-8066-83bf-c92b8a1dbc15" class="page sans"><header><h1 class="page-title" dir="auto"><strong>UNI POWER – AI TOOLKIT &amp; PROMPT LIBRARY (2025)</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-8096-bbe9-ceac9c1350bc" class=""><strong>Phân nhóm theo loại công việc</strong></p></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-805e-92b7-d8562dce7c48" class=""><em>(Chuẩn hóa cho môi trường doanh nghiệp năng lượng &amp; vận tải thông minh)</em></p></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-80d8-b501-e50646607466"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-80bd-bdb8-e7185594423a" class=""><strong>🔹 1️⃣ LÃNH ĐẠO &amp; BOD (Executive Decision &amp; Strategy)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-80e5-a2c0-cb923ec5f938" class=""><strong>🔧 Công cụ AI</strong></h3></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-802a-9de7-c763f2a32b99" class="bulleted-list"><li style="list-style-type:disc"><strong>ChatGPT Enterprise / Claude 3.5 / Gemini Advanced:</strong> tóm tắt, dự báo, chiến lược</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80e4-9283-f7953a1b35a8" class="bulleted-list"><li style="list-style-type:disc"><strong>Perplexity AI:</strong> cập nhật tin tức ngành nhanh</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8035-93d1-e589146cc48c" class="bulleted-list"><li style="list-style-type:disc"><strong>Microsoft Copilot / Notion AI:</strong> viết báo cáo, ghi chú, biên bản</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80ec-90d5-d29cd150691b" class="bulleted-list"><li style="list-style-type:disc"><strong>Power BI + Copilot:</strong> dashboard tự động, phân tích KPI</li></ul></div><div style="display:contents" d
ir="auto"><h3 id="291c5e6f-95bd-80b3-b210-d1a98f3200e7" class=""><strong>💼 Nhiệm vụ</strong></h3></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8089-90c6-c4c7f3154ff6" class="bulleted-list"><li style="list-style-type:disc">Tạo báo cáo tuần/tháng cho BOD</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-803d-addf-e2dd2ddc97e1" class="bulleted-list"><li style="list-style-type:disc">Phân tích rủi ro tài chính &amp; vận hành</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-806f-bc50-c0c91932ba06" class="bulleted-list"><li style="list-style-type:disc">Viết thông điệp nội bộ &amp; kế hoạch truyền thông</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80b9-8ee0-c5991e75df61" class="bulleted-list"><li style="list-style-type:disc">Tạo 3 kịch bản chiến lược (base / optimistic / stress)</li></ul></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-8078-be84-fad746b8d09a" class=""><strong>💬 Prompts mẫu</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-8009-ba78-d6b630a11f63" class="numbered-list" start="1"><li>“Tạo <strong>bản tóm tắt điều hành</strong> 1 trang: gồm 5 chỉ số chính, 3 rủi ro, và 3 đề xuất hành động.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-80d9-aaba-e757f9bd5b3f" class="numbered-list" start="2"><li>“Phân tích xu hướng <strong>ngành xe điện Việt Nam 2025–2027</strong>, chia theo chính sách, hạ tầng, hành vi tiêu dùng.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-80a5-9363-e2a0601bf82c" class="numbered-list" start="3"><li>“Từ dữ liệu doanh thu &amp; chi phí tháng này, tạo <strong>3 kịch bản dòng tiền</strong> (base / bull / bear).”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-802a-ae93-f122c5679a45" class="numbered-list" start="4"><li>“Viết <strong>thông điệp CEO</strong> 
00 từ cho nhân viên, giọng chân thực, cảm hứng, không khoa trương.”</li></ol></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-804a-baf1-db93e5c74fb0"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-80c0-abfc-f7470c9fda80" class=""><strong>🔹 2️⃣ TÀI CHÍNH &amp; ĐẦU TƯ (Finance &amp; UniFinance)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-80cb-8901-e30defe51c7d" class=""><strong>🔧 Công cụ AI</strong></h3></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80f2-99eb-df324b63f054" class="bulleted-list"><li style="list-style-type:disc"><strong>ChatGPT + Excel Copilot</strong>: phân tích chi phí &amp; lợi nhuận</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80b9-940b-e7f7c321ebba" class="bulleted-list"><li style="list-style-type:disc"><strong>Power BI + Copilot / Tableau GPT:</strong> theo dõi dòng tiền &amp; KPI</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80e3-925a-f3642c1b197c" class="bulleted-list"><li style="list-style-type:disc"><strong>Klarity / MindBridge AI:</strong> phát hiện sai lệch kế toán</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-804d-b376-ecd558d25a06" class="bulleted-list"><li style="list-style-type:disc"><strong>Revolut AI Finance / Ramp AI:</strong> dự báo chi tiêu, phát hiện bất thường</li></ul></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-8076-b086-ca33ca5e540e" class=""><strong>💼 Nhiệm vụ</strong></h3></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80e7-9798-f3d314e71c1a" class="bulleted-list"><li style="list-style-type:disc">Dự báo dòng tiền 12 tuần</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8032-9599-d974d6c11025" class="bulleted-list"><li style="list-style-type:disc">Đối soát doanh thu theo trạm / đội xe</li></ul></div><div style="display:contents" dir="auto"><ul i
d="291c5e6f-95bd-80b0-9f11-c53741344b0e" class="bulleted-list"><li style="list-style-type:disc">Phân tích ROI của mô hình EaaS (Energy-as-a-Service)</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8087-93ca-ddd795ae58f7" class="bulleted-list"><li style="list-style-type:disc">Phát hiện giao dịch ví năng lượng bất thường</li></ul></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-807d-8a54-c3c92d3950dd" class=""><strong>💬 Prompts mẫu</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-8085-ab6d-e4927f75d9c4" class="numbered-list" start="1"><li>“Phân tích dữ liệu chi phí vận hành và gợi ý <strong>3 cách giảm 10% chi phí điện năng</strong>.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-8019-85ea-f55830c8b04c" class="numbered-list" start="2"><li>“Tạo <strong>báo cáo P&amp;L</strong> tháng này cho UniPower, chia theo khu vực, định dạng trình BOD.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-8056-99f5-dff8fe5e0532" class="numbered-list" start="3"><li>“Dự báo <strong>dòng tiền 12 tuần tới</strong>, cảnh báo nếu ngân quỹ &lt; 8 tuần.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-8021-aa07-cfba1d564d92" class="numbered-list" start="4"><li>“Phát hiện các <strong>mẫu giao dịch bất thường</strong> trong ví năng lượng UniPower Wallet.”</li></ol></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-80ae-9c2c-d7214ba7284e"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-80c4-9635-cba8a8e6bfae" class=""><strong>🔹 3️⃣ VẬN HÀNH TRẠM SẠC &amp; NĂNG LƯỢNG (UniCharge / Energy Ops)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-8068-b613-edd5f7de604a" class=""><strong>🔧 Công cụ AI</strong></h3></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-801f-a77a-c5ef8873da1d" c
lass="bulleted-list"><li style="list-style-type:disc"><strong>Power BI + IoT Data Connector</strong>: giám sát uptime</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-804d-a769-f732acb9dd93" class="bulleted-list"><li style="list-style-type:disc"><strong>ChatGPT Vision / Gemini Pro Vision:</strong> phân tích ảnh trạm sạc (camera / lỗi hiển thị)</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80d2-a302-daf9b7087a68" class="bulleted-list"><li style="list-style-type:disc"><strong>Octopus Energy Kraken AI:</strong> mô hình tariff linh hoạt</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8076-818d-d88b0d756bdb" class="bulleted-list"><li style="list-style-type:disc"><strong>Zapier / Make + OCPP API:</strong> tự động báo lỗi &amp; tạo ticket</li></ul></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-80a6-a437-c7b0a0ca1169" class=""><strong>💼 Nhiệm vụ</strong></h3></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8043-8fb3-eda9614c7b64" class="bulleted-list"><li style="list-style-type:disc">Giám sát trạm sạc theo thời gian thực</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8084-a1d1-c3166ed01bfc" class="bulleted-list"><li style="list-style-type:disc">Phát hiện connector lỗi, quá tải, hay mất tín hiệu</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-807a-ad92-f4950337cf16" class="bulleted-list"><li style="list-style-type:disc">Tối ưu chi phí điện giờ cao điểm</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80c0-a3f6-cdc9b743065e" class="bulleted-list"><li style="list-style-type:disc">Tạo lịch bảo trì định kỳ tự động</li></ul></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-808b-881e-fff22bb77121" class=""><strong>💬 Prompts mẫu</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-8028-9a82-ce4d71ec4ad6" c
lass="numbered-list" start="1"><li>“Từ dữ liệu OCPP tuần này, tạo <strong>báo cáo Uptime</strong> từng trạm &amp; highlight 3 trạm dưới 97%.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-80b5-9ef5-d5afb968e7e6" class="numbered-list" start="2"><li>“Phân tích nguyên nhân <strong>trạm lỗi nhiều nhất</strong>, chia theo phần cứng / phần mềm / điện áp.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-802a-9b5a-e3710fd274ba" class="numbered-list" start="3"><li>“Gợi ý <strong>khung giờ sạc rẻ nhất</strong> và ước tính tiết kiệm chi phí 7 ngày tới.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-80ca-a516-d6b585ee47f1" class="numbered-list" start="4"><li>“Tạo <strong>checklist bảo trì trạm sạc 15 điểm</strong>, định dạng bảng dễ in.”</li></ol></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-8039-a237-dc458ea62dcb"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-804c-9b00-d020ddb5955d" class=""><strong>🔹 4️⃣ ĐỘI XE &amp; TÀI XẾ (Fleet Management / Driver Ops)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-80ac-97ce-fc5e22926e59" class=""><strong>🔧 Công cụ AI</strong></h3></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-800f-a863-c3f7cb557bb6" class="bulleted-list"><li style="list-style-type:disc"><strong>ChatGPT Vision + Map API:</strong> phân tích hành trình, quãng đường</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80d6-a15e-dfe46a208371" class="bulleted-list"><li style="list-style-type:disc"><strong>Otter.ai + Notion AI:</strong> tóm tắt họp đội trưởng</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80fb-8aed-f61122616d51" class="bulleted-list"><li style="list-style-type:disc"><strong>UniOS Dashboard + AI Copilot:</strong> báo cáo xe hoạt động</li></ul></div><div style="display:contents" d
ir="auto"><ul id="291c5e6f-95bd-8011-9e2a-fddb6b82c21d" class="bulleted-list"><li style="list-style-type:disc"><strong>ChatGPT Custom GPT (Driver Coach):</strong> huấn luyện &amp; phản hồi cá nhân</li></ul></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-8033-9b2c-fe1e3c4af055" class=""><strong>💼 Nhiệm vụ</strong></h3></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8090-b416-fb8a03c3d9f1" class="bulleted-list"><li style="list-style-type:disc">Theo dõi hiệu suất tài xế (utilization, an toàn)</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8068-a056-c62fb3028b96" class="bulleted-list"><li style="list-style-type:disc">Gợi ý lịch sạc &amp; nghỉ phù hợp sinh học</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-801d-9257-dc0e02c4c25c" class="bulleted-list"><li style="list-style-type:disc">Tự động nhắc nhở vi phạm (tốc độ, SOC thấp, bảo dưỡng)</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80b9-8d5f-eebe31b3eeb8" class="bulleted-list"><li style="list-style-type:disc">Tạo “coaching note” cho từng đội trưởng</li></ul></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-80ba-9b52-c0b9f29ce94a" class=""><strong>💬 Prompts mẫu</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-80fe-9da6-f6308cbd732e" class="numbered-list" start="1"><li>“Phân tích dữ liệu hành trình 7 ngày, liệt kê <strong>10 tài xế có hiệu suất cao nhất &amp; thấp nhất</strong>.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-80cf-843e-ea9a1451648c" class="numbered-list" start="2"><li>“Tạo <strong>feedback mẫu</strong> cho tài xế vi phạm tốc độ 3 lần/tháng, giọng khích lệ.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-8036-98a6-ddc3f57c238e" class="numbered-list" start="3"><li>“Gợi ý <strong>lịch nghỉ hợp lý</strong> cho đội xe khu vực Q.7 để giảm 
ệt mỏi.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-8099-b19c-e304263ebf21" class="numbered-list" start="4"><li>“Tạo <strong>bảng điểm tài xế</strong> (doanh thu, an toàn, thái độ) – format Excel tự cập nhật.”</li></ol></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-8053-a5a7-e20eff757902"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-8099-a195-ec9d8b54d6b4" class=""><strong>🔹 5️⃣ TUYỂN DỤNG &amp; ĐÀO TẠO (HR &amp; Recruitment AI)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-8086-8e6a-c8e7c541be1a" class=""><strong>🔧 Công cụ AI</strong></h3></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8036-bc51-f62b310ead76" class="bulleted-list"><li style="list-style-type:disc"><strong>HireVue / ChatGPT Interview Bot:</strong> phỏng vấn tự động</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80d3-af04-e131fb611dee" class="bulleted-list"><li style="list-style-type:disc"><strong>Notion AI / Typeform AI:</strong> tạo trắc nghiệm tuyển dụng</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8002-b6a9-ee17cb9cf496" class="bulleted-list"><li style="list-style-type:disc"><strong>Otter.ai / Whisper / Gemini AI:</strong> chấm &amp; tóm tắt phỏng vấn</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-801d-8e85-c237a7acdb7e" class="bulleted-list"><li style="list-style-type:disc"><strong>ChatGPT Fine-tuned:</strong> phản hồi &amp; xếp hạng ứng viên</li></ul></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-8051-8825-ebb1df54ab7e" class=""><strong>💼 Nhiệm vụ</strong></h3></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-804a-a314-d8a91d68f721" class="bulleted-list"><li style="list-style-type:disc">Sàng lọc hồ sơ tài xế tự động (CCCD, GPLX, LLTP)</li></ul></div><div style="display:contents" dir="auto"><ul i
d="291c5e6f-95bd-80f8-847e-ce7313fda80f" class="bulleted-list"><li style="list-style-type:disc">Tạo bộ câu hỏi hành vi &amp; kỹ năng</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8013-8d71-ec9887aaae66" class="bulleted-list"><li style="list-style-type:disc">Viết feedback kết quả phỏng vấn</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-807b-acad-d02a13d74193" class="bulleted-list"><li style="list-style-type:disc">Phân tích pipeline tuyển dụng</li></ul></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-8075-b6ed-d1beb72a3466" class=""><strong>💬 Prompts mẫu</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-80ec-83a7-ea9d8f73e2f7" class="numbered-list" start="1"><li>“Tạo <strong>10 câu hỏi phỏng vấn tài xế EV</strong> về an toàn, dịch vụ, tình huống.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-80cb-8144-ce4643a5c0ef" class="numbered-list" start="2"><li>“Chấm <strong>video phỏng vấn</strong> này và tóm tắt điểm mạnh – điểm yếu trong 150 từ.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-80e0-83d2-d4b80b4b73a8" class="numbered-list" start="3"><li>“Viết <strong>email phản hồi</strong> lịch sự cho ứng viên chưa đạt.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-80e7-af93-f3c0783b0a33" class="numbered-list" start="4"><li>“Phân tích funnel tuyển dụng, xác định vòng rớt nhiều nhất và lý do.”</li></ol></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-8057-93bc-c2dfd1db48a6"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-80b6-a765-ece2d3b78e5d" class=""><strong>🔹 6️⃣ MARKETING &amp; TRUYỀN THÔNG (Marketing / Brand)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-80ef-bbc1-d5e5b92bda83" class=""><strong>🔧 Công cụ AI</strong></h3></div><div s
tyle="display:contents" dir="auto"><ul id="291c5e6f-95bd-8070-8ee9-c5886ca48468" class="bulleted-list"><li style="list-style-type:disc"><strong>ChatGPT / Jasper / Notion AI:</strong> viết bài, thông điệp</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8078-a9be-c2b7459f3f67" class="bulleted-list"><li style="list-style-type:disc"><strong>Canva Magic Write / Gamma.app:</strong> tạo slide / visual</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8038-b0e1-ced6db743210" class="bulleted-list"><li style="list-style-type:disc"><strong>Perplexity / Google Gemini:</strong> phân tích xu hướng</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8011-a4c6-c967f886264f" class="bulleted-list"><li style="list-style-type:disc"><strong>Synthesia / HeyGen:</strong> tạo video AI có giọng nói tiếng Việt</li></ul></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-802d-b960-da531539ea09" class=""><strong>💼 Nhiệm vụ</strong></h3></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80a6-919b-c0d46e313cf0" class="bulleted-list"><li style="list-style-type:disc">Viết nội dung mạng xã hội / bài PR</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8048-90b4-c681747ac2b6" class="bulleted-list"><li style="list-style-type:disc">Tạo hình ảnh, video quảng bá EV</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8010-9f55-de02faceff6b" class="bulleted-list"><li style="list-style-type:disc">Theo dõi phản hồi người dùng &amp; báo cáo sentiment</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-802f-9e6d-db33c0251e9c" class="bulleted-list"><li style="list-style-type:disc">Tạo chiến dịch email tự động</li></ul></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-808b-a22d-d13f7b6c6d6c" class=""><strong>💬 Prompts mẫu</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" i
d="291c5e6f-95bd-80f1-a998-e04f585fc67e" class="numbered-list" start="1"><li>“Viết <strong>bài đăng LinkedIn 200 chữ</strong> về mô hình EaaS của UniPower, giọng chuyên nghiệp.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-8075-acb1-c6dbd9781372" class="numbered-list" start="2"><li>“Tạo <strong>3 ý tưởng chiến dịch marketing</strong> gắn với Ngày Môi trường Thế giới.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-8025-a742-ee21de274138" class="numbered-list" start="3"><li>“Viết <strong>email mời hợp tác</strong> cho đại lý trạm sạc, giọng tin cậy &amp; thân thiện.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-80da-bbcf-fa35d7c87608" class="numbered-list" start="4"><li>“Phân tích <strong>phản hồi người dùng</strong> 30 ngày qua trên Facebook, tóm tắt 5 insight chính.”</li></ol></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-801a-8977-f25adfc9fa67"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-807a-a090-ec6e7c5b1582" class=""><strong>🔹 7️⃣ KHÁCH HÀNG &amp; HỖ TRỢ (Customer Support / Partner Ops)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-8094-a73b-fdfc75cf02aa" class=""><strong>🔧 Công cụ AI</strong></h3></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80f5-a06e-d1d5eb8fbc06" class="bulleted-list"><li style="list-style-type:disc"><strong>Zendesk AI / ChatGPT API:</strong> chatbot &amp; ticket phân loại</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8064-b14a-f22b9e2cd1be" class="bulleted-list"><li style="list-style-type:disc"><strong>Notion AI / Copilot:</strong> tạo câu trả lời mẫu (macro)</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-805d-9634-f69c36b837a8" class="bulleted-list"><li style="list-style-type:disc"><strong>Claude 3 / ChatGPT Vision:</strong> đọc ảnh lỗi trạm do khách 
ửi</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80dc-99f1-f6e2143b9793" class="bulleted-list"><li style="list-style-type:disc"><strong>Speech-to-Text (Whisper)</strong>: tóm tắt cuộc gọi CSKH</li></ul></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-80b6-a2bb-dd8c2578ff27" class=""><strong>💼 Nhiệm vụ</strong></h3></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8080-8b37-f0f479326c9c" class="bulleted-list"><li style="list-style-type:disc">Tự động trả lời câu hỏi thường gặp</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80e6-8629-df043e8ccba5" class="bulleted-list"><li style="list-style-type:disc">Phân loại &amp; chuyển ticket đúng nhóm</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8088-971d-df11a27e6f25" class="bulleted-list"><li style="list-style-type:disc">Gợi ý phản hồi nhanh</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80d7-b503-de82cf489e4a" class="bulleted-list"><li style="list-style-type:disc">Tổng hợp top lỗi khách hàng</li></ul></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-8072-82ab-ecf6e8210c9c" class=""><strong>💬 Prompts mẫu</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-8046-a7c7-f1afdf2e1104" class="numbered-list" start="1"><li>“Tạo <strong>macro trả lời</strong> cho lỗi sạc không kết nối, hướng dẫn 4 bước đơn giản.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-8016-b22d-f81f8a1aa8c8" class="numbered-list" start="2"><li>“Tóm tắt <strong>10 cuộc gọi CSKH gần nhất</strong>, nêu 3 vấn đề lặp lại nhiều nhất.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-8058-ac0f-e0b0186d03e9" class="numbered-list" start="3"><li>“Gợi ý <strong>FAQ tiếng Việt</strong> cho tài xế về ví năng lượng UniPower Wallet.”</li></ol></div><div style="display:contents" d
ir="auto"><ol type="1" id="291c5e6f-95bd-8095-b89a-dff101556c8a" class="numbered-list" start="4"><li>“Phân loại <strong>ticket tuần này</strong> theo kỹ thuật / thanh toán / trải nghiệm.”</li></ol></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-804a-9e44-f023cf270530"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-802b-aca4-f6811f158d7a" class=""><strong>🔹 8️⃣ PHÁP CHẾ &amp; ESG (Legal / Compliance / Sustainability)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-8015-b9b9-cb602f5d0c84" class=""><strong>🔧 Công cụ AI</strong></h3></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-801e-8571-d808edd665bf" class="bulleted-list"><li style="list-style-type:disc"><strong>Harvey AI / ChatGPT Legal Mode:</strong> soạn hợp đồng &amp; tóm điều khoản</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-801f-a28b-f97ae3f15327" class="bulleted-list"><li style="list-style-type:disc"><strong>Klarity / DocAI:</strong> kiểm tra rủi ro pháp lý</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8043-8cf3-e8b147d7e28f" class="bulleted-list"><li style="list-style-type:disc"><strong>ESG GPT / ChatGPT Advanced Data:</strong> tạo báo cáo môi trường</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8071-ae52-f803f9a49809" class="bulleted-list"><li style="list-style-type:disc"><strong>Google Sheets Copilot:</strong> tính toán CO₂ tránh được</li></ul></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-8041-b331-fdd54352b56b" class=""><strong>💼 Nhiệm vụ</strong></h3></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8038-8534-e346c340a084" class="bulleted-list"><li style="list-style-type:disc">Soạn &amp; rà hợp đồng BCC, MOU, NDA</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80af-87b7-c5003fef4243" class="bulleted-list"><li s
tyle="list-style-type:disc">Tạo báo cáo ESG quý</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80fe-b3b0-cbc904fdaccb" class="bulleted-list"><li style="list-style-type:disc">Viết thông báo quyền dữ liệu cá nhân (NĐ 13/2023)</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80ce-ad4c-c6f3044e14aa" class="bulleted-list"><li style="list-style-type:disc">Đánh giá rủi ro pháp lý của trạm / hợp tác</li></ul></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-8004-9ecc-c5c8b9be6000" class=""><strong>💬 Prompts mẫu</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-80c7-bc8c-ccf4212f5c94" class="numbered-list" start="1"><li>“Soạn <strong>hợp đồng BCC 5 năm</strong> giữa UniPower &amp; đối tác trạm sạc, chia sẻ doanh thu 70/30.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-8083-951f-e3c43066d090" class="numbered-list" start="2"><li>“Tóm tắt <strong>điều khoản pháp lý</strong> trong hợp đồng này, nêu 3 rủi ro tiềm ẩn.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-80cb-a499-d5aff190152b" class="numbered-list" start="3"><li>“Tạo <strong>báo cáo ESG quý</strong>, bao gồm điện năng sạch &amp; lượng CO₂ tránh được.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-80df-ae01-c62127dd3f4e" class="numbered-list" start="4"><li>“Viết <strong>privacy notice</strong> ngắn, dễ hiểu cho người dùng ví năng lượng.”</li></ol></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-80e6-95dd-ea3bf65ae59a"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-801e-82bf-c996070dd1a6" class=""><strong>🔹 9️⃣ DỮ LIỆU &amp; PHÂN TÍCH (Data / BI / Product)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-8014-bd9b-e5497cf97a5b" class=""><strong>🔧 Công cụ AI</strong></h3></div><div style="display:contents" d
ir="auto"><ul id="291c5e6f-95bd-804f-aca6-d3b4f3b27a6a" class="bulleted-list"><li style="list-style-type:disc"><strong>ChatGPT Code Interpreter / Python Sandbox:</strong> xử lý CSV, biểu đồ</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8056-b084-f58dcc31ccb9" class="bulleted-list"><li style="list-style-type:disc"><strong>Power BI + Copilot / Tableau GPT:</strong> báo cáo động</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8048-9c2b-ebbcb61085d6" class="bulleted-list"><li style="list-style-type:disc"><strong>BigQuery + Vertex AI:</strong> dự đoán xu hướng KPI</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-805a-a32b-ef148e98cbd5" class="bulleted-list"><li style="list-style-type:disc"><strong>ChatGPT Vision:</strong> đọc &amp; diễn giải dashboard</li></ul></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-8017-8998-c4b9f1b104c8" class=""><strong>💼 Nhiệm vụ</strong></h3></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80ce-b070-eaaadd172a17" class="bulleted-list"><li style="list-style-type:disc">Phân tích dữ liệu đội xe, trạm, tài xế</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-809c-929a-cb788c8864c7" class="bulleted-list"><li style="list-style-type:disc">Dự báo doanh thu, tải lưới, chi phí</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8035-9b73-f5d280775f0e" class="bulleted-list"><li style="list-style-type:disc">Phát hiện outlier hoặc sai lệch</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80f8-a8e7-d53712aac0fd" class="bulleted-list"><li style="list-style-type:disc">Tạo biểu đồ tự động cho báo cáo</li></ul></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-804b-baf9-c1f7b1435755" class=""><strong>💬 Prompts mẫu</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-8035-8f24-c1de25f9177b" c
lass="numbered-list" start="1"><li>“Phân tích file CSV này, tạo <strong>3 biểu đồ</strong> thể hiện doanh thu theo khu vực &amp; thời gian.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-8075-9c1f-d55565a4fe72" class="numbered-list" start="2"><li>“Tìm <strong>10 điểm dữ liệu bất thường</strong> trong bảng KPI tháng 9.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-801d-8b30-f3e5d26d9144" class="numbered-list" start="3"><li>“Dự báo <strong>nhu cầu sạc điện</strong> tuần tới dựa trên dữ liệu 30 ngày qua.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-809d-8e51-d6129ef3c3be" class="numbered-list" start="4"><li>“Tóm tắt dashboard Power BI này trong 5 dòng, tập trung vào chỉ số năng lượng.”</li></ol></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-8009-a0ea-fbcf06bd5fe5"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-8099-a9ee-de3f46ca057f" class=""><strong>🔹 🔟 NHÂN SỰ &amp; VĂN HÓA NỘI BỘ (People &amp; Culture)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-80a3-933c-e44604b642be" class=""><strong>🔧 Công cụ AI</strong></h3></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-804c-a58a-f283130ddb7e" class="bulleted-list"><li style="list-style-type:disc"><strong>ChatGPT / Notion AI:</strong> viết thông báo &amp; chính sách</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80be-8f88-cce658157a42" class="bulleted-list"><li style="list-style-type:disc"><strong>Otter.ai / Copilot:</strong> ghi biên bản cuộc họp nhân sự</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-809e-85cc-e7b37521eca5" class="bulleted-list"><li style="list-style-type:disc"><strong>Reflect AI / ChatGPT Journal:</strong> huấn luyện lãnh đạo &amp; phản chiếu tư duy</li></ul></div><div style="display:contents" dir="auto"><ul i
d="291c5e6f-95bd-80b3-a509-fca11dee5f68" class="bulleted-list"><li style="list-style-type:disc"><strong>ChatGPT HR GPT:</strong> tạo JD &amp; đánh giá năng lực</li></ul></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-80a1-9c64-e24f579136ed" class=""><strong>💼 Nhiệm vụ</strong></h3></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8067-90e7-e7cca11543bb" class="bulleted-list"><li style="list-style-type:disc">Viết JD / đăng tin tuyển dụng</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-809a-a5a1-fd4bcdff55b8" class="bulleted-list"><li style="list-style-type:disc">Soạn chính sách nội bộ</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-807a-afc8-ee9fb8dc5037" class="bulleted-list"><li style="list-style-type:disc">Tạo bản đánh giá năng lực</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-807e-bff3-c1f6b4d0e5b2" class="bulleted-list"><li style="list-style-type:disc">Huấn luyện phản chiếu (reflective coaching)</li></ul></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-80de-8763-f53a6b6c3208" class=""><strong>💬 Prompts mẫu</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-8028-a87a-ef77fad919b9" class="numbered-list" start="1"><li>“Viết <strong>JD Đội trưởng khu vực TP.HCM</strong>, 200 từ, giọng chuyên nghiệp.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-808e-93a6-f4b7a5280b02" class="numbered-list" start="2"><li>“Tạo <strong>mẫu đánh giá năng lực</strong> tài xế 3 cấp độ (mới – ổn – xuất sắc).”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-80c2-8bbd-f022b2b0f843" class="numbered-list" start="3"><li>“Soạn <strong>thông báo nội bộ</strong> về chính sách bảo hiểm mới, ngắn gọn &amp; rõ ràng.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-80c1-b97b-f0fc5ebe28d7" c
lass="numbered-list" start="4"><li>“Giúp tôi <strong>phản chiếu ngày làm việc hôm nay</strong>, chỉ ra 2 điểm cần cải thiện.”</li></ol></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-80be-a22d-e75a9845f499"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-8026-adbd-ec42a6ec5bcc" class=""><strong>🔹 11️⃣ SÁNG TẠO &amp; PHÁT TRIỂN SẢN PHẨM (Innovation / R&amp;D)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-8078-83b9-e4cf5018310e" class=""><strong>🔧 Công cụ AI</strong></h3></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8072-b33c-ceb9bb1e4785" class="bulleted-list"><li style="list-style-type:disc"><strong>ChatGPT / Ideaflow / Miro AI:</strong> brainstorming ý tưởng</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80df-b16c-d1b0d107c88c" class="bulleted-list"><li style="list-style-type:disc"><strong>Midjourney / DALL·E 3:</strong> tạo hình sản phẩm / mockup</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8019-a590-c2630020fe62" class="bulleted-list"><li style="list-style-type:disc"><strong>ChatGPT + Figma AI:</strong> giao diện UX/UI</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8064-8710-ce59099aa8fe" class="bulleted-list"><li style="list-style-type:disc"><strong>Claude 3.5 / Cursor AI:</strong> sinh mã code nhanh</li></ul></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-805e-9ed0-ebc60ada0c62" class=""><strong>💼 Nhiệm vụ</strong></h3></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-806b-96cd-d7dad679ab7f" class="bulleted-list"><li style="list-style-type:disc">Brainstorm mô hình sản phẩm mới (ví, app, dashboard)</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-807a-aa34-ec64c2fad4e9" class="bulleted-list"><li style="list-style-type:disc">Thiết kế giao diện prototype</li></ul></div><div style="display:contents" d
ir="auto"><ul id="291c5e6f-95bd-80e6-8df2-c3f49bd6dbab" class="bulleted-list"><li style="list-style-type:disc">Sinh code giao diện thử nghiệm</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80dd-8a93-cfc51203508f" class="bulleted-list"><li style="list-style-type:disc">Viết tài liệu kỹ thuật (API docs, SOP)</li></ul></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-8046-9395-ca334bb86805" class=""><strong>💬 Prompts mẫu</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-803c-8280-c13af48ef060" class="numbered-list" start="1"><li>“Brainstorm <strong>3 tính năng mới</strong> cho UniPower Wallet – tập trung vào loyalty &amp; carbon point.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-80c3-9133-ef652b85b1ac" class="numbered-list" start="2"><li>“Thiết kế <strong>giao diện dashboard</strong> quản lý trạm sạc thân thiện, dễ đọc.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-8096-a5d9-ed6a9f3a8947" class="numbered-list" start="3"><li>“Sinh <strong>mã HTML/CSS</strong> cho giao diện UniPower App theo style xanh trắng.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="291c5e6f-95bd-80f5-9840-cf479fb064cf" class="numbered-list" start="4"><li>“Viết <strong>API specification</strong> cho endpoint lấy dữ liệu ví năng lượng.”</li></ol></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-8075-8027-cc10e514a1e0"/></div><div style="display:contents" dir="auto"><h1 id="291c5e6f-95bd-80e2-a791-dda8b8414779" class=""><strong>🧱 TỔNG HỢP CÔNG CỤ &amp; CHỨC NĂNG CHÍNH</strong></h1></div><div style="display:contents" dir="ltr"><table id="291c5e6f-95bd-80c6-b7fa-c1bdbbce87ce" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="291c5e6f-95bd-8015-a996-e0ec51f0556c"><th id="Nh?U" class="simple-table-header-color s
imple-table-header"><strong>Nhóm</strong></th><th id="Q[xd" class="simple-table-header-color simple-table-header"><strong>Công cụ AI tiêu chuẩn</strong></th><th id="tkX`" class="simple-table-header-color simple-table-header"><strong>Ứng dụng chính</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="291c5e6f-95bd-80f9-bab6-ed3617290645"><td id="Nh?U" class="">Quản trị &amp; chiến lược</td><td id="Q[xd" class="">ChatGPT, Perplexity, Copilot</td><td id="tkX`" class="">Báo cáo, phân tích, ra quyết định</td></tr></div><div style="display:contents" dir="ltr"><tr id="291c5e6f-95bd-8041-9991-f07a90c89c9f"><td id="Nh?U" class="">Tài chính</td><td id="Q[xd" class="">Excel Copilot, Power BI, MindBridge</td><td id="tkX`" class="">P&amp;L, dòng tiền, phát hiện bất thường</td></tr></div><div style="display:contents" dir="ltr"><tr id="291c5e6f-95bd-8038-a8f4-d9ed81e1fc1c"><td id="Nh?U" class="">Năng lượng</td><td id="Q[xd" class="">Power BI IoT, Octopus AI, Gemini Vision</td><td id="tkX`" class="">Uptime, tariff, tối ưu tải điện</td></tr></div><div style="display:contents" dir="ltr"><tr id="291c5e6f-95bd-80f1-9dc8-c0327e6bc085"><td id="Nh?U" class="">Đội xe</td><td id="Q[xd" class="">ChatGPT Vision, Map API, Notion</td><td id="tkX`" class="">Hiệu suất, hành trình, coaching</td></tr></div><div style="display:contents" dir="ltr"><tr id="291c5e6f-95bd-808f-9887-c9253ea0cba4"><td id="Nh?U" class="">Tuyển dụng</td><td id="Q[xd" class="">HireVue, Notion AI, Otter</td><td id="tkX`" class="">Phỏng vấn, chấm điểm, phản hồi</td></tr></div><div style="display:contents" dir="ltr"><tr id="291c5e6f-95bd-8059-9a33-f7d1dffa1aba"><td id="Nh?U" class="">Marketing</td><td id="Q[xd" class="">Jasper, Canva Magic, Synthesia</td><td id="tkX`" class="">Nội dung, video, chiến dịch</td></tr></div><div style="display:contents" dir="ltr"><tr id="291c5e6f-95bd-809c-aa0f-e3ec3870a4da"><td id="Nh?U" class="">CSKH</td><td id="Q[xd" class="">Zendesk AI, Claude, ChatGPT</td><td i
d="tkX`" class="">Chatbot, macro, phân loại lỗi</td></tr></div><div style="display:contents" dir="ltr"><tr id="291c5e6f-95bd-809a-abc3-fe1c193af50f"><td id="Nh?U" class="">Pháp chế &amp; ESG</td><td id="Q[xd" class="">Harvey AI, DocAI, ESG GPT</td><td id="tkX`" class="">Hợp đồng, rủi ro, báo cáo môi trường</td></tr></div><div style="display:contents" dir="ltr"><tr id="291c5e6f-95bd-80f6-8c7b-cf2b659a111e"><td id="Nh?U" class="">Dữ liệu</td><td id="Q[xd" class="">ChatGPT Code, Power BI, BigQuery</td><td id="tkX`" class="">Dự báo, biểu đồ, anomaly detection</td></tr></div><div style="display:contents" dir="ltr"><tr id="291c5e6f-95bd-8027-aa93-e505489cdb4b"><td id="Nh?U" class="">Nhân sự</td><td id="Q[xd" class="">ChatGPT HR, Reflect AI</td><td id="tkX`" class="">JD, đánh giá, coaching</td></tr></div><div style="display:contents" dir="ltr"><tr id="291c5e6f-95bd-80ad-8a85-d3488b3a9b1d"><td id="Nh?U" class="">R&amp;D</td><td id="Q[xd" class="">Ideaflow, Midjourney, Cursor AI</td><td id="tkX`" class="">Prototype, code, tài liệu kỹ thuật</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-80b7-b219-fa9bd4cf5ec8"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-80fb-a687-f3ba8750aed4" class=""><strong>🧩 Kết luận</strong></h2></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80b2-a8a8-e355406ad026" class="bulleted-list"><li style="list-style-type:disc">Danh mục này bao phủ <strong>tất cả nghiệp vụ chính của UniPower</strong>, từ <strong>chiến lược – tài chính – năng lượng – nhân sự – marketing – công nghệ.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80a3-9734-dbcb206cce2a" class="bulleted-list"><li style="list-style-type:disc">Mỗi công cụ đi kèm <strong>prompts &amp; nhiệm vụ cụ thể</strong> có thể dùng ngay, giúp <strong>BOD và đội ngũ giảm 30–50% thời gian vận hành.</strong></li></ul></div><div style="display:contents" dir="auto"><ul i
d="291c5e6f-95bd-8003-beb7-c2e7c1e45346" class="bulleted-list"><li style="list-style-type:disc">Có thể tích hợp toàn bộ vào hệ thống <strong>UniTech / UniOS Dashboard</strong>, dùng như “AI Workspace” nội bộ.</li></ul></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
