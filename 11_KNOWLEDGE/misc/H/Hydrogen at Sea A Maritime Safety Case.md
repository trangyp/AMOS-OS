---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Hydrogen at Sea: A Maritime Safety Case</title><style>
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
	
</style></head><body><article id="2e4c5e6f-95bd-80f6-aed7-cf6d8f52f912" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Hydrogen at Sea: A Maritime Safety Case</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8021-b487-e4946ff58464" class=""><strong>Why Hydrogen Is Emerging as the Safest Energy Vector in High-Risk Maritime Environments</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80c0-80bd-f2679e4136e0" class=""><strong>Executive Thesis</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800a-905a-f82300bf8257" class="">Maritime safety is not constrained by fuel efficiency.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8038-b47c-dc5c9453349f" class="">It is constrained by <strong>fire behavior, smoke toxicity, detectability, evacuation delay, and governance</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80fb-8106-d8ae2962da4d" class="">In this context, hydrogen is not being adopted <em>despite</em> its risks —</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8055-81c3-ee441a105645" class="">it is being adopted <strong>because its risks are more governable</strong> than incumbent marine fuels.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8097-88a0-ea80f7a6f7cd" class="">This article explains why.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-805b-897d-e579eff468d6"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8030-acea-eb7172ecd057" class=""><strong>1. The Maritime Safety Reality (Baseline)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b1-9cf1-d79da4ea8dc7" class="">Shipping is one of the most unforgiving operating environments on Earth.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8086-8d21-f51362862f53" class="">Structural facts (IMO, EMSA, IHS casualty analyses):</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80bd-a5b7-c73d340c4ecf" class="bulleted-list"><li style="list-style-type:disc">~<strong>55–65% of shipboard fires originate in engine or fuel-handling spaces</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8097-9c1b-e9d676cd92f5" class="bulleted-list"><li style="list-style-type:disc">Fire is among the <strong>top three causes of total vessel loss</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806d-861b-c0fc629cf506" class="bulleted-list"><li style="list-style-type:disc">At sea, <strong>external emergency response is delayed or unavailable</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e0-a6c3-ce4143ca97ad" class="bulleted-list"><li style="list-style-type:disc">Smoke inhalation is the <strong>primary cause of crew fatalities</strong>, not burns</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c7-84f2-de5dd1b4c93f" class="bulleted-list"><li style="list-style-type:disc">Confined spaces + fuel pooling = escalation, not containment</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f3-8147-c580c6bd7b5c" class="">Key maritime truth:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8031-a559-fae926dc3291" class="">A small fire at sea is more dangerous than a large fire on land.</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80cb-9015-f210c2402fd8" class="">This is why fuel choice is a safety decision first, an energy decision second.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-801e-8e7b-c9c05bd87ebc"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8010-8488-fd5acbb48110" class=""><strong>2. Why Incumbent Marine Fuels Are Structurally Dangerous</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80a1-a6f0-e3370aef0b78" class=""><strong>2.1 Heavy Fuel Oil &amp; Marine Diesel</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8075-838d-fb55381374cd" class=""><strong>Primary risks:</strong></p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d6-b9bc-fb126bccfbcf" class="bulleted-list"><li style="list-style-type:disc">High energy density</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-808f-90be-f18a88959af2" class="bulleted-list"><li style="list-style-type:disc">Liquid pooling in bilges</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8087-8fd5-f6108042a0ec" class="bulleted-list"><li style="list-style-type:disc">Persistent combustion</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8010-8da8-c075f1c9ef72" class="bulleted-list"><li style="list-style-type:disc">Thick, toxic smoke (CO, particulates)</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f7-a868-fa5f59ac2fae" class="">Failure mode:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8074-b4ed-c3917b652dbf" class="bulleted-list"><li style="list-style-type:disc">Fires spread laterally</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d7-beb3-de648a0802b1" class="bulleted-list"><li style="list-style-type:disc">Smoke fills compartments</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-803d-a00d-f24651d415fc" class="bulleted-list"><li style="list-style-type:disc">Fire suppression is prolonged</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f3-83e5-edc2e3a57573" class="bulleted-list"><li style="list-style-type:disc">Visibility collapses before heat does</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a5-8e89-e285fcefbd71" class="">Statistically:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8090-b2c4-f381fb22da53" class="">Diesel-related fires account for a majority of engine-room incidents.</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8093-9871-d0a3085fd04f" class="">Diesel is “familiar,” not safe.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80ad-8cf3-d79a4784a06d"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80a5-b08c-cc4eeb694318" class=""><strong>2.2 LNG (Liquefied Natural Gas)</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8055-a338-cb8821463cb8" class="">LNG improves emissions but introduces new hazards:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-809d-9ac9-f71e5a89b676" class="bulleted-list"><li style="list-style-type:disc">Cryogenic burns</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e3-b1f2-ca671f8a537d" class="bulleted-list"><li style="list-style-type:disc">Gas accumulation in enclosed spaces</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ba-be56-fd0d7106034d" class="bulleted-list"><li style="list-style-type:disc">Explosion risk if ignition occurs after pooling</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8027-89dd-f33d685528ca" class="bulleted-list"><li style="list-style-type:disc">Asphyxiation risk (oxygen displacement)</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8098-9ea5-e9c0062cd206" class="">LNG’s safety depends heavily on <strong>perfect ventilation discipline</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-804d-856a-ecdc3c9d2f8f" class="">At sea, perfection is rare.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8020-ae44-c924232da8a3"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80b9-9b83-ebff921a7ed1" class=""><strong>2.3 Battery-Only Systems (Maritime Context)</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d7-b79d-f63b854f852f" class="">Lithium-ion systems introduce:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ac-9d46-c1307841e7d3" class="bulleted-list"><li style="list-style-type:disc">Thermal runaway</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8015-b79d-fbb48ee85260" class="bulleted-list"><li style="list-style-type:disc">Self-propagating fires</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8030-b55c-eb8b836d3e74" class="bulleted-list"><li style="list-style-type:disc">Toxic off-gassing (HF, CO)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8021-b592-e92d2ab827c3" class="bulleted-list"><li style="list-style-type:disc">Difficult fire suppression (water re-ignition risk)</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8016-8b3b-f10554b76430" class="">Multiple ferry and vessel incidents have shown:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8001-8604-e199ffd51d72" class="">Battery fires are<div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8013-977a-e3316d64ea49" class=""><strong>harder to extinguish</strong></p></div></blockquote></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80ff-8577-d97a010abf86"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80d1-8b6f-e9a6660d0402" class=""><strong>3. Hydrogen’s Physical Safety Properties (Not Marketing Claims)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8013-8a0e-c798f52f75c7" class="">Hydrogen is not “safe” by default.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f8-90fe-eff448257ac5" class="">It is <strong>predictable</strong> — and predictability is the foundation of maritime safety.</p></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80b8-b9ab-fddb88c57dd2" class=""><strong>3.1 Dispersion Behavior (Critical at Sea)</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-804e-b7d5-fad3ac0b3208" class="bulleted-list"><li style="list-style-type:disc">Hydrogen is <strong>~14× lighter than air</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ed-9741-f90b147259ba" class="bulleted-list"><li style="list-style-type:disc">In open or semi-open marine environments:<div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b4-80f9-db0b4ae33631" class="bulleted-list"><li style="list-style-type:circle">it rises</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-805c-844a-df3339c855ac" class="bulleted-list"><li style="list-style-type:circle">it disperses vertically</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8084-820d-d27622c6bf96" class="bulleted-list"><li style="list-style-type:circle">it does not pool in bilges or decks</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8070-9059-d24cd10b6439" class="">Contrast:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80cd-af99-e5ea37e1ab8a" class="bulleted-list"><li style="list-style-type:disc">Diesel vapor, LNG, and fuel mist <strong>accumulate</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d8-87f0-c0dff204b995" class="bulleted-list"><li style="list-style-type:disc">Accumulation is what turns leaks into disasters</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80e7-a00f-ea07b6b3a1f5" class="">At sea, dispersion saves lives.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-805d-98c8-db56cb28b2f4"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80c2-98d3-ed43d55bca22" class=""><strong>3.2 Flame &amp; Smoke Characteristics</strong></h3></div><div style="display:contents" dir="ltr"><table id="2e4c5e6f-95bd-8021-8d1c-c667aa50c78e" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2e4c5e6f-95bd-803f-b06c-c0c47432489f"><th id="xue]" class="simple-table-header-color simple-table-header"><strong>Property</strong></th><th id="uNYn" class="simple-table-header-color simple-table-header"><strong>Diesel</strong></th><th id="kmY~" class="simple-table-header-color simple-table-header"><strong>LNG</strong></th><th id="Nkc;" class="simple-table-header-color simple-table-header"><strong>Batteries</strong></th><th id="y?o_" class="simple-table-header-color simple-table-header"><strong>Hydrogen</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2e4c5e6f-95bd-8019-8353-f1443a47b053"><td id="xue]" class="">Smoke</td><td id="uNYn" class="">Heavy</td><td id="kmY~" class="">Moderate</td><td id="Nkc;" class="">Toxic</td><td id="y?o_" class=""><strong>None</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2e4c5e6f-95bd-80fc-99e3-c9331b6e5a04"><td id="xue]" class="">CO production</td><td id="uNYn" class="">High</td><td id="kmY~" class="">Moderate</td><td id="Nkc;" class="">High</td><td id="y?o_" class=""><strong>Zero</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2e4c5e6f-95bd-802b-9ff5-c2a349c4fad0"><td id="xue]" class="">Flame persistence</td><td id="uNYn" class="">Long</td><td id="kmY~" class="">Medium</td><td id="Nkc;" class="">Long</td><td id="y?o_" class=""><strong>Short</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="2e4c5e6f-95bd-80f0-b4ed-cdcf4febead3"><td id="xue]" class="">Visibility loss</td><td id="uNYn" class="">Severe</td><td id="kmY~" class="">Moderate</td><td id="Nkc;" class="">Severe</td><td id="y?o_" class=""><strong>Minimal</strong></td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8078-85e8-ffdbcffcf49e" class="">Maritime insight:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8063-a28a-cf395272079f" class="">Smoke incapacitates crews before fire does.</blockquote></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8004-91f8-da46b0ec91fc" class="">Hydrogen produces no smoke.</blockquote></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8038-9436-e61e1cd20b3b"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-8012-896c-d69d3b7c1dbf" class=""><strong>3.3 Detectability</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-801d-9b1a-e0f5bd66fccb" class="">Hydrogen is <strong>easy to detect</strong>:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8095-9d3f-c3043149a744" class="bulleted-list"><li style="list-style-type:disc">Dedicated sensors respond in milliseconds</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8075-b69c-f0d74f079337" class="bulleted-list"><li style="list-style-type:disc">Leak thresholds are well below flammability limits</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-805d-b2a7-e393c9e0823d" class="bulleted-list"><li style="list-style-type:disc">Detection forces system shutdown</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8055-a43d-fcc61e55193c" class="">Diesel leaks often go unnoticed.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8018-bf41-e222b5a43978" class="">LNG leaks can be odorless in confined spaces.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803e-be77-c245d75fc005" class="">Battery failures are often detected <strong>after ignition</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-807d-8b90-fba2550d013d" class="">Hydrogen fails loudly — which is safer.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8091-ac78-f566fee5838d"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8088-a988-c3ba575045cb" class=""><strong>4. Fire Behavior: Containment vs Escalation</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-8039-bf8f-eb07f3089e75" class=""><strong>Hydrogen fires:</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8074-8195-c467f2ee9baa" class="bulleted-list"><li style="list-style-type:disc">Burn upward</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b9-be3c-d3f4009f937f" class="bulleted-list"><li style="list-style-type:disc">Do not spread laterally</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8079-911f-ceb783cce42c" class="bulleted-list"><li style="list-style-type:disc">Do not generate secondary fuel pools</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806e-a3c6-d80b4a0a8a3c" class="bulleted-list"><li style="list-style-type:disc">Self-limit if supply is cut</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-8055-96cd-eddf620b3e03" class=""><strong>Hydrocarbon fires:</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8040-93e5-e408b0a4a74e" class="bulleted-list"><li style="list-style-type:disc">Spread across surfaces</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8088-b8bd-e0a4d10a02dc" class="bulleted-list"><li style="list-style-type:disc">Reignite from residual fuel</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8068-a85e-c2170972b087" class="bulleted-list"><li style="list-style-type:disc">Produce cascading ignition points</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8078-abca-e365949e9f1c" class="">This difference matters enormously on ships.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80a9-bf51-f99488ea6708"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-803f-995f-dcdf2fe40d24" class=""><strong>5. Governance: Why Hydrogen Forces Better Safety</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-801d-bf92-f7b6ca933154" class="">Hydrogen cannot be handled casually.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-807c-a2af-e2d666350273" class="">It requires:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ed-b893-f6764ce64ccc" class="bulleted-list"><li style="list-style-type:disc">continuous monitoring</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8078-85f4-c07f36a4a7cd" class="bulleted-list"><li style="list-style-type:disc">certified containment</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e2-8f3b-d6b51c8d8533" class="bulleted-list"><li style="list-style-type:disc">automated shutdown</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d1-97e7-fb05b38e6153" class="bulleted-list"><li style="list-style-type:disc">ventilation interlocks</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a8-8993-faea3201a50a" class="bulleted-list"><li style="list-style-type:disc">documented operating envelopes</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80da-a2f3-de423b6f1c72" class="">This is not a weakness.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8085-91d3-f6ad437e31bf" class="">It is <strong>institutionalized discipline</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d2-904f-fd895d3fd092" class="">Most maritime disasters are not chemical failures —</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80dd-a004-f7b491a013c9" class="">they are <strong>governance failures</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d0-8761-f1e0c6f41d07" class="">Hydrogen makes governance unavoidable.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8063-b584-e9ba1ee9e345"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-805e-9e3a-c9b63702c45b" class=""><strong>6. The Real Safety Metric: Failure Transparency</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-801e-85a0-e7d9d9c12b1a" class="">The safest maritime systems share one trait:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-80e3-830a-ea136644a063" class="">They make unsafe states impossible to ignore.</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f6-842c-d6e482f77fe6" class="">Hydrogen:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e4-9b67-ca7ada9b8928" class="bulleted-list"><li style="list-style-type:disc">exposes leaks immediately</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ee-8023-f5673da179d3" class="bulleted-list"><li style="list-style-type:disc">triggers alarms</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f3-8f4e-caba16fbbb32" class="bulleted-list"><li style="list-style-type:disc">forces shutdown</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b2-8a03-cccad2cbd233" class="bulleted-list"><li style="list-style-type:disc">prevents silent degradation</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8079-a557-db5a82b33ae5" class="">Diesel:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8040-a958-de220cbc8888" class="bulleted-list"><li style="list-style-type:disc">leaks quietly</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8060-82be-fa6aa4fd18f5" class="bulleted-list"><li style="list-style-type:disc">accumulates residue</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ac-a233-c699f98234d2" class="bulleted-list"><li style="list-style-type:disc">degrades slowly</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8087-9767-c13e17548cea" class="bulleted-list"><li style="list-style-type:disc">fails catastrophically later</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-808f-871e-f634fb042522" class="">Safety favors visibility.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8094-a0a2-f22af4d785ff"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8033-b335-fc10e8f03a96" class=""><strong>7. Regulatory Momentum (Signal, Not Hype)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-802c-b626-e129ebb6e712" class="">Global maritime authorities are converging on hydrogen not for novelty, but control:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8070-b4f9-dd0a47323fb7" class="bulleted-list"><li style="list-style-type:disc">IMO: hydrogen included in alternative fuel safety codes</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a1-9bc6-c1442eda423b" class="bulleted-list"><li style="list-style-type:disc">Class societies (DNV, ABS, LR): hydrogen-specific safety frameworks</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8005-8a4a-fb5607d6a053" class="bulleted-list"><li style="list-style-type:disc">Port authorities: hydrogen favored for zero-smoke operations</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8072-a2db-cce17fe4b164" class="bulleted-list"><li style="list-style-type:disc">Naval programs: hydrogen evaluated for survivability, not efficiency</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8059-9c4d-ca7bc3773a33" class="">Regulators follow safety physics, not trends.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-807b-b612-d6481d56fcc2"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8019-9a98-f4f0af7524e3" class=""><strong>8. The Misconception That Slows Adoption</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8068-bd1c-da3a60d39f56" class="">The dominant misconception:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8070-b230-fd44777c4a34" class="">“Hydrogen is dangerous.”</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80fb-950e-d218b18aec17" class="">The accurate statement:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8058-a8cf-d77aee8b8460" class="">Unmanaged energy is dangerous.</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8016-885a-f60d9c8b74e8" class="">Hydrogen’s danger is explicit.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d7-b896-cdeaad34ccbf" class="">Diesel’s danger is normalized.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800a-bb2b-d43ab0701871" class="">Batteries’ danger is misunderstood.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8041-ae6d-ef9943802a95" class="">Maritime history shows:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-80a9-b0ab-dc1c1b31e58d" class="">Normalized danger kills more people than feared danger.</blockquote></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80ad-843d-e842774a34e1"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-802d-ba1a-ff8cadb665d7" class=""><strong>9. Hydrogen as a Maritime Endgame (Not a Silver Bullet)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8056-8fa2-c69a4c2f0807" class="">Hydrogen is not a universal replacement.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8030-bcaf-e96ec35f27fc" class="">But it is uniquely suited for:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80da-ae26-d115e750a82f" class="bulleted-list"><li style="list-style-type:disc">vessels with delayed evacuation</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a5-9aea-d400ddd1d278" class="bulleted-list"><li style="list-style-type:disc">crewed systems where smoke is fatal</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8075-a99a-cfcda77d8068" class="bulleted-list"><li style="list-style-type:disc">ships operating near ports or coasts</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f5-b63f-e52e7740a824" class="bulleted-list"><li style="list-style-type:disc">applications where safety dominates efficiency</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800a-a05a-fbecfa7c5a60" class="">In maritime environments, <strong>governability beats convenience</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-803d-86b4-decdfac6bbd3"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80bf-bf88-c42946417502" class=""><strong>10. Final Position</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8024-955f-ce2229ad6a2a" class="">Maritime safety is not about choosing the least powerful energy source.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8056-bb59-ed2f1bdbaf73" class="">It is about choosing the energy source whose failure modes:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8053-86e1-e752b4ac696b" class="bulleted-list"><li style="list-style-type:disc">are visible</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c5-8f76-d0c31bdb696e" class="bulleted-list"><li style="list-style-type:disc">are detectable</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8077-b26d-c26210a7c9e1" class="bulleted-list"><li style="list-style-type:disc">are interruptible</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a3-b9be-e9348b85a46c" class="bulleted-list"><li style="list-style-type:disc">do not produce toxic smoke</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8054-b82b-d8d155d41e5c" class="bulleted-list"><li style="list-style-type:disc">do not accumulate invisibly</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80eb-b3c1-db1f8e06dd7d" class="bulleted-list"><li style="list-style-type:disc">force accountability</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c4-9eef-ce0a603fd0f4" class="">By these criteria, hydrogen is not the most dangerous fuel at sea.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-802d-9739-e245ace0ebee" class="">It is one of the most governable.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-805f-b35b-d95391ccbb97" class="">And at sea, governance is survival.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
