---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Why Solar Is More Expensive Than It Is Advertised</title><style>
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
	
</style></head><body><article id="2e4c5e6f-95bd-8059-8f49-e4a1253c037b" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Why Solar Is More Expensive Than It Is Advertised</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80ea-bb22-c87315996da8" class=""><strong>The Economics of Partial Truths, Deferred Costs, and Missing System Boundaries</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80eb-bd9f-c1f8e14ca432" class="">Solar power is marketed as cheap.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80eb-89fb-fbdedb206bb0" class="">In many cases, the numbers are not wrong — but they are incomplete.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-806e-8b1e-c13a26fcfe30" class="">The cost problem with solar is not deception in pricing.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d9-afee-f42602a4a9ed" class="">It is <strong>deception by omission</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b9-bc46-c3e3851dca34" class="">Solar appears inexpensive because <strong>only part of the system is priced</strong>, while the most difficult costs are deferred, externalized, or pushed onto someone else.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80e7-ba70-d3e0d2a0f91c"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80ee-a661-d9faed2a3555" class=""><strong>The First Illusion: Panel Cost Is Not System Cost</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d3-86b6-c0e50eb1c171" class="">Most solar pricing highlights:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e3-aeaa-f4fb0ab736ec" class="bulleted-list"><li style="list-style-type:disc">panel price per watt</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8051-901c-df5f27539e5f" class="bulleted-list"><li style="list-style-type:disc">inverter cost</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80de-b7df-c9127ece886b" class="bulleted-list"><li style="list-style-type:disc">installation labor</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b0-9abc-d11a1fb87e3d" class="bulleted-list"><li style="list-style-type:disc">simple payback period</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c4-8cdf-fef6f931c9e1" class="">This captures only the <strong>generation layer</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80cf-a6ba-c8a30aa753aa" class="">What it excludes:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80df-a730-dd2cf0b96f68" class="bulleted-list"><li style="list-style-type:disc">intermittency management</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80cd-93cc-f2760da673af" class="bulleted-list"><li style="list-style-type:disc">grid integration</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8052-a53f-eb73159979a7" class="bulleted-list"><li style="list-style-type:disc">storage</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b4-a3f9-c21112695e68" class="bulleted-list"><li style="list-style-type:disc">curtailment losses</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-808d-968d-f3e9b5828381" class="bulleted-list"><li style="list-style-type:disc">peak mismatch</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b6-9c1c-d6c13c702975" class="bulleted-list"><li style="list-style-type:disc">degradation over time</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80db-89e0-d447f9a4a455" class="bulleted-list"><li style="list-style-type:disc">operational complexity</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8049-bc5d-f139b63ff6a9" class="">Solar panels are cheap.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f9-af89-fdc39488dc12" class=""><strong>Solar systems are not.</strong></p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80ab-a76f-cb5c49b08ce3"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80db-8cbc-e8f56006656b" class=""><strong>Cheap Generation, Expensive Integration</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d8-bac1-f7292afc30bd" class="">Solar generates electricity when:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8014-9c37-f1e311617f65" class="bulleted-list"><li style="list-style-type:disc">the sun is available</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80fb-b559-fd580cd5ce5d" class="bulleted-list"><li style="list-style-type:disc">regardless of when demand exists</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-804d-9ce9-ea962d1a840f" class="">Electric systems, however, must:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a4-8fb4-ec0146c3cd63" class="bulleted-list"><li style="list-style-type:disc">meet demand instantly</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-808f-9fb9-d33911f6062c" class="bulleted-list"><li style="list-style-type:disc">remain stable</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-805f-be85-e81a1cc50504" class="bulleted-list"><li style="list-style-type:disc">handle peaks</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8084-a998-c136c255ad32" class="bulleted-list"><li style="list-style-type:disc">recover from faults</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8036-b18c-e38957ff369c" class="">This mismatch creates costs that are <strong>not optional</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f0-8bf3-c5ffc6135b0f" class="">Those costs include:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c4-929b-f6c3f786be9f" class="bulleted-list"><li style="list-style-type:disc">grid reinforcement</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8039-827b-ed0d83ad7c64" class="bulleted-list"><li style="list-style-type:disc">voltage regulation</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-808c-b554-e982acc219e7" class="bulleted-list"><li style="list-style-type:disc">frequency control</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802b-b9b8-f82d10d621e7" class="bulleted-list"><li style="list-style-type:disc">spinning reserve</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f0-8348-f8b434cf9f9d" class="bulleted-list"><li style="list-style-type:disc">backup generation</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8002-816d-c972d4306529" class="bulleted-list"><li style="list-style-type:disc">storage or curtailment</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8084-ac3d-d25bbadb04de" class="">These costs exist whether or not they appear on the invoice.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8065-8c02-c92a783b0693"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80d2-9d46-c655f378b856" class=""><strong>The Storage Gap: Where Solar Gets Expensive</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d7-84ae-ee21cf3e37e3" class="">Solar is cheap <strong>only at the moment of generation</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8062-86e1-cb2b4b87b662" class="">The moment you need electricity:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8040-962d-d75c24de39a0" class="bulleted-list"><li style="list-style-type:disc">at night</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80da-8d41-d9b994a65fb0" class="bulleted-list"><li style="list-style-type:disc">during storms</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8035-aa4d-f2dd2d3bb746" class="bulleted-list"><li style="list-style-type:disc">during peak demand</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8091-869d-d8024ec8f858" class="bulleted-list"><li style="list-style-type:disc">during grid stress</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8058-a353-c5a4f134640f" class="">solar alone is insufficient.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8020-83ec-d1caff6cc376" class="">Storage fills the gap — and storage is expensive.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-805f-b406-f12724f91222" class="">What is often advertised:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8023-b6ee-de12ba748431" class="bulleted-list"><li style="list-style-type:disc">solar LCOE (levelized cost of energy)</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80df-952b-cdef3e1d9648" class="">What is rarely advertised:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e2-b0e1-f08158154c60" class="bulleted-list"><li style="list-style-type:disc">solar + storage LCOE</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-809b-ab21-fcad3488e9f4" class="bulleted-list"><li style="list-style-type:disc">cost per <em>usable</em> kWh</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80de-a351-f044c3633504" class="bulleted-list"><li style="list-style-type:disc">cost under worst-case conditions</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80e6-ac6f-cd233f5d729b" class="">Adding storage:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-807c-932a-f8674d5b5530" class="bulleted-list"><li style="list-style-type:disc">doubles or triples capital cost</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8025-b3eb-e74bd85991fa" class="bulleted-list"><li style="list-style-type:disc">introduces degradation</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8049-b2fd-ebb7520f78ce" class="bulleted-list"><li style="list-style-type:disc">adds replacement cycles</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e3-b72f-fde47f847d6a" class="bulleted-list"><li style="list-style-type:disc">increases operational complexity</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-804a-8970-fb12c83e13b9" class="">Solar without storage is incomplete.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8078-bd43-cb11a580ed53" class="">Solar with storage is no longer “cheap.”</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-802c-a69e-d52f0c234c14"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80c9-ae83-d44d3e8d6a15" class=""><strong>The Intermittency Tax</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-805d-bf5b-c6de13c16e4a" class="">Every intermittent energy source imposes an <strong>intermittency tax</strong> on the system.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ac-b32d-c82ffb6dc2bc" class="">This tax is paid through:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e3-83ef-f3dc307f36f4" class="bulleted-list"><li style="list-style-type:disc">backup capacity</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8053-a70d-c3e53cfdb2ce" class="bulleted-list"><li style="list-style-type:disc">grid redundancy</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8099-8d6a-d45171122a15" class="bulleted-list"><li style="list-style-type:disc">operational reserves</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b0-9b14-d993f2511614" class="bulleted-list"><li style="list-style-type:disc">market balancing costs</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f5-af4b-db5ffd3886d0" class="">The tax is real even if:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806b-8681-fb104825521d" class="bulleted-list"><li style="list-style-type:disc">it is not paid by the solar owner</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8089-ac45-e24c2f86d602" class="bulleted-list"><li style="list-style-type:disc">it is absorbed by utilities</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c5-b0da-d63e0e58df2d" class="bulleted-list"><li style="list-style-type:disc">it is socialized across ratepayers</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-809d-a24d-f9df8f8d4792" class="">Solar looks cheap because <strong>someone else is paying the intermittency tax</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-803f-a68b-eb3764c4496c"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80f0-b953-ce2aebb6c699" class=""><strong>Curtailment: Paying for Energy You Can’t Use</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-801f-94b2-e0ce9d855de1" class="">As solar penetration rises, a new cost appears: <strong>curtailment</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c3-9dce-c65d0e2dca5d" class="">Curtailment means:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a6-913d-f7f963278ce6" class="bulleted-list"><li style="list-style-type:disc">solar generates electricity</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80da-912d-de526916aaec" class="bulleted-list"><li style="list-style-type:disc">the grid cannot absorb it</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806c-83c8-f8e8beab28f4" class="bulleted-list"><li style="list-style-type:disc">the energy is discarded</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f9-a77e-fcccebe7f35c" class="">The system still paid for:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-804b-b423-e15a8311dcf3" class="bulleted-list"><li style="list-style-type:disc">the panels</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8020-8233-d5dc6c2faa8b" class="bulleted-list"><li style="list-style-type:disc">the land</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8068-b518-ee472ffb7303" class="bulleted-list"><li style="list-style-type:disc">the grid connection</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-804e-a24d-eebce6777d3c" class="bulleted-list"><li style="list-style-type:disc">the capital</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80da-9382-ffe622e6e20e" class="">But the energy delivers <strong>zero value</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8013-81ab-e2531419ce87" class="">Curtailment increases as:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8014-8c9c-c2721163e968" class="bulleted-list"><li style="list-style-type:disc">solar scales faster than grids</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8035-bf00-dfdf2c76c1e4" class="bulleted-list"><li style="list-style-type:disc">storage lags deployment</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8044-b2e9-ffaaa52b522c" class="bulleted-list"><li style="list-style-type:disc">planning remains fragmented</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d6-9c56-daed99cd02a0" class="">From a system perspective:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8072-bb55-cd8b16b82876" class="">Energy that cannot be delivered is not cheap energy — it is wasted capital.</blockquote></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8039-b132-d3c8966ce7d0"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8099-8ece-ed9bd900e658" class=""><strong>The Degradation Reality</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f1-b18d-ec04087e4c28" class="">Solar panels degrade.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8067-ab0f-c0c0e1bd2c3f" class="">Inverters fail faster.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b9-b7a9-e8f8a6555020" class="">Batteries degrade much faster.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8038-b7df-fa4dd958c867" class="">Advertised costs often assume:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a0-91df-d45ee08fa737" class="bulleted-list"><li style="list-style-type:disc">ideal performance</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8097-b615-c047180ad8de" class="bulleted-list"><li style="list-style-type:disc">minimal downtime</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8032-8481-dfa901af9948" class="bulleted-list"><li style="list-style-type:disc">optimistic degradation curves</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-808e-881b-f36ebd217a4c" class="bulleted-list"><li style="list-style-type:disc">perfect maintenance</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a6-af68-c11633f0d20e" class="">Real systems experience:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8093-9949-c9ee5c91c977" class="bulleted-list"><li style="list-style-type:disc">heat stress</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8072-a77f-df2819fed4ad" class="bulleted-list"><li style="list-style-type:disc">dust</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8028-8266-d816e4858811" class="bulleted-list"><li style="list-style-type:disc">humidity</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8076-960c-fa31f284e56f" class="bulleted-list"><li style="list-style-type:disc">voltage fluctuations</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8080-9d6d-dd3b88c84824" class="bulleted-list"><li style="list-style-type:disc">component mismatch</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8086-a18f-dee242d9cdd3" class="">Over time, the cost per usable kWh rises.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8093-925a-ea8f7b1594ee" class="">The brochure price never reflects year 10 reality.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8000-a6bb-c3a4d95bd468"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80b8-8bc3-e0fdc1b5e8fe" class=""><strong>The Grid Subsidy Nobody Mentions</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8068-b243-e86b35123a11" class="">Grid-connected solar relies on the grid as:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8010-a863-dcfd51338e41" class="bulleted-list"><li style="list-style-type:disc">backup</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8016-96a8-e11f445b1153" class="bulleted-list"><li style="list-style-type:disc">storage proxy</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-800d-8adc-c96ebad39b6a" class="bulleted-list"><li style="list-style-type:disc">balancing mechanism</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8081-81e1-cdce142feccc" class="bulleted-list"><li style="list-style-type:disc">reliability guarantor</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ac-bcb9-c428664a4f01" class="">Yet solar owners typically pay:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8074-b65f-dd1cd0ccdbbf" class="bulleted-list"><li style="list-style-type:disc">retail tariffs</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806d-ad4c-ed015c78693b" class="bulleted-list"><li style="list-style-type:disc">minimal connection fees</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f0-948a-d845566974e7" class="">They do not pay proportionally for:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b1-b569-c17d39ea51b8" class="bulleted-list"><li style="list-style-type:disc">peak capacity</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-804a-8112-d3f2f419aa85" class="bulleted-list"><li style="list-style-type:disc">reserve margins</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-800d-a1e3-d5a26415f64c" class="bulleted-list"><li style="list-style-type:disc">grid reinforcement</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8047-aa2a-e49a00240785" class="bulleted-list"><li style="list-style-type:disc">stability services</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8020-92f2-ee9806aedccb" class="">This creates an implicit subsidy:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8071-b201-f75e26f9059a" class="bulleted-list"><li style="list-style-type:disc">from non-solar users</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b6-91e9-ee41205b30dd" class="bulleted-list"><li style="list-style-type:disc">from future rate increases</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8004-9248-fa6b203bfcc9" class="bulleted-list"><li style="list-style-type:disc">from deferred public investment</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a7-b98d-c50cbef34675" class="">Solar is cheap <strong>because the grid is underpriced</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-806b-9605-c5779f73d0c7"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-800c-951b-c42a6c57027c" class=""><strong>Peak Demand Is the Solar Reckoning</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a3-8c0a-f2d694f74ddf" class="">Solar performs best:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8085-afcd-f2df73b4bf65" class="bulleted-list"><li style="list-style-type:disc">midday</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b6-8448-d79d9985a15f" class="bulleted-list"><li style="list-style-type:disc">low demand periods (in many regions)</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8024-9bae-eb69b7508830" class="">Grids are built for:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8029-a8be-d500a990f306" class="bulleted-list"><li style="list-style-type:disc">evening peaks</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e7-ba54-e384fd789687" class="bulleted-list"><li style="list-style-type:disc">seasonal extremes</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f4-be5a-fa29b4233add" class="bulleted-list"><li style="list-style-type:disc">worst-case conditions</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8096-8bde-fcd1ad0b00f9" class="">Solar reduces average energy cost.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-804a-aac4-ea63f7a696bd" class="">It does <strong>not</strong> reduce peak infrastructure requirements unless paired with storage and demand control.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d7-89ab-f8df5490c19f" class="">Infrastructure is sized for peaks, not averages.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ee-83cb-c783ecccb204" class="">That is why system costs keep rising even as solar prices fall.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-808e-8ab7-c22dd0e3dcfb"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8003-aaef-f7971e2f69f3" class=""><strong>The Vietnam-Specific Dimension</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a4-af3e-ed451892f2fa" class="">In Vietnam:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ec-a536-fdb86337439e" class="bulleted-list"><li style="list-style-type:disc">electricity tariffs are politically constrained</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f1-806d-f39450056b00" class="bulleted-list"><li style="list-style-type:disc">grid upgrades lag demand</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ea-8ed1-df9a324463ec" class="bulleted-list"><li style="list-style-type:disc">rooftop solar expanded faster than planning capacity</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d9-be93-f87f09dd642c" class="bulleted-list"><li style="list-style-type:disc">curtailment has already appeared in utility-scale solar</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800d-bc3c-cd1ceb90ee86" class="">This makes the cost illusion more fragile.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b0-b501-fb13bafdb464" class="">When solar penetration rises without:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ea-9223-f9db3ef1712f" class="bulleted-list"><li style="list-style-type:disc">dispatch authority</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a1-bce1-e20ecba21244" class="bulleted-list"><li style="list-style-type:disc">storage coordination</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8020-b110-e1e46cfcde52" class="bulleted-list"><li style="list-style-type:disc">pricing reform</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8017-8d0d-dfb1f9841e0a" class="">the result is:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80aa-8931-f46069eac893" class="bulleted-list"><li style="list-style-type:disc">grid stress</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ea-bb62-f77dc6a53fc2" class="bulleted-list"><li style="list-style-type:disc">hidden costs</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8035-93ac-dd9cd5843d1f" class="bulleted-list"><li style="list-style-type:disc">delayed correction</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802f-b24c-d8bd96d5ba0c" class="bulleted-list"><li style="list-style-type:disc">sudden policy reversals</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80df-8498-d2cc68359bfc" class="">Solar does not become expensive gradually.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ac-8c01-e6533d5846e3" class="">It becomes expensive <strong>when the system can no longer hide the cost</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80fe-88a1-f4116cea5b4d"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80ab-b131-e51430093ead" class=""><strong>The Core Truth</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-809a-82a0-ce33a90e7dec" class="">Solar is not expensive because:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8027-8b89-cd8550b9d20c" class="bulleted-list"><li style="list-style-type:disc">panels are overpriced</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8050-aa20-d9a3a12f0184" class="bulleted-list"><li style="list-style-type:disc">technology failed</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8029-8125-dca11432f830" class="bulleted-list"><li style="list-style-type:disc">renewables don’t work</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8070-89bf-f51e1036490f" class="">Solar is expensive because:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8025-b178-f73db559afdf" class="">energy systems are not priced at the system boundary.</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b4-b0c4-f4e539166b30" class="">Solar is cheap at the component level.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8007-9e58-c49b0d40b681" class="">It is costly at the system level.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8083-a294-e1bfa4a5c9fe"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-802e-97f2-cfeb3377105b" class=""><strong>What Honest Solar Economics Requires</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8083-bb33-f25a25eae169" class="">Solar becomes genuinely affordable only when:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8042-bd35-f29398bb7e57" class="bulleted-list"><li style="list-style-type:disc">storage is priced explicitly</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8077-a69d-c9a78250e935" class="bulleted-list"><li style="list-style-type:disc">curtailment is acknowledged</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8012-bdf5-f8d1b4a2fa7a" class="bulleted-list"><li style="list-style-type:disc">peak responsibility is assigned</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8030-8274-c9e6bbeeec20" class="bulleted-list"><li style="list-style-type:disc">grid costs are transparently allocated</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c2-a4fa-e421ccec25f8" class="bulleted-list"><li style="list-style-type:disc">dispatch is governed, not assumed</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8090-b383-c44658ba3005" class="">Until then:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80bb-a277-e52baa9cac55" class="bulleted-list"><li style="list-style-type:disc">advertised prices will remain incomplete</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-807d-a734-f6b58ced7184" class="bulleted-list"><li style="list-style-type:disc">savings will depend on who absorbs risk</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f6-b4bf-eff74b05f8d9" class="bulleted-list"><li style="list-style-type:disc">correction will be political, not technical</li></ul></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8010-ae1c-d07d84bc449a"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80b2-9a50-dbd4be65810c" class=""><strong>The Final Line</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8011-b6ee-c7d1cf42faca" class="">Solar is not as cheap as advertised — not because the numbers are wrong, but because <strong>the hardest costs are missing from the calculation</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803f-91fb-ff6e49e1ee2c" class="">Cheap solar without system accounting is not affordability.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-802d-bebb-f8dcbea612b3" class="">It is <strong>underpriced complexity waiting to surface</strong>.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
