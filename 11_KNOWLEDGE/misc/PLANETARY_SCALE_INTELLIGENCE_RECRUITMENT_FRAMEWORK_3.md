---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Planetary-Scale Intelligence Recruitment Framework </title><style>
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
	
</style></head><body><article id="24cc5e6f-95bd-801f-86a6-eeb88b123b78" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Planetary-Scale Intelligence Recruitment Framework</strong> </h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><hr id="24cc5e6f-95bd-8065-98b9-d846fab85457"/></div><div style="display:contents" dir="auto"><h2 id="24cc5e6f-95bd-802c-b546-d480436d585c" class=""><strong>1. Core Definition of Planetary-Scale Intelligence</strong></h2></div><div style="display:contents" dir="auto"><p id="24cc5e6f-95bd-807d-988a-c1fee1c5a4e7" class="">Before recruiting, the organization must define exactly what “planetary-scale” means in measurable terms:</p></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-80ed-9a1f-ddc88e3a4a5e" class="bulleted-list"><li style="list-style-type:disc"><strong>Systemic Span</strong> — The ability to integrate environmental, technological, economic, biological, and cultural systems into unified strategies.</li></ul></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-8003-bb64-e44796674f0c" class="bulleted-list"><li style="list-style-type:disc"><strong>Time Horizon</strong> — The ability to design for decades or centuries, not just fiscal quarters.</li></ul></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-8098-9ba7-c745f278f4b1" class="bulleted-list"><li style="list-style-type:disc"><strong>Ethical Integrity</strong> — Proven record of applying decisions that scale without harming planetary systems or future generations.</li></ul></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-801d-8b72-dbf3c3d741a6" class="bulleted-list"><li style="list-style-type:disc"><strong>Cross-Domain Literacy</strong> — Competence in multiple disciplines (e.g., neuroscience + climate science + governance).</li></ul></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-80c2-b49d-eb056569aaeb" class="bulleted-list"><li style="list-style-type:disc"><strong>Action Orientation</strong> — History of implementing large-scale changes, not just theorizing.</li></ul></div><div style="display:contents" dir="auto"><hr id="24cc5e6f-95bd-805d-a01e-f758c8ac0fc5"/></div><div style="display:contents" dir="auto"><h2 id="24cc5e6f-95bd-8049-a2d8-e2eac150ff34" class=""><strong>2. Selection Criteria</strong></h2></div><div style="display:contents" dir="auto"><h3 id="24cc5e6f-95bd-80e1-b381-e474e7f7583f" class=""><strong>A. Cognitive &amp; Structural Capabilities</strong></h3></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-8053-b914-e6d03e9a5ef6" class="bulleted-list"><li style="list-style-type:disc">Demonstrated ability to <strong>map interdependent global systems</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-8063-b03c-c3ebc70e5c37" class="bulleted-list"><li style="list-style-type:disc">Proven skill in <strong>first principles reasoning</strong> at macro scale.</li></ul></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-80f2-b971-ff0d2a12e1d7" class="bulleted-list"><li style="list-style-type:disc">Ability to <strong>operationalize planetary strategies</strong> into implementable programs.</li></ul></div><div style="display:contents" dir="auto"><h3 id="24cc5e6f-95bd-80d3-8d35-d282016791ec" class=""><strong>B. Domain Breadth</strong></h3></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-8086-8770-f87caf517ea0" class="bulleted-list"><li style="list-style-type:disc">At least two domains at expert level (e.g., AI systems + ecological governance).</li></ul></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-80a2-8842-d47f1f00f185" class="bulleted-list"><li style="list-style-type:disc">Track record in <strong>integrating biology with technology</strong> or equivalent.</li></ul></div><div style="display:contents" dir="auto"><h3 id="24cc5e6f-95bd-80b4-85b2-f731032e85a8" class=""><strong>C. Decision-Making Integrity</strong></h3></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-8088-ae24-c4706ed339c3" class="bulleted-list"><li style="list-style-type:disc">Documented history of <strong>avoiding short-term optimization traps</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-80f5-a6af-dc14080d5f38" class="bulleted-list"><li style="list-style-type:disc">Willingness to <strong>suspend personal gain</strong> for planetary-scale outcomes.</li></ul></div><div style="display:contents" dir="auto"><hr id="24cc5e6f-95bd-8013-aeef-fbdc423e5c95"/></div><div style="display:contents" dir="auto"><h2 id="24cc5e6f-95bd-801f-a179-f02a1a23a9e2" class=""><strong>3. Sourcing Strategy</strong></h2></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-8079-b067-edbac18ebf88" class="bulleted-list"><li style="list-style-type:disc"><strong>Global Systems Conferences</strong> — Stockholm Resilience Centre, Planetary Boundaries dialogues, UN AI for Good.</li></ul></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-8065-8e5f-d737b22d143e" class="bulleted-list"><li style="list-style-type:disc"><strong>Cross-Disciplinary Research Institutes</strong> — Santa Fe Institute, MIT Media Lab, Future Earth.</li></ul></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-803f-b7b9-ca6e2454b092" class="bulleted-list"><li style="list-style-type:disc"><strong>High-Impact Fellowships</strong> — Schmidt Futures, Ashoka Fellows, Global Good Fund.</li></ul></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-807d-9d68-d164106149bd" class="bulleted-list"><li style="list-style-type:disc"><strong>Elite Network Mapping</strong> — Identify individuals at the nexus of policy, science, and technology.</li></ul></div><div style="display:contents" dir="auto"><hr id="24cc5e6f-95bd-8003-a777-e65780d492e5"/></div><div style="display:contents" dir="auto"><h2 id="24cc5e6f-95bd-80e5-b9a7-fb704477eb93" class=""><strong>4. Screening Process</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="24cc5e6f-95bd-8056-a352-f483ea31c445" class="numbered-list" start="1"><li><strong>Scenario Stress Test</strong> — Present a hypothetical planetary crisis (e.g., collapse of oceanic ecosystems) and evaluate their systemic solution design.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24cc5e6f-95bd-800c-92c8-ca4a48cc15f2" class="numbered-list" start="2"><li><strong>Interdisciplinary Synthesis Exercise</strong> — Give inputs from five unrelated fields; assess ability to merge into a coherent, actionable model.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24cc5e6f-95bd-8029-979c-ff270b5d80be" class="numbered-list" start="3"><li><strong>Ethics Alignment Audit</strong> — Measure their willingness to uphold Absolute Biological Integrity™ principles.</li></ol></div><div style="display:contents" dir="auto"><hr id="24cc5e6f-95bd-80c3-8609-ed10981f0d49"/></div><div style="display:contents" dir="auto"><h2 id="24cc5e6f-95bd-807a-8f57-dcd3162202f3" class=""><strong>5. Integration into the Ecosystem</strong></h2></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-8051-b044-d50d341c90a8" class="bulleted-list"><li style="list-style-type:disc">Assign them to <strong>planetary governance pods</strong> within UBI and NeuroSyncAI projects.</li></ul></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-802a-add5-e9b101ec4791" class="bulleted-list"><li style="list-style-type:disc">Ensure <strong>cross-pollination with other high-scale thinkers</strong> to expand scope.</li></ul></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-80c0-a11a-f48a79b39557" class="bulleted-list"><li style="list-style-type:disc">Use the <strong>Metacognitive Loop™</strong> as the integration and governance protocol.</li></ul></div><div style="display:contents" dir="auto"><hr id="24cc5e6f-95bd-8006-9180-f5ad62c18d3a"/></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="24cc5e6f-95bd-806d-b970-d48d3db5c849" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">flowchart TD
    A[Universe of Candidates] --&gt; B[Targeted Sourcing]
    B --&gt; C[Signal Scan + Portfolio Triage]
    C --&gt; D[Planetary Scenario Stress Test]
    D --&gt; E[Interdisciplinary Synthesis Exercise]
    E --&gt; F[Ethics &amp; Integrity Audit ABI]
    F --&gt; G[Deep Dossier &amp; References]
    G --&gt; H[Trial Pod Sprint 4–6 weeks]
    H --&gt; I[Score &amp; Decision Gate]
    I --&gt;|≥85 Composite| J[Offer: Planetary Architect]
    I --&gt;|70–84| K[Talent Bench / Fellowship]
    I --&gt;|&lt;70| L[Decline with Feedback]

    %% Sourcing channels
    B --&gt; B1[Santa Fe Institute / Future Earth]
    B --&gt; B2[Planetary Boundaries / SRC]
    B --&gt; B3[MIT/Stanford cross-dept labs]
    B --&gt; B4[Schmidt Futures / Ashoka Fellows]

    %% Scoring rubric inputs
    D --&gt; R1Systemic Span  0–30
    E --&gt; R2Cross-Domain Synthesis 0–25
    F --&gt; R3Ethical Integrity ABI 0–25
    H --&gt; R4Execution Under Ambiguity 0–20
    R1 --&gt; I
    R2 --&gt; I
    R3 --&gt; I
    R4 --&gt; I</code></pre></div><div style="display:contents" dir="auto"><p id="24cc5e6f-95bd-80c0-b123-cb7a1e4baa6a" class=""><strong>What each gate checks</strong></p></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-80cb-8f74-c69b21b7f8ad" class="bulleted-list"><li style="list-style-type:disc"><strong>Signal Scan:</strong> evidence of planetary systems thinking, multi-decade horizon, prior implementation.</li></ul></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-8073-a171-fe41b2080b9d" class="bulleted-list"><li style="list-style-type:disc"><strong>Scenario Stress Test:</strong> designs for coupled crises (e.g., oceans + energy + governance) with measurable outcomes.</li></ul></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-80d8-a395-c73ce77ff9d9" class="bulleted-list"><li style="list-style-type:disc"><strong>Interdisciplinary Synthesis:</strong> turns 5 disjoint inputs into one executable model.</li></ul></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-808b-9ff9-dd83d69d4258" class="bulleted-list"><li style="list-style-type:disc"><strong>Ethics &amp; Integrity (ABI):</strong> alignment with Absolute Biological Integrity; refusal of short-term optimization that harms systems.</li></ul></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-804d-b7f8-c1ffa0f96a08" class="bulleted-list"><li style="list-style-type:disc"><strong>Trial Pod Sprint:</strong> 4–6 weeks inside a UBI/NeuroSyncAI pod to validate execution, collaboration, and drift resistance.</li></ul></div><div style="display:contents" dir="auto"><p id="24cc5e6f-95bd-80f7-9597-f0efce9ea93b" class=""><strong>Composite scoring (100)</strong></p></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-80f6-90ee-d683fab914a4" class="bulleted-list"><li style="list-style-type:disc">Systemic Span <strong>30</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-8009-8191-c256ae9f2aa5" class="bulleted-list"><li style="list-style-type:disc">Cross-Domain Synthesis <strong>25</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-8013-9c5e-e982087e377a" class="bulleted-list"><li style="list-style-type:disc">ABI Ethics <strong>25</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="24cc5e6f-95bd-804a-a519-d1072e1d22bf" class="bulleted-list"><li style="list-style-type:disc">Execution Under Ambiguity <strong>20</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="24cc5e6f-95bd-80f5-a3c8-f5261e5f9a5b"/></div><div style="display:contents" dir="auto"><p id="24cc5e6f-95bd-8070-92e1-d7843bf6cecd" class=""><strong>This framework ensure all cadidates meet the 3 criteria: </strong></p></div><div style="display:contents" dir="auto"><ol type="1" id="24cc5e6f-95bd-8046-bb9e-ee764271e893" class="numbered-list" start="1"><li><strong>Ethics →</strong> The <em>Ethics &amp; Integrity Audit (ABI)</em> isn’t just a culture-fit check. It tests for Absolute Biological Integrity™ compliance, meaning the candidate must demonstrate decisions that maintain system health over short-term gains. This removes opportunists and “vision without morality” types.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24cc5e6f-95bd-8098-ac6e-e08d4ee9528d" class="numbered-list" start="2"><li><strong>Vision →</strong> The <em>Systemic Span</em> and <em>Interdisciplinary Synthesis</em> steps force candidates to think at planetary scale and integrate cross-domain inputs into a single, executable model — a direct measure of large-scale vision.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24cc5e6f-95bd-8061-8b9f-c81010396c69" class="numbered-list" start="3"><li><strong>Capability → </strong>The <em>Trial Pod Sprint</em> and <em>Execution Under Ambiguity</em> scoring verify that they can deliver in real-world complexity, not just theorize. This weeds out pure “idea people” who can’t execute.</li></ol></div><div style="display:contents" dir="auto"><p id="24cc5e6f-95bd-80d5-a428-c10602fa4aeb" class="">Because these gates are sequential, no one can pass without all three traits being present in balance — if they have vision but no ethics, they fail. If they have ethics but no execution, they fail.</p></div><div style="display:contents" dir="auto"><p id="24cc5e6f-95bd-8029-882e-d7590bc26c27" class="">
