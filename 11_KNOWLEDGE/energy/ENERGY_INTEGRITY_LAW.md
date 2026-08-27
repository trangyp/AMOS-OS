---
tags: [energy]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title> Energy / Integrity law</title><style>
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
	
</style></head><body><article id="2edc5e6f-95bd-80e7-8510-cebd8552acbd" class="page sans"><header><h1 class="page-title" dir="auto"><strong> Energy / Integrity law</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-8098-80c3-e6c6ccaee902" class="">Good. This is the <strong>right move</strong>, and it can be done cleanly without hand-waving.</p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-80aa-a24c-ebf8414188a3" class="">I’ll integrate the <strong>governance invariants</strong> into your <strong>Energy / Integrity law</strong> in a way that:</p></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-8073-9d1b-e3b442beb6ff" class="bulleted-list"><li style="list-style-type:disc">is <strong>non-moral</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80f3-b786-dc039a57cb18" class="bulleted-list"><li style="list-style-type:disc">is <strong>invariant-based</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80a2-b8ec-e17dab13be27" class="bulleted-list"><li style="list-style-type:disc">is <strong>auditable</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80fb-a92e-d1cf3fea15cb" class="bulleted-list"><li style="list-style-type:disc">survives stress tests</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-8048-afe7-ea340728b600" class="bulleted-list"><li style="list-style-type:disc">and does <strong>not collapse into metaphor</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-8042-a469-c4aad54a7afc" class="">I will be precise and conservative.</p></div><div style="display:contents" dir="auto"><hr id="2edc5e6f-95bd-80c7-b0dd-fab2f1722104"/></div><div style="display:contents" dir="auto"><h2 id="2edc5e6f-95bd-803f-90f2-da373c4c13a2" class=""><strong>Step 1 — Restate your Energy / Integrity law (clean form)</strong></h2></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-805b-a738-e9a09b60275a" class="">We lock this first.</p></div><div style="display:contents" dir="auto"><h3 id="2edc5e6f-95bd-80e4-9295-eec764efa7d0" class=""><strong>Definitions</strong></h3></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-804b-9ab3-f0d8a032e263" class="bulleted-list"><li style="list-style-type:disc"><strong>Potential Energy (P):</strong><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-8012-911b-e07bd4fc0085" class="">The total capacity of a system to act (resources, intelligence, labor, capital, time).</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80a4-8688-c34ec4093ba2" class="bulleted-list"><li style="list-style-type:disc"><strong>Integrity (I):</strong><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-804f-9e16-d274cc5b30c4" class="">The degree of internal coherence between:</p></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80b2-ad27-c785bd157258" class="bulleted-list"><li style="list-style-type:circle">intent</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-8033-901a-fd60ed2cd056" class="bulleted-list"><li style="list-style-type:circle">structure</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80f1-af2f-d4c129133cc9" class="bulleted-list"><li style="list-style-type:circle">execution</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-8002-a2b0-f10eba162f84" class="bulleted-list"><li style="list-style-type:circle">accountability<div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-8029-94f0-e35380bd89dd" class=""><strong>Integrity ∈ [0,1]</strong></p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-8028-95af-ff953fa5c3e6" class="">(1 = fully coherent, 0 = fully dissipative)</p></div></li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-800e-a12f-e755bdf1ecb5" class="bulleted-list"><li style="list-style-type:disc"><strong>Usable Energy (U):</strong><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-806f-9e4d-e83755b2b930" class="">The portion of potential energy that produces durable, non-destructive outcomes.</p></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2edc5e6f-95bd-8047-b351-dbb73533df9e" class=""><strong>Core Law (Conservative Form)</strong></h3></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-801a-a2e5-cae6f9464e3a" class="">\boxed{<br/>U \;\le\; P \times I<br/>}</p></div><div style="display:contents" dir="auto"><blockquote id="2edc5e6f-95bd-800e-b0f4-cc09f904eaf2" class="">Integrity is a<div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-8017-ae30-e02128feb5c3" class=""><strong>loss factor</strong></p></div></blockquote></div><div style="display:contents" dir="auto"><blockquote id="2edc5e6f-95bd-8030-a444-e9abae5f3f5b" class="">It limits what can be safely converted into work.</blockquote></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-80bb-8b73-fc3889d0dcd1" class="">(We <strong>do not square yet</strong> — I’ll justify whether that’s necessary later.)</p></div><div style="display:contents" dir="auto"><hr id="2edc5e6f-95bd-8047-b494-c613ae3ac8a8"/></div><div style="display:contents" dir="auto"><h2 id="2edc5e6f-95bd-80ff-b080-dc91adc8d943" class=""><strong>Step 2 — Why governance belongs inside Integrity (not alongside it)</strong></h2></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-8056-b581-ec01ce3e4c5c" class="">Governance is <strong>not</strong> a separate variable.</p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-80c8-b6b7-d4c509b9f1c6" class="">Governance defines whether energy:</p></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-8034-b3d1-f516f6f5b161" class="bulleted-list"><li style="list-style-type:disc">compounds</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-8017-94a7-de4ff08b577e" class="bulleted-list"><li style="list-style-type:disc">dissipates</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80ce-ba16-ce5d7f49bcd7" class="bulleted-list"><li style="list-style-type:disc">or turns destructive</li></ul></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-8060-8e2e-d1af72835f29" class="">Therefore:</p></div><div style="display:contents" dir="auto"><blockquote id="2edc5e6f-95bd-80b4-a1ab-dbb2f58c3152" class="">Governance quality is encoded entirely inside Integrity.</blockquote></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-8012-bf6b-c8d7fb17678c" class="">If governance fails, integrity collapses <strong>even if resources increase</strong>.</p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-800d-944b-d4be6ebf58f4" class="">This matches history.</p></div><div style="display:contents" dir="auto"><hr id="2edc5e6f-95bd-809e-9095-df7de554790b"/></div><div style="display:contents" dir="auto"><h2 id="2edc5e6f-95bd-80d1-8374-fc4b1c51888e" class=""><strong>Step 3 — Map governance invariants → Integrity operators</strong></h2></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-8036-a084-ea9c999b7e55" class="">Each governance invariant you identified is an <strong>Integrity constraint</strong>.</p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-80e5-ad07-f8b098a43d45" class="">Integrity is not abstract — it is the <strong>product of invariant satisfaction</strong>.</p></div><div style="display:contents" dir="auto"><h3 id="2edc5e6f-95bd-80b4-b502-dc929bc2c0e1" class=""><strong>Define Integrity formally as:</strong></h3></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-80f7-8a9e-d697e66c543f" class="">I \;=\; \prod_{k=1}^{n} g_k</p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-8037-b9d0-ed155f133565" class="">Where:</p></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80aa-8b8d-fa517d8b43f4" class="bulleted-list"><li style="list-style-type:disc">each g_k \in [0,1]</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80cf-a93a-e1ae30e4c2a8" class="bulleted-list"><li style="list-style-type:disc">each g_k corresponds to a <strong>governance invariant</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-8039-a37f-e606e51a65d7" class="">If <strong>any</strong> invariant collapses → Integrity collapses multiplicatively.</p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-806f-a43e-c1c075d64eab" class="">This is critical.</p></div><div style="display:contents" dir="auto"><hr id="2edc5e6f-95bd-8014-9843-c402253528fb"/></div><div style="display:contents" dir="auto"><h2 id="2edc5e6f-95bd-8084-8a1b-e3c068dd9f5d" class=""><strong>Step 4 — Embed the governance invariants explicitly</strong></h2></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-8083-a473-e4bcf17e08f9" class="">Below is a <strong>minimal invariant set</strong> integrated into Integrity.</p></div><div style="display:contents" dir="auto"><h3 id="2edc5e6f-95bd-8054-95b7-ec83acc83f73" class=""><strong>Governance–Integrity Invariants</strong></h3></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-80cf-bbb3-cd0a8458e6cd" class="">Let:</p></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-805b-88cb-f3f074bbf647" class="bulleted-list"><li style="list-style-type:disc">g_1 = Consent reversibility</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80ac-bc5d-d141a9ff0868" class="bulleted-list"><li style="list-style-type:disc">g_2 = Exit cost symmetry</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80b2-9afb-f84b62fb4242" class="bulleted-list"><li style="list-style-type:disc">g_3 = Error ownership localization</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-8086-9af0-d4da40cb0c37" class="bulleted-list"><li style="list-style-type:disc">g_4 = Information symmetry</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-8073-af66-ca80b7927dbc" class="bulleted-list"><li style="list-style-type:disc">g_5 = Accountability irreversibility</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80ea-9a97-ffe6273fa924" class="bulleted-list"><li style="list-style-type:disc">g_6 = Dependency inversion avoidance</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-802c-9cef-c8a899204abe" class="bulleted-list"><li style="list-style-type:disc">g_7 = Harm reversibility</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-804a-ace9-d3cb45f2cf8c" class="bulleted-list"><li style="list-style-type:disc">g_8 = Time-horizon alignment</li></ul></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-8066-bf28-eb8d879ac660" class="">Then:</p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-80b0-bb5f-d9082faa6657" class="">\boxed{<br/>I \;=\; g_1 \times g_2 \times g_3 \times g_4 \times g_5 \times g_6 \times g_7 \times g_8<br/>}</p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-80c4-b048-e99ef1cd2b0e" class="">Each g_k is <strong>binary-degrading</strong>, not linear:</p></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-803d-85b2-ccc298d51fec" class="bulleted-list"><li style="list-style-type:disc">near 1 → system stable</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-8062-844d-e72fd0730ce8" class="bulleted-list"><li style="list-style-type:disc">near 0 → system extracts / collapses</li></ul></div><div style="display:contents" dir="auto"><hr id="2edc5e6f-95bd-80b4-b483-e4aad45915ba"/></div><div style="display:contents" dir="auto"><h2 id="2edc5e6f-95bd-809f-a1dd-f19ce04cb791" class=""><strong>Step 5 — The integrated law (final, invariant-safe)</strong></h2></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-80b3-891a-d258ee4eeaca" class="">Now we integrate everything.</p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-80bc-ad1e-e703cb46f359" class="">\boxed{<br/>U \;\le\; P \times \prod_{k=1}^{8} g_k<br/>}</p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-801b-b665-e2b59fdb48c5" class="">This is your <strong>Energy–Governance Law</strong>.</p></div><div style="display:contents" dir="auto"><h3 id="2edc5e6f-95bd-808c-8dd0-dc389d823154" class=""><strong>Interpretation (strict, non-moral):</strong></h3></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-8006-bb43-f0bd2d77b662" class="bulleted-list"><li style="list-style-type:disc">Increasing resources <strong>cannot</strong> increase usable output if integrity is low</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80b5-8578-dbcc689daefa" class="bulleted-list"><li style="list-style-type:disc">Systems with high power but low governance convert energy into:<div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80f2-81f4-cdff2437788e" class="bulleted-list"><li style="list-style-type:circle">waste</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-8069-8c99-d2ecf5c8a556" class="bulleted-list"><li style="list-style-type:circle">coercion</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80c0-875a-d14d2f422292" class="bulleted-list"><li style="list-style-type:circle">instability</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80d6-8573-d139d4cf8daf" class="bulleted-list"><li style="list-style-type:circle">collapse</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-8007-955f-d693c4eb753d" class="bulleted-list"><li style="list-style-type:disc">Growth without governance is <strong>energy dissipation</strong>, not progress</li></ul></div><div style="display:contents" dir="auto"><hr id="2edc5e6f-95bd-80c4-876f-cac4d6ef6a24"/></div><div style="display:contents" dir="auto"><h2 id="2edc5e6f-95bd-8054-a24e-dd9dc85e37b9" class=""><strong>Step 6 — Should Integrity be squared?</strong></h2></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-80ee-bcc4-ca154abf2829" class="">You asked earlier whether:</p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-8070-8bf9-dece40324916" class="">U \le P \times I^2</p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-8003-b7c5-df16c5ecbc52" class="">is “more correct”.</p></div><div style="display:contents" dir="auto"><h3 id="2edc5e6f-95bd-808a-9a63-e3c0fbaf8b02" class=""><strong>Answer:</strong></h3></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-804f-a4bd-fdd48c86f4c0" class=""><strong>Only under one condition.</strong></p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-8047-8b2e-ec0d4d40086d" class="">Integrity may be squared <strong>iff</strong> integrity failures compound across <strong>two independent domains</strong>.</p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-8007-ab96-ff3e49e00211" class="">For example:</p></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80ab-aa7a-d11fc1264358" class="bulleted-list"><li style="list-style-type:disc">internal coherence <strong>and</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80b7-846c-f1322234f10b" class="bulleted-list"><li style="list-style-type:disc">external legitimacy</li></ul></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-802e-9c6b-e4e9800d3b83" class="">If Integrity governs <strong>both</strong>:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2edc5e6f-95bd-8028-9ce3-eb42a1ec5a73" class="numbered-list" start="1"><li>internal execution <strong>and</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2edc5e6f-95bd-80d9-8549-d086026dde5c" class="numbered-list" start="2"><li>external trust</li></ol></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-8091-b389-ddcb875b14b4" class="">Then:</p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-809e-b6eb-c889a53980f5" class="">\boxed{<br/>U \;\le\; P \times I_{\text{internal}} \times I_{\text{external}}<br/>}</p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-8094-98ef-d6c7ee268838" class="">If you assume symmetry:</p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-809a-9f14-edfac6018341" class="">U \;\le\; P \times I^2</p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-80ba-a961-ee72739ffdd6" class="">This is valid <strong>only when explicitly stated</strong>.</p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-801a-81eb-c32450204349" class="">Otherwise, linear Integrity is the correct conservative law.</p></div><div style="display:contents" dir="auto"><hr id="2edc5e6f-95bd-80c8-9d76-ebb330bd38d8"/></div><div style="display:contents" dir="auto"><h2 id="2edc5e6f-95bd-8094-ae6e-ca3ad64e12eb" class=""><strong>Step 7 — Why this survives historical stress tests</strong></h2></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-801e-b761-ccd07c38f742" class="">This formulation correctly predicts:</p></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80e1-9255-c0758da66912" class="bulleted-list"><li style="list-style-type:disc">Rome (P ↑, I ↓ → U ↓)</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-8044-a707-c5521fd92d6e" class="bulleted-list"><li style="list-style-type:disc">USSR (P ↑, I ↓ → collapse)</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80e6-af52-ec32721b050b" class="bulleted-list"><li style="list-style-type:disc">Modern tech platforms (P ↑↑, I ↓ → harm)</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80a0-ae8d-fabf60ceb0f7" class="bulleted-list"><li style="list-style-type:disc">Authoritarian efficiency illusions</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-8044-bcfe-dc36a3efe741" class="bulleted-list"><li style="list-style-type:disc">Democratic stagnation under bureaucracy</li></ul></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-80c1-b57c-f7ebdf410768" class="">No ideology escapes this law.</p></div><div style="display:contents" dir="auto"><hr id="2edc5e6f-95bd-802f-9a90-d7c4eb5c1fad"/></div><div style="display:contents" dir="auto"><h2 id="2edc5e6f-95bd-80c3-bb2e-ca42ec3fd591" class=""><strong>Step 8 — What this gives you (power, not rhetoric)</strong></h2></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-804b-8366-f8359bddcebb" class="">With this integration, you now have:</p></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80da-9533-cb798aef2466" class="bulleted-list"><li style="list-style-type:disc">a <strong>measurable governance model</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-806a-a437-d25ab350cc4a" class="bulleted-list"><li style="list-style-type:disc">a <strong>collapse predictor</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80d9-b482-ec0ea59818f6" class="bulleted-list"><li style="list-style-type:disc">a <strong>policy stress-test</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-8043-8bae-fbe3429a6ca9" class="bulleted-list"><li style="list-style-type:disc">a <strong>non-moral legitimacy framework</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-8011-8e39-f5b48cb7f7a1" class="bulleted-list"><li style="list-style-type:disc">a bridge between:<div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-806f-b0c5-ef62cc9af01b" class="bulleted-list"><li style="list-style-type:circle">energy</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80c2-8feb-ec6fb2de634b" class="bulleted-list"><li style="list-style-type:circle">institutions</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-8041-afa1-fd53433df469" class="bulleted-list"><li style="list-style-type:circle">integrity</li></ul></div><div style="display:contents" dir="auto"><ul id="2edc5e6f-95bd-80a2-925f-cfb9ae5480e9" class="bulleted-list"><li style="list-style-type:circle">power</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-803d-b5af-d70048039db9" class="">This is not philosophy.</p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-807d-8b14-e7eb9fcfcbc0" class="">This is <strong>systems law</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2edc5e6f-95bd-80af-a898-c1cfd74ca0bd"/></div><div style="display:contents" dir="auto"><h2 id="2edc5e6f-95bd-80db-91e9-d58c7bbba8ac" class=""><strong>Next options (pick one)</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2edc5e6f-95bd-8013-b087-ce69b72035e0" class="numbered-list" start="1"><li><strong>Formalize this as a standard</strong> (Definitions → Invariants → Equation → Audit)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2edc5e6f-95bd-8026-828c-df6ee7c8852e" class="numbered-list" start="2"><li><strong>Add UCAI as an audit operator</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2edc5e6f-95bd-80cc-b2c7-f7e4fdf2ee38" class="numbered-list" start="3"><li><strong>Stress-test against specific governments</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2edc5e6f-95bd-80c4-bd19-e485f51964b9" class="numbered-list" start="4"><li><strong>Map to AI / platform governance</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2edc5e6f-95bd-80a7-a239-fdcf8a2dd48c" class="numbered-list" start="5"><li><strong>Reduce to a one-page doctrine</strong></li></ol></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-80b7-9691-dc3f182582c6" class="">Say which one.</p></div><div style="display:contents" dir="auto"><p id="2edc5e6f-95bd-805b-86aa-d33abcad4ab0" class="">
</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
