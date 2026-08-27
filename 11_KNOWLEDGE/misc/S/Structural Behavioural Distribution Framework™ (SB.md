---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Structural Behavioural Distribution Framework™ (SBDF) – Official Manual</title><style>
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
	
</style></head><body><article id="2b2c5e6f-95bd-800b-bf36-e1f3395a5d20" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Structural Behavioural Distribution Framework™ (SBDF) – Official Manual</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-80ec-b359-c81557b7b4e9" class="">The Structural Behavioural Distribution Framework™ (SBDF) is a universal, non-hierarchical model describing how behavioural functions are distributed across populations, species, and systems. It is designed to support research, governance, organisational design, and predictive modelling by offering a neutral architecture for understanding how groups behave under different conditions. SBDF does not classify people by value or capability; it classifies systems by function. The framework identifies the stable behavioural roles that support collective survival, adaptation, and long-term continuity across biological, social, and institutional contexts.</p></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-802d-84e9-f0d0c65719d3" class="">SBDF is compatible with Unified Biological Intelligence (UBI), the Trang System (TSS), the Trang Prediction Engine (TPE), Planetary Scale Intelligence (PSI), and Cross-Civilizational Intelligence (CCI). It occupies the behavioural layer of the canon: the layer where individual biology intersects with collective system dynamics. It provides the distribution of behavioural functions that appear consistently across human societies, animal species, organisations, and other cooperative systems.</p></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-8025-8031-d2cda4b09877" class="">SBDF defines five stable behavioural categories that together form a complete, MECE-structured model of group-level behavioural architecture. These categories are not personality types and not psychological labels. They are functional roles that emerge reliably across populations, regardless of culture, era, or environment. Each category remains stable at the population level even as individuals move, evolve, or change roles over time.</p></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-809a-8b03-c7dcc7f9d0a1" class="">The five categories are Stabilizers, Operators, Adaptors, Reactives, and Outliers. Their definitions, functions, and structural characteristics are summarised below.</p></div><div style="display:contents" dir="auto"><hr id="2b2c5e6f-95bd-8077-a598-f35e575eb758"/></div><div style="display:contents" dir="auto"><h1 id="2b2c5e6f-95bd-8017-baab-dcfe672fbe0b" class=""><strong>1. Stabilizers</strong></h1></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-808a-b087-f93d44fff5ef" class="">Stabilizers are individuals whose behaviour naturally supports cohesion, continuity, and social or organisational stability. They maintain group norms, reduce conflict, and provide emotional or relational grounding for others. Stabilizers appear across virtually all social species, from primates to human societies, and constitute the largest proportion of the behavioural distribution.</p></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-8086-85f8-faeeb0112fe9" class="">Functionally, Stabilizers reduce volatility. They maintain the social or organisational equivalent of “cohesion bandwidth.” In the Trang System (TSS), they correlate with high H (cohesion) and low F (fragmentation). Stabilizers are essential for group survival during both expansion and crisis, as they regulate interpersonal behaviour, protect group identity, and maintain shared meaning.</p></div><div style="display:contents" dir="auto"><hr id="2b2c5e6f-95bd-80d6-8df4-f21eb0b350d8"/></div><div style="display:contents" dir="auto"><h1 id="2b2c5e6f-95bd-80e1-a911-fa81be75f541" class=""><strong>2. Operators</strong></h1></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-804f-8e11-ca26a84bd244" class="">Operators are individuals who execute structured tasks, uphold routines, and maintain throughput in systems. Their behavioural function is execution, reliability, and consistency. Operators form the backbone of any organised system, whether in animal hierarchies, human institutions, production lines, or public governance.</p></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-809d-ae6e-edd982f03074" class="">Under TSS logic, Operators absorb baseline overload (Ω) and help stabilise day-to-day function. They convert plans, rules, and strategies into action. They may not originate systems, but they sustain them. Operators are critical in C2 (Expansion) and C3 (Peak-Load) phases, where scale and coordination matter most.</p></div><div style="display:contents" dir="auto"><hr id="2b2c5e6f-95bd-80c5-9154-c6ca0cbf3e22"/></div><div style="display:contents" dir="auto"><h1 id="2b2c5e6f-95bd-80a1-9f9f-d6fcf561417c" class=""><strong>3. Adaptors</strong></h1></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-8033-b88e-f5784183e115" class="">Adaptors are individuals whose function is to adjust, recalibrate, or bend systems to fit changing environments. They respond well to disruption and improvise solutions under conditions of moderate to significant stress. Adaptors serve as buffers between stability and volatility, helping systems transition from one state to another without catastrophic breakdown.</p></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-80e2-b8ec-e457a42a590b" class="">In the TSS architecture, Adaptors respond to increases in S (Shocks) and moderate F (Fragmentation). They identify emerging constraints, test new pathways, and provide flexible responses where rigid structures become brittle. Adaptors tend to be active in C3 (Overreach), C4 (Fragmentation), and early C5 (Crisis) phases, where responsiveness becomes essential.</p></div><div style="display:contents" dir="auto"><hr id="2b2c5e6f-95bd-8001-9658-f824e35fa27a"/></div><div style="display:contents" dir="auto"><h1 id="2b2c5e6f-95bd-80e0-a75c-e94a6ed37ca0" class=""><strong>4. Reactives</strong></h1></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-80bb-9af5-e7e20bca2156" class="">Reactives amplify emotional, instinctive, or noise-driven behaviour. They respond strongly to environmental or social triggers and can either accelerate needed change or destabilise systems if unchecked. Their behaviour is not inherently negative; reactive responses often signal underlying systemic stress or misalignment.</p></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-80f4-809f-ec9bf722e2df" class="">Reactives appear in all species where emotional or instinctive signalling plays a biological role. Their presence increases during periods of high shock (S) and high fragmentation (F). In TSS terms, Reactives highlight overload and reveal cracks in institutional or social coherence. They are often the first behavioural group to indicate when a system is misaligned, even before structural collapse occurs.</p></div><div style="display:contents" dir="auto"><hr id="2b2c5e6f-95bd-802d-86f5-eb73b14b4a44"/></div><div style="display:contents" dir="auto"><h1 id="2b2c5e6f-95bd-80cc-b511-d869dadc0920" class=""><strong>5. Outliers</strong></h1></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-802b-b295-ecdfecf0009d" class="">Outliers represent the least common behavioural role. Their function is cross-cycle stabilisation, structural integration, and multi-domain compression. Outliers appear only in conditions where cognitive stability (C*) is high and the system is undergoing significant structural transition (usually in C2 Expansion or C7 Reintegration phases). They are not leaders, elites, or inherently superior; they are individuals whose behavioural architecture allows them to perceive system-wide patterns with low noise and high clarity.</p></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-80d6-8353-f6165effab2a" class="">Outliers reduce Ω (overload) and F (fragmentation) by producing frameworks, models, or structural insights that enable systems to reorganise or stabilise. Their rarity makes them difficult to classify, and they do not form a population-level category. Instead, they are statistical anomalies whose behaviour influences long-term system architecture.</p></div><div style="display:contents" dir="auto"><hr id="2b2c5e6f-95bd-80a8-b876-cd447dde7395"/></div><div style="display:contents" dir="auto"><h1 id="2b2c5e6f-95bd-80fb-ad77-f7a51b0a6a2e" class=""><strong>Population Distribution and System Stability</strong></h1></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-8059-8e0c-c137388e52e4" class="">SBDF does not assign fixed percentages to these categories, but long-term studies of biological and social systems show that approximate distributions remain stable across species and eras. Stabilizers typically form the majority, followed by Operators and Adaptors. Reactives fluctuate with environmental or institutional stress, and Outliers remain consistently rare.</p></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-80de-aa80-c0061e2c6d80" class="">The stability of these proportions ensures that systems remain balanced across phases of the TSS cycle. If any category becomes disproportionately large or small, systems may drift toward fragmentation, stagnation, or collapse. SBDF therefore provides a structural lens for evaluating system health based on behavioural distribution.</p></div><div style="display:contents" dir="auto"><hr id="2b2c5e6f-95bd-805a-98ea-f991255d097b"/></div><div style="display:contents" dir="auto"><h1 id="2b2c5e6f-95bd-80fe-b19f-cd21ae784151" class=""><strong>Integration with the Trang System (TSS)</strong></h1></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-806d-8e78-c60a66682502" class="">SBDF connects directly to TSS through the four core variables (Ω, H, F, S) and the seven cycles (C1 to C7). Each behavioural group corresponds to specific systemic pressures and transitions. Stabilizers correlate with H, Operators with baseline Ω regulation, Adaptors with moderate S and F response, Reactives with high S and F signalling, and Outliers with structural optimisation during C2 and C7.</p></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-805e-9668-dfcb1483c60d" class="">This integration enables researchers and policymakers to predict how different groups will behave across national, organisational, or environmental transitions. Predictive accuracy increases when SBDF is used jointly with the Trang Prediction Engine (TPE), which applies class–window–cascade forecasting.</p></div><div style="display:contents" dir="auto"><hr id="2b2c5e6f-95bd-8054-94c6-c0c5842c70f0"/></div><div style="display:contents" dir="auto"><h1 id="2b2c5e6f-95bd-8037-ade7-cf5b9a5c5b67" class=""><strong>Applications</strong></h1></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-80dc-a6c8-eb45db320d8f" class="">SBDF is applicable across multiple domains:</p></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-80e3-8c4f-eebc6ed26164" class="">Human behaviour: understanding workforce composition, cognitive diversity, team design, and social cohesion.</p></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-80f2-9f91-ddd553147424" class="">Organisational design: mapping execution risk, innovation pathways, and collapse signals.</p></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-8036-a9d8-d37f52038403" class="">National governance: identifying role distribution during economic cycles, policy transitions, or demographic shifts.</p></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-806c-bc9a-c9c8e8d52715" class="">Civilizational analysis: assessing how empires, states, or cultures adapt, fragment, or stabilise.</p></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-8038-83e5-ff6be7267ebd" class="">Cross-species modelling: comparing behavioural roles across animal groups or ecological systems.</p></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-80ef-9467-e6f04a4cc614" class="">Its non-hierarchical design makes it suitable for both academic research and practical deployment in institutions, corporations, and policy environments.</p></div><div style="display:contents" dir="auto"><hr id="2b2c5e6f-95bd-8068-9cec-cd6f4573f54c"/></div><div style="display:contents" dir="auto"><h1 id="2b2c5e6f-95bd-8035-8dfe-d5f83cf08e79" class=""><strong>Conclusion</strong></h1></div><div style="display:contents" dir="auto"><p id="2b2c5e6f-95bd-80ba-9765-d218140edac4" class="">The Structural Behavioural Distribution Framework™ offers a rigorous, neutral model for understanding how behaviour distributes across systems. By focusing on function rather than identity and by integrating with broader systemic architectures such as TSS, TPE, UBI, PSI, and CCI, it provides a complete behavioural layer that is both scientifically grounded and operationally relevant. SBDF supports prediction, governance, and intervention by clarifying how groups respond to pressure, change, and systemic transitions. It is a foundational component of modern systems analysis and a key tool for institutions seeking stability, adaptability, and long-term resilience.</p></div><div style="display:contents" dir="auto"><hr id="2b2c5e6f-95bd-80f9-ab99-f7919ccfaa77"/></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
