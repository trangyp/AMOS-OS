---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Fund Deployment Roadmap (Post-Transaction)</title><style>
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
}

@page {
	margin: 1in;
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
	justify-content: space-between;
}

.column {
	padding: 0 1em;
}

.column:first-child {
	padding-left: 0;
}

.column:last-child {
	padding-right: 0;
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
	
</style></head><body><article id="24ac5e6f-95bd-801c-baec-fb911aa07257" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Fund Deployment Roadmap (Post-Transaction)</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8062-9236-c673e10fe210" class=""><strong>0) Scope &amp; Principles</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8086-9b9f-f431ca765338" class="bulleted-list"><li style="list-style-type:disc"><strong>Objective:</strong> Convert gold proceeds into audited, scalable, humanitarian and infrastructure outcomes while preserving capital integrity and liquidity.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80f8-ac89-ea0b8842a1fd" class="bulleted-list"><li style="list-style-type:disc"><strong>Operating Axioms:</strong> Legality-first; anti-corruption by design; tranching with performance gates; measurability; reversibility; sovereign compatibility.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8047-bd92-f3ec46a1f031" class="bulleted-list"><li style="list-style-type:disc"><strong>Primary Use Domains (mutually exclusive, collectively exhaustive):</strong><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-8053-aa7c-d1c13ac0cc4c" class="numbered-list" start="1"><li>Governance &amp; Compliance</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-80b1-8cfc-e70869d36605" class="numbered-list" start="2"><li>Treasury &amp; Capital Structure</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-80b2-ac9b-e4160505f5c8" class="numbered-list" start="3"><li>Program Pillars (core spend)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-8048-88c4-cbc96e49af0b" class="numbered-list" start="4"><li>Geographic Strategy</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-80e8-a060-f69e8783b1e6" class="numbered-list" start="5"><li>Partner &amp; Vendor Ecosystem</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-80bb-80f3-c21052cf0ea0" class="numbered-list" start="6"><li>Procurement &amp; Controls</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-80c9-a66b-fab81817cdbe" class="numbered-list" start="7"><li>Risk, Audit &amp; Ethics</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-8035-acdd-d447505eb7da" class="numbered-list" start="8"><li>Monitoring, Evaluation &amp; Learning (MEL)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-8014-af71-ff877662c7c6" class="numbered-list" start="9"><li>Transparency &amp; Reporting</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-803c-bad1-cf2da888e872" class="numbered-list" start="10"><li>Exit, Continuity &amp; Return Strategy</li></ol></div></li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-806c-9c21-d1d8c98a2d90"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-800e-8776-c4379b6ff038" class=""><strong>1) Governance &amp; Compliance (Who decides; how it’s enforced)</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8055-914c-fcbe4297745f" class="bulleted-list"><li style="list-style-type:disc"><strong>Legal Vehicles:</strong><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8091-ba8c-f11ca141438a" class="bulleted-list"><li style="list-style-type:circle"><strong>Top-level Trust</strong> (e.g., Switzerland/Singapore) with irrevocable <strong>Use-of-Proceeds Charter</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80b2-90b0-d8e4950ed7b9" class="bulleted-list"><li style="list-style-type:circle"><strong>Program Subsidiaries/SPVs</strong> per country (nonprofit or hybrid, per law).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8013-baed-e0d133b1bd17" class="bulleted-list"><li style="list-style-type:disc"><strong>Org Structure (non-overlapping):</strong><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-806c-92f8-e4a8e571cbca" class="bulleted-list"><li style="list-style-type:circle"><strong>Board of Trustees</strong> (fiduciary, charter change only).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80ac-a1ed-e7c457263505" class="bulleted-list"><li style="list-style-type:circle"><strong>Investment Committee (IC)</strong> (treasury, hedging, reserves).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8032-9ce8-e6f0a1e1c498" class="bulleted-list"><li style="list-style-type:circle"><strong>Program Councils</strong> (Health, Education, Justice, Digital Integrity, R&amp;D).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80ef-b6c6-ebd1d5b6291c" class="bulleted-list"><li style="list-style-type:circle"><strong>Risk &amp; Audit Committee</strong> (independent; whistleblower channel).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8022-ba15-e5028127bb5b" class="bulleted-list"><li style="list-style-type:circle"><strong>Ethics &amp; Safeguards Panel</strong> (human subjects, privacy, AI safety).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8027-bd60-e6f0e21a1f11" class="bulleted-list"><li style="list-style-type:disc"><strong>Compliance:</strong> FATF AML/CFT, OECD responsible sourcing, UN/EU/OFAC sanctions, IFRS/IPSAS reporting, country-level charity &amp; data protection laws.</li></ul></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8040-9862-e326b9d53e3c" class=""><strong>Decision Flow (approvals &amp; gates)</strong></p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="24ac5e6f-95bd-80af-bace-e92a07c66b05" class="code code-wrap"><code class="language-Mermaid" style="white-space:pre-wrap;word-break:break-all">flowchart TB
  A[Program Proposal] --&gt; B[Program Council Review]
  B --&gt; C[Risk &amp; Audit Pre-Check]
  C --&gt; D[Ethics &amp; Safeguards Review]
  D --&gt; E[Investment Committee: Budget &amp; Cash Plan]
  E --&gt; F[Board of Trustees: Tranche Release]
  F --&gt; G[Disbursement &amp; Contracting]
  G --&gt; H[MEL: KPIs &amp; Evidence]
  H --&gt; I[Quarterly Audit &amp; Public Report]
  I --&gt;|Pass| J[Next Tranche]
  I --&gt;|Fail| K[Remediation/Stop]</code></pre></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80cb-a0c4-d2c300f9484c"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-80b3-8533-c915be8d43bb" class=""><strong>2) Treasury &amp; Capital Structure (How funds are held, protected, grown)</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80db-9115-e11334b3467d" class="bulleted-list"><li style="list-style-type:disc"><strong>Total Proceeds (illustrative):</strong> mark to LBMA on settlement; for planning, assume <strong>$32B</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80b4-b6db-f256be9bab62" class="bulleted-list"><li style="list-style-type:disc"><strong>Capital Stack (targets):</strong><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8092-b85f-f91e1e89a012" class="bulleted-list"><li style="list-style-type:circle"><strong>Liquidity Reserve (20–30%)</strong>: T-bills, AAA money funds, short-duration IG.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8006-b034-d86bac732398" class="bulleted-list"><li style="list-style-type:circle"><strong>Core Program Escrows (40–50%)</strong>: time-boxed, project-tied, milestone-released.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80c3-ab22-d17a37e61206" class="bulleted-list"><li style="list-style-type:circle"><strong>Strategic Endowment (10–20%)</strong>: diversified, low-volatility multi-asset.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-804d-97d6-e55c680d9635" class="bulleted-list"><li style="list-style-type:circle"><strong>Operating Buffer (3–5%)</strong>: 12–18 months runway.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-805c-b2aa-f031f61bb510" class="bulleted-list"><li style="list-style-type:disc"><strong>Hedging:</strong> FX and interest-rate hedges aligned to deployment currencies and timelines.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8040-86d5-e5d9dbebac0c" class="bulleted-list"><li style="list-style-type:disc"><strong>Contra-party Risk:</strong> Tier-1 banks only; concentration caps; daily exposure dashboard.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8042-b09d-ca8c552aeba0" class="bulleted-list"><li style="list-style-type:disc"><strong>Cash Cadence:</strong> Weekly disbursement windows; no ad-hoc releases outside calendar.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80eb-b907-dd1608e1081b"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8073-b025-e2160800c519" class=""><strong>3) Program Pillars (Core Spend; MECE buckets with % allocations &amp; KPIs)</strong></h2></div><div style="display:contents" dir="auto"><blockquote id="24ac5e6f-95bd-80cb-a66b-c5ec3b3c90f6" class="">Illustrative portfolio (sum 100%). Each pillar runs<div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-803f-9492-ffe009f7eb7c" class=""><strong>pilot → scale → nationalization</strong></p></div></blockquote></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-80b4-886f-cd996c28e261" class=""><strong>3.1 Public Health &amp; Trauma Resolution —</strong></h3></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-80f4-acba-fc59fc3e5a6b" class=""><strong>20%</strong></h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8055-a794-f9f8e5315728" class="bulleted-list"><li style="list-style-type:disc"><strong>CapEx:</strong> Clinics, training centers, secure data infra.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8039-bde9-f6c2e89de930" class="bulleted-list"><li style="list-style-type:disc"><strong>OpEx:</strong> Clinicians, protocols, outreach, subsidies.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80bd-beaa-d0d4dfca1ef1" class="bulleted-list"><li style="list-style-type:disc"><strong>KPIs:</strong> Access ≤30 days; symptom reduction (validated scales); return-to-work %; relapse &lt;10% @12m.</li></ul></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-8082-b517-ebcc4db6ccba" class=""><strong>3.2 Education &amp; Human Performance —</strong></h3></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-80df-8308-e50ad35c60e2" class=""><strong>15%</strong></h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-804d-b918-c45b63e1c20f" class="bulleted-list"><li style="list-style-type:disc"><strong>CapEx:</strong> Curriculum design, digital platforms, labs.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-801a-96d6-f158999418df" class="bulleted-list"><li style="list-style-type:disc"><strong>OpEx:</strong> Teacher upskilling, stipends, evaluation.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80c1-bd94-f185b401e9ac" class="bulleted-list"><li style="list-style-type:disc"><strong>KPIs:</strong> Literacy/numeracy gains; completion rates; time-to-competency; employer satisfaction.</li></ul></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-80d3-bf61-cec2d6d8e1f4" class=""><strong>3.3 Justice &amp; Governance Reform —</strong></h3></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-807e-96d2-f821b2c03e32" class=""><strong>10%</strong></h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8081-bada-efa0c12e8b7c" class="bulleted-list"><li style="list-style-type:disc"><strong>CapEx:</strong> Case management systems, restorative justice facilities.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80b5-8619-f614112863ae" class="bulleted-list"><li style="list-style-type:disc"><strong>OpEx:</strong> Legal aid, mediation, training.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8028-9b1f-c69756d1fc5c" class="bulleted-list"><li style="list-style-type:disc"><strong>KPIs:</strong> Case time -30%; recidivism -40% @24m; victim satisfaction; cost per resolved case.</li></ul></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-804b-8707-d9356c4e9365" class=""><strong>3.4 Digital Integrity &amp; NeuroSyncAI™ —</strong></h3></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-80bc-965b-fc14105221a0" class=""><strong>15%</strong></h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8064-ad8f-dee30fbbdb33" class="bulleted-list"><li style="list-style-type:disc"><strong>CapEx:</strong> Integrity interfaces, secure hardware modules, audits.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8086-85ea-faab36b429e9" class="bulleted-list"><li style="list-style-type:disc"><strong>OpEx:</strong> Model ops, red-teaming, certification.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8014-a75e-d8baaa9af6e1" class="bulleted-list"><li style="list-style-type:disc"><strong>KPIs:</strong> Policy compliance; breach rate; audit pass rate; citizen trust indices.</li></ul></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-808a-86cb-f4fe3eb9031a" class=""><strong>3.5 Economic Infrastructure &amp; SMEs —</strong></h3></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-8025-8a85-c79e264e4f62" class=""><strong>15%</strong></h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80b8-a04d-eb2a0dcc5cd1" class="bulleted-list"><li style="list-style-type:disc"><strong>CapEx:</strong> Industrial parks, logistics, energy upgrades.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80cc-8e44-e010c122a9c5" class="bulleted-list"><li style="list-style-type:disc"><strong>OpEx:</strong> SME grants, credit guarantees.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-807e-a809-db195fc6ca13" class="bulleted-list"><li style="list-style-type:disc"><strong>KPIs:</strong> Jobs created; SME survival @24m; export growth; energy efficiency gains.</li></ul></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-8019-b0c8-fd81881ccf77" class=""><strong>3.6 R&amp;D &amp; Standards (UBI, biometrics, safety) —</strong></h3></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-80e0-9660-c8170df997b3" class=""><strong>10%</strong></h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80ad-b167-c1092b74a9a6" class="bulleted-list"><li style="list-style-type:disc"><strong>CapEx/OpEx:</strong> Research labs, trials, standards bodies participation.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8026-a395-ca1a70acb387" class="bulleted-list"><li style="list-style-type:disc"><strong>KPIs:</strong> Peer-reviewed outputs; standards authored/adopted; regulatory approvals.</li></ul></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-8093-bd3a-f075eaaeccb8" class=""><strong>3.7 Climate &amp; Resilience —</strong></h3></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-807a-8ae9-c9511e36a2cb" class=""><strong>10%</strong></h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-808d-a3f5-e1a8b687ea47" class="bulleted-list"><li style="list-style-type:disc"><strong>CapEx:</strong> Resilient housing, water systems, renewables.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80a9-9c49-cb0dd6d9473e" class="bulleted-list"><li style="list-style-type:disc"><strong>OpEx:</strong> Maintenance, training, insurance pools.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8059-b96a-f8a68aa9d25f" class="bulleted-list"><li style="list-style-type:disc"><strong>KPIs:</strong> Emissions reduced; resilience indices; avoided loss metrics.</li></ul></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-8086-8406-c68d4587caec" class=""><strong>3.8 Operations &amp; Shared Services —</strong></h3></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-80c2-bd9e-d12f46f25563" class=""><strong>5%</strong></h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80f0-8352-d9c411f2b586" class="bulleted-list"><li style="list-style-type:disc"><strong>OpEx:</strong> HR, finance, legal, cyber, comms; ≤8% cap overhead.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80c6-8ca9-c46a5d47e0be" class="bulleted-list"><li style="list-style-type:disc"><strong>KPIs:</strong> Overhead ratio; SLA adherence; audit findings = 0 material.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80f5-89cc-e19c69b831e1"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-80bb-ba08-c6b61cb7d395" class=""><strong>4) Geographic Strategy (Where and why)</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-803e-af16-d2c4523c985a" class="bulleted-list"><li style="list-style-type:disc"><strong>Tiering:</strong><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80d4-975a-d0a68f06672c" class="bulleted-list"><li style="list-style-type:circle"><strong>Tier-1 Hubs (Pilot):</strong> Regulatory maturity, low corruption, strong partners (e.g., CH/SG/EU hub).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-802a-b135-c09c5ddab362" class="bulleted-list"><li style="list-style-type:circle"><strong>Tier-2 Scale:</strong> Emerging markets with reform appetite and MOUs in place.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-808f-84f7-f94b81220439" class="bulleted-list"><li style="list-style-type:circle"><strong>Tier-3 Frontier:</strong> Humanitarian focus with enhanced safeguards.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-804e-818a-e4bb5051f409" class="bulleted-list"><li style="list-style-type:disc"><strong>Selection Criteria:</strong> Rule of law, co-funding, data protection, need index, partner depth.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8016-b368-dd5656983d91" class="bulleted-list"><li style="list-style-type:disc"><strong>MOUs &amp; Co-Financing:</strong> Blend with development banks, ministries, and reputable NGOs.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-807a-958e-d8dc5a6ee113"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-80a4-b58a-e49f6ec37071" class=""><strong>5) Partner &amp; Vendor Ecosystem (Who executes)</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80d5-bf95-c4063dbcfcf2" class="bulleted-list"><li style="list-style-type:disc"><strong>Partner Categories (non-overlapping):</strong><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8023-922a-fe7c401250be" class="bulleted-list"><li style="list-style-type:circle">Public sector (ministries, municipalities)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8083-aeab-ed5c83562310" class="bulleted-list"><li style="list-style-type:circle">Multilaterals/DFIs (World Bank, regional dev banks)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80d0-9019-d11c1b7932bc" class="bulleted-list"><li style="list-style-type:circle">Academia &amp; research labs</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80df-99da-d355c9e9174f" class="bulleted-list"><li style="list-style-type:circle">NGOs &amp; community orgs</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8059-b26f-f751d8b6b0c2" class="bulleted-list"><li style="list-style-type:circle">Private vendors (audited, competitive)</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8046-8f8d-d2e2580ea13e" class="bulleted-list"><li style="list-style-type:disc"><strong>Onboarding:</strong> RfP, conflict-check, past-performance scoring, sanctions screening, site visits.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80da-8e49-c09de0ae08aa" class="bulleted-list"><li style="list-style-type:disc"><strong>Performance Contracts:</strong> Output &amp; outcome-based; clawback clauses; escrowed milestones.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-807c-8598-ed54439d2dff"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8058-9c9a-c66575f40d99" class=""><strong>6) Procurement &amp; Financial Controls (How money moves)</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8000-b51a-c3f263ac1821" class="bulleted-list"><li style="list-style-type:disc"><strong>Procurement:</strong> Competitive tenders; three-quote rule; framework agreements for critical items.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-808f-8f59-f98b2a719bc2" class="bulleted-list"><li style="list-style-type:disc"><strong>Approvals:</strong> Dual-signature policy; amount-based authority matrix; pre-commitment budget control.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8039-a32a-f7217c7413ae" class="bulleted-list"><li style="list-style-type:disc"><strong>Payments:</strong> Program escrow → vendor via verified invoices; no cash; country banking compliance.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8094-8364-dad83be686d8" class="bulleted-list"><li style="list-style-type:disc"><strong>Inventory &amp; Asset Registry:</strong> Barcode/RFID; periodic physical reconciliations.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8079-873a-cf7cb3fa13d9" class="bulleted-list"><li style="list-style-type:disc"><strong>Data &amp; Privacy:</strong> PII minimization; lawful basis by country; external DPO oversight.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80ed-bb11-fba07a1bd8aa"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8020-9d2e-ee7803ca4968" class=""><strong>7) Risk, Audit &amp; Ethics (What can go wrong; how it’s prevented)</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8035-981c-d81e87da5329" class="bulleted-list"><li style="list-style-type:disc"><strong>Risk Types (MECE):</strong> Legal/regulatory, financial, operational, cyber, reputational, ESG, partner, FX/market.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8036-b124-ef4b57989b8a" class="bulleted-list"><li style="list-style-type:disc"><strong>Controls:</strong> Pre-mortems; KRIs; quarterly internal audit; annual Big-4 external audit.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8019-9e77-c18449bbe6f1" class="bulleted-list"><li style="list-style-type:disc"><strong>Ethics:</strong> Human subjects review; informed consent; grievance redress; whistleblower hotline.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80ae-9943-e2376026db2f" class="bulleted-list"><li style="list-style-type:disc"><strong>Sanctions/AML:</strong> Continuous screening; automatic vendor holds upon watchlist hits.</li></ul></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-80fd-8393-e1d247c71635" class=""><strong>Risk Matrix (abbrev.)</strong></p></div><div style="display:contents" dir="ltr"><table id="24ac5e6f-95bd-8045-a39f-f8c73cf159dd" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-80f4-b0f9-f3bcfb1d9545"><th id="W^Y:" class="simple-table-header-color simple-table-header"><strong>Risk</strong></th><th id="wEoH" class="simple-table-header-color simple-table-header"><strong>Likelihood</strong></th><th id="ZXMh" class="simple-table-header-color simple-table-header"><strong>Impact</strong></th><th id="pM&gt;v" class="simple-table-header-color simple-table-header"><strong>Control</strong></th><th id="~|;l" class="simple-table-header-color simple-table-header"><strong>Gate</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-80fe-a1b2-d18bfd55360b"><td id="W^Y:" class="">Fraud</td><td id="wEoH" class="">Med</td><td id="ZXMh" class="">High</td><td id="pM&gt;v" class="">Segregation of duties; anomaly detection</td><td id="~|;l" class="">Pre-payment</td></tr></div><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-8034-ac4f-c02b0454eaf8"><td id="W^Y:" class="">Scope creep</td><td id="wEoH" class="">Med</td><td id="ZXMh" class="">Med</td><td id="pM&gt;v" class="">Change control board</td><td id="~|;l" class="">Budget release</td></tr></div><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-8089-b535-e8fe61df3d6d"><td id="W^Y:" class="">Data breach</td><td id="wEoH" class="">Low</td><td id="ZXMh" class="">High</td><td id="pM&gt;v" class="">Encryption; zero-trust; audits</td><td id="~|;l" class="">Go-live</td></tr></div><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-80b2-9dfd-c8a40196660c"><td id="W^Y:" class="">FX shock</td><td id="wEoH" class="">Med</td><td id="ZXMh" class="">Med</td><td id="pM&gt;v" class="">Hedges; currency baskets</td><td id="~|;l" class="">IC review</td></tr></div><div style="display:contents" dir="ltr"><tr id="24ac5e6f-95bd-8065-be07-effd289cd3d1"><td id="W^Y:" class="">Political change</td><td id="wEoH" class="">Med</td><td id="ZXMh" class="">Med</td><td id="pM&gt;v" class="">MOUs; exit clauses</td><td id="~|;l" class="">Country entry</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-809a-9885-c569d91b0726"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-80d2-bcd8-d0d745441348" class=""><strong>8) Monitoring, Evaluation &amp; Learning (MEL)</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80cf-9b1b-edf8656d9133" class="bulleted-list"><li style="list-style-type:disc"><strong>Framework:</strong> Inputs → Outputs → Outcomes → Impact; counterfactual baselines; external evaluations.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8049-bca8-e98c789d1da0" class="bulleted-list"><li style="list-style-type:disc"><strong>Cadence:</strong> Monthly ops reviews; quarterly KPI reports; annual impact evaluations.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80db-83ca-d2c27b6f3d0d" class="bulleted-list"><li style="list-style-type:disc"><strong>Data Quality:</strong> Independent verification; sampling plans; public data catalog (de-identified).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-804c-8405-fa81bf4718ac" class="bulleted-list"><li style="list-style-type:disc"><strong>Adaptive Management:</strong> Underperforming programs pause/re-scope; successful pilots scale.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80cf-a36b-d1f2fa9ec477"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-800d-a8ca-fcec43540b91" class=""><strong>9) Transparency &amp; Reporting (Trust by design)</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-802b-9c4a-dfd14cf297fa" class="bulleted-list"><li style="list-style-type:disc"><strong>Public Portal:</strong> Projects, budgets, KPIs, audits, procurement awards.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-809f-818e-ee1ead5e303d" class="bulleted-list"><li style="list-style-type:disc"><strong>Disclosures:</strong> Quarterly financials; annual audited statements; incident reports.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8094-9531-c9628e0a415f" class="bulleted-list"><li style="list-style-type:disc"><strong>Stakeholder Comms:</strong> Community briefings; regulator updates; investor notes.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-8046-b09c-cb0cf4941f92"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8042-8da7-fae16827fb61" class=""><strong>10) Exit, Continuity &amp; Return Strategy</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8040-a89b-f6d59f2a45f9" class="bulleted-list"><li style="list-style-type:disc"><strong>Sustainability:</strong> Local revenue models, government adoption, or multilateral take-over.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-802a-9a56-e7971f70ded9" class="bulleted-list"><li style="list-style-type:disc"><strong>Endowment Policy:</strong> 3–4% payout target; inflation-hedged; permanent capital.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8065-820b-ec2412de6322" class="bulleted-list"><li style="list-style-type:disc"><strong>Contingencies:</strong> Pandemic/war protocols; rapid reallocation rules; data &amp; asset protection.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80b8-aa62-f040d6fa7c28" class="bulleted-list"><li style="list-style-type:disc"><strong>Legacy:</strong> Open standards; know-how transfer; local capacity built into all contracts.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-802a-b974-ea073331c3d9"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8078-8a88-d62559008d9a" class=""><strong>11) Tranche Plan &amp; Timeline (Illustrative Gantt)</strong></h2></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="24ac5e6f-95bd-8046-a6e0-dab4cc750dc9" class="code code-wrap"><code class="language-Mermaid" style="white-space:pre-wrap;word-break:break-all">gantt
  dateFormat  YYYY-MM-DD
  title 24-Month Deployment (Pilot → Scale → Nationalization)
  section Setup
  Legal Vehicles &amp; Governance     :done, s1, 2025-08-15, 30d
  Treasury &amp; Risk Framework       :active, s2, 2025-09-15, 20d
  Country MOUs &amp; Partner Onboarding: s3, 2025-10-05, 40d
  section Tranche 1 (Pilots)
  Health &amp; Education Pilots (3 hubs) : t1, 2025-11-15, 120d
  Justice &amp; Digital Integrity Pilots : t2, 2025-11-15, 120d
  MEL Baselines &amp; First Reviews      : t3, 2026-03-15, 20d
  section Tranche 2 (Scale)
  Scale to 6–8 Regions               : t4, 2026-04-01, 180d
  Infra &amp; SME Programs               : t5, 2026-04-01, 180d
  External Audit &amp; Adjustments       : t6, 2026-10-01, 30d
  section Tranche 3 (Nationalize)
  National Programs &amp; Handover       : t7, 2026-11-01, 210d
  Endowment Stabilization &amp; Exit     : t8, 2026-11-01, 210d</code></pre></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80b2-bfd3-fd11806ed1c4"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-80ea-9801-c9e0ae1f4b96" class=""><strong>12) Budget Envelope (Illustrative split on $32B)</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80ce-893d-e36fc94650e2" class="bulleted-list"><li style="list-style-type:disc"><strong>Liquidity Reserve:</strong> 25% → $8.0B</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8074-b1fb-e0f131f02e45" class="bulleted-list"><li style="list-style-type:disc"><strong>Program Escrows:</strong> 45% → $14.4B</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8080-beb1-d3e3a349112c" class="bulleted-list"><li style="list-style-type:disc"><strong>Strategic Endowment:</strong> 20% → $6.4B</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80d7-adc6-d3734cba5e99" class="bulleted-list"><li style="list-style-type:disc"><strong>Operating Buffer:</strong> 5% → $1.6B</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8061-9289-d367cbb59217" class="bulleted-list"><li style="list-style-type:disc"><strong>Contingency/Price Slippage:</strong> 5% → $1.6B</li></ul></div><div style="display:contents" dir="auto"><blockquote id="24ac5e6f-95bd-806d-8a7d-ec6e7f78bc65" class="">Gatekeeping:</blockquote></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80af-80b5-c507c7a9e6e8"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-80e1-b2c5-f29ee2200262" class=""><strong>13) One-Page Use-of-Proceeds Statement (for banks/regulators)</strong></h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80f5-815f-eba022208c90" class="bulleted-list"><li style="list-style-type:disc">Proceeds are <strong>ring-fenced</strong> in a trust with a <strong>charter-bound use taxonomy</strong> (health, education, justice, digital integrity, SME, climate, R&amp;D).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80c8-a3ae-d3d6e9376ff0" class="bulleted-list"><li style="list-style-type:disc">Disbursements occur <strong>only</strong> via program escrows tied to <strong>auditable milestones</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8023-8670-cfde18424520" class="bulleted-list"><li style="list-style-type:disc">Funds are protected by <strong>Tier-1 custody</strong>, <strong>diversified reserves</strong>, <strong>FX hedging</strong>, and <strong>independent audits</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-806b-9871-d242a396053c" class="bulleted-list"><li style="list-style-type:disc">Transparency is real-time; ethics and human rights safeguards are embedded by design.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-803a-ab7a-f85827127075"/></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
