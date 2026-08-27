---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Resource Planning Matrix </title><style>
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
	
</style></head><body><article id="24ac5e6f-95bd-804d-b993-daca47b66dc2" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Resource Planning Matrix</strong> </h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-803c-829f-c62b81457e86" class=""><strong>1. Core Governance &amp; Legal</strong></h2></div><div style="display:contents" dir="ltr"><table id="24ac5e6f-95bd-8056-8e70-c105c521356f" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-807f-af45-e090d0f00788"><th id="&gt;P^^" class="simple-table-header-color simple-table-header">Role</th><th id="rIF&lt;" class="simple-table-header-color simple-table-header">FTE</th><th id="&lt;LEu" class="simple-table-header-color simple-table-header">Phase(s)</th><th id="`z[O" class="simple-table-header-color simple-table-header">Monthly Cost (USD)</th><th id="vXPw" class="simple-table-header-color simple-table-header">Notes</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-807a-b476-fb78220aa383"><td id="&gt;P^^" class="">General Counsel (Data/IP)</td><td id="rIF&lt;" class="">0.5</td><td id="&lt;LEu" class="">0–6</td><td id="`z[O" class="">$12k</td><td id="vXPw" class="">GDPR/DPA + IP licensing expertise</td></tr></div><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-800a-b52f-dd927efa3262"><td id="&gt;P^^" class="">Compliance Officer</td><td id="rIF&lt;" class="">1.0</td><td id="&lt;LEu" class="">0–6</td><td id="`z[O" class="">$9k</td><td id="vXPw" class="">Oversees ISO, DPIAs, audits</td></tr></div><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-8053-83fe-e693de23c355"><td id="&gt;P^^" class="">Data Protection Officer (DPO)</td><td id="rIF&lt;" class="">0.25</td><td id="&lt;LEu" class="">0–6</td><td id="`z[O" class="">$4k</td><td id="vXPw" class="">Mandatory under GDPR</td></tr></div><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-8034-94bc-f3ca8c5c542b"><td id="&gt;P^^" class="">DAO Governance Lead</td><td id="rIF&lt;" class="">0.5</td><td id="&lt;LEu" class="">0–6</td><td id="`z[O" class="">$6k</td><td id="vXPw" class="">Oversees multi-sig ops &amp; proposals</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-8048-8867-fcd0d4ddc2a2"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-80eb-bccf-f35d30ee53c5" class=""><strong>2. Engineering</strong></h2></div><div style="display:contents" dir="ltr"><table id="24ac5e6f-95bd-80da-bd2e-d727462ad7bf" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-80ae-97b7-fca81dae2167"><th id="fY[F" class="simple-table-header-color simple-table-header">Role</th><th id="OypW" class="simple-table-header-color simple-table-header">FTE</th><th id="eLr{" class="simple-table-header-color simple-table-header">Phase(s)</th><th id="{tMX" class="simple-table-header-color simple-table-header">Monthly Cost</th><th id="oFyt" class="simple-table-header-color simple-table-header">Notes</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-8028-bf25-fece2d1539d6"><td id="fY[F" class="">Blockchain Engineer (PoSg)</td><td id="OypW" class="">2.0</td><td id="eLr{" class="">1–4</td><td id="{tMX" class="">$20k</td><td id="oFyt" class="">Hyperledger, Canton, smart contracts</td></tr></div><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-8007-8956-c1bebafeba88"><td id="fY[F" class="">Full-Stack Cloud Engineer</td><td id="OypW" class="">2.0</td><td id="eLr{" class="">1–5</td><td id="{tMX" class="">$18k</td><td id="oFyt" class="">Multi-cloud, sovereign APIs</td></tr></div><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-80f4-bb7a-eec9945fcca2"><td id="fY[F" class="">Data Pipeline Engineer</td><td id="OypW" class="">1.0</td><td id="eLr{" class="">2–6</td><td id="{tMX" class="">$9k</td><td id="oFyt" class="">ETL, anonymization, consent registry</td></tr></div><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-8025-bf51-ffc7eff90e1f"><td id="fY[F" class="">DevOps/SRE</td><td id="OypW" class="">1.0</td><td id="eLr{" class="">1–6</td><td id="{tMX" class="">$8k</td><td id="oFyt" class="">CI/CD, failover automation</td></tr></div><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-80f8-beee-d2b5ecd14abc"><td id="fY[F" class="">Security Engineer (Hardware Attestation)</td><td id="OypW" class="">0.5</td><td id="eLr{" class="">3–4</td><td id="{tMX" class="">$5k</td><td id="oFyt" class="">TPM/TEE integration</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80cf-b9e6-d2a5108ecc71"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-80c8-a934-f5968498b6ac" class=""><strong>3. Data Operations</strong></h2></div><div style="display:contents" dir="ltr"><table id="24ac5e6f-95bd-8097-916c-e0681b25e019" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-80fd-b99f-c8d3bcd9ee18"><th id="RuWZ" class="simple-table-header-color simple-table-header">Role</th><th id="D@\O" class="simple-table-header-color simple-table-header">FTE</th><th id="Jgd:" class="simple-table-header-color simple-table-header">Phase(s)</th><th id="KrOM" class="simple-table-header-color simple-table-header">Monthly Cost</th><th id="{:p?" class="simple-table-header-color simple-table-header">Notes</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-80fa-abe8-cc0d6582da6d"><td id="RuWZ" class="">Data Steward</td><td id="D@\O" class="">1.0</td><td id="Jgd:" class="">2–6</td><td id="KrOM" class="">$7k</td><td id="{:p?" class="">Manages metadata integrity</td></tr></div><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-804e-a96a-ef9edb0314cd"><td id="RuWZ" class="">Anonymization Specialist</td><td id="D@\O" class="">0.5</td><td id="Jgd:" class="">4–6</td><td id="KrOM" class="">$4k</td><td id="{:p?" class="">Designs pseudonymization pipeline</td></tr></div><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-800b-9664-c2fd3b3aadef"><td id="RuWZ" class="">Database Administrator (DBA)</td><td id="D@\O" class="">0.5</td><td id="Jgd:" class="">2–6</td><td id="KrOM" class="">$4k</td><td id="{:p?" class="">Sovereign DB performance + security</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-8028-8ea1-edacca54c922"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8070-8d61-fb9dcc97285e" class=""><strong>4. Security &amp; Compliance</strong></h2></div><div style="display:contents" dir="ltr"><table id="24ac5e6f-95bd-801d-9a65-e3ad9d63157b" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-8041-8480-e0453e904e97"><th id="&lt;;mU" class="simple-table-header-color simple-table-header">Role</th><th id="PWEY" class="simple-table-header-color simple-table-header">FTE</th><th id="XIO{" class="simple-table-header-color simple-table-header">Phase(s)</th><th id="\@a]" class="simple-table-header-color simple-table-header">Monthly Cost</th><th id="iJuP" class="simple-table-header-color simple-table-header">Notes</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-80a5-8d94-d64a236a9dfb"><td id="&lt;;mU" class="">CISO</td><td id="PWEY" class="">0.25</td><td id="XIO{" class="">0–6</td><td id="\@a]" class="">$6k</td><td id="iJuP" class="">Security strategy &amp; audits</td></tr></div><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-806b-bdda-ce4d9d5d50ee"><td id="&lt;;mU" class="">Penetration Tester</td><td id="PWEY" class="">contract</td><td id="XIO{" class="">Qtrly</td><td id="\@a]" class="">$15k/qtr</td><td id="iJuP" class="">External security testing</td></tr></div><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-8037-b28e-f1a1eae09e78"><td id="&lt;;mU" class="">ISO Auditor</td><td id="PWEY" class="">contract</td><td id="XIO{" class="">as needed</td><td id="\@a]" class="">$10k/audit</td><td id="iJuP" class="">Pre-cert &amp; recertification</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80cd-8d5f-ccf0a4c1076a"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-804b-8b22-ca3a63ee6b1d" class=""><strong>5. Partnerships &amp; Procurement</strong></h2></div><div style="display:contents" dir="ltr"><table id="24ac5e6f-95bd-80a6-b355-c4c692818900" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-80d1-a63c-faea613da7b7"><th id="|b:d" class="simple-table-header-color simple-table-header">Role</th><th id="i&lt;Jb" class="simple-table-header-color simple-table-header">FTE</th><th id="yNC[" class="simple-table-header-color simple-table-header">Phase(s)</th><th id="uNUY" class="simple-table-header-color simple-table-header">Monthly Cost</th><th id="pmDa" class="simple-table-header-color simple-table-header">Notes</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-802c-ab55-f62d00794615"><td id="|b:d" class="">Business Dev Lead</td><td id="i&lt;Jb" class="">1.0</td><td id="yNC[" class="">1–6</td><td id="uNUY" class="">$8k</td><td id="pmDa" class="">Partner acquisition &amp; SLAs</td></tr></div><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-8039-ac7b-c8274b5cf943"><td id="|b:d" class="">Procurement Officer</td><td id="i&lt;Jb" class="">0.5</td><td id="yNC[" class="">1–6</td><td id="uNUY" class="">$4k</td><td id="pmDa" class="">Vendor contract negotiation</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80dd-96c9-f61170d70e2e"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-802d-bfdf-c7c13b9f2b0d" class=""><strong>6. Finance</strong></h2></div><div style="display:contents" dir="ltr"><table id="24ac5e6f-95bd-8065-a81e-f995a03448a8" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-80e7-9462-fbfed7460f61"><th id="FwP{" class="simple-table-header-color simple-table-header">Role</th><th id="\BO?" class="simple-table-header-color simple-table-header">FTE</th><th id="Sa`M" class="simple-table-header-color simple-table-header">Phase(s)</th><th id="Lo~;" class="simple-table-header-color simple-table-header">Monthly Cost</th><th id="khAF" class="simple-table-header-color simple-table-header">Notes</th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-80f4-aa48-e5f5e01027be"><td id="FwP{" class="">Financial Controller</td><td id="\BO?" class="">0.5</td><td id="Sa`M" class="">0–6</td><td id="Lo~;" class="">$6k</td><td id="khAF" class="">Budget tracking, reporting</td></tr></div><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-80b9-bb5e-f965fbd878b8"><td id="FwP{" class="">Crypto Treasury Manager</td><td id="\BO?" class="">0.25</td><td id="Sa`M" class="">1–6</td><td id="Lo~;" class="">$5k</td><td id="khAF" class="">BTC reward pool ops</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-8041-a487-f8c5122df170"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8062-b5b2-ff8b2ee75889" class=""><strong>Estimated Monthly Burn (Full Build-Out)</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8008-b2e3-d83f626bc79a" class="bulleted-list"><li style="list-style-type:disc"><strong>Peak Months (Phase 2–4)</strong>: ~$150k/month (staff + contracts + infra)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8037-acd4-f29024ea4d7c" class="bulleted-list"><li style="list-style-type:disc"><strong>Ramp-Up Months (Phase 0–1)</strong>: ~$60k–$80k/month</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8093-9450-f334bdc74c88" class="bulleted-list"><li style="list-style-type:disc"><strong>Post-Scale (Phase 6)</strong>: ~$90k–$110k/month (lean ops, governance heavy)</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-8066-a3dc-c080c06999b4"/></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-805b-9b05-e558ca01f707" class="">Here’s the <strong>Mermaid Gantt chart</strong> with role timelines, phase alignment, and monthly cost overlay for your Signal Economy rollout.</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="24ac5e6f-95bd-8054-a6bb-c9dae09d6942" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">gantt
    title Resource Deployment Plan — Signal Economy Rollout
    dateFormat  YYYY-MM-DD
    axisFormat  %b %Y
    section Governance &amp; Legal
    General Counsel ($12k)          :active, gc, 2025-08-15, 24m
    Compliance Officer ($9k)        :active, comp, 2025-08-15, 24m
    DPO ($4k)                        :active, dpo, 2025-08-15, 24m
    DAO Governance Lead ($6k)       :active, dao, 2025-08-15, 24m

    section Engineering
    Blockchain Engineer x2 ($20k)   :active, bceng, 2025-10-01, 12m
    Full-Stack Cloud Eng x2 ($18k)  :active, cloud, 2025-10-01, 15m
    Data Pipeline Engineer ($9k)    :active, dataeng, 2026-01-01, 18m
    DevOps/SRE ($8k)                 :active, devops, 2025-10-01, 20m
    Security Eng ($5k)               :active, seceng, 2026-03-01, 8m

    section Data Operations
    Data Steward ($7k)               :active, steward, 2026-01-01, 18m
    Anonymization Spec ($4k)         :active, anon, 2026-06-01, 12m
    DBA ($4k)                         :active, dba, 2026-01-01, 18m

    section Security &amp; Compliance
    CISO ($6k)                        :active, ciso, 2025-08-15, 24m
    Pen Tester ($15k/qtr)             :milestone, pentest, 2025-11-01, 3m
    ISO Auditor ($10k/audit)          :milestone, iso, 2026-04-01, 6m

    section Partnerships &amp; Procurement
    Biz Dev Lead ($8k)                :active, bizdev, 2025-10-01, 20m
    Procurement Officer ($4k)         :active, procure, 2025-10-01, 20m

    section Finance
    Controller ($6k)                  :active, ctrl, 2025-08-15, 24m
    Crypto Treasury Mgr ($5k)         :active, ctm, 2025-10-01, 20m
</code></pre></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-805d-aee5-c458342cb303" class=""><strong>How to read this:</strong></p></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80bc-86e3-d2b145256586" class="bulleted-list"><li style="list-style-type:disc"><strong>Green bars</strong> (active) = ongoing monthly engagement.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8096-b148-e0da1e1e19f7" class="bulleted-list"><li style="list-style-type:disc"><strong>Diamonds</strong> (milestone) = point-in-time contract deliverable (pen tests, audits).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80ed-bcb8-eafeb546f88e" class="bulleted-list"><li style="list-style-type:disc">Dates are anchored to a start of <strong>Aug 15, 2025</strong> for planning purposes.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80ee-b7b0-dbd060ea6777" class="bulleted-list"><li style="list-style-type:disc">Costs shown per month or per occurrence.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-8063-abe0-e7f2d0addfd8"/></div><div style="display:contents" dir="auto"><h1 id="24ac5e6f-95bd-8098-b834-c8ddee44042b" class="">Combined rollout + resourcing (single Gantt)</h1></div><div style="display:contents" dir="auto"><pre id="24ac5e6f-95bd-808f-908b-f7024a68f3a7" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">gantt
    dateFormat  YYYY-MM-DD
    axisFormat  %b %Y
    title Signal Economy — Phases • Partners • Roles (Unified Plan)

    %% =======================
    %% TRACK A — Program Phases (from your rollout plan)
    %% =======================
    section Program Phases
    Phase 0 — Foundational (100% founder)                 :done, p0, 2025-08-15, 30d
    Phase 1 — Governance Install (80/20)                  :p1, after p0, 40d
    Phase 2 — Sovereign Hosting                           :p2, after p1, 90d
    Phase 3 — Security Certification                      :p3, after p2, 90d
    Phase 4 — Monetization Layer                          :p4, after p3, 90d
    Phase 5 — Beta Network Launch (20/80)                 :p5, after p4, 45d
    Phase 6 — Global Activation (≥70% participant)        :milestone, p6, after p5, 0d

    %% =======================
    %% TRACK B — Partners (aligned to phases)
    %% =======================
    section Partners
    Hyperledger (Consent/Rewards Ledger)                  :b1, 2025-09-20, 120d
    OVHcloud (EU, SecNumCloud)                            :b2, 2025-10-01, 120d
    Open Telekom Cloud (ISO/BSI C5)                       :b3, after b2, 100d
    Virt8ra Sovereign Edge                                :b4, after b3, 120d
    Canton Network (Licensing rails)                      :b5, after b4, 60d
    AWS European Sovereign Cloud                          :b6, 2026-04-01, 120d
    Microsoft Cloud for Sovereignty                       :b7, after b6, 120d
    Google Sovereign Controls + S3NS                      :b8, after b7, 120d

    %% =======================
    %% TRACK C — Compliance &amp; Security
    %% =======================
    section Compliance &amp; Security
    ISO 27001/27701 Prep + Gap Fix                        :c1, 2025-10-10, 60d
    Hardware Attestation Rollout                          :c2, after c1, 30d
    Compliance Audit + DPO                                :c3, after c2, 35d

    %% =======================
    %% TRACK D — Monetization
    %% =======================
    section Monetization
    Reward Logic Integration                              :m1, 2025-12-01, 30d
    Licensing Framework                                   :m2, after m1, 25d
    Pseudonymization Tooling                              :m3, after m2, 20d

    %% =======================
    %% TRACK E — Resources (roles with monthly cost)
    %% =======================
    section Resources (Monthly Cost in $)
    General Counsel ($12k)                                :active, r1, 2025-08-15, 24m
    Compliance Officer ($9k)                              :active, r2, 2025-08-15, 24m
    DPO ($4k)                                             :active, r3, 2025-08-15, 24m
    DAO Gov Lead ($6k)                                    :active, r4, 2025-08-15, 24m

    Blockchain Eng ×2 ($20k)                              :active, r5, 2025-10-01, 12m
    Full‑Stack Cloud Eng ×2 ($18k)                        :active, r6, 2025-10-01, 15m
    DevOps/SRE ($8k)                                      :active, r7, 2025-10-01, 20m
    Data Pipeline Eng ($9k)                               :active, r8, 2026-01-01, 18m
    Security Eng ($5k)                                    :active, r9, 2026-03-01, 8m

    Data Steward ($7k)                                    :active, r10, 2026-01-01, 18m
    Anonymization Specialist ($4k)                        :active, r11, 2026-06-01, 12m
    DBA ($4k)                                             :active, r12, 2026-01-01, 18m

    CISO ($6k)                                            :active, r13, 2025-08-15, 24m
    Biz Dev Lead ($8k)                                    :active, r14, 2025-10-01, 20m
    Procurement ($4k)                                     :active, r15, 2025-10-01, 20m
    Controller ($6k)                                      :active, r16, 2025-08-15, 24m
    Crypto Treasury Manager ($5k)                         :active, r17, 2025-10-01, 20m

    %% =======================
    %% TRACK F — Launch
    %% =======================
    section Launch
    Beta Network Online                                   :l1, after c3, 45d
    Global Activation (Milestone)                         :milestone, l2, after l1, 0d
</code></pre></div><div style="display:contents" dir="auto"><h1 id="24ac5e6f-95bd-805d-ab14-d17370be1972" class="">Cumulative cost curve (illustrative, monthly burn)</h1></div><div style="display:contents" dir="auto"><blockquote id="24ac5e6f-95bd-80db-9319-da9e34062fcb" class="">Note: This is an estimate based on earlier ranges (ramp $60–80k/mo, peak ~$150k/mo, post‑scale $90–110k/mo). Adjust the points as you finalize vendor quotes and hires.</blockquote></div><div style="display:contents" dir="auto"><pre id="24ac5e6f-95bd-8083-828b-e704a16ceb7d" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">xychart-beta
    title &quot;Cumulative Spend — Months 1–24 (USD, illustrative)&quot;
    x-axis [M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12, M13, M14, M15, M16, M17, M18, M19, M20, M21, M22, M23, M24]
    y-axis &quot;USD (Millions)&quot; 0 --&gt; 3.5
    line &quot;Cumulative&quot; [0.07, 0.14, 0.22, 0.30, 0.40, 0.50, 0.62, 0.74, 0.89, 1.05, 1.22, 1.40, 1.60, 1.82, 2.05, 2.20, 2.32, 2.45, 2.58, 2.72, 2.86, 3.02, 3.18, 3.35]
</code></pre></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8077-a00a-cc94638acef9" class="">
</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
