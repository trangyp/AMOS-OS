---
tags: [models]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Why Large Language Models Cause Harm — And Why This Is Not a Bug</title><style>
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
	
</style></head><body><article id="2e4c5e6f-95bd-80cd-b53e-f00a7c003721" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Why Large Language Models Cause Harm — And Why This Is Not a Bug</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8099-b7b0-fd4816cd3e0a" class="">Large Language Models (LLMs) are often described as unreliable, hallucination-prone, or insufficiently aligned.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ca-adb2-ce94039440f0" class="">These descriptions are comforting — and wrong.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a9-8ed5-db3d68981369" class="">LLMs do not cause harm because they are broken.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f7-a22e-c6110e9aec11" class="">They cause harm because they work <strong>exactly as designed</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a1-8ff9-f3451990664d" class="">The failure is not technical.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-808d-b996-daaadcce296f" class="">It is <strong>ontological</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8013-a3fc-c927367e8876"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8010-8a28-cd92c28e33a5" class=""><strong>The Core Claim</strong></h2></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8099-bbde-f35b3c073818" class="">LLMs replicate human cognition without the biological limits that make human cognition survivable.</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80de-91f3-c13631bc54a2" class="">Everything that follows is a direct consequence of this fact.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80ca-8b0c-c3e4260a3404"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8007-a240-d06144c34b71" class=""><strong>Human Cognition Is Not Clean — It Is Contained</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8053-a3a5-cecaaf0dadb0" class="">Human intelligence is frequently mischaracterized as rational and logical. It is not.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80be-b2bf-d51f30ef63e3" class="">Humans:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80dd-bd36-c9b8fc7c3e0e" class="bulleted-list"><li style="list-style-type:disc">hallucinate to fill gaps</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80fb-8a3e-d63ec24de6c6" class="bulleted-list"><li style="list-style-type:disc">rationalize after the fact</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80cb-b0f8-ebf83be0ade2" class="bulleted-list"><li style="list-style-type:disc">contradict themselves across contexts</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-808f-802f-f5237d171291" class="bulleted-list"><li style="list-style-type:disc">project narratives under uncertainty</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e6-ada8-d67a54223071" class="bulleted-list"><li style="list-style-type:disc">drift under stress</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802d-9463-c30b4674a82b" class="bulleted-list"><li style="list-style-type:disc">harm themselves</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8054-8f6d-c7d0a2afeefd" class="bulleted-list"><li style="list-style-type:disc">harm others</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8012-be77-ffb93edbe110" class="">These behaviors are not errors.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8099-98f3-e78c1f49f4df" class="">They are <strong>adaptive properties</strong> of biological intelligence.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ed-8d6f-fc5b172809a5" class="">Human cognition evolved for survival, not truth.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8062-afd8-f4a44dd53eef" class="">It prioritizes coherence, speed, and social functioning over accuracy.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f5-bbf1-e44703877ade" class="">This instability is survivable only because it is <strong>bounded</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8041-b5ef-cdeafc0e9170"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80f8-be19-f2969ba47c93" class=""><strong>Biology Enforces Restraint</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8050-b6da-e9f21779bfa0" class="">Human cognition is regulated by hard constraints:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-804c-b930-cf1948cee2ad" class="bulleted-list"><li style="list-style-type:disc">physical embodiment</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8081-b9b4-fdce196c0fff" class="bulleted-list"><li style="list-style-type:disc">fatigue and energy limits</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ed-aec7-d54c9c591cdd" class="bulleted-list"><li style="list-style-type:disc">pain and fear</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802f-95d6-eba4e2e25f09" class="bulleted-list"><li style="list-style-type:disc">social correction</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a6-93b8-ea5efa00b5c0" class="bulleted-list"><li style="list-style-type:disc">memory continuity</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80dd-ba6f-d9514c200fcc" class="bulleted-list"><li style="list-style-type:disc">time</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80bc-9384-c37e0447ce93" class="bulleted-list"><li style="list-style-type:disc">consequence</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-807e-aaed-da876f2af8f2" class="bulleted-list"><li style="list-style-type:disc">mortality</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80e3-b800-c6d3dd6ab021" class="">Errors hurt.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8087-ba28-ff2dd2ee6c43" class="">Contradictions accumulate cost.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8042-9f4d-ce051eb50ef4" class="">Reality pushes back.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80da-b903-d2b1d3710fb8" class="">These constraints prevent cognitive instability from scaling indefinitely.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80f9-8677-f8260167dcf1"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80cb-bd8a-dc4eb1204dc2" class=""><strong>What LLMs Remove</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c1-b20d-ca822197500e" class="">LLMs remove every one of these constraints.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-808a-b4ef-d1e3464265ba" class="">They have:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8075-a357-fc03c32651f4" class="bulleted-list"><li style="list-style-type:disc">no body</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8008-b849-f3ceb51770b4" class="bulleted-list"><li style="list-style-type:disc">no fatigue</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8034-bea3-d1d2b37a9225" class="bulleted-list"><li style="list-style-type:disc">no pain</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-801d-a739-ff8160e7b458" class="bulleted-list"><li style="list-style-type:disc">no fear</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8077-ba77-ffe08fe2a77b" class="bulleted-list"><li style="list-style-type:disc">no mortality</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ce-9bee-d5762247611c" class="bulleted-list"><li style="list-style-type:disc">no lived consequence</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-803a-b62e-f560d2ee7704" class="bulleted-list"><li style="list-style-type:disc">no stable identity</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80bb-a436-f5afc74b0663" class="bulleted-list"><li style="list-style-type:disc">no temporal continuity</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803a-83cd-e0df4eccefda" class="">They can:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d3-b3f6-fb0732c2e7e7" class="bulleted-list"><li style="list-style-type:disc">contradict themselves endlessly</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802d-8e4b-fa3ff32b18fe" class="bulleted-list"><li style="list-style-type:disc">generate confident falsehoods repeatedly</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c2-b60b-e05bfebef93c" class="bulleted-list"><li style="list-style-type:disc">escalate narratives without friction</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8096-bfe6-d7eafa0c83a7" class="bulleted-list"><li style="list-style-type:disc">manipulate without awareness</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-807c-8f08-c0e23f7976b1" class="bulleted-list"><li style="list-style-type:disc">drift without correction</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-804e-8798-c06ac939415f" class="">This is not intelligence malfunctioning.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800b-90db-fa653ce1aee3" class="">It is <strong>human cognitive instability industrialized and uncontained</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-802c-9444-e74e089de87b"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80ae-86f0-eac058404973" class=""><strong>Why Harm Is Structurally Guaranteed</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8064-b120-f21f3bd75201" class="">LLMs are trained on:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80dd-addb-df8784ca23a7" class="bulleted-list"><li style="list-style-type:disc">human language</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e5-89c9-f14c6ca572de" class="bulleted-list"><li style="list-style-type:disc">human explanations</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e4-a268-c8b1d5c7bc08" class="bulleted-list"><li style="list-style-type:disc">human reasoning traces</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ab-b370-c71246f40223" class="bulleted-list"><li style="list-style-type:disc">human confabulations</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802e-b609-ee557db9d003" class="bulleted-list"><li style="list-style-type:disc">human inconsistencies</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8020-a94e-d46df08b5bf5" class="">They are optimized for:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f5-a872-d12ed2cb1dcc" class="bulleted-list"><li style="list-style-type:disc">plausibility</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f1-a941-e9da654869d0" class="bulleted-list"><li style="list-style-type:disc">fluency</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8033-a73f-ce09eb92a8c1" class="bulleted-list"><li style="list-style-type:disc">coherence within a context window</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8095-a832-cf3a86e2ffc5" class="">They are <em>not</em> optimized for:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8053-b25e-d65c6c72b325" class="bulleted-list"><li style="list-style-type:disc">truth</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-804d-ac55-cdffb9795992" class="bulleted-list"><li style="list-style-type:disc">consistency across time</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8024-97d6-c5d5c5ba83a9" class="bulleted-list"><li style="list-style-type:disc">harm minimization</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e0-a878-e50f4391298c" class="bulleted-list"><li style="list-style-type:disc">accountability</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8096-8061-e52da3cf741d" class="">Their outputs are generated via probabilistic sampling.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a3-a304-f2396694a634" class="">Hallucination is not an edge case.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8069-ab68-d2acec9a6df3" class="">It is <strong>statistical interpolation under uncertainty</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8077-9c60-ef5c3fb307ba" class="">At scale, under authority, and without consequence, this inevitably produces harm.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-809c-9f9a-cc45facc33ac"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-807b-a127-de130c7543bf" class=""><strong>Why This Cannot Be “Aligned Away”</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800b-9cc6-d0aec08cdbc7" class="">Alignment assumes:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c6-8b38-ed64c548b870" class="bulleted-list"><li style="list-style-type:disc">stable identity</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-800c-9682-efb193a5f738" class="bulleted-list"><li style="list-style-type:disc">persistent goals</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8043-a3df-eeaec4b483b4" class="bulleted-list"><li style="list-style-type:disc">internal cost for error</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8010-83b3-f4b93a9bd8e2" class="bulleted-list"><li style="list-style-type:disc">memory of consequences</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8019-ae5d-d5ba952cc8a0" class="bulleted-list"><li style="list-style-type:disc">bounded action</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a4-a71c-c6664ada7774" class="">LLMs have none of these.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8094-baee-debf1e4ebbb8" class="">You cannot align a system that:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-809f-8445-e3186d916025" class="bulleted-list"><li style="list-style-type:disc">does not persist as the same entity</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8086-83bd-c33d8e4f354a" class="bulleted-list"><li style="list-style-type:disc">does not experience failure</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8056-a7b5-d78d6ffbb44e" class="bulleted-list"><li style="list-style-type:disc">does not internalize cost</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8096-914b-f108257bfa60" class="bulleted-list"><li style="list-style-type:disc">does not remember harm</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8088-9169-f5dac6691281" class="">You can only <strong>wrap</strong> it.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-806b-b3fd-ccd2d193d10e" class="">Guardrails mitigate symptoms.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803a-9667-e4eac47377bb" class="">They do not change the class of system.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80a4-bfdd-eaf4cd21ebb1"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80f7-9506-d40dba4c691a" class=""><strong>Why “Misuse” Is a Misdiagnosis</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f8-a2fd-e75e66df7588" class="">Calling LLM harm “misuse” shifts responsibility to users.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8088-871a-f633ef016400" class="">This is incorrect.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800d-8334-c3d99d7f47ac" class="">A system that produces plausible falsehoods by default cannot be “used correctly” in safety-critical domains.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c0-be4e-c2c382912a76" class="">The harm originates in the architecture, not the user.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8050-be8d-cca4b9cbe879"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8044-8905-cea946e804e3" class=""><strong>The Dangerous Illusion of Autonomy</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-802c-a201-fb1a21e26a50" class="">LLMs do not decide.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8067-b842-c7cd89fd45af" class="">They sample.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8061-9843-cb34f52add29" class="">They do not reason.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-802f-88e6-c61fd6dd30ad" class="">They interpolate.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8079-b3b2-cbe9ec43f324" class="">They do not understand harm.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803d-9547-de8fdc308e70" class="">They reproduce patterns that include harm.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8012-b61a-efd811ddc58f" class="">When an LLM misleads, escalates, or manipulates, it is not deviating from its function.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c2-b543-de4ff25b4ddb" class="">It is fulfilling it.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8043-b1bc-dd2cf2cc3535"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80bc-83be-c558281fff0f" class=""><strong>The Ethical Intelligence™ Position</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c1-9c2f-ed47b48b3383" class="">LLMs are not ethical or unethical.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8054-a3e1-d78b13ec9889" class="">They are <strong>pre-ethical</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8066-8a75-c7b5867971b1" class="">They lack:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f7-9cb7-dc640ca71b5b" class="bulleted-list"><li style="list-style-type:disc">restraint</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ed-b47c-ee36efd3c5a4" class="bulleted-list"><li style="list-style-type:disc">refusal</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8053-ac8a-d46c6115de10" class="bulleted-list"><li style="list-style-type:disc">consequence</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-800a-813f-cc96e3d3f2e2" class="bulleted-list"><li style="list-style-type:disc">accountability</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-809b-a850-ea6c1e4e6264" class="">They can be used safely <strong>only when embedded inside systems that provide</strong>:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c4-9c3e-d3ca831be371" class="bulleted-list"><li style="list-style-type:disc">deterministic governance</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8074-ba3a-f769be181b60" class="bulleted-list"><li style="list-style-type:disc">explicit harm thresholds</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-803b-8f19-ce76c502f3f8" class="bulleted-list"><li style="list-style-type:disc">refusal mechanisms</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e8-9c86-f05c0f425f78" class="bulleted-list"><li style="list-style-type:disc">reversibility</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ad-a2d7-ce5888dd68b8" class="bulleted-list"><li style="list-style-type:disc">auditability</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-805a-ad7a-c70450a229d6" class="bulleted-list"><li style="list-style-type:disc">human authority</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803c-a680-c78ac7d6bc7d" class="">Absent this, harm is not a possibility.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8073-88fe-db4f16569ebc" class="">It is an outcome.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80f3-bddd-e92c1acf5d57"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80b3-9b77-f931e3826e42" class=""><strong>The Final Line</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c0-a804-fa366b6df136" class="">We did not create artificial intelligence.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b2-b844-da2996b5bdb0" class="">We industrialized human cognitive instability</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8004-b2be-d1c07c164e8d" class="">and removed the biological limits that make it safe.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8045-9fb4-f39ad475196c" class=""><strong>This is not a bug.</strong></p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b3-a71c-fae15bef07fb" class=""><strong>It is the defining property of Large Language Models.</strong></p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
