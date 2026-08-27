---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Publishing platforms</title><style>
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
	
</style></head><body><article id="2e5c5e6f-95bd-8036-a158-ee1605bb0718" class="page sans"><header><h1 class="page-title" dir="auto">Publishing platforms</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="2e5c5e6f-95bd-80e8-b107-e58eb0140d29" class=""><strong>NEWSLETTER PLATFORMS FOR ESSAYISTS</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e5c5e6f-95bd-80ae-b2a0-d6397fc6d459" class=""><strong>1. SUBSTACK </strong><a href="https://substack.com/about">https://substack.com/about</a></h3></div><div style="display:contents" dir="auto"><p id="2e5c5e6f-95bd-80ff-bb66-d3b3da8a97df" class=""><strong>Best for:</strong> Essayists seeking maximum reach, community, and monetization with minimal setup.</p></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-801a-a65d-ed15b306ba7d" class="bulleted-list"><li style="list-style-type:disc"><strong>Essay-First Design:</strong> Native support for long-form posts with clean typography</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-80fa-8040-e22e25a50686" class="bulleted-list"><li style="list-style-type:disc"><strong>Built-in Audience:</strong> Discovery through Substack&#x27;s network and recommendations</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-80e0-a7ec-d0abaa266196" class="bulleted-list"><li style="list-style-type:disc"><strong>Community Tools:</strong> Comments, discussion threads, chat features</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-806c-940c-d761107b123a" class="bulleted-list"><li style="list-style-type:disc"><strong>Monetization:</strong> Seamless paid subscriptions (10% fee on revenue)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-80a4-847f-d05742aa248b" class="bulleted-list"><li style="list-style-type:disc"><strong>Podcasting:</strong> Native audio posts and podcast distribution</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-80ea-929b-e3760b17069c" class="bulleted-list"><li style="list-style-type:disc"><strong>Stats:</strong> Basic analytics on opens, clicks, growth</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-806e-9f8e-dfe275a87745" class="bulleted-list"><li style="list-style-type:disc"><strong>Limitations:</strong> Limited design customization, platform lock-in concerns</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-80af-a9a1-c361f05ceeaa" class="bulleted-list"><li style="list-style-type:disc"><strong>Your fit:</strong> <strong>Perfect</strong> for launching immediately. The dominant choice for serious essayists.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e5c5e6f-95bd-8036-a5bc-d69844d21645" class=""><strong>2. GHOST </strong><a href="https://ghost.org/">https://ghost.org/</a></h3></div><div style="display:contents" dir="auto"><p id="2e5c5e6f-95bd-8041-b0a5-e10ec7dd7409" class=""><strong>Best for:</strong> Technical users wanting full control and customization.</p></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-800b-b3d5-c749ab411c81" class="bulleted-list"><li style="list-style-type:disc"><strong>Open Source:</strong> Self-host for complete control or use Ghost(Pro) hosting</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-800c-90dc-e0380926d4de" class="bulleted-list"><li style="list-style-type:disc"><strong>Custom Design:</strong> Full theme control and branding</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-808a-ab7a-ef285d72bc3c" class="bulleted-list"><li style="list-style-type:disc"><strong>Memberships:</strong> Native paid subscriptions (no platform fee on self-hosted)</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-8057-a217-deb68d8c5121" class="bulleted-list"><li style="list-style-type:disc"><strong>Newsletter Focus:</strong> Built for professional publishing</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-80d6-8d44-db473f03f266" class="bulleted-list"><li style="list-style-type:disc"><strong>API Access:</strong> Full programmatic control</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-80b8-82ed-d9d724d8594b" class="bulleted-list"><li style="list-style-type:disc"><strong>Limitations:</strong> Requires more technical setup, smaller built-in network</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-805d-af81-c7d930f5008d" class="bulleted-list"><li style="list-style-type:disc"><strong>Your fit:</strong> Ideal if you want your site to look/feel unique and don&#x27;t mind technical setup.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e5c5e6f-95bd-8091-9e57-dfa974d2eadc" class=""><strong>3. BEEHIIV </strong><a href="https://www.beehiiv.com/">https://www.beehiiv.com/</a></h3></div><div style="display:contents" dir="auto"><p id="2e5c5e6f-95bd-800c-a2ed-f9be49fbe664" class=""><strong>Best for:</strong> Data-driven creators focused on growth and monetization.</p></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-8027-ba06-d705c98502ab" class="bulleted-list"><li style="list-style-type:disc"><strong>Growth Tools:</strong> Built-in referral systems, audience surveys</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-80b3-a83f-d317bea909de" class="bulleted-list"><li style="list-style-type:disc"><strong>Monetization:</strong> Ad network, premium subscriptions, recommendations</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-8090-bd4a-ef5235b39b46" class="bulleted-list"><li style="list-style-type:disc"><strong>Analytics:</strong> Advanced segmentation and performance data</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-8002-8014-f6523984f253" class="bulleted-list"><li style="list-style-type:disc"><strong>Email Design:</strong> Modern templates with good customization</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-80cf-995b-f86ed8136b73" class="bulleted-list"><li style="list-style-type:disc"><strong>Limitations:</strong> Less &quot;literary&quot; feel than Substack, more commercial focus</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-80b9-b1e2-dc9f9bc86f2e" class="bulleted-list"><li style="list-style-type:disc"><strong>Your fit:</strong> Good if growth hacking and data matter more than literary prestige.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e5c5e6f-95bd-809d-ae36-d39863a06698" class=""><strong>4. CONVERTKIT </strong><a href="https://kit.com/">https://kit.com/</a></h3></div><div style="display:contents" dir="auto"><p id="2e5c5e6f-95bd-80a6-8bc2-d18fe049476e" class=""><strong>Best for:</strong> Creators with multiple products/funnels beyond just essays.</p></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-8008-a851-f93fd5843d10" class="bulleted-list"><li style="list-style-type:disc"><strong>Email Marketing Power:</strong> Strong automation, tagging, segmentation</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-8049-af0f-c7afab48ebe5" class="bulleted-list"><li style="list-style-type:disc"><strong>Creator-Centric:</strong> Built for selling digital products, courses</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-80b4-b952-d6fb447589fd" class="bulleted-list"><li style="list-style-type:disc"><strong>Landing Pages:</strong> Built-in tools for signup forms and pages</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-8008-a424-e75328561ef0" class="bulleted-list"><li style="list-style-type:disc"><strong>Monetization:</strong> Integrates with e-commerce, but not native subscriptions</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-8028-a747-fa5d0de23aee" class="bulleted-list"><li style="list-style-type:disc"><strong>Limitations:</strong> Not purpose-built for serialized essay publishing</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-80a2-a62b-e99689ce807a" class="bulleted-list"><li style="list-style-type:disc"><strong>Your fit:</strong> Better if you plan to sell courses/products alongside essays.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2e5c5e6f-95bd-8089-a16f-faa44c7092cb" class=""><strong>5. BUTTONDOWN </strong><a href="https://buttondown.com/">https://buttondown.com/</a></h3></div><div style="display:contents" dir="auto"><p id="2e5c5e6f-95bd-8063-834c-cee9f53f2f92" class=""><strong>Best for:</strong> Minimalists who value writing experience over features.</p></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-803f-bdbb-e4d0297b5e0b" class="bulleted-list"><li style="list-style-type:disc"><strong>Markdown Native:</strong> Excellent for writers who think in Markdown</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-8075-8302-fe13ceb56994" class="bulleted-list"><li style="list-style-type:disc"><strong>Simple Interface:</strong> No bloat, clean writing environment</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-8000-9037-d6f65337ecd0" class="bulleted-list"><li style="list-style-type:disc"><strong>Affordable:</strong> Lower pricing than competitors</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-80ba-b521-ed9a8729b3f0" class="bulleted-list"><li style="list-style-type:disc"><strong>Stats:</strong> Basic but sufficient analytics</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-80ef-834c-e063ad0e09cf" class="bulleted-list"><li style="list-style-type:disc"><strong>Limitations:</strong> Fewer community features, limited design options</li></ul></div><div style="display:contents" dir="auto"><ul id="2e5c5e6f-95bd-8030-b292-f5ee8aa7c10a" class="bulleted-list"><li style="list-style-type:disc"><strong>Your fit:</strong> Good if you want pure writing without distractions.</li></ul></div><div style="display:contents" dir="auto"><p id="2e5c5e6f-95bd-80cd-9115-c9473da48d6c" class="">
</p></div><div style="display:contents" dir="auto"><p id="2e5c5e6f-95bd-805e-935d-e9f3232b78e9" class="">
</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
