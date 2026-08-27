---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Theoretical and Practical Foundations of State Management on Anti-Counterfeiting in Vietnam</title><style>
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
	
</style></head><body><article id="286c5e6f-95bd-80ef-a1ae-fc826e4aed7d" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Theoretical and Practical Foundations of State Management on Anti-Counterfeiting in Vietnam</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80d6-a7f3-fea798b55927" class=""><em>(Policy briefing; McKinsey-style, MECE, APA-International references; compliant with 10-part academic structure)</em></p></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-8044-af76-c29c00aedd7a"/></div><div style="display:contents" dir="auto"><h2 id="286c5e6f-95bd-803c-8e82-d2c292f5ea36" class=""><strong>1. Abstract</strong></h2></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-8038-81b5-cdeaef6c7d13" class="">Counterfeiting has become a systemic governance issue rather than a single-market anomaly. This briefing examines the theoretical and practical foundations of state management on anti-counterfeiting in Vietnam, situating them within administrative, economic, and digital governance theory. It outlines the evolution of Vietnam’s legal and institutional systems, identifies the key structural challenges (fragmented laws, overlapping mandates, technology deficits), and frames them within a five-pillar <strong>State Management Effectiveness Model (SMEM)</strong>. Findings show that Vietnam’s enforcement architecture—though active—is characterised by limited data integration and low deterrence elasticity. Practical reforms require a unified legal framework, permanent coordination authority, and a digital traceability backbone. 
The analysis integrates evidence from OECD–EUIPO (2025), WIPO (2024), MOIT Market Management reports (2024–2025), and ASEAN governance frameworks, ensuring both conceptual depth and empirical validity.</p></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-80be-b729-d96f0c6de12a"/></div><div style="display:contents" dir="auto"><h2 id="286c5e6f-95bd-809a-8a94-fd0bf5555a3b" class=""><strong>2. Keywords</strong></h2></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80dc-a778-dafbdf48d492" class="">Administrative management; counterfeit goods; governance theory; institutional design; Vietnam.</p></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-806e-bb7e-cf7dc6c9ac26"/></div><div style="display:contents" dir="auto"><h2 id="286c5e6f-95bd-8026-87a6-d504069acff8" class=""><strong>3. Introduction</strong></h2></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-8048-936f-e9befdd96793" class="">The management of counterfeit prevention in Vietnam represents a convergence of <strong>public governance</strong>, <strong>economic regulation</strong>, and <strong>technological control</strong>. 
Counterfeiting undermines state legitimacy, weakens public trust, and erodes national competitiveness.</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-8069-8813-d4f532c30783" class="">This briefing aims to:</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-809b-ae26-fd55695ac131" class="">(i) clarify the theoretical bases underpinning state management on anti-counterfeiting;</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80e9-9730-cd8ade04c2e5" class="">(ii) analyse the institutional evolution of Vietnam’s framework from 2005 to 2025; and</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-8017-9639-d017b73bdef2" class="">(iii) derive principles to inform future system design.</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-8002-98a8-f571912076b4" class="">Vietnam’s approach—anchored in administrative law and state responsibility—requires modernisation to adapt to global digital trade patterns. The analysis applies comparative governance theory and practical institutional mapping to identify strengths, weaknesses, and reform imperatives.</p></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-80a1-a4ed-c1cf2ca46356"/></div><div style="display:contents" dir="auto"><h2 id="286c5e6f-95bd-80f3-a364-ef65a30ed322" class=""><strong>4. 
Research Overview (literature and practice)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="286c5e6f-95bd-8025-8930-c8d0eac83a38" class=""><strong>4.1 Governance and law (what the state must do, and why it fragments in practice)</strong></h3></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8068-83ee-e74b899d6de8" class="bulleted-list"><li style="list-style-type:disc"><strong>Conceptual baseline.</strong> Vietnamese administrative scholarship defines <em>state management</em> as the lawful exercise of public authority to regulate social and market relations for collective welfare; anti-counterfeiting sits within the state’s market-integrity function (norm-setting, licensing, inspection, sanctioning, and adjudication). The literature also notes a persistent dispersion of legal bases across multiple instruments, which weakens uniform application. (Nguyen, 2019; Vu, 2021).<div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80f0-acee-cb8bc10ecf40" class=""><em>Implication:</em> clear authority exists in theory, but the <strong>translation from legal authority to operational deterrence</strong> is degraded by statutory fragmentation and overlapping mandates.</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-8087-aeb0-c1528e5113f1" class=""><em>(Context sources for global framing and Vietnam’s dispersion:)</em></p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-809e-8b82-c179fe4309c8" class="bulleted-list"><li style="list-style-type:disc"><strong>Latest global anchor for “why the state must act”.</strong> The <strong>OECD–EUIPO 2025</strong> update (based on 2021 seizure data) estimates counterfeit and pirated goods at <strong>~2.3% of world trade (≈ USD 467 billion)</strong> and <strong>~4.7% of EU imports</strong>—a persistent share, not a short-term spike. 
That magnitude justifies active regulatory intervention and enforcement.</li></ul></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-80eb-9baf-cae2e84a2df5"/></div><div style="display:contents" dir="auto"><h3 id="286c5e6f-95bd-8076-9e15-e1266e81bfaf" class=""><strong>4.2 Economic regulation (externalities, fiscal risk, and prioritisation)</strong></h3></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80ea-ac0b-d27af4281cb8" class="bulleted-list"><li style="list-style-type:disc"><strong>Externality logic.</strong> Counterfeiting imposes negative externalities—consumer harm, tax leakage, reputational damage, and innovation loss—unpriced by private actors. OECD/WIPO treat anti-counterfeiting as a <strong>market-correcting public good</strong> requiring state action (deterrent sanctions, information transparency, and enforcement).</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8055-8707-cfba40c5cdd7" class="bulleted-list"><li style="list-style-type:disc"><strong>Prioritisation signal.</strong> Within the EU, the 2025 figures translate to <strong>~EUR 99 billion</strong> of fake-goods imports (2021), guiding cost–benefit prioritisation by sector and channel. 
Vietnam lacks equivalent monetised loss estimates, reducing the ability to rank interventions by fiscal impact.</li></ul></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-8019-9ae2-f51f5e576114"/></div><div style="display:contents" dir="auto"><h3 id="286c5e6f-95bd-803a-9d7c-f22ec3ea21c5" class=""><strong>4.3 Technological governance (from inspection to prediction)</strong></h3></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80a0-8668-f6edf3e7a2a5" class="bulleted-list"><li style="list-style-type:disc"><strong>What works globally.</strong> Jurisdictions that pair <strong>serialisation/traceability</strong> with <strong>interoperable enforcement data</strong> shift from reactive raids to risk-led, predictive enforcement. The EU’s move to <strong>digital customs/data hubs</strong> and the U.S. model of <strong>recordation-driven targeting</strong> have underpinned sustained interception results.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80ce-8527-e72ce1787d8a" class="bulleted-list"><li style="list-style-type:disc"><strong>EU throughput (latest).</strong> In <strong>2024</strong>, EU customs and market-surveillance authorities <strong>intercepted 112 million items</strong>, <strong>~€3.8 billion</strong> in estimated retail value—reported 1 October 2025 by DG TAXUD (the decline in item count from 2023’s peak is offset by a value surge in higher-value categories).</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-800a-9df6-cbd082837059" class="bulleted-list"><li style="list-style-type:disc"><strong>U.S. 
throughput (latest).</strong> <strong>CBP FY2024</strong> statistics confirm continued high-volume IPR seizures and the operational role of <strong>e-recordation</strong> and brand product guides in risk targeting—again indicating that <strong>data + serialisation</strong> improves detection precision and evidentiary quality.</li></ul></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-80e3-bc7a-d9db2ddf7465"/></div><div style="display:contents" dir="auto"><h3 id="286c5e6f-95bd-8004-ab04-f01ae970b09d" class=""><strong>4.4 Channels and sectoral composition (where the risk concentrates)</strong></h3></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8045-aab0-ddda7164ebc9" class="bulleted-list"><li style="list-style-type:disc"><strong>Demand via marketplaces.</strong> WIPO’s enforcement work and a 17-country survey show <strong>74%</strong> of consumers reported purchasing at least one counterfeit item in the prior year; <strong>68%</strong> were deceived at least once; <strong>52%</strong> knowingly purchased at least once; <strong>21%</strong> were habitual knowing buyers—underscoring <strong>e-commerce as a principal vector</strong> and the need for intermediary obligations.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80bc-8be0-d3ff37cdd141" class="bulleted-list"><li style="list-style-type:disc"><strong>Product mix (EU lens).</strong> EUIPO’s 2025 synopsis highlights dominant categories (<strong>clothing/footwear/accessories</strong>) and growing safety-critical types (e.g., <strong>medicines, cosmetics, toys, auto parts</strong>). 
Provenance economies include <strong>China and Hong Kong</strong>, with <strong>Türkiye</strong> and certain re-export hubs prominent—relevant for Vietnam’s import-risk profiling.</li></ul></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-80b0-b7af-ec8b22f2a2e0"/></div><div style="display:contents" dir="auto"><h3 id="286c5e6f-95bd-8004-b265-c544f7884d5a" class=""><strong>4.5 Vietnam practice (latest signals, institutions, and pain points)</strong></h3></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8069-a067-f801e1784b22" class="bulleted-list"><li style="list-style-type:disc"><strong>Throughput (2024).</strong> Vietnam’s Market Management teams conducted <strong>&gt;3,400 e-commerce inspections</strong>; <strong>1,256</strong> involved counterfeits/IP infringements; <strong>≈ USD 1.9 m</strong> in fines; <strong>≈ USD 2 m</strong> in confiscations—confirming a pivot to platform-linked enforcement.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80b4-a91a-dc4988761054" class="bulleted-list"><li style="list-style-type:disc"><strong>2025 operations.</strong> High-profile <strong>Saigon Square</strong> raids seized thousands of luxury fakes (watches, bags), highlighting both political will and the persistence of offline hubs feeding from online supply. 
Government statements in May 2025 also flagged <strong>1,100 counterfeit/IP cases</strong> year-to-date alongside broader smuggling and trade-fraud data.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8093-853a-ca319b7fe625" class="bulleted-list"><li style="list-style-type:disc"><strong>Regulatory tightening on foreign platforms.</strong> Vietnam has pressed platform registration/compliance (e.g., late-2024 actions toward cross-border marketplaces) as part of a wider programme to curb counterfeit flows via e-commerce.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8019-bcbe-df1d2da4e1f5" class="bulleted-list"><li style="list-style-type:disc"><strong>Institutional reality.</strong> Enforcement remains <strong>multi-agency</strong> (Market Management—MOIT; Customs—MOF; Economic Police—MPS; sector inspectorates), with <strong>campaign-based coordination</strong> and <strong>siloed data</strong>; consumer-side verification tools are not yet universal.</li></ul></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-80c6-8838-d0beeec1c919"/></div><div style="display:contents" dir="auto"><h3 id="286c5e6f-95bd-8063-ae29-e67a3e9f8f04" class=""><strong>4.6 What the literature converges on (and what Vietnam still lacks)</strong></h3></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80f1-9eb8-d965f28fd4e9" class="bulleted-list"><li style="list-style-type:disc"><strong>Convergence internationally:</strong><div style="display:contents" dir="auto"><ol type="1" id="286c5e6f-95bd-800f-b044-cfd1e9854d55" class="numbered-list" start="1"><li><strong>Unified legal architecture</strong> (single owner; 
consistent offence/penalty ladders),</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="286c5e6f-95bd-806f-b9c0-e4c33a02495f" class="numbered-list" start="2"><li><strong>Permanent, data-driven coordination nodes</strong> (customs + market + prosecutors),</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="286c5e6f-95bd-80ba-b6d2-f5dfa9662cfb" class="numbered-list" start="3"><li><strong>Digital traceability/serialisation</strong> plus <strong>case-intelligence backbones</strong>,</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="286c5e6f-95bd-8007-b8a0-df0419d806f9" class="numbered-list" start="4"><li><strong>Enforceable public–private compacts</strong> (platforms, logistics, payments, rights holders), and</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="286c5e6f-95bd-801b-9d2d-eb2eb331a4d7" class="numbered-list" start="5"><li><strong>Live cross-border risk alerts</strong>.</li></ol></div></li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-803c-98d6-f07baa700fb3" class="bulleted-list"><li style="list-style-type:disc"><strong>Vietnam’s unresolved deficits (mirror the evidence):</strong><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80c1-b79b-f7593917bcf1" class=""><strong>(i)</strong> <em>Statutory dispersion</em>—no unified Anti-Counterfeiting Act; 
uneven sanction certainty (diagnosed in domestic reporting and implied by case-qualification frictions).</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-802b-87d2-f543fd489ecd" class=""><strong>(ii)</strong> <em>Institutional silos</em>—no shared case backbone linking <strong>Customs ⇄ Market Management ⇄ Police ⇄ Procuracy</strong>.</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80ca-b1f0-eb5e95af6301" class=""><strong>(iii)</strong> <em>Technology gap</em>—pilots exist, but <strong>no national, GS1-compatible traceability platform</strong> with consumer verification and end-to-end chain-of-custody.</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-804f-8277-d55857432709" class=""><strong>(iv)</strong> <em>Partnership asymmetry</em>—voluntary MoUs with platforms/brands, limited duties for logistics and payments.</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80fc-aca7-dd97bc959834" class=""><strong>(v)</strong> <em>International latency</em>—periodic (not real-time) risk exchange, while EU/U.S. 
demonstrate sustained gains from data-led coordination.</p></div></li></ul></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-80d9-a2ea-cbd84b35a5cb"/></div><div style="display:contents" dir="auto"><h3 id="286c5e6f-95bd-802e-b7b7-caab7c4be826" class=""><strong>4.7 Why this matters for policy design (MECE closure)</strong></h3></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8021-8922-cff129e9bc93" class="bulleted-list"><li style="list-style-type:disc"><strong>Scale justifies intervention</strong> (OECD–EUIPO 2.3%/USD 467 bn; EU 4.7% imports).</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80d4-84a3-d55741c3de05" class="bulleted-list"><li style="list-style-type:disc"><strong>Channels explain persistence</strong> (high consumer contact via e-commerce; 17-country survey).</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80f4-a8ea-c4fbb1042916" class="bulleted-list"><li style="list-style-type:disc"><strong>Technology explains results</strong> (EU 2024: 112 m items; €3.8 bn; U.S. FY2024 sustained seizures—both tied to data/traceability).</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80a8-8d25-c539eefbb39c" class="bulleted-list"><li style="list-style-type:disc"><strong>Vietnam’s outputs show effort, not deterrence</strong> (3,400+ checks; 1,256 IPR cases; high-profile raids) because <strong>integration levers remain missing</strong>.</li></ul></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-8023-9016-ec0ce802f28c" class=""><strong>Bottom line:</strong> The <strong>evidence base is mature and consistent</strong>; the <strong>gap is structural</strong>. 
Closing Vietnam’s law–institution–technology gaps (not merely adding campaigns) is the only path to durable deterrence.</p></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-80de-b5a8-cf0cf88973b2"/></div><div style="display:contents" dir="auto"><h2 id="286c5e6f-95bd-802f-b0ad-c4c2f912e17e" class=""><strong>5. Methods</strong></h2></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80aa-9dbd-ea5a58865253" class="bulleted-list"><li style="list-style-type:disc"><strong>Document and policy review:</strong> Analysis of Vietnam’s legal corpus (IP Law 2005/2022, Decree 98/2020/NĐ-CP, Penal Code 2015/2017, Competition and Consumer Protection Law 2023).</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8012-9c0a-d35117e2f96a" class="bulleted-list"><li style="list-style-type:disc"><strong>Comparative framework:</strong> Benchmarking against EU, U.S., and ASEAN governance systems for counterfeiting control.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80a5-b1cd-f072cb6bf3c2" class="bulleted-list"><li style="list-style-type:disc"><strong>Analytical model:</strong> Application of the <strong>State Management Effectiveness Model (SMEM)</strong>—five pillars: <em>Law, Institutions, Technology, Partnerships, International Coordination</em>.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8071-9e40-d07e607ce5eb" class="bulleted-list"><li style="list-style-type:disc"><strong>Empirical validation:</strong> Use of 2024–2025 enforcement data from MOIT, Customs, and press reports (Vietnam News, Reuters).</li></ul></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-80a6-a548-e46877d981b7"/></div><div style="display:contents" dir="auto"><h2 id="286c5e6f-95bd-802e-8064-dfcab7228e40" class=""><strong>6. 
Research Results</strong></h2></div><div style="display:contents" dir="auto"><h3 id="286c5e6f-95bd-8008-9562-c3d3301a23b7" class=""><strong>6.1 Legal Foundation</strong></h3></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80bb-a85f-d7c54db1c032" class="">Vietnam’s anti-counterfeiting legal structure is <strong>broad but fragmented</strong>—spanning multiple laws, decrees, and circulars without a single governing statute.</p></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80eb-8c5a-d0432745bbfa" class="bulleted-list"><li style="list-style-type:disc"><strong>Legal dispersion:</strong> Core provisions are scattered across the <em>Law on Intellectual Property (2005, amended 2022)</em>, <em>Law on Competition and Consumer Protection (2023)</em>, <em>Penal Code (2015, amended 2017)</em>, and <em>Decree No. 98/2020/NĐ-CP</em> on trade violations. Each defines offences and sanctions differently, creating interpretive inconsistency.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-808d-a337-e0685b48cffc" class="bulleted-list"><li style="list-style-type:disc"><strong>Penalty asymmetry:</strong> Administrative fines for counterfeit trade range from <strong>VND 1 million – 250 million</strong>, while criminal thresholds depend on product type and value—producing uneven deterrence and opportunities for regulatory arbitrage.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80f1-8b8c-c069d3b9534e" class="bulleted-list"><li style="list-style-type:disc"><strong>Overlap of enforcement powers:</strong> Inspection, seizure, and prosecution authority are distributed among <em>Market Management</em>, <em>Customs</em>, and <em>Police</em>. 
No unified statute specifies hierarchy or procedural sequencing, delaying action and complicating case transfer.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8051-b4c2-fd686458f5ab" class="bulleted-list"><li style="list-style-type:disc"><strong>Procedural bottlenecks:</strong> Evidence standards differ between administrative and criminal routes, causing delays of <strong>60–120 days</strong> for inter-agency coordination before prosecution.</li></ul></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-802f-b7c5-c1f3709bfc84" class=""><strong>Implication:</strong> Vietnam’s legal base meets WTO/TRIPS compliance but lacks <em>codified integration</em>. 
Without a single <em>Anti-Counterfeiting Act</em>, sanction certainty and enforcement velocity remain low.</p></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-8056-b2e7-fb3ee3d078ba"/></div><div style="display:contents" dir="auto"><h3 id="286c5e6f-95bd-8032-9ab7-d3de96d6b612" class=""><strong>6.2 Institutional Foundation</strong></h3></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80a9-9a87-dd80e8318e98" class="">Vietnam operates a <strong>multi-agency enforcement system</strong>, ensuring coverage across the supply chain but with diffuse accountability.</p></div><div style="display:contents" dir="ltr"><table id="286c5e6f-95bd-80ea-961a-eff568d63900" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="286c5e6f-95bd-801a-aa25-ffa3840bd506"><th id="yLc[" class="simple-table-header-color simple-table-header"><strong>Agency</strong></th><th id="pwDh" class="simple-table-header-color simple-table-header"><strong>Parent ministry</strong></th><th id="ir@M" class="simple-table-header-color simple-table-header"><strong>Core mandate</strong></th><th id="GXqy" class="simple-table-header-color simple-table-header"><strong>Observed gaps</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="286c5e6f-95bd-80d1-9ffd-cf9069e959de"><td id="yLc[" class="">Market Management Directorate</td><td id="pwDh" class="">Ministry of Industry &amp; Trade (MOIT)</td><td id="ir@M" class="">Domestic trade, retail, and e-commerce inspections</td><td id="GXqy" class="">Case overlap with local police; 
limited access to customs risk data</td></tr></div><div style="display:contents" dir="ltr"><tr id="286c5e6f-95bd-804b-ae6f-f93f4f384a0c"><td id="yLc[" class="">General Department of Customs</td><td id="pwDh" class="">Ministry of Finance (MOF)</td><td id="ir@M" class="">Border inspection and declaration review</td><td id="GXqy" class="">Seizure data not linked to domestic follow-up</td></tr></div><div style="display:contents" dir="ltr"><tr id="286c5e6f-95bd-8053-aab4-edc78226f5f5"><td id="yLc[" class="">Economic Police (C03, C46)</td><td id="pwDh" class="">Ministry of Public Security (MPS)</td><td id="ir@M" class="">Criminal investigation and prosecution</td><td id="GXqy" class="">Reactive approach; limited digital evidence sharing</td></tr></div><div style="display:contents" dir="ltr"><tr id="286c5e6f-95bd-803f-99a2-e033b370d8fe"><td id="yLc[" class="">Sectoral inspectorates</td><td id="pwDh" class="">MOH, MARD, MOST</td><td id="ir@M" class="">Safety and specialised sectors (food, drugs, electronics)</td><td id="GXqy" class="">Parallel workflows; 
no standard reporting format</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80d9-80e9-ec6d95fdb351" class="bulleted-list"><li style="list-style-type:disc"><strong>Coordination latency:</strong> Average cycle from detection to sanction exceeds <strong>90 days</strong>, partly due to manual data exchange and lack of a shared case backbone.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8033-8254-e7bdd1bd9585" class="bulleted-list"><li style="list-style-type:disc"><strong>Budget dispersion:</strong> Separate line items across ministries prevent central performance benchmarking.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8087-a5ee-fd1ba459677e" class="bulleted-list"><li style="list-style-type:disc"><strong>Human-capital asymmetry:</strong> Less than <strong>15%</strong> of Market Management staff hold digital-evidence training or certification (MOIT 2024).</li></ul></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80fa-970d-daeb88d910d1" class=""><strong>Implication:</strong> Institutional mandates cover all stages (border–market–criminal), but no single entity owns <em>case closure</em>—reducing deterrence through diluted accountability.</p></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-80eb-ab7c-efeedd227b73"/></div><div style="display:contents" dir="auto"><h3 id="286c5e6f-95bd-809a-996a-eacafbc14df4" class=""><strong>6.3 Technological Foundation</strong></h3></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-801f-9bd9-e9b177edf04f" class="">Digital infrastructure remains <strong>nascent and unintegrated</strong>, 
limiting traceability and risk-led targeting.</p></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80e4-bc59-e8769bcb14fe" class="bulleted-list"><li style="list-style-type:disc"><strong>Existing pilots:</strong><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-8054-9376-cf9fa1a1a440" class="">– <em>GS1 Vietnam</em> codes for food and pharmaceuticals;</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80ef-8cfd-dcc33622eef9" class="">– <em>Brand-authentication labels</em> (QR or hologram) under MOIT Circular 15/2020;</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80e6-86e6-dfd46481e4c4" class="">– <em>Blockchain tagging</em> trials (2022–2024) by selected consumer-goods brands.</p></div></li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8038-8a3a-f9671d76d3f4" class="bulleted-list"><li style="list-style-type:disc"><strong>Lack of scale:</strong> None of these initiatives operate at national coverage or integrate with <em>Customs</em> or <em>Market Management</em> systems.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8009-a158-d98e2799f9bc" class="bulleted-list"><li style="list-style-type:disc"><strong>System fragmentation:</strong> Separate platforms for import declarations (VNACCS/VCIS), e-commerce inspection logs, and police evidence management operate independently.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8058-9873-daf5b9dd242b" class="bulleted-list"><li style="list-style-type:disc"><strong>Traceability coverage:</strong> Estimated at <strong>&lt; 25%</strong> of high-risk SKUs** (pharma, cosmetics, electronics) as of mid-2025.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-802e-a3c1-ef236261069c" class="bulleted-list"><li style="list-style-type:disc"><strong>Consumer verification:</strong> No unified mobile app exists; 
consumers rely on brand-specific QR systems with variable reliability.</li></ul></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80b1-842f-cbb762a84eb8" class=""><strong>Implication:</strong> Absence of an <em>end-to-end digital case pipeline</em> allows counterfeit products to re-enter circulation post-seizure, undermining enforcement credibility.</p></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-8037-ad92-f2b607955aeb"/></div><div style="display:contents" dir="auto"><h3 id="286c5e6f-95bd-80bc-93dd-f645635266d0" class=""><strong>6.4 Practical Enforcement (2024–2025)</strong></h3></div><div style="display:contents" dir="ltr"><table id="286c5e6f-95bd-800e-9c1c-e0e4e0908b0d" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="286c5e6f-95bd-80f0-899e-ff0ebddb6b5b"><th id="Y`|o" class="simple-table-header-color simple-table-header"><strong>Indicator</strong></th><th id="Xas&gt;" class="simple-table-header-color simple-table-header"><strong>2024</strong></th><th id="ZlDB" class="simple-table-header-color simple-table-header"><strong>2025 (1H)</strong></th><th id="FcH]" class="simple-table-header-color simple-table-header"><strong>Source</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="286c5e6f-95bd-8008-891d-e922ac31251e"><td id="Y`|o" class="">E-commerce inspections</td><td id="Xas&gt;" class="">3 420</td><td id="ZlDB" class="">&gt; 
2 100</td><td id="FcH]" class="">MOIT 2025</td></tr></div><div style="display:contents" dir="ltr"><tr id="286c5e6f-95bd-8060-b066-dfd58ac72bd9"><td id="Y`|o" class="">IPR-infringement cases</td><td id="Xas&gt;" class="">1 256</td><td id="ZlDB" class="">≈ 720</td><td id="FcH]" class="">MOIT 2025</td></tr></div><div style="display:contents" dir="ltr"><tr id="286c5e6f-95bd-8061-9e7f-c4a585a80b37"><td id="Y`|o" class="">Administrative fines (USD)</td><td id="Xas&gt;" class="">1.9 million</td><td id="ZlDB" class="">1.0 million +</td><td id="FcH]" class="">MOIT 2025</td></tr></div><div style="display:contents" dir="ltr"><tr id="286c5e6f-95bd-8039-afde-c8dfcc604cb7"><td id="Y`|o" class="">Goods confiscated (USD)</td><td id="Xas&gt;" class="">2.0 million</td><td id="ZlDB" class="">2.5 million</td><td id="FcH]" class=""><em>Reuters</em>, 2025</td></tr></div><div style="display:contents" dir="ltr"><tr id="286c5e6f-95bd-80cf-be65-d09ac08f9933"><td id="Y`|o" class="">Average case duration</td><td id="Xas&gt;" class="">88 days</td><td id="ZlDB" class="">79 days</td><td id="FcH]" class="">MOIT internal data</td></tr></div><div style="display:contents" dir="ltr"><tr id="286c5e6f-95bd-80a1-974c-fdfbad1500fa"><td id="Y`|o" class="">Repeat-offender rate</td><td id="Xas&gt;" class="">27 %</td><td id="ZlDB" class="">25 %</td><td id="FcH]" class="">Market Management Directorate</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8001-8c27-d44f9cff50c8" class="bulleted-list"><li style="list-style-type:disc"><strong>E-commerce focus:</strong> The share of online-channel cases rose from <strong>32 % (2023)</strong> to <strong>&gt; 
50 % (2024)</strong>, driven by high visibility of platforms such as TikTok Shop and Shopee.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8022-8fca-c7fe626c0083" class="bulleted-list"><li style="list-style-type:disc"><strong>High-profile raids:</strong> The 2025 <em>Saigon Square</em> operation (Ho Chi Minh City) seized thousands of luxury-brand fakes (Rolex, Prada), signalling intensified enforcement yet recurring offences—proof of system fragility.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-801d-8034-dcada391454a" class="bulleted-list"><li style="list-style-type:disc"><strong>Cross-border linkages:</strong> Customs reports a <strong>17 % year-on-year increase</strong> in counterfeit seizures at express-freight hubs; 
however, only <strong>42 %</strong> of these were referred for domestic follow-up, showing the persistence of border-to-market disconnects.</li></ul></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-805c-9c11-f40e713ee739" class=""><strong>Implication:</strong> Enforcement activity is rising, but structural fragmentation allows rapid counterfeit regeneration—turning raids into cyclical rather than preventive measures.</p></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-8084-b191-d691812d1b1a"/></div><div style="display:contents" dir="auto"><h3 id="286c5e6f-95bd-8007-9173-d4256317c55f" class=""><strong>Summary of Findings</strong></h3></div><div style="display:contents" dir="ltr"><table id="286c5e6f-95bd-8059-8ee6-f9e3745438a7" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="286c5e6f-95bd-801e-b869-cf8459bea84a"><th id="Mewc" class="simple-table-header-color simple-table-header"><strong>SMEM Pillar</strong></th><th id="\uGk" class="simple-table-header-color simple-table-header"><strong>Current Capability (Vietnam)</strong></th><th id="Ym`P" class="simple-table-header-color simple-table-header"><strong>Observed Weakness</strong></th><th id="neIV" class="simple-table-header-color simple-table-header"><strong>Benchmark Reference</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="286c5e6f-95bd-80c0-a656-fd9d197b3ac6"><td id="Mewc" class="">Law</td><td id="\uGk" class="">Multi-law dispersion; partial harmonisation</td><td id="Ym`P" class="">Inconsistent offences and penalties</td><td id="neIV" class="">EU IPR Enforcement Directive (2019/2161)</td></tr></div><div style="display:contents" dir="ltr"><tr id="286c5e6f-95bd-8038-9875-c4f9fa22be7f"><td id="Mewc" class="">Institutions</td><td id="\uGk" class="">Five key agencies, campaign-based coordination</td><td id="Ym`P" class="">No central case-management node</td><td id="neIV" class="">U.S. 
CBP–ICE Joint Task Force model</td></tr></div><div style="display:contents" dir="ltr"><tr id="286c5e6f-95bd-80b5-b26e-f8683184487f"><td id="Mewc" class="">Technology</td><td id="\uGk" class="">Pilot traceability systems</td><td id="Ym`P" class="">No integrated digital backbone</td><td id="neIV" class="">EU Digital Customs Reform (2024)</td></tr></div><div style="display:contents" dir="ltr"><tr id="286c5e6f-95bd-8039-b4c7-f2d4df5f6b02"><td id="Mewc" class="">Partnerships</td><td id="\uGk" class="">Ad-hoc MoUs with brands/platforms</td><td id="Ym`P" class="">No formal PPP compacts or KYC standards</td><td id="neIV" class="">WIPO ACE 2023 trusted-notifier model</td></tr></div><div style="display:contents" dir="ltr"><tr id="286c5e6f-95bd-80ac-8daf-e8b3162bdd25"><td id="Mewc" class="">International</td><td id="\uGk" class="">ASEAN cooperation; annual joint actions</td><td id="Ym`P" class="">No real-time data exchange</td><td id="neIV" class="">EU ROP and OLAF coordinated operations</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-807a-b019-f19f7fdbc750" class=""><strong>Overall conclusion:</strong> Vietnam’s enforcement framework demonstrates commitment and coverage but not <em>systemic integration</em>. Structural latency across <strong>law, institutions, and technology</strong> explains the persistence of counterfeit circulation despite visible enforcement effort.</p></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-8015-b2f5-e099615f6015"/></div><div style="display:contents" dir="auto"><h2 id="286c5e6f-95bd-80e4-b664-fd207e5b02f2" class=""><strong>7. Discussion (root-cause analysis; MECE)</strong></h2></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80b3-bdfa-c2260241d3ed" class="">This section converts the diagnostic into root causes with clear mechanisms, impact pathways, and targeted levers. 
Each item follows the pattern <strong>diagnosis → mechanism → observable indicators → policy lever</strong> and maps to one SMEM pillar.</p></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-806b-a25d-d1b527421ce3"/></div><div style="display:contents" dir="auto"><h3 id="286c5e6f-95bd-80c7-a2a8-e9f220939abb" class=""><strong>A. 
Legal dispersion (SMEM: Law)</strong></h3></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80f9-b2b6-c5b1c4dc7cba" class=""><strong>Diagnosis.</strong> Offences and sanctions are spread across multiple instruments; 
thresholds and procedures differ by sector and channel.</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-800f-b438-ccca063794f2" class=""><strong>Mechanism.</strong> Investigators face qualification ambiguity (administrative vs criminal), which elongates case routing and lowers expected punishment (probability × severity × swiftness).</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80c2-889b-e439ee265df4" class=""><strong>Observable indicators.</strong></p></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-807b-8ee9-d72ae7c87398" class="bulleted-list"><li style="list-style-type:disc">High proportion of cases downgraded from criminal to administrative.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-805e-98ec-e62d4bd0a5e3" class="bulleted-list"><li style="list-style-type:disc">Wide variance in penalties for similar conduct across provinces/sectors.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80d4-9434-dbc5818ba86a" class="bulleted-list"><li style="list-style-type:disc">Long legal-qualification time (handoffs between inspectorates, police, procuracy).</li></ul></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80a8-ae8e-dee6cdde4967" class=""><strong>Policy lever.</strong></p></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80e0-8702-eeb9e989c82d" class="bulleted-list"><li style="list-style-type:disc"><strong>Unified Anti-Counterfeiting and Market Integrity Act</strong>: single offence taxonomy, harmonised sanction ladders, online-to-offline coverage, 
and fast-track injunctive powers.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80f3-b989-e51a49827e23" class="bulleted-list"><li style="list-style-type:disc"><strong>Authoritative guidance circular</strong> from the Procuracy to standardise qualification and evidence sufficiency.</li></ul></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80f2-ad01-d0d9ec04c119" class=""><strong>Result metric.</strong> ≥30–40% reduction in time-to-charge; ≤10% variance in sanctions for like cases.</p></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-80e5-b838-fdc7c83ddd02"/></div><div style="display:contents" dir="auto"><h3 id="286c5e6f-95bd-80dd-8945-e1606e0795d3" class=""><strong>B. 
Institutional fragmentation (SMEM: Institutions)</strong></h3></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80df-9f6f-c59e220d7671" class=""><strong>Diagnosis.</strong> Five core bodies operate in parallel; no permanent owner of end-to-end outcomes.</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-8055-ae3f-e3804da6f154" class=""><strong>Mechanism.</strong> Paper or spreadsheet-based handoffs create cycle-time “dead zones”; duplicated inspections crowd out risk-led work; 
accountability diffuses.</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-8040-b451-e826ee5f6e56" class=""><strong>Observable indicators.</strong></p></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80a1-ab74-ecdda1400588" class="bulleted-list"><li style="list-style-type:disc">2 agency handoffs per case on average.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8063-929c-f75231e882a1" class="bulleted-list"><li style="list-style-type:disc">Redundant field inspections on the same premises/seller.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8047-be66-c1e0c92a5a9e" class="bulleted-list"><li style="list-style-type:disc">Low referral conversion: border seizures that do not trigger domestic follow-up.</li></ul></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-809c-9e48-e9ed8822011f" class=""><strong>Policy lever.</strong></p></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8051-9b41-d73c4953059e" class="bulleted-list"><li style="list-style-type:disc"><strong>National Anti-Counterfeiting Authority (NACA)</strong> with a <strong>Joint Targeting Cell</strong> and shared KPIs (case cycle time, referral conversion, repeat-offender rate).</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-802a-9aab-fae2c10f441c" class="bulleted-list"><li style="list-style-type:disc">Performance-linked budgets across agencies tied to joint outputs.</li></ul></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-8072-b6da-d7e87aecdd70" class=""><strong>Result metric.</strong> ≥50% reduction in investigation-to-sanction days; ≥70% border-to-market referral conversion.</p></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-800e-8552-e660403c5910"/></div><div style="display:contents" dir="auto"><h3 id="286c5e6f-95bd-8078-bf8e-cfaac18817bd" class=""><strong>C. 
Technological deficit (SMEM: Technology)</strong></h3></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-801d-bed9-ebfd4613c34b" class=""><strong>Diagnosis.</strong> Serialisation/traceability pilots exist but are siloed; there is no interoperable case backbone linking customs, platforms, logistics, and prosecutors.</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-800a-8130-f7e745be842b" class=""><strong>Mechanism.</strong> Without machine-readable product IDs and chain-of-custody records, detection in small consignments is low and evidentiary robustness weak; counterfeit goods can recycle post-seizure.</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80f5-b09f-cfff9542371e" class=""><strong>Observable indicators.</strong></p></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8077-9623-c3f2d1a48e8f" class="bulleted-list"><li style="list-style-type:disc">Detection rate for small parcels &lt;0.02%.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-804b-bac0-ca3dff6e3f8d" class="bulleted-list"><li style="list-style-type:disc">Evidence rejection or supplementation requests from prosecutors due to chain-of-custody gaps.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80cd-b8a2-e622060d1288" class="bulleted-list"><li style="list-style-type:disc">Limited consumer verification usage; multiple brand apps with inconsistent reliability.</li></ul></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-8051-80da-c8f0fd81702c" class=""><strong>Policy lever.</strong></p></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80a2-8faa-dd6c1fcb1d3e" class="bulleted-list"><li style="list-style-type:disc"><strong>National Digital Traceability &amp; 
Case-Intelligence Platform (NT-CIP)</strong>: GS1-compatible serialisation, consumer app, automated customs–market data flow, digital evidence locker, API links to marketplaces and payment processors.</li></ul></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-8072-85f3-febba6363715" class=""><strong>Result metric.</strong> +50% precision in targeted checks; −60% evidentiary losses; ≥85% traceability coverage in five priority categories by year 4.</p></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-8032-9dbc-d193285fe4b4"/></div><div style="display:contents" dir="auto"><h3 id="286c5e6f-95bd-806e-bfdb-e8f70a8c31fb" class=""><strong>D. 
Partnership asymmetry (SMEM: Partnerships)</strong></h3></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-800d-ae2c-f51b7e17b028" class=""><strong>Diagnosis.</strong> Rights holders, platforms, logistics, and payment intermediaries hold most of the actionable intelligence; cooperation is voluntary and ad-hoc.</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80e2-90ad-d0c3f215732c" class=""><strong>Mechanism.</strong> Absent enforceable duties, data arrive late (or not at all); takedowns lag; 
the state pays to rediscover what firms already know.</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-8078-b55b-c2207c330588" class=""><strong>Observable indicators.</strong></p></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8061-a71b-da5920493933" class="bulleted-list"><li style="list-style-type:disc">Long takedown latency for flagged listings.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-807a-853d-d800177ee5ec" class="bulleted-list"><li style="list-style-type:disc">Minimal inbound signals from payment and fulfilment providers.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80be-ac41-f3f8c6c34b2c" class="bulleted-list"><li style="list-style-type:disc">Duplicated investigations by agencies and brands.</li></ul></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80a3-94e4-e0f663c9efec" class=""><strong>Policy lever.</strong></p></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80bf-82d5-ea0311ec8496" class="bulleted-list"><li style="list-style-type:disc"><strong>Statutory PPP compacts</strong> under NACA with three tracks:<div style="display:contents" dir="auto"><ol type="1" id="286c5e6f-95bd-807d-ae70-d6761f0d1950" class="numbered-list" start="1"><li><strong>Platforms:</strong> trusted-notifier channels, 24-hour takedown SLA, seller KYC and listing provenance logs.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="286c5e6f-95bd-803a-bfa0-e28a0493162d" class="numbered-list" start="2"><li><strong>Logistics/fulfilment:</strong> shipper/consignee KYC, parcel data feeds, high-risk-route flags.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="286c5e6f-95bd-800b-b883-d40ba5a060e6" class="numbered-list" start="3"><li><strong>Rights holders/associations:</strong> product-guide libraries, rapid testing kits, 
co-funded training.</li></ol></div></li></ul></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80f7-9ee8-e3e554a90f11" class=""><strong>Result metric.</strong> 40–60% faster online removal; ≥30% reduction in duplicated inspections; ≥20% uplift in risk-signal volume from private partners.</p></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-801a-a64e-daeea6b147e8"/></div><div style="display:contents" dir="auto"><h3 id="286c5e6f-95bd-802c-b042-f0e214042802" class=""><strong>E. 
International exchange limits (SMEM: International Coordination)</strong></h3></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-803a-b23d-c603a39f4035" class=""><strong>Diagnosis.</strong> Participation in ASEAN/WIPO mechanisms is largely periodic and report-based; there is no live risk-signal exchange with regional customs and police.</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80cb-949f-e752b11af28a" class=""><strong>Mechanism.</strong> High-risk consignments identified abroad are not interdicted upstream; repeat shippers exploit time lags and route fragmentation.</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80c2-ad0e-d50fe1725849" class=""><strong>Observable indicators.</strong></p></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80cf-8e88-c2313c9f4849" class="bulleted-list"><li style="list-style-type:disc">Low number of actionable inbound alerts; limited joint operations targeting small consignments.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80be-90bd-e3a0b41c40a5" class="bulleted-list"><li style="list-style-type:disc">Duplicate seizures of identical MOQs/SKUs across borders within short intervals.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80bf-9471-f2f10da8785e" class="bulleted-list"><li style="list-style-type:disc">Slow mutual legal assistance (MLA) cycle times.</li></ul></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-808a-97b3-fe4f4e177725" class=""><strong>Policy lever.</strong></p></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-804d-84a9-c3ca21cb8f6e" class="bulleted-list"><li style="list-style-type:disc"><strong>ASEAN Real-Time Alert Protocol (pilot)</strong> for small-parcel routes; standardised digital evidence packets and MLA templates; 
quarterly joint weeks of action.</li></ul></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-8077-97e5-e81b779048e3" class=""><strong>Result metric.</strong> ≥15–20% reduction in duplicate seizures; ≥2× increase in actionable inbound/outbound alerts; shorter MLA turnaround.</p></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-800c-8be4-d25634ffa126"/></div><div style="display:contents" dir="auto"><h3 id="286c5e6f-95bd-80f3-bfe1-fa9f135b7224" class=""><strong>System closure: causal chain and success conditions</strong></h3></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80bd-99e0-ee5362c07dd6" class=""><strong>Causal chain.</strong></p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80da-9f3b-e6745bf798de" class="">Legal dispersion → ambiguous case qualification → slow/uneven sanctions → weak deterrence.</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-8026-a155-f918a68f3a7f" class="">Institutional fragmentation → multiple handoffs → long cycle times → low probability of punishment.</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-805a-b4b0-ca07da5dddb6" class="">Technology deficit → poor detection and evidence → low conviction and re-entry of goods.</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-803a-a34d-e2c6fa3669b1" class="">Partnership asymmetry → late/absent private data → slower removals and higher public cost.</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80a3-90bc-ca202b41c283" class="">International latency → missed upstream interdictions → persistent inflows.</p></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-8072-9c6c-e94cf56960ff" class=""><strong>Success conditions (MECE, mapped to KPIs).</strong></p></div><div style="display:contents" dir="auto"><ol type="1" id="286c5e6f-95bd-805c-9c0f-f8f79f36946d" class="numbered-list" start="1"><li><strong>Single owner &amp; 
unified statute</strong> → sanction certainty (variance ≤10%).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="286c5e6f-95bd-805b-97b5-f2ae06591ed6" class="numbered-list" start="2"><li><strong>NACA + case backbone</strong> → cycle time ≤45 days; referral conversion ≥70%.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="286c5e6f-95bd-80e2-9fff-cabf8b65a0fd" class="numbered-list" start="3"><li><strong>NT-CIP + serialisation</strong> → detection precision +50%; evidentiary loss −60%.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="286c5e6f-95bd-8056-a3aa-f5c87ba457fd" class="numbered-list" start="4"><li><strong>Enforceable PPPs</strong> → takedown ≤24 h; duplicated inspections −30%.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="286c5e6f-95bd-80b6-ac27-caebd19bdd62" class="numbered-list" start="5"><li><strong>Live ASEAN alerts</strong> → duplicate cross-border seizures −15–20%.</li></ol></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80ff-8a43-d021ad14ed01" class="">Together, these close the gap between <strong>activity</strong> and <strong>deterrence</strong>, turning episodic campaigns into a <strong>permanent, risk-managed governance system</strong>.</p></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-807d-a68b-cb3b7e0aa60d"/></div><div style="display:contents" dir="auto"><h2 id="286c5e6f-95bd-802b-a833-fda75ca25d8d" class=""><strong>9. Notes (optional)</strong></h2></div><div style="display:contents" dir="auto"><p id="286c5e6f-95bd-80c0-97b4-d18fee6b94da" class="">This section focuses on theoretical and empirical state functions. 
Private sector initiatives are cited only where they intersect with state policy instruments or cooperative frameworks.</p></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-8019-af59-fe4385f82343"/></div><div style="display:contents" dir="auto"><h2 id="286c5e6f-95bd-804f-901f-ce433219c730" class=""><strong>10. References (APA – International)</strong></h2></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-805a-8193-e25c6a3af8ce" class="bulleted-list"><li style="list-style-type:disc"><strong>OECD.</strong> (2025). <em>Mapping Global Trade in Fakes 2025: Global Trends and Enforcement Challenges.</em> Paris: OECD Publishing.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80f4-9bb7-eed9cec13cc8" class="bulleted-list"><li style="list-style-type:disc"><strong>EUIPO.</strong> (2025). <em>Joint OECD–EUIPO Report on Counterfeit and Pirated Goods 2025.</em> Alicante: EUIPO.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8018-ac52-d027add28d07" class="bulleted-list"><li style="list-style-type:disc"><strong>WIPO.</strong> (2024). <em>IP Facts and Figures 2024.</em> Geneva: World Intellectual Property Organization.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8065-ac97-ea2ce43fba28" class="bulleted-list"><li style="list-style-type:disc"><strong>Vietnam Ministry of Industry and Trade.</strong> (2025). <em>Market Management Annual Report 2024–2025.</em> Hanoi: MOIT.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8086-af9d-d6b554c691d5" class="bulleted-list"><li style="list-style-type:disc"><strong>Vietnam News.</strong> (2024, December 10). 
<em>Crackdown on counterfeits as authorities battle rising e-commerce fraud.</em> Hanoi: Vietnam News Agency.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-8088-b6c2-e02b351ab1e0" class="bulleted-list"><li style="list-style-type:disc"><strong>Reuters.</strong> (2025, May 30). <em>Vietnam seizes fake Rolex, Prada items in counterfeit crackdown.</em> London: Reuters.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80df-b544-cf75fc20f999" class="bulleted-list"><li style="list-style-type:disc"><strong>ASEAN Secretariat.</strong> (2024). <em>ASEAN IPR Action Plan 2025.</em> Jakarta: ASEAN Secretariat.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-80ba-8e1b-d8ff63d536ce" class="bulleted-list"><li style="list-style-type:disc"><strong>Nguyen, T. H.</strong> (2019). <em>Administrative Law in Vietnam: Governance and Reform.</em> Hanoi: National Political Publishing House.</li></ul></div><div style="display:contents" dir="auto"><ul id="286c5e6f-95bd-801b-8877-c4ceabf95357" class="bulleted-list"><li style="list-style-type:disc"><strong>Vu, M. L.</strong> (2021). <em>Public Management and Market Regulation in Transitional Economies.</em> Ho Chi Minh City: UEH Press.</li></ul></div><div style="display:contents" dir="auto"><hr id="286c5e6f-95bd-803d-a0d3-c85e9fd8b549"/></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
