---
tags: [trang]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>The Seven Cycles of the Trang System™ – Official Manual (Comprehensive Edition)</title><style>
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
	
</style></head><body><article id="2b1c5e6f-95bd-8070-9b16-fc7b5d4eccf0" class="page sans"><header><h1 class="page-title" dir="auto"><strong>The Seven Cycles of the Trang System™ – Official Manual (Comprehensive Edition)</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80c6-93f7-f6ec681f9878" class="">The seven-cycle model of the Trang System™ (TSS) provides a universal structure for understanding how human-linked systems evolve over time. Whether the system is a family, a corporation, a political party, a national government, or a civilization, it moves through the same sequence of structural phases. These cycles describe how systems emerge, grow, overstretch, fracture, face crisis, collapse, and eventually reset into new forms. The model does not depend on cultural background, ideology, or historical moment. It reflects the underlying mechanics of human cooperation, organizational structure, and systemic stress. Because these mechanics are universal, the seven-cycle model provides a common language for analyzing system health, formulating interventions, and anticipating long-term trajectories.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8048-aba2-edc461848b84" class=""><strong>1. Overview of the Seven Cycles</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8030-8fe5-ede310bae2a2" class="">The seven cycles can be summarized as follows:</p></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-80dd-9128-d7803417aabc" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8035-8231-cd2ab3b6a357"><th id="ffjK" class="simple-table-header-color simple-table-header"><strong>Cycle</strong></th><th id="~^W:" class="simple-table-header-color simple-table-header"><strong>Name</strong></th><th id="rdTK" class="simple-table-header-color simple-table-header"><strong>Core Meaning</strong></th><th id="IiR_" class="simple-table-header-color simple-table-header"><strong>Structural Profile (Ω, H, F, S)</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8097-9dc7-e323167bf47a"><td id="ffjK" class="">C1</td><td id="~^W:" class="">Emergence</td><td id="rdTK" class="">Birth of a new system with a unified core</td><td id="IiR_" class="">Ω low, H high, F low, S low</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-802b-9048-d39ab5cbf6e9"><td id="ffjK" class="">C2</td><td id="~^W:" class="">Expansion</td><td id="rdTK" class="">Growth in scale, complexity, and capability</td><td id="IiR_" class="">Ω rising, H strong, F low–moderate, S mild</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8008-95bb-e7b4a18026a4"><td id="ffjK" class="">C3</td><td id="~^W:" class="">Peak &amp; Overreach</td><td id="rdTK" class="">Maximum capability with rising strain</td><td id="IiR_" class="">Ω high, H declining, F rising, S increasing</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-802b-b0cc-cebb8112b725"><td id="ffjK" class="">C4</td><td id="~^W:" class="">Fragmentation</td><td id="rdTK" class="">Internal splitting and weakened coordination</td><td id="IiR_" class="">Ω high, H low, F high, S moderate</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80ac-905b-cf361916ade0"><td id="ffjK" class="">C5</td><td id="~^W:" class="">Crisis–Shock</td><td id="rdTK" class="">Major disruption forces structural confrontation</td><td id="IiR_" class="">S high, H unstable, F high, Ω high</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-808e-ad22-ca03cdcbded8"><td id="ffjK" class="">C6</td><td id="~^W:" class="">Collapse</td><td id="rdTK" class="">Old model stops functioning; authority breaks down</td><td id="IiR_" class="">Ω unsustainable, H minimal, F extreme</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8035-95cb-f9218777407f"><td id="ffjK" class="">C7</td><td id="~^W:" class="">Reset</td><td id="rdTK" class="">New model forms; system stabilizes</td><td id="IiR_" class="">Ω falling, H rising, F falling, S controlled</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80fa-ac4e-eb6cca123ebc" class="">Each cycle reflects a combination of internal pressure and external conditions. Understanding these cycles enables early detection of systemic drift and timely intervention.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8080-b7c0-c51135f08e6a" class=""><strong>2. C1 – Emergence</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8060-87ed-de36977d71b6" class="">C1 is the foundational phase where a new system forms. It may be a newly established organization, a newly independent country, a startup, or a reform coalition. The defining feature of C1 is unity. Members share a common vision, trust is high, and complexity is low. Because the system is small and the environment relatively simple, overload remains low. This allows rapid response to challenges and strong alignment around foundational decisions. Decisions made in C1 shape long-term identity. Systems with strong C1 foundations typically retain resilience even during later crises.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-8061-9af3-de6d31506bbc" class=""><strong>Characteristics of C1</strong></h3></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-8011-9483-cc1f96c8e74d" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8048-bb05-e4b2ee358a3f"><th id="xtkz" class="simple-table-header-color simple-table-header"><strong>Dimension</strong></th><th id="J_Y;" class="simple-table-header-color simple-table-header"><strong>Description</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-809e-9e51-d0683b3427ae"><td id="xtkz" class="">Identity</td><td id="J_Y;" class="">Clear and cohesive</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-803e-98c0-e9a5526b7b17"><td id="xtkz" class="">Leadership</td><td id="J_Y;" class="">Centralized or unified</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8020-ad1f-d8606d2515f9"><td id="xtkz" class="">Governance</td><td id="J_Y;" class="">Simple and adaptable</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-806d-b248-e6fbbc338211"><td id="xtkz" class="">Risks</td><td id="J_Y;" class="">Overconcentration of power; vulnerability to early shocks</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80bf-bc00-cc0c7324cd04" class="">C1 systems benefit from simplicity, but they require careful transition into C2 to avoid stagnation or early instability.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-808a-a0bf-da2c79b28667" class=""><strong>3. C2 – Expansion</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80c8-8b40-eed8b7d0a0f0" class="">In C2, the system begins to grow—expanding membership, markets, territory, influence, or institutional capacity. This growth increases complexity, workload, and resource demands. Cohesion generally remains high because the system still carries forward the unity established in C1. However, the early signs of overload appear as responsibilities begin to outpace capacity. C2 is often the most optimistic phase. Systems feel capable and successful, and external observers may view them as rising powers. Successful navigation of C2 requires balancing growth with capacity development.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-80a0-98b5-d6f76eb5591f" class=""><strong>Characteristics of C2</strong></h3></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-8085-b0b9-d84615a4debf" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8078-b7d4-def94dec0f10"><th id="TxoU" class="simple-table-header-color simple-table-header"><strong>Dimension</strong></th><th id="fIk[" class="simple-table-header-color simple-table-header"><strong>Description</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8012-b925-f22749519709"><td id="TxoU" class="">Capability</td><td id="fIk[" class="">Increasing rapidly</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8043-b862-f4ce879daaf7"><td id="TxoU" class="">Complexity</td><td id="fIk[" class="">Growing but manageable</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-804b-a0b2-de46d1d05048"><td id="TxoU" class="">Cohesion</td><td id="fIk[" class="">Strong but diluted by scale</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8087-a611-d97485ec6800"><td id="TxoU" class="">Risks</td><td id="fIk[" class="">Excessive growth without infrastructure; leadership bottlenecks</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8036-829b-d778c07b6689" class="">If the system expands too quickly or fails to build strong institutions, C2 transitions into C3 with structural weaknesses already in place.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-806a-9801-c250de482628" class=""><strong>4. C3 – Peak and Overreach</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-806b-a192-d1e8374aa074" class="">C3 represents the height of the system’s influence. It appears strong from the outside: abundant resources, sophisticated institutions, and a reputation for stability or dominance. However, internally, the system is under rising strain. Overload is high due to accumulated responsibilities, bureaucratic expansion, or institutional drag. Cohesion begins to erode as subgroups develop divergent interests. Fragmentation emerges as competition forms between regions, departments, factions, or internal elites. C3 is inherently unstable. Without intervention, systems in C3 drift toward C4 or C5.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-8007-b3da-d1e734aeb78b" class=""><strong>Characteristics of C3</strong></h3></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-8091-84bd-f7bc18afb3a8" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80c2-a71a-fdc32b594621"><th id="aQ_c" class="simple-table-header-color simple-table-header"><strong>Dimension</strong></th><th id=":BGn" class="simple-table-header-color simple-table-header"><strong>Description</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8045-91cf-c7e35f297e5a"><td id="aQ_c" class="">Strength</td><td id=":BGn" class="">Externally impressive</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-805b-9a0b-db3dbcb55873"><td id="aQ_c" class="">Strain</td><td id=":BGn" class="">Internally rising</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-804f-8d00-c34191eec06b"><td id="aQ_c" class="">Efficiency</td><td id=":BGn" class="">Declining due to complexity</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8068-aab5-c017c432b777"><td id="aQ_c" class="">Risks</td><td id=":BGn" class="">Overconfidence, institutional fatigue, delayed reform</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8079-b771-f7dc570d3314" class="">This is the phase where timely reform can redirect the system toward renewal (C7) without passing through crisis or collapse.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-800b-a736-f39e8d87b17d" class=""><strong>5. C4 – Fragmentation</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80bf-84b7-e4eb5f6777d0" class="">C4 occurs when internal divisions grow stronger than internal unity. The system is still formally intact, but coordination breaks down. Subgroups begin to operate semi-independently, and shared identity weakens. Fragmentation may be political (factionalism), organizational (departmental silos), regional (autonomous zones), or ideological (parallel narratives). Overload remains high, but cohesion collapses. The system becomes reactive, slow, and unable to implement reforms. Without external pressure, C4 may persist for years; however, the arrival of a shock typically accelerates movement toward C5.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-80b9-a87b-d9574f8176a6" class=""><strong>Characteristics of C4</strong></h3></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-802b-92af-cac411bf53b9" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8007-a50d-f33bc70b17e0"><th id="kAWD" class="simple-table-header-color simple-table-header"><strong>Dimension</strong></th><th id="ksZs" class="simple-table-header-color simple-table-header"><strong>Description</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80ed-9385-c04456a7dd68"><td id="kAWD" class="">Identity</td><td id="ksZs" class="">Fragmented</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8011-b076-c45e7196c386"><td id="kAWD" class="">Governance</td><td id="ksZs" class="">Uneven or contested</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8018-8acd-eb819592ae2d"><td id="kAWD" class="">Coordination</td><td id="ksZs" class="">Low</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80fb-889d-f135b63690ff"><td id="kAWD" class="">Risks</td><td id="ksZs" class="">Paralysis, competing power centers, policy gridlock</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-803f-8681-fb9e1720f136" class="">C4 is a fragile equilibrium. It can be reversed only through strong, broad-based reform that rebuilds cohesion.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-805c-a209-d22e6b0f3971" class=""><strong>6. C5 – Crisis–Shock</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b8-a076-e01366bce607" class="">C5 is triggered when a major disruptive event collides with an already stressed or divided system. Examples include financial crises, wars, pandemics, political breakdowns, institutional scandals, or environmental disasters. The crisis exposes structural weaknesses accumulated during earlier cycles and forces difficult decisions. In C5, the system must adapt or fail. The outcome depends on leadership response, cohesion reserves, and shock management capacity. A system with moderate cohesion and effective crisis management can transition from C5 to C7. A system with extreme fragmentation or high overload tends to move to C6.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-8095-827a-d63624b52e55" class=""><strong>Characteristics of C5</strong></h3></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-80a2-a859-f7b0e15debbb" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-801f-bb7a-fdf81bf6896d"><th id="Bir`" class="simple-table-header-color simple-table-header"><strong>Dimension</strong></th><th id="Wpd{" class="simple-table-header-color simple-table-header"><strong>Description</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8075-b7d0-e612e28dd43f"><td id="Bir`" class="">Conditions</td><td id="Wpd{" class="">Volatile and unpredictable</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-801e-95e2-d3f1e75a9ac9"><td id="Bir`" class="">Governance</td><td id="Wpd{" class="">Crisis-driven, improvisational</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8023-804f-ec8adc4a4fe9"><td id="Bir`" class="">Risks</td><td id="Wpd{" class="">Rapid escalation, irreversible damage</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8079-b839-dbb1d533e4fa"><td id="Bir`" class="">Opportunity</td><td id="Wpd{" class="">Window for major reform or reset</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80fc-903b-d9f1962bdb2a" class="">C5 is not inherently negative; many systems transform positively under crisis pressures if underlying cohesion is not fully depleted.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80a5-9655-c8cb2815b20f" class=""><strong>7. C6 – Collapse</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8085-8cd1-e729aca62542" class="">C6 occurs when the old structure can no longer function. Collapse does not necessarily mean destruction; it means the existing model loses authority and operational capacity. Institutions break down, rules cease to be followed, and power may shift rapidly. Collapse can be partial or complete. Partial collapse affects only parts of the system (e.g., certain institutions), while full collapse ends the old model entirely. The key feature of C6 is that the system cannot return to previous cycles without restructuring.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-80f4-b757-fc54f77b9f6d" class=""><strong>Characteristics of C6</strong></h3></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-8005-a253-ebf97e25a6aa" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8020-a29c-ed4cbbc4b072"><th id="{F]&lt;" class="simple-table-header-color simple-table-header"><strong>Dimension</strong></th><th id="mvrp" class="simple-table-header-color simple-table-header"><strong>Description</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80d8-8433-fcbc40547644"><td id="{F]&lt;" class="">Institutions</td><td id="mvrp" class="">Fail or lose legitimacy</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8042-82ee-d8c7ae1fb31e"><td id="{F]&lt;" class="">Order</td><td id="mvrp" class="">Fragmented or absent</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80a2-8a96-c6ed01b6b49e"><td id="{F]&lt;" class="">Risks</td><td id="mvrp" class="">State failure, organizational shutdown, systemic vacuum</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80c3-bdfa-e501780cbcf5"><td id="{F]&lt;" class="">Transition</td><td id="mvrp" class="">Moves toward one of the four long-term outcomes</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8054-b3c8-f68650538c27" class="">C6 is the end of “how things used to work,” but not necessarily the end of the system.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80a2-bc65-e73aa1193118" class=""><strong>8. C7 – Reset</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-802b-96db-dffc52072957" class="">C7 is the phase of reconstruction and reconfiguration. A new model emerges—new leadership, new institutions, new policies, new identity, new narrative. Cohesion slowly increases as new social contracts or organizational charters take shape. Overload decreases because the system reduces responsibilities or simplifies its structure. Fragmentation declines as old divisions are resolved or lose relevance. C7 marks the beginning of a new cycle that eventually flows back into C1 and C2. Reset may be peaceful or turbulent, depending on the conditions under which C6 ended.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-80d9-993a-d485fe0688da" class=""><strong>Characteristics of C7</strong></h3></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-80c0-a990-c54ff67cae68" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8004-9b1a-fe10295f1d2b"><th id="[lzE" class="simple-table-header-color simple-table-header"><strong>Dimension</strong></th><th id="Y=Ko" class="simple-table-header-color simple-table-header"><strong>Description</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-801b-98da-f7ff7044757a"><td id="[lzE" class="">Structure</td><td id="Y=Ko" class="">Rebuilt on new foundations</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-805a-9122-c8af024880ca"><td id="[lzE" class="">Cohesion</td><td id="Y=Ko" class="">Strengthening</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80cb-8f5f-e30af44cdc80"><td id="[lzE" class="">Overload</td><td id="Y=Ko" class="">Lower than before collapse</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8019-9e4b-ca3716058dd9"><td id="[lzE" class="">Risks</td><td id="Y=Ko" class="">Incomplete reform, return of old patterns</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8030-a669-e900ef5bc0f4" class="">Successful resets require sustained commitment to institutional rebuilding.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-801e-a8b1-d72f12d1b328" class=""><strong>9. Why the Seven Cycles Always Appear</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80f5-8d49-d26752b7ebe6" class="">Human systems repeatedly move through these cycles because the structural forces behind them arise from basic human behavior:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8094-9e07-ff206f2312dc" class="">Growth increases complexity, eventually creating overload.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8019-959b-d6c76c91c8b4" class="">Diversity and scale reduce cohesion over time.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-808b-9d29-c4bce5302162" class="">Overload and declining cohesion produce fragmentation.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80aa-9e64-ddf40229e785" class="">Fragmentation increases vulnerability to shocks.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ba-a249-fe5cea47f9cf" class="">Shocks force crisis or collapse.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8054-8777-c5b77dc82488" class="">Collapse creates opportunity for reset.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8019-a884-d20f6ac56922" class="">Resets produce unity and low complexity, restarting the cycle.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-807d-bfaa-c846f208bd0d" class="">This pattern has been observed across ancient empires, modern governments, large corporations, social movements, and digital networks. The cycles are not rigid; their timing varies. But the underlying sequence remains consistent.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-801a-9d75-d9315515393a" class=""><strong>10. Practical Use of the Seven Cycles</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-801b-afed-c2186b7b0b2f" class="">The seven cycles help decision-makers by:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8021-9cee-eab11822c5ec" class="">Identifying a system’s current position</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8086-9eb0-c679d02fdb9c" class="">Assessing its structural risks</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-809d-a5df-f1d4a1171326" class="">Anticipating the next likely transition</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80d1-9c6c-ed5f829ab787" class="">Choosing interventions that change the trajectory</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-803e-b853-f8bd79a4c2db" class="">Designing institutions that resist overload and fragmentation</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8098-b673-edb7e2455a2c" class="">By grounding decisions in cycle logic rather than short-term events, leaders gain a clearer view of long-term outcomes.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-808b-b0c5-d8e58a4afba4" class=""><strong>11. Summary</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8095-afe4-fac51b92e8d2" class="">The seven cycles of the Trang System™ provide a complete and universal framework for understanding how human-linked systems evolve. They describe how systems are born, grow, overstretch, fragment, encounter crisis, collapse, and rebuild. These cycles form the structural backbone of TSS and serve as the foundation for forecasting through the Trang Prediction Engine™. Together, they create a powerful tool for governance, resilience planning, institutional design, and civilizational foresight.</p></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-8018-aaf3-fb7398d596ea"/></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ca-9e7d-edb80af57f52" class="">If you want, I can now produce:</p></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-8031-8910-d688e86c02bc" class="bulleted-list"><li style="list-style-type:disc">a visual diagram version</li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-80bc-b8e5-e8f8daaf51fb" class="bulleted-list"><li style="list-style-type:disc">a training curriculum for policymakers</li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-8071-bf89-f8a1cbdeb7de" class="bulleted-list"><li style="list-style-type:disc">a case-study book applying all 7 cycles</li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-8028-8fda-c336dc1af707" class="bulleted-list"><li style="list-style-type:disc">or a combined TSS + 7 Cycles master edition</li></ul></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
