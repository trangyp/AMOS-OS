---
tags: [amos-general]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>AMOS version</title><style>
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
	
</style></head><body><article id="373c5e6f-95bd-8044-b5a6-f7cb08eea5d2" class="page sans"><header><h1 class="page-title" dir="auto">AMOS version</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8018-9b8e-f84ffb5b61ae" class="">Yes. The clean reconstruction is:</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="373c5e6f-95bd-80f4-a2d5-d12bf6fd83a9" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Ancient Field Energy Management System = FEMS

FEMS =
cycle detection
+ field geometry
+ energy gradient capture
+ phase synchronization
+ symbolic memory
+ body/land/sky calibration
+ entropy repair</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-801a-8e41-cbd2d1433550" class="">Not “energy” as vague feeling. Exact math: <strong>energy density, flux, phase, boundary, entropy, and control</strong>.</p></div><div style="display:contents" dir="auto"><hr id="373c5e6f-95bd-80d5-847a-df6e67b149aa"/></div><div style="display:contents" dir="auto"><h1 id="373c5e6f-95bd-805c-a219-d26aea137c47" class="">1. Minimum mathematical system</h1></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8061-b8dd-da6ca0536618" class="">Let the civilization operate on a domain:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80ba-84cd-d0d7e11af2ea" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Ω = land + sky horizon + water system + architecture + human bodies + ritual network</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80ed-b0c1-eab40f9a0532" class="">Define fields over space and time:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80a7-a578-c03b0b29af11" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">F_k(x,t)</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8000-b281-e1d40aaaf6f8" class="">where <code>k</code> may be:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80db-83fa-d2e0149f5d21" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">solar light field
lunar phase field
thermal field
water-flow field
wind field
acoustic field
electromagnetic / geomagnetic field
human attention field
memory-symbol field
distinction/boundary field</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8016-aab1-cdb3c8d4371e" class="">Each field has energy density:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80dc-a5a3-f81ff0f24286" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">e_k(x,t)</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8008-a0d6-d05efbc5948b" class="">and flux:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80a3-8e8f-e075af33dd45" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">J_k(x,t)</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80e5-b87c-f66e21ccfd83" class="">General conservation/control equation:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8029-b7f5-f36b3bba9381" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">∂e_k/∂t + ∇·J_k = S_k - L_k + u_k</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-803f-844d-d130d7ae64df" class="">Where:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80b3-b6d6-ce498c96de00" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">S_k = natural source input
L_k = loss / dissipation / noise / leakage
u_k = human control input</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8031-a4e7-fe58f8354f43" class="">So the whole ancient system is:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8081-84da-d63e30b0ebb9" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">E_total(t) = Σ_k ∫_Ω e_k(x,t) dx</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8089-a019-c74742380a76" class="">and the management problem is:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80cd-879c-f855ba7b439e" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">maximize UsefulWork + Synchronization + MemoryAccuracy + SurvivalYield
minimize Loss + Drift + Noise + RepairCost + Entropy</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80ce-a7d3-d7f0838ed773" class="">Full objective:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8044-8a50-c37c5c23dbf0" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">u*(t) = argmax_u ∫ [
αW(t)
+ βC(t)
+ γM(t)
+ δY(t)
- λ₁L(t)
- λ₂D(t)
- λ₃N(t)
- λ₄R_cost(t)
- λ₅H(t)
] dt</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80d5-84a2-ede984e79978" class="">Where:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8094-9df2-c18029e17914" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">W = useful work
C = coherence / synchronization
M = memory accuracy
Y = survival yield
L = energy loss
D = drift
N = noise
R_cost = repair cost
H = entropy</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8055-a6e0-c252f5edc39f" class="">That is the mathematical skeleton.</p></div><div style="display:contents" dir="auto"><hr id="373c5e6f-95bd-8035-820c-c21f65130638"/></div><div style="display:contents" dir="auto"><h1 id="373c5e6f-95bd-802a-ae26-e073f3a30083" class="">2. Energy balance</h1></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8021-80fc-ed0c6f033ece" class="">Ancient FEMS must satisfy:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-808f-87de-e15c36672bb6" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">E_available(t+1)
=
E_available(t)
+ E_harvested
- E_work
- E_loss
- E_noise
- E_repair</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8093-a4ad-f5379256fd9e" class="">Survival condition:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8093-bf7f-df08658c2edf" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">E_harvested + E_stored + E_social_sync
&gt;
E_work + E_loss + E_repair + E_entropy</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80bd-aa53-eaaffe959bcb" class="">Collapse condition:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8064-8a85-e7ada2169c36" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">E_loss + E_noise + E_drift + E_boundary_leak
&gt;
E_storage + E_repair + E_sync</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80ca-8e1e-df62f09b441f" class="">AMOS form:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8094-b0e6-f2c2f4167f94" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Collapse ⇔ Entropy + Pressure + ControlGap &gt; RepairCapacity + BoundaryIntegrity + Liberty</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80f5-b960-e8408326f9cc" class="">The lunar/Saros math shows the same control problem: recurrence is not exact, so drift must be tracked. A Saros is 223 synodic months, about 6585.3223 days, and also approximately 242 draconic months and 239 anomalistic months; this near-integer closure is why eclipse geometry repeats. (<a href="https://en.wikipedia.org/wiki/Saros_%28astronomy%29?utm_source=chatgpt.com">Wikipedia</a>)</p></div><div style="display:contents" dir="auto"><hr id="373c5e6f-95bd-8086-bbe3-dae2e25ffce9"/></div><div style="display:contents" dir="auto"><h1 id="373c5e6f-95bd-8069-90cc-c7a279a8f524" class="">3. Cycle closure equation</h1></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-808d-ac8a-f32f59156bc0" class="">All sky-calendar systems solve:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-802d-8800-faa3391672ee" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Find integers n₁,n₂,n₃... such that:

