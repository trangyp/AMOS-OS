---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>We Dream of Mars to Avoid Earth</title><style>
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
	
</style></head><body><article id="2e4c5e6f-95bd-80c4-b205-e361aa7f93aa" class="page sans"><header><h1 class="page-title" dir="auto"><strong>We Dream of Mars to Avoid Earth</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8035-88c8-dbd43ef48cc5" class=""><strong>Why a Civilization That Cannot Govern One Biosphere Should Not Pretend to Build Another</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80db-adac-fbcfa081c155" class="">Mars is not humanity’s future.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8038-9f2e-c54f5d871ed6" class="">Mars is a mirror.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ef-b12a-d55a41afdeaa" class="">And what it reflects is not courage or ambition, but avoidance.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8001-b14a-ebbbb39cd3d9"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8075-9bd8-f27a74099b1e" class=""><strong>The Seduction of Mars</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f1-92b0-e1e110182876" class="">Mars feels honest in a way Earth no longer does.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8046-8628-eabff5ca3bd0" class="">It has no politics.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-805c-a034-fa2508b6fc79" class="">No voters.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8044-816d-ccc4a4c1b0d9" class="">No ecosystems asking for protection.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8086-9fdc-c8d4496afd47" class="">No history of broken promises.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8093-8cc6-d4b2d3211e76" class="">Mars is clean — not physically, but morally.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8065-8c1e-e17d1327a58d" class="">Nothing there can accuse us of neglect.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-802b-80ad-fed480e5785d" class="">Earth, by contrast, is crowded with responsibility.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80bb-9255-e85d15f42911" class="">So we project hope outward.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8030-bfa1-df205d9171f4" class="">When people say <em>“Mars is our backup plan”</em>, what they are really saying is:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-80eb-a4af-d5762c6f2904" class="">We have lost confidence in our ability to govern ourselves on Earth.</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8099-8c8e-e27f17048eec" class="">That is not a technological statement.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b7-99f5-df5df452d82f" class="">It is a governance confession.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80ff-96b1-ecc466e00f01"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-800b-a103-cdf17022dd0a" class=""><strong>The Backup Planet Fantasy</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ef-93a1-f6b8f52c3356" class="">The idea of Mars as a “second home” rests on a dangerous abstraction.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d7-ae63-fa1dde75b46d" class="">It assumes that:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ea-a287-fa0379d785e1" class="bulleted-list"><li style="list-style-type:disc">planetary systems are interchangeable</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8021-b220-fb7ba0ba8c08" class="bulleted-list"><li style="list-style-type:disc">life is portable</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d0-8ed6-f23cbb10e903" class="bulleted-list"><li style="list-style-type:disc">governance failures are local, not structural</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8046-8232-df6f7e07dd5a" class="bulleted-list"><li style="list-style-type:disc">complexity can be escaped rather than managed</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80e8-b29e-f71a78671b15" class="">None of these are true.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8024-956c-ea536f78db9e" class="">Mars does not solve:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80bf-a013-e77e901ab272" class="bulleted-list"><li style="list-style-type:disc">political failure</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8003-9566-e26790274e8f" class="bulleted-list"><li style="list-style-type:disc">inequality</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e4-9c7c-e60d544f8802" class="bulleted-list"><li style="list-style-type:disc">extractive economics</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8041-8b2b-c58d2b3e7be8" class="bulleted-list"><li style="list-style-type:disc">weak institutions</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8078-abfa-d259a088fe60" class="bulleted-list"><li style="list-style-type:disc">ecological blindness</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80df-b40b-f81c0027b0c3" class="bulleted-list"><li style="list-style-type:disc">short-term thinking</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80bb-864b-d39de0445e4a" class="">It simply removes the evidence.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-808b-8b13-f8e95cdf8078" class="">A civilization that cannot maintain a living planet does not become more capable by fleeing it.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80fd-8ae4-e20273668454" class="">It becomes more fragile.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-803e-95e1-c14a266d115a"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8073-a07c-e846bce16585" class=""><strong>Mars Is Not Hostile — It Is Unforgiving</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-809d-af79-fe05da6ac5d9" class="">Mars is often described as “harsh.”</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f0-996a-d52556fd3623" class="">That language is misleading.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c8-a197-eb6f32ad18bf" class="">Mars is not hostile in the way Earth can be hostile.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f2-9d85-e7e9414b6118" class="">It is unforgiving.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b4-a5ad-f3781c6b1b4a" class="">There is no margin for error.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8014-b869-eddbb8f0ccca" class="">No biological buffer.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80e4-b4bf-cff3954c451e" class="">No redundancy provided by nature.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80be-ae7f-c72b322ec7d8" class="">Every system must be:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c2-b92a-c94de8c10b79" class="bulleted-list"><li style="list-style-type:disc">perfectly maintained</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8018-80dc-ecee8aeb4ecd" class="bulleted-list"><li style="list-style-type:disc">continuously powered</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80fd-8000-cc4a4afd4d64" class="bulleted-list"><li style="list-style-type:disc">politically stable</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80bf-a2be-fdd9aaafb580" class="bulleted-list"><li style="list-style-type:disc">socially cohesive</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80bf-bafa-f1218771e431" class="bulleted-list"><li style="list-style-type:disc">technically flawless</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8023-9776-f932743e6ded" class="">On Earth, failure is often survivable.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-809e-b922-d82776a5a358" class="">On Mars, failure is final.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8029-a532-f9882be651a5" class="">If a society struggles with:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8043-be61-c87d576adcae" class="bulleted-list"><li style="list-style-type:disc">maintaining water systems</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ce-9c33-f8dec9dbf048" class="bulleted-list"><li style="list-style-type:disc">ensuring healthcare</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8044-8611-ec7f64fba046" class="bulleted-list"><li style="list-style-type:disc">preventing institutional decay</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8084-b67f-fcce0cdbabc8" class="bulleted-list"><li style="list-style-type:disc">coordinating long-term policy</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-804a-8caf-ddec7d45d66f" class="">…it has no business exporting those weaknesses to a closed-loop death environment.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-800d-8351-daea33d6f311"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8033-87a2-fc4cbe03a9cf" class=""><strong>Closed-Loop Life Is the Real Test — And We Are Failing It Here</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8066-adb3-ea8e93036f85" class="">Mars survival depends on closed-loop systems:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-805e-b58a-dc8f7d33a24c" class="bulleted-list"><li style="list-style-type:disc">air</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-809b-bfba-da5baed0331d" class="bulleted-list"><li style="list-style-type:disc">water</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80db-a2ed-c5b4b7b52223" class="bulleted-list"><li style="list-style-type:disc">food</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8094-b6d7-d3ea9e4788a9" class="bulleted-list"><li style="list-style-type:disc">waste</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e4-a9ab-c894f241463e" class="bulleted-list"><li style="list-style-type:disc">energy</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a0-abfa-d288a5b7cae4" class="">We already fail at closed loops on Earth.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80fc-ae07-ff1ab0801d08" class="">We cannot:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80bd-845e-ea8cf6559320" class="bulleted-list"><li style="list-style-type:disc">close material cycles</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-804e-88cd-de113550f610" class="bulleted-list"><li style="list-style-type:disc">manage waste without leakage</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8094-be07-e0ffabc9a542" class="bulleted-list"><li style="list-style-type:disc">protect oceans from runoff</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-807d-92da-e3a5ab27ce40" class="bulleted-list"><li style="list-style-type:disc">prevent atmospheric accumulation</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806f-859f-cc853145df3b" class="bulleted-list"><li style="list-style-type:disc">govern shared resources without exploitation</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8073-87cd-f2182320b8af" class="">Mars does not offer a reset.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f9-bff4-c0a40b410b62" class="">It removes the illusion of abundance that currently hides our incompetence.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80d8-830e-c52e8486e0a3"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80ec-8241-c41ffa99464e" class=""><strong>The Ethical Cost We Don’t Name</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8080-babc-c594875bdb92" class="">Mars exploration is often framed as noble sacrifice.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80e7-8421-d6838195807e" class="">But sacrifice by whom?</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ad-b8ed-ce85b380cd42" class="">The risks are not distributed equally.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ff-997a-d4b673e32487" class="">The rewards are not shared fairly.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80eb-829a-f1a071d7c440" class="">The decisions are not democratically made.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800b-a5e0-f156f98329a3" class="">Radiation exposure.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-809a-87c6-ebf447b8d593" class="">Infertility risk.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d7-abbe-eb306bd64f68" class="">Generational health uncertainty.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c6-b45d-f848b7de0063" class="">Psychological isolation.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80bd-9184-e713d294aadc" class="">These are treated as “acceptable tradeoffs” — not because they are ethical, but because they affect few, distant bodies.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803b-a497-f4b9a3b84688" class="">This is a familiar pattern.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a8-800d-d82a1bec739f" class="">When a system cannot solve injustice, it relocates risk to the least visible.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a3-a4e6-fa7db2b420a2" class="">Mars is not immune to politics.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8026-ad84-e2cfa6bf5154" class="">It is simply politically quiet.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-803d-8f40-d47dce04df2f"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8023-aa32-c31a6f6382c8" class=""><strong>Why Mars Gets Funding and Oceans Don’t</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f1-8207-e2e3da6198f8" class="">This is not accidental.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d7-9508-cc108f531f2a" class="">Mars is attractive because:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-803a-8588-d5eb2a86b6ae" class="bulleted-list"><li style="list-style-type:disc">it has no existing stakeholders</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8003-90c1-e927bd48ceca" class="bulleted-list"><li style="list-style-type:disc">it bypasses legal complexity</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b0-880e-ef33c15abf84" class="bulleted-list"><li style="list-style-type:disc">it offers clean hero narratives</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-809d-bbba-c77fa8582980" class="bulleted-list"><li style="list-style-type:disc">it avoids Indigenous rights</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8016-a077-f0c88ae008d1" class="bulleted-list"><li style="list-style-type:disc">it avoids governance reform</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a0-a1a4-d83b0bc425a6" class="">Earth’s oceans, forests, and cities are harder.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8021-9968-cf12328b24e9" class="">They involve:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8016-9562-ef9c08dcb5bf" class="bulleted-list"><li style="list-style-type:disc">conflict</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806c-b285-e21c58921cf9" class="bulleted-list"><li style="list-style-type:disc">consent</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f2-a8ff-d51774e47de4" class="bulleted-list"><li style="list-style-type:disc">accountability</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-800d-8b5a-ed6778dc107f" class="bulleted-list"><li style="list-style-type:disc">repair</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8083-9f96-c9dc4b3e6db2" class="bulleted-list"><li style="list-style-type:disc">restraint</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80fc-afd9-d1c84cf838ed" class="">Mars is simpler to imagine than Earth is to fix.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-805d-a176-f7ec57ae197d" class="">That alone should trouble us.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80b1-8332-e0bbd2317643"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8011-821e-cb3673292f39" class=""><strong>Exploration vs Escape</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8061-be1e-e360c0d3dc48" class="">Exploration is not the problem.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800e-b937-e521606c2347" class="">Escape is.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b2-a0ce-ed652844fb6c" class="">True exploration expands understanding and resilience.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a8-b4c2-e13922d54b0a" class="">Escape redirects attention away from responsibility.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-807a-9ad4-c21f3e5b1592" class="">A simple test applies:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8051-8845-f227d43c37f1" class="">Does this exploration measurably strengthen Earth’s capacity to survive?</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8082-9413-fb61fc12f8c8" class="">If the answer is no, then it is not progress.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f6-8124-e9fae3579e55" class="">It is distraction.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8067-9e01-cfd02c6c946e" class="">Mars research that:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8002-84c8-f82425ff2909" class="bulleted-list"><li style="list-style-type:disc">advances closed-loop life for Earth</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d9-8932-de2ca329b86a" class="bulleted-list"><li style="list-style-type:disc">improves disaster resilience</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8034-8bd2-ff78dd29b016" class="bulleted-list"><li style="list-style-type:disc">strengthens planetary monitoring</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8046-bb25-e348e0c218cc" class="bulleted-list"><li style="list-style-type:disc">enhances ecological repair</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8087-8e88-e3ebe5190483" class="">…is defensible.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8095-a5d7-d0d25516ea61" class="">Mars colonization framed as destiny is not.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8085-9804-cde75ae70488"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8004-83ef-e61bb56224db" class=""><strong>Terraforming Mars vs Governing Earth</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8036-a079-cd2c86850749" class="">Terraforming Mars is often presented as a grand engineering challenge.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a8-9cb0-dedc3445d598" class="">But Earth is already terraformed.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8077-9787-e15905085065" class="">By us.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8044-8df0-fc6f9457e78a" class="">Poorly.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8064-b9f7-cafb3618020c" class="">We altered:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806c-96c7-d3c968f2942f" class="bulleted-list"><li style="list-style-type:disc">climate</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8084-9451-ec4d185a9494" class="bulleted-list"><li style="list-style-type:disc">oceans</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8037-aebc-f0a17e556505" class="bulleted-list"><li style="list-style-type:disc">nitrogen cycles</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b5-8cb4-ee749bc11265" class="bulleted-list"><li style="list-style-type:disc">biodiversity</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ca-aaa4-c031bb8b44f1" class="bulleted-list"><li style="list-style-type:disc">land systems</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80cc-898c-ecf83a7f39b1" class="">Without governance.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8042-96a9-df00f38937cd" class="">Without restraint.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f1-92ed-ebd8d42b6eed" class="">Without long-term modeling.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8076-8104-fa3e583d1e74" class="">Why should anyone believe we will behave differently on Mars?</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-808d-9e3f-e30fba1b9fee" class="">A civilization that cannot manage unintended consequences on a forgiving planet should not be trusted with intentional ones on an unforgiving one.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80c8-8500-d425befd523e"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8035-8d25-e3d320af2061" class=""><strong>The Language Problem: Colonization, Destiny, Inevitability</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8087-a020-c3b60950062e" class="">Mars rhetoric often borrows from old myths:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80cd-a0a0-fed6652bc727" class="bulleted-list"><li style="list-style-type:disc">frontier</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802d-8748-cfb4dc39c93a" class="bulleted-list"><li style="list-style-type:disc">destiny</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8005-9c37-e2182d0ac437" class="bulleted-list"><li style="list-style-type:disc">manifest progress</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f4-b40a-cbdbd8cd20fc" class="bulleted-list"><li style="list-style-type:disc">heroic expansion</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-804b-bf94-fa3496f5ac5c" class="">These myths have a track record.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80cd-b447-c0f35d69ad32" class="">They end in:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d0-9ede-e943c612933f" class="bulleted-list"><li style="list-style-type:disc">extraction</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80af-9131-fc63f18458d0" class="bulleted-list"><li style="list-style-type:disc">exclusion</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-807c-b75b-c4f25cadc983" class="bulleted-list"><li style="list-style-type:disc">collapse</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8090-adba-c431d92688bc" class="bulleted-list"><li style="list-style-type:disc">moral amnesia</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8064-8911-f5b9d082fbb2" class="">The language itself should raise alarms.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800d-9d4d-c75e32e1b9bb" class="">A mature civilization does not need destiny narratives to justify survival.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8074-aa85-ec242365fcd6"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8044-9794-f9e03fb9b2ca" class=""><strong>The Real Multi-Planet Future</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8084-8df9-ca672c5c7411" class="">If “multi-planetary” is to mean anything legitimate, it must begin here.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-807d-a8b8-e4798f3d3892" class="">A civilization capable of sustaining life on Earth would:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8041-aa52-d8c4c82307d8" class="bulleted-list"><li style="list-style-type:disc">manage ecosystems as infrastructure</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8076-b896-e0bb9682740c" class="bulleted-list"><li style="list-style-type:disc">treat biodiversity as capital</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ab-a216-e161c11d5fc5" class="bulleted-list"><li style="list-style-type:disc">govern shared resources transparently</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802c-b720-e3d7802bedbc" class="bulleted-list"><li style="list-style-type:disc">plan across generations</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8027-9a8a-f4532ebbb4f9" class="bulleted-list"><li style="list-style-type:disc">accept limits without collapse</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ae-ab88-e5de82ffe33c" class="">Only such a civilization could responsibly expand outward.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a1-a921-dc94aab997bf" class="">Mars is not the test of humanity’s ingenuity.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b2-b954-c99f2bcfa9aa" class="">Earth is.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-809c-87ae-ce6cba8a4260"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8073-bb50-e03ea17a82ba" class=""><strong>Mars as a Teacher, Not an Escape</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b2-9499-dffd007e7556" class="">Mars should be used to teach humility, not ambition.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f5-a2f4-db4d4cc8a1ee" class="">It shows us:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8045-9358-e501f72117e0" class="bulleted-list"><li style="list-style-type:disc">how narrow the margin for life is</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-801b-820e-f6cb4f0d2493" class="bulleted-list"><li style="list-style-type:disc">how dependent we are on stable systems</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8015-babb-e7d3e07de70f" class="bulleted-list"><li style="list-style-type:disc">how fragile closed loops can be</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80bc-9031-fe31e8143626" class="bulleted-list"><li style="list-style-type:disc">how unforgiving physics is</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-808f-9fea-f99ab01635c2" class="">If Mars inspires anything, it should be this:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8025-bcbc-c085aaa2f36b" class="">If we cannot care for a planet that gives us air, water, and life for free, we are not ready to build one that gives us nothing at all.</blockquote></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-807d-88f9-e314065a398a"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80bb-927b-db1e2d9c7f4b" class=""><strong>The Final Claim</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8013-b700-d4f8a4e8fc3b" class="">Mars is not hope.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-805c-9e48-df43080eebb8" class="">Mars is a diagnostic.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-809f-a723-d7775c0c5d06" class="">And the diagnosis is clear:</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803e-96d5-d0480b833da9" class="">A civilization dreaming of Mars while neglecting Earth is not reaching for the future.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8056-a48f-e35f7fe861f4" class="">It is running from responsibility.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b0-b57f-c59b7226ee0f" class="">The future is not whether we can reach another planet.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8072-92d6-e074a233731b" class="">The future is whether we can become the kind of civilization that deserves one.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8017-9c75-dd953f83755e"/></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f6-a85d-e109df45af9b" class="">If you want next, I can:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e3-8aeb-dd93157adaa5" class="bulleted-list"><li style="list-style-type:disc">harden this into a <strong>book-length chapter</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b9-8cd3-c16fc79795e3" class="bulleted-list"><li style="list-style-type:disc">write a counterpiece: <strong>“The Case for Space — If Earth Comes First”</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8067-9cf6-c27e4af90ca0" class="bulleted-list"><li style="list-style-type:disc">or produce a <strong>Planet-First exploration doctrine</strong> usable by policymakers</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8009-ba79-d7c1002bc8ee" class="">Just say the word.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
