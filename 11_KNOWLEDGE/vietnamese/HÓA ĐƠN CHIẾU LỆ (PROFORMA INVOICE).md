---
tags: [vietnamese]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>HÓA ĐƠN CHIẾU LỆ (PROFORMA INVOICE)</title><style>
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
	
</style></head><body><article id="2cfc5e6f-95bd-80b9-be2e-c466d9e3aea8" class="page sans"><header><h1 class="page-title" dir="auto"><strong>HÓA ĐƠN CHIẾU LỆ (PROFORMA INVOICE)</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-800d-be2f-f81ca16c4b5d" class=""><strong>CÔNG TY:</strong> HENGWAI HOLDING LIMITED</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8032-b336-c09c89ce9159" class=""><strong>ĐỊA CHỈ:</strong></p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80c7-a2c6-c1e444d29a80" class="">Phòng 2306, Khối A, Tầng 23, Tòa nhà Công nghiệp Luxury,</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8062-82a0-e6be3cd71d21" class="">Số 26–38 đường Kwai Cheong, Kwai Chung,</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-805e-a5eb-ec1b3dc78899" class="">New Territories, Hồng Kông, Trung Quốc</p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-8031-a8ad-eaa37af09d07"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-80f2-8e50-fabfdb3ece28" class=""><strong>HÓA ĐƠN CHIẾU LỆ (PROFORMA INVOICE)</strong></h2></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8011-b8ce-f0371dde5ada" class=""><strong>SỐ HÓA ĐƠN:</strong> HH2025121902</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80b5-a47d-e47d378849b4" class=""><strong>NGÀY:</strong> 19/12/2025</p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-800c-a083-eac578252954"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-80b8-9fa9-e7945954c176" class=""><strong>NGƯỜI NHẬN (TO):</strong></h2></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-80de-8db4-e2a150cde9b0" class=""><em>(Không ghi rõ trong hóa đơn)</em></p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-80a4-88f4-c658186fb34c"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-80e2-bd2b-eb491b64d6a7" class=""><strong>CHI TIẾT HÀNG HÓA</strong></h2></div><div style="display:contents" dir="ltr"><table id="2cfc5e6f-95bd-80d2-ad2d-ca999cc18f2a" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2cfc5e6f-95bd-80bf-b1db-f00bdbc49012"><th id="]vOb" class="simple-table-header-color simple-table-header"><strong>STT</strong></th><th id="vntW" class="simple-table-header-color simple-table-header"><strong>Hãng</strong></th><th id="mXbP" class="simple-table-header-color simple-table-header"><strong>Nhãn hiệu &amp; Mẫu xe</strong></th><th id="Zu~U" class="simple-table-header-color simple-table-header"><strong>Quy cách xe</strong></th><th id="Eq_c" class="simple-table-header-color simple-table-header"><strong>Màu sắc</strong></th><th id="y{Zz" class="simple-table-header-color simple-table-header"><strong>Số lượng</strong></th><th id="Pmea" class="simple-table-header-color simple-table-header"><strong>Đơn giá FOB (USD)</strong></th><th id="psgx" class="simple-table-header-color simple-table-header"><strong>Thành tiền FOB (USD)</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2cfc5e6f-95bd-80cb-9944-ddaef8dca336"><td id="]vOb" class="">1</td><td id="vntW" class="">Baojun</td><td id="mXbP" class="">Baojun E6</td><td id="Zu~U" class="">Phiên bản 2026 – Tầm hoạt động 500 km – Bản Enjoyment</td><td id="Eq_c" class="">Trắng</td><td id="y{Zz" class="">2</td><td id="Pmea" class="">12.570</td><td id="psgx" class="">25.140</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-8028-9994-cb76d352f2e6"/></div><div style="display:contents" dir="auto"><h3 id="2cfc5e6f-95bd-8064-9e2d-d2d0355a7365" class=""><strong>TỔNG CỘNG (FOB Cảng Nansha, Quảng Châu)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8025-a177-dc3a90a06596" class="bulleted-list"><li style="list-style-type:disc"><strong>Tổng số lượng:</strong> 2 xe</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8075-abbf-c79d01d42395" class="bulleted-list"><li style="list-style-type:disc"><strong>Đơn giá:</strong> 12.570 USD/xe</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80be-b5dd-e787bf56a828" class="bulleted-list"><li style="list-style-type:disc"><strong>Tổng giá trị:</strong> <strong>25.140 USD</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-8005-9731-f200573ac348"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-8030-bd25-c9577278ed87" class=""><strong>THÔNG TIN BÊN THỤ HƯỞNG (BNF – BENEFICIARY)</strong></h2></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8088-af62-ff6183e78604" class="bulleted-list"><li style="list-style-type:disc"><strong>TÊN CÔNG TY:</strong> HENGWAI HOLDING LIMITED</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80c5-921a-ca6df0269988" class="bulleted-list"><li style="list-style-type:disc"><strong>SỐ TÀI KHOẢN:</strong> NRA35601002010590002151</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8049-9d42-f4119aa97a6b" class="bulleted-list"><li style="list-style-type:disc"><strong>ĐỊA CHỈ CÔNG TY:</strong><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8049-b3ca-c83a15350e03" class="">Phòng 2306, Khối A, Tầng 23,</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-800b-9d8f-d6f1dbe58f69" class="">Tòa nhà Công nghiệp Luxury,</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-804c-98f6-df9d64503c5a" class="">Số 26–38 đường Kwai Cheong, Kwai Chung,</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-809e-a020-c52b0e4f208e" class="">New Territories, Hồng Kông</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-808c-88d1-f29e17b9ab22"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-80f2-8913-d140780034a6" class=""><strong>THÔNG TIN NGÂN HÀNG</strong></h2></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8098-8790-f4e3e112a689" class="bulleted-list"><li style="list-style-type:disc"><strong>TÊN NGÂN HÀNG:</strong> Zhejiang Chouzhou Commercial Bank Co., Ltd</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80cd-b607-e8cb8f6813da" class="bulleted-list"><li style="list-style-type:disc"><strong>ĐỊA CHỈ NGÂN HÀNG:</strong><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8020-b98c-e4ba2b554eac" class="">Tầng 2, Số 320 đường Wusibei,</p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-801c-80c5-c4a1a502e996" class="">Phúc Châu, Phúc Kiến, Trung Quốc, 350000</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80e2-a7f9-c124e90647e6" class="bulleted-list"><li style="list-style-type:disc"><strong>MÃ SWIFT:</strong> CZCBCN2XXXX</li></ul></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-80a7-9e89-d5e052d5be86"/></div><div style="display:contents" dir="auto"><h2 id="2cfc5e6f-95bd-80e6-b3a3-c7468a90cc40" class=""><strong>BÊN BÁN (SELLER)</strong></h2></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-806a-bdb9-d94796d61c74" class="bulleted-list"><li style="list-style-type:disc"><strong>Tên công ty:</strong> HENGWAI HOLDING LIMITED</li></ul></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-8051-ba7f-e8a776cc4d40" class=""><strong>ĐẠI DIỆN KÝ TÊN:</strong></p></div><div style="display:contents" dir="auto"><p id="2cfc5e6f-95bd-802c-86a9-dcf345b72cc4" class="">By: <em>(chưa ký)</em></p></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-802a-bd51-c5c5bf06296c"/></div><div style="display:contents" dir="auto"><h3 id="2cfc5e6f-95bd-8023-a877-c82423d8fa48" class=""><strong>GHI CHÚ QUAN TRỌNG</strong></h3></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80a0-b59b-cf883553c42c" class="bulleted-list"><li style="list-style-type:disc">Giá nêu trên là <strong>FOB (Free On Board)</strong> tại <strong>cảng Nansha, Quảng Châu</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-80ac-92fd-e611cef63130" class="bulleted-list"><li style="list-style-type:disc">Hóa đơn này là <strong>Proforma Invoice</strong>, <strong>không phải hóa đơn thương mại cuối cùng</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8077-939a-dd069350fc64" class="bulleted-list"><li style="list-style-type:disc">Dùng làm cơ sở cho:<div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-808a-ad42-f1b865443c77" class="bulleted-list"><li style="list-style-type:circle">Đàm phán hợp đồng</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8003-ae46-e329a8ce4d5a" class="bulleted-list"><li style="list-style-type:circle">Mở L/C hoặc chuyển tiền T/T</li></ul></div><div style="display:contents" dir="auto"><ul id="2cfc5e6f-95bd-8067-863e-eb9f73644c73" class="bulleted-list"><li style="list-style-type:circle">Chuẩn bị hồ sơ nhập khẩu</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2cfc5e6f-95bd-8019-863f-d0963138ed99"/></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
