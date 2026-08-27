---
tags: [vietnamese]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Đề xuất phê duyệt mua và triển khai giải pháp nền tảng gọi xe “Wooberly”</title><style>
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
	
</style></head><body><article id="290c5e6f-95bd-8005-abb9-dc0a957cb601" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Đề xuất phê duyệt mua và triển khai giải pháp nền tảng gọi xe “Wooberly”</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h1 id="290c5e6f-95bd-805a-8259-d52a7b0d1cf6" class=""><strong>TỜ TRÌNH</strong></h1></div><div style="display:contents" dir="auto"><p id="290c5e6f-95bd-80c2-b06f-f40d694350e6" class=""><strong>V/v: Đề xuất phê duyệt mua và triển khai giải pháp nền tảng gọi xe “Wooberly”</strong></p></div><div style="display:contents" dir="auto"><p id="290c5e6f-95bd-80dd-a324-c2671089bc97" class=""><strong>Kính gửi:</strong> Chủ tịch HĐQT &amp; Tổng Giám đốc (CEO)</p></div><div style="display:contents" dir="auto"><p id="290c5e6f-95bd-80d8-93f5-cdd76db479bc" class=""><strong>Người trình:</strong> Giám đốc Công nghệ (CTO) – UniPower</p></div><div style="display:contents" dir="auto"><p id="290c5e6f-95bd-80ee-bfd3-c220234b4206" class=""><strong>Ngày:</strong> …/…/2025</p></div><div style="display:contents" dir="auto"><hr id="290c5e6f-95bd-80df-9f70-e730e6bd41e5"/></div><div style="display:contents" dir="auto"><h2 id="290c5e6f-95bd-807d-8818-c05f9a828ec0" class=""><strong>I. Mục tiêu &amp; bối cảnh</strong></h2></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-806e-bf5d-d7ebbdfaa907" class="bulleted-list"><li style="list-style-type:disc">Đáp ứng yêu cầu <strong>ra mắt nhanh MVP</strong> cho UniTaxi/UniLogistics, sở hữu <strong>100% mã nguồn</strong>, giảm phụ thuộc nhà cung cấp, tối ưu <strong>CAPEX/OPEX</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-80eb-a9b9-c84c8e4add2a" class="bulleted-list"><li style="list-style-type:disc">So sánh 3 lựa chọn thị trường (EMDDI – VN, Wooberly – Ấn Độ, Miracuves – Ấn Độ). Trên cơ sở kỹ thuật, pháp lý, chi phí và tiến độ, <strong>Wooberly</strong> là phương án phù hợp nhất để khởi động nhanh, kiểm soát công nghệ, và mở rộng hệ sinh thái.</li></ul></div><div style="display:contents" dir="auto"><hr id="290c5e6f-95bd-8012-91f4-cd75f2848e70"/></div><div style="display:contents" dir="auto"><h2 id="290c5e6f-95bd-808d-85f8-f6ffd8733fe2" class=""><strong>II. Tóm tắt đề xuất</strong></h2></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-800c-98fb-dd5a6e86e410" class="bulleted-list"><li style="list-style-type:disc"><strong>Phê duyệt mua: Wooberly (Enterprise)</strong> – thanh toán một lần (<strong>$1,999</strong>), bàn giao <strong>100% mã nguồn</strong> (frontend, backend, mobile).</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-808b-ab72-e9e88d8efd7f" class="bulleted-list"><li style="list-style-type:disc"><strong>Triển khai 25–30 ngày</strong>: rebranding, cài đặt server, publish app iOS/Android, tích hợp thanh toán VN (MoMo/ZaloPay/VietQR), SMS/Zalo OA.</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-803e-af52-c86471518e5d" class="bulleted-list"><li style="list-style-type:disc"><strong>Mục tiêu Go-Live (MVP)</strong>: tối đa 30 ngày kể từ ngày duyệt.</li></ul></div><div style="display:contents" dir="auto"><hr id="290c5e6f-95bd-80dc-8a2c-c59d39bfbc86"/></div><div style="display:contents" dir="auto"><h2 id="290c5e6f-95bd-80be-8648-e05e519f1055" class=""><strong>III. Lý do khuyến nghị Wooberly (so với các phương án khác)</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="290c5e6f-95bd-8038-bac6-cb146870415e" class="numbered-list" start="1"><li><strong>Sở hữu công nghệ &amp; dữ liệu</strong><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-8071-a4be-d255286b4f51" class="bulleted-list"><li style="list-style-type:disc">Bàn giao <strong>100% mã nguồn</strong> ngay sau thanh toán → chủ động phát triển dài hạn, không “lock-in”.</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-80fe-b38f-df5b7ea6821f" class="bulleted-list"><li style="list-style-type:disc">Dữ liệu vận hành thuộc UniPower, thuận lợi tích hợp BI/ESG/insurtech.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="290c5e6f-95bd-8088-83de-ee57fb499d3d" class="numbered-list" start="2"><li><strong>Chi phí tối ưu – Tốc độ triển khai</strong><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-8008-a983-f28a4a51a125" class="bulleted-list"><li style="list-style-type:disc"><strong>CAPEX thấp</strong> (≈ $1,999) và <strong>không OPEX cố định</strong> (không % doanh thu).</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-8031-887c-fd63e3535c52" class="bulleted-list"><li style="list-style-type:disc"><strong>MVP trong 2–4 tuần</strong>, phù hợp chiến lược “đánh nhanh – học nhanh”.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="290c5e6f-95bd-801b-a1dd-fc5959db5416" class="numbered-list" start="3"><li><strong>Kiến trúc hiện đại – Dễ tích hợp</strong><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-8059-911a-dcb461cead53" class="bulleted-list"><li style="list-style-type:disc"><strong>Node.js + GraphQL + Flutter</strong> → API-first, realtime tốt, UI/UX đồng nhất.</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-801d-98d9-cdb782e350c1" class="bulleted-list"><li style="list-style-type:disc">Thuận lợi mở rộng logistics, merchant, loyalty, bản đồ, bảo hiểm, AI scoring.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="290c5e6f-95bd-8003-bfb4-d8c3f9f9c5cd" class="numbered-list" start="4"><li><strong>Khả năng mở rộng đội ngũ</strong><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-80f6-b9fb-e09fdaafb75a" class="bulleted-list"><li style="list-style-type:disc">Công nghệ phổ biến tại VN/Ấn Độ, dễ thuê dev nội bộ, giảm rủi ro nhân sự.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><blockquote id="290c5e6f-95bd-8026-8542-efbe8ecdb2ef" class="">Kết luận:<div style="display:contents" dir="auto"><p id="290c5e6f-95bd-806d-919d-ceb5a8e4f3ea" class=""><strong>đầy đủ 4 tiêu chí lõi</strong></p></div></blockquote></div><div style="display:contents" dir="auto"><hr id="290c5e6f-95bd-8065-96c7-da3f8ea3d91b"/></div><div style="display:contents" dir="auto"><h2 id="290c5e6f-95bd-80fb-a621-f3ead44e3ddf" class=""><strong>IV. Phân tích rủi ro &amp; biện pháp kiểm soát</strong></h2></div><div style="display:contents" dir="ltr"><table id="290c5e6f-95bd-803e-8ca8-e8901aad7a53" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="290c5e6f-95bd-806c-b1e4-c315fcc01ce7"><th id="NZT{" class="simple-table-header-color simple-table-header"><strong>Rủi ro</strong></th><th id="?=Dd" class="simple-table-header-color simple-table-header"><strong>Ảnh hưởng</strong></th><th id=":=QZ" class="simple-table-header-color simple-table-header"><strong>Biện pháp</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="290c5e6f-95bd-80c6-ae37-cb33aa5df1a9"><td id="NZT{" class="">Không có Git/Docker mặc định</td><td id="?=Dd" class="">Khó quản lý version/CI-CD</td><td id=":=QZ" class="">CTO thiết lập <strong>Git private + CI/CD</strong> (GitLab/GitHub Actions); chuẩn quy trình release.</td></tr></div><div style="display:contents" dir="ltr"><tr id="290c5e6f-95bd-80ee-9b2f-dc35991811b3"><td id="NZT{" class="">Hỗ trợ giờ hành chính (24–48h)</td><td id="?=Dd" class="">Chậm xử lý sự cố</td><td id=":=QZ" class="">Ký <strong>SLA nội bộ</strong>; bố trí <strong>1 DevOps + 1 Full-stack</strong> trực ca.</td></tr></div><div style="display:contents" dir="ltr"><tr id="290c5e6f-95bd-8002-baa8-e1cabe3d5be8"><td id="NZT{" class="">Chưa có stress-test công khai</td><td id="?=Dd" class="">Rủi ro tải cao</td><td id=":=QZ" class="">Làm <strong>kiểm thử tải</strong> (Locust/JMeter), scale MySQL/Redis/Socket; sẵn sàng <strong>autoscaling</strong>.</td></tr></div><div style="display:contents" dir="ltr"><tr id="290c5e6f-95bd-8036-b76a-d778a9f10744"><td id="NZT{" class="">Tích hợp cổng thanh toán nội địa</td><td id="?=Dd" class="">Phụ thuộc dev VN</td><td id=":=QZ" class="">Dự toán <strong>40–80 giờ</strong> × $25/giờ; ưu tiên <strong>VietQR/MoMo</strong> trước.</td></tr></div><div style="display:contents" dir="ltr"><tr id="290c5e6f-95bd-807d-8577-c055f458d4a9"><td id="NZT{" class="">Bảo trì dài hạn</td><td id="?=Dd" class="">Năng lực nội bộ</td><td id=":=QZ" class="">Kế hoạch <strong>build team</strong>: 1 PM, 1 DevOps, 2 Dev (Flutter + Node).</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="290c5e6f-95bd-8009-98a7-e94b1fb4c6f4"/></div><div style="display:contents" dir="auto"><h2 id="290c5e6f-95bd-807e-bc03-faa2d9e3965f" class=""><strong>V. Phạm vi triển khai (Scope)</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="290c5e6f-95bd-8057-8c92-c6c1806f0800" class="numbered-list" start="1"><li><strong>Rebranding &amp; i18n:</strong> Logo, màu sắc, VN/EN (bao gồm trong gói).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="290c5e6f-95bd-804b-b3f1-f8e7891cc851" class="numbered-list" start="2"><li><strong>Hạ tầng:</strong> VPS/Cloud (FPT/AWS/GCP), domain, SSL, WAF cơ bản.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="290c5e6f-95bd-80d7-8ee8-c2214ea24b98" class="numbered-list" start="3"><li><strong>Tích hợp Việt Nam:</strong> Thanh toán (MoMo/ZaloPay/VietQR), SMS/ZNS, bản đồ (Google Maps, sẵn sàng Map4D).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="290c5e6f-95bd-8007-a948-fd0a3bcc9629" class="numbered-list" start="4"><li><strong>Vận hành:</strong> Onboarding tài xế, định vị, tính cước, ví trong app, đối soát.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="290c5e6f-95bd-80fa-b09b-c5be9edd53e6" class="numbered-list" start="5"><li><strong>Bảo mật &amp; tuân thủ:</strong> NĐ 13/2023 (dữ liệu cá nhân), nhật ký truy cập, phân quyền.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="290c5e6f-95bd-8014-94e4-f8a1da262687" class="numbered-list" start="6"><li><strong>Báo cáo:</strong> Dashboard vận hành, doanh thu, đơn/giờ, tỷ lệ nhận cuốc, NPS.</li></ol></div><div style="display:contents" dir="auto"><hr id="290c5e6f-95bd-80bd-8e29-f3d7404052e6"/></div><div style="display:contents" dir="auto"><h2 id="290c5e6f-95bd-8009-bfd6-fb73f349d98e" class=""><strong>VI. Kế hoạch thực thi &amp; mốc thời gian</strong></h2></div><div style="display:contents" dir="ltr"><table id="290c5e6f-95bd-8030-92a7-c48c10fb525a" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="290c5e6f-95bd-8039-94e6-cdc2fa3b8be6"><th id="p~t;" class="simple-table-header-color simple-table-header"><strong>Giai đoạn</strong></th><th id="J=b^" class="simple-table-header-color simple-table-header"><strong>Nội dung</strong></th><th id=":C=K" class="simple-table-header-color simple-table-header"><strong>Trách nhiệm</strong></th><th id="me@@" class="simple-table-header-color simple-table-header"><strong>Thời gian</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="290c5e6f-95bd-80ba-94ce-df1e38222cb9"><td id="p~t;" class="">1</td><td id="J=b^" class="">Mua license, nhận mã nguồn + IP transfer</td><td id=":C=K" class="">CTO + Legal + Finance</td><td id="me@@" class="">Ngày 1–3</td></tr></div><div style="display:contents" dir="ltr"><tr id="290c5e6f-95bd-8084-8499-ea5782242649"><td id="p~t;" class="">2</td><td id="J=b^" class="">Thiết lập server, DB, Git, CI/CD</td><td id=":C=K" class="">DevOps</td><td id="me@@" class="">Ngày 3–6</td></tr></div><div style="display:contents" dir="ltr"><tr id="290c5e6f-95bd-809c-9791-fd5b9b94f41a"><td id="p~t;" class="">3</td><td id="J=b^" class="">Rebranding + dịch giao diện</td><td id=":C=K" class="">Vendor (bao gồm)</td><td id="me@@" class="">Ngày 6–12</td></tr></div><div style="display:contents" dir="ltr"><tr id="290c5e6f-95bd-80ba-ad68-c5eac4c71722"><td id="p~t;" class="">4</td><td id="J=b^" class="">Tích hợp thanh toán + SMS</td><td id=":C=K" class="">Dev nội bộ/Vendor</td><td id="me@@" class="">Ngày 10–18</td></tr></div><div style="display:contents" dir="ltr"><tr id="290c5e6f-95bd-805b-886e-d27273984d96"><td id="p~t;" class="">5</td><td id="J=b^" class="">QA/UAT + kiểm thử tải &amp; bảo mật</td><td id=":C=K" class="">QA + CTO</td><td id="me@@" class="">Ngày 18–23</td></tr></div><div style="display:contents" dir="ltr"><tr id="290c5e6f-95bd-808c-a6ca-dd48bef8c30a"><td id="p~t;" class="">6</td><td id="J=b^" class="">Publish App Store/Play Store</td><td id=":C=K" class="">Vendor (bao gồm)</td><td id="me@@" class="">Ngày 23–30</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="290c5e6f-95bd-80e5-bae7-ef7407873dbc" class=""><strong>Go-Live dự kiến:</strong> ngày …/…/2025 (≤ 30 ngày sau phê duyệt).</p></div><div style="display:contents" dir="auto"><hr id="290c5e6f-95bd-8085-bef8-f6bdd3148d67"/></div><div style="display:contents" dir="auto"><h2 id="290c5e6f-95bd-8015-82df-e93df9e2185b" class=""><strong>VII. Ngân sách &amp; nguồn lực</strong></h2></div><div style="display:contents" dir="auto"><p id="290c5e6f-95bd-8045-a0a9-e10c420130ee" class=""><strong>Chi phí một lần (ước tính):</strong></p></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-80d0-a0ab-f429894320fd" class="bulleted-list"><li style="list-style-type:disc">License <strong>Wooberly Enterprise</strong>: <strong>$1,999</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-80d8-8adb-ef44b3302040" class="bulleted-list"><li style="list-style-type:disc">Tùy chỉnh &amp; tích hợp (ước <strong>80–120 giờ × $25/giờ</strong>): <strong>$2,000–$3,000</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-80fa-a06b-ffec3566a179" class="bulleted-list"><li style="list-style-type:disc">DevOps/CI-CD &amp; bảo mật ban đầu: <strong>30–50 giờ</strong> (nội bộ)</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-8019-a028-c4107b391657" class="bulleted-list"><li style="list-style-type:disc">Hạ tầng Cloud 3 tháng (staging + prod): <strong>$500–$1,000</strong></li></ul></div><div style="display:contents" dir="auto"><p id="290c5e6f-95bd-80e1-bd3e-ce0122390978" class=""><strong>Tổng CAPEX dự kiến:</strong> <strong>$4,500 – $6,000</strong> (≈ 110–150 triệu VNĐ).</p></div><div style="display:contents" dir="auto"><p id="290c5e6f-95bd-800e-906a-eb424d628de5" class=""><strong>OPEX hằng tháng:</strong> theo usage cloud (không % doanh thu); nhân sự nội bộ.</p></div><div style="display:contents" dir="auto"><p id="290c5e6f-95bd-8007-b0a2-f3aad2aa995f" class=""><strong>Nhân sự triển khai:</strong></p></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-8028-b595-ca3e87d37fdc" class="bulleted-list"><li style="list-style-type:disc">01 PM/Tech Lead (kiêm CTO giám sát)</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-80f0-b6b2-f120793a4d92" class="bulleted-list"><li style="list-style-type:disc">01 DevOps (part-time giai đoạn đầu)</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-802f-9d1a-cef74e963201" class="bulleted-list"><li style="list-style-type:disc">01 Flutter dev + 01 Node.js dev</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-808a-887c-dbeb44dcd42d" class="bulleted-list"><li style="list-style-type:disc">Hỗ trợ vendor theo gói (3–6 tháng)</li></ul></div><div style="display:contents" dir="auto"><hr id="290c5e6f-95bd-807e-9ebc-cf58e4357a98"/></div><div style="display:contents" dir="auto"><h2 id="290c5e6f-95bd-80d6-b28b-d6d8a9676221" class=""><strong>VIII. Chỉ số thành công (KPI) &amp; bàn giao</strong></h2></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-80cb-8d25-d79601f3977d" class="bulleted-list"><li style="list-style-type:disc"><strong>Ngày T+30</strong>: MVP Go-Live, <strong>99% chức năng cốt lõi</strong> hoạt động.</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-8012-bd0e-e2979487a65a" class="bulleted-list"><li style="list-style-type:disc"><strong>Ngày T+45</strong>: Tối thiểu <strong>500 tài xế kích hoạt</strong>, <strong>10.000 cuốc/tháng</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-8081-a5cc-dbfa5194c5e9" class="bulleted-list"><li style="list-style-type:disc"><strong>Ngày T+60</strong>: NPS khách ≥ <strong>4,6/5</strong>; tỷ lệ nhận cuốc ≥ <strong>85%</strong>; uptime ≥ <strong>99,5%</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-80f0-9386-d440fd170368" class="bulleted-list"><li style="list-style-type:disc">Bàn giao: <strong>Tài liệu hệ thống, sơ đồ kiến trúc, runbook vận hành, mã nguồn trên Git private</strong>, checklist bảo mật.</li></ul></div><div style="display:contents" dir="auto"><hr id="290c5e6f-95bd-8038-9fa9-ee4b7748c113"/></div><div style="display:contents" dir="auto"><h2 id="290c5e6f-95bd-809b-88cd-e384442999c5" class=""><strong>IX. Pháp lý &amp; sở hữu trí tuệ</strong></h2></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-8080-99dd-c7dabdbd1e7d" class="bulleted-list"><li style="list-style-type:disc">Hợp đồng <strong>mua đứt – chuyển giao mã nguồn &amp; quyền sử dụng trọn đời</strong>, kèm <strong>văn bản IP transfer</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-80a9-b8e6-ef7d1728aedb" class="bulleted-list"><li style="list-style-type:disc">Dữ liệu do UniPower sở hữu; vendor không được chia sẻ bên thứ ba.</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-80cc-98f1-e0b3494efd65" class="bulleted-list"><li style="list-style-type:disc">Tuân thủ: NĐ 13/2023 (bảo vệ dữ liệu cá nhân), tiêu chuẩn an toàn thông tin nội bộ.</li></ul></div><div style="display:contents" dir="auto"><hr id="290c5e6f-95bd-80d4-b061-e5d793e782f6"/></div><div style="display:contents" dir="auto"><h2 id="290c5e6f-95bd-8044-809a-e36a04d2c2a0" class=""><strong>X. Kiến nghị phê duyệt</strong></h2></div><div style="display:contents" dir="auto"><p id="290c5e6f-95bd-80f5-82a5-f932b9acbc2c" class="">Đề nghị HĐQT/CEO:</p></div><div style="display:contents" dir="auto"><ol type="1" id="290c5e6f-95bd-80b4-bd41-cc3d34d7e3fd" class="numbered-list" start="1"><li><strong>Phê duyệt mua license Wooberly Enterprise</strong> (one-time <strong>$1,999</strong>).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="290c5e6f-95bd-8020-abb7-f6970a25f0ce" class="numbered-list" start="2"><li><strong>Phê duyệt ngân sách triển khai</strong> tổng mức <strong>$6,000</strong> (bao gồm tích hợp, hạ tầng khởi động, dự phòng 15%).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="290c5e6f-95bd-801c-8fc7-e96992f5b35a" class="numbered-list" start="3"><li>Cho phép <strong>CTO ký kết &amp; thực hiện</strong>: hợp đồng mua, IP transfer, triển khai hạ tầng, công bố Go-Live.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="290c5e6f-95bd-8024-a122-dd08d36e495f" class="numbered-list" start="4"><li>Giao <strong>Phòng Tài chính</strong> tạm ứng/chi theo tiến độ; <strong>Phòng Pháp chế</strong> rà soát điều khoản license &amp; IP.</li></ol></div><div style="display:contents" dir="auto"><hr id="290c5e6f-95bd-8099-a57b-d88884e470ff"/></div><div style="display:contents" dir="auto"><h2 id="290c5e6f-95bd-80c0-a5bb-f4bb725eba79" class=""><strong>XI. Phụ lục tham chiếu (tóm tắt so sánh 3 giải pháp)</strong></h2></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-8060-a1bb-cf1fea29ee24" class="bulleted-list"><li style="list-style-type:disc"><strong>Quyền sở hữu mã nguồn:</strong> EMDDI (❌/36 tháng + $350k) – Wooberly (✅ 100%) – Miracuves (✅ 100%).</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-80c5-9ac6-dcb9c7ebe459" class="bulleted-list"><li style="list-style-type:disc"><strong>Chi phí khởi tạo:</strong> EMDDI (~20.000 USD + 2% doanh thu) – Wooberly ($1.5–2k, không OPEX) – Miracuves ($2.5–3k).</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-803f-afc0-e31c28027a87" class="bulleted-list"><li style="list-style-type:disc"><strong>Kiến trúc:</strong> EMDDI (PHP monolith) – <strong>Wooberly (Node + GraphQL + Flutter)</strong> – Miracuves (Laravel + Flutter).</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-80f7-9b2f-feb1a403e24f" class="bulleted-list"><li style="list-style-type:disc"><strong>Localisation/Payment:</strong> Wooberly &amp; Miracuves dễ tích hợp MoMo/ZaloPay/VietQR; EMDDI khóa trong hệ thống.</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-80d5-9029-c0ffe96d7c1c" class="bulleted-list"><li style="list-style-type:disc"><strong>Tiến độ MVP:</strong> EMDDI 2–3 tháng; <strong>Wooberly 2–4 tuần</strong>; Miracuves 3–4 tuần.</li></ul></div><div style="display:contents" dir="auto"><hr id="290c5e6f-95bd-80d3-a439-f75955701adf"/></div><div style="display:contents" dir="auto"><h3 id="290c5e6f-95bd-809a-8483-d0b77ef7280b" class=""><strong>XÁC NHẬN &amp; PHÊ DUYỆT</strong></h3></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-804d-8726-fb7eb814382c" class="bulleted-list"><li style="list-style-type:disc"><strong>CTO (Người lập):</strong> ……………………………….. Ngày ……/……/2025</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-80ca-a5cf-c239f6c3f362" class="bulleted-list"><li style="list-style-type:disc"><strong>CFO (Thẩm định ngân sách):</strong> …………………….. Ngày ……/……/2025</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-806d-b806-effc5aaf5b58" class="bulleted-list"><li style="list-style-type:disc"><strong>CEO (Phê duyệt):</strong> ………………………………….. Ngày ……/……/2025</li></ul></div><div style="display:contents" dir="auto"><ul id="290c5e6f-95bd-80cb-a0fe-cacac5fdaa62" class="bulleted-list"><li style="list-style-type:disc"><strong>Chủ tịch HĐQT (Chuẩn y):</strong> ……………………… Ngày ……/……/2025</li></ul></div><div style="display:contents" dir="auto"><hr id="290c5e6f-95bd-80ed-8608-cb3431b97b96"/></div><div style="display:contents" dir="auto"><p id="290c5e6f-95bd-8099-883f-d46285664bba" class=""><strong>Kính trình HĐQT/CEO xem xét phê duyệt.</strong></p></div><div style="display:contents" dir="auto"><p id="290c5e6f-95bd-80c8-a40d-e937dfe0a720" class=""><em>CTO – UniPower</em></p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
