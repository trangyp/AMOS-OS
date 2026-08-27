---
tags: [energy]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Why Energy Justice Cannot Be Priced</title><style>
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
	
</style></head><body><article id="2e4c5e6f-95bd-806f-918f-f6af56b1e8cf" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Why Energy Justice Cannot Be Priced</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8045-b4aa-ca40aedaa7bd" class=""><strong>Markets Can Allocate Electricity. They Cannot Allocate Dignity.</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8059-914c-d51c41e6c942" class="">Energy justice is routinely framed as a pricing problem.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a2-b009-dc500e27a3fe" class="">Subsidies. Tariffs. Rebates. Dynamic rates. Compensation mechanisms.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-805c-b219-e418c9bf50c8" class="">This framing is incorrect.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8098-aa50-f4604dad12fc" class="">Energy justice fails the moment it is reduced to price, because <strong>price is a mechanism for allocation, not protection</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8077-bfea-d46322571daa" class="">What energy justice governs is not consumption.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a0-8982-e7bd5d4a870a" class="">It governs <strong>exposure to harm</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-801b-9fa4-db21735e67bf" class="">And harm is not evenly priced.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8064-8650-cf2374981dbb"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8002-819d-e6c97419391e" class=""><strong>I. The Foundational Error</strong></h2></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8009-8a11-df441cbc456c" class="">Markets price willingness to pay.</blockquote></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-80c3-8129-da7842d65c08" class="">Energy justice concerns inability to refuse.</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b8-99f0-e1bf5c570457" class="">These are not the same domain.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8023-9458-d0343849f1c9" class="">Electricity is not a discretionary good.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ff-b41f-d87989f838a4" class="">It is a life-support input.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8082-8e3f-c0d9bf75b040" class="">Any system that prices access to life-support will inevitably allocate harm to those with the least bargaining power.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8048-8103-e3a914c2ebdf" class="">This is not ideology.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b3-96f4-c63b35a82391" class="">It is arithmetic.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8047-977a-f7103124113e"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-805e-8256-c8c9b50605a9" class=""><strong>II. What Pricing Can Do — and What It Cannot</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-809d-9577-e5b9653f53eb" class="">Pricing is effective when all of the following are true:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8004-a0b2-f2e97bb8b3ae" class="bulleted-list"><li style="list-style-type:disc">demand is elastic</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8009-abb1-cd810c107992" class="bulleted-list"><li style="list-style-type:disc">consumption is deferrable</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8092-93c3-c0ec168954a9" class="bulleted-list"><li style="list-style-type:disc">users have alternatives</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8054-9c81-d3c6a83c17ec" class="bulleted-list"><li style="list-style-type:disc">refusal is viable</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e1-a3d7-d92ae57e6d92" class="bulleted-list"><li style="list-style-type:disc">consequences are reversible</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f5-867e-fad979c05b70" class="">Energy violates every one of these conditions during stress.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8060-81d6-f87a129f464a" class="">At peak load, during outages, heat waves, medical dependency, or grid failure:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80de-900a-eb9b9eaaf48b" class="bulleted-list"><li style="list-style-type:disc">demand is <strong>inelastic</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d3-84ef-e38e29522edf" class="bulleted-list"><li style="list-style-type:disc">deferral is <strong>lethal</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d4-9e9d-edeebcf7cf08" class="bulleted-list"><li style="list-style-type:disc">alternatives are <strong>unequally distributed</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8041-8fa5-e92726cab79e" class="bulleted-list"><li style="list-style-type:disc">refusal is <strong>biologically constrained</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-804a-831d-f2e48da3d0d5" class="bulleted-list"><li style="list-style-type:disc">consequences are <strong>irreversible</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a2-bd49-db55006b2abf" class="">No price signal can resolve this.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80ea-bd02-f08f59830936"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-803b-8af7-d6e5c6993598" class=""><strong>III. The Lie of “Fair Pricing”</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80e5-bc9d-d6c37d875d4b" class="">Energy markets defend themselves with the concept of fairness:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-80a7-888d-cf092091d386" class="">“Those who use more should pay more.”</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a2-a36b-d57737b4c77b" class="">This collapses under reality.</p></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80ec-865f-d9990c6929e5" class=""><strong>Because people do not consume electricity equally — they</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80d9-bee3-ea56019c755e" class=""><strong>depend</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80ce-bc91-e97e881692e4" class=""><strong>on it unequally.</strong></h3></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b4-94c7-f2b0d419282d" class="bulleted-list"><li style="list-style-type:disc">Medical equipment cannot power down</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ff-af01-fdbae50719cf" class="bulleted-list"><li style="list-style-type:disc">Care work cannot reschedule heat</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-807d-b72d-f176534d8bdd" class="bulleted-list"><li style="list-style-type:disc">Informal labor cannot absorb blackout penalties</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8094-8050-e08ed236660b" class="bulleted-list"><li style="list-style-type:disc">Dense housing cannot self-insure</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8028-a318-c6d134407f6d" class="">Price does not measure dependence.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-806c-b311-fabde2e51de8" class="">It measures liquidity.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80dd-99ed-cac8e32ad426" class="">Liquidity is not justice.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8022-9784-ffe525e25ac1"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80e3-b8a5-c4aa7fe019fe" class=""><strong>IV. Five Things Pricing Always Erases (MECE)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-809f-b515-c1cf15418096" class=""><strong>1. Biological Inelasticity</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8095-be35-c57418c639d1" class="">Bodies cannot negotiate tariffs.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80db-9eb3-c1bdf592cc2e" class="">Heat stress, hypoxia, dehydration, insulin failure — none respond to price signals.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803c-a0eb-d36019158cda" class="">When energy systems spike prices during stress, they are monetizing biology.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80c8-8a29-f2000fba3c02"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-806e-86b8-fe0cac9778a0" class=""><strong>2. Time Asymmetry</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80e4-9345-ca435275e819" class="">Pricing assumes users can plan.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8083-8238-c651d55bc9fd" class="">But energy harm arrives in minutes:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b5-b3e1-f6d60ed47f35" class="bulleted-list"><li style="list-style-type:disc">heat stroke</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-804a-89b4-efe930dd5fd2" class="bulleted-list"><li style="list-style-type:disc">hypothermia</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8061-8d1e-e2c35892caf9" class="bulleted-list"><li style="list-style-type:disc">ICU failure</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8010-8926-ecca0f8667c5" class="bulleted-list"><li style="list-style-type:disc">neonatal risk</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8082-9cf3-ff618ec75fc3" class="">Markets operate on billing cycles.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8042-879e-cc0ef8788eba" class="">Bodies operate on thresholds.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-808e-a3f5-e95b1d4ebbc9"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-804c-be40-f010f3381a3b" class=""><strong>3. Spatial Lock-In</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8037-8923-e494b0496ba8" class="">Energy exposure is geographically fixed.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8065-8e22-fc70c4af734a" class="">You cannot move your apartment when the transformer fails.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-809d-81e1-f5293f75fbff" class="">You cannot relocate your neighborhood when diesel peakers start.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80bb-93ac-d64bca4a13f5" class="">Pricing assumes mobility.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-809a-b0e3-deb775feacf5" class="">Justice must assume immobility.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8057-b1fe-c18cda6352ba"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80ff-8a71-cba041cb5f15" class=""><strong>4. Responsibility Asymmetry</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8009-8d6e-f42c7bfd1bf2" class="">Those who trigger peak load are rarely those who pay for it.</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f6-bd0a-d1a8ab84e5f6" class="bulleted-list"><li style="list-style-type:disc">EV fleets</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-805c-937d-f4818e1669fc" class="bulleted-list"><li style="list-style-type:disc">data centers</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80cd-9696-ecf230e44d14" class="bulleted-list"><li style="list-style-type:disc">industrial loads</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-801a-97f2-cae1271b2af1" class="bulleted-list"><li style="list-style-type:disc">speculative growth</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8000-befc-e6b38308ef72" class="">The costs are pushed downstream:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8052-839c-cdcd503c28b7" class="bulleted-list"><li style="list-style-type:disc">to households</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80bd-9cc5-dcd57579aa6e" class="bulleted-list"><li style="list-style-type:disc">to renters</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80da-8670-f40e91bd41d4" class="bulleted-list"><li style="list-style-type:disc">to neighborhoods</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8015-aad9-c2e545f01c7f" class="bulleted-list"><li style="list-style-type:disc">to workers</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80af-9ee6-c6ac0ad31a7c" class="">Pricing conceals causality.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8097-a5e9-c6963f808245"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-80de-8f61-cd96f3fade04" class=""><strong>5. Irreversibility</strong></h3></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80e9-85ae-c8994a9b7437" class="">Lost income can be recovered.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-809e-a233-de2997342217" class="">Lost equipment can be replaced.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8086-a775-d20306e1e95a" class="">Lost health cannot.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ec-ac02-c3e64e710f98" class="">Pricing systems cannot reverse harm — they can only record it.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8035-b739-cd5c524a9391"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80b6-8c11-d9438442f093" class=""><strong>V. Peak Pricing Is Not Neutral — It Is Violent</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ba-9caa-ec2d2a49eeae" class="">During peak load, pricing performs a specific function:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-80de-a135-e22ce65d9b73" class="">It converts scarcity into coercion.</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a8-8721-cb8d2f06ff9c" class="">When price rises faster than people can adapt:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8078-a77d-e93b7eaf3833" class="bulleted-list"><li style="list-style-type:disc">choice collapses</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-805f-96c4-e7a2246473b7" class="bulleted-list"><li style="list-style-type:disc">consent dissolves</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8034-a451-dcb769402e61" class="bulleted-list"><li style="list-style-type:disc">compliance replaces agency</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80cd-927c-c479c493f873" class="">A choice made under threat is not a choice.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8066-a9af-c2bc9a170c92" class="">It is surrender under design.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-808c-bd83-dd562e53b50d"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8069-af0b-c5f323122ff8" class=""><strong>VI. Why “Targeted Subsidies” Fail</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c9-b4fb-f2b89b2dadc5" class="">Subsidies are offered as the ethical fix.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8048-b665-f13334ff06ac" class="">They fail structurally.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8034-8f84-e13c96252d50" class="">Because:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802a-8704-cbc2ac62b7b1" class="bulleted-list"><li style="list-style-type:disc">they arrive after harm</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8098-b76c-c3ae57f4dd6c" class="bulleted-list"><li style="list-style-type:disc">they require bureaucratic literacy</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ba-9824-e0814b88607b" class="bulleted-list"><li style="list-style-type:disc">they lag real-time crises</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8061-b0c6-cf0cb3ccd1c8" class="bulleted-list"><li style="list-style-type:disc">they assume stability where none exists</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-803a-ba92-ca2dddbd83cd" class="bulleted-list"><li style="list-style-type:disc">they compensate money, not damage</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8076-b4ba-de7e5f6ef7bf" class="">Subsidies are <strong>post-hoc apologies</strong>, not protection mechanisms.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-808d-8a2f-e7cb30d5447e"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8024-a9b1-cbb9685f6c4b" class=""><strong>VII. Energy Justice Is a Constraint Problem, Not a Distribution Problem</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b0-9669-cb26353a9ce2" class="">Justice requires systems to ask a different question:</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8020-a88c-f7709fee3feb" class="">Not:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8029-85cf-de8e494c471a" class="">“Who pays?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8066-9812-f9a83fd6b7ca" class="">But:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-80c4-b20c-e19c208e4280" class="">“Who is protected when the system fails?”</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b0-9176-d9557b455408" class="">This shifts the domain from economics to governance.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80bb-a48f-c8c599ac2d64"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80de-80d5-e196e7b6924e" class=""><strong>VIII. What Energy Justice Actually Requires</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80e8-909f-f513c3cfc600" class="">Energy justice exists only when <strong>five non-priced guarantees</strong> are enforced:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8053-a64f-f261e46a8dd7" class="numbered-list" start="1"><li><strong>Inviolable minimum service</strong><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800c-8605-ca888ba5fe6e" class="">Certain loads must never be shed, regardless of price.</p></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80c8-babe-f04df0c3c8e2" class="numbered-list" start="2"><li><strong>Protected refusal</strong><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8058-816c-f9af9a83f38b" class="">No household may be coerced into unsafe behavior through pricing.</p></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80b8-815c-e966b74b67e7" class="numbered-list" start="3"><li><strong>Peak creators bear peak costs</strong><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8091-9d31-e2e48d2fb004" class="">Demand that creates stress must fund buffers before scaling.</p></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8002-b008-d0e007334f39" class="numbered-list" start="4"><li><strong>Mandatory slack</strong><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8020-9007-f178a53c6cd6" class="">Systems must carry excess capacity, not just theoretical averages.</p></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80a4-af56-deb1b8d939f4" class="numbered-list" start="5"><li><strong>Transparent harm ownership</strong><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80fc-a8b0-c1a0d4c0964f" class="">Downstream risk must be declared before deployment.</p></div></li></ol></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8006-b735-dd64bd5446f2" class="">None of these can be implemented by markets alone.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80b6-86df-e4da1e0d6a7d"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-807d-9775-ec196c0e7fef" class=""><strong>IX. Why Institutions Prefer Pricing</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8099-a952-d455a049df80" class="">Because pricing:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806c-8f02-eb576ace5618" class="bulleted-list"><li style="list-style-type:disc">shifts blame to “consumer choice”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-805d-993a-c8e87841bb9a" class="bulleted-list"><li style="list-style-type:disc">avoids naming winners and losers</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802b-80da-d28a60133e23" class="bulleted-list"><li style="list-style-type:disc">hides structural underinvestment</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8011-9c7e-db6197100c1a" class="bulleted-list"><li style="list-style-type:disc">converts ethical failure into spreadsheets</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-808c-b251-faac04d84d30" class="bulleted-list"><li style="list-style-type:disc">preserves deniability</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8078-9f06-ceb2c0d59b32" class="">Pricing is politically convenient because it is <strong>morally evasive</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-803c-a145-f68008811f7b"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80c6-9bb1-db94747a5131" class=""><strong>X. The Uncomfortable Truth</strong></h2></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-80a1-8237-d9f7151bac47" class="">If a system requires people to suffer correctly in order to function, the system is unjust by design.</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b0-a3af-f1b8292f8a2f" class="">No tariff can fix that.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80bf-b723-eb5cf7e586ad" class="">No rebate redeems it.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-809f-8be0-e4bcf0731323"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8085-8022-f52473d7fbdb" class=""><strong>XI. Energy Justice Is About Limits, Not Discounts</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8046-8b7d-d28cc8c3f6dc" class="">Justice is enforced when systems <strong>refuse to operate beyond safe envelopes</strong>, even if profitable.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ab-b73c-fa23d5365739" class="">That requires:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-809c-8715-d9defd68d2bc" class="bulleted-list"><li style="list-style-type:disc">governance</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8085-b61c-ea0a0bf9209a" class="bulleted-list"><li style="list-style-type:disc">restraint</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ba-a226-c727ec752456" class="bulleted-list"><li style="list-style-type:disc">redundancy</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8036-9462-f769d4ed08e1" class="bulleted-list"><li style="list-style-type:disc">accountability</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8015-b7d7-e1c3303e7ab2" class="bulleted-list"><li style="list-style-type:disc">refusal authority</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800a-bb73-ec54972fc71b" class="">Not dynamic pricing.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-800b-b16c-c883903a82ad"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80f1-aee4-e442016d3726" class=""><strong>XII. The Final Law</strong></h2></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-80b2-94f8-ccd507d1a503" class="">Energy justice cannot be priced because harm is not a commodity and dignity is not demand-responsive.</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8042-8e5f-e99dc670d723" class="">Markets can allocate electricity.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8026-94b5-dc335a753aeb" class="">Only governance can allocate protection.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8021-8bcb-d851a15aeba8"/></div><div style="display:contents" dir="auto"><h3 id="2e4c5e6f-95bd-808d-98a0-f67e7ac3eb5d" class=""><strong>Canonical Close</strong></h3></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-809d-bec3-d73c022281d7" class="">Civilizations fail energy transitions not when technology lags,</blockquote></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-8089-99b0-df86ff01c102" class="">but when they mistake price signals for moral judgment.</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a9-bdab-e78f77741905" class="">When energy systems price justice, they have already decided who may be harmed.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8089-8d2f-f1c7291d751f" class="">And they rarely choose themselves.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8023-bf1e-c0243dabd585"/></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b4-b0b0-d3aa8dbab117" class="">If you want the next lock-in, the natural continuations are:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c8-b05d-cb9c5239cc51" class="bulleted-list"><li style="list-style-type:disc"><strong>“Slack Is the Only Honest Safety Mechanism”</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8029-afee-cc8d9bcd7295" class="bulleted-list"><li style="list-style-type:disc"><strong>“Why Energy Markets Collapse Before Grids Do”</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-807b-995e-d9f39a333d00" class="bulleted-list"><li style="list-style-type:disc"><strong>“When Optimization Becomes Negligence”</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ed-8a1a-f11f189c7e86" class="bulleted-list"><li style="list-style-type:disc"><strong>“The Difference Between Affordability and Safety”</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c6-b837-fd4f68a7e889" class="">Say the word.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
