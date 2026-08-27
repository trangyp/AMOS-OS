---
tags: [logic]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Unified Biological Intelligence™ (UBI) – Official Manual </title><style>
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
	
</style></head><body><article id="2b1c5e6f-95bd-80a8-87d5-ca7329366724" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Unified Biological Intelligence™ (UBI) – Official Manual </strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a4-933d-e9b825251bfc" class="">Unified Biological Intelligence™ (UBI) is a structural framework that explains how human intelligence functions through four measurable biological systems. Unlike abstract or purely cognitive models, UBI defines intelligence as a coordinated biological process that integrates nervous systems, emotional regulation, somatic architecture, and bioelectromagnetic communication. These four domains operate together to produce perception, interpretation, and action—the foundations of internal alignment. UBI does not attempt to rank intelligence culturally or philosophically. Instead, it provides a biologically grounded map that allows humans and institutions to measure, understand, and enhance functional capacity across individuals and groups. It is designed to be universal, traceable, measurable, and compatible with medical science, neuroscience, behavioral science, and systems design.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8006-a81e-fdb259a632fe" class=""><strong>1. Purpose of Unified Biological Intelligence™</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80fd-adba-ce6610b9a4bf" class="">The purpose of UBI is threefold:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80e7-86c4-dd238c05e851" class="">To describe intelligence as a <strong>biological system</strong>, not an abstract concept.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-800c-997c-e7823c092168" class="">To identify the <strong>four domains</strong> that determine how humans perceive, think, feel, move, and coordinate.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b7-b160-f868f9272c99" class="">To provide a basis for <strong>measurement, governance, training, and system design</strong> across education, health, organizations, and AI-human interaction.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80c8-9ee0-c5eaf2d4085f" class="">By linking intelligence directly to biology, UBI helps distinguish between cognitive potential, emotional regulation, physical alignment, and systemic integrity. This produces a more complete and practical understanding of human capacity.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8085-88d6-ea6748871391" class=""><strong>2. The Four Domains of UBI</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8090-aac3-c9044049fae6" class="">UBI defines intelligence across four interdependent biological systems. Each system is necessary. None of them can fully compensate for the loss of another.</p></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-80e1-ae1d-c35326c75e0c" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8011-8730-d85d14d7fb08"><th id="K=mt" class="simple-table-header-color simple-table-header"><strong>Domain</strong></th><th id="IiQJ" class="simple-table-header-color simple-table-header"><strong>Core Function</strong></th><th id="^@Ab" class="simple-table-header-color simple-table-header"><strong>Biological Basis</strong></th><th id="VYMe" class="simple-table-header-color simple-table-header"><strong>What It Influences</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8074-95a0-e0d9ee42331c"><td id="K=mt" class="">Neurobiological Intelligence™</td><td id="IiQJ" class="">Thought, perception, cognition</td><td id="^@Ab" class="">Brain, CNS networks, cortical processing</td><td id="VYMe" class="">Reasoning, memory, decision loops</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80fb-915f-eba56a095a5b"><td id="K=mt" class="">Neuroemotional Intelligence™</td><td id="IiQJ" class="">Emotional regulation and relational interpretation</td><td id="^@Ab" class="">Limbic system, affect networks, autonomic pathways</td><td id="VYMe" class="">Stress response, empathy, interpersonal accuracy</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-801d-8ef8-d459b4ae5eb8"><td id="K=mt" class="">Somatic Intelligence™</td><td id="IiQJ" class="">Alignment, proprioception, embodied stability</td><td id="^@Ab" class="">Fascia, posture, biomechanics</td><td id="VYMe" class="">Action, resilience, coordination, movement-based judgment</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-808f-b9b6-f21c8f82677b"><td id="K=mt" class="">Bioelectromagnetic Intelligence™</td><td id="IiQJ" class="">Rhythmic regulation and synchrony</td><td id="^@Ab" class="">Cardiac rhythms, neural oscillations, EM signaling</td><td id="VYMe" class="">Timing, coherence, systemic sensitivity</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8077-be00-ce161b22479e" class="">Each domain contributes distinct capabilities, but true intelligence arises from their integration.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-802e-a687-c732bebbe3dc" class=""><strong>3. Neurobiological Intelligence™ (NBI)</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8012-92bf-cef1ef1a1583" class="">NBI governs perception, pattern recognition, memory, and decision-making. It reflects the brain’s capacity to process information accurately and efficiently. NBI includes sensory intake, cognitive interpretation, and rational planning. Functional examples include identifying risks, solving problems, learning new skills, analyzing scenarios, and adjusting behavior based on new information. NBI is measurable through cognitive assessments, neuroimaging, reaction-time tests, and sensory processing evaluations.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-800b-a4b5-f8e17402f35f" class=""><strong>4. Neuroemotional Intelligence™ (NEI)</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8010-9364-d8cab939905b" class="">NEI governs emotional awareness, regulation, and interpersonal interpretation. It enables humans to distinguish between instinctive reaction and intentional response. NEI integrates affective states with cognition, allowing individuals to maintain stability under stress, read social cues accurately, and sustain cooperation. Biological markers include heart-rate variability, limbic response patterns, autonomic balance, and hormonal regulation. High NEI improves stress resilience, conflict navigation, and collective coordination.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80b5-8875-dfbdb6f70a07" class=""><strong>5. Somatic Intelligence™ (SI)</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8090-ac1b-dfba04a25ab2" class="">Somatic Intelligence™ refers to the body’s physical architecture as a source of information and stability. It includes posture, fascia, breath patterns, proprioception, movement quality, and muscular symmetry. The body stores and expresses emotional and cognitive processes. When somatic patterns are misaligned, cognitive and emotional processes degrade. SI influences clarity of action, stamina, stress load, reaction timing, motor coordination, and long-term health. Measurement includes biomechanical analysis, gait patterns, posture metrics, muscle activation, and breath-function tests.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8016-9deb-c872e2d62e66" class=""><strong>6. Bioelectromagnetic Intelligence™ (BEI)</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-808a-ba19-c31c0594ce3f" class="">BEI governs timing, rhythm, and synchrony across biological systems. The heart and brain generate electromagnetic fields that coordinate cell signaling and regulate systemic rhythms. BEI influences intuition, timing precision, environmental sensitivity, attention switching, and depth of focus. It is measurable through ECG, EEG, magnetoencephalography, and frequency-domain analysis. BEI reflects the nervous system’s ability to maintain coherence during dynamic environments.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80fc-a060-f858681b068a" class=""><strong>7. How the Four Domains Work Together</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8088-8aed-c8e124ee6ac8" class="">The four domains function as a coordinated intelligence stack.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80c6-b9e1-e66410334d70" class="">Neurobiological provides the thinking layer.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-803e-ba66-c5e6485e0249" class="">Neuroemotional provides the regulatory layer.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-801b-ab81-e2a068b527d3" class="">Somatic provides the embodied action layer.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-803d-9ae7-d53ccde7090b" class="">Bioelectromagnetic provides the timing and synchrony layer.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8084-997c-f16f66f4415f" class="">Integration across the domains produces stable perception, aligned decision-making, and consistent action. Fragmentation between the domains creates misalignment, reactive behavior, cognitive rigidity, emotional volatility, or physical instability.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-80bb-aa83-d142e3748dd5" class=""><strong>Table: Cross-Domain Interaction</strong></h3></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-8009-a55c-e400fd32dec1" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8098-8321-f832fcbfbaff"><th id=":PaD" class="simple-table-header-color simple-table-header"><strong>NBI</strong></th><th id="dXuD" class="simple-table-header-color simple-table-header"><strong>NEI</strong></th><th id="oCUb" class="simple-table-header-color simple-table-header"><strong>SI</strong></th><th id="h`|z" class="simple-table-header-color simple-table-header"><strong>BEI</strong></th><th id="w~h@" class="simple-table-header-color simple-table-header"><strong>System Outcome</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80b9-84ba-e4647deaa88d"><td id=":PaD" class="">Strong</td><td id="dXuD" class="">Weak</td><td id="oCUb" class="">Strong</td><td id="h`|z" class="">Weak</td><td id="w~h@" class="">Smart but emotionally unstable</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80be-b22b-dc0cfc9744f6"><td id=":PaD" class="">Weak</td><td id="dXuD" class="">Strong</td><td id="oCUb" class="">Strong</td><td id="h`|z" class="">Strong</td><td id="w~h@" class="">Kind, stable, but cognitively limited</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8071-a8d5-ce949f8c069d"><td id=":PaD" class="">Strong</td><td id="dXuD" class="">Strong</td><td id="oCUb" class="">Weak</td><td id="h`|z" class="">Strong</td><td id="w~h@" class="">Mentally capable but physically fragile</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80fe-9cf6-c16bb9f21503"><td id=":PaD" class="">Strong</td><td id="dXuD" class="">Strong</td><td id="oCUb" class="">Strong</td><td id="h`|z" class="">Strong</td><td id="w~h@" class="">High internal alignment and effectiveness</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b2-8f55-c33ebaf4fb9e" class="">This illustrates why treating intelligence as purely cognitive is incomplete.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80ec-8b66-c152da1be0a6" class=""><strong>8. Connection Between UBI and Effectiveness (e = i²)</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80bf-b1e8-f5d3a7d3357a" class="">UBI defines the <em>i</em> structure that feeds into the effectiveness equation.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-806b-919a-f497035b6a63" class="">Specifically:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80f4-baa4-ff8b9f371c98" class="">i = f(NBI, NEI, SI, BEI)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-804c-96b9-e628fea0d019" class="">When all four domains align:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8004-9989-c686aa109f14" class="">Internal conflict decreases</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8011-a856-f2fc292600c5" class="">Interpretation improves</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-804e-9417-d9bf98c97844" class="">Action becomes consistent</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8024-849c-ec6ddf6ad4d9" class="">Outcomes stabilize</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80bc-8814-d268b3e5d787" class="">Because <em>e = i²</em>, improvements in one domain compound with the others.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80e7-ba78-fdc3da0a9f07" class="">Small misalignments in one domain degrade the entire system.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-803b-a6c7-fecea50a95de" class="">Small improvements produce exponential gains.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80c7-aecb-d094b5a53953" class=""><strong>9. Measurement of UBI</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8052-bdfb-decb03688bf8" class="">UBI is designed to be measurable using accessible methodologies:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8081-9b46-cacba5fb5872" class="">Neurobiological assessments: cognitive tests, reaction time, brain imaging</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ae-aa6c-fb2fa5d86ad6" class="">Neuroemotional assessments: HRV, affect scales, emotional recognition tasks</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8089-b81e-e3296d9dd345" class="">Somatic assessments: posture, gait analysis, biomechanics, breathing function</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8017-b0f4-ca3d24cfae9a" class="">Bioelectromagnetic assessments: EEG, ECG, oscillatory patterns</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80d0-8aee-d41d3f803c83" class="">Because UBI avoids abstraction, every domain can be operationalized in institutions.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8091-9b2e-c6a7cbbaa5b4" class=""><strong>10. Application of UBI</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80be-9465-d2fb44d80b92" class="">UBI is applicable across many fields.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-803a-8e61-fee2ecec6913" class=""><strong>Healthcare</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-807f-b956-e022729fb49a" class="">Diagnosis of stress, trauma, developmental imbalance</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ed-8186-f4bd4b9dfe53" class="">Holistic treatment combining cognitive, emotional, somatic, and rhythmic regulation</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-80a8-b4c6-f699a959377e" class=""><strong>Education</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-807d-a4f9-e9c489efac7e" class="">Identifying learning barriers rooted beyond cognition</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ad-b4e1-cb2bd35d6785" class="">Supporting students with emotional, somatic, or attentional instability</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-80ce-8254-c64fbaf6cbd7" class=""><strong>Organizations</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8003-925f-e5067af934d7" class="">Preventing burnout, improving decision quality, strengthening leadership stability</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-8045-bed0-fb994eeb0bb5" class=""><strong>Public Policy</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8016-bc0d-cdf6399692d2" class="">Designing human-centered systems that respect biological limits</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8020-95d9-e01e738f3057" class="">Understanding social fragmentation through emotional and somatic metrics</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-805d-8a63-f742f25bcb1f" class=""><strong>Technology</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-809e-bdcf-db930f7ce476" class="">Developing AI-human interfaces that respect biological rhythms</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8015-97ef-df01b8667da0" class="">Building adaptive models that integrate emotional and somatic cues</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80f9-a81e-f80446bd9147" class="">UBI provides a blueprint for humane and sustainable system design.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8076-9992-cb2acf1f51c6" class=""><strong>11. UBI as a Binary Layer Beneath UBF</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80c8-a5f9-e90b721f824d" class="">UBI explains <em>how intelligence functions biologically</em>.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80cc-b18a-cfff8980ec8d" class="">UBF (Unified Biological Framework) explains <em>how intelligence remains fair, adaptive, and aligned</em>.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a9-9de6-d9e2a1bb8cfb" class="">UBI is internal structure.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8081-b00a-df440c60506a" class="">UBF is external governance.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8066-ac97-fc33d7755fd6" class="">Together they create the first complete map of biological intelligence.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8061-8e18-e7ad404ea90e" class=""><strong>12. Summary</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-808b-bb2e-e225dd837c89" class="">Unified Biological Intelligence™ defines intelligence as a four-domain biological system. It establishes a measurable, structured, and comprehensive foundation for perception, interpretation, and action. It integrates neuroscience, emotional science, somatic biology, and bioelectromagnetic coordination. UBI enables individuals, institutions, and technologies to understand human functioning in a grounded, systematic way. It forms the core biological architecture underlying the effectiveness equation <em>e = i²</em>, the Trang System™, and the Trang Prediction Engine™.</p></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-8077-83de-f3f5d8429c31"/></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