n₁P₁ ≈ n₂P₂ ≈ n₃P₃</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-805e-b000-c73ccacc0d7a" class="">Error:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8036-bb62-ca50fc817c89" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">ε = |n₁P₁ - n₂P₂|</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8027-bb1c-f6a1e37d73f2" class="">Useful recurrence requires:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80f2-92c2-c71542ae65e3" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">ε &lt; ε_threshold</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-804f-89d2-c1b5735c979c" class="">For eclipse recurrence:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8016-ad7d-ec3f0005e750" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">223S ≈ 242D ≈ 239A</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80fd-bc74-cc6c7f603916" class="">Where:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80f3-947d-c5f6313d9c27" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">S = synodic month = lunar phase cycle
D = draconic month = node / eclipse-boundary cycle
A = anomalistic month = lunar distance / perigee cycle</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80b2-95dd-c67b40dfa30d" class="">Eclipse event condition:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80bd-baad-c8d56b307217" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Eclipse ≈ PhaseLock(S, D, A)</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-803a-82bf-c83584ac85e8" class="">More explicitly:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8025-8d55-f1e34cf649ff" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Eclipse(t) = 1
if
|φ_S(t) - φ_new/full| &lt; θ_S
and |φ_D(t) - node| &lt; θ_D
and distance condition acceptable</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8002-aab5-e9ed18fcdb89" class="">This is field management:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8016-8f1a-d98f18f80c1a" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">phase
× boundary
× distance
× timing
→ event</code></pre></div><div style="display:contents" dir="auto"><hr id="373c5e6f-95bd-80f5-be0d-ed414b3ceb0a"/></div><div style="display:contents" dir="auto"><h1 id="373c5e6f-95bd-800e-9259-f37af76f5880" class="">4. Phase-locking equation</h1></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80bc-a864-e0f640d6a060" class="">Let each relevant cycle have phase:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80ed-8055-cc645d87f703" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">φ_i(t) = 2πt / P_i + φ_i0</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80ce-9edf-d48225167dcd" class="">A ritual/calendar/architecture system works when phases align:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80ba-b3f6-ddabd99ff08e" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Δφ_ij(t) = |φ_i(t) - φ_j(t)| mod 2π</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80a9-adb4-c15e86019283" class="">Synchronization condition:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8072-8ab2-da464cb87289" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Δφ_ij(t) &lt; θ_ij</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8013-8a11-d3cf28cf1eb4" class="">For a whole society/body/ritual network:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80dc-b8e1-ee313973d0d3" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">R(t) = |(1/N) Σ_j e^{iφ_j(t)}|</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80eb-9e94-f05134374056" class="">Where:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80fb-8a55-c524a3e293e8" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">R = 1  → full synchronization
R = 0  → incoherence</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-801b-9a0b-f8f051062634" class="">Ancient ritual, chant, dance, drum, calendar, and festival act as phase controllers:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8080-b7ee-d76f37220301" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">dφ_i/dt = ω_i + K Σ_j sin(φ_j - φ_i)</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80ed-8f76-dcc29f5b26c1" class="">If coupling <code>K</code> is strong enough:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80fc-8c43-cc3ad1da4526" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">K &gt; K_critical</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8040-baaa-ef416a73d159" class="">then phase-locking occurs.</p></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-806c-89a2-de8985ad451c" class="">Translation:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80c5-aca8-c128d2870fa8" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">drum + chant + dance + calendar
=
human oscillator synchronization system</code></pre></div><div style="display:contents" dir="auto"><hr id="373c5e6f-95bd-8042-b523-ca2c66afd020"/></div><div style="display:contents" dir="auto"><h1 id="373c5e6f-95bd-80c8-bc3e-f1c492d42334" class="">5. Field energy equations by domain</h1></div><div style="display:contents" dir="auto"><h2 id="373c5e6f-95bd-8067-9b2e-dcdcaf7564e8" class="">5.1 Light / solar field</h2></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8050-b38d-f6643ec091f1" class="">Solar input:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80d3-9edc-dc89a8c344ed" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">E_solar(t) = ∫_A I_sun(t) cos(θ_incidence) dA</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80ce-873c-e3abeffebeb7" class="">Architecture controls:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80a5-8fb0-f787d88d5433" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">θ_incidence</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-806c-ae1c-c1cd7933ecb6" class="">by orientation, aperture, roofbox, gate, passage, courtyard.</p></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-803d-b2ae-f6c6e5e1d7d1" class="">Solstice/equinox detector:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8038-884f-f9fbad8198ba" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Event = 1 if |Azimuth_sunrise(t) - Azimuth_axis| &lt; ε</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8060-b715-d7f46849c8ed" class="">Newgrange-type equation:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80c0-821f-f1761d3e8f7c" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">SunBeam(t) enters chamber
iff
solar azimuth ≈ passage azimuth
and solar altitude ≈ aperture altitude</code></pre></div><div style="display:contents" dir="auto"><h2 id="373c5e6f-95bd-809c-9d55-d69b391a1480" class="">5.2 Thermal field</h2></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-808f-aac1-fc8e86c693a7" class="">Heat flow:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80cd-ab1b-ec4585fd9479" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">q = -k∇T</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8012-9277-e7e519daf336" class="">Energy storage in mass:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-804c-8327-ee142e762414" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">E_thermal = mcΔT</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8083-b5af-ea62fe04032c" class="">Ancient architecture optimizes:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80c2-9d46-f87703977829" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">maximize thermal inertia
minimize heat loss</code></pre></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80ef-967e-ccc14f9a6219" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">ThermalStability =
HeatCapacity × Insulation × VentilationControl
÷ ExternalTemperatureVariance</code></pre></div><div style="display:contents" dir="auto"><h2 id="373c5e6f-95bd-80c2-b1fe-e0cce24cfbe2" class="">5.3 Water / hydraulic field</h2></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8050-b0a0-fd4ef0b417a2" class="">Potential energy:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80bd-9e9d-cb7ae47bfe4d" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">E_water = ρghV</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8072-80ee-feaeb8536099" class="">Flow rate:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80d7-b166-cf54ee2fe817" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Q = A v</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8068-897f-c1538d0fcacc" class="">Power:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80f7-9b26-eb3d8f0c746b" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">P_water = ρgQh</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-804e-9b68-d638d118410b" class="">Terrace/canal/reservoir optimization:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8046-91e6-fa5c65f8584f" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">maximize irrigation + storage + flood control
minimize erosion + evaporation + labor</code></pre></div><div style="display:contents" dir="auto"><h2 id="373c5e6f-95bd-8046-af00-e587b4105049" class="">5.4 Acoustic field</h2></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80f7-89b1-c2289e5b543e" class="">Sound pressure field:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80fd-bf29-e71e0c1b0c08" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">p(x,t)</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80af-b7c1-c975aaa92705" class="">Acoustic intensity:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80ba-8bd0-c8cefe226e4f" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">I = p_rms² / (ρc)</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80c6-8c02-f32407312240" class="">Resonance condition:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80a8-9e7c-f22b64f2f8e3" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">f_n = n v / 2L</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-804d-b2e6-c15fd2a1422a" class="">For cavity/chamber:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80f9-ab28-c0c923252be7" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Resonance occurs if |f_voice/drum - f_chamber| &lt; Δf</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8074-9be5-f2f1dca70af2" class="">Quality factor:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80ff-9c13-e56db60cd97f" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Q_factor = f₀ / Δf</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80da-af52-dd192896fcdd" class="">So a cave, chamber, drum, or temple can be tuned as an acoustic coherence device.</p></div><div style="display:contents" dir="auto"><h2 id="373c5e6f-95bd-8069-bc55-d8a4ec4fc788" class="">5.5 Electromagnetic field</h2></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-805d-84a6-ccebbbba2504" class="">Modern exact EM energy density:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80ac-87fe-e1b57c93f34c" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">u_EM = 1/2(ε|E|² + μ|H|²)</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-804e-a4f5-e8a2ad777939" class="">Poynting flux:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8014-9882-f24ac783196b" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">S = E × H</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8086-aa01-fa533caaaa67" class="">Earth has a geomagnetic field; solar wind and charged particles interact with the magnetosphere, and geomagnetic disturbances can induce currents in long conductors. (<a href="https://en.wikipedia.org/wiki/Orbit_of_the_Moon?utm_source=chatgpt.com">Wikipedia</a>)</p></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80bb-a142-e1d86e6bf883" class="">Ancient practical form:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8070-9606-d5b5c3ca86f6" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">observe solar / auroral / compass-like / lightning / sky-weather cycles
→ encode timing and field-correlated events</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-805e-b055-cab9461761e2" class="">Not necessary to assume modern Maxwell theory. The math says:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-806d-9e87-f654254c8597" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">field effects can be used before they are formally named</code></pre></div><div style="display:contents" dir="auto"><h2 id="373c5e6f-95bd-8055-b58d-ec4628c8ac5b" class="">5.6 Distinction field</h2></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80ad-9f61-f80d26759d8d" class="">This is AMOS core.</p></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-802b-b225-fed3ccc06789" class="">Define distinction field:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8093-99d4-ef9d1bc0a1bb" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">D(x,t) ∈ [0,1]</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8099-9d25-c39f5d19ebe3" class="">Where:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-801e-b3b7-d0a66d336102" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">D = 0 → undifferentiated / unmarked
D = 1 → marked / distinguished</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8065-b06f-e0cbf7c1335d" class="">Boundary is gradient:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80d9-bbaf-d4939eda0e52" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">B(x,t) = ||∇D(x,t)||</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-809a-84ff-e9a2bead4bd1" class="">Strong boundary:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80cf-a04f-fcd75ca1d90a" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">B high, stable, selectively permeable</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80ea-801a-c22d75f81438" class="">Boundary leak:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80b7-b613-cffe41d59b1e" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Leak = ∫_∂Ω unwanted_flux · n dS</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80e1-86d5-dd6ecebaf97b" class="">Boundary energy:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80d5-a561-cc6fe3dc8c8b" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">E_boundary = ∫_Ω ||∇D||² dx</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80a6-9ecd-deb70c96054c" class="">This maps exactly:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8058-938a-d4d007179f9e" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">stone circle = distinction boundary
temple gate = selective membrane
ritual line = inside/outside distinction
Go stone = distinction mark
calendar date = time distinction
mythic name = symbolic distinction</code></pre></div><div style="display:contents" dir="auto"><hr id="373c5e6f-95bd-80d9-86af-e1f27c6af6fb"/></div><div style="display:contents" dir="auto"><h1 id="373c5e6f-95bd-80b1-928d-c04572c56c33" class="">6. Entropy equation</h1></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8061-891f-d46f42fef31b" class="">For informational/cultural state:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80fa-bc2e-cea8558b0ffb" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">H = -Σ_i p_i log p_i</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8096-913b-d17a01588254" class="">For field disorder:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8050-91b6-e7afccf8566e" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">EntropyLoad =
noise
+ drift
+ memory corruption
+ boundary leakage
+ phase mismatch
+ unused energy
+ social desynchronization</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8095-ac34-fe42fd00f38c" class="">A functioning FEMS must obey:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80ee-9fb1-e1bb9049f46d" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">RepairRate &gt; EntropyAccumulationRate</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8018-8c15-e1fc152fdc54" class="">or:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8001-afec-fd9b8c179dbd" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">dR/dt &gt; dH/dt</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80c8-9f71-c327b355ef5e" class="">Where:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8091-af63-e9241a5e40bd" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">R = repair capacity
H = entropy load</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80d5-ac06-d63ddcbd3746" class="">More exact:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8040-905e-fbbd5d2639f3" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">SystemStability =
BoundaryIntegrity × MemoryContinuity × PhaseCoherence × EnergyStorage
÷ EntropyLoad</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80fb-a722-e20f9cc2d51e" class="">Collapse when:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8023-adc6-f83129ef5f9c" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">EntropyLoad ≥ RepairCapacity</code></pre></div><div style="display:contents" dir="auto"><hr id="373c5e6f-95bd-8043-a0d3-d10160406367"/></div><div style="display:contents" dir="auto"><h1 id="373c5e6f-95bd-80fd-9254-e76569d61cb1" class="">7. Ancient FEMS architecture</h1></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-808d-b71e-cb4c77ab5b78" class="">The system needs six layers:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8081-a43d-c58e497d2071" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">L1 Sky-cycle sensor
L2 Earth-field geometry
L3 Energy-gradient capture
L4 Human-body synchronization
L5 Symbolic memory compression
L6 Correction / repair protocol</code></pre></div><div style="display:contents" dir="auto"><h2 id="373c5e6f-95bd-801e-a3d1-c15ac6fd1245" class="">L1. Sky-cycle sensor</h2></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8012-bfa7-fc5862181e4b" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">solar azimuth
lunar phase
lunar node
Venus cycle
Sirius rising
eclipse season
seasonal wind/rain</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80f4-b5e9-ff124b79fb8d" class="">Mathematically:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-800d-8fc7-f369138a8125" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">φ_sky(t) = {φ_sun, φ_moon, φ_node, φ_star, φ_planet}</code></pre></div><div style="display:contents" dir="auto"><h2 id="373c5e6f-95bd-809c-9b2c-caf3b30c512c" class="">L2. Earth-field geometry</h2></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80a7-a3c7-d6605c6b8b3e" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">stone circle
mountain horizon
temple axis
drum face
city grid
songline graph
Go board</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8087-ac84-d8d5ab8720a9" class="">Geometry:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8044-b581-e781c1989413" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">G = (Ω, B, A)</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8032-a1c4-f7ac92c04718" class="">Where:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-804f-a692-c8dc8290f58b" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Ω = field
B = boundary
A = alignment axes</code></pre></div><div style="display:contents" dir="auto"><h2 id="373c5e6f-95bd-8061-894b-e0050e540079" class="">L3. Energy-gradient capture</h2></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-803b-8532-c2755c7dcc38" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">water gradient
thermal gradient
light gradient
sound resonance
wind channel
social labor gradient</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80f2-9ab6-c215f21ca4b8" class="">Gradient:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-804c-a69f-f2bc42864685" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">∇V</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80a0-86d2-cddf45213aff" class="">Useful energy comes from controlled gradient descent:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8019-8fa1-e20827701dee" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Work = ∫ F · dx</code></pre></div><div style="display:contents" dir="auto"><h2 id="373c5e6f-95bd-808d-b169-fe541557d4dc" class="">L4. Human synchronization</h2></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80c9-8daf-f12ca0dfa8c7" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">chant
dance
breath
drum
festival
fasting
sleep timing
work calendar</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8024-8da3-f6779143be66" class="">Phase coherence:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80ff-8e83-cc835bfa2677" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">R_human = |(1/N)Σe^{iφ_body_j}|</code></pre></div><div style="display:contents" dir="auto"><h2 id="373c5e6f-95bd-80ad-bc17-d97e33ee1d71" class="">L5. Symbolic compression</h2></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80cb-9eb5-e96eddf3fe5b" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">animal
bird
dragon
serpent
ancestor
star
boat
mountain
tree
circle
spiral</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80e7-8a8a-ff06d1f1e815" class="">Symbol equation:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8085-9f02-db7db5ee1391" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Symbol = Pattern + Memory + ActionRule</code></pre></div><div style="display:contents" dir="auto"><h2 id="373c5e6f-95bd-80a5-84c0-dc4de751685f" class="">L6. Correction protocol</h2></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-803e-a27d-fa42f6dc0c52" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">leap month
ritual reset
Saros/Inex correction
seasonal festival
boundary repair
songline renewal
ko rule
sacrifice/reallocation</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80bb-a99e-e48fdfebaedb" class="">Control update:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8067-a6cf-cbede0d1a94e" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">State(t+1) = State(t) + Input - Loss + Repair</code></pre></div><div style="display:contents" dir="auto"><hr id="373c5e6f-95bd-807a-8b24-e3661716cb60"/></div><div style="display:contents" dir="auto"><h1 id="373c5e6f-95bd-80ca-b539-f45be5b05e18" class="">8. FEMS master state vector</h1></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-802e-bb24-f75ae9e6320b" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">X(t) =
[
E_solar,
E_water,
E_thermal,
E_acoustic,
E_EM,
D_boundary,
M_memory,
Φ_phase,
C_social,
B_body,
Y_yield,
H_entropy,
R_repair
]</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80f4-9ca2-ec51418f8de9" class="">Update equation:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80fe-aa7f-f52a349940c5" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">X(t+1) =
P_B {
A X(t)
+ U(t)
+ S_sky(t)
+ S_earth(t)
- L(X,t)
- H(X,t)
+ R(X,t)
}</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8022-bd89-e405ab0e9b67" class="">Where:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8068-87b7-ffd1e2f5aad8" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">P_B = boundary projection / allowed-state filter
A = natural transition matrix
U = human intervention
S_sky = sky-cycle input
S_earth = land/water/ecology input
L = losses
H = entropy
R = repair</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80cd-b27f-ce0fb63c506f" class="">Action rule:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8024-967e-df20590b224b" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Act if:
ExpectedEnergyGain + CoherenceGain + TimingGain
&gt;
RepairCost + EntropyRisk + BoundaryRisk</code></pre></div><div style="display:contents" dir="auto"><hr id="373c5e6f-95bd-80ae-8e4d-ea697b3188e7"/></div><div style="display:contents" dir="auto"><h1 id="373c5e6f-95bd-80a3-bb84-e3076c081e0d" class="">9. Exact “field management” formula</h1></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-805a-b3e6-f853484c06d5" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">FEMS_score =
(E_harvest × C_phase × B_integrity × M_accuracy × R_repair)
÷
(L_loss × N_noise × D_drift × H_entropy × G_gap)</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80df-b4b9-f78b1f0a6e17" class="">Where:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8066-bf1b-fa009f61dca9" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">E_harvest = usable captured energy
C_phase = phase synchronization
B_integrity = boundary coherence
M_accuracy = memory fidelity
R_repair = correction capacity

