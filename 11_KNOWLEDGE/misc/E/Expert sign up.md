---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Expert sign up</title><style>
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
	
</style></head><body><article id="304c5e6f-95bd-80cb-ae10-e3974948caa2" class="page sans"><header><h1 class="page-title" dir="auto">Expert sign up</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h1 id="304c5e6f-95bd-807d-afe2-d79f93a8d802" class=""><strong>I. Tier 1 — Global Institutional Expert Networks</strong></h1></div><div style="display:contents" dir="auto"><p id="304c5e6f-95bd-8073-a451-cc9b6828c72a" class="">Large, multinational, used by PE / hedge funds / strategy consulting.</p></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8023-8df3-fea7aa3cd459" class="bulleted-list"><li style="list-style-type:disc">GLG (Gerson Lehrman Group)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-800f-bb84-e9cb96b8fa9e" class="bulleted-list"><li style="list-style-type:disc">AlphaSights</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80eb-8da6-e2d7f06196ef" class="bulleted-list"><li style="list-style-type:disc">Guidepoint</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80f4-aba8-d1c7789c1706" class="bulleted-list"><li style="list-style-type:disc">Third Bridge</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-809e-a639-f02c2534d106" class="bulleted-list"><li style="list-style-type:disc">Coleman Research</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8057-8d12-ff1f439c3736" class="bulleted-list"><li style="list-style-type:disc">Atheneum</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80a5-9f2c-d43b76d78678" class="bulleted-list"><li style="list-style-type:disc">Capvision (strong Asia presence)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8095-bd3c-de9c6f0385df" class="bulleted-list"><li style="list-style-type:disc">ProSapient</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8003-ba56-ff3f1d2c97a3" class="bulleted-list"><li style="list-style-type:disc">Evalueserve (research-heavy)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8020-aec4-f78583976406" class="bulleted-list"><li style="list-style-type:disc">Informa Connect Expert Network</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80ca-af42-f5cbe75e158a" class="bulleted-list"><li style="list-style-type:disc">BTG Insights (not same as Business Talent Group)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80be-a1ba-f407b719cbbd" class="bulleted-list"><li style="list-style-type:disc">Dialectica</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80d8-8e25-fb128abb1f24" class="bulleted-list"><li style="list-style-type:disc">Aranca (research hybrid)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80ae-a017-fa796b958cfa" class="bulleted-list"><li style="list-style-type:disc">Broadfield Group</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80c2-8150-fcf628becc9f" class="bulleted-list"><li style="list-style-type:disc">Enginuity Research</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80ea-a8be-d5f1ed7f77fa" class="bulleted-list"><li style="list-style-type:disc">KOL Research</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80f1-8847-e84ffdf2d755" class="bulleted-list"><li style="list-style-type:disc">Maven Research</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8066-867e-f2814c0f21ee" class="bulleted-list"><li style="list-style-type:disc">Maven Insights (separate from cohort Maven)</li></ul></div><div style="display:contents" dir="auto"><hr id="304c5e6f-95bd-8003-8538-eb20af393bd8"/></div><div style="display:contents" dir="auto"><h1 id="304c5e6f-95bd-809c-848e-e117710406bd" class=""><strong>II. Tier 2 — High-Quality Niche / Regional Networks</strong></h1></div><div style="display:contents" dir="auto"><p id="304c5e6f-95bd-8011-b6e2-f4109aa5feda" class="">More selective or regionally strong.</p></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80a0-a902-dde79d7c2354" class="bulleted-list"><li style="list-style-type:disc">NewtonX</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-804b-adc8-c3c998ade07e" class="bulleted-list"><li style="list-style-type:disc">Arbolus</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80d8-a3a4-fcf2a3ecd785" class="bulleted-list"><li style="list-style-type:disc">VisasQ (Japan strong)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8007-a0f9-c95a5d5d8978" class="bulleted-list"><li style="list-style-type:disc">Silverlight Research</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-802d-87a7-ebf3b0df627f" class="bulleted-list"><li style="list-style-type:disc">Tegus (PE-heavy, hybrid)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80dc-97f7-d7d1c9b47bd4" class="bulleted-list"><li style="list-style-type:disc">Stream Research</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8046-985e-f3e1d606c928" class="bulleted-list"><li style="list-style-type:disc">Inex One (aggregator marketplace)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80da-8bf6-d4763cb6553e" class="bulleted-list"><li style="list-style-type:disc">Primary Insight</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80b8-b4bf-f63417962673" class="bulleted-list"><li style="list-style-type:disc">Lynk Global</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80ec-9d22-c776651beedd" class="bulleted-list"><li style="list-style-type:disc">ExpertConnect</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8006-a919-e8dd7ebcbce0" class="bulleted-list"><li style="list-style-type:disc">Techspert</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8028-9f7f-e11eb6c4fd37" class="bulleted-list"><li style="list-style-type:disc">Ridgetop Research</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8093-a78b-d4c8c652e60a" class="bulleted-list"><li style="list-style-type:disc">FocusPoint</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-804b-999c-eeb45c8fa06b" class="bulleted-list"><li style="list-style-type:disc">DeepBench</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-806d-9bd6-e9e07ef9ebd3" class="bulleted-list"><li style="list-style-type:disc">Zintro</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8056-b235-c936e5192529" class="bulleted-list"><li style="list-style-type:disc">RSRCHXchange</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8071-999d-e90a4145c504" class="bulleted-list"><li style="list-style-type:disc">Coresignal (data + expert layer emerging)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80f9-bef4-ea6cbd56bfe9" class="bulleted-list"><li style="list-style-type:disc">Alphasights alternatives in EU (e.g., Atheneum regional desks)</li></ul></div><div style="display:contents" dir="auto"><hr id="304c5e6f-95bd-8015-acf9-caf559dd4c98"/></div><div style="display:contents" dir="auto"><h1 id="304c5e6f-95bd-8071-9838-d83dfd69f6b7" class=""><strong>III. Private Equity / Hedge Fund / Investment Intelligence Platforms</strong></h1></div><div style="display:contents" dir="auto"><p id="304c5e6f-95bd-809e-ac2f-e1d013cae225" class="">More diligence-oriented. Often higher rates if recurring.</p></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-803d-9d86-f4542515d7d8" class="bulleted-list"><li style="list-style-type:disc">Tegus</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-809a-a3e3-dddb91eea21c" class="bulleted-list"><li style="list-style-type:disc">InPractise</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80c1-a360-f2ace0b07cbd" class="bulleted-list"><li style="list-style-type:disc">Affinity</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80da-8a9b-c5894fb0016b" class="bulleted-list"><li style="list-style-type:disc">BlueMatrix</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8069-920a-f2a9d26c65b6" class="bulleted-list"><li style="list-style-type:disc">Sentieo (research distribution)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-804e-be26-e11c455b613c" class="bulleted-list"><li style="list-style-type:disc">Preqin expert panels</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80f0-bd65-e2d01513e70e" class="bulleted-list"><li style="list-style-type:disc">PitchBook advisory panels</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8006-a55e-fc2724fbe4f4" class="bulleted-list"><li style="list-style-type:disc">S&amp;P Global expert outreach</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8048-9d83-e6416e786623" class="bulleted-list"><li style="list-style-type:disc">Refinitiv / LSEG contributor networks</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8099-861b-c7d5c98dc101" class="bulleted-list"><li style="list-style-type:disc">Mergermarket intelligence contacts</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80c9-9d2f-ed069b42bb2e" class="bulleted-list"><li style="list-style-type:disc">Dealogic advisor panels</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80b7-a5f7-f04ed4aad62a" class="bulleted-list"><li style="list-style-type:disc">Capital IQ expert contributor channels</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8068-98d2-edcfddafc368" class="bulleted-list"><li style="list-style-type:disc">FactSet expert programs</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80e0-b85a-c9a6dc757fb2" class="bulleted-list"><li style="list-style-type:disc">Smartkarma</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-806d-911c-f7ac219d4b36" class="bulleted-list"><li style="list-style-type:disc">Visible Alpha</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-809c-899c-d437e4b5b921" class="bulleted-list"><li style="list-style-type:disc">YipitData (selective contributors)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8020-8898-fcfe6c6ee0bf" class="bulleted-list"><li style="list-style-type:disc">AlphaSense expert ecosystem</li></ul></div><div style="display:contents" dir="auto"><hr id="304c5e6f-95bd-80f7-a60a-f53ad7068539"/></div><div style="display:contents" dir="auto"><h1 id="304c5e6f-95bd-80ef-91d4-d69b771713df" class=""><strong>IV. Litigation / Expert Witness Networks</strong></h1></div><div style="display:contents" dir="auto"><p id="304c5e6f-95bd-8012-9914-dbd3446d343c" class="">Extremely high paid if credible.</p></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-806f-aba1-cae42a06669d" class="bulleted-list"><li style="list-style-type:disc">IMS Consulting</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80ba-91a3-d112400138a3" class="bulleted-list"><li style="list-style-type:disc">Berkeley Research Group (BRG)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8062-aab2-e8e4e372fba2" class="bulleted-list"><li style="list-style-type:disc">FTI Consulting (Expert Services)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-804c-84c3-c2613a178832" class="bulleted-list"><li style="list-style-type:disc">Secretariat Advisors</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80d5-8c6b-e57a4dc14857" class="bulleted-list"><li style="list-style-type:disc">HKA Global</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80cd-afb9-f1a71e49ca8e" class="bulleted-list"><li style="list-style-type:disc">Cornerstone Research (economics-heavy)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-805b-b547-c33ea94f5bc5" class="bulleted-list"><li style="list-style-type:disc">Ankura</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8059-9f20-e633de5572e7" class="bulleted-list"><li style="list-style-type:disc">Charles River Associates (CRA)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80ac-a340-d2f06b490aea" class="bulleted-list"><li style="list-style-type:disc">Navigant (now Guidehouse)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-807e-94b6-e671ba7cf08c" class="bulleted-list"><li style="list-style-type:disc">Alvarez &amp; Marsal expert pools</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-806a-b7a3-d52ce2d408bd" class="bulleted-list"><li style="list-style-type:disc">Kroll expert services</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8005-ae66-fefa759f8c2b" class="bulleted-list"><li style="list-style-type:disc">Duff &amp; Phelps (valuation side)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80f4-ab81-c089ad196951" class="bulleted-list"><li style="list-style-type:disc">ForensisGroup</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8073-b2ad-da7a890a69a9" class="bulleted-list"><li style="list-style-type:disc">Round Table Group</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-800c-aab5-c10dbde303f8" class="bulleted-list"><li style="list-style-type:disc">TASA Group</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80df-a8e0-c997e4054b76" class="bulleted-list"><li style="list-style-type:disc">Expert Institute</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80cd-8a17-f9359d6e91cc" class="bulleted-list"><li style="list-style-type:disc">SEAK expert witness directory</li></ul></div><div style="display:contents" dir="auto"><hr id="304c5e6f-95bd-8091-8e20-f28bc6ed1298"/></div><div style="display:contents" dir="auto"><h1 id="304c5e6f-95bd-8099-a067-cacc71b4cf2a" class=""><strong>V. Fractional Executive / Strategy Marketplaces</strong></h1></div><div style="display:contents" dir="auto"><p id="304c5e6f-95bd-80eb-949c-eedfe3ab9a6c" class="">High-value project-based.</p></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8044-b200-d29f079af516" class="bulleted-list"><li style="list-style-type:disc">Catalant</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8041-b8af-c3f1b4471d0e" class="bulleted-list"><li style="list-style-type:disc">Business Talent Group (BTG)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8060-865b-c6666ee5f7bd" class="bulleted-list"><li style="list-style-type:disc">Toptal (executive tier)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-801e-b43b-c301bd3ead18" class="bulleted-list"><li style="list-style-type:disc">A.Team</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80e3-b520-dc8d69b24c8a" class="bulleted-list"><li style="list-style-type:disc">Talmix</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8089-8915-d2e5a5777ce2" class="bulleted-list"><li style="list-style-type:disc">Graphite</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8001-80f5-e3943d592f85" class="bulleted-list"><li style="list-style-type:disc">Eden McCallum</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80e6-a192-d4c2d1301d43" class="bulleted-list"><li style="list-style-type:disc">Umbrex</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80c1-97df-ed48d791ee4e" class="bulleted-list"><li style="list-style-type:disc">COMATCH (now Malt Strategy)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-807a-b514-d4bc8579b959" class="bulleted-list"><li style="list-style-type:disc">Expert360 (AU-based)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80ab-bf61-d68b344a84af" class="bulleted-list"><li style="list-style-type:disc">Nurole (board roles)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80b6-b692-d46c8da22bda" class="bulleted-list"><li style="list-style-type:disc">AdvisoryCloud</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80b1-adb2-d2b2086e7247" class="bulleted-list"><li style="list-style-type:disc">BoardProspects</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80b8-b6c6-e1088c9b5294" class="bulleted-list"><li style="list-style-type:disc">ExecThread (adjacent)</li></ul></div><div style="display:contents" dir="auto"><hr id="304c5e6f-95bd-8045-b0fe-f3d6492750bf"/></div><div style="display:contents" dir="auto"><h1 id="304c5e6f-95bd-8006-a786-ddb171bfa0a1" class=""><strong>VI. Government / Multilateral Consultant Rosters</strong></h1></div><div style="display:contents" dir="auto"><p id="304c5e6f-95bd-807f-a7b5-d124a2faf23b" class="">Often overlooked but stable pay.</p></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80f7-856a-e8c950a7d6b6" class="bulleted-list"><li style="list-style-type:disc">World Bank consultant roster</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-803e-847c-ec1d83fc75c4" class="bulleted-list"><li style="list-style-type:disc">IFC short-term consultant pool</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8094-8391-c657720a3dc8" class="bulleted-list"><li style="list-style-type:disc">Asian Development Bank CMS</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80c2-bd50-d7bd844f35db" class="bulleted-list"><li style="list-style-type:disc">Inter-American Development Bank expert pool</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8089-86ef-c9c847948bf2" class="bulleted-list"><li style="list-style-type:disc">UNDP consultant roster</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80b0-858e-c28a0600d487" class="bulleted-list"><li style="list-style-type:disc">UNICEF expert roster</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8055-8864-ea3c1e999311" class="bulleted-list"><li style="list-style-type:disc">UNOPS</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-808a-b853-f13121f548ae" class="bulleted-list"><li style="list-style-type:disc">OECD expert pools</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80a0-8e81-f7d9f7a081b3" class="bulleted-list"><li style="list-style-type:disc">European Commission expert database</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8046-afc9-dbe213a04b2b" class="bulleted-list"><li style="list-style-type:disc">UK Cabinet Office consultancy framework</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8031-b560-c3fa4b571552" class="bulleted-list"><li style="list-style-type:disc">Australian Government consultancy panels</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80f7-8d8e-e3fe314cf7e5" class="bulleted-list"><li style="list-style-type:disc">US GSA schedules (if registered via entity)</li></ul></div><div style="display:contents" dir="auto"><hr id="304c5e6f-95bd-8025-bacc-f86fa573b8a1"/></div><div style="display:contents" dir="auto"><h1 id="304c5e6f-95bd-80bf-addc-de5bf9f23874" class=""><strong>VII. Institutional Research &amp; Publishing Platforms (Paid Contributors)</strong></h1></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8045-a6a8-df6afb2e9022" class="bulleted-list"><li style="list-style-type:disc">Smartkarma</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8063-8b50-f0f7f83dd919" class="bulleted-list"><li style="list-style-type:disc">Seeking Alpha Pro</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80c2-ba73-c6c9fd6cff45" class="bulleted-list"><li style="list-style-type:disc">Tegus contributor track</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80b2-acd1-c04cd2506691" class="bulleted-list"><li style="list-style-type:disc">InPractise interview contributor</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8071-ad6e-d608220d9725" class="bulleted-list"><li style="list-style-type:disc">BlueMatrix content distribution</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8007-bc98-e495c231e09d" class="bulleted-list"><li style="list-style-type:disc">Substack (institutional tier only)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80c8-8845-cad646903dd1" class="bulleted-list"><li style="list-style-type:disc">SSRN (credibility signal)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8032-ac8f-d12513688172" class="bulleted-list"><li style="list-style-type:disc">ResearchGate (academic-adjacent)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8063-93b0-d8c5568b3cd2" class="bulleted-list"><li style="list-style-type:disc">arXiv (technical)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80f9-b211-d34812c5035a" class="bulleted-list"><li style="list-style-type:disc">Alpha Architect (selective)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80a1-a9cb-c6454429b49a" class="bulleted-list"><li style="list-style-type:disc">Responsible AI Institute (governance niche)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8098-98d8-dd1aa434aa4c" class="bulleted-list"><li style="list-style-type:disc">IEEE working group publications</li></ul></div><div style="display:contents" dir="auto"><hr id="304c5e6f-95bd-80eb-855c-da223c791fb7"/></div><div style="display:contents" dir="auto"><h1 id="304c5e6f-95bd-8061-92b4-c918a2fb28de" class=""><strong>VIII. Specialized / Emerging Platforms</strong></h1></div><div style="display:contents" dir="auto"><p id="304c5e6f-95bd-8037-adfb-d299b11f5491" class="">More niche but growing.</p></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-805b-bcf4-d8c5e9b79598" class="bulleted-list"><li style="list-style-type:disc">DeepBench (tech expert)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8013-9b9a-efb49ab62d2e" class="bulleted-list"><li style="list-style-type:disc">Guidepoint Qsight (special division)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8069-86f3-cd93d4b36276" class="bulleted-list"><li style="list-style-type:disc">GLG Surveys (survey track)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8025-a1ba-dda45d8ba630" class="bulleted-list"><li style="list-style-type:disc">NewtonX surveys</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80e3-bf9f-dd6fb9cd5a97" class="bulleted-list"><li style="list-style-type:disc">Cint (survey panel if domain-specific)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80e9-906f-d6ee11bf087b" class="bulleted-list"><li style="list-style-type:disc">Atheneum Insights</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8065-9b72-c98c546be7fc" class="bulleted-list"><li style="list-style-type:disc">Dialectica Insights</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80f9-96fc-f4479f686567" class="bulleted-list"><li style="list-style-type:disc">Alphasights Survey unit</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80e6-8b46-d25ccbfca3b1" class="bulleted-list"><li style="list-style-type:disc">Kantar expert panels (if sector match)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8052-9c49-fa5eb87eb3e6" class="bulleted-list"><li style="list-style-type:disc">Gartner peer insights (reputation signal, not direct pay)</li></ul></div><div style="display:contents" dir="auto"><hr id="304c5e6f-95bd-8051-ba20-d95d90ace582"/></div><div style="display:contents" dir="auto"><h1 id="304c5e6f-95bd-8000-9d8a-efd6779eadfc" class=""><strong>IX. Aggregators (Multiply Your Surface Area)</strong></h1></div><div style="display:contents" dir="auto"><p id="304c5e6f-95bd-8002-9062-d66ae5bdfde4" class="">These let you access multiple networks.</p></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80e8-9b0b-c4c5457b8c75" class="bulleted-list"><li style="list-style-type:disc">Inex One</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8034-9c82-c9b1af05b769" class="bulleted-list"><li style="list-style-type:disc">Lynk</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-801a-bbd9-c68fbfe5e212" class="bulleted-list"><li style="list-style-type:disc">Maven Insights</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8037-9c3e-c796b176d1fa" class="bulleted-list"><li style="list-style-type:disc">Techspert</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8058-bdfd-c5ef2279aa7b" class="bulleted-list"><li style="list-style-type:disc">Zintro</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8068-a1c8-d852d9ab4a25" class="bulleted-list"><li style="list-style-type:disc">Expert360 (AU)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80bf-99bc-e6f97927f6be" class="bulleted-list"><li style="list-style-type:disc">GLG referrals into partner pools</li></ul></div><div style="display:contents" dir="auto"><hr id="304c5e6f-95bd-80b2-8335-f563c1ed478e"/></div><div style="display:contents" dir="auto"><h1 id="304c5e6f-95bd-8003-b569-c88a85fbecf1" class=""><strong>X. Board / Governance / Oversight Pools</strong></h1></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80ab-829e-cf6cba09a765" class="bulleted-list"><li style="list-style-type:disc">Nurole</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8043-b50f-e35731b24afc" class="bulleted-list"><li style="list-style-type:disc">AdvisoryCloud</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8055-bb49-d0c8ef3df609" class="bulleted-list"><li style="list-style-type:disc">BoardProspects</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80a2-92eb-dd215daa2c5b" class="bulleted-list"><li style="list-style-type:disc">DirectorPrep</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8054-a8ac-c77f2f2bec93" class="bulleted-list"><li style="list-style-type:disc">Australian Institute of Company Directors (AICD panels)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80b1-b666-f0727e14fb95" class="bulleted-list"><li style="list-style-type:disc">NACD (US directors association)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80a5-979a-f482c084f0cf" class="bulleted-list"><li style="list-style-type:disc">Institute of Directors UK</li></ul></div><div style="display:contents" dir="auto"><hr id="304c5e6f-95bd-80e3-8f51-d8d1f2386e70"/></div><div style="display:contents" dir="auto"><h1 id="304c5e6f-95bd-80a4-8261-dc88a7e5fc8f" class=""><strong>XI. Capital / Family Office / Sovereign Channels (Harder Access)</strong></h1></div><div style="display:contents" dir="auto"><p id="304c5e6f-95bd-80a4-b465-e5b53d0b53b5" class="">Usually referral-based, but searchable.</p></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8037-838e-f108da5ab92f" class="bulleted-list"><li style="list-style-type:disc">Sovereign wealth advisory pools</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8060-be91-dd79557f18ec" class="bulleted-list"><li style="list-style-type:disc">Family office networks (Tiger 21, Campden)</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8050-a271-ef328f142f47" class="bulleted-list"><li style="list-style-type:disc">PE operating partner pools</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8044-bc2d-cc1419d177ad" class="bulleted-list"><li style="list-style-type:disc">VC venture partner pools</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8000-acc1-df8242939058" class="bulleted-list"><li style="list-style-type:disc">Strategic advisory boards of startups</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80f2-868d-d86c622bd3e6" class="bulleted-list"><li style="list-style-type:disc">AngelList advisor listings</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80e5-b614-ee6fe25823eb" class="bulleted-list"><li style="list-style-type:disc">SeedInvest expert rosters</li></ul></div><div style="display:contents" dir="auto"><hr id="304c5e6f-95bd-8054-abff-fa65fbc7a1af"/></div><div style="display:contents" dir="auto"><h1 id="304c5e6f-95bd-803b-8141-e9a1431ead7d" class=""><strong>Strategic Reality</strong></h1></div><div style="display:contents" dir="auto"><p id="304c5e6f-95bd-80c8-ba49-c9092af4e205" class="">If optimized properly, serious operators sit in:</p></div><div style="display:contents" dir="auto"><p id="304c5e6f-95bd-80e0-bddc-f860ca18d7b0" class="">8–15 networks simultaneously.</p></div><div style="display:contents" dir="auto"><p id="304c5e6f-95bd-8027-b0d6-f54418f6c077" class="">They:</p></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8078-a24a-f6193ea4d771" class="bulleted-list"><li style="list-style-type:disc">Tighten niche keywords</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8041-8e3b-cc35bf42642a" class="bulleted-list"><li style="list-style-type:disc">Respond within minutes</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80f5-b282-e659732fa767" class="bulleted-list"><li style="list-style-type:disc">Gradually raise rates</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-8051-9909-e2708533d814" class="bulleted-list"><li style="list-style-type:disc">Refuse misfit calls</li></ul></div><div style="display:contents" dir="auto"><ul id="304c5e6f-95bd-80e9-b577-f2894b4c7657" class="bulleted-list"><li style="list-style-type:disc">Track conversion by topic</li></ul></div><div style="display:contents" dir="auto"><p id="304c5e6f-95bd-8050-b853-ef898e732281" class="">That is how $400k–$700k/year happens quietly.</p></div><div style="display:contents" dir="auto"><hr id="304c5e6f-95bd-803d-9f3b-f460d38e8cb3"/></div><div style="display:contents" dir="auto"><h1 id="304c5e6f-95bd-8068-8823-d48db05bb442" class=""></h1></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
