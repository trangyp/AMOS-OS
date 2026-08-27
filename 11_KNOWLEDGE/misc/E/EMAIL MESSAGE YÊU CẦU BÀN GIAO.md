---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>EMAIL / MESSAGE YÊU CẦU BÀN GIAO</title><style>
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
	
</style></head><body><article id="33ac5e6f-95bd-806f-b000-c7bad108c6e4" class="page sans"><header><h1 class="page-title" dir="auto">EMAIL / MESSAGE YÊU CẦU BÀN GIAO</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><hr id="33ac5e6f-95bd-80b7-9ff1-fc8938542705"/></div><div style="display:contents" dir="auto"><h2 id="33ac5e6f-95bd-802d-a60d-d5501b4f124f" class="">1. QUYỀN TRUY CẬP &amp; TÀI KHOẢN</h2></div><div style="display:contents" dir="auto"><p id="33ac5e6f-95bd-80cd-9ae3-c1c32b104c18" class="">Vui lòng cung cấp đầy đủ:</p></div><div style="display:contents" dir="auto"><p id="33ac5e6f-95bd-8044-afb9-e77628c6751c" class=""><strong>Danh sách + quyền truy cập thực tế:</strong></p></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-806e-b916-f2b2d6081b66" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Server (IP, user, quyền root/sudo)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80de-8d39-cfaeffa5bed2" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Cloud (AWS/GCP/Azure – account + IAM)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-804a-8f26-edc670edf714" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Database (host, user admin, quyền truy cập)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8022-9a72-d9940da48105" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Firewall / network (login + quyền cấu hình)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8027-b30b-cf32a10f3722" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Domain + DNS + SSL (nơi quản lý + login)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8078-9821-ed2211f8c5e1" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Git repo (link + quyền owner)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-804d-8132-cdabc8777bfe" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">CI/CD (Jenkins/Gitlab CI…)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80c5-8157-e5977204d1ce" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">App Store + Google Play (account + quyền)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80b6-9295-c2f95d7b6ad3" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Vendor accounts (DC, payment, SMS, email…)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><p id="33ac5e6f-95bd-80b3-9750-ff0004704bd9" class=""><strong>Yêu cầu thêm:</strong></p></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80c8-a9f3-dabd9d3bd231" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Danh sách ai đang giữ quyền admin</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-806d-b02e-e51671b6774d" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">MFA / OTP đang thuộc về ai</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80e1-a7f3-d75f946eaeb9" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Tài khoản dùng chung (nếu có)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><hr id="33ac5e6f-95bd-8082-914d-d01f54559ca2"/></div><div style="display:contents" dir="auto"><h2 id="33ac5e6f-95bd-806a-8a63-c1c6eab2a771" class="">2. HẠ TẦNG &amp; HỢP ĐỒNG</h2></div><div style="display:contents" dir="auto"><p id="33ac5e6f-95bd-8013-880c-cb159d654eda" class=""><strong>Danh sách hạ tầng:</strong></p></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-805e-bcd7-c6f89a00c66e" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Server vật lý (DC nào, rack nào)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8014-a23b-f3785b63349c" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Cloud (service nào đang dùng)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-809a-b56d-cd7e1875f657" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Network (leased line, VPN, firewall)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><p id="33ac5e6f-95bd-8037-823a-c78181aa295d" class=""><strong>Với mỗi nhà cung cấp:</strong></p></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-807a-80ae-ffcacbd9f769" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Tên vendor</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8093-a48b-fb07580c9d52" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Hợp đồng + ngày hết hạn</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8030-a47c-fc5e5e65bbbf" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Công nợ hiện tại</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8041-a12a-c48956143194" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">SLA cam kết</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80f4-975b-ce1faad69ddd" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Điều kiện tạm ngưng/cắt dịch vụ</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><hr id="33ac5e6f-95bd-802b-a7f2-f63bd5a8ca8c"/></div><div style="display:contents" dir="auto"><h2 id="33ac5e6f-95bd-80a6-9479-fdaf986d6167" class="">3. DANH SÁCH HỆ THỐNG (SYSTEM INVENTORY)</h2></div><div style="display:contents" dir="auto"><p id="33ac5e6f-95bd-80b6-97f1-f681d9039543" class="">Vui lòng cung cấp bảng gồm:</p></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8051-b8b6-dbc38a963670" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Tên hệ thống (app khách, app tài xế, backend…)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8088-b10f-fd64f567e5e9" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Mô tả chức năng chính</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80fc-b21e-e5354408b68f" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Môi trường chạy (server/cloud nào)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8002-b7f2-eca711e51e1e" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Database sử dụng</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80a5-9ef7-d927c85110f1" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Người phụ trách chính</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8089-81fd-dc99b315bccd" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Mức độ quan trọng (critical / high / normal)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><hr id="33ac5e6f-95bd-80f3-b23b-f17aa3e4a8df"/></div><div style="display:contents" dir="auto"><h2 id="33ac5e6f-95bd-805f-8c2c-f67d51dba5c6" class="">4. KIẾN TRÚC &amp; LUỒNG HỆ THỐNG</h2></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80ef-82b3-daf4d260fc54" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Sơ đồ tổng thể (system architecture)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80e6-b4a9-dc2decf8ac9f" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Sơ đồ network (IP, kết nối giữa các hệ)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8036-91ee-c61ab1a23e0c" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Luồng chính:</span><div class="indented"><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-807c-a833-e5e7d36e8399" class="bulleted-list"><li style="list-style-type:disc">booking → dispatch → tài xế → thanh toán</li></ul></div></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80a6-9c11-f877eab8160e" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Danh sách tất cả tích hợp bên thứ ba</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><p id="33ac5e6f-95bd-809f-a875-c62d2e33d14b" class=""><strong>Yêu cầu:</strong></p></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80df-9962-cde8886dbd64" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Chỉ rõ hệ thống nào phụ thuộc hệ thống nào</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><hr id="33ac5e6f-95bd-8036-ab4d-c92e377fcebd"/></div><div style="display:contents" dir="auto"><h2 id="33ac5e6f-95bd-80f7-be7b-c0f379fe0413" class="">5. BACKUP &amp; KHÔI PHỤC</h2></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-805c-b6d9-c1b8437cca7e" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Danh sách hệ thống đang được backup</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80e9-8a9f-ea52cc1a438f" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Loại backup (full/incremental)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80a9-a3bc-ce3826dd69cb" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Tần suất (daily/weekly…)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80b2-ae86-fa01eb9e48dd" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Nơi lưu (server/cloud/offsite)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><p id="33ac5e6f-95bd-80ec-a465-d7bd3abde52c" class=""><strong>Bắt buộc cung cấp:</strong></p></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8039-bd64-d656ef441d61" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Quy trình restore từng hệ thống</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8053-b027-e43758c0fd7c" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Lần test restore gần nhất (ngày + kết quả)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><hr id="33ac5e6f-95bd-8092-9ebf-e1e3f6960d07"/></div><div style="display:contents" dir="auto"><h2 id="33ac5e6f-95bd-80e1-aefc-c3c3cdf1084e" class="">6. CODE &amp; TRIỂN KHAI</h2></div><div style="display:contents" dir="auto"><p id="33ac5e6f-95bd-802d-a6db-d177c761307f" class=""><strong>Source code:</strong></p></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80b2-85a4-ec2f8408666a" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Danh sách repo đầy đủ</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-807b-81b4-f936ff3f72f1" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Repo nào là production</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><p id="33ac5e6f-95bd-80af-9875-febcceff9e34" class=""><strong>Deploy:</strong></p></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80b3-a9c5-fb1e313fb0aa" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Quy trình deploy backend (step-by-step)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-801e-9400-eba754bd0b9d" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Quy trình deploy mobile (Android/iOS)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80a0-87cf-e83a579734b8" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">CI/CD pipeline (nếu có)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><p id="33ac5e6f-95bd-80cd-8a97-fa3258588ee7" class=""><strong>Mobile:</strong></p></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80f3-aadf-dda7192498e7" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Keystore Android</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8092-b9a8-d823dc5ee1b8" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Certificate iOS</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8091-af8d-f6849b9535c2" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Quyền ký app</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><hr id="33ac5e6f-95bd-809b-aeb5-d0ebd5748446"/></div><div style="display:contents" dir="auto"><h2 id="33ac5e6f-95bd-80e7-860b-c20c66d7a5e2" class="">7. DATABASE &amp; DỮ LIỆU</h2></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80ec-9167-e502a14cf9b9" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Danh sách database (tên, loại, dung lượng)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80b4-9556-ebc611c13a68" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Database nào là production</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80da-9d83-e3b54f146dba" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Có replication không</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><p id="33ac5e6f-95bd-80ac-98dc-fc881e5c9fc9" class=""><strong>Dữ liệu chính:</strong></p></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8055-87aa-df447f502015" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Khách hàng</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80c5-b3ce-ca210058276d" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Tài xế</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80b2-a5d5-e139fe493243" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Giao dịch</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-803a-a1ef-f96ac80a31ae" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Thanh toán</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><p id="33ac5e6f-95bd-8062-883f-c5feb0eba1d2" class=""><strong>Yêu cầu:</strong></p></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8021-8680-f70487dd585a" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Cách đối soát dữ liệu (nếu có)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><hr id="33ac5e6f-95bd-8062-a0ef-c2d71bcde79c"/></div><div style="display:contents" dir="auto"><h2 id="33ac5e6f-95bd-8096-af9f-fd06ad53ffa9" class="">8. VẬN HÀNH (OPS)</h2></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-803d-bcd9-fbca952933f5" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Hệ thống monitoring đang dùng (tool gì)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8053-83ad-fc2cb1370c30" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Dashboard (link)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-802a-8dbb-c78ecb53777f" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Alert (gửi cho ai, qua đâu)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><p id="33ac5e6f-95bd-8091-896e-f601156b4b3c" class=""><strong>Sự cố:</strong></p></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8018-9369-e165561b6a08" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Quy trình xử lý incident</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8019-bb11-f762a1d54789" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Danh sách sự cố lớn 6–12 tháng:</span><div class="indented"><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8013-b8ab-dec7aa2d13ed" class="bulleted-list"><li style="list-style-type:disc">nguyên nhân</li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80c5-9627-dfa2cfca1aa5" class="bulleted-list"><li style="list-style-type:disc">cách xử lý</li></ul></div></div></li></ul></div><div style="display:contents" dir="auto"><p id="33ac5e6f-95bd-802d-b9cb-dddbedbe1041" class=""><strong>Runbook:</strong></p></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80bb-9135-d9149750e749" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Restart system</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-802a-b593-e7587bb9d54e" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Xử lý lỗi phổ biến</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><hr id="33ac5e6f-95bd-806a-a691-d0fe4b71f741"/></div><div style="display:contents" dir="auto"><h2 id="33ac5e6f-95bd-80e4-a209-f62aa15674eb" class="">9. TÍCH HỢP BÊN THỨ BA</h2></div><div style="display:contents" dir="auto"><p id="33ac5e6f-95bd-80d6-8598-f89a5cab588b" class="">Cho mỗi tích hợp:</p></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80fe-8e90-f949a9e4200f" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Tên đối tác (payment, SMS, map…)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8051-8035-e077698adb6f" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Mục đích sử dụng</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8020-929f-e4bb90a5c72b" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">API endpoint / tài liệu</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-802f-a4ac-e384b7ece131" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">API key / credential</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80a5-a3a2-f974b0110d8d" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">SLA</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8028-9bd4-fbd0ddd31538" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Người phụ trách</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><hr id="33ac5e6f-95bd-8089-b6ee-ef6d2efb0be4"/></div><div style="display:contents" dir="auto"><h2 id="33ac5e6f-95bd-800b-8f9e-ff0436b02a0a" class="">10. BẢO MẬT</h2></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80bc-b352-d920492976a5" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Firewall rule hiện tại</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80f8-b82c-c44608904d3f" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Danh sách port mở</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80d8-a6f9-ea0ee6dbae48" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">VPN (cách truy cập)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80d2-baff-cbc00b90ce7f" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Patch hệ điều hành</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><p id="33ac5e6f-95bd-808b-abfd-ccf301be0f18" class=""><strong>Secret:</strong></p></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-805f-ae91-e99d1cea6c2c" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Nơi lưu password / API key</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8002-b7c5-c540f761707d" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Danh sách key quan trọng</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80f5-8ba1-f4fd676b0dc6" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">SSL certificate (file + private key)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><hr id="33ac5e6f-95bd-8001-98ad-c12003544fa6"/></div><div style="display:contents" dir="auto"><h2 id="33ac5e6f-95bd-8028-9443-f75cb852aced" class="">11. NHÂN SỰ &amp; PHỤ THUỘC</h2></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80a9-9c7d-ddfff8f1dddb" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Sơ đồ team tech</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80be-bd0d-cb8d0795210d" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Ai phụ trách từng hệ thống</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-801f-8b10-c14097a27f73" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Hệ thống nào chỉ 1 người biết</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><p id="33ac5e6f-95bd-8052-ac46-c2a109564eb5" class=""><strong>Tài liệu:</strong></p></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8094-966e-cc8384b5a802" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">SOP</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80de-9e25-f6769f78f4c9" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Wiki</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8000-8d30-dd4fb13cf433" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Hướng dẫn vận hành</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><hr id="33ac5e6f-95bd-800d-9451-cdba67d0219c"/></div><div style="display:contents" dir="auto"><h2 id="33ac5e6f-95bd-80e9-a575-f6e96fe24ad1" class="">12. CHI PHÍ &amp; THANH TOÁN</h2></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8052-897c-c5a1260872ad" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Chi phí DC / cloud</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8073-b971-cbcc0cc70d70" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Chi phí license</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80fa-9925-e3441c4044ab" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Chi phí vendor</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><p id="33ac5e6f-95bd-80cc-8777-d3fd30e0de59" class=""><strong>Yêu cầu:</strong></p></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80c9-9546-e4fddcf30e7f" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Chi phí theo tháng</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8051-922d-ef5dad5668b0" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Các khoản sắp đến hạn</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><hr id="33ac5e6f-95bd-8070-83b4-cd49d74ac43c"/></div><div style="display:contents" dir="auto"><h1 id="33ac5e6f-95bd-80d5-9c56-e07ba8f0c50d" class="">YÊU CẦU CÁCH BÀN GIAO</h1></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-802e-99f7-d6b895310605" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Gửi tài liệu dạng file (Excel/Doc)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-8000-8cbe-f6b87bc1437e" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Cấp quyền truy cập thực tế</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-808d-af73-fcf8ecc248be" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Tổ chức session walkthrough (3–5 ngày)</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><ul id="33ac5e6f-95bd-80be-a29d-f19f888a6870" class="to-do-list"><li><div class="checkbox checkbox-off"></div> <span class="to-do-children-unchecked">Ghi lại video nếu có thể</span><div class="indented"></div></li></ul></div><div style="display:contents" dir="auto"><hr id="33ac5e6f-95bd-80a5-ab55-c1042d22fff9"/></div><div style="display:contents" dir="auto"><h1 id="33ac5e6f-95bd-801f-a8da-f27120c46b64" class="">10 ĐIỂM PHẢI XÁC NHẬN TRONG BUỔI BÀN GIAO</h1></div><div style="display:contents" dir="auto"><ol type="1" id="33ac5e6f-95bd-8099-b31f-f9f16ab8171c" class="numbered-list" start="1"><li>Ai giữ toàn bộ quyền admin?</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="33ac5e6f-95bd-80a4-a6b8-e599431331a6" class="numbered-list" start="2"><li>Hệ thống nào quan trọng nhất?</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="33ac5e6f-95bd-8043-8562-dac3feabb600" class="numbered-list" start="3"><li>Backup có restore được không?</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="33ac5e6f-95bd-80dc-96f2-fbbb4928f053" class="numbered-list" start="4"><li>Nếu DC down → xử lý thế nào?</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="33ac5e6f-95bd-8005-8942-fb4694edbdd8" class="numbered-list" start="5"><li>Thanh toán phụ thuộc hệ nào?</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="33ac5e6f-95bd-80c0-9d95-c259f5f25ae5" class="numbered-list" start="6"><li>Có vendor nào giữ code/data không?</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="33ac5e6f-95bd-8098-b466-f7d6fd4ae659" class="numbered-list" start="7"><li>Có hệ thống nào không có owner?</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="33ac5e6f-95bd-8056-954d-fd5a68eec39e" class="numbered-list" start="8"><li>Có rủi ro bị cắt dịch vụ không?</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="33ac5e6f-95bd-80ce-a7af-c6d1816fcc92" class="numbered-list" start="9"><li>Có lỗi lớn nào chưa fix?</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="33ac5e6f-95bd-80df-a07d-f217bcbe081b" class="numbered-list numbered-list-digits-2" start="10"><li>Có phụ thuộc cá nhân không?</li></ol></div><div style="display:contents" dir="auto"><hr id="33ac5e6f-95bd-806e-95d8-e648640db2a4"/></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
