---
tags: [vietnamese]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>HỢP ĐỒNG MUA BÁN</title><style>
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
	
</style></head><body><article id="2cfc5e6f-95bd-80b2-b60c-d3e79afa4842" class="page sans"><header><h1 class="page-title" dir="auto"><strong>HỢP ĐỒNG MUA BÁN</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8071-a075-c38d28a35557" class=""><strong>Số Hợp đồng:</strong> HH2025121902</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8050-b2bb-cf4e81231cd8" class=""><strong>Ngày ký:</strong> 19/12/2025</p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-80b9-bd2b-d16106dd235c"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-8097-884c-e20464195f0f" class=""><strong>BÊN BÁN (SELLER)</strong></h2></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8066-9529-cae4269d6bf2" class=""><strong>Tên công ty:</strong> HENGWAI HOLDING LIMITED</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-808a-86f4-e59349ff3436" class=""><strong>Số đăng ký kinh doanh:</strong> 7020775100012245</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8076-a013-cf36bac87fab" class=""><strong>Địa chỉ:</strong> Phòng 2306, Tòa A, Tầng 23, Tòa nhà Công nghiệp Cao cấp,</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8065-bea4-e97965b8b7b6" class="">Số 26–38 đường Kwai Cheong, Kwai Chung,</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8009-b596-e60abd8afcc8" class="">Khu Tân Giới, Hồng Kông, Trung Quốc</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80ef-94c0-cae913da86f4" class=""><strong>Người đại diện:</strong> LI PEI HONG</p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-80e6-9551-e436b04bc956"/></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-801e-9873-e8bd72f476bd" class="">Căn cứ theo <strong>INCOTERMS 2010</strong>, Bên Bán và Bên Mua ký kết và thống nhất thực hiện giao dịch theo các điều khoản và điều kiện quy định dưới đây:</p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-807f-8b55-f18b0190105a" class="bulleted-list"><li style="list-style-type:disc"><strong>Cảng xếp hàng:</strong> Nansha, Quảng Châu</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8056-9d39-f61809839707" class="bulleted-list"><li style="list-style-type:disc"><strong>Cảng đến:</strong> Cảng Ho Chi Minh – Ki Lai</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80fc-9569-ca4a5d2abe7a" class="bulleted-list"><li style="list-style-type:disc"><strong>Hình thức vận chuyển:</strong> Đường biển</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-808c-8880-e584448610ba" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều kiện giao hàng:</strong> FOB</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-805e-9f55-ee907deb4697" class="bulleted-list"><li style="list-style-type:disc"><strong>Thời gian giao hàng:</strong> Trước ngày 31/01/2026</li></ul></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-8021-880c-c9d4dae9a978"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-809b-a886-c8514df38bdc" class=""><strong>ĐIỀU 1. THÔNG TIN HÀNG HÓA</strong></h2></div><div style="display:contents" dir="ltr"><table id="2cfc5e6f-95bd-80ab-a084-ee3fa7428d10" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2cfc5e6f-95bd-80b5-a4d7-de77d67c835a"><th id="dCA{" class="simple-table-header-color simple-table-header"><strong>STT</strong></th><th id="U&gt;Hc" class="simple-table-header-color simple-table-header"><strong>Nhãn hiệu</strong></th><th id=":EUB" class="simple-table-header-color simple-table-header"><strong>Mẫu xe</strong></th><th id="vuiG" class="simple-table-header-color simple-table-header"><strong>Thông số</strong></th><th id="nT_~" class="simple-table-header-color simple-table-header"><strong>Phiên bản</strong></th><th id="BAlc" class="simple-table-header-color simple-table-header"><strong>Màu sắc</strong></th><th id="mBxq" class="simple-table-header-color simple-table-header"><strong>Số lượng</strong></th><th id="IQx}" class="simple-table-header-color simple-table-header"><strong>Đơn giá FOB (USD)</strong></th><th id="RTiv" class="simple-table-header-color simple-table-header"><strong>Thành tiền FOB (USD)</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2cfc5e6f-95bd-80ed-9734-cf1c9d424809"><td id="dCA{" class="">1</td><td id="U&gt;Hc" class="">Baojun</td><td id=":EUB" class="">Baojun E6</td><td id="vuiG" class="">2026 – 500km</td><td id="nT_~" class="">Enjoyment Edition</td><td id="BAlc" class="">Trắng</td><td id="mBxq" class="">2</td><td id="IQx}" class="">12.570</td><td id="RTiv" class="">25.140</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8011-b319-d1d69731d92f" class=""><strong>Tổng cộng:</strong></p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-804c-9d85-cfd78797875f" class="bulleted-list"><li style="list-style-type:disc">Số lượng: 2 xe</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8028-92dc-de9d71748cc6" class="bulleted-list"><li style="list-style-type:disc">Tổng giá trị FOB: <strong>25.140 USD</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-8093-9e49-c59c0a910622"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-8036-afe2-fd2725a12248" class=""><strong>ĐIỀU 2. ĐIỀU KHOẢN THANH TOÁN</strong></h2></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80f8-b66e-e30f9143cad3" class="">Bên Mua thanh toán bằng hình thức <strong>chuyển khoản điện tử (T/T)</strong> ngay sau khi ký hợp đồng.</p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-80ab-8b5c-dec79c8dde8b"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-80d4-98e4-d9f2a5f67a16" class=""><strong>ĐIỀU 3. THÔNG TIN TÀI KHOẢN NGÂN HÀNG CỦA BÊN BÁN</strong></h2></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8065-a469-cb2e28be9bb7" class="bulleted-list"><li style="list-style-type:disc"><strong>Tên công ty thụ hưởng:</strong> HENGWAI HOLDING LIMITED</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8079-92b7-fc0a5056bb63" class="bulleted-list"><li style="list-style-type:disc"><strong>Số tài khoản:</strong> NRA35601002010590002151</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80b1-be80-e554dfe20b0a" class="bulleted-list"><li style="list-style-type:disc"><strong>Địa chỉ công ty:</strong> Phòng 2306, Tòa A, Tầng 23, Tòa nhà Công nghiệp Cao cấp,<div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80e8-b5e7-d7346b932c27" class="">26–38 Kwai Cheong Road, Kwai Chung, New Territories, Hong Kong</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-801c-90c1-c1ad7a8894e2" class="bulleted-list"><li style="list-style-type:disc"><strong>Tên ngân hàng:</strong> Zhejiang Chouzhou Commercial Bank Co., Ltd</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8040-b306-ec7214f177b5" class="bulleted-list"><li style="list-style-type:disc"><strong>Địa chỉ ngân hàng:</strong> Tầng 2, Số 320 đường Wusibei, Phúc Châu, Phúc Kiến, Trung Quốc, 350000</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80e2-8b48-dd6536b5439b" class="bulleted-list"><li style="list-style-type:disc"><strong>Mã SWIFT:</strong> CZCBCN2XXXX</li></ul></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-805b-b556-dee92146edf6"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-80c2-8b8b-cf0e9bba97dd" class=""><strong>ĐIỀU 4. ĐIỀU KIỆN GIAO HÀNG &amp; CẢNG ĐẾN</strong></h2></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8030-a1df-dce79dff873f" class="bulleted-list"><li style="list-style-type:disc"><strong>Điều kiện giao hàng:</strong> FOB Nansha, Quảng Châu</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80f2-b57f-eb0b8052bb63" class="bulleted-list"><li style="list-style-type:disc"><strong>Cảng đến:</strong> Cảng Ho Chi Minh – Ki Lai</li></ul></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8020-83a5-c46e449475aa" class="">Bên Bán hỗ trợ Bên Mua trong việc:</p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8041-98f4-eab5d74020bc" class="bulleted-list"><li style="list-style-type:disc">đặt chỗ tàu,</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8064-932d-eb3b291dd377" class="bulleted-list"><li style="list-style-type:disc">sắp xếp xếp xe,</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-803c-b52f-c9e9ee050c65" class="bulleted-list"><li style="list-style-type:disc">vận chuyển hàng hóa.</li></ul></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-8092-bbe7-fd9341779b79"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-8022-8519-c4740964a3f7" class=""><strong>ĐIỀU 5. THỜI GIAN GIAO HÀNG</strong></h2></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8091-a2b6-c65551c70b97" class="">Trong vòng <strong>15 ngày kể từ ngày Bên Bán nhận đủ tiền thanh toán</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-806f-a34a-f0b3215785ef"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-8073-b407-cbf9d4af095d" class=""><strong>ĐIỀU 6. CHỨNG TỪ CUNG CẤP CHO THÔNG QUAN</strong></h2></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80f5-86bc-efc231c62fa8" class="">Bên Bán cung cấp cho Bên Mua các chứng từ sau:</p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8097-8e01-c50e9e73af8b" class="bulleted-list"><li style="list-style-type:disc">Hóa đơn thương mại (Commercial Invoice)</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-808b-b7b4-cacf7850ce66" class="bulleted-list"><li style="list-style-type:disc">Phiếu đóng gói (Packing List)</li></ul></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-8089-9957-d9ae73468003"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-80a8-9725-c472e143ddfe" class=""><strong>ĐIỀU 7. THỜI HẠN NGHIỆM THU &amp; DỊCH VỤ SAU BÁN</strong></h2></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8072-b180-e58848cfe1fd" class="">Trong vòng <strong>07 ngày làm việc</strong> kể từ ngày hàng đến nơi.</p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-8056-8d7d-cadf82eca474"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-80c1-8f6d-d4de4c0e0149" class=""><strong>ĐIỀU 8. SỐ BẢN HỢP ĐỒNG</strong></h2></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-803c-8b34-c86d4b30cdca" class="">Hợp đồng được lập thành <strong>02 bản</strong>, có giá trị pháp lý như nhau, mỗi bên giữ 01 bản.</p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-8040-95c1-c81295b6bc25"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-805e-becc-d116ebd089fe" class=""><strong>ĐIỀU 9. LUẬT ÁP DỤNG</strong></h2></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8043-8610-fb6288ce9146" class="">Mọi tranh chấp phát sinh từ hợp đồng này được điều chỉnh bởi <strong>pháp luật nước Cộng hòa Nhân dân Trung Hoa</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-800b-9b5f-fd71616dfda4"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-809c-9466-c8a0d779c55f" class=""><strong>ĐIỀU 10. GIẢI QUYẾT TRANH CHẤP &amp; THẨM QUYỀN</strong></h2></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-809e-8bc0-dd59b0b36bad" class="bulleted-list"><li style="list-style-type:disc">Trường hợp có sự khác biệt giữa bản tiếng Trung và tiếng Anh, <strong>bản tiếng Trung sẽ được ưu tiên áp dụng</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80eb-af5e-e3f1274aabcb" class="bulleted-list"><li style="list-style-type:disc">Mọi tranh chấp trước hết sẽ được giải quyết bằng <strong>thương lượng thiện chí</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8016-91f4-c2d92b54b80f" class="bulleted-list"><li style="list-style-type:disc">Nếu thương lượng không thành, tranh chấp sẽ thuộc <strong>thẩm quyền giải quyết của Tòa án Nhân dân tại nơi Bên Bán đặt trụ sở</strong>.</li></ul></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8055-bb77-e92c0f7ef0b6" class="">Hợp đồng có hiệu lực kể từ ngày ký và đóng dấu của hai bên, như ghi tại trang đầu của hợp đồng.</p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-80b2-877a-eac09b9d0c27"/></div><div style="display:contents" dir="auto"><h1 id="2cfc5e6f-95bd-80d7-8c31-fd01888f3bc3" class=""><strong>ĐIỀU KHOẢN CHUNG</strong></h1></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-8036-bd3a-fba7ee4d00d6"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-8083-ad2b-ce8aab45174f" class=""><strong>1. MIỄN TRỪ TRÁCH NHIỆM</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2cfc5e6f-95bd-80cf-8bea-fb135ced82a3" class=""><strong>1.1</strong></h3></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80f5-903b-d69ffdaed3e3" class="">Trước khi ký hợp đồng, Bên Mua biết rõ rằng <strong>toàn bộ hàng hóa do Bên Bán giao là xe đã qua sử dụng</strong>.</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8009-8b65-c4576aa469d1" class="">Bên Mua đã được Bên Bán thông báo đầy đủ về tình trạng cụ thể của xe và <strong>đồng ý chấp nhận mọi khiếm khuyết</strong>, kể cả những khiếm khuyết có thể <strong>chưa được Bên Bán công bố</strong>.</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8096-98f1-d5694501713c" class="">Bên Mua <strong>miễn trừ hoàn toàn</strong> mọi nghĩa vụ bảo đảm chất lượng liên quan của Bên Bán.</p></div><div style="display:contents" dir="auto"><h3 id="2cfc5e6f-95bd-8064-98c5-f71708ea2fa1" class=""><strong>1.2</strong></h3></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8079-a6a5-ea4c48c38c5c" class="">Bên Mua tự chịu trách nhiệm <strong>dịch vụ sau bán hàng</strong> đối với xe đã qua sử dụng.</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8066-9649-d259688f4e8f" class="">Bên Bán <strong>không chịu bất kỳ trách nhiệm nào</strong> về dịch vụ sau bán hàng.</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8050-8710-cffb28ebf9f3" class="">Theo yêu cầu bằng văn bản của Bên Mua, Bên Bán <strong>có thể hỗ trợ</strong>, nhưng không chịu nghĩa vụ.</p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-8030-9f11-c69a5aca7eeb"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-8022-b5f0-d37484c54aa4" class=""><strong>2. GIAO DỊCH ĐẠO ĐỨC</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2cfc5e6f-95bd-8026-a527-ec9c343b9cac" class=""><strong>2.1</strong></h3></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8052-b7ba-c62f8bd54854" class="">Bên Mua cam kết:</p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8014-bc9b-eefef0fc11e2" class="bulleted-list"><li style="list-style-type:disc">tuân thủ nghiêm ngặt pháp luật về <strong>chống hối lộ, tham nhũng và các hành vi kinh doanh bị cấm</strong>;</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80d4-86ba-d0ecd951e660" class="bulleted-list"><li style="list-style-type:disc">không trực tiếp hoặc gián tiếp đưa, hứa hẹn, hoặc đồng ý đưa tiền, quà hay bất kỳ lợi ích nào nhằm tác động đến quyết định của bên thứ ba.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2cfc5e6f-95bd-8007-a4b0-fbe9e08a931a" class=""><strong>2.2</strong></h3></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8025-9439-fd237202c94c" class="">Bên Mua cam kết tuân thủ các quy định về <strong>cấm vận và trừng phạt</strong> của:</p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-808b-b4c5-caeadde01d46" class="bulleted-list"><li style="list-style-type:disc">Liên Hợp Quốc</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8083-acf4-f265a6e8c68c" class="bulleted-list"><li style="list-style-type:disc">Trung Quốc</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8040-bafc-ec0d9f623a6d" class="bulleted-list"><li style="list-style-type:disc">Hoa Kỳ</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-806c-9051-c10358271013" class="bulleted-list"><li style="list-style-type:disc">Liên minh Châu Âu</li></ul></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8002-8d23-ca69ef527d18" class="">Không tham gia bất kỳ giao dịch nào liên quan đến danh mục hàng hóa bị cấm vận.</p></div><div style="display:contents" dir="auto"><h3 id="2cfc5e6f-95bd-8063-bc35-f9ae31bd1cbc" class=""><strong>2.3</strong></h3></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80ac-ae91-c4a7d8b9a667" class="">Bên Bán có quyền <strong>kiểm tra, kiểm toán định kỳ hoặc đột xuất</strong> việc tuân thủ các cam kết trên.</p></div><div style="display:contents" dir="auto"><h3 id="2cfc5e6f-95bd-803f-9ce1-c6e831163715" class=""><strong>2.4</strong></h3></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80d2-990f-e3e8a1b5f4f2" class="">Nếu phát hiện vi phạm, Bên Bán có quyền:</p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8012-9023-c2866ff1ee23" class="bulleted-list"><li style="list-style-type:disc">chấm dứt hợp đồng ngay lập tức</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-809e-807a-e1c8e5435666" class="bulleted-list"><li style="list-style-type:disc"><strong>không phải bồi thường</strong> bất kỳ khoản nào.</li></ul></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-803a-9668-fc314cc3e291"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-80af-81bb-e09653a03fcf" class=""><strong>3. BẢO MẬT</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2cfc5e6f-95bd-80d0-88fa-fd578967699e" class=""><strong>3.1 Nghĩa vụ bảo mật</strong></h3></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-809b-8ba4-df57fc243747" class="">Trong suốt thời hạn hợp đồng và <strong>10 năm sau khi hợp đồng chấm dứt</strong>, Bên Nhận Thông Tin phải:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2cfc5e6f-95bd-8084-86ba-e1d24b0faf7b" class="numbered-list" start="1"><li>giữ bí mật thông tin;</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2cfc5e6f-95bd-80fd-bcda-db792a36f508" class="numbered-list" start="2"><li>chỉ sử dụng thông tin cho mục đích của hợp đồng;</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2cfc5e6f-95bd-80c2-8ac8-ed9e909376f3" class="numbered-list" start="3"><li>không tiết lộ cho bên thứ ba, trừ nhân viên, đại lý, luật sư, kế toán có nghĩa vụ bảo mật tương đương.</li></ol></div><div style="display:contents" dir="auto"><h3 id="2cfc5e6f-95bd-80dc-a053-c35cf4f381ac" class=""><strong>3.2 Ngoại lệ</strong></h3></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-803f-8601-d3da446ad409" class="">Nghĩa vụ bảo mật không áp dụng nếu thông tin:</p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-809f-b1ed-fd7b138669b8" class="bulleted-list"><li style="list-style-type:disc">đã biết trước bằng chứng văn bản;</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8007-a302-d4b06f950c87" class="bulleted-list"><li style="list-style-type:disc">đã công khai không do vi phạm hợp đồng;</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-803f-8e3a-e90e10c8ec0b" class="bulleted-list"><li style="list-style-type:disc">nhận từ bên thứ ba không bị ràng buộc bảo mật.</li></ul></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-80d3-9978-ed1674f5f418"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-80ce-bd58-e9cfc1972d4d" class=""><strong>4. BẤT KHẢ KHÁNG</strong></h2></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-803f-992d-f325121388d1" class="">Không bên nào chịu trách nhiệm nếu không thể thực hiện hợp đồng do:</p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-804a-9df9-cce44edca208" class="bulleted-list"><li style="list-style-type:disc">thiên tai, chiến tranh, hỏa hoạn, động đất, hạn hán,</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-802f-8c02-f1026a9a72a0" class="bulleted-list"><li style="list-style-type:disc">hoặc sự kiện ngoài khả năng kiểm soát.</li></ul></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8021-92ab-e3f42a9fc202" class="">Bên bị ảnh hưởng phải:</p></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80ad-94a6-d71aaec44873" class="bulleted-list"><li style="list-style-type:disc">thông báo bằng văn bản sớm nhất;</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8039-8678-f7a3db06849b" class="bulleted-list"><li style="list-style-type:disc">cung cấp xác nhận của cơ quan có thẩm quyền trong vòng <strong>15 ngày</strong>.</li></ul></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8023-a14a-c68672cfad4f" class="">Nếu sự kiện kéo dài quá <strong>60 ngày</strong>, hai bên sẽ thương lượng tiếp tục hoặc chấm dứt hợp đồng.</p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-8077-95d7-fd13e2d9018e"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-8077-83c7-ecdc7d10f953" class=""><strong>5. NGÔN NGỮ HỢP ĐỒNG</strong></h2></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-809d-8897-c0894a10145f" class="">Hợp đồng được lập bằng <strong>tiếng Anh</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-802f-872e-d6450e19977e"/></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8068-a56e-ee1c320df20e" class=""><strong>ĐẠI DIỆN BÊN BÁN:</strong></p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8044-8f19-f2a88b734ddf" class="">HENGWAI HOLDING LIMITED</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-807f-965d-d1fb689753f6" class="">(Ký)</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8058-ae99-f3aff47f07e3" class=""><strong>ĐẠI DIỆN BÊN MUA:</strong></p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8075-970d-eaac2877d83b" class="">(Ký)</p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-8012-852f-f230ad36d7ee"/></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
