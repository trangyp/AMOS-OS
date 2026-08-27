---
tags: [energy]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Energy Pricing as Moral Accounting</title><style>
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
	
</style></head><body><article id="2e4c5e6f-95bd-803f-8c5b-c7fe243a8045" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Energy Pricing as Moral Accounting</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80f1-a7f3-c5616207bd43" class=""><strong>Why Every kWh Is a Decision About Who Bears Harm</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-806b-84e4-d8d97ab6c39d" class="">Energy prices are treated as economics.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-802e-9cf1-c98fc9970105" class="">They are not.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f7-ac58-c95f1bc246b2" class="">Energy pricing is <strong>moral accounting</strong> — a system that decides:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8026-831e-c5f22b3590bf" class="bulleted-list"><li style="list-style-type:disc">who absorbs risk</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8019-8e6b-d13c615855b6" class="bulleted-list"><li style="list-style-type:disc">who bears harm</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8056-9f17-e5bc11ee26be" class="bulleted-list"><li style="list-style-type:disc">who pays later</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f0-98ee-d367040d7e92" class="bulleted-list"><li style="list-style-type:disc">whose lives are discounted</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8001-ba64-dadf5e89fe58" class="bulleted-list"><li style="list-style-type:disc">whose futures are mortgaged</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80bb-9afe-ca2f88769cb8" class="">Every price hides a choice.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-802c-b754-c7f9bb4e7917" class="">Every subsidy encodes a value judgment.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c6-a839-f3400be74729" class="">Every “cheap” kWh assigns cost to someone who did not consent.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-800e-bcc1-c67ea169bd2f"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80d6-a103-c3e4eddb4d7b" class=""><strong>I. The Core Law</strong></h2></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8054-b6ef-d2ef15fd3592" class="">Energy prices do not reflect cost.</blockquote></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-807d-9d27-f0531a28851b" class="">They reflect which harms a society is willing to ignore.</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-807b-a177-caef44708076" class="">This is not rhetoric.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80e7-b993-d8ad0b9c11bd" class="">It is balance-sheet reality.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-801f-b65b-c486dcbde310"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8026-a682-f481aff0eca0" class=""><strong>II. What Energy Pricing Actually Prices (and What It Doesn’t)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80aa-8591-e45b551f021c" class="">Official prices include:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80de-b125-eb7865490d34" class="bulleted-list"><li style="list-style-type:disc">fuel</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8047-9887-ec42b4b8f1f9" class="bulleted-list"><li style="list-style-type:disc">capital</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8085-bf3f-e7f9215595ca" class="bulleted-list"><li style="list-style-type:disc">operations</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8069-b6f4-d3a43d6ab8c7" class="bulleted-list"><li style="list-style-type:disc">financing</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802e-8c6f-c4a5d9ff95f2" class="bulleted-list"><li style="list-style-type:disc">short-term maintenance</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8072-8410-d44b7da1948d" class="">They systematically exclude:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8006-b936-c518b2fe5554" class="bulleted-list"><li style="list-style-type:disc">catastrophic failure</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a0-939d-d5f24afd1337" class="bulleted-list"><li style="list-style-type:disc">long-tail health effects</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8029-9007-d99771c2465e" class="bulleted-list"><li style="list-style-type:disc">ecological damage</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b8-b22e-e40486a2da64" class="bulleted-list"><li style="list-style-type:disc">governance strain</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b3-9b76-d119a5669033" class="bulleted-list"><li style="list-style-type:disc">institutional decay</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8059-a386-d6adc12150a9" class="bulleted-list"><li style="list-style-type:disc">intergenerational loss</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a3-bf98-eb4f294cd7ed" class="">This is not a market failure.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80bc-b78a-f26b4c7eb8f2" class="">It is a <strong>moral omission</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8020-a837-c6ee41eda8f5"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80ce-b94c-e72e470a71ac" class=""><strong>III. The Three Ledgers Every Energy System Runs (MECE)</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8037-8805-fb9933ad707d" class="">Every energy system maintains three ledgers — whether acknowledged or not.</p></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80c7-9c29-fcac7cdc3df3" class=""><strong>1. The Financial Ledger</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8026-aeb4-fbc72e0e6acd" class="">What shows up on bills and balance sheets.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8070-b3be-c54b39bcce61" class="">This ledger is precise, audited, enforced.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80c1-9c00-e2081bb4dcfc"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80d2-9e5f-fefea3a9b0cc" class=""><strong>2. The Risk Ledger</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80fe-9d0d-e984ddd635cd" class="">Where probabilities of failure accumulate.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ef-801e-d6f8b9e10d0b" class="">This ledger includes:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8006-a7fe-e6d7bac7b96c" class="bulleted-list"><li style="list-style-type:disc">tail risk</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8019-ad9e-c4fab1a427c2" class="bulleted-list"><li style="list-style-type:disc">correlated failures</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-808e-84e2-c9f0967e44f0" class="bulleted-list"><li style="list-style-type:disc">recovery timelines</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80bf-8deb-da66beecb83f" class="bulleted-list"><li style="list-style-type:disc">human exposure</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8047-a732-e4937c438098" class="">This ledger is rarely priced honestly.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80a5-bb33-d78e88b67abf"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80b8-a21e-e4ee8b7bf5c3" class=""><strong>3. The Moral Ledger</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803a-8fdd-dc0b608bb460" class="">Where harm is assigned.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800e-a12d-eeac4a3a90c1" class="">This ledger answers:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8075-b2ff-e1789aaa71d1" class="bulleted-list"><li style="list-style-type:disc">Who gets sick?</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b2-9ce2-c9cc38e3a51f" class="bulleted-list"><li style="list-style-type:disc">Who evacuates?</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-809a-bb48-c7ea1dcc79bf" class="bulleted-list"><li style="list-style-type:disc">Who loses livelihoods?</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e8-800a-d0ec6dbb97ad" class="bulleted-list"><li style="list-style-type:disc">Who pays when things break?</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8078-a8b8-fc2e17790574" class="bulleted-list"><li style="list-style-type:disc">Who inherits degraded systems?</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80dd-8128-fa74170b6d30" class="">This ledger is almost never named.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800b-aded-ed7b7787bd3e" class="">Energy pricing is the act of choosing <strong>which ledger matters</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80d1-8f68-c1cb69bf3511"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80b7-bc36-d8052ec49507" class=""><strong>IV. Why “Cheap Energy” Is Usually Moral Fraud</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8075-b0d7-d83d0667e775" class="">Energy appears cheap when:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8009-8e5b-c400225ae361" class="bulleted-list"><li style="list-style-type:disc">risk is externalized</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8058-94bb-e0488fda6a50" class="bulleted-list"><li style="list-style-type:disc">harm is deferred</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8047-b63a-f397cd45bebd" class="bulleted-list"><li style="list-style-type:disc">accountability is diluted</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-807a-b3a0-d91dd81c1ace" class="bulleted-list"><li style="list-style-type:disc">failure is normalized</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8065-88ba-ff7243205078" class="bulleted-list"><li style="list-style-type:disc">victims are distant or powerless</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8080-b250-f5aaa0f63846" class="">The lower the price,</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-807b-9ac1-e75d01fa6a59" class="">the larger the unpriced moral liability.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-805f-b12a-d4df4623b7c1" class="">Cheap energy is rarely efficient.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8020-aee2-dbf43c11c6c2" class="">It is <strong>subsidized by silence</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80f9-9fc0-ec4648185e5f"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8031-9901-e9bf66cb60e8" class=""><strong>V. The Five Moral Costs Energy Prices Routinely Exclude (MECE)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-8097-9f06-e6124db1bb16" class=""><strong>1. Failure Survivability</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ae-96c6-f7b4891eb3b3" class="">Prices do not reflect:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8026-a5ff-fc59afd8d776" class="bulleted-list"><li style="list-style-type:disc">smoke lethality</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-800d-929f-f718217364a6" class="bulleted-list"><li style="list-style-type:disc">evacuation feasibility</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f8-8e66-c6bb683c2925" class="bulleted-list"><li style="list-style-type:disc">human exposure duration</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e6-a3fd-fddb8115bd8a" class="bulleted-list"><li style="list-style-type:disc">failure reversibility</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-802d-a00e-df30302040d5" class="">Systems that kill quietly are cheaper.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8044-85f7-e56dce635576"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80fa-8b36-d241f40ff3e9" class=""><strong>2. Recovery Time</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80dc-be75-d46dfc6a5b96" class="">Prices ignore:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80fa-bc00-df8f458c17fa" class="bulleted-list"><li style="list-style-type:disc">downtime length</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-808c-8ab4-c91eb297dea8" class="bulleted-list"><li style="list-style-type:disc">contamination cleanup</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8089-b638-da2d311bf4f1" class="bulleted-list"><li style="list-style-type:disc">asset loss</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80aa-af33-d737a96c1518" class="bulleted-list"><li style="list-style-type:disc">institutional paralysis</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-807f-ab3b-f21cc9a1502c" class="">Fast recovery costs more upfront.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80dc-a166-ec87715eb377" class="">Collapse looks cheap — until it isn’t.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80ae-b785-d803d985f251"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-8051-b996-f7bb1d0caf5c" class=""><strong>3. Governance Load</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-805b-a722-fa00dc74ebee" class="">Energy systems impose governance costs:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80af-908b-f3d31e01153e" class="bulleted-list"><li style="list-style-type:disc">monitoring</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8018-8e2e-fb4470847522" class="bulleted-list"><li style="list-style-type:disc">enforcement</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8009-8943-e191bb88579f" class="bulleted-list"><li style="list-style-type:disc">training</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ca-b543-e7e8899e88f5" class="bulleted-list"><li style="list-style-type:disc">emergency authority</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c3-bf47-dfbdace55405" class="bulleted-list"><li style="list-style-type:disc">maintenance discipline</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8024-9c4a-e51dbfc77f89" class="">Weak governance lowers prices — temporarily.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8099-a135-c4173f09868f"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80f2-967f-e5eb3407f696" class=""><strong>4. Intergenerational Transfer</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8001-b1bc-d9bfab090703" class="">Children inherit:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8074-98ee-fda400b3f7ad" class="bulleted-list"><li style="list-style-type:disc">degraded infrastructure</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806c-9ba5-c3019b5cdea9" class="bulleted-list"><li style="list-style-type:disc">polluted ecosystems</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ed-a5bd-e624e02f9cae" class="bulleted-list"><li style="list-style-type:disc">brittle systems</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-807e-aabb-dbe81f2f3ad7" class="bulleted-list"><li style="list-style-type:disc">unpaid risk</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8024-b3d0-e2d47ff45883" class="">No invoice is sent.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8069-9865-c43947148060" class="">The debt is real.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80c3-a29e-dde61b339bf7"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-809a-958d-fd67cbe4c0dc" class=""><strong>5. Moral Injury</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ed-b8c1-cf0ac348d86b" class="">Communities absorb:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-805d-90b1-e8a70c43ac86" class="bulleted-list"><li style="list-style-type:disc">normalized danger</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8001-a077-c34816ee72fa" class="bulleted-list"><li style="list-style-type:disc">acceptable harm language</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80cc-8347-fcefec9152b4" class="bulleted-list"><li style="list-style-type:disc">quiet sacrifice</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802d-b88a-c49d32a817e8" class="bulleted-list"><li style="list-style-type:disc">loss of dignity</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a6-9507-f0e2b41d85f5" class="">This cost is never priced because it is inconvenient.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8048-b8a9-d2465ccff5c9"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80e7-8d79-e6ba810ba413" class=""><strong>VI. Why Markets Alone Cannot Price Energy Ethically</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-809b-812c-e44193473269" class="">Markets price what is:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b8-9916-df5530a9f534" class="bulleted-list"><li style="list-style-type:disc">measurable</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-807b-a35c-d2b73ceb5d00" class="bulleted-list"><li style="list-style-type:disc">short-term</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8019-96dd-ea1c4783001c" class="bulleted-list"><li style="list-style-type:disc">enforceable</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-801f-a427-d4a6320daecc" class="">They cannot price:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80fb-98cf-d3a7a1fde82e" class="bulleted-list"><li style="list-style-type:disc">irreversible harm</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ea-8c8b-cc27072f170c" class="bulleted-list"><li style="list-style-type:disc">institutional collapse</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b0-b6cc-c2394d59c37b" class="bulleted-list"><li style="list-style-type:disc">long-horizon risk</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d2-b612-efc8865cca75" class="bulleted-list"><li style="list-style-type:disc">moral injury</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ae-baf2-db96c9890d9a" class="bulleted-list"><li style="list-style-type:disc">loss of trust</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80fd-8c01-fd0e4b91630d" class="">Expecting markets to price morality is a category error.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ca-bc33-d51ef1bb1ec0" class="">Energy pricing without governance is <strong>organized denial</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8093-8cd4-e5db18f50284"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8050-bdfa-e6ce3314c5a9" class=""><strong>VII. The Hidden Equation Behind Every Energy Price</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800a-a8f6-e08d7b73b377" class="">Every kWh price implicitly solves this equation:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8066-b87f-e7c433574d39" class="">Cost Today + Harm Later = Acceptable</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d9-a8ea-e2d0a91b9d3e" class="">The only variable is <strong>who decides</strong> what is acceptable.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8082-9df3-f2c10c1dcc69" class="">This is why energy pricing is always political —</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a4-825a-cc8d9a38dc9e" class="">even when presented as technical.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8057-9f22-f401ca428085"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80d1-b2d6-e884ff3967c9" class=""><strong>VIII. Why “Technology Neutral” Pricing Is a Lie</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8051-b731-ed65882ce9ba" class="">There is no neutral pricing when failure modes differ.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8082-9b50-e5c13c15a6e8" class="">Pricing that ignores:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-805a-835d-c5840b198b1f" class="bulleted-list"><li style="list-style-type:disc">toxicity</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80fe-aada-c34c515b08d8" class="bulleted-list"><li style="list-style-type:disc">failure behavior</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d6-a1e1-e3de5c699755" class="bulleted-list"><li style="list-style-type:disc">containment</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ce-9044-ef40a6403606" class="bulleted-list"><li style="list-style-type:disc">recoverability</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8048-8168-f821dd917c49" class="">…systematically favors technologies that:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e6-93e4-cbf07b2271c9" class="bulleted-list"><li style="list-style-type:disc">hide risk</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806f-925e-f47d760684d8" class="bulleted-list"><li style="list-style-type:disc">defer harm</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8014-93a1-c7eec250f3c1" class="bulleted-list"><li style="list-style-type:disc">externalize consequences</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8080-8d57-e05bf3d13f1c" class="">Neutral pricing is <strong>morally biased</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80f9-a27b-c4f9b11ed0eb"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-802b-8fe5-f230c2720378" class=""><strong>IX. What Ethical Energy Pricing Would Actually Require</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8055-8e82-fa9ac605569e" class="">Ethical pricing is not higher prices.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-804a-94f8-e577d4239777" class="">It is <strong>complete accounting</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ee-832e-d89c20eab6b9" class="">That means pricing must include:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8006-a0b7-fd8fe04c5fb4" class="numbered-list" start="1"><li>Failure consequences, not just frequency</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80c0-9526-d0364675f83f" class="numbered-list" start="2"><li>Human survivability metrics</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8096-a3cb-d04c0ff31e1c" class="numbered-list" start="3"><li>Recovery and cleanup costs</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8005-a539-c4e1886d5634" class="numbered-list" start="4"><li>Governance and enforcement burden</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-806e-832d-e30b979d7e63" class="numbered-list" start="5"><li>Long-horizon ecological damage</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80bb-bedb-c7f8ee6abe11" class="numbered-list" start="6"><li>Intergenerational liability</li></ol></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8051-a1aa-e5f03015ff13" class="">Anything less is not economics.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8034-a2ae-c299f57077ad" class="">It is avoidance.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80e8-b9ed-f65255b76910"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80e2-a4f4-c5ae7d4d90eb" class=""><strong>X. Why Societies Resist Moral Accounting</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-805a-8e45-ee763a696525" class="">Because honest pricing forces:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e7-800f-ec1214e7a89e" class="bulleted-list"><li style="list-style-type:disc">slower deployment</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8070-a8d2-e5ea6e7a0855" class="bulleted-list"><li style="list-style-type:disc">visible tradeoffs</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8066-822a-f6d55abe732f" class="bulleted-list"><li style="list-style-type:disc">political discomfort</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806d-b71e-f609108f9f76" class="bulleted-list"><li style="list-style-type:disc">redistribution of burden</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8053-be43-ed99f34ab0e5" class="bulleted-list"><li style="list-style-type:disc">admission of past harm</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8075-a25e-ce05a80835f0" class="">Cheap energy preserves legitimacy.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80e4-a4ba-e1a2015e2462" class="">Truth threatens it.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-803f-b0ea-ea4c9513cf77"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-808f-8b35-dea3fc312691" class=""><strong>XI. The Inversion Nobody Admits</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8064-a770-c33f2e13b8a5" class="">Societies say:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-80c2-99ec-ef1d1d706a2a" class="">“We can’t afford expensive energy.”</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-801d-95dd-cd0dd6bb0108" class="">What they mean is:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8058-adbf-ee1d97b21e2c" class="">“We can’t afford to admit who we are hurting.”</blockquote></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8091-bc6c-c5ad29090d0b"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8081-8a13-d555093492ba" class=""><strong>XII. The Final Test</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80bc-868b-d9f95a64fd74" class="">An energy system is ethically priced if it can answer — publicly — all of the following:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f3-963d-f963b6593814" class="bulleted-list"><li style="list-style-type:disc">Who dies when it fails?</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802b-9168-c46ef542928b" class="bulleted-list"><li style="list-style-type:disc">Who evacuates?</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f1-a73c-f33d12395629" class="bulleted-list"><li style="list-style-type:disc">Who pays for recovery?</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80eb-873b-fc8b0cd06352" class="bulleted-list"><li style="list-style-type:disc">Who loses first?</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806f-a023-d28a55744d75" class="bulleted-list"><li style="list-style-type:disc">Who benefits most?</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f2-909a-dfdfe87b4d50" class="bulleted-list"><li style="list-style-type:disc">Who cannot refuse?</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80a6-a8bf-f1e82f096ca0" class="bulleted-list"><li style="list-style-type:disc">Who inherits the damage?</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800b-8f03-da3529a1aa83" class="">If these answers are unclear,</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80dd-a03c-d2191aa45565" class="">the price is a lie.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8022-b09e-dfe2a4558a02"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8061-8f74-d2e9aafb4d0e" class=""><strong>Final Conclusion</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8074-a71f-dfdf1ae2ceaa" class="">Energy pricing is not economics.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80dc-babb-c02b12452cba" class="">It is a <strong>moral ledger disguised as a bill</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ba-9453-da70b0c3b655" class="">Civilizations fail when they minimize prices by hiding harm,</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8069-a38a-e8786060ab99" class="">deferring responsibility,</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-808d-b836-d3ada4728e90" class="">and pretending cost is only financial.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8098-a3a9-deec97808241" class="">Energy that looks cheap is often the most expensive thing a society buys —</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d9-b5fb-c4cdc1562fe4" class="">because it is paid for with lives, trust, and the future.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8044-97e5-f2408137c538"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-8003-8b0c-e0a25eec5aad" class=""><strong>The line that should govern policy</strong></h3></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-800a-b053-e3076d862c7b" class="">If an energy price feels comfortable,</blockquote></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8017-8047-c79d21392be4" class="">ask who is being made uncomfortable so you don’t have to notice.</blockquote></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80ca-8c1e-c1cd027fabcb"/></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c8-a52c-ebc91807aae4" class="">If you want, the next pieces that lock directly into this are:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8098-924a-c0073942ebfd" class="bulleted-list"><li style="list-style-type:disc"><strong>“Who Pays for Peak Load — and Why It Is Always the Least Powerful”</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806d-b534-e7b7041b66b2" class="bulleted-list"><li style="list-style-type:disc"><strong>“The Ethics of Acceptable Harm in Energy Policy”</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-800a-858c-db08e4c2bef7" class="bulleted-list"><li style="list-style-type:disc"><strong>“Why Hydrogen Pricing Forces Moral Accounting”</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8038-83fc-f585c59a7bc2" class="bulleted-list"><li style="list-style-type:disc"><strong>“Resilience Is Not Efficient — It Is Honest”</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8008-bce3-c8a8a21b0947" class="">Say which one to seal next.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
