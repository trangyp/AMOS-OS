---
tags: [vietnamese]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title> THIẾT KẾ MÔ HÌNH MÔI GIỚI BẤT ĐỘNG SẢN</title><style>
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
	
</style></head><body><article id="371c5e6f-95bd-80d1-bd7b-f080b0e5e9a1" class="page sans"><header><h1 class="page-title" dir="auto"> THIẾT KẾ MÔ HÌNH MÔI GIỚI BẤT ĐỘNG SẢN</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80e6-b55b-ed9c0f33ed60" class=""> <strong>Công ty Môi giới Số tinh gọn (Digital Brokerage Studio)</strong> </p></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-804d-8aae-c6e737799ffc" class="">I. TÁI CẤU TRÚC SƠ ĐỒ TỔ CHỨC: CON NGƯỜI VS. AGENT</h2></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8003-97c9-e08bd695b5bc" class="">Mô hình vận hành mới triệt tiêu các phòng ban Telesales, Admin nhập liệu và Marketing thô. Bộ máy công ty được chia làm 2 tầng rõ rệt:</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80f6-815a-dd99501dac84" class=""><code>                  [ BAN ĐIỀU HÀNH / SOLOPRENEUR ]<br/>                                │<br/>         ┌──────────────────────┴──────────────────────┐<br/>         ▼                                             ▼<br/>┌─────────────────────────────────┐   ┌─────────────────────────────────┐<br/>│ TẦNG ĐỊNH LƯỢNG (AUTOMATED AI)  │   │  TẦNG ĐỊNH TÍNH (HUMAN ELITE)   │<br/>├─────────────────────────────────┤   ├─────────────────────────────────┤<br/>│ - Agent 1: The Gatekeeper (Pháp │   │ - Broker Thợ Cả: Dẫn khách thực │<br/>│   lý, Quy hoạch, Đọc sổ OCR).   │   │   tế, xử lý từ chối.            │<br/>│ - Agent 2: The Qualifier (Trực  │   │ - Giám đốc Pháp lý: Kiểm duyệt  │<br/>│   Zalo OA 24/7, lọc BANT).      │   │   giao dịch cuối, ký công chứng.│<br/>│ - Agent 3: The Matchmaker       │   │ - Tech Admin: Bảo trì luồng     │<br/>│   (Quét Airtable, xuất PDF Desk)│   │   n8n, tối ưu Prompt.           │<br/>└─────────────────────────────────┘   └─────────────────────────────────┘</code></p></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-8071-9821-d5e83a4916c8" class="">II. LUỒNG VẬN HÀNH 4 BƯỚC THỰC CHIẾN (DOCK-TO-SHIP DATA FLOW)</h2></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-801f-a698-eaaec05a613a" class="">Mọi dữ liệu bất động sản và thông tin khách hàng biến động theo thời gian thực ($E$ - State transitions) được xử lý qua 4 bước khép kín nhằm bảo vệ uy tín thương hiệu và tối ưu tỷ lệ chốt deal.</p></div><div style="display:contents" dir="auto"><h3 id="371c5e6f-95bd-80bf-9e8b-d53193237435" class="">Bước 1: Tiếp nhận &amp; Kiểm toán Đầu vào (Rổ hàng &amp; Pháp lý)</h3></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8026-9ff6-c799503f572e" class="bulleted-list"><li style="list-style-type:disc"><strong>Hành động của Agent 1 (The Gatekeeper):</strong> Khi có thông tin ký gửi mới, Agent 1 sử dụng công nghệ Vision OCR để đọc ảnh quét Sổ đỏ/Sổ hồng. Hệ thống tự động tách xuất các trường thông tin: <em>Số tờ, Số thửa, Diện tích, Tọa độ XY</em>.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8085-927a-d8dbd2d7269e" class="bulleted-list"><li style="list-style-type:disc"><strong>Xử lý ngầm (Background Check):</strong> Gửi yêu cầu qua API/Webhook đến hệ thống dữ liệu quy hoạch địa phương để kiểm tra trạng thái tranh chấp, lộ giới, quy hoạch treo.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8084-ba11-fb602a39fea2" class="bulleted-list"><li style="list-style-type:disc">Nếu đạt tiêu chuẩn $\rightarrow$ Tự động đẩy vào Database <strong>Airtable</strong> ở trạng thái <code>[Sẵn sàng giao dịch]</code>.</li></ul></div><div style="display:contents" dir="auto"><h3 id="371c5e6f-95bd-8043-aee7-fb56c916846c" class="">Bước 2: Tiếp cận &amp; Phân loại Động (Sàng lọc BANT 24/7)</h3></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8032-8c8f-f63e4d63baef" class="bulleted-list"><li style="list-style-type:disc"><strong>Hành động của Agent 2 (The Qualifier):</strong> Toàn bộ Lead thô từ quảng cáo Facebook/Google/TikTok đổ về sẽ được phân phối ngay lập tức cho Agent 2 trên Zalo OA trong vòng tối đa <strong>30 giây</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8033-ad7a-db26e01aaf92" class="bulleted-list"><li style="list-style-type:disc"><strong>Hội thoại nghệ thuật:</strong> Áp dụng kỹ thuật <em>Tư vấn ngược và Đồng cảm (Empathetic Inverted Consulting)</em> theo kịch bản Prompt được thiết lập sẵn để trích xuất cấu trúc dữ liệu khách hàng:</li></ul></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8087-87a7-e46b400d95ae" class="">$$\text{Trạng thái Lead} = f(\text{Budget}, \text{Authority}, \text{Need}, \text{Timeline})$$</p></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8098-95ec-cc8742f4f75c" class="bulleted-list"><li style="list-style-type:disc">Chỉ khi thu thập đủ tối thiểu $3/4$ thông tin và không dính điểm liệt tài chính, trạng thái dữ liệu mới chuyển từ <code>[Cold Lead]</code> $\rightarrow$ <code>[Hot Lead]</code>.</li></ul></div><div style="display:contents" dir="auto"><h3 id="371c5e6f-95bd-80df-b73f-c3d17e59ad76" class="">Bước 3: Khớp nối &amp; Đóng gói Giải pháp Tài chính</h3></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80bc-a8e1-ebbf68904d8d" class="bulleted-list"><li style="list-style-type:disc"><strong>Hành động của Agent 3 (The Matchmaker):</strong> Nhận tín hiệu <code>[Hot Lead]</code>, Agent 3 thực hiện truy vấn (Query) thời gian thực vào bảng Airtable.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80a8-bc68-fb7f7adfcd0c" class="bulleted-list"><li style="list-style-type:disc"><strong>Kiểm soát rổ hàng động (Dynamic Inventory Control):</strong><div style="display:contents" dir="auto"><blockquote id="371c5e6f-95bd-80fa-9151-c4e449b1cf33" class="">⚠️ <strong>Quy tắc chặn ngầm:</strong> Hệ thống bắt buộc phải kiểm tra cột <code>[Trạng thái]</code> của căn nhà. Nếu trong vòng 1 tiếng trước, căn nhà đã chuyển sang trạng thái <code>[Đang nhận cọc]</code> bởi một môi giới khác, Agent 3 sẽ tự động loại bỏ mã căn này ra khỏi thuật toán ghép nối, thay thế bằng căn có chỉ số tương đương để bảo vệ trải nghiệm khách hàng.</blockquote></div></li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-809b-8289-f89db361d56e" class="bulleted-list"><li style="list-style-type:disc"><strong>Xuất bản:</strong> Đổ dữ liệu sang Canva API, xuất ra file <strong>PDF Sales Deck</strong> (Giải pháp dòng tiền, vị trí, bài toán tài chính riêng cho khách) và gửi trực tiếp qua Zalo cho khách.</li></ul></div><div style="display:contents" dir="auto"><h3 id="371c5e6f-95bd-80aa-8747-fc5e21ce5f27" class="">Bước 4: Chuyển giao Định tính (Human Closing)</h3></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8005-86fc-cc28a3439c6f" class="bulleted-list"><li style="list-style-type:disc">Ngay khi khách hàng bấm mở xem file PDF, hệ thống n8n tự động kích hoạt Webhook bắn thông tin toàn bộ lịch sử trò chuyện của khách kèm mã định danh <strong>ID Lead</strong> vào nhóm Telegram của <strong>Broker Thợ Cả</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80bc-9027-fda899f1456a" class="bulleted-list"><li style="list-style-type:disc">Broker người tiếp quản từ khâu: Gọi điện hẹn giờ, đưa đi xem nhà trực tiếp, thương lượng giá và chốt hợp đồng.</li></ul></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-8036-bcca-cea467e80ac9" class="">III. THIẾT KẾ MÔ HÌNH DOANH THU &amp; ĐỐI SOÁT UY TÍN (UNIT ECONOMICS)</h2></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8008-bd62-db84cfa4e7d9" class="">Để vận hành an toàn trong bối cảnh thị trường Việt Nam chưa phổ biến cơ chế tài khoản phong tỏa (Escrow), mô hình tài chính được xây dựng trên nguyên tắc <strong>Hợp đồng Ghi nhận Nguồn (Source Tracking Contract)</strong>:</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80fd-bac8-da323f109248" class=""><code>[Khách mua hàng] ──(Sử dụng mã ID do AI gán)──&gt; [Ký công chứng tại Sàn]<br/>                                                      │<br/>                                                      ▼<br/>[AI Studio đối soát] &lt;──(Đối chiếu ID trên hợp đồng)── [Thu 5% - 10% Success Fee]</code></p></div><div style="display:contents" dir="auto"><h3 id="371c5e6f-95bd-8098-bf61-ca93dd9a1c31" class="">Bảng toán dòng tiền vận hành của Sàn Môi giới Mới (Dưới 30 nhân sự)</h3></div><div style="display:contents" dir="ltr"><table id="371c5e6f-95bd-80b6-95be-f7cfa96cbc58" class="simple-table"><tbody><div style="display:contents" dir="ltr"><tr id="371c5e6f-95bd-806f-aa7e-c0cc156f6773"><td id="YzRu" class=""><strong>Chỉ số vận hành (Metrics)</strong></td><td id="PS&lt;}" class=""><strong>Mô hình Truyền thống</strong></td><td id="JV&lt;u" class=""><strong>Mô hình Mới (AI Agent Lab)</strong></td><td id="v_ox" class=""><strong>Bản chất thay đổi</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="371c5e6f-95bd-80a3-b156-df4d3217126d"><td id="YzRu" class=""><strong>Chi phí nhân sự cố định</strong></td><td id="PS&lt;}" class="">50.000.000 VND / tháng <em>(Nuôi 5 Telesales/Admin)</em></td><td id="JV&lt;u" class=""><strong>10.000.000 VND / tháng</strong> <em>(Phí API &amp; duy trì hạ tầng n8n)</em></td><td id="v_ox" class="">Giảm 80% định phí, chuyển định phí thành biến phí theo lượng Lead.</td></tr></div><div style="display:contents" dir="ltr"><tr id="371c5e6f-95bd-80bc-99a2-e62e02a18afe"><td id="YzRu" class=""><strong>Thời gian phản hồi khách</strong></td><td id="PS&lt;}" class="">5 phút - 2 tiếng <em>(Phụ thuộc ca trực của con người)</em></td><td id="JV&lt;u" class=""><strong>&lt; 30 giây (24/7)</strong></td><td id="v_ox" class="">Bắt đúng điểm chạm tâm lý nóng nhất của khách hàng khi vừa xem quảng cáo.</td></tr></div><div style="display:contents" dir="ltr"><tr id="371c5e6f-95bd-8076-bff2-ce1c312dcecc"><td id="YzRu" class=""><strong>Tỷ lệ rò rỉ dữ liệu / Quên khách</strong></td><td id="PS&lt;}" class="">15% - 25% <em>(Do nhân sự quên nhập liệu, sót tin nhắn)</em></td><td id="JV&lt;u" class=""><strong>0%</strong></td><td id="v_ox" class="">Toàn bộ tiến trình hội thoại được lưu vết tự động vào hệ thống Airtable.</td></tr></div><div style="display:contents" dir="ltr"><tr id="371c5e6f-95bd-8028-aa80-dd0cacabd231"><td id="YzRu" class=""><strong>Hình thức tiếp cận khách</strong></td><td id="PS&lt;}" class="">Gửi tin nhắn text thô, spam hình ảnh gây ngộp thông tin</td><td id="JV&lt;u" class="">Gửi <strong>PDF Sales Deck</strong> cá nhân hóa cao cấp</td><td id="v_ox" class="">Định vị công ty thành đơn vị tư vấn tài chính, tăng tỷ lệ mở tin nhắn.</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h2 id="371c5e6f-95bd-803f-a0e4-d1962c0cd07d" class="">IV. KỊCH BẢN HÀNH ĐỘNG 7 NGÀY ĐỂ KÍCH HOẠT HỆ THỐNG</h2></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80e5-8816-f7349dc1db60" class="">Nếu anh Linh muốn kích hoạt ngay mô hình này cho doanh nghiệp của mình hoặc đóng gói mang đi cho thuê, hãy tuân thủ nghiêm ngặt lộ trình Sprints sau:</p></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8086-8b2d-dd6d02bfb103" class="bulleted-list"><li style="list-style-type:disc"><strong>Ngày 1 - Ngày 2:</strong> Chuẩn hóa cấu trúc dữ liệu của 100 căn hộ/đất nền thuộc phân khúc mục tiêu vào Airtable. Cấu hình rõ các cột: <code>Mã căn</code>, <code>Vị trí</code>, <code>Giá</code>, <code>Trạng thái giao dịch</code>, <code>Tọa độ</code>.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80f4-a2fc-c67401ce1272" class="bulleted-list"><li style="list-style-type:disc"><strong>Ngày 3 - Ngày 4:</strong> Cấu hình luồng n8n kết nối Zalo OA với Claude 3.5 Sonnet. Nạp đoạn <strong>System Prompt BANT nghệ thuật</strong> vào hệ thống. Thực hiện test giả lập 50 hội thoại để cấu hình chặn đứng hiện tượng AI tự &quot;bịa&quot; thông tin ngoài cơ sở dữ liệu.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-8067-a163-d686813b3d4e" class="bulleted-list"><li style="list-style-type:disc"><strong>Ngày 5:</strong> Thiết lập tính năng kiểm tra trạng thái ngầm (Background check) của rổ hàng trước khi xuất file PDF.</li></ul></div><div style="display:contents" dir="auto"><ul id="371c5e6f-95bd-80ed-b964-f7d18d5c08e3" class="bulleted-list"><li style="list-style-type:disc"><strong>Ngày 6 - Ngày 7:</strong> Chạy thử nghiệm thực tế với 20 khách hàng đầu tiên từ nguồn quảng cáo, đo lường tỷ lệ chuyển đổi từ Lead thô sang Lead Hot và thực hiện bàn giao dữ liệu tự động cho Broker người qua Telegram.</li></ul></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-806e-9cfb-fd6a36a36e41" class="">Mô hình này không chỉ giúp giảm thiểu tối đa áp lực tài chính cố định cho doanh nghiệp trong giai đoạn hiện tại, mà còn tạo ra một nền tảng vận hành cực kỳ vững chắc, sẵn sàng bùng nổ quy mô (Scale-up) với hiệu suất vượt trội khi dòng tiền thị trường bất động sản quay trở lại.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
