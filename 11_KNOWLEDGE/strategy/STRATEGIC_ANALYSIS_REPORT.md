---
tags: [strategy]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>STRATEGIC ANALYSIS REPORT</title><style>
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
	
</style></head><body><article id="284c5e6f-95bd-80fb-b910-cfbe2bd09701" class="page sans"><header><h1 class="page-title" dir="auto"><strong>STRATEGIC ANALYSIS REPORT</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h3 id="284c5e6f-95bd-8025-ba9d-f72aaacaa68f" class=""><strong>ESTABLISHMENT OF UNITAXI &amp; UNI LOGISTIC ENTITIES</strong></h3></div><div style="display:contents" dir="auto"><p id="284c5e6f-95bd-8011-b96c-c995113826bd" class=""><strong>Part of the UNIPOWER Energy Alliance</strong></p></div><div style="display:contents" dir="auto"><hr id="284c5e6f-95bd-8039-9bb8-f63a1dfb0b15"/></div><div style="display:contents" dir="auto"><h3 id="284c5e6f-95bd-8079-a43c-f53a46a1a3c5" class=""><strong>I. STRATEGIC OBJECTIVE</strong></h3></div><div style="display:contents" dir="auto"><p id="284c5e6f-95bd-80d9-b3ac-db55b90b8983" class="">The <strong>UNIPOWER Alliance</strong> plans to establish two strategic legal entities:</p></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-8094-a5d7-eb635480d7c6" class="bulleted-list"><li style="list-style-type:disc"><strong>UNITAXI</strong> – A high-tech passenger transport system using 100% electric vehicles, integrated with UNIPOWER’s charging and clean energy infrastructure.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-80ac-9d51-d3892f1cf783" class="bulleted-list"><li style="list-style-type:disc"><strong>UNI LOGISTIC</strong> – A green logistics network for smart freight transport, operated with light and medium electric trucks, integrating real-time data and digital management platforms.</li></ul></div><div style="display:contents" dir="auto"><p id="284c5e6f-95bd-801a-94da-d405043d5059" class="">Both companies will serve as the <em>operational outputs</em> of UNIPOWER’s energy–transport–technology value chain.</p></div><div style="display:contents" dir="auto"><p id="284c5e6f-95bd-80e2-8142-db5cd29c991c" class="">The goal is to create an integrated ecosystem that connects <strong>electric vehicles – charging stations – operations – data – applications</strong>, enabling full ownership of Vietnam’s green transportation infrastructure.</p></div><div style="display:contents" dir="auto"><hr id="284c5e6f-95bd-80b1-9a87-f3ce7b02f177"/></div><div style="display:contents" dir="auto"><h3 id="284c5e6f-95bd-80b6-b0af-e134df49f58c" class=""><strong>II. ENTITY FORMATION PLAN</strong></h3></div><div style="display:contents" dir="auto"><h3 id="284c5e6f-95bd-80d6-b064-c6270cc4bf58" class=""><strong>1. UNITAXI – Green Technology Transport Service Joint Stock Company</strong></h3></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-8017-b2e6-d68a74131c03" class="bulleted-list"><li style="list-style-type:disc"><strong>Business sector:</strong> passenger transport via electric vehicles, tech-based taxi services, and premium EV ride-hailing.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-80a2-b9e9-d24cd3d3ce9e" class="bulleted-list"><li style="list-style-type:disc"><strong>Business licence:</strong> new registration under Decree 10/2020/NĐ-CP on automobile transport operations.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-8017-b7b9-c5eba66e7ad6" class="bulleted-list"><li style="list-style-type:disc"><strong>Advantages:</strong><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-80d4-9227-c9a189bb1b81" class="bulleted-list"><li style="list-style-type:circle">Full control over brand and governance model.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-8074-ac14-f6f62c00597c" class="bulleted-list"><li style="list-style-type:circle">Legalised nationwide transport operations, facilitating expansion to major cities such as HCMC, Hanoi, and Da Nang.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-80e3-b023-f35d28a31a06" class="bulleted-list"><li style="list-style-type:disc"><strong>Headquarters:</strong> Ho Chi Minh City.</li></ul></div><div style="display:contents" dir="auto"><h3 id="284c5e6f-95bd-8099-b641-cf69c63603c3" class=""><strong>2. UNI LOGISTIC – Smart Green Logistics Solutions Joint Stock Company</strong></h3></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-80fb-b233-fb47b7463905" class="bulleted-list"><li style="list-style-type:disc"><strong>Business sector:</strong> green logistics, express delivery via EVs, and inter-provincial freight transport.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-8098-bdb2-ef483b735edf" class="bulleted-list"><li style="list-style-type:disc"><strong>Technology:</strong> adopts <strong>One Teuch Vietnam</strong> (transport–warehouse–data management platform), integrated via API with <strong>DiDi</strong>, China’s leading transport app, to develop a <em>Smart Logistic Hub</em> managing vehicles, goods, and charging stations in real time.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-806c-8176-c6c0a4d391a6" class="bulleted-list"><li style="list-style-type:disc"><strong>Strategic role:</strong> regional logistics hub connecting goods and services along routes such as Saigon – Da Lat – Binh Thuan – Phan Thiet, etc.</li></ul></div><div style="display:contents" dir="auto"><hr id="284c5e6f-95bd-80d9-ab95-f45822a4cfb3"/></div><div style="display:contents" dir="auto"><h3 id="284c5e6f-95bd-8094-8b0f-c28c9eaecd34" class=""><strong>III. ADVANTAGES OVER ACQUISITION APPROACH</strong></h3></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-800a-a100-dffa65a67cfd" class="bulleted-list"><li style="list-style-type:disc"><strong>Clean legal structure:</strong> avoids liabilities, debts, or pending legal risks from old entities.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-8099-8326-cd0cc1321b1a" class="bulleted-list"><li style="list-style-type:disc"><strong>Operational flexibility:</strong> freedom in brand, technology, and capital structure.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-80aa-b8f2-fb4219a2944e" class="bulleted-list"><li style="list-style-type:disc"><strong>Attractive to investors:</strong> easier to raise capital without being tied to previous financial records.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-80ec-9eb9-c68629559ce1" class="bulleted-list"><li style="list-style-type:disc"><strong>IPO readiness:</strong> transparent documentation and well-defined assets facilitate listing after 3 years.</li></ul></div><div style="display:contents" dir="auto"><hr id="284c5e6f-95bd-80d4-b4b2-e35cc75e2eea"/></div><div style="display:contents" dir="auto"><h3 id="284c5e6f-95bd-8020-b34f-d998abc2e564" class=""><strong>IV. OPERATIONAL MODEL WITHIN UNIPOWER ALLIANCE</strong></h3></div><div style="display:contents" dir="auto"><p id="284c5e6f-95bd-809d-924b-fcde9157a3c0" class=""><strong>UNIPOWER</strong> will act as the parent company — providing strategic coordination and capital allocation for its subsidiaries.</p></div><div style="display:contents" dir="auto"><p id="284c5e6f-95bd-80e6-95fa-f2b5688d94a2" class=""><strong>Organisational structure:</strong></p></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-8047-8465-eee1c26f7f2f" class="bulleted-list"><li style="list-style-type:disc"><strong>UNIPOWER:</strong> parent company overseeing energy ecosystem and investments.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-8059-90e3-dda043352052" class="bulleted-list"><li style="list-style-type:disc"><strong>UNITAXI:</strong> passenger transport operations using EVs.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-80ee-a747-d82fb6935576" class="bulleted-list"><li style="list-style-type:disc"><strong>UNI LOGISTIC:</strong> logistics, freight transport, and data management platform.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-8069-9d73-f46c8082698d" class="bulleted-list"><li style="list-style-type:disc"><strong>INFIPOWER, ISAC Charging:</strong> charging station infrastructure providers.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-8054-b4d1-f39b7f0af377" class="bulleted-list"><li style="list-style-type:disc"><strong>ONE TEUCH:</strong> technology development and international API integration.</li></ul></div><div style="display:contents" dir="auto"><hr id="284c5e6f-95bd-80dc-9726-cf9158dbe9ae"/></div><div style="display:contents" dir="auto"><h3 id="284c5e6f-95bd-80aa-a843-c6d956e66b1a" class=""><strong>V. OPERATIONAL MODEL ILLUSTRATION</strong></h3></div><div style="display:contents" dir="auto"><p id="284c5e6f-95bd-8091-9384-f6f095b7d883" class=""><strong>Example:</strong></p></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-8090-97e8-ec811beae17d" class="bulleted-list"><li style="list-style-type:disc">A customer in HCMC books a ride via the UNITAXI app; the system automatically suggests the nearest car and calculates fares in real time.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-80e8-b232-fcb35d5904ae" class="bulleted-list"><li style="list-style-type:disc">The EV charges at the nearest UNIPOWER ISAC station; charging, operation, and maintenance data are automatically logged on the <strong>ONE TEUCH</strong> platform.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-80a6-9e77-eb302479bdaa" class="bulleted-list"><li style="list-style-type:disc">All operational, financial, and energy consumption data are synchronised on UNIPOWER’s unified management system.</li></ul></div><div style="display:contents" dir="auto"><p id="284c5e6f-95bd-8001-b93c-c9e1024bc050" class=""><strong>Conclusion:</strong></p></div><div style="display:contents" dir="auto"><p id="284c5e6f-95bd-80e3-a3f9-e53090c4ce9c" class="">Establishing new entities for UNITAXI and UNI LOGISTIC is a <strong>strategic, transparent, and flexible long-term solution</strong>, superior to acquiring existing companies.</p></div><div style="display:contents" dir="auto"><p id="284c5e6f-95bd-808f-a360-d4d7dfda9944" class="">This model aligns with UNIPOWER’s vision to <strong>master the integrated value chain of green transport, smart logistics, and renewable energy.</strong></p></div><div style="display:contents" dir="auto"><hr id="284c5e6f-95bd-80fd-b892-ee81d8e60890"/></div><div style="display:contents" dir="auto"><h3 id="284c5e6f-95bd-80d5-b68b-fd79343fcd4b" class=""><strong>VI. VINA TAXI ACQUISITION OPTION</strong></h3></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-809a-9229-efbd9e08997e" class="bulleted-list"><li style="list-style-type:disc"><strong>Estimated value:</strong> ~55 billion VND.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-80c9-b069-f047fc017bf8" class="bulleted-list"><li style="list-style-type:disc"><strong>Existing assets:</strong> 6,000 m² land lot in Binh Tan Industrial Park, HCMC.</li></ul></div><div style="display:contents" dir="auto"><p id="284c5e6f-95bd-804c-a975-fe1e6b2cf638" class=""><strong>Strategic advantages:</strong></p></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-80c7-8023-f1ad8e17b641" class="bulleted-list"><li style="list-style-type:disc">Possesses a valid national taxi business licence, allowing operation in multiple provinces.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-80ae-b903-f4875e11cb6c" class="bulleted-list"><li style="list-style-type:disc">Existing infrastructure and brand can be restructured into <strong>UNITAXI – Green Mobility</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-8048-9840-e5634bf0098e" class="bulleted-list"><li style="list-style-type:disc">The Binh Tan land can serve as a <strong>Southern Depot</strong>, EV maintenance centre, and large-scale 240kW charging station.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-8045-a00d-efbc09c34716" class="bulleted-list"><li style="list-style-type:disc">Can inherit industry codes, transport licences, and personnel.</li></ul></div><div style="display:contents" dir="auto"><p id="284c5e6f-95bd-8056-8c27-f481bd3fa818" class=""><strong>Challenges:</strong></p></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-805d-8f7e-e16d1fcb40bd" class="bulleted-list"><li style="list-style-type:disc">Requires settlement of old debts or fixed assets.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-8088-bad7-de31a0ea79f1" class="bulleted-list"><li style="list-style-type:disc">Vina Taxi brand is outdated → needs strong rebranding to an intelligent EV model.</li></ul></div><div style="display:contents" dir="auto"><p id="284c5e6f-95bd-8073-b738-f95fe90f132b" class=""><strong>Conclusion:</strong></p></div><div style="display:contents" dir="auto"><p id="284c5e6f-95bd-8014-9b99-f6765d8e14f4" class="">This entity serves as an ideal foundation for nationwide UNITAXI development due to its solid legal status, strategic location, and scalability potential.</p></div><div style="display:contents" dir="auto"><hr id="284c5e6f-95bd-80ed-9aba-d349b9faa4dc"/></div><div style="display:contents" dir="auto"><h3 id="284c5e6f-95bd-8037-8d1e-ea4c7b3bf265" class=""><strong>VII. LOGISTICS &amp; TECHNOLOGY SEGMENT</strong></h3></div><div style="display:contents" dir="auto"><p id="284c5e6f-95bd-8069-a685-ff984a27071f" class=""><strong>UNI LOGISTIC</strong> will deploy light and medium electric trucks from <strong>BAOJUN, Tesla, or AION</strong>.</p></div><div style="display:contents" dir="auto"><p id="284c5e6f-95bd-80f4-b2ba-e02f44fa32af" class="">The <em>Green Logistics Hub</em> model connects UNIPOWER’s energy stations, leveraging infrastructure from <strong>VNPOST – ISAC – Mai Linh Logistics</strong>, forming a clean transport network from cities to rural areas.</p></div><div style="display:contents" dir="auto"><p id="284c5e6f-95bd-80c5-ab4f-d82aef9aa517" class=""><strong>Technology solution: One Teuch Vietnam + DiDi Platform</strong></p></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-8052-b007-d47ce0b08677" class="bulleted-list"><li style="list-style-type:disc"><strong>One Teuch Vietnam:</strong> domestic developer of transport and logistics platforms integrating payment, mapping, and AI dispatch.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-80b0-bbd6-ce9987a3d3d9" class="bulleted-list"><li style="list-style-type:disc"><strong>DiDi (China):</strong> world-leading intelligent ride-hailing platform.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-809d-ac91-c74d0ec75cd7" class="bulleted-list"><li style="list-style-type:disc"><strong>Strategic partnership:</strong> between One Teuch Vietnam and DiDi to create a <strong>“UNITAXI–UNI LOGISTIC SuperApp”</strong> for comprehensive management.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-8094-9d7b-e96a5bb1cf61" class="bulleted-list"><li style="list-style-type:disc"><strong>AI integration:</strong> route optimisation and journey analytics to reduce operating costs by 30–40%.</li></ul></div><div style="display:contents" dir="auto"><ul id="284c5e6f-95bd-80e8-bb5d-f0d351cc61c4" class="bulleted-list"><li style="list-style-type:disc"><strong>Direct connection</strong> with UNIPOWER’s charging network, forming a unified <strong>vehicle–energy–data–customer</strong> ecosystem.</li></ul></div><div style="display:contents" dir="auto"><hr id="284c5e6f-95bd-80ea-974f-d56d7211d389"/></div><div style="display:contents" dir="auto"><h3 id="284c5e6f-95bd-80cd-88fd-c58312fb9080" class=""><strong>VIII. IMPLEMENTATION ROADMAP 2025–2026</strong></h3></div><div style="display:contents" dir="auto"><hr id="284c5e6f-95bd-80a5-a15d-db8726554c22"/></div><div style="display:contents" dir="auto"><h3 id="284c5e6f-95bd-806a-8951-e7bc1ad738dd" class=""><strong>IX. SUMMARY REPORT TO BOARD OF DIRECTORS</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="284c5e6f-95bd-8021-9732-dd21a39c17d4" class="numbered-list" start="1"><li>Establishing new entities while leveraging existing legal structures saves licensing time.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="284c5e6f-95bd-80da-9fcc-d7c1b8315878" class="numbered-list" start="2"><li>Combining <strong>international technology (DiDi)</strong> with <strong>domestic platforms (One Teuch Vietnam)</strong> creates a unique competitive edge.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="284c5e6f-95bd-8079-81e9-d0802f8977fe" class="numbered-list" start="3"><li>Optimises UNIPOWER operations by turning static energy into mobile energy through taxi, logistics, and charging networks.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="284c5e6f-95bd-809f-93b3-d659f927b11d" class="numbered-list" start="4"><li>Long-term vision: toward IPO or strategic M&amp;A within 3 years, targeting a high valuation for the UNIPOWER ecosystem.</li></ol></div><div style="display:contents" dir="auto"><hr id="284c5e6f-95bd-80da-9419-d63e6d0c5821"/></div><div style="display:contents" dir="auto"><p id="284c5e6f-95bd-80cd-a744-d923d8ee99d0" class=""><strong>Ho Chi Minh City, 07 October 2025</strong></p></div><div style="display:contents" dir="auto"><p id="284c5e6f-95bd-80b1-b8a5-d82a4cd47df1" class=""><strong>CEO: Hồ Anh Tuấn</strong></p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
