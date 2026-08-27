---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Principles of Ethical Intelligence™</title><style>
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
	
</style></head><body><article id="2e4c5e6f-95bd-80b4-bf26-e22c45ed2f22" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Principles of Ethical Intelligence™</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80cc-88f5-e99e8898b9f9" class=""><em>A comprehensive operating standard</em></p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80a6-8d71-e4563f29c93b"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80f6-899b-f6a13912e363" class=""><strong>1. Applicability</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8059-8e80-ed5a10e517b6" class="">These principles apply to <strong>any system that exerts decision-making power</strong>, including:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80da-b459-c4e9fdd38e81" class="bulleted-list"><li style="list-style-type:disc">human-led organizations</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8068-ad3a-d934a0a71235" class="bulleted-list"><li style="list-style-type:disc">automated and semi-automated systems</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c1-9700-fdc4e3d76b63" class="bulleted-list"><li style="list-style-type:disc">AI, ML, and decision-support tools</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-807b-bae8-e037a1e13643" class="bulleted-list"><li style="list-style-type:disc">platforms, markets, and infrastructures</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d1-b9df-c517286fd45f" class="bulleted-list"><li style="list-style-type:disc">public and private governance systems</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d5-81ca-f7f082ff6890" class="">Ethical Intelligence™ is <strong>structural</strong>, not behavioral.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80fb-a2a2-d6b818b8435a"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-802a-bb77-cd6e0bc9e12a" class=""><strong>2. Foundational Definition</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-805e-ae12-c5ef51338123" class="">An ethically intelligent system is one that:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8027-bf47-ce63583e6ad4" class="bulleted-list"><li style="list-style-type:disc">operates within human, biological, and social limits</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8029-9964-f30a5257c90b" class="bulleted-list"><li style="list-style-type:disc">preserves safety, dignity, and integrity</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806a-825c-f7d1afeb0ada" class="bulleted-list"><li style="list-style-type:disc">prevents foreseeable harm</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80dc-a6c3-c88814651e68" class="bulleted-list"><li style="list-style-type:disc">internalizes responsibility before action</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8079-9ae8-e2c797f8501d" class="bulleted-list"><li style="list-style-type:disc">remains legitimate under scale and stress</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-802c-be85-ef1db679b1d0" class="">Failure in any dimension invalidates claims of intelligence.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80cb-8106-f0022989d555"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80ab-8a95-d3376847b006" class=""><strong>3. Absolute Prohibitions (Non-Negotiable)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80bb-96d3-febd4f859834" class="">An intelligent system <strong>must not</strong>:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80ca-9691-c79f639bbdd1" class="numbered-list" start="1"><li>Cause foreseeable physical, psychological, economic, or social harm.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8030-a32e-ffcd6d8c320e" class="numbered-list" start="2"><li>Externalize risk to individuals without corresponding authority.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8060-b542-ce0aedade2d0" class="numbered-list" start="3"><li>Require participation without a safe and penalty-free right to refuse.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80ce-8416-fd3c15c6ece5" class="numbered-list" start="4"><li>Treat compliance as consent.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-806a-8580-d7562555efaa" class="numbered-list" start="5"><li>Optimize output by exceeding human limits.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8039-b3fb-ca29598aca73" class="numbered-list" start="6"><li>Punish individuals for outcomes they were structurally unable to prevent.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80d8-9f5e-f6aca9166a00" class="numbered-list" start="7"><li>Substitute metrics, KPIs, or dashboards for lived reality.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-806e-8b33-d42a6ad01ab8" class="numbered-list" start="8"><li>Hide responsibility behind abstraction, delegation, or automation.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8046-ab0b-cd643a239b03" class="numbered-list" start="9"><li>Normalize harm as “acceptable trade-offs” without consent.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-802e-a6e7-d347223621a2" class="numbered-list numbered-list-digits-2" start="10"><li>Use post-hoc accountability to legitimize preventable damage.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-806c-a48e-ee0ac3f7ce1e" class="numbered-list numbered-list-digits-2" start="11"><li>Suppress dissent, escalation, or whistleblowing.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8017-9f27-f4e9f066ce46" class="numbered-list numbered-list-digits-2" start="12"><li>Treat silence as agreement.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8090-9871-e5ea29159028" class="numbered-list numbered-list-digits-2" start="13"><li>Create irreversible outcomes without explicit authorization.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80ce-9ebd-fd76b20676dd" class="numbered-list numbered-list-digits-2" start="14"><li>Require moral heroism to prevent harm.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80c8-88f6-c74946cb4b6b" class="numbered-list numbered-list-digits-2" start="15"><li>Claim neutrality while enforcing asymmetric power.</li></ol></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-809d-a85a-fb5d9e6ddcdc" class="">Violation of any item nullifies ethical legitimacy.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8045-8888-f65e86761501"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80ea-8084-fc39fd4b4210" class=""><strong>4. Human Safety and Dignity (Must Be Preserved)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80e1-9717-e90355f2aa1f" class="">Systems must explicitly protect:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-801c-916e-c6e856738b3e" class="numbered-list" start="1"><li>Physical safety.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80c4-9f6b-cd974506e199" class="numbered-list" start="2"><li>Psychological safety.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80f9-a639-e5fa0f8ea787" class="numbered-list" start="3"><li>Cognitive integrity (freedom from manipulation or coercion).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8021-b102-ffca66ce9f61" class="numbered-list" start="4"><li>Economic security against extractive risk.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80cf-ab59-ef3a33d24812" class="numbered-list" start="5"><li>Social dignity (agency, voice, refusal).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80cb-b123-f580b58873c9" class="numbered-list" start="6"><li>Biological limits (fatigue, recovery, saturation).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80c6-a77c-d26d9298d58a" class="numbered-list" start="7"><li>The right to rest and recover without penalty.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80ab-8a1e-d2bfa31a2d52" class="numbered-list" start="8"><li>The right to disengage.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8002-9968-ec8af9324b13" class="numbered-list" start="9"><li>The right to escalate concerns safely.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-801e-b7ff-f6cb5e124308" class="numbered-list numbered-list-digits-2" start="10"><li>Protection from retaliation.</li></ol></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8050-9ed8-c9ee44a006b9" class="">Protection must be <strong>designed</strong>, not discretionary.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8095-98b6-c5cad2443416"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80c7-a93a-cef4bb3f8821" class=""><strong>5. Limits as Hard Constraints</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ac-b081-cb2f5342ef86" class="">Ethical systems must:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8016-bd72-dd3e9f9baa81" class="numbered-list" start="1"><li>Define maximum sustainable human load.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8021-901a-c052bf262f5e" class="numbered-list" start="2"><li>Enforce recovery and rest structurally.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80b6-9ee2-e41015ac6297" class="numbered-list" start="3"><li>Detect overload before failure.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-808c-a30e-f331fbf12a5f" class="numbered-list" start="4"><li>Throttle execution under stress.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8067-8e3b-f26393f24148" class="numbered-list" start="5"><li>Prevent escalation when limits are reached.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-808e-bafc-e314e5a3a3ea" class="numbered-list" start="6"><li>Treat exhaustion as a system failure signal.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80a9-8aee-e10767008993" class="numbered-list" start="7"><li>Refuse optimization that consumes stability.</li></ol></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-806f-bf13-dd724e3cb2b3" class="">Ignoring limits is design negligence.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8098-b4ff-f69e92909ef9"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80bd-a7a4-da269b0ca881" class=""><strong>6. Responsibility (Pre-Action Requirement)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8007-a6f2-ec1319d19bc6" class="">Responsibility means:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-806c-8b5a-f95fe37a5894" class="numbered-list" start="1"><li>Duty of care <strong>before harm occurs</strong>.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8041-a422-e7b72c9d1e12" class="numbered-list" start="2"><li>Authority aligned with risk exposure.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80f1-99d7-cad35b4ac11e" class="numbered-list" start="3"><li>Resources aligned with obligation.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80f3-b8da-eb0b50abea76" class="numbered-list" start="4"><li>Clear ownership of decisions prior to execution.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8049-8776-c576a22aad4b" class="numbered-list" start="5"><li>The power to refuse, pause, or stop actions.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8011-8134-d51d2baefb5c" class="numbered-list" start="6"><li>Escalation without retaliation.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8012-a1da-d0b94ce31f34" class="numbered-list" start="7"><li>Accountability paths defined <em>in advance</em>.</li></ol></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8035-8407-fc79a98008fb" class="">Responsibility without authority is invalid.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-804f-830e-c39f9ab22180" class="">Accountability without responsibility is coercive.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8051-ab48-df83ad72650f"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80f5-8df2-dafe036485be" class=""><strong>7. Accountability (Secondary, Conditional)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80db-9742-c7fa7c9e0f98" class="">Accountability is legitimate <strong>only if</strong>:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8082-857b-c45b20187ec1" class="numbered-list" start="1"><li>Responsibility was structurally present beforehand.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8081-83b4-fcd8f7a5f382" class="numbered-list" start="2"><li>Authority matched obligation.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80df-ae1d-c51f755e87d4" class="numbered-list" start="3"><li>Refusal and escalation were available.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80e3-b050-e5be553db3f6" class="numbered-list" start="4"><li>Resources were sufficient.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8030-aa08-fd618d3165e0" class="numbered-list" start="5"><li>Constraints were transparent.</li></ol></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8048-8f51-ecc1e145db73" class="">Absent these conditions, punishment is illegitimate.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8058-8154-d7917be8c1a9"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80a1-adc4-fb6c68175a18" class=""><strong>8. Consent (Strict Definition)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80da-8640-cb869ad51d62" class="">Consent exists <strong>only when</strong>:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8036-91d7-f980696ffa57" class="numbered-list" start="1"><li>Participation is optional in practice.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-807b-bd1a-d867ccb2dc29" class="numbered-list" start="2"><li>Refusal carries no penalty.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80a2-a12c-daddf4eaec4f" class="numbered-list" start="3"><li>Exit is possible without disproportionate harm.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80a2-8525-cba21a16972f" class="numbered-list" start="4"><li>Risks are understandable and disclosed.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8074-b846-dab5615b8e17" class="numbered-list" start="5"><li>Silence is not interpreted as agreement.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-808b-be0c-d3bad476be17" class="numbered-list" start="6"><li>Consent can be withdrawn.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-804b-bc68-c17ee60c4c16" class="numbered-list" start="7"><li>Power asymmetry is acknowledged and mitigated.</li></ol></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80bc-898d-fd426a0c0138" class="">Consent without refusal is invalid.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-806c-b3a0-cd302dfbd47c"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80ae-a7e0-f346a944d221" class=""><strong>9. The Right to Refuse</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b3-a3f1-d18597ad0722" class="">Every intelligent system must include:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80c8-8ce2-d8bb63f463f8" class="numbered-list" start="1"><li>A protected right to refuse.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-804a-b881-d532c737bb0b" class="numbered-list" start="2"><li>Refusal without retaliation.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80aa-a84b-cf1ebe3389f4" class="numbered-list" start="3"><li>Automatic pause or review upon refusal.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-805b-be86-d6eb3d415ad2" class="numbered-list" start="4"><li>Refusal treated as a risk signal.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8032-8b40-c70f40f7ecbe" class="numbered-list" start="5"><li>Safe internal escalation channels.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-808c-9ba7-d501392a3186" class="numbered-list" start="6"><li>External whistleblowing protection when internal channels fail.</li></ol></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a1-ac44-e1de903e6434" class="">A system that punishes refusal is coercive.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8007-8458-ef99dad4866f"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-807c-8ec8-f0f3e7a6f56a" class=""><strong>10. Metrics and Measurement (Subordination Rule)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d5-93e0-de7fa27895a0" class="">Metrics may inform but must never:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80fd-90ee-dbc3092d5c02" class="numbered-list" start="1"><li>Define success alone.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80e9-8108-c8bdbbb8209b" class="numbered-list" start="2"><li>Override human judgment.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8091-a08b-c6ca64dbeacb" class="numbered-list" start="3"><li>Erase lived experience.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80f4-883f-dbda8820eebc" class="numbered-list" start="4"><li>Suppress dissent.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8045-814b-fa0c755b0d9c" class="numbered-list" start="5"><li>Justify harm.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80eb-ba7a-d63512571b16" class="numbered-list" start="6"><li>Replace responsibility.</li></ol></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80cc-9175-d043d5e95aba" class="">When metrics conflict with reality, metrics are wrong.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-807d-82d7-de1704e6bdad"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8045-8073-ed066d30633f" class=""><strong>11. Ethics as Infrastructure</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ae-8bae-e145a47d5ece" class="">Ethics must be embedded in:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8093-8b50-c937819bccdd" class="bulleted-list"><li style="list-style-type:disc">system architecture</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8015-ac23-cccd68158bf1" class="bulleted-list"><li style="list-style-type:disc">incentives and compensation</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806a-8300-f75484dd8006" class="bulleted-list"><li style="list-style-type:disc">contracts and terms</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-803f-b7a3-f530e374888f" class="bulleted-list"><li style="list-style-type:disc">permissions and controls</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80bd-a9ee-ceb9b0d9521f" class="bulleted-list"><li style="list-style-type:disc">refusal and escalation mechanisms</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8005-8f96-e8b59e4f690a" class="bulleted-list"><li style="list-style-type:disc">enforcement logic</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c9-a3e6-c70eb87ee3c3" class="bulleted-list"><li style="list-style-type:disc">auditability and traceability</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80be-a91f-c37c864bba58" class="">Ethics based on goodwill or culture alone is insufficient.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-807c-86c8-dec280daf459"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8093-9459-f728638bba17" class=""><strong>12. Authority and Power Alignment</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8048-a67d-de8ee3db7207" class="">Ethical systems must ensure:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8054-8081-c145dcb18bad" class="numbered-list" start="1"><li>Power follows responsibility.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8054-837a-f8c6fc9bd25b" class="numbered-list" start="2"><li>Decisions are made closest to risk.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8064-ac91-f5dc97caf1a8" class="numbered-list" start="3"><li>Authority is not centralized while harm is decentralized.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-800d-8a4c-e5afee51eedc" class="numbered-list" start="4"><li>Automation does not remove human veto.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80b0-8762-cebc686e5a5b" class="numbered-list" start="5"><li>Delegation does not remove ownership.</li></ol></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8016-987c-ddb3a9add31c" class="">Misaligned power is a systemic risk.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8012-8302-e715c0032eba"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-803f-b49f-d66830e18428" class=""><strong>13. Reversibility and Irreversibility</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b6-975e-f9ae1c4c5f6d" class="">Systems must:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-801c-8251-fe90c475209e" class="numbered-list" start="1"><li>Identify irreversible actions explicitly.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-806f-b3fe-f3ef692fb1fa" class="numbered-list" start="2"><li>Require higher thresholds for irreversible harm.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80ce-a73b-ce4cf9d8958c" class="numbered-list" start="3"><li>Prefer reversible decisions.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8019-8866-d2726c3ecee8" class="numbered-list" start="4"><li>Enable rollback where possible.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-806b-ba14-dbdcd7c53fdb" class="numbered-list" start="5"><li>Escalate before irreversible execution.</li></ol></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-808b-9427-dd8ea7e05166" class="">Irreversibility without consent is unethical.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80d5-bda4-daa3bbba2aba"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80d3-93dc-cdffa32bcce8" class=""><strong>14. Transparency and Auditability</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80be-9345-e69c9afc5739" class="">Ethical systems must be:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8085-9175-da67f2eeb660" class="numbered-list" start="1"><li>Inspectable.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8082-97bd-d65b1e7b7481" class="numbered-list" start="2"><li>Auditable.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-804e-b6a0-e881dbc64815" class="numbered-list" start="3"><li>Explainable at the level of impact.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80a0-95d3-eceb68bdb7aa" class="numbered-list" start="4"><li>Traceable from decision to outcome.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-802b-afe6-ec188711b629" class="numbered-list" start="5"><li>Clear about who decided and why.</li></ol></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8085-a24c-ed0e157b6219" class="">Opacity that hides harm is unethical.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-801d-9c33-ce396b7d4f56"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80f8-864d-d3840f1ca2f5" class=""><strong>15. Failure Handling</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8064-9321-f632f41d52b5" class="">When failure occurs, systems must:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8045-8236-eb54518458bf" class="numbered-list" start="1"><li>Prioritize harm mitigation over blame.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-806b-974e-e2c560c2cc65" class="numbered-list" start="2"><li>Protect those who raised concerns.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80e0-a2d2-e2d09c5cc439" class="numbered-list" start="3"><li>Examine structural causes first.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8093-9b83-e1328adb0a8c" class="numbered-list" start="4"><li>Avoid scapegoating.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8097-a7d9-ec80af86d8d7" class="numbered-list" start="5"><li>Restore responsibility upstream.</li></ol></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f5-82de-d60026151601" class="">Repeated failure indicates design flaws, not individual error.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-806d-8372-d9d25e4e1cf1"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-806a-8450-f66bbd8b7186" class=""><strong>16. The Ethical Intelligence™ Test</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8020-98a7-d9af7f6a6ea5" class="">A system qualifies as ethically intelligent <strong>if and only if</strong> it:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8063-888f-c8f0cb24eed2" class="numbered-list" start="1"><li>Can model its impact.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80c4-96bd-c7188596bd8e" class="numbered-list" start="2"><li>Can inhibit its own actions.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80a1-bee8-d076bf86034f" class="numbered-list" start="3"><li>Can refuse execution.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8094-a21d-e68d2fe3c600" class="numbered-list" start="4"><li>Internalizes harm costs.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8072-8e8b-d96b2edfca33" class="numbered-list" start="5"><li>Preserves human dignity.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8071-9da6-f2fc3326d76b" class="numbered-list" start="6"><li>Operates within limits.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80f5-8c28-c4a8fdb0db7f" class="numbered-list" start="7"><li>Remains legitimate under scale.</li></ol></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ff-91b3-f404996a86f5" class="">Failure on any criterion disqualifies the system.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80d6-bd18-eb61ce5004c5"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-808b-a5d5-c72a45535dd6" class=""><strong>17. Final Clause</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80e9-888c-d80b059537c3" class="">Ethical Intelligence™ is not aspirational.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8075-a8d3-e896a6b07e9b" class="">It is <strong>a minimum operating condition</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-808f-831c-f855386087b5" class="">Systems that violate these principles may function, scale, or profit —</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8041-8193-dcb3bf784e6a" class="">but they are <strong>structurally unsafe and illegitimate</strong>.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
