---
tags: [amos-general]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>AMOS ORGANISM OS — CANONICAL EXHAUSTIVE PYTHON ARCHITECTURE</title><style>
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
	
</style></head><body><article id="2e6c5e6f-95bd-800b-8dfe-e9cce9642e80" class="page sans"><header><h1 class="page-title" dir="auto"><strong>AMOS ORGANISM OS — CANONICAL EXHAUSTIVE PYTHON ARCHITECTURE</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="2e6c5e6f-95bd-8096-880b-d694369d4cd1" class=""><strong>Global naming constraint (hard)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e6c5e6f-95bd-80de-bdea-fe7d081d3eeb" class="">All directories and modules must match:</p></div><div style="display:contents" dir="auto"><p id="2e6c5e6f-95bd-8072-97c3-ce6d104b0a39" class="">^[a-z_][a-z0-9_]*$</p></div><div style="display:contents" dir="auto"><hr id="2e6c5e6f-95bd-80fc-8ab3-d16b78fc41ab"/></div><div style="display:contents" dir="auto"><h2 id="2e6c5e6f-95bd-806c-b65c-daa928eec869" class=""><strong>0) Root: OS-level scaffolding (this was missing)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e6c5e6f-95bd-803e-adf6-df959623fc50" class="">These are not “nice-to-have”. They are required for determinism, quality, and operability.</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2e6c5e6f-95bd-8059-b6c2-cc4349cd7802" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">amos/
├── __init__.py
├── __main__.py                 # single entrypoint (boot)
│
├── root/                       # identity + registries + schemas + boot policy
│   ├── __init__.py
│   ├── readme.md
│   ├── identity.json           # operator identity + system identity
│   ├── mission.json            # goals, non-goals, constraints
│   ├── state_schema.json       # canonical world+internal state schema
│   ├── registry/               # SINGLE source of truth registries
│   │   ├── system_registry.json
│   │   ├── kernel_registry.json
│   │   ├── engine_registry.json
│   │   ├── agent_registry.json
│   │   ├── tool_registry.json
│   │   ├── interface_registry.json
│   │   ├── risk_registry.json
│   │   ├── quality_registry.json
│   │   └── provenance_registry.json
│   └── contracts/              # typed contracts (inputs/outputs/errors)
│       ├── claim_contract.json
│       ├── evidence_contract.json
│       ├── invariant_contract.json
│       ├── signal_contract.json
│       ├── action_contract.json
│       └── refusal_contract.json
│
├── build/                      # reproducible build system (deterministic)
│   ├── readme.md
│   ├── lockfiles/              # dependency locks (pip/uv/poetry etc)
│   ├── constraints/            # build constraints (hashes, allowlists)
│   ├── scripts/                # build scripts (no ad hoc)
│   └── sbom/                   # software bill of materials (supply chain)
│
├── runtime/                    # runtime policy + lifecycle + orchestration
│   ├── readme.md
│   ├── orchestrator.py         # the only orchestrator
│   ├── scheduler.py            # time + cycles
│   ├── state_store.py          # state persistence interface
│   ├── event_bus.py            # internal eventing
│   ├── lifecycle.py            # start/stop/sleep/degrade
│   └── feature_flags.json      # controlled activation of capabilities
│
├── observability/              # logs/metrics/traces (operability)
│   ├── readme.md
│   ├── logger.py
│   ├── metrics.py
│   ├── tracer.py
│   ├── audit_log.py            # append-only audit trail
│   └── dashboards/             # optional
│
├── security/                   # security is not only &quot;immune&quot;
│   ├── readme.md
│   ├── secrets.py              # secret access contract (never plaintext)
│   ├── auth.py                 # identity/authz hooks
│   ├── sandbox.py              # execution sandbox policy
│   ├── supply_chain.py         # dependency verification
│   └── threat_model.json
│
├── quality/                    # code quality enforcement (your “rubbish code” issue)
│   ├── readme.md
│   ├── static_checks/          # lint/type/format configs
│   ├── test_policy.json        # required test types per subsystem
│   ├── invariant_tests/        # kernel invariant tests
│   └── ci/                     # CI definitions (even if local)
│
├── data/                       # canonical data boundaries (prevents leakage/drift)
│   ├── readme.md
│   ├── inputs/                 # raw inputs (immutable)
│   ├── cache/                  # cache (evictable)
│   ├── artifacts/              # generated outputs (traceable)
│   ├── models/                 # model files (versionless -&gt; content-addressed)
│   └── backups/                # backup policy + snapshots
│
├── plugins/                    # tool + engine extension without mutating canon
│   ├── readme.md
│   ├── plugin_contract.json
│   ├── installed/              # installed plugins (registered)
│   └── sandboxed/              # untrusted plugins
│
├── docs/                       # system documentation (not scattered)
│   ├── readme.md
│   ├── architecture.md
│   ├── invariants.md
│   ├── threat_model.md
│   └── runbook.md
│
├── archive/                    # deprecated (read-only)
│   └── readme.md
│
└── subsystems/                 # the organism organs live here (MECE enforced)
    ├── brain/
    ├── senses/
    ├── immune/
    ├── blood/
    ├── skeleton/
    ├── muscle/
    ├── metabolism/
    ├── world_model/
    ├── social_engine/
    ├── life_engine/
    ├── legal_brain/
    ├── quantum_layer/
    ├── factory/
    └── interfaces/</code></pre></div><div style="display:contents" dir="auto"><p id="2e6c5e6f-95bd-80ec-885d-db6be7cd2ea2" class=""><strong>Key closure:</strong> organs ≠ OS scaffolding. You need both.</p></div><div style="display:contents" dir="auto"><hr id="2e6c5e6f-95bd-80d3-bc41-e0446a8ec9c9"/></div><div style="display:contents" dir="auto"><h2 id="2e6c5e6f-95bd-8070-b3c6-d504b439595f" class=""><strong>1) Subsystem internal structure (locked + enforceable)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e6c5e6f-95bd-8071-8adf-d3e4ff2f1aba" class="">Every subsystem must be identical in shape:</p></div><div style="display:contents" dir="auto"><pre id="2e6c5e6f-95bd-8089-b044-dbb41d278607" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">subsystems/&lt;name&gt;/
