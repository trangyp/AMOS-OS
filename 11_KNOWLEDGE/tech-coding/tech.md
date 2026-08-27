---
tags: [tech-coding]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>tech </title><style>
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
	
</style></head><body><article id="2a7c5e6f-95bd-80c1-ba72-d1b666157322" class="page sans"><header><h1 class="page-title" dir="auto">tech </h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-8006-b1db-cc24d92cb6bf" class=""><strong>1️⃣ Reframe your CTO role</strong></h2></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80f5-b7f1-e84403909803" class="">Instead of thinking of yourself as a “coding CTO,” position yourself as the <strong>Chief Systems Architect</strong> — responsible for:</p></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-8003-a4d8-c7ea9ab2e1b1" class="bulleted-list"><li style="list-style-type:disc"><strong>Vision and integration</strong> (how every product connects).</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-8069-81b0-e7bbe82da83a" class="bulleted-list"><li style="list-style-type:disc"><strong>Prioritisation and sequencing</strong> (which module builds first).</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-800c-99c1-d4f840300cde" class="bulleted-list"><li style="list-style-type:disc"><strong>Design logic and user experience coherence.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-80b8-8ab9-f54dfc67c890" class="bulleted-list"><li style="list-style-type:disc"><strong>Vendor and partner management</strong> (who builds what, to what standard).</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-8031-9c93-e9b6951fc775" class="bulleted-list"><li style="list-style-type:disc"><strong>Data and business outcomes</strong> — you don’t need to code, just to interpret output.</li></ul></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80fb-b2aa-d60ba4c89fe6" class="">This is often called a <strong>“Product-Strategic CTO”</strong> — and it’s the most valuable kind for companies like UniPower, because you can connect product design, business, and tech execution into one loop.</p></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-806c-9d94-c5d68e1a24e0"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-802b-9c4e-fc6b9bcff8d2" class=""><strong>2️⃣ Hire a strong Tech Architect as your technical counterpart</strong></h2></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-800e-b4a0-cc2919765654" class="">Think of them as your <strong>“execution half.”</strong></p></div><div style="display:contents" dir="ltr"><table id="2a8c5e6f-95bd-80c4-a619-c7c6c236380e" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80dc-9ae2-ff7894c7fd17"><th id="AHMe" class="simple-table-header-color simple-table-header"><strong>Role</strong></th><th id="[RFJ" class="simple-table-header-color simple-table-header"><strong>Your Focus</strong></th><th id="xYUv" class="simple-table-header-color simple-table-header"><strong>Their Focus</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8089-a743-da6954a72f70"><td id="AHMe" class="">You (CTO/Strategic Lead)</td><td id="[RFJ" class="">Vision, experience, business priorities, architecture direction</td><td id="xYUv" class="">Translating that into code, pipelines, servers, and frameworks</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8058-b0c4-e43dd90330d9"><td id="AHMe" class="">Tech Architect</td><td id="[RFJ" class="">Code standards, scalability, database design, deployment pipelines</td><td id="xYUv" class="">Reporting technical options, risks, and costs in plain language</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80a4-a20a-fd9ecc24e2eb" class="">Together, you create a “two-in-one CTO office” — you decide <em>what and why</em>, they decide <em>how</em>.</p></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-8075-94c6-c32b4783cd17"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-80f2-b67a-eb9705b319ca" class=""><strong>3️⃣ Structure your tech leadership team</strong></h2></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80e7-8cd3-f9143917a9ac" class="">Here’s the setup that works for your profile:</p></div><div style="display:contents" dir="ltr"><table id="2a8c5e6f-95bd-80f7-9677-f51735324153" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8089-8cbb-f8aac991a2ae"><th id="Atjf" class="simple-table-header-color simple-table-header"><strong>Role</strong></th><th id="QktU" class="simple-table-header-color simple-table-header"><strong>Reports to</strong></th><th id="zRdf" class="simple-table-header-color simple-table-header"><strong>Focus</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8030-be21-cdd34cb9bf98"><td id="Atjf" class=""><strong>Tech Architect / Lead Engineer</strong></td><td id="QktU" class="">You</td><td id="zRdf" class="">Manages all backend and system architecture decisions.</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8088-b63b-c3fa109313f6"><td id="Atjf" class=""><strong>Product Manager (AI &amp; Data)</strong></td><td id="QktU" class="">You</td><td id="zRdf" class="">Keeps roadmap aligned with strategy and business needs.</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8055-94dd-ec9a470ae53d"><td id="Atjf" class=""><strong>DevOps + Security Engineer</strong></td><td id="QktU" class="">Tech Architect</td><td id="zRdf" class="">Ensures uptime, pipelines, cost optimisation.</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80d0-b572-e6c4d2014574"><td id="Atjf" class=""><strong>Frontend &amp; Mobile Leads</strong></td><td id="QktU" class="">Tech Architect</td><td id="zRdf" class="">Delivery and app experience.</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80b5-9008-ec3968a3f1be"><td id="Atjf" class=""><strong>UI/UX Designer</strong></td><td id="QktU" class="">You</td><td id="zRdf" class="">Brand, user experience, customer journeys.</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-8096-b24f-d0e70fb08277" class="">You stay at the <strong>intersection of design, data, and direction</strong> — where the value is created.</p></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-806f-acbb-cb3e1dad483d"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-8042-820d-e3f3eb620064" class=""><strong>4️⃣ Communication framework between you and the Tech Lead</strong></h2></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80d6-a835-f08e047fbba7" class="">To make it efficient even if you don’t code daily:</p></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-80f7-bc72-d33c79fb3524" class="bulleted-list"><li style="list-style-type:disc"><strong>Weekly Architecture Review (60 min):</strong> they explain new builds using diagrams, not code.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-80ab-81b7-f6f190bd7e32" class="bulleted-list"><li style="list-style-type:disc"><strong>Design–Tech Sync (biweekly):</strong> you walk through product flows, they ensure technical feasibility.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-80a9-bf36-d0d56beb23d4" class="bulleted-list"><li style="list-style-type:disc"><strong>Documentation Policy:</strong> every new system must have diagrams and plain-English summaries.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-8084-befe-e651bee9aa65" class="bulleted-list"><li style="list-style-type:disc"><strong>Risk Reports:</strong> they flag cost, security, or scale issues early; you handle decision trade-offs.</li></ul></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80b0-a5fc-d13635a2f73c" class="">That keeps you informed and in control — without needing to review every line of code.</p></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-80cd-9bde-d062a6f6f0f6"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-8016-b963-c593f6397f5e" class=""><strong>5️⃣ Hire sequencing for you</strong></h2></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-8006-8a44-cd5adc1a859b" class="">1️⃣  <strong>Tech Architect / Principal Engineer</strong> – your right hand (Month 0).</p></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80f0-9648-f655029e0dbc" class="">2️⃣  <strong>Backend Lead + DevOps</strong> – report to architect (Month 1).</p></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-8021-9302-e35c99400ab5" class="">3️⃣  <strong>Product Manager (Data/AI)</strong> – bridges you + engineers (Month 2–3).</p></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-8060-a485-ca73ef5936d4" class="">4️⃣  <strong>Frontend + UX</strong> – execute design logic (Month 3–6).</p></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-8081-8c39-c2e4f9475a8c" class="">5️⃣  <strong>Automation &amp; AI Engineers</strong> – follow once infrastructure is stable (Month 6–9).</p></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-80c4-a6d3-f5a49ed5953f"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-801a-96aa-c6002da933a5" class=""><strong>6️⃣ Practical tip: audit before you scale</strong></h2></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80bb-a611-c4f1b7c3bd7e" class="">Before hiring 10+ developers, ask your architect to:</p></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-80a9-a2aa-cc8b37cd7c03" class="bulleted-list"><li style="list-style-type:disc">Audit current codebase (Wooberly, websites, internal apps).</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-809f-a654-f62612e5a9b7" class="bulleted-list"><li style="list-style-type:disc">Build an <strong>Architecture Map</strong> (APIs, data flows, integration points).</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-806e-9b3d-d5c3e3687e4e" class="bulleted-list"><li style="list-style-type:disc">Estimate what can be reused, rebuilt, or automated.</li></ul></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-8086-a8fd-fb3160c9417e" class="">This one document will save you hundreds of thousands and months of rework.</p></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-8014-a93a-f979cab55b07"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-802a-b8c3-ebb3022bf06b" class=""><strong>7️⃣ How to recruit the right Tech Architect</strong></h2></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80c0-94ee-f35c59570fb8" class="">Look for:</p></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-8021-842d-f6b86a268c06" class="bulleted-list"><li style="list-style-type:disc">Experience in <strong>multi-product or mobility platforms</strong> (Grab, Gojek, fintech startups).</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-8032-9106-d71351590f35" class="bulleted-list"><li style="list-style-type:disc">Strong at <strong>systems integration</strong> (APIs, cloud, AI pipelines).</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-8086-bffd-fe34161ac62d" class="bulleted-list"><li style="list-style-type:disc">Comfortable translating code logic into business English.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-8036-ac70-f23f0bb6f587" class="bulleted-list"><li style="list-style-type:disc">Ideally someone who has built and scaled teams before (5–20 engineers).</li></ul></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-8005-93de-ea581733f3f6" class="">Offer them equity or revenue share, not just salary — that attracts the right calibre.</p></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-8029-aa6e-c63bc55896a9"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-8058-ad3a-c7f6a967b493" class=""><strong>8️⃣ Example role split summary</strong></h2></div><div style="display:contents" dir="ltr"><table id="2a8c5e6f-95bd-8012-b727-c0d253e210fe" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80f6-b4ba-d539330d84d9"><th id="G}by" class="simple-table-header-color simple-table-header"><strong>You</strong></th><th id="\AzF" class="simple-table-header-color simple-table-header"><strong>Tech Architect</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80b8-ae90-fef6625ef19f"><td id="G}by" class="">Define the architecture vision</td><td id="\AzF" class="">Translate vision into technical implementation</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8067-aa34-f3cd71eea463"><td id="G}by" class="">Prioritise features</td><td id="\AzF" class="">Plan tech stack and modules</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-809b-8d54-cb6531b5dd0e"><td id="G}by" class="">Lead product, CX, and brand integration</td><td id="\AzF" class="">Lead engineering team and delivery</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-806e-a219-d914a8c9adfa"><td id="G}by" class="">Represent UniPower to partners and investors</td><td id="\AzF" class="">Represent UniPower to developers and vendors</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-809f-872e-f0769f81cf36"><td id="G}by" class="">Enforce UX and systemic logic</td><td id="\AzF" class="">Enforce code and security standards</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-80fb-b3c5-eae6e3940959"/></div><div style="display:contents" dir="auto"><h3 id="2a8c5e6f-95bd-8098-b3a1-c0cea73fbd56" class=""><strong>Bottom line</strong></h3></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-8084-97d0-eefb946c9841" class="">You don’t need to be a “technical CTO.”</p></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80a0-bb7b-e93b7ecaf22e" class="">You need to be a <strong>Systems CTO</strong> — one who designs logic and direction, while a <strong>Technical Architect</strong> executes the translation layer.</p></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80a4-b70a-d5b61b100fdc" class="">That’s actually <em>the modern CTO model</em> — and it fits you perfectly.</p></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-806a-8086-c1eb7a42ee6a"/></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-809d-be1c-ef3d056d8748" class="">Would you like me to write the <strong>exact job description and evaluation guide</strong> for your future Tech Architect (skills, salary range, interview questions, and deliverables for the first 90 days)?</p></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-808c-a3e6-fa1b437c5339" class="">That will make your recruitment process very precise and safe.</p></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80a2-8b9e-efa19a013ac5" class="">That’s a very sharp and realistic assessment — and you’re absolutely right.</p></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80f1-8695-d71079eabb96" class="">In Vietnam, <strong>top-tier engineers and designers are rare</strong>, but when you structure the team <em>lean and intelligently</em> (with clear hierarchy and cross-functional roles), you can absolutely execute at world-class level without the overhead of a big agency.</p></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80fb-a842-ed04cc1d4c1a" class="">Here’s the <strong>refined UniPower tech team model</strong>, tailored to your background, Vietnam’s talent market, and the fact you want a small, efficient team that still covers everything — AI, apps, web, automation, fintech, and design.</p></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-8060-bc12-fe0b8d6af510"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-80f2-9575-e974746193d9" class=""><strong>1️⃣ Target team size: 8–10 people (lean but elite)</strong></h2></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-8089-a414-e476a67edf43" class="">This is the <em>sweet spot</em> for Vietnam: enough coverage for serious delivery, still lean enough to keep quality control and direct oversight.</p></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-8093-b1fa-cb6fe5181cb0"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-8007-9457-dd8903f5b5dc" class=""><strong>2️⃣ Core structure (by function)</strong></h2></div><div style="display:contents" dir="ltr"><table id="2a8c5e6f-95bd-806d-91ae-cd22067be79d" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-803c-a828-f5c35a7ca08e"><th id="cU\t" class="simple-table-header-color simple-table-header"><strong>Function</strong></th><th id="MLPS" class="simple-table-header-color simple-table-header"><strong>Role</strong></th><th id="m:Bi" class="simple-table-header-color simple-table-header"><strong>Profile / Focus</strong></th><th id="oqor" class="simple-table-header-color simple-table-header"><strong>Notes</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80a8-8427-f0300114e14d"><td id="cU\t" class=""><strong>Leadership / Direction</strong></td><td id="MLPS" class=""><strong>CTO (You)</strong></td><td id="m:Bi" class="">Product direction, CX, strategy, integration roadmap, ecosystem design</td><td id="oqor" class="">Focus on what to build and why</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80f1-b1d9-c95493b8af0d"><td id="cU\t" class=""></td><td id="MLPS" class=""><strong>Tech Architect / Lead Engineer</strong></td><td id="m:Bi" class="">Full-stack thinker (backend + infra + integration)</td><td id="oqor" class="">Your technical counterpart</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8055-b759-e6b75fecb032"><td id="cU\t" class=""><strong>Product &amp; Delivery</strong></td><td id="MLPS" class=""><strong>Product Manager / Agile Coach</strong></td><td id="m:Bi" class="">Convert your strategy into tasks, backlog, sprints; manage dev rhythm</td><td id="oqor" class="">Critical — acts as translator between you and engineers</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80b6-a9a5-d0ee2e122130"><td id="cU\t" class=""><strong>Design &amp; Experience</strong></td><td id="MLPS" class=""><strong>Mid/Senior Designer (UX/UI)</strong></td><td id="m:Bi" class="">Consistent brand, mobile/web UX, visual flow, presentation design</td><td id="oqor" class="">Ideally hybrid — can do both UI + UX research</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8068-9369-cb4229adf497"><td id="cU\t" class=""><strong>Backend / Integration</strong></td><td id="MLPS" class=""><strong>2 Backend Devs</strong></td><td id="m:Bi" class="">Node/Laravel + API + microservices; EV, payment, AI integrations</td><td id="oqor" class="">Need disciplined, senior-level; reuse as much code as possible</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8012-9b88-da78374d74f3"><td id="cU\t" class=""><strong>Frontend / App</strong></td><td id="MLPS" class=""><strong>1 Frontend Dev (React)</strong></td><td id="m:Bi" class="">Dashboard, web admin, UniPower website integration</td><td id="oqor" class="">Should know Next.js for SEO + performance</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80c0-acdf-c09fb2628576"><td id="cU\t" class=""></td><td id="MLPS" class=""><strong>1 Flutter Dev</strong></td><td id="m:Bi" class="">Maintain UniTaxi + new mobile apps</td><td id="oqor" class="">Must understand multi-flavour builds (white-labeling)</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80cc-a7ae-c540891b215c"><td id="cU\t" class=""><strong>Data &amp; AI</strong></td><td id="MLPS" class=""><strong>1 Data Engineer</strong></td><td id="m:Bi" class="">Build data pipelines, analytics dashboards, connect to AI/ML APIs</td><td id="oqor" class="">Optional part-time or remote hire from abroad</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8031-b6bc-e4a37db69fdd"><td id="cU\t" class=""><strong>Automation / DevOps</strong></td><td id="MLPS" class=""><strong>1 DevOps / Automation Engineer</strong></td><td id="m:Bi" class="">Deployments, backups, automation, cost optimisation</td><td id="oqor" class="">Handles pipeline, n8n, CI/CD, etc.</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-8022-b1b5-e9f72a40bfc9" class="">➡️ Total: <strong>9–10 key people</strong>, manageable under one daily standup.</p></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-80ff-a554-f19324ff35ab"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-8051-a16b-e0f677f71dce" class=""><strong>3️⃣ Why this structure works for you</strong></h2></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-80d6-a384-e3b6afa43284" class="bulleted-list"><li style="list-style-type:disc">You stay <strong>strategic and design-oriented</strong> — not buried in Jira tickets.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-804c-94ee-d873e9628912" class="bulleted-list"><li style="list-style-type:disc">Your <strong>Tech Architect + PM</strong> handle all technical translation and planning.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-80bc-887b-f81cdaea7efd" class="bulleted-list"><li style="list-style-type:disc">One <strong>designer</strong> ensures every interface (internal and public) looks and feels world-class.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-8001-bb16-c505544e2f20" class="bulleted-list"><li style="list-style-type:disc">You get <strong>real velocity</strong>: with 8–10 disciplined people, you can ship new releases monthly.</li></ul></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-809f-8a0f-fdd61d6f9dc6"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-80a5-b01f-d4072910eff3" class=""><strong>4️⃣ Hiring order &amp; priority</strong></h2></div><div style="display:contents" dir="ltr"><table id="2a8c5e6f-95bd-802d-af3e-e7266117a9d6" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80e8-bd05-f3b179dea500"><th id="U=y~" class="simple-table-header-color simple-table-header"><strong>Phase</strong></th><th id="|qK}" class="simple-table-header-color simple-table-header"><strong>Roles to hire first</strong></th><th id="xFN;" class="simple-table-header-color simple-table-header"><strong>Why</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80f5-a9be-fdefa2235720"><td id="U=y~" class=""><strong>Phase 1 (Month 0–2)</strong></td><td id="|qK}" class="">Tech Architect, PM/Agile Coach, Designer</td><td id="xFN;" class="">These three enable you to lead effectively and set standards early</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80dc-8136-e31e248930ff"><td id="U=y~" class=""><strong>Phase 2 (Month 2–4)</strong></td><td id="|qK}" class="">Backend (2), Flutter, DevOps</td><td id="xFN;" class="">Build solid core product and automation pipelines</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8081-a823-e3af055fa594"><td id="U=y~" class=""><strong>Phase 3 (Month 5–8)</strong></td><td id="|qK}" class="">Frontend, Data Engineer</td><td id="xFN;" class="">Add dashboard, analytics, and AI features</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-8042-924e-c126a13eadb5"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-803d-9c32-fe6e4615da08" class=""><strong>5️⃣ What the Agile Coach / PM actually does</strong></h2></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80df-92fe-fb39801e8363" class="">Because you’re not managing sprint tickets daily, this person keeps the team tight:</p></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-8077-a9a9-f1de6e545924" class="bulleted-list"><li style="list-style-type:disc">Breaks your strategic roadmap into <strong>2-week sprints</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-80f2-b83a-eb64646353ca" class="bulleted-list"><li style="list-style-type:disc">Writes clear <strong>user stories</strong> (technical + UX).</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-806d-bf79-e2f7692affde" class="bulleted-list"><li style="list-style-type:disc">Tracks deadlines, blockers, dependencies.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-806c-8592-ef9ab6df5cc5" class="bulleted-list"><li style="list-style-type:disc">Runs <strong>standups, retros, and demo sessions</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-80ba-8234-d6da360da901" class="bulleted-list"><li style="list-style-type:disc">Reports weekly progress to you in <em>plain language</em>.</li></ul></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80eb-be5a-e12920bc00ec" class="">This one person ensures <strong>discipline and execution</strong> while you stay in creative control.</p></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-806e-9f3a-f8ace07a5417"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-80ad-9858-da1a8db76b7c" class=""><strong>6️⃣ Vietnam-specific hiring strategy</strong></h2></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-8006-a8d4-e9d4c2387052" class="">Because great people are rare, use <strong>hybrid mix</strong>:</p></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-8015-b187-e970e3215755" class="bulleted-list"><li style="list-style-type:disc">Hire <strong>Tech Architect + PM + Designer</strong> full-time in Vietnam (core control team).</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-8002-a8ce-cb9c61c3c981" class="bulleted-list"><li style="list-style-type:disc">Hire <strong>1–2 remote backend/data engineers</strong> from outside Vietnam (Philippines, India, Eastern Europe).</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-8032-93c3-f503ca38aec5" class="bulleted-list"><li style="list-style-type:disc">Keep <strong>DevOps and Flutter</strong> either freelance or local contract.</li></ul></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-8048-b452-c8ee455eea64" class="">That way, you get competence where Vietnam is strong (frontend/mobile, UX) and stability where it’s weak (data/backend).</p></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-80a4-a791-eb254ef0822e"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-80a7-a421-f500018158a8" class=""><strong>7️⃣ Cost model (monthly, in USD)</strong></h2></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80f0-b493-e286275ea885" class=""><em>(realistic for Vietnam + remote hybrid)</em></p></div><div style="display:contents" dir="ltr"><table id="2a8c5e6f-95bd-80bb-a869-ca56e2a6ae58" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-803a-a09d-f1837fa73183"><th id="TbTc" class="simple-table-header-color simple-table-header" style="width:248.1328125px"><strong>Role</strong></th><th id="iYuc" class="simple-table-header-color simple-table-header" style="width:224.5390625px"><strong>Range</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80f8-a7b1-c8b8154db936"><td id="TbTc" class="" style="width:248.1328125px">Tech Architect</td><td id="iYuc" class="" style="width:224.5390625px">2,500 – 4,000</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80ec-bf1e-d9f96c79f089"><td id="TbTc" class="" style="width:248.1328125px">Product Manager / Agile Coach</td><td id="iYuc" class="" style="width:224.5390625px">1,800 – 2,500</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8028-a79f-f494905cd42e"><td id="TbTc" class="" style="width:248.1328125px">UX/UI Designer</td><td id="iYuc" class="" style="width:224.5390625px">1,200 – 2,000</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80d0-9f73-c4f41f47d0d5"><td id="TbTc" class="" style="width:248.1328125px">Backend Dev (x2)</td><td id="iYuc" class="" style="width:224.5390625px">1,500 – 2,000 each</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80f6-a698-e6260a8023b4"><td id="TbTc" class="" style="width:248.1328125px">Frontend Dev</td><td id="iYuc" class="" style="width:224.5390625px">1,500 – 2,000</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80f9-a17d-fa80339b42c3"><td id="TbTc" class="" style="width:248.1328125px">Flutter Dev</td><td id="iYuc" class="" style="width:224.5390625px">1,500 – 2,000</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8046-8373-f3598625a0b8"><td id="TbTc" class="" style="width:248.1328125px">Data Engineer</td><td id="iYuc" class="" style="width:224.5390625px">2,000 – 3,000</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-805b-889a-e65c45a6a6ea"><td id="TbTc" class="" style="width:248.1328125px">DevOps / Automation</td><td id="iYuc" class="" style="width:224.5390625px">1,800 – 2,500</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-808e-8969-fffb68c3ad67" class="">➡️ <strong>Total monthly burn:</strong> ~16,000–20,000 USD</p></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-809c-a088-ddb606c1fc84" class="">➡️ <strong>Total annual burn:</strong> ~200–240K USD — lean but elite team capable of building multi-million-dollar platforms.</p></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-80dd-b26a-d2c9b0b1fbdc"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-80b1-b4f7-f4e47e1c1f60" class=""><strong>8️⃣ Summary of leadership structure</strong></h2></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2a8c5e6f-95bd-80af-a528-c025c4632ee7" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">You (CTO / Strategy Lead)
│
├── Product Manager / Agile Coach
│    ├── Tech Architect (reports directly to you)
│    │     ├── Backend Team (2)
│    │     ├── Frontend Dev
│    │     ├── Flutter Dev
│    │     ├── DevOps / Automation
│    │     └── Data Engineer
│    └── Designer (reports to you functionally)</code></pre></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80dc-9e59-d2d1d2c0e0c6" class="">You focus on <em>vision, partnerships, and user experience</em>.</p></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-8090-b3a9-fb6fbc831d6d" class="">Your PM &amp; Architect focus on <em>execution, sprint rhythm, and quality control.</em></p></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-800a-bfb3-e045973fe464"/></div><div style="display:contents" dir="auto"><h3 id="2a8c5e6f-95bd-803f-96c5-e36fb8f12199" class=""><strong>In summary</strong></h3></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80fb-8933-e0a62d24e771" class="">You don’t need 30 people — you need <strong>10 strategic hires, disciplined process, and clarity of direction. </strong>That combination — <em>your CX + design brain + a strong architect + agile execution layer</em> — is exactly how world-class platforms like Gojek and Tesla’s internal apps were built in their first years.</p></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-80e6-9ddf-d8222c026704"/></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-805b-a22f-cf62c77a3a04" class="">Rất hay — dưới đây là <strong>phiên bản cập nhật của kế hoạch tuyển dụng UniPower</strong> với <strong>mức lương quy đổi sang VNĐ</strong>, theo <strong>mặt bằng thị trường hiện tại (2025)</strong> cho nhân sự công nghệ trung – cao cấp tại Việt Nam (TP.HCM / Hà Nội).</p></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-8001-819c-ec61ba2e3711" class="">Số liệu này được tính theo <strong>giá thị trường freelancer + nhân sự chính thức</strong>, dựa trên khảo sát 2024–2025 của TopDev, Glints và GEEK Up.</p></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-80f9-b2af-c2c72bf0bbf8"/></div><div style="display:contents" dir="auto"><h1 id="2a8c5e6f-95bd-803b-975b-d7fc411dc434" class=""><strong>🧭</strong></h1></div><div style="display:contents" dir="auto"><h1 id="2a8c5e6f-95bd-800a-ad3c-db0f40890e2b" class=""><strong>KẾ HOẠCH TUYỂN DỤNG &amp; NHÂN SỰ CÔNG NGHỆ UNIPOWER (PHIÊN BẢN VNĐ)</strong></h1></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-80be-b25a-ce50a0c918e6"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-8075-960d-c461f32f7f86" class=""><strong>I. CẤU TRÚC NHÓM NÒNG CỐT (FULL-TIME CORE TEAM)</strong></h2></div><div style="display:contents" dir="ltr"><table id="2a8c5e6f-95bd-80f0-b094-f24e372f0b13" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-805f-9410-c7ee20bcda9e"><th id="edFN" class="simple-table-header-color simple-table-header"><strong>Vị trí</strong></th><th id="Jfh@" class="simple-table-header-color simple-table-header"><strong>Mức lương thị trường (VNĐ/tháng)</strong></th><th id="ZTxA" class="simple-table-header-color simple-table-header"><strong>Ghi chú / Vai trò</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80ac-af1d-cb3c91c187df"><td id="edFN" class=""><strong>Tech Architect / Lead Engineer</strong></td><td id="Jfh@" class="">60 – 90 triệu</td><td id="ZTxA" class="">Thiết kế kiến trúc, review code, quản lý toàn bộ kỹ thuật.</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8088-b1c0-e9dc0e34e1bd"><td id="edFN" class=""><strong>Product Manager / Agile Coordinator</strong></td><td id="Jfh@" class="">40 – 65 triệu</td><td id="ZTxA" class="">Chia sprint, quản lý tiến độ, kết nối kinh doanh – kỹ thuật.</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8080-855c-eb016027c00e"><td id="edFN" class=""><strong>Designer (UI/UX)</strong></td><td id="Jfh@" class="">25 – 45 triệu</td><td id="ZTxA" class="">Thiết kế giao diện, hệ thống nhận diện sản phẩm.</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-803f-9460-e6856b2885d9"><td id="edFN" class=""><strong>CTO / Strategic Lead (Anh/Chị)</strong></td><td id="Jfh@" class="">—</td><td id="ZTxA" class="">Định hướng sản phẩm, tích hợp hệ sinh thái, giám sát chất lượng.</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-8092-b759-c0533781d8d4" class="">➡️ <strong>Tổng chi phí nhóm nòng cốt:</strong> khoảng <strong>125 – 200 triệu VNĐ/tháng</strong></p></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-809d-869e-cbbf49e657d1" class="">➡️ 4 người này là “bộ não vận hành liên tục” – không thay đổi, không thuê theo dự án.</p></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-80d8-9aee-d3d0eb21b848"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-80a8-91df-cc11eb760503" class=""><strong>II. NHÓM LINH HOẠT (FREELANCE / CONTRACT)</strong></h2></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80d1-a4b8-c871f73df1b9" class="">Tham gia theo module hoặc dự án (3–6 tháng). Có thể ký hợp đồng dịch vụ (Service Contract) hoặc freelance có hóa đơn.</p></div><div style="display:contents" dir="ltr"><table id="2a8c5e6f-95bd-809a-9d45-d326ae7a8f7b" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-809f-bf94-ecb6d9a88052"><th id="FhDa" class="simple-table-header-color simple-table-header"><strong>Vị trí</strong></th><th id="xpjD" class="simple-table-header-color simple-table-header"><strong>Mức lương / phí trung bình (VNĐ/tháng)</strong></th><th id="ay`d" class="simple-table-header-color simple-table-header"><strong>Hình thức</strong></th><th id="~rss" class="simple-table-header-color simple-table-header"><strong>Ghi chú</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80d8-b9e5-fb15bf468f95"><td id="FhDa" class=""><strong>Backend Developer (2 người)</strong></td><td id="xpjD" class="">25 – 40 triệu/người</td><td id="ay`d" class="">Hợp đồng 3–6 tháng</td><td id="~rss" class="">Tham gia khi phát triển module mới.</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8043-a67d-e7558754988e"><td id="FhDa" class=""><strong>Flutter Developer</strong></td><td id="xpjD" class="">20 – 35 triệu</td><td id="ay`d" class="">Retainer (40–60h/tháng)</td><td id="~rss" class="">Duy trì và cập nhật app UniTaxi.</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80da-87f4-fe2ae2d73933"><td id="FhDa" class=""><strong>Frontend Developer (React)</strong></td><td id="xpjD" class="">20 – 35 triệu</td><td id="ay`d" class="">Theo milestone hoặc tháng</td><td id="~rss" class="">Dashboard, website, CMS.</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8017-a102-caa0a12b2d03"><td id="FhDa" class=""><strong>DevOps / Automation Engineer</strong></td><td id="xpjD" class="">15 – 30 triệu</td><td id="ay`d" class="">Theo giờ hoặc dự án</td><td id="~rss" class="">CI/CD, bảo trì server, tối ưu hạ tầng.</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8056-b861-e800b87d904f"><td id="FhDa" class=""><strong>Data Engineer / AI Developer</strong></td><td id="xpjD" class="">25 – 45 triệu</td><td id="ay`d" class="">Theo dự án</td><td id="~rss" class="">Tích hợp AI, dashboard dữ liệu, scoring.</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-8063-994d-d660505def5a" class="">➡️ <strong>Tổng chi phí trung bình nhóm linh hoạt:</strong> khoảng <strong>100 – 150 triệu VNĐ/tháng (tuỳ khối lượng)</strong></p></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-8019-89c0-e5dfbd8fe28a"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-8081-b9d5-d4bd5a77c85e" class=""><strong>III. TỔNG NGÂN SÁCH DỰ KIẾN</strong></h2></div><div style="display:contents" dir="ltr"><table id="2a8c5e6f-95bd-80b8-9831-fcbb9ccfc998" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8088-b04d-fb59f95566c4"><th id="?QEm" class="simple-table-header-color simple-table-header"><strong>Nhóm</strong></th><th id="@&lt;za" class="simple-table-header-color simple-table-header"><strong>Chi phí ước tính / tháng (VNĐ)</strong></th><th id="rNfb" class="simple-table-header-color simple-table-header"><strong>Ghi chú</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-804e-a184-cf7ea15106b5"><td id="?QEm" class="">Nhóm nòng cốt (4 người)</td><td id="@&lt;za" class="">125 – 200 triệu</td><td id="rNfb" class="">Duy trì liên tục</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8064-8886-dd87a8ab1cb9"><td id="?QEm" class="">Nhóm linh hoạt (5–6 người)</td><td id="@&lt;za" class="">100 – 150 triệu</td><td id="rNfb" class="">Tùy module / giai đoạn</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8091-89e8-dc8289327e44"><td id="?QEm" class=""><strong>Tổng chi phí trung bình</strong></td><td id="@&lt;za" class=""><strong>230 – 320 triệu/tháng</strong></td><td id="rNfb" class="">≈ <strong>2.7 – 3.8 tỷ/năm</strong></td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80f8-9ecb-db781ab8706a" class="">💡 <em>Chi phí này tương đương chỉ bằng 30–40% so với đội in-house full-time quy mô tương đương ở doanh nghiệp lớn.</em></p></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-80b7-af8d-e55c5e6d078d"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-80cb-b703-d3aa025305c5" class=""><strong>IV. LỘ TRÌNH TUYỂN DỤNG 6 THÁNG</strong></h2></div><div style="display:contents" dir="ltr"><table id="2a8c5e6f-95bd-8014-8641-e5ffcebae13b" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8025-8ae8-dbb0f4fbcf0b"><th id="scWx" class="simple-table-header-color simple-table-header"><strong>Giai đoạn</strong></th><th id="NMVb" class="simple-table-header-color simple-table-header"><strong>Vị trí ưu tiên</strong></th><th id="gaA{" class="simple-table-header-color simple-table-header"><strong>Mục tiêu</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-800b-8f73-d4a4c7f51605"><td id="scWx" class=""><strong>Tháng 1–2</strong></td><td id="NMVb" class="">Tech Architect, PM, Designer</td><td id="gaA{" class="">Thiết lập khung tổ chức, quy trình, sản phẩm lõi.</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8007-ba59-e7f1e3130a02"><td id="scWx" class=""><strong>Tháng 3–4</strong></td><td id="NMVb" class="">Backend (2), Flutter Dev</td><td id="gaA{" class="">Hoàn thiện API + ứng dụng di động.</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80bf-84c1-dfd63c30cab4"><td id="scWx" class=""><strong>Tháng 5–6</strong></td><td id="NMVb" class="">Frontend, DevOps</td><td id="gaA{" class="">Dashboard &amp; website UniPower 2.0.</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-80f1-963d-ca7155e357af"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-80c1-b222-e15c1c276526" class=""><strong>V. MÔ HÌNH HỢP TÁC &amp; THANH TOÁN</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2a8c5e6f-95bd-8002-989d-fed8f59f80aa" class=""><strong>1️⃣ Phương án trả lương / phí</strong></h3></div><div style="display:contents" dir="ltr"><table id="2a8c5e6f-95bd-8069-a77f-f45f9d955514" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8003-90c1-cd1a3bdbdc68"><th id="_ETG" class="simple-table-header-color simple-table-header"><strong>Loại nhân sự</strong></th><th id="fqmU" class="simple-table-header-color simple-table-header"><strong>Hình thức thanh toán</strong></th><th id="dhgN" class="simple-table-header-color simple-table-header"><strong>Ghi chú</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-804c-8289-ff494c894fae"><td id="_ETG" class="">Full-time core</td><td id="fqmU" class="">Trả lương cố định hàng tháng</td><td id="dhgN" class="">Ký HĐLĐ hoặc hợp đồng tư vấn dài hạn.</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8042-b7ea-d6dfbad887b1"><td id="_ETG" class="">Freelancer / Contract</td><td id="fqmU" class="">Trả theo milestone hoặc sprint (2 tuần/lần)</td><td id="dhgN" class="">Thanh toán khi hoàn thành đầu việc, có checklist nghiệm thu.</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h3 id="2a8c5e6f-95bd-8029-b684-dfb8b69c61c9" class=""><strong>2️⃣ Chính sách thưởng</strong></h3></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-8090-aeca-ddec177e7744" class="bulleted-list"><li style="list-style-type:disc">Thưởng theo tiến độ (5–10% milestone nếu hoàn thành sớm).</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-8067-a75b-c6553347d575" class="bulleted-list"><li style="list-style-type:disc">Thưởng hiệu suất hàng quý cho nhóm nòng cốt.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-80b6-b323-e8c101fa7f19" class="bulleted-list"><li style="list-style-type:disc">Chính sách bonus theo sản phẩm (AI, fintech, API hub) sau khi go-live thành công.</li></ul></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-800d-8d13-ce66c19a12b5"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-8011-aa78-d93218a25188" class=""><strong>VI. CHÍNH SÁCH VÀ QUY TRÌNH QUẢN LÝ NHÂN SỰ LINH HOẠT</strong></h2></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-8054-8ded-fb6a6a4cec69" class="bulleted-list"><li style="list-style-type:disc"><strong>Mọi task</strong> phải có trong Notion / ClickUp, gắn sprint ID, có người duyệt.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-804e-a692-e7f6a748efd6" class="bulleted-list"><li style="list-style-type:disc"><strong>Mọi freelancer</strong> ký <strong>NDA + Hợp đồng chuyển giao IP (Intellectual Property Transfer)</strong> trước khi bắt đầu.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-809b-8eed-eca43ff395b7" class="bulleted-list"><li style="list-style-type:disc"><strong>PM / Tech Architect</strong> chịu trách nhiệm duyệt đầu ra kỹ thuật trước khi thanh toán.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-803c-b455-f1d6cf605e53" class="bulleted-list"><li style="list-style-type:disc"><strong>Không trả phí theo giờ</strong> — chỉ trả theo đầu việc hoàn thành, demo rõ ràng.</li></ul></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-808e-8085-c2e670e26bf9"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-80c9-b6d6-f7a66c1e6680" class=""><strong>VII. KHI NÀO CẦN MỞ RỘNG FULL-TIME</strong></h2></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80dc-a26a-c81a3d67db6a" class="">Chỉ mở rộng đội full-time khi:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2a8c5e6f-95bd-80ee-ad98-df3cbec504e3" class="numbered-list" start="1"><li>UniPower có <strong>≥3 sản phẩm hoạt động song song</strong> (app, fintech, AI, automation).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2a8c5e6f-95bd-8037-9d4c-f9eb3c86524e" class="numbered-list" start="2"><li>Có <strong>nguồn doanh thu / hợp đồng ổn định từ chính phủ hoặc doanh nghiệp lớn.</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2a8c5e6f-95bd-80d8-82b5-f74cb767379c" class="numbered-list" start="3"><li>Cần vận hành <strong>hệ thống dữ liệu &amp; thanh toán 24/7.</strong></li></ol></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80bb-9a05-cb387328b238" class="">Khi đó, nên tuyển:</p></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-8013-bf2c-e8f47aa25e4c" class="bulleted-list"><li style="list-style-type:disc"><strong>01 DevOps cố định.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-8053-8ac4-c1530592cbb2" class="bulleted-list"><li style="list-style-type:disc"><strong>01 Backend chính thức.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-8033-ba08-cffc3133ef0c" class="bulleted-list"><li style="list-style-type:disc"><strong>01 QA Automation / Tester.</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-8081-86bc-ed60f37b05d4"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-8006-8d4e-d8496ebdf9b0" class=""><strong>VIII. LỢI THẾ MÔ HÌNH FREELANCE – HYBRID TECH POD</strong></h2></div><div style="display:contents" dir="ltr"><table id="2a8c5e6f-95bd-806e-a590-f5cf45d5e466" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8086-920a-f8c58613db49"><th id="jULC" class="simple-table-header-color simple-table-header"><strong>Tiêu chí</strong></th><th id="HYX:" class="simple-table-header-color simple-table-header"><strong>Ưu thế cụ thể</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8057-876e-c188fb0f9932"><td id="jULC" class=""><strong>Chi phí</strong></td><td id="HYX:" class="">Giảm 70–80% so với đội in-house.</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80e0-866e-c6e41c8eaa99"><td id="jULC" class=""><strong>Tốc độ triển khai</strong></td><td id="HYX:" class="">Có thể khởi động module mới trong 1–2 tuần.</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8077-8e30-e7e3b925dd2a"><td id="jULC" class=""><strong>Linh hoạt mở rộng</strong></td><td id="HYX:" class="">Tăng/giảm nhân sự theo khối lượng công việc.</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-80e4-83b2-cb50b43a0917"><td id="jULC" class=""><strong>Quản trị rõ ràng</strong></td><td id="HYX:" class="">Có PM và Tech Architect kiểm soát toàn bộ tiến độ.</td></tr></div><div style="display:contents" dir="ltr"><tr id="2a8c5e6f-95bd-8055-8d28-f538940df765"><td id="jULC" class=""><strong>Rủi ro thấp</strong></td><td id="HYX:" class="">Không phát sinh lương cố định khi tạm ngưng dự án.</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-8097-b7ac-d3654689684a"/></div><div style="display:contents" dir="auto"><h2 id="2a8c5e6f-95bd-80b1-b388-dd00c2ffd940" class=""><strong>IX. KẾT LUẬN</strong></h2></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-80b0-bacc-cf488e10d2e8" class="">Mô hình <strong>Hybrid Tech Pod</strong> là lựa chọn tối ưu cho giai đoạn hiện tại của UniPower:</p></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-8035-9580-e2c6266707e4" class="bulleted-list"><li style="list-style-type:disc">Tập trung nguồn lực vào chiến lược, trải nghiệm và sản phẩm cốt lõi.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-809a-b92f-fb258fc18166" class="bulleted-list"><li style="list-style-type:disc">Giữ chi phí nhân sự linh hoạt, dễ kiểm soát.</li></ul></div><div style="display:contents" dir="auto"><ul id="2a8c5e6f-95bd-80b4-b6ad-d7e3ec5a1e45" class="bulleted-list"><li style="list-style-type:disc">Đảm bảo tốc độ phát triển song song nhiều nền tảng (App – Fintech – AI – Automation – Website).</li></ul></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-8077-8f0c-d44daee474a4" class="">Tổng ngân sách khoảng <strong>230–320 triệu VNĐ/tháng</strong> là hợp lý để duy trì tốc độ phát triển của một doanh nghiệp công nghệ quốc gia đang mở rộng.</p></div><div style="display:contents" dir="auto"><hr id="2a8c5e6f-95bd-801f-b963-fc8dcbc6220f"/></div><div style="display:contents" dir="auto"><p id="2a8c5e6f-95bd-8071-8cf9-c48e63a19db3" class="">Anh/chị có muốn tôi viết thêm <strong>bộ JD chi tiết + mô tả đầu ra 90 ngày</strong> cho từng vị trí (kèm mức lương cụ thể theo năng lực) để bắt đầu đăng tuyển ngay trên TopDev / ITviec / LinkedIn không?</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
