---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>A) Account + Infrastructure Setup (Execution-only)</title><style>
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
	
</style></head><body><article id="2ddc5e6f-95bd-80e9-ace6-df548e2d0066" class="page sans"><header><h1 class="page-title" dir="auto"><strong>A) Account + Infrastructure Setup (Execution-only)</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="2ddc5e6f-95bd-8028-bb8f-f964df266bf2" class=""><strong>Task A1 — Create Launch Asset Accounts</strong></h2></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-8088-98f5-fea163893954" class=""><strong>Deliverable:</strong> launch/ops/accounts.md</p></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-8051-a42e-e30ea3bbe12d" class="">Register + store access for:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2ddc5e6f-95bd-800f-9e45-d825820ba4ea" class="numbered-list" start="1"><li>Email forwarding (support@, hello@) </li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2ddc5e6f-95bd-809d-8775-f3cb9a398ad0" class="numbered-list" start="2"><li>Newsletter platform (Beehiiv/Substack/Mailchimp)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2ddc5e6f-95bd-8021-9356-e7a95350655a" class="numbered-list" start="3"><li>Social accounts: X, LinkedIn Page, YouTube, Medium</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2ddc5e6f-95bd-80d0-98d8-f6d78b081afd" class="numbered-list" start="4"><li>Product listing accounts: Product Hunt, Hacker News, Indie Hackers</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2ddc5e6f-95bd-80b5-9d0c-c56b7f616541" class="numbered-list" start="5"><li>Community: Discord + Slack workspace (if needed)</li></ol></div><div style="display:contents" dir="auto"><p id="2dfc5e6f-95bd-8046-8aa0-e1d1dd4edad2" class="">
</p></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-807a-b58c-f037d75f4247" class=""><strong>Rules</strong></p></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-804c-b139-dd3bd28cc1a8" class="bulleted-list"><li style="list-style-type:disc">Use company email.</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8095-90e2-e1d4558d9d54" class="bulleted-list"><li style="list-style-type:disc">Save:<div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8023-97bc-edaf90e06a3e" class="bulleted-list"><li style="list-style-type:circle">URL</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8057-a3d5-f0348071fb6c" class="bulleted-list"><li style="list-style-type:circle">username</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-804b-b709-f186fb746bdf" class="bulleted-list"><li style="list-style-type:circle">password manager entry name</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80c2-a86d-d46023a7f8a3" class="bulleted-list"><li style="list-style-type:circle">2FA method</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-805f-8902-d3afc123b4d7" class="bulleted-list"><li style="list-style-type:circle">recovery codes location</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2ddc5e6f-95bd-8071-9469-e108af3e9e9f"/></div><div style="display:contents" dir="auto"><h2 id="2ddc5e6f-95bd-8066-be98-e985d0ae54d0" class=""><strong>Task A2 — Create a Launch Folder System</strong></h2></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-8088-a47c-c8dad9017b86" class=""><strong>Deliverable:</strong> Folder tree + launch/ops/folder_structure.md</p></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-801d-8e8d-d437f8329080" class="">Required structure:</p></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80db-9ecb-f9e1be369289" class="bulleted-list"><li style="list-style-type:disc">launch/<div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-808c-a170-c3e86644db54" class="bulleted-list"><li style="list-style-type:circle">ops/</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80a6-a59b-d3fa5ada2d37" class="bulleted-list"><li style="list-style-type:circle">research/</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80e3-9344-e8649fea64ce" class="bulleted-list"><li style="list-style-type:circle">copy/</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80a0-9bba-dbb858d90503" class="bulleted-list"><li style="list-style-type:circle">press/</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8048-a803-d8574362e01c" class="bulleted-list"><li style="list-style-type:circle">screenshots/</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-807f-82cd-cd85f7b8f8ea" class="bulleted-list"><li style="list-style-type:circle">demo/</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-807e-b4e1-d45132eaac56" class="bulleted-list"><li style="list-style-type:circle">pricing/</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8094-ae6d-f16ed27e20e4" class="bulleted-list"><li style="list-style-type:circle">landing/</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8041-b18b-d2e2c822e11c" class="bulleted-list"><li style="list-style-type:circle">social/</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8061-84a3-d909501d84fd" class="bulleted-list"><li style="list-style-type:circle">competitors/</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-801e-aaa7-e69f16b7ffb2" class="bulleted-list"><li style="list-style-type:circle">refs/</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2ddc5e6f-95bd-8000-98ec-cc4d9f09e258"/></div><div style="display:contents" dir="auto"><h1 id="2ddc5e6f-95bd-807f-a8e6-fdbec0196d77" class=""><strong>B) Document Reformatting (Turning Your Notes into Launch-Ready Assets)</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2ddc5e6f-95bd-808e-aabf-e2b1ab6e4bcf" class=""><strong>Task B1 — Convert Your Raw Notes into 1-page Product Brief</strong></h2></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-80a0-8049-d9be412c47a1" class=""><strong>Input:</strong> your notes (you provide)</p></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-80ff-bbdc-dfea2e543657" class=""><strong>Deliverable:</strong> launch/copy/amos_product_brief_1pager.md</p></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-80d1-a40a-cd898c0b58e8" class="">Template:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2ddc5e6f-95bd-80d9-9be8-c67347afa4f9" class="numbered-list" start="1"><li>What AMOS is (1 paragraph)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2ddc5e6f-95bd-80d2-a2e7-def7689b2f61" class="numbered-list" start="2"><li>Who it’s for (3 bullets)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2ddc5e6f-95bd-8016-b4e2-eef38f315483" class="numbered-list" start="3"><li>What problem it solves (5 bullets)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2ddc5e6f-95bd-80c0-861a-f049a00ed991" class="numbered-list" start="4"><li>Key capabilities (6 bullets)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2ddc5e6f-95bd-80f0-9650-e9d5a6733506" class="numbered-list" start="5"><li>Differentiators (3 bullets)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2ddc5e6f-95bd-80d1-ba42-d94c6372734c" class="numbered-list" start="6"><li>What exists now (what’s shipped)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2ddc5e6f-95bd-80e7-ad03-d5b40b1cabe6" class="numbered-list" start="7"><li>Next milestone (what’s next)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2ddc5e6f-95bd-80aa-ac5d-ddec6f91d7ed" class="numbered-list" start="8"><li>Call-to-action</li></ol></div><div style="display:contents" dir="auto"><hr id="2ddc5e6f-95bd-8010-b1d0-e8be3970575c"/></div><div style="display:contents" dir="auto"><h2 id="2ddc5e6f-95bd-805f-86ae-dbd0f34da64f" class=""><strong>Task B2 — Convert Your Notes into Website Copy (Clean Format)</strong></h2></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-804d-ae78-f58757632239" class=""><strong>Input:</strong> your written content</p></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-80dd-bac3-dc4317b4c4c2" class=""><strong>Deliverable:</strong> launch/landing/homepage_copy.md</p></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-802f-8936-d92c5b82445f" class="">Sections:</p></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-806d-b9c7-fa85984b5884" class="bulleted-list"><li style="list-style-type:disc">Hero headline + subheadline</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8078-99a3-f8f3dfb8ade4" class="bulleted-list"><li style="list-style-type:disc">3 value pillars</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80bb-9bdb-fd59027bde27" class="bulleted-list"><li style="list-style-type:disc">Feature list</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8096-8291-dd59c5fbf436" class="bulleted-list"><li style="list-style-type:disc">“How it works” (3 steps)</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80c4-ae67-d19838846594" class="bulleted-list"><li style="list-style-type:disc">Proof points (placeholders ok)</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-808f-ac94-cb57657575c8" class="bulleted-list"><li style="list-style-type:disc">CTA blocks</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8053-a980-e58615a64632" class="bulleted-list"><li style="list-style-type:disc">FAQ (8 questions)</li></ul></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-80ef-b1bf-c61ee085300b" class="">Junior is only formatting and structuring.</p></div><div style="display:contents" dir="auto"><hr id="2ddc5e6f-95bd-8041-8e7a-f427b1d493e8"/></div><div style="display:contents" dir="auto"><h2 id="2ddc5e6f-95bd-805f-a749-c27a0f23e6e0" class=""><strong>Task B3 — Rewrite Your Messages into Launch Posts (Tone Cleanup)</strong></h2></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-8077-acce-c9e0f81a98ad" class=""><strong>Input:</strong> your own writing</p></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-80dc-97b5-c9f08c631d63" class=""><strong>Deliverable:</strong> launch/social/posts_cleaned.md</p></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-80a7-8cf9-ff08535f17fb" class="">For each original post:</p></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80d2-b6d9-d96d4d6d06e3" class="bulleted-list"><li style="list-style-type:disc">cleaned short version (X)</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8059-bdd6-d8b369a96edf" class="bulleted-list"><li style="list-style-type:disc">cleaned long version (LinkedIn)</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80ee-8cd4-e6b47930a38e" class="bulleted-list"><li style="list-style-type:disc">a neutral “technical credibility” version</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-801e-b002-c7425f720feb" class="bulleted-list"><li style="list-style-type:disc">hashtags removed unless you instruct</li></ul></div><div style="display:contents" dir="auto"><hr id="2ddc5e6f-95bd-8018-a274-c1f28ff75d33"/></div><div style="display:contents" dir="auto"><h1 id="2ddc5e6f-95bd-806e-8add-e16379e49444" class=""><strong>C) Asset Collection + Evidence Library (No thinking, just collecting)</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2ddc5e6f-95bd-8095-ad27-dda37445a891" class=""><strong>Task C1 — Download and Organize Free High-Quality Reports (Evidence Pack)</strong></h2></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-805e-974e-c8b7ddd2577b" class=""><strong>Deliverable:</strong> launch/research/evidence_pack/ + launch/research/evidence_index.md</p></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-80b5-95bc-d3047a55caf8" class="">What to collect (minimum 20 total):</p></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80b0-a625-c02c07818f4b" class="bulleted-list"><li style="list-style-type:disc">AI governance</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8032-89d7-d40351bada9d" class="bulleted-list"><li style="list-style-type:disc">AI agent frameworks</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80a3-a27e-d9698bc12634" class="bulleted-list"><li style="list-style-type:disc">auditability/compliance in AI</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8080-9478-ccbadffa64dc" class="bulleted-list"><li style="list-style-type:disc">LLM reliability issues</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8061-9ab9-f7b1e905981c" class="bulleted-list"><li style="list-style-type:disc">enterprise AI adoption barriers</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8010-9a70-c590794763ff" class="bulleted-list"><li style="list-style-type:disc">deterministic AI / safety</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-808d-a375-ff77709c12b4" class="bulleted-list"><li style="list-style-type:disc">autonomous systems tooling</li></ul></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-8010-be32-d267130ab8e6" class=""><strong>Rules</strong></p></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8084-9ccc-d8a282a3198b" class="bulleted-list"><li style="list-style-type:disc">Only credible sources: McKinsey, BCG, Deloitte, Gartner summaries, Stanford AI Index, OECD, NIST, arXiv, IEEE, ACM, major universities.</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-803b-83fa-c6b17da21c80" class="bulleted-list"><li style="list-style-type:disc">Store the PDF locally.</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80d9-9c97-f5e5d90b6f4a" class="bulleted-list"><li style="list-style-type:disc">In index file include:<div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8014-ba3e-dcccd1cf2304" class="bulleted-list"><li style="list-style-type:circle">title</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-805f-abcd-ef2ddfeda24c" class="bulleted-list"><li style="list-style-type:circle">publisher</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80d7-9991-e2728aade1cb" class="bulleted-list"><li style="list-style-type:circle">year</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8058-ae7a-f3fff30f0a8f" class="bulleted-list"><li style="list-style-type:circle">link</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-803c-90cd-cea1eb95ae90" class="bulleted-list"><li style="list-style-type:circle">2–3 sentence summary</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8008-aaf0-ecadfb9c4b4f" class="bulleted-list"><li style="list-style-type:circle">key quote/snippet</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80ad-b230-e6c2df9e5e21" class="bulleted-list"><li style="list-style-type:circle">why it supports AMOS positioning</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-809a-967e-e9ca93f1ee3a" class="">Junior does not need to interpret deeply; summaries are descriptive.</p></div><div style="display:contents" dir="auto"><hr id="2ddc5e6f-95bd-8062-86ea-dd3617aa72a9"/></div><div style="display:contents" dir="auto"><h2 id="2ddc5e6f-95bd-8081-986d-e65538e105e6" class=""><strong>Task C2 — Build Competitor Screenshot Library</strong></h2></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-809f-9437-dbb6fd45db6e" class=""><strong>Deliverable:</strong> launch/competitors/screenshots/ + competitor_index.md</p></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-8004-b118-c3352d072bb7" class="">Pick 15 competitors.</p></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-80ee-8cfa-c05139b43a2f" class="">For each competitor:</p></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8075-86f8-f8996d0c81f4" class="bulleted-list"><li style="list-style-type:disc">homepage screenshot</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80ce-9d14-ec6ef6ccd1fa" class="bulleted-list"><li style="list-style-type:disc">pricing page screenshot (if exists)</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8008-adef-d6338ec1b931" class="bulleted-list"><li style="list-style-type:disc">docs screenshot (if exists)</li></ul></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-809f-a299-d472dfd904ba" class="">Index must include:</p></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80e6-81eb-ea08974d6790" class="bulleted-list"><li style="list-style-type:disc">URL</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80d2-9b3d-e62efab00581" class="bulleted-list"><li style="list-style-type:disc">what they claim in 1 sentence (copied)</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80ef-842b-e74af1b928e3" class="bulleted-list"><li style="list-style-type:disc">pricing (if visible)</li></ul></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-80fa-aff4-e247f3195b6e" class="">No opinions.</p></div><div style="display:contents" dir="auto"><hr id="2ddc5e6f-95bd-8087-ab65-f494dd26f8ba"/></div><div style="display:contents" dir="auto"><h2 id="2ddc5e6f-95bd-801b-a10c-c718c6afed9e" class=""><strong>Task C3 — Build “Launch Reference Vault”</strong></h2></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-807c-b944-cb375219dfee" class=""><strong>Deliverable:</strong> launch/refs/launch_reference_vault.md</p></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-807d-a03e-f4628ec7c076" class="">Collect:</p></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80b3-a347-e7ccad6c5c0a" class="bulleted-list"><li style="list-style-type:disc">20 great launch landing pages (dev tools / AI tools)</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-805c-9b7b-cbc6aeb50085" class="bulleted-list"><li style="list-style-type:disc">20 good product hunt pages</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-807b-bd2f-f4ae8f3efbc1" class="bulleted-list"><li style="list-style-type:disc">20 good demo videos</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80a4-abb4-f40e32e774bc" class="bulleted-list"><li style="list-style-type:disc">10 press kits you can imitate</li></ul></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-8025-a876-db35a0181019" class="">For each:</p></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-801e-9192-d2b29f4c2f99" class="bulleted-list"><li style="list-style-type:disc">link</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80b1-941d-f7ccb0d167c2" class="bulleted-list"><li style="list-style-type:disc">why it’s good (1 sentence)</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8081-9730-ca5b66cae904" class="bulleted-list"><li style="list-style-type:disc">what to copy (headline layout / sections / video style)</li></ul></div><div style="display:contents" dir="auto"><hr id="2ddc5e6f-95bd-8083-bb93-ea48f287067d"/></div><div style="display:contents" dir="auto"><h1 id="2ddc5e6f-95bd-80a0-8cf0-e084ec569b91" class=""><strong>D) Conversion Logistics (Execution-only)</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2ddc5e6f-95bd-8042-bdaf-fc18e63c4e56" class=""><strong>Task D1 — Create Launch Intake Forms</strong></h2></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-8061-aecb-f3b5288b24bb" class=""><strong>Deliverable:</strong> launch/ops/forms.md</p></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-80b8-9a8e-d5773750926f" class="">Set up:</p></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8094-b907-ddb98c68d6f4" class="bulleted-list"><li style="list-style-type:disc">Demo request form</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-801c-9f27-f252f9ff07b7" class="bulleted-list"><li style="list-style-type:disc">Early access signup form</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8090-b267-c0c4a4d77e55" class="bulleted-list"><li style="list-style-type:disc">Newsletter signup</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80ab-a79b-eb201dd413a9" class="bulleted-list"><li style="list-style-type:disc">“Enterprise inquiry” form</li></ul></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-809e-b196-f77fe4f198f5" class="">Each must:</p></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80c1-a1f4-cb0caf3c6133" class="bulleted-list"><li style="list-style-type:disc">collect name, company, role, use case, budget range (optional), urgency</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-801b-89a2-f262b8b88579" class="bulleted-list"><li style="list-style-type:disc">send results to your email</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8094-89e5-cc1879030d2e" class="bulleted-list"><li style="list-style-type:disc">store in spreadsheet</li></ul></div><div style="display:contents" dir="auto"><hr id="2ddc5e6f-95bd-80ff-88f5-c0dcd7fd88b5"/></div><div style="display:contents" dir="auto"><h2 id="2ddc5e6f-95bd-805e-a541-e5a75adc711b" class=""><strong>Task D2 — Build “Launch Inbox + Autoresponder”</strong></h2></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-8014-abde-cfae1eddc0ad" class=""><strong>Deliverable:</strong> launch/ops/email_setup.md</p></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-80e1-a7bd-d3b6e566de7b" class="">Set up:</p></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8007-99c5-d4fdca3c7d33" class="bulleted-list"><li style="list-style-type:disc">support@domain</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8086-ab8a-ed75ad10f3d9" class="bulleted-list"><li style="list-style-type:disc">hello@domain</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8061-8120-e051ac95bb0c" class="bulleted-list"><li style="list-style-type:disc">partnerships@domain</li></ul></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-80c7-8646-ea279f93569a" class="">Write autoresponder drafts (you approve later):</p></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-808c-b517-fb24b92bb0b6" class="bulleted-list"><li style="list-style-type:disc">demo request received</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8057-aa00-dc5aa7e57573" class="bulleted-list"><li style="list-style-type:disc">early access request received</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8062-a40e-c1a78a266dc8" class="bulleted-list"><li style="list-style-type:disc">enterprise inquiry received</li></ul></div><div style="display:contents" dir="auto"><hr id="2ddc5e6f-95bd-8051-bc7f-ebcf29950b57"/></div><div style="display:contents" dir="auto"><h1 id="2ddc5e6f-95bd-80cd-b994-c6f64e8d36b4" class=""><strong>E) Internal AMOS Repository Hygiene (Low-skill formatting)</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2ddc5e6f-95bd-8084-bddc-f5270a3906cd" class=""><strong>Task E1 — README Cleanup</strong></h2></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-80ad-b1a2-e0791022c6d7" class=""><strong>Deliverable:</strong> PR with improved README.md</p></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-80e8-a3c3-ce05b7e3851f" class="">Must include:</p></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-800b-833e-c18f69877de2" class="bulleted-list"><li style="list-style-type:disc">what it is</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80b0-a030-f52a380c9803" class="bulleted-list"><li style="list-style-type:disc">install</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-805b-9117-daa4745ea408" class="bulleted-list"><li style="list-style-type:disc">quickstart</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80b5-b5b4-c423d30bea9f" class="bulleted-list"><li style="list-style-type:disc">architecture diagram placeholder</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80e5-9065-c437dd55f769" class="bulleted-list"><li style="list-style-type:disc">roadmap</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8056-8502-c8c67dc18836" class="bulleted-list"><li style="list-style-type:disc">contribution rules</li></ul></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-80d2-8cbe-e6d13e4d9fc0" class="">Junior only formats + rearranges.</p></div><div style="display:contents" dir="auto"><hr id="2ddc5e6f-95bd-80c1-99c0-f9f3ca836f84"/></div><div style="display:contents" dir="auto"><h2 id="2ddc5e6f-95bd-8068-aeac-c3f9bcf7bcb8" class=""><strong>Task E2 — Convert Logs into “Progress Report”</strong></h2></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-80c4-bbb1-f547fdafc6d6" class=""><strong>Deliverable:</strong> launch/copy/progress_report.md</p></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-8051-90d0-e95339b37e66" class="">Input: your runtime logs/screenshots.</p></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-801f-879c-cb4dbbfb87ca" class="">Output: clean summary with:</p></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80a4-9da8-d3755d958917" class="bulleted-list"><li style="list-style-type:disc">what’s running</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-809b-8872-e1f631d33a01" class="bulleted-list"><li style="list-style-type:disc">what’s missing</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-807a-958c-fe29ba24cecf" class="bulleted-list"><li style="list-style-type:disc">what’s next</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-800a-b891-e9a91f5c7e62" class="bulleted-list"><li style="list-style-type:disc">known issues</li></ul></div><div style="display:contents" dir="auto"><hr id="2ddc5e6f-95bd-80a1-a047-e7aa06fd38b9"/></div><div style="display:contents" dir="auto"><h1 id="2ddc5e6f-95bd-80ea-a98f-ee23478dd442" class=""><strong>F) Output You Should Expect (from Junior)</strong></h1></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-80e0-ba15-fb47369d691c" class="">At the end you will have:</p></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80f2-a58e-c213cd830766" class="bulleted-list"><li style="list-style-type:disc">accounts created + documented</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80e3-8772-ceb5ec20a0c3" class="bulleted-list"><li style="list-style-type:disc">organized folder structure</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80cc-907c-e96d5cf56bff" class="bulleted-list"><li style="list-style-type:disc">your writing reformatted into:<div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8062-9ed0-eedc63b9cf64" class="bulleted-list"><li style="list-style-type:circle">1-page product brief</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8001-96eb-efef4a8515a5" class="bulleted-list"><li style="list-style-type:circle">homepage copy draft</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8067-b6e2-db19b047c631" class="bulleted-list"><li style="list-style-type:circle">cleaned launch posts</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-806e-be69-d0f315e61703" class="bulleted-list"><li style="list-style-type:disc">a curated library of:<div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-803f-ac6a-f9024714a4d2" class="bulleted-list"><li style="list-style-type:circle">20 credible PDFs</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8045-8458-d6da738e985b" class="bulleted-list"><li style="list-style-type:circle">competitor screenshots</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80f4-a35a-f686cb3848b8" class="bulleted-list"><li style="list-style-type:circle">launch inspiration vault</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8092-bbf5-c0c4df16e14f" class="bulleted-list"><li style="list-style-type:disc">intake + email plumbing ready</li></ul></div><div style="display:contents" dir="auto"><hr id="2ddc5e6f-95bd-804e-8744-fca1f3e7e40e"/></div><div style="display:contents" dir="auto"><h1 id="2ddc5e6f-95bd-805b-b944-cb9002de6ecd" class=""><strong>What I Need From You (to start immediately)</strong></h1></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-80c9-bcc4-c297afebd35f" class="">Send your junior:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2ddc5e6f-95bd-80d1-929f-d0ab0344b889" class="numbered-list" start="1"><li>Your preferred domain name (or list of options)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2ddc5e6f-95bd-80f8-9054-c8813f66cc75" class="numbered-list" start="2"><li>Your existing raw notes / docs for AMOS positioning and features</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2ddc5e6f-95bd-802a-8fa0-d82e9ef1dc5a" class="numbered-list" start="3"><li>Your target audience (pick one for now):<div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-800b-8c65-e97b9d2b1aa3" class="bulleted-list"><li style="list-style-type:disc">AI dev tools teams</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8097-ad16-e9b25cd16896" class="bulleted-list"><li style="list-style-type:disc">enterprise security/compliance</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80ed-8c9b-e8e60d4cc495" class="bulleted-list"><li style="list-style-type:disc">startups building agents</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><p id="2ddc5e6f-95bd-8065-af45-d19c1c19a753" class="">Then I can generate a <strong>single “Junior Assignment Brief”</strong> with:</p></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-8033-aa61-c239c950ae0c" class="bulleted-list"><li style="list-style-type:disc">exact step-by-step instructions</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-808b-884e-e178be332cca" class="bulleted-list"><li style="list-style-type:disc">definition of done for each task</li></ul></div><div style="display:contents" dir="auto"><ul id="2ddc5e6f-95bd-80aa-8c5f-c91848c16745" class="bulleted-list"><li style="list-style-type:disc">a checklist to ensure he doesn’t miss anything.</li></ul></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
