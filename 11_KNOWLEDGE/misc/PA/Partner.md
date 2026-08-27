---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Partner</title><style>
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
	
</style></head><body><article id="2a5c5e6f-95bd-8064-8512-e778528a482e" class="page sans"><header><h1 class="page-title" dir="auto">Partner</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-8040-a711-d1063ea8d64a"/></div><div style="display:contents" dir="auto"><h2 id="2a5c5e6f-95bd-8062-99b0-d2566777e103" class="">🇪🇺 <strong>1. Bolt (Estonia – Top Priority)</strong></h2></div><div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-8060-81fe-f256bfbce089" class="">✅ Already discussed — best match in structure, culture, and speed.</p></div><div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-8023-add7-f81b42765ee0" class="">They have capital, clean brand, and expansion appetite.</p></div><div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-8097-ad10-de237ae14111" class=""><strong>UniPower = instant EV network + compliance + local credibility.</strong></p></div><div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-807d-a134-f4c83157df18" class="">→ <em>Still the #1 strategic fit globally.</em></p></div><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-8093-a97d-d62a99da95d7"/></div><div style="display:contents" dir="auto"><h2 id="2a5c5e6f-95bd-80e3-a6a0-f5ea078c3c68" class="">🇫🇷 <strong>2. BlaBlaCar / BlaBlaMove</strong></h2></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-8011-b6f5-e6153d1e36d3" class="bulleted-list"><li style="list-style-type:disc">Active in Europe, expanding into Asia for <em>shared mobility and carpool EV</em> models.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-801f-b015-c4f5c9d187df" class="bulleted-list"><li style="list-style-type:disc">Looking for partners with <em>fleet management + data compliance</em>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-808f-a027-d1a3dcd0fc1f" class="bulleted-list"><li style="list-style-type:disc">Vietnam fits their “high-density, under-supplied” mobility profile.<br/>→ <em>You could position UniPower as their exclusive entry platform (fleet, energy, compliance).</em></li></ul></div><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-809b-8eb7-d2c730e1f5e9"/></div><div style="display:contents" dir="auto"><h2 id="2a5c5e6f-95bd-80aa-a3a4-c13edcea9585" class="">🇨🇳 <strong>3. DiDi Global (China)</strong></h2></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-8054-92d0-e9751ec650cc" class="bulleted-list"><li style="list-style-type:disc">Pulled back from SEA after Grab dominance, but <strong>quietly exploring re-entry via EV focus</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-806e-be68-de3a00801707" class="bulleted-list"><li style="list-style-type:disc">Backed by BYD and other Chinese OEMs with surplus EVs they want to export.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-80ec-a907-f77a5909235f" class="bulleted-list"><li style="list-style-type:disc"><strong>UniPower’s EV + charging infra</strong> gives them ready deployment + local face.<br/>→ <em>High potential if approached through EV or OEM lens, not as ride-hailing competitor.</em></li></ul></div><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-804c-8ac9-fb606fbfff57"/></div><div style="display:contents" dir="auto"><h2 id="2a5c5e6f-95bd-8013-a83e-cc7055f2dbbd" class="">🇮🇳 <strong>4. Ola Electric (India)</strong></h2></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-8040-901a-e1785e501039" class="bulleted-list"><li style="list-style-type:disc">Expanding internationally; publicly announced <strong>SEA expansion plans starting 2026–2027</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-8001-a56e-c328fe49cfd0" class="bulleted-list"><li style="list-style-type:disc">Building both <strong>ride-hailing and EV manufacturing ecosystem</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-8003-8e1a-da13907dadc1" class="bulleted-list"><li style="list-style-type:disc">Will need <strong>charging and local fleet partners</strong> to deploy outside India.<br/>→ <em>You can be their Vietnam + Indochina anchor.</em></li></ul></div><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-803d-ae2d-c902c2b18e0b"/></div><div style="display:contents" dir="auto"><h2 id="2a5c5e6f-95bd-8000-aa14-c6e45249fb21" class="">🇸🇬 <strong>5. Ryde (Singapore)</strong></h2></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-80cb-955d-f8cd8189a471" class="bulleted-list"><li style="list-style-type:disc">Smaller but ambitious; currently in Singapore and Malaysia.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-8017-9e57-efb99ba77f31" class="bulleted-list"><li style="list-style-type:disc">Looking for <strong>low-cost regional partners</strong> with EV or green credentials.<br/>→ <em>UniPower can provide full operational + data compliance support.</em></li></ul></div><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-804b-bfcb-fffdfbd5b242"/></div><div style="display:contents" dir="auto"><h2 id="2a5c5e6f-95bd-8024-aab2-d1660ea128d2" class="">🇩🇪 <strong>6. Tier Mobility / FreeNow (Europe)</strong></h2></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-8054-8772-d1c723503bef" class="bulleted-list"><li style="list-style-type:disc">EV scooter &amp; micro-mobility companies expanding beyond Europe.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-80a0-925e-d71d47a98c38" class="bulleted-list"><li style="list-style-type:disc">Need <strong>charging base + energy operator</strong> for multi-modal expansion in developing cities.<br/>→ <em>UniPower can host Tier’s infrastructure for EV micro fleets.</em></li></ul></div><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-80c0-947a-c3968bf8dd64"/></div><div style="display:contents" dir="auto"><h2 id="2a5c5e6f-95bd-80e1-ac7b-e6fc1d4069f8" class="">🇰🇷 <strong>7. Kakao Mobility (Korea)</strong></h2></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-8083-a94f-e595c54ea0ff" class="bulleted-list"><li style="list-style-type:disc">Exploring Southeast Asia expansion via JV models (especially EV-based).</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-809c-9142-deaae28aef77" class="bulleted-list"><li style="list-style-type:disc">Strong capital base, but requires <strong>local partner with licences &amp; fleet</strong>.<br/>→ <em>Could form “Kakao × UniPower Vietnam” JV focused on EV taxis &amp; smart dispatch.</em></li></ul></div><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-808c-86aa-d6ae7e5e5a1b"/></div><div style="display:contents" dir="auto"><h2 id="2a5c5e6f-95bd-80f8-b8a3-dd117531d209" class="">🇺🇸 <strong>8. Uber (re-entry pathway)</strong></h2></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-80fe-8b9e-e56a36423a18" class="bulleted-list"><li style="list-style-type:disc">After selling to Grab in 2018, <strong>Uber has considered selective re-entry in regulated markets</strong> under EV/ESG narratives.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-8012-a746-c0d7d83d39a3" class="bulleted-list"><li style="list-style-type:disc"><strong>Vietnam’s EV transformation</strong> + UniPower’s compliance shield could make this viable.<br/>→ <em>Position: “Uber Green powered by UniPower.”</em></li></ul></div><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-80a0-b791-eebf58763a46"/></div><div style="display:contents" dir="auto"><h2 id="2a5c5e6f-95bd-80f4-a96b-c3e4dac341e8" class="">🇯🇵 <strong>9. SoftBank-backed logistics &amp; mobility ventures</strong></h2></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-8048-ab88-f034a7c51f05" class="bulleted-list"><li style="list-style-type:disc">SoftBank Vision Fund is reinvesting in <strong>clean mobility &amp; data-driven fleet models</strong> (e.g., in India, Indonesia).</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-8002-ab44-e0bcc56a3cae" class="bulleted-list"><li style="list-style-type:disc">They <strong>prefer local execution partners</strong> with scalable, ESG-verified infra.<br/>→ <em>UniPower fits as a ready operator for their next SEA move.</em></li></ul></div><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-80c6-8405-e95d8002c231"/></div><div style="display:contents" dir="auto"><h2 id="2a5c5e6f-95bd-8019-bf7d-e4b19139fa9c" class="">🟢 <strong>Summary – Tier 1 Partners (High Potential)</strong></h2></div><div style="display:contents" dir="ltr"><table id="2a5c5e6f-95bd-8036-a1ae-c5dbc3f73afd" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2a5c5e6f-95bd-8095-884a-d3f9eb5f8e49"><th id="Rjmk" class="simple-table-header-color simple-table-header" style="width:58px">Tier</th><th id="t}qF" class="simple-table-header-color simple-table-header">Partner</th><th id="ntM&gt;" class="simple-table-header-color simple-table-header">Type</th><th id="cZQ;" class="simple-table-header-color simple-table-header">Why They Fit</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2a5c5e6f-95bd-805b-a9a3-d807a8d5b9aa"><td id="Rjmk" class="" style="width:58px">1</td><td id="t}qF" class=""><strong>Bolt (Estonia)</strong></td><td id="ntM&gt;" class="">Ride-hailing</td><td id="cZQ;" class="">Cultural + operational fit; fast decision cycles</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a5c5e6f-95bd-80f4-9e41-ca51a6f2fd34"><td id="Rjmk" class="" style="width:58px">1</td><td id="t}qF" class=""><strong>Ola Electric (India)</strong></td><td id="ntM&gt;" class="">EV + Ride</td><td id="cZQ;" class="">Wants SEA base; UniPower offers full infra</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a5c5e6f-95bd-80b5-bd53-f6d35aef401b"><td id="Rjmk" class="" style="width:58px">1</td><td id="t}qF" class=""><strong>Kakao Mobility (Korea)</strong></td><td id="ntM&gt;" class="">EV Ride + Data</td><td id="cZQ;" class="">Needs regulated entry + local ops partner</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a5c5e6f-95bd-80cc-84ed-fcb1b465a895"><td id="Rjmk" class="" style="width:58px">1</td><td id="t}qF" class=""><strong>DiDi Global (China)</strong></td><td id="ntM&gt;" class="">EV + Fleet</td><td id="cZQ;" class="">Needs face and infra to re-enter SEA</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a5c5e6f-95bd-8010-9717-dff4786d8d38"><td id="Rjmk" class="" style="width:58px">2</td><td id="t}qF" class=""><strong>BlaBlaCar (France)</strong></td><td id="ntM&gt;" class="">Shared mobility</td><td id="cZQ;" class="">Low competition, clean ESG positioning</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a5c5e6f-95bd-80cc-87a1-db2aff9ad6ba"><td id="Rjmk" class="" style="width:58px">2</td><td id="t}qF" class=""><strong>Tier Mobility / FreeNow (Europe)</strong></td><td id="ntM&gt;" class="">Micro-mobility</td><td id="cZQ;" class="">Needs host infra for scooters/EVs</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a5c5e6f-95bd-805e-b70c-e78bc64deb38"><td id="Rjmk" class="" style="width:58px">2</td><td id="t}qF" class=""><strong>SoftBank Mobility Ventures</strong></td><td id="ntM&gt;" class="">Investor-operator</td><td id="cZQ;" class="">Could fund expansion + JV with UniPower</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-8059-a29e-ebe97ec2240a"/></div><div style="display:contents" dir="auto"><h3 id="2a5c5e6f-95bd-80d8-b73e-dbf3e890c03f" class="">🔍 <strong>Strategic insight</strong></h3></div><div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-8059-ac08-e7a590ab9b14" class="">You sit in the <strong>sweet spot of three global trends</strong>:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2a5c5e6f-95bd-800a-8e32-e896642f9578" class="numbered-list" start="1"><li><strong>EV-first ride-hailing</strong> (Bolt, Ola, DiDi).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2a5c5e6f-95bd-80e0-9def-cab68ab1e462" class="numbered-list" start="2"><li><strong>Compliance-led market entry</strong> (Kakao, SoftBank-backed startups).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2a5c5e6f-95bd-80b9-858a-fe4fd51d87f8" class="numbered-list" start="3"><li><strong>Green mobility + ESG branding</strong> (BlaBlaCar, Tier, Uber Green).</li></ol></div><div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-805d-a946-feab13c2bcdf" class="">None of them can operate in Vietnam <strong>without a local infrastructure and data partner</strong> — which is exactly what UniPower is.</p></div><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-80fa-b211-cb99901c9d99"/></div><div style="display:contents" dir="auto"><h1 id="2a5c5e6f-95bd-8027-a32e-c05bc1e3f3a9" class=""><strong>1) Nền tảng e-commerce logistics &amp; sorting hubs</strong></h1></div><div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-8074-98c8-faae5549ed95" class=""><strong>Tại sao hợp tác:</strong> họ cần <strong>điện hoá chặng cuối</strong>, giảm chi phí năng lượng, và đáp ứng KPI ESG.</p></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-80c2-8027-f093739eb5a2" class="bulleted-list"><li style="list-style-type:disc"><strong>Cainiao (Alibaba)</strong> – đầu tư mạnh sorting tự động, vừa triển khai <strong>trung tâm phân loại tự động lớn nhất miền Nam</strong> cho 1 hãng chuyển phát VN → nhu cầu ổn định hoá hạ tầng xanh quanh hub (bãi sạc, xe tải/van điện). (【Cainiao sorting lớn nhất miền Nam】 )<div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-80f1-8875-e08323fed582" class=""><strong>Gợi ý:</strong> “Green Hub Play” – đồng phát triển <strong>bãi sạc nhanh + đội van điện</strong> quanh hub; báo cáo <strong>g CO₂e/đơn</strong> cho sàn.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-803d-9ede-ee745dd07ffa" class="bulleted-list"><li style="list-style-type:disc"><strong>SPX (Shopee Express)</strong> – xây <strong>siêu trung tâm phân loại lớn nhất Đông Nam Á tại VN</strong> (bắt đầu 2025, hoàn thành 2027). ( )<div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-80bb-8cea-c43db9becdd3" class=""><strong>Gợi ý:</strong> hợp đồng <strong>dịch vụ sạc theo ca</strong> + <strong>“Green Line-haul”</strong> kết nối hub–hub bằng e-LCV.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-80f9-9303-cfe082979204" class="bulleted-list"><li style="list-style-type:disc"><strong>SHEIN</strong> – thuê <strong>kho 15ha gần TP.HCM</strong> (bước vào VN để đa dạng chuỗi cung ứng). ( )<div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-80b8-ba9c-f5ef106d976a" class=""><strong>Gợi ý:</strong> cung cấp <strong>đội xe EV cho xuất-nhập kho &amp; line-haul ngắn</strong>, kèm <strong>bảng điều khiển ESG</strong>.</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-80c9-b00f-c216b77c3b95"/></div><div style="display:contents" dir="auto"><h1 id="2a5c5e6f-95bd-8016-82f0-f6a899f2738a" class=""><strong>2) 3PL/Integrators toàn cầu (hậu cần hợp đồng, fulfillment, line-haul)</strong></h1></div><div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-808b-9a10-eae670d8e034" class=""><strong>Tại sao hợp tác:</strong> đang <strong>điện hoá logistics</strong> tại châu Á, cần <strong>đối tác hạ tầng sạc + đội xe xanh</strong> bản địa.</p></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-80db-b9f8-e89edf0044e7" class="bulleted-list"><li style="list-style-type:disc"><strong>DHL Group</strong> – mở <strong>EV Centers of Excellence</strong> ở APAC (2024), giải pháp end-to-end cho EV supply chain. ( )<div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-8075-babc-d8a8b276bded" class=""><strong>Gợi ý:</strong> thí điểm <strong>EV last-mile &amp; middle-mile</strong> tại Hà Nội/TP.HCM; UniPower cung cấp <strong>bãi sạc + quản trị kWh</strong>.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-8039-8a58-e1d40eda4795" class="bulleted-list"><li style="list-style-type:disc"><strong>Maersk Contract Logistics</strong> – đã vận hành <strong>kho ngoại quan (bonded) tự cấp phép đầu tiên ở miền Bắc VN</strong>, <strong>Amazon</strong> là khách hàng đầu tiên. ( )<div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-80af-b76d-dfe640b44e65" class=""><strong>Gợi ý:</strong> <strong>điện hoá vận tải kho–cảng</strong> (Hải Phòng/Lạch Huyện) bằng e-truck/e-tractor + trạm sạc depot.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-80e0-853f-d2488ddb8d8c" class="bulleted-list"><li style="list-style-type:disc"><strong>Kuehne+Nagel, DB Schenker, UPS, FedEx</strong> – có hiện diện; cần <strong>case “Green First-&amp;-Middle Mile”</strong> để thắng thầu FDI/ESG.<div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-806d-a549-e7a5752e1ce1" class=""><strong>Gợi ý:</strong> gói <strong>SLA xanh</strong> (on-time% + gCO₂e/chuyến) cho khách công nghiệp/khu công nghệ.</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-800f-a07a-d732638ec493"/></div><div style="display:contents" dir="auto"><h1 id="2a5c5e6f-95bd-80a3-b292-d8649e002114" class=""><strong>3) CEP khu vực/cross-border (bưu kiện, last-mile)</strong></h1></div><div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-802c-bf0d-f665e628f613" class=""><strong>Tại sao hợp tác:</strong> tái cấu trúc tại VN, tìm <strong>mô hình chi phí thấp + ESG</strong>.</p></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-80e8-bbef-ee9c92a23f63" class="bulleted-list"><li style="list-style-type:disc"><strong>J&amp;T Express</strong> – tiếp tục mở rộng khu vực, công bố lộ trình <strong>xanh hoá đội phương tiện</strong> tại VN (Euro 5, bao bì xanh). ( )<div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-80a4-8237-c1b3095b8740" class=""><strong>Gợi ý:</strong> cung cấp <strong>đội xe điện theo ca</strong> + <strong>bãi sạc thuê bao</strong> cho tuyến nội thành.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-802f-9985-de81011d54c4" class="bulleted-list"><li style="list-style-type:disc"><strong>SF Express (SF Group, Trung Quốc)</strong> – làm việc với <strong>ACV</strong> về <strong>hàng không logistics</strong> tại VN (mở rộng air cargo). ( )<div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-806f-ae5e-e46b6b9dd67c" class=""><strong>Gợi ý:</strong> <strong>EV air-side/near-air-side</strong> (xe kéo, van điện sân bay) + bãi sạc tại logistics parks gần sân bay.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-80fb-b355-e7ee38c501b3" class="bulleted-list"><li style="list-style-type:disc"><strong>Ninja Van</strong> – đang <strong>rút mảng express tại VN 2025</strong>, xoay trục sang <strong>B2B restocking &amp; cold-chain</strong> khu vực. ( )<div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-80e9-ba58-f6f89e50ab6e" class=""><strong>Gợi ý:</strong> hợp tác <strong>cold-chain EV</strong> (van điện thùng lạnh) cho B2B giao hàng định tuyến.</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-8040-abe5-d50dcb2aed97"/></div><div style="display:contents" dir="auto"><h1 id="2a5c5e6f-95bd-801e-95e8-e3a727a10d9a" class=""><strong>4) Cold-chain &amp; kho nhiệt độ (FMCG, dược)</strong></h1></div><div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-80be-b596-e4b0d403378a" class=""><strong>Tại sao hợp tác:</strong> khối này bị áp lực <strong>ESG + an toàn thực phẩm/dược</strong> → ưu tiên <strong>đội xe điện ổn định nhiệt</strong>.</p></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-8080-9356-eb61bc437f9a" class="bulleted-list"><li style="list-style-type:disc"><strong>Lineage Logistics (Emergent Cold APAC)</strong> – hiện diện VN qua M&amp;A <strong>Emergent Cold</strong> (mạng kho lạnh khu vực). ( )<div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-8073-94b7-f2522cb026f9" class=""><strong>Gợi ý:</strong> <strong>điện hoá chặng kho-siêu thị/nhà hàng</strong> bằng <strong>e-reefer vans</strong>, theo dõi <strong>kWh &amp; nhiệt</strong> trên một dashboard.</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-809e-a56d-f78ed825e255"/></div><div style="display:contents" dir="auto"><h1 id="2a5c5e6f-95bd-80c9-97ec-f036c263bb0a" class=""><strong>5) Hàng không, cảng biển &amp; sân bay (air-sea logistics)</strong></h1></div><div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-803c-a06f-e0ae13bc457b" class=""><strong>Tại sao hợp tác:</strong> cần <strong>EV for air-side/port-side</strong> + <strong>hạ tầng sạc depot</strong> để giảm phát thải phạm vi 3.</p></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-8087-8371-ecb1485d4a97" class="bulleted-list"><li style="list-style-type:disc"><strong>ACV &amp; đối tác air cargo (SF Group, DHL Aviation, …)</strong> – cửa vào <strong>EV sân bay</strong> (xe kéo, van, shuttle). ( )</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-803b-a4cd-e4e1f919cc60" class="bulleted-list"><li style="list-style-type:disc"><strong>Hệ sinh thái cảng (Hải Phòng, Cát Lái, Cái Mép-Thị Vải)</strong> qua các tích hợp của <strong>Maersk/APM</strong>. ( )<div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-80aa-b5ad-fdd5c43d31bd" class=""><strong>Gợi ý:</strong> trạm sạc <strong>depot-fast DC</strong> cho đầu kéo/tractor trong cảng + tuyến <strong>kho ngoại quan ↔ cảng</strong>.</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-80fe-896e-e349756a7f9b"/></div><div style="display:contents" dir="auto"><h1 id="2a5c5e6f-95bd-801a-a480-e395e2342b47" class=""><strong>6) OEM EV thương mại &amp; hệ sinh thái pin/swap (đòn bẩy đội xe)</strong></h1></div><div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-8022-bd24-c00e0d5aa7b8" class=""><strong>Tại sao hợp tác:</strong> <strong>đồng phát triển đội xe</strong> với OEM giúp nhanh quy mô &amp; chi phí mua sắm.</p></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-804b-b9c7-f4758568eb35" class="bulleted-list"><li style="list-style-type:disc"><strong>BYD</strong> – mở rộng mạnh tại VN, hướng tới 100 đại lý tới <strong>2026</strong>, cân nhắc nhà máy khu Bắc. ( )<div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-800f-adf3-d1f0b879cffb" class=""><strong>Gợi ý:</strong> <strong>JV fleet</strong> e-LCV (BYD T3/e-van) + mua điện/sạc của UniPower; cùng chào thầu 3PL/CEP.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-806d-82ce-f2b129335c6f" class="bulleted-list"><li style="list-style-type:disc"><strong>VinFast (VF) &amp; V-Green</strong> – mạng sạc lớn; (hạn chế ưu tiên nội hệ). <strong>Gợi ý</strong>: nơi khó dùng V-Green, <strong>UniPower lấp khoảng trống</strong> với hub độc lập.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-806d-81fd-eac243897476" class="bulleted-list"><li style="list-style-type:disc"><strong>Nhà sản xuất thùng lạnh/hoán cải</strong> (châu Âu/Thái/Nhật): đồng thiết kế <strong>e-reefer</strong> cho Việt Nam (nhiệt-ẩm cao).</li></ul></div><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-8090-8fc2-fb95409e311e"/></div><div style="display:contents" dir="auto"><h1 id="2a5c5e6f-95bd-8078-bda9-f8cf3c6a1328" class=""><strong>7) Nhóm “khách hàng chiến lược” cần giải pháp trọn gói (không thuần nền tảng)</strong></h1></div><div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-8018-807a-c60100ea1d9a" class=""><strong>Tại sao hợp tác:</strong> hợp đồng <strong>ESG/SLA</strong> dài hạn, biên lợi nhuận tốt.</p></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-805e-8bce-fc2ed5c634ee" class="bulleted-list"><li style="list-style-type:disc"><strong>FMCG &amp; bán lẻ hiện đại</strong> (Unilever, Nestlé, Central Retail…): yêu cầu <strong>CO₂ minh bạch</strong> trong đấu thầu logistics.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-8095-9511-eec159b612c6" class="bulleted-list"><li style="list-style-type:disc"><strong>Dược &amp; thiết bị y tế</strong>: cần <strong>cold-chain chuẩn GSP</strong> → hợp đồng e-reefer định tuyến.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-8019-a36a-ef1b586602e9" class="bulleted-list"><li style="list-style-type:disc"><strong>Hãng thời trang/marketplace xuyên biên giới</strong> (SHEIN, Temu, Amazon Global Selling): cần <strong>green consolidation</strong> tại VN. (Amazon đã là khách đầu tiên của kho Maersk miền Bắc). ( )</li></ul></div><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-8043-b302-e41f72298ff5"/></div><div style="display:contents" dir="auto"><h2 id="2a5c5e6f-95bd-80f1-b362-ea293a14f7e0" class=""><strong>Cách “đóng gói” đề xuất cho từng nhóm (Playbooks ngắn)</strong></h2></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-80fb-9a50-e314ff2344be" class="bulleted-list"><li style="list-style-type:disc"><strong>Green Hub Play (E-commerce hubs):</strong> bãi sạc nhanh + đội e-van theo ca quanh hub; <strong>SLA: on-time% &amp; gCO₂e/đơn</strong>. (Cainiao, SPX)</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-8012-ac9a-c3bda9047a1b" class="bulleted-list"><li style="list-style-type:disc"><strong>Green Middle-mile (3PL/Integrators):</strong> e-LCV kho↔cảng/sân bay; <strong>định giá theo kWh</strong> + <strong>slot sạc đặt chỗ</strong>. (DHL, Maersk)</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-80de-aad9-c4662a3a0d0d" class="bulleted-list"><li style="list-style-type:disc"><strong>Cold-chain Electric:</strong> e-reefer van + cảm biến nhiệt/kWh; <strong>bảng điều khiển ESG</strong>. (Lineage, Ninja Van pivot)</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-8093-a4d6-f8c2aacdba89" class="bulleted-list"><li style="list-style-type:disc"><strong>Air-side EV:</strong> xe kéo/van sân bay chạy điện + depot sạc; hợp tác <strong>ACV</strong>. (SF/ACV)</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-8078-9983-e38712fdaa7a" class="bulleted-list"><li style="list-style-type:disc"><strong>OEM Co-Fleet:</strong> đồng đầu tư đội e-van với BYD/VF; UniPower <strong>vận hành + sạc</strong>, OEM <strong>xe &amp; bảo dưỡng</strong>.</li></ul></div><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-802d-89f2-e64fb26ff4ca"/></div><div style="display:contents" dir="auto"><h2 id="2a5c5e6f-95bd-8095-8a1c-da03b5072311" class=""><strong>Ưu tiên tiếp cận (Top-6, khả năng “win-win” cao)</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2a5c5e6f-95bd-802d-9d35-d76f7de12d8f" class="numbered-list" start="1"><li><strong>Cainiao</strong> – khóa <strong>Green Hub</strong> tại miền Nam; volume lớn, cần chuẩn ESG. ( )</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2a5c5e6f-95bd-80c8-be02-cd2072272a89" class="numbered-list" start="2"><li><strong>SPX (Shopee Express)</strong> – siêu sorting 2025–2027 → cần <strong>điện hoá chặng hub-cuối</strong>. ( )</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2a5c5e6f-95bd-801d-aaaa-f36592b63d1d" class="numbered-list" start="3"><li><strong>DHL</strong> – chương trình <strong>EV COEs APAC</strong>, sẵn sàng mở <strong>pilot</strong> tại VN. ( )</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2a5c5e6f-95bd-8062-844d-c71e5f726772" class="numbered-list" start="4"><li><strong>Maersk Contract Logistics</strong> – <strong>kho ngoại quan + Amazon</strong> ở Hải Phòng → “green port shuttle”. ( )</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2a5c5e6f-95bd-80a4-b592-e7d66e38b5e1" class="numbered-list" start="5"><li><strong>SF Express (air cargo)</strong> – đang làm việc với <strong>ACV</strong> → cơ hội EV air-side. ( )</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2a5c5e6f-95bd-80b2-a8a5-e1e896145fca" class="numbered-list" start="6"><li><strong>Lineage (Emergent Cold APAC)</strong> – mạng kho lạnh khu vực; hợp đồng <strong>e-reefer</strong>. ( )</li></ol></div><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-806a-9bc0-ef652eb7a0f0"/></div><div style="display:contents" dir="auto"><h2 id="2a5c5e6f-95bd-80fa-a058-c4ea8aabf643" class=""><strong>Tại sao họ nên chọn UniPower (giá trị khác biệt)</strong></h2></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-805e-808b-dfb406c67f6d" class="bulleted-list"><li style="list-style-type:disc"><strong>Hạ tầng sạc &amp; EV nationwide</strong>: sẵn sàng mở rộng theo cụm hub/kho/sân bay.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-80ff-960d-f961b3391c68" class="bulleted-list"><li style="list-style-type:disc"><strong>Unit economics “Mobility × Energy”</strong>: kiểm soát <strong>kWh</strong> → <strong>chi phí/đơn</strong> thấp, giá ổn định.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-8018-9e56-f288add34ad7" class="bulleted-list"><li style="list-style-type:disc"><strong>Tuân thủ dữ liệu &amp; ESG</strong>: chuẩn PDPD, <strong>dashboard gCO₂e/đơn</strong> cho khách toàn cầu.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a5c5e6f-95bd-80cc-bc3f-fd815e2e02d5" class="bulleted-list"><li style="list-style-type:disc"><strong>Đội ngũ bản địa + chuyên gia quốc tế</strong>: <strong>triển khai nhanh</strong>, nói chung “ngôn ngữ MNC”.</li></ul></div><div style="display:contents" dir="auto"><hr id="2a5c5e6f-95bd-80c5-b319-f3d5ce7d34fa"/></div><div style="display:contents" dir="auto"><p id="2a5c5e6f-95bd-80bb-a563-f653066d1a4f" class="">
</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
