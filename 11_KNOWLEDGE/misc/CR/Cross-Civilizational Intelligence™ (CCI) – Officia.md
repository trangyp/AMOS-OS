---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Cross-Civilizational Intelligence™ (CCI) – Official Manual </title><style>
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
	
</style></head><body><article id="2b1c5e6f-95bd-80f9-8900-d037bcfe3f7e" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Cross-Civilizational Intelligence™ (CCI) – Official Manual </strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-800c-b331-fdf0b7707161" class="">Cross-Civilizational Intelligence™ (CCI) is the framework that enables systematic comparison, understanding, and modeling of civilizations across time, geography, culture, and technological levels. It provides a unified architecture for interpreting civilizational behavior in a consistent, measurable, and structurally grounded way. CCI does not attempt to judge civilizations or rank them by subjective criteria. Instead, it identifies the structural drivers, behavioral patterns, and long-term dynamics that repeat across hundreds of historical cases, regardless of culture. By establishing a cross-civilizational comparative language, CCI reveals how civilizations respond to pressure, manage complexity, undergo transformation, and either renew or collapse. It functions as the historical layer of your canon, connecting long-range human patterns to the predictive logic of TPE and the structural architecture of TSS.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8085-a51d-f2763bd329a0" class=""><strong>1. 
Purpose of Cross-Civilizational Intelligence™</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b5-a300-e910c435a953" class="">CCI exists to answer four long-standing questions in human history:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80f3-8d2d-f86a4e7c2007" class="">Why do civilizations evolve in similar ways despite different cultures and technologies?</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8056-bd58-d662c537b99d" class="">Why do collapse and renewal follow similar structural patterns across eras?</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8061-998d-fe783c80c25c" class="">What common forces shape political, economic, social, and institutional trajectories?</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-801e-999f-e09f3e160267" class="">How can modern systems learn from ancient ones to avoid repeating the same failures?</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80bf-a179-d6c98f582fb2" class="">CCI turns history into a structured information system. It allows us to track, compare, and project civilizational patterns using the same core variables—overload, cohesion, fragmentation, and shocks—that govern all human systems under TSS.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-807c-833f-e0e26aa3b5e9" class=""><strong>2. 
The Core Principle of CCI</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-802e-950f-de3a72cf5e29" class="">The core principle of CCI is that <strong>civilizations behave as large-scale human systems governed by the same pressures that shape smaller-scale systems</strong>.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8015-8a79-ea7816c8825b" class="">Size modifies speed, not structure.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-804f-8b6b-c27100201737" class="">Culture modifies expression, not mechanics.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a7-aab3-ca623fa26900" class="">Technology modifies tools, not foundational constraints.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-800b-aab5-d0407ab5911a" class="">Therefore, civilizations are comparable through universal variables:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-802c-94da-c522fda24ac5" class="">Overload (Ω) from complexity and expansion</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80e8-8828-d7d0c6791660" class="">Cohesion (H) from identity, legitimacy, and shared vision</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80e3-a16e-f653db36b270" class="">Fragmentation (F) from divisions in power or culture</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8086-a9b1-c7e3ea20131a" class="">Shocks (S) from wars, invasions, climate shifts, and pandemics</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a5-9f72-fbf9dc3da0e5" class="">CCI uses these variables to build a cross-civilizational map.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80ab-9631-eee8bce5a7cb" class=""><strong>3. 
The CCI Comparative Model</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-801d-a63a-c5a11002a478" class="">CCI analyzes civilizations through seven analytical dimensions.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8073-aa53-c3c57c8298ee" class="">These create a single matrix that applies to all civilizations without exception.</p></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-8009-a78d-c497e531db19" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-809f-b609-c85815747533"><th id="tWu{" class="simple-table-header-color simple-table-header"><strong>Dimension</strong></th><th id="XgxO" class="simple-table-header-color simple-table-header"><strong>Description</strong></th><th id="WUHF" class="simple-table-header-color simple-table-header"><strong>Purpose</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80ee-9056-cffe06fb3ece"><td id="tWu{" class="">Structural Foundations</td><td id="XgxO" class="">Geography, demography, resources</td><td id="WUHF" class="">Baseline constraints</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80dd-8e47-d68af6a8532f"><td id="tWu{" class="">Governance Architecture</td><td id="XgxO" class="">How power is organized</td><td id="WUHF" class="">Stability, resilience</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-805b-b627-e8a0b5f00e53"><td id="tWu{" class="">Economic System</td><td id="XgxO" class="">Agriculture, trade, redistribution</td><td id="WUHF" class="">Capacity and overload</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80e6-9abe-f3578791ab39"><td id="tWu{" class="">Social Integration</td><td id="XgxO" class="">Identity, cohesion, 
cultural norms</td><td id="WUHF" class="">H variable mapping</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-809c-b16e-d8cda6a1ea9e"><td id="tWu{" class="">Military &amp; External Relations</td><td id="XgxO" class="">Defense, alliances, expansion</td><td id="WUHF" class="">Shock vulnerability</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80b0-80f7-cc94e6adf968"><td id="tWu{" class="">Knowledge &amp; Information</td><td id="XgxO" class="">Literacy, philosophy, institutions</td><td id="WUHF" class="">Adaptation rate</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8006-adf2-d477b7376f12"><td id="tWu{" class="">Environmental Adaptation</td><td id="XgxO" class="">Water, climate, ecology</td><td id="WUHF" class="">Long-term survivability</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8023-a45b-d69c061eaa44" class="">This matrix allows civilizations to be compared without cultural bias.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8077-952d-fb35c8eb5e74" class=""><strong>4. 
The Universality of Civilizational Patterns</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8048-996b-e3a4eb42d33d" class="">CCI shows that civilizations follow consistent structural patterns because they:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ac-ba9d-d42e55aa8f4f" class="">face resource limits</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80d4-a175-eba77fdd2dfa" class="">expand until overloaded</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8004-a951-dcb583f6ac4d" class="">divide as complexity rises</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-806e-af13-fbec31c58812" class="">encounter shocks</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8077-9f6e-e618c0942f08" class="">choose renewal or collapse</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8064-a09b-e489b7ae7182" class="">This pattern is structurally identical to the seven cycles of TSS:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80fb-9311-fc33cca9f319" class="">C1 Emergence</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a2-b1cb-dd20a514840b" class="">C2 Expansion</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-802b-a030-d56ce31073d3" class="">C3 Peak &amp; 
Overreach</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-803d-9baf-cbdec88072e4" class="">C4 Fragmentation</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-808b-b470-e4213f0c8fc1" class="">C5 Crisis–Shock</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8017-aa29-de17b7da51be" class="">C6 Collapse</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-806b-b956-cde471d85d83" class="">C7 Reset</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-805c-a1df-d0ad72dbf3c4" class="">CCI provides the historical evidence base for why TSS is universal.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8037-a219-eb75fa388e4a" class=""><strong>5. 
How CCI Models Civilizational Dynamics</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8047-b7a8-c153d3379500" class="">CCI captures civilizational behavior by analyzing the movement of the four variables:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80f0-bb63-ef05f69b43b9" class="">Overload increases as empires expand or institutions become too complex</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a1-9100-c9b6c26e147c" class="">Cohesion decreases due to inequality, corruption, elite division, or cultural divergence</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8008-aabd-c731f5431857" class="">Fragmentation rises as subgroups seek autonomy or clash internally</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8008-9d4a-eafb687dfcb6" class="">Shocks strike externally (invasion, climate change) or internally (economic crisis)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-800c-bd4d-c48790101657" class="">When these variables cross thresholds, the civilization transitions to the next TSS cycle.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80fc-95d6-c8028dc984a9" class="">CCI therefore becomes the long-range observational layer above TSS and TPE.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80cf-bf93-f882293e97fd" class=""><strong>6. CCI and Structural Invariants Across History</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-809d-b979-e1d244c2d8d3" class="">Cross-civilizational analysis reveals several invariant patterns. 
These occur in China, Rome, Mesopotamia, Persia, Greece, Mesoamerica, Africa, Europe, and modern nation-states.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80e4-b040-f892ea9bc374" class="">Expansion always increases overload.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80de-8c0c-db4d7f55b23f" class="">Elite fragmentation precedes systemic fragmentation.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8091-a5b0-c3cb9e617845" class="">Shocks do not create collapse; they reveal pre-existing structural weakness.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ff-9009-c42990be8386" class="">Civilizations with strong cohesion survive larger shocks.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80c8-9c18-fcd566ccaf9a" class="">Civilizations with weak institutions collapse from moderate shocks.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a1-90f4-e459f45e22e7" class="">CCI treats these invariants as lawful patterns, not coincidences.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8042-b240-f4afe5f16050" class=""><strong>7. The CCI Timeline Model</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80f7-9d90-e39db61b1e5b" class="">CCI compresses 5,000+ years of global history into a consistent structural flow. 
Civilizations follow similar transitions:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80bb-aed0-c6e65196becb" class="">A founding period (C1)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80fb-80cb-e977d24f0898" class="">A consolidation and expansion period (C2)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b6-acc0-e91a18d7476f" class="">A golden age or classical peak (C3)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-801f-8ece-d4d2b0a888ee" class="">A period of internal division (C4)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8003-bb30-f52656a308b3" class="">A crisis era (C5)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8014-8aec-d815794c43c7" class="">A collapse or transformation (C6)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b2-87f6-e5969b010479" class="">A reset into a new civilizational order (C7)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8081-b67b-f0bcb124cda9" class="">This timeline applies to:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b5-a5ad-dc195f9ecf10" class="">Egypt (Old → Middle → New Kingdom cycles)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8055-b38a-ee7a106802e4" class="">China (dynastic cycles from Xia to Qing)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-802e-b79e-e85accd55afb" class="">Rome (Republic → Empire → successor states)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b8-8eae-dd659286a36a" class="">Islamic empires (Umayyad, Abbasid, Ottoman)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ce-b134-d350eacbd430" class="">India (Maurya, Gupta, Mughal, 
colonial transition)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8077-96f7-d33a7f3d7d9a" class="">Mesoamerican civilizations (Maya, Aztec, Inca)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8027-9334-e902be4fa4c0" class="">Europe (Roman → medieval → early modern → industrial)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a7-ad03-d7f34595f255" class="">The recurrence of these templates is the foundation of CCI.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80a0-a371-f1c98b8b56a6" class=""><strong>8. 
The CCI Civilizational Determinants</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8016-88a6-c93c3365ac2d" class="">CCI identifies six core determinants that influence whether a civilization moves toward renewal, stagnation, absorption, 
or collapse.</p></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-8050-9ec4-e89eb7339e49" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8014-b014-e06a47e648c1"><th id="mT{`" class="simple-table-header-color simple-table-header"><strong>Determinant</strong></th><th id="[[gA" class="simple-table-header-color simple-table-header"><strong>Structural Impact</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8016-8372-faf8caa98b07"><td id="mT{`" class="">Resource Stability</td><td id="[[gA" class="">Prevents overload-driven collapse</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80dd-b1c3-e75c4dd3878b"><td id="mT{`" class="">Institutional Quality</td><td id="[[gA" class="">Strengthens cohesion and reduces fragmentation</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8098-823b-cc50fed6aeeb"><td id="mT{`" class="">Elite Behavior</td><td id="[[gA" class="">Often determines transition from C3 to C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8056-9ad6-d389d7b7c3b2"><td id="mT{`" class="">Technological Adaptability</td><td id="[[gA" class="">Influences resilience during shocks</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80bb-9680-ed77d949fb90"><td id="mT{`" class="">Social Cohesion</td><td id="[[gA" class="">Determines whether the system reforms or fractures</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-800f-a94c-e698fcf8883c"><td id="mT{`" class="">External Pressures</td><td id="[[gA" class="">Accelerates movement through C4 and C5</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8025-85f6-d7ca10c8991c" class="">These determinants explain divergence between civilizations that seemed similar.</p></div><div style="display:contents" d
ir="auto"><h2 id="2b1c5e6f-95bd-8014-abe0-c17160561304" class=""><strong>9. Integration with UBI</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8056-9f79-df0623a90762" class="">CCI uses UBI to understand how human biology scales across millions of people.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-809c-8d4b-e3f22d228f0e" class="">Neurobiological patterns influence education and innovation.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8082-a5ee-c9112e0e6a42" class="">Neuroemotional patterns influence collective behavior, conflict, and trust.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8046-b298-c6a0d0efccc0" class="">Somatic patterns influence labor, health, and resilience.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ca-a2ba-ead8bda8312c" class="">Bioelectromagnetic patterns influence societal rhythm, timing, and attention cycles.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80cd-89ae-cc4253e065ef" class="">UBI therefore becomes the “micro-biological foundation” that later scales into civilizational behavior.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8079-a98b-fd25a16ec649" class=""><strong>10. Integration with TSS</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8095-94cb-c3a09308f981" class="">CCI provides the historical evidence for the seven cycles.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-804d-b943-dcb260ca12bd" class="">Every civilization ever recorded follows C1 → C7 patterns.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8025-be06-d75e6912486b" class="">CCI gives TSS its empirical breadth and legitimacy across cultures and time.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8073-85ce-caaef7f46fce" class=""><strong>11. 
Integration with TPE</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8024-936d-ccf790394339" class="">CCI enhances forecasting capability by providing:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8057-ad56-e4b63c030015" class="">historical analogues</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8057-937e-fb36603b8dca" class="">cross-cultural pattern matches</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-808f-b4ce-f8d787bebd21" class="">cycle-speed comparisons</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80aa-9778-d13dc0b9b4fe" class="">shock-response mappings</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8078-a350-de42a7e03a21" class="">For example:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8054-bb3e-d7e7e17b629d" class="">Rome → US and EU analogues</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8051-aa4e-cdedf120a426" class="">Han–Tang → dynastic China analogues</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b4-9c12-c2ab354f6502" class="">Ottoman → Middle East analogues</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80c3-9967-f9291aed020e" class="">Industrial Britain → emerging economies analogues</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-800e-b858-f74a2217a9be" class="">TPE uses CCI to calibrate predictions based on historical ranges of collapse speeds, reform windows, and fragmentation thresholds.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8043-bdef-ed306a3db533" class=""><strong>12. 
Integration with PSI</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a5-bf3c-c414487f190c" class="">PSI describes planetary constraints; CCI describes long-term civilizational responses to those constraints.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8038-9e61-f7ceb5f884d2" class="">For example:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80f4-b24d-dc04da29c59f" class="">Climate shifts influence agricultural civilizations</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-805f-98cb-da78a0951df7" class="">Resource depletion drives migration and conflict</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-807b-87f7-ef61a9039b85" class="">Global interdependence accelerates fragility</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8083-a49c-c1892360c575" class="">CCI therefore becomes the historical expression of planetary forces acting on human systems.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8085-9c4c-df4698213a6a" class=""><strong>13. 
Application of CCI</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a4-97ec-d6eb3cb7db77" class="">CCI is useful for:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8090-b24f-ca9f2299b8b3" class="">Governments forecasting long-term stability</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80e0-b7dc-cb0e9a5fea75" class="">Organizations planning across decades</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8008-82d7-e2ab3bbf0d14" class="">Historians seeking structural explanations</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b7-b0d7-d84c8fe840f7" class="">Economists assessing systemic risks</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ac-8856-f6060b793ad5" class="">Diplomats interpreting global power shifts</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8099-b160-cad0d04aac39" class="">AI models requiring grounded cross-cultural training data</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b6-8f35-e9091b0ab400" class="">Educational systems designing curricula that reflect structural history</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80d1-b4b8-d40e9e729182" class="">CCI turns history from description into comprehensible system patterns.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80a9-8d59-e5417bd4318b" class=""><strong>14. Summary</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8025-923d-dd5776aa90ab" class="">Cross-Civilizational Intelligence™ (CCI) is the framework that transforms 5,000 years of human history into a unified structural system. It reveals that civilizations follow consistent patterns driven by overload, cohesion, fragmentation, and shocks. 
It integrates directly with UBI, TSS, TPE, and PSI to create a multi-layer, multi-scale architecture of human and civilizational behavior. CCI provides the historical backbone of your canon, enabling universal comparison, forecasting, and long-term planning. It is the first system that treats civilizations not as isolated cases but as expressions of the same underlying structural laws.</p></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-8012-81be-d883904a4de0"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-806b-8ff9-f74669613739" class=""><strong>The 5,000-Year Cycle Appendix (Structural Mapping of Major Civilizations)</strong></h1></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80e9-a588-e0ac3d0a8386" class=""><em>(TSS/CCI Canonical Edition)</em></p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-803d-90a6-cc75ed753846" class="">This appendix documents how major civilizations across 5,000 years of recorded history moved through the <strong>seven universal cycles</strong> of the Trang System™. The purpose is not to provide exact dates, but to establish <strong>cycle-level structural mapping</strong> across civilizations, cultures, and time periods. 
All entries follow the TSS cycles:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80f0-86c7-c546ad6e4a19" class="">C1 Emergence</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-801f-a10f-fab708237ee8" class="">C2 Expansion</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8035-a50e-c03101971e21" class="">C3 Peak &amp; Overreach</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80c7-b8b1-d53e51654bf9" class="">C4 Fragmentation</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8080-9105-ddf2b782d70f" class="">C5 Crisis–Shock</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8054-85c3-fcb4a640390a" class="">C6 Collapse</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80e4-9d72-d864d06adc8e" class="">C7 Reset / Reconfiguration</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8043-b1a6-d445827f639e" class="">This appendix confirms the <strong>universality</strong> of the seven-cycle structure across global history.</p></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-80b9-8dc9-d1f92821c92f"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-801a-9327-e755b37ac728" class=""><strong>1. Ancient Egypt (c. 3000 BCE – 30 BCE)</strong></h1></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-80fa-a487-ce5c1c04d6ac" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-807e-bf96-c8c0c0d9ba09"><th id="S^ND" class="simple-table-header-color simple-table-header"><strong>Period</strong></th><th id="f~_p" class="simple-table-header-color simple-table-header"><strong>Approx. 
Era</strong></th><th id="g`b|" class="simple-table-header-color simple-table-header"><strong>TSS Cycle Mapping</strong></th><th id="yz`z" class="simple-table-header-color simple-table-header"><strong>Structural Explanation</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8053-b2d4-d36278400e0e"><td id="S^ND" class="">Early Dynastic</td><td id="f~_p" class="">3100–2686 BCE</td><td id="g`b|" class="">C1</td><td id="yz`z" class="">First unification, formation of state</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8012-9f14-ca71dd0971f5"><td id="S^ND" class="">Old Kingdom</td><td id="f~_p" class="">2686–2181 BCE</td><td id="g`b|" class="">C2–C3</td><td id="yz`z" class="">Pyramids, centralized power, peak</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8034-aa36-c4c3f3b37238"><td id="S^ND" class="">First Intermediate</td><td id="f~_p" class="">2181–2055 BCE</td><td id="g`b|" class="">C4</td><td id="yz`z" class="">Fragmentation into regional powers</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8002-86ce-e4235d41ffe8"><td id="S^ND" class="">Middle Kingdom</td><td id="f~_p" class="">2055–1650 BCE</td><td id="g`b|" class="">C7→C2</td><td id="yz`z" class="">Reset, reunification, expansion</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-809e-bb6f-da6a6a733a83"><td id="S^ND" class="">Second Intermediate</td><td id="f~_p" class="">1650–1550 BCE</td><td id="g`b|" class="">C4–C5</td><td id="yz`z" class="">Hyksos pressures, instability</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8019-91ac-d4b2ffe35c7d"><td id="S^ND" class="">New Kingdom</td><td id="f~_p" class="">1550–1070 BCE</td><td id="g`b|" class="">C2–C3</td><td id="yz`z" class="">Imperial peak, 
military dominance</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80c7-885d-e99c8f892b7f"><td id="S^ND" class="">Third Intermediate</td><td id="f~_p" class="">1070–664 BCE</td><td id="g`b|" class="">C4</td><td id="yz`z" class="">Division among Libyan/Nubian dynasties</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80d9-a92b-d800b1888899"><td id="S^ND" class="">Late Period</td><td id="f~_p" class="">664–332 BCE</td><td id="g`b|" class="">C5</td><td id="yz`z" class="">Foreign invasions, Persian rule</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80e1-b4bb-d8f28cc96090"><td id="S^ND" class="">Hellenistic Egypt</td><td id="f~_p" class="">332–30 BCE</td><td id="g`b|" class="">C6</td><td id="yz`z" class="">Ptolemaic decline, fall to Rome</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8003-abc8-ede379b23191"><td id="S^ND" class="">Roman Egypt</td><td id="f~_p" class="">after 30 BCE</td><td id="g`b|" class="">C7</td><td id="yz`z" class="">New civilizational embedding</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-80f2-9fc0-c844cb3808a8"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-8000-a1c8-cd1be87fa254" class=""><strong>2. 
Mesopotamia (Sumer → Babylonia → Assyria)</strong></h1></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-8099-a6e7-f14cf9882234" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8052-acb3-dd6a161247b8"><th id="B?yN" class="simple-table-header-color simple-table-header"><strong>Civilization</strong></th><th id="XOgB" class="simple-table-header-color simple-table-header"><strong>Period</strong></th><th id="j|a|" class="simple-table-header-color simple-table-header"><strong>TSS Cycle</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80b8-a4db-c28d51a7bc74"><td id="B?yN" class="">Sumerian City-States</td><td id="XOgB" class="">3500–2350 BCE</td><td id="j|a|" class="">C1–C2</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8088-a180-e1393b014eb9"><td id="B?yN" class="">Akkadian Empire</td><td id="XOgB" class="">2334–2154 BCE</td><td id="j|a|" class="">C2–C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8051-bded-daca896e0bd0"><td id="B?yN" class="">Gutian &amp; city-state period</td><td id="XOgB" class="">2154–2100 BCE</td><td id="j|a|" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8030-8a58-ce90813b281f"><td id="B?yN" class="">Ur III revival</td><td id="XOgB" class="">2100–2000 BCE</td><td id="j|a|" class="">C7</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80e4-97dc-d3b0c66cc62b"><td id="B?yN" class="">Old Babylonian</td><td id="XOgB" class="">2000–1595 BCE</td><td id="j|a|" class="">C2–C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8025-92bb-edc92342da2b"><td id="B?yN" class="">Kassites &amp; 
Assyrians</td><td id="XOgB" class="">1595–911 BCE</td><td id="j|a|" class="">C4–C5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8059-acaf-e04c003444f1"><td id="B?yN" class="">Neo-Assyrian Empire</td><td id="XOgB" class="">911–609 BCE</td><td id="j|a|" class="">C2–C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80aa-9a9b-e2a22afc2fc3"><td id="B?yN" class="">Neo-Babylonian Empire</td><td id="XOgB" class="">626–539 BCE</td><td id="j|a|" class="">C3–C6</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8087-bec1-dfa7e324ae8f"><td id="B?yN" class="">Persian conquest</td><td id="XOgB" class="">539 BCE onward</td><td id="j|a|" class="">C7</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-80a3-9509-e42fc63addce"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-80de-b192-fc63bbfacf52" class=""><strong>3. 
Indus Valley Civilization</strong></h1></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-8018-8132-d12ce95be232" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80b2-a4cb-ca8d882c8582"><th id="xf&gt;G" class="simple-table-header-color simple-table-header"><strong>Period</strong></th><th id=";?eq" class="simple-table-header-color simple-table-header"><strong>TSS Cycle</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8023-a4fd-c56d8d061923"><td id="xf&gt;G" class="">Urban Formation (Harappa/Mohenjo-Daro)</td><td id=";?eq" class="">C1–C2</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80bf-b629-c3837aa62d62"><td id="xf&gt;G" class="">Mature Urban Era</td><td id=";?eq" class="">C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8005-84b7-f9ae66d6720b"><td id="xf&gt;G" class="">Environmental &amp; societal strain</td><td id=";?eq" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80ba-86dd-cd93746cc554"><td id="xf&gt;G" class="">Collapse &amp; dispersal</td><td id=";?eq" class="">C5–C6</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80f2-aefc-d27cca78ed73"><td id="xf&gt;G" class="">South Asian reconfiguration</td><td id=";?eq" class="">C7</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-8076-be41-ce80c0ae5dca"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-800b-adcd-e9a93040947c" class=""><strong>4. 
Ancient China (Xia → Qin → Han → Tang → Song → Ming → Qing)</strong></h1></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b0-883c-d64ced49cc73" class=""><em>Presented as repeated dynastic cycles.</em></p></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-8005-85f6-db022d099a0e" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8027-972e-fa4598bec37d"><th id="uFy`" class="simple-table-header-color simple-table-header"><strong>Dynasty</strong></th><th id="uYSD" class="simple-table-header-color simple-table-header"><strong>Structural Peak</strong></th><th id="KOw\" class="simple-table-header-color simple-table-header"><strong>TSS Cycle Flow</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8012-bee3-c08bdd886cf7"><td id="uFy`" class="">Xia (semi-legendary)</td><td id="uYSD" class="">Early formation</td><td id="KOw\" class="">C1</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-803e-87b2-cff68a8e5b12"><td id="uFy`" class="">Shang</td><td id="uYSD" class="">State formation</td><td id="KOw\" class="">C1–C2</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8071-be74-c929ecd9b9ef"><td id="uFy`" class="">Zhou</td><td id="uYSD" class="">Expansion + overreach</td><td id="KOw\" class="">C2–C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-806b-a0b0-ddf76c44f6f9"><td id="uFy`" class="">Warring States</td><td id="uYSD" class="">Fragmentation</td><td id="KOw\" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8025-b70e-e1b5af6c2151"><td id="uFy`" class="">Qin</td><td id="uYSD" class="">Shock, 
unification</td><td id="KOw\" class="">C5–C7</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8054-adef-f260924e1475"><td id="uFy`" class="">Han</td><td id="uYSD" class="">Imperial peak</td><td id="KOw\" class="">C2–C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80cd-b022-d5d9b4af1ae9"><td id="uFy`" class="">Late Han</td><td id="uYSD" class="">Factional breakdown</td><td id="KOw\" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80d5-8223-d8373ff7f5fa"><td id="uFy`" class="">Three Kingdoms</td><td id="uYSD" class="">Crisis</td><td id="KOw\" class="">C5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8028-8042-e0d7ecab9b03"><td id="uFy`" class="">Jin → Northern/Southern</td><td id="uYSD" class="">Collapse</td><td id="KOw\" class="">C6</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8054-8a08-d98ce480571b"><td id="uFy`" class="">Sui/Tang</td><td id="uYSD" class="">Reset &amp; peak</td><td id="KOw\" class="">C7→C2–C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8065-bbe2-de91ae7eef2f"><td id="uFy`" class="">Five Dynasties</td><td id="uYSD" class="">Fragmentation</td><td id="KOw\" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80a6-87f2-f1c3ce8fd123"><td id="uFy`" class="">Song</td><td id="uYSD" class="">Expansion under constraint</td><td id="KOw\" class="">C2–C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80c9-9892-c4d5565d33ce"><td id="uFy`" class="">Yuan</td><td id="uYSD" class="">Shock/reset (Mongol)</td><td id="KOw\" class="">C5–C7</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8020-89c4-c96c3b26db3b"><td id="uFy`" class="">Ming</td><td id="uYSD" class="">Peak &amp; 
stagnation</td><td id="KOw\" class="">C2–C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-800a-a98a-ca55a60d1d24"><td id="uFy`" class="">Late Ming → Qing</td><td id="uYSD" class="">Internal division</td><td id="KOw\" class="">C4–C5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-809d-b5f0-f4e3a2efd02e"><td id="uFy`" class="">Qing collapse</td><td id="uYSD" class="">1911</td><td id="KOw\" class="">C6</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-80a7-aff8-fe515cae0b69"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-8076-a1b5-e31068cb82fa" class=""><strong>5. 
Persia / Iran (Achaemenid → Sassanid → Islamic Empires)</strong></h1></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-800e-ad53-d6d6d148ee51" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8057-883e-fcbd4a851d50"><th id="p=`?" class="simple-table-header-color simple-table-header"><strong>Period</strong></th><th id="ZTfh" class="simple-table-header-color simple-table-header"><strong>TSS Cycle</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8080-b16f-e685ddcd7bb3"><td id="p=`?" class="">Achaemenid</td><td id="ZTfh" class="">C2–C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80fa-ae3f-f95129d6076d"><td id="p=`?" class="">Conquests by Alexander</td><td id="ZTfh" class="">C5–C6</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8093-b350-c04f7e7919b1"><td id="p=`?" class="">Parthian</td><td id="ZTfh" class="">C7→C2</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80ec-89bc-c828f56ba435"><td id="p=`?" class="">Sassanid</td><td id="ZTfh" class="">C2–C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-803c-9134-e46a4f643780"><td id="p=`?" class="">Arab conquest</td><td id="ZTfh" class="">C5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80d7-af83-ddc844b8712a"><td id="p=`?" class="">Persian Islamic Golden Age</td><td id="ZTfh" class="">C7–C2</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80ec-b56c-d3d5c36a56f7"><td id="p=`?" class="">Mongol invasion</td><td id="ZTfh" class="">C5–C6</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80a6-8702-c5e6c623ed90"><td id="p=`?" class="">Safavid</td><td id="ZTfh" class="">C7–C2</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8009-a0db-f61314f7e607"><td id="p=`?" c
lass="">Qajar weakening</td><td id="ZTfh" class="">C3–C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8012-8e94-c589a83a7c96"><td id="p=`?" class="">Modern Iran formation</td><td id="ZTfh" class="">C7</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-804d-b98d-c3b762a96650"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-8098-8186-e12f9113966b" class=""><strong>6. 
Ancient Greece</strong></h1></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-806e-bce7-ef5715074bcc" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8058-867a-c61a401fa017"><th id="\Z;L" class="simple-table-header-color simple-table-header"><strong>Period</strong></th><th id="KfYm" class="simple-table-header-color simple-table-header"><strong>TSS Cycle</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8098-a6ff-c063c28d54dd"><td id="\Z;L" class="">Mycenaean</td><td id="KfYm" class="">C2–C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8077-b6bf-fe85a1aa9c19"><td id="\Z;L" class="">Collapse</td><td id="KfYm" class="">C6</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8011-a770-f92bf51b5ae5"><td id="\Z;L" class="">Greek Dark Age</td><td id="KfYm" class="">C7 (slow)</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8027-a74b-d82296a921d3"><td id="\Z;L" class="">Classical Greece</td><td id="KfYm" class="">C2–C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8056-9104-d627ef8284b4"><td id="\Z;L" class="">City-state fragmentation</td><td id="KfYm" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-801e-ad66-ebecd8ae5a86"><td id="\Z;L" class="">Macedonian conquest</td><td id="KfYm" class="">C5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8070-b1a5-dd56744309d7"><td id="\Z;L" class="">Hellenistic era</td><td id="KfYm" class="">C3–C6</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80f0-b3e0-d2b0e94620f8"><td id="\Z;L" class="">Roman absorption</td><td id="KfYm" class="">C6–A</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-805f-a98b-e8e373dfa747"/></div><div s
tyle="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-8033-b0d3-eb0491efdbee" class=""><strong>7. 
Roman Civilization (Republic → Empire)</strong></h1></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-807d-8f3c-d27ee288d4e7" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80cc-b0dc-f0aea437f497"><th id="{y}p" class="simple-table-header-color simple-table-header"><strong>Period</strong></th><th id="yh^g" class="simple-table-header-color simple-table-header"><strong>TSS Cycle</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8069-aafa-c4192099acd4"><td id="{y}p" class="">Roman Kingdom</td><td id="yh^g" class="">C1</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8032-b358-f8bb732b74d3"><td id="{y}p" class="">Early/Mid Republic</td><td id="yh^g" class="">C2</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80f7-a8d4-d68f50218885"><td id="{y}p" class="">Late Republic</td><td id="yh^g" class="">C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8012-80a7-f13a58af8154"><td id="{y}p" class="">Civil Wars</td><td id="yh^g" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80a1-b32d-d3e95ada755d"><td id="{y}p" class="">Augustus stabilization</td><td id="yh^g" class="">C7</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80f5-9f7f-c3438ac3084c"><td id="{y}p" class="">High Empire</td><td id="yh^g" class="">C2–C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8065-8a83-e72cef5909cc"><td id="{y}p" class="">Crisis of 3rd century</td><td id="yh^g" class="">C5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8037-b713-f9da55b561e9"><td id="{y}p" class="">Division East/West</td><td id="yh^g" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-805b-9c0e-d3b85d7d1e40"><td id="{y}p" class="">Western f
all</td><td id="yh^g" class="">476 CE</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80a1-ae69-ec6e58808779"><td id="{y}p" class="">Byzantine continuation</td><td id="yh^g" class="">C7→C2</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-806b-9cbe-f8e0d78d35f3"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-8019-8b9c-eb2755d3c2b6" class=""><strong>8. 
Maya Civilization</strong></h1></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-80b3-b286-dc297d66c661" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8057-a518-c47544fff2a9"><th id="y?em" class="simple-table-header-color simple-table-header"><strong>Period</strong></th><th id="ww:|" class="simple-table-header-color simple-table-header"><strong>TSS Cycle</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8008-a8c6-d43e160c6291"><td id="y?em" class="">Preclassic</td><td id="ww:|" class="">C1–C2</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-808b-b478-fa2d5a498c35"><td id="y?em" class="">Classic Peak</td><td id="ww:|" class="">C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8072-8049-d34556e8119c"><td id="y?em" class="">Late Classic wars</td><td id="ww:|" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80e2-b20a-d13696848496"><td id="y?em" class="">Terminal Classic collapses</td><td id="ww:|" class="">C5–C6</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-809d-b439-d87c1715d822"><td id="y?em" class="">Postclassic reorganization</td><td id="ww:|" class="">C7</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-8038-8849-cd660a0c7131"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-80aa-903b-d5e5cd3aba44" class=""><strong>9. 
Inca Civilization</strong></h1></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-80b2-8188-c87f46f059fb" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8083-beb2-e7624c637263"><th id="\puO" class="simple-table-header-color simple-table-header"><strong>Period</strong></th><th id="kdED" class="simple-table-header-color simple-table-header"><strong>TSS Cycle</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8000-94f6-e03accd29896"><td id="\puO" class="">Kingdom of Cusco</td><td id="kdED" class="">C1</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80d4-9852-d7f8c31aa8bf"><td id="\puO" class="">Imperial expansion</td><td id="kdED" class="">C2</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80e6-bc54-df5a60c0492c"><td id="\puO" class="">Rapid consolidation</td><td id="kdED" class="">C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8090-af19-da258ca1e4c9"><td id="\puO" class="">Civil war</td><td id="kdED" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-803c-a242-d4043437ff8a"><td id="\puO" class="">Spanish arrival</td><td id="kdED" class="">C5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8027-9c29-f92ac5707b2b"><td id="\puO" class="">Imperial collapse</td><td id="kdED" class="">C6</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8007-ad1b-e1c7d8c04cd2"><td id="\puO" class="">Colonial reconfiguration</td><td id="kdED" class="">C7</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-8099-b2f2-e8282fc13fbe"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-80f2-9011-e92a5c0be474" class=""><strong>10. 
Aztec Civilization</strong></h1></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-80ae-9f32-fa6a2de03a8f" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-808d-add7-ff902024e474"><th id="b~pi" class="simple-table-header-color simple-table-header"><strong>Period</strong></th><th id="ea@W" class="simple-table-header-color simple-table-header"><strong>TSS Cycle</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80f7-b503-ecb0c074ea87"><td id="b~pi" class="">Mexica arrival</td><td id="ea@W" class="">C1</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-802a-8a08-e1400c27bc9d"><td id="b~pi" class="">Triple Alliance formation</td><td id="ea@W" class="">C2</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8075-ad98-e66ec19e1b2c"><td id="b~pi" class="">Imperial tributary system</td><td id="ea@W" class="">C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-803d-97b7-c1fd5572b55a"><td id="b~pi" class="">Provincial strain</td><td id="ea@W" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-803e-a311-c9da96d0c67c"><td id="b~pi" class="">Conquistador invasion</td><td id="ea@W" class="">C5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80ab-bd23-d200b6be1ec2"><td id="b~pi" class="">Collapse</td><td id="ea@W" class="">C6</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80ef-8916-e7e3c10c7f1a"><td id="b~pi" class="">New colonial order</td><td id="ea@W" class="">C7</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-8045-9449-f5f348b57d24"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-80db-a8b2-c4a61d5381b6" class=""><strong>11. 
Europe After Rome</strong></h1></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-806b-86b5-ca90c5acb49e" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80f0-88ce-e30f634d26f3"><th id="XYts" class="simple-table-header-color simple-table-header"><strong>Period</strong></th><th id="wPVF" class="simple-table-header-color simple-table-header"><strong>TSS Cycle</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80a6-9986-dbe092fde9d4"><td id="XYts" class="">Post-Roman fragmentation</td><td id="wPVF" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-809a-9c4f-f90893308a8d"><td id="XYts" class="">Medieval feudal formation</td><td id="wPVF" class="">C7–C2</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8019-a5ad-c70a61f47d1e"><td id="XYts" class="">High Middle Ages</td><td id="wPVF" class="">C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80f5-9a77-f6aaa8beca02"><td id="XYts" class="">Crises (plague, war)</td><td id="wPVF" class="">C5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80c7-9679-e37af1bf46b2"><td id="XYts" class="">Feudal decline</td><td id="wPVF" class="">C6</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-802b-938d-e223d82ca5a9"><td id="XYts" class="">Renaissance/early modern reset</td><td id="wPVF" class="">C7–C2</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8054-b5f6-e3034dd8d7a0"><td id="XYts" class="">Industrial era</td><td id="wPVF" class="">C3</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-80dd-af18-f456ed0327e2"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-8068-b566-e0ce7d180be1" class=""><strong>12. 
Islamic Civilization</strong></h1></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-80d6-9de8-d3c060729561" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80a8-b01a-f32c0254991d"><th id="tPop" class="simple-table-header-color simple-table-header"><strong>Period</strong></th><th id="x&gt;|x" class="simple-table-header-color simple-table-header"><strong>TSS Cycle</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-806a-b4aa-c541d54591b1"><td id="tPop" class="">Muhammad/early Caliphate</td><td id="x&gt;|x" class="">C1–C2</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80e2-89e1-e04856899d7b"><td id="tPop" class="">Umayyad expansion</td><td id="x&gt;|x" class="">C2–C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8067-aa90-db98215de85b"><td id="tPop" class="">Abbasid fragmentation</td><td id="x&gt;|x" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8040-85ce-c2d2fe73ba49"><td id="tPop" class="">Mongol shock</td><td id="x&gt;|x" class="">C5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-800b-8bb8-f79ad2836dea"><td id="tPop" class="">Regional Islamic states</td><td id="x&gt;|x" class="">C7</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8047-9847-e5237eeb0656"><td id="tPop" class="">Ottoman rise</td><td id="x&gt;|x" class="">C2–C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-801e-b4e0-dcf46c466fe5"><td id="tPop" class="">Ottoman stagnation</td><td id="x&gt;|x" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-807c-8f14-c6053f444897"><td id="tPop" class="">WWI shock</td><td id="x&gt;|x" class="">C5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80dc-94bd-d90604ade9ad"><td i
d="tPop" class="">Collapse</td><td id="x&gt;|x" class="">C6</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80f8-8348-e935de182f0f"><td id="tPop" class="">Middle East modern states</td><td id="x&gt;|x" class="">C7</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-800f-b7e0-c69e594a9df9"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-80fb-a34f-c4c6159f7ab8" class=""><strong>13. 
Indian Subcontinent</strong></h1></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-80eb-b52e-c1f02d1ba31c" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-809e-802f-f82208ec388a"><th id="Lvfr" class="simple-table-header-color simple-table-header"><strong>Period</strong></th><th id="sHR=" class="simple-table-header-color simple-table-header"><strong>TSS Cycle</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80e9-8f31-e636b422867b"><td id="Lvfr" class="">Vedic era</td><td id="sHR=" class="">C1–C2</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-805a-b1b2-ed337eebe41e"><td id="Lvfr" class="">Maurya</td><td id="sHR=" class="">C2–C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-805f-89bc-c148b138c3ff"><td id="Lvfr" class="">Fragmentation</td><td id="sHR=" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-808e-aa8a-d1c1601a8260"><td id="Lvfr" class="">Gupta</td><td id="sHR=" class="">C2–C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8015-847e-c8949f21dc2f"><td id="Lvfr" class="">Post-Gupta</td><td id="sHR=" class="">C4–C5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-807b-ae87-ee75508e9430"><td id="Lvfr" class="">Delhi Sultanate</td><td id="sHR=" class="">C7</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80ae-ad7f-ec0c1b31c505"><td id="Lvfr" class="">Mughal peak</td><td id="sHR=" class="">C2–C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80ca-9437-daad38d8b94d"><td id="Lvfr" class="">Mughal decline</td><td id="sHR=" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80a7-ac29-d874a6233328"><td id="Lvfr" class="">British shock</td><td id="sHR=" c
lass="">C5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80f4-84d7-c16abc5b070b"><td id="Lvfr" class="">Collapse of old order</td><td id="sHR=" class="">C6</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80b1-9fa1-e82b4a40c3b2"><td id="Lvfr" class="">Modern India/Pakistan</td><td id="sHR=" class="">C7</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-80c4-88bc-e1432a9a7ad5"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-807f-8b4d-c912a27cebac" class=""><strong>14. 
Japan (Yamato → Tokugawa → Meiji → Modern)</strong></h1></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-80c2-897e-f5e0199dd320" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80f6-8986-f4f246b63bec"><th id="j&gt;B:" class="simple-table-header-color simple-table-header"><strong>Period</strong></th><th id="{yM:" class="simple-table-header-color simple-table-header"><strong>TSS Cycle</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8058-8cc0-e529d943ba90"><td id="j&gt;B:" class="">Yamato formation</td><td id="{yM:" class="">C1</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-807f-9a38-de789a5d932a"><td id="j&gt;B:" class="">Classical Nara/Heian</td><td id="{yM:" class="">C2</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80cb-bfa0-d45a06f4c918"><td id="j&gt;B:" class="">Feudal fragmentation</td><td id="{yM:" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80bb-b2aa-d9f52e480502"><td id="j&gt;B:" class="">Sengoku crisis</td><td id="{yM:" class="">C5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80a6-a56c-cbc54e9bbe50"><td id="j&gt;B:" class="">Tokugawa stabilization</td><td id="{yM:" class="">C7</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80fe-9572-cee75b53493f"><td id="j&gt;B:" class="">Isolation and stagnation</td><td id="{yM:" class="">C3→Sg</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80d6-979e-fdb4022c480d"><td id="j&gt;B:" class="">Meiji shock/reset</td><td id="{yM:" class="">C5–C7</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-805e-acec-fc38bf597ad8"><td id="j&gt;B:" class="">Modern expansion</td><td id="{yM:" class="">C2</td></tr></div><div style="display:contents" dir="ltr"><tr i
d="2b1c5e6f-95bd-8094-9ccd-fc99cf487c99"><td id="j&gt;B:" class="">WWII shock</td><td id="{yM:" class="">C5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8016-9206-d8a8301740e0"><td id="j&gt;B:" class="">Postwar reset</td><td id="{yM:" class="">C7</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8081-90f1-ecbff8d479fb"><td id="j&gt;B:" class="">Modern Japan</td><td id="{yM:" class="">C2–C3</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-8047-9419-e64b77d97e38"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-80a3-882f-cbe08b14ca3e" class=""><strong>15. 
Chinese Civilizational Core (Modern 20th–21st Century)</strong></h1></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-808f-9ff6-ea501c1ffd38" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8012-b429-e4681e197046"><th id="H=hD" class="simple-table-header-color simple-table-header"><strong>Period</strong></th><th id="xC];" class="simple-table-header-color simple-table-header"><strong>TSS Cycle</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-801a-abb3-dbb3ab455783"><td id="H=hD" class="">Late Qing overload</td><td id="xC];" class="">C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8052-8bf8-e3c33b2d9fd3"><td id="H=hD" class="">Collapse 1911</td><td id="xC];" class="">C6</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80c6-9c93-cfcd7659b467"><td id="H=hD" class="">Warlord fragmentation</td><td id="xC];" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-801c-81f2-c6ea89da3c2a"><td id="H=hD" class="">Republican era crisis</td><td id="xC];" class="">C5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8017-88b0-f6bbfe324716"><td id="H=hD" class="">1949 reset</td><td id="xC];" class="">C7</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8092-8f9c-e26b0a9e7724"><td id="H=hD" class="">Early PRC consolidation</td><td id="xC];" class="">C2</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80da-b8cc-c135fa649440"><td id="H=hD" class="">Reform era expansion</td><td id="xC];" class="">C2–C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8010-b0aa-e52c8da0fb8c"><td id="H=hD" class="">21st century strain</td><td id="xC];" class="">C3–C4 (structural)</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr i
d="2b1c5e6f-95bd-80be-98e3-eafb2d3c0f9b"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-8003-8ac1-c6a8562addd2" class=""><strong>16. 
United States</strong></h1></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-80bf-8992-f7b09a8ed266" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8026-987f-f5258f63e7f6"><th id="aZxZ" class="simple-table-header-color simple-table-header"><strong>Period</strong></th><th id="MhP&lt;" class="simple-table-header-color simple-table-header"><strong>TSS Cycle</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8060-8388-da7891f94e50"><td id="aZxZ" class="">Founding</td><td id="MhP&lt;" class="">C1</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-803d-8ffb-e87662b3c970"><td id="aZxZ" class="">Early expansion</td><td id="MhP&lt;" class="">C2</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-809c-9135-e4dfb6a31b1d"><td id="aZxZ" class="">Industrial/WWII peak</td><td id="MhP&lt;" class="">C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8042-b28f-f7a7c19cf93c"><td id="aZxZ" class="">Cold War strain</td><td id="MhP&lt;" class="">C3–C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8014-9668-e05394bad53f"><td id="aZxZ" class="">Post–Cold War high</td><td id="MhP&lt;" class="">C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8086-b768-f61207168a3d"><td id="aZxZ" class="">21st century fragmentation</td><td id="MhP&lt;" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-809b-8b94-e04ab3e668ec"><td id="aZxZ" class="">Ongoing systemic shocks</td><td id="MhP&lt;" class="">C5 (in progress)</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-80fe-ad96-cc6997b03c25"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-8052-a89a-faf9c72fc24f" class=""><strong>17. 
Middle East (Modern Era)</strong></h1></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-804c-981b-f9264595b984" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-805e-bbde-d41c7a8c5701"><th id="^d==" class="simple-table-header-color simple-table-header"><strong>Period</strong></th><th id=";Sga" class="simple-table-header-color simple-table-header"><strong>TSS Cycle</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8053-81ca-c2cfded0947d"><td id="^d==" class="">Colonial carve-up</td><td id=";Sga" class="">C5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8001-be1e-ffca6ac75553"><td id="^d==" class="">Postcolonial state formation</td><td id=";Sga" class="">C7</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80bc-8f8c-e64936b066ca"><td id="^d==" class="">Oil expansion</td><td id=";Sga" class="">C2–C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8022-99a0-ffb8c4f7ec6d"><td id="^d==" class="">Sectarian/ethnic fragmentation</td><td id=";Sga" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8038-9c3f-fc02837c8857"><td id="^d==" class="">Arab Spring shocks</td><td id=";Sga" class="">C5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80df-8962-dddae9edaad6"><td id="^d==" class="">State failures</td><td id=";Sga" class="">C6</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80eb-a0d0-ce9ad80c3988"><td id="^d==" class="">Partial resets (Gulf states)</td><td id=";Sga" class="">C7</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-80f8-a613-e15332141860"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-8056-8e87-e8795025ea26" class=""><strong>18. 
Africa (Pre-colonial → Colonial → Modern)</strong></h1></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-80f5-8301-d0b6bd1b9706" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8040-955d-cc8b2ae6666a"><th id="ZL?k" class="simple-table-header-color simple-table-header"><strong>Period</strong></th><th id="F{Fp" class="simple-table-header-color simple-table-header"><strong>TSS Cycle</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-804d-8fb8-d88c60602fc8"><td id="ZL?k" class="">Indigenous kingdoms</td><td id="F{Fp" class="">C1–C2</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8064-8e34-d945cd57b3f4"><td id="ZL?k" class="">Inter-kingdom wars</td><td id="F{Fp" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8009-a70e-cea2f12a4125"><td id="ZL?k" class="">European colonization</td><td id="F{Fp" class="">C5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8091-847d-ea2358b58f6b"><td id="ZL?k" class="">Traditional order collapse</td><td id="F{Fp" class="">C6</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8042-b3fc-ec1e3c487a39"><td id="ZL?k" class="">Independence era</td><td id="F{Fp" class="">C7</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8025-a4bb-f97cbc4d4bd4"><td id="ZL?k" class="">Modern expansion + fragmentation</td><td id="F{Fp" class="">C2–C4</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-80be-949b-e95a79b07b87"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-8066-baff-c7cf19e3ac15" class=""><strong>19. 
Western Europe (Modern Era)</strong></h1></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-8028-8ad2-e64ce1ba14ef" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-802e-899b-c2986ec8152c"><th id="oros" class="simple-table-header-color simple-table-header"><strong>Period</strong></th><th id="zncg" class="simple-table-header-color simple-table-header"><strong>TSS Cycle</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8066-91a7-e5d6af02f9bc"><td id="oros" class="">Early modern expansion</td><td id="zncg" class="">C2</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-806f-95ce-f2221076bd48"><td id="oros" class="">Imperial overreach</td><td id="zncg" class="">C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8026-878d-dfa1ce3a2ded"><td id="oros" class="">WWI/WWII shocks</td><td id="zncg" class="">C5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8000-8b7e-d26fba922f67"><td id="oros" class="">Collapse of empires</td><td id="zncg" class="">C6</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-808b-a3c1-dc434596d9e1"><td id="oros" class="">EU formation</td><td id="zncg" class="">C7</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8078-8400-fb019bf54324"><td id="oros" class="">Modern fragmentation</td><td id="zncg" class="">C4</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-804c-9326-dd8baaf22cd4"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-80e1-94b9-d04fbdb3fbae" class=""><strong>20. 
Global Civilization (21st Century)</strong></h1></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80fc-8e4c-cb0664b23b82" class="">This is the first time the world behaves as a single interdependent system.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b7-92df-eb9c1459fc1b" class="">Structure-level mapping:</p></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-805d-aba0-d8147b4f0b7e" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80bb-9e53-d7d9bbff481b"><th id="vKe:" class="simple-table-header-color simple-table-header"><strong>Global Condition</strong></th><th id="RDEQ" class="simple-table-header-color simple-table-header"><strong>TSS Cycle</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-805e-b829-c7b448b3ebdf"><td id="vKe:" class="">Hyper-globalization</td><td id="RDEQ" class="">C2–C3</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-806a-9a72-ee506dad6f34"><td id="vKe:" class="">Fragmentation &amp; 
polarization</td><td id="RDEQ" class="">C4</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8065-b44f-e9eef5712854"><td id="vKe:" class="">Climate/energy/economic shocks</td><td id="RDEQ" class="">C5</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8052-951d-e05e11150fd9"><td id="vKe:" class="">Pending structural transition</td><td id="RDEQ" class="">TBD (C6 or C7)</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-8071-a009-d812ed4e1a28"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-80fa-89d7-da4fb95f7cff" class=""><strong>Summary of the Appendix</strong></h1></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-807d-be83-ff32307c7a2b" class="">Across 5,000 years and every major civilization, the same structural sequence repeats:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b8-b3e8-ee18edcd6475" class="">Emergence → Expansion → Overreach → Fragmentation → Shock → Collapse → Reset</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80bb-ad4a-fb7890e96b41" class="">No civilization breaks the pattern.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8064-96f5-fd6a90255640" class="">Differences appear in duration, speed, 
and expression—but <strong>the structural mechanics remain constant</strong>.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-802f-bff3-eecd35bfe16e" class="">This appendix confirms that the TSS seven-cycle model is:</p></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-8076-b4af-fad54ed01bab" class="bulleted-list"><li style="list-style-type:disc">cross-cultural</li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-8060-9a1a-f1cd5226c372" class="bulleted-list"><li style="list-style-type:disc">cross-temporal</li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-807e-9141-d921ba63fd29" class="bulleted-list"><li style="list-style-type:disc">cross-geographical</li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-80ab-9766-cd37afd9634b" class="bulleted-list"><li style="list-style-type:disc">universal at civilizational scale</li></ul></div><div style="display:contents" dir="auto"><ul id="2b1c5e6f-95bd-8083-bf67-f12d0331c20e" class="bulleted-list"><li style="list-style-type:disc">predictive at structural scale</li></ul></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-804d-8d76-c6f9c5ad9bdf" class="">This is the <strong>empirical backbone</strong> of CCI and the <strong>historical validation layer</strong> of TSS and TPE.</p></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-80b8-b4dc-c6c86cc09472"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-8077-b8bc-e4ee5645b9e3" class=""><strong>Civilizational Scoring Protocol (CSP)</strong></h1></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8068-a5d0-fd529bb1debd" class=""><em>Official Manual for Quantifying Civilizational Trajectories Under TSS × CCI × PSI</em></p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b9-a95d-d201df2cf8e2" class="">The Civilizational Scoring Protocol (CSP) provides a standardized method to e
valuate the structural health, stability, and trajectory of any civilization. Its purpose is to transform qualitative civilizational analysis into a <strong>repeatable, comparable, cross-era measurement system</strong> grounded in the universal architecture of the Trang System™ and Cross-Civilizational Intelligence™.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8051-983c-cfef1e288183" class="">CSP does not measure culture, morality, greatness, or subjective value. It measures structural forces.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a3-86dd-c16bf4684b74" class="">It scores civilizations using <strong>ten dimensions</strong>, categorized under the four universal variables (Ω, H, F, S), the seven cycles (C1–C7), and planetary context (PSI).</p></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-80e4-8976-dc8bc4443c30"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-8036-bc1f-c189e4e69835" class=""><strong>1. 
The Structure of the Civilizational Scoring Protocol</strong></h1></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ee-bb46-cf89bcc83247" class="">CSP consists of <strong>10 scoring axes</strong>:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2b1c5e6f-95bd-8043-9972-df6884227ad1" class="numbered-list" start="1"><li>Ω–Overload Score</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b1c5e6f-95bd-80cb-9f7f-faff50354a39" class="numbered-list" start="2"><li>H–Cohesion Score</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b1c5e6f-95bd-804a-8a7f-f0e26fa98418" class="numbered-list" start="3"><li>F–Fragmentation Score</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b1c5e6f-95bd-8018-ab25-fd531880394e" class="numbered-list" start="4"><li>S–Shock Exposure Score</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b1c5e6f-95bd-809e-9a3b-f581e9549603" class="numbered-list" start="5"><li>Institutional Quality Score</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b1c5e6f-95bd-8005-8b22-f38aed118555" class="numbered-list" start="6"><li>Resource Stability Score (PSI Pillar 1)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b1c5e6f-95bd-8020-952d-d534102b2273" class="numbered-list" start="7"><li>Climate Vulnerability Score (PSI Pillar 2)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b1c5e6f-95bd-8035-8a8c-fc057ac012f9" class="numbered-list" start="8"><li>Biological Resilience Score (PSI Pillar 3)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b1c5e6f-95bd-80be-a6dd-e472b5df428e" class="numbered-list" start="9"><li>Interdependence Fragility Score (PSI Pillar 4)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2b1c5e6f-95bd-805b-a458-d476c9610c99" class="numbered-list numbered-list-digits-2" start="10"><li>Cycle Position 
core (C1–C7 location)</li></ol></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-803d-839e-c8f202c6b0aa" class="">A civilization’s <strong>structural effectiveness score (e)</strong> is then derived from the equation:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-809c-9bff-f3fe442af43f" class="">e = i²</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80c0-80b0-cfd6a119e251" class="">where i is a composite index of axes 1–9.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80fe-ad06-e1be93142a66" class="">This produces a <strong>universal rating</strong> of civilizational stability and trajectory.</p></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-80af-b694-f2f83bdf0d93"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-80ec-935d-c63efa5d70ac" class=""><strong>2. 
The Scoring Scale (0–5)</strong></h1></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80dd-b7f6-d212ef010331" class="">Each axis is scored on a 0–5 scale:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-806e-8e32-f4c3b006a67c" class="">0 = Critical</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8005-bc17-fbac512a2ee3" class="">1 = Severe</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80f3-a5ff-dc64fc806fc0" class="">2 = Weak</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ac-b1bc-d248ea10a4b9" class="">3 = Moderate</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80df-b433-f16c84f72ca3" class="">4 = Strong</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-801d-a944-e59928061c10" class="">5 = Robust</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8056-b907-fb3b055e2383" class="">This range captures <strong>structural strength</strong>, not moral or cultural judgment.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ad-a172-cb479170bf6e" class="">Example interpretation:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-803f-a498-fe7d479ba17f" class="">Ω–Overload Score = 1 means severe overload;</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8034-95ad-ce9b8954506e" class="">H–Cohesion Score = 5 means extremely strong cohesion.</p></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-809b-bef8-f4319e6853df"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-80ce-95ac-e0fe25c2bb2e" class=""><strong>3. 
Axis Definitions and Scoring Criteria</strong></h1></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8098-96eb-ff69c4def8af" class="">Below are the <strong>10 axes</strong>, each with scoring rules.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80be-991b-d8cee463e584" class=""><strong>Axis 1: Ω – Overload Score</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-805d-a1c1-fac3629862c8" class="">Measures whether the civilization’s responsibilities exceed its capacity.</p></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-8066-a188-c12ec74b5fcd" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80b2-bed6-f07051c2b014"><th id="Ptzz" class="simple-table-header-color simple-table-header"><strong>Score</strong></th><th id="MqHr" class="simple-table-header-color simple-table-header"><strong>Criteria</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8035-9567-cebf1f5e9d56"><td id="Ptzz" class="">5</td><td id="MqHr" class="">Capacity exceeds demands; long-term sustainability</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80f4-93d6-cc034bbeacf9"><td id="Ptzz" class="">4</td><td id="MqHr" class="">Balanced load; manageable strain</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80c9-9aa7-d1c64f43f88c"><td id="Ptzz" class="">3</td><td id="MqHr" class="">Noticeable strain; early signs of overreach</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80f9-9963-dd752d240179"><td id="Ptzz" class="">2</td><td id="MqHr" class="">High overload in key sectors</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-809d-9afa-f77a72070f79"><td id="Ptzz" class="">1</td><td id="MqHr" class="">System-wide overload; 
chronic strain</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8071-85e2-d66fe6a5fec4"><td id="Ptzz" class="">0</td><td id="MqHr" class="">Collapse-level overload; 
system failure</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80fb-9482-f91b887e42fe" class=""><strong>Axis 2: H – Cohesion Score</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8002-a897-f52ac13d060f" class="">Measures unity, legitimacy, and identity coherence.</p></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-80cb-b6fa-c8fc99584036" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80aa-a370-db988d9e10c2"><th id="SHh\" class="simple-table-header-color simple-table-header"><strong>Score</strong></th><th id="l|AV" class="simple-table-header-color simple-table-header"><strong>Criteria</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8038-89b9-f3286d06d89f"><td id="SHh\" class="">5</td><td id="l|AV" class="">High trust, unified identity, minimal conflict</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-804f-84b0-c7a3a47cf073"><td id="SHh\" class="">4</td><td id="l|AV" class="">Strong institutions, manageable divides</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8081-a31a-d0dcc2407d46"><td id="SHh\" class="">3</td><td id="l|AV" class="">Visible polarization but stable</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-801c-8ae0-da4e4f83bd71"><td id="SHh\" class="">2</td><td id="l|AV" class="">Low trust, rising conflict</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-805f-8870-ce461c06a424"><td id="SHh\" class="">1</td><td id="l|AV" class="">Deep polarization, 
institutional delegitimization</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80db-913f-d11f5e6cc064"><td id="SHh\" class="">0</td><td id="l|AV" class="">Near-total social breakdown</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80d6-837e-c4e061143154" class=""><strong>Axis 3: F – Fragmentation Score</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-805a-8598-d14d8473bd5c" class="">Measures the degree of internal division.</p></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-80c3-a326-c5ceddb03f42" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8052-b367-ef78463f5394"><th id="]aMk" class="simple-table-header-color simple-table-header"><strong>Score</strong></th><th id="H@{=" class="simple-table-header-color simple-table-header"><strong>Criteria</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-809d-afb6-cdc380667004"><td id="]aMk" class="">5</td><td id="H@{=" class="">Unified power structure</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-802e-81eb-e8dc08eb0f89"><td id="]aMk" class="">4</td><td id="H@{=" class="">Minor factions</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8079-9e3a-c07324bd2281"><td id="]aMk" class="">3</td><td id="H@{=" class="">Moderate factionalism</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-808f-a307-dfc4267164fe"><td id="]aMk" class="">2</td><td id="H@{=" class="">Strong factional divides</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8034-b4cd-ce2db5e1a943"><td id="]aMk" class="">1</td><td id="H@{=" class="">Multiple competing authorities</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80ba-bbbc-e348e90d102b"><td id="]aMk" c
lass="">0</td><td id="H@{=" class="">Parallel governments / open fragmentation</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8016-b5e0-c75230fc1ee6" class=""><strong>Axis 4: S – Shock Exposure Score</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-809b-9430-c35670270170" class="">Measures vulnerability to disruptions.</p></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-804f-b9b1-c81278e3c66a" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-802a-b447-cd9bdefe363a"><th id="dQIZ" class="simple-table-header-color simple-table-header"><strong>Score</strong></th><th id="oA]L" class="simple-table-header-color simple-table-header"><strong>Criteria</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80dc-a8ba-cd1495997e75"><td id="dQIZ" class="">5</td><td id="oA]L" class="">Strong buffers, low exposure</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8011-ad64-c4d2ed076e7c"><td id="dQIZ" class="">4</td><td id="oA]L" class="">Well-managed risk</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8011-98d4-c2e95a439325"><td id="dQIZ" class="">3</td><td id="oA]L" class="">Periodic disruptions</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80a1-8ce0-db54472bd188"><td id="dQIZ" class="">2</td><td id="oA]L" class="">High risk, 
limited readiness</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8066-8e66-c63602b9df90"><td id="dQIZ" class="">1</td><td id="oA]L" class="">Recurring shocks</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80cc-b408-eecef2c9d085"><td id="dQIZ" class="">0</td><td id="oA]L" class="">Shocks overwhelming system capacity</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-801d-a4b7-c158301c7a89" class=""><strong>Axis 5: Institutional Quality Score</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a8-8ead-e59fbae0835f" class="">Measures the strength of core civilizational institutions.</p></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-8088-9bdc-e2e89ffec47a" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8050-8877-d48aa0429369"><th id="v;dT" class="simple-table-header-color simple-table-header"><strong>Score</strong></th><th id="OCEo" class="simple-table-header-color simple-table-header"><strong>Criteria</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8019-9142-e03ac72376bd"><td id="v;dT" class="">5</td><td id="OCEo" class="">Predictable, fair, adaptive institutions</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80e7-89b1-d610e0532042"><td id="v;dT" class="">4</td><td id="OCEo" class="">Generally stable</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-809c-95ce-db879dd5def4"><td id="v;dT" class="">3</td><td id="OCEo" class="">Some institutional drag</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80d3-977b-d8d0b955f005"><td id="v;dT" class="">2</td><td id="OCEo" class="">Corruption, 
inefficiency common</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8061-80df-ec5663593880"><td id="v;dT" class="">1</td><td id="OCEo" class="">Institutional decay</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8003-bbbe-fe3ade79366b"><td id="v;dT" class="">0</td><td id="OCEo" class="">Institutional collapse</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8070-a463-c30afba00b61" class=""><strong>Axis 6: Resource Stability Score (PSI Pillar 1)</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8013-95c6-e43ccc3af57c" class="">Measures water, soil, food, minerals, 
and energy stability.</p></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-8099-9c39-d590b0c1ad8a" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8064-86c1-fceed829bfd3"><th id="cX&gt;E" class="simple-table-header-color simple-table-header"><strong>Score</strong></th><th id="arCo" class="simple-table-header-color simple-table-header"><strong>Criteria</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80e5-a716-e1a571a9a613"><td id="cX&gt;E" class="">5</td><td id="arCo" class="">Highly stable resources</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80b8-9a4a-e7aed5b10709"><td id="cX&gt;E" class="">4</td><td id="arCo" class="">Manageable fluctuations</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80de-a29a-f759e9f31f19"><td id="cX&gt;E" class="">3</td><td id="arCo" class="">Emerging scarcity</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8033-9de4-e465ce02dddb"><td id="cX&gt;E" class="">2</td><td id="arCo" class="">Chronic scarcity</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80dd-86ae-ea19cdba596f"><td id="cX&gt;E" class="">1</td><td id="arCo" class="">Structural shortages</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-803e-9687-f11bb892616f"><td id="cX&gt;E" class="">0</td><td id="arCo" class="">Collapse-level scarcity</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8014-9c2e-ff54d3d253c9" class=""><strong>Axis 7: Climate Vulnerability Score (PSI Pillar 2)</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-805c-be33-e86ea9dfead4" class="">Measures susceptibility to climate stress.</p></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-8033-8e5d-ff7555c02dac" c
lass="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-800a-b854-d785835fdd48"><th id="bqDo" class="simple-table-header-color simple-table-header"><strong>Score</strong></th><th id="a\xg" class="simple-table-header-color simple-table-header"><strong>Criteria</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8073-9144-f2f9fa429399"><td id="bqDo" class="">5</td><td id="a\xg" class="">Highly resilient</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8038-ac72-c85c289cb669"><td id="bqDo" class="">4</td><td id="a\xg" class="">Manageable climate impacts</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-800b-99d1-f2991729a8cb"><td id="bqDo" class="">3</td><td id="a\xg" class="">Regular disruptions</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8067-ace8-dade4dfc63ae"><td id="bqDo" class="">2</td><td id="a\xg" class="">Severe regional risks</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-805d-a2b6-c2e3567933f7"><td id="bqDo" class="">1</td><td id="a\xg" class="">Extreme vulnerability</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-805c-a568-cb90e9f1088d"><td id="bqDo" class="">0</td><td id="a\xg" class="">Climate-induced destabilization</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-808b-82ea-d738160db3c3" class=""><strong>Axis 8: Biological Resilience Score (PSI Pillar 3)</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80c6-afec-e34a120209d5" class="">Measures population health, disease risk, 
and biosphere stability.</p></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-807d-b362-d486a6eacdfb" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8004-8118-dd319a5bd16f"><th id=":re?" class="simple-table-header-color simple-table-header"><strong>Score</strong></th><th id="e~Xd" class="simple-table-header-color simple-table-header"><strong>Criteria</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8033-aad0-e578e560f925"><td id=":re?" class="">5</td><td id="e~Xd" class="">Strong biological resilience</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80af-afc5-f45e3382c943"><td id=":re?" class="">4</td><td id="e~Xd" class="">Good health and biosphere conditions</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80df-906d-c2103a00c040"><td id=":re?" class="">3</td><td id="e~Xd" class="">Noticeable vulnerabilities</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80a9-843f-cf1acd992e8c"><td id=":re?" class="">2</td><td id="e~Xd" class="">High disease exposure</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8052-bca5-fd199ddf423a"><td id=":re?" class="">1</td><td id="e~Xd" class="">Structural public health risks</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80a0-a996-e3b19d16a19c"><td id=":re?" class="">0</td><td id="e~Xd" class="">Serial biological shocks</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-801f-b631-dc3d3ffdf916" class=""><strong>Axis 9: Interdependence Fragility Score (PSI Pillar 4)</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80d3-952d-d323a8d4a95e" class="">Measures global dependencies and vulnerability to cascades.</p></div><div style="display:contents" dir="ltr"><table i
d="2b1c5e6f-95bd-804e-b270-f9c45a08f852" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80fd-b0eb-d408745bac57"><th id="DJdg" class="simple-table-header-color simple-table-header"><strong>Score</strong></th><th id="iMys" class="simple-table-header-color simple-table-header"><strong>Criteria</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80df-b7bc-edd90ce45503"><td id="DJdg" class="">5</td><td id="iMys" class="">Independent + robust networks</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80af-8335-d50e4d86c1b2"><td id="DJdg" class="">4</td><td id="iMys" class="">Healthy interdependence</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-808b-8d50-d3bf74e571a5"><td id="DJdg" class="">3</td><td id="iMys" class="">Moderate systemic exposure</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80a5-a56a-c66915eda7c1"><td id="DJdg" class="">2</td><td id="iMys" class="">Dependence on fragile networks</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-804a-8983-e0073a65d8ce"><td id="DJdg" class="">1</td><td id="iMys" class="">High exposure to global cascades</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-804f-8181-d426cc7d501b"><td id="DJdg" class="">0</td><td id="iMys" class="">Full fragility; 
cascades propagate instantly</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80ac-a46e-e49bcfde1ad0" class=""><strong>Axis 10: Cycle Position Score (C1–C7)</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-800a-9cca-e1956e3c9324" class="">Assigns a value 1–7 representing the civilizational stage.</p></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-8063-b06e-d8a20d06e457" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80d2-a6db-da6a817252f7"><th id="frOa" class="simple-table-header-color simple-table-header"><strong>Cycle</strong></th><th id="TlN&gt;" class="simple-table-header-color simple-table-header"><strong>Score</strong></th><th id=":?YO" class="simple-table-header-color simple-table-header"><strong>Description</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8002-a749-d1dc64b673ec"><td id="frOa" class="">C1</td><td id="TlN&gt;" class="">1</td><td id=":?YO" class="">Emergence</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8038-94fc-fec0178c5679"><td id="frOa" class="">C2</td><td id="TlN&gt;" class="">2</td><td id=":?YO" class="">Expansion</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80eb-8f98-f461c7eddcd8"><td id="frOa" class="">C3</td><td id="TlN&gt;" class="">3</td><td id=":?YO" class="">Peak &amp; 
Overreach</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-804d-9069-eb2fcd558210"><td id="frOa" class="">C4</td><td id="TlN&gt;" class="">4</td><td id=":?YO" class="">Fragmentation</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-808b-8ddf-f465ec9f1a95"><td id="frOa" class="">C5</td><td id="TlN&gt;" class="">5</td><td id=":?YO" class="">Crisis–Shock</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80cf-909a-f0e6894a7276"><td id="frOa" class="">C6</td><td id="TlN&gt;" class="">6</td><td id=":?YO" class="">Collapse</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80d2-824f-cd0b637b8846"><td id="frOa" class="">C7</td><td id="TlN&gt;" class="">7</td><td id=":?YO" class="">Reset</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-806a-b60f-ffe61b641391"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-8064-94e7-d4e69898f2b5" class=""><strong>4. 
Composite Index (Internal Alignment Index, i)</strong></h1></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8030-bf7a-eeb7087060c6" class="">To compute i:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ff-9cd2-cb1ae07d193c" class="">Take the <strong>average of axes 1–9</strong> (excluding cycle position).</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8029-a23c-ea0ac6b59dbc" class="">Normalize to 0–1 range.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-807c-9030-d3f17246095f" class="">Example:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-808e-9ea5-d2dfdab2d31d" class="">If a civilization scores 30 out of a maximum of 45 → i ≈ 0.67</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b3-9d6b-c93ffb6c7bd2" class="">This becomes the structural alignment measure.</p></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-8073-97cf-c90bdb8f32ec"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-80bd-b176-cf9bcbefe569" class=""><strong>5. 
Effectiveness Score (e = i²)</strong></h1></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8067-9a97-dfb2fc0a3897" class="">Apply the canonical equation:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-801c-b615-f51053e89eca" class="">e = i²</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-807b-92d4-d36f454b5565" class="">This produces the <strong>Civilizational Effectiveness Index (CEI)</strong> indicating how effectively a civilization operates under current structural load.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8070-86a9-de74c9ae6c3f" class="">Example:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80d1-b22c-ea0d91eb2284" class="">If i = 0.67 → e = 0.45</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80dd-b514-c28060424ef6" class="">Meaning:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8054-953c-ed74b4b6a5df" class="">45% functional effectiveness relative to structural potential.</p></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-80ab-93b7-e6381fc82c06"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-80e1-8eee-f5ad8088bfe5" class=""><strong>6. 
Outcome Probability Model (R/T/A/Sg)</strong></h1></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8093-ae87-e4cb1e8b64e9" class="">Based on e and cycle position (C1–C7), assign outcome probabilities:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80bb-8a9c-e7268ce4db99" class="">High e + C1–C3 → Renewal path</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b8-ad20-d34e992e2bc8" class="">Moderate e + C3–C4 → Stagnation or partial renewal</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80c5-b04e-ed4dcffa6048" class="">Low e + C4–C5 → Absorption or collapse</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8014-8a9f-c8d4e093b553" class="">Very low e + C5–C6 → Collapse path</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-809a-af0b-e44a987d05a0" class="">High e + C7 → Sustainable renewal</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-807a-bab8-d1180871f7a8" class="">This matches 5,000 years of civilizational history.</p></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-8083-bd29-cb528de8701e"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-80c8-bcbf-f700e4f85491" class=""><strong>7. 
Interpreting Scores</strong></h1></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-8089-b666-d853165fed74" class=""><strong>High Scores (4–5)</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8095-ad55-e2a91e4a5ad6" class="">Stable, resilient, expansion-capable systems.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-806f-ac01-e0805b516226" class=""><strong>Mid Scores (2–3)</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b5-a003-e5113877566b" class="">Systems under tension but salvageable through reform.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-805e-9494-e7a3a1d24c80" class=""><strong>Low Scores (0–1)</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80c6-b9de-c8e9f7d2fc37" class="">Systems approaching crisis, collapse, or absorption.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-8053-87a4-fdfc01bd011d" class=""><strong>Thresholds</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8023-a105-cb42ac57702e" class="">i &lt; 0.4 → unstable trajectory</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8090-a3ec-e0c288b735a5" class="">i &lt; 0.3 → high collapse probability</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b4-9bc3-c16c7921e048" class="">i &lt; 0.2 → near-inevitable C6</p></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-80fc-a164-cf532f14c918"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-80e3-8e02-f3c1e1ec046a" class=""><strong>8. 
Applying CSP Across Time</strong></h1></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8042-a26b-c697cc80d4f1" class="">CSP can be applied to:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8009-b98d-d8e15ce6bdfd" class="">Ancient civilizations (Egypt, Rome, Han China)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80cc-8234-e4bdf4fc7648" class="">Medieval civilizations (Byzantium, Islamic Caliphates, Khmer)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80dc-b6c4-fa0833b3064e" class="">Modern nations (US, China, EU, Iran, India)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-801a-9b5f-f36132e4ac89" class="">Emerging states</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8033-9098-e1cb3b562687" class="">Pan-national systems (EU, AU, ASEAN)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80d3-9d2e-e9dd2e336572" class="">Civilizational blocs</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8089-91fb-ee8a5ad653d6" class="">Global civilization (21st century)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80c2-9dc1-cf54cee54d3a" class="">Because CSP uses structural variables, 
it functions consistently across:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-801e-aff4-ea07292e6dc5" class="">time periods</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8020-8f26-d68d7d10a9d6" class="">cultures</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8032-bf8c-f08f51bbe6ed" class="">ideologies</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-800e-b316-f4b3c8addc25" class="">political systems</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ae-ba8b-dcd59e1e1720" class="">technological levels</p></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-80d6-a99f-c30ae937783f"/></div><div style="display:contents" dir="auto"><h1 id="2b1c5e6f-95bd-80f1-a6f9-ce69523e2a27" class=""><strong>9. Summary</strong></h1></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8039-bcb1-c5474f48e8db" class="">The Civilizational Scoring Protocol (CSP) is the official method for quantifying the structural health and future trajectory of civilizations. 
It integrates TSS variables, PSI planetary constraints, CCI historical patterns, and the effectiveness equation <em>e=i²</em>.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8013-a047-e76681064d0a" class="">CSP provides:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ee-b1ab-fba3c50a2032" class="">a universal scoring scale</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8028-b448-c3baf0a12782" class="">a cross-civilizational comparison method</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ad-a91b-c4af0ae313d1" class="">a forecasting foundation</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-804f-9f46-ccbb37b8b8fb" class="">a governance early-warning tool</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8068-bb8d-d21c1ca79282" class="">and a dataset for AI and institutional use</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80da-ba3f-c1e8c504d74c" class="">This scoring system is now part of the canonical architecture of your full stack.</p></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-8024-920d-c12c980a2929"/></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
