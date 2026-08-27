---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>AU Gov Funding — Ultra-Detailed To-Do List</title><style>
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
	
</style></head><body><article id="2e2c5e6f-95bd-80c3-85de-d5294388ad34" class="page sans"><header><h1 class="page-title" dir="auto"><strong>AU Gov Funding — Ultra-Detailed To-Do List</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80d2-a179-e9be6295ecb8" class=""><strong>Phase 0 — Foundation (Day 1–3)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80e4-bf16-c109117284dd" class=""><strong>0.1 Set up your “Grant Ops” system (1–2 hours)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8051-839f-e8d413beff20" class="bulleted-list"><li style="list-style-type:disc">Create a folder structure (or Notion) with:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b1-9dac-c3d83030882b" class="bulleted-list"><li style="list-style-type:circle"><strong>01_Core_Decks</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80bb-b3fb-ecd3b5d80e33" class="bulleted-list"><li style="list-style-type:circle"><strong>02_CVs</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80bc-9ba3-cca096895ceb" class="bulleted-list"><li style="list-style-type:circle"><strong>03_Budgets</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80eb-bf24-dd6895026497" class="bulleted-list"><li style="list-style-type:circle"><strong>04_Risk_Compliance</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8081-92d1-ffa2f281d83d" class="bulleted-list"><li style="list-style-type:circle"><strong>05_Applications</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8045-8c1e-dbe9e2efd14f" class="bulleted-list"><li style="list-style-type:circle"><strong>06_Evidence</strong></li></ul></div><div style="display:contents" dir="auto"><ul i
d="2e2c5e6f-95bd-801b-8a36-d93e0eba034f" class="bulleted-list"><li style="list-style-type:circle"><strong>07_Partners</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8046-984b-f7cafe35b04d" class="bulleted-list"><li style="list-style-type:circle"><strong>08_Submissions_Tracking</strong></li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-800c-8ddb-ff98fb2fd687" class="bulleted-list"><li style="list-style-type:disc">Create a <strong>Grant Tracker table</strong> (Google Sheet/Notion):<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ce-ad11-f50c256f5fde" class="bulleted-list"><li style="list-style-type:circle">Grant Name</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8009-bfde-d0446362db21" class="bulleted-list"><li style="list-style-type:circle">Level (Federal/State/Local/Uni)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80dd-9867-c20c906ae0af" class="bulleted-list"><li style="list-style-type:circle">Opening/Closing</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8041-9022-fc7811dd4cf0" class="bulleted-list"><li style="list-style-type:circle">Eligibility gate(s)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e1-b27e-ce750f588505" class="bulleted-list"><li style="list-style-type:circle">Max funding</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-803f-a1a3-d72b712fa6f6" class="bulleted-list"><li style="list-style-type:circle">Match funding required? 
(Y/N)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8087-b727-cfbb002e22b9" class="bulleted-list"><li style="list-style-type:circle">TRL stage expected</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8036-994e-d4fe58f7e8dd" class="bulleted-list"><li style="list-style-type:circle">Partner required (Y/N)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8092-ae45-c303b1dbf220" class="bulleted-list"><li style="list-style-type:circle">Contact person</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8005-a80e-c1f1726d46e4" class="bulleted-list"><li style="list-style-type:circle">Status (Watch / Draft / Submitted / Won / Lost)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8060-959f-c4b2c209fdfa" class="bulleted-list"><li style="list-style-type:circle">Notes + feedback log</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8018-a040-ca2cff20ad59" class=""><strong>Done =</strong> you can list 10 grants and track them without chaos.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8080-a3f4-f449667f2376"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80d8-aa3e-d6c505b6d8d9" class=""><strong>Phase 1 — Eligibility &amp; 
compliance (Day 1–5)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8026-9acc-d4bc33748917" class=""><strong>1.1 Confirm entity readiness (30–60 mins)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8023-8799-f80a6f74731c" class="bulleted-list"><li style="list-style-type:disc">Confirm you have <strong>ABN</strong> (and ACN if company)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8021-bfba-f08ce1d975d2" class="bulleted-list"><li style="list-style-type:disc">Confirm director details correct</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8095-87eb-e30729c0933e" class="bulleted-list"><li style="list-style-type:disc">Confirm business address and contact email stable</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e4-bc91-e2941ca32456" class="bulleted-list"><li style="list-style-type:disc">Confirm bank account is business-compatible for receipts</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-807f-9c28-e7359d06bd9e" class=""><strong>Done =</strong> you can receive grant funds legally.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80ba-9885-e816d1e5f220" class=""><strong>1.2 Government access setup (30–90 mins)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-804e-a793-d6a42f14dbb7" class="bulleted-list"><li style="list-style-type:disc">MyGovID active</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-805d-b1a9-d630adca4f37" class="bulleted-list"><li style="list-style-type:disc">RAM (Relationship Authorisation Manager) access (if company)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8011-9ae4-c7f003e28b12" class="bulleted-list"><li style="list-style-type:disc">GrantConnect account created</li></ul></div><div style="display:contents" dir="auto"><p i
d="2e2c5e6f-95bd-80f8-a6a5-cdb87749b8eb" class=""><strong>Done =</strong> you can submit without last-minute access failure.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8019-b7cd-c5b9702f35fd" class=""><strong>1.3 Build the “eligibility story” (1 page)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a1-865e-db414a768eac" class="bulleted-list"><li style="list-style-type:disc">One page: <strong>Who you are + what entity is applying</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8085-af5f-c203fe5c1390" class="bulleted-list"><li style="list-style-type:disc">One sentence: “This project is delivered by X entity; IP owned by Y; 
partners Z if needed.”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8041-a005-d1354d6e716a" class="bulleted-list"><li style="list-style-type:disc">Clarify:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-807f-9461-e3629633955f" class="bulleted-list"><li style="list-style-type:circle">IP ownership (you/company)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ee-9de9-eb4b64ddc1d0" class="bulleted-list"><li style="list-style-type:circle">Any prior funding (if none: say none)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8092-969d-d56e145ab9b7" class="bulleted-list"><li style="list-style-type:circle">Any conflicts (if none: say none)</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80e2-b08d-debb5ee55132" class=""><strong>Done =</strong> you can paste this into any application.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-803f-9cec-c3c73525f16e"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80bc-8130-cafe1c9d0c73" class=""><strong>Phase 2 — Core application pack (Day 3–10)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80f0-838b-cda0ec8656f9" class="">You will reuse these 80% across all grants.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8065-a084-c0669b0b709a" class=""><strong>2.1 Create “Grant-Safe Executive Summary” (1 page)</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80f1-8242-ede4c1ae4836" class="">Must include:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8038-afcd-de3a501f1ff6" class="bulleted-list"><li style="list-style-type:disc">Problem (public-sector phrasing, 
not startup hype)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8004-aae5-f5870a90c9d0" class="bulleted-list"><li style="list-style-type:disc">Solution (what you built, what will be built next)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ae-b1f6-e283d6efc6ed" class="bulleted-list"><li style="list-style-type:disc">Who benefits (citizens, SMEs, infrastructure, 
government)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b0-bcc1-caf88a32e3d9" class="bulleted-list"><li style="list-style-type:disc">Why now (policy / risk / capability gap)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8086-b0c0-dacb170f4c68" class="bulleted-list"><li style="list-style-type:disc">Outcomes in 6 months</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80bb-addc-d9e8ddf95262" class="bulleted-list"><li style="list-style-type:disc">Outcomes in 12 months</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8082-bf87-e9cc1097c603" class="bulleted-list"><li style="list-style-type:disc">Risks + mitigation (3 bullets)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-809a-8b39-d72e369a9cc9" class="bulleted-list"><li style="list-style-type:disc">Budget request range (ballpark)</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80e6-a9f3-f56dd04b35f1" class=""><strong>Done =</strong> 1 page that can be copy-pasted anywhere.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-809a-854f-ceeeb10e85bd" class=""><strong>2.2 Create “2–3 page Technical Plan”</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-800f-bcf0-ff3336856a5c" class="bulleted-list"><li style="list-style-type:disc">Architecture summary (non-sensitive)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80df-b4ae-e36fb9bfaa46" class="bulleted-list"><li style="list-style-type:disc">Delivery approach (phased)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c8-b7b3-cb786f3d3cfd" class="bulleted-list"><li style="list-style-type:disc">Milestones (M1–M6)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-806a-8d0b-c84940c8c8b1" class="bulleted-list"><li style="list-style-type:disc">Acceptance c
riteria (what success looks like)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c0-9366-f947cc7b6d2d" class="bulleted-list"><li style="list-style-type:disc">Security posture summary (high-level)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80de-85b9-f206be025fb8" class="bulleted-list"><li style="list-style-type:disc">Governance: audit logs / traceability / human-in-loop (if relevant)</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-802e-bb97-fbf69784a8a0" class=""><strong>Done =</strong> a panel can see “low execution risk.”</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-801a-9ac0-ffba7ebb092f" class=""><strong>2.3 Create “Risk &amp; 
Governance Sheet” (1 page)</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-807b-be8a-e422876af7cb" class="">Include:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8057-bc35-fc494c78e945" class="bulleted-list"><li style="list-style-type:disc">Risk register table (5–8 risks)<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-807b-a0f1-cc3215c84cfa" class="bulleted-list"><li style="list-style-type:circle">Technical risk</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d8-8ec7-d0a36727c5f5" class="bulleted-list"><li style="list-style-type:circle">Delivery risk</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-800c-8bfd-cc9bdf7a0784" class="bulleted-list"><li style="list-style-type:circle">Partner risk</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d0-b9f1-c0297e17ddb4" class="bulleted-list"><li style="list-style-type:circle">Compliance risk</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8030-8677-fb4f6dbd25a9" class="bulleted-list"><li style="list-style-type:circle">Data/privacy risk</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80cd-b6f0-fd85c06a1901" class="bulleted-list"><li style="list-style-type:circle">Reputational risk</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8057-be5d-c56c310ed359" class="bulleted-list"><li style="list-style-type:disc">Controls / mitigations per risk</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c6-b48b-e37c019d37c8" class="bulleted-list"><li style="list-style-type:disc">Ethics &amp; 
safety boundary (“what system will NOT do”)</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8007-9830-df5d8d067348" class=""><strong>Done =</strong> you look safe to fund.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-802c-b412-e11de0b0bf80" class=""><strong>2.4 Create “Budget Template” (spreadsheet)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b8-9b02-db43675c3d97" class="bulleted-list"><li style="list-style-type:disc">Direct labour (hours x rate)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80fd-a615-d0ea516842ae" class="bulleted-list"><li style="list-style-type:disc">Contractors (if any)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8015-9e48-c4479001f8f4" class="bulleted-list"><li style="list-style-type:disc">Cloud costs</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c8-a8e0-ca39da9eac70" class="bulleted-list"><li style="list-style-type:disc">Tools/licenses</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80be-863b-f910ef0f40b8" class="bulleted-list"><li style="list-style-type:disc">Travel (if needed)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80aa-9fda-c66f42d2758b" class="bulleted-list"><li style="list-style-type:disc">Evaluation (independent reviewer, if required)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8073-84b5-e8f71c01fb67" class="bulleted-list"><li style="list-style-type:disc">Overheads allowed? 
(varies by grant)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e9-b719-cc7c7cc2613f" class="bulleted-list"><li style="list-style-type:disc">In-kind contributions</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8088-a2f1-dbb775ea1c2b" class="bulleted-list"><li style="list-style-type:disc">Match funding if required</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-804c-88a6-cefdc3d1714e" class=""><strong>Done =</strong> you can generate a budget for any grant in &lt;30 mins.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80b6-87e1-c855b005c36e" class=""><strong>2.5 Create two CV versions (VERY important)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8047-b5a2-fd07fb91b64b" class="bulleted-list"><li style="list-style-type:disc"><strong>Government CV</strong> (2 pages max):<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8039-9dec-f358438c11e8" class="bulleted-list"><li style="list-style-type:circle">delivery, risk, governance, 
outcomes</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c9-acea-fac3b32c1ad7" class="bulleted-list"><li style="list-style-type:circle">remove hype words</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-808e-b44b-eb5e0ff75d28" class="bulleted-list"><li style="list-style-type:disc"><strong>Industry CV</strong> (2–3 pages):<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-809f-a966-fba070e56ab1" class="bulleted-list"><li style="list-style-type:circle">achievements + commercial impact</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80d0-9b1c-f87f8850101a" class=""><strong>Done =</strong> you never scramble for “format fit.”</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-809b-9dcf-f10cad2eec15"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-802a-818d-c69749e810a9" class=""><strong>Phase 3 — Evidence pack (Day 5–14)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8035-9b00-d2cf4329bd8c" class="">Panels fund evidence, 
not claims.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8007-87cf-fce36c88d191" class=""><strong>3.1 Build “Proof of Capability” bundle (PDF)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-805d-8dc5-ee6919317326" class="bulleted-list"><li style="list-style-type:disc">1 page: portfolio snapshot (3–5 projects)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80bb-851d-d20ca6a67b10" class="bulleted-list"><li style="list-style-type:disc">1 page: metrics (cost/time/outcomes)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8039-9a55-fc084299f736" class="bulleted-list"><li style="list-style-type:disc">screenshots (non-sensitive)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8029-bfd9-d955f903b739" class="bulleted-list"><li style="list-style-type:disc">architecture diagram (high level)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80cf-bedc-d56f8904e827" class="bulleted-list"><li style="list-style-type:disc">reference letters / testimonials if available (even 1 helps)</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80ee-94d8-e8faeafc6383" class=""><strong>Done =</strong> credibility in one file.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8022-b2a4-d468751847c4" class=""><strong>3.2 Create “Pilot Readiness” checklist</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8022-b12b-f3e13a9ddb26" class="bulleted-list"><li style="list-style-type:disc">Pilot use case defined (one narrow scope)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ad-8d79-e167244768d9" class="bulleted-list"><li style="list-style-type:disc">Data inputs defined (dummy or real)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e0-975d-c275570237f0" class="bulleted-list"><li s
tyle="list-style-type:disc">Hosting plan (where it runs)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8082-ba55-c4676d386e4c" class="bulleted-list"><li style="list-style-type:disc">Security controls for pilot (access, 
logs)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ee-868a-e84f451c5522" class="bulleted-list"><li style="list-style-type:disc">Who the pilot user is (agency/council/university/SME)</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80f6-b005-cbd268ad8827" class=""><strong>Done =</strong> you can say “ready to pilot in 8–12 weeks.”</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8041-a549-f48200502e45"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80d4-8d2a-e8f1dcfdbf6f" class=""><strong>Phase 4 — Grant hunting workflow (Week 2 onwards)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-809a-a8be-eecaecfd232c" class=""><strong>4.1 Federal: GrantConnect weekly routine (30 mins/week)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-802e-add5-e48c146b0573" class="bulleted-list"><li style="list-style-type:disc">Set alerts for keywords:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8040-9030-dabc97b8e31f" class="bulleted-list"><li style="list-style-type:circle">“innovation”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8024-a2e6-c1e17615ef99" class="bulleted-list"><li style="list-style-type:circle">“digital”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8099-b60c-de68a33c10b9" class="bulleted-list"><li style="list-style-type:circle">“artificial intelligence”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-804e-bad5-c30d67d8af48" class="bulleted-list"><li style="list-style-type:circle">“cyber”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c7-b37a-c58b61e3ead0" class="bulleted-list"><li style="list-style-type:circle">“infrastructure”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8042-b42f-f803d60a60a1" class="bulleted-list"><li s
tyle="list-style-type:circle">“energy”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d5-912c-f5f8379dc13e" class="bulleted-list"><li style="list-style-type:circle">“transport”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ab-b9cd-dcf2967cf727" class="bulleted-list"><li style="list-style-type:circle">“research translation”</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8052-9bdb-c7198f782f19" class="bulleted-list"><li style="list-style-type:disc">Every Monday:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8083-92de-de99ab70834c" class="bulleted-list"><li style="list-style-type:circle">add new relevant grants to tracker</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8060-9429-ff837864a758" class="bulleted-list"><li style="list-style-type:circle">mark closing dates</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-808e-86a9-e210d8d1c46f" class="bulleted-list"><li style="list-style-type:circle">record eligibility gates</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8049-9ed0-e450428d3cff" class=""><strong>Done =</strong> you never miss a round.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8009-9558-d03670d35925" class=""><strong>4.2 business.gov.au Finder (1–2 hours once)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8003-b961-cd1cc2560be6" class="bulleted-list"><li style="list-style-type:disc">Run the finder</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b9-95ff-fe56829e054b" class="bulleted-list"><li style="list-style-type:disc">Export list into tracker</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8000-81b2-d5b6da01930d" class="bulleted-list"><li style="list-style-type:disc">Filter out irrelevant ones f
ast:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a5-874a-cc3c7c1c4442" class="bulleted-list"><li style="list-style-type:circle">location restrictions</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-807b-9f10-dc4dcc136b56" class="bulleted-list"><li style="list-style-type:circle">company-size caps</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80db-93ed-d6bf4d539f79" class="bulleted-list"><li style="list-style-type:circle">sector mismatch</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-802d-ae1a-cf8fdd16ac90" class=""><strong>Done =</strong> you have a shortlist.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8081-8fce-e89c5e94a196" class=""><strong>4.3 State grants (pick your state)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8037-addd-f295aa08bc30" class="bulleted-list"><li style="list-style-type:disc">Identify your state’s:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-809c-b17d-ff394872bcd2" class="bulleted-list"><li style="list-style-type:circle">innovation department site</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8035-8fc5-dbad5555bdb4" class="bulleted-list"><li style="list-style-type:circle">“business grants” portal</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8025-837c-e72e15806940" class="bulleted-list"><li style="list-style-type:circle">digital / cyber unit programs</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a9-a871-e35bac58b3d6" class="bulleted-list"><li style="list-style-type:disc">Add 5–10 to tracker</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8016-a6e2-e0e264edf78b" class=""><strong>Done =</strong> state pipeline ready.</p></div><div style="display:contents" dir="auto"><h3 i
d="2e2c5e6f-95bd-80fd-a6fd-f4187a630ca3" class=""><strong>4.4 Local / council grants (easier wins)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8004-8007-c8d7a4d570a1" class="bulleted-list"><li style="list-style-type:disc">Identify:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-808d-9cd7-e4a35e4dcc7a" class="bulleted-list"><li style="list-style-type:circle">local council innovation grants</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-801a-ac37-fc4e7cd40bf3" class="bulleted-list"><li style="list-style-type:circle">regional development authority programs</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-800d-967b-f3787291dae1" class="bulleted-list"><li style="list-style-type:circle">innovation vouchers</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-803a-9b6e-f257a0275144" class="bulleted-list"><li style="list-style-type:disc">Add 3–6 to tracker</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-808b-887a-e6b21b4ebf52" class=""><strong>Done =</strong> high probability pilot cash.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-806e-8016-e4bc50c99ad3"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-807f-988c-cf9c45e40843" class=""><strong>Phase 5 — Application strategy (critical)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80e0-ad8f-cb7470cd5ead" class=""><strong>5.1 Choose your “Grant Stack” (do not spray)</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-806e-b5a6-dd623e1f28f4" class="">Pick:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-801c-a4f6-fc6b40f2aef6" class="bulleted-list"><li style="list-style-type:disc">2 local/state “easy wins” (pilot-friendly)</li></ul></div><div style="display:contents" dir="auto"><ul i
d="2e2c5e6f-95bd-80fa-baff-cde332051cde" class="bulleted-list"><li style="list-style-type:disc">1 state flagship</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8080-8730-f62cb36793e6" class="bulleted-list"><li style="list-style-type:disc">1 federal mid-tier (not AEA yet)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f2-bc91-eec8a9438935" class="bulleted-list"><li style="list-style-type:disc">R&amp;D Tax Incentive setup in parallel</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80df-a842-c9fba0ba2380" class=""><strong>Done =</strong> focused pipeline.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8026-9136-e0799e356b98" class=""><strong>5.2 Pre-submission calls (increase win rate)</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8026-90eb-c6d03f6f5648" class="">Before applying:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8054-a9d9-dbe4cb2d7741" class="bulleted-list"><li style="list-style-type:disc">email/call program officer with:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-804c-9ea3-d5b56f384f1b" class="bulleted-list"><li style="list-style-type:circle">5 sentence pitch</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8038-a794-f46808d97555" class="bulleted-list"><li style="list-style-type:circle">1 page exec summary</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-800c-8969-c0f1b921b36a" class="bulleted-list"><li style="list-style-type:circle">3 questions about eligibility</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-804b-ad96-ed217d6bf054" class="bulleted-list"><li style="list-style-type:disc">log answers in tracker</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-804b-aaac-f22e1b4a0586" class=""><strong>Done =</strong> you avoid d
isqualifying mistakes.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80c1-9f94-f941073441c9"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8055-9425-c4671cfd2fcf" class=""><strong>Phase 6 — Submission execution (per grant)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80d0-9dfd-eac82f8ca804" class=""><strong>6.1 Create an application checklist per grant</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ee-82b1-fafad2a243b9" class="bulleted-list"><li style="list-style-type:disc">Eligibility gates checked</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-802b-b107-da2888938c2c" class="bulleted-list"><li style="list-style-type:disc">Word count compliance</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d1-9a02-d6076ea9184c" class="bulleted-list"><li style="list-style-type:disc">Budget format compliance</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a7-b621-fae798d7eedb" class="bulleted-list"><li style="list-style-type:disc">Attachments correct format</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8079-9ace-c9d9be4b4239" class="bulleted-list"><li style="list-style-type:disc">Partner letters included (if required)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b0-ac10-c1d1a2fef2c6" class="bulleted-list"><li style="list-style-type:disc">Internal review pass (you read it once as assessor)</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8068-8f8e-ce96e4e15523" class=""><strong>Done =</strong> submission quality control.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80b3-80dc-e059e85a06ba" class=""><strong>6.2 Write to scoring criteria (not your story)</strong></h3></div><div style="display:contents" dir="auto"><ul i
d="2e2c5e6f-95bd-80c7-bc20-d2c517c32e57" class="bulleted-list"><li style="list-style-type:disc">Copy each criterion into doc</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d8-8b98-ee86b8a76ab4" class="bulleted-list"><li style="list-style-type:disc">Answer directly</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-809b-9ef4-e496bc0b5064" class="bulleted-list"><li style="list-style-type:disc">Use evidence</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80be-885b-f6de7af8311b" class="bulleted-list"><li style="list-style-type:disc">Use metrics</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ff-b658-e6a49721d608" class="bulleted-list"><li style="list-style-type:disc">Use risk mitigation language</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80f3-b45f-ddeef2aceb65" class=""><strong>Done =</strong> assessor can score easily.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8052-b0b8-c664ad484911"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8061-9f48-d21191fbf303" class=""><strong>Phase 7 — Partnership path (if you want AEA later)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80d8-bb54-e38a3a3f55e8" class=""><strong>7.1 University partner plan (Month 1–3)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f3-bcc6-da0598878d54" class="bulleted-list"><li style="list-style-type:disc">Identify 3 universities + 1 centre each (cyber/AI/infra)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8065-b208-d52ea84cc56c" class="bulleted-list"><li style="list-style-type:disc">Contact:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8018-9dfe-c13d67cdff40" class="bulleted-list"><li style="list-style-type:circle">Industry engagement office</li></ul></div><div s
tyle="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8056-be18-d6092203305c" class="bulleted-list"><li style="list-style-type:circle">Research translation office</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8030-b75e-fee2623640bc" class="bulleted-list"><li style="list-style-type:disc">Ask for:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-801f-b4a1-e13ec8e56528" class="bulleted-list"><li style="list-style-type:circle">pilot collaboration</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8069-ac6f-e8455d8a431e" class="bulleted-list"><li style="list-style-type:circle">letter of support</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8059-a4d9-d16d12c6029e" class="bulleted-list"><li style="list-style-type:circle">pathway to AEA Ignite</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8057-8a72-c1c6b1fa3d64" class=""><strong>Done =</strong> you unlock bigger money.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8009-9b65-e3f54cdfc75e"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8039-b354-e3e22429fc75" class=""><strong>Phase 8 — R&amp;D Tax Incentive (parallel, 
Month 1 onwards)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8048-84da-fa6dcab477ac" class=""><strong>8.1 Recordkeeping (weekly)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e5-b890-ca5c11c28fac" class="bulleted-list"><li style="list-style-type:disc">hypothesis/technical uncertainty log</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8043-a3c3-f33cc17f6ce6" class="bulleted-list"><li style="list-style-type:disc">experiment log</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b7-9bdc-f3bdec9ffb65" class="bulleted-list"><li style="list-style-type:disc">code commits + notes</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8069-9eac-e26a27445115" class="bulleted-list"><li style="list-style-type:disc">time tracking</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-809b-87cc-fa3b13910b18" class="bulleted-list"><li style="list-style-type:disc">expenses tagged “R&amp;D”</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8008-9de5-d641ff7c7e9c" class=""><strong>Done =</strong> you can claim properly.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80e1-8f65-d3f2f538616a"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-8021-9647-f59d1020e15d" class=""><strong>✅ QUEENSLAND (QLD) GOVERNMENT FUNDING — DETAILED TO-DO LIST</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80cb-ac98-d220f5a20de9" class=""><strong>PHASE 0 — QLD-Specific Setup (Day 1–2)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8035-9729-ed9fd8ab70dd" class=""><strong>0.1 Confirm QLD eligibility anchors</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f2-94c1-de5fdeeffe33" class="bulleted-list"><li style="list-style-type:disc">☐ Business registered i
n QLD <strong>OR</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8048-8374-ca0b58c7da05" class="bulleted-list"><li style="list-style-type:disc">☐ Primary operations / pilot activity located in QLD</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80fc-a2c3-ed777a9cc61a" class="bulleted-list"><li style="list-style-type:disc">☐ QLD address (can be coworking / registered office)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ee-82c1-d004f25126e7" class="bulleted-list"><li style="list-style-type:disc">☐ QLD bank account acceptable for funding receipts</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8058-acbb-d6fbaf1e0d64" class="">👉 <em>Most QLD grants require “economic benefit to QLD”, not HQ exclusivity.</em></p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80d5-a78c-c550edc66f00"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80ef-b60a-e0c4dfb06474" class=""><strong>0.2 Create QLD grant access points</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80db-afb9-c3043e572e3e" class="bulleted-list"><li style="list-style-type:disc">☐ <strong>GrantConnect</strong> (federal, still needed)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ad-b834-fca687566f42" class="bulleted-list"><li style="list-style-type:disc">☐ <strong>Business Queensland</strong> account</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80fb-9024-da3bfdc75e3b" class="bulleted-list"><li style="list-style-type:disc">☐ Bookmark:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-803e-a1a1-c0dac931cf9b" class="bulleted-list"><li style="list-style-type:circle">Business Queensland – Grants &amp; 
Funding</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8020-bd9c-cc882b4e6939" class="bulleted-list"><li style="list-style-type:circle">Advance Queensland portal</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-803e-aa82-cb5744e1c240" class="bulleted-list"><li style="list-style-type:circle">Department of State Development, Infrastructure &amp; 
Planning (DSDIP)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b4-bff1-effbf29f3bf0" class="bulleted-list"><li style="list-style-type:circle">Queensland Treasury (innovation-linked programs)</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8042-a427-f7c6ba8acd4b"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80a8-b710-c2d367a7cbf6" class=""><strong>PHASE 1 — CORE QLD GRANT PROGRAMS (HIGH PRIORITY)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80e6-be75-cc9be7d7addc" class=""><strong>1️⃣</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80e2-ab75-d5702cd593ee" class="">This is QLD’s flagship innovation funding ecosystem.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80ca-9708-dd0afe55050c" class=""><strong>Programs to monitor / apply to:</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8087-b7ca-c1fa649dc641" class="bulleted-list"><li style="list-style-type:disc">☐ <strong>Advance Queensland Innovation Partnerships</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8077-bcbb-ed52dd924486" class="bulleted-list"><li style="list-style-type:disc">☐ <strong>Industry Research Fellowships</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8011-97ee-ca3aa5d6dae1" class="bulleted-list"><li style="list-style-type:disc">☐ <strong>Ignite Ideas Fund</strong> (SMEs, tech, 
digital)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8052-b391-c6cab64a8f65" class="bulleted-list"><li style="list-style-type:disc">☐ <strong>Regional Innovation Program</strong> (if pilot regional)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8011-ac78-cfc4c2869399" class="bulleted-list"><li style="list-style-type:disc">☐ <strong>Queensland Future Skills / Digital Capability rounds</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-800e-b1c2-ce341c8fbd86" class=""><strong>Typical funding:</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8096-8e44-ed971d04d07f" class="bulleted-list"><li style="list-style-type:disc">$100k – $300k (some up to $1M+ with partners)</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80ca-8822-e5e63af71843" class=""><strong>To-do:</strong></p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8007-ba62-c76264cc91b7" class="bulleted-list"><li style="list-style-type:disc">☐ Subscribe to Advance Queensland alerts</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8093-b385-f31f6baf576a" class="bulleted-list"><li style="list-style-type:disc">☐ Download guidelines for <strong>Ignite Ideas Fund</strong> immediately</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-801a-8da6-f2aed898da96" class="bulleted-list"><li style="list-style-type:disc">☐ Map your project to:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a4-8019-f2ddaccba08a" class="bulleted-list"><li style="list-style-type:circle">productivity</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8058-87d5-e637eb3d92e2" class="bulleted-list"><li style="list-style-type:circle">digital capability</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-806a-a163-d75d304025c4" c
lass="bulleted-list"><li style="list-style-type:circle">infrastructure</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8026-b628-e985cd16f716" class="bulleted-list"><li style="list-style-type:circle">energy / transport / resilience</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80b8-991d-ff01bf6a8156" class=""><strong>Done when:</strong></p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-807e-af0d-f863c0b4d564" class="">You have <strong>one Advance QLD grant chosen as your anchor application</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80e6-80d9-fa34fa94ae13"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8086-a1d5-f50891e0713f" class=""><strong>2️⃣</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8071-8956-ffa39950f580" class=""><strong>Ignite Ideas Fund — Immediate Target</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-806d-8d99-d2162b0a1401" class="">This is one of the <strong>best fits</strong> for you.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-809a-aebc-c65f969bd3d0" class=""><strong>To-do checklist:</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8050-b71e-ee77f9eb7203" class="bulleted-list"><li style="list-style-type:disc">☐ Confirm SME eligibility thresholds</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8028-b1e3-f989e17fdf8b" class="bulleted-list"><li style="list-style-type:disc">☐ Prepare:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-809f-932d-eb6d2cec473f" class="bulleted-list"><li style="list-style-type:circle">1-page commercialisation plan</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-802f-b739-e974b3699549" class="bulleted-list"><li style="list-style-type:circle">2-page technical delivery p
lan</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8003-ad46-c061d091b6e4" class="bulleted-list"><li style="list-style-type:circle">Budget + milestones</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-809b-9469-f3372402cc2e" class="bulleted-list"><li style="list-style-type:disc">☐ Emphasise:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-806b-97e9-cf2e0841a7dd" class="bulleted-list"><li style="list-style-type:circle">risk reduction</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-801c-b842-eff60ca6a044" class="bulleted-list"><li style="list-style-type:circle">execution certainty</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8080-8d3a-d4efd2726aa6" class="bulleted-list"><li style="list-style-type:circle">public benefit to QLD economy</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-803d-ba8f-cc22deb58f6e" class=""><strong>Pro tip (important):</strong></p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8057-a710-ee32053701d1" class="">Ignite Ideas panels <strong>hate hype</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80d4-898f-d4d8c80c46c8" class="">They LOVE:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c0-ada0-ee7f3de3be5f" class="bulleted-list"><li style="list-style-type:disc">delivery evidence</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-802d-a59a-d5713ee9f0b8" class="bulleted-list"><li style="list-style-type:disc">conservative claims</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c8-acdf-e6aa2a65b96f" class="bulleted-list"><li style="list-style-type:disc">“this will not fail” tone</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8077-af00-d8abca0c625f"/></div><div style="display:contents" d
ir="auto"><h2 id="2e2c5e6f-95bd-80e5-bb7e-fd44524f7272" class=""><strong>PHASE 2 — QLD DEPARTMENTS &amp; PILOTS (VERY HIGH WIN RATE)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-809e-9927-ea0c7684ed73" class=""><strong>3️⃣</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8096-819a-e20e03ea6656" class=""><strong>Department-led pilots (quiet but powerful)</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8036-9f26-f4c8e255b5f2" class="">QLD departments regularly fund:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80eb-b964-e38bae9d5446" class="bulleted-list"><li style="list-style-type:disc">digital pilots</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-803c-8db3-df28e1ec2160" class="bulleted-list"><li style="list-style-type:disc">infrastructure analytics</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-802a-a288-cbe2d2369c6a" class="bulleted-list"><li style="list-style-type:disc">safety &amp; governance systems</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e9-9eb6-d00f79d5fa0f" class="bulleted-list"><li style="list-style-type:disc">AI governance tools</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8024-b466-f78fd21f7370" class="bulleted-list"><li style="list-style-type:disc">decision-support platforms</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8028-8b04-e53310a8e928" class="">Departments to watch:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f8-a127-fb680a249503" class="bulleted-list"><li style="list-style-type:disc">☐ Transport and Main Roads (TMR)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80af-927e-dd2754f8a4c4" class="bulleted-list"><li style="list-style-type:disc">☐ Energy &amp; 
Public Works</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8056-9ba8-db3c10617165" class="bulleted-list"><li style="list-style-type:disc">☐ Queensland Health (governance tools only)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ff-8e34-f27c0a285c59" class="bulleted-list"><li style="list-style-type:disc">☐ Department of Environment, Science &amp; 
Innovation (DESI)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f3-9a16-f295f2d60d7a" class="bulleted-list"><li style="list-style-type:disc">☐ Queensland Treasury (digital policy tools)</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80e8-a406-f49f685b64bd" class=""><strong>To-do:</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8088-bd70-d85ed6778230" class="bulleted-list"><li style="list-style-type:disc">☐ Prepare a <strong>2-page pilot concept note</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c1-a66d-c6bfd8792a6c" class="bulleted-list"><li style="list-style-type:disc">☐ Request informal meetings via:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-809f-962d-fbb26a83b899" class="bulleted-list"><li style="list-style-type:circle">innovation units</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8021-84cc-c83a705ff1d7" class="bulleted-list"><li style="list-style-type:circle">digital transformation teams</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c0-9a1e-d892b806acdf" class="bulleted-list"><li style="list-style-type:disc">☐ Ask:<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-807c-8544-f0b7fd056195" class=""><em>“Is there a pilot or challenge program we could align with?”</em></p></div></li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80a6-ae98-e4be49e77b6c" class=""><strong>Done when:</strong></p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8034-b9e8-ed9aa23cd94a" class="">You have <strong>1 department conversation</strong>, 
not necessarily funding yet.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-809d-8571-dff841e0ebae"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80e0-b843-f1eba16f4b10" class=""><strong>PHASE 3 — LOCAL &amp; 
REGIONAL QLD GRANTS (EASY WINS)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8080-9002-eeb4e87c125e" class=""><strong>4️⃣</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-800f-aa44-f22fcccd1994" class=""><strong>Local Council Innovation Grants</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-800b-91d9-d96ef0ab0a41" class="">These are <strong>much easier</strong> and often overlooked.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8055-8c2d-c11b02a1f0cb" class="">Councils to check (examples):</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8016-a036-fd9fc5c17fc0" class="bulleted-list"><li style="list-style-type:disc">Brisbane City Council</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80dc-af6a-fe0bd1fcf9eb" class="bulleted-list"><li style="list-style-type:disc">Gold Coast City</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8003-820f-d0dbe53b8056" class="bulleted-list"><li style="list-style-type:disc">Sunshine Coast Council</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8074-a70b-e0a1a87d355a" class="bulleted-list"><li style="list-style-type:disc">Regional Development Australia (RDA QLD)</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-808e-b4db-f8427971d8b7" class="">Funding:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-809f-bab7-e3d2d3cd80c2" class="bulleted-list"><li style="list-style-type:disc">$10k – $100k</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8077-983e-e989f81c802e" class="bulleted-list"><li style="list-style-type:disc">Faster decisions</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f9-abb0-d19e86e05890" class="bulleted-list"><li style="list-style-type:disc">Pilot-friendly</li></ul></div><div s
tyle="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80be-994a-e4898cfc147b" class=""><strong>To-do:</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a4-8b9f-f4e07adb40c8" class="bulleted-list"><li style="list-style-type:disc">☐ Identify <strong>2 councils</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80fd-9a31-e44474063b34" class="bulleted-list"><li style="list-style-type:disc">☐ Check:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-800d-be63-f060c5626a7c" class="bulleted-list"><li style="list-style-type:circle">innovation grants</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8002-862b-dbf4621cab98" class="bulleted-list"><li style="list-style-type:circle">smart city funding</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-809b-ae6c-e60b1630f355" class="bulleted-list"><li style="list-style-type:circle">digital economy initiatives</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8075-aa6b-c2c15b489f0e" class="bulleted-list"><li style="list-style-type:disc">☐ Submit <strong>1–2 applications</strong> max</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80ef-943d-e74391d58bd7"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8055-8abf-e6af84ecad51" class=""><strong>PHASE 4 — UNIVERSITY PARTNERS (QLD IS STRONG HERE)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80d5-a87e-cbb08d492d78" class=""><strong>5️⃣</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80b4-9f2d-d67ae6f23f4e" class=""><strong>QLD Universities — Translation Funding</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-805d-80ec-e1db429af958" class="">Key institutions:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f3-afdd-d4e3462eb1bd" c
lass="bulleted-list"><li style="list-style-type:disc">☐ UQ</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8015-9251-cb6880511a44" class="bulleted-list"><li style="list-style-type:disc">☐ QUT</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8052-949e-c7572ce38557" class="bulleted-list"><li style="list-style-type:disc">☐ Griffith</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8043-8b83-f00b2af2b678" class="bulleted-list"><li style="list-style-type:disc">☐ UniSC</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80e7-bb72-e2b8f2341969" class="">What to ask for:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8098-8c6a-e1a02b0de2b6" class="bulleted-list"><li style="list-style-type:disc">proof-of-concept grants</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8037-bc30-ec64ba6c085b" class="bulleted-list"><li style="list-style-type:disc">industry translation funding</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8004-8bf6-d8ccfe4a73d4" class="bulleted-list"><li style="list-style-type:disc">joint pilots</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-802b-a1e3-dc78e0fe99b1" class="bulleted-list"><li style="list-style-type:disc">letters of support</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-809c-821b-f9a9fb1ee4dd" class=""><strong>To-do:</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d2-a17d-d7a4fa4ad08f" class="bulleted-list"><li style="list-style-type:disc">☐ Contact <strong>Industry Engagement / Research Translation office</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8019-90d9-d8f85236ad5a" class="bulleted-list"><li style="list-style-type:disc">☐ Pitch yourself as:<div style="display:contents" dir="auto"><blockquote i
d="2e2c5e6f-95bd-80ac-a62e-dcf8d7712f99" class="">“Industry architect + delivery lead”</blockquote></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c7-a771-d8f9c34c7c38" class="bulleted-list"><li style="list-style-type:disc">☐ Aim for:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e7-bf22-eb65122ed85b" class="bulleted-list"><li style="list-style-type:circle">letter of support</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80da-8126-c76444b6ad36" class="bulleted-list"><li style="list-style-type:circle">pilot partnership</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8083-9383-ffa5e5b24075" class="bulleted-list"><li style="list-style-type:circle">pathway to AEA Ignite later</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8085-8ea0-f9d47ef4fd5d"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8012-8292-c818c9cc6077" class=""><strong>PHASE 5 — FEDERAL (BUT QLD-LEVERAGED)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-806e-9459-c912eadc5ac9" class=""><strong>6️⃣</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-800e-b27b-f57e7126fc22" class=""><strong>Federal grants you should target from QLD</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ff-85a5-fe06ebd6be97" class="bulleted-list"><li style="list-style-type:disc">☐ Mid-tier federal innovation grants (non-AEA first)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c4-a615-e6c06fb8d427" class="bulleted-list"><li style="list-style-type:disc">☐ Infrastructure &amp; 
digital resilience programs</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8066-ae23-ee5a2191f210" class="bulleted-list"><li style="list-style-type:disc">☐ AI governance / cyber / critical systems funding</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80ee-b858-e58907603fcc" class=""><strong>Note:</strong></p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8058-81ec-cb495aaa1079" class="">You will win federal money <strong>after</strong>:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80cf-9bb5-d98a7241725a" class="bulleted-list"><li style="list-style-type:disc">1–2 QLD grants</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80de-b21d-c2c6ab32e701" class="bulleted-list"><li style="list-style-type:disc">1 pilot</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8041-b07b-cd06d706d9c5" class="bulleted-list"><li style="list-style-type:disc">1 department or uni backing</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-809b-8d96-d5410307fa8b"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80ad-8b03-e3c2e46a5f55" class=""><strong>PHASE 6 — R&amp;D TAX INCENTIVE (DO IN PARALLEL)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80d0-9b39-eaf5fd2a1336" class=""><strong>7️⃣ R&amp;D Tax Incentive — QLD friendly</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8083-b75c-e43ff898466b" class="bulleted-list"><li style="list-style-type:disc">☐ Register R&amp;D activities</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-804e-87ad-f6dd4ae24b43" class="bulleted-list"><li style="list-style-type:disc">☐ Maintain logs:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c1-a8f6-fc28afdabba1" class="bulleted-list"><li style="list-style-type:circle">technical u
ncertainty</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-808b-8f03-d918e2d3a9ce" class="bulleted-list"><li style="list-style-type:circle">experiments</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8005-8ed4-ea821b011e67" class="bulleted-list"><li style="list-style-type:circle">iterations</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8009-a607-fe087b904293" class="bulleted-list"><li style="list-style-type:disc">☐ Track staff hours + costs</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8034-9002-e859164583bb" class="">This stacks <strong>on top of all QLD grants</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8013-8ae9-e1e5b421922b"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-8018-9910-d8dd096926ae" class=""><strong>🔢 REALISTIC QLD FUNDING OUTCOME (HONEST)</strong></h1></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-801c-b56e-c882669f9081" class=""><strong>Year 1 (QLD-focused)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80d3-9a06-e324f472312c" class="bulleted-list"><li style="list-style-type:disc">$150k – $600k very realistic</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-805d-9c96-cebd80dd9745" class=""><strong>Year 2 (QLD + Federal)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-804e-80d6-f02fa04e7d06" class="bulleted-list"><li style="list-style-type:disc">$1M – $3M cumulative</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8073-b98a-fb94d5ccd717" class=""><strong>Year 3+</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8097-803c-c351669112e0" class="bulleted-list"><li style="list-style-type:disc">AEA + multi-year programs</li></ul></div><div style="display:contents" dir="auto"><ul i
d="2e2c5e6f-95bd-8063-a006-ece776fb4f0e" class="bulleted-list"><li style="list-style-type:disc">$5M+ cumulative plausible</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8034-b304-c8456f71d724"/></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80c9-a47a-eda94b999874" class="">Here’s the <strong>clean, correct, step-by-step way to register an ACN in Australia</strong>, written so you can do it <strong>today without mistakes</strong>. No fluff.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8086-b404-c546f6e5fc6d"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-80d8-95e5-f3dd8112b421" class=""><strong>✅ How to Register an ACN (Australia)</strong></h1></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8012-ba0b-fdfebf49c300" class="">An <strong>ACN (Australian Company Number)</strong> is issued automatically when you register a <strong>company</strong> with ASIC.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8004-a26d-dc912f270810" class="">Here’s the <strong>clean, correct, step-by-step way to register an ACN in Australia</strong>, written so you can do it <strong>today without mistakes</strong>. 
No fluff.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80a9-8b31-c03a8aea959c"/></div><div style="display:contents" dir="auto"><h1 id="2e2c5e6f-95bd-80f2-93fd-dd5de97ca8b4" class=""><strong>✅ How to Register an ACN (Australia)</strong></h1></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8013-b3cd-e7e85ae24eec" class="">An <strong>ACN (Australian Company Number)</strong> is issued automatically when you register a <strong>company</strong> with ASIC.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-804a-a7bf-fb9b119ded58" class="">You do <strong>not</strong> apply for an ACN separately.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80de-826b-e32d9a679cad"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8068-b1df-c4c37c4fe715" class=""><strong>OPTION 1 —</strong></h2></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8018-b624-fed84005fee7" class=""><strong>Register directly with ASIC (recommended)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-806c-9fe5-f7f9b3909eb4" class="">This is the <strong>cheapest, 
cleanest</strong> way.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8029-880a-f8e2b72ce0cd" class=""><strong>🔹 What you need (prepare first)</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8068-8c77-ff7d60a9ad75" class="">Have these ready before you start:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8008-9ea6-f0f1049d94be" class="bulleted-list"><li style="list-style-type:disc">✔ Company name (or choose “proprietary limited” without a name)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8069-bb71-cffe92e931f1" class="bulleted-list"><li style="list-style-type:disc">✔ Director details (you)<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8090-a963-c3054d078eb5" class="bulleted-list"><li style="list-style-type:circle">Full legal name</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8031-b190-ef5997b8098d" class="bulleted-list"><li style="list-style-type:circle">Date &amp; 
place of birth</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c4-bedf-c623c06ea242" class="bulleted-list"><li style="list-style-type:circle">Residential address</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80bc-ae76-da4669b0c0b8" class="bulleted-list"><li style="list-style-type:disc">✔ Shareholder details (you)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ca-bce3-fe5cbfea08e4" class="bulleted-list"><li style="list-style-type:disc">✔ Registered office address (can be your home)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-800d-993c-d9699a9f10be" class="bulleted-list"><li style="list-style-type:disc">✔ Principal place of business (can be same as above)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f7-ad80-e270359d2b4a" class="bulleted-list"><li style="list-style-type:disc">✔ Email address</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80eb-9568-cd2ade2c367f" class="bulleted-list"><li style="list-style-type:disc">✔ Payment method</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-807e-9e40-c645e5b01919"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80af-9b86-f3a72ec3734c" class=""><strong>🔹 Step-by-step (10–20 minutes)</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8033-823a-ec0f2291cfcf" class="">1️⃣ Go to <strong>ASIC Company Registration</strong></p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8079-8f1e-c55355b48e1b" class="">(Official ASIC site → “Register a company”)</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80da-96af-e6e944b6960e" class="">2️⃣ Choose:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8001-9bcb-f2ff29ecdb8d" class="bulleted-list"><li s
tyle="list-style-type:disc"><strong>Proprietary company</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8030-bb0e-dc7133389233" class="bulleted-list"><li style="list-style-type:disc"><strong>Limited by shares</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8064-b2f1-f518a145a589" class="bulleted-list"><li style="list-style-type:disc">Usually <strong>Pty Ltd</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80dc-98ed-ef6b750fb924" class="">3️⃣ Enter:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8047-86b4-d65b9fe2f62f" class="bulleted-list"><li style="list-style-type:disc">Company name<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8093-aa3f-d0336d0de427" class=""><em>(or choose “ACN Pty Ltd” if you want speed)</em></p></div></li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80b8-a478-d2a2f5d7e754" class="">4️⃣ Add director(s) and shareholder(s)</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ed-8b1f-db10d546987a" class="bulleted-list"><li style="list-style-type:disc">You can be <strong>100% owner &amp; sole director</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8069-b62c-e010e0ac6490" class="">5️⃣ Addresses</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-801c-8e9b-f2cc58851c20" class="bulleted-list"><li style="list-style-type:disc">Registered office</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ab-bda6-cec0eca836d3" class="bulleted-list"><li style="list-style-type:disc">Principal place of business</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80cf-b43e-e42a400501c3" class="">6️⃣ Review &amp; 
submit</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8056-ad76-d8194fcaf4d2" class="">7️⃣ Pay fee</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8023-8140-f98deb0c0ce5" class="">💰 <strong>~AUD $576</strong> (ASIC fee)</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-808b-824a-eb6c4ca258c6"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8055-9ba3-e9fb31acf71f" class=""><strong>🔹 What you get</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8044-aef8-dd26898cf5fa" class="">Within minutes to a few hours:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-803b-b2e9-e7555e9a613e" class="bulleted-list"><li style="list-style-type:disc">✅ <strong>ACN issued</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80fd-b777-f340a4a4cb32" class="bulleted-list"><li style="list-style-type:disc">✅ Company registered</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-800c-900f-c5dc9159668d" class="bulleted-list"><li style="list-style-type:disc">✅ Company details live on ASIC</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-800f-b579-cdc8d38c0442" class="bulleted-list"><li style="list-style-type:disc">⏳ Certificate emailed (same day or next day)</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8021-b674-fe76dd030c50" class="">That’s it.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80a6-8958-ebb5a5163f0c"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-802f-b5aa-fb90e783e51f" class=""><strong>OPTION 2 — Use a company registration service (easier, 
slightly more expensive)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8015-818c-cf54395f1325" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8019-80be-ff0b45307747" class="bulleted-list"><li style="list-style-type:disc">EasyCompanies</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8070-9940-f2f8b6fedecd" class="bulleted-list"><li style="list-style-type:disc">Cleardocs</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e4-96a8-c0f86c3b3934" class="bulleted-list"><li style="list-style-type:disc">Lawpath</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80bb-9115-f48216bc425d" class=""><strong>Pros</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-805d-b360-c5704493b7b7" class="bulleted-list"><li style="list-style-type:disc">Guided</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80fe-8589-ef847df5aace" class="bulleted-list"><li style="list-style-type:disc">Less thinking</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8002-9b61-c48bd8fe0f3d" class="bulleted-list"><li style="list-style-type:disc">Often includes constitution</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-809d-ba00-f619e14b5c6a" class=""><strong>Cons</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8046-8b2c-d05f50bf6906" class="bulleted-list"><li style="list-style-type:disc">Costs ~$700–$900 total</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8044-af6b-ca0ae33a9ba5" class=""><strong>Not necessary</strong> if you’re comfortable filling a form.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-804e-bb55-f6aefb2f572b"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80b7-a898-ee66b8b3df90" class=""><strong>AFTER you g
et the ACN (DO THESE NEXT)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80f8-af60-e59f043a9ac7" class=""><strong>🔹 1️⃣ Get an ABN for the company (free)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-806f-90e1-c04244bfae7a" class="bulleted-list"><li style="list-style-type:disc">Apply via ABR (Australian Business Register)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ba-a236-fb059c0a2503" class="bulleted-list"><li style="list-style-type:disc">Use your <strong>new ACN</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-804e-98dc-d3639d2aa909" class="bulleted-list"><li style="list-style-type:disc">ABN usually issued instantly</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8035-ba92-f4cebb1ede30" class="">👉 Grants almost always require <strong>ABN + ACN</strong></p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8052-b38d-cb24e05ec582"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80f3-a031-fc6d270fd438" class=""><strong>🔹 2️⃣ Open a company bank account</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8010-99ae-d89cba5c7a49" class="bulleted-list"><li style="list-style-type:disc">Any major bank</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f2-9882-f3dba6ddd1d7" class="bulleted-list"><li style="list-style-type:disc">Use:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-801a-9bda-d1c86aebf048" class="bulleted-list"><li style="list-style-type:circle">Certificate of registration</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-800b-97cc-c424f8e6882b" class="bulleted-list"><li style="list-style-type:circle">ACN</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80cc-b5e5-d70f831c42dd" class="bulleted-list"><li s
tyle="list-style-type:circle">ABN</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8067-a1fa-c70abd0082b6" class="bulleted-list"><li style="list-style-type:disc">This is <strong>mandatory</strong> for grant payments</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80a6-adb8-f9c7c5a2b770"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8098-b55d-d4af81cc4ce8" class=""><strong>🔹 3️⃣ Set up MyGovID + RAM</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f2-a221-edcdc3d1f9da" class="bulleted-list"><li style="list-style-type:disc">Needed to:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ba-a617-c16cb4f6d596" class="bulleted-list"><li style="list-style-type:circle">apply for grants</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8002-a84c-ccbfe11d983b" class="bulleted-list"><li style="list-style-type:circle">manage ASIC</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8092-ae81-e64b514fb14e" class="bulleted-list"><li style="list-style-type:circle">access business services</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-800d-b906-c1546bf4d76d"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80f1-8a69-f2c7bce03e82" class=""><strong>🔹 4️⃣ IP assignment (important for grants)</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-809b-9c05-d8487b50cf55" class="">If you created IP personally <strong>before</strong> the company:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-803a-90df-fdc847786ad3" class="bulleted-list"><li style="list-style-type:disc">Assign IP to the company</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8063-9bb9-ca8676216e45" class="bulleted-list"><li style="list-style-type:disc">Simple one-page IP a
ssignment deed is enough</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8066-afb5-dd731b49c69b" class="">Grant panels care about <strong>clean IP ownership</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80e4-9ce0-c4db30cc262e"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8073-9135-f44044ba0746" class=""><strong>Minimal structure I recommend (for grants)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80f0-96c7-ef3db938d992" class="">For speed + funding eligibility:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-802d-a1ab-e1d9f5d24753" class="bulleted-list"><li style="list-style-type:disc">✔ 1 director (you)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-801e-aa79-fa75dcbacde1" class="bulleted-list"><li style="list-style-type:disc">✔ 1 shareholder (you)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f1-8b47-d48a1985bf52" class="bulleted-list"><li style="list-style-type:disc">✔ Standard constitution</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-805f-ae35-e0f73df22bf7" class="bulleted-list"><li style="list-style-type:disc">✔ No employees yet (fine)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-804d-8c89-e509c19caa4b" class="bulleted-list"><li style="list-style-type:disc">✔ No complex share classes</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80f7-ae64-e1de15236dac" class="">This is a <strong>“grant-ready shell”</strong>, 
not a startup bureaucracy.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-806d-ad70-c2d02a9610c3"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8074-abaa-fd2d8cfbf365" class=""><strong>Timeline (realistic)</strong></h2></div><div style="display:contents" dir="ltr"><table id="2e2c5e6f-95bd-8054-a120-dcc3031e5eee" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2e2c5e6f-95bd-806a-9b5a-fe0fb8068d3b"><th id="r`E_" class="simple-table-header-color simple-table-header"><strong>Step</strong></th><th id="KX[X" class="simple-table-header-color simple-table-header"><strong>Time</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2e2c5e6f-95bd-8048-bec0-e754b14a8fc8"><td id="r`E_" class="">ASIC registration</td><td id="KX[X" class="">15–30 min</td></tr></div><div style="display:contents" dir="ltr"><tr id="2e2c5e6f-95bd-80de-9808-f90ace231161"><td id="r`E_" class="">ACN issued</td><td id="KX[X" class="">Same day</td></tr></div><div style="display:contents" dir="ltr"><tr id="2e2c5e6f-95bd-80a6-a944-e8a63a0cce62"><td id="r`E_" class="">ABN</td><td id="KX[X" class="">Same day</td></tr></div><div style="display:contents" dir="ltr"><tr id="2e2c5e6f-95bd-8051-abd3-dac34b48d2df"><td id="r`E_" class="">Bank account</td><td id="KX[X" class="">1–3 days</td></tr></div><div style="display:contents" dir="ltr"><tr id="2e2c5e6f-95bd-804c-aa78-d949149ba904"><td id="r`E_" class="">Fully grant-ready</td><td id="KX[X" class="">2–5 days</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8028-af7f-cb6da2b9d6e7"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8005-abca-e2590fd135ae" class=""><strong>One-line summary</strong></h2></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-804d-b9e5-eab3d26b195d" class="">You don’t apply for an ACN.</blockquote></div><div s
tyle="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-800d-9dff-da5f21e36d71" class="">You get an ACN by registering a company with ASIC.</blockquote></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-800b-8296-fbf18dc6dce7"/></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-809c-9851-d3694c09d256" class="">If you want, next I can:</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-802f-87c6-d34f9f9d2a87" class="">1️⃣ Tell you <strong>what to name the company</strong> for grants</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-809e-9e33-d9b7ca323104" class="">2️⃣ Give you a <strong>grant-safe constitution setup</strong></p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-800d-b69b-e5d311d88010" class="">3️⃣ Proceed assuming company is registered and shortlist <strong>current QLD grants</strong></p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8062-a948-e34841ad1b46" class="">Just say <strong>1, 2, or 3</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-806a-ac0d-d6cc7248e4c1" class="">You do <strong>not</strong> apply for an ACN separately.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80a1-906e-da0403a46c80"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8053-8912-cf3c8f0e87eb" class=""><strong>OPTION 1 —</strong></h2></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80da-a17c-daec23c6910c" class=""><strong>Register directly with ASIC (recommended)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8098-9f68-c7d18d8cc7c1" class="">This is the <strong>cheapest, 
cleanest</strong> way.</p></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8043-b0b3-fd562772983f" class=""><strong>🔹 What you need (prepare first)</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8016-acf8-e0c055a0d684" class="">Have these ready before you start:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80de-94a8-cf2fcfefd6ea" class="bulleted-list"><li style="list-style-type:disc">✔ Company name (or choose “proprietary limited” without a name)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8021-8a8b-cb99b9bf8022" class="bulleted-list"><li style="list-style-type:disc">✔ Director details (you)<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-808c-980d-cc18bc39212b" class="bulleted-list"><li style="list-style-type:circle">Full legal name</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c9-a1f9-c2a79d0a80a7" class="bulleted-list"><li style="list-style-type:circle">Date &amp; 
place of birth</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8076-97fd-d26cb895322a" class="bulleted-list"><li style="list-style-type:circle">Residential address</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80cd-936c-d27ddf29e876" class="bulleted-list"><li style="list-style-type:disc">✔ Shareholder details (you)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ce-b7d9-cac791067941" class="bulleted-list"><li style="list-style-type:disc">✔ Registered office address (can be your home)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8011-a49b-c123f56f0f2b" class="bulleted-list"><li style="list-style-type:disc">✔ Principal place of business (can be same as above)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8025-82fc-e91dab5cf261" class="bulleted-list"><li style="list-style-type:disc">✔ Email address</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a1-918c-f9f0bd1320d5" class="bulleted-list"><li style="list-style-type:disc">✔ Payment method</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-809d-ad32-e13fda6388ef"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-803b-b812-c4af469580b3" class=""><strong>🔹 Step-by-step (10–20 minutes)</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8001-9163-f1bf862b4f8c" class="">1️⃣ Go to <strong>ASIC Company Registration</strong></p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8014-ae25-e10e4610b2a9" class="">(Official ASIC site → “Register a company”)</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8054-8e60-d8bde522e9bc" class="">2️⃣ Choose:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c4-8db6-e8d90b294902" class="bulleted-list"><li s
tyle="list-style-type:disc"><strong>Proprietary company</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80bb-aeb5-e9c235a227b8" class="bulleted-list"><li style="list-style-type:disc"><strong>Limited by shares</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8044-b9dd-fa235852b0ed" class="bulleted-list"><li style="list-style-type:disc">Usually <strong>Pty Ltd</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-809c-a4b3-e4d6b326efec" class="">3️⃣ Enter:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-800a-8f09-cfc0d4ef6204" class="bulleted-list"><li style="list-style-type:disc">Company name<div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80dc-9154-e39caaf1b92a" class=""><em>(or choose “ACN Pty Ltd” if you want speed)</em></p></div></li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80c1-9090-d3e0299dafdd" class="">4️⃣ Add director(s) and shareholder(s)</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8010-934a-ed40b46fa1c9" class="bulleted-list"><li style="list-style-type:disc">You can be <strong>100% owner &amp; sole director</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8014-8588-cb8bf40a2adc" class="">5️⃣ Addresses</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8043-a1d0-e69082e7c7a4" class="bulleted-list"><li style="list-style-type:disc">Registered office</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-801d-a39b-e96c415f2e65" class="bulleted-list"><li style="list-style-type:disc">Principal place of business</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-806b-8b59-d2348c78ef3a" class="">6️⃣ Review &amp; 
submit</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-802e-91e5-ed0424e83298" class="">7️⃣ Pay fee</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80e3-aab4-f43d2d5c1f31" class="">💰 <strong>~AUD $576</strong> (ASIC fee)</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8042-a55d-dcc68bc62860"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8031-a8bd-c1d910d721d3" class=""><strong>🔹 What you get</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80c3-9f8b-d1c691a6dee0" class="">Within minutes to a few hours:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-804a-afdd-cd9cd68eab48" class="bulleted-list"><li style="list-style-type:disc">✅ <strong>ACN issued</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80e8-8403-c087bd808f4b" class="bulleted-list"><li style="list-style-type:disc">✅ Company registered</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-806d-b7b4-cc397d39d5a7" class="bulleted-list"><li style="list-style-type:disc">✅ Company details live on ASIC</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8013-a254-dd010bfe5bb2" class="bulleted-list"><li style="list-style-type:disc">⏳ Certificate emailed (same day or next day)</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80e7-83c9-f234a457c281" class="">That’s it.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8003-8dec-c43671bf88b6"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8081-8e79-cc086578ad4c" class=""><strong>OPTION 2 — Use a company registration service (easier, 
slightly more expensive)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80ae-a7dc-c68165aa6ee8" class="">Examples:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8016-ab9e-f3ef656dcadb" class="bulleted-list"><li style="list-style-type:disc">EasyCompanies</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80fc-8ef2-cd9dac8df0ac" class="bulleted-list"><li style="list-style-type:disc">Cleardocs</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8009-bdd3-c212116566a2" class="bulleted-list"><li style="list-style-type:disc">Lawpath</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8043-b0de-da2f0dcec8f0" class=""><strong>Pros</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8043-be33-e3d81917677b" class="bulleted-list"><li style="list-style-type:disc">Guided</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80ba-b3a5-c137b44b2457" class="bulleted-list"><li style="list-style-type:disc">Less thinking</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-808d-8e07-eedde91fb37e" class="bulleted-list"><li style="list-style-type:disc">Often includes constitution</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8088-9892-f84d4d410c17" class=""><strong>Cons</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80c5-b257-d4c54b5cc254" class="bulleted-list"><li style="list-style-type:disc">Costs ~$700–$900 total</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-806c-a06d-c4a4abc2de1c" class=""><strong>Not necessary</strong> if you’re comfortable filling a form.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8098-af35-fc4b779a8b8b"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8014-b395-f5c9114bf548" class=""><strong>AFTER you g
et the ACN (DO THESE NEXT)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80b5-9cdf-c6c1a965adae" class=""><strong>🔹 1️⃣ Get an ABN for the company (free)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80a5-98f1-ff54f53d944f" class="bulleted-list"><li style="list-style-type:disc">Apply via ABR (Australian Business Register)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80bf-a103-e355e0517484" class="bulleted-list"><li style="list-style-type:disc">Use your <strong>new ACN</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8069-958c-dddcb6dcf1c8" class="bulleted-list"><li style="list-style-type:disc">ABN usually issued instantly</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8041-951a-e531fcbb2bb0" class="">👉 Grants almost always require <strong>ABN + ACN</strong></p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8050-90f8-ff33bb214594"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80f5-be70-f5a85ef89924" class=""><strong>🔹 2️⃣ Open a company bank account</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8040-be75-ca78b9b6b8a5" class="bulleted-list"><li style="list-style-type:disc">Any major bank</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b1-b99d-d197ecccb357" class="bulleted-list"><li style="list-style-type:disc">Use:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-801f-9738-db58270bee58" class="bulleted-list"><li style="list-style-type:circle">Certificate of registration</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80f4-8a71-d2d3ce6b0dba" class="bulleted-list"><li style="list-style-type:circle">ACN</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-803e-a26a-e8f833e81f18" class="bulleted-list"><li s
tyle="list-style-type:circle">ABN</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-808f-9c65-ed2eb663aded" class="bulleted-list"><li style="list-style-type:disc">This is <strong>mandatory</strong> for grant payments</li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8038-8938-ffad5377543e"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-80ff-a67a-d27f034d8492" class=""><strong>🔹 3️⃣ Set up MyGovID + RAM</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80bc-b8d4-cd90f9f33ea3" class="bulleted-list"><li style="list-style-type:disc">Needed to:<div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8050-83d8-daf861acdeb9" class="bulleted-list"><li style="list-style-type:circle">apply for grants</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-800a-9d05-f040a333911b" class="bulleted-list"><li style="list-style-type:circle">manage ASIC</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8017-8438-ed17c18b362a" class="bulleted-list"><li style="list-style-type:circle">access business services</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80a4-99fb-e43549e83cbf"/></div><div style="display:contents" dir="auto"><h3 id="2e2c5e6f-95bd-8086-9246-ef14ac9cacea" class=""><strong>🔹 4️⃣ IP assignment (important for grants)</strong></h3></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-808b-9e1c-ef73935580f0" class="">If you created IP personally <strong>before</strong> the company:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-804c-b1ca-ff58ff93ce9b" class="bulleted-list"><li style="list-style-type:disc">Assign IP to the company</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8087-a63c-dfb9f43d0928" class="bulleted-list"><li style="list-style-type:disc">Simple one-page IP a
ssignment deed is enough</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8004-8ef9-cc44c54949e0" class="">Grant panels care about <strong>clean IP ownership</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80bd-b12b-f43be48b3d44"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-8010-9c88-c85d66c206ff" class=""><strong>Minimal structure I recommend (for grants)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-809c-af97-f2528ca2b7f2" class="">For speed + funding eligibility:</p></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8031-b0a2-c0e565bb2609" class="bulleted-list"><li style="list-style-type:disc">✔ 1 director (you)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8054-86b8-fa6d1c0003e7" class="bulleted-list"><li style="list-style-type:disc">✔ 1 shareholder (you)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8048-9de9-c8090b755665" class="bulleted-list"><li style="list-style-type:disc">✔ Standard constitution</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-80b8-979d-db0288e3d80b" class="bulleted-list"><li style="list-style-type:disc">✔ No employees yet (fine)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e2c5e6f-95bd-8034-ad1c-d6c39c23abbc" class="bulleted-list"><li style="list-style-type:disc">✔ No complex share classes</li></ul></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-800e-84c9-d6db2a37c307" class="">This is a <strong>“grant-ready shell”</strong>, 
not a startup bureaucracy.</p></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-8025-95db-fb78f85d20bb"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80f4-9c43-dd1357296a0d" class=""><strong>Timeline (realistic)</strong></h2></div><div style="display:contents" dir="ltr"><table id="2e2c5e6f-95bd-809f-8eea-ff14c07bef82" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2e2c5e6f-95bd-8008-b358-d2c0984a8c2e"><th id="@g~g" class="simple-table-header-color simple-table-header"><strong>Step</strong></th><th id="tN{z" class="simple-table-header-color simple-table-header"><strong>Time</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2e2c5e6f-95bd-80e1-8e5a-d92d39090a75"><td id="@g~g" class="">ASIC registration</td><td id="tN{z" class="">15–30 min</td></tr></div><div style="display:contents" dir="ltr"><tr id="2e2c5e6f-95bd-8080-8aaf-d94049fe448d"><td id="@g~g" class="">ACN issued</td><td id="tN{z" class="">Same day</td></tr></div><div style="display:contents" dir="ltr"><tr id="2e2c5e6f-95bd-800f-8ee6-efac48288a07"><td id="@g~g" class="">ABN</td><td id="tN{z" class="">Same day</td></tr></div><div style="display:contents" dir="ltr"><tr id="2e2c5e6f-95bd-80ef-8378-e9ede62b7009"><td id="@g~g" class="">Bank account</td><td id="tN{z" class="">1–3 days</td></tr></div><div style="display:contents" dir="ltr"><tr id="2e2c5e6f-95bd-80db-9f25-f65bd909f8ab"><td id="@g~g" class="">Fully grant-ready</td><td id="tN{z" class="">2–5 days</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-808a-b76c-d60074c173e8"/></div><div style="display:contents" dir="auto"><h2 id="2e2c5e6f-95bd-80e4-943e-d3b127f0dec2" class=""><strong>One-line summary</strong></h2></div><div style="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-808a-a946-c1ae22d625cd" class="">You don’t apply for an ACN.</blockquote></div><div s
tyle="display:contents" dir="auto"><blockquote id="2e2c5e6f-95bd-806c-98db-ff2c943b15bd" class="">You get an ACN by registering a company with ASIC.</blockquote></div><div style="display:contents" dir="auto"><hr id="2e2c5e6f-95bd-80b0-b4f5-e60c6f7a82dd"/></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8091-973c-d45581c160c5" class="">If you want, next I can:</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-809d-b6f9-c3ee1218598a" class="">1️⃣ Tell you <strong>what to name the company</strong> for grants</p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8072-bd35-deb4a4ea91d3" class="">2️⃣ Give you a <strong>grant-safe constitution setup</strong></p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-8090-82d8-f274b22afc76" class="">3️⃣ Proceed assuming company is registered and shortlist <strong>current QLD grants</strong></p></div><div style="display:contents" dir="auto"><p id="2e2c5e6f-95bd-80bd-ba34-d3baf0ad57d5" class="">Just say <strong>1, 2, or 3</strong>.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
