---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Attraction</title><style>
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
	
</style></head><body><article id="30dc5e6f-95bd-803e-a0ca-fb60cef531d2" class="page sans"><header><h1 class="page-title" dir="auto">Attraction</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80a7-bdd5-cee18fe4c5e0" class="">Good. We go deeper.</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80d1-8802-e54c71d66967" class="">Not more surface regimes.</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80fe-a012-dadb335200d5" class="">We go to structural invariants underneath civilization, across 100,000+ years.</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80ea-8c8e-ff6dd758cce4" class="">We move from:</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80d7-96bb-cfeae3aa2745" class="">civilization types</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80af-b036-c3f8da2e0cb3" class="">→ to control variables</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80a1-9069-ec72b91936c2" class="">→ to attractor basins</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-801d-805d-d29410992ab5" class="">→ to stability equations</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8051-b0f6-d550fae54b9d" class="">→ to phase transitions</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80da-a363-e754be4ce016" class="">This is deeper layer modeling.</p></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-80b2-a361-e3d56a795831"/></div><div style="display:contents" dir="auto"><h1 id="30dc5e6f-95bd-805d-a4ab-edeee65c18e1" class="">I. Civilization as a Mating Field Attractor</h1></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80b5-8176-cbb79e4827b0" class="">Forget labels like “agrarian” or “modern”.</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80af-84ae-dc0089650301" class="">At base, every civilization is a <strong>mating field with constraints</strong>.</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8009-a51f-f2ce9ceb403e" class="">The field is defined by:</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-802b-a4d6-cfdb930bd382" class="bulleted-list"><li style="list-style-type:disc">Energy density (E)</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8034-8670-e6423119dc65" class="bulleted-list"><li style="list-style-type:disc">Enforcement strength (L)</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80fc-bddd-f0c26d4b2e47" class="bulleted-list"><li style="list-style-type:disc">Information distortion (I)</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8034-b4e5-f1d42a1bd248" class="bulleted-list"><li style="list-style-type:disc">Mobility (M)</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8030-89bb-c62080633d22" class="bulleted-list"><li style="list-style-type:disc">Hierarchy variance (H)</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80eb-ba3b-fc391017f743" class="bulleted-list"><li style="list-style-type:disc">Child cost (C)</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8026-9bc8-f9e37524031e" class="bulleted-list"><li style="list-style-type:disc">Nervous system stress baseline (S)</li></ul></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80da-9e51-ed6d0700a833" class="">So civilization = dynamic system:</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="30dc5e6f-95bd-8031-9cca-c1cc096dc1ff" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\mathcal{C}(t) = f(E, L, I, M, H, C, S)</code></pre></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-809d-a146-e5197482f9ff" class="">Attraction dynamics emerge from this field.</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8018-80f7-e827e318c455" class="">Not culture first.<br/>Biophysics first.</p></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-8092-b3f3-f895c810218c"/></div><div style="display:contents" dir="auto"><h1 id="30dc5e6f-95bd-805a-9aff-dca43fd8c6be" class="">II. Deep Invariants (Beyond Culture)</h1></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-808f-9776-d591b7d3954d" class="">1. Sexual Selection Gradient</h2></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8093-87d2-f15e1168a5d0" class="">When inequality (H) increases:</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-804c-87a0-e60a1e08822b" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\sigma_{male\ reproductive\ variance} \uparrow</code></pre></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80ff-8ef2-c5e7c598f657" class="">Meaning:</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8093-899d-d3ebbd4c7b60" class="bulleted-list"><li style="list-style-type:disc">Fewer men reproduce disproportionately.</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80c0-a319-f217bc3b5fe5" class="bulleted-list"><li style="list-style-type:disc">Female selectivity rises.</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8011-9b65-fd26eccde5e8" class="bulleted-list"><li style="list-style-type:disc">Male competition intensity rises.</li></ul></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8012-8cf7-d624745ec88c" class="">This is invariant across:</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8021-be1a-e705d4323f16" class="bulleted-list"><li style="list-style-type:disc">elephant seals</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80e2-a468-f4a7a728bd13" class="bulleted-list"><li style="list-style-type:disc">warrior clans</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-806f-966b-e4cdce957a8a" class="bulleted-list"><li style="list-style-type:disc">tech billionaires</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8067-87c7-f8d9f55c70a3" class="bulleted-list"><li style="list-style-type:disc">influencer platforms</li></ul></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-804e-849c-d37700e84c1f" class="">Only the medium changes.</p></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-8050-b5f9-d75259651204"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-804a-afe8-f963a0ee5a4d" class="">2. Enforcement–Desire Tension Law</h2></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8045-a1e3-fda8f1f9cc76" class="">When external enforcement (L) is high:</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-8020-af81-d9a910449734" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\text{Behavior conformity} \uparrow</code></pre></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80ca-9efc-c4284e2f0022" class="">\text{Private desire divergence} \uparrow<br/></p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-805f-8273-e603a83c349a" class="">This produces:</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80f9-aafb-f9a2db36a98a" class="bulleted-list"><li style="list-style-type:disc">mistress systems</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-804f-9f2d-c425bd49d27f" class="bulleted-list"><li style="list-style-type:disc">hidden markets</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-803a-b3a7-cfefc8a7a6f5" class="bulleted-list"><li style="list-style-type:disc">emotional fragmentation</li></ul></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80ed-bc14-c88eb111756d" class="">Seen in:</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80ab-a557-ee2d5a62ed3f" class="bulleted-list"><li style="list-style-type:disc">imperial China</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80a1-a2ef-d70eb9168dbc" class="bulleted-list"><li style="list-style-type:disc">Victorian England</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8041-81ce-fd8bd414e36c" class="bulleted-list"><li style="list-style-type:disc">conservative modern states</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-802d-8f51-d5dfb72b8767" class="bulleted-list"><li style="list-style-type:disc">high-shame cultures</li></ul></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80fe-b2ca-dd202bd53efa" class="">This tension is structural, not moral.</p></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-80cc-8258-c0eb8319d28d"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-80be-8a95-f82e39ecb42b" class="">3. Information Noise Law</h2></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80a7-9b6a-ed7df3f15b2f" class="">When information distortion (I) increases:</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-80e5-a5df-d56913d28f65" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\text{Signal reliability} \downarrow</code></pre></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8085-bcf4-de87eca89208" class="">Then mate selection shifts toward:</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80cf-bf7a-ea9faceb971c" class="bulleted-list"><li style="list-style-type:disc">hard-to-fake signals</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-805e-bf5b-fd7300e027fe" class="bulleted-list"><li style="list-style-type:disc">embodied behavior</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80ee-a8e6-fd00e74298be" class="bulleted-list"><li style="list-style-type:disc">long-term observation</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8035-b615-e84506a02a6d" class="bulleted-list"><li style="list-style-type:disc">in-person regulation</li></ul></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80dc-ac3d-d8bfcbb2b5d6" class="">Platform eras (high I) increase:</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8005-ad2b-cfe7e68ba094" class="bulleted-list"><li style="list-style-type:disc">anxiety</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-806f-91fd-e001285ddaf0" class="bulleted-list"><li style="list-style-type:disc">distrust</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-804e-919a-dd4bb6167351" class="bulleted-list"><li style="list-style-type:disc">ghosting</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80b3-a88f-e388094bf002" class="bulleted-list"><li style="list-style-type:disc">paradox of choice</li></ul></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-8068-a87e-fcc796024e6e"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-80f2-889b-d91667177e49" class="">4. Mobility–Commitment Inversion</h2></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8008-b50d-fffb41b6c83d" class="">When mobility (M) increases:</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-809a-b100-f250f9861b45" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\text{Exit cost} \downarrow</code></pre></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-807f-bbb7-e6f85b40ac35" class="">\text{Commitment probability} \downarrow<br/></p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80bb-88d2-e031c86f9821" class="">Stable pair bonds require:</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-80b6-b7fa-ef226eb0c0ff" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\text{Exit cost} &gt; \text{Temptation delta}</code></pre></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80db-a978-dfafa98eb83e" class="">This is why frontier societies and app-dating eras have unstable bonding.</p></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-8029-b94f-e0ecc56b50d0"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-8076-83fb-e4252e33e8e0" class="">5. Nervous System Synchrony Invariant</h2></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-809e-89cf-ed42f182e3b4" class="">Across all eras:</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-809b-a36d-cf08177a9472" class="">Pair stability ∝ regulation synchrony.</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-80a3-9b46-e462969577cc" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Stability \propto \frac{CoRegulation}{TriggerLoad}</code></pre></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80ba-9e23-c8944598792d" class="">This is more predictive than:</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8025-b968-d9e40be73d6e" class="bulleted-list"><li style="list-style-type:disc">income</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8060-8a9e-d1f887e48263" class="bulleted-list"><li style="list-style-type:disc">education</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8008-926e-c62bb55817a9" class="bulleted-list"><li style="list-style-type:disc">ideology</li></ul></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-807a-80e3-d9f5e27c51a5" class="">In chaotic civilizations (high S), people pair for regulation first.</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-800e-a25f-f49aefdadd07" class="">In safe civilizations (low S), they pair for self-actualization.</p></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-80e3-9e49-df1c99245e6e"/></div><div style="display:contents" dir="auto"><h1 id="30dc5e6f-95bd-8091-bff6-de38128e77f3" class="">III. The 4 Attractor Basins of Mating Systems</h1></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-806a-a4e4-c720492500d1" class="">Every civilization falls into one of four gravitational basins:</p></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-803e-8020-ff282e33714b"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-8079-a28f-e700c564377b" class="">Basin A: Survival Pairing</h2></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8049-9d9e-fd4061be216f" class="">High volatility + high child cost.</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8002-9ea8-f34159fc7994" class="bulleted-list"><li style="list-style-type:disc">Strong gender polarity</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8019-9f2b-c359ffedd8de" class="bulleted-list"><li style="list-style-type:disc">Provisioning dominant</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80d1-b955-e11a37013117" class="bulleted-list"><li style="list-style-type:disc">Loyalty enforced</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-800f-8cc9-db81cfd43121" class="bulleted-list"><li style="list-style-type:disc">Emotional depth secondary</li></ul></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80b0-8609-e7fb5478026f" class="">Seen in:</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80b0-baaa-f53810675c59" class="bulleted-list"><li style="list-style-type:disc">pre-state tribes</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80fb-838e-da23bb527871" class="bulleted-list"><li style="list-style-type:disc">war zones</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8098-b9ca-ffaa3c439bb9" class="bulleted-list"><li style="list-style-type:disc">economic collapse periods</li></ul></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-808c-81cf-c589a4ca8fcf"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-80ce-892d-eb5daa0ba05e" class="">Basin B: Lineage Pairing</h2></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80da-9ef4-e40958581a88" class="">Moderate volatility + strong hierarchy.</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-809f-9540-d5a6f3f08814" class="bulleted-list"><li style="list-style-type:disc">Family alliance &gt; personal desire</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8084-9fc0-c4338e74b401" class="bulleted-list"><li style="list-style-type:disc">Reputation policing high</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80fb-b45f-f6f36e36cd3b" class="bulleted-list"><li style="list-style-type:disc">Female sexuality tightly regulated</li></ul></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-807a-8a70-f80356434b66" class="">Seen in:</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80b1-b1f5-d97f438be589" class="bulleted-list"><li style="list-style-type:disc">agrarian empires</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80fb-896d-c8073ed3910c" class="bulleted-list"><li style="list-style-type:disc">feudal systems</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8088-aec7-f658f4bfd05c" class="bulleted-list"><li style="list-style-type:disc">honor cultures</li></ul></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-804d-9be1-dfe2987d239f"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-8005-a9b4-d47a18f5e998" class="">Basin C: Companionate Pairing</h2></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80f9-a8ea-e3348db38b0e" class="">High institutional trust + moderate surplus.</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-805e-a627-e5950a2d66d4" class="bulleted-list"><li style="list-style-type:disc">Love legitimized</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8007-b008-e744519a9f5f" class="bulleted-list"><li style="list-style-type:disc">Monogamy idealized</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8044-97dc-c17ed8c47887" class="bulleted-list"><li style="list-style-type:disc">Divorce socially costly but possible</li></ul></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-809f-b198-efea014e1a09" class="">Seen in:</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80c2-9d7b-c3ab8bcf583c" class="bulleted-list"><li style="list-style-type:disc">post-WWII West</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8057-bbdc-e4850d6222fb" class="bulleted-list"><li style="list-style-type:disc">high-trust welfare states</li></ul></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-802a-9e53-f9ea259313b1"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-8077-ba64-fcbac5a4832f" class="">Basin D: Hyperchoice Pairing</h2></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-803d-abe2-e55bb039643d" class="">High mobility + high information noise + low enforcement.</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8025-98ca-e5b4911096f5" class="bulleted-list"><li style="list-style-type:disc">Delayed commitment</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80db-b454-ea2c4da6df99" class="bulleted-list"><li style="list-style-type:disc">High standards</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80f2-8c88-ee9ef4296336" class="bulleted-list"><li style="list-style-type:disc">High loneliness</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8046-8e42-fc018dac714d" class="bulleted-list"><li style="list-style-type:disc">Fragmented bonding</li></ul></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-800b-99ad-c370323d0d5e" class="">Seen in:</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-804c-9153-edb369b66119" class="bulleted-list"><li style="list-style-type:disc">global cities</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-808b-ae28-e6f0f7efa7ad" class="bulleted-list"><li style="list-style-type:disc">platform-dominant markets</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80f5-802b-c36c6177da64" class="bulleted-list"><li style="list-style-type:disc">post-materialist elites</li></ul></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-8050-b866-fcf88b607099"/></div><div style="display:contents" dir="auto"><h1 id="30dc5e6f-95bd-8032-863a-d3248eba2707" class="">IV. Phase Transition Model (Deep)</h1></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-805c-b1d8-cbced58b0b4a" class="">Civilizations don’t change smoothly.</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8054-bbba-cbba4589189c" class="">They shift when control variables cross thresholds.</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8091-ae8c-d53cedc05635" class="">Example:</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80ff-84cb-c22288896060" class="">If:</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-80f4-8e21-ebd570a06933" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
M \uparrow \uparrow</code></pre></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8023-a03d-c4a9a9cc7c05" class="">I \uparrow \uparrow<br/></p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-800a-9987-f949cbb06bd9" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
L \downarrow</code></pre></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80d4-aa37-e173dbd0e532" class="">Then system moves from Companionate → Hyperchoice.</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8085-b771-ed796a401b21" class="">If:</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-8032-91c3-eda4ba39d04a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Volatility \uparrow</code></pre></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80c4-8306-f7df74f7bfc1" class="">Trust \downarrow<br/></p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-802c-8277-e118731ce323" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Violence \uparrow</code></pre></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80cc-a644-eef9f3c94fd8" class="">System moves Hyperchoice → Survival.</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8064-b37c-f77c793d7fe0" class="">These transitions repeat cyclically across history.</p></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-8090-bfea-d4e74906d1e1"/></div><div style="display:contents" dir="auto"><h1 id="30dc5e6f-95bd-8036-99cb-f428b7a5c181" class="">V. Where “Exceptional Women” Sit Structurally</h1></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8054-beb2-e129ab4ab78a" class="">A high-competence woman is:</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-805b-9dc7-d459d5939276" class="">High K (competence capital)<br/>High P potential (status convertible)</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8016-8789-ed1fd0668da4" class="">Her romantic stability depends on regime:</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80d8-b959-d932402588c2" class="bulleted-list"><li style="list-style-type:disc">Basin B (Lineage): tolerated if aligned to family power</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80a5-a9d6-cc48e4f101d3" class="bulleted-list"><li style="list-style-type:disc">Basin C (Companionate): attractive if not destabilizing male ego</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8033-9300-fc8b04167bb3" class="bulleted-list"><li style="list-style-type:disc">Basin D (Hyperchoice): polarizing — admired but filtered by insecure men</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8017-b0a5-d03428a5e1e0" class="bulleted-list"><li style="list-style-type:disc">Basin A (Survival): competence highly valued if it increases survival</li></ul></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8038-b249-f3eb35051c5b" class="">So the equation becomes:</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-80e0-9395-d64bab9cd224" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
Romantic\ Stability = f(Partner\ Security,\ System\ Basin,\ Polarity\ Balance)</code></pre></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80d7-9e96-e893d7056763" class="">Not just “are men attracted to intelligence”.</p></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-8043-a8c4-ecd2be9401ea"/></div><div style="display:contents" dir="auto"><h1 id="30dc5e6f-95bd-80fe-a4c1-d7b888aae7ee" class="">VI. Across 100,000 Years — The Meta Pattern</h1></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80ec-ae6f-f1dffcb3c257" class="numbered-list" start="1"><li>Energy surplus rises → individual choice rises.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-800b-925a-f52e4aa55d48" class="numbered-list" start="2"><li>Choice rises → standards rise.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80f8-b813-dd4ea15a5f3b" class="numbered-list" start="3"><li>Standards rise → pairing delay rises.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80ce-939a-c965a7eca43c" class="numbered-list" start="4"><li>Delay rises → fertility drops.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80ec-ad29-c5ddd762ff33" class="numbered-list" start="5"><li>Fertility drops → system destabilizes.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-807a-8cf4-dc4013ac918f" class="numbered-list" start="6"><li>Crisis increases → system re-polarizes.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80fe-b4bb-d0535d17b497" class="numbered-list" start="7"><li>Cycle repeats.</li></ol></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80c2-bbde-d87aa5bad4ae" class="">This loop is consistent from:</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8020-be74-d45b356b7c2d" class="bulleted-list"><li style="list-style-type:disc">late Rome</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80e1-b51e-e1bf173d3a0e" class="bulleted-list"><li style="list-style-type:disc">Song dynasty</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8053-a21f-cbb76cfe16f4" class="bulleted-list"><li style="list-style-type:disc">19th century France</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80ea-b5fb-ce7f9adad66d" class="bulleted-list"><li style="list-style-type:disc">modern Japan</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80f5-ac0f-cf3145bf4217" class="bulleted-list"><li style="list-style-type:disc">modern Western Europe</li></ul></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8031-81a5-cc0bc299290f" class="">Different surface.<br/>Same structure.</p></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-8046-99d6-e10a8088c565"/></div><div style="display:contents" dir="auto"><h1 id="30dc5e6f-95bd-801d-b534-ed3238b2ce75" class="">VII. The Deepest Layer: Entropy vs Structure</h1></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80eb-902e-de134d714b2f" class="">Attraction markets behave like thermodynamic systems.</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80a3-a4d0-d1ed9229acfa" class="">Define:</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80fd-a003-fa27e9b7f29a" class="">Order (O) = stable family structures</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8035-8252-f5664010e494" class="">Entropy (H) = fragmented relationships + instability</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-8049-ba0b-faab09d23c1f" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\frac{dO}{dt} = InstitutionalStrength - Mobility - InformationNoise</code></pre></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-800b-856d-c9cd5bea5e8e" class="">When entropy exceeds repair capacity:</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8014-9062-c44516e408ad" class="">Family formation collapses.<br/>Loneliness rises.<br/>Birth rate collapses.<br/>Then enforcement or crisis reorders the field.</p></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-8006-9832-fb94bbea2900"/></div><div style="display:contents" dir="auto"><h1 id="30dc5e6f-95bd-8033-99bb-c4ad43254d51" class="">VIII. Why This Matters</h1></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80b7-bf7d-e3f47297128b" class="">You’re not asking about romance.</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8068-9560-c9793206d711" class="">You’re modeling:</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80d9-9997-f7d376897790" class="">Attraction as a civilizational variable.</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80a6-9884-dd33d2ab5ec1" class="">And at deep layer:</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-803f-bb60-e15e8b5565b3" class="">It’s not ideology.<br/>It’s constraint physics.</p></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-8011-a99c-c4fb4c1abef4"/></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-802a-ad87-fc5c1ecb6f44" class="">If you want to go deeper, we can now:</p></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80d6-a5b6-ee1c4b807cc4" class="numbered-list" start="1"><li>Model AI as an entropy amplifier or regulator.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80c5-aad1-c6ce4ae9d0b3" class="numbered-list" start="2"><li>Map Western vs East Asia onto the 4 basins precisely.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80ab-8e2b-de82a27f2e9b" class="numbered-list" start="3"><li>Quantify divorce probability under different variable combinations.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-8028-bd3a-cee28b6e206d" class="numbered-list" start="4"><li>Go micro → map this to neurobiology and reproductive strategy at cellular level.</li></ol></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8073-bc03-ed8e2151333a" class="">Pick direction.</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8062-87c0-f506e4fc7003" class="">Got it — here is the <strong>“invariants × civilization-regime” matrix</strong> (a <strong>19×19</strong> grid) you can reuse as a classifier.</p></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-806b-8df7-da0dc4b48fd5" class="">Legend</h3></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-804f-b8b5-e9b40e1f7168" class="bulleted-list"><li style="list-style-type:disc"><strong>++</strong> very high / dominates</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8010-a614-e3d69ee52223" class="bulleted-list"><li style="list-style-type:disc"><strong>+</strong> high</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80ee-bb95-e2874a963082" class="bulleted-list"><li style="list-style-type:disc"><strong>0</strong> medium / mixed</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80c0-b1f7-fb2f1f47692f" class="bulleted-list"><li style="list-style-type:disc"> low</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-802a-8aa7-e9fad51b09e7" class="bulleted-list"><li style="list-style-type:disc"><strong>-</strong> very low<br/>(Interpret each cell as the <em>typical structural level</em> of that variable inside that regime.)</li></ul></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-8094-8d4b-eac72ffce9a7"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-8067-ac5d-d0d0ff9efcd4" class="">Column key (19 civilizational regimes)</h2></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80b4-bb1a-d189d680cfb8" class="numbered-list" start="1"><li><strong>F-Band</strong> (forager band, high transparency)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80b4-bcba-d38a2d6b7745" class="numbered-list" start="2"><li><strong>F-Coast</strong> (forager w/ seasonal surplus, trade)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-8029-affc-e2864b426f28" class="numbered-list" start="3"><li><strong>Pastoral</strong> (herder/raid ecology)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80d3-8fc3-f9d8ac60af56" class="numbered-list" start="4"><li><strong>Warrior</strong> (high violence + honor)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-8017-92fd-fd767ba08620" class="numbered-list" start="5"><li><strong>Agr-early</strong> (early agrarian lineage)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80ef-a802-defe2373d27f" class="numbered-list" start="6"><li><strong>Feudal</strong> (land + hierarchy + kin control)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-8039-bb3b-c9fd9dd9c5c5" class="numbered-list" start="7"><li><strong>Imperial</strong> (bureaucratic empire)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80f5-91f8-ff4a93693285" class="numbered-list" start="8"><li><strong>City-State</strong> (merchant republic / port hub)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-806a-9127-eab254a0fe1e" class="numbered-list" start="9"><li><strong>Theocracy</strong> (formal religious enforcement)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-805f-8f6e-cb7115d15ab2" class="numbered-list numbered-list-digits-2" start="10"><li><strong>Honor/Shame</strong> (tight communities, reputation policing)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-8079-951f-cff95454f24b" class="numbered-list numbered-list-digits-2" start="11"><li><strong>Frontier</strong> (weak institutions, fast mobility)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-8012-a1d7-e2506c7dfbf6" class="numbered-list numbered-list-digits-2" start="12"><li><strong>Industrial-E</strong> (early industrial, bourgeois norms)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80b2-a949-c738f48db509" class="numbered-list numbered-list-digits-2" start="13"><li><strong>Industrial-L</strong> (late industrial, mass consumer)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-800a-8dd4-cd481165f029" class="numbered-list numbered-list-digits-2" start="14"><li><strong>Welfare</strong> (high safety net, high trust institutions)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-8062-aa1f-f02e7c5e800a" class="numbered-list numbered-list-digits-2" start="15"><li><strong>Global City</strong> (neoliberal metro, credential sorting)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80c6-8f7d-d911b68c7af4" class="numbered-list numbered-list-digits-2" start="16"><li><strong>Postmaterial</strong> (elite values, self-actualization)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-8047-807f-f7409a634d9b" class="numbered-list numbered-list-digits-2" start="17"><li><strong>Platform</strong> (app-mediated dating market)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-8072-8b2a-de6fcbbf8943" class="numbered-list numbered-list-digits-2" start="18"><li><strong>AI/Surveil</strong> (algorithmic sorting + monitoring)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80f1-9187-c77cbaa5ca5b" class="numbered-list numbered-list-digits-2" start="19"><li><strong>Crisis</strong> (recession/war/instability shock)</li></ol></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-80b6-b013-c1fc8c1d5c40"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-8092-a41e-c00f459eceef" class="">Row key (19 invariants / control variables)</h2></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8096-886a-f357aeeef92a" class="">I’m using “system knobs” you can set from observation (often without formal data).</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8022-91fc-c50c3b0b9b4b" class="">R1 <strong>Energy surplus (E)</strong></p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80ed-bc71-c74287a855db" class="">R2 <strong>Resource volatility (Vol)</strong></p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8025-bd74-e956fc6692df" class="">R3 <strong>Violence/physical risk (V)</strong></p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80cd-82bb-dd2bfe573c4b" class="">R4 <strong>Mobility/exit (M)</strong></p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-807a-b36e-f56302fe4e05" class="">R5 <strong>Kin control strength (K)</strong></p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8032-8abd-fa19ab1f9de5" class="">R6 <strong>Legal enforcement strength (L)</strong></p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8091-b25b-d0c4b0e9372b" class="">R7 <strong>Inequality / hierarchy steepness (H)</strong></p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8051-b7b1-ec78cc7041bc" class="">R8 <strong>Child cost burden (C)</strong></p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80a4-b450-d65507ee4f3b" class="">R9 <strong>Female economic autonomy (FA)</strong></p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-805f-94da-fe7116d3fdb2" class="">R10 <strong>Male provisioning edge (MP)</strong></p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8013-ae87-f25252a214cb" class="">R11 <strong>Reputation transparency (RT)</strong></p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8021-b332-e38d07cc4bae" class="">R12 <strong>Information manipulation load (IM)</strong></p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8094-a75c-cca2534091c3" class="">R13 <strong>Tech mediation of pairing (T)</strong></p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80dc-9281-d36925dbc6ea" class="">R14 <strong>Labor specialization (LS)</strong></p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80a4-b25f-e61860d409b5" class="">R15 <strong>Urban density / anonymity (UD)</strong></p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8064-bfdc-c043a0428589" class="">R16 <strong>Housing constraint (HC)</strong></p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80bc-a341-d77bdadc77ea" class="">R17 <strong>Health burden / pathogen load (HB)</strong></p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-809c-b61d-eaa4d8be0be6" class="">R18 <strong>Norm strictness / sanctioning (NS)</strong></p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8084-a838-ec69353ce880" class="">R19 <strong>Institutional trust (IT)</strong></p></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-804d-982c-ee2601a18448"/></div><div style="display:contents" dir="auto"><h1 id="30dc5e6f-95bd-8087-8af5-d8ae36e1225c" class="">19×19 Matrix (++, +, 0, -, --)</h1></div><div style="display:contents" dir="auto"><blockquote id="30dc5e6f-95bd-809b-9f64-f065cd59b0d2" class="">Columns are <strong>1→19</strong> as defined above.</blockquote></div><div style="display:contents" dir="ltr"><table id="30dc5e6f-95bd-80be-a005-ecb051dc43f3" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="30dc5e6f-95bd-80b3-a94c-cbeef29daf0a"><th id="ayt\" class="simple-table-header-color simple-table-header">Row (variable)</th><th id="llVj" class="simple-table-header-color simple-table-header">1</th><th id="TTeP" class="simple-table-header-color simple-table-header">2</th><th id="J;l?" class="simple-table-header-color simple-table-header">3</th><th id="@@:]" class="simple-table-header-color simple-table-header">4</th><th id="ZxAN" class="simple-table-header-color simple-table-header">5</th><th id="bL&lt;J" class="simple-table-header-color simple-table-header">6</th><th id="gz&lt;d" class="simple-table-header-color simple-table-header">7</th><th id="o:La" class="simple-table-header-color simple-table-header">8</th><th id="pHE[" class="simple-table-header-color simple-table-header">9</th><th id="P~`[" class="simple-table-header-color simple-table-header">10</th><th id="F`pF" class="simple-table-header-color simple-table-header">11</th><th id="AiNP" class="simple-table-header-color simple-table-header">12</th><th id="^riF" class="simple-table-header-color simple-table-header">13</th><th id="hnuc" class="simple-table-header-color simple-table-header">14</th><th id="wsx\" class="simple-table-header-color simple-table-header">15</th><th id="qB?W" class="simple-table-header-color simple-table-header">16</th><th id="btT]" class="simple-table-header-color simple-table-header">17</th><th id="tgXN" class="simple-table-header-color simple-table-header">18</th><th id="ySX[" class="simple-table-header-color simple-table-header">19</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="30dc5e6f-95bd-80d2-9b2a-cd8ba6855947"><td id="ayt\" class="">R1 E</td><td id="llVj" class="">-</td><td id="TTeP" class="">0</td><td id="J;l?" class="">0</td><td id="@@:]" class="">-</td><td id="ZxAN" class="">0</td><td id="bL&lt;J" class="">0</td><td id="gz&lt;d" class="">+</td><td id="o:La" class="">+</td><td id="pHE[" class="">0</td><td id="P~`[" class="">0</td><td id="F`pF" class="">0</td><td id="AiNP" class="">+</td><td id="^riF" class="">++</td><td id="hnuc" class="">++</td><td id="wsx\" class="">++</td><td id="qB?W" class="">++</td><td id="btT]" class="">++</td><td id="tgXN" class="">++</td><td id="ySX[" class="">-</td></tr></div><div style="display:contents" dir="ltr"><tr id="30dc5e6f-95bd-806d-ac52-e9a1f2bc2f69"><td id="ayt\" class="">R2 Vol</td><td id="llVj" class="">+</td><td id="TTeP" class="">0</td><td id="J;l?" class="">+</td><td id="@@:]" class="">+</td><td id="ZxAN" class="">0</td><td id="bL&lt;J" class="">0</td><td id="gz&lt;d" class="">0</td><td id="o:La" class="">0</td><td id="pHE[" class="">0</td><td id="P~`[" class="">0</td><td id="F`pF" class="">+</td><td id="AiNP" class="">0</td><td id="^riF" class="">-</td><td id="hnuc" class="">--</td><td id="wsx\" class="">-</td><td id="qB?W" class="">-</td><td id="btT]" class="">0</td><td id="tgXN" class="">0</td><td id="ySX[" class="">++</td></tr></div><div style="display:contents" dir="ltr"><tr id="30dc5e6f-95bd-80f2-9aea-e5083b2513f0"><td id="ayt\" class="">R3 V</td><td id="llVj" class="">0</td><td id="TTeP" class="">0</td><td id="J;l?" class="">+</td><td id="@@:]" class="">++</td><td id="ZxAN" class="">0</td><td id="bL&lt;J" class="">+</td><td id="gz&lt;d" class="">0</td><td id="o:La" class="">0</td><td id="pHE[" class="">0</td><td id="P~`[" class="">0/+</td><td id="F`pF" class="">+</td><td id="AiNP" class="">0</td><td id="^riF" class="">-</td><td id="hnuc" class="">--</td><td id="wsx\" class="">-</td><td id="qB?W" class="">-</td><td id="btT]" class="">-</td><td id="tgXN" class="">0</td><td id="ySX[" class="">++</td></tr></div><div style="display:contents" dir="ltr"><tr id="30dc5e6f-95bd-80b6-8feb-d1239934a946"><td id="ayt\" class="">R4 M</td><td id="llVj" class="">0</td><td id="TTeP" class="">+</td><td id="J;l?" class="">+</td><td id="@@:]" class="">+</td><td id="ZxAN" class="">-</td><td id="bL&lt;J" class="">--</td><td id="gz&lt;d" class="">-</td><td id="o:La" class="">+</td><td id="pHE[" class="">-</td><td id="P~`[" class="">--</td><td id="F`pF" class="">++</td><td id="AiNP" class="">0</td><td id="^riF" class="">+</td><td id="hnuc" class="">+</td><td id="wsx\" class="">++</td><td id="qB?W" class="">++</td><td id="btT]" class="">++</td><td id="tgXN" class="">0/+</td><td id="ySX[" class="">+</td></tr></div><div style="display:contents" dir="ltr"><tr id="30dc5e6f-95bd-8069-86c2-c8564f20bcd2"><td id="ayt\" class="">R5 K</td><td id="llVj" class="">+</td><td id="TTeP" class="">+</td><td id="J;l?" class="">0/+</td><td id="@@:]" class="">+</td><td id="ZxAN" class="">++</td><td id="bL&lt;J" class="">++</td><td id="gz&lt;d" class="">+</td><td id="o:La" class="">0/+</td><td id="pHE[" class="">++</td><td id="P~`[" class="">++</td><td id="F`pF" class="">-</td><td id="AiNP" class="">0</td><td id="^riF" class="">-</td><td id="hnuc" class="">-</td><td id="wsx\" class="">--</td><td id="qB?W" class="">--</td><td id="btT]" class="">--</td><td id="tgXN" class="">0/+</td><td id="ySX[" class="">++</td></tr></div><div style="display:contents" dir="ltr"><tr id="30dc5e6f-95bd-80d2-a05e-f0f16b4f18a8"><td id="ayt\" class="">R6 L</td><td id="llVj" class="">-</td><td id="TTeP" class="">-</td><td id="J;l?" class="">-</td><td id="@@:]" class="">0</td><td id="ZxAN" class="">+</td><td id="bL&lt;J" class="">+</td><td id="gz&lt;d" class="">++</td><td id="o:La" class="">+</td><td id="pHE[" class="">++</td><td id="P~`[" class="">+</td><td id="F`pF" class="">-</td><td id="AiNP" class="">+</td><td id="^riF" class="">++</td><td id="hnuc" class="">++</td><td id="wsx\" class="">++</td><td id="qB?W" class="">++</td><td id="btT]" class="">+</td><td id="tgXN" class="">++</td><td id="ySX[" class="">0</td></tr></div><div style="display:contents" dir="ltr"><tr id="30dc5e6f-95bd-8067-a455-ebd597771102"><td id="ayt\" class="">R7 H</td><td id="llVj" class="">0</td><td id="TTeP" class="">0</td><td id="J;l?" class="">+</td><td id="@@:]" class="">+</td><td id="ZxAN" class="">+</td><td id="bL&lt;J" class="">++</td><td id="gz&lt;d" class="">++</td><td id="o:La" class="">+</td><td id="pHE[" class="">+</td><td id="P~`[" class="">+</td><td id="F`pF" class="">+</td><td id="AiNP" class="">+</td><td id="^riF" class="">++</td><td id="hnuc" class="">0/+</td><td id="wsx\" class="">++</td><td id="qB?W" class="">++</td><td id="btT]" class="">++</td><td id="tgXN" class="">++</td><td id="ySX[" class="">++</td></tr></div><div style="display:contents" dir="ltr"><tr id="30dc5e6f-95bd-8049-bd50-f8b5e79374e4"><td id="ayt\" class="">R8 C</td><td id="llVj" class="">0</td><td id="TTeP" class="">0</td><td id="J;l?" class="">0</td><td id="@@:]" class="">0/+</td><td id="ZxAN" class="">+</td><td id="bL&lt;J" class="">++</td><td id="gz&lt;d" class="">++</td><td id="o:La" class="">+</td><td id="pHE[" class="">+</td><td id="P~`[" class="">+</td><td id="F`pF" class="">0</td><td id="AiNP" class="">+</td><td id="^riF" class="">++</td><td id="hnuc" class="">++</td><td id="wsx\" class="">++</td><td id="qB?W" class="">++</td><td id="btT]" class="">++</td><td id="tgXN" class="">++</td><td id="ySX[" class="">++</td></tr></div><div style="display:contents" dir="ltr"><tr id="30dc5e6f-95bd-80fb-b0c4-de2abec17888"><td id="ayt\" class="">R9 FA</td><td id="llVj" class="">0/+</td><td id="TTeP" class="">0/+</td><td id="J;l?" class="">-</td><td id="@@:]" class="">-</td><td id="ZxAN" class="">--</td><td id="bL&lt;J" class="">--</td><td id="gz&lt;d" class="">-</td><td id="o:La" class="">0</td><td id="pHE[" class="">--</td><td id="P~`[" class="">--</td><td id="F`pF" class="">+</td><td id="AiNP" class="">0/+</td><td id="^riF" class="">+</td><td id="hnuc" class="">++</td><td id="wsx\" class="">++</td><td id="qB?W" class="">++</td><td id="btT]" class="">++</td><td id="tgXN" class="">+</td><td id="ySX[" class="">0</td></tr></div><div style="display:contents" dir="ltr"><tr id="30dc5e6f-95bd-8041-b331-d6b31960ab74"><td id="ayt\" class="">R10 MP</td><td id="llVj" class="">+</td><td id="TTeP" class="">+</td><td id="J;l?" class="">++</td><td id="@@:]" class="">++</td><td id="ZxAN" class="">++</td><td id="bL&lt;J" class="">++</td><td id="gz&lt;d" class="">+</td><td id="o:La" class="">+</td><td id="pHE[" class="">++</td><td id="P~`[" class="">++</td><td id="F`pF" class="">+</td><td id="AiNP" class="">+</td><td id="^riF" class="">0</td><td id="hnuc" class="">--</td><td id="wsx\" class="">-</td><td id="qB?W" class="">-</td><td id="btT]" class="">--</td><td id="tgXN" class="">--</td><td id="ySX[" class="">++</td></tr></div><div style="display:contents" dir="ltr"><tr id="30dc5e6f-95bd-80e2-9332-d26fc0f86757"><td id="ayt\" class="">R11 RT</td><td id="llVj" class="">++</td><td id="TTeP" class="">+</td><td id="J;l?" class="">+</td><td id="@@:]" class="">+</td><td id="ZxAN" class="">++</td><td id="bL&lt;J" class="">++</td><td id="gz&lt;d" class="">+</td><td id="o:La" class="">0</td><td id="pHE[" class="">++</td><td id="P~`[" class="">++</td><td id="F`pF" class="">0</td><td id="AiNP" class="">0</td><td id="^riF" class="">-</td><td id="hnuc" class="">-</td><td id="wsx\" class="">--</td><td id="qB?W" class="">--</td><td id="btT]" class="">--</td><td id="tgXN" class="">--</td><td id="ySX[" class="">+</td></tr></div><div style="display:contents" dir="ltr"><tr id="30dc5e6f-95bd-809d-995b-e0fdbb031375"><td id="ayt\" class="">R12 IM</td><td id="llVj" class="">-</td><td id="TTeP" class="">0</td><td id="J;l?" class="">0</td><td id="@@:]" class="">+</td><td id="ZxAN" class="">+</td><td id="bL&lt;J" class="">+</td><td id="gz&lt;d" class="">++</td><td id="o:La" class="">+</td><td id="pHE[" class="">++</td><td id="P~`[" class="">+</td><td id="F`pF" class="">0</td><td id="AiNP" class="">+</td><td id="^riF" class="">++</td><td id="hnuc" class="">+</td><td id="wsx\" class="">++</td><td id="qB?W" class="">++</td><td id="btT]" class="">++</td><td id="tgXN" class="">++</td><td id="ySX[" class="">++</td></tr></div><div style="display:contents" dir="ltr"><tr id="30dc5e6f-95bd-80d1-9c60-c3923633444b"><td id="ayt\" class="">R13 T</td><td id="llVj" class="">--</td><td id="TTeP" class="">--</td><td id="J;l?" class="">--</td><td id="@@:]" class="">--</td><td id="ZxAN" class="">--</td><td id="bL&lt;J" class="">--</td><td id="gz&lt;d" class="">-</td><td id="o:La" class="">0</td><td id="pHE[" class="">-</td><td id="P~`[" class="">-</td><td id="F`pF" class="">--</td><td id="AiNP" class="">0</td><td id="^riF" class="">+</td><td id="hnuc" class="">+</td><td id="wsx\" class="">++</td><td id="qB?W" class="">++</td><td id="btT]" class="">++</td><td id="tgXN" class="">++</td><td id="ySX[" class="">+</td></tr></div><div style="display:contents" dir="ltr"><tr id="30dc5e6f-95bd-8071-a817-c1741486982a"><td id="ayt\" class="">R14 LS</td><td id="llVj" class="">-</td><td id="TTeP" class="">-</td><td id="J;l?" class="">-</td><td id="@@:]" class="">-</td><td id="ZxAN" class="">0</td><td id="bL&lt;J" class="">0</td><td id="gz&lt;d" class="">++</td><td id="o:La" class="">++</td><td id="pHE[" class="">+</td><td id="P~`[" class="">0</td><td id="F`pF" class="">0</td><td id="AiNP" class="">+</td><td id="^riF" class="">++</td><td id="hnuc" class="">++</td><td id="wsx\" class="">++</td><td id="qB?W" class="">++</td><td id="btT]" class="">+</td><td id="tgXN" class="">++</td><td id="ySX[" class="">0</td></tr></div><div style="display:contents" dir="ltr"><tr id="30dc5e6f-95bd-8064-8f12-f512a2332474"><td id="ayt\" class="">R15 UD</td><td id="llVj" class="">--</td><td id="TTeP" class="">--</td><td id="J;l?" class="">--</td><td id="@@:]" class="">--</td><td id="ZxAN" class="">-</td><td id="bL&lt;J" class="">-</td><td id="gz&lt;d" class="">+</td><td id="o:La" class="">++</td><td id="pHE[" class="">0</td><td id="P~`[" class="">-</td><td id="F`pF" class="">-</td><td id="AiNP" class="">+</td><td id="^riF" class="">++</td><td id="hnuc" class="">++</td><td id="wsx\" class="">++</td><td id="qB?W" class="">++</td><td id="btT]" class="">++</td><td id="tgXN" class="">++</td><td id="ySX[" class="">0</td></tr></div><div style="display:contents" dir="ltr"><tr id="30dc5e6f-95bd-80f1-941d-e787a040139a"><td id="ayt\" class="">R16 HC</td><td id="llVj" class="">--</td><td id="TTeP" class="">--</td><td id="J;l?" class="">--</td><td id="@@:]" class="">--</td><td id="ZxAN" class="">-</td><td id="bL&lt;J" class="">-</td><td id="gz&lt;d" class="">0</td><td id="o:La" class="">0</td><td id="pHE[" class="">0</td><td id="P~`[" class="">-</td><td id="F`pF" class="">-</td><td id="AiNP" class="">0</td><td id="^riF" class="">+</td><td id="hnuc" class="">0/+</td><td id="wsx\" class="">++</td><td id="qB?W" class="">++</td><td id="btT]" class="">++</td><td id="tgXN" class="">++</td><td id="ySX[" class="">+</td></tr></div><div style="display:contents" dir="ltr"><tr id="30dc5e6f-95bd-8098-9436-c1541485b1a7"><td id="ayt\" class="">R17 HB</td><td id="llVj" class="">0</td><td id="TTeP" class="">0</td><td id="J;l?" class="">0</td><td id="@@:]" class="">0</td><td id="ZxAN" class="">+</td><td id="bL&lt;J" class="">+</td><td id="gz&lt;d" class="">0/+</td><td id="o:La" class="">0</td><td id="pHE[" class="">0/+</td><td id="P~`[" class="">0/+</td><td id="F`pF" class="">0</td><td id="AiNP" class="">0</td><td id="^riF" class="">-</td><td id="hnuc" class="">--</td><td id="wsx\" class="">-</td><td id="qB?W" class="">-</td><td id="btT]" class="">-</td><td id="tgXN" class="">-</td><td id="ySX[" class="">+</td></tr></div><div style="display:contents" dir="ltr"><tr id="30dc5e6f-95bd-8029-8973-e7c5cf0ac7c7"><td id="ayt\" class="">R18 NS</td><td id="llVj" class="">+</td><td id="TTeP" class="">+</td><td id="J;l?" class="">+</td><td id="@@:]" class="">++</td><td id="ZxAN" class="">++</td><td id="bL&lt;J" class="">++</td><td id="gz&lt;d" class="">+</td><td id="o:La" class="">0/+</td><td id="pHE[" class="">++</td><td id="P~`[" class="">++</td><td id="F`pF" class="">-</td><td id="AiNP" class="">0/+</td><td id="^riF" class="">-</td><td id="hnuc" class="">-</td><td id="wsx\" class="">--</td><td id="qB?W" class="">--</td><td id="btT]" class="">--</td><td id="tgXN" class="">0/+</td><td id="ySX[" class="">++</td></tr></div><div style="display:contents" dir="ltr"><tr id="30dc5e6f-95bd-806a-9576-ec4ad56f11a3"><td id="ayt\" class="">R19 IT</td><td id="llVj" class="">+</td><td id="TTeP" class="">+</td><td id="J;l?" class="">-</td><td id="@@:]" class="">-</td><td id="ZxAN" class="">0/+</td><td id="bL&lt;J" class="">0</td><td id="gz&lt;d" class="">+</td><td id="o:La" class="">+</td><td id="pHE[" class="">+</td><td id="P~`[" class="">0/+</td><td id="F`pF" class="">-</td><td id="AiNP" class="">0/+</td><td id="^riF" class="">0/+</td><td id="hnuc" class="">++</td><td id="wsx\" class="">+</td><td id="qB?W" class="">+</td><td id="btT]" class="">-</td><td id="tgXN" class="">0</td><td id="ySX[" class="">--</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-80eb-ba4f-c1bba964ff87"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-8041-a459-d8530db31324" class="">How to <em>use</em> this matrix (the “classifier equation”)</h2></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-804d-bb7b-c390c96467d5" class="">Step 1 — Encode your society/scene into a 19-vector</h3></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-8045-99ef-d3d24f37498e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
x = [E, Vol, V, M, K, L, H, C, FA, MP, RT, IM, T, LS, UD, HC, HB, NS, IT]</code></pre></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-80bc-9736-e1dbf09cbdc6" class="">Step 2 — Each regime column is a “prototype vector”</h3></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80e2-b8b8-f406f4ce9013" class="">Compute similarity:</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-80c9-9551-f94488a2318d" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\text{Score}(j)= -\sum_{i=1}^{19} \alpha_i \, |x_i - c_{ij}|</code></pre></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-80b0-a734-f4d335ef55dc" class="">Step 3 — Predict attraction weights from variables</h3></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-806e-ab0f-d88dd3bb514c" class="">A simple mapping (works cross-civilization):</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-800e-a968-e90e51561608" class="bulleted-list"><li style="list-style-type:disc"><strong>Provisioning weight</strong></li></ul></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-8062-9cf2-da9017f9b96e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
w_S \propto Vol + V + C - E</code></pre></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-807a-a30c-f9c573a40a53" class="bulleted-list"><li style="list-style-type:disc"><strong>Status weight</strong></li></ul></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-8033-9abe-e3a9c9724c49" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
w_P \propto H + UD + IM</code></pre></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-800b-9a84-d674339b581b" class="bulleted-list"><li style="list-style-type:disc"><strong>Reputation / conformity weight</strong></li></ul></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-804e-b827-c286c69e1dfb" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
w_C \propto RT + NS + K</code></pre></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80fe-8538-f3961028b4e5" class="bulleted-list"><li style="list-style-type:disc"><strong>Nervous-system fit / stability weight</strong></li></ul></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-802d-b9b0-d5ec486717a1" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
w_A \propto V + Vol + IM - IT</code></pre></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8011-a721-c2bd47fcb876" class="bulleted-list"><li style="list-style-type:disc"><strong>“Genius/competence woman” acceptance</strong></li></ul></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-80a5-a291-d282936bfd0e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\text{Acceptance} \propto FA + IT + E - NS - K</code></pre></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-809b-8e63-fdddb477e272"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-805d-a21c-e8a595571313" class="">What this matrix implies about “female thiên tài” being attractive</h2></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80f3-9e6b-c51036baec0a" class="">It’s not “men” as one group — it’s <strong>regime + male subtype</strong>.</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80f1-9dee-df4990538d49" class="">A competence-heavy woman is most romantically advantaged when:</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80b1-aa73-ccdef2453126" class="bulleted-list"><li style="list-style-type:disc"><strong>FA is high</strong>, <strong>IT is high</strong>, <strong>NS and K are low</strong>, and <strong>status is credentialized</strong> (Global City / Postmaterial / Welfare).</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8069-af5d-dfa55e4a227b" class="bulleted-list"><li style="list-style-type:disc">In high <strong>NS+K</strong> regimes (Feudal / Theocracy / Honor/Shame), she’s often <strong>respected</strong> but pressured into <strong>role-compliance</strong>.</li></ul></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8083-9837-fdcdc11d6c96" class="">You can treat it as a conversion equation:</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-8074-815e-d0eddff276d8" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\text{Romantic conversion} = \text{Respect} \times \text{Polarity} \times \text{Safety}</code></pre></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8001-97ee-ed47a7ec20a1" class="">High competence boosts <strong>Respect</strong>.</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8089-955c-f92d27b89b3c" class="">But if it threatens partner ego or gender scripts, <strong>Polarity</strong> drops unless the partner is secure/high-competence too.</p></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-80c7-b6ae-fe9516c0a503"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-8021-a0c0-f168332bcebb" class="">Next (still “Option 2”): do you want <strong>12×12</strong> or the <strong>19×19 into a 19×19 matrix-of-outcomes</strong>?</h2></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80fa-b9d5-c4327c6a1ace" class="">I can output either of these, pick one:</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80d1-b630-da9a0fcf2f3f" class=""><strong>2A)</strong> A <strong>19×19 outcomes matrix</strong> (each regime → typical outcomes: marriage form, jealousy policing, divorce dynamics, “mistress” dynamics, loneliness, etc.)</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8026-880e-fa5b718f9978" class=""><strong>2B)</strong> A <strong>12×12 compressed</strong> version (same logic, easier to use daily)</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80c2-a646-dd6731256972" class="">Reply with <strong>2A</strong> or <strong>2B</strong>.</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8050-8232-e304cece42c0" class="">Below is a <strong>cross-civilizational “attraction map”</strong>: the <strong>invariants</strong> (what stays true across time/species), plus the <strong>clusters</strong> (how attraction reorganizes under different ecologies, technologies, laws, and status systems). Think of it as a physics-of-mating lens: same forces, different boundary conditions.</p></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-808b-a074-d2af40803099"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-8055-8b5b-d8297232ba08" class="">0) Core premise</h2></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-809c-a0bd-e1a074cce418" class="">Across time + civilizations, <strong>attraction is a multi-objective optimization under constraints</strong>:</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-806f-91ac-ed5b51d8e152" class=""><strong>Choose mate</strong> to maximize:</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8036-86f5-ecb7f50d4732" class="bulleted-list"><li style="list-style-type:disc"><strong>R</strong> = reproductive viability (fertility/health/genes)</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80fa-9e08-f378403e8a3f" class="bulleted-list"><li style="list-style-type:disc"><strong>S</strong> = survival + provisioning (resources, safety, competence)</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80ac-a653-f29468b67031" class="bulleted-list"><li style="list-style-type:disc"><strong>P</strong> = social positioning (status, alliances, legitimacy)</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-808d-95d6-e2d9ed46d2ed" class="bulleted-list"><li style="list-style-type:disc"><strong>A</strong> = affect regulation (nervous system fit, attachment safety)</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80be-85cf-d3e9862b33c5" class="bulleted-list"><li style="list-style-type:disc"><strong>C</strong> = cultural fit (norms, religion, class, family compatibility)</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-808d-98e0-f01401901ebd" class="bulleted-list"><li style="list-style-type:disc"><strong>F</strong> = future option value (mobility, adaptability, network)</li></ul></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80e0-80cd-f710c7ec7b72" class="">A simple invariant form:</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-8098-ab7f-c3c586fa3313" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
U = w_R R + w_S S + w_P P + w_A A + w_C C + w_F F - \text{Costs}(\text{risk}, \text{conflict}, \text{sanction})</code></pre></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-801c-bd3a-cd7efa29e79d" class="">Civilizations differ mainly by the <strong>weights</strong>  and the <strong>cost functions</strong> (sanctions, scarcity, policing, reputation).</p></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-80fa-bcbe-dd624eab4a88"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-80fa-bdef-ef9e62723eb8" class="">1) The universal invariants (time-proof)</h2></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8041-818b-f8dd1c025b38" class="">These show up in hunter-gatherers, empires, industrial states, and online dating:</p></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-80d4-a3b6-d2ffa6dc9e7f" class="">I1 — <strong>Scarcity amplifies provisioning</strong></h3></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80ad-8e54-ea19d05d16c0" class="">When resources are uncertain, <strong>competence + reliability</strong> rises in value.</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-80a8-82bd-ded989cf828a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
w_S \uparrow \text{ as } \text{resource volatility} \uparrow</code></pre></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-80ae-9281-edd57c826146" class="">I2 — <strong>Hierarchy converts into desirability</strong></h3></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80be-a64a-dc332f6d7c22" class="">Where status is transferable (land, titles, credentials, followers), it increases mate value.</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-800c-b17f-f98e0c1b5058" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
P \propto \log(1+\text{status capital})</code></pre></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-804b-ad43-dee74169f603" class="">I3 — <strong>Female choice tightens when female costs are high</strong></h3></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80c3-a2e5-f8d3127df6ce" class="">If pregnancy/child costs and social penalties are high, filtering becomes stricter.</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-80ce-836c-e9366b03aa2b" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\text{Selectivity} \uparrow \text{ as } \text{child cost} \uparrow</code></pre></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-8050-ae08-edf961b0a469" class="">I4 — <strong>Male competition intensifies when variance in payoff increases</strong></h3></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-801d-ba12-ea9f9668765a" class="">If top males can monopolize more resources/partners, competition spikes.</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-805c-ae9b-ecd9755df38e" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\text{male competition} \uparrow \text{ as } \text{winner-take-most} \uparrow</code></pre></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-809d-82dd-d6e1cfe1aad8" class="">I5 — <strong>Reputation is always a mating currency</strong></h3></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80d9-a8f8-ef12bd6eefef" class="">Even without money, <strong>trust signals</strong> matter.</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-8085-a93d-ca1bbb568f8b" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\text{Trust} = f(\text{consistency}, \text{third-party validation}, \text{past behavior})</code></pre></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-804b-809e-db9c84b702d4" class="">I6 — <strong>“Signal vs substance” arms race</strong></h3></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8017-8e75-f058425020ff" class="">As signaling gets easier (fashion, curated photos), selection shifts toward costly-to-fake signals (track record, network, endurance, competence).</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-8074-9d08-e4884769f2c0" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\text{If } \text{signal noise} \uparrow \Rightarrow \text{substance signals} \uparrow</code></pre></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-800a-9066-d6ed4a123b78" class="">I7 — <strong>Nervous system fit predicts relationship stability</strong></h3></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80cc-9fad-d16c655d525b" class="">Beyond ideology: matching in arousal level, conflict style, repair capacity.</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-806c-9692-f4960773647a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
A \approx \text{co-regulation bandwidth} - \text{trigger load}</code></pre></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-80e4-8baa-db5e131648cd"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-8069-951a-d19fc6ae0e38" class="">2) The 8 civilizational “attraction regimes” (clusters)</h2></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80af-b003-ca33324f879c" class="">Each regime is a stable cluster of norms + constraints. Civilizations move between these depending on energy, law, and tech.</p></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-8046-822d-f0b088aeeb1a" class="">Regime A — <strong>Forager / band</strong></h3></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8091-aa35-fb985c9e25f7" class="bulleted-list"><li style="list-style-type:disc">Constraint: survival, small pool, reputation visibility</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8073-af8d-edaba32dd209" class="bulleted-list"><li style="list-style-type:disc">High value: competence, generosity, emotional steadiness</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80b3-b323-e24cae8b0160" class="bulleted-list"><li style="list-style-type:disc">Pairing: mostly serial monogamy + flexible arrangements (varies)</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80c1-9961-fb520d5a3ef0" class="bulleted-list"><li style="list-style-type:disc">Invariant: “everyone knows everyone” → behavior matters more than branding</li></ul></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-8092-91a3-e2c30cb4816b" class="">Regime B — <strong>Pastoral / warrior</strong></h3></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80b8-8c92-cc0d34818190" class="bulleted-list"><li style="list-style-type:disc">Constraint: violence risk, raiding, mobile wealth</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80f5-8a8b-e1219d4f57bd" class="bulleted-list"><li style="list-style-type:disc">High value: male strength/coalitional power; female kin alliances</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80bc-b91d-d73476cc2d76" class="bulleted-list"><li style="list-style-type:disc">Patterns: polygyny more feasible; honor norms; strong jealousy policing</li></ul></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-802c-bf88-ed8691736152" class="">Regime C — <strong>Agrarian lineage state</strong></h3></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-802f-bfbe-f9e6eb2d6ba9" class="bulleted-list"><li style="list-style-type:disc">Constraint: land inheritance, legitimacy, family strategy</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8062-8df8-fac72a78ca7c" class="bulleted-list"><li style="list-style-type:disc">High value: chastity/reputation, fertility, family alliances, obedience to kin</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80aa-a7a4-f77751536190" class="bulleted-list"><li style="list-style-type:disc">Marriage = property + lineage contract</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80aa-96d1-cb5f565dc275" class="bulleted-list"><li style="list-style-type:disc">Love often secondary; duty primary</li></ul></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-80ee-9b01-e7d8a8658df0" class="">Regime D — <strong>Imperial urban-trade</strong></h3></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8007-979a-f1b9ccd05d8b" class="bulleted-list"><li style="list-style-type:disc">Constraint: class stratification + cosmopolitan mixing</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8083-8804-fa459fb4eab4" class="bulleted-list"><li style="list-style-type:disc">High value: status markers, education, manners, network, patronage</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80f6-84f0-d773450ca1de" class="bulleted-list"><li style="list-style-type:disc">Dual system: public “respectable marriage” + private affairs more common</li></ul></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-80f1-bdb2-ee2f1cf76ea5" class="">Regime E — <strong>Religious-moral enforcement</strong></h3></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-803d-9527-d0b0d6ae8053" class="bulleted-list"><li style="list-style-type:disc">Constraint: strong sanctioning (sin, shame, law)</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80dc-a355-ca3782f2f154" class="bulleted-list"><li style="list-style-type:disc">High value: piety, compliance, family acceptance</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80c3-876b-e3ccb8441413" class="bulleted-list"><li style="list-style-type:disc">Attraction channeled through “approved pathways”</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8041-98af-e123efa1e89c" class="bulleted-list"><li style="list-style-type:disc">Courtship becomes coded (ritualized)</li></ul></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-8040-8e4a-f1a466d90d6c" class="">Regime F — <strong>Industrial-bourgeois</strong></h3></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-802d-969a-ccafc0624e70" class="bulleted-list"><li style="list-style-type:disc">Constraint: wage labor, nuclear household, “companionate marriage” rises</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-802d-89b5-da5345338e12" class="bulleted-list"><li style="list-style-type:disc">High value: reliability, industriousness, domestic competence, respectability</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8017-a52a-f657889044ec" class="bulleted-list"><li style="list-style-type:disc">Love becomes “legitimized,” but still bounded by class</li></ul></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-80fd-9fdb-c2e3b3b2f13c" class="">Regime G — <strong>Late-modern individualist</strong></h3></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8019-a817-dd9c4b383861" class="bulleted-list"><li style="list-style-type:disc">Constraint: hyperchoice, mobility, identity politics, self-actualization scripts</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80f4-9e71-c599b787fe2e" class="bulleted-list"><li style="list-style-type:disc">High value: personality fit, emotional intelligence, sexual chemistry, “growth”</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-809e-a660-d88c8ccb35ff" class="bulleted-list"><li style="list-style-type:disc">But also: marketized attention → inequality in dating outcomes</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-803f-ae5f-f34290a22a15" class="bulleted-list"><li style="list-style-type:disc">Commitment delayed; standards rise; loneliness rises</li></ul></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-80aa-af37-f729678f92e3" class="">Regime H — <strong>Platform/AI mediated</strong></h3></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-807a-b76e-ff0d4ad2c2f0" class="bulleted-list"><li style="list-style-type:disc">Constraint: algorithmic sorting, abundance illusion, deep signaling, surveillance</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8020-87d4-cfc976a5f3ba" class="bulleted-list"><li style="list-style-type:disc">High value: proof of authenticity, stability, privacy safety, calm nervous system</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-809b-b7e3-ed23ec254d74" class="bulleted-list"><li style="list-style-type:disc">“Soft power” (communication) becomes decisive</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80b0-ac2c-f4b024809103" class="bulleted-list"><li style="list-style-type:disc">Co-regulation becomes scarce → prized</li></ul></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-8063-9922-ec3aa4577692"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-803c-8242-e244b6416907" class="">3) Spatial clusters (space matters as much as time)</h2></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-80d4-b342-e48031ae2693" class="">S1 — Frontier zones (new money, weak institutions)</h3></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80b7-b429-f00e7ed18d44" class="bulleted-list"><li style="list-style-type:disc">Attraction leans to <strong>risk tolerance + dominance + opportunism</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-806d-bd2d-c07a6dbfe482" class="bulleted-list"><li style="list-style-type:disc">Faster pairing; faster breakups; higher volatility</li></ul></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-8031-86b7-f7fc2b4433c6" class="">S2 — High-trust dense cities (strong institutions)</h3></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8074-b3b9-e7b573d52ff5" class="bulleted-list"><li style="list-style-type:disc">Attraction leans to <strong>credentials + conscientiousness + reputation networks</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8052-868d-e62a1aedce48" class="bulleted-list"><li style="list-style-type:disc">But also: high standards and slow commitment</li></ul></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-800e-9665-f606d051b390" class="">S3 — Rural/kin-dense</h3></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-804a-a389-fb46f07404b7" class="bulleted-list"><li style="list-style-type:disc">Attraction leans to <strong>family compatibility + stability + role fit</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80c4-842c-dc328aca2e28" class="bulleted-list"><li style="list-style-type:disc">“Social proof” is everything</li></ul></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-8027-aed5-e5c95bbc6465" class="">S4 — Trade hubs / cosmopolitan ports</h3></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8087-bfd5-f602d4d8e5d3" class="bulleted-list"><li style="list-style-type:disc">Attraction leans to <strong>charisma + adaptability + cultural fluency</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8064-9ab5-d9b0a4544feb" class="bulleted-list"><li style="list-style-type:disc">Intercultural pairings more common; identity becomes flexible</li></ul></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-803b-b597-e3c88dfb9d5c"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-80f4-a890-d7533ed6a55b" class="">4) The 6 “attraction capitals” (invariant currency types)</h2></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8026-b72f-f9e6f93746e8" class="">Across civilizations, desirability clusters into <strong>convertible capitals</strong>:</p></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80d5-88ea-c2efdbd62402" class="numbered-list" start="1"><li><strong>Biological capital</strong>: health, fertility cues, symmetry, vitality</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80ad-80d6-d0355b63e404" class="numbered-list" start="2"><li><strong>Competence capital</strong>: skills, discipline, problem solving</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80d1-a01f-d435b6666442" class="numbered-list" start="3"><li><strong>Resource capital</strong>: money/land/access</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80fd-a9c8-ee4ba2bbd12f" class="numbered-list" start="4"><li><strong>Status capital</strong>: rank, prestige, titles, brand, followers</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80f3-be99-caeac8724740" class="numbered-list" start="5"><li><strong>Social capital</strong>: network, alliances, family backing</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-8086-a524-db3a4a97c327" class="numbered-list" start="6"><li><strong>Regulation capital</strong>: calm nervous system, repair skill, loyalty, low chaos</li></ol></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80d2-84e4-e2a3fc1f6765" class="">You can model mate value as:</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-80c4-b5ed-e0cbcf90acde" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
V = \alpha B + \beta K + \gamma R + \delta S + \epsilon N + \zeta G</code></pre></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8050-a874-c180995d6dd1" class="">Where  are the six capitals.</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-802f-b8e0-d8672edf0acf" class="">Civilizations change the coefficients .</p></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-80f6-aad8-c091e828a61f"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-8091-9e06-cb902dbb38a9" class="">5) Where “female genius / exceptional competence” sits in this map</h2></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80a0-a8bd-c1cb7bc83d63" class="">A “thiên tài” woman is basically <strong>high competence capital + often high status potential</strong>. Whether that converts into romantic desirability depends on regime:</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80ed-a7b5-ede1c98cdcad" class="bulleted-list"><li style="list-style-type:disc"><strong>Agrarian lineage / moral enforcement (C/E)</strong>: competence can threaten gender scripts → admired but constrained.</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80c7-bc12-f1d0a267202e" class="bulleted-list"><li style="list-style-type:disc"><strong>Imperial urban-trade (D)</strong>: competence is attractive if it <strong>raises family prestige</strong>; still bounded by class politics.</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80d4-8db8-cf84f71df31d" class="bulleted-list"><li style="list-style-type:disc"><strong>Industrial-bourgeois (F)</strong>: competence attractive if paired with “respectability”; many men prefer it <em>privately</em> not <em>publicly</em>.</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80df-b4a7-d041c92cde30" class="bulleted-list"><li style="list-style-type:disc"><strong>Late modern (G)</strong>: competence polarizes—high attraction for secure/high-competence men; avoidance by ego-fragile men.</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-801e-8263-f4c525cb4d8f" class="bulleted-list"><li style="list-style-type:disc"><strong>Platform/AI (H)</strong>: competence is valuable, but <strong>regulation capital</strong> becomes the real scarcity—calm &gt; brilliance for many.</li></ul></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-802a-8bc5-f92c9e388283" class="">Invariant:</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-8031-8ed7-c801d4f2f982" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\text{If competence signals dominance competition, attraction drops for insecure partners.}</code></pre></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8038-8212-ecb513555a4b" class="">\text{If competence signals shared mission + stability, attraction rises for secure partners.}<br/></p></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-8018-9998-e86797fe19c8"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-80c8-8b9d-dcf6b4d6f112" class="">6) Misunderstandings that repeat across history</h2></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-808d-b7c1-fc949ae7c8d7" class="">M1 — “Respect ≠ desire”</h3></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80d7-90d9-ddeb51e7b5c4" class="">Many men respect power/competence but desire polarity + safety.</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-806e-a9c0-ff6dc85a8a0b" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\text{Desire} \neq \text{Admiration}</code></pre></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-80cc-978a-eba2ed1b8e94" class="">M2 — “Choice overload creates the illusion of better”</h3></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8042-8b13-d23239080937" class="">In high-choice regimes, people keep searching and under-invest.</p></div><div style="display:contents" dir="auto"><pre id="30dc5e6f-95bd-80ac-9061-c43e60d26a9a" class="code code-wrap"><code class="language-latex" style="white-space:pre-wrap;word-break:break-all">
\text{Commitment} \downarrow \text{ when perceived options} \uparrow</code></pre></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-80ad-8795-d419070b5b5c" class="">M3 — “Signals invert under noise”</h3></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80f3-8b6c-c691dbb6c58e" class="">When everyone can <em>look</em> high-status online, real filters shift to:</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8007-aabb-d10e03cc676b" class="bulleted-list"><li style="list-style-type:disc">consistency</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-806a-a8e8-ea175f830253" class="bulleted-list"><li style="list-style-type:disc">calmness</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8067-915b-e587d8e757d1" class="bulleted-list"><li style="list-style-type:disc">verified community reputation</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80a8-8db3-c9c96172bf61" class="bulleted-list"><li style="list-style-type:disc">long-term behavior</li></ul></div><div style="display:contents" dir="auto"><h3 id="30dc5e6f-95bd-8070-aba9-efb420b18d7e" class="">M4 — “Institutions decide the mating market”</h3></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8096-b554-d6b0ffa927aa" class="">Marriage laws, housing, childcare, inheritance, policing—these move attraction weights more than romance philosophies do.</p></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-8020-8d38-cce939bdbac1"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-80fc-9631-d8739e24962a" class="">7) A compact clustering “matrix” you can reuse (invariants → regimes)</h2></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8016-9ca6-d6a6229019e4" class="">If you want a reusable classifier, set these control variables:</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-807a-b323-e63bbae333e1" class="bulleted-list"><li style="list-style-type:disc">= energy abundance (food/wealth stability)</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8003-a540-c7b385d05989" class="bulleted-list"><li style="list-style-type:disc">= legal enforcement + family control</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80ad-903b-ff8717ade924" class="bulleted-list"><li style="list-style-type:disc">= hierarchy steepness (winner-take-most)</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8031-8dff-d6a605208399" class="bulleted-list"><li style="list-style-type:disc">= mobility (can you leave + restart?)</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8070-8167-df31118ad059" class="bulleted-list"><li style="list-style-type:disc">= tech mediation (platform/AI)</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-807c-93a1-d1ea18cb2be8" class="bulleted-list"><li style="list-style-type:disc">= violence risk</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8098-93f9-cbbc54047079" class="bulleted-list"><li style="list-style-type:disc">= childcare cost burden</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80cc-bc0f-fde67659d51f" class="bulleted-list"><li style="list-style-type:disc">= reputation transparency (small town vs anonymous)</li></ul></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8003-a777-e5141c618fd8" class="">Then:</p></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80a7-b30c-c22f4434f38f" class="bulleted-list"><li style="list-style-type:disc">High + high → warrior/pastoral dynamics</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-8023-82a7-cf74fb586f36" class="bulleted-list"><li style="list-style-type:disc">High + high → moral/kin enforcement</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80cf-8d4a-ea1d0e77b7de" class="bulleted-list"><li style="list-style-type:disc">High + high + low → platform/late-modern volatility</li></ul></div><div style="display:contents" dir="auto"><ul id="30dc5e6f-95bd-80a4-88e7-d8653cb31ec6" class="bulleted-list"><li style="list-style-type:disc">High + high (child expensive) → delayed commitment + hyperselectivity</li></ul></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-80bb-9847-cf50c99cd152"/></div><div style="display:contents" dir="auto"><h2 id="30dc5e6f-95bd-8050-bb11-c636ea5df1d0" class="">8) What you asked for: “invariants and clusters” — distilled</h2></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-801f-b380-fa171aad120f" class=""><strong>Invariants (forces):</strong> scarcity, hierarchy, reputation, risk, fertility costs, signal arms races, nervous system fit.</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80d5-9fef-c24c0208ff5e" class=""><strong>Clusters (states):</strong> forager, warrior, agrarian lineage, imperial urban, moral enforcement, industrial bourgeois, late-modern, platform/AI.</p></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-8099-80d8-d2e11aef9988" class=""><strong>Space matters:</strong> frontier vs high-trust city vs rural kin vs trade hub.</p></div><div style="display:contents" dir="auto"><hr id="30dc5e6f-95bd-8046-ac3b-d64eb303d70b"/></div><div style="display:contents" dir="auto"><p id="30dc5e6f-95bd-80ea-b7c3-ddf570bb5d35" class="">If you want the next step, tell me which format you prefer:</p></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80ba-86d2-fff6e559a233" class="numbered-list" start="1"><li><strong>A diagram</strong> (systems map: variables → regimes → outcomes)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80ab-968f-e57e31055a5f" class="numbered-list" start="2"><li><strong>A 12×12 or 19×19 matrix</strong> (your “clusters/invariants grid”)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-8089-b238-dce9165c2541" class="numbered-list" start="3"><li>Apply it to <strong>Western vs East Asian</strong> mating markets <em>qualitatively</em> (no fake numbers)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="30dc5e6f-95bd-80e2-9cd3-fb92f5c851e4" class="numbered-list" start="4"><li>Apply it to <strong>“female genius”</strong> specifically: how to keep polarity without shrinking.</li></ol></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
