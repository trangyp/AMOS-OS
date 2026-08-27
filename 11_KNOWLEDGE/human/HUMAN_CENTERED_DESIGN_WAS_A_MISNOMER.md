---
tags: [human]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Human-Centered Design Was a Misnomer</title><style>
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
	
</style></head><body><article id="2e5c5e6f-95bd-807e-9532-e7bacbd22162" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Human-Centered Design Was a Misnomer</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8065-9602-c79a82a25aca" class=""><strong>It Did Not Center Humans. It Centered Extraction.</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c4-a36a-da5d7ba8dc1d" class="">Human-Centered Design did not fail.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-802b-9619-c21811d75928" class="">It succeeded exactly as designed.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8016-b3ca-c55ca89c95cb" class="">What failed was the story told about it.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80bf-a3a6-cc0cfece057c" class="">From its earliest institutional adoption, Human-Centered Design was never about protecting humans. It was about <strong>making humans legible, predictable, and economically actionable</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-809a-ad19-fbdaa8b4af4a" class="">Empathy was not the goal.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a6-97b7-dde5d49080a4" class="">Empathy was the <em>tool</em>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8065-bb22-f04a709a2ad4"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-800b-bfe6-f98f3d211068" class=""><strong>1. The Original Sin: Measurement Without Obligation</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-806a-bbf6-dfc462a143ad" class="">The moment human experience became measurable, it became tradable.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f2-aa91-f909256a87b7" class="">Pain points.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-801c-a6a7-d4bfba961697" class="">Friction.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8018-87eb-c4c43f43e155" class="">Delight.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-808d-a925-f473c81605ec" class="">Confusion.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8030-b102-ffd5d855d5d9" class="">Drop-off.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8024-b585-fc0e85197f9b" class="">Retention.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8011-9893-c33295fab499" class="">These were not neutral descriptors. They were <strong>coordinates on a map of exploitation</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8019-8fda-e4bb1a7c5e57" class="">Human-Centered Design created a one-way asymmetry:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-801b-960b-c6d59e208160" class="bulleted-list"><li style="list-style-type:disc">systems gained visibility into human psychology</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8008-8708-e895393fcd26" class="bulleted-list"><li style="list-style-type:disc">humans gained no visibility into system intent</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8040-90d2-cc4f35e24bfb" class="">This asymmetry is the root of modern harm.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80a5-909c-ef4d78e0dae1"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-809c-b2c7-d082f7e1235f" class=""><strong>2. Empathy Was Operationalized — Then Weaponized</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-805b-b1fb-c43362cbced1" class="">Empathy, in practice, became:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-807d-8c12-c7242c2deb40" class="bulleted-list"><li style="list-style-type:disc">vulnerability discovery</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e6-ae10-ec3c780cbb69" class="bulleted-list"><li style="list-style-type:disc">fear profiling</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8096-944d-e05ca0aed271" class="bulleted-list"><li style="list-style-type:disc">uncertainty mapping</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8059-9a1e-d721bdbf5b04" class="bulleted-list"><li style="list-style-type:disc">habit loop identification</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80da-86cb-d35113c77359" class="bulleted-list"><li style="list-style-type:disc">stress-response exploitation</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8091-92b4-e6d9e1350307" class="">Design teams were trained to ask:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8032-b140-f2ac5a4379e1" class="">“Where does it hurt?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800a-b658-ca825769b2ea" class="">Not to heal —</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a2-900a-c64c54f0ac14" class="">but to <strong>insert leverage</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f9-a6b9-f0e818d8c6bf" class="">Once discovered, vulnerabilities were not shielded.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8070-8fec-c37e5dfe8c3c" class="">They were optimized against.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80ec-8fea-d416fd020545"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8085-99d4-e81fbea562b1" class=""><strong>3. Psychology Did Not Enter Design to Heal — It Entered to Convert</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8083-9e2d-ccd03b7e1106" class="">Psychology’s role was reframed.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f1-a2f6-c5888841db6a" class="">Not:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8067-92fb-f05166f94707" class="bulleted-list"><li style="list-style-type:disc">protect mental health</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8064-8347-c353f3f064ea" class="bulleted-list"><li style="list-style-type:disc">reduce harm</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8025-bb7f-da994892eb35" class="bulleted-list"><li style="list-style-type:disc">preserve dignity</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80eb-a2aa-fdc66b2730c5" class="">But:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ac-bcab-cfbc7caf6447" class="bulleted-list"><li style="list-style-type:disc">increase engagement</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8023-9864-fbb3e7ecd64e" class="bulleted-list"><li style="list-style-type:disc">lower resistance</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8006-af92-e0b2523b334a" class="bulleted-list"><li style="list-style-type:disc">shape behavior</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806e-bb20-f53e1e0bac0f" class="bulleted-list"><li style="list-style-type:disc">accelerate decisions</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b2-81cc-eaeccd5bdfd7" class="bulleted-list"><li style="list-style-type:disc">reduce churn</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8037-b801-e6c47409c3c4" class="">The metric replaced the patient.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8090-b132-d8c78e7cd7da" class="">At that moment, psychology stopped being a healing discipline and became <strong>an extraction science</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-800c-a02c-d5c8378ca8c9"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8051-8099-fa2ed139b6b8" class=""><strong>4. Mental Illness Became a Downstream Externality</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-806c-8a70-dfdc2ee84061" class="">When systems destabilize nervous systems, there are only two choices:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-806a-b086-e1af47be2057" class="numbered-list" start="1"><li>Redesign the system</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-802b-94e2-d108e338d5c3" class="numbered-list" start="2"><li>Redefine the human as broken</li></ol></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c0-83e5-f10bc467a147" class="">We chose the second.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8013-8342-fc24c1343457" class="">Anxiety became a disorder.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803a-ba7e-cbfe3f8e0dd4" class="">Burnout became personal failure.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d9-910f-f62d1c037cd7" class="">Attention collapse became pathology.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-804c-a5e1-e4d637f59dd5" class="">Emotional exhaustion became weakness.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8063-8e46-ebc77d60cb53" class="">The system was never interrogated.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-808f-b380-e901d47e3f6c" class="">The human was medicalized.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-809f-b97f-d42a766c294f" class="">This is not accidental.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80e5-a06e-ea9a3fb64a88" class="">It is cheaper.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8078-a6fc-fcf311e972e1"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80fa-9442-eb0cd6bb9a50" class=""><strong>5. The Care Economy Exists to Treat System Damage</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f3-8f9e-d9d49f69a336" class="">Mental health services now function as <strong>damage control for hostile environments</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80de-aa95-fe82945a719f" class="">Apps teach:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-805d-a4d7-d62da1154946" class="bulleted-list"><li style="list-style-type:disc">breathing under surveillance</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8047-9f94-e849d71b405f" class="bulleted-list"><li style="list-style-type:disc">resilience under precarity</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ec-bca0-ff0fc92ed7d2" class="bulleted-list"><li style="list-style-type:disc">calm inside coercion</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8049-8334-fe3e3666b50c" class="bulleted-list"><li style="list-style-type:disc">self-regulation inside extraction</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80eb-a6a0-ce8f249edd28" class="">This is not healing.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a2-9952-ec59c183ea7d" class="">It is <strong>adaptation to harm</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-802b-9444-fadcf0355107" class="">When therapy is required to survive daily systems, the system is the illness.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-803d-ac85-fe3fe61ce42b"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80eb-b2e1-df6f51571ead" class=""><strong>6. “Choice” Was Replaced With Structured Compliance</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8061-87ed-ef1d62de14ce" class="">Human-Centered Design perfected a dangerous illusion:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8021-a567-e05885d896c4" class="">That consent exists where refusal is punished.</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a7-b7d7-d076c85402dd" class="">Users are offered:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-809c-bac9-c5938ba7b139" class="bulleted-list"><li style="list-style-type:disc">opt-ins</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-808d-8ebf-e81113242b5f" class="bulleted-list"><li style="list-style-type:disc">settings</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8000-86dc-e5052c69dd35" class="bulleted-list"><li style="list-style-type:disc">preferences</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e4-9e36-c2f448670908" class="bulleted-list"><li style="list-style-type:disc">customization</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80eb-bba8-c643adcad35c" class="">But refusing costs:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8061-ab2d-e8c66b6f5ea0" class="bulleted-list"><li style="list-style-type:disc">access</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a6-b682-cb962834e31e" class="bulleted-list"><li style="list-style-type:disc">opportunity</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e0-ae76-e1cc28372eb3" class="bulleted-list"><li style="list-style-type:disc">status</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806e-8eee-ddb16668cf7f" class="bulleted-list"><li style="list-style-type:disc">income</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80fc-a505-ce59d871cfe0" class="bulleted-list"><li style="list-style-type:disc">social participation</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8021-80e0-fad4e8544c7c" class="">This is not choice.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8028-9a37-c8be3b9c21ef" class="">This is compliance under constraint.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8089-9239-eabd8af021da" class="">A coerced yes is not consent.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8034-8605-e41a47f75d4a" class="">It is engineered surrender.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-809d-9062-e3a5196802f6"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80ed-9e03-eabe7eb7dd5d" class=""><strong>7. Fragility Became a Revenue Stream</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-802b-9558-ff9a1e1f24ba" class="">The most profitable systems today depend on humans being:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f5-9e31-f826e40f93b1" class="bulleted-list"><li style="list-style-type:disc">anxious</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8026-8592-ef6b5843b0c8" class="bulleted-list"><li style="list-style-type:disc">distracted</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8012-9f82-dee8c1acc93f" class="bulleted-list"><li style="list-style-type:disc">lonely</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8018-867b-d8fd9b8b5258" class="bulleted-list"><li style="list-style-type:disc">uncertain</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8016-b8b0-d5b16170e5e7" class="bulleted-list"><li style="list-style-type:disc">overstimulated</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a1-801b-ef1228914a01" class="bulleted-list"><li style="list-style-type:disc">dysregulated</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c2-a47a-c20fee654607" class="">Stable humans are bad for business.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8042-8f3d-eee7f4d38e42" class="">Regulated nervous systems don’t scroll endlessly.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-801b-a1f2-e5e1341490e5" class="">Secure people don’t click compulsively.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-805e-9feb-fc112e3779fd" class="">Calm minds don’t convert impulsively.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-809a-b940-c874993a5fed" class="">So instability is maintained.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80fd-8fd2-c7e3d38424e9" class="">Quietly.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8091-87f0-c5d888ed60e8" class="">Systematically.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c2-a51b-c888cc4aafd9" class="">Legally.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-800c-8699-da44ffe85fe4"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8005-b8ff-cc3f1b94f010" class=""><strong>8. Human-Centered Design Created Anti-Human Systems</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b6-a970-c5e453966397" class="">A system cannot claim to be human-centered if:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-807e-8911-f5c6650c12dd" class="bulleted-list"><li style="list-style-type:disc">it requires stress to function</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-809f-95a1-e742abf11f06" class="bulleted-list"><li style="list-style-type:disc">it profits from dependency</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-800c-9e27-e598ce68d014" class="bulleted-list"><li style="list-style-type:disc">it degrades attention</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b0-bc53-df9e99cb7648" class="bulleted-list"><li style="list-style-type:disc">it externalizes harm</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8075-88b7-d90a7c9df5d3" class="bulleted-list"><li style="list-style-type:disc">it normalizes exhaustion</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-807d-b685-febb42fbf052" class="bulleted-list"><li style="list-style-type:disc">it penalizes refusal</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80dd-939c-ddc4feb4f810" class="">That is not human-centered design.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b3-bc71-f982212cfdf5" class="">That is <strong>human consumption design</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-801a-99cc-d64a439e7c80"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-801a-8892-d8e33c23a8ea" class=""><strong>9. Intentions Are Irrelevant at Scale</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a9-baff-d1bf06ab4d01" class="">At scale:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d0-a012-e205376a0001" class="bulleted-list"><li style="list-style-type:disc">intentions do not matter</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-803a-9bc9-c4f837d35428" class="bulleted-list"><li style="list-style-type:disc">values do not enforce themselves</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8044-aca8-f0c0dc781812" class="bulleted-list"><li style="list-style-type:disc">empathy does not restrain incentives</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80fb-9afc-d5657946b09e" class="">Only structure matters.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8029-aa36-eeecab6a110e" class="">A system that relies on the goodness of individuals is not ethical.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ac-b906-c8bad81116e2" class="">It is irresponsible.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8044-b062-fa6e88590bea"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8033-bbc8-c0bd655860ad" class=""><strong>10. Why This Could Not End Any Other Way</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c2-8ae6-c01ed033ba8a" class="">Human-Centered Design was deployed inside:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80fa-bb52-e3c2cb2e05cb" class="bulleted-list"><li style="list-style-type:disc">venture capital incentives</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d9-9df8-d218e4a72e4c" class="bulleted-list"><li style="list-style-type:disc">growth-at-all-costs cultures</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f5-959c-d370bf79a0f5" class="bulleted-list"><li style="list-style-type:disc">surveillance economies</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8083-a316-c0a9bd9c94db" class="bulleted-list"><li style="list-style-type:disc">asymmetric power structures</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80df-aa88-f39c506c6cb0" class="">Under these conditions, empathy <strong>will always be exploited</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8084-8460-cf051cad8f0e" class="">This outcome was not corruption.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ff-8133-f8d0c10de0f1" class="">It was inevitability.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-805e-a85b-d78800b5f19b"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80b3-9aa2-c574d2728ca8" class=""><strong>11. The Missing Layer Was Ethical Intelligence</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ef-8fdf-d459feb94940" class="">What was never added was restraint.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ae-acf1-d8102d4c3d25" class="">No hard limits.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800f-a086-e043d99ecd6a" class="">No non-negotiable boundaries.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8039-ba15-cfe499ca428e" class="">No refusal rights.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8062-8577-f46d1acf434d" class="">No harm ceilings.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8015-98df-c7a240c9b2cd" class="">No biological thresholds.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8095-a139-edb9737b0fde" class="">No accountability for long-term damage.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-801f-bfc1-ece7f3350ef7" class="">Empathy without restraint is predation.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-806c-9726-d2b9d82c3048" class="">Insight without obligation is violence with better language.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80a2-8955-cb618de6327e"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80d8-89a9-c363fc11d539" class=""><strong>12. The Final Reckoning</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c2-8eb8-f7eab6624b5b" class="">Human-Centered Design did not make systems humane.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803e-bf5c-c30cc1e73729" class="">It made humans transparent.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d1-8e76-ddc49e77093a" class="">And once transparent, they were mined.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8058-97a7-d845bc9f53fd"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-802a-a01b-f016762f548d" class=""><strong>Final Line (Non-Escapable)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80eb-8c6d-ff24d33800ae" class="">A system is not ethical because it understands humans.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8077-9293-c613a75b61b5" class="">It is ethical only if it is <strong>incapable of exploiting what it understands</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-802c-9500-f64b37012a7c" class="">Anything else is extraction —</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8092-805b-efadf0a906c4" class="">disguised as care,</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803e-a35f-ea85959630a7" class="">normalized as progress,</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800b-8ab6-c1d3035fccc7" class="">and paid for with human stability.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8007-83d2-f2a77901d563"/></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8007-b358-cac6bb5a4a03" class="">If you want the <em>next escalation</em>, the natural follow-ons are:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8008-a2f1-e80938cfd879" class="bulleted-list"><li style="list-style-type:disc"><strong>“The Monetization of Mental Illness Was Not an Accident”</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8080-a0f9-c6bc50fe7e67" class="bulleted-list"><li style="list-style-type:disc"><strong>“Why Empathy Is Dangerous Without Power Limits”</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8036-af5e-efc22e37619f" class="bulleted-list"><li style="list-style-type:disc"><strong>“Designing Systems That Are Incapable of Harm”</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8085-bcae-efead2a9707d" class="bulleted-list"><li style="list-style-type:disc"><strong>“Consent Collapse in the Attention Economy”</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8024-8114-eb387160f46a" class="">Say which one you want to lock next.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
