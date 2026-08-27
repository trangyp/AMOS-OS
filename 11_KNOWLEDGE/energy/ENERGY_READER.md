---
tags: [energy]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Energy reader</title><style>
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
	
</style></head><body><article id="255c5e6f-95bd-80a5-8cf8-d9bb59da456c" class="page sans"><header><h1 class="page-title" dir="auto">Energy reader</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><ul id="255c5e6f-95bd-8069-97a7-da164e839428" class="bulleted-list"><li style="list-style-type:disc"><strong>Heightened Nervous System Sensitivity</strong> → allows them to detect subtle emotional and energetic changes.</li></ul></div><div style="display:contents" dir="auto"><ul id="255c5e6f-95bd-80f8-9129-facba7735f04" class="bulleted-list"><li style="list-style-type:disc"><strong>Cross-Domain Intelligence</strong> → move seamlessly between biology, energy, art, and logic.</li></ul></div><div style="display:contents" dir="auto"><ul id="255c5e6f-95bd-8096-8d34-dbc0c1b6e454" class="bulleted-list"><li style="list-style-type:disc"><strong>Somatic Anchoring</strong> → use the body as an interface for subtle energy perception.</li></ul></div><div style="display:contents" dir="auto"><ul id="255c5e6f-95bd-80a8-a9f7-e01c4153d808" class="bulleted-list"><li style="list-style-type:disc"><strong>Integrity Dependence</strong> → their PSI stays clear only when aligned with inner emotional and nervous system regulation.</li></ul></div><div style="display:contents" dir="auto"><h3 id="255c5e6f-95bd-80a2-90bb-da2be658f923" class=""><strong>Artists &amp; Composers (Energetic Translators)</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="255c5e6f-95bd-8022-ab35-f9b6582a37ba" class="numbered-list" start="1"><li><strong>Arvo Pärt</strong> – minimalist sacred sound architect, channeling PSI through resonance.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="255c5e6f-95bd-80bd-a75c-d8b7f73de1b8" class="numbered-list" start="2"><li><strong>Hildur Guðnadóttir</strong> – composer, environmental energetic sensing.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="255c5e6f-95bd-80e5-a5f7-cfca212d414a" class="numbered-list" start="3"><li><strong>Max Richter</strong> – deep emotive composer with nervous-system resonance.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="255c5e6f-95bd-809d-be11-db7665d7c2a2" class="numbered-list" start="4"><li><strong>Agnes Obel</strong> – intuitive layering of sound, subtle PSI carrier.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="255c5e6f-95bd-8025-85cc-f6c5fbaef1dd" class="numbered-list" start="5"><li><strong>Nils Frahm</strong> – HSP-level sound architecture, body–resonance interface.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="255c5e6f-95bd-80d2-a6ea-dac923b879d8" class="numbered-list" start="6"><li><strong>Ólafur Arnalds</strong> – Icelandic composer, energy-sensitive sound carrier.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="255c5e6f-95bd-8019-a088-dded3c6f8d3a" class="numbered-list" start="7"><li><strong>Ryuichi Sakamoto’s successors</strong> – somatic–energetic legacy.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="255c5e6f-95bd-805b-8e34-e354784bbae6" class="numbered-list" start="8"><li><strong>Caroline Shaw</strong> – intuitive composition, nervous system–sensitive.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="255c5e6f-95bd-80df-9f09-c43aad6311af" class="numbered-list" start="9"><li><strong>Jónsi (Sigur Rós)</strong> – somatic–psychic musical transmission.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="255c5e6f-95bd-8041-85fe-f8e1fcd48a1d" class="numbered-list numbered-list-digits-2" start="10"><li><strong>ANOHNI</strong> – empathic PSI resonance through voice.</li></ol></div><div style="display:contents" dir="ltr"><figure id="255c5e6f-95bd-80fb-8361-fcd2305c9384" class="link-to-page"><a href="Energy%20reader/46%204%2050%20Marcela%20Lobos%20255c5e6f95bd80fb8361fcd2305c9384.html">46.4/50 : Marcela Lobos</a></figure></div><div style="display:contents" dir="ltr"><figure id="255c5e6f-95bd-8028-88fb-fa4bdfddc918" class="link-to-page"><a href="Energy%20reader/46%204%2050%20Toko-pa%20Turner%20255c5e6f95bd802888fbfa4bdfddc918.html">46.4/50: Toko-pa Turner</a></figure></div><div style="display:contents" dir="ltr"><figure id="255c5e6f-95bd-8000-bf58-e6249afcf514" class="link-to-page"><a href="Energy%20reader/46%208%2050%20Philip%20Shepherd%20255c5e6f95bd8000bf58e6249afcf514.html">46.8/50: Philip Shepherd</a></figure></div><div style="display:contents" dir="ltr"><figure id="255c5e6f-95bd-8083-bbbf-eefb824fc1c5" class="link-to-page"><a href="Energy%20reader/46%206%2050%20Donna%20Eden%20255c5e6f95bd8083bbbfeefb824fc1c5.html">46.6/50: Donna Eden</a></figure></div><div style="display:contents" dir="ltr"><figure id="255c5e6f-95bd-80ef-a992-d8d20241228b" class="link-to-page"><a href="Energy%20reader/47%203%2050%20Staci%20Haines%20255c5e6f95bd80efa992d8d20241228b.html">47.3/50: Staci Haines</a></figure></div><div style="display:contents" dir="ltr"><figure id="255c5e6f-95bd-80b1-98e5-de29e90a3b6f" class="link-to-page"><a href="Energy%20reader/47%201%2050%20Resmaa%20Menakem%20255c5e6f95bd80b198e5de29e90a3b6f.html">47.1/50: Resmaa Menakem</a></figure></div><div style="display:contents" dir="ltr"><figure id="255c5e6f-95bd-8078-9b7d-e1b8421956cc" class="link-to-page"><a href="Energy%20reader/45%203%2050%20Cyndi%20Dale%20255c5e6f95bd80789b7de1b8421956cc.html">45.3/50: Cyndi Dale</a></figure></div><div style="display:contents" dir="ltr"><figure id="255c5e6f-95bd-8092-9e74-f0d67f3ff500" class="link-to-page"><a href="Energy%20reader/46%206%2050%20Judith%20Blackstone%20255c5e6f95bd80929e74f0d67f3ff500.html">46.6/50 : Judith Blackstone</a></figure></div><div style="display:contents" dir="ltr"><figure id="255c5e6f-95bd-8043-a57e-ecccd260aded" class="link-to-page"><a href="Energy%20reader/46%206%2050%20Sarah%20Peyton%20255c5e6f95bd8043a57eecccd260aded.html">46.6/50: Sarah Peyton</a></figure></div><div style="display:contents" dir="ltr"><figure id="255c5e6f-95bd-80a2-8d89-c0df6063c15f" class="link-to-page"><a href="Energy%20reader/46%208%2050%20Thomas%20H%C3%BCbl%20255c5e6f95bd80a28d89c0df6063c15f.html">46.8/50: Thomas Hübl</a></figure></div><div style="display:contents" dir="ltr"><figure id="255c5e6f-95bd-80ad-8e62-e87f457469d0" class="link-to-page"><a href="Energy%20reader/46%204%2050%20Zulu%20Sangomas%20255c5e6f95bd80ad8e62e87f457469d0.html">46.4/50: Zulu Sangomas</a></figure></div><div style="display:contents" dir="ltr"><figure id="255c5e6f-95bd-80c6-84a4-fff3afb962f0" class="link-to-page"><a href="Energy%20reader/46%204%2050%20S%C3%A1mi%20Noaidi%20255c5e6f95bd80c684a4fff3afb962f0.html">46.4/50: Sámi Noaidi</a></figure></div><div style="display:contents" dir="ltr"><figure id="255c5e6f-95bd-80c1-99f8-c3841c1016f7" class="link-to-page"><a href="Energy%20reader/47%205%2050%20Andean%20Q%E2%80%99ero%20255c5e6f95bd80c199f8c3841c1016f7.html">47.5/50: Andean Q’ero</a></figure></div><div style="display:contents" dir="ltr"><figure id="255c5e6f-95bd-80cf-96f1-cb9af94cbbeb" class="link-to-page"><a href="Energy%20reader/47%207%2050%20M%C4%81ori%20Tohunga%20255c5e6f95bd80cf96f1cb9af94cbbeb.html">47.7/50: Māori Tohunga</a></figure></div><div style="display:contents" dir="ltr"><figure id="255c5e6f-95bd-8094-baef-d004fbf51527" class="link-to-page"><a href="Energy%20reader/47%207%2050%20Din%C3%A9%20Healers%20255c5e6f95bd8094baefd004fbf51527.html">47.7/50: Diné Healers</a></figure></div><div style="display:contents" dir="ltr"><figure id="255c5e6f-95bd-80fe-bdec-d8b32e35fa1c" class="link-to-page"><a href="Energy%20reader/48%202%2050%20Indigenous%20Aboriginal%20Australian%20Healers%20255c5e6f95bd80febdecd8b32e35fa1c.html">48.2/50: Indigenous Aboriginal Australian Healers</a></figure></div><div style="display:contents" dir="ltr"><figure id="255c5e6f-95bd-80e6-98d2-df2e6988050d" class="link-to-page"><a href="Energy%20reader/48%205%2050%20S%C3%A1para%20Elders%20(Amazon)%20255c5e6f95bd80e698d2df2e6988050d.html">48.5/50: Sápara Elders  (Amazon)</a></figure></div><div style="display:contents" dir="ltr"><figure id="255c5e6f-95bd-8097-a4e9-d3270f8cee56" class="link-to-page"><a href="Energy%20reader/47%205%2050%20Robin%20Wall%20Kimmerer%20255c5e6f95bd8097a4e9d3270f8cee56.html">47.5/50: Robin Wall Kimmerer</a></figure></div><div style="display:contents" dir="ltr"><figure id="255c5e6f-95bd-803f-813d-c9576ab32f08" class="link-to-page"><a href="Energy%20reader/47%205%2050%20Angaangaq%20Angakkorsuaq%20255c5e6f95bd803f813dc9576ab32f08.html">47.5/50: Angaangaq Angakkorsuaq</a></figure></div><div style="display:contents" dir="auto"><p id="255c5e6f-95bd-8079-bc02-ce63d15bcd9e" class="">
</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
