---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Primary Realistic Buyers</title><style>
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
	
</style></head><body><article id="24ac5e6f-95bd-80e0-a994-cd296ed55071" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Primary Realistic Buyers</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80fe-8e84-e80f2828a79b"/></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-80d4-8e95-ecf9a76fdaa9" class=""><em>(Can execute 50–500 t tranches directly)</em></p></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-80af-b49f-e5bcdd8a480c" class=""><strong>A. Central Banks / Monetary Authorities</strong></h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80c0-83c5-f89b07a7a1dc" class="bulleted-list"><li style="list-style-type:disc"><strong>Why</strong>: Reserve diversification, de-dollarization hedge, liquidity buffer.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-808f-a9c7-e73ef7de7350" class="bulleted-list"><li style="list-style-type:disc"><strong>Examples</strong>: Active buyers in recent years include Poland, Turkey, India, China.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80a3-b0c1-ee72a180184e" class="bulleted-list"><li style="list-style-type:disc"><strong>Requirements</strong>:<div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8084-a144-ea8a7008be85" class="bulleted-list"><li style="list-style-type:circle">Bank-to-bank Proof of Product (POP) from UBS.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80bd-8c52-c3a4305a87b3" class="bulleted-list"><li style="list-style-type:circle">Full serialized bar list with refiner, fineness, and weights.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8082-acbd-eacac6299fd5" class="bulleted-list"><li style="list-style-type:circle">Sanctions and AML compliance.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8068-b2e3-f4c3390bbd17" class="bulleted-list"><li style="list-style-type:circle">Optional assay pre-first tranche.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80d3-b6d0-ea392d72a33e" class="bulleted-list"><li style="list-style-type:circle">Sovereign-approved SPA under Swiss or English law.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8060-b3e0-dfb3384efff8" class="bulleted-list"><li style="list-style-type:disc"><strong>Contact Path</strong>: Approach via reserve management desks or through sovereign diplomatic channels.</li></ul></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-80d3-8410-d7f731235acb" class=""><strong>B. LBMA Clearing / Market-Making Bullion Banks</strong></h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80c8-a1dd-fcb178b48509" class="bulleted-list"><li style="list-style-type:disc"><strong>Why</strong>: They hold LPMCL clearing capability and principal market-making books.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80ae-a508-fafb1dca8911" class="bulleted-list"><li style="list-style-type:disc"><strong>Examples</strong>: HSBC, ICBC Standard Bank, J.P. Morgan, UBS.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8019-b9af-dcd23b06ecc7" class="bulleted-list"><li style="list-style-type:disc"><strong>Requirements</strong>:<div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-804f-9c09-d9e0049955d6" class="bulleted-list"><li style="list-style-type:circle">POP and bar list.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80da-8594-d2b03d92be15" class="bulleted-list"><li style="list-style-type:circle">Loco London or Loco Zurich deliverability.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8031-ad81-e19740e1c610" class="bulleted-list"><li style="list-style-type:circle">MT103 or instrumented settlement rails.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8056-9b32-ccf78dbadf64" class="bulleted-list"><li style="list-style-type:circle">Tranche blocks (25–50 t).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8003-8401-eac49dcc57cf" class="bulleted-list"><li style="list-style-type:disc"><strong>Contact Path</strong>: Direct bank-to-bank communication with bullion desk officers.</li></ul></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-80d9-a88f-d621f0779979" class=""><strong>C. Sovereign Wealth Funds (SWFs)</strong></h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80f3-b43c-c37b06c3fde5" class="bulleted-list"><li style="list-style-type:disc"><strong>Why</strong>: Strategic macro hedge; physical reserve diversification.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8035-b14e-e4554ae26ba1" class="bulleted-list"><li style="list-style-type:disc"><strong>Examples</strong>: ADIA (UAE), PIF (Saudi), QIA (Qatar), GIC/Temasek (Singapore), KIA (Kuwait), NBIM (Norway).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8039-9dfa-d7cfb9331ba7" class="bulleted-list"><li style="list-style-type:disc"><strong>Requirements</strong>:<div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-803f-9a75-c6202e97cb68" class="bulleted-list"><li style="list-style-type:circle">Escrow and optional assay.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8068-b491-cd6be94813fb" class="bulleted-list"><li style="list-style-type:circle">May prefer structured notes or gold-backed facilities over outright purchase.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-806f-939d-c554500ad364" class="bulleted-list"><li style="list-style-type:disc"><strong>Contact Path</strong>: Relationship banking teams or sovereign investment liaisons.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-802e-9ef4-e1c1444b3a3f"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-803a-9176-c8f8bc056b34" class=""><strong>2. Secondary / Indirect Buyers</strong></h2></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8039-a91b-e1030fb8aefe" class=""><em>(Require intermediated execution routes)</em></p></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-800f-9ae7-f4ae1d4759da" class=""><strong>D. Gold ETFs via Authorized Participants (APs)</strong></h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-802f-9252-c85afcd27445" class="bulleted-list"><li style="list-style-type:disc"><strong>Why</strong>: Large ETFs like SPDR GLD hold allocated bars; APs can absorb physical through basket creation.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-804f-9cbd-e3ddb388f8c3" class="bulleted-list"><li style="list-style-type:disc"><strong>Requirements</strong>:<div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8053-9fae-fa15166d1122" class="bulleted-list"><li style="list-style-type:circle">POP, bar list, Good Delivery standards.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80fc-9372-e6adf353447c" class="bulleted-list"><li style="list-style-type:circle">Loco London delivery.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-80ec-83a7-d4b2d8bd38c1" class=""><strong>E. State Mints / Strategic Reserves Entities</strong></h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8003-9150-d09baf475884" class="bulleted-list"><li style="list-style-type:disc"><strong>Why</strong>: Coin/bar programs or contingency reserves.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8058-acf2-c76714651f07" class="bulleted-list"><li style="list-style-type:disc"><strong>Requirements</strong>:<div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80c0-a4d0-cadfaa03f246" class="bulleted-list"><li style="list-style-type:circle">Usually bank-intermediated.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8079-b27b-c859fb419cbc" class="bulleted-list"><li style="list-style-type:circle">POP and optional assay.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-80bf-a44f-ccb0de6a5da7" class=""><strong>F. Multilateral or Sovereign Program Vehicles</strong></h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-808e-856f-ec7c6fe60e35" class="bulleted-list"><li style="list-style-type:disc"><strong>Why</strong>: Collateral for FX stability, development programs.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8064-9a22-f74f3f7fdfa1" class="bulleted-list"><li style="list-style-type:disc"><strong>Requirements</strong>:<div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80e7-a523-ee518e0d0705" class="bulleted-list"><li style="list-style-type:circle">Full AML and beneficial ownership transparency.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-803d-bfe6-c286703ae8cf" class="bulleted-list"><li style="list-style-type:circle">Escrow linked to policy or trade programs.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80c3-a78f-ea8a240de02e"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8064-8fa9-e47e59711bc7" class=""><strong>3. Not Suitable at This Scale</strong></h2></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-80bb-8e8a-c8500780ccda" class=""><em>(For completeness)</em></p></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80e7-afa3-f67c8bbe83bb" class="bulleted-list"><li style="list-style-type:disc">Large jewelry houses and fabricators.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-808f-bfb3-f1389c4b5c75" class="bulleted-list"><li style="list-style-type:disc">Commodity trading houses.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8089-9f51-eff09448e5e6" class="bulleted-list"><li style="list-style-type:disc">Refineries (unless acting as agent for larger principal).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-804c-8ae6-fc2937f42c5b" class="bulleted-list"><li style="list-style-type:disc">Family offices/HNW investors.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80d3-a0ec-e28427b63435"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-805c-b7b1-d8c9c43093e4" class=""><strong>Audit Checklist for All Principals</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-800c-9da0-f166dcb37232" class="bulleted-list"><li style="list-style-type:disc">UBS SKR reference and POP.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-804d-8aa7-de394b2cb78f" class="bulleted-list"><li style="list-style-type:disc">Serialized bar list (refiner, fineness, weights).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80d5-8a08-cb45427476ab" class="bulleted-list"><li style="list-style-type:disc">Sanctions/AML/KYC compliance.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80b9-ab2d-ea1b4fe33c04" class="bulleted-list"><li style="list-style-type:disc">SPA under Swiss or English law.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-803d-8ac1-f729455ee20c" class="bulleted-list"><li style="list-style-type:disc">Tranche schedule (25–50 t).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80f0-98a9-f49d567f8808" class="bulleted-list"><li style="list-style-type:disc">In-vault title transfer.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80c6-b4e3-cc0b35036255" class="bulleted-list"><li style="list-style-type:disc">Settlement via MT103, MT799/760 + escrow.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80df-8409-fc79a37c4ece" class="bulleted-list"><li style="list-style-type:disc">Optional SGS or Bureau Veritas assay.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80bf-879f-f8880294db26"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-80f7-9f3f-f56edd195eb9" class=""><strong>Priority Outreach Order</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-80f0-821e-dd975a229c22" class="numbered-list" start="1"><li><strong>LBMA Clearing Banks</strong> – HSBC, ICBC Standard Bank, J.P. Morgan, UBS.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-806b-a790-da47002e79e6" class="numbered-list" start="2"><li><strong>Active Central Banks</strong> – Poland, Turkey, India, China.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-8092-b70a-f26b10950cc8" class="numbered-list" start="3"><li><strong>Top SWFs</strong> – ADIA, PIF, QIA, GIC, Temasek, KIA, NBIM.</li></ol></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-804f-a476-e0fb5d4052c8"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8051-82a0-cca027d0959c" class=""><strong>Red-Flag Exclusions</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80b0-bedc-e5687f3e4611" class="bulleted-list"><li style="list-style-type:disc">Broker chains without proof of authority.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80b0-8aec-f8d04ed64e64" class="bulleted-list"><li style="list-style-type:disc">Parties resisting NDA/KYC.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80b0-a5f2-d5c834af9794" class="bulleted-list"><li style="list-style-type:disc">Non-standard off-ledger settlement proposals.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80a9-b605-c8b45550bce3" class="bulleted-list"><li style="list-style-type:disc">Sanctions-exposed jurisdictions.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-8045-839f-c9f1d6aa05ce"/></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-80e2-af37-c3ebb15ad9c8" class=""><strong>Gold Transaction Outreach Map</strong></p></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-8040-b1fb-e23c4f5a10f8"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8014-8885-e1b38440bc4b" class=""><strong>1. Visual Outreach Map</strong></h2></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="24ac5e6f-95bd-8037-b237-e8ce5009761c" class="code code-wrap"><code class="language-Mermaid" style="white-space:pre-wrap;word-break:break-all">flowchart TD
    A[UBS SKR Gold Custody] --&gt; B[LBMA Clearing Banks]
    A --&gt; C[Central Banks]
    A --&gt; D[Sovereign Wealth Funds]
    B --&gt; B1[HSBC]
    B --&gt; B2[ICBC Standard Bank]
    B --&gt; B3[J.P. Morgan]
    B --&gt; B4[UBS Internal Desk]
    C --&gt; C1[Poland]
    C --&gt; C2[Turkey]
    C --&gt; C3[India]
    C --&gt; C4[China]
    D --&gt; D1[ADIA - UAE]
    D --&gt; D2[PIF - Saudi Arabia]
    D --&gt; D3[QIA - Qatar]
    D --&gt; D4[GIC - Singapore]
    D --&gt; D5[Temasek - Singapore]
    D --&gt; D6[KIA - Kuwait]
    D --&gt; D7[NBIM - Norway]
    style A fill:#f2f2f2,stroke:#333,stroke-width:2px
    style B fill:#f9f9c0,stroke:#333
    style C fill:#c0f9d1,stroke:#333
    style D fill:#c0d9f9,stroke:#333
