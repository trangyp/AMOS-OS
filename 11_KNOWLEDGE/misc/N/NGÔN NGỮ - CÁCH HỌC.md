---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>NGÔN NGỮ - CÁCH HỌC</title><style>
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
	
</style></head><body><article id="371c5e6f-95bd-8002-a572-fb9e32d5c462" class="page sans"><header><h1 class="page-title" dir="auto">NGÔN NGỮ - CÁCH HỌC</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80bc-bb54-fdd6841a98c7" class="">NHÀ BÁC HỌC NGÔN NGỮ TRƯƠNG VĨNH KÝ TỪNG KHIẾN NHÀ VĂN PHÁP KINH NGẠC- CÒN NHIỀU ĐIỀU TA CHƯA BIẾT</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8066-9b7f-e0b034cf5ae6" class="">Thông thạo 26 thứ tiếng lúc 25 tuổi, Trương Vĩnh Ký khiến nhà văn Pháp Émile Littré (1801-1881) kinh ngạc: &quot;Sự hiểu biết tới 26 ngoại ngữ của P. Trương Vĩnh Ký đủ để loài người tôn vinh anh như một nhà bác ngữ học (bác học ngôn ngữ) bậc nhất thời nay&quot;.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-805e-9494-fd74b3e94cf8" class="">Ngay từ thập kỷ 50 - 60 của thế kỷ XIX, Trương Vĩnh Ký, một người Việt Nam đã thông thạo nhiều ngôn ngữ Đông Nam Á cũng như các ngôn ngữ khác trên thế giới, như các thứ tiếng: Campuchia, Thái Lan, Lào, Malaysia, Myanmar, Chăm, Ấn Độ, Trung Quốc, Nhật Bản, Anh, Pháp, Ý, Bồ Đào Nha, Tây Ban Nha, Hi Lạp, Latin… để giao lưu và hội nhập dễ dàng với các nước trong khu vực và trên thế giới. Nhưng sự học của ông không hề bằng phẳng. Hơn thế, Trương Vĩnh Ký từ lúc lọt lòng mẹ (6-12-1837) ở Cái Mơn, xã Vĩnh Thành cho đến lúc qua đời (1-9-1898) ở Chợ Quán, Sài Gòn đã trải qua bao cơn sóng gió.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8075-9d35-cc1c3650e769" class="">Cha ông là cụ Trương Chánh Thi, quê quán Bình Định, vào Nam lập nghiệp ở một khu vực đất Vĩnh Long (nay khu vực này thuộc Bến Tre). Cha ông là một nhà Nho học, thích thi phú, được bổ nhiệm làm lãnh binh dưới triều Minh Mạng của nhà Nguyễn, mất lúc Trương Vĩnh Ký 3 tuổi. Mẹ ông là bà Nguyễn Thị Châu, một người mẹ hiền và lam lũ, sinh một gái và hai trai.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8045-a12f-ecdeaa87ea33" class="">3 tuổi, ông thuộc làu Tam tự kinh.  4 tuổi, ông học viết. 5 tuổi (năm 1842) cắp sách đến trường học chữ Nho, chữ Nôm với thầy giáo Học. Sau vài ba năm, ông thông suốt Minh Tâm Bửu Giám, đọc Tứ thư, Ngũ kinh, thuộc nhiều thơ Đường, thơ Tống...</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8029-858d-c94ac2359648" class="">Sau khi ông Trương Chánh Thi chết, một nhà truyền giáo thường được mọi người gọi là Cố Tám đã chỉ dạy cho cậu bé Trương Vĩnh Ký học chữ Latin, chữ Nôm và ít chữ sau này gọi chữ “Quốc ngữ“. Ông nhận thấy cậu Ký còn nhỏ mà có đầu óc thông minh hơn người, chỉ biết thú đọc sách hơn đi chơi đùa, có chí cầu tiến, đã gửi cậu Ký cho một người Pháp tên Borelle (tên Việt Nam là Thừa Hòa) ở Cái Nhum (Vĩnh Long) nhận nuôi dạy Trương Vĩnh Ký về tiếng Latin và tiếng Pháp năm 1846. Rồi ông Thừa Hòa phải đi xa nên đã nhờ một người Pháp tên là Bouilleaux (tên Việt Nam là Cố Long) lo hộ việc nuôi dưỡng và học hành của cậu Ký.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-806a-b2b6-d53052e03026" class="">Năm 11 tuổi (1848), Trương Vĩnh Ký được Cố Long gởi đến học tại Pinhalu (Phnom Penh, Campuchia) được xây cất ở giữa một rừng thốt nốt hoang vu gần sông Mekong và cách Phnom Penh độ 6 dặm, dành cho cả vùng Đông Nam Á và Trung Hoa. Lớp học có 25 học sinh từ 13-15 tuổi và Trương Vĩnh Ký là người nhỏ nhất. Trương Vĩnh Ký gặp gỡ, ăn ở chung với học sinh các nước Đông Nam Á như: Campuchia, Lào, Thái Lan, Myanmar, Trung Quốc, Nhật Bản, Ấn Độ, Ciampois (Chăm)… Kết quả: cậu thiếu niên 13 tuổi Ký đã nói và viết thông thạo các ngôn ngữ kể trên của các bạn cùng trường.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80f4-8062-dbcfa70e434f" class="">Trương Vĩnh Ký còn học ngoại ngữ ở các sách và tự điển có trong thư viện của nhà trường. Các nhà ngôn ngữ học đương thời cho rằng Trương Vĩnh Ký đã tự tìm ra những quy luật ngữ pháp giống nhau, khác nhau của các tiếng nước ngoài để học nhanh và dễ dàng.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80d2-86e3-c637e1ec853f" class="">Vào ngày mãn khóa học ở chủng viện Pinhalu, Trương Vĩnh Ký được chọn là một học sinh xuất sắc, đỗ đầu lớp và được tuyển lựa cùng hai người nữa để tiếp tục đi học ở đảo Penang, Malaysia.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-802d-8f85-d77fe679aa95" class="">Năm 14 tuổi (1851), Trương Vĩnh Ký tiếp tục được gởi vào trường ở Poulo Penang (một hòn đảo nhỏ trên vùng Nam Dương, thuộc Malaysia, nơi người Hoa và thổ dân Malaysia sống bằng kỹ nghệ khai thác mỏ kẽm.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80ca-9039-fab954492865" class="">Khi đến nơi, Trương Vĩnh Ký rất ngạc nhiên khi thấy một vùng đảo ở vùng Đông Nam Á mà có nếp sinh hoạt cơ giới ồn ào, một sự phát triển lạ thường mà ông chưa từng thấy ở nước mình và Cao Miên.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8074-9c1b-ed1ae57d3cc1" class="">Trong khoảng thời gian 7 năm theo học tại đây, Trương Vĩnh Ký học chuyên ngữ Latin và Hi Lạp. Ngoài ra, ông còn học nâng cao các thứ tiếng khác như Ấn Độ, Anh, Tây Ban Nha, Malaysia, Nhật, Hi Lạp, Thái Lan, Pháp, Ý…</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80f4-8e17-e6909f986cfb" class="">Trong thời gian theo học tại Penang, Trương Vĩnh Ký tự học tiếng Nhật, Ấn bằng cách cắt các báo cũ, rồi dùng phương pháp đối chiếu, diễn dịch mà tìm ra các mẹo luật văn phạm.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-802c-81a9-f21c4f4d2d8f" class="">Trương Vĩnh Ký thông thạo và nắm vững quy luật học các ngoại ngữ của các quốc gia trong khu vực và đã truyền kinh nghiệm của mình qua việc xuất bản sách. Vào cuối thập niên 1880, ông đã xuất bản sách dạy tiếng Thái Lan, Campuchia.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-804c-9ca6-c375733fbe93" class="">Đến năm 1892, ông soạn được ba bộ sách dạy tiếng Miến Điện (tức Myanmar ngày nay): Cours de langue birmane, Vocabulaire français-birman, Guide de la conversation birman[e]-français. Từ năm 1893, ông tiếp tục xuất bản sách dạy tiếng Lào, Malay, Tamoule (Tamil?), Ciampois (Chàm).</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8099-9a09-eca63ff48a52" class="">Émile Littré, nhà văn Pháp, năm 1862 đã viết: “Trên trái đất này rất khó tìm ra người thứ hai say mê ngôn ngữ như Trương Vĩnh Ký. Gặp người Anh, Trương Vĩnh Ký nói bằng tiếng Anh nhuần nhị như người Luân Đôn. Tiếp xúc với người Ý Đại Lợi, người Y Pha Nho, người Bồ Đào Nha... hay người Nhựt Bổn, Mã Lai, Xiêm... Trương Vĩnh Ký đều nói đúng theo âm luật của kinh đô nước đó... Sự hiểu biết tới 26 ngoại ngữ của P. Trương Vĩnh Ký đủ để loài người tôn vinh anh như một nhà bác ngữ học vào bậc nhất của thời nay”.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-805f-a157-fb12c1545d29" class="">Năm 1874, Trương Vĩnh Ký đã được thế giới bình chọn là “nhà bác học về ngôn ngữ”, nằm trong danh sách 18 nhà bác học thế giới của thế kỷ XIX, được ghi tên vào các danh nhân thế giới trong Tự điển Larousse.</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-8033-97ab-dd8444fd64c7" class="">Theo báo Tuổi trẻ</p></div><div style="display:contents" dir="auto"><p id="371c5e6f-95bd-80de-a180-e17a2a474241" class=""><strong><a href="https://tuoitre.vn/nha-bac-hoc-the-gioi-truong-vinh-ky-hoc-ngoai-ngu-sieu-pham-1030399.htm?fbclid=IwZXh0bgNhZW0CMTAAYnJpZBExT094WFBueElkTDdmUmV5c3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6c37WhAUvXaXzoLPgMg6K_gdo0kqaRB6JkwG0k5q4vp-QzlJENSZiLJ3zzgQ_aem__mJPS_cLA8ROREo8ND-RyQ">https://tuoitre.vn/nha-bac-hoc-the-gioi-truong-vinh-ky...</a></strong></p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
