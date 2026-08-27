---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>BÁO CÁO KỸ THUẬT – TÍCH HỢP UNITAXI (APK)</title><style>
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
	
</style></head><body><article id="2b9c5e6f-95bd-8070-81e0-db78ba78b1f1" class="page sans"><header><h1 class="page-title" dir="auto"><strong>BÁO CÁO KỸ THUẬT – TÍCH HỢP UNITAXI (APK)</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2b9c5e6f-95bd-8076-b4c9-e82b9c6af792" class="">Triển khai Hệ Điều Hành Vận Hành UniPower (3N: Nhàn – Nhanh – Nhạy)**</p></div><div style="display:contents" dir="auto"><p id="2b9c5e6f-95bd-80f3-a4ba-ef261cc8d098" class=""><strong>Dành cho CEO – CTO – Ban Điều Hành UniPower</strong></p></div><div style="display:contents" dir="auto"><hr id="2b9c5e6f-95bd-80b7-9e8d-d2e7dbe9f517"/></div><div style="display:contents" dir="auto"><h1 id="2b9c5e6f-95bd-8053-83e6-cde3d0afc4ed" class=""><strong>I. EXECUTIVE SUMMARY</strong></h1></div><div style="display:contents" dir="auto"><p id="2b9c5e6f-95bd-802b-b3ba-ea816b2c3a98" class="">UniTaxi (Rider App + Driver App) vận hành trên <strong>Wooberly backend</strong>, đang kết nối với:</p></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80ca-8f85-c822114b1976" class="bulleted-list"><li style="list-style-type:disc">hệ thống điều phối chuyến (Wooberly),</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-8002-8484-c0673a0a1c56" class="bulleted-list"><li style="list-style-type:disc">hệ thống xe – tài xế – doanh thu của UniPower,</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-808c-b959-f51f97615a46" class="bulleted-list"><li style="list-style-type:disc">hạ tầng trạm sạc <strong>iSAC</strong>,</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-800e-b743-fd789e6d2248" class="bulleted-list"><li style="list-style-type:disc">đối soát – kế toán – hóa đơn qua <strong>MISA AMIS</strong>.</li></ul></div><div style="display:contents" dir="auto"><p id="2b9c5e6f-95bd-8077-ae1b-c671f7aec0e0" class=""><strong>Mục tiêu dự án AMIS:</strong></p></div><div style="display:contents" dir="auto"><ol type="1" id="2b9c5e6f-95bd-803b-8686-da35bd488393" class="numbered-list" start="1"><li>Đưa toàn bộ dữ liệu &amp; quy trình UniTaxi → <strong>Hệ điều hành vận hành thống nhất (AMIS)</strong>.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b9c5e6f-95bd-8014-98ef-e60266751f6a" class="numbered-list" start="2"><li>Tự động hóa 60–70% quy trình vận hành (onboarding, cuốc xe, tài chính, bảo trì, trạm sạc).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b9c5e6f-95bd-80be-9a98-eb938c2af613" class="numbered-list" start="3"><li>Giảm tải thủ công, tăng tốc đối soát, nâng cấp khả năng mở rộng lên 2.000–10.000 xe.</li></ol></div><div style="display:contents" dir="auto"><p id="2b9c5e6f-95bd-8013-a467-f9207870cfdd" class=""><strong>Đánh giá kỹ thuật: khả thi 95%</strong> nếu đảm bảo:</p></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-803d-a34f-c086c6aedd7e" class="bulleted-list"><li style="list-style-type:disc">Chuẩn hóa <strong>Data Contract Wooberly → AMIS → iSAC</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-8093-b581-f97ead502c88" class="bulleted-list"><li style="list-style-type:disc">Xây lớp tích hợp <strong>Integration Layer (API Gateway + Message Queue + ETL)</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80c4-b7b0-d8bdaa53c530" class="bulleted-list"><li style="list-style-type:disc">Tạo <strong>Master Data Management (MDM)</strong> cho tài xế – xe – cuốc – trạm iSAC</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-805c-8890-dd8946f30b48" class="bulleted-list"><li style="list-style-type:disc">Thiết kế <strong>Dashboard vận hành realtime UniTaxi</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="2b9c5e6f-95bd-805d-b2a3-c0038b068a31"/></div><div style="display:contents" dir="auto"><h1 id="2b9c5e6f-95bd-803c-943f-d9f8843a7af1" class=""><strong>II. KIỂM TRA TÍNH KHẢ THI KỸ THUẬT</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2b9c5e6f-95bd-8067-bdb8-f336e988582c" class=""><strong>1. Nguồn dữ liệu cần tích hợp từ UniTaxi (Wooberly backend)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2b9c5e6f-95bd-80df-a4f9-f06121dd499b" class=""><strong>A. Dữ liệu từ Rider App (khách hàng)</strong></h3></div><div style="display:contents" dir="ltr"><table id="2b9c5e6f-95bd-80b4-9aa8-f1e3488265c1" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b9c5e6f-95bd-8096-995b-cd613a89eafc"><th id="pEjm" class="simple-table-header-color simple-table-header"><strong>Nhóm</strong></th><th id="DvIZ" class="simple-table-header-color simple-table-header"><strong>Trường chính</strong></th><th id="&gt;x{]" class="simple-table-header-color simple-table-header"><strong>Mức độ</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b9c5e6f-95bd-80fc-966c-ea1835b69373"><td id="pEjm" class="">Cuốc xe</td><td id="DvIZ" class="">trip_id, customer_id, start_time, end_time, route, distance, status</td><td id="&gt;x{]" class="">Bắt buộc</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b9c5e6f-95bd-808a-bd3f-f6a2426c6a97"><td id="pEjm" class="">Thanh toán</td><td id="DvIZ" class="">amount, method, transaction_id, captured_status</td><td id="&gt;x{]" class="">Bắt buộc</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b9c5e6f-95bd-80c0-a269-d977a8931ae5"><td id="pEjm" class="">Phản hồi</td><td id="DvIZ" class="">rating, complaint_code</td><td id="&gt;x{]" class="">Khuyến nghị</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b9c5e6f-95bd-80db-aa97-e6e519367099"/></div><div style="display:contents" dir="auto"><h3 id="2b9c5e6f-95bd-805c-b1aa-df0e3f8b4764" class=""><strong>B. Dữ liệu từ Driver App (tài xế)</strong></h3></div><div style="display:contents" dir="ltr"><table id="2b9c5e6f-95bd-80e1-b0e1-e7056447801f" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b9c5e6f-95bd-8015-93b6-dc264c50b492"><th id="Tp&lt;[" class="simple-table-header-color simple-table-header"><strong>Nhóm</strong></th><th id="?yU[" class="simple-table-header-color simple-table-header"><strong>Trường chính</strong></th><th id="E@by" class="simple-table-header-color simple-table-header"><strong>Mức độ</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b9c5e6f-95bd-80a9-bd60-ee65dae7d293"><td id="Tp&lt;[" class="">Tài xế</td><td id="?yU[" class="">driver_id, license, contract_type, status</td><td id="E@by" class="">Bắt buộc</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b9c5e6f-95bd-8039-a41c-ebf42a78b1cf"><td id="Tp&lt;[" class="">Xe</td><td id="?yU[" class="">vehicle_id, battery_level, odometer, health_status</td><td id="E@by" class="">Bắt buộc</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b9c5e6f-95bd-80c5-b105-c135cce3b54a"><td id="Tp&lt;[" class="">Hoạt động</td><td id="?yU[" class="">online, offline, busy, idle, trip_assigned</td><td id="E@by" class="">Bắt buộc</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b9c5e6f-95bd-8031-8b31-f260ec26ed52"/></div><div style="display:contents" dir="auto"><h3 id="2b9c5e6f-95bd-8067-82ae-d22c0e65f50f" class=""><strong>C. Dữ liệu từ iSAC (trạm sạc &amp; phiên sạc)</strong></h3></div><div style="display:contents" dir="ltr"><table id="2b9c5e6f-95bd-80d7-b876-e02aa996f75b" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b9c5e6f-95bd-80d8-83af-d51673c8ada7"><th id="@h&lt;J" class="simple-table-header-color simple-table-header"><strong>Nhóm</strong></th><th id="M&gt;|r" class="simple-table-header-color simple-table-header"><strong>Trường chính</strong></th><th id="iOok" class="simple-table-header-color simple-table-header"><strong>Mục đích</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b9c5e6f-95bd-80ff-bb08-e54474f3848a"><td id="@h&lt;J" class="">Trạm sạc</td><td id="M&gt;|r" class="">station_id, charger_id, status, error_code</td><td id="iOok" class="">Giám sát vận hành</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b9c5e6f-95bd-80d9-be00-faf998fb771d"><td id="@h&lt;J" class="">Phiên sạc</td><td id="M&gt;|r" class="">session_id, vehicle_id, kWh, cost, start_time, end_time</td><td id="iOok" class="">Đối soát chi phí</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b9c5e6f-95bd-80ae-998d-fe1387038f3d"><td id="@h&lt;J" class="">Doanh thu sạc</td><td id="M&gt;|r" class="">amount, tax, reconciled_flag</td><td id="iOok" class="">Đẩy sang AMIS Finance</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b9c5e6f-95bd-803a-952d-d6313b9dc829"/></div><div style="display:contents" dir="auto"><h2 id="2b9c5e6f-95bd-80e7-b93c-da21db86f0e4" class=""><strong>2. Tính khả thi kết nối AMIS</strong></h2></div><div style="display:contents" dir="auto"><p id="2b9c5e6f-95bd-80c7-ad2d-eb6c2a7deef6" class=""><strong>Cách tích hợp khả thi:</strong></p></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-8077-bc7a-ed25d99e2c2c" class="bulleted-list"><li style="list-style-type:disc">REST API 2 chiều</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-808e-b96f-f866fcd9cced" class="bulleted-list"><li style="list-style-type:disc">Webhook: TripStatusUpdated, PaymentCaptured, ChargerStatusChanged</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80f4-a3fa-f4c70fb6e329" class="bulleted-list"><li style="list-style-type:disc">Message Queue (Kafka / RabbitMQ): xử lý giờ cao điểm</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-8015-aeea-c0914a88c0fe" class="bulleted-list"><li style="list-style-type:disc">ETL batch cuối ngày: reconciliation</li></ul></div><div style="display:contents" dir="auto"><p id="2b9c5e6f-95bd-806b-9c73-d7c1a755fa11" class=""><strong>Rủi ro &amp; giải pháp</strong></p></div><div style="display:contents" dir="ltr"><table id="2b9c5e6f-95bd-805c-9be9-f50e6816d178" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b9c5e6f-95bd-8023-b98a-e7ace0ccef21"><th id="vA=Q" class="simple-table-header-color simple-table-header"><strong>Rủi ro</strong></th><th id="SBL;" class="simple-table-header-color simple-table-header"><strong>Giải pháp</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b9c5e6f-95bd-8027-93f4-c2c0f0a2c493"><td id="vA=Q" class="">Data Wooberly không thống nhất</td><td id="SBL;" class="">Data Contract + MDM</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b9c5e6f-95bd-8063-baec-ecbdefea5169"><td id="vA=Q" class="">API bị nghẽn giờ cao điểm</td><td id="SBL;" class="">Queue + Cache Layer</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b9c5e6f-95bd-80f0-a100-e9a8bdd7ae62"><td id="vA=Q" class="">Trùng lặp sự kiện</td><td id="SBL;" class="">Idempotent API + Event Sourcing</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b9c5e6f-95bd-8079-9921-f819f80764ea"><td id="vA=Q" class="">Chênh lệch doanh thu giữa Wooberly – cổng thanh toán – iSAC – AMIS</td><td id="SBL;" class="">Reconciliation pipeline</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b9c5e6f-95bd-8049-b9a3-de16a1fbc8fa"/></div><div style="display:contents" dir="auto"><h1 id="2b9c5e6f-95bd-807b-a96f-d2c2a22f6101" class=""><strong>III. KIẾN TRÚC KỸ THUẬT UNI-TAXI → AMIS</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2b9c5e6f-95bd-8070-9d61-e886bfb23669" class=""><strong>1. Kiến trúc tổng thể</strong></h2></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2b9c5e6f-95bd-8062-8870-d9f32dc2a8eb" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">Rider App (Wooberly)
Driver App (Wooberly)
           ↓
       Wooberly Backend
           ↓
  Integration Layer (API Gateway + MQ + ETL)
           ↓
          AMIS
 (CRM • HRM • Finance • Workflow • Dashboard)

iSAC → Integration Layer → AMIS (song song)</code></pre></div><div style="display:contents" dir="auto"><hr id="2b9c5e6f-95bd-8017-85c4-dee1c7040da1"/></div><div style="display:contents" dir="auto"><h2 id="2b9c5e6f-95bd-80e9-b9a0-e2fa4113db9c" class=""><strong>2. Luồng dữ liệu theo nhóm</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2b9c5e6f-95bd-808d-be9c-f8c6b5f22e7f" class=""><strong>A. Luồng cuốc xe (Trip Flow)</strong></h3></div><div style="display:contents" dir="auto"><p id="2b9c5e6f-95bd-8060-8f59-ed05e9693095" class="">Nguồn: <strong>Wooberly</strong> → Đích: <strong>AMIS Workflow + AMIS Finance</strong></p></div><div style="display:contents" dir="auto"><p id="2b9c5e6f-95bd-8094-8672-d1bee5ddb35a" class=""><strong>Sự kiện bắt buộc:</strong></p></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80bf-a264-f9032d77eabb" class="bulleted-list"><li style="list-style-type:disc">TripCreated</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-807f-8843-c92ecf6c50c0" class="bulleted-list"><li style="list-style-type:disc">DriverAssigned</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80ec-b77b-f0a8e8510387" class="bulleted-list"><li style="list-style-type:disc">TripStart</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-808f-883a-e199e7100cbe" class="bulleted-list"><li style="list-style-type:disc">TripEnd</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80ed-9669-e1f219cb7426" class="bulleted-list"><li style="list-style-type:disc">PaymentCaptured</li></ul></div><div style="display:contents" dir="auto"><p id="2b9c5e6f-95bd-805f-9791-f5c8b7d0a605" class=""><strong>Mục tiêu vận hành:</strong></p></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-8017-a13f-f4edc2b440a0" class="bulleted-list"><li style="list-style-type:disc">CEO biết số cuốc theo giờ</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80f0-9e44-eba52931fb1b" class="bulleted-list"><li style="list-style-type:disc">CFO biết doanh thu theo trạng thái</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80d1-b8de-d230b7e6259a" class="bulleted-list"><li style="list-style-type:disc">Ops phát hiện điểm nghẽn (tài xế, khu vực, ứng dụng)</li></ul></div><div style="display:contents" dir="auto"><hr id="2b9c5e6f-95bd-80e3-9ede-d8d788ebb66d"/></div><div style="display:contents" dir="auto"><h3 id="2b9c5e6f-95bd-80df-985b-e3990564646a" class=""><strong>B. Luồng xe điện (EV Operations)</strong></h3></div><div style="display:contents" dir="auto"><p id="2b9c5e6f-95bd-8080-8e37-d2ea18c8ce44" class="">Nguồn: Driver App → Wooberly → AMIS</p></div><div style="display:contents" dir="auto"><p id="2b9c5e6f-95bd-8011-902a-d3494bcefbef" class=""><strong>Dữ liệu cần:</strong></p></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-8059-a410-ec4ac6caee03" class="bulleted-list"><li style="list-style-type:disc">battery_level</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-808c-9d10-efbfc783e03f" class="bulleted-list"><li style="list-style-type:disc">last_charge</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-8029-a9d0-dab0f706a127" class="bulleted-list"><li style="list-style-type:disc">predicted_range</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-803e-88d0-d27bc9d18da1" class="bulleted-list"><li style="list-style-type:disc">health_status</li></ul></div><div style="display:contents" dir="auto"><p id="2b9c5e6f-95bd-80f9-bdaf-f988f0371ea5" class=""><strong>Ứng dụng:</strong></p></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80c7-a7fd-c616589c7d77" class="bulleted-list"><li style="list-style-type:disc">Cảnh báo pin thấp</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80ca-97f4-cb5c37036e2b" class="bulleted-list"><li style="list-style-type:disc">Tự động tạo ticket bảo trì</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-805a-9cbd-e9c0a7fe9046" class="bulleted-list"><li style="list-style-type:disc">Phân bổ xe – tài xế – tuyến theo pin</li></ul></div><div style="display:contents" dir="auto"><hr id="2b9c5e6f-95bd-8064-bfeb-c6867f7e593c"/></div><div style="display:contents" dir="auto"><h3 id="2b9c5e6f-95bd-8074-8127-f6ccfc3feb6a" class=""><strong>C. Luồng trạm sạc (iSAC)</strong></h3></div><div style="display:contents" dir="auto"><p id="2b9c5e6f-95bd-80e5-abfa-f88fc1dc67a1" class="">Nguồn: iSAC → Integration Layer → AMIS</p></div><div style="display:contents" dir="auto"><p id="2b9c5e6f-95bd-807a-8be5-f1eb8477db1d" class=""><strong>Sự kiện:</strong></p></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80d7-9891-f21d85bb8020" class="bulleted-list"><li style="list-style-type:disc">ChargerStatusChanged</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-8018-9192-c17041926ebb" class="bulleted-list"><li style="list-style-type:disc">SessionStart / SessionEnd</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80cc-aafc-fdb91f6cddab" class="bulleted-list"><li style="list-style-type:disc">SessionRevenue</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80a6-bdd6-d4f913453162" class="bulleted-list"><li style="list-style-type:disc">ChargerOffline</li></ul></div><div style="display:contents" dir="auto"><p id="2b9c5e6f-95bd-806b-a346-f9b3c363cf73" class=""><strong>Ứng dụng:</strong></p></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-809a-91e9-c33d3802578d" class="bulleted-list"><li style="list-style-type:disc">Cảnh báo realtime</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80fb-a7f2-f2711ae10690" class="bulleted-list"><li style="list-style-type:disc">Đối soát doanh thu sạc</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80b8-94b2-d882f19c89a8" class="bulleted-list"><li style="list-style-type:disc">Tính EV cost per trip</li></ul></div><div style="display:contents" dir="auto"><hr id="2b9c5e6f-95bd-8003-9488-ca94b0a28602"/></div><div style="display:contents" dir="auto"><h1 id="2b9c5e6f-95bd-80df-8217-e26c26ab22a8" class=""><strong>IV. ROADMAP TRIỂN KHAI 12 THÁNG (UNI-TAXI + iSAC + AMIS)</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2b9c5e6f-95bd-80e4-a1e5-e814fabeeff1" class=""><strong>Giai đoạn 0 — 0 đến 4 tuần</strong></h2></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-8032-ab03-cf0d50844ee5" class="bulleted-list"><li style="list-style-type:disc">Xây <strong>Data Contract</strong>: trip / driver / vehicle / station / charger / session</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-8018-9c8e-f73127131297" class="bulleted-list"><li style="list-style-type:disc">Chuẩn hóa schema trong Wooberly + iSAC</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80ec-8db9-c32e46c48a38" class="bulleted-list"><li style="list-style-type:disc">Thiết lập Integration Layer</li></ul></div><div style="display:contents" dir="auto"><hr id="2b9c5e6f-95bd-80df-9583-d00f5f2f110f"/></div><div style="display:contents" dir="auto"><h2 id="2b9c5e6f-95bd-80c2-a500-cc7fa7237a58" class=""><strong>Giai đoạn 1 — 1 đến 3 tháng</strong></h2></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-8072-be58-de0a82f6afa7" class="bulleted-list"><li style="list-style-type:disc">Kết nối 3 luồng cốt lõi: <strong>Trip – Revenue – Driver</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-8005-970a-f193bf539b71" class="bulleted-list"><li style="list-style-type:disc">Tạo Dashboard <strong>UniTaxi Realtime</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-8081-a56b-e8005185cdb0" class="bulleted-list"><li style="list-style-type:disc">Đối soát doanh thu cơ bản</li></ul></div><div style="display:contents" dir="auto"><hr id="2b9c5e6f-95bd-80ee-8b5b-cc45bf459e87"/></div><div style="display:contents" dir="auto"><h2 id="2b9c5e6f-95bd-80e4-a234-e5df153ed3fd" class=""><strong>Giai đoạn 2 — 3 đến 6 tháng</strong></h2></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80ba-b151-dd4caea8bc6f" class="bulleted-list"><li style="list-style-type:disc">Tự động hóa onboarding tài xế</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-8059-9bd1-f53305f4c4d0" class="bulleted-list"><li style="list-style-type:disc">Tự động hóa reconciliation Wooberly – iSAC – AMIS – cổng thanh toán</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-8042-bbcf-f0a6b5d6f5f9" class="bulleted-list"><li style="list-style-type:disc">Tự động ticket bảo trì xe</li></ul></div><div style="display:contents" dir="auto"><hr id="2b9c5e6f-95bd-80bb-a67c-eab91bc937f5"/></div><div style="display:contents" dir="auto"><h2 id="2b9c5e6f-95bd-80dd-9441-d1c0681e7ebd" class=""><strong>Giai đoạn 3 — 6 đến 12 tháng</strong></h2></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80a9-ae38-ebc55aa7d931" class="bulleted-list"><li style="list-style-type:disc">Tích hợp CRM – HRM – Finance đầy đủ</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-802b-bd23-ed89b0c1d05a" class="bulleted-list"><li style="list-style-type:disc">Chuẩn hóa vòng đời tài xế &amp; xe</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80d5-b4ee-d15db3f04b0e" class="bulleted-list"><li style="list-style-type:disc">Mở rộng sang tỉnh/thành mới</li></ul></div><div style="display:contents" dir="auto"><hr id="2b9c5e6f-95bd-80ed-a7f4-d3d78cb295ca"/></div><div style="display:contents" dir="auto"><h1 id="2b9c5e6f-95bd-80cb-bb90-fc7e3f849636" class=""><strong>V. KPI GIÁM SÁT</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2b9c5e6f-95bd-8052-9434-f5a021d3919e" class=""><strong>A. KPI vận hành</strong></h2></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80f4-a19f-da3be3491dda" class="bulleted-list"><li style="list-style-type:disc">Trip Success Rate ≥ <strong>94%</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-8065-8c1c-cd165f50348b" class="bulleted-list"><li style="list-style-type:disc">Cuốc lỗi do app &lt; <strong>1%</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-808f-85aa-f4d6a89151a3" class="bulleted-list"><li style="list-style-type:disc">Time-to-assign &lt; <strong>6 giây</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80b7-ad35-ebdd31f0f3f3" class="bulleted-list"><li style="list-style-type:disc">Driver Online Peak ≥ <strong>70%</strong></li></ul></div><div style="display:contents" dir="auto"><h2 id="2b9c5e6f-95bd-80f5-8cdb-f57010f28151" class=""><strong>B. KPI tài chính</strong></h2></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-806f-86a6-c97e75f1305e" class="bulleted-list"><li style="list-style-type:disc">Revenue reconciliation accuracy ≥ <strong>99%</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-8043-ae23-d22b19f31e61" class="bulleted-list"><li style="list-style-type:disc">Revenue leakage giảm ≥ <strong>30%</strong></li></ul></div><div style="display:contents" dir="auto"><h2 id="2b9c5e6f-95bd-80db-8a05-fed56b7d4668" class=""><strong>C. KPI đội xe EV</strong></h2></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80d2-90f8-f292e7fb5bb8" class="bulleted-list"><li style="list-style-type:disc">Vehicle readiness ≥ <strong>90%</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80bc-878f-d31880ae9e04" class="bulleted-list"><li style="list-style-type:disc">Pin &lt; 20% → cảnh báo trong <strong>10 giây</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-8066-9418-dc4d2b1e3e10" class="bulleted-list"><li style="list-style-type:disc">Thời gian xử lý sự cố xe &lt; <strong>2 giờ</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="2b9c5e6f-95bd-80b5-9ab1-ff0affa72e74"/></div><div style="display:contents" dir="auto"><h1 id="2b9c5e6f-95bd-8016-9373-eb746710a697" class=""><strong>VI. KẾT LUẬN CHO CEO &amp; CTO</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2b9c5e6f-95bd-8029-810f-c4d9b482e73a" class=""><strong>1. Mức khả thi kỹ thuật: ~95%</strong></h2></div><div style="display:contents" dir="auto"><h2 id="2b9c5e6f-95bd-8054-87c9-df4facf4fe9d" class=""><strong>2. Hạng mục bắt buộc (phê duyệt ngay)</strong></h2></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-8041-a43d-ca3377cfe671" class="bulleted-list"><li style="list-style-type:disc">Chuẩn hóa dữ liệu Wooberly + iSAC (Data Contract + MDM)</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-807d-b992-e16b859949bb" class="bulleted-list"><li style="list-style-type:disc">Xây Integration Layer (API Gateway + Queue + ETL)</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80bf-b670-dd21e13cf7b1" class="bulleted-list"><li style="list-style-type:disc">MDM: driver – vehicle – trip – station – charger – session</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80de-9a69-c88a4e68c7e8" class="bulleted-list"><li style="list-style-type:disc">Ký Data Contract giữa UniTaxi – iSAC – AMIS</li></ul></div><div style="display:contents" dir="auto"><h2 id="2b9c5e6f-95bd-8002-a7f5-e11189348633" class=""><strong>3. Lợi ích dự án</strong></h2></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80f8-a72e-d2cdc2f0f924" class="bulleted-list"><li style="list-style-type:disc">Giảm ~60% lỗi vận hành</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-8007-8f9b-d69a33d8eaf0" class="bulleted-list"><li style="list-style-type:disc">Rút ngắn 40–50% thời gian xử lý thủ công</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-80d6-a2bc-cb852f5c0e5d" class="bulleted-list"><li style="list-style-type:disc">Đối soát doanh thu nhanh &amp; chính xác</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-805e-a42a-ec3bee7aeacf" class="bulleted-list"><li style="list-style-type:disc">Giảm 20–30% chi phí vận hành đội xe</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-8035-984a-fef6719efec6" class="bulleted-list"><li style="list-style-type:disc">Mở rộng lên 2.000–10.000 xe mà không thay core</li></ul></div><div style="display:contents" dir="auto"><ul id="2b9c5e6f-95bd-800b-a615-fcb0a80a32c8" class="bulleted-list"><li style="list-style-type:disc">Chuẩn hóa pháp lý hoàn toàn theo VN</li></ul></div><div style="display:contents" dir="auto"><hr id="2b9c5e6f-95bd-804b-89e8-e91a292ba13e"/></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
