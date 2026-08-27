---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Public messaging </title><style>
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
	
</style></head><body><article id="269c5e6f-95bd-806d-8bf9-ed7e6613665e" class="page sans"><header><h1 class="page-title" dir="auto">Public messaging </h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-80c2-b7a0-c4f89972433e"/></div><div style="display:contents" dir="auto"><h1 id="269c5e6f-95bd-80db-afb9-c22ac259f693" class=""><strong>Making the Signal Economy Relatable</strong></h1></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-80a3-91df-d32d8ffd10e2" class=""><strong>The Simple Explanation</strong></h3></div><div style="display:contents" dir="auto"><p id="269c5e6f-95bd-8007-b848-f787efdce8de" class="">Think of it like a <strong>universal signal ledger</strong> for everything — from your Apple Watch to global financial markets. Instead of companies, insurers, or governments using your signals without consent, the <strong>Signal Economy™</strong> makes every action — biological, digital, or systemic — logged, consented, and trusted.</p></div><div style="display:contents" dir="auto"><p id="269c5e6f-95bd-80d1-afd1-cb00e73541c6" class="">It’s not just about data or money. 
At the heart of tomorrow’s economy is <strong>signal</strong>: the patterns of life itself.</p></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-802a-a733-c070491d897a"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-8070-979a-e49be3713879" class=""><strong>Relatable Anecdotes &amp; Examples</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-80c1-ac79-e349be5672c0" class="numbered-list" start="1"><li><strong>The Watch That Builds Trust</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8081-8f3f-ff748f23499e" class="bulleted-list"><li style="list-style-type:disc">Today: Your Apple Watch tracks your heartbeat, stress, and sleep, but those signals get lost in fragmented apps.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8071-af46-d2a431065982" class="bulleted-list"><li style="list-style-type:disc">Tomorrow: Each signal is logged in the Signal Economy. Your <strong>NeuroSignal™ Agent</strong> interprets it, adds consent, and makes it usable for health insurers or employers — but <em>only if you approve</em>.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8021-ab5f-c557062389e2" class="bulleted-list"><li style="list-style-type:disc">Why it matters: You stay in control, and your health signals become an asset, not an extraction.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-805c-b744-c58b06fb5752" class="numbered-list" start="2"><li><strong>The Coffee That Proves Itself</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8094-93df-f4eb27976b3f" class="bulleted-list"><li style="list-style-type:disc">Today: “Fair trade” labels are inconsistent. 
You can’t verify if farmers were truly paid fairly.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80d6-987b-fd3ace6df72f" class="bulleted-list"><li style="list-style-type:disc">Tomorrow: Every signal in the coffee chain — from the farm to the roaster — is logged in the <strong>Signal Economy with PCI governance</strong>. 
Consent is verified at each step, so when you drink it, you know every actor agreed.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80ce-b627-ff56a5c8d51d" class="bulleted-list"><li style="list-style-type:disc">Why it matters: Ethical sourcing stops being a marketing slogan and becomes a verifiable reality.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-80ff-8237-d9b4845c38b7" class="numbered-list" start="3"><li><strong>The City That Listens</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80e2-9c7a-ccd28e04dee1" class="bulleted-list"><li style="list-style-type:disc">Today: Cities roll out traffic sensors or cameras without asking you how your data should be used.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-804b-a9cc-eb7f5f38d9d7" class="bulleted-list"><li style="list-style-type:disc">Tomorrow: Signals from your commute feed into the ledger, but PCI ensures you consented: “Okay for traffic optimisation, not for advertising.”</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-802a-8caa-c8fd728714d8" class="bulleted-list"><li style="list-style-type:disc">Why it matters: Urban systems improve without exploiting residents.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-8046-9310-eae9871ee947" class="numbered-list" start="4"><li><strong>The Insurance Policy That Adapts to You</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-806c-a51b-cbdc726ccfb4" class="bulleted-list"><li style="list-style-type:disc">Today: Insurance premiums are based on blunt averages and guesswork.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-809e-9a97-e065f00a4e41" class="bulleted-list"><li style="list-style-type:disc">Tomorrow: Your <strong>Trust &amp; 
Consent Index</strong> (built on NeuroSignal™ + PCI) shows you’re resilient, low-risk, and consistent. That gets you lower premiums instantly.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80df-8f8f-ca18d427e027" class="bulleted-list"><li style="list-style-type:disc">Why it matters: Signals reward individuals fairly, instead of hiding behind opaque actuarial tables.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-8059-ad68-d4eec1159970"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-802d-8b19-f38f68932cec" class=""><strong>Key Benefits in Simple Terms</strong></h3></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8089-87cf-d86b0ed5c229" class="bulleted-list"><li style="list-style-type:disc"><strong>For Individuals</strong> → “Your signals are respected, not exploited. 
You see value, not noise.”</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8016-bd94-e86fcad130d1" class="bulleted-list"><li style="list-style-type:disc"><strong>For Businesses</strong> → “Trust and consent become the new competitive advantage.”</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80c2-9fdc-e27434d5609b" class="bulleted-list"><li style="list-style-type:disc"><strong>For Communities</strong> → “Decisions are made with consent, not top-down control.”</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80cc-9e10-caab5dccbbdb" class="bulleted-list"><li style="list-style-type:disc"><strong>For the Planet</strong> → “Signals coordinate global action on energy, climate, and finance without drift.”</li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-8074-b828-e9251557db06"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-807d-8581-da2de70aaa06" class=""><strong>The Bottom Line</strong></h3></div><div style="display:contents" dir="auto"><p id="269c5e6f-95bd-80b6-aa02-e001e987854a" class="">The <strong>Signal Economy™</strong> is the foundation for a world where:</p></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-800d-b0a2-cbcbf197d049" class="bulleted-list"><li style="list-style-type:disc"><strong>NeuroSignal™</strong> grounds every action in biology (real human stability).</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80df-a8b8-df90485f19e5" class="bulleted-list"><li style="list-style-type:disc"><strong>PCI</strong> ensures every signal is consented, verified, and auditable.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8098-b00d-dbb87f50162f" class="bulleted-list"><li style="list-style-type:disc"><strong>Signal Economy™</strong> becomes the universal ledger of trust — across health, finance, energy, 
and governance.</li></ul></div><div style="display:contents" dir="auto"><p id="269c5e6f-95bd-805b-a6a6-ce1bbc1b59b2" class="">It’s not about controlling technology. It’s about technology that finally respects <strong>your control, your consent, and your signals</strong>.</p></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-8096-b01f-c1ad13112d94"/></div><div style="display:contents" dir="auto"><h1 id="269c5e6f-95bd-8060-8bd2-de3537b2304d" class=""><strong>The Trust &amp; Consent Index Stack</strong></h1></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-80b6-8e48-dfe6e59d6b96" class=""><strong>1. Personal Trust Index (PTI)</strong></h3></div><div style="display:contents" dir="auto"><p id="269c5e6f-95bd-8093-abc6-cf0e4d43f786" class=""><strong>What it is:</strong> A score that reflects how stable, resilient, and trustworthy an individual’s signals are.</p></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8087-a02b-d09a928f5a1c" class="bulleted-list"><li style="list-style-type:disc"><strong>How it works:</strong> Based on wearables (Apple Watch, Oura, etc.) + NeuroSignal™ Agent readings. Tracks Biological Resilience Score™ (BRS), emotional stability, and how consistently someone manages their consent.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8086-8531-d44c9edb9878" class="bulleted-list"><li style="list-style-type:disc"><strong>Example:</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-808e-9adc-c80de09b6e30" class="bulleted-list"><li style="list-style-type:circle">Today: Two people apply for health insurance. Both look healthy on paper.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80b3-88cf-d6ef0b06db1c" class="bulleted-list"><li style="list-style-type:circle">Tomorrow: PTI shows that one person has high nervous system resilience and consistent stress recovery, while the other shows instability. 
Insurers price premiums fairly — not on averages, but on real signals.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80c6-afda-f8d0d0515ede" class="bulleted-list"><li style="list-style-type:disc"><strong>Why it matters:</strong> Individuals gain leverage. Your PTI is portable and improves as you train your nervous system, like a “fitness + trust passport.”</li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-8062-b822-cefd0916b7ba"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-8011-8045-e4c2089f241e" class=""><strong>2. Consent Integrity Index (CII)</strong></h3></div><div style="display:contents" dir="auto"><p id="269c5e6f-95bd-80d2-879d-cdd4ff68e912" class=""><strong>What it is:</strong> A benchmark for how companies handle user consent.</p></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-809a-943d-de48c1119878" class="bulleted-list"><li style="list-style-type:disc"><strong>How it works:</strong> PCI records how often a company honours revocations, avoids manipulation (dark patterns), and logs data access transparently.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8092-9e00-c2d1f04150b5" class="bulleted-list"><li style="list-style-type:disc"><strong>Example:</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80b6-b85c-d2c6053aa5a8" class="bulleted-list"><li style="list-style-type:circle">Today: A streaming app buries your “unsubscribe” button.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8058-9939-f75626132c31" class="bulleted-list"><li style="list-style-type:circle">Tomorrow: Its CII drops because PCI shows low consent integrity. Consumers see it, regulators flag it, and investors hesitate. 
A competitor with higher CII scores earns more trust — and more business.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-800a-ab30-c9762ee1d315" class="bulleted-list"><li style="list-style-type:disc"><strong>Why it matters:</strong> Companies can’t hide. Consent becomes a measurable competitive advantage.</li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-8068-8aef-fb6cb69186c9"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-80d7-9c04-fe7d2b9d8553" class=""><strong>3. 
Organisational Trust Index (OTI)</strong></h3></div><div style="display:contents" dir="auto"><p id="269c5e6f-95bd-8060-833f-f40a0e0b5f19" class=""><strong>What it is:</strong> A trust score for whole organisations, combining employee, customer, and system signals.</p></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-809d-b413-e431b138904d" class="bulleted-list"><li style="list-style-type:disc"><strong>How it works:</strong> Aggregates PTI (employees), CII (consent practices), and systemic alignment (supply chain, governance).</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8064-bdf6-cc1ddc8a6b04" class="bulleted-list"><li style="list-style-type:disc"><strong>Example:</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8011-9c9a-d6eb7a6169af" class="bulleted-list"><li style="list-style-type:circle">Today: A corporation publishes a glossy ESG report, but it’s unverifiable.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8049-a2c0-d9d3b80e8b8b" class="bulleted-list"><li style="list-style-type:circle">Tomorrow: OTI shows how resilient their workforce is, how ethically they manage consent, and whether their operations align with real signals (energy, carbon, talent).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8087-bc4b-d07f88a63923" class="bulleted-list"><li style="list-style-type:disc"><strong>Why it matters:</strong> Investors and banks can instantly see whether a company deserves financing — no greenwashing, no fake reputations.</li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-807b-8e2e-fc4cc49b64e3"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-80b0-8772-dbabd87719e5" class=""><strong>4. 
Planetary Consent Index (PCI Score)</strong></h3></div><div style="display:contents" dir="auto"><p id="269c5e6f-95bd-8095-bf09-e9b6a78ed71a" class=""><strong>What it is:</strong> The global benchmark of trust across governments, industries, and systems.</p></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80fb-83f9-f53431101f89" class="bulleted-list"><li style="list-style-type:disc"><strong>How it works:</strong> Aggregates signals from energy, finance, governance, and health into one auditable index. Measures how well entire systems respect consent, reduce drift, and prevent fraud.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80c7-a610-c493d1e25d12" class="bulleted-list"><li style="list-style-type:disc"><strong>Example:</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80c0-aa8b-eff82f2789b4" class="bulleted-list"><li style="list-style-type:circle">Today: A country claims strong climate progress, but no one can verify.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8018-850a-d7f5db0eac32" class="bulleted-list"><li style="list-style-type:circle">Tomorrow: PCI Score shows whether its carbon, energy, and governance signals align with planetary baselines. 
Investors allocate capital accordingly.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8087-bc5a-c1f1c371cd97" class="bulleted-list"><li style="list-style-type:disc"><strong>Why it matters:</strong> Becomes the <strong>S&amp;P 500 of trust</strong> — a reference point for global stability and legitimacy.</li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-8058-a570-c0a44aca9362"/></div><div style="display:contents" dir="auto"><h1 id="269c5e6f-95bd-80da-9564-ccea6732d78b" class=""><strong>Why This Stack Wins</strong></h1></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80ed-aa87-c4366977a0ee" class="bulleted-list"><li style="list-style-type:disc"><strong>For Individuals</strong> → A portable, improvable trust score (PTI).</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80b1-8550-c7d82ae2847b" class="bulleted-list"><li style="list-style-type:disc"><strong>For Companies</strong> → A visible benchmark of integrity (CII + OTI).</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8077-a71b-e7779b7c3c7c" class="bulleted-list"><li style="list-style-type:disc"><strong>For Governments &amp; Markets</strong> → A planetary trust layer (PCI Score).</li></ul></div><div style="display:contents" dir="auto"><p id="269c5e6f-95bd-8082-9569-f184fe12f996" class="">Together, the <strong>Trust &amp; 
Consent Index Stack</strong> makes <strong>trust measurable, portable, and tradable</strong> — turning integrity into the new competitive edge of the 21st century.</p></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-8003-bee0-e22a402526f0"/></div><div style="display:contents" dir="auto"><h1 id="269c5e6f-95bd-8021-8609-ceb840fc5f70" class=""><strong>Personal Trust Index (PTI) Scoring Model</strong></h1></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-8000-a9fb-e7119e9ac753" class=""><strong>Score Range</strong></h3></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-803a-a22b-dc3150928b0f" class="bulleted-list"><li style="list-style-type:disc"><strong>0–100 scale</strong> (higher = stronger trust/resilience).</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-807e-ab0f-c4b8e1d92038" class="bulleted-list"><li style="list-style-type:disc"><strong>Bands for interpretation:</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80f7-b77e-cd447ed49b01" class="bulleted-list"><li style="list-style-type:circle"><strong>80–100</strong> → Highly resilient, consistent, trustworthy.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-800b-8007-e05453aaa4fa" class="bulleted-list"><li style="list-style-type:circle"><strong>60–79</strong> → Stable but improvable.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-804f-85b0-e37828711fe1" class="bulleted-list"><li style="list-style-type:circle"><strong>40–59</strong> → Vulnerable to stress or drift.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-808f-b6b3-c8c7a839782b" class="bulleted-list"><li style="list-style-type:circle"><strong>0–39</strong> → Unstable; 
signals unreliable without intervention.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-80fe-a47c-d2087709bfb6"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-8086-acb4-fac27f05d3c9" class=""><strong>Dimensions &amp; Weights</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-80a0-816a-f771522dd06b" class="numbered-list" start="1"><li><strong>Biological Resilience Score™ (BRS)</strong> → <em>40%</em><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8042-a3bc-f8414943ae72" class="bulleted-list"><li style="list-style-type:disc">Based on HRV (heart rate variability), stress recovery, sleep consistency.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8043-a0fb-d7951925a4ee" class="bulleted-list"><li style="list-style-type:disc">Captured via wearables + NeuroSignal™ Agent stress tasks.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80b8-b5b3-da4cbad1fd77" class="bulleted-list"><li style="list-style-type:disc"><strong>Why:</strong> Foundation of all other abilities; 
instability here reveals drift risk.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-800f-9003-d8490c339a98" class="numbered-list" start="2"><li><strong>Emotional Neutrality</strong> → <em>20%</em><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80cf-89d3-f7af52818989" class="bulleted-list"><li style="list-style-type:disc">Measures bias-free communication under observation.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-802e-a218-d9b2ec51d2b8" class="bulleted-list"><li style="list-style-type:disc">Example: Interview simulation with NeuroSignal™ detects projection vs clarity.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80fe-b4ab-eac2adf015b9" class="bulleted-list"><li style="list-style-type:disc"><strong>Why:</strong> Neutrality reduces noise and distortion.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-8080-a5f9-f901e6f3a1fb" class="numbered-list" start="3"><li><strong>Consistency of Consent</strong> → <em>15%</em><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80fc-b6f4-e1f5b0c45a18" class="bulleted-list"><li style="list-style-type:disc">Logs how consistently an individual gives/revokes consent across systems.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80b9-84f9-f2a4bb3b8560" class="bulleted-list"><li style="list-style-type:disc">Example: Not toggling privacy on/off randomly; 
stable patterns of decision.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80a4-9b20-f03769aab6bd" class="bulleted-list"><li style="list-style-type:disc"><strong>Why:</strong> Reflects predictability and reliability in decision-making.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-80c2-8e5a-c8d8be363744" class="numbered-list" start="4"><li><strong>Logic Compression</strong> → <em>15%</em><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80aa-a6b7-c92395e5d7b5" class="bulleted-list"><li style="list-style-type:disc">Assessed via problem-solving tasks.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80f9-b609-e774173d4e3b" class="bulleted-list"><li style="list-style-type:disc">Scoring based on ability to reduce complexity into executable steps.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-801c-bb4e-da6e41152c36" class="bulleted-list"><li style="list-style-type:disc"><strong>Why:</strong> High compression → clarity under uncertainty.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-8015-9116-d4e786b9bcbc" class="numbered-list" start="5"><li><strong>Pattern Recognition</strong> → <em>10%</em><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80b9-b5fb-d8eb6dad6377" class="bulleted-list"><li style="list-style-type:disc">Detects ability to spot systemic connections (tested via simulations).</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-804f-983e-ce5cfe6b8ede" class="bulleted-list"><li style="list-style-type:disc">Example: Anticipating failure points in a scenario before they occur.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80dd-b341-e2e3374c3ed0" class="bulleted-list"><li style="list-style-type:disc"><strong>Why:</strong> Future-focused; 
shows foresight and systemic awareness.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-8067-bf02-e70ef0c38b4b"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-80ef-af62-f1d27b0d2085" class=""><strong>Example Candidate Profiles</strong></h3></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8013-8443-f93588779328" class="bulleted-list"><li style="list-style-type:disc"><strong>Profile A: “The Resilient Operator”</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8094-9649-d24d2c98f498" class="bulleted-list"><li style="list-style-type:circle">BRS: 85, Emotional Neutrality: 70, Consent Consistency: 80, Logic Compression: 60, Pattern Recognition: 55.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80dd-aa38-e8083258568b" class="bulleted-list"><li style="list-style-type:circle">Weighted PTI = <strong>74</strong> (Stable but can improve compression &amp; 
foresight).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-803a-aa24-df26e8fbc4aa" class="bulleted-list"><li style="list-style-type:disc"><strong>Profile B: “The Sharp but Fragile”</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-800e-9344-c6e20d260bae" class="bulleted-list"><li style="list-style-type:circle">BRS: 45, Emotional Neutrality: 60, Consent Consistency: 50, Logic Compression: 85, Pattern Recognition: 90.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80c1-aeb5-ca6a0f6fb7a2" class="bulleted-list"><li style="list-style-type:circle">Weighted PTI = <strong>61</strong> (High intelligence, but resilience is weak — vulnerable under stress).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80d4-8b0c-fb2881a03a24" class="bulleted-list"><li style="list-style-type:disc"><strong>Profile C: “The Consistent All-Rounder”</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-806f-a781-eb0dc6dd4c1d" class="bulleted-list"><li style="list-style-type:circle">BRS: 75, Emotional Neutrality: 75, Consent Consistency: 70, Logic Compression: 70, Pattern Recognition: 65.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-807b-9d91-e8245c56e378" class="bulleted-list"><li style="list-style-type:circle">Weighted PTI = <strong>72</strong> (Balanced, reliable, 
steady growth potential).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-8060-a6a0-e9efb9f89847"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-8057-83f5-dd381a9f0090" class=""><strong>User Experience</strong></h3></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-809c-9f93-f4b265b50108" class="bulleted-list"><li style="list-style-type:disc">PTI displayed as a <strong>dynamic dashboard</strong> inside the NeuroSignal™ app.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8054-b723-c5c5ccc70985" class="bulleted-list"><li style="list-style-type:disc">Shows <strong>overall score + dimension breakdown</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8057-bf9b-d7f653a80391" class="bulleted-list"><li style="list-style-type:disc">Provides <strong>targeted training recommendations</strong>:<div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8015-8d4a-fe1ded889ff4" class="bulleted-list"><li style="list-style-type:circle">“Improve BRS → practice 5-min recovery drills daily.”</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-805d-8633-e59c20c43064" class="bulleted-list"><li style="list-style-type:circle">“Logic Compression → complete weekly challenge tasks.”</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80f3-8ae9-ea5160f952ce" class="bulleted-list"><li style="list-style-type:disc">Users can <strong>track progress over time</strong> like fitness apps → “Your PTI rose from 61 → 72 in 3 months.”</li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-8004-8698-e177d0e42a6e"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-80b9-8440-ee5a5694b760" class=""><strong>Investor Hook</strong></h3></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8091-8bf9-d01bce33b035" c
lass="bulleted-list"><li style="list-style-type:disc">PTI = <strong>the FICO score of human resilience &amp; trust</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8056-a27d-f2ee16499c4c" class="bulleted-list"><li style="list-style-type:disc">Insurers, employers, and lenders can license PTI as a benchmark for pricing risk or hiring decisions.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80c5-b0e4-f7da65c9280b" class="bulleted-list"><li style="list-style-type:disc">High-margin: data captured once, monetised across sectors.</li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-809b-8c96-ce0ca663ae15"/></div><div style="display:contents" dir="auto"><h1 id="269c5e6f-95bd-803e-9e14-e4f47db9407d" class=""><strong>Organisational Trust Index (OTI) Scoring Model</strong></h1></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-80b7-8c4a-cf676e340ed0" class=""><strong>Score Range</strong></h3></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8009-968a-e6b35cbd5c44" class="bulleted-list"><li style="list-style-type:disc"><strong>0–100 scale</strong> (higher = stronger trust &amp; 
consent alignment).</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80e0-b02a-fa613795ce51" class="bulleted-list"><li style="list-style-type:disc"><strong>Bands for interpretation:</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8036-8944-dabb87715982" class="bulleted-list"><li style="list-style-type:circle"><strong>80–100</strong> → Highly trustworthy, resilient, market-leading integrity.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8083-8953-e574f58267f3" class="bulleted-list"><li style="list-style-type:circle"><strong>60–79</strong> → Stable but with identifiable risks.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80d6-82b4-d10dffb92982" class="bulleted-list"><li style="list-style-type:circle"><strong>40–59</strong> → Weak trust signals; vulnerable to drift, instability, or manipulation.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8066-ac8b-e32066e50521" class="bulleted-list"><li style="list-style-type:circle"><strong>0–39</strong> → Unreliable; high risk for investors, regulators, or partners.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-80d2-a409-ebd2f44b1e39"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-802f-8f43-fdba8d7f98fd" class=""><strong>Dimensions &amp; Weights</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-8036-bc27-d9ac68dbf9e6" class="numbered-list" start="1"><li><strong>Employee Resilience &amp; 
Integrity (ERI)</strong> → <em>30%</em><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-806e-9f35-dd20169d9d23" class="bulleted-list"><li style="list-style-type:disc">Aggregated <strong>Biological Resilience Score™ (BRS)</strong> across employees (via NeuroSignal™ opt-in).</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8095-bb56-f02777afcb27" class="bulleted-list"><li style="list-style-type:disc">Stability under stress, workforce adaptability, 
and consistency of ethical behaviour.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-809c-a191-c0b331f9d915" class="bulleted-list"><li style="list-style-type:disc"><strong>Why:</strong> A resilient workforce reduces operational and reputational risk.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-8079-b31c-e329582abb06" class="numbered-list" start="2"><li><strong>Consent Integrity (CI)</strong> → <em>25%</em><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-801e-b687-feb653d7d8e0" class="bulleted-list"><li style="list-style-type:disc">Measured through PCI logs:<div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8078-bdf8-c56fc7646240" class="bulleted-list"><li style="list-style-type:circle">Are customer and employee consents honoured?</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80a2-a0ab-dcaea0d4f83b" class="bulleted-list"><li style="list-style-type:circle">Are revocations respected?</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8084-8e83-d7331d3d7797" class="bulleted-list"><li style="list-style-type:circle">Are dark patterns avoided?</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-803b-a8fb-edf42e0c5cfb" class="bulleted-list"><li style="list-style-type:disc"><strong>Why:</strong> Consent handling is the foundation of long-term trust.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-8088-b36f-c308a333edb4" class="numbered-list" start="3"><li><strong>Leadership Ethical Alignment (LEA)</strong> → <em>20%</em><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8002-920d-ceb64ab8d398" class="bulleted-list"><li style="list-style-type:disc">Assesses executive decision-making against ethical infrastructure.</li></ul></div><div style="display:contents" dir="auto"><ul i
d="269c5e6f-95bd-80f4-8ffd-c9c0bfe7c351" class="bulleted-list"><li style="list-style-type:disc">Tracks whether leaders choose long-term systemic stability over short-term profit.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80e7-8527-c873faccae64" class="bulleted-list"><li style="list-style-type:disc"><strong>Why:</strong> Tone at the top drives systemic behaviour.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-8024-b54c-cd9402dfe360" class="numbered-list" start="4"><li><strong>Operational Transparency (OT)</strong> → <em>15%</em><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80c3-97bd-cddc0632cc78" class="bulleted-list"><li style="list-style-type:disc">Publicly verifiable disclosures: supply chain, carbon, compliance, audit trails.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8026-ad4c-fa838dca0bb7" class="bulleted-list"><li style="list-style-type:disc">Cross-validation by external attestors (PCI marketplace).</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-809d-8940-ee53808ef95e" class="bulleted-list"><li style="list-style-type:disc"><strong>Why:</strong> Transparency prevents misallocation and reduces investor uncertainty.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-8093-a3f6-d98d1685f572" class="numbered-list" start="5"><li><strong>Systemic Contribution (SC)</strong> → <em>10%</em><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80a9-86be-e5b2c6fea82d" class="bulleted-list"><li style="list-style-type:disc">Measures whether company outputs align with planetary needs (energy, environment, 
social wellbeing).</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8033-8ede-fd420973b220" class="bulleted-list"><li style="list-style-type:disc">Signals pulled from public data and PCI records.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80b2-9070-e0ce1751bd1f" class="bulleted-list"><li style="list-style-type:disc"><strong>Why:</strong> Organisations that contribute systemically attract capital and trust.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-806d-8a68-e71053d389d0"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-807b-a178-d7d7e7d081ef" class=""><strong>Example Company Profiles</strong></h3></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80fb-b2c0-f2c2a7f8b882" class="bulleted-list"><li style="list-style-type:disc"><strong>Profile A: “The Trusted Innovator”</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8034-b292-c4b11c6f3c42" class="bulleted-list"><li style="list-style-type:circle">ERI: 85, CI: 90, LEA: 80, OT: 75, SC: 70.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-808a-94a8-d7cff2c97c07" class="bulleted-list"><li style="list-style-type:circle">Weighted OTI = <strong>82</strong> (Resilient workforce + high consent = strong long-term performer).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-809b-9442-d2a5685d51df" class="bulleted-list"><li style="list-style-type:disc"><strong>Profile B: “The Fragile High-Flier”</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8042-8ffe-e2ce71a010cf" class="bulleted-list"><li style="list-style-type:circle">ERI: 50, CI: 60, LEA: 70, OT: 55, 
SC: 80.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-807a-876f-e285da0117c4" class="bulleted-list"><li style="list-style-type:circle">Weighted OTI = <strong>61</strong> (Innovative but unstable workforce + weak transparency = medium risk).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-802c-9bb2-ef8da2192aa1" class="bulleted-list"><li style="list-style-type:disc"><strong>Profile C: “The Stable Operator”</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-802e-a7ea-f49239e8a2db" class="bulleted-list"><li style="list-style-type:circle">ERI: 70, CI: 75, LEA: 65, OT: 70, SC: 65.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-808c-89c1-f9f19be373b9" class="bulleted-list"><li style="list-style-type:circle">Weighted OTI = <strong>71</strong> (Balanced, low-drama company; safe for investors, steady growth).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-80fa-b9c5-e32ba8ed59c4"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-80d8-8fa1-f6a9fe5a6005" class=""><strong>User Experience for Companies</strong></h3></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8016-b110-c1536c914802" class="bulleted-list"><li style="list-style-type:disc">OTI shown on a <strong>dashboard for leadership, regulators, and investors</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80fc-9a01-c0d9fdf3917f" class="bulleted-list"><li style="list-style-type:disc">Breaks down dimensions → e.g., “Your weakest area: Consent Integrity (CI 60). 
Improving this raises overall trust.”</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8050-a179-e176939e1ee0" class="bulleted-list"><li style="list-style-type:disc">Linked to <strong>NeuroSignal™ training programs</strong> for employees (stress resilience, ethical alignment).</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8034-b916-f1044a92a197" class="bulleted-list"><li style="list-style-type:disc">Public OTI scores can be published like ESG ratings → building market trust.</li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-80d1-9368-d91799d2d231"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-8049-bf96-c07fbab16029" class=""><strong>Investor &amp; 
Market Hook</strong></h3></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8096-8548-d9e7e0de2d11" class="bulleted-list"><li style="list-style-type:disc">OTI = <strong>the S&amp;P rating of trust and resilience</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-809c-b2e4-d289a3f7a9fb" class="bulleted-list"><li style="list-style-type:disc">Investors use it for risk pricing (e.g., financing terms tied to OTI band).</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80a7-a566-effa29dd6d8f" class="bulleted-list"><li style="list-style-type:disc">Insurers use it to adjust premiums for liability and operational risk.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8010-9e5b-e87dcf9e5b4a" class="bulleted-list"><li style="list-style-type:disc">Customers use it to choose ethical brands with verifiable integrity.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80f9-b8f6-e467b793d3fa" class="bulleted-list"><li style="list-style-type:disc">Governments and regulators use it as a benchmark for compliance.</li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-80a0-9c8f-d1a2b0c71276"/></div><div style="display:contents" dir="auto"><p id="269c5e6f-95bd-8019-b54a-f384acd089ca" class="">✅ Together, <strong>PTI (for individuals)</strong> and <strong>OTI (for companies)</strong> form the <strong>core commercial stack</strong> of the Signal Economy™.</p></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80e5-9f22-ebce48586cc1" class="bulleted-list"><li style="list-style-type:disc">PTI → monetisable via insurance, health, talent, consumer apps.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80a0-9c39-c82c50de57a1" class="bulleted-list"><li style="list-style-type:disc">OTI → monetisable via finance, regulation, ESG, 
corporate risk.</li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-80c5-9f7a-c729655a7d16"/></div><div style="display:contents" dir="auto"><h1 id="269c5e6f-95bd-80c1-84b0-d87209aa8fe5" class=""><strong>Consent Integrity Index (CII) Scoring Model</strong></h1></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-808b-9c24-c1548bc02102" class=""><strong>Score Range</strong></h3></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-800b-9d00-f9a99ee170c8" class="bulleted-list"><li style="list-style-type:disc"><strong>0–100 scale</strong> (higher = stronger consent integrity).</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8089-b8ed-dc5f235db55c" class="bulleted-list"><li style="list-style-type:disc"><strong>Bands for interpretation:</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-803d-b1cf-dd3a42b255b8" class="bulleted-list"><li style="list-style-type:circle"><strong>80–100</strong> → Consent practices exemplary; benchmark for industry.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80e3-8e7a-f00ccd085bd6" class="bulleted-list"><li style="list-style-type:circle"><strong>60–79</strong> → Generally good, but with gaps or occasional violations.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-801a-81bf-d556981af8fa" class="bulleted-list"><li style="list-style-type:circle"><strong>40–59</strong> → Weak practices; prone to manipulation or complaints.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8065-9049-f20b625c27d7" class="bulleted-list"><li style="list-style-type:circle"><strong>0–39</strong> → Untrustworthy; 
high likelihood of exploitation or legal risk.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-8002-8377-f77d48e9929d"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-80a3-b5ef-fef230abcc76" class=""><strong>Dimensions &amp; 
Weights</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-8098-840c-e0f65f5757ca" class="numbered-list" start="1"><li><strong>Consent Honouring (CH)</strong> → <em>35%</em><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8047-9a90-eb853d9b9cda" class="bulleted-list"><li style="list-style-type:disc">% of requests where consent is granted/revoked <em>exactly as the user intended</em>.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8073-b105-f92f824548c3" class="bulleted-list"><li style="list-style-type:disc">Tracked by PCI across all systems.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80a9-9f5d-f98f9b6a7fb1" class="bulleted-list"><li style="list-style-type:disc"><strong>Why:</strong> This is the foundation of trust — respect for user agency.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-80f8-951e-fcd0dac92613" class="numbered-list" start="2"><li><strong>Transparency of Use (TU)</strong> → <em>25%</em><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8092-ac06-f78617facccf" class="bulleted-list"><li style="list-style-type:disc">How clearly and accessibly companies explain what signals are collected and how they’re used.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8091-a06b-d2b15a4ef925" class="bulleted-list"><li style="list-style-type:disc">PCI validation ensures no hidden clauses.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8082-8c4d-fdf7474c4381" class="bulleted-list"><li style="list-style-type:disc"><strong>Why:</strong> Clear disclosures reduce drift and manipulation.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-807d-93dd-f77d5af20165" class="numbered-list" start="3"><li><strong>Revocation Respect (RR)</strong> → <em>20%</em><div s
tyle="display:contents" dir="auto"><ul id="269c5e6f-95bd-80b2-817c-c3e7ffd0bf91" class="bulleted-list"><li style="list-style-type:disc">How reliably systems delete or stop using signals after consent is withdrawn.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8021-834a-e601e6fd09f3" class="bulleted-list"><li style="list-style-type:disc">Audited by PCI logs and third-party attestations.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8016-a475-d79a837599c5" class="bulleted-list"><li style="list-style-type:disc"><strong>Why:</strong> Revocation is the ultimate test of trust.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-8033-8bcb-e2fe6acb8b69" class="numbered-list" start="4"><li><strong>Dark Pattern Avoidance (DPA)</strong> → <em>10%</em><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-803f-b2c4-dddce34ea970" class="bulleted-list"><li style="list-style-type:disc">Detects manipulative design that pressures users into giving consent.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-802e-826a-ce16c915bb5b" class="bulleted-list"><li style="list-style-type:disc"><strong>Why:</strong> Prevents coercion and restores true choice.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-80f5-9e1d-d4a31cb016c1" class="numbered-list" start="5"><li><strong>Audit &amp; 
Accountability (AA)</strong> → <em>10%</em><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-803d-828f-e5b41f53a14e" class="bulleted-list"><li style="list-style-type:disc">How accessible and auditable consent records are to users, regulators, and watchdogs.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8088-b966-ea06563dd66e" class="bulleted-list"><li style="list-style-type:disc"><strong>Why:</strong> Accountability makes trust enforceable.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-807d-820b-f03dcad678d4"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-80ba-96b9-d4ee6a5f92fd" class=""><strong>Example Platform Profiles</strong></h3></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8019-897d-f96df6a4857e" class="bulleted-list"><li style="list-style-type:disc"><strong>Profile A: “The Gold Standard App”</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80c0-b8da-eb43fcc4d88f" class="bulleted-list"><li style="list-style-type:circle">CH: 90, TU: 85, RR: 88, DPA: 80, AA: 85.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8098-8547-cef05c2ffbcd" class="bulleted-list"><li style="list-style-type:circle">Weighted CII = <strong>87</strong> (Transparent, trustworthy; attracts loyal users &amp; 
investors).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80de-a735-d749ff41b40b" class="bulleted-list"><li style="list-style-type:disc"><strong>Profile B: “The Shaky Middle”</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80aa-bb8d-cf4c174d6ca3" class="bulleted-list"><li style="list-style-type:circle">CH: 65, TU: 60, RR: 50, DPA: 45, AA: 60.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8006-bfd8-ce4d9b6b31bf" class="bulleted-list"><li style="list-style-type:circle">Weighted CII = <strong>58</strong> (Common today; users tolerated but distrust builds).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80bc-a165-c89f9c9d76ba" class="bulleted-list"><li style="list-style-type:disc"><strong>Profile C: “The Extractor”</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80d8-baa0-e4d89760a83b" class="bulleted-list"><li style="list-style-type:circle">CH: 30, TU: 40, RR: 20, DPA: 25, AA: 35.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8031-9675-c9ea63c55fe1" class="bulleted-list"><li style="list-style-type:circle">Weighted CII = <strong>30</strong> (Exploitative; lawsuits and customer flight inevitable).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-80ae-8376-cf2a3d89bf16"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-804c-88e8-c230c1ca18b0" class=""><strong>User &amp; 
Market Experience</strong></h3></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80f9-aa26-d68761c2cf3d" class="bulleted-list"><li style="list-style-type:disc"><strong>For Users:</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-803a-8281-e8284c1e6515" class="bulleted-list"><li style="list-style-type:circle">A simple <strong>CII badge</strong> shows whether an app or service can be trusted.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-800b-bd83-c8b02e00abef" class="bulleted-list"><li style="list-style-type:circle">High CII → safe, respectful.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80b5-b7be-ebce73891723" class="bulleted-list"><li style="list-style-type:circle">Low CII → warning of risk.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8011-9250-d4d81c57ff17" class="bulleted-list"><li style="list-style-type:disc"><strong>For Companies:</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80fa-984d-fbe4754d0ea7" class="bulleted-list"><li style="list-style-type:circle">CII is a <strong>competitive advantage</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80f8-a2af-fa2fa564ccb7" class="bulleted-list"><li style="list-style-type:circle">Higher scores = more users, cheaper financing, regulatory goodwill.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8087-b977-c8afa7a4bf28" class="bulleted-list"><li style="list-style-type:disc"><strong>For Regulators &amp; 
Investors:</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-803a-b2e5-e57758ba46cc" class="bulleted-list"><li style="list-style-type:circle">CII acts like a <strong>compliance thermometer</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-806b-a8a5-ed87b0f10e80" class="bulleted-list"><li style="list-style-type:circle">Easy to benchmark who is aligned vs. 
who is at risk.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-8056-bb7d-fb7ddad2b7ec"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-8019-b920-c9f7626cfb49" class=""><strong>Investor Hook</strong></h3></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-800f-9cd6-f08bb8a8e9e5" class="bulleted-list"><li style="list-style-type:disc">CII = <strong>the ESG score of consent</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80b1-86ab-f45ee377f1b4" class="bulleted-list"><li style="list-style-type:disc">Subscription revenues from companies seeking audits and higher ratings.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-805f-b19a-fbc897bfe938" class="bulleted-list"><li style="list-style-type:disc">Demand from insurers, banks, and regulators who want to de-risk portfolios.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80b8-a398-f501da87ff37" class="bulleted-list"><li style="list-style-type:disc">Consumer pull: trusted companies display their <strong>CII badge</strong> like “Fair Trade” — but for consent.</li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-802a-a559-ed201d834cc2"/></div><div style="display:contents" dir="auto"><p id="269c5e6f-95bd-80f1-aac8-f5466d7d25e4" class="">✅ With PTI (individuals), CII (consent practices), and OTI (organisations), 
the Signal Economy builds a <strong>full-trust stack</strong>:</p></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8058-8263-dc5b862c632f" class="bulleted-list"><li style="list-style-type:disc">PTI → “How trustworthy are you?”</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80e9-b218-fbb98f330c69" class="bulleted-list"><li style="list-style-type:disc">CII → “How trustworthy is this service?”</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8043-909b-ea8782876f58" class="bulleted-list"><li style="list-style-type:disc">OTI → “How trustworthy is this organisation?”</li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-80f0-94aa-e7c4208f6c82"/></div><div style="display:contents" dir="auto"><h1 id="269c5e6f-95bd-8013-9e08-ccfe6faa7619" class=""><strong>Planetary Consent Index (PCI Score)</strong></h1></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-8061-bf1b-d4bd72c118e3" class=""><strong>Score Range</strong></h3></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80d0-be8d-d26ff043a6d6" class="bulleted-list"><li style="list-style-type:disc"><strong>0–100 scale</strong> (higher = stronger systemic trust, consent, and alignment).</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-801d-bed0-f968d45ddcd9" class="bulleted-list"><li style="list-style-type:disc"><strong>Bands for interpretation:</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8006-91f5-d3f37c673e09" class="bulleted-list"><li style="list-style-type:circle"><strong>80–100</strong> → Globally trusted, high stability, exemplary governance.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80e3-9d6f-d2b8a00274f0" class="bulleted-list"><li style="list-style-type:circle"><strong>60–79</strong> → Generally strong, 
but with systemic gaps or weak enforcement.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80c4-8c7e-ed4cd0d4bedc" class="bulleted-list"><li style="list-style-type:circle"><strong>40–59</strong> → Significant trust issues; prone to drift, opacity, or corruption.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8095-888b-c3c46165b821" class="bulleted-list"><li style="list-style-type:circle"><strong>0–39</strong> → Unstable or extractive; systemic collapse or capture risk.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-80fe-8f51-e2d9295e56bf"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-8050-b7b0-d448661bd64d" class=""><strong>Dimensions &amp; 
Weights</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-8097-af3d-f7d150641be9" class="numbered-list" start="1"><li><strong>Consent Infrastructure Alignment (CIA)</strong> → <em>30%</em><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80cb-895b-fc7131a47b73" class="bulleted-list"><li style="list-style-type:disc">How fully a country, sector, or industry has adopted PCI governance.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80e4-8886-f69f994a82c5" class="bulleted-list"><li style="list-style-type:disc">% of signals logged, consent respected, revocations honoured.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80bb-8678-ec5f411ba270" class="bulleted-list"><li style="list-style-type:disc"><strong>Why:</strong> Consent is the backbone of legitimacy at scale.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-80b6-af8e-e7697dc92142" class="numbered-list" start="2"><li><strong>Systemic Transparency (ST)</strong> → <em>25%</em><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8069-9f27-e9a1df8a7605" class="bulleted-list"><li style="list-style-type:disc">Degree of open reporting for energy, carbon, finance, health, 
governance.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80b0-a577-d94f268cd1bc" class="bulleted-list"><li style="list-style-type:disc">Signals must be verifiable and auditable across borders.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80ac-9f39-da045f7c463c" class="bulleted-list"><li style="list-style-type:disc"><strong>Why:</strong> Transparency prevents manipulation and collapse.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-80a9-bde8-cce892291736" class="numbered-list" start="3"><li><strong>Trust Stability (TS)</strong> → <em>20%</em><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8048-b008-e5eeeefbc563" class="bulleted-list"><li style="list-style-type:disc">Measures the consistency of trust signals over time (low volatility, stable baselines).</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-802c-96ab-e76b974abf34" class="bulleted-list"><li style="list-style-type:disc"><strong>Why:</strong> Stability attracts capital and global cooperation.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-8060-9688-f6cad47d308b" class="numbered-list" start="4"><li><strong>Ethical Alignment (EA)</strong> → <em>15%</em><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-802f-b55b-c6d6c750d873" class="bulleted-list"><li style="list-style-type:disc">Whether systemic decisions align with planetary survival (e.g., carbon, health, 
equity).</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-804b-98fe-fac2a3d2d84b" class="bulleted-list"><li style="list-style-type:disc"><strong>Why:</strong> Systems with drift eventually collapse — ethics anchors continuity.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="269c5e6f-95bd-807b-86da-c17f07fe6dfd" class="numbered-list" start="5"><li><strong>Resilience &amp; Adaptability (RA)</strong> → <em>10%</em><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-804b-999b-d169547cf62f" class="bulleted-list"><li style="list-style-type:disc">Ability to absorb shocks (climate, economic, political) without collapsing trust.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80ef-9123-e154a412fa52" class="bulleted-list"><li style="list-style-type:disc"><strong>Why:</strong> Resilient systems sustain themselves under stress.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-8032-a048-ea3bedd02c54"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-80b6-a895-fd9877f281b1" class=""><strong>Example Profiles</strong></h3></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8086-a88e-f8db87a5d461" class="bulleted-list"><li style="list-style-type:disc"><strong>Profile A: “The High-Trust Nation”</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8051-86e4-eb044b17067f" class="bulleted-list"><li style="list-style-type:circle">CIA: 85, ST: 90, TS: 88, EA: 80, RA: 85.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80b9-a513-d366498b52c0" class="bulleted-list"><li style="list-style-type:circle">Weighted PCI Score = <strong>86</strong> (Stable, trusted globally; 
attracts investment and talent).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80a4-94a3-d5253fe6ed18" class="bulleted-list"><li style="list-style-type:disc"><strong>Profile B: “The Fragile Middle Power”</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8093-be31-c96c9fecc6a0" class="bulleted-list"><li style="list-style-type:circle">CIA: 55, ST: 60, TS: 50, EA: 45, RA: 55.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80c6-b434-c0f89e3ae8dd" class="bulleted-list"><li style="list-style-type:circle">Weighted PCI Score = <strong>53</strong> (Functional but unstable; 
high systemic risk).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80d3-b485-d4a919aca1dd" class="bulleted-list"><li style="list-style-type:disc"><strong>Profile C: “The Extractive Regime”</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8032-922e-c6099541c899" class="bulleted-list"><li style="list-style-type:circle">CIA: 25, ST: 30, TS: 20, EA: 25, RA: 35.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-803e-9484-f71a6282be39" class="bulleted-list"><li style="list-style-type:circle">Weighted PCI Score = <strong>27</strong> (Low trust, prone to collapse, unattractive to investors).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-8095-bc2c-f9cd7cc23818"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-805d-824b-fa2dff9b5a44" class=""><strong>Why PCI Score Matters</strong></h3></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8095-aec1-edbc40f0c644" class="bulleted-list"><li style="list-style-type:disc"><strong>For Governments:</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8031-93cc-d4610b868429" class="bulleted-list"><li style="list-style-type:circle">PCI is the benchmark for global trust — high scores attract capital, trade, 
and cooperation.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80de-a07d-f550cf3aaecf" class="bulleted-list"><li style="list-style-type:circle">Low scores push regimes toward reform or risk isolation.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80bb-9b14-c51141c62c44" class="bulleted-list"><li style="list-style-type:disc"><strong>For Markets:</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8014-ba0d-da041be5a435" class="bulleted-list"><li style="list-style-type:circle">PCI acts like a <strong>credit rating for nations and sectors</strong>, but rooted in consent and trust, not just debt.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80a5-9f1d-f303984defd0" class="bulleted-list"><li style="list-style-type:circle">Investors instantly see systemic risk and opportunity.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-807a-8b04-fffd5913cc79" class="bulleted-list"><li style="list-style-type:disc"><strong>For Citizens:</strong><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80d9-9067-c216da20e6e1" class="bulleted-list"><li style="list-style-type:circle">PCI provides transparency into whether their rights, data, and planetary survival are truly respected.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-8000-a19f-c8012311f29d"/></div><div style="display:contents" dir="auto"><h3 id="269c5e6f-95bd-80f4-b57c-d4d81421b9dc" class=""><strong>Investor Hook</strong></h3></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-80b7-9f6a-d95e9046ac71" class="bulleted-list"><li style="list-style-type:disc">PCI = <strong>the new global benchmark</strong>, like Moody’s or S&amp;P ratings, 
but harder to game.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-804e-b006-eb2acef286d1" class="bulleted-list"><li style="list-style-type:disc">Subscription model for governments, NGOs, and multilaterals.</li></ul></div><div style="display:contents" dir="auto"><ul id="269c5e6f-95bd-8062-9149-fc5085e1d954" class="bulleted-list"><li style="list-style-type:disc">Private markets (banks, insurers, funds) pay premiums for PCI data to price systemic risk.</li></ul></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-80b1-ac23-c336e16fda10"/></div><div style="display:contents" dir="auto"><p id="269c5e6f-95bd-8027-aa1e-c9c134501144" class="">✅ With <strong>PTI (individuals), CII (consent practices), OTI (organisations), and PCI Score (systems)</strong>, the <strong>Signal Economy™ is a complete, multi-layer trust architecture</strong>.</p></div><div style="display:contents" dir="auto"><hr id="269c5e6f-95bd-8006-93eb-fb65b55dbb8c"/></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
