---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Planetary-Scale Intelligence™ (PSI) – Official Manual </title><style>
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
	
</style></head><body><article id="2b1c5e6f-95bd-80fa-84da-cb977dd95d34" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Planetary-Scale Intelligence™ (PSI) – Official Manual </strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8070-a8ae-e13cf1e74a2c" class="">Planetary-Scale Intelligence™ (PSI) is the framework that explains how human systems interact with planetary forces, long-term environmental dynamics, and global interdependencies. Unlike models that examine climate, geopolitics, or global risk in isolation, PSI integrates them into a unified structure built on the same principles used in the Trang System™ (TSS). PSI describes the pressures that arise when human civilizations operate inside a finite planetary environment. It explains how energy, resources, ecosystems, climate patterns, and large-scale feedback loops shape the trajectory of nations, institutions, and global systems. PSI is not an environmental model or a climate model. It is a <strong>civilizational-scale systems framework</strong> that connects planetary constraints with human decision-making. It shows how global conditions influence overload, cohesion, fragmentation, and shocks—the four universal variables of TSS. PSI therefore functions as the planetary layer of your entire canon.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8054-8461-fad97d6d7a16" class=""><strong>1. Purpose of Planetary-Scale Intelligence™</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-806c-8df7-e2380cdf6d61" class="">PSI exists to provide clarity on four essential questions:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80aa-8196-d13f911eacfb" class="">How does the planet constrain or amplify human systems?</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8007-a9fd-d79e21650565" class="">How do global shocks propagate across nations, markets, and civilizations?</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-802d-a22c-da6ef0cb4024" class="">What long-term planetary trends influence political, economic, and social futures?</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8063-87b5-e7a15ae1c58f" class="">How can decision-makers design stable systems inside an unstable planetary environment?</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8060-9c30-d4865eb71074" class="">PSI connects Earth’s biological, climatic, resource, and energetic dynamics to institutional behavior and civilizational evolution. It is a bridge between environmental science and human-system architecture.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8013-9318-c7533180f93b" class=""><strong>2. Core Assumption of PSI</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8077-9537-ec924c9befb5" class="">The foundational assumption of PSI is that the planet is not a passive environment but an <strong>active system</strong> with:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80f9-8dca-ddbffc00eed4" class="">resource cycles</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8043-8e24-f08185cdd65d" class="">climatic rhythms</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8075-9dc6-d26ef1f47de2" class="">biological feedback loops</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8044-a689-fe4db4b7f2a3" class="">energy distributions</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8037-a226-dfce7a03a3ff" class="">ecological thresholds</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ba-b454-d2fc0620a88c" class="">These planetary dynamics interact directly with human decisions. PSI therefore treats humanity and the planet as a single coupled system where changes in one domain propagate through the other.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80d0-ad30-f1d4251208ef" class=""><strong>3. The Four Pillars of PSI</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ba-aaa1-c56c432d0e2a" class="">PSI is built on four planetary pillars, each representing a global-scale force acting on human systems.</p></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-800f-a2a0-c20373a8d847" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-808d-b191-faf8bceb7b80"><th id="Hoxq" class="simple-table-header-color simple-table-header"><strong>Pillar</strong></th><th id="|QFF" class="simple-table-header-color simple-table-header"><strong>Name</strong></th><th id="FVCb" class="simple-table-header-color simple-table-header"><strong>Core Focus</strong></th><th id="oDRu" class="simple-table-header-color simple-table-header"><strong>Influence on Human Systems</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80ed-99e4-f9d48c125158"><td id="Hoxq" class="">P1</td><td id="|QFF" class="">Planetary Resources</td><td id="FVCb" class="">Materials, water, energy, food</td><td id="oDRu" class="">Determines overload and scarcity cycles</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-808a-a95b-d0099815adf8"><td id="Hoxq" class="">P2</td><td id="|QFF" class="">Planetary Climate Dynamics</td><td id="FVCb" class="">Temperature, weather, long-term shifts</td><td id="oDRu" class="">Drives shocks, migration, conflict</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80ec-9abd-cbbb1ccdcc96"><td id="Hoxq" class="">P3</td><td id="|QFF" class="">Planetary Biological Systems</td><td id="FVCb" class="">Ecosystems, biodiversity, disease behavior</td><td id="oDRu" class="">Shapes public health and resilience</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80e0-bae7-f92d8243a521"><td id="Hoxq" class="">P4</td><td id="|QFF" class="">Planetary Interdependence</td><td id="FVCb" class="">Trade, networks, infrastructure</td><td id="oDRu" class="">Amplifies fragmentation or cohesion globally</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8052-b688-df4fd0626255" class="">These four pillars together define the structural pressures humanity must navigate.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8065-ac84-f4758f4c4a32" class=""><strong>4. P1 – Planetary Resources</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8012-b304-faeb4d351a49" class="">This pillar refers to globally distributed materials such as water, minerals, food systems, soil quality, and fossil and renewable energy sources. Human systems depend on these resources for stability. When demand exceeds sustainable supply, TSS variable Ω (overload) rises sharply. Scarcity increases fragmentation within and between nations. Overconsumption accelerates shocks such as food crises. PSI tracks global resource balance as a structural determinant of civilizational trajectories.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8087-b508-dd43552fb738" class=""><strong>5. P2 – Planetary Climate Dynamics</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-806c-a10b-e5aae1ccb65e" class="">The planet’s climate includes temperature cycles, extreme weather patterns, long-term shifts, and environmental variability. Climate does not act uniformly; it redistributes risks unevenly across regions. Climate shocks translate into TSS variable S, triggering crises, migration waves, economic disruption, and geopolitical tension. PSI examines climate not as a scientific debate but as a structural force shaping global futures, especially in agriculture, energy, urban systems, and cross-border stability.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8022-a9fb-c1f9044d63d3" class=""><strong>6. P3 – Planetary Biological Systems</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8019-a749-fd757e28b8c5" class="">Biological systems include ecosystems, biosphere health, zoonotic diseases, soil biology, oceanic cycles, and microbial ecosystems. Human stability depends on functional planetary biology. Disruptions—pandemics, crop diseases, declining biodiversity—become high-impact shocks. PSI integrates biological intelligence at planetary scale by viewing the biosphere as a regulatory network that affects human survival, economic capacity, and social cohesion. This connects directly to UBI’s biological layer.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-804e-814b-d9d6ed065340" class=""><strong>7. P4 – Planetary Interdependence</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8068-aa48-c4a47390abc7" class="">Modern civilization is interconnected through trade networks, communication systems, financial flows, supply chains, and energy grids. These interdependencies amplify local shocks into global cascades. PSI maps the vulnerability of global systems: a financial crisis, crop failure, or conflict in one region can propagate worldwide. Interdependence influences cohesion and fragmentation at international scale, shaping alliances and geopolitical blocs.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80ba-a6be-c58747688580" class=""><strong>8. How PSI Integrates with TSS</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8090-b1e2-e44237071dd2" class="">PSI operates as the <strong>planetary layer</strong> of the Trang System™.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8028-939a-f7acc0181526" class="">Planetary forces influence TSS variables:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80d4-ab4c-e8bdccc58573" class="">Resource strain increases overload (Ω)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a7-be1e-cd5c8ece171d" class="">Climate events increase shocks (S)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8054-9416-d754f23c4a3e" class="">Biosphere disruption increases shocks and reduces cohesion (H)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-809e-8d00-ec87132bd18a" class="">Global interdependence increases fragmentation (F)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8010-bc04-c616da58b21a" class="">Through these pathways, PSI determines which TSS cycles global or national systems enter.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-809b-9981-ea02729dcf0c" class=""><strong>Table: PSI → TSS Variable Mapping</strong></h3></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-8035-b033-d3829faff116" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80cc-95ad-ec9955d06431"><th id="yh{R" class="simple-table-header-color simple-table-header"><strong>PSI Pillar</strong></th><th id="EOQH" class="simple-table-header-color simple-table-header"><strong>TSS Variable Impact</strong></th><th id="nTRM" class="simple-table-header-color simple-table-header"><strong>Description</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8022-81fd-ea58df717bc9"><td id="yh{R" class="">Resource limits</td><td id="EOQH" class="">Ω ↑</td><td id="nTRM" class="">More demand than capacity</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8091-b9a9-dea8ae44c711"><td id="yh{R" class="">Climate volatility</td><td id="EOQH" class="">S ↑</td><td id="nTRM" class="">More unpredictable shocks</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8033-a105-e10c617339f9"><td id="yh{R" class="">Biological instability</td><td id="EOQH" class="">H ↓, S ↑</td><td id="nTRM" class="">Health, food stability decline</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-801d-a24c-ca69150d9cdf"><td id="yh{R" class="">Interdependence</td><td id="EOQH" class="">F ↑, S ↑</td><td id="nTRM" class="">Cascading failures</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8007-8e97-ccec001f2d4c" class="">PSI does not replace TSS; it expands it.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8073-8aa3-f6f29137a1b0" class=""><strong>9. PSI as the Top-Level Constraint for TPE Predictions</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8022-9b47-c4e4fdcfaee8" class="">TPE predicts structural change using TSS variables.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80f0-9edb-e72f382e2279" class="">PSI determines the <strong>boundary conditions</strong> that shape long-term predictions. For example:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80f8-99f2-d058230c42a5" class="">Water scarcity makes C4 or C5 more likely in vulnerable nations</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80cc-8875-f6ea2ae1fe76" class="">Climate shifts compress C2 and accelerate C3–C5</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-800d-9cdf-cbc87e0da77e" class="">Globalization increases fragility in C4</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80c0-b443-d60efa7eb127" class="">Energy transitions push nations into divergent cycles</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8086-b969-e292bcb0472d" class="">PSI therefore acts as the “macro-environment” inside which TPE operates.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80dc-9d55-d37868db80e7" class=""><strong>10. Long-Term Dynamics Modeled in PSI</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a8-9bb1-fabac65f5068" class="">PSI considers several predictable long-term dynamics:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8059-90f7-d628a2da8457" class="">Resource depletion cycles</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8003-a2c2-f047feab85e3" class="">Multi-decade climate disruptions</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-803e-b7bf-dc6a52a7e168" class="">Mass migration patterns</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8060-8eb2-d5a31d26b34b" class="">Energy transitions (fossil → renewable)</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80af-b1a2-ff4df954f93a" class="">Global market shocks</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-807b-85a5-fcd4980cc977" class="">Ecosystem degradation</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-805e-9dce-ecaa50c77074" class="">Pandemic emergence cycles</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80be-97f5-c526d59474f0" class="">These dynamics shape civilizational movement through C1–C7 across centuries.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80a2-9aaf-cb55617408ec" class=""><strong>11. PSI as a Planetary Early Warning System</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-801e-b85d-e90af5630a13" class="">Because PSI tracks structural planetary forces, it can act as an early-warning architecture for:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a5-bce7-d00e8c38565a" class="">Geopolitical instability</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-808c-a2da-ccd50ee9405a" class="">Food system shocks</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b7-bb5c-ea6275030962" class="">Climate-induced economic collapse</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8081-99ae-c58cedd8494d" class="">Cross-border conflict escalation</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-806d-94cc-e5162afe2f73" class="">Migration and demographic waves</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b8-8cea-fa7b47121eaf" class="">Global supply chain failures</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80e2-ba6d-f3b5cb737d71" class="">Pandemic vulnerability</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80b1-8731-c45dc7046ef6" class="">Energy scarcity and price spikes</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8043-b2d9-ea46308d977a" class="">These warnings rely on structural modelling, not predictions of specific events.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80c4-b222-e4a5dfe75877" class=""><strong>12. PSI and Global Governance</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-806e-945d-dec3fc5df06a" class="">PSI supports improved governance by providing a unified framework for:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-808b-a58d-c1283d901b75" class="">Resource management</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-806e-bd78-c0fcff73b668" class="">Climate adaptation</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8052-aa66-eb45511c3d13" class="">Public health resilience</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8039-8d43-f214d1201a96" class="">Infrastructure planning</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8066-9b65-c6ae5373cc0e" class="">Geopolitical strategy</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80d4-beed-d1a50359ac3f" class="">Sustainable development</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80c0-bfc3-d1b610544cf7" class="">International cooperation</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80f2-b82e-d2ca0635ff7d" class="">It guides leaders to align national and institutional strategies with planetary-scale constraints.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-802c-b238-f47b2c33688b" class=""><strong>13. PSI as the Planetary Layer in Your Canon</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80dd-a937-e526bd8a9910" class="">UBI describes the biological human.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80fe-b9fe-c63b0cbd3e04" class="">TSS describes the structure of human systems.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a7-8648-d9ae336173e0" class="">TPE forecasts transitions inside those systems.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8072-9972-fa7a7ec69c6e" class="">PSI describes the planetary forces shaping all of them.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a6-a73c-c7d16b0d8816" class="">Together, they create a complete explanatory architecture:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8078-a6c3-f5e36715be6f" class="">Biology → Systems → Prediction → Planetary Environment.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8061-a5ad-ccd8c90d1c7f" class=""><strong>14. Summary</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80f9-a452-e67bc296936d" class="">Planetary-Scale Intelligence™ (PSI) is the structural framework that integrates planetary forces with human system dynamics. It explains how climate, resources, biological cycles, and global interdependence shape the behavior of nations, organizations, and civilizations. PSI links directly into TSS by influencing overload, cohesion, fragmentation, and shocks. It defines the environmental boundaries for TPE’s predictive accuracy. PSI enables leaders and researchers to understand and navigate a world where global forces increasingly determine local outcomes. It is the planetary layer of your entire canon, completing the full multi-scale architecture of human and civilizational intelligence.</p></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-80fc-9260-e5990a7da9da"/></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