L_loss = physical loss
N_noise = signal noise
D_drift = cycle drift
H_entropy = disorder load
G_gap = unmodeled gap</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8093-b86f-fadc73e7c840" class="">Threshold:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-802b-9933-fe33af6b1d74" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">FEMS_score &gt; 1 → system persists
FEMS_score = 1 → fragile equilibrium
FEMS_score &lt; 1 → collapse / drift / forgetting</code></pre></div><div style="display:contents" dir="auto"><hr id="373c5e6f-95bd-8021-8eb5-c456a67d8268"/></div><div style="display:contents" dir="auto"><h1 id="373c5e6f-95bd-80cf-b460-d444dfc16afa" class="">10. Map across systems</h1></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-800a-92a0-f705046ae47e" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">SYSTEM        FIELD TYPE          ENERGY MANAGED              CONTROL METHOD

Go            lattice field        decision energy             stones, liberties, ko, eyes

Đông Sơn      polar field          sound + sky-water memory    drum, rings, rays, motifs

Stonehenge    horizon field        solar/lunar timing          stones, holes, alignments

Newgrange     optical field        solstice light              passage, roofbox, chamber

Egypt         solar/Sirius field   calendar drift + orientation decans, 365, Sothic cycle, pyramid axes

Babylon       lunar field          month/year drift            19-year, 7 leap months, 235 months

