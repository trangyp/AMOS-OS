---
tags: [amos-general]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>AMOS — JUNIOR ASSISTANT OPERATING GUIDE</title><style>
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
	
</style></head><body><article id="2e1c5e6f-95bd-80f0-982b-d455d43b774c" class="page sans"><header><h1 class="page-title" dir="auto"><strong>AMOS — JUNIOR ASSISTANT OPERATING GUIDE</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-8072-af69-d3fc0a39f0aa" class=""><strong>Purpose:</strong> Clear structure, safe execution, predictable outcomes</p></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-806d-9c14-fcb884506776" class=""><strong>Audience:</strong> Entry-level, no prior domain knowledge required</p></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-807d-b4cb-dae7b80de13c" class=""><strong>Role:</strong> Administrative and operational support</p></div><div style="display:contents" dir="auto"><hr id="2e1c5e6f-95bd-8037-b783-da1710c24f7c"/></div><div style="display:contents" dir="auto"><h2 id="2e1c5e6f-95bd-8070-8a06-d292d5c33c64" class=""><strong>A quick note before we start</strong></h2></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-80b6-8632-eb17620b2b81" class="">This guide exists to <strong>make your work clear, bounded, and manageable</strong>. You are not expected to understand the full project, make judgment calls, or “figure things out” on your own. Your role is important because it keeps work organised, accurate, and on track. If at any point something feels unclear, the correct action is always to pause and ask. That is part of doing the job well.</p></div><div style="display:contents" dir="auto"><hr id="2e1c5e6f-95bd-809b-9aa7-c4c11dc1113e"/></div><div style="display:contents" dir="auto"><h2 id="2e1c5e6f-95bd-807b-a6bf-de1371468340" class=""><strong>Core working principle (important)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-804b-b7e5-e8d157a3f01d" class="">Your responsibility is <strong>execution</strong>, not interpretation.</p></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-80e6-bdbf-e3a0b0e01fa9" class="">That means:</p></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8073-8cdc-ed5333c80515" class="bulleted-list"><li style="list-style-type:disc">following instructions as written</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8027-8a66-e7ee04b434df" class="bulleted-list"><li style="list-style-type:disc">completing tasks fully</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8037-9800-f33bd9358682" class="bulleted-list"><li style="list-style-type:disc">communicating clearly</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-805e-b32e-d301fe6582d3" class="bulleted-list"><li style="list-style-type:disc">flagging issues early</li></ul></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-8024-a3fa-c84e3ae6d1b3" class="">Accuracy, consistency, and follow-through matter more than speed or initiative.</p></div><div style="display:contents" dir="auto"><hr id="2e1c5e6f-95bd-808d-8bdd-cb71e8ff9b80"/></div><div style="display:contents" dir="auto"><h2 id="2e1c5e6f-95bd-80d4-b2c6-c28bc55144c5" class=""><strong>What you are</strong></h2></div><div style="display:contents" dir="auto"><h2 id="2e1c5e6f-95bd-80ac-902e-ee2bb3d45205" class=""><strong>not</strong></h2></div><div style="display:contents" dir="auto"><h2 id="2e1c5e6f-95bd-80c4-a521-dc1a78ac072d" class=""><strong>expected to do</strong></h2></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-807c-bc79-cedb133b938b" class="">You are <strong>not</strong> expected to:</p></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8043-bfca-dcc0f736b298" class="bulleted-list"><li style="list-style-type:disc">decide whether something is good or bad</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8038-804e-c63419ff1554" class="bulleted-list"><li style="list-style-type:disc">improve wording or rewrite content</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-802f-8b6c-f979dd7edce6" class="bulleted-list"><li style="list-style-type:disc">explain the AMOS project to anyone</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80e6-88d1-decb2ed2a6fa" class="bulleted-list"><li style="list-style-type:disc">answer questions from funders or external parties</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80c2-b373-c06924d1f21e" class="bulleted-list"><li style="list-style-type:disc">interpret legal or technical language</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80b8-85b1-da032fd5bbd2" class="bulleted-list"><li style="list-style-type:disc">guess what something means</li></ul></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-80af-a821-ddaedfb3f8a8" class="">If something is unclear, incomplete, or confusing, you should stop and ask.</p></div><div style="display:contents" dir="auto"><hr id="2e1c5e6f-95bd-803a-912d-e0eee8ac58af"/></div><div style="display:contents" dir="auto"><h1 id="2e1c5e6f-95bd-804d-a272-f7a90df271c2" class=""><strong>PART 1 — DAILY WORK BASICS</strong></h1></div><div style="display:contents" dir="auto"><h3 id="2e1c5e6f-95bd-80fe-aaf0-c3171ef5d66c" class=""><strong>What your role includes</strong></h3></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-80bd-9738-e751f4ac711c" class="">You will regularly:</p></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-804a-b6ce-f304174d5e16" class="bulleted-list"><li style="list-style-type:disc">check official funding and government websites</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-805c-a851-ffa01eca184b" class="bulleted-list"><li style="list-style-type:disc">copy information exactly as it appears</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8060-8882-efaa35c873a9" class="bulleted-list"><li style="list-style-type:disc">enter information into spreadsheets or trackers</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-807e-8add-c94218a0ea1d" class="bulleted-list"><li style="list-style-type:disc">prepare drafts using existing templates</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-803d-8130-f1cd4c8a70c2" class="bulleted-list"><li style="list-style-type:disc">flag risks or unclear items</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80c9-84d1-fad3ff709e56" class="bulleted-list"><li style="list-style-type:disc">track deadlines and status</li></ul></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-8076-b8c3-d7da8ca1b3e9" class="">You will always be given direction on <em>what</em> to work on.</p></div><div style="display:contents" dir="auto"><hr id="2e1c5e6f-95bd-80c2-b513-d45467ed2347"/></div><div style="display:contents" dir="auto"><h3 id="2e1c5e6f-95bd-8060-a85c-ee251725c029" class=""><strong>What your role does not include</strong></h3></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-803b-b353-f31805768a04" class="">You do not:</p></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8030-a2d7-ee1c0a56276e" class="bulleted-list"><li style="list-style-type:disc">set priorities or strategy</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8064-8fcd-f541043b802a" class="bulleted-list"><li style="list-style-type:disc">decide eligibility</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8059-9edd-c9b6542522eb" class="bulleted-list"><li style="list-style-type:disc">negotiate or communicate positions</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-802d-bbc4-d8dd19ec73f7" class="bulleted-list"><li style="list-style-type:disc">submit applications</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8065-bb02-d60b5238cc69" class="bulleted-list"><li style="list-style-type:disc">represent the project externally</li></ul></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-80f3-8de6-ed715b23319a" class="">Those responsibilities sit elsewhere.</p></div><div style="display:contents" dir="auto"><hr id="2e1c5e6f-95bd-8024-bb58-d721e7f123d4"/></div><div style="display:contents" dir="auto"><h1 id="2e1c5e6f-95bd-80a6-8a3c-d802a1efa0eb" class=""><strong>PART 2 — FILE &amp; FOLDER HANDLING</strong></h1></div><div style="display:contents" dir="auto"><h3 id="2e1c5e6f-95bd-8058-a07d-f29d8fdfea25" class=""><strong>Folder structure (please do not change)</strong></h3></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-8022-b5d7-ebcd06efaa92" class="">You will see folders such as:</p></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80de-a2b9-c6de7d456f0a" class="bulleted-list"><li style="list-style-type:disc">AMOS_Master_Dossier/</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8019-900b-ce03af42bdc6" class="bulleted-list"><li style="list-style-type:disc">AMOS_Grants_Tracker/</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80ab-86b9-e581d0bb6497" class="bulleted-list"><li style="list-style-type:disc">AMOS_Funders_Contacts/</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-803e-ab26-f0449741b8aa" class="bulleted-list"><li style="list-style-type:disc">AMOS_Submitted/</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80b1-b070-fb2f24602184" class="bulleted-list"><li style="list-style-type:disc">AMOS_Contracts_IP/</li></ul></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-8005-b2d3-de9c12925382" class="">Please:</p></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-805f-bd55-fd466498b08c" class="bulleted-list"><li style="list-style-type:disc">do not rename folders</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8026-886f-f692257f8a98" class="bulleted-list"><li style="list-style-type:disc">do not move files between folders</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80ef-b7d5-e99f8010818a" class="bulleted-list"><li style="list-style-type:disc">do not delete files</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80f9-a217-f54b3cfe2ef1" class="bulleted-list"><li style="list-style-type:disc">if you see duplicates, keep both and flag them</li></ul></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-8047-9747-e9f2687064e7" class="">Organisation and traceability matter.</p></div><div style="display:contents" dir="auto"><hr id="2e1c5e6f-95bd-80d2-9641-e413b3e1230f"/></div><div style="display:contents" dir="auto"><h3 id="2e1c5e6f-95bd-80f5-a5d4-e02bd2d023e8" class=""><strong>Files that must not be edited</strong></h3></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-8033-95fc-f91b24e56b8c" class="">If a file name includes:</p></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-804c-a19c-d69741329373" class="bulleted-list"><li style="list-style-type:disc"><strong>IMMUTABLE</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-806d-97a1-f5e26ce21e8d" class="bulleted-list"><li style="list-style-type:disc"><strong>CORE</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8030-ab28-f900691207d9" class="bulleted-list"><li style="list-style-type:disc"><strong>IP</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8052-995e-fe55202cef8a" class="bulleted-list"><li style="list-style-type:disc"><strong>MASTER</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-80b9-888e-c5aea1d15e32" class="">Please do not edit it.</p></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-8097-8c1d-d1e0fc8970f5" class="">If a funder requests changes to one of these files, pause and escalate.</p></div><div style="display:contents" dir="auto"><hr id="2e1c5e6f-95bd-801e-b499-c40a93cc6bb0"/></div><div style="display:contents" dir="auto"><h1 id="2e1c5e6f-95bd-80fc-a37f-f9914d7c893b" class=""><strong>PART 3 — FUNDING TRACKER (KEY RESPONSIBILITY)</strong></h1></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-8019-ab2c-fe8fa45210b7" class="">You will work primarily in the <strong>AMOS_Funding_Tracker</strong> spreadsheet.</p></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-8031-9bf9-ebd6e88dd3b6" class="">Each row represents <strong>one</strong> funding opportunity.</p></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-80b1-aada-db077891aced" class="">Please fill columns as follows:</p></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-807c-8a52-da9edb6f85c6" class="bulleted-list"><li style="list-style-type:disc"><strong>Funding Class:</strong> number only (1–11). If unsure, write <em>UNKNOWN</em>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8019-b768-df48b16dcacd" class="bulleted-list"><li style="list-style-type:disc"><strong>Funder Name:</strong> copy exactly from the website.</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80ff-ae49-fa88f0f8053e" class="bulleted-list"><li style="list-style-type:disc"><strong>Country:</strong> country name only.</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-806f-8c01-e04b9f532394" class="bulleted-list"><li style="list-style-type:disc"><strong>Portal URL:</strong> exact webpage link.</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80a6-9a3e-e32bf522a074" class="bulleted-list"><li style="list-style-type:disc"><strong>Programme Name:</strong> official programme title.</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8055-a757-c318195b15e6" class="bulleted-list"><li style="list-style-type:disc"><strong>Workstream ID:</strong> leave blank unless instructed.</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-807b-8d0c-f89a5bb6c096" class="bulleted-list"><li style="list-style-type:disc"><strong>Status:</strong> choose only from<div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8003-8c95-f2c147ec7e71" class="bulleted-list"><li style="list-style-type:circle">Not Started</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80c0-acdd-e54b427244ae" class="bulleted-list"><li style="list-style-type:circle">Drafting</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80a1-821a-f90fa1f6eb30" class="bulleted-list"><li style="list-style-type:circle">Submitted</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8081-982b-f89111f993aa" class="bulleted-list"><li style="list-style-type:circle">Awarded</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80bd-b9b9-ec76671303e5" class="bulleted-list"><li style="list-style-type:circle">Rejected</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80b9-aa92-f1655285170a" class="bulleted-list"><li style="list-style-type:disc"><strong>Deadline:</strong> exact date, or <em>Rolling</em> if none listed.</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80a1-b5ef-c94a77971e70" class="bulleted-list"><li style="list-style-type:disc"><strong>Max Funding:</strong> number + currency, or <em>Not stated</em>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80b3-be6c-d622b1ac47b2" class="bulleted-list"><li style="list-style-type:disc"><strong>IP Risk:</strong> always start as <em>Unknown</em>. Do not decide this yourself.</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80b4-b974-f27425fb59ab" class="bulleted-list"><li style="list-style-type:disc"><strong>Notes:</strong> factual information only.</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8036-82de-c7e4d075bd93" class="bulleted-list"><li style="list-style-type:disc"><strong>Next Action:</strong> e.g. <em>Await instruction</em>, <em>Draft requested</em>.</li></ul></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-809a-a9b2-c464d16187ae" class="">Precision here is essential.</p></div><div style="display:contents" dir="auto"><hr id="2e1c5e6f-95bd-80a9-b6db-edad4cb15709"/></div><div style="display:contents" dir="auto"><h1 id="2e1c5e6f-95bd-80dd-8320-e66dcc983dde" class=""><strong>PART 4 — WEEKLY PORTAL CHECKS</strong></h1></div><div style="display:contents" dir="auto"><h3 id="2e1c5e6f-95bd-80d5-b8f2-e4befd1ad72b" class=""><strong>Websites to check</strong></h3></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-8049-b2d3-d1d19ddcdf25" class="">Please check <strong>only</strong> the following sites:</p></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8061-8dd7-d58ff65a153c" class="bulleted-list"><li style="list-style-type:disc">grants.gov.au</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80ad-9806-cf39868b37e5" class="bulleted-list"><li style="list-style-type:disc">business.gov.au</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80df-9e7d-f2a2cbe9ac80" class="bulleted-list"><li style="list-style-type:disc">EU Funding &amp; Tenders Portal</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80c9-a98b-de301dd3f611" class="bulleted-list"><li style="list-style-type:disc">Innovate UK competitions</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80be-a6eb-d075fed91175" class="bulleted-list"><li style="list-style-type:disc">Innovation Canada</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8042-9c7c-f2d52f1cf56a" class="bulleted-list"><li style="list-style-type:disc">Enterprise Singapore</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8027-95a3-fb401e861b2a" class="bulleted-list"><li style="list-style-type:disc">ADIO (UAE)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80bc-9295-c29b10290b8d" class="bulleted-list"><li style="list-style-type:disc">Dubai Future Foundation</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8032-9b32-e3cb23d84b1e" class="bulleted-list"><li style="list-style-type:disc">AusTender</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-805a-984a-dfb05b3a9713" class="bulleted-list"><li style="list-style-type:disc">TED (EU tenders)</li></ul></div><div style="display:contents" dir="auto"><hr id="2e1c5e6f-95bd-8066-81d4-e3cc17a0902b"/></div><div style="display:contents" dir="auto"><h3 id="2e1c5e6f-95bd-802a-b056-eda9263a9782" class=""><strong>How to check each portal</strong></h3></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-8091-8c0f-cd947a703cac" class="">For each site:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e1c5e6f-95bd-803c-802f-dc471de27226" class="numbered-list" start="1"><li>Open the website</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e1c5e6f-95bd-80e1-9398-fef75252f52d" class="numbered-list" start="2"><li>Search using only these keywords:<div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80c1-ba61-f2ced3b692fe" class="bulleted-list"><li style="list-style-type:disc">digital</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80c3-b0fe-e510bd8ec142" class="bulleted-list"><li style="list-style-type:disc">governance</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80c5-8859-ea3a3867f072" class="bulleted-list"><li style="list-style-type:disc">decision</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8077-9d51-e3a4b32696c7" class="bulleted-list"><li style="list-style-type:disc">policy</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-809d-9eb0-ff2d2e2df5c9" class="bulleted-list"><li style="list-style-type:disc">infrastructure</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8032-82de-fe2c02e5631d" class="bulleted-list"><li style="list-style-type:disc">AI</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e1c5e6f-95bd-80c3-8d7e-c186b9e87043" class="numbered-list" start="3"><li>If something appears relevant:<div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80d0-bd89-c5ae874e1a73" class="bulleted-list"><li style="list-style-type:disc">open it</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80e2-a180-f95680e7c45a" class="bulleted-list"><li style="list-style-type:disc">copy details into the tracker</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e1c5e6f-95bd-802f-9780-cb3494ad661e" class="numbered-list" start="4"><li>Do not decide if it is suitable</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e1c5e6f-95bd-808b-ae2b-c2d91a71cdae" class="numbered-list" start="5"><li>Do not discard opportunities on your own</li></ol></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-8089-95ff-dd7559291e4a" class="">Flag rather than filter.</p></div><div style="display:contents" dir="auto"><hr id="2e1c5e6f-95bd-8056-85ef-f6a6aa69a56d"/></div><div style="display:contents" dir="auto"><h1 id="2e1c5e6f-95bd-8070-979e-f27891c6b92a" class=""><strong>PART 5 — DRAFT PREPARATION</strong></h1></div><div style="display:contents" dir="auto"><h3 id="2e1c5e6f-95bd-8044-80f8-ca06d684c282" class=""><strong>When drafting is requested</strong></h3></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-80a4-953b-f48aa26db42a" class="">You will be told:</p></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80e9-86c8-d9ed976c3264" class="bulleted-list"><li style="list-style-type:disc">which funder</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8001-9e0c-f17be7cd96c8" class="bulleted-list"><li style="list-style-type:disc">which workstream (WS-#)</li></ul></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-80fd-a71d-e5b6467fa1fb" class="">Please do not choose these yourself.</p></div><div style="display:contents" dir="auto"><hr id="2e1c5e6f-95bd-801d-92bd-fd5eaa67de2c"/></div><div style="display:contents" dir="auto"><h3 id="2e1c5e6f-95bd-80eb-b526-cc5ba8f5f68d" class=""><strong>Drafting steps</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="2e1c5e6f-95bd-8000-9660-c26f4ba47614" class="numbered-list" start="1"><li>Copy the Master Dossier</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e1c5e6f-95bd-8055-b171-cff39dbb7e17" class="numbered-list" start="2"><li>Rename the file:<div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-8017-98f0-d07ea7575548" class="">AMOS_[FUNDER NAME]_WS[#]_DRAFT</p></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e1c5e6f-95bd-8018-b7fc-c5136f4f9980" class="numbered-list" start="3"><li>Edit <strong>only</strong> the following sections:<div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8050-8107-d6b978a78ec3" class="bulleted-list"><li style="list-style-type:disc">Section 1</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-802e-89d1-d7684a3c7c1a" class="bulleted-list"><li style="list-style-type:disc">Section 4</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80da-8ffe-f7bffedff487" class="bulleted-list"><li style="list-style-type:disc">Section 9</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-806d-9dd2-fea9b60f3b75" class="bulleted-list"><li style="list-style-type:disc">Section 10</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-802c-89ce-c0a284ac2a68" class="bulleted-list"><li style="list-style-type:disc">Section 11</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e1c5e6f-95bd-8067-bd1d-e16cd2d70a52" class="numbered-list" start="4"><li>Fill placeholders only</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e1c5e6f-95bd-80fa-9bb4-df79574d5145" class="numbered-list" start="5"><li>Do not change sentence structure</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e1c5e6f-95bd-8031-aa4a-c27e0133c3fd" class="numbered-list" start="6"><li>Highlight unclear requirements in yellow</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e1c5e6f-95bd-80e0-985b-cd9fdff5325d" class="numbered-list" start="7"><li>Save and stop</li></ol></div><div style="display:contents" dir="auto"><hr id="2e1c5e6f-95bd-8062-90d9-e5a06f451ced"/></div><div style="display:contents" dir="auto"><h1 id="2e1c5e6f-95bd-8005-b80b-e84914dbd974" class=""><strong>PART 6 — IP &amp; LEGAL HANDLING (VERY IMPORTANT)</strong></h1></div><div style="display:contents" dir="auto"><h3 id="2e1c5e6f-95bd-8084-9c71-eb6a434ac71d" class=""><strong>What to extract every time</strong></h3></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-8011-af9a-c6a95b70b0bd" class="">From each funding call, please copy <strong>word-for-word</strong> any text relating to:</p></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80d5-9c02-fb609a426165" class="bulleted-list"><li style="list-style-type:disc">Background IP</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-809c-aed7-e30154f337a9" class="bulleted-list"><li style="list-style-type:disc">Foreground IP</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8084-a082-d5270f15cabf" class="bulleted-list"><li style="list-style-type:disc">Ownership</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80b0-8654-d8798cd7292b" class="bulleted-list"><li style="list-style-type:disc">Licence</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-809a-887d-ea10a5b658a9" class="bulleted-list"><li style="list-style-type:disc">Open source</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-808c-bb31-f3500548d1d6" class="bulleted-list"><li style="list-style-type:disc">Disclosure</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-805e-973f-ccdfcb76cd0b" class="bulleted-list"><li style="list-style-type:disc">Derivative works</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-806b-9b64-c130bdb8cf5a" class="bulleted-list"><li style="list-style-type:disc">Exclusivity</li></ul></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-8094-8312-e900c61fcf9c" class="">Save this in AMOS_Contracts_IP/.</p></div><div style="display:contents" dir="auto"><hr id="2e1c5e6f-95bd-8012-8c27-ea029bfeba1e"/></div><div style="display:contents" dir="auto"><h3 id="2e1c5e6f-95bd-80d8-b0c2-ca4eb142723d" class=""><strong>Stop-and-flag terms</strong></h3></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-801b-a826-caeefb3c4043" class="">If you see any of the following phrases, please stop and flag immediately:</p></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80ce-acd2-cd0ac3c0ebb3" class="bulleted-list"><li style="list-style-type:disc">“must open source”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80b6-b43b-c871a40aff5e" class="bulleted-list"><li style="list-style-type:disc">“exclusive licence”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80f4-8bd0-d8d980089f06" class="bulleted-list"><li style="list-style-type:disc">“joint ownership”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80e2-b581-fb25a3c14780" class="bulleted-list"><li style="list-style-type:disc">“source code”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8075-ab0c-ef58a00b5cf7" class="bulleted-list"><li style="list-style-type:disc">“escrow”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-804c-a634-e172f9bfb459" class="bulleted-list"><li style="list-style-type:disc">“transfer of IP”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-805d-901a-db1a09fb0ebb" class="bulleted-list"><li style="list-style-type:disc">“government owns”</li></ul></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-80fa-9706-e7e14affac8c" class="">You do not need to interpret them — just flag them.</p></div><div style="display:contents" dir="auto"><hr id="2e1c5e6f-95bd-80f1-b83b-d47ab5f7e92c"/></div><div style="display:contents" dir="auto"><h1 id="2e1c5e6f-95bd-808a-923f-fee698746e2b" class=""><strong>PART 7 — COMMUNICATION</strong></h1></div><div style="display:contents" dir="auto"><h3 id="2e1c5e6f-95bd-8099-b00c-c02dcd0e97fe" class=""><strong>Emails you may prepare (with approval)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8020-b719-c3ca38f844f6" class="bulleted-list"><li style="list-style-type:disc">asking for deadlines</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-802b-8ed8-e4645e07b40f" class="bulleted-list"><li style="list-style-type:disc">requesting application links</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-809c-9d78-c6abf8bd2437" class="bulleted-list"><li style="list-style-type:disc">requesting templates</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e1c5e6f-95bd-806c-9094-eeb8543aa8ed" class=""><strong>Emails you may not prepare</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-805a-b3f4-ceea68644c7a" class="bulleted-list"><li style="list-style-type:disc">explaining the project</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-805a-8f1a-c35a1961ec51" class="bulleted-list"><li style="list-style-type:disc">discussing scope or capability</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80ba-ab23-d6e2b1b7341d" class="bulleted-list"><li style="list-style-type:disc">discussing IP or ownership</li></ul></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-80e4-8c81-e1a350129eef" class="">All emails must be approved before sending.</p></div><div style="display:contents" dir="auto"><hr id="2e1c5e6f-95bd-8063-abce-c1cf17cf93ab"/></div><div style="display:contents" dir="auto"><h1 id="2e1c5e6f-95bd-8027-ae40-c3bcee110a37" class=""><strong>PART 8 — WEEKLY STATUS UPDATE</strong></h1></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-8029-8c9d-f13dcdad1852" class="">Please send a short weekly update including:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e1c5e6f-95bd-8079-a254-fa07dd8851d8" class="numbered-list" start="1"><li>New opportunities added</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e1c5e6f-95bd-8042-87f3-d2b481a22a0f" class="numbered-list" start="2"><li>Deadlines in the next 60 days</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e1c5e6f-95bd-8027-b994-ffaadb5bd5df" class="numbered-list" start="3"><li>Drafts in progress</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e1c5e6f-95bd-802d-95de-e7822441cc55" class="numbered-list" start="4"><li>IP clauses flagged</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e1c5e6f-95bd-8074-b707-d447669168e5" class="numbered-list" start="5"><li>Questions needing clarification</li></ol></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-808b-b550-ef5a34dc67ef" class="">No opinions or recommendations are required.</p></div><div style="display:contents" dir="auto"><hr id="2e1c5e6f-95bd-8039-bb30-c22ac0aec1ed"/></div><div style="display:contents" dir="auto"><h1 id="2e1c5e6f-95bd-803c-93ff-e8cd529015fb" class=""><strong>PART 9 — IF SOMETHING GOES WRONG</strong></h1></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-801f-9bba-d810cd0f3c4e" class="bulleted-list"><li style="list-style-type:disc">If you are unsure: pause and ask</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80c7-81c6-da5c00d15660" class="bulleted-list"><li style="list-style-type:disc">If a funder contacts you: forward the message, do not reply</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8056-974e-ff44a2e6d853" class="bulleted-list"><li style="list-style-type:disc">If you make a mistake: flag it early</li></ul></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-80aa-81cb-e856b4ee58d1" class="">Early visibility is always preferred.</p></div><div style="display:contents" dir="auto"><hr id="2e1c5e6f-95bd-80a2-b0e9-d2ed97dcda90"/></div><div style="display:contents" dir="auto"><h1 id="2e1c5e6f-95bd-8005-9c15-c6c57ada1866" class=""><strong>PART 10 — WHAT GOOD PERFORMANCE LOOKS LIKE</strong></h1></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-809c-b258-f09900e5eb16" class="">You are doing well if:</p></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-809d-af2c-e318deab5054" class="bulleted-list"><li style="list-style-type:disc">tasks are completed on time</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80ac-919f-e7e74e8aff7e" class="bulleted-list"><li style="list-style-type:disc">information is accurate</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-804d-bf5b-f0b1dd907b90" class="bulleted-list"><li style="list-style-type:disc">nothing important is missed</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-8083-a93d-ff9e24a156e9" class="bulleted-list"><li style="list-style-type:disc">work does not need to be redone</li></ul></div><div style="display:contents" dir="auto"><ul id="2e1c5e6f-95bd-80d2-906e-fe98fbf2ab57" class="bulleted-list"><li style="list-style-type:disc">communication is clear</li></ul></div><div style="display:contents" dir="auto"><p id="2e1c5e6f-95bd-806c-9db3-fbb9921af480" class="">That is the standard.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