</code></pre></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-803c-8c9f-f7b3e851d15d"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-800c-a36d-de165b2a2c3f" class=""><strong>2. Contacting Playbook</strong></h2></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-80b6-a2b8-c49742a4c127" class=""><strong>Step 1 – Pre-Outreach Preparation</strong></h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80db-afcc-f3d0c9a8b93d" class="bulleted-list"><li style="list-style-type:disc"><strong>NDA/NCNDA</strong> ready for execution.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80b3-88b9-d4982b19a267" class="bulleted-list"><li style="list-style-type:disc">UBS-issued <strong>Proof of Product (POP)</strong> and <strong>full serialized bar list</strong> (refiner, fineness, weight).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-806f-ba01-d24e04063ff2" class="bulleted-list"><li style="list-style-type:disc">Bank officer–level <strong>KYC/AML package</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8098-9693-d34a19fc9312" class="bulleted-list"><li style="list-style-type:disc">Defined tranche schedule (25–50 t).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8090-a210-f3d3be0f47c5" class="bulleted-list"><li style="list-style-type:disc">Executable <strong>SPA draft</strong> under Swiss or English law.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80d8-adfb-dc602da03732"/></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-80c1-987a-fbfe8e00d332" class=""><strong>Step 2 – Priority Outreach Order</strong></h3></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-80ff-b2ce-f10514d45578" class=""><strong>1. LBMA Clearing Banks</strong> <em>(Fastest execution, principal-to-principal)</em></p></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80a7-9dec-c0cb22edca20" class="bulleted-list"><li style="list-style-type:disc">Target bullion desk heads.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8014-ad2a-f2cbabeb4fc0" class="bulleted-list"><li style="list-style-type:disc">Use POP + tranche offer sheet.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8088-bd54-d846689a2104" class="bulleted-list"><li style="list-style-type:disc">Settlement: MT103 or MT799/760 + escrow.</li></ul></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8040-838b-cb2c217e8277" class=""><strong>2. Active Central Banks</strong> <em>(Strategic reserve expansion)</em></p></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-802d-8fb6-c2d170229f54" class="bulleted-list"><li style="list-style-type:disc">Engage reserve management department.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80d2-a7b5-e1d826e31342" class="bulleted-list"><li style="list-style-type:disc">Emphasize sovereign-grade custody at UBS.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80e5-a3fc-cc54870f6a74" class="bulleted-list"><li style="list-style-type:disc">Highlight liquidity and delivery readiness.</li></ul></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-80f3-9490-dd76c5ac74df" class=""><strong>3. Top Sovereign Wealth Funds</strong> <em>(Long-term macro hedge buyers)</em></p></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-807d-a08e-d6a055972515" class="bulleted-list"><li style="list-style-type:disc">Engage through relationship managers or sovereign investment teams.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-803a-8caa-eae5df932685" class="bulleted-list"><li style="list-style-type:disc">Offer optional structured acquisition over rolling tranches.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-809e-a71e-fc1546cad53c"/></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-8052-a08f-c3df6aedecdf" class=""><strong>Step 3 – Approach Scripts</strong></h3></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-806e-9b02-c0819b82ce53" class=""><strong>A. Initial Contact</strong></p></div><div style="display:contents" dir="auto"><blockquote id="24ac5e6f-95bd-804a-a089-e82805dad25c" class="">&quot;We represent the direct principal holder of 500 metric tonnes of UBS SKR-custodied gold, fully compliant with LBMA Good Delivery standards. The allocation is ready for rolling tranche execution (25–50 t) with full POP, serialized bar list, and SPA under Swiss law. We are inviting select principal buyers for immediate engagement at bank-to-bank level.&quot;</blockquote></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-80cd-bea3-dc2a48db7f99" class=""><strong>B. Confirmation &amp; Next Steps</strong></p></div><div style="display:contents" dir="auto"><blockquote id="24ac5e6f-95bd-80bc-bbfb-fd53f6065ba0" class="">&quot;Upon NDA execution, we will deliver the POP and bar list directly from UBS custody. Our process follows bank-to-bank confirmation, SPA finalization, and secure in-vault title transfer prior to settlement.&quot;</blockquote></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80b7-bac3-d0d99d65e708"/></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-80aa-998a-ecc43a48f7d8" class=""><strong>Step 4 – Execution Sequence</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-80e5-b3a9-d101d5ad4199" class="numbered-list" start="1"><li>NDA / NCNDA executed.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-805e-8657-c28522b41f7b" class="numbered-list" start="2"><li>Bank-to-bank POP &amp; bar list delivery.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-8062-b6df-fb7eea95c43a" class="numbered-list" start="3"><li>SPA finalization &amp; IMFPA (if applicable).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-8035-9f18-f8424d03c16b" class="numbered-list" start="4"><li>Escrow funding or MT799.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-80e4-8ecc-d54f7db89991" class="numbered-list" start="5"><li>In-vault title transfer.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-8008-a0b4-ec31560d08da" class="numbered-list" start="6"><li>MT103 settlement &amp; release.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-809b-8c6c-cf84cefb495f" class="numbered-list" start="7"><li>Rolling tranche continuation until completion.</li></ol></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-8024-b2c8-c0ddc8a05205"/></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-80d2-93da-fc1917f389e7" class="">
</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
