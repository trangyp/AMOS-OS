---
tags: [math]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Hydrogen vs. Batteries: The Safety Math Nobody Publishes</title><style>
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
	
</style></head><body><article id="2e4c5e6f-95bd-80b4-ad0f-f5e9196c88c8" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Hydrogen vs. Batteries: The Safety Math Nobody Publishes</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80fa-9bfc-fbf77e223516" class=""><strong>Why Failure Physics — Not Efficiency — Decides Life-Critical Energy Systems</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ae-866f-df273ba3033e" class="">The public debate between hydrogen and batteries is framed incorrectly.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8076-8f41-fee48a3b94c6" class="">It focuses on:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a1-91d2-fb904e944518" class="bulleted-list"><li style="list-style-type:disc">efficiency</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8054-82ca-e067e61ed79e" class="bulleted-list"><li style="list-style-type:disc">cost curves</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8054-9898-d8d67ddf5f49" class="bulleted-list"><li style="list-style-type:disc">energy density</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8031-9c92-e2e6923e2d9c" class="bulleted-list"><li style="list-style-type:disc">climate narratives</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8065-966f-ff2cae65f0f8" class="">These are <strong>secondary variables</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c2-b971-db1bad84f4cc" class="">In life-critical systems — cities, hospitals, transport, offshore, space — the governing variable is <strong>how systems fail</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c2-8fc6-cf8f1e4a8909" class="">The safety math is not about how often failure happens.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-807f-9a9e-e8da7f9f2905" class="">It is about <strong>what happens when failure is inevitable</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8085-8663-f41fe992825a"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80c6-9ee6-c6d7aa7ae341" class=""><strong>I. The Non-Negotiable Premise</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ab-8cf5-f81d5e437675" class="">All energy systems fail.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80bc-bbc0-c369fc900996" class="">The only question that matters is:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-801f-aba9-fb2ea0248627" class="">When failure occurs, do humans survive long enough to respond?</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80eb-97cc-cad9559d4e5a" class="">Most safety discussions stop before answering this.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8032-85b4-de5137877855"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-809e-bac0-de0ee0a4be45" class=""><strong>II. The Five Safety Axes That Actually Matter (MECE)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b1-ac23-cfacf6e535ca" class="">Any energy storage system can be evaluated against five non-overlapping safety dimensions:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8019-8701-f664c1f2bb1b" class="numbered-list" start="1"><li><strong>Failure Visibility</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8074-99e8-d716d69e66c5" class="numbered-list" start="2"><li><strong>Failure Speed</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80cd-83f5-fd047ea56a49" class="numbered-list" start="3"><li><strong>Failure Toxicity</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8039-afa9-e1b0401e83a4" class="numbered-list" start="4"><li><strong>Failure Containment</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80af-be14-c2e23fcac210" class="numbered-list" start="5"><li><strong>Failure Reversibility</strong></li></ol></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a2-82ec-ed93626602c9" class="">Efficiency does not appear on this list.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80fd-983d-d3dfe86a0e8d"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-802f-919f-cfdcd9e49fd5" class=""><strong>III. Axis 1: Failure Visibility</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80db-8f3b-e5b7e7db3944" class=""><strong>Batteries</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-805d-9105-dd713e8d68ac" class="bulleted-list"><li style="list-style-type:disc">Internal chemical reactions are invisible</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-800d-857c-f2b5f005320d" class="bulleted-list"><li style="list-style-type:disc">Thermal runaway begins <em>inside</em> sealed cells</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f1-9568-e5ab3e46987f" class="bulleted-list"><li style="list-style-type:disc">Sensors detect heat <strong>after</strong> critical thresholds</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-807c-9f61-e31b406c753f" class="bulleted-list"><li style="list-style-type:disc">Cell-level failure is opaque until escalation</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800b-91f7-f187bfcad806" class="">Result:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-80b7-b1bf-d889abd8ae90" class="">Failure is discovered late.</blockquote></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8031-bcb1-e0dc0c9a89c2"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80f5-b51d-df1e9b0fd5d8" class=""><strong>Hydrogen</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a0-9ac9-d21c37cb3425" class="bulleted-list"><li style="list-style-type:disc">Leaks are externally detectable</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802a-8d20-c2cb517729de" class="bulleted-list"><li style="list-style-type:disc">Hydrogen sensors are mandatory and sensitive</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d3-9d5f-dc8c319a51df" class="bulleted-list"><li style="list-style-type:disc">Concentration thresholds are explicit</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e3-93b4-f929b3a3ec6b" class="bulleted-list"><li style="list-style-type:disc">System state is continuously observable</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80de-af23-e3b73f319738" class="">Result:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-80b0-8d58-eaa2fe1a366f" class="">Failure is discovered early.</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800b-8af4-dad30ca94cc7" class=""><strong>Safety implication:</strong></p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-802e-987e-ce22c68654ac" class="">Early detection is the single most powerful risk reducer in any system.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8038-9555-dc1135423fd7"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80fb-9bd1-ee2a1fc9efde" class=""><strong>IV. Axis 2: Failure Speed</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-801c-a690-f4c4f41ba3fa" class=""><strong>Batteries</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b1-8126-e1c78f328aee" class="bulleted-list"><li style="list-style-type:disc">Thermal runaway accelerates exponentially</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-801b-89d6-c8757d8776a3" class="bulleted-list"><li style="list-style-type:disc">Escalation occurs faster than human response</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b1-a534-f1e0672508a3" class="bulleted-list"><li style="list-style-type:disc">Adjacent cells ignite via heat transfer</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-805c-a9e2-dbb43023248b" class="bulleted-list"><li style="list-style-type:disc">Fire suppression often triggers secondary reactions</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8013-99b5-ea9f63ab2833" class="">Measured reality:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d0-949a-ff304d80b276" class="bulleted-list"><li style="list-style-type:disc">Runaway propagation measured in seconds to minutes</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8040-904d-fb432cd03fdd" class="bulleted-list"><li style="list-style-type:disc">Human intervention is usually too late</li></ul></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80ab-ae4f-f07137be5178"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-8001-a760-de80d7d80f00" class=""><strong>Hydrogen</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806c-9f93-ca932d5dc469" class="bulleted-list"><li style="list-style-type:disc">Combustion is immediate but brief</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8067-8ca5-ded1f417c8e3" class="bulleted-list"><li style="list-style-type:disc">Energy is released rapidly upward</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8042-a33f-d246e6c7d96e" class="bulleted-list"><li style="list-style-type:disc">No sustained reaction without continuous fuel flow</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80bf-ad1c-ebf53851a53c" class="bulleted-list"><li style="list-style-type:disc">Automatic shutdown halts escalation</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b8-830e-e6977e87014a" class="">Measured reality:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806c-9e11-d4afea712422" class="bulleted-list"><li style="list-style-type:disc">Event duration is short</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a5-b40c-ed2c565f4031" class="bulleted-list"><li style="list-style-type:disc">System stabilizes once flow stops</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8029-b8e5-e6025bdc0307" class=""><strong>Safety implication:</strong></p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80bf-acc9-da19bfc21fd8" class="">Fast, finite failures are safer than slow, compounding ones.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8085-8ba2-c8ad2864dc89"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8080-85ec-f383ac00fc42" class=""><strong>V. Axis 3: Failure Toxicity (This Is the Kill Variable)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-801a-be0e-de7dc0c8fb9b" class=""><strong>Batteries</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b6-93d3-f6baa6a93e36" class="">Failure produces:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802a-a937-ff2156cb4743" class="bulleted-list"><li style="list-style-type:disc">hydrogen fluoride (HF)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8080-a1b4-c31bdafc3a1b" class="bulleted-list"><li style="list-style-type:disc">carbon monoxide</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802f-9a7b-c68f679b3a62" class="bulleted-list"><li style="list-style-type:disc">volatile organic compounds</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8049-9d1a-dd096c456eea" class="bulleted-list"><li style="list-style-type:disc">dense particulate smoke</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d3-8600-e7f9a596a107" class="">Empirical data across fire investigations:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8042-9061-c595a3f76afb" class="bulleted-list"><li style="list-style-type:disc"><strong>Most fatalities occur from smoke inhalation, not heat</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e7-bc41-ff8de7aae88b" class="bulleted-list"><li style="list-style-type:disc">HF exposure causes delayed death and permanent injury</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8008-ab72-fb28e50daf57" class="bulleted-list"><li style="list-style-type:disc">Firefighters require specialized PPE and retreat zones</li></ul></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8049-9c71-c2552d06c920"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-809f-9f7c-c9d6fd63f3ea" class=""><strong>Hydrogen</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-801c-8a28-fbf96329c9c3" class="">Failure produces:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c9-8f04-d6154c30f00d" class="bulleted-list"><li style="list-style-type:disc">water vapor</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-800a-963d-cc8893b900fe" class="bulleted-list"><li style="list-style-type:disc">heat</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8057-a94b-dca85e6f6863" class="bulleted-list"><li style="list-style-type:disc">visible flame</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-805c-aca9-f9a0b2d87486" class="">Critically:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ec-91af-ffc3c2cab93d" class="bulleted-list"><li style="list-style-type:disc"><strong>no smoke</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8044-a8c5-fa14dfdcfb5c" class="bulleted-list"><li style="list-style-type:disc"><strong>no toxic byproducts</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c5-a52c-da5b868cd092" class="bulleted-list"><li style="list-style-type:disc"><strong>no residue</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f7-b883-cac1e8ab13b9" class=""><strong>Safety implication:</strong></p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a0-8ee9-eacdd964f546" class="">Absence of smoke dramatically increases human survival probability.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8055-b11a-e5491218e668"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80cf-a103-cd5125901863" class=""><strong>VI. Axis 4: Failure Containment</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80b4-81aa-c892c9c6df23" class=""><strong>Batteries</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8061-9394-fe9f47d64bc2" class="bulleted-list"><li style="list-style-type:disc">Fire spreads laterally</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c9-8e49-c25a43e74522" class="bulleted-list"><li style="list-style-type:disc">Enclosed spaces trap heat and gases</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-807d-b22f-f6d5d8626d92" class="bulleted-list"><li style="list-style-type:disc">Re-ignition occurs hours or days later</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8027-abfd-e5b8cfb90cca" class="bulleted-list"><li style="list-style-type:disc">Firefighting requires isolation and sacrifice of assets</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803a-99bb-e283595a9355" class="">Observed outcomes:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-809c-925d-c84c357bbbc9" class="bulleted-list"><li style="list-style-type:disc">Entire buildings lost due to contamination</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8080-b6e2-c53b7a3e6080" class="bulleted-list"><li style="list-style-type:disc">Long-term unusability even after extinguishment</li></ul></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8083-b7eb-f8a663af527e"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-8053-b50a-cce96e69a3d2" class=""><strong>Hydrogen</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-808a-a18e-df51e9800adc" class="bulleted-list"><li style="list-style-type:disc">Gas disperses vertically</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802c-971e-d8c8b6d447f5" class="bulleted-list"><li style="list-style-type:disc">Does not pool or accumulate</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ff-b3f7-d552bf2b487b" class="bulleted-list"><li style="list-style-type:disc">Flame path is narrow and directional</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80bf-b7ed-f8eead830b35" class="bulleted-list"><li style="list-style-type:disc">Surrounding systems remain intact</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c6-baba-c55329a31638" class="">Observed outcomes:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f8-8cfe-c1cd0441c93a" class="bulleted-list"><li style="list-style-type:disc">Localized damage</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806c-90b8-d5b6c8f8bff2" class="bulleted-list"><li style="list-style-type:disc">Minimal secondary impact</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e6-939b-c2e54d909db3" class="bulleted-list"><li style="list-style-type:disc">Faster system recovery</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8011-808f-fd6dc6e6ed01" class=""><strong>Safety implication:</strong></p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800d-9ec7-c59cdc12f5d7" class="">Vertical dispersion beats lateral propagation.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8006-90de-f368e3ce821c"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8000-8771-df807a70609d" class=""><strong>VII. Axis 5: Failure Reversibility</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80fb-a816-d0c5b9b3c671" class=""><strong>Batteries</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8085-b09c-d604a0bb9e6e" class="bulleted-list"><li style="list-style-type:disc">Once runaway begins, it cannot be stopped</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e1-9e9a-c22b3b3ec6ee" class="bulleted-list"><li style="list-style-type:disc">Cells are destroyed by design</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b2-892c-e2a9f2901e73" class="bulleted-list"><li style="list-style-type:disc">Surrounding infrastructure is often written off</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-807e-b4c5-e044db97ca47" class="bulleted-list"><li style="list-style-type:disc">Restart timelines measured in weeks or months</li></ul></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80d0-9852-cfbc514b4ce3"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-805c-aa16-feb97aba6e5e" class=""><strong>Hydrogen</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d8-b2f2-fcaac941eb7f" class="bulleted-list"><li style="list-style-type:disc">Flow can be stopped</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c3-80d8-c428f85d3200" class="bulleted-list"><li style="list-style-type:disc">Systems can be purged</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8002-8551-e78912137d00" class="bulleted-list"><li style="list-style-type:disc">Hardware often remains intact</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e1-82e6-f7bbc159bef3" class="bulleted-list"><li style="list-style-type:disc">Restart possible after inspection</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-806c-b54b-d2984fce33f1" class=""><strong>Safety implication:</strong></p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8032-848e-de915db3b277" class="">Reversible failure preserves both lives and infrastructure.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-806a-bd8f-df47840e1c46"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8035-b70c-c7ac64a3c96b" class=""><strong>VIII. The Aggregated Safety Profile (Plain Language)</strong></h2></div><div style="display:contents" dir="ltr"><table id="2e4c5e6f-95bd-8073-af36-d05587b3afb7" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2e4c5e6f-95bd-8096-b09f-da6079bc280e"><th id="O:Ki" class="simple-table-header-color simple-table-header"><strong>Dimension</strong></th><th id="KaMn" class="simple-table-header-color simple-table-header"><strong>Batteries</strong></th><th id="ohzN" class="simple-table-header-color simple-table-header"><strong>Hydrogen</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2e4c5e6f-95bd-8093-b53b-dfba1ce846f3"><td id="O:Ki" class="">Failure visibility</td><td id="KaMn" class="">Low</td><td id="ohzN" class="">High</td></tr></div><div style="display:contents" dir="ltr"><tr id="2e4c5e6f-95bd-80bb-976f-fc0599b87c2b"><td id="O:Ki" class="">Failure speed</td><td id="KaMn" class="">Escalating</td><td id="ohzN" class="">Finite</td></tr></div><div style="display:contents" dir="ltr"><tr id="2e4c5e6f-95bd-80c2-948d-e2fe9f8c0bd1"><td id="O:Ki" class="">Toxicity</td><td id="KaMn" class="">Extreme</td><td id="ohzN" class="">None</td></tr></div><div style="display:contents" dir="ltr"><tr id="2e4c5e6f-95bd-808b-9826-ffab7111c9da"><td id="O:Ki" class="">Containment</td><td id="KaMn" class="">Poor</td><td id="ohzN" class="">Strong</td></tr></div><div style="display:contents" dir="ltr"><tr id="2e4c5e6f-95bd-80e6-8450-f7b4e2d6bf21"><td id="O:Ki" class="">Reversibility</td><td id="KaMn" class="">No</td><td id="ohzN" class="">Yes</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-801b-90db-ff36c4e81929" class="">This is not opinion.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80af-bbf0-d962fc6725a5" class="">It is <strong>failure physics</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-808e-b403-c66008360924"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80db-b2c0-e4701a9872e6" class=""><strong>IX. Why This Math Is Rarely Published</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8010-992b-d8c85eccf500" class="">Because safety math is inconvenient.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8073-b044-edd960c66a90" class="">It reveals that:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c2-91a7-e3942c716c01" class="bulleted-list"><li style="list-style-type:disc">cheap systems externalize risk</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ba-865b-c5e0e981acd8" class="bulleted-list"><li style="list-style-type:disc">efficiency hides tail risk</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8002-bef3-f4dfb08fea74" class="bulleted-list"><li style="list-style-type:disc">“rare events” dominate real harm</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80cd-8c16-d58af9fb1f82" class="bulleted-list"><li style="list-style-type:disc">governance quality matters more than chemistry</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8025-9cc2-f747b67cb983" class="">Battery economics look good <strong>until failure</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-804a-8b85-eb51ab0bea70" class="">Hydrogen economics look expensive <strong>until disaster</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8074-b4f1-cb42ff2cbb12"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80b5-950d-f9ac9b3a6c90" class=""><strong>X. Where Each Technology Belongs (Non-Ideological)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80a7-816d-e715f0b7f769" class=""><strong>Batteries are appropriate when:</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806c-b134-e9acbc6f4cfd" class="bulleted-list"><li style="list-style-type:disc">environments are open</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8039-bdb1-edcf83e10e5d" class="bulleted-list"><li style="list-style-type:disc">evacuation is easy</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c4-9d59-cbcb9952167a" class="bulleted-list"><li style="list-style-type:disc">assets are disposable</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f3-b9a6-e79830d71c01" class="bulleted-list"><li style="list-style-type:disc">human density is low</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-801f-9196-fa8d7c3a22e2" class="bulleted-list"><li style="list-style-type:disc">downtime is acceptable</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-8074-ac94-e607350770f6" class=""><strong>Hydrogen is appropriate when:</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c2-9943-cb58ac15c0be" class="bulleted-list"><li style="list-style-type:disc">humans cannot evacuate</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b4-b715-ca87213d0cee" class="bulleted-list"><li style="list-style-type:disc">smoke is unacceptable</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-804e-ab3d-e610d7e6173e" class="bulleted-list"><li style="list-style-type:disc">systems must be auditable</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80cc-b8b7-d0559c2a32c5" class="bulleted-list"><li style="list-style-type:disc">failure must be survivable</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8031-9546-f04a58e5e732" class="bulleted-list"><li style="list-style-type:disc">governance must be explicit</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8029-ae2f-e5def79cad10" class="">This is why hydrogen appears in:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ce-b0af-cb26268b1449" class="bulleted-list"><li style="list-style-type:disc">aerospace</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ce-9be8-de0bf76b2561" class="bulleted-list"><li style="list-style-type:disc">hospitals</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8061-869a-c285ba781d17" class="bulleted-list"><li style="list-style-type:disc">submarines</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8035-a1f4-fe6c46b5bfef" class="bulleted-list"><li style="list-style-type:disc">offshore platforms</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-800c-918a-fd122ff8c73e" class="bulleted-list"><li style="list-style-type:disc">data centers</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80bf-8437-d5fa058db713" class="bulleted-list"><li style="list-style-type:disc">civil protection systems</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8009-a53e-d9b1ceb38411" class="">Not because it is fashionable.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8020-91e8-e82bf456f614" class="">Because people survive its failures.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8058-80dc-edd73db05462"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8025-9ac4-d13c04df74c4" class=""><strong>XI. The Hidden Variable: Institutional Strength</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8063-8f6c-cdb1b73b7c09" class="">Hydrogen <strong>demands</strong>:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a9-a9af-fff92e4215ed" class="bulleted-list"><li style="list-style-type:disc">sensors</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-804e-adaa-d96f4542e6ce" class="bulleted-list"><li style="list-style-type:disc">maintenance</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ef-9fcd-e9cca577ccbd" class="bulleted-list"><li style="list-style-type:disc">clear authority</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8035-8606-cc9ff894dec3" class="bulleted-list"><li style="list-style-type:disc">transparent reporting</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-809e-bc03-c341af586cf7" class="bulleted-list"><li style="list-style-type:disc">enforced shutdown rules</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803e-857c-c4640bd76c88" class="">Weak institutions hate hydrogen.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80fb-845b-f4631eb7ac66" class="">Strong institutions choose it deliberately.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803d-99af-d104e0bb90c0" class="">This is why hydrogen adoption correlates with:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8071-9957-de6aab7b215a" class="">governance maturity, not energy ideology.</blockquote></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8062-a19a-c1b996c82d37"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-807e-8a12-cbd95b5ae96a" class=""><strong>XII. The Final Accounting</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80be-8681-d3a3a3cbc65c" class="">Batteries optimize for:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-803a-8414-e0fac31a77aa" class="bulleted-list"><li style="list-style-type:disc">convenience</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a2-88b7-ff2d4d39da49" class="bulleted-list"><li style="list-style-type:disc">efficiency</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8046-938e-db28dc271505" class="bulleted-list"><li style="list-style-type:disc">short-term cost</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8071-96ff-cd0b2b8ad959" class="bulleted-list"><li style="list-style-type:disc">minimal governance burden</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8007-8e39-fec446636553" class="">Hydrogen optimizes for:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806b-bc8e-ea0d5658864d" class="bulleted-list"><li style="list-style-type:disc">human survivability</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b2-b2ce-ff25a9c62083" class="bulleted-list"><li style="list-style-type:disc">failure legibility</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8085-afbd-d32c299e96e7" class="bulleted-list"><li style="list-style-type:disc">accountability</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80fa-ad94-ed8801ee5aeb" class="bulleted-list"><li style="list-style-type:disc">long-term resilience</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ab-81ae-cc890df2ff5f" class="">One hides risk.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-801e-93a6-c0de4d32da4a" class="">The other exposes it.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80a1-b63e-f5c0db371d7e"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-807c-9ce4-cf1cb1956914" class=""><strong>Final Conclusion</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803d-9449-ceca97a4ad5b" class="">The safety math is clear:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-804b-8baf-ccdeb4e80fa3" class="">Batteries fail silently and catastrophically.</blockquote></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-80bd-b8a2-f9664cdd2926" class="">Hydrogen fails visibly and survivably.</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a2-8581-dad85d827668" class="">In life-critical systems, there is no ethical justification for choosing opacity over survivability.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8063-b4c2-e99c6ef9888b" class="">Hydrogen is not the future everywhere.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-809c-998e-c6bcddcec8f0" class="">But wherever human life cannot be treated as expendable, hydrogen is not optional — it is inevitable.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8005-8e9a-d9b52e052e5d"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80cd-a843-ed35a980b571" class=""><strong>The line nobody prints</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b5-ae05-cfdf286fa80c" class="">Efficiency saves money.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-804a-b718-e645d5f22958" class="">Safety saves lives.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800f-9626-f42073715810" class="">The math was always there.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80e6-8e5e-d9a4b2670db1" class="">We just didn’t want to publish it.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-807d-a01c-e15a3f9c3f9f"/></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f7-857e-f9418d521dfc" class="">If you want next, we can go deeper into:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802b-b0be-fb5a8e16b595" class="bulleted-list"><li style="list-style-type:disc"><strong>“Battery Fire Statistics the Insurance Industry Uses”</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c9-9d5b-fbb477c1e1ce" class="bulleted-list"><li style="list-style-type:disc"><strong>“Why Urban Hydrogen Requires Ethical Intelligence™ Governance”</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b8-9689-cc7f91f8e61b" class="bulleted-list"><li style="list-style-type:disc"><strong>“When Efficiency Becomes Negligence”</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8077-8de8-cba34abd9e08" class="bulleted-list"><li style="list-style-type:disc"><strong>“Why Some Technologies Are Safe Only in Honest Societies”</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8012-bdc8-f1de84e57901" class="">Just say which one to lock next.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
