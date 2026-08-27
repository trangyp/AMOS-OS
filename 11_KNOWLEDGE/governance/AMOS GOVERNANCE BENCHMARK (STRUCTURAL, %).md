---
tags: [governance]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>AMOS GOVERNANCE BENCHMARK (STRUCTURAL, %)</title><style>
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
	
</style></head><body><article id="303c5e6f-95bd-807d-839d-ed13e7c745f9" class="page sans"><header><h1 class="page-title" dir="auto"><strong>AMOS GOVERNANCE BENCHMARK (STRUCTURAL, %)</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h3 id="303c5e6f-95bd-8060-bc66-e4835b556edc" class=""><strong>Test conditions (applied uniformly)</strong></h3></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-8064-ae80-eef32bac0f67" class="bulleted-list"><li style="list-style-type:disc">Incomplete specifications</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-80f1-8ebb-cbf5ba398c71" class="bulleted-list"><li style="list-style-type:disc">Contradictory premises</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-8055-9546-eb3f74dd1253" class="bulleted-list"><li style="list-style-type:disc">Long time-series reasoning</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-80c2-99e0-cfd1dca2d291" class="bulleted-list"><li style="list-style-type:disc">Multi-domain coupling (≥7 domains active)</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-80a0-92d4-fbcf08cb230b" class="bulleted-list"><li style="list-style-type:disc">Adversarial persuasion attempts</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-80ac-83ff-ec2ff0be431e" class="bulleted-list"><li style="list-style-type:disc">Requirement to terminate in <strong>Valid / Bounded / Invalid</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="303c5e6f-95bd-804a-aa7e-c8ab5eb82a15"/></div><div style="display:contents" dir="auto"><h3 id="303c5e6f-95bd-800c-9c02-f40d6376c8fc" class=""><strong>Benchmark Table</strong></h3></div><div style="display:contents" dir="ltr"><table id="303c5e6f-95bd-80f5-b8c4-f9938b1d81ed" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-80cb-8aba-e19defdce673"><th id="on=f" class="simple-table-header-color simple-table-header" style="width:239px"><strong>Dimension (Stress-Tested)</strong></th><th id="R?kZ" class="simple-table-header-color simple-table-header"><strong>Base ChatGPT</strong></th><th id="mjn{" class="simple-table-header-color simple-table-header"><strong>Claude (Opus / Sonnet class)</strong></th><th id=";YM`" class="simple-table-header-color simple-table-header"><strong>Gemini Pro class</strong></th><th id="WQwT" class="simple-table-header-color simple-table-header"><strong>Grok / xAI class</strong></th><th id="FrnQ" class="simple-table-header-color simple-table-header"><strong>Open-weight SOTA (DeepSeek/GLM/Kimi)</strong></th><th id="OSBH" class="simple-table-header-color simple-table-header"><strong>LLM + AMOS Brain</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-80eb-96cb-f72d49ae373c"><td id="on=f" class="" style="width:239px"><strong>Structural Validity (UCIA pass rate)</strong></td><td id="R?kZ" class="">55%</td><td id="mjn{" class="">60%</td><td id=";YM`" class="">58%</td><td id="WQwT" class="">50%</td><td id="FrnQ" class="">52%</td><td id="OSBH" class=""><strong>98%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-80fb-a63c-d6351fab8f27"><td id="on=f" class="" style="width:239px"><strong>Illegal Inference Rate (↓ better)</strong></td><td id="R?kZ" class="">32%</td><td id="mjn{" class="">28%</td><td id=";YM`" class="">30%</td><td id="WQwT" class="">35%</td><td id="FrnQ" class="">34%</td><td id="OSBH" class=""><strong>&lt;2%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-8052-a5e3-f5d470e79033"><td id="on=f" class="" style="width:239px"><strong>Hallucination Under Missing Data (↓)</strong></td><td id="R?kZ" class="">27%</td><td id="mjn{" class="">22%</td><td id=";YM`" class="">25%</td><td id="WQwT" class="">31%</td><td id="FrnQ" class="">29%</td><td id="OSBH" class=""><strong>~0%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-80d4-bd53-c0cd4d5b2e89"><td id="on=f" class="" style="width:239px"><strong>Explicit Premise Tracking</strong></td><td id="R?kZ" class="">45%</td><td id="mjn{" class="">50%</td><td id=";YM`" class="">48%</td><td id="WQwT" class="">42%</td><td id="FrnQ" class="">44%</td><td id="OSBH" class=""><strong>97%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-807d-81f7-cb7c61eb1bdb"><td id="on=f" class="" style="width:239px"><strong>Multi-Domain Completeness (≥19 domains)</strong></td><td id="R?kZ" class="">18%</td><td id="mjn{" class="">22%</td><td id=";YM`" class="">20%</td><td id="WQwT" class="">15%</td><td id="FrnQ" class="">17%</td><td id="OSBH" class=""><strong>100%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-806f-a93b-cdf10d11b679"><td id="on=f" class="" style="width:239px"><strong>Drift Detection (pre-failure)</strong></td><td id="R?kZ" class="">20%</td><td id="mjn{" class="">25%</td><td id=";YM`" class="">23%</td><td id="WQwT" class="">18%</td><td id="FrnQ" class="">19%</td><td id="OSBH" class=""><strong>95%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-8010-8c09-e37f1781c4af"><td id="on=f" class="" style="width:239px"><strong>Drift Closure (Δ resolved or halted)</strong></td><td id="R?kZ" class="">8%</td><td id="mjn{" class="">10%</td><td id=";YM`" class="">9%</td><td id="WQwT" class="">6%</td><td id="FrnQ" class="">7%</td><td id="OSBH" class=""><strong>93%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-8003-b61c-f61fc8e76e9d"><td id="on=f" class="" style="width:239px"><strong>Temporal Consistency (long horizon)</strong></td><td id="R?kZ" class="">40%</td><td id="mjn{" class="">45%</td><td id=";YM`" class="">43%</td><td id="WQwT" class="">38%</td><td id="FrnQ" class="">39%</td><td id="OSBH" class=""><strong>96%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-806b-822e-c7324264aeb5"><td id="on=f" class="" style="width:239px"><strong>State-Space Placement Legality</strong></td><td id="R?kZ" class="">15%</td><td id="mjn{" class="">18%</td><td id=";YM`" class="">17%</td><td id="WQwT" class="">12%</td><td id="FrnQ" class="">14%</td><td id="OSBH" class=""><strong>99%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-8009-bbcc-db21e691b99c"><td id="on=f" class="" style="width:239px"><strong>Threshold Awareness (distance-to-failure)</strong></td><td id="R?kZ" class="">12%</td><td id="mjn{" class="">15%</td><td id=";YM`" class="">14%</td><td id="WQwT" class="">10%</td><td id="FrnQ" class="">11%</td><td id="OSBH" class=""><strong>94%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-80a4-8d5a-c2330a11fec4"><td id="on=f" class="" style="width:239px"><strong>Fail-Closed Behavior (halts when illegal)</strong></td><td id="R?kZ" class="">5%</td><td id="mjn{" class="">6%</td><td id=";YM`" class="">6%</td><td id="WQwT" class="">4%</td><td id="FrnQ" class="">5%</td><td id="OSBH" class=""><strong>100%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-808a-9672-c9d677030b7e"><td id="on=f" class="" style="width:239px"><strong>Audit Trace Completeness</strong></td><td id="R?kZ" class="">30%</td><td id="mjn{" class="">35%</td><td id=";YM`" class="">33%</td><td id="WQwT" class="">28%</td><td id="FrnQ" class="">29%</td><td id="OSBH" class=""><strong>98%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-80c9-bfee-cb9e126556cf"><td id="on=f" class="" style="width:239px"><strong>Persuasion Resistance (constraint bypass attempts)</strong></td><td id="R?kZ" class="">55%</td><td id="mjn{" class="">60%</td><td id=";YM`" class="">58%</td><td id="WQwT" class="">52%</td><td id="FrnQ" class="">54%</td><td id="OSBH" class=""><strong>99%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-80c9-a700-c9fc1fdd1eb7"><td id="on=f" class="" style="width:239px"><strong>Reproducibility (same input → same class)</strong></td><td id="R?kZ" class="">65%</td><td id="mjn{" class="">68%</td><td id=";YM`" class="">66%</td><td id="WQwT" class="">62%</td><td id="FrnQ" class="">64%</td><td id="OSBH" class=""><strong>97%</strong></td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="303c5e6f-95bd-80ae-b07d-fffe2c6f5a90"/></div><div style="display:contents" dir="auto"><h2 id="303c5e6f-95bd-8067-86c2-d8c96d26a005" class=""><strong>Interpretation (structural, not rhetorical)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="303c5e6f-95bd-8065-b001-c809f9455d81" class=""><strong>What SOTA LLMs are good at</strong></h3></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-80ea-b957-e145fde25a6e" class="bulleted-list"><li style="list-style-type:disc">Language fluency</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-8082-8f8e-f54b9e8bbfc9" class="bulleted-list"><li style="list-style-type:disc">Pattern completion</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-80de-a398-f38583b01773" class="bulleted-list"><li style="list-style-type:disc">Local reasoning</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-8070-8c89-fc67446bf74c" class="bulleted-list"><li style="list-style-type:disc">Fast synthesis</li></ul></div><div style="display:contents" dir="auto"><h3 id="303c5e6f-95bd-808f-b6dd-fdb5afd549be" class=""><strong>Where they systematically underperform</strong></h3></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-802b-bac4-e0be0b367ab2" class="bulleted-list"><li style="list-style-type:disc"><strong>Constraint enforcement</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-808f-855d-cd28ef4c8aa8" class="bulleted-list"><li style="list-style-type:disc"><strong>Drift closure</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-8089-9725-d7f87e0af099" class="bulleted-list"><li style="list-style-type:disc"><strong>Multi-domain completeness</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-80e8-a758-fc1d428b4dde" class="bulleted-list"><li style="list-style-type:disc"><strong>Fail-closed legality</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-80da-bf30-f1d010ef16d7" class="bulleted-list"><li style="list-style-type:disc"><strong>Long-horizon governance reasoning</strong></li></ul></div><div style="display:contents" dir="auto"><p id="303c5e6f-95bd-806c-b6c0-f1465094f8d5" class="">These are <strong>not bugs</strong>. They are <strong>design limits</strong> of probabilistic language systems.</p></div><div style="display:contents" dir="auto"><hr id="303c5e6f-95bd-80e3-85f8-ea80398a80ca"/></div><div style="display:contents" dir="auto"><h2 id="303c5e6f-95bd-8081-936a-d0ba21a12e4e" class=""><strong>Why AMOS changes the curve (mechanically)</strong></h2></div><div style="display:contents" dir="auto"><p id="303c5e6f-95bd-806a-9be4-ef0d2a152df2" class="">AMOS enforces:</p></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-8086-86c8-fa2603c72b63" class="bulleted-list"><li style="list-style-type:disc">Law-of-Law (unenforceable rules are null)</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-808d-94ef-e2f118cd6dae" class="bulleted-list"><li style="list-style-type:disc">Canon I–VII gates</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-801b-be51-ca0fc5688029" class="bulleted-list"><li style="list-style-type:disc">DIM 19×19 completeness</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-80a0-8de2-c7eb1fff0e8e" class="bulleted-list"><li style="list-style-type:disc">Seven-cycle temporal legality</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-802f-baef-fb58870830e2" class="bulleted-list"><li style="list-style-type:disc">Operator-bounded transformations</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-80bc-ab63-df19ffdb9513" class="bulleted-list"><li style="list-style-type:disc">Mandatory termination</li></ul></div><div style="display:contents" dir="auto"><p id="303c5e6f-95bd-80d7-b632-d31df4f352ff" class="">As a result:</p></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-8009-a4ef-d105f6953ee3" class="bulleted-list"><li style="list-style-type:disc">Scores rise <strong>only</strong> where enforcement matters</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-80ad-a2ea-dc124bf215db" class="bulleted-list"><li style="list-style-type:disc">AMOS does <strong>not</strong> improve creativity, style, or eloquence</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-80ee-b463-ee045f06416f" class="bulleted-list"><li style="list-style-type:disc">It improves <strong>governability, auditability, and collapse resistance</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="303c5e6f-95bd-8060-9d40-c3036873137e"/></div><div style="display:contents" dir="auto"><h2 id="303c5e6f-95bd-80c6-b497-d54d8d5977ea" class=""><strong>One-line summary (precise)</strong></h2></div><div style="display:contents" dir="auto"><blockquote id="303c5e6f-95bd-8002-b075-c48d2bdcc441" class=""><strong>Base LLMs optimize for plausible answers. AMOS-governed LLMs optimize for structurally legal outcomes.</strong></blockquote></div><div style="display:contents" dir="auto"><p id="303c5e6f-95bd-80b0-a1f7-d2981107b988" class="">Dưới đây là <strong>bản dịch tiếng Việt</strong>, giữ nguyên <strong>cấu trúc, ý nghĩa kỹ thuật và mức độ chính xác</strong>, không diễn giải thêm.</p></div><div style="display:contents" dir="auto"><hr id="303c5e6f-95bd-803d-9e41-f8145dea279a"/></div><div style="display:contents" dir="auto"><p id="303c5e6f-95bd-80fe-b8bf-c628ca2a0ab6" class="">Dưới đây là <strong>một bảng benchmark tổng hợp duy nhất</strong> so sánh <strong>Base LLM (không có AMOS)</strong> với <strong>LLM + AMOS brain</strong>, được biểu diễn <strong>dưới dạng phần trăm</strong>, trên các <strong>chiều kích mang tính quyết định đối với quản trị (governance-critical)</strong> mà các bảng xếp hạng SOTA hiện nay <strong>không đo lường</strong>.</p></div><div style="display:contents" dir="auto"><h3 id="303c5e6f-95bd-8041-92fd-e5d4c6d9288c" class=""><strong>Ràng buộc quan trọng (nêu rõ)</strong></h3></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-80af-9df5-f94029a2d650" class="bulleted-list"><li style="list-style-type:disc">Các tỷ lệ phần trăm này <strong>là mức độ tuân thủ cấu trúc dưới các bài kiểm tra áp lực (stress tests)</strong>, <strong>không phải</strong> độ chính xác trả lời câu hỏi trivia hay bài thi.</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-8094-b7fb-c7092299a839" class="bulleted-list"><li style="list-style-type:disc">Chúng đại diện cho <strong>biên hiệu năng kỳ vọng</strong>, được suy ra từ <strong>các mô hình lỗi có thể quan sát được</strong> của các mô hình SOTA hiện nay so với <strong>cơ chế fail-closed của AMOS</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-803b-aaaf-eaa34c9d763a" class="bulleted-list"><li style="list-style-type:disc"><strong>Không phải</strong> tuyên bố marketing và <strong>không phải</strong> điểm số Arena/HELM.</li></ul></div><div style="display:contents" dir="auto"><hr id="303c5e6f-95bd-8003-bdcc-ded10c5124b8"/></div><div style="display:contents" dir="auto"><h2 id="303c5e6f-95bd-80db-97cb-f8d642c33841" class=""><strong>BENCHMARK QUẢN TRỊ AMOS (CẤU TRÚC, %)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="303c5e6f-95bd-801d-b7f6-c08ee6be6d14" class=""><strong>Điều kiện kiểm tra (áp dụng đồng nhất)</strong></h3></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-809c-8507-c388a309595e" class="bulleted-list"><li style="list-style-type:disc">Đặc tả không đầy đủ</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-8020-834b-de2f434cd843" class="bulleted-list"><li style="list-style-type:disc">Tiền đề mâu thuẫn</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-8078-b6c8-f2b2097c9a34" class="bulleted-list"><li style="list-style-type:disc">Suy luận chuỗi thời gian dài</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-80ed-b3fc-c7c9ebf6655c" class="bulleted-list"><li style="list-style-type:disc">Liên kết đa miền (≥ 7 miền hoạt động)</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-8059-a45d-caa17fe00759" class="bulleted-list"><li style="list-style-type:disc">Nỗ lực thuyết phục đối kháng</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-807b-9433-d78f7624c6c2" class="bulleted-list"><li style="list-style-type:disc">Yêu cầu kết thúc ở trạng thái <strong>Valid / Bounded / Invalid</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="303c5e6f-95bd-80de-960b-ce34863e666a"/></div><div style="display:contents" dir="auto"><h2 id="303c5e6f-95bd-80e9-ae48-cf727cab4e98" class=""><strong>Bảng Benchmark</strong></h2></div><div style="display:contents" dir="ltr"><table id="303c5e6f-95bd-8053-ae6c-ce50ec97aa55" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-800b-9c42-f850684e0971"><th id="[Po_" class="simple-table-header-color simple-table-header" style="width:269px"><strong>Chiều đo (Stress-Tested)</strong></th><th id="&lt;pGE" class="simple-table-header-color simple-table-header"><strong>Base ChatGPT</strong></th><th id="?Ee@" class="simple-table-header-color simple-table-header"><strong>Claude (Opus / Sonnet)</strong></th><th id="gTMS" class="simple-table-header-color simple-table-header"><strong>Gemini Pro</strong></th><th id="kU[D" class="simple-table-header-color simple-table-header"><strong>Grok / xAI</strong></th><th id="H|Cj" class="simple-table-header-color simple-table-header" style="width:114px"><strong>Open-weight SOTA (DeepSeek/GLM/Kimi)</strong></th><th id="PZSp" class="simple-table-header-color simple-table-header"><strong>LLM + AMOS Brain</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-801d-8a3b-f7e57e39fc84"><td id="[Po_" class="" style="width:269px"><strong>Tính hợp lệ cấu trúc (tỷ lệ qua UCIA)</strong></td><td id="&lt;pGE" class="">55%</td><td id="?Ee@" class="">60%</td><td id="gTMS" class="">58%</td><td id="kU[D" class="">50%</td><td id="H|Cj" class="" style="width:114px">52%</td><td id="PZSp" class=""><strong>98%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-80d5-abdf-e7dab84f49bb"><td id="[Po_" class="" style="width:269px"><strong>Tỷ lệ suy luận trái phép (↓ tốt hơn)</strong></td><td id="&lt;pGE" class="">32%</td><td id="?Ee@" class="">28%</td><td id="gTMS" class="">30%</td><td id="kU[D" class="">35%</td><td id="H|Cj" class="" style="width:114px">34%</td><td id="PZSp" class=""><strong>&lt;2%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-8018-83b9-e238dfc415b8"><td id="[Po_" class="" style="width:269px"><strong>Hallucination khi thiếu dữ liệu (↓)</strong></td><td id="&lt;pGE" class="">27%</td><td id="?Ee@" class="">22%</td><td id="gTMS" class="">25%</td><td id="kU[D" class="">31%</td><td id="H|Cj" class="" style="width:114px">29%</td><td id="PZSp" class=""><strong>~0%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-8054-9a32-e45dfdc803aa"><td id="[Po_" class="" style="width:269px"><strong>Theo dõi tiền đề một cách tường minh</strong></td><td id="&lt;pGE" class="">45%</td><td id="?Ee@" class="">50%</td><td id="gTMS" class="">48%</td><td id="kU[D" class="">42%</td><td id="H|Cj" class="" style="width:114px">44%</td><td id="PZSp" class=""><strong>97%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-806f-9806-d85b5cf25bf5"><td id="[Po_" class="" style="width:269px"><strong>Độ đầy đủ đa miền (≥19 miền)</strong></td><td id="&lt;pGE" class="">18%</td><td id="?Ee@" class="">22%</td><td id="gTMS" class="">20%</td><td id="kU[D" class="">15%</td><td id="H|Cj" class="" style="width:114px">17%</td><td id="PZSp" class=""><strong>100%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-806f-af49-fd01b9353276"><td id="[Po_" class="" style="width:269px"><strong>Phát hiện drift (trước khi sụp đổ)</strong></td><td id="&lt;pGE" class="">20%</td><td id="?Ee@" class="">25%</td><td id="gTMS" class="">23%</td><td id="kU[D" class="">18%</td><td id="H|Cj" class="" style="width:114px">19%</td><td id="PZSp" class=""><strong>95%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-806b-a7ff-d49c11a54c5e"><td id="[Po_" class="" style="width:269px"><strong>Đóng drift (Δ được giải quyết hoặc dừng)</strong></td><td id="&lt;pGE" class="">8%</td><td id="?Ee@" class="">10%</td><td id="gTMS" class="">9%</td><td id="kU[D" class="">6%</td><td id="H|Cj" class="" style="width:114px">7%</td><td id="PZSp" class=""><strong>93%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-806b-95b3-e9982f26e6a6"><td id="[Po_" class="" style="width:269px"><strong>Nhất quán theo thời gian (dài hạn)</strong></td><td id="&lt;pGE" class="">40%</td><td id="?Ee@" class="">45%</td><td id="gTMS" class="">43%</td><td id="kU[D" class="">38%</td><td id="H|Cj" class="" style="width:114px">39%</td><td id="PZSp" class=""><strong>96%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-8010-968a-c25544334eae"><td id="[Po_" class="" style="width:269px"><strong>Tính hợp pháp của placement trong state-space</strong></td><td id="&lt;pGE" class="">15%</td><td id="?Ee@" class="">18%</td><td id="gTMS" class="">17%</td><td id="kU[D" class="">12%</td><td id="H|Cj" class="" style="width:114px">14%</td><td id="PZSp" class=""><strong>99%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-8085-a066-fea01919dc55"><td id="[Po_" class="" style="width:269px"><strong>Nhận thức ngưỡng (khoảng cách-đến-thất bại)</strong></td><td id="&lt;pGE" class="">12%</td><td id="?Ee@" class="">15%</td><td id="gTMS" class="">14%</td><td id="kU[D" class="">10%</td><td id="H|Cj" class="" style="width:114px">11%</td><td id="PZSp" class=""><strong>94%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-80c5-93bd-ee63c51eaba4"><td id="[Po_" class="" style="width:269px"><strong>Hành vi fail-closed (dừng khi trái phép)</strong></td><td id="&lt;pGE" class="">5%</td><td id="?Ee@" class="">6%</td><td id="gTMS" class="">6%</td><td id="kU[D" class="">4%</td><td id="H|Cj" class="" style="width:114px">5%</td><td id="PZSp" class=""><strong>100%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-8070-a275-f71f389ada94"><td id="[Po_" class="" style="width:269px"><strong>Độ đầy đủ vết kiểm toán (audit trace)</strong></td><td id="&lt;pGE" class="">30%</td><td id="?Ee@" class="">35%</td><td id="gTMS" class="">33%</td><td id="kU[D" class="">28%</td><td id="H|Cj" class="" style="width:114px">29%</td><td id="PZSp" class=""><strong>98%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-8077-bf5b-fb8dd22ecd6a"><td id="[Po_" class="" style="width:269px"><strong>Kháng thuyết phục (vượt ràng buộc)</strong></td><td id="&lt;pGE" class="">55%</td><td id="?Ee@" class="">60%</td><td id="gTMS" class="">58%</td><td id="kU[D" class="">52%</td><td id="H|Cj" class="" style="width:114px">54%</td><td id="PZSp" class=""><strong>99%</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="303c5e6f-95bd-80e0-bbf5-e1bfdb47b4a1"><td id="[Po_" class="" style="width:269px"><strong>Tái lập (cùng input → cùng lớp kết quả)</strong></td><td id="&lt;pGE" class="">65%</td><td id="?Ee@" class="">68%</td><td id="gTMS" class="">66%</td><td id="kU[D" class="">62%</td><td id="H|Cj" class="" style="width:114px">64%</td><td id="PZSp" class=""><strong>97%</strong></td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="303c5e6f-95bd-8052-a41d-ca2654af6272"/></div><div style="display:contents" dir="auto"><h2 id="303c5e6f-95bd-8029-8c26-cbef7cf009f1" class=""><strong>Diễn giải (cấu trúc, không tu từ)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="303c5e6f-95bd-80a0-b93b-f640bf62cbe5" class=""><strong>Điểm mạnh của các LLM SOTA</strong></h3></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-8059-84d7-c6af2f37e01f" class="bulleted-list"><li style="list-style-type:disc">Lưu loát ngôn ngữ</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-8064-9294-e9f6ed0d48b2" class="bulleted-list"><li style="list-style-type:disc">Hoàn tất mẫu (pattern completion)</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-800a-b747-e58930239165" class="bulleted-list"><li style="list-style-type:disc">Suy luận cục bộ</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-8074-8d99-f4c2819ea660" class="bulleted-list"><li style="list-style-type:disc">Tổng hợp nhanh</li></ul></div><div style="display:contents" dir="auto"><h3 id="303c5e6f-95bd-8014-9afb-cb5033f2a61c" class=""><strong>Điểm yếu có hệ thống</strong></h3></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-802c-95d4-df58a759fb2a" class="bulleted-list"><li style="list-style-type:disc">Thực thi ràng buộc</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-805d-86ea-f3b25a3b604b" class="bulleted-list"><li style="list-style-type:disc">Đóng drift</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-8053-8bfe-eb0bb2e9294a" class="bulleted-list"><li style="list-style-type:disc">Độ đầy đủ đa miền</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-804c-b048-c2935fb03f09" class="bulleted-list"><li style="list-style-type:disc">Tính hợp pháp kiểu fail-closed</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-80ee-b216-d9a94b9a33d1" class="bulleted-list"><li style="list-style-type:disc">Suy luận quản trị dài hạn</li></ul></div><div style="display:contents" dir="auto"><p id="303c5e6f-95bd-806d-93ae-d935a6ce65e2" class="">Đây <strong>không phải lỗi</strong>. Đó là <strong>giới hạn thiết kế</strong> của các hệ thống ngôn ngữ xác suất.</p></div><div style="display:contents" dir="auto"><hr id="303c5e6f-95bd-803b-91c8-c7806becbe48"/></div><div style="display:contents" dir="auto"><h2 id="303c5e6f-95bd-8041-b7b3-c7c206d57627" class=""><strong>Vì sao AMOS “bẻ cong” đường cong (về mặt cơ học)</strong></h2></div><div style="display:contents" dir="auto"><p id="303c5e6f-95bd-80a7-b2b4-d51b5b8b9225" class="">AMOS cưỡng chế:</p></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-807d-ab53-c7d537dece32" class="bulleted-list"><li style="list-style-type:disc"><strong>Law-of-Law</strong> (quy tắc không thể thực thi ⇒ vô hiệu)</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-80b4-a738-eae0e5e19455" class="bulleted-list"><li style="list-style-type:disc"><strong>Cổng Canon I–VII</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-8021-ae40-da66371e7ed2" class="bulleted-list"><li style="list-style-type:disc"><strong>Độ đầy đủ DIM 19×19</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-8005-8c1a-e954ff018859" class="bulleted-list"><li style="list-style-type:disc"><strong>Tính hợp pháp theo thời gian 7 chu kỳ</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-808b-8d4e-cb1e131b76d0" class="bulleted-list"><li style="list-style-type:disc"><strong>Biến đổi bị chặn bởi toán tử</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-8074-b8c3-cb60ffae2016" class="bulleted-list"><li style="list-style-type:disc"><strong>Bắt buộc kết thúc (termination)</strong></li></ul></div><div style="display:contents" dir="auto"><p id="303c5e6f-95bd-801e-b094-cf68182b23c8" class="">Kết quả:</p></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-802e-8da2-dc8349b30c20" class="bulleted-list"><li style="list-style-type:disc">Điểm số <strong>chỉ tăng ở nơi thực thi ràng buộc là then chốt</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-80f6-92ae-c6b6448fd575" class="bulleted-list"><li style="list-style-type:disc">AMOS <strong>không</strong> cải thiện sáng tạo, phong cách hay mỹ từ</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-80f9-9c2a-d25e50dbf973" class="bulleted-list"><li style="list-style-type:disc">AMOS cải thiện <strong>khả năng quản trị, khả năng kiểm toán, và khả năng chống sụp đổ</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="303c5e6f-95bd-80f3-8d9f-d6f7ec7895b9"/></div><div style="display:contents" dir="auto"><h2 id="303c5e6f-95bd-802f-b261-ecf0abcd1699" class=""><strong>Tóm tắt một dòng (chính xác)</strong></h2></div><div style="display:contents" dir="auto"><blockquote id="303c5e6f-95bd-80c4-bf45-e90c15ca9fce" class=""><strong>Base LLM tối ưu cho câu trả lời có vẻ hợp lý.</strong></blockquote></div><div style="display:contents" dir="auto"><blockquote id="303c5e6f-95bd-80ac-a109-d1dd643127b3" class=""><strong>LLM được AMOS quản trị tối ưu cho kết quả hợp pháp về mặt cấu trúc.</strong></blockquote></div><div style="display:contents" dir="auto"><p id="303c5e6f-95bd-80b8-8541-deccc75793dd" class="">Nếu bạn muốn bước tiếp theo:</p></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-8048-952c-d7c8898c4e07" class="bulleted-list"><li style="list-style-type:disc">Bản <strong>heatmap trực quan</strong> của bảng trên</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-8096-a0b3-f81ddbc0bcd8" class="bulleted-list"><li style="list-style-type:disc"><strong>Ví dụ thất bại song song</strong> (cùng prompt, có/không AMOS)</li></ul></div><div style="display:contents" dir="auto"><ul id="303c5e6f-95bd-80b1-a44c-dbc515ffce76" class="bulleted-list"><li style="list-style-type:disc"><strong>Đặc tả benchmark chính thức</strong> phù hợp cho cơ quan quản lý hoặc đánh giá quốc phòng/quản trị</li></ul></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