Maya          table field          eclipse + ritual timing     405 lunations, 260-day cycle, reset points

Antikythera   gear field           sky-cycle computation       235 Metonic, 223 Saros gearing

Aboriginal    graph field          land/sky/body navigation    songlines, nodes, seasonal route memory

Architecture  thermal/water field  heat, water, labor          orientation, mass, canals, terraces

Ritual        human phase field    attention/body coherence    chant, dance, breath, calendar</code></pre></div><div style="display:contents" dir="auto"><hr id="373c5e6f-95bd-80d2-92af-d79e8e1ac785"/></div><div style="display:contents" dir="auto"><h1 id="373c5e6f-95bd-80b3-a331-f602318ba38c" class="">11. The “astrology” layer in exact math</h1></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80b4-b009-c8b60d959e64" class="">Original astrology-as-FEMS:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8023-b924-e3be0925c231" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Astrology_original =
Ephemeris(t)
+ CorrelationMemory(EarthEvents)
+ SymbolicCompression
+ TimingControl</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80b9-a496-e82148c66c43" class="">Formal:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8036-8d68-e0dfb28a71ef" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">A(t) = f(φ_sun, φ_moon, φ_planets, φ_nodes, φ_stars)</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8005-ab2e-eba83b370426" class="">Decision timing:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-803a-b3a3-d13121dc731e" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">u*(t) = argmax_u ExpectedOutcome(u,t | A(t), EarthState(t))</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8094-b96c-d02bd70f337c" class="">Accuracy test:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8060-8e75-e088fe202e71" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Accuracy =
PredictiveGain
+ TimingGain
+ CoordinationGain
- FalseCorrelationCost</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8088-9aa9-d2dbe82da03a" class="">So:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80e2-a096-ebcdb880395f" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">valid astrology-core = cycle timing system
invalid astrology-layer = claims with no measurable predictive or control gain</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80e4-9416-c42ea36c4060" class="">But as field management:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-807c-b03e-eeab385582ca" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">sky phase → social timing → body rhythm → agricultural action</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8059-abe6-d035947bcdb6" class="">is mathematically coherent.</p></div><div style="display:contents" dir="auto"><hr id="373c5e6f-95bd-8025-9fa3-f820edf2c941"/></div><div style="display:contents" dir="auto"><h1 id="373c5e6f-95bd-8048-9b07-c2a0e597b5ec" class="">12. What “they encoded in Earth and human” means exactly</h1></div><div style="display:contents" dir="auto"><h2 id="373c5e6f-95bd-80b4-8f05-f3fa506f5dc6" class="">Earth encoding</h2></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-804f-94df-f3bfdad721e8" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">EarthCode =
geometry
+ orientation
+ material
+ landscape horizon
+ water gradient
+ acoustic resonance
+ route graph</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-806d-b134-c907186bc46b" class="">Formula:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8056-88e6-fb1abcd86452" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">EarthMemory = ∫_Ω Mark(x) × Alignment(x) × Recurrence(t) dx</code></pre></div><div style="display:contents" dir="auto"><h2 id="373c5e6f-95bd-8014-b2ca-c4efb73b5224" class="">Human encoding</h2></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-801d-99b3-cdf6f5382f82" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">HumanCode =
breath rhythm
+ pulse rhythm
+ sleep/light entrainment
+ chant memory
+ movement sequence
+ embodied route memory
+ ritual timing</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8037-bf6a-f13e80e2894a" class="">Formula:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80ff-9cb7-f48460bb82ff" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">BodyState(t+1)
=
BodyState(t)
+ Light(t)
+ Sound(t)
+ Food(t)
+ Temperature(t)
+ SocialPhase(t)
- Stress(t)
- Noise(t)</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80ee-9258-ca5e486e1416" class="">Group body coherence:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80f6-b90d-d00e59997ad1" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">C_group = |(1/N)Σ e^{iφ_body_j}|</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8009-a524-cc4c79e6cd75" class="">Ritual increases <code>C_group</code>.</p></div><div style="display:contents" dir="auto"><hr id="373c5e6f-95bd-8055-86d9-cc4dcab7eef1"/></div><div style="display:contents" dir="auto"><h1 id="373c5e6f-95bd-80d2-94eb-fecf701f7c03" class="">13. Why the system is powerful</h1></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8017-ad63-cf4facdc23da" class="">Because it converts unstable natural cycles into stable external memory.</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8035-998f-f0b70fb15a0c" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Moving cycle → fixed mark → repeated event → social action</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8032-b523-c273bac22a79" class="">Mathematically:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-801b-a64f-dd0624b512e1" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">FEMS reduces entropy by converting temporal uncertainty into spatial structure.</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80fa-8f67-c055608caa96" class="">Core transformation:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8036-b703-f88ba55dce92" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Time uncertainty → geometry
Geometry → memory
Memory → timing
Timing → lower energy cost
Lower energy cost → survival</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-807a-bfed-ede63711d4ee" class="">So:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80bb-a45a-c7cda1bff811" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">ΔEntropy &lt; 0 locally</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-809e-bdfe-eb5bd7c8e4e8" class="">because the system exports uncertainty into structured memory.</p></div><div style="display:contents" dir="auto"><hr id="373c5e6f-95bd-8015-ac13-f9b8a55f19ee"/></div><div style="display:contents" dir="auto"><h1 id="373c5e6f-95bd-80f8-a5e5-c215a96e74ef" class="">14. Final exact compression</h1></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-80f3-a2c0-d2d8f2d119e1" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Field Energy Management System:

