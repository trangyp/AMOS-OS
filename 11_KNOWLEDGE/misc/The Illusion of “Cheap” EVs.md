---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>The Illusion of “Cheap” EVs</title><style>
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
	
</style></head><body><article id="2e4c5e6f-95bd-8044-9373-ce5aee1fb86e" class="page sans"><header><h1 class="page-title" dir="auto"><strong>The Illusion of “Cheap” EVs</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80aa-9b90-d24b87f3d59f" class=""><strong>Why Low Prices Persist Only While Costs Are Hidden</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f5-917b-efbb7f88cec4" class="">EVs are widely perceived as “cheap” to operate.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8033-af2e-c5fbfff26cae" class="">This perception is not false — but it is incomplete.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ed-af12-f6e7fb3d0f1a" class="">EVs are cheap <strong>only because their most expensive costs are not paid by the user at the moment of consumption</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-806e-ace8-cd42ac1d79ec" class="">They are deferred, diluted, or socialized.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8008-bdb2-da131650b39d" class="">This creates an illusion of affordability that holds <strong>until peak load arrives</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8082-8ae7-c283cf4175ab"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-8082-b634-d76ab0a797b0" class=""><strong>Cheap Energy ≠ Cheap Infrastructure</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8034-8b45-e8cd2f9f7b75" class="">Electricity can be cheap per kWh.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a0-b317-f15b64b22c0c" class="">Infrastructure is never cheap.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8060-9bf1-fd5e9a54af52" class="">What EV pricing typically reflects:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-807b-a11d-d33e995ebc1a" class="bulleted-list"><li style="list-style-type:disc">marginal energy cost</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8050-b8c6-d2788676bb4b" class="bulleted-list"><li style="list-style-type:disc">fuel displacement savings</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802b-aa09-d097c4c7cf39" class="bulleted-list"><li style="list-style-type:disc">efficiency gains</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8073-b2e8-c5e9d33e6476" class="">What it omits:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f0-a930-e31b55983c2b" class="bulleted-list"><li style="list-style-type:disc">distribution upgrades</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8076-84b8-e3bfdd9540d2" class="bulleted-list"><li style="list-style-type:disc">transformer reinforcement</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f7-9243-f55d2d039a19" class="bulleted-list"><li style="list-style-type:disc">substation expansion</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a0-9d8c-e592cfeb6b1a" class="bulleted-list"><li style="list-style-type:disc">protection equipment</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806d-8b7d-d733ad9576bf" class="bulleted-list"><li style="list-style-type:disc">peak reserve capacity</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-804e-b3c3-f627ec270f75" class="bulleted-list"><li style="list-style-type:disc">accelerated asset degradation</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8010-bfca-dbc5afd490fe" class="">These costs do not disappear.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ff-a37e-ce64b9c99282" class="">They are simply <strong>pushed elsewhere</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8039-bf3a-f9f05177cdba"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-802e-ae8f-f4483d8967a3" class=""><strong>How the Illusion Is Manufactured</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d2-9858-c37bc4203d21" class="">The illusion of cheap EVs is sustained through four mechanisms:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80f1-9aae-d79951c3d6f4" class="numbered-list" start="1"><li><strong>Deferred Cost Recognition</strong><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-806e-a200-fbc6321853b5" class="">Grid upgrades lag demand by years. EVs feel cheap now because the bill arrives later.</p></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80ed-b3ac-de835438c774" class="numbered-list" start="2"><li><strong>Cost Socialization</strong><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ae-b746-ea9108e119e7" class="">Infrastructure costs are spread across all ratepayers, including non-EV households.</p></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-808f-9f36-e2043df8a4e2" class="numbered-list" start="3"><li><strong>Peak Blindness</strong><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ad-835c-f10896d2e337" class="">Pricing reflects average consumption, while infrastructure is built for peaks.</p></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8007-9f1a-d8a49392a877" class="numbered-list" start="4"><li><strong>Political Suppression</strong><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-808a-9685-c14868c7560d" class="">True peak pricing is avoided to protect adoption narratives.</p></div></li></ol></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-809c-8f94-ea4c9e3f000e" class="">As long as these mechanisms hold, EVs appear inexpensive.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b3-9125-c11eebd1fc2d" class="">When they fail, tariffs spike or reliability collapses.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-800c-943d-f55666da5aad"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-805c-bd74-d6c06ff521d8" class=""><strong>Peak Load Is Where “Cheap” Breaks</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8059-a08a-cd17c3d344f3" class="">EV charging is cheap when:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8074-9a58-e6144db54045" class="bulleted-list"><li style="list-style-type:disc">load is off-peak</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-804a-b549-e0741541d944" class="bulleted-list"><li style="list-style-type:disc">infrastructure has spare capacity</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8023-84e4-fe412fc17ceb" class="bulleted-list"><li style="list-style-type:disc">utilization is smooth</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8033-8f10-fe58eb35df5d" class="">EV charging becomes expensive when:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f0-a132-eeaf742849cc" class="bulleted-list"><li style="list-style-type:disc">demand is synchronized</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8032-b17c-c8703ad05c2a" class="bulleted-list"><li style="list-style-type:disc">infrastructure is saturated</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-800e-9085-fc6f3d6eabd3" class="bulleted-list"><li style="list-style-type:disc">upgrades become unavoidable</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8033-ab30-d99785412b7f" class="">Peak load is the <strong>moment of truth</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8056-987c-f13c6b40bc87" class="">Every EV transition eventually collides with this moment.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8023-9dfc-fd2c97ba0ccb"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80ab-8a91-f396d4c2f31a" class=""><strong>Who Actually Pays for “Cheap” EVs</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f7-a76f-df6f9ba44c64" class="">When EV prices remain low despite rising peak load, costs are absorbed by:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8068-9d0f-e2d71acb6d2c" class="bulleted-list"><li style="list-style-type:disc">utilities (balance sheet erosion)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8032-8cd2-c7c28766020e" class="bulleted-list"><li style="list-style-type:disc">non-EV users (cross-subsidy)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f9-9783-f4641a70ceb4" class="bulleted-list"><li style="list-style-type:disc">governments (delayed public investment)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8086-821b-e39aead4c101" class="bulleted-list"><li style="list-style-type:disc">future consumers (tariff shock later)</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-802a-97c4-ff44180e3369" class="">This is not market efficiency.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f5-9989-daa94a0af7ee" class="">It is <strong>temporal cost shifting</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80b2-acbd-f636ed9a8871"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-8074-b8e5-f9fd432c215b" class=""><strong>Why Fast Charging Makes the Illusion Collapse Faster</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-801c-a024-ea95364b88d2" class="">Fast charging compresses energy consumption into:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d0-af30-f06d70c3bc84" class="bulleted-list"><li style="list-style-type:disc">shorter time windows</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8014-803f-f427867aaca5" class="bulleted-list"><li style="list-style-type:disc">higher power levels</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ad-8b03-dcbb568a55e0" class="bulleted-list"><li style="list-style-type:disc">tighter locations</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-804f-8e28-c52cd48a34d7" class="">This accelerates:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a8-858f-e1fa4153af17" class="bulleted-list"><li style="list-style-type:disc">transformer saturation</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8045-848f-d9ba40e211ce" class="bulleted-list"><li style="list-style-type:disc">feeder overload</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a2-8e0f-f73d74e44211" class="bulleted-list"><li style="list-style-type:disc">voltage instability</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d9-93ed-e9393f1f9239" class="">Fast charging does not just increase cost.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-807a-8bb2-c855feaca93c" class="">It <strong>reveals cost earlier</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f6-aec1-d06e64fa8f86" class="">That is why unplanned fast-charging networks are financially explosive.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80bc-aaaa-f8da9dd4d409"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-8089-a62a-e8c58da016a7" class=""><strong>The Vietnam-Specific Risk</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80fe-80b1-f195a767f524" class="">Vietnam’s electricity tariffs are politically sensitive.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8088-9814-d43a05079fef" class="">This makes the illusion of cheap EVs <strong>harder to unwind safely</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8048-bcf4-dc629acfec00" class="">When grid stress appears, policymakers face a choice:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ef-b08b-c0649378ffdb" class="bulleted-list"><li style="list-style-type:disc">raise tariffs (political backlash)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d7-ad82-c3bcd61abd44" class="bulleted-list"><li style="list-style-type:disc">ration power (reliability loss)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8047-94a0-e6258de2926a" class="bulleted-list"><li style="list-style-type:disc">delay upgrades (system decay)</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ce-a9c4-f8f5c4aba888" class="">None are painless.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-802f-9c3f-e61b9135d3ca" class="">The earlier peak costs are acknowledged, the cheaper the transition remains.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8040-ac7a-e965d835ff4e"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80e9-bf73-c07dc517c152" class=""><strong>Cheap Without Governance Is Not Cheap</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8005-8263-c039bfd9c173" class="">An EV system is only genuinely cheap if:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8061-950d-f4d8f8bb11cf" class="bulleted-list"><li style="list-style-type:disc">peak load is controlled</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8013-b696-cfac06321a65" class="bulleted-list"><li style="list-style-type:disc">siting is rational</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a5-b823-ebef0a75b674" class="bulleted-list"><li style="list-style-type:disc">charging is time-responsive</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-804a-a99d-ce2bcf5f25b7" class="bulleted-list"><li style="list-style-type:disc">responsibility is explicit</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8005-8064-ffbe376511e5" class="">Otherwise:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c7-b87c-f3771e4156d7" class="bulleted-list"><li style="list-style-type:disc">prices are artificially low</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-801a-9a5a-d0ebfc3d55cf" class="bulleted-list"><li style="list-style-type:disc">risk accumulates invisibly</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8078-ab66-c5d348bc5086" class="bulleted-list"><li style="list-style-type:disc">correction becomes sudden and political</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f0-999b-fbd75ec8a4ef" class="">Cheap energy without peak governance is not affordability.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8050-b727-d1f988341d9e" class="">It is <strong>underpriced liability</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8040-839e-ee1605f416fa"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80bc-88d4-dfb63b30efd0" class=""><strong>The Final Reality Check</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b5-ba20-ddf75e935c06" class="">EVs are not cheap because electricity is cheap.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-807c-b41f-d1dae1de2622" class="">They are cheap because <strong>someone else is paying for the hardest part of the system</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-807f-bc83-dcee5467b4ab" class="">The moment peak load is no longer hidden, “cheap” EVs stop being cheap — not gradually, but abruptly.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-802d-a639-cda32730d941" class="">Sustainable electrification does not depend on lower prices.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8099-9133-f4e0e98cca72" class="">It depends on <strong>honest pricing of peak responsibility</strong>.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