</p></div><div style="display:contents" dir="ltr"><figure id="24ec5e6f-95bd-8063-b812-e31d3128ec1d" class="link-to-page"><a href="Planetary-Scale%20Intelligence%20Recruitment%20Framework/PSA%20Due%20Diligent%20-%20Not%20alive%2024ec5e6f95bd8063b812e31d3128ec1d.html">PSA Due Diligent - Not alive</a></figure></div><div style="display:contents" dir="ltr"><figure id="24cc5e6f-95bd-80f6-8a0a-e638f47dc84e" class="link-to-page"><a href="Planetary-Scale%20Intelligence%20Recruitment%20Framework/Planetary-Scale%20Intelligence%20Recruitment%20Trial%20Pod%2024cc5e6f95bd80f68a0ae638f47dc84e.html">Planetary-Scale Intelligence Recruitment: Trial Pod Sprint Brief</a></figure></div><div style="display:contents" dir="ltr"><figure id="24ec5e6f-95bd-807e-a477-c40fbc1d6593" class="link-to-page"><a href="Planetary-Scale%20Intelligence%20Recruitment%20Framework/Planetary%20Scale%20Intelligence%20Recruitment%20Framework%2024ec5e6f95bd807ea477c40fbc1d6593.html">Planetary Scale Intelligence Recruitment Framework (PSI)</a></figure></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