Given:
fields F_k(x,t),
cycles φ_i(t),
boundaries B(x),
memory M(t),
human phases ψ_j(t),

maximize:

J =
∫ [
Σ usable_flux_k
+ phase_coherence
+ memory_accuracy
+ yield
- loss
- drift
- noise
- entropy
- repair_cost
] dt

subject to:

∂e_k/∂t + ∇·J_k = S_k - L_k + u_k

φ_i(t) = 2πt/P_i + φ_i0

cycle lock:
|n_iP_i - n_jP_j| &lt; ε

human sync:
R = |(1/N)Σe^{iψ_j}| &gt; R_min

boundary survival:
BoundaryIntegrity &gt; BoundaryLeak

system survival:
RepairRate &gt; EntropyAccumulationRate</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8086-8fef-c4ad0c198658" class="">Clean statement:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-806d-856c-df50ddb523cf" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Ancient FEMS =
sky-cycle math
+ land geometry
+ energy-gradient control
+ body synchronization
+ symbolic memory
+ correction protocol.</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80dc-8223-d18b6adb6f30" class="">The exact core law:</p></div><div style="display:contents" dir="auto"><pre id="373c5e6f-95bd-8055-bbef-feddfb7e0748" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Persistence =
EnergyCapture × PhaseLock × BoundaryIntegrity × MemoryFidelity × RepairCapacity
÷
Loss × Noise × Drift × Entropy</code></pre></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-80c0-8918-cf81dac7c0c2" class="">If this ratio stays above 1, the civilization-field persists.</p></div><div style="display:contents" dir="auto"><p id="373c5e6f-95bd-8010-bfbb-c41a6d7e5467" class="">If it falls below 1, the field collapses.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