├── __init__.py
├── readme.md
├── kernels/
├── engines/
├── agents/
├── config/
├── tests/
└── registry.json</code></pre></div><div style="display:contents" dir="auto"><p id="2e6c5e6f-95bd-80ae-b2dd-e01c6cce7650" class="">No “utils” folders. No “misc”. No silent dumping ground.</p></div><div style="display:contents" dir="auto"><hr id="2e6c5e6f-95bd-8028-9427-e0c150adca98"/></div><div style="display:contents" dir="auto"><h2 id="2e6c5e6f-95bd-80d1-ad2e-c1917651ad0c" class=""><strong>2) UCIA architecture gap scan — what was missing, now closed</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e6c5e6f-95bd-80e6-9492-ed13c1141089" class=""><strong>Gap class: OS determinism gaps</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-80bb-9f43-e0bb70ce8aa2" class="bulleted-list"><li style="list-style-type:disc"><strong>Build determinism</strong> (lockfiles + SBOM + allowlists) ✅ added build/</li></ul></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-8068-82df-d5b7325adc6e" class="bulleted-list"><li style="list-style-type:disc"><strong>Runtime lifecycle</strong> (start/stop/sleep/degrade) ✅ added runtime/</li></ul></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-8065-91e0-fffd87198be9" class="bulleted-list"><li style="list-style-type:disc"><strong>State persistence contract</strong> ✅ added runtime/state_store.py + root/contracts/</li></ul></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-800f-b74b-dda2ebc878be" class="bulleted-list"><li style="list-style-type:disc"><strong>Provenance</strong> (what produced what) ✅ added provenance_registry.json</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e6c5e6f-95bd-8008-b8d4-df1576bafd5f" class=""><strong>Gap class: “agents write rubbish code”</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-8046-85c8-f6a3cb7a8c08" class="bulleted-list"><li style="list-style-type:disc"><strong>Test policy + invariant tests</strong> ✅ added quality/</li></ul></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-8044-be8e-c15d1bd624c0" class="bulleted-list"><li style="list-style-type:disc"><strong>Static checks</strong> ✅ added quality/static_checks/</li></ul></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-80fe-8868-c08b9543debf" class="bulleted-list"><li style="list-style-type:disc"><strong>CI/runbook</strong> ✅ added quality/ci/ + docs/runbook.md</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e6c5e6f-95bd-8065-8f34-c339d938d10e" class=""><strong>Gap class: security ≠ immune</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-80ba-bccb-d1efe9050bc3" class="bulleted-list"><li style="list-style-type:disc"><strong>Secrets, auth, sandbox, supply chain</strong> ✅ added security/</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e6c5e6f-95bd-80b1-85dd-c3b86845c311" class=""><strong>Gap class: operability / no signal miss</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-80fb-a982-da8bd7dcca72" class="bulleted-list"><li style="list-style-type:disc"><strong>Audit logs + traces + metrics</strong> ✅ added observability/</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e6c5e6f-95bd-8051-9541-c19e5def28bf" class=""><strong>Gap class: extendability without mutation</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-809e-9643-f5b3d3e5fb08" class="bulleted-list"><li style="list-style-type:disc"><strong>Plugins with contracts + registry gating</strong> ✅ added plugins/</li></ul></div><div style="display:contents" dir="auto"><hr id="2e6c5e6f-95bd-8041-8301-fa8d1c7ecb3e"/></div><div style="display:contents" dir="auto"><h2 id="2e6c5e6f-95bd-806b-952d-d9dce905d409" class=""><strong>3) One-source-of-truth rule (your “no v2” constraint)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e6c5e6f-95bd-80f4-a0cf-cc11e6103229" class="">You’re correct: “v2” violates single-source-of-truth.</p></div><div style="display:contents" dir="auto"><p id="2e6c5e6f-95bd-80b3-ab34-c90b08b7f2ed" class="">So the canon uses <strong>content-addressed identity</strong>, not “versions”:</p></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-8035-80a8-d771beac35e4" class="bulleted-list"><li style="list-style-type:disc">Every file that is “identity-critical” has:<div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-8064-8b41-f6e7aac86973" class="bulleted-list"><li style="list-style-type:circle">id</li></ul></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-803d-b641-c5d73a02d336" class="bulleted-list"><li style="list-style-type:circle">hash</li></ul></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-80f8-8aea-f0e38c58baa8" class="bulleted-list"><li style="list-style-type:circle">depends_on</li></ul></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-8068-8704-fd026f416903" class="bulleted-list"><li style="list-style-type:circle">provides</li></ul></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-8094-b93f-e56b472700ec" class="bulleted-list"><li style="list-style-type:circle">scope_sigma</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2e6c5e6f-95bd-808d-a401-c9e388755501" class="">Stored in registries as immutable records (append-only).</p></div><div style="display:contents" dir="auto"><p id="2e6c5e6f-95bd-80d4-8b42-f9a77723bb7d" class="">You don’t rename reality; you <strong>append evidence</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e6c5e6f-95bd-8086-9ae1-f86bbe96a204" class="">That preserves “human body” semantics: one organism, continuous history.</p></div><div style="display:contents" dir="auto"><hr id="2e6c5e6f-95bd-8059-aea8-f01fd98c959e"/></div><div style="display:contents" dir="auto"><h2 id="2e6c5e6f-95bd-80f5-9a59-eef1f848cb60" class=""><strong>4) Hard constraints to prevent drift/hallucination in architecture</strong></h2></div><div style="display:contents" dir="auto"><p id="2e6c5e6f-95bd-80b9-98fd-d13a9267f49e" class="">These are enforcement constraints, not prose:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e6c5e6f-95bd-807e-aea5-ebca077000d0" class="numbered-list" start="1"><li><strong>MECE placement:</strong> every module registers exactly one subsystem.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e6c5e6f-95bd-80a2-aa12-f6605387aed2" class="numbered-list" start="2"><li><strong>No hidden dependencies:</strong> imports must match declared depends_on.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e6c5e6f-95bd-8025-ab5d-f59cc1254166" class="numbered-list" start="3"><li><strong>No untyped outputs:</strong> all outputs must bind to contracts/*.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e6c5e6f-95bd-8007-a828-d6a3cd94e804" class="numbered-list" start="4"><li><strong>No silent execution:</strong> every action must emit an audit log entry.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e6c5e6f-95bd-80a6-8dc7-ece4cb82b52a" class="numbered-list" start="5"><li><strong>No unsafe tooling:</strong> any tool must register with capability + risk class.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e6c5e6f-95bd-802b-88a2-ccf2bfbfc475" class="numbered-list" start="6"><li><strong>No agent autonomy bypass:</strong> skeleton + immune + legal_brain are veto layers.</li></ol></div><div style="display:contents" dir="auto"><hr id="2e6c5e6f-95bd-806b-bd9a-f88a8ab6027e"/></div><div style="display:contents" dir="auto"><h2 id="2e6c5e6f-95bd-8014-83d2-d595b05525e7" class=""><strong>5) Important truth (non-negotiable)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e6c5e6f-95bd-8022-8738-df8498f96eb1" class="">You asked for “0 bug / 0 risk / 0 gap”.</p></div><div style="display:contents" dir="auto"><p id="2e6c5e6f-95bd-8028-afdb-ef4d8c233afb" class="">A real UCIA-compliant answer must say:</p></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-806d-ad5f-d029f6f78539" class="bulleted-list"><li style="list-style-type:disc"><strong>You can enforce a zero-gap schema</strong> (everything typed, scoped, registered, tested).</li></ul></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-8003-a4c3-f35b319136e0" class="bulleted-list"><li style="list-style-type:disc">You <strong>cannot guarantee</strong> zero bugs or zero risk in an open world.</li></ul></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-80bd-af81-f9c91f72c283" class="bulleted-list"><li style="list-style-type:disc">What you <em>can</em> guarantee is: <strong>no untyped space</strong> and <strong>fail-closed behavior</strong>.</li></ul></div><div style="display:contents" dir="auto"><p id="2e6c5e6f-95bd-800f-97df-fdcc4de2a428" class="">That is the only honest “absolute integrity” claim.</p></div><div style="display:contents" dir="auto"><hr id="2e6c5e6f-95bd-8085-a5eb-c28c8a4d5ec2"/></div><div style="display:contents" dir="auto"><h1 id="2e6c5e6f-95bd-807f-a76a-f6af4dc9ff16" class=""><strong>If you want the next step, I can do it immediately</strong></h1></div><div style="display:contents" dir="auto"><p id="2e6c5e6f-95bd-8099-9e38-eadc24292320" class="">Pick one (no clarifying back-and-forth):</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e6c5e6f-95bd-807e-a322-d15db52c5004" class="numbered-list" start="1"><li><strong>Generate the canonical system_registry.json schema + example entries</strong> for this full architecture.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e6c5e6f-95bd-8003-b4e8-df339c1ff6a3" class="numbered-list" start="2"><li><strong>Generate the build-time validator</strong> (Python) that enforces:<div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-80aa-9335-c6ccb345ee18" class="bulleted-list"><li style="list-style-type:disc">python-safe names</li></ul></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-8052-966c-ebd519198e55" class="bulleted-list"><li style="list-style-type:disc">registry completeness</li></ul></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-8006-9f53-dc2a7fd7e217" class="bulleted-list"><li style="list-style-type:disc">MECE placement</li></ul></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-8032-ac64-d253f296e2df" class="bulleted-list"><li style="list-style-type:disc">import-vs-dependency matching</li></ul></div><div style="display:contents" dir="auto"><ul id="2e6c5e6f-95bd-80ed-8f36-de889002eb14" class="bulleted-list"><li style="list-style-type:disc">contract binding</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e6c5e6f-95bd-8011-9403-ecbccf6d6b98" class="numbered-list" start="3"><li><strong>UCIA scan your uploaded canon files</strong> and map them into this structure (no invention).</li></ol></div><div style="display:contents" dir="auto"><p id="2e6c5e6f-95bd-806f-9cb5-c68932d30edf" class="">Say <strong>1, 2, or 3</strong>.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
