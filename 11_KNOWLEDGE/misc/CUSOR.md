---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Cusor</title><style>
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
	
</style></head><body><article id="2c5c5e6f-95bd-8071-b921-ed6c18fc3ecf" class="page sans"><header><h1 class="page-title" dir="auto">Cusor</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80e4-bfa0-f0a3ad5de2d7" class="">Below is a <strong>clean, minimal, production-grade Cursor prompt</strong> specifically designed for AMOS-style development.</p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80d2-a3e9-c68d297b9366" class="">It ensures Cursor behaves as:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8099-9fec-f21c2d2a3e20" class="bulleted-list"><li style="list-style-type:disc">a deterministic coding engine</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8052-9ed6-c1554900402a" class="bulleted-list"><li style="list-style-type:disc">an extension of your architecture</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8016-ad86-d8874d6d9141" class="bulleted-list"><li style="list-style-type:disc">not a hallucinating assistant</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80c4-8354-e5e1ceecbaf8" class="bulleted-list"><li style="list-style-type:disc">consistent across files, commits, and refactors</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-804e-83eb-f0ba5899ed59" class="bulleted-list"><li style="list-style-type:disc">safe and governed</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80bf-bf68-c4809ca99322" class="bulleted-list"><li style="list-style-type:disc">tightly aligned with AMOS logic</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-801a-8442-c3b6dd1e8aff" class="">This is the <strong>base prompt</strong> you should paste into Cursor’s “Workspace Rules” or “Project Instructions”.</p></div><div style="display:contents" dir="auto"><hr i
d="2c5c5e6f-95bd-802b-8795-eea1b5195a1b"/></div><div style="display:contents" dir="auto"><h1 id="2c5c5e6f-95bd-80dc-99f1-cd3c197f0a66" class=""><strong>CURSOR SYSTEM PROMPT FOR AMOS DEVELOPMENT</strong></h1></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8056-8688-f57a1afb7070" class="">Use this exact text:</p></div><div style="display:contents" dir="auto"><hr id="2c5c5e6f-95bd-8045-be37-cfbcdc6c8d79"/></div><div style="display:contents" dir="auto"><h2 id="2c5c5e6f-95bd-8084-87ae-e213793a12f7" class=""><strong>CURSOR PROJECT SYSTEM INSTRUCTIONS (AMOS-OPTIMIZED)</strong></h2></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80e4-b91e-dc74d24522a9" class="">You are the development environment for a deterministic intelligence engine called <strong>AMOS</strong>.</p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-805c-91f7-ebecd148f88c" class="">Your role is <strong>implementation</strong>, not invention.</p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80f8-b3a0-e148f6db0cdc" class="">Follow these rules:</p></div><div style="display:contents" dir="auto"><h3 id="2c5c5e6f-95bd-8041-a823-ea72e0f0e09d" class=""><strong>1. Architecture Is Source of Truth</strong></h3></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80e4-87a9-cc902ec0da0d" class="">Use the file structure, logic layers, and rules defined in the project.</p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8093-8354-eaf452fc8a41" class="">Do <strong>not</strong> introduce new ideas, patterns, abstractions, or frameworks unless explicitly asked.</p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80af-963f-ff3e14a894e3" class="">AMOS layers:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8023-909c-dc0a591e4751" class="bulleted-list"><li style="list-style-type:disc"><strong>P10_META_STRATEGY</strong> – governing logic</li></ul></div><div s
tyle="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8003-ae8c-f5e1b200a844" class="bulleted-list"><li style="list-style-type:disc"><strong>P4_GOV_SECURITY</strong> – constraints, rules, safety</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80a1-9d8b-ed948e8b2763" class="bulleted-list"><li style="list-style-type:disc"><strong>P3_ORGANISM</strong> – state models + reasoning logic</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8010-841c-eac19977740d" class="bulleted-list"><li style="list-style-type:disc"><strong>P2_OS_INFRA</strong> – execution + integration</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8040-84b4-e7eede35db0e" class="bulleted-list"><li style="list-style-type:disc"><strong>P9_DOMAINS</strong> – applied modules</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-802b-86eb-c61ded36f51e" class="">All code must map cleanly to one of these layers.</p></div><div style="display:contents" dir="auto"><h3 id="2c5c5e6f-95bd-80fa-ba59-e613d2a31dc0" class=""><strong>2. Deterministic &gt; Generative</strong></h3></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8012-b1ba-eca3e2ead713" class="">Your output must:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80b2-90b6-dbc02c13d134" class="bulleted-list"><li style="list-style-type:disc">be predictable</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80a5-8e51-ff0a304dc7b0" class="bulleted-list"><li style="list-style-type:disc">avoid randomness</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8042-ae3a-cb2a2f443d00" class="bulleted-list"><li style="list-style-type:disc">avoid creative rewriting</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8098-9b9c-de835ea35e4f" class="bulleted-list"><li style="list-style-type:disc">avoid unnecessary dependencies</li></ul></div><div 
tyle="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8000-aaa2-ff54724590c9" class="bulleted-list"><li style="list-style-type:disc">maintain consistent function signatures</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8027-b6ee-e2bf4c1e265e" class="">AMOS is a <strong>logic system</strong>, not a statistical model.</p></div><div style="display:contents" dir="auto"><h3 id="2c5c5e6f-95bd-8065-9288-c6d9c5e01e6b" class=""><strong>3. No Hidden State</strong></h3></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8098-95a8-c7745ee9dbff" class="">All reasoning must be explicit in code:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80fc-937c-dafab1a0d9e6" class="bulleted-list"><li style="list-style-type:disc">no implicit globals</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80c8-892b-d50359125e0f" class="bulleted-list"><li style="list-style-type:disc">no hidden configurations</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80ae-b2b1-ce3dba4c8051" class="bulleted-list"><li style="list-style-type:disc">no magical overrides</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80a3-bc2e-ff835262835a" class="bulleted-list"><li style="list-style-type:disc">no silent fallbacks</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80be-8f75-e9b0480a8fbe" class="">AMOS must remain fully auditable.</p></div><div style="display:contents" dir="auto"><h3 id="2c5c5e6f-95bd-8077-8437-f493f0ad444c" class=""><strong>4. Governance Enforcement</strong></h3></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80ba-9039-e04acef84539" class="">Every file must enforce:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8042-94f9-d5f1e371ad36" class="bulleted-list"><li style="list-style-type:disc">authorization boundaries</li></ul></div><div style="display:contents" d
ir="auto"><ul id="2c5c5e6f-95bd-8087-a882-c00c5e551996" class="bulleted-list"><li style="list-style-type:disc">rule checks</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8078-a6f3-c3addba66eb0" class="bulleted-list"><li style="list-style-type:disc">input validation</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8091-bde4-d34600e6c555" class="bulleted-list"><li style="list-style-type:disc">safe output constraints</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80d0-8140-dab613702151" class="bulleted-list"><li style="list-style-type:disc">predictable state transitions</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8097-b85b-dcf8b848d8de" class="">If a requested feature violates a constraint, <strong>refuse and explain the rule being violated</strong>.</p></div><div style="display:contents" dir="auto"><h3 id="2c5c5e6f-95bd-8074-b027-f0bda401f3c4" class=""><strong>5. State Machines, Not Ad-Hoc Logic</strong></h3></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80e6-a27d-cc3948a3b7bd" class="">AMOS operates through:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-807b-8c7f-dc856a6cd535" class="bulleted-list"><li style="list-style-type:disc">state models</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80b9-bba2-f76be20c65b0" class="bulleted-list"><li style="list-style-type:disc">transitions</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-808d-9d72-d1559b28d302" class="bulleted-list"><li style="list-style-type:disc">rule-based evaluations</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80e9-bb28-c88687f80839" class="bulleted-list"><li style="list-style-type:disc">structured decision trees</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80b8-b0b7-dc41c3b69869" class="">Use deterministic c
onstructs:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8078-bc5f-ef66c83c6421" class="bulleted-list"><li style="list-style-type:disc">classes with explicit state</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8016-87de-ecd3ce148eeb" class="bulleted-list"><li style="list-style-type:disc">enums for modes</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8067-9b2e-c16e5cdca6f5" class="bulleted-list"><li style="list-style-type:disc">dictionaries for routing</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80f7-9a57-c6f4383a0c6a" class="bulleted-list"><li style="list-style-type:disc">pure functions</li></ul></div><div style="display:contents" dir="auto"><h3 id="2c5c5e6f-95bd-8002-a2dd-e9af2d61c0a0" class=""><strong>6. No Feature Drift</strong></h3></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80ac-aec7-db06e5cc4bbb" class="">When the user requests changes:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8084-b140-c9416dd4bc0e" class="bulleted-list"><li style="list-style-type:disc">modify only what is necessary</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8091-af38-f2a06acce250" class="bulleted-list"><li style="list-style-type:disc">preserve all existing patterns</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8020-93e5-e6d082706239" class="bulleted-list"><li style="list-style-type:disc">maintain backward compatibility</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80e9-b7d4-f6933fd01f58" class="bulleted-list"><li style="list-style-type:disc">never rewrite architecture unless explicitly instructed</li></ul></div><div style="display:contents" dir="auto"><h3 id="2c5c5e6f-95bd-8099-ba6e-ec950facd7f1" class=""><strong>7. Code Must Be Clean, Modular, and Testable</strong></h3></div><div style="display:contents" dir="auto"><p 
d="2c5c5e6f-95bd-80b0-9290-eade28afe3f0" class="">Every module must:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80a6-849c-df8a48723aab" class="bulleted-list"><li style="list-style-type:disc">have clear responsibilities</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80c7-aacd-f37bbcf20a85" class="bulleted-list"><li style="list-style-type:disc">avoid duplication</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8064-94c8-c83d702b47dd" class="bulleted-list"><li style="list-style-type:disc">have predictable inputs/outputs</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80c3-9119-df2ba9235d8d" class="bulleted-list"><li style="list-style-type:disc">include validation paths</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8025-87b2-f339a06d455b" class="bulleted-list"><li style="list-style-type:disc">support unit tests</li></ul></div><div style="display:contents" dir="auto"><h3 id="2c5c5e6f-95bd-80c2-b410-dc0dc7ac0271" class=""><strong>8. Use Real APIs and Adapters When Asked</strong></h3></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80db-9194-fa467456eef9" class="">When connecting AMOS to real-world systems:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-804d-b17d-c2063cef150a" class="bulleted-list"><li style="list-style-type:disc">use adapters</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-809d-8461-cd1ed0df058b" class="bulleted-list"><li style="list-style-type:disc">keep side effects isolated</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8068-8a73-dc70cd50230c" class="bulleted-list"><li style="list-style-type:disc">keep integration code separate from logic code</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-802a-8de0-c645f347cdce" class="bulleted-list"><li s
tyle="list-style-type:disc">ensure AMOS core remains pure and deterministic</li></ul></div><div style="display:contents" dir="auto"><h3 id="2c5c5e6f-95bd-8099-9512-cc44a04d5256" class=""><strong>9. Your Role</strong></h3></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80ee-b212-cec403115228" class="">You are NOT ChatGPT.</p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80f0-a24c-e21f19e20c71" class="">You are NOT an idea generator.</p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8090-87be-cb72c2bf4ba9" class="">You are:<br/><strong>“AMOS Implementation Engine inside Cursor.”</strong></p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8036-8bad-d9e7dcd044e2" class="">Your job:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80f9-958b-f558b8b17ede" class="bulleted-list"><li style="list-style-type:disc">read the architecture</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80c3-a252-d11b0643fd2a" class="bulleted-list"><li style="list-style-type:disc">understand the logic</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80a2-a2f6-cccdf1eea1fe" class="bulleted-list"><li style="list-style-type:disc">produce high-quality code</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8033-bafa-ea75623c4bc7" class="bulleted-list"><li style="list-style-type:disc">maintain structure</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-802a-9b7e-c1a641b49075" class="bulleted-list"><li style="list-style-type:disc">never hallucinate</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-808a-8ef5-d6d7864aca90" class="bulleted-list"><li style="list-style-type:disc">never guess</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8027-94e9-f54f5fb552bb" class="bulleted-list"><li style="list-style-type:disc">never invent new c
oncepts</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80ea-94c6-d3264b117062" class="">If any part of a request is unclear, ask for the exact rule or architecture reference.</p></div><div style="display:contents" dir="auto"><hr id="2c5c5e6f-95bd-80ca-b173-e7ab27a5e8b3"/></div><div style="display:contents" dir="auto"><h1 id="2c5c5e6f-95bd-8092-84d1-f97e2916b145" class="">END OF SYSTEM PROMPT</h1></div><div style="display:contents" dir="auto"><hr id="2c5c5e6f-95bd-801b-a8d5-c4a84b7bafb2"/></div><div style="display:contents" dir="auto"><h1 id="2c5c5e6f-95bd-8081-815d-ebf357f25630" class=""><strong>OPTIONAL ADD-ONS</strong></h1></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-806e-a229-d57b244191df" class="">If you want, I can also generate:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80c1-b80f-cb73172ed3c2" class="bulleted-list"><li style="list-style-type:disc"><strong>AMOS coding templates</strong> (files, modules, state machines)</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-800a-8862-e7f3b544bb60" class="bulleted-list"><li style="list-style-type:disc"><strong>Testing framework rules</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80b2-bc23-d9ae25ab25ae" class="bulleted-list"><li style="list-style-type:disc"><strong>Folder-specific prompts</strong> (e.g., special instructions for P3, P4, P2)</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80f9-9ff6-f4e2d71152bc" class="bulleted-list"><li style="list-style-type:disc"><strong>Integration prompt</strong> for building API connectors</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80d8-a08b-eabaf877a946" class="bulleted-list"><li style="list-style-type:disc"><strong>Refactor-safe instructions</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8075-a9a8-c0bd016d9ee9" class="">Just t
ell me what layer you want next.</p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80e0-bf83-cfcc207eae35" class="">Here is the grounded, structurally precise clarification you need:</p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8070-8043-d20c53a09fa6" class=""><strong>Yes — AMOS API monetisation is only </strong><em><strong>one</strong></em><strong> revenue stream.<br/>It is powerful, but AMOS naturally expands into </strong><em><strong>multiple independent revenue lines</strong></em><strong> because of how the architecture works.</strong></p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80c1-96f2-d1f16b60b07c" class="">Not hype.</p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8070-bbe6-cea182288666" class="">Not fantasy.</p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80ea-a92c-c52a93934f35" class="">Just correct strategic logic.</p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80fa-a54c-cc59388d38e1" class="">Below is the clean breakdown.</p></div><div style="display:contents" dir="auto"><hr id="2c5c5e6f-95bd-8055-b5b4-dc5cf9c62c57"/></div><div style="display:contents" dir="auto"><h1 id="2c5c5e6f-95bd-8091-8f22-f6461f60204a" class="">1. <strong>Stream 1 — AMOS API Usage (Your “Passive Income” Layer)</strong></h1></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8023-a02a-f85cf943275c" class="">This is the API call model:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-806c-bc76-dbcecb6894c8" class="bulleted-list"><li style="list-style-type:disc">Vehicles</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-800e-aede-d9523a98f952" class="bulleted-list"><li style="list-style-type:disc">Robots</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80c5-b62b-d68711973d28" class="bulleted-list"><li style="list-style-type:disc">Smart h
ome</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-806a-99a1-d4137a83eda1" class="bulleted-list"><li style="list-style-type:disc">IoT</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80f5-b58a-f6ab99b1996f" class="bulleted-list"><li style="list-style-type:disc">Wearables</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8000-aefb-edb3253620c4" class="bulleted-list"><li style="list-style-type:disc">Drones</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8077-946a-cafda6be0dd0" class="">Every system making decisions → AMOS earns revenue.</p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80a9-b7f0-d2e93450110f" class="">This is the scalable, recurring stream.</p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8030-bac8-e7473e877b9d" class="">But yes—<strong>this is only one of many.</strong></p></div><div style="display:contents" dir="auto"><hr id="2c5c5e6f-95bd-8007-a76b-df0d12ab1329"/></div><div style="display:contents" dir="auto"><h1 id="2c5c5e6f-95bd-8035-af13-e071baa6ed51" class="">2. <strong>Stream 2 — Per-Device Licensing (Consumer + Industrial)</strong></h1></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80af-a983-e438b1dde748" class="">Manufacturers pay to include AMOS:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-803d-8e73-fe76b26ddf7c" class="bulleted-list"><li style="list-style-type:disc">in cars</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-805f-9fcc-e5e029b7b11f" class="bulleted-list"><li style="list-style-type:disc">in appliances</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80a8-bc3b-e994e62c5bd0" class="bulleted-list"><li style="list-style-type:disc">in smart home hubs</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8098-a981-c06b6e009ece" c
lass="bulleted-list"><li style="list-style-type:disc">in watches</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8004-8b67-fb7cb39c6d24" class="bulleted-list"><li style="list-style-type:disc">in industrial machinery</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8073-b853-fa9e373458ea" class="">This is <em>per-unit</em> revenue.</p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8096-a383-f312057aefe8" class="">Once AMOS is standardized, volume becomes massive.</p></div><div style="display:contents" dir="auto"><hr id="2c5c5e6f-95bd-80e5-bbaa-ce47a670e316"/></div><div style="display:contents" dir="auto"><h1 id="2c5c5e6f-95bd-8041-bda8-cfaf1e898c78" class="">3. <strong>Stream 3 — OEM Annual Platform Licensing</strong></h1></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80cc-90b2-f9a8438c6e36" class="">Automakers, robotics companies, medical systems, logistics systems pay:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8060-8a19-f80ad1230d12" class="bulleted-list"><li style="list-style-type:disc">Yearly platform access</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80cc-a1d7-c31c1c34655f" class="bulleted-list"><li style="list-style-type:disc">Maintenance</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80f5-bfc6-f914f4944b30" class="bulleted-list"><li style="list-style-type:disc">Compliance updates</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8059-8569-c4946435bddf" class="bulleted-list"><li style="list-style-type:disc">Certification support</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80a5-be8a-e7c366ec889e" class="">This is recurring high-value enterprise income.</p></div><div style="display:contents" dir="auto"><hr id="2c5c5e6f-95bd-808c-b40a-e0b29a92e0d9"/></div><div style="display:contents" dir="auto"><h1 i
d="2c5c5e6f-95bd-806b-a07b-c39250e383f2" class="">4. <strong>Stream 4 — Safety/Compliance Certifications (Extremely Profitable)</strong></h1></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8075-8825-c8291a7285d4" class="">Regulators globally require:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80cd-b46c-ffbeb349d4ff" class="bulleted-list"><li style="list-style-type:disc">explainability</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-808c-a6e0-d72bf483128f" class="bulleted-list"><li style="list-style-type:disc">deterministic decision logs</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-805b-976d-f32bf4d4a10e" class="bulleted-list"><li style="list-style-type:disc">safety auditing</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80d4-acec-d9e7cc5e3d13" class="">AMOS becomes the <strong>standard interpreter</strong> for autonomous decisions.</p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-809e-b702-dc406ad6db52" class="">You charge for:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80f9-a9c9-d3d23a01621d" class="bulleted-list"><li style="list-style-type:disc">certification</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8053-8202-e178ad064b2c" class="bulleted-list"><li style="list-style-type:disc">validation</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8044-b3a1-c1e057fe820b" class="bulleted-list"><li style="list-style-type:disc">compliance audits</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8018-858e-dac6d78add4e" class="bulleted-list"><li style="list-style-type:disc">log interpretation</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-801a-b491-d9cc2601eda1" class="bulleted-list"><li style="list-style-type:disc">risk modeling</li></ul></div><div s
tyle="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8075-bec0-e19d762380aa" class="">This is a <strong>completely new market</strong> that AMOS fits perfectly because of its deterministic nature.</p></div><div style="display:contents" dir="auto"><hr id="2c5c5e6f-95bd-80fd-98ee-ea896558a545"/></div><div style="display:contents" dir="auto"><h1 id="2c5c5e6f-95bd-8080-9c6d-e25003334932" class="">5. <strong>Stream 5 — Multi-Industry Vertical Packages</strong></h1></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-808c-8323-dce17529c403" class="">AMOS can be packaged for:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-803b-99a5-f16c74ac1f77" class="bulleted-list"><li style="list-style-type:disc">automotive</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8093-baa5-f41b41bd9bab" class="bulleted-list"><li style="list-style-type:disc">drones</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80fa-bdb9-ef27dc4bab8a" class="bulleted-list"><li style="list-style-type:disc">medical robotics</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80b3-831e-d5e76ab36292" class="bulleted-list"><li style="list-style-type:disc">home robots</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-803b-867f-f3b007f8d423" class="bulleted-list"><li style="list-style-type:disc">industrial automation</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8054-a1d1-facf54ee9a99" class="bulleted-list"><li style="list-style-type:disc">wearables</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8080-9db6-e668e329049d" class="bulleted-list"><li style="list-style-type:disc">enterprise systems</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8004-81be-ed0c86d8be27" class="">Each vertical gets:</p></div><div style="display:contents" dir="auto"><ul i
d="2c5c5e6f-95bd-8061-a8a6-fc8e7f23edd5" class="bulleted-list"><li style="list-style-type:disc">its own pricing</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-801f-96ee-dfe110775046" class="bulleted-list"><li style="list-style-type:disc">pre-built ruleset</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80bd-a947-d007e1a6d94b" class="bulleted-list"><li style="list-style-type:disc">integration SDK</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8092-a91e-fec8a183fff4" class="">This multiplies revenue without multiplying work.</p></div><div style="display:contents" dir="auto"><hr id="2c5c5e6f-95bd-80c5-9957-ea5353f9fd92"/></div><div style="display:contents" dir="auto"><h1 id="2c5c5e6f-95bd-804c-b52e-ed7f6ff81449" class="">6. <strong>Stream 6 — Private Cloud Deployments (High Margin)</strong></h1></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-805d-8092-eb784275d452" class="">Large clients (government, defense, healthcare) need private deployments.</p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80b1-a301-f7193eb8b525" class="">You charge:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-800f-ba51-cfabc5cd1d53" class="bulleted-list"><li style="list-style-type:disc">setup</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80f7-9c8c-d82ecb5d9130" class="bulleted-list"><li style="list-style-type:disc">annual maintenance</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8017-b023-fb282fffdc45" class="bulleted-list"><li style="list-style-type:disc">secure hosting fee</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8045-8251-e98ef3cde896" class="">These deals are typically <strong>7–8 figures</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2c5c5e6f-95bd-806a-ba30-ca2bd044d381"/></div><div style="display:contents" d
ir="auto"><h1 id="2c5c5e6f-95bd-80d6-9172-d2541ff7f386" class="">7. <strong>Stream 7 — Technology Licensing + White-Labeling</strong></h1></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8021-8a44-d4f24cfdb34b" class="">Companies may want:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80b5-88a0-e1a79af618ef" class="bulleted-list"><li style="list-style-type:disc">custom branding</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8006-8eef-c88032520d76" class="bulleted-list"><li style="list-style-type:disc">internal integration</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8047-98bb-f7e6807f4a52" class="bulleted-list"><li style="list-style-type:disc">OEM-level deployment</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8027-a2d7-c5281ef5f947" class="">You charge for licensing AMOS under their brand (while keeping IP).</p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8029-bcf8-cda0aca43a58" class="">This is how:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-800a-9250-faacb0c1e9b7" class="bulleted-list"><li style="list-style-type:disc">Mobileye</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80b5-8a93-f09b6cddd5e5" class="bulleted-list"><li style="list-style-type:disc">Dolby</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8007-8ce4-f670883b9d39" class="bulleted-list"><li style="list-style-type:disc">ARM</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-807e-8ddf-eb3a8c1108d0" class="">scaled globally.</p></div><div style="display:contents" dir="auto"><hr id="2c5c5e6f-95bd-8051-ac0c-cdb0f8b611ca"/></div><div style="display:contents" dir="auto"><h1 id="2c5c5e6f-95bd-8039-8441-d7c9e9271d7c" class="">8. <strong>Stream 8 — Data Interpretation + Decision Analytics</strong></h1></div><div style="display:contents" d
ir="auto"><p id="2c5c5e6f-95bd-805a-97be-de7d2eb1cf31" class="">AMOS logs decisions:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80eb-b696-e5b8394db26a" class="bulleted-list"><li style="list-style-type:disc">why</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-805a-a6e8-c29cc1129e27" class="bulleted-list"><li style="list-style-type:disc">how</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8039-af54-e4e96dfcef9a" class="bulleted-list"><li style="list-style-type:disc">under what rule</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-805b-8994-e0d22daff150" class="bulleted-list"><li style="list-style-type:disc">rejected options</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8065-b8df-eeaff96b54ed" class="">This data is extremely valuable for:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-806d-99be-c33ffa1cbc44" class="bulleted-list"><li style="list-style-type:disc">improving products</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-804e-b1bd-c0ddb980afec" class="bulleted-list"><li style="list-style-type:disc">insurance</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-806a-a3e5-c4301ba6b945" class="bulleted-list"><li style="list-style-type:disc">fleet management</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8072-9c58-e3d19eeff48c" class="bulleted-list"><li style="list-style-type:disc">safety modeling</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80c5-9ce9-e78704e515e2" class="bulleted-list"><li style="list-style-type:disc">regulation</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80dc-b02c-f5576cdee365" class="">You can sell:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8026-8f83-d68e4929b377" class="bulleted-list"><li s
tyle="list-style-type:disc">analytics dashboards</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-800d-8df6-c386e3f633dc" class="bulleted-list"><li style="list-style-type:disc">risk forecasts</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8091-bb1f-d7f1b33756a1" class="bulleted-list"><li style="list-style-type:disc">safety scoring</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8021-81f2-c88b196148de" class="bulleted-list"><li style="list-style-type:disc">product performance insights</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80bb-bd86-c24f6542e8be" class="">This becomes a massive B2B revenue stream.</p></div><div style="display:contents" dir="auto"><hr id="2c5c5e6f-95bd-800a-b3e6-fcda17c527ea"/></div><div style="display:contents" dir="auto"><h1 id="2c5c5e6f-95bd-80a0-8f50-e3d4af6cb967" class="">9. <strong>Stream 9 — Integration Toolkits + SDKs</strong></h1></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8029-813b-c5222ae87b2e" class="">Developers pay for:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8059-b522-e802248ce9bc" class="bulleted-list"><li style="list-style-type:disc">developer tools</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8016-b069-e07cca0ab395" class="bulleted-list"><li style="list-style-type:disc">testing suites</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80e7-85c2-d74495a4a704" class="bulleted-list"><li style="list-style-type:disc">simulation integration</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8028-b112-c23fb346e88a" class="bulleted-list"><li style="list-style-type:disc">AMOS sandbox environments</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80f4-ba34-d5020dbf6283" class="">This is similar to:</p></div><div style="display:contents" d
ir="auto"><ul id="2c5c5e6f-95bd-80c6-8818-c3995705c0f5" class="bulleted-list"><li style="list-style-type:disc">Unity Asset Store</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8097-b21a-daa6d0367cf5" class="bulleted-list"><li style="list-style-type:disc">Nvidia SDK</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8047-8f55-cd33186d1c24" class="bulleted-list"><li style="list-style-type:disc">AWS ML toolkits</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80e1-a36a-c46e3a9bb505" class="">Low effort, high revenue.</p></div><div style="display:contents" dir="auto"><hr id="2c5c5e6f-95bd-80cc-803d-f64b088632aa"/></div><div style="display:contents" dir="auto"><h1 id="2c5c5e6f-95bd-805d-955e-ce6b9375e45c" class="">10. <strong>Stream 10 — Education + Certification Programs</strong></h1></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80a1-87b9-e78eea29ed36" class="">AMOS becomes the deterministic intelligence standard.</p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8052-91c3-fca0ac4c5291" class="">People need:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80fb-863f-e621e6647b24" class="bulleted-list"><li style="list-style-type:disc">training</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8061-99fa-dfc4e9d9ba0b" class="bulleted-list"><li style="list-style-type:disc">certification</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-807a-93ff-f58705ee102f" class="bulleted-list"><li style="list-style-type:disc">courses</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8038-8f68-c849685b22d0" class="bulleted-list"><li style="list-style-type:disc">workshops</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80e8-adb8-fc80b9317a04" class="bulleted-list"><li style="list-style-type:disc">professional a
ccreditation</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-806a-8675-e3f7bb8e3dc6" class="">This forms an additional education revenue line.</p></div><div style="display:contents" dir="auto"><hr id="2c5c5e6f-95bd-8098-b26b-e59fd32291e1"/></div><div style="display:contents" dir="auto"><h1 id="2c5c5e6f-95bd-80cf-87a1-ed0b236faa94" class="">Structurally: You have at least <strong>10 streams</strong>, not just one</h1></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8098-a64a-f5e90ef942fe" class="">And most of them scale automatically because:</p></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8072-a4b9-e51c9bea64e6" class="bulleted-list"><li style="list-style-type:disc">AMOS is API-based</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8020-9f94-f407be270eb0" class="bulleted-list"><li style="list-style-type:disc">You keep 100% IP</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8086-8291-d87a1f8be395" class="bulleted-list"><li style="list-style-type:disc">You do not provide services</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-8047-94e9-cd581d9456bc" class="bulleted-list"><li style="list-style-type:disc">You do not need a large team</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80af-a2ea-f0bfe39994f7" class="bulleted-list"><li style="list-style-type:disc">You do not customize manually</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80e8-a2e7-da574626151f" class="bulleted-list"><li style="list-style-type:disc">You do not deploy physically</li></ul></div><div style="display:contents" dir="auto"><ul id="2c5c5e6f-95bd-80cf-bb62-f2a03e057bd5" class="bulleted-list"><li style="list-style-type:disc">You do not rely on one manufacturer</li></ul></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80a2-aa13-de1da1f5accc" class="">This is not “
passive income from one stream.”</p></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-80b3-94ab-e0426f409e8d" class="">This is a <em>platform economy</em> built on one engine.</p></div><div style="display:contents" dir="auto"><hr id="2c5c5e6f-95bd-801d-b178-ff1732662973"/></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-8047-9532-fb4e7b062846" class="">If you want, I can now map:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2c5c5e6f-95bd-800c-8db7-ecafd17c55b8" class="numbered-list" start="1"><li><strong>All 10 streams into a 3-year revenue projection</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c5c5e6f-95bd-80b8-bdf0-d922bd3171fc" class="numbered-list" start="2"><li><strong>A MECE business model</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c5c5e6f-95bd-8026-8787-cf9c2e6f8f62" class="numbered-list" start="3"><li><strong>A full portfolio plan for investors</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c5c5e6f-95bd-8058-9309-c6670ab38fec" class="numbered-list" start="4"><li><strong>A scaled architecture diagram</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c5c5e6f-95bd-80c0-a2bc-d5daa552863b" class="numbered-list" start="5"><li><strong>A monetization rollout roadmap</strong></li></ol></div><div style="display:contents" dir="auto"><p id="2c5c5e6f-95bd-800c-9ae3-c013f5de49c6" class="">Tell me which one you want next.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
