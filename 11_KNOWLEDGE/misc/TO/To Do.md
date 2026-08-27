---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>To Do</title><style>
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
	
</style></head><body><article id="2e2c5e6f-95bd-801c-ac7c-e404add70372" class="page sans"><header><h1 class="page-title" dir="auto">To Do</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-8026-9dbd-e4a27fcee149" class=""><strong>GOOGLE DRIVE — GRANTS FOLDER STRUCTURE</strong></h1></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80b1-8f9a-ceb7868eb361" class=""><strong>Rule: </strong>If a file is not in the correct folder, 
it is considered <strong>not done</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8023-9f76-ded68f6e3a04"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8049-9d13-c344c352bfc4" class=""><strong>SECTION 1 — CREATE THE MAIN FOLDER (ONCE)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8031-9183-cc94ac1f5232" class=""><strong>Task 1.1 — Create root folder</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8020-a4c9-e3f3eb9c0333" class="numbered-list" start="1"><li>Open <strong>Google Drive</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80c3-a53c-ffe8821f9ae9" class="numbered-list" start="2"><li>Click <strong>New</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8084-92f2-eb3edfd1575b" class="numbered-list" start="3"><li>Click <strong>Folder</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8049-88ed-e5f6eb909779" class="numbered-list" start="4"><li>Name the folder EXACTLY:</li></ol></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2e2c5e6f-95bd-8030-86b0-fbda34627ae7" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">GRANTS_MASTER</code></pre></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-802b-824a-c55a2bacae5b" c
lass="numbered-list" start="1"><li>Press <strong>Create</strong></li></ol></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8073-8088-f85236579f84" class="">✅ Done when folder exists at top level.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8074-93e0-ee4205cbf2dc"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8046-85d9-f14052a3de58" class=""><strong>SECTION 2 — CREATE MAIN SUBFOLDERS (DO NOT RENAME)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8010-92c9-f26f81435df6" class="">Inside GRANTS_MASTER, create these folders <strong>exactly as written</strong>.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80df-9946-c9c33625a4bf" class=""><strong>Task 2.1 — Core folders</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8092-beb7-c064f899d602" class="">Create ONE folder at a time:</p></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-8093-9f5f-f468d1c8a07a" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">01_TRACKERS
02_GRANT_SOURCES
03_ACTIVE_GRANTS
04_DRAFT_APPLICATIONS
05_SUBMITTED
06_IP_AND_LEGAL
07_TEMPLATES
08_REFERENCE
09_ARCHIVE</code></pre></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8017-954e-c4b03f2910c5" class=""><strong>Rules:</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c3-8b72-cec086a87c33" class="bulleted-list"><li style="list-style-type:disc">Numbers matter</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a2-8fab-facd67a4a161" class="bulleted-list"><li style="list-style-type:disc">Spelling matters</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ad-8b0b-d994c3a9e642" class="bulleted-list"><li style="list-style-type:disc">Do not add extra folders</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8088-9313-fb04615ce57b" class="">✅ Done when all 9 folders exist.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-802a-a78f-d6aa5e65631a"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-809f-bec3-ec0b497b99cb" class=""><strong>SECTION 3 — TRACKERS FOLDER (01_TRACKERS)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80a4-b827-e9b8af75c465" class=""><strong>Task 3.1 — Create tracker files</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80c7-bc38-f9a1b0f365d2" class="">Inside 01_TRACKERS, 
create:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80a1-875e-d2a2d77b65df" class="numbered-list" start="1"><li>Google Sheet named:</li></ol></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-80d4-8fa5-e77f074ed271" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">GRANT_TRACKER_MASTER</code></pre></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-805a-b27f-f395520d8219" class="numbered-list" start="1"><li>Google Doc named:</li></ol></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-807b-b196-ff97372d1481" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">WEEKLY_STATUS_REPORT</code></pre></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8088-b773-ef3425083396"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-800c-91b9-decdc4dd0dac" class=""><strong>Task 3.2 — GRANT_TRACKER_MASTER sheet tabs</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80bc-808c-ea56c4b51645" class="">Create these tabs (bottom of sheet):</p></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-804a-a21f-f8083d74e648" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">FEDERAL
STATE
LOCAL
AEA
UNIVERSITY
OTHER</code></pre></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8093-a973-d35998ecbcd5" class="">Do NOT change names.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8032-a440-f9daf6f007aa"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-807a-97fb-dedcb307daaf" class=""><strong>SECTION 4 — GRANT SOURCES (02_GRANT_SOURCES)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8072-9ae6-eae073a6e27b" class="">Purpose: store <strong>links and screenshots only</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80ce-92e9-d9a21e519c58" class="">Inside 02_GRANT_SOURCES, create folders:</p></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-808d-b9af-e13c96bc751d" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">FEDERAL_PORTALS
STATE_PORTALS
LOCAL_PORTALS
AEA</code></pre></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8018-9ae6-d8570a389682" class=""><strong>What goes here:</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d5-b5b8-d34b619c8ff5" class="bulleted-list"><li style="list-style-type:disc">Portal links (Google Docs)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a0-868c-f373dee61a2e" class="bulleted-list"><li style="list-style-type:disc">Screenshots of grant listings</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-800b-b454-cc815fb03aa8" class="bulleted-list"><li style="list-style-type:disc">PDF copies of “list pages”</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-804d-8f66-e5b4201c3d45" class="">❌ No applications</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-806c-bf87-f33d264d643c" class="">❌ No drafts</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80f6-a251-f90168c427f6"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80ea-b630-e64bfc77c525" class=""><strong>SECTION 5 — ACTIVE GRANTS (03_ACTIVE_GRANTS)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-805b-ad0f-dc3e34cebed7" class="">This is the <strong>most important working folder</strong>.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80de-b1f7-fa712861c46d" class=""><strong>Task 5.1 — Create one folder per grant</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80e0-a000-e9416bd0a777" class="">Folder naming rule:</p></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-805c-958a-e3df1073f616" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">YYYYMMDD_GRANTNAME_FUNDER</code></pre></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80e6-9ad0-e2cf7bbda85f" class="">Example:</p></div><div s
tyle="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-80bf-b358-fa62bf79c1af" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">20260615_AI_INNOVATION_GRANT_DISR</code></pre></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8068-99ff-f3c6c708c11f"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80ad-8268-cfb736e362ad" class=""><strong>Task 5.2 — Inside EACH grant folder, create subfolders</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8004-b406-e617e54d915c" class="">Inside each grant folder, create:</p></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-8032-a222-e3edce33caeb" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">01_GUIDELINES
02_ELIGIBILITY
03_IP_AND_RISK
04_REQUIREMENTS
05_BUDGET
06_DRAFTS</code></pre></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8055-906e-d48198158236" class="">Do NOT skip any.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80ff-aa03-ceac27a8b3f0"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80f0-92f9-cf416446d53f" class=""><strong>What goes in each:</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8030-883b-c0395099a5e2" class=""><strong>01_GUIDELINES</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ef-813f-d655fe88f0d4" class="bulleted-list"><li style="list-style-type:disc">Official guidelines PDFs</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8005-b767-c25d8758f611" class="bulleted-list"><li style="list-style-type:disc">Rules documents</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8015-9ebf-e2af17f57547" class=""><strong>02_ELIGIBILITY</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8017-8e69-e8325a1a4061" class="bulleted-list"><li style="list-style-type:disc">Copied eligibility text</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-801e-91b0-c61090a748a5" class="bulleted-list"><li style="list-style-type:disc">Screenshots of “Who can apply”</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8011-acfd-d3f59dd3c9d4" class=""><strong>03_IP_AND_RISK</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c1-aea0-f6776ea04acd" class="bulleted-list"><li style="list-style-type:disc">Copied IP clauses</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a0-bca5-eaca8556c381" class="bulleted-list"><li style="list-style-type:disc">Highlighted risk text</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8056-a2ee-dbb0dd0edb12" c
lass=""><strong>04_REQUIREMENTS</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b2-8cac-cd8cde9b740d" class="bulleted-list"><li style="list-style-type:disc">Word limits</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8038-a0ba-c5bba954066e" class="bulleted-list"><li style="list-style-type:disc">Document lists</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80cb-a305-dde0e75d82f5" class="bulleted-list"><li style="list-style-type:disc">Deadlines (doc)</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8085-9c93-d7351a2323b1" class=""><strong>05_BUDGET</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ab-a1ff-d607e51cbfce" class="bulleted-list"><li style="list-style-type:disc">Budget templates</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8071-936f-db9ea242f8ef" class="bulleted-list"><li style="list-style-type:disc">Cost tables</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-801d-8282-fcd20fd93daa" class=""><strong>06_DRAFTS</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80af-8288-cf1af53e7694" class="bulleted-list"><li style="list-style-type:disc">Working drafts ONLY</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e8-91bf-f0372a9acec5" class="bulleted-list"><li style="list-style-type:disc">Clearly marked DRAFT</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80a1-a3fe-d14e6a8dc5d1"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80e4-84b4-c5b75a116100" class=""><strong>SECTION 6 — DRAFT APPLICATIONS (04_DRAFT_APPLICATIONS)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80e0-8a3a-fff4f512bd67" class="">Purpose: cross-grant drafting workspace.</p></div><div style="display:contents" dir="auto"><p i
d="2e2c5e6f-95bd-8021-a233-ff8f2433df29" class="">Inside create folders:</p></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-80c8-aa80-cc9c7d06d79d" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">IN_PROGRESS
READY_FOR_REVIEW
BLOCKED</code></pre></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8079-8ddc-cd2f142ce34b" class=""><strong>Rules:</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8086-822d-e6956ab92505" class="bulleted-list"><li style="list-style-type:disc">A file can only be in ONE folder</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8054-a6b2-c3315718adb6" class="bulleted-list"><li style="list-style-type:disc">If blocked → move to BLOCKED</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80dc-a2ef-deffafd1040d"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8038-8f72-fb66080c78d6" class=""><strong>SECTION 7 — SUBMITTED GRANTS (05_SUBMITTED)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8019-81af-cd835c5cc456" class=""><strong>Task 7.1 — One folder per submitted grant</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8045-a857-e4ff59ed259c" class="">Folder naming rule (same as active):</p></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-80c8-bbb6-c95bd5c3cd52" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">YYYYMMDD_GRANTNAME_FUNDER_SUBMITTED</code></pre></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8050-9fdf-d57344fa73b3" class="">Inside include:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8028-a9af-dc7e2c0ee261" class="bulleted-list"><li style="list-style-type:disc">Final submitted application</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8086-b4dd-dd0b3387cdc3" class="bulleted-list"><li style="list-style-type:disc">Submission confirmation</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ec-9b86-ece0f4a2d3db" class="bulleted-list"><li style="list-style-type:disc">Any correspondence</li></ul></div><div s
tyle="display:contents" dir="auto"><p id="2e2c5e6f-95bd-807b-a572-e381f11946c7" class="">❌ No drafts</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8089-9353-d10350b7dd5e" class="">❌ No working files</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8041-941f-e5ac8b65233c"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80b3-9c06-f6ac44ad8508" class=""><strong>SECTION 8 — IP &amp; LEGAL (06_IP_AND_LEGAL)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-803a-ad1a-cf4895b7c67b" class="">Inside create:</p></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-8060-a282-ca6640a13336" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">IP_EXTRACTS
RISK_FLAGS
AGREEMENTS</code></pre></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-805b-84be-c71e8d05cc89" class=""><strong>What goes here:</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8065-b6bc-ca36d8a99288" class="bulleted-list"><li style="list-style-type:disc">Copy-pasted IP clauses</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80cf-876f-d1161bc81e8d" class="bulleted-list"><li style="list-style-type:disc">Highlighted red-flag text</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-801b-93e8-f0021f6aea51" class="bulleted-list"><li style="list-style-type:disc">Signed agreements ONLY</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8091-bf69-c053d7976282"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80cb-97c1-e3e0039f5410" class=""><strong>SECTION 9 — TEMPLATES (07_TEMPLATES)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8061-b851-c28fc7e8a28d" class="">Inside create:</p></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-80e7-8142-c563f562fb27" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">APPLICATION_TEMPLATES
BUDGET_TEMPLATES
REPORTING_TEMPLATES</code></pre></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80e5-9e18-d93fddac1ceb" class=""><strong>Rules:</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8053-a55f-e967e27fb160" class="bulleted-list"><li style="list-style-type:disc">Templates are NEVER edited</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8003-a31a-c898c200f853" class="bulleted-list"><li style="list-style-type:disc">Always make a copy before use</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8078-ad23-e1152df4ed0f"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8089-8a4e-fafe4a724c4f" class=""><strong>SECTION 10 — REFERENCE (08_REFERENCE)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80c1-96c3-dfd87ee56aab" class="">Purpose: read-only knowledge.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80a1-8446-c18e982ffe16" class="">Inside put:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-803a-ac01-e204740532cb" class="bulleted-list"><li style="list-style-type:disc">Past successful applications</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80cd-8841-f60618bfb8f9" class="bulleted-list"><li style="list-style-type:disc">Policy docs</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a4-b93c-ea9d255e9db8" class="bulleted-list"><li style="list-style-type:disc">Government strategy PDFs</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8048-b8b1-fe133961aaa6"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8048-82f5-d5d72019ddd2" class=""><strong>SECTION 11 — ARCHIVE (09_ARCHIVE)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8083-944e-c97828493cd3" class="">Purpose: finished or abandoned work.</p></div><div s
tyle="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8057-b0c7-d6010bc81b1e" class="">Move here:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b3-8bb2-ef20d44be95e" class="bulleted-list"><li style="list-style-type:disc">Rejected grants</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8017-87a8-f692eb2f1126" class="bulleted-list"><li style="list-style-type:disc">Old drafts</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8024-83c1-e09aa2924187" class="bulleted-list"><li style="list-style-type:disc">Superseded documents</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80eb-94fe-d75cb15638ab" class="">Never delete files. 
Only archive.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-802c-82a3-df2d8883905b"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80b1-b799-eefd21f01a71" class=""><strong>SECTION 12 — FILE NAMING RULES (NON-NEGOTIABLE)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8041-b431-dbde19449a60" class="">Every file name must include:</p></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-8042-82bf-cc7955ac6000" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">DATE_GRANTNAME_DESCRIPTION_VERSION</code></pre></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-804e-a88b-eaa074ed3f87" class="">Example:</p></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-80f7-b798-d0a8a0b4f0fe" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">20260610_AI_INNOVATION_ELIGIBILITY_V1</code></pre></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80f8-89af-f910eedbae0a" class="">❌ No “final_final”</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-801d-8199-dc577a805b9d" class="">❌ No “new version”</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8076-a3c1-e1ee9bb901ca"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80dc-b7e3-f5f4f59ded78" class=""><strong>SECTION 13 — DAILY JUNIOR CHECK</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8029-9ae1-d399d123eb42" class="">End of day, 
junior must confirm:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-807e-939a-f82657e72365" class="bulleted-list"><li style="list-style-type:disc">All new files saved in correct folder</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8047-8879-ce2e1c659988" class="bulleted-list"><li style="list-style-type:disc">No loose files in root</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e0-a82c-c387d67db6fa" class="bulleted-list"><li style="list-style-type:disc">Tracker updated</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-805b-8587-d3f68cfebac4" class="bulleted-list"><li style="list-style-type:disc">Manager notified of changes</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80a0-ac62-fd471b118f4b"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8058-aab4-f33c27f63b3c" class=""><strong>DEFINITION OF DONE (FOR FILE ORGANISATION)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8070-9094-df9c089b4725" class="">Organisation is DONE when:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d6-9d26-c043c3463ae9" class="bulleted-list"><li style="list-style-type:disc">Every grant has its own folder</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8002-8ba8-e27ecfde0917" class="bulleted-list"><li style="list-style-type:disc">Every file is in the correct subfolder</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8070-96e7-d95f231c758a" class="bulleted-list"><li style="list-style-type:disc">Naming rules followed</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ab-a5e5-ccee7e9716d0" class="bulleted-list"><li style="list-style-type:disc">Nothing is sitting “temporarily” anywhere</li></ul></div><div style="display:contents" dir="auto"><hr i
d="2e2c5e6f-95bd-80d3-90fd-e8e14a2fdf5b"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-80d7-9351-fce6d9118795" class=""><strong>WHERE DOES THIS FILE GO?</strong></h1></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8015-8beb-df07020cd39a"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8043-a892-fecf929cec0a" class=""><strong>START HERE</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80d1-a8e5-cf0df5837ab5" class="">You have a file and you need to save it. 
<strong>DO NOT save it anywhere until you answer these questions in order.</strong></p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80ca-a420-f6a06670de9c"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8002-a76c-cae03d359759" class=""><strong>QUESTION 1 — IS THIS FILE RELATED TO GRANTS?</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80e9-8e5d-cc26c52246fc" class="">Ask yourself:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-805f-9468-d59404a292f3" class="">“Is this file about funding, grants, applications, or tenders?”</blockquote></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d4-89a6-d20cb60a078d" class="bulleted-list"><li style="list-style-type:disc">❌ <strong>NO</strong> →<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80e7-8aed-f295d7449728" class="">This file does <strong>not</strong> belong in GRANTS_MASTER.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80f7-aa65-fec0ccc830a1" class="">Stop and ask the manager where it goes.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8083-a5d1-db3b16ef07d8" class="bulleted-list"><li style="list-style-type:disc">✅ <strong>YES</strong> →<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8051-84b7-d894f3c4a365" class="">Continue to Question 2.</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8004-a294-d0e7aff3830e"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8075-83c0-ccd8b1cca806" class=""><strong>QUESTION 2 — IS THIS A TRACKING OR STATUS FILE?</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-800d-997d-e7ee69bc0de3" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-80ab-a9e5-d1f26888e4ec" class="">“Is this a tracker, list, log, 
or status report used across many grants?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8080-9231-d02b8075f526" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80dd-a32a-cd568bec67d7" class="bulleted-list"><li style="list-style-type:disc">Grant tracker spreadsheet</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8022-8518-e087eca2a9c7" class="bulleted-list"><li style="list-style-type:disc">Weekly status report</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-800e-9c74-d0842c81f789" class="bulleted-list"><li style="list-style-type:disc">Overview list</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-807c-bd0b-f8615c6e7f4c" class="bulleted-list"><li style="list-style-type:disc">✅ <strong>YES</strong> →<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8060-974d-c9d39cfccd6b" class="">Save in:</p></div></li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-804a-a061-c91fb79e8adc" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">GRANTS_MASTER / 01_TRACKERS</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b0-8203-e4f4739fa1e6" class="bulleted-list"><li style="list-style-type:disc">STOP.</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8075-81c1-f87184a439d3" class="bulleted-list"><li style="list-style-type:disc">❌ <strong>NO</strong> →<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80db-951c-dfd79d04c3a0" class="">Continue to Question 3.</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8001-ab47-c9950f38a393"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8070-88ce-e445a04e176d" class=""><strong>QUESTION 3 — IS THIS A LINK, SCREENSHOT, 
OR LISTING PAGE?</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-807b-9c35-c7088e1a7d55" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-8065-8226-c135bdcb5ef0" class="">“Is this just showing where grants are listed, 
not a specific grant?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80b3-875e-f02e2f2d1f3d" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8077-8521-e06c821c6a3b" class="bulleted-list"><li style="list-style-type:disc">Screenshots of grant portals</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-802a-8b77-e6b18584a49b" class="bulleted-list"><li style="list-style-type:disc">Links to GrantConnect / state portals</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f2-8dbb-e0c070091c71" class="bulleted-list"><li style="list-style-type:disc">Pages listing many grants</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8032-844e-f1f6f59111e0" class="bulleted-list"><li style="list-style-type:disc">✅ <strong>YES</strong> →<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80aa-b7fb-db22c5da65b5" class="">Save in:</p></div></li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-80a4-bf80-cb8f0564cf7c" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">GRANTS_MASTER / 02_GRANT_SOURCES</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-803c-91d1-d314fe25f7de" class="bulleted-list"><li style="list-style-type:disc">Then choose the correct subfolder:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d9-a53e-e4e2ed7e6931" class="bulleted-list"><li style="list-style-type:circle">FEDERAL_PORTALS</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8063-991d-d0e9f99415bc" class="bulleted-list"><li style="list-style-type:circle">STATE_PORTALS</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8072-bad1-e71c0e381ff2" class="bulleted-list"><li style="list-style-type:circle">LOCAL_PORTALS</li></ul></div><div style="display:contents" dir="auto"><ul i
d="2e2c5e6f-95bd-80b9-b925-fb7bb0990699" class="bulleted-list"><li style="list-style-type:circle">AEA</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80e7-8be5-cf6c2459f44c" class="">STOP.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8080-b11a-e23ee31d369a" class="bulleted-list"><li style="list-style-type:disc">❌ <strong>NO</strong> →<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8022-9ca1-dfeb1284e4bd" class="">Continue to Question 4.</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80cf-b709-ce4e7bce57e8"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80ac-98d5-d37ac1ea2bc3" class=""><strong>QUESTION 4 — IS THIS FILE ABOUT ONE SPECIFIC GRANT?</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-809c-a674-ea226a7d2411" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-80bb-8462-f55d47d9b14b" class="">“Is this file for ONE named grant (not multiple)?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8016-a455-f0ff4786718e" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-809b-a385-da2f1b61695d" class="bulleted-list"><li style="list-style-type:disc">Guidelines for one grant</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-809b-8963-fd4be1f57865" class="bulleted-list"><li style="list-style-type:disc">Eligibility text for one grant</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-806c-a06b-cb6883fbdff0" class="bulleted-list"><li style="list-style-type:disc">Draft application for one grant</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8064-859a-c46c1342fe14" class="bulleted-list"><li style="list-style-type:disc">❌ <strong>NO</strong> →<div style="display:contents" dir="auto"><p i
d="2e2c5e6f-95bd-801b-8f5a-decea632f307" class="">Stop and ask the manager.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80cd-aa68-c004691c55bf" class="bulleted-list"><li style="list-style-type:disc">✅ <strong>YES</strong> →<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80de-a8df-e562310c4e78" class="">Continue to Question 5.</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-802c-940f-f99ade69e61f"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80cf-affa-e48a5e6d6219" class=""><strong>QUESTION 5 — HAS THIS GRANT BEEN SUBMITTED YET?</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-807e-9290-dd311494ba77" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-801e-bc68-e396d9227a32" class="">“Has the application already been officially submitted?”</blockquote></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8086-8d87-e2d77a832fb2" class="bulleted-list"><li style="list-style-type:disc">❌ <strong>NO (not submitted yet)</strong> →<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8060-92bd-ece37a94d58b" class="">Go to:</p></div></li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-80f1-a03c-e58ecd825d01" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">GRANTS_MASTER / 03_ACTIVE_GRANTS</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ee-85f1-ec090519cece" class="bulleted-list"><li style="list-style-type:disc">Then open the folder for that grant.<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-809c-bf39-d99f416f70bd" class="">Continue to Question 6.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80be-b854-cb05ef1a192a" class="bulleted-list"><li style="list-style-type:disc">✅ <strong>YES (already s
ubmitted)</strong> →<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80c0-90c9-cd83ccb6695d" class="">Go to:</p></div></li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-80e6-be5a-e161750053da" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">GRANTS_MASTER / 05_SUBMITTED</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8040-bfb2-cb2e6aa0ee1a" class="bulleted-list"><li style="list-style-type:disc">Then open the folder for that grant.<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8092-9f95-f2a7f1912c57" class="">Save file there.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-803e-86e8-e6508f6e4331" class="">STOP.</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80e2-8868-d3db37303ef5"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8075-8ad0-f0b461879537" class=""><strong>QUESTION 6 — WHAT TYPE OF FILE IS IT? 
(ACTIVE GRANT)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80c1-8ea2-dac60734029e" class="">You are now <strong>inside one specific grant folder</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80f4-ad93-d6ef85f0cffd" class="">Choose the FIRST option that matches.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80fc-8480-d9d364e773e2"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80c1-90c2-dcba34117bcf" class=""><strong>OPTION A — OFFICIAL RULES OR GUIDELINES</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80e7-83ef-ff035ee8f0fa" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-8058-9ece-dfdddf5adcae" class="">“Is this an official document explaining the rules of the grant?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-809f-aea5-f0503fdbc77f" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a9-8e19-d36735ad1c27" class="bulleted-list"><li style="list-style-type:disc">Guidelines PDF</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8058-b6a9-c3c59d4c5fe6" class="bulleted-list"><li style="list-style-type:disc">Rules document</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ba-bee9-fe9275c4425b" class="bulleted-list"><li style="list-style-type:disc">Official program overview</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8017-b990-ed10ad1b460c" class="bulleted-list"><li style="list-style-type:disc">✅ YES → Save in:</li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-8092-b884-edbdb0e4df07" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">01_GUIDELINES</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-803e-b4f2-c532c1a427de" c
lass="bulleted-list"><li style="list-style-type:disc">STOP.</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8007-a8a4-d5d66f4e3efa"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8078-ad9a-e0abcf26be59" class=""><strong>OPTION B — ELIGIBILITY INFORMATION</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-802b-a0cc-e56b74828808" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-80d7-ba30-e5dea4f6af22" class="">“Does this explain who can apply or what is allowed?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8084-a934-da212985f24f" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ba-837a-dae503fe6aad" class="bulleted-list"><li style="list-style-type:disc">“Who can apply” text</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-808e-9a1d-c88866e23b7f" class="bulleted-list"><li style="list-style-type:disc">Eligibility screenshots</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d9-b94e-f7fea1c997a9" class="bulleted-list"><li style="list-style-type:disc">Copied eligibility clauses</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8094-9b1c-eba79cba44df" class="bulleted-list"><li style="list-style-type:disc">✅ YES → Save in:</li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-80f6-9309-c2b5e4457d27" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">02_ELIGIBILITY</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8074-9737-fa9a808c9995" class="bulleted-list"><li style="list-style-type:disc">STOP.</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-805e-837a-c45fc1f0d2fc"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80f4-8250-e94d65c04203" c
lass=""><strong>OPTION C — IP, LEGAL, OR RISK CONTENT</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8045-8969-c7386745e439" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-8069-8020-cedf8f5e486f" class="">“Does this mention IP, ownership, licence, data, 
or risk?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80e8-9845-e807b1fdc4fb" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-805f-9ab8-eff0ffcbdd74" class="bulleted-list"><li style="list-style-type:disc">IP clauses</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8061-b9b1-c12f747b065e" class="bulleted-list"><li style="list-style-type:disc">Ownership rules</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80bd-a7da-ff679f08231b" class="bulleted-list"><li style="list-style-type:disc">Open-source requirements</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-809a-b6ca-ec28afc9f704" class="bulleted-list"><li style="list-style-type:disc">Highlighted risk text</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80df-86a4-e6de5dd52c58" class="bulleted-list"><li style="list-style-type:disc">✅ YES → Save in:</li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-80a9-b71b-e420e857d36f" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">03_IP_AND_RISK</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8070-88dc-ce3782f333fc" class="bulleted-list"><li style="list-style-type:disc">STOP.</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8024-becc-d51b66b2ab11"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80e2-9994-e0ac4ff82b00" class=""><strong>OPTION D — REQUIREMENTS OR DEADLINES</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8043-83bc-ef3b9d8a2103" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-80d5-9c74-cea091fa2438" class="">“Is this about what must be submitted and by when?”</blockquote></div><div style="display:contents" dir="auto"><p i
d="2e2c5e6f-95bd-807f-a7c9-f6a630c3dc1e" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8074-93ef-e25ff3b8019c" class="bulleted-list"><li style="list-style-type:disc">Deadline notes</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8093-a76a-ea975bf51cf7" class="bulleted-list"><li style="list-style-type:disc">Required document lists</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-809e-b603-f76775663ff0" class="bulleted-list"><li style="list-style-type:disc">Word limits</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8085-9074-f4ac023d4a4e" class="bulleted-list"><li style="list-style-type:disc">Submission instructions</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8078-bde8-ec5d4512ad4d" class="bulleted-list"><li style="list-style-type:disc">✅ YES → Save in:</li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-8004-bb64-ea254bf842c6" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">04_REQUIREMENTS</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-801c-9a20-cffa2254c5d5" class="bulleted-list"><li style="list-style-type:disc">STOP.</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80b5-bd98-fd5603344b65"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80ad-b5b0-dc00aaac7d78" class=""><strong>OPTION E — BUDGET OR COSTS</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8070-926a-d0c61412c7e5" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-8054-b859-cf3ffacfaf80" class="">“Does this contain numbers, costs, 
or budget templates?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80b8-abba-e464a5ddbb78" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f4-a55f-ec34e224b3ac" class="bulleted-list"><li style="list-style-type:disc">Budget spreadsheets</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c9-be21-c7724b7bf668" class="bulleted-list"><li style="list-style-type:disc">Cost breakdowns</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8061-a7e0-ef7a21d989e5" class="bulleted-list"><li style="list-style-type:disc">Funding allocation tables</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-804b-8c82-e711106365a7" class="bulleted-list"><li style="list-style-type:disc">✅ YES → Save in:</li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-80ba-86e3-e8a1a2eabf97" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">05_BUDGET</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a8-9c59-f7eec5ea46e2" class="bulleted-list"><li style="list-style-type:disc">STOP.</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80c2-acfb-c7c27b450127"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8045-91b7-d98581ae67bc" class=""><strong>OPTION F — DRAFT APPLICATION CONTENT</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8096-87ce-c5ff80e5c095" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-8076-9e89-c465240919e7" class="">“Is this a draft or working version of the application?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8086-9460-f29a33c294ae" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c2-941f-fd64b14f76e2" class="bulleted-list"><li s
tyle="list-style-type:disc">Draft answers</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-802c-8547-f5b8bd9367c0" class="bulleted-list"><li style="list-style-type:disc">Filled templates (not final)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e7-b4c6-d67be82196c8" class="bulleted-list"><li style="list-style-type:disc">In-progress text</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8092-b530-c5590ccb2e30" class="bulleted-list"><li style="list-style-type:disc">✅ YES → Save in:</li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-80f7-aefa-cc5051c4e9bc" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">06_DRAFTS</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c9-af05-deaa79cee407" class="bulleted-list"><li style="list-style-type:disc">STOP.</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-809a-9c50-ce990563c16a"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8082-8765-d73680f17f85" class=""><strong>QUESTION 7 — IS THIS A TEMPLATE?</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80ba-a279-e493904dbfda" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-8086-96a9-d8bdf5bff7db" class="">“Is this a blank template meant to be reused?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8055-87e7-c2f24c115f09" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a8-bd58-c3261d841676" class="bulleted-list"><li style="list-style-type:disc">Application template</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-801c-8341-c1b48e1bea44" class="bulleted-list"><li style="list-style-type:disc">Budget template</li></ul></div><div style="display:contents" dir="auto"><ul i
d="2e2c5e6f-95bd-808e-8645-fe417dcffa57" class="bulleted-list"><li style="list-style-type:disc">Reporting template</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8054-b173-c70ecd100dd4" class="bulleted-list"><li style="list-style-type:disc">✅ YES → Save in:</li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-80e5-9070-f9c4934cddb9" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">GRANTS_MASTER / 07_TEMPLATES</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80bb-91f9-d70e07273333" class="bulleted-list"><li style="list-style-type:disc">STOP.</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-808d-bd87-d3594b0530ff" class="bulleted-list"><li style="list-style-type:disc">❌ NO → Continue.</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80c5-bbad-e45c2c9dc97d"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-804c-b165-d279539ef340" class=""><strong>QUESTION 8 — IS THIS REFERENCE MATERIAL?</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8085-abf6-e1ddb3a788a5" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-8067-9b62-f4a7b294ea9f" class="">“Is this background reading or past examples?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80e8-b776-cd340f5964c1" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-800a-aa34-c77e778672a0" class="bulleted-list"><li style="list-style-type:disc">Old successful applications</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c4-b0a2-e3d9b191643e" class="bulleted-list"><li style="list-style-type:disc">Policy documents</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-806f-83ad-c3a3b6c5c478" class="bulleted-list"><li s
tyle="list-style-type:disc">Strategy papers</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80af-bbdd-ee993cedfca6" class="bulleted-list"><li style="list-style-type:disc">✅ YES → Save in:</li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-80d7-b660-e9dfd5d97f3a" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">GRANTS_MASTER / 08_REFERENCE</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8060-bf25-e5b3359113b2" class="bulleted-list"><li style="list-style-type:disc">STOP.</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-801a-9e35-ecdffc526dea"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-809c-84bb-e4017ff482eb" class=""><strong>QUESTION 9 — IS THIS FINISHED OR NO LONGER ACTIVE?</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-808d-a6ea-efae9c5901e6" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-80dc-a147-c83e6d18a944" class="">“Is this from a rejected, closed, 
or abandoned grant?”</blockquote></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-804a-9f3c-f6dedc4f86bf" class="bulleted-list"><li style="list-style-type:disc">✅ YES → Save in:</li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-8006-a172-d5c9628df4c2" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">GRANTS_MASTER / 09_ARCHIVE</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-807f-a4e1-fb96ef1bdae7" class="bulleted-list"><li style="list-style-type:disc">STOP.</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d3-984b-c2aee32cab06" class="bulleted-list"><li style="list-style-type:disc">❌ NO → Ask the manager.</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8046-a748-fcd4ad8b19db"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80c7-99f5-d30c06a51fe9" class=""><strong>FINAL RULE (VERY IMPORTANT)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80b3-9a45-cb2af7630115" class="">If you reach a point where:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-805a-8635-fd9b2d4bcf64" class="bulleted-list"><li style="list-style-type:disc">two folders both seem possible</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b3-b858-c7c71551f1ae" class="bulleted-list"><li style="list-style-type:disc">or none seem correct</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8051-9431-d09f1c4f32da" class=""><strong>DO NOT SAVE THE FILE ANYWHERE.</strong></p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80ed-8c10-e45cb8a636fc" class="">Instead:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-804a-bbeb-f4d96f8f715d" class="numbered-list" start="1"><li>Stop</li></ol></div><div style="display:contents" dir="auto"><ol type="1" i
d="2e2c5e6f-95bd-8016-95ea-f3b3c919e3ee" class="numbered-list" start="2"><li>Message the manager:<div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-8026-96d4-c2ee749b9030" class="">“Unsure where to file [file name]. 
Please advise.”</blockquote></div></li></ol></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80fe-b12f-db55234002c3"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8008-aac6-c7f41c28df45" class=""><strong>REMEMBER</strong></h2></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-804a-ad2b-f282829b2d5a" class="bulleted-list"><li style="list-style-type:disc">Wrong folder = task not done</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80bc-b39c-f8120c0b8331" class="bulleted-list"><li style="list-style-type:disc">“Temporary” does not exist</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8034-a801-fb03283fff43" class="bulleted-list"><li style="list-style-type:disc">Guessing is worse than asking</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-802e-ac52-d199ce67c9fc" class="">This decision tree exists so <strong>you don’t have to think</strong> — only follow steps.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-806f-86fb-e9f1abb49919"/></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80af-8d2d-ca6db2b5300a" class="">If you want, 
next I can:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8071-b665-fc9ae617ee25" class="bulleted-list"><li style="list-style-type:disc">turn this into a <strong>1-page flowchart image</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f8-98dc-eeee0a20aa0b" class="bulleted-list"><li style="list-style-type:disc">simplify it into a <strong>yes/no checklist card</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8059-a2ea-dd3c64879714" class="bulleted-list"><li style="list-style-type:disc">or adapt it for <strong>Google Drive permissions</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8050-b521-c70c249ae308" class="">Just say which.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8081-bbb3-e9abc5c6ad0b" class="">Below is a <strong>literal decision tree</strong> written so a junior can follow it <strong>without thinking</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8071-a6b5-e5fb0c980897" class="">It is phrased as <strong>yes / no questions only</strong>, with <strong>one correct destination per path</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8013-969b-fc16e0fcd6b4" class="">You can paste this into a Google Doc titled:</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-803a-9510-cc486e0e07b8" class=""><strong>“WHERE DOES THIS FILE GO — READ BEFORE SAVING”</strong></p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-803c-99ef-e011df3269b5"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-8024-8310-fe804b2814a8" class=""><strong>WHERE DOES THIS FILE GO?</strong></h1></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8045-88bc-c877b9f7c6eb" class=""><strong>(DO NOT GUESS. 
FOLLOW THE QUESTIONS IN ORDER.)</strong></p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8019-b457-eabc3c98a623"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80b2-963e-d442b8bdcb2c" class=""><strong>START HERE</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80dd-b325-fa06dd9fd43e" class="">You have a file and you need to save it.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8089-b1c9-d2e3758a8dba" class=""><strong>DO NOT save it anywhere until you answer these questions in order.</strong></p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8057-bae5-d2c7830dc5fd"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8070-b293-d7c7c2abed65" class=""><strong>QUESTION 1 — IS THIS FILE RELATED TO GRANTS?</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8022-b192-c51387745ca4" class="">Ask yourself:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-80fa-83a7-f26ff283fc3d" class="">“Is this file about funding, grants, applications, 
or tenders?”</blockquote></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-806a-97eb-e7c3b5a5d832" class="bulleted-list"><li style="list-style-type:disc">❌ <strong>NO</strong> →<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8067-9bfc-e6accc04fe0c" class="">This file does <strong>not</strong> belong in GRANTS_MASTER.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8083-b6cd-f5c160e387a5" class="">Stop and ask the manager where it goes.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ec-9481-c27193d9519b" class="bulleted-list"><li style="list-style-type:disc">✅ <strong>YES</strong> →<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80d5-88ec-d8f8b923c103" class="">Continue to Question 2.</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80fb-a9fa-fc57c2ad778f"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-802d-9072-ea795633db6c" class=""><strong>QUESTION 2 — IS THIS A TRACKING OR STATUS FILE?</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80c2-a584-c8ed3f90f74e" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-8098-8495-fb0b908afe37" class="">“Is this a tracker, list, log, 
or status report used across many grants?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-807b-8896-fb006f62add2" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e8-b71c-fb6440b91b24" class="bulleted-list"><li style="list-style-type:disc">Grant tracker spreadsheet</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a3-82f7-e23a19ee7b16" class="bulleted-list"><li style="list-style-type:disc">Weekly status report</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8095-a20e-fc178a0510bd" class="bulleted-list"><li style="list-style-type:disc">Overview list</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-808c-9203-f3f5eda5c299" class="bulleted-list"><li style="list-style-type:disc">✅ <strong>YES</strong> →<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-806c-9b61-dfb95e863c9f" class="">Save in:</p></div></li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-809d-bd41-c70990013a46" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">GRANTS_MASTER / 01_TRACKERS</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-801c-a511-fec722404979" class="bulleted-list"><li style="list-style-type:disc">STOP.</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-805f-afb4-d605864449c6" class="bulleted-list"><li style="list-style-type:disc">❌ <strong>NO</strong> →<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8058-bed4-cb03d0c63088" class="">Continue to Question 3.</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8092-8e06-cb1b67e9ec3a"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8068-9e20-df985a56be22" class=""><strong>QUESTION 3 — IS THIS A LINK, SCREENSHOT, 
OR LISTING PAGE?</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8085-9d38-d86ad4627e21" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-8071-8fe6-fd5aaf6ce0de" class="">“Is this just showing where grants are listed, 
not a specific grant?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8050-b35d-fef4bbe64934" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a3-a95e-f616aa10d58e" class="bulleted-list"><li style="list-style-type:disc">Screenshots of grant portals</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c0-819f-ff0d255eea0d" class="bulleted-list"><li style="list-style-type:disc">Links to GrantConnect / state portals</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a0-8865-cc8f6a57cab7" class="bulleted-list"><li style="list-style-type:disc">Pages listing many grants</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8074-8c52-f85081fde869" class="bulleted-list"><li style="list-style-type:disc">✅ <strong>YES</strong> →<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8097-b9e3-e945cf75e503" class="">Save in:</p></div></li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-80e1-89d8-d90a5b907284" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">GRANTS_MASTER / 02_GRANT_SOURCES</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-808e-b8ea-f8d220a97b05" class="bulleted-list"><li style="list-style-type:disc">Then choose the correct subfolder:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-807f-9529-d807b12fc903" class="bulleted-list"><li style="list-style-type:circle">FEDERAL_PORTALS</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c6-8afd-df4de730b8ea" class="bulleted-list"><li style="list-style-type:circle">STATE_PORTALS</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8070-81c1-f44f47247916" class="bulleted-list"><li style="list-style-type:circle">LOCAL_PORTALS</li></ul></div><div style="display:contents" dir="auto"><ul i
d="2e2c5e6f-95bd-8025-af5f-cdab1f56ab53" class="bulleted-list"><li style="list-style-type:circle">AEA</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8019-9ef5-d34d23ba372b" class="">STOP.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ed-8a8f-ceedcadccb0b" class="bulleted-list"><li style="list-style-type:disc">❌ <strong>NO</strong> →<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80a3-8027-dbcbcb6a828e" class="">Continue to Question 4.</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-806c-b8d7-de84a8b59c4b"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-805b-a83b-f5b344a7e1de" class=""><strong>QUESTION 4 — IS THIS FILE ABOUT ONE SPECIFIC GRANT?</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80f2-b958-c318a8975d46" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-80f6-943d-e4d24b758053" class="">“Is this file for ONE named grant (not multiple)?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80d2-b62c-e029e67d2287" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-807f-8707-e3c64fcba40e" class="bulleted-list"><li style="list-style-type:disc">Guidelines for one grant</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b3-85f3-e738996ef2a9" class="bulleted-list"><li style="list-style-type:disc">Eligibility text for one grant</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b5-835a-df430616e2d2" class="bulleted-list"><li style="list-style-type:disc">Draft application for one grant</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f1-b620-e0e30fee0605" class="bulleted-list"><li style="list-style-type:disc">❌ <strong>NO</strong> →<div style="display:contents" dir="auto"><p i
d="2e2c5e6f-95bd-80a6-8840-d2755f3b1753" class="">Stop and ask the manager.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-801d-89ba-dff8d2b71099" class="bulleted-list"><li style="list-style-type:disc">✅ <strong>YES</strong> →<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8085-8378-c563d4667a0b" class="">Continue to Question 5.</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80e3-b962-da7e0121e974"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80d1-a10b-d5eac57a8d78" class=""><strong>QUESTION 5 — HAS THIS GRANT BEEN SUBMITTED YET?</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80c1-a17c-f3db71b14a3a" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-8033-b8ad-d48efb712b54" class="">“Has the application already been officially submitted?”</blockquote></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f5-b5fd-f1d66453425c" class="bulleted-list"><li style="list-style-type:disc">❌ <strong>NO (not submitted yet)</strong> →<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8004-9ffe-c5374adf8d30" class="">Go to:</p></div></li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-80d6-9ec7-d52ea83ce0d2" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">GRANTS_MASTER / 03_ACTIVE_GRANTS</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-808d-97d1-e923ebd45d90" class="bulleted-list"><li style="list-style-type:disc">Then open the folder for that grant.<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8030-8a1f-f8e4fb0267af" class="">Continue to Question 6.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-802e-9923-f202bd7c7c68" class="bulleted-list"><li style="list-style-type:disc">✅ <strong>YES (already s
ubmitted)</strong> →<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8093-9685-c56db752ea3b" class="">Go to:</p></div></li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-8052-8ad2-f1f60757d651" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">GRANTS_MASTER / 05_SUBMITTED</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e4-85cc-fdeba06b6cde" class="bulleted-list"><li style="list-style-type:disc">Then open the folder for that grant.<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80b6-bb00-dd7b6052dc76" class="">Save file there.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8004-a2fd-ca619a4bacc9" class="">STOP.</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8053-888a-d88fa6e8ad82"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80a2-9659-d0ec31d48e64" class=""><strong>QUESTION 6 — WHAT TYPE OF FILE IS IT? 
(ACTIVE GRANT)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80bb-8ed7-d616fdaf54dc" class="">You are now <strong>inside one specific grant folder</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8072-9c73-d5b2120cda9c" class="">Choose the FIRST option that matches.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8070-a019-c96677ae4679"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80f6-9669-ed0bcfa4e190" class=""><strong>OPTION A — OFFICIAL RULES OR GUIDELINES</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8098-b434-c2ddd26ee6f5" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-80b3-89ea-d6d7debdfb7e" class="">“Is this an official document explaining the rules of the grant?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80f9-adba-ec3df2dc402a" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8038-ae5c-c0f095282588" class="bulleted-list"><li style="list-style-type:disc">Guidelines PDF</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8042-bdfc-fec560840e26" class="bulleted-list"><li style="list-style-type:disc">Rules document</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f6-8d43-d365f03e5fc3" class="bulleted-list"><li style="list-style-type:disc">Official program overview</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8079-b876-e12c86c0765a" class="bulleted-list"><li style="list-style-type:disc">✅ YES → Save in:</li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-80b2-b019-d171dc423163" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">01_GUIDELINES</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-805f-b99a-d4f88dd22f52" c
lass="bulleted-list"><li style="list-style-type:disc">STOP.</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-801b-b356-d7cfefce9218"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8076-bc92-d0978717056d" class=""><strong>OPTION B — ELIGIBILITY INFORMATION</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80da-bb60-caa0edf2d2aa" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-80c6-9b62-c53e943b5dc7" class="">“Does this explain who can apply or what is allowed?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80ea-90b0-d42914dffe8a" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a4-a02a-f3e05eadbc62" class="bulleted-list"><li style="list-style-type:disc">“Who can apply” text</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ce-8939-d56e687aa29b" class="bulleted-list"><li style="list-style-type:disc">Eligibility screenshots</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8046-9270-fbff1555ef7b" class="bulleted-list"><li style="list-style-type:disc">Copied eligibility clauses</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-806d-a986-f5e522770eec" class="bulleted-list"><li style="list-style-type:disc">✅ YES → Save in:</li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-8085-84d8-d55e8cb105e5" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">02_ELIGIBILITY</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80de-bbda-e3d358e2d71b" class="bulleted-list"><li style="list-style-type:disc">STOP.</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-806b-bba9-f977955f83b1"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8081-8812-f3c33677c1fd" c
lass=""><strong>OPTION C — IP, LEGAL, OR RISK CONTENT</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8071-8395-e52ded1a95d9" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-80d7-804c-c1f8177191c9" class="">“Does this mention IP, ownership, licence, data, 
or risk?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80f2-93c8-e903c97997ba" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-806b-a30f-e689bd66fe5b" class="bulleted-list"><li style="list-style-type:disc">IP clauses</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8087-939b-f0586235f5d2" class="bulleted-list"><li style="list-style-type:disc">Ownership rules</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-801d-8b67-d103818108b8" class="bulleted-list"><li style="list-style-type:disc">Open-source requirements</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d0-93bb-d67ab0c321cd" class="bulleted-list"><li style="list-style-type:disc">Highlighted risk text</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f7-b7bd-ef07155136ac" class="bulleted-list"><li style="list-style-type:disc">✅ YES → Save in:</li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-8064-8378-ce86a7b22419" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">03_IP_AND_RISK</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-804f-84ef-fc4e7f2cde7b" class="bulleted-list"><li style="list-style-type:disc">STOP.</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80d2-9d13-d3549fac5d75"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-803a-bf44-d15262b18c1f" class=""><strong>OPTION D — REQUIREMENTS OR DEADLINES</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80eb-8831-dca3a073f303" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-8042-ab09-ee0ad9fdc599" class="">“Is this about what must be submitted and by when?”</blockquote></div><div style="display:contents" dir="auto"><p i
d="2e2c5e6f-95bd-80ac-ad85-fbf05464865f" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f2-8e35-d2b59fe0fe5f" class="bulleted-list"><li style="list-style-type:disc">Deadline notes</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8091-86e5-ca3fcdc18783" class="bulleted-list"><li style="list-style-type:disc">Required document lists</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8024-adde-dbbf52583fb2" class="bulleted-list"><li style="list-style-type:disc">Word limits</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-808c-9149-de394b13ba25" class="bulleted-list"><li style="list-style-type:disc">Submission instructions</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-803e-8e48-f4e6983d8c25" class="bulleted-list"><li style="list-style-type:disc">✅ YES → Save in:</li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-8079-a372-c90d81b80dd3" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">04_REQUIREMENTS</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80bf-a0e0-d9be748c7eb8" class="bulleted-list"><li style="list-style-type:disc">STOP.</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8086-87e6-ddf86c708671"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8006-a6ee-f284075c23fa" class=""><strong>OPTION E — BUDGET OR COSTS</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8098-b294-cd316309c929" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-808d-b66b-d8d90f41a9cd" class="">“Does this contain numbers, costs, 
or budget templates?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80b1-8a89-dea07851c53e" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8021-a3a2-d7b2aa4e0210" class="bulleted-list"><li style="list-style-type:disc">Budget spreadsheets</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f1-a4fd-ea4a525f27d8" class="bulleted-list"><li style="list-style-type:disc">Cost breakdowns</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80bf-862b-f79867d33717" class="bulleted-list"><li style="list-style-type:disc">Funding allocation tables</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8031-86f6-ce2b6e706e1e" class="bulleted-list"><li style="list-style-type:disc">✅ YES → Save in:</li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-8013-9f05-ec3a5ba4803e" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">05_BUDGET</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-800c-b350-d9ed558bf6bf" class="bulleted-list"><li style="list-style-type:disc">STOP.</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80a1-8631-cdcb10ced5ff"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8036-8dfc-eaa99e1cee5f" class=""><strong>OPTION F — DRAFT APPLICATION CONTENT</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8061-8b00-f83aa72b02fc" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-800f-a7bd-f30f932342b6" class="">“Is this a draft or working version of the application?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8042-b5e2-c34d1739ed0a" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-803e-8cac-cd447cc6d34a" class="bulleted-list"><li s
tyle="list-style-type:disc">Draft answers</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b9-9e53-d17c57382d34" class="bulleted-list"><li style="list-style-type:disc">Filled templates (not final)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8038-98b3-c2339cfedf71" class="bulleted-list"><li style="list-style-type:disc">In-progress text</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8040-a737-cfd447463cd4" class="bulleted-list"><li style="list-style-type:disc">✅ YES → Save in:</li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-80ad-a7b0-e8117ca01cbc" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">06_DRAFTS</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8012-92d5-ed39495d550a" class="bulleted-list"><li style="list-style-type:disc">STOP.</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-800f-a2de-c38b8954d010"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-808b-afcd-e24fbde7c8eb" class=""><strong>QUESTION 7 — IS THIS A TEMPLATE?</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8088-9df0-c25cf534a86b" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-8079-88fe-c876b5f63ba5" class="">“Is this a blank template meant to be reused?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-808e-a4f3-c15a0437ae2e" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c4-acd3-d777686ac7a6" class="bulleted-list"><li style="list-style-type:disc">Application template</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b6-8d6f-e655cdf1e7eb" class="bulleted-list"><li style="list-style-type:disc">Budget template</li></ul></div><div style="display:contents" dir="auto"><ul i
d="2e2c5e6f-95bd-805a-958b-e380601218da" class="bulleted-list"><li style="list-style-type:disc">Reporting template</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e7-af1c-cea80ab21fd4" class="bulleted-list"><li style="list-style-type:disc">✅ YES → Save in:</li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-80a0-b0a2-d5ff0519a184" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">GRANTS_MASTER / 07_TEMPLATES</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b5-871f-c49ed8cb9eac" class="bulleted-list"><li style="list-style-type:disc">STOP.</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8061-a5ac-f7ec6309985d" class="bulleted-list"><li style="list-style-type:disc">❌ NO → Continue.</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-802d-9b33-dcde86cdf019"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8087-b1bc-eecf691e7b47" class=""><strong>QUESTION 8 — IS THIS REFERENCE MATERIAL?</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8077-a11f-c56a7f340983" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-806c-9f0a-d2e3ba624eb7" class="">“Is this background reading or past examples?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-805c-92b7-c98c589dfe94" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8089-8a27-f029785485e7" class="bulleted-list"><li style="list-style-type:disc">Old successful applications</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-807d-8b82-ce5eb2560751" class="bulleted-list"><li style="list-style-type:disc">Policy documents</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a5-8558-e59862089887" class="bulleted-list"><li s
tyle="list-style-type:disc">Strategy papers</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-809c-a80b-ce2fbcd0e43d" class="bulleted-list"><li style="list-style-type:disc">✅ YES → Save in:</li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-8013-9881-feffcd56da08" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">GRANTS_MASTER / 08_REFERENCE</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c2-8e37-ffb8d3b21080" class="bulleted-list"><li style="list-style-type:disc">STOP.</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-802a-bfd2-e7f622193c87"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80c7-bb6c-f06d4893668b" class=""><strong>QUESTION 9 — IS THIS FINISHED OR NO LONGER ACTIVE?</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8014-8e2f-e1ad7ea8d408" class="">Ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-80b3-848a-eebaa60e8e87" class="">“Is this from a rejected, closed, 
or abandoned grant?”</blockquote></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e9-b802-e35f2d3c9498" class="bulleted-list"><li style="list-style-type:disc">✅ YES → Save in:</li></ul></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-8085-b360-d35fe649e3a8" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">GRANTS_MASTER / 09_ARCHIVE</code></pre></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b4-9e84-cbc25cad6d98" class="bulleted-list"><li style="list-style-type:disc">STOP.</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-805a-8054-e7d789ab5150" class="bulleted-list"><li style="list-style-type:disc">❌ NO → Ask the manager.</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80dc-883b-f47c6b432af2"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8039-92ea-c3ea21cf6570" class=""><strong>FINAL RULE (VERY IMPORTANT)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80ee-ab56-c5a9d6173323" class="">If you reach a point where:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8082-8466-d725b30e69e5" class="bulleted-list"><li style="list-style-type:disc">two folders both seem possible</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8091-a7a5-e10806a4e333" class="bulleted-list"><li style="list-style-type:disc">or none seem correct</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80d0-bfaf-cab4270192d8" class=""><strong>DO NOT SAVE THE FILE ANYWHERE.</strong></p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8077-b5a6-d8cce3f0b372" class="">Instead:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80ee-b1aa-dd95cf7b00e9" class="numbered-list" start="1"><li>Stop</li></ol></div><div style="display:contents" dir="auto"><ol type="1" i
d="2e2c5e6f-95bd-80a0-aa1e-c497bd593448" class="numbered-list" start="2"><li>Message the manager:<div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-8051-a6a6-d8a3b539d5d4" class="">“Unsure where to file [file name]. Please advise.”</blockquote></div></li></ol></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-801d-9c13-ca369a4c1416"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-805a-9f41-fa2c828a271e" class=""><strong>REMEMBER</strong></h2></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ed-88e5-f3a0cae2df84" class="bulleted-list"><li style="list-style-type:disc">Wrong folder = task not done</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e5-bdc4-ddad773ee247" class="bulleted-list"><li style="list-style-type:disc">“Temporary” does not exist</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80eb-979d-e414b2289619" class="bulleted-list"><li style="list-style-type:disc">Guessing is worse than asking</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-807f-8cdc-da28dd3f6115" class="">This decision tree exists so <strong>you don’t have to think</strong> — only follow steps.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-809f-8062-c165bae3dedd"/></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8045-89a9-dd705560585e" class="">
</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8063-ba11-e0d396724a59" class="">
</p></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-8014-9bc1-da1105826d7f" class=""><strong>SECTION 2 — FEDERAL GRANTS (GRANTCONNECT)</strong></h1></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8093-9896-e1248dd58e61" class=""><strong>Objective:</strong> Find and correctly log <em>every</em> open federal grant</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80ce-ad44-f6d0f076bddf" class=""><strong>Frequency:</strong> 2× per week (e.g. 
Monday &amp; 
Thursday)</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8030-a2e2-ee5b1a593cfe"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-800a-958b-dbd03b7fa0dd" class=""><strong>2.1 Open GrantConnect (EXACT STEPS)</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-804e-8fb9-f681da9dad7a" class="numbered-list" start="1"><li>Open Google Chrome</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80f9-94f9-d2fb805c7d00" class="numbered-list" start="2"><li>Click address bar</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8091-ba44-d492e86342f6" class="numbered-list" start="3"><li>Type <strong>exactly</strong>:</li></ol></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-8071-8cc4-ec9677d8bfd9" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">https://www.grants.gov.au</code></pre></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80c3-ad3e-cfa7bdf21ed8" class="numbered-list" start="1"><li></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8004-a5af-c51b9d14cdf6" class="numbered-list" start="2"><li>Press <strong>Enter</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8013-a7d7-e8bec80ea4a2" class="numbered-list" start="3"><li>Wait for page to fully load</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80e2-a92e-c3f648b84852" class="numbered-list" start="4"><li>Do NOT click anything else yet</li></ol></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80ee-b8ea-f4cd4eb6024a"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-802b-8301-e64d2a843504" class=""><strong>2.2 Navigate to Search Page</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" i
d="2e2c5e6f-95bd-80a1-9f27-d054c55ec4f5" class="numbered-list" start="1"><li>On the top menu, 
find <strong>“Search Grants”</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8013-a9f0-ce732677ff07" class="numbered-list" start="2"><li>Click <strong>“Search Grants”</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8080-909c-d4852577dd26" class="numbered-list" start="3"><li>Confirm the page title says something like:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b9-9024-c6864224fc82" class="bulleted-list"><li style="list-style-type:disc">“Search Grants”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8091-bebb-d17d12712cac" class="bulleted-list"><li style="list-style-type:disc">or “Find a Grant”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80be-8f7a-d95c477ad546" class="">If not → you are on the wrong page.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8034-b827-d4bbded44f6c"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8049-8ef2-e268d43f394c" class=""><strong>2.3 Apply Mandatory Filters (DO NOT CHANGE)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8073-b031-cd794565dbbd" class="">On the left or top filter panel:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8039-905d-e42e1243fe6d" class="numbered-list" start="1"><li>Find <strong>Grant Status</strong><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ec-96ff-d78dcd4fc851" class="bulleted-list"><li style="list-style-type:disc">Select <strong>Open</strong></li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8089-944a-dc3136f8f351" class="numbered-list" start="2"><li>Find <strong>Closing Soon</strong><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ef-a885-f788216a53df" class="bulleted-list"><li style="list-style-type:disc">Select <
strong>Yes</strong> (if available)</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8074-b6e3-d4623b19f433" class="numbered-list" start="3"><li>Find <strong>Sort By</strong><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c3-b6ca-d5cba5b21bc4" class="bulleted-list"><li style="list-style-type:disc">Select <strong>Closing Date (Soonest First)</strong></li></ul></div></li></ol></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80b8-8c10-d8e5c1309a54" class="">❌ Do NOT add industry filters</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80a4-b290-cf0bbe6ae3cf" class="">❌ Do NOT add funding amount filters</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8015-a137-c63960c62ee5"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8020-bece-c568606a152a" class=""><strong>2.4 Keyword Search (ONE WORD AT A TIME)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-807a-9b58-e6ff3eeda101" class="">You must repeat <strong>all steps below</strong> for <strong>each keyword</strong>.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8060-b935-e7190f5568ca" class=""><strong>Approved keywords (ONLY THESE):</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-801f-89ba-feacce634aa1" class="bulleted-list"><li style="list-style-type:disc">technology</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b5-aebf-edd0c770a771" class="bulleted-list"><li style="list-style-type:disc">digital</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d0-a70e-f194c91a9564" class="bulleted-list"><li style="list-style-type:disc">innovation</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80aa-9055-f423e9e3c56e" class="bulleted-list"><li style="list-style-type:disc">research</li></ul></div><div s
tyle="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8028-921b-fbff9df70374" class="bulleted-list"><li style="list-style-type:disc">AI</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e0-90fc-c07099556bff" class="bulleted-list"><li style="list-style-type:disc">infrastructure</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80fa-b19f-cb7667ca4017"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-800d-9e3a-ff37ccd9eb14" class=""><strong>For EACH keyword:</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-802f-9f61-c94f38e98e12" class="numbered-list" start="1"><li>Click into the keyword search box</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8063-b099-c1b0393c7cd9" class="numbered-list" start="2"><li>Type the keyword exactly</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8022-9b34-fe4e75a17be2" class="numbered-list" start="3"><li>Click <strong>Search</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80c7-b9d8-ef799b8edbd7" class="numbered-list" start="4"><li>Wait for results to load</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80b4-92ad-ff88cb8a8117" class="numbered-list" start="5"><li>Scroll slowly from top to bottom</li></ol></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-806a-88d1-f66ab966756a" class="">❌ Do NOT skip results</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80a5-9397-ef90944b6f06" class="">❌ Do NOT decide relevance</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8088-b61e-f85fdf7ecb8e"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-806c-8aaf-e215ebfa5852" class=""><strong>2.5 Open EVERY Result (NO EXCEPTIONS)</strong></h2></div><div style="display:contents" dir="auto"><p i
d="2e2c5e6f-95bd-80f7-b1ce-eea1553c6ffd" class="">For <strong>each grant result shown</strong>:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80e2-bee3-cc51ea1f5c07" class="numbered-list" start="1"><li>Click the <strong>grant title</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-805a-8746-fd349e65719f" class="numbered-list" start="2"><li>Wait for page to load</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8002-80e6-cbddd33581ff" class="numbered-list" start="3"><li>Scroll from top to bottom once</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80fd-988c-c783755a5d1a" class="numbered-list" start="4"><li>Do NOT skim randomly</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80cf-b78f-e631171f8d74" class="numbered-list" start="5"><li>Proceed immediately to logging</li></ol></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80f8-af88-c37c3a49b9eb"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8055-96aa-cc5abd4f8441" class=""><strong>2.6 Log the Grant (FIELD-BY-FIELD)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80e1-a9e2-feaf0c8225d9" class="">Open the <strong>Grant Tracker Spreadsheet</strong>.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80d5-bdfb-ed9f39def11b" class=""><strong>Create ONE new row per grant.</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-804d-80b1-fb0d759f69e8" class="">Fill columns EXACTLY as follows:</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8094-b5f3-eea625ccdeaf"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-807f-9c8b-d52cf0564339" class=""><strong>Column A — Grant Name</strong></h3></div><div style="display:contents" dir="auto"><ul i
d="2e2c5e6f-95bd-8007-b9c7-ed478fc36382" class="bulleted-list"><li style="list-style-type:disc">Copy the grant title</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8018-97b0-e68249cc690d" class="bulleted-list"><li style="list-style-type:disc">Paste exactly</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8038-82aa-fb442e2e5953" class="bulleted-list"><li style="list-style-type:disc">Do NOT edit wording</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8058-b407-e6d472d1425c"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80a0-8e44-e77c4e9d5c19" class=""><strong>Column B — Grant ID</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-802a-9754-ca6a53b4deea" class="bulleted-list"><li style="list-style-type:disc">Look for:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a9-ae2e-f2e1e6eca71a" class="bulleted-list"><li style="list-style-type:circle">Grant ID</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8040-889e-f194e2f05e1f" class="bulleted-list"><li style="list-style-type:circle">Opportunity number</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8045-8805-ecbe56703fc2" class="bulleted-list"><li style="list-style-type:disc">If found → copy-paste</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a6-8814-ccc1db59036e" class="bulleted-list"><li style="list-style-type:disc">If not found → type <strong>Not stated</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8011-9238-c4599eb184dc"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-809b-a4bd-c1937a1b923d" class=""><strong>Column C — Funding Body</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8020-bd96-d7020ebebc4f" class="bulleted-list"><li s
tyle="list-style-type:disc">Copy-paste organisation name</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d5-a67d-d2d2e6f2394e" class="bulleted-list"><li style="list-style-type:disc">Example:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-808f-9c04-c1a959aaed2d" class="bulleted-list"><li style="list-style-type:circle">“Department of Industry, 
Science and Resources”</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8034-bf07-d3e31b0da459"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8034-9824-e393726e9f49" class=""><strong>Column D — Country</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80cb-b49f-f6e7417e36be" class="bulleted-list"><li style="list-style-type:disc">Type <strong>Australia</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8077-9bf7-fdbf01c5a272" class="bulleted-list"><li style="list-style-type:disc">Always the same</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80f3-b6b8-cb34977e7a79"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-800d-823f-ec78ca331be8" class=""><strong>Column E — Official URL</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-809e-9c0b-fd4015a624c4" class="bulleted-list"><li style="list-style-type:disc">Copy full page URL</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8047-a651-e3b55689bb54" class="bulleted-list"><li style="list-style-type:disc">Paste exactly</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8025-8c3a-c14d9691c002"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8074-bde4-d54b579c7e5c" class=""><strong>Column F — Opening Date</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b9-8c90-ed8d22573629" class="bulleted-list"><li style="list-style-type:disc">Copy exact date</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8078-8753-c15b7bb33a9e" class="bulleted-list"><li style="list-style-type:disc">If not shown → type <strong>Not stated</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-808d-ac6d-f0eab9f1fb0e"/></div><div style="display:contents" dir="auto"><h3 i
d="2e2c5e6f-95bd-80d6-a9b8-d26a507919ad" class=""><strong>Column G — Closing Date</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-803a-a6e9-cb973ea3f958" class="bulleted-list"><li style="list-style-type:disc">Copy exact date</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-806e-b533-dc0f82f362a4" class="bulleted-list"><li style="list-style-type:disc">Include day, month, 
year</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80b0-bed4-c5c56b08a4bd"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8050-84ad-d7970d2087a7" class=""><strong>Column H — Funding Amount</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-807c-9a02-c7553d4556c0" class="bulleted-list"><li style="list-style-type:disc">Copy exact wording:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8033-bf62-faa71608131f" class="bulleted-list"><li style="list-style-type:circle">“Up to $500,000”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-807a-9339-d92b186c1472" class="bulleted-list"><li style="list-style-type:circle">“Between $50,000 and $1 million”</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8076-88bd-fb350c8bf4ba" class="bulleted-list"><li style="list-style-type:disc">Do NOT simplify</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8065-950e-cd0b6b050e97"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8061-9623-dfaf8b88dfa7" class=""><strong>Column I — Status</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80fa-a6aa-dccd4b7f936e" class="bulleted-list"><li style="list-style-type:disc">Type <strong>Identified</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-804c-852a-dca2e82c2ab0" class="bulleted-list"><li style="list-style-type:disc">Do not use any other word</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8075-a19d-c19a18043eb9"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80ce-983a-eb48d3c9900a" class=""><strong>Column J — Notes</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8010-bd2d-e04fd644f8b3" class="bulleted-list"><li style="list-style-type:disc">Leave blank for n
ow</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-801f-867d-f0dad2fe2c91"/></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80aa-a4c7-d287645b006b" class="">✅ <strong>DONE when:</strong></p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-805d-80b6-ef628ae73153" class="">Row is fully filled, 
no empty cells except Notes.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80b6-a335-f31fc0a83625"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-8051-ba60-fe86453ca168" class=""><strong>SECTION 3 — BUSINESS.GOV.AU GRANTS FINDER</strong></h1></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80cc-9405-e5f039716043" class=""><strong>Objective:</strong> Capture SME + innovation programs</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80d9-b3e8-e66beb263fd0" class=""><strong>Frequency:</strong> Monthly</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-805c-a4eb-ef3db7052b48"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80e1-bd46-f633c9eef7cb" class=""><strong>3.1 Open Grants Finder</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80e6-9472-d2d41b042096" class="numbered-list" start="1"><li>Open new browser tab</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8073-8ace-d3c896302f69" class="numbered-list" start="2"><li>Type:</li></ol></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-804a-b915-d0bb071c10b5" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">https://business.gov.au/grants-and-programs</code></pre></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80d3-b026-c59bc39f0333" class="numbered-list" start="1"><li></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80d4-bce6-c72b56399447" class="numbered-list" start="2"><li>Press Enter</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-805f-a6d5-cd99dddcce83" class="numbered-list" start="3"><li>Wait for page load</li></ol></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80dd-b40b-f420533c7587"/></div><div style="display:contents" d
ir="auto"><h2 id="2e2c5e6f-95bd-8099-9d06-f52850679b0f" class=""><strong>3.2 Apply Filters</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-804d-abff-fca3decac91f" class="numbered-list" start="1"><li>Find <strong>Industry</strong><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b5-b398-c4066060e667" class="bulleted-list"><li style="list-style-type:disc">Select:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e3-95b6-c3087d5f5d2b" class="bulleted-list"><li style="list-style-type:circle">Technology</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8032-a4c9-d9109cfea984" class="bulleted-list"><li style="list-style-type:circle">Digital (if available)</li></ul></div></li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80c5-b5f7-d84812ab8aee" class="numbered-list" start="2"><li>Find <strong>Business Stage</strong><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c1-9bf2-f13caf33fcb6" class="bulleted-list"><li style="list-style-type:disc">Select:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-803b-afdf-c771cc9845e2" class="bulleted-list"><li style="list-style-type:circle">Startup</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8068-b0d9-f89f20ab38ae" class="bulleted-list"><li style="list-style-type:circle">Small business</li></ul></div></li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80b2-9cab-d3604028f23b" class="numbered-list" start="3"><li>Click <strong>Search</strong></li></ol></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80e8-b084-d25d43fe0b44"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-800e-9305-e650cc5a82c7" class=""><strong>3.3 Open EACH Result</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8087-bf25-f15886354feb" c
lass="">For every program shown:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8018-ab9e-d7b05321a2f2" class="numbered-list" start="1"><li>Click program name</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80da-b5a0-ccaf1d7ca5a7" class="numbered-list" start="2"><li>Scroll entire page</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80a2-b63c-c07308572f30" class="numbered-list" start="3"><li>Proceed to logging</li></ol></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-808d-833a-f2463e784238"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8072-bec2-e13d2df50785" class=""><strong>3.4 Log Program (Same Tracker)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8009-b7c0-c2f8f913701a" class="">Fill same columns as Section 2.6 plus:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80df-ab07-dc45245468e1" class="bulleted-list"><li style="list-style-type:disc">Eligibility summary → paste into Notes</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f9-87b1-cc600ed6050d" class="bulleted-list"><li style="list-style-type:disc">Funding type → Grant / Support / Voucher (if stated)</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80e8-acb8-ca54687bf59b"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-8002-90be-cecaeee84786" class=""><strong>SECTION 4 — AEA (AUSTRALIA’S ECONOMIC ACCELERATOR)</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-807e-ab30-c8058e836f83" class=""><strong>4.1 Monthly Check</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80d7-8033-d67b5dc92254" class="numbered-list" start="1"><li>Open Google</li></ol></div><div style="display:contents" dir="auto"><ol type="1" i
d="2e2c5e6f-95bd-8036-8f60-fa3304129fc9" class="numbered-list" start="2"><li>Search:</li></ol></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-809b-8b13-c35e8f4adfac" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Australia’s Economic Accelerator grant</code></pre></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-808c-8c30-e6d7c9fd7107" class="numbered-list" start="1"><li></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80f6-990e-d547e7346308" class="numbered-list" start="2"><li>Open <strong>official gov.au page only</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80ce-9bc4-c22ad75076f8" class="numbered-list" start="3"><li>Ignore blogs or news articles</li></ol></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8046-8c03-fa6c5e9d4c23"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8010-a8a6-e0c8b193b379" class=""><strong>4.2 Identify Rounds</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8023-95aa-e35129701f3c" class="">Look for:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c8-9973-fbfbd6f2ec17" class="bulleted-list"><li style="list-style-type:disc">Ignite</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80fc-b450-cdeb133209b0" class="bulleted-list"><li style="list-style-type:disc">Innovate</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80da-883a-c11af49eb29e" class="bulleted-list"><li style="list-style-type:disc">Open</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8040-abc9-e378437b6eaa" class="bulleted-list"><li style="list-style-type:disc">Upcoming</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-800d-9095-e56d09f3dca6" class="bulleted-list"><li s
tyle="list-style-type:disc">Closing dates</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80ae-a37f-c58c889edcb6"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-800c-b3d4-cbca245b620d" class=""><strong>4.3 Log AEA Opportunity</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80f1-9232-dbb71e54b3fd" class="">Fill tracker fields plus:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80fe-af6a-efca187dd110" class="bulleted-list"><li style="list-style-type:disc">Program type: Ignite / Innovate</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d4-87ab-ebb0e24c2949" class="bulleted-list"><li style="list-style-type:disc">Round number (if shown)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8043-bec3-e760862528dc" class="bulleted-list"><li style="list-style-type:disc">Partner required:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8007-8c23-deadeb329536" class="bulleted-list"><li style="list-style-type:circle">Yes</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8033-a58e-eef2d2b26f27" class="bulleted-list"><li style="list-style-type:circle">No</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e6-82e0-e29691991d22" class="bulleted-list"><li style="list-style-type:circle">Not stated</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8010-b3d4-fb041f4ebd30"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-800e-927e-dac7e489c63a" class=""><strong>SECTION 5 — STATE GOVERNMENT GRANTS</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-804f-bbbd-defe620413da" class=""><strong>5.1 Identify State Portal (ONCE)</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8019-bc3e-dbc9ab435a83" class="numbered-list" s
tart="1"><li>Google:</li></ol></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-8030-90bb-c2cee4a75f7b" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">[STATE NAME] government innovation grants</code></pre></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8054-8c84-c9fd420ea417" class="numbered-list" start="1"><li></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80b2-85c8-fb20e4f32bb4" class="numbered-list" start="2"><li>Click official state website only</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-801b-bec0-d9d5512763dd" class="numbered-list" start="3"><li>Save URL in tracker header</li></ol></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80a6-9206-cf578f6ac788"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80fb-86e6-eb9e539a5ce2" class=""><strong>5.2 Monthly Scan</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-804c-85a6-ca8672c3b411" class="numbered-list" start="1"><li>Open state portal</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-804f-aad5-e6b8e6053267" class="numbered-list" start="2"><li>Search:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80db-bcdc-d3d02a616992" class="bulleted-list"><li style="list-style-type:disc">innovation</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8039-b5ea-ca4218a492b1" class="bulleted-list"><li style="list-style-type:disc">digital</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-804a-90eb-c0f55e5285bb" class="bulleted-list"><li style="list-style-type:disc">research</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-809c-adb9-fd173e5c342d" class="numbered-list" start="3"><li>For EACH open grant:<div s
tyle="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-809e-b673-ddee7a0f760c" class="bulleted-list"><li style="list-style-type:disc">Open page</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d1-8d90-f43ed04f8ba4" class="bulleted-list"><li style="list-style-type:disc">Log EXACTLY like Section 2.6</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8028-a103-cf2145cf08c7"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-80fe-b109-c95ebd36953e" class=""><strong>SECTION 6 — ELIGIBILITY TEXT (COPY ONLY)</strong></h1></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80a1-b43e-fb43eabc7a43" class="">For EACH logged grant:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-808f-8e5e-c8bef6579bc7" class="numbered-list" start="1"><li>Find section titled:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ff-9f34-f243bf2b4bb5" class="bulleted-list"><li style="list-style-type:disc">“Who can apply”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-803e-9077-f6c4d2f6247e" class="bulleted-list"><li style="list-style-type:disc">“Eligibility”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8084-877a-fa431d6698ba" class="numbered-list" start="2"><li>Highlight text</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80e7-985d-fdfb4074df40" class="numbered-list" start="3"><li>Copy-paste into Notes column</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80b2-ad63-e1f60b16aea6" class="numbered-list" start="4"><li>Do NOT rewrite</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-809e-843c-d2810b35a849" class="numbered-list" start="5"><li>Do NOT summarise</li></ol></div><div style="display:contents" dir="auto"><hr i
d="2e2c5e6f-95bd-804f-8769-d1f1bc873de5"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-808e-91b9-d07b9a5b4166" class=""><strong>SECTION 7 — IP &amp; 
LEGAL TEXT (CRITICAL)</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80e6-8808-e6d328529c7e" class=""><strong>7.1 Search Documents</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8014-9ed6-f1a127c111c6" class="numbered-list" start="1"><li>Open grant guidelines</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8012-937e-f501684e1975" class="numbered-list" start="2"><li>Press <strong>Ctrl + F</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80ce-b23a-e4ff515aa304" class="numbered-list" start="3"><li>Search words ONE AT A TIME:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-807b-95af-dbe5e31bdadb" class="bulleted-list"><li style="list-style-type:disc">IP</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ce-b10c-cd5f9bccb275" class="bulleted-list"><li style="list-style-type:disc">ownership</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8087-bcf7-c8eba220c57d" class="bulleted-list"><li style="list-style-type:disc">licence</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8039-ad00-f05981df2ff2" class="bulleted-list"><li style="list-style-type:disc">open source</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b0-b77c-ecce9158b10b" class="bulleted-list"><li style="list-style-type:disc">data</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-809c-9123-e48b905fde25"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80f3-a6ce-de098c8fc35c" class=""><strong>7.2 Copy Text</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-806e-9729-d1e8534e7077" class="">For EACH match:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80cf-991b-ee0884f53f65" class="numbered-list" 
tart="1"><li>Highlight full paragraph</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8033-8bd9-e2b0e46b1766" class="numbered-list" start="2"><li>Copy</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80b8-a112-e0b4c9fd9ec0" class="numbered-list" start="3"><li>Paste into IP Notes document</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-805f-b146-e8c94416abdd" class="numbered-list" start="4"><li>Label with grant name</li></ol></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8019-a00d-d3e8dcbc5cf2"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8098-a06e-f4e0256ffa4b" class=""><strong>7.3 Red Flag Protocol (STOP RULE)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-806a-9cc7-e24eace3eba6" class="">If text includes:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-803e-8eec-e5b2d5c28da5" class="bulleted-list"><li style="list-style-type:disc">open source</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c7-9e95-d0c784a1ccc0" class="bulleted-list"><li style="list-style-type:disc">government owns</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8096-88a1-c3b211d1320c" class="bulleted-list"><li style="list-style-type:disc">joint ownership</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-809c-b4b0-dbf197fc6340" class="bulleted-list"><li style="list-style-type:disc">source code</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8087-ade3-c329f3ba2466" class="bulleted-list"><li style="list-style-type:disc">IP transfer</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80fc-9027-d2616936858f" class="">Then:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8077-b325-dd403eb1ba96" c
lass="numbered-list" start="1"><li>Highlight red</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8097-9c93-f629ae1f26b9" class="numbered-list" start="2"><li>Message manager:</li></ol></div><div style="display:contents" dir="auto"><pre id="2e2c5e6f-95bd-8076-927c-e09bb39da54b" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">IP risk found in [Grant Name]. 
Please review.</code></pre></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-809f-8c83-c9051ead5f0d" class="numbered-list" start="1"><li></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-808e-b1db-da3feaf9cdad" class="numbered-list" start="2"><li>Stop working on this grant</li></ol></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80fb-9873-dafa95fbe2fa"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-8086-8050-de42c82c4e3b" class=""><strong>SECTION 8 — DEADLINES &amp; 
REQUIREMENTS</strong></h1></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8012-837c-c7f3c4c1672c" class="">For EACH grant:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-806c-bea9-ffe33de9730d" class="bulleted-list"><li style="list-style-type:disc">Copy deadline date</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80be-9419-cb3de00ceae7" class="bulleted-list"><li style="list-style-type:disc">Copy time zone</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e4-a784-dd407fb73182" class="bulleted-list"><li style="list-style-type:disc">Copy submission method</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-808d-bef3-c7ebe71d8cd5" class="bulleted-list"><li style="list-style-type:disc">List required documents</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8010-b0d9-c3986cee3f48" class="bulleted-list"><li style="list-style-type:disc">List word limits</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8066-8a96-ef6bfa562edf" class="bulleted-list"><li style="list-style-type:disc">List file formats</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80ac-a0e9-eff20dd7516f"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-8003-ad9f-c9187dcfd35d" class=""><strong>SECTION 9 — APPLICATION PREP (ONLY WHEN TOLD)</strong></h1></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8011-94f1-ec62819fdc8e" class="">When instructed:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-809b-bc9f-e2194ef428d9" class="numbered-list" start="1"><li>Download templates</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80c6-8cf0-f1456803622e" class="numbered-list" start="2"><li>Copy master content</li></ol></div><div style="display:contents" dir="auto"><ol type="1" i
d="2e2c5e6f-95bd-80c5-9b4d-c5ce4cc8ec56" class="numbered-list" start="3"><li>Paste into template</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80ef-8f98-dbb20f1d01c1" class="numbered-list" start="4"><li>Do NOT edit text</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-805b-ab8a-f895422ccf09" class="numbered-list" start="5"><li>Highlight missing info</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80d6-b72c-c7e69d11a353" class="numbered-list" start="6"><li>Save draft</li></ol></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80ed-98cf-f2921d6cdf29"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-8012-8fad-cf327494926c" class=""><strong>SECTION 10 — STATUS UPDATES</strong></h1></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8008-9860-eedae8e0beb2" class="">Only allowed statuses:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8032-bb82-c8d5d8cca16f" class="bulleted-list"><li style="list-style-type:disc">Identified</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c7-a4c8-e6649698a0f3" class="bulleted-list"><li style="list-style-type:disc">In Review</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80da-a330-c5925a54c30a" class="bulleted-list"><li style="list-style-type:disc">Drafting</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f9-a0ca-ffb31268e550" class="bulleted-list"><li style="list-style-type:disc">Submitted</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8028-bb3c-d56e27ad7d48" class="bulleted-list"><li style="list-style-type:disc">Awarded</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8088-ad3d-c65b5a02431e" class="bulleted-list"><li style="list-style-type:disc">Rejected</li></ul></div><div s
tyle="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8055-84e1-f0fdeac1f362" class="">Never invent new ones.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-807c-b97b-f5c24fe94767"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-80e4-b6bd-ea7ccb4ea14b" class=""><strong>SECTION 11 — END OF DAY CHECK</strong></h1></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-8000-8b74-c28447e2ca13" class="numbered-list" start="1"><li>Save tracker</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80da-af91-ff53ba228151" class="numbered-list" start="2"><li>Save documents</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e2c5e6f-95bd-80a1-9b22-c818e1906ddd" class="numbered-list" start="3"><li>Message manager:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-802d-b015-c66ff373b389" class="bulleted-list"><li style="list-style-type:disc">What was completed</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80fb-b5a6-f28fc078fe25" class="bulleted-list"><li style="list-style-type:disc">What is blocked</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8015-8b2b-c6488b30025e" class="bulleted-list"><li style="list-style-type:disc">What is next</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-803b-bcde-d2303fa850fe"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80c4-8ac3-e68db57c11d5" class=""><strong>FINAL DEFINITION OF DONE</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80fb-a39b-f1ee578e7c34" class="">DONE means:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80fc-8bc4-f421bae839ef" class="bulleted-list"><li style="list-style-type:disc">every field filled</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-808b-b726-dc1b3b62d689" c
lass="bulleted-list"><li style="list-style-type:disc">every step followed</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e8-954d-e90f441a47fd" class="bulleted-list"><li style="list-style-type:disc">no assumptions</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8035-a187-ed1d8a23945f" class="bulleted-list"><li style="list-style-type:disc">no silence</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80b5-87e3-c87dade0fdee"/></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80da-91f4-fcd48f4b8f5d" class="">If you want, next I can:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80dd-8b74-f33f2cd5d04f" class="bulleted-list"><li style="list-style-type:disc">expand this to <strong>SECTION 12–15</strong> (budget, reporting, audits)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b2-a0b6-e11dc2c3d2fd" class="bulleted-list"><li style="list-style-type:disc">turn each section into <strong>one-page task cards</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8022-939d-faf7c64e8d2f" class="bulleted-list"><li style="list-style-type:disc">or produce a <strong>fillable checklist PDF</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-806e-a68b-eb675bb0f9b1" class="">Say the word.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
