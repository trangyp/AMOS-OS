---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>APPENDIX 01: FEATURE LIST</title><style>
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
	
</style></head><body><article id="285c5e6f-95bd-802e-a1e3-eacd50787629" class="page sans"><header><h1 class="page-title" dir="auto"><strong>APPENDIX 01: FEATURE LIST</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="285c5e6f-95bd-801a-8751-d8dfb4da6661" class=""><em>(Attached to the Business Cooperation Contract between EMDDI Joint Stock Company and UNITAXI Joint Stock Company)</em></p></div><div style="display:contents" dir="auto"><hr id="285c5e6f-95bd-80bc-813e-f25736c520db"/></div><div style="display:contents" dir="auto"><h2 id="285c5e6f-95bd-801b-a3cf-faa26b64d4fb" class=""><strong>FEATURE LIST</strong></h2></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-80d4-b4b8-ea1d04b665f7" class=""><strong>Customer App</strong></h3></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-8074-8bbc-f6219b996790" class=""><strong>Access Management</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80a1-a15e-fccd560bc9cc" class="bulleted-list"><li style="list-style-type:disc"><strong>Register:</strong> Register an account via:<div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-805f-94c3-fa71cf6501d0" class="bulleted-list"><li style="list-style-type:circle">Phone number</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8016-860d-e1b360d6a257" class="bulleted-list"><li style="list-style-type:circle">Password</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8089-9649-e04bc9fda67e" class="bulleted-list"><li style="list-style-type:disc"><strong>Log out:</strong> Allows users to log out of the application.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-808c-b0a8-c9f13205dc12" class="bulleted-list"><li style="list-style-type:disc"><strong>Log in:</strong> Log in using registered credentials (phone number and password).</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8012-9c12-dc4b754963fe" class="bulleted-list"><li style="list-style-type:disc"><strong>Forgot password:</strong> Allows users to retrieve passwords when forgotten.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8069-b089-ebedbaec2851" class="bulleted-list"><li style="list-style-type:disc"><strong>OTP verification:</strong> The system automatically sends a code to the login phone number.</li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-8056-a971-fe52781aa04a" class=""><strong>Home Page</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8009-912f-ec9cfbafacff" class="bulleted-list"><li style="list-style-type:disc"><strong>Display service list:</strong> Shows all available services configured in the admin control panel.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-804d-b8f0-fb78eac3c594" class="bulleted-list"><li style="list-style-type:disc"><strong>News:</strong> Allows users to view configured news information.</li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-8054-b31f-f103a24b9d54" class=""><strong>Account Information</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8006-9602-dbcd6ba117b9" class="bulleted-list"><li style="list-style-type:disc"><strong>Update profile:</strong> Allows users to update account profile information.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-807c-8c45-d9bfb2cacc0b" class="bulleted-list"><li style="list-style-type:disc"><strong>Change password:</strong> Allows users to change their password.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8079-87bd-e4b72b0aa6c5" class="bulleted-list"><li style="list-style-type:disc"><strong>Delete account:</strong> Allows users to delete their account.</li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-804d-af4f-c3cabea1d65c" class=""><strong>Refer Friends</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80d4-bb6d-c1a130febcbd" class="bulleted-list"><li style="list-style-type:disc"><strong>Refer friends:</strong> Allows users to invite friends to use the app.</li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-80fe-bd34-c19dcbf86e5d" class=""><strong>Manage Favourite Addresses</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80f3-8557-ea6039d0e7b2" class="bulleted-list"><li style="list-style-type:disc"><strong>View saved addresses:</strong> Shows a list of saved favourite addresses.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8096-a564-e2cac4b8e1ba" class="bulleted-list"><li style="list-style-type:disc"><strong>Add home, work, or favourite address:</strong><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80ec-93f3-d55164a307bf" class="bulleted-list"><li style="list-style-type:circle">Home address</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8040-9b60-c12b08c37748" class="bulleted-list"><li style="list-style-type:circle">Work address</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80e0-838f-db8029cb348f" class="bulleted-list"><li style="list-style-type:disc"><strong>Delete address:</strong> Allows users to delete saved addresses.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80c4-a70b-d34063d06ccf" class="bulleted-list"><li style="list-style-type:disc"><strong>Delete search history:</strong> Allows users to clear previous searches.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80d0-a004-c23053382827" class="bulleted-list"><li style="list-style-type:disc"><strong>View recent locations:</strong> Shows recently searched locations.</li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-80b2-8afe-f6d5abddc132" class=""><strong>Customer Support</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80f1-a097-f37c0bc7a4a0" class="bulleted-list"><li style="list-style-type:disc"><strong>Hotline:</strong> Tap to call customer support.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80bc-be77-e369eabae5a1" class="bulleted-list"><li style="list-style-type:disc"><strong>Customer service email:</strong> Quick link to send email to support team.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-805d-9e94-e5884d0aff99" class="bulleted-list"><li style="list-style-type:disc"><strong>Company address:</strong> View service provider address.</li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-805f-a24d-ce126fc2ea05" class=""><strong>Terms and Policies</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8041-b383-e49217efe063" class="bulleted-list"><li style="list-style-type:disc"><strong>Policies and conditions:</strong> Opens the company website to display policy and terms.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80da-bfc4-e15e53f250f1" class="bulleted-list"><li style="list-style-type:disc"><strong>Privacy policy:</strong> Opens the website to display data protection policies.</li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-809f-8485-ffcaa8dbe7c4" class=""><strong>Language</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-801a-8292-de73ba9dd529" class="bulleted-list"><li style="list-style-type:disc"><strong>Vietnamese / English:</strong> Users can select preferred language.</li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-80b2-9bd6-ccfa0beef2ef" class=""><strong>Notifications</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80c7-b952-d5f801b52479" class="bulleted-list"><li style="list-style-type:disc"><strong>View notifications list:</strong> Displays all notifications.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-805d-9113-d85ec1c074ae" class="bulleted-list"><li style="list-style-type:disc"><strong>View details:</strong> Allows users to read detailed notification content.</li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-808e-882f-c399bbcb9959" class=""><strong>Activity</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80a5-8949-e07358a4aa36" class="bulleted-list"><li style="list-style-type:disc"><strong>View activity history:</strong> Allows users to view all past bookings.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80ab-886d-df3c335e61f5" class="bulleted-list"><li style="list-style-type:disc"><strong>Trip details:</strong> View trip history details.</li></ul></div><div style="display:contents" dir="auto"><hr id="285c5e6f-95bd-80ca-a5c4-d0fa1066fdfb"/></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-8085-9387-d1a75f3dedf7" class=""><strong>Book Taxi – Immediate Ride</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-804a-80db-e4383cbbb2a7" class="bulleted-list"><li style="list-style-type:disc"><strong>Search pick-up and drop-off points.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-809b-8a5c-e1af43ae86e4" class="bulleted-list"><li style="list-style-type:disc"><strong>Auto-detect current location.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80a7-9b5f-c8f06dd92a4a" class="bulleted-list"><li style="list-style-type:disc"><strong>Select points from map or saved favourites.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-807b-9a86-d1d20c9517c6" class="bulleted-list"><li style="list-style-type:disc"><strong>View fare estimate for each service type.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8059-a945-f0cec7dc32e4" class="bulleted-list"><li style="list-style-type:disc"><strong>Book one-destination trip.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80da-9239-cd566100c94d" class="bulleted-list"><li style="list-style-type:disc"><strong>Track driver arrival in real-time.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8068-9cd8-e0e80b270b28" class="bulleted-list"><li style="list-style-type:disc"><strong>View estimated pick-up time.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-800d-a020-cdfe0af4ec96" class="bulleted-list"><li style="list-style-type:disc"><strong>Add notes to trip.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-807a-afcf-e00bbd632f11" class="bulleted-list"><li style="list-style-type:disc"><strong>Rate trip (star rating).</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80cd-bd2c-d016ebbf2cf8" class="bulleted-list"><li style="list-style-type:disc"><strong>Swap pick-up and drop-off locations.</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="285c5e6f-95bd-800a-a81c-fb435762b38f"/></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-809d-a75b-d6f42a6c81a1" class=""><strong>Promotions</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-801c-84f9-cbb3aa0a3ddc" class="bulleted-list"><li style="list-style-type:disc"><strong>View promo list:</strong> Includes value, conditions, and validity period.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8066-ad3f-c0e15c32b2b3" class="bulleted-list"><li style="list-style-type:disc"><strong>View details:</strong> Displays specific promo details.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80d4-a5df-f6291896f111" class="bulleted-list"><li style="list-style-type:disc"><strong>Apply promo code:</strong> Allows use of a promotion code.</li></ul></div><div style="display:contents" dir="auto"><hr id="285c5e6f-95bd-80f5-9112-de3661949f20"/></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-80bd-9e17-ea05f1bab291" class=""><strong>Multi-Destination Booking (2 stops)</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8023-9737-f971d075dc8c" class="bulleted-list"><li style="list-style-type:disc"><strong>Add destination:</strong> Search and add extra drop-off point.</li></ul></div><div style="display:contents" dir="auto"><hr id="285c5e6f-95bd-80bb-8798-d31e04dd252e"/></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-80c6-b72b-d6576a951b15" class=""><strong>Book with Assigned Driver</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80e2-b110-fb9cc47a2788" class="bulleted-list"><li style="list-style-type:disc"><strong>Choose “Assigned Driver” option.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80fc-8d9f-ea539fed3e52" class="bulleted-list"><li style="list-style-type:disc"><strong>Display code for assigned trip.</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="285c5e6f-95bd-8033-a8de-d11e28b44e4a"/></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-80b8-b9ca-da7a7123cf5d" class=""><strong>Change Destination</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80de-9e8f-e19aadf4f171" class="bulleted-list"><li style="list-style-type:disc">Allows users to change destination while trip is ongoing.</li></ul></div><div style="display:contents" dir="auto"><hr id="285c5e6f-95bd-8067-b2d1-eeea1e8509ea"/></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-80e1-92f4-cb0ee033b650" class=""><strong>Referral Codes</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80e2-8af0-f61e24d8e15c" class="bulleted-list"><li style="list-style-type:disc"><strong>Enter referral code.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8004-a83e-ebe0ef3d14dd" class="bulleted-list"><li style="list-style-type:disc"><strong>View referrer list.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80d7-a8e3-d4350885f32c" class="bulleted-list"><li style="list-style-type:disc"><strong>Receive discount codes or revenue-based bonuses from campaigns.</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="285c5e6f-95bd-80b4-92e3-fe2bf590dbf2"/></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-8093-b6e8-fdaeaa59dcca" class=""><strong>Shared Rides / Call Center Bookings</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80aa-b879-dd8239f5f1ea" class="bulleted-list"><li style="list-style-type:disc"><strong>Create trip for customer (by dispatcher):</strong><div style="display:contents" dir="auto"><p id="285c5e6f-95bd-80e9-91b6-f52b84bfe646" class="">Includes pick-up, drop-off, time, car type, seat number.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80ff-ba0e-d10a063b58f8" class="bulleted-list"><li style="list-style-type:disc"><strong>Create delivery trip:</strong> For parcels, including sender/receiver info.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8078-957b-d674c09e184e" class="bulleted-list"><li style="list-style-type:disc"><strong>Edit trip details:</strong> Before trip completion.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80ce-b733-c6c97f79e1d3" class="bulleted-list"><li style="list-style-type:disc"><strong>Cancel trip:</strong> When customer no longer needs service.</li></ul></div><div style="display:contents" dir="auto"><hr id="285c5e6f-95bd-8077-83b2-e1b74dc35844"/></div><div style="display:contents" dir="auto"><h2 id="285c5e6f-95bd-80ad-b04c-c159e5220a8e" class=""><strong>Driver App</strong></h2></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-8016-b637-f98fef4cd07e" class=""><strong>Login &amp; Access</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-809f-a0ab-e471de608d41" class="bulleted-list"><li style="list-style-type:disc"><strong>Login:</strong> Account created by admin; driver logs in using provided credentials.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-803b-a0ff-c2e238ea3612" class="bulleted-list"><li style="list-style-type:disc"><strong>Forgot password:</strong> New password sent to driver’s registered phone number.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80ed-bdc4-f3638878908c" class="bulleted-list"><li style="list-style-type:disc"><strong>Logout:</strong> Log out of account.</li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-8051-b24b-da1f48a08a36" class=""><strong>Home</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80c6-a838-c758f7402b89" class="bulleted-list"><li style="list-style-type:disc"><strong>Wallet balance (Upper Wallet):</strong><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-806e-87bf-cd00a5971fb6" class="bulleted-list"><li style="list-style-type:circle">Shows driver’s technical wallet used for commission deduction.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8023-a8ca-fdf46b9bc1c9" class="bulleted-list"><li style="list-style-type:circle">Deduction rate configured by admin.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80f8-9e85-e353ef0c103d" class="bulleted-list"><li style="list-style-type:disc"><strong>Trip acceptance rate:</strong> Displays driver activity report.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8047-83bf-e8cce0a0c9d4" class="bulleted-list"><li style="list-style-type:disc"><strong>Average rating:</strong> Displays average star rating per trip (daily/weekly).</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80e5-b678-fd9953191c65" class="bulleted-list"><li style="list-style-type:disc"><strong>Cancellation rate:</strong> Includes both customer and driver cancellations.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8042-ac3c-df8921feec4d" class="bulleted-list"><li style="list-style-type:disc"><strong>Online time statistics:</strong> Total online duration per day/week.</li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-80ee-bc32-d223d1b2b790" class=""><strong>Vehicle Management</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-805d-bd18-da68248e1a1d" class="bulleted-list"><li style="list-style-type:disc"><strong>View vehicle list.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80b9-8acb-d76676585379" class="bulleted-list"><li style="list-style-type:disc"><strong>Select vehicle to go online:</strong> System sends suitable ride requests.</li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-80ec-be9a-ec0f4ad10972" class=""><strong>Wallets</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8088-bbb1-eed2b65cb954" class="bulleted-list"><li style="list-style-type:disc"><strong>Lower Wallet:</strong><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80e7-bbe5-fb9e033a659e" class="bulleted-list"><li style="list-style-type:circle">Shows transaction history (commissions, bonuses).</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8006-aa56-d6a53a15ae72" class="bulleted-list"><li style="list-style-type:circle">Can transfer money from lower → upper wallet.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8057-8788-dd55727a22b0" class="bulleted-list"><li style="list-style-type:circle">Allows withdrawal requests.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8097-be83-cfef14060167" class="bulleted-list"><li style="list-style-type:circle">Displays withdrawal history and details.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8048-b6b8-fbf833902847" class="bulleted-list"><li style="list-style-type:disc"><strong>Upper Wallet:</strong><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-803f-a422-c82bd421aeea" class="bulleted-list"><li style="list-style-type:circle">View deduction and top-up history.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80fb-8b38-e6fbcfff4897" class="bulleted-list"><li style="list-style-type:circle">Supports <strong>OnePay</strong> QR recharge.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-8002-9a44-e49c9f31b71c" class=""><strong>Street Hails</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8076-aceb-cf650e0a913b" class="bulleted-list"><li style="list-style-type:disc"><strong>Pick up walk-in passengers.</strong></li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-8036-bd69-fa255a0d8eb7" class=""><strong>Trip History</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8002-871e-cdad226ce089" class="bulleted-list"><li style="list-style-type:disc"><strong>View completed, canceled, or active trips.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8084-a043-e79b31971622" class="bulleted-list"><li style="list-style-type:disc"><strong>Filter by trip status.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-808c-804a-c8f661ae0344" class="bulleted-list"><li style="list-style-type:disc"><strong>View details:</strong> Invoice, fare, promotions, surcharges.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8025-b3b3-d342ce6110c5" class="bulleted-list"><li style="list-style-type:disc"><strong>View canceled trip reason and customer name.</strong></li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-8023-bb4f-dbe6459e7092" class=""><strong>Support</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80fc-b177-dbb478687efc" class="bulleted-list"><li style="list-style-type:disc"><strong>Call support staff in case of issues.</strong></li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-8083-9394-cfed5422120e" class=""><strong>Notifications</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-803e-9cce-cf67bc5df467" class="bulleted-list"><li style="list-style-type:disc"><strong>View notification list and details.</strong></li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-8057-9f97-cbafe9308135" class=""><strong>Multi-Destination Rides</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8089-9e99-f0cd3daa4d05" class="bulleted-list"><li style="list-style-type:disc"><strong>View drop-off route and map navigation.</strong></li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-80ed-bdaf-e0ebba6a9d46" class=""><strong>Assigned Trips</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80ac-9f99-cedcb0004bda" class="bulleted-list"><li style="list-style-type:disc"><strong>Display assignment code.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-808b-8c1d-ff540fe4c91d" class="bulleted-list"><li style="list-style-type:disc"><strong>View customer booking info.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8093-93dd-fd5af6590a0f" class="bulleted-list"><li style="list-style-type:disc"><strong>Cancel assigned trip before confirmation.</strong></li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-8074-b71a-c2b9a4d19384" class=""><strong>Shared Rides</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80de-8f25-dbe3bf06313f" class="bulleted-list"><li style="list-style-type:disc"><strong>Send available route to dispatcher.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80a0-89d2-e910ef36c505" class="bulleted-list"><li style="list-style-type:disc"><strong>Manually accept rides.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8030-9663-e72a701c95de" class="bulleted-list"><li style="list-style-type:disc"><strong>Swipe actions: “Accept,” “Picked up,” “Dropped off.”</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="285c5e6f-95bd-80bb-a4a8-c18acc1795af"/></div><div style="display:contents" dir="auto"><h2 id="285c5e6f-95bd-808c-a2bb-f04dd9d5f973" class=""><strong>Web Admin Portal</strong></h2></div><div style="display:contents" dir="auto"><p id="285c5e6f-95bd-804a-9018-c0232d65bc7b" class="">Covers full management of:</p></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-801c-966c-d343b50b757b" class="bulleted-list"><li style="list-style-type:disc">Drivers, vehicles, trips, transactions, withdrawals, customers, promotions, advertising, and system governance.</li></ul></div><div style="display:contents" dir="auto"><p id="285c5e6f-95bd-808e-8408-fc0c947b1844" class="">Includes:</p></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8046-a8f8-cf9397b89a9b" class="bulleted-list"><li style="list-style-type:disc">Add/edit/delete users and vehicles.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8095-a678-fa9a27ab1eef" class="bulleted-list"><li style="list-style-type:disc">Assign services and reset statuses.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-803c-8152-fe89e0235c27" class="bulleted-list"><li style="list-style-type:disc">Lock/unlock accounts.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8048-b35b-e5595591d3c5" class="bulleted-list"><li style="list-style-type:disc">Driver document management (ID, driver’s license, photo).</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-801a-a632-c283c4411c17" class="bulleted-list"><li style="list-style-type:disc">View online activity, location, violations, and connection logs.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80d4-9bda-f67a07e4649c" class="bulleted-list"><li style="list-style-type:disc">Export data to Excel.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8013-91d0-c016052ca144" class="bulleted-list"><li style="list-style-type:disc">Approve or reject withdrawal requests.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80c0-b767-c3d9d14677c7" class="bulleted-list"><li style="list-style-type:disc">Generate statistical and financial reports.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80d0-a2b4-dabbbc6db59a" class="bulleted-list"><li style="list-style-type:disc">Configure fare calculation method (by meter).</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8033-9039-dacbc4fcbed6" class="bulleted-list"><li style="list-style-type:disc">Manage promotions, referral programs, and ad notifications.</li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-802f-897f-e51d886882cc" class="bulleted-list"><li style="list-style-type:disc">Manage departments, roles, and system accounts.</li></ul></div><div style="display:contents" dir="auto"><hr id="285c5e6f-95bd-8031-a409-ea0fda394b02"/></div><div style="display:contents" dir="auto"><h2 id="285c5e6f-95bd-80da-b433-f48772dfd1b0" class=""><strong>Corporate Customer Web Portal (Merchant Business)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-804a-989c-f6c36e9a94b3" class=""><strong>Account Management</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8007-94dc-cf14e3a925ea" class="bulleted-list"><li style="list-style-type:disc"><strong>Login / Logout.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80a9-906b-cdb3332790c7" class="bulleted-list"><li style="list-style-type:disc"><strong>Language selection (EN/VN).</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-800f-8880-f9f59eef62a8" class="bulleted-list"><li style="list-style-type:disc"><strong>Change password.</strong></li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-8004-a65c-c9586dda5de2" class=""><strong>Enterprise</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8092-968c-c6448c4fc25b" class="bulleted-list"><li style="list-style-type:disc"><strong>Company information.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-803a-bb67-e06ffb0cd38d" class="bulleted-list"><li style="list-style-type:disc"><strong>Monthly limit tracking.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8055-9ba2-ceec265cf77c" class="bulleted-list"><li style="list-style-type:disc"><strong>Department and card budget allocation.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80eb-a676-f034b7d1ffc9" class="bulleted-list"><li style="list-style-type:disc"><strong>Expense tracking and usage reports.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8092-b501-d5fd519aa05a" class="bulleted-list"><li style="list-style-type:disc"><strong>Department management (add/edit/delete).</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8041-8ee6-e3783f894ea1" class="bulleted-list"><li style="list-style-type:disc"><strong>Admin management (add/edit/delete/lock).</strong></li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-809d-83fb-db9c8d1b6630" class=""><strong>Trips</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8037-9015-f0c0b630f171" class="bulleted-list"><li style="list-style-type:disc"><strong>View company trip list.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8076-8712-f3ed0a49c52d" class="bulleted-list"><li style="list-style-type:disc"><strong>Filter by time range, department, or trip status.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80d9-acf9-e40b489e7a99" class="bulleted-list"><li style="list-style-type:disc"><strong>Keyword search and Excel export.</strong></li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-800b-aea9-d8847705d66f" class=""><strong>Card / Employee Management</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80b6-af75-fe15dda60fae" class="bulleted-list"><li style="list-style-type:disc"><strong>View all company cards.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-8096-b764-cef5df40f899" class="bulleted-list"><li style="list-style-type:disc"><strong>Search, filter, add, edit, delete, or lock/unlock cards.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80ef-a7f3-d2bf9abda36b" class="bulleted-list"><li style="list-style-type:disc"><strong>Generate and export QR codes and PINs.</strong></li></ul></div><div style="display:contents" dir="auto"><h3 id="285c5e6f-95bd-80f8-b6b3-e2950e037b39" class=""><strong>History</strong></h3></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-803d-b0b7-ec284bfe7b05" class="bulleted-list"><li style="list-style-type:disc"><strong>View card limit changes.</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="285c5e6f-95bd-80a3-b366-e79ee01607d8" class="bulleted-list"><li style="list-style-type:disc"><strong>Export Excel reports of card limit history.</strong></li></ul></div><div style="display:contents" dir="auto"><hr id="285c5e6f-95bd-8013-9567-c595609ecf82"/></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
