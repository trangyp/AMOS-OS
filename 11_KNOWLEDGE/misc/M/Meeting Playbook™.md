---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Meeting Playbook™</title><style>
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
	
</style></head><body><article id="26fc5e6f-95bd-80eb-b3f8-e136b11b7389" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Meeting Playbook™</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80d0-b081-cb58761047d3" class=""><strong>Authored by Trang Phan</strong><br/><br/>This is the <strong>definitive operating system</strong> for EDC Fintech meetings.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80c4-8484-de21d51c9ed2" class="">Every session — whether formal or adhoc — must result in <strong>alignment, decisions, or documented next steps</strong>. If no outcome is expected → switch to async update (Google Doc / Telegram post).</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80ed-b2ee-e47507c2f4bd" class="">
</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8015-865b-e8a851684ae1" class="">This framework does three things:<br/>✅ <strong>Prevents drift</strong> by making meetings outcome-driven.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80bc-ba16-d2a7872b7a31" class="">✅ <strong>Creates systemic precision</strong> by recording and assigning every decision.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80a9-88eb-c0f34c7826da" class="">✅ <strong>Builds trust</strong> by showing that no input vanishes into a black hole — everything is acknowledged, owned, and closed.</p></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80be-9c2a-e7154ba61579"/></div><div style="display:contents" dir="auto"><p id="270c5e6f-95bd-804a-9fdc-fef66f91d00f" class="">The <strong>EDC Fintech  Meeting Playbook</strong> is not merely a set of productivity tips; it is a <strong>philosophical and biological system</strong> for human interaction, deeply rooted in the principles of Quantum Life Science (QLS). 
It shares some surface-level best practices with MBB and Big Tech but is fundamentally different in its <strong>purpose, underlying philosophy, and definition of success</strong></p></div><div style="display:contents" dir="auto"><p id="270c5e6f-95bd-8098-8141-e9859454ea8b" class="">Where MBB meetings are designed for <strong>decisive action</strong> and Big Tech meetings for <strong>efficient information exchange</strong>, EDC Fintech  meetings are designed for <strong>collective biological and electromagnetic alignment</strong> to produce <strong>lawful, coherent, and sustainable outcomes.</strong></p></div><div style="display:contents" dir="auto"><h3 id="270c5e6f-95bd-806f-9f75-dc5c6ea2e4e1" class=""><strong>Key Differentiators of the EDC Fintech  Playbook</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="270c5e6f-95bd-806d-837a-d07bfc366024" class="numbered-list" start="1"><li><strong>Biological First:</strong> It is the only model that explicitly designs for the human nervous system as a primary input and output. The &quot;pre-sync&quot; and &quot;micro-recovery&quot; are as important as the agenda.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="270c5e6f-95bd-8089-bd66-f380f78937bf" class="numbered-list" start="2"><li><strong>Purpose is Alignment, Not Just Output:</strong> The goal is not just to make a decision, but to ensure that decision was made in a state of collective biological and intentional alignment, which QLS argues is necessary for its long-term success.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="270c5e6f-95bd-806c-a4fe-db21eec90dc9" class="numbered-list" start="3"><li><strong>Rejects &quot;Extractive&quot; Communication:</strong> The playbook is designed to avoid the &quot;extractive&quot; meeting culture common in high-pressure environments (e.g., draining energy, forcing consensus through fatigue). 
It seeks to be regenerative.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="270c5e6f-95bd-80ae-a356-d00d0c3ec7b3" class="numbered-list" start="4"><li><strong>Integrated Ethical Boundary:</strong> The constant emphasis on &quot;clean intent&quot; and &quot;ethical continuity&quot; (a QLS law) builds an ethical guardrail directly into the process, which is often an afterthought in other models.</li></ol></div><div style="display:contents" dir="auto"><h3 id="270c5e6f-95bd-80ab-83fc-f5d53ac8fc08" class=""><strong>Conclusion: Who Is This For?</strong></h3></div><div style="display:contents" dir="auto"><ul id="270c5e6f-95bd-809a-8453-d6def67d9f61" class="bulleted-list"><li style="list-style-type:disc"><strong>MBB/Big Tech Meetings:</strong> Are optimised for <strong>output and velocity</strong> in complex, high-stakes environments. They are the industry standard for a reason—they work for achieving business goals quickly.</li></ul></div><div style="display:contents" dir="auto"><ul id="270c5e6f-95bd-80da-8a79-c7b1085e64cb" class="bulleted-list"><li style="list-style-type:disc"><strong>EDC Fintech  Meeting Playbook:</strong> Is optimised for <strong>sustainability, wisdom, and collective resonance.</strong> It is designed for organizations that believe the <em>quality of the process</em> directly determines the <em>longevity and integrity of the outcome</em>.</li></ul></div><div style="display:contents" dir="auto"><p id="270c5e6f-95bd-80f7-9c57-f3a73af914ef" class="">It is not that one is better than the other in an absolute sense. They are tools for different purposes. 
The EDC Fintech  playbook is a radical, next-generation approach for leaders and organizations that are building not for the next quarter, but for the next quarter-<em>century</em>, and who believe that human systems must operate in harmony with biological and physical laws to endure.</p></div><div style="display:contents" dir="auto"><hr id="270c5e6f-95bd-8040-aa33-ee1df3439546"/></div><div style="display:contents" dir="auto"><h2 id="26fc5e6f-95bd-8007-9104-f56edb7bb942" class=""><strong>Meeting Types</strong></h2></div><div style="display:contents" dir="ltr"><table id="26fc5e6f-95bd-8052-b0a2-e2ba2e1899f9" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-803d-8448-cbd4f7c2d9d1"><th id="Yjd[" class="simple-table-header-color simple-table-header" style="width:203.75px"><strong>Meeting Type</strong></th><th id="VFmn" class="simple-table-header-color simple-table-header" style="width:185.75px"><strong>Purpose</strong></th><th id="P\R&gt;" class="simple-table-header-color simple-table-header" style="width:212.75px"><strong>Example Questions</strong></th><th id="VuRo" class="simple-table-header-color simple-table-header" style="width:179px"><strong>Cadence</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80b1-b9fc-d43e67ec81a2"><td id="Yjd[" class="" style="width:203.75px"><strong>1. Decision-Making Meetings</strong></td><td id="VFmn" class="" style="width:185.75px">Choose between options, commit to action</td><td id="P\R&gt;" class="" style="width:212.75px">“Do we launch Campaign A or B?” “Do we approve this supplier contract?”</td><td id="VuRo" class="" style="width:179px">As needed — should be short and final</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-809d-8e02-fac2bace478f"><td id="Yjd[" class="" style="width:203.75px"><strong>2. 
Problem-Solving / Triage</strong></td><td id="VFmn" class="" style="width:185.75px">Resolve blockers and crises fast</td><td id="P\R&gt;" class="" style="width:212.75px">“What’s stopping this launch?” “Who owns this fix?”</td><td id="VuRo" class="" style="width:179px">Daily standups, ad-hoc</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8047-9125-e9ac20e77c55"><td id="Yjd[" class="" style="width:203.75px"><strong>3. Planning / Roadmap Sessions</strong></td><td id="VFmn" class="" style="width:185.75px">Align on sprints, OKRs, campaigns</td><td id="P\R&gt;" class="" style="width:212.75px">“What does success look like this quarter?” “Where are dependencies?”</td><td id="VuRo" class="" style="width:179px">Quarterly, monthly</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80d5-aa67-e636248c198d"><td id="Yjd[" class="" style="width:203.75px"><strong>4. Status Updates</strong></td><td id="VFmn" class="" style="width:185.75px">Share progress, surface early risks</td><td id="P\R&gt;" class="" style="width:212.75px">“Are we on track?” “What changed since last sync?”</td><td id="VuRo" class="" style="width:179px">Weekly (max 15–20 mins)</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8054-a42f-c6763a1a74ab"><td id="Yjd[" class="" style="width:203.75px"><strong>5. Innovation / Ideation Workshops</strong></td><td id="VFmn" class="" style="width:185.75px">Generate new campaign ideas, product features</td><td id="P\R&gt;" class="" style="width:212.75px">“What problems do customers face we can solve?”</td><td id="VuRo" class="" style="width:179px">Monthly or per project</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8002-8e30-d9be104f1185"><td id="Yjd[" class="" style="width:203.75px"><strong>6. 
Stakeholder Reviews</strong></td><td id="VFmn" class="" style="width:185.75px">Present work to board, partners, investors</td><td id="P\R&gt;" class="" style="width:212.75px">“Do we have approval to move to next phase?”</td><td id="VuRo" class="" style="width:179px">End-of-phase, milestone-based</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80b1-92cc-fbfb3b234e04"><td id="Yjd[" class="" style="width:203.75px"><strong>7. Retrospectives / Post-Mortems</strong></td><td id="VFmn" class="" style="width:185.75px">Extract lessons, prevent repeat mistakes</td><td id="P\R&gt;" class="" style="width:212.75px">“What worked, what didn’t, what to change?”</td><td id="VuRo" class="" style="width:179px">After launches or failures</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-809b-b30f-c869a7866f50"><td id="Yjd[" class="" style="width:203.75px"><strong>8. 1:1s / Coaching Sessions</strong></td><td id="VFmn" class="" style="width:185.75px">Build team growth, remove personal blockers</td><td id="P\R&gt;" class="" style="width:212.75px">“What’s your biggest challenge this week?”</td><td id="VuRo" class="" style="width:179px">Biweekly or monthly</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8078-93a4-d91787b9a577"><td id="Yjd[" class="" style="width:203.75px"><strong>9. Supplier / Partner Meetings</strong></td><td id="VFmn" class="" style="width:185.75px">Secure alignment on deliverables, timelines, costs</td><td id="P\R&gt;" class="" style="width:212.75px">“What risks do you see on your side?” “How do we improve collaboration?”</td><td id="VuRo" class="" style="width:179px">Kickoff + milestone check-ins</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8005-9a2d-e176a2760eca"><td id="Yjd[" class="" style="width:203.75px"><strong>10. 
Information-Gathering Sessions</strong></td><td id="VFmn" class="" style="width:185.75px">Research market trends, customer insights</td><td id="P\R&gt;" class="" style="width:212.75px">“What are competitors doing?” “What are customers saying?”</td><td id="VuRo" class="" style="width:179px">Ad hoc — should be structured and time-boxed</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h1 id="26fc5e6f-95bd-80cb-ac82-cbcc5259fd54" class=""><strong>EDC Fintech  Meeting Communication Style Guide</strong></h1></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80b3-8f17-c6bc8b0813fc" class="">Meetings are only effective if communication is clear, respectful, and outcome-driven. This guide defines how we speak, ask questions, and deliver information so every session ends with alignment instead of confusion.</p></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-809e-923c-c533b6e870f2"/></div><div style="display:contents" dir="auto"><h2 id="26fc5e6f-95bd-80d4-a5e2-d7d1fc6d6004" class=""><strong>1. Core Principles</strong></h2></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-804d-b95f-e053f9ad6a5a" class="bulleted-list"><li style="list-style-type:disc"><strong>Clarity over cleverness</strong> – Use simple, direct language. Avoid jargon unless everyone in the room understands it.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8056-9275-f4187c9e56a3" class="bulleted-list"><li style="list-style-type:disc"><strong>Signal over noise</strong> – Focus on information that moves the work forward. Side topics go to async threads.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8017-8dbe-f7500af05620" class="bulleted-list"><li style="list-style-type:disc"><strong>Respect time and energy</strong> – Be concise. 
Every minute should contribute to the session outcome.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80c8-b15f-caadeaeec8f8" class="bulleted-list"><li style="list-style-type:disc"><strong>Close loops in real time</strong> – Don’t leave agreements vague. End every topic with clear decisions, owners, and deadlines.</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-805b-a934-ef96da47bb9f"/></div><div style="display:contents" dir="auto"><h2 id="26fc5e6f-95bd-803b-a450-c3e9c390c1cd" class=""><strong>2. How to Ask Questions</strong></h2></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80c4-bfef-cd6b7f438188" class="">Questions are powerful — they can open clarity or derail focus. 
Use these best practices:</p></div><div style="display:contents" dir="ltr"><table id="26fc5e6f-95bd-807a-93c4-fe94bd705797" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8080-a2d0-cfa7aa3c43e4"><th id="]G_L" class="simple-table-header-color simple-table-header" style="width:326px"><strong>DO</strong></th><th id="n|UD" class="simple-table-header-color simple-table-header" style="width:387px"><strong>DON’T</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8034-986b-cb1abdb4a112"><td id="]G_L" class="" style="width:326px">Ask <strong>open, specific questions</strong> that help the group move toward a decision.</td><td id="n|UD" class="" style="width:387px">Ask vague, rhetorical, 
or accusatory questions.</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80e9-9696-f80b3b5262ac"><td id="]G_L" class="" style="width:326px">Use <strong>“What” and “How” questions</strong> to clarify facts or unblock work.</td><td id="n|UD" class="" style="width:387px">Ask “Why are we doing this?” in a confrontational way — instead ask “Can we restate the objective?”</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8091-8cac-fe2699070416"><td id="]G_L" class="" style="width:326px">Ask <strong>one question at a time</strong> and wait for an answer.</td><td id="n|UD" class="" style="width:387px">Stack multiple questions without pause.</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-800a-95f3-c188990555e9"><td id="]G_L" class="" style="width:326px">State <strong>the context first</strong> so others can answer accurately.</td><td id="n|UD" class="" style="width:387px">Drop questions without framing — it confuses the group.</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80bc-93cd-d1572a455c35"><td id="]G_L" class="" style="width:326px">Use <strong>solution-seeking language</strong>: “What would it take to…?”</td><td id="n|UD" class="" style="width:387px">Use blame-oriented language: “Who messed this up?”</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80d9-9111-fb371e8047f0" class=""><strong>Examples:</strong></p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-801a-a345-ccf214cf0cc1" class="">✅ “What’s blocking this shipment, 
and who can own clearing it by Friday?”</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80ff-9ca7-c95771f7131f" class="">✅ “How does this decision affect our Q3 targets?”</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80a2-8a6c-f1a880e952a7" class="">🚫 “Why is this always late?”</p></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80c1-b02c-e1f21c4e471e"/></div><div style="display:contents" dir="auto"><h2 id="26fc5e6f-95bd-80fa-a467-f3d7349748d7" class=""><strong>3. 
Top-Down Communication</strong></h2></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-801a-bb6c-db8ae23fc564" class="">Top-down communication is the practice of <strong>sharing decisions, priorities, 
and context clearly from leadership to teams</strong> — rather than leaving them to guess.</p></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-8003-afd8-e414874d3b29" class=""><strong>Why It Matters</strong></h3></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80fc-b422-f091ce6d8abe" class="bulleted-list"><li style="list-style-type:disc"><strong>Removes ambiguity</strong> – People do their best work when they know exactly what’s expected.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80e0-81c8-dab3bb1a094e" class="bulleted-list"><li style="list-style-type:disc"><strong>Reduces wasted cycles</strong> – Clear direction saves teams from rework or chasing the wrong priorities.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8020-971a-f01bb76d3250" class="bulleted-list"><li style="list-style-type:disc"><strong>Builds trust</strong> – Transparent decisions reduce anxiety and create psychological safety.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80b2-936a-c5295650777d" class="bulleted-list"><li style="list-style-type:disc"><strong>Speeds execution</strong> – Teams can act faster when they don’t need to decode intent.</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80d4-a3dd-d75642f3f52f"/></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-8041-a952-c32a88500354" class=""><strong>How to Deliver Top-Down Communication</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80e1-8e33-f954c579e08e" class="numbered-list" start="1"><li><strong>Lead with the “Why”</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-804d-a547-c318e4fa4391" class="bulleted-list"><li style="list-style-type:disc">Explain the purpose behind the decision or request.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80b2-823f-ef7cf8ee9ecf" 
lass="bulleted-list"><li style="list-style-type:disc">Example: “We’re shifting resources to Product A because it’s the highest revenue driver for Q2.”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-8047-85ff-d39c7081ad4e" class="numbered-list" start="2"><li><strong>Be Specific and Actionable</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-800f-a263-c4b9167e5c68" class="bulleted-list"><li style="list-style-type:disc">Define what needs to happen, who owns it, and by when.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8054-9c0a-fd9d8fbaf05f" class="bulleted-list"><li style="list-style-type:disc">Example: “Marketing to deliver final assets by April 15. 
Ops to confirm supplier capacity by April 20.”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-8029-836e-c5a14cf24cbe" class="numbered-list" start="3"><li><strong>Use Written + Verbal Channels</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8014-83e6-f02c3a6e9807" class="bulleted-list"><li style="list-style-type:disc">Say it once in the meeting, then post a written recap in Google Docs/Telegram so it can’t be lost.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80d5-b605-cc8177de0973" class="numbered-list" start="4"><li><strong>Invite Clarifying Questions</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8084-b21e-ea6489904e46" class="bulleted-list"><li style="list-style-type:disc">“Does anyone see a risk we missed?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8015-b368-c005f88e1a61" class="bulleted-list"><li style="list-style-type:disc">“Are there blockers to executing this plan?”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-809a-940b-ece4cb973fd3" class="numbered-list" start="5"><li><strong>Reinforce Until Understood</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-800a-a7ef-df00ae5c6841" class="bulleted-list"><li style="list-style-type:disc">Don’t assume one message is enough. Repeat key decisions in follow-ups until everyone is aligned.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-804a-8056-ed280f600dac"/></div><div style="display:contents" dir="auto"><h2 id="26fc5e6f-95bd-80ae-b9a8-d632915d313d" class=""><strong>4. 
Cultural Guardrails</strong></h2></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80ef-b86b-c3b25d74e275" class="bulleted-list"><li style="list-style-type:disc"><strong>No passive aggression.</strong> Feedback is direct and focused on work, not personalities.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8030-8f50-e404b2a094fe" class="bulleted-list"><li style="list-style-type:disc"><strong>No information hoarding.</strong> Context is shared openly unless confidential by necessity.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-806a-85de-ef76a9ad10b2" class="bulleted-list"><li style="list-style-type:disc"><strong>No silent misalignment.</strong> If you disagree, raise it during the meeting, not after.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80e4-b116-c51bcd0aa5e9" class="bulleted-list"><li style="list-style-type:disc"><strong>No endless loops.</strong> Max three feedback rounds unless escalation is justified.</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-8029-95f0-cf60b9593409"/></div><div style="display:contents" dir="auto"><h1 id="26fc5e6f-95bd-8093-a87e-e2c0b82ad0bf" class="">Meeting Types</h1></div><div style="display:contents" dir="auto"><h2 id="26fc5e6f-95bd-8044-aa22-f11f49b1fa7f" class=""><strong>1. 
Decision-Making Meetings</strong></h2></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8080-a2d9-f6818ad929dc" class=""><strong>Purpose:</strong> Lock a final decision — supplier choice, budget, creative approval, go/no-go.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8077-81e5-ced45810ad86" class=""><strong>When to Use:</strong> After research is done and waiting will slow momentum.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-802d-a51c-ee6458d63f4d" class=""><strong>Sample Agenda:</strong></p></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-803e-8c66-f07f81683e1d" class="numbered-list" start="1"><li><strong>Purpose Declaration (2 mins)</strong> – “We are here to decide X so that Y can move forward.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80d4-aa15-c513fe758793" class="numbered-list" start="2"><li><strong>Current State Review (5 mins)</strong> – Show data (Google Sheet, Notion table, Jira ticket).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80c5-8600-cf1c722e9d06" class="numbered-list" start="3"><li><strong>Options &amp; Trade-Offs (10 mins)</strong> – Present 2–3 options, pros/cons side by side.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-8086-a225-e633d8e2293f" class="numbered-list" start="4"><li><strong>Discussion + Decision (10 mins)</strong> – Capture decision live in shared doc.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80ce-aaa3-e1a2030a1bfd" class="numbered-list" start="5"><li><strong>Owner &amp; 
Timeline (3 mins)</strong> – Assign who executes and set deadline.</li></ol></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8043-91ac-c4ad8d858cac" class=""><strong>Facilitator Tips:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-801e-8a81-dbcf3a4ffed3" class="bulleted-list"><li style="list-style-type:disc">Bring only decision-makers.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-804e-90b1-cd321d66a53c" class="bulleted-list"><li style="list-style-type:disc">Use a decision log (Google Doc) to avoid repeating debates.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8047-9345-c9dc774fd829" class="bulleted-list"><li style="list-style-type:disc">Capture in Jira immediately so execution begins right after.</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-800d-ad2a-d7643c09f542" class=""><strong>Success Metrics:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80c1-9f1a-eb168f4cf2d4" class="bulleted-list"><li style="list-style-type:disc">✅ Decision logged before end of meeting.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8023-abcc-e66d40256caa" class="bulleted-list"><li style="list-style-type:disc">✅ No repeat discussion next week.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8028-9204-c9aaa7c2484d" class="bulleted-list"><li style="list-style-type:disc">✅ Owner updates Jira/Slack within 24 hours.</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80ab-9eec-cb8ab79f7ba6"/></div><div style="display:contents" dir="auto"><h2 id="26fc5e6f-95bd-8026-85d1-e528e87a68b2" class=""><strong>2. 
Problem-Solving / Triage</strong></h2></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8034-b8fa-ec9f6a86d314" class=""><strong>Purpose:</strong> Clear blockers, protect timelines, and avoid escalation later.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-801d-9ec8-c6ad73ba194d" class=""><strong>When to Use:</strong> When Jira shows unresolved blockers or a risk threatens delivery.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80f1-864d-fab3b0434b12" class=""><strong>Sample Agenda:</strong></p></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-804d-9ca9-f72fdc2d4b46" class="numbered-list" start="1"><li><strong>Align on Current State (5 mins)</strong> – Show Jira board, focus on blocked tasks.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-8017-9b1b-dad82972ccf9" class="numbered-list" start="2"><li><strong>List All Blockers (5 mins)</strong> – Whiteboard or shared doc.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80e6-995c-d70dac68f9ec" class="numbered-list" start="3"><li><strong>Classify Blockers (5 mins)</strong> – Decision gap, resource gap, unclear owner, process failure.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80f8-ad39-c11b90e759cb" class="numbered-list" start="4"><li><strong>Resolve in Order of Impact (15 mins)</strong> – Quick decisions first, 
log next steps in Jira.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80ca-ab41-f9b6b3731f6e" class="numbered-list" start="5"><li><strong>Confirm Actions + Owners (3 mins)</strong> – Each owner says out loud what they will do and by when.</li></ol></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8073-a74d-caf77b8241d4" class=""><strong>Facilitator Tips:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80db-844a-f52925755b22" class="bulleted-list"><li style="list-style-type:disc">Use “one blocker per person” rule — stop pile-on and solve one thing at a time.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80b7-b633-e12a7d966ee3" class="bulleted-list"><li style="list-style-type:disc">If resolution needs fewer people, schedule a follow-up with only the relevant owner.</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-804b-aede-eec08332a3cf" class=""><strong>Success Metrics:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80ff-a30f-e47f4978c772" class="bulleted-list"><li style="list-style-type:disc">✅ ≥70% blockers resolved in-session.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80ff-a46e-fd3e77fe503b" class="bulleted-list"><li style="list-style-type:disc">✅ Jira board cleared of “red” items within 24h.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8047-9e7e-d5290d2a958e" class="bulleted-list"><li style="list-style-type:disc">✅ No surprises for leadership later.</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80b1-97f6-dfe3bb10531c"/></div><div style="display:contents" dir="auto"><h2 id="26fc5e6f-95bd-8009-b6a9-e9efede29cde" class=""><strong>3. 
Planning / Roadmap Sessions</strong></h2></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8007-9ce6-e4aef6dd5405" class=""><strong>Purpose:</strong> Build clarity on future work and avoid mid-cycle thrash.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80ff-984a-d74f9efdeed3" class=""><strong>When to Use:</strong> Start of a quarter, sprint, or large initiative.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80df-93b2-ce8324d31d97" class=""><strong>Sample Agenda:</strong></p></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-8083-af64-f2a1e9d9ff2c" class="numbered-list" start="1"><li><strong>Purpose + Context (5 mins)</strong> – What we are planning for (quarter, launch).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-8053-a9e5-edbcb6e620a9" class="numbered-list" start="2"><li><strong>Priorities Review (10 mins)</strong> – What matters most to EDC Fintech  this cycle.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80ba-bd8a-f1e7391f4bdd" class="numbered-list" start="3"><li><strong>Resource Reality (10 mins)</strong> – People, budget, 
suppliers.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80be-88d8-f1f9b81ad817" class="numbered-list" start="4"><li><strong>Timeline Draft (15 mins)</strong> – Build live in Jira.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80be-bd9a-fc7317c5ea0e" class="numbered-list" start="5"><li><strong>Risk + Dependency Call-Out (5 mins)</strong> – Flag anything that might slip.</li></ol></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80b1-8d6f-e7969fead888" class=""><strong>Example Questions:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80fd-90ac-e7fa845fd747" class="bulleted-list"><li style="list-style-type:disc">“If we only did 3 things this quarter, 
which matter most?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-808f-8f1d-fdff4c1dd8f9" class="bulleted-list"><li style="list-style-type:disc">“What are we overcommitting to?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80dd-9bf2-f4a789e1e372" class="bulleted-list"><li style="list-style-type:disc">“What risks do we need exec sign-off on?”</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-806b-8793-fb17e88e5527" class=""><strong>Success Metrics:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8084-b878-d0aa280d196b" class="bulleted-list"><li style="list-style-type:disc">✅ Jira roadmap complete with owners + dates.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8030-87ba-ca6b878456a8" class="bulleted-list"><li style="list-style-type:disc">✅ Budget request finalised same day.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8076-bf30-f2022fdc2713" class="bulleted-list"><li style="list-style-type:disc">✅ Risks tracked in Google Sheet or risk register.</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80c1-a6cf-fd4e143eaf13"/></div><div style="display:contents" dir="auto"><h2 id="26fc5e6f-95bd-8040-8a2f-d5c8dbd26544" class=""><strong>4. 
Status Updates / Check-Ins</strong></h2></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-804f-91c8-c25e5502b650" class=""><strong>Purpose:</strong> Share progress and surface risks — not storytelling.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80a9-951e-c8175f2eacab" class=""><strong>When to Use:</strong> Weekly standups or async docs.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80b3-8256-f28994b26438" class=""><strong>Sample Agenda:</strong></p></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-800f-b8e4-d2ae23793f5f" class="numbered-list" start="1"><li><strong>Yesterday / Last Week</strong> – Done items.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-807a-abc5-febfaf368323" class="numbered-list" start="2"><li><strong>Today / This Week</strong> – Focus items.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-804a-a0bd-f75aefe5dd14" class="numbered-list" start="3"><li><strong>Blockers</strong> – Immediate escalations.</li></ol></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80af-a926-d4915e2d17a2" class=""><strong>Facilitator Tips:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8010-b469-f12a8257a986" class="bulleted-list"><li style="list-style-type:disc">Use Telegram thread for async updates — no meeting unless blockers need live discussion.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-809a-aa57-e5ac01441845" class="bulleted-list"><li style="list-style-type:disc">Rotate facilitator weekly so everyone owns team health.</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8074-b248-ee5b515eacc1" class=""><strong>Success Metrics:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80f2-b248-c641f1520285" class="bulleted-list"><li s
tyle="list-style-type:disc">✅ Standup ≤15 mins.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80ad-a751-c29ec80eb0c7" class="bulleted-list"><li style="list-style-type:disc">✅ Jira board reflects reality (no stale tasks).</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8039-8ef3-e2dde70f8fa1" class="bulleted-list"><li style="list-style-type:disc">✅ &lt;2 unplanned escalations after standup.</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-808c-8f37-ec0c1b1c548c"/></div><div style="display:contents" dir="auto"><h2 id="26fc5e6f-95bd-80ac-9046-cbc7a7c2d56d" class=""><strong>5. 
Innovation / Ideation</strong></h2></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8049-bf09-d3ea13c2d724" class=""><strong>Purpose:</strong> Generate creative solutions and spark fresh thinking.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80ca-947f-f0e37a2a8f98" class=""><strong>When to Use:</strong> Early stage of product, campaign, or process.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8026-9e0c-ef7e78d0eb41" class=""><strong>Sample Agenda:</strong></p></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-8009-b3fd-fcbbaa8a7547" class="numbered-list" start="1"><li><strong>Problem Statement (5 mins)</strong> – “What are we solving for?”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-8040-bb74-c3b6c96295e7" class="numbered-list" start="2"><li><strong>Diverge (15 mins)</strong> – Generate as many ideas as possible (Figma/Miro).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-807d-8d30-ccc829cc7bd1" class="numbered-list" start="3"><li><strong>Cluster &amp; 
Vote (10 mins)</strong> – Group similar ideas, use dot-voting.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-8079-b744-ef13426a592b" class="numbered-list" start="4"><li><strong>Prioritise (10 mins)</strong> – Select top 2–3 for testing.</li></ol></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-804d-bb7b-db804e1cb3b3" class=""><strong>Facilitator Tips:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-803b-a95e-f04535967834" class="bulleted-list"><li style="list-style-type:disc">Create psychological safety — no idea-shaming.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80a3-a72e-f00e8a3048e3" class="bulleted-list"><li style="list-style-type:disc">Use timeboxing to prevent overthinking.</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80ba-8503-c8c301b02907" class=""><strong>Success Metrics:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8083-941b-db08137d351a" class="bulleted-list"><li style="list-style-type:disc">✅ ≥10 ideas generated.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-802d-8bb2-e09524646de2" class="bulleted-list"><li style="list-style-type:disc">✅ Top ideas validated within 48h.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80dc-808b-c1c9022f5437" class="bulleted-list"><li style="list-style-type:disc">✅ Next sprint includes at least 1 experiment.</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-8041-9bdb-c928f7431478"/></div><div style="display:contents" dir="auto"><h2 id="26fc5e6f-95bd-809a-b768-f185aa8189ce" class=""><strong>6. 
Stakeholder Reviews</strong></h2></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-800b-8c3e-f94eebeca6ba" class=""><strong>Purpose:</strong> Gain alignment with leadership or board before proceeding.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80b8-afa1-c959c1bdcd89" class=""><strong>When to Use:</strong> Monthly/quarterly, 
or for major asks.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80e4-b6af-d15aa60a2928" class=""><strong>Sample Agenda:</strong></p></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80d4-8e1f-f74c82d50a53" class="numbered-list" start="1"><li><strong>State Purpose (3 mins)</strong> – “We need approval for X.”</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80b2-9536-c02876ad8e03" class="numbered-list" start="2"><li><strong>Data Review (10 mins)</strong> – Show only relevant KPIs.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-808d-92f5-e519827bd059" class="numbered-list" start="3"><li><strong>Decision Requests (10 mins)</strong> – Make clear asks.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-8072-a313-e8a97decee94" class="numbered-list" start="4"><li><strong>Q&amp;A + Alignment (10 mins)</strong> – Capture agreements in doc.</li></ol></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80ca-90de-e51294d45e11" class=""><strong>Facilitator Tips:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8031-a63e-d17ef5010436" class="bulleted-list"><li style="list-style-type:disc">Send deck 48h before meeting.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80ec-b722-cda06786b198" class="bulleted-list"><li style="list-style-type:disc">Always end with summary email + next steps.</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-805f-bece-f23040b59305" class=""><strong>Success Metrics:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8012-86a9-f86c1eae4129" class="bulleted-list"><li style="list-style-type:disc">✅ Clear yes/no/redirect recorded.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80b6-b2a8-e84b9e575a3a" class="bulleted-list"><li s
tyle="list-style-type:disc">✅ Execs never ask for same data twice.</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80ea-8405-fdaae24d683a"/></div><div style="display:contents" dir="auto"><h2 id="26fc5e6f-95bd-80d5-a3b6-e44def84c45f" class=""><strong>7. 
Retrospectives / Post-Mortems</strong></h2></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8051-af83-d8064f5b406c" class=""><strong>Purpose:</strong> Learn from wins/failures, improve systems.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-801a-b44f-fcab2aeab3d3" class=""><strong>When to Use:</strong> End of project or after an incident.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-807e-af26-e13ff25a34cf" class=""><strong>Sample Agenda:</strong></p></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80c7-8062-f2de594ed5ed" class="numbered-list" start="1"><li><strong>What Worked (10 mins)</strong> – Celebrate wins.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80d0-aa42-e51977c8b31c" class="numbered-list" start="2"><li><strong>What Didn’t (10 mins)</strong> – Be candid, no blame.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80c6-813a-f40186690a28" class="numbered-list" start="3"><li><strong>Actions (10 mins)</strong> – Assign fixes, update playbooks.</li></ol></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8091-b52b-e14f30d306ac" class=""><strong>Facilitator Tips:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-801b-afdf-c8f60d733cc1" class="bulleted-list"><li style="list-style-type:disc">Keep focus on process, 
not personal blame.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80c5-9100-d18214053d92" class="bulleted-list"><li style="list-style-type:disc">Capture learning in team handbook.</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-809b-b1ea-f9926e782937" class=""><strong>Success Metrics:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8077-9c30-e989f48d3527" class="bulleted-list"><li style="list-style-type:disc">✅ ≥2 process improvements implemented.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-804d-9527-de1a28a49ade" class="bulleted-list"><li style="list-style-type:disc">✅ Fewer repeat issues next cycle.</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-8073-a57f-e6bf08841e9b"/></div><div style="display:contents" dir="auto"><h2 id="26fc5e6f-95bd-80ea-b43e-f5943c1013d5" class=""><strong>8. 
1:1s / Coaching Sessions</strong></h2></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-809b-85fb-d10fb7ea804f" class=""><strong>Purpose:</strong> Strengthen trust and support growth.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8008-9396-f891aed70113" class=""><strong>When to Use:</strong> Weekly or biweekly.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-804c-a0dd-d7c7bd350194" class=""><strong>Sample Agenda:</strong></p></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-803f-af00-f220090f2622" class="numbered-list" start="1"><li><strong>Wins (5 mins)</strong> – Acknowledge progress.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-803e-9c9a-f65f759b93ff" class="numbered-list" start="2"><li><strong>Challenges (10 mins)</strong> – Talk blockers.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-804f-8fff-f1976c606e6d" class="numbered-list" start="3"><li><strong>Development (10 mins)</strong> – Feedback both ways.</li></ol></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-806c-bd70-d5dfb4381f5a" class=""><strong>Facilitator Tips:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8094-84c9-c5c1f642a04e" class="bulleted-list"><li style="list-style-type:disc">Keep this sacred — don’t cancel unless urgent.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8051-8220-f08adfcb4072" class="bulleted-list"><li style="list-style-type:disc">Write follow-up notes for accountability.</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-802d-914c-df29e5c401da" class=""><strong>Success Metrics:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-800e-b982-e8d7a1a6a622" class="bulleted-list"><li style="list-style-type:disc">✅ Team member reports feeling supported.</li></ul></div><div s
tyle="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8018-968b-f2b5024e12c3" class="bulleted-list"><li style="list-style-type:disc">✅ Blockers resolved within a week.</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-803c-b701-e29ab2dab3f4"/></div><div style="display:contents" dir="auto"><h2 id="26fc5e6f-95bd-80a2-93bf-e6c4a88dbb3e" class=""><strong>9. Supplier Meetings</strong></h2></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8027-b0da-e78d26877e62" class=""><strong>Kick-Off:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8037-bd03-d72e29950b45" class="bulleted-list"><li style="list-style-type:disc">Share timeline, compliance, quality standards.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80e7-a108-c6f2f0ee66b4" class="bulleted-list"><li style="list-style-type:disc">Confirm POC, communication channel (Telegram).</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-805a-8b9a-fad800c27f54" class="bulleted-list"><li style="list-style-type:disc">Outcome: First delivery schedule agreed.</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-807b-bd3f-ed963ce0f22c" class=""><strong>Quarterly Review:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8088-853a-e2f4864c4576" class="bulleted-list"><li style="list-style-type:disc">Review on-time %, defect rates, cost.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-801c-950b-c84e92fb2401" class="bulleted-list"><li style="list-style-type:disc">Outcome: Continue/adjust contract + corrective actions.</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80f0-be43-dcf7393741f8"/></div><div style="display:contents" dir="auto"><h2 id="26fc5e6f-95bd-800b-80c9-ebe11386097f" class=""><strong>10. 
Information-Gathering Sessions</strong></h2></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8020-a7f9-c0686efc6ae3" class=""><strong>Purpose:</strong> Market and supplier intel to feed decisions.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8055-969b-eb9c60e19d23" class=""><strong>When to Use:</strong> Pre-launch or when trends shift.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-801d-8658-e23f0731ed6b" class="">Questions:</p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8031-9cab-d1046fe37ead" class="bulleted-list"><li style="list-style-type:disc">“What’s happening with competitor pricing?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80d6-ae5e-f8bd1271a61e" class="bulleted-list"><li style="list-style-type:disc">“What materials are trending in market?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8048-8dc8-e872b4a762c0" class="bulleted-list"><li style="list-style-type:disc">“Where is customer sentiment shifting?”</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-804c-954a-da464db17d57" class="">Outcome: Documented insights → roadmap prioritisation.</p></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80ce-8f23-d066b631749a"/></div><div style="display:contents" dir="auto"><h2 id="26fc5e6f-95bd-808e-9eb9-f8451e52fbcb" class=""><strong>11. 
Adhoc Quick-Action Meetings</strong></h2></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80b6-b3d9-f731b6c78bdb" class=""><strong>Purpose:</strong> Make a decision or unblock in real-time.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8015-84b6-d0eabebb806b" class=""><strong>Format:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-802c-bb70-e5f0dbed5ba2" class="bulleted-list"><li style="list-style-type:disc"><strong>10-min decision huddles</strong> — capture outcome in Jira before leaving.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80d9-a56f-c23229ba37fd" class="bulleted-list"><li style="list-style-type:disc"><strong>Crisis response calls</strong> — assign owners, post public update.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8094-8176-efa5adec88d5" class="bulleted-list"><li style="list-style-type:disc"><strong>Micro-planning sessions</strong> — align next 48h of work.</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-803e-985b-d8068e230203" class="">Success = No Slack/Telegram thread longer than 15 messages without a resolution call.</p></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-800f-9689-e93e640cac0b"/></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-805a-b57f-d96bf1e6037d" class="">
</p></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80a0-88cb-e76f2d770a75"/></div><div style="display:contents" dir="auto"><h1 id="26fc5e6f-95bd-8080-a724-f2de353fbd5a" class=""><strong>Decision-Making Meetings – Deep Dive</strong></h1></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-802a-9169-ca744cef98f8" class=""><strong>✅ Facilitator Checklist (Before Meeting)</strong></h3></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80fc-8b72-ea4b0418347c" class="bulleted-list"><li style="list-style-type:disc">Confirm <strong>purpose</strong> of the meeting in 1 sentence: <em>“We are here to decide X so Y can move forward.”</em></li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80ac-a563-e7536ecc654c" class="bulleted-list"><li style="list-style-type:disc">Pre-distribute <strong>data pack</strong> (Google Doc / Sheet) 24h before.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80ab-8edf-c8ff0feb69c5" class="bulleted-list"><li style="list-style-type:disc">Invite <strong>only decision-makers</strong> + key advisors — no observers.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8025-9fa1-f9ae6a57e91a" class="bulleted-list"><li style="list-style-type:disc">Add a <strong>decision log section</strong> at the top of the doc for real-time capture.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-807d-b7c7-c26d5b46b4b9" class="bulleted-list"><li style="list-style-type:disc">Prepare <strong>2–3 options</strong> with trade-offs and recommendations.</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80d6-ac4e-c0f043e2f70b"/></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-80e5-a567-ec97e3f73d9f" class=""><strong>❓ Question Prompts (During Meeting)</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80a5-a1cf-d6e722a747d9" c
lass="numbered-list" start="1"><li><strong>Clarify Readiness:</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8006-aad0-d979c68091ea" class="bulleted-list"><li style="list-style-type:disc">“Do we have enough data to decide today?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8003-a7eb-db8377d24c59" class="bulleted-list"><li style="list-style-type:disc">“Is anyone missing critical context?”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80e8-84b2-c0713a151936" class="numbered-list" start="2"><li><strong>Explore Options:</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8037-a878-f2e174b43c0d" class="bulleted-list"><li style="list-style-type:disc">“What are the top pros and cons for Option A/B/C?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80a3-9f0a-f3c546ee447f" class="bulleted-list"><li style="list-style-type:disc">“What is the cost of delay if we wait?”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80db-a885-e6312bc628b5" class="numbered-list" start="3"><li><strong>Surface Risks:</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8082-9ccd-c2c727656018" class="bulleted-list"><li style="list-style-type:disc">“What could go wrong if we choose this path?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8035-ac04-ed3dcb06892d" class="bulleted-list"><li style="list-style-type:disc">“Who owns mitigation if that happens?”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80ca-8aaa-eb8b9ccba4ca" class="numbered-list" start="4"><li><strong>Close the Decision:</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8047-a5d1-d5bb5abafdb1" class="bulleted-list"><li style="list-style-type:disc">“Are we aligned?”</li></ul></div><div s
tyle="display:contents" dir="auto"><ul id="26fc5e6f-95bd-807e-9149-efa5f439b626" class="bulleted-list"><li style="list-style-type:disc">“Who is responsible for execution and by when?”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80ab-8682-fed1e3c3d8cd"/></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-809d-9726-eb773015a518" class=""><strong>📝 Outcome Logging (End of Meeting)</strong></h3></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80a3-aea0-e4fdea02848a" class="">Capture decisions in a shared doc or Jira ticket:</p></div><div style="display:contents" dir="ltr"><table id="26fc5e6f-95bd-80c7-b4c2-e007c0f061b2" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80e3-9861-dccaf62232f7"><th id="B&lt;ed" class="simple-table-header-color simple-table-header"><strong>Decision</strong></th><th id="Y^;m" class="simple-table-header-color simple-table-header"><strong>Owner</strong></th><th id=":A@R" class="simple-table-header-color simple-table-header"><strong>Due Date</strong></th><th id="&gt;nCl" class="simple-table-header-color simple-table-header"><strong>Next Review</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80b3-ad31-efd6b3a3c48b"><td id="B&lt;ed" class="">Choose Supplier A for Q3 production</td><td id="Y^;m" class="">Minh (Procurement)</td><td id=":A@R" class="">15 Aug</td><td id="&gt;nCl" class="">Q3 Review</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80f4-bb16-ef3cc5947ac9"><td id="B&lt;ed" class="">Approve $10k budget for launch ads</td><td id="Y^;m" class="">Finance + Marketing</td><td id=":A@R" class="">22 Aug</td><td id="&gt;nCl" class="">Q4 Spend Review</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-801b-97ce-c1db0ae59862" class="">Post <strong>recap in T
elegram</strong> immediately after — no one leaves unclear about the outcome.</p></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80f4-b9bc-de695ce76194"/></div><div style="display:contents" dir="auto"><h1 id="26fc5e6f-95bd-801c-aa41-f2dd48a44e87" class=""><strong>Problem-Solving / Triage Meetings – Deep Dive</strong></h1></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-806a-bebe-c17761be8d91" class=""><strong>✅ Facilitator Checklist (Before Meeting)</strong></h3></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8028-8759-d492db71c2ca" class="bulleted-list"><li style="list-style-type:disc">Confirm <strong>urgent blocker</strong> is real — not just a status update.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80d4-8d1c-fc51d883659d" class="bulleted-list"><li style="list-style-type:disc">Collect <strong>facts, screenshots, Jira tickets, 
or supplier updates</strong> in advance.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80f3-ae3b-de53e0aa3e31" class="bulleted-list"><li style="list-style-type:disc">Invite <strong>only those who can fix or approve</strong> the solution (avoid spectators).</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8025-9c57-f9ed8b0a24ad" class="bulleted-list"><li style="list-style-type:disc">Timebox meeting (max 30 mins) — prepare to park off-topic issues.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8020-80eb-f11c47972a97" class="bulleted-list"><li style="list-style-type:disc">Prepare a <strong>shared doc or board</strong> with sections: <em>Blocker → Root Cause → Action → Owner → Deadline</em>.</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-8044-9083-fb58ba7d0364"/></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-80ad-8e85-c5a4cb76bc78" class=""><strong>❓ Question Prompts (During Meeting)</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80fe-99d1-e8f6a2602447" class="numbered-list" start="1"><li><strong>Identify the Core Blocker:</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-803f-ab1d-e8f0304f0a2c" class="bulleted-list"><li style="list-style-type:disc">“What is the #1 thing preventing progress right now?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80b7-b1d1-daf6f7bd3dc5" class="bulleted-list"><li style="list-style-type:disc">“Where exactly is the issue occurring — tool, process, 
supplier?”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-8055-abf3-fecd18f726fe" class="numbered-list" start="2"><li><strong>Classify the Blocker:</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-804f-a6f4-e31d0cce6375" class="bulleted-list"><li style="list-style-type:disc">Decision Needed → “Who can sign off right now?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8094-bf36-d98ea30f14aa" class="bulleted-list"><li style="list-style-type:disc">Resource Gap → “What resource or budget is missing?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-802c-a54c-fb87cbcccb4a" class="bulleted-list"><li style="list-style-type:disc">Ownership Gap → “Who should be responsible for this?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80a2-b005-e9bf88f371f0" class="bulleted-list"><li style="list-style-type:disc">Process Misalignment → “What policy or workflow broke?”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80b0-911e-ee09a591d445" class="numbered-list" start="3"><li><strong>Evaluate Impact:</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80ea-89dd-f6d8efac1d8a" class="bulleted-list"><li style="list-style-type:disc">“What happens if this isn’t resolved today?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80f7-840b-c054421f5ec1" class="bulleted-list"><li style="list-style-type:disc">“Who downstream is waiting on this?”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80f4-9aad-fa7889a2ae4e" class="numbered-list" start="4"><li><strong>Resolve or Escalate:</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-802c-9f4d-d9a1c1c29ae3" class="bulleted-list"><li style="list-style-type:disc">“Can we solve this right h
ere?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80f4-b4ba-d55bc6bcbbbf" class="bulleted-list"><li style="list-style-type:disc">“If not, 
who will own the mini-session and by when?”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80c2-962f-fddc65ebd7b7"/></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-801a-9e21-db807fa6347c" class=""><strong>📝 Outcome Logging (End of Meeting)</strong></h3></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-807e-96bc-d42096550554" class="">Capture each blocker resolution live in a doc or Jira comment:</p></div><div style="display:contents" dir="ltr"><table id="26fc5e6f-95bd-8065-81d7-e7cb7bcfb1e0" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8098-8c0a-fd8069c6c55e"><th id="vTgY" class="simple-table-header-color simple-table-header"><strong>Blocker</strong></th><th id="Q?IS" class="simple-table-header-color simple-table-header"><strong>Resolution</strong></th><th id="eWq}" class="simple-table-header-color simple-table-header"><strong>Owner</strong></th><th id="aEgH" class="simple-table-header-color simple-table-header"><strong>Due Date</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80c8-903e-f9279016950c"><td id="vTgY" class="">Supplier delayed raw material shipment</td><td id="Q?IS" class="">Schedule follow-up call to confirm new ETA</td><td id="eWq}" class="">Linh (Ops)</td><td id="aEgH" class="">Today 4PM</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8089-8b53-e9b19965ec4f"><td id="vTgY" class="">Pricing approval stuck in finance</td><td id="Q?IS" class="">Escalate to CFO for final sign-off</td><td id="eWq}" class="">Bao (Finance)</td><td id="aEgH" class="">Tomorrow EOD</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8009-811e-e1ddd8e30564" class="">Send recap in <strong>Telegram / Slack</strong> with:</p></div><div style="display:contents" dir="auto"><p i
d="26fc5e6f-95bd-8086-a8d5-fd49389d49a1" class="">✅ Resolved blockers</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8083-9753-c974f9caf911" class="">⏳ Pending actions + deadlines</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80b3-ad96-fd8d6f2612c9" class="">📌 Escalations (if any)</p></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-800b-8ecf-db02bf0162e7"/></div><div style="display:contents" dir="auto"><h1 id="26fc5e6f-95bd-803f-943a-f45bfc80e7f5" class=""><strong>Planning / Roadmap Sessions – Deep Dive</strong></h1></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-8064-9b50-fde734509375" class=""><strong>✅ Facilitator Checklist (Before Meeting)</strong></h3></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80e2-b753-f454011d0a66" class="bulleted-list"><li style="list-style-type:disc">Prepare <strong>current-state snapshot</strong> (active projects, budgets, resource map).</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80a5-bb5f-d98d2858d36b" class="bulleted-list"><li style="list-style-type:disc">Collect <strong>data on velocity, costs, risks</strong> from Jira/Google Sheets.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80c5-9bb0-ef2791e0b4ff" class="bulleted-list"><li style="list-style-type:disc">Draft <strong>preliminary roadmap</strong> or list of priorities for discussion.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80cb-a87a-d9acb696c03a" class="bulleted-list"><li style="list-style-type:disc">Ensure all key decision-makers are invited (PM, ops, finance, 
suppliers if relevant).</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8048-b331-df37a17203c6" class="bulleted-list"><li style="list-style-type:disc">Block <strong>60–90 mins</strong> depending on scope (quarterly or sprint planning).</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-8081-955a-dfb806dd089d"/></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-8089-9bf2-ec9e2549e972" class=""><strong>❓ Question Prompts (During Meeting)</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80f9-8993-d5c99d1412bf" class="numbered-list" start="1"><li><strong>Clarify Goals &amp; Success Metrics:</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80f8-8a93-c4715ad33b4b" class="bulleted-list"><li style="list-style-type:disc">“What are the top 3 measurable outcomes we must deliver this quarter?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-807f-a827-e88f77904f5b" class="bulleted-list"><li style="list-style-type:disc">“Which KPI, revenue target, or cost-saving is most critical?”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-8052-affb-ede5298d04d0" class="numbered-list" start="2"><li><strong>Prioritise Work:</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80f2-9abb-c8a0061aea0c" class="bulleted-list"><li style="list-style-type:disc">“What must ship first to unblock other streams?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8093-93f7-c0d05483360f" class="bulleted-list"><li style="list-style-type:disc">“What is nice-to-have vs. 
must-have?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80d7-a572-cfa37b255ab1" class="bulleted-list"><li style="list-style-type:disc">“Where is the biggest ROI?”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80a9-8e1b-ce1f92e831bd" class="numbered-list" start="3"><li><strong>Map Resources &amp; 
Dependencies:</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80f6-9781-d6f311a29647" class="bulleted-list"><li style="list-style-type:disc">“Do we have enough capacity for this plan?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8051-ba8d-c20ab7211f12" class="bulleted-list"><li style="list-style-type:disc">“Where do we need more suppliers, budget, 
or headcount?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80ca-a24a-d44b1ada8309" class="bulleted-list"><li style="list-style-type:disc">“Which teams are interdependent — how do we reduce bottlenecks?”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-802a-8229-c99df27a7d19" class="numbered-list" start="4"><li><strong>Identify Risks:</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8018-83c7-c2c3f9c2195d" class="bulleted-list"><li style="list-style-type:disc">“What could derail this plan?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80f5-81f3-e05c401daf9d" class="bulleted-list"><li style="list-style-type:disc">“Which decisions do we need from leadership now?”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-803f-bd12-c3ed317d7a21"/></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-80ea-980d-deffd04a677e" class=""><strong>📝 Outcome Logging (End of Meeting)</strong></h3></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8059-afb7-c81c67cd2168" class="">Lock everything into a shared source of truth before closing:</p></div><div style="display:contents" dir="ltr"><table id="26fc5e6f-95bd-80ac-b5b5-fdb2bb1044cb" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80a7-851f-cf35e7bbef14"><th id="&gt;UTj" class="simple-table-header-color simple-table-header"><strong>Priority</strong></th><th id="FKQt" class="simple-table-header-color simple-table-header"><strong>Owner</strong></th><th id="NVOS" class="simple-table-header-color simple-table-header"><strong>Start Date</strong></th><th id="D:&lt;e" class="simple-table-header-color simple-table-header"><strong>Due Date</strong></th><th id="\CI=" class="simple-table-header-color s
imple-table-header"><strong>Dependencies</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8012-9cff-e762ee8a2281"><td id="&gt;UTj" class="">Launch new wellness product line</td><td id="FKQt" class="">Minh (PM)</td><td id="NVOS" class="">Feb 1</td><td id="D:&lt;e" class="">Mar 15</td><td id="\CI=" class="">Final design sign-off + supplier contract</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80d8-82a1-e2c037b1c196"><td id="&gt;UTj" class="">Supplier diversification initiative</td><td id="FKQt" class="">Linh (Ops)</td><td id="NVOS" class="">Feb 10</td><td id="D:&lt;e" class="">Apr 5</td><td id="\CI=" class="">Budget approval from finance</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8054-b3bc-d6b234ee68fa" class="">Post recap within 15 mins to:</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8058-b10f-d7452106cef4" class="">📌 <strong>Google Doc</strong> – Updated roadmap + KPIs</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8099-9324-f7adb3d89237" class="">📌 <strong>Jira</strong> – New tickets created with owners + dates</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-806d-a877-c630148d10e1" class="">📌 <strong>Telegram</strong> – Summary for leadership (“3 priorities locked, 
budget gaps flagged”)</p></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-805c-99f5-d38fc25c0158"/></div><div style="display:contents" dir="auto"><h1 id="26fc5e6f-95bd-806c-87e0-e88b4a6540a3" class=""><strong>Decision-Making Meetings – Deep Dive</strong></h1></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-804b-81e3-c89fc975e462" class=""><strong>✅ Facilitator Checklist (Before Meeting)</strong></h3></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-808d-87a4-c67c2f6abd11" class="bulleted-list"><li style="list-style-type:disc">Gather <strong>all relevant data</strong> (financial models, supplier quotes, user feedback).</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80ef-985f-e7431bff0b60" class="bulleted-list"><li style="list-style-type:disc">Prepare <strong>a decision brief</strong> (1-page summary: context, options, pros/cons).</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80b6-b2b2-c08d55a7ba6d" class="bulleted-list"><li style="list-style-type:disc">Confirm that <strong>key decision-makers</strong> will be present (CEO, PM, Ops, Finance).</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8008-8ef3-cb76405f28f4" class="bulleted-list"><li style="list-style-type:disc">Pre-distribute data + brief in Google Doc so everyone reviews ahead of time.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8040-81e7-ea44c4f27b63" class="bulleted-list"><li style="list-style-type:disc">Block <strong>30–45 mins</strong> max — decisions should be focused, 
not brainstorming.</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80c8-ac36-f2c6b07a88de"/></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-8053-bfc3-edb79c3e3f53" class=""><strong>❓ Question Prompts (During Meeting)</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-8006-aed1-dbae322bbcfd" class="numbered-list" start="1"><li><strong>Clarify the Decision:</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8055-bc30-dc389c43d224" class="bulleted-list"><li style="list-style-type:disc">“What exact decision are we making today?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8038-a1ad-df37ab9e4f1b" class="bulleted-list"><li style="list-style-type:disc">“What does a ‘yes’ or ‘no’ mean in action?”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-805d-b99a-fe137b2d7aa5" class="numbered-list" start="2"><li><strong>Evaluate Options:</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8000-a02a-f7b9b9c8a8e0" class="bulleted-list"><li style="list-style-type:disc">“What are the trade-offs of Option A vs. 
Option B?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80e9-a891-e34efe2fac98" class="bulleted-list"><li style="list-style-type:disc">“What would make this option fail?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-806b-823e-dd3c74201909" class="bulleted-list"><li style="list-style-type:disc">“Do we have enough data to make this call now?”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80f2-9642-c32bac0b16a4" class="numbered-list" start="3"><li><strong>Assess Impact:</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8085-aa64-c618c3d07d5a" class="bulleted-list"><li style="list-style-type:disc">“What’s the cost (time, money, 
reputation) of saying yes?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80c6-a28d-d8d89abcad83" class="bulleted-list"><li style="list-style-type:disc">“What’s the cost of delaying this decision?”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80a4-8104-cae4c8d4e118" class="numbered-list" start="4"><li><strong>Assign Ownership:</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8031-9d44-ee5dc0a0b82d" class="bulleted-list"><li style="list-style-type:disc">“Who will execute once the decision is made?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-802f-bd3a-e9a0e787bb5e" class="bulleted-list"><li style="list-style-type:disc">“What does success look like and by when?”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-8007-bdc2-d91a8ea2d32a"/></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-8052-b8bf-eb84ec1a6ef6" class=""><strong>📝 Outcome Logging (End of Meeting)</strong></h3></div><div style="display:contents" dir="ltr"><table id="26fc5e6f-95bd-80cf-99e6-f75b245be564" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80e3-b3b9-ea246414985e"><th id="frrC" class="simple-table-header-color simple-table-header"><strong>Decision</strong></th><th id="ClY;" class="simple-table-header-color simple-table-header"><strong>Chosen Option</strong></th><th id="RsT_" class="simple-table-header-color simple-table-header"><strong>Owner</strong></th><th id="&gt;cLX" class="simple-table-header-color simple-table-header"><strong>Execution Date</strong></th><th id="|l_{" class="simple-table-header-color simple-table-header"><strong>Follow-up</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8057-8368-e84c3785651d"><td id="frrC" class="">Select supplier for Q3 p
roduction</td><td id="ClY;" class="">Supplier A</td><td id="RsT_" class="">Linh (Ops)</td><td id="&gt;cLX" class="">Contract signed by Feb 5</td><td id="|l_{" class="">Quality check report due Mar 1</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-809b-9bcc-c9816ab9e0c9"><td id="frrC" class="">Launch campaign</td><td id="ClY;" class="">Creative v2</td><td id="RsT_" class="">Mai (Marketing)</td><td id="&gt;cLX" class="">Live by Feb 20</td><td id="|l_{" class="">Engagement review Mar 15</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8042-8ec7-c628c2dc3eed" class="">Post recap within 15 mins to:</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-809f-befa-df53be0f8301" class="">📌 <strong>Google Doc</strong> – Decision brief updated with final choice</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-801e-be53-f09bddc2eb81" class="">📌 <strong>Jira</strong> – New tasks created for follow-up actions</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8026-ba35-dfee844f4edf" class="">📌 <strong>Telegram</strong> – Short message: “Decision made: Supplier A chosen. 
Linh owns execution.”</p></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-8012-a70c-c5df613a183b"/></div><div style="display:contents" dir="auto"><h1 id="26fc5e6f-95bd-80b9-b3ba-ddb8c05931c6" class=""><strong>Problem-Solving / Triage Meetings – Deep Dive</strong></h1></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-80f3-8358-eab95eea5d02" class=""><strong>✅ Facilitator Checklist (Before Meeting)</strong></h3></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80fd-b5b6-d177270c19ab" class="bulleted-list"><li style="list-style-type:disc">Review <strong>Jira / dashboard</strong> to see current blockers.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80ba-be3e-d94b49b16006" class="bulleted-list"><li style="list-style-type:disc">Invite <strong>only relevant stakeholders</strong> (decision-makers, owners, subject experts).</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-805f-ad3e-e9e47e33647f" class="bulleted-list"><li style="list-style-type:disc">Prepare a <strong>shared board or Google Doc</strong> with blockers pre-listed by priority.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-803f-9def-e27520486668" class="bulleted-list"><li style="list-style-type:disc">Set a <strong>strict 15–30 min agenda</strong> to stay focused on resolution.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8030-b2e1-f3ae387b29f4" class="bulleted-list"><li style="list-style-type:disc">Define success: “By the end of this meeting, 
blockers are either resolved or have a clear owner + deadline.”</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-8019-a2f4-ebb640489a64"/></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-80b5-bb8f-dca9a2d7bb79" class=""><strong>❓ Question Prompts (During Meeting)</strong></h3></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80f6-b871-f186f7e1c182" class="numbered-list" start="1"><li><strong>Identify the Blocker Clearly:</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8014-a9b7-e30dfc2112aa" class="bulleted-list"><li style="list-style-type:disc">“What exactly is stopping this from moving forward?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-800b-bacc-e283cadbb5aa" class="bulleted-list"><li style="list-style-type:disc">“Is this a decision gap, a missing resource, or unclear ownership?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-806e-830c-dd7b4df9c411" class="bulleted-list"><li style="list-style-type:disc">“What does ‘unblocked’ look like?”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-8004-8649-e697bc075957" class="numbered-list" start="2"><li><strong>Classify the Blocker:</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80c0-9f95-fff84be29fbb" class="bulleted-list"><li style="list-style-type:disc"><strong>Decision Needed</strong> – requires leadership approval.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-809d-8e21-c8f5b4f8ff15" class="bulleted-list"><li style="list-style-type:disc"><strong>Resource Gap</strong> – missing budget, tool, 
or talent.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80e9-81f0-de9e1ba71dac" class="bulleted-list"><li style="list-style-type:disc"><strong>Unclear Owner</strong> – no one accountable.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8031-97f6-c3f3950a25d9" class="bulleted-list"><li style="list-style-type:disc"><strong>Process Misalignment</strong> – conflicting timelines, workflows, or expectations.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80de-9007-ed3b5ca5cab4" class="numbered-list" start="3"><li><strong>Prioritise by Impact:</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80fa-98dc-f9a192d361fa" class="bulleted-list"><li style="list-style-type:disc">“Which blocker, if solved, 
unlocks the most progress?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-800a-b4c4-d2b0eeab86ad" class="bulleted-list"><li style="list-style-type:disc">“What will cause the biggest delay if left unresolved?”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="26fc5e6f-95bd-80f3-84a7-c36ee4e515c9" class="numbered-list" start="4"><li><strong>Move to Resolution:</strong><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80c8-b5e4-ed446e555d10" class="bulleted-list"><li style="list-style-type:disc">“Who can resolve this today?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-809f-a59e-d538c5f9f11e" class="bulleted-list"><li style="list-style-type:disc">“What is the smallest next step to get unstuck?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8049-ab95-c2d8f8020522" class="bulleted-list"><li style="list-style-type:disc">“Do we need a quick spin-off session with a smaller group?”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80c9-a284-e87d94647b63"/></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-807a-82b9-dc7fbe78423b" class=""><strong>📝 Outcome Logging (End of Meeting)</strong></h3></div><div style="display:contents" dir="ltr"><table id="26fc5e6f-95bd-80a6-8546-d0ac0c2e2bcb" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8054-a033-d53b959eabe4"><th id="hx&gt;{" class="simple-table-header-color simple-table-header"><strong>Blocker</strong></th><th id="mWUQ" class="simple-table-header-color simple-table-header"><strong>Category</strong></th><th id="UNwX" class="simple-table-header-color simple-table-header"><strong>Resolution / Next Step</strong></th><th id="[OKc" class="simple-table-header-color simple-table-header"><strong>Owner</strong></th><th id="ZOBC" c
lass="simple-table-header-color simple-table-header"><strong>Due Date</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80dd-8432-cefaaff6dfbb"><td id="hx&gt;{" class="">Artwork stuck in approval</td><td id="mWUQ" class="">Decision Needed</td><td id="UNwX" class="">Creative lead to sign-off by 3 PM</td><td id="[OKc" class="">Minh</td><td id="ZOBC" class="">Today</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-803d-afb6-e971f0286f6c"><td id="hx&gt;{" class="">Missing payment to supplier</td><td id="mWUQ" class="">Resource Gap</td><td id="UNwX" class="">Finance to release PO</td><td id="[OKc" class="">Trang</td><td id="ZOBC" class="">Friday</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8081-92a4-f5f88aa09ab6"><td id="hx&gt;{" class="">QA not scheduled</td><td id="mWUQ" class="">Unclear Owner</td><td id="UNwX" class="">Assign QA team to sprint</td><td id="[OKc" class="">Bao</td><td id="ZOBC" class="">End of Day</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80a1-a9ff-eefebd61d8f8" class="">📌 <strong>Google Doc</strong> – Meeting notes saved with decisions + owners</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8066-a915-d5d716767f5d" class="">📌 <strong>Jira</strong> – Blockers marked as “In Progress” or “Resolved”</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8094-a970-d8c11105a68c" class="">📌 <strong>Telegram</strong> – Short status post: “3 blockers cleared, 
2 escalated to leadership”</p></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-807a-a21d-dad71515fbb3"/></div><div style="display:contents" dir="auto"><h1 id="26fc5e6f-95bd-801d-befb-e90b097a438d" class=""><strong>Planning / Roadmap Sessions – Deep Dive</strong></h1></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-8078-93f1-effcb20b7326" class=""><strong>✅ Facilitator Checklist (Before Meeting)</strong></h3></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80a0-96c0-c810a175356e" class="bulleted-list"><li style="list-style-type:disc">Collect <strong>all current projects, priorities, and backlog items</strong> (from Jira, Google Sheets).</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-800f-ac6a-fa0d03483a25" class="bulleted-list"><li style="list-style-type:disc">Prepare a <strong>single view</strong> (Kanban board, roadmap slide, or FigJam) for everyone to reference.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8098-8f94-ed4394317c0d" class="bulleted-list"><li style="list-style-type:disc">Pre-align with leadership on <strong>budget, resources, and non-negotiable priorities</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8091-9464-f4af5b8c6594" class="bulleted-list"><li style="list-style-type:disc">Timebox agenda: <strong>60–90 mins</strong> for quarterly planning, <strong>30–45 mins</strong> for sprint planning.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-807f-83df-f70125faa0c0" class="bulleted-list"><li style="list-style-type:disc">Define success: “By the end of this session, 
we have a prioritised plan with owners and dates.”</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80d6-849b-c0325bf90429"/></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-800b-b886-eaec43a72b96" class=""><strong>❓ Question Prompts (During Meeting)</strong></h3></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8034-946b-e2296ee872ba" class=""><strong>1. Set the Context:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80ef-8bc1-c921db46c73d" class="bulleted-list"><li style="list-style-type:disc">“What are the top 3 outcomes we must deliver this quarter?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8098-a0e8-e3ab3655c031" class="bulleted-list"><li style="list-style-type:disc">“What is the business impact if we hit or miss these goals?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8088-8513-f1015f158eb0" class="bulleted-list"><li style="list-style-type:disc">“Are there non-negotiables (compliance, customer commitments, investor promises) we must include?”</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-808b-9ac8-cadece1ce1db" class=""><strong>2. 
Prioritise Initiatives:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8023-9d17-e44a98e5419a" class="bulleted-list"><li style="list-style-type:disc">“Which initiatives have the highest ROI or urgency?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8097-8e27-fe09cc6204de" class="bulleted-list"><li style="list-style-type:disc">“What can be safely delayed or deprioritised?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8091-b0f0-eb0c81f8a323" class="bulleted-list"><li style="list-style-type:disc">“Are there dependencies that must be resolved first?”</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80cf-a0dd-e9a176e50283" class=""><strong>3. Allocate Resources:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-806d-807f-df06fc9c4952" class="bulleted-list"><li style="list-style-type:disc">“Do we have enough design/engineering/supplier capacity for this plan?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80ce-a25c-fb6a95c5d9e2" class="bulleted-list"><li style="list-style-type:disc">“What support is needed from finance, marketing, or leadership?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8034-9861-c399bb9aa043" class="bulleted-list"><li style="list-style-type:disc">“Do we need to bring in external suppliers or freelancers?”</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-809e-8e4f-ffd20384f1ce" class=""><strong>4. 
Define Success Metrics:</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-803f-8c19-e38208ee0317" class="bulleted-list"><li style="list-style-type:disc">“What does success look like for each initiative?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80a0-a7e4-e757096d68aa" class="bulleted-list"><li style="list-style-type:disc">“How will we measure progress (KPI, milestone, 
Jira ticket)?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8007-b976-ed0f7db784ea" class="bulleted-list"><li style="list-style-type:disc">“Who owns this and is accountable for delivery?”</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-8029-9f72-f36e1ad8caeb"/></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-8093-b2de-e6fa45dded6a" class=""><strong>📝 Outcome Logging (End of Meeting)</strong></h3></div><div style="display:contents" dir="ltr"><table id="26fc5e6f-95bd-80bf-aa1c-eb2306f15c0c" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8004-b6f0-e066c0be49fe"><th id="VtT^" class="simple-table-header-color simple-table-header"><strong>Initiative</strong></th><th id="HMhG" class="simple-table-header-color simple-table-header"><strong>Owner</strong></th><th id="BTx{" class="simple-table-header-color simple-table-header"><strong>Start Date</strong></th><th id="|mVJ" class="simple-table-header-color simple-table-header"><strong>Target Completion</strong></th><th id="&lt;x\k" class="simple-table-header-color simple-table-header"><strong>KPI / Success Metric</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-802b-9d21-d0aa608916a1"><td id="VtT^" class="">New Supplier Onboarding</td><td id="HMhG" class="">Mai</td><td id="BTx{" class="">Mar 5</td><td id="|mVJ" class="">Mar 31</td><td id="&lt;x\k" class="">100% suppliers trained + contracts signed</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8098-b6cd-cd3f786548e8"><td id="VtT^" class="">Q2 Campaign Launch</td><td id="HMhG" class="">Duy</td><td id="BTx{" class="">Apr 1</td><td id="|mVJ" class="">Apr 30</td><td id="&lt;x\k" class="">≥10% engagement increase on social</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8074-a583-c1c7e881a44d"><td id="VtT^" c
lass="">Inventory Optimisation</td><td id="HMhG" class="">Trang</td><td id="BTx{" class="">Ongoing</td><td id="|mVJ" class="">End of Q2</td><td id="&lt;x\k" class="">Reduce stockouts by 20%</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80a6-b0a0-c3dd060398d5" class="">📌 <strong>Jira / Roadmap Tool</strong> – Updated live during session.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8092-9c36-eba1e04953e8" class="">📌 <strong>Google Doc</strong> – Final roadmap shared within 24 hours.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8029-b965-e23aad98a0b5" class="">📌 <strong>Telegram</strong> – Summary post: “Q2 roadmap locked: 3 major initiatives, owners assigned.”</p></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80d7-8d99-dc82e4b0d27e"/></div><div style="display:contents" dir="auto"><h1 id="26fc5e6f-95bd-80af-8fb0-feb603c72233" class=""><strong>Innovation / Ideation Workshops – Deep Dive</strong></h1></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-8088-8cef-f92625310cd0" class=""><strong>✅ Facilitator Checklist (Before Meeting)</strong></h3></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-805b-b7c1-c908e1ba20e0" class="bulleted-list"><li style="list-style-type:disc">Define <strong>problem statement or opportunity area</strong> (1–2 sentences).</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-806e-aed6-e62fe2efb349" class="bulleted-list"><li style="list-style-type:disc">Set a <strong>clear objective</strong>: “Generate 20 ideas and pick top 3 to test.”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-803b-a2ac-d1726decee3e" class="bulleted-list"><li style="list-style-type:disc">Prepare <strong>collaboration space</strong> (Figma/Miro board with idea templates, 
sticky notes).</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8038-82aa-e0f23f0f620c" class="bulleted-list"><li style="list-style-type:disc">Invite a <strong>diverse group</strong> (marketing, tech, suppliers if relevant).</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-802b-a9fe-c3e5bd13e73b" class="bulleted-list"><li style="list-style-type:disc">Timebox: 45–90 mins, with <strong>warm-up activity</strong> to encourage creativity.</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-8034-b53e-c79116c0e07b"/></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-80ef-81ff-cc93ddf35549" class=""><strong>❓ Question Prompts (During Meeting)</strong></h3></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-808d-b417-e21f567e4c29" class=""><strong>1. Warm-Up (5 mins)</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8008-8a9f-e5157d932934" class="bulleted-list"><li style="list-style-type:disc">“If budget and resources were unlimited, what would we do?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8079-bd8f-f34575596bc9" class="bulleted-list"><li style="list-style-type:disc">“What’s the craziest idea we could try that might work?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8055-b8b5-f051f59682d7" class="bulleted-list"><li style="list-style-type:disc">“If a competitor beat us tomorrow, what would they have done?”</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80c5-be76-d042b5172b3e" class=""><strong>2. 
Idea Generation (20–30 mins)</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-806f-bffd-eca3542de749" class="bulleted-list"><li style="list-style-type:disc">“Generate at least 10 ideas each — quantity over quality.”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8075-b49f-c5f92d0f392c" class="bulleted-list"><li style="list-style-type:disc">“What do we know from customers/suppliers that others don’t?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8046-800e-cca3499eb251" class="bulleted-list"><li style="list-style-type:disc">“How could we 10x impact with half the cost?”</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8036-b41b-e4749e9ae047" class=""><strong>3. Idea Clustering + Voting (15–20 mins)</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8013-afc7-eab6dc6dfc56" class="bulleted-list"><li style="list-style-type:disc">Group ideas by theme (pricing, product, campaign, ops).</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-801e-aaf0-cbcc5ba4a917" class="bulleted-list"><li style="list-style-type:disc">Use dot voting (Figma or Miro) to pick top ideas.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80ea-98e9-d45d4c72fd73" class="bulleted-list"><li style="list-style-type:disc">Ask: “Would this idea excite a customer? Would it excite a supplier?”</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8022-a8f3-f69d5435d2fc" class=""><strong>4. 
Select for Action (15 mins)</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8069-a856-f3ca74b4bf38" class="bulleted-list"><li style="list-style-type:disc">“Which top 3 ideas are we committed to testing?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8029-8bfe-fb3e671d278f" class="bulleted-list"><li style="list-style-type:disc">“Who owns the prototype or first experiment?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8095-b679-e3645194a452" class="bulleted-list"><li style="list-style-type:disc">“What is the cheapest test we can run in 2 weeks?”</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80b5-a0a8-e2419fc6a7ef"/></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-80d0-8ab9-dc2fbbc4dee1" class=""><strong>📝 Outcome Logging (End of Meeting)</strong></h3></div><div style="display:contents" dir="ltr"><table id="26fc5e6f-95bd-80f1-9ffe-cf280bab69af" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8076-a6e0-cf629d1ce069"><th id="tJEA" class="simple-table-header-color simple-table-header"><strong>Idea / Concept</strong></th><th id="BTIy" class="simple-table-header-color simple-table-header"><strong>Owner</strong></th><th id="ep{\" class="simple-table-header-color simple-table-header"><strong>Next Step</strong></th><th id="Yvs=" class="simple-table-header-color simple-table-header"><strong>Test Date</strong></th><th id="Ssm|" class="simple-table-header-color simple-table-header"><strong>Success Metric</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8056-bcb6-f4aa1d1c356b"><td id="tJEA" class="">Smart Supplier Portal</td><td id="BTIy" class="">Quang</td><td id="ep{\" class="">Build wireframe in Figma</td><td id="Yvs=" class="">Apr 10</td><td id="Ssm|" class="">Supplier adoption ≥70%</td></tr></div><div s
tyle="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80eb-9ec6-d9e9dfe5ee25"><td id="tJEA" class="">TikTok Creator Campaign</td><td id="BTIy" class="">Thao</td><td id="ep{\" class="">Secure 5 influencers</td><td id="Yvs=" class="">Apr 15</td><td id="Ssm|" class="">Reach ≥100k views</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80b8-928e-d32e0c2d591d"><td id="tJEA" class="">Sustainable Packaging Trial</td><td id="BTIy" class="">Hoa</td><td id="ep{\" class="">Source samples from supplier</td><td id="Yvs=" class="">Apr 30</td><td id="Ssm|" class="">20% cost-neutral adoption</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80e5-984a-cec9e05beaa1" class="">📌 <strong>Figma/Miro</strong> – Screenshots of final board saved.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8021-9052-d126a063575d" class="">📌 <strong>Jira</strong> – Experiments created as tickets with deadlines.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80b6-a414-d04bf9690ec1" class="">📌 <strong>Telegram</strong> – Post top 3 ideas with owners to create public accountability.</p></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80ca-9144-c81405a73561"/></div><div style="display:contents" dir="auto"><h1 id="26fc5e6f-95bd-80d8-a240-f6fd480506e6" class=""><strong>Stakeholder Reviews – Deep Dive</strong></h1></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-80c9-b857-e65aa2a950c9" class=""><strong>✅ Facilitator Checklist (Before Meeting)</strong></h3></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80a6-b5e4-d5b77ecbdd19" class="bulleted-list"><li style="list-style-type:disc">Define <strong>objective</strong>: decision, approval, 
or funding ask.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80b1-bcf2-fff2c56d9342" class="bulleted-list"><li style="list-style-type:disc">Prepare <strong>pre-read deck</strong> (Google Slides) with:<div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-807d-92f1-fb12b8ef4488" class="bulleted-list"><li style="list-style-type:circle">Latest metrics (sales, margin, pipeline, supplier KPIs).</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80eb-b921-ca80b2f28b00" class="bulleted-list"><li style="list-style-type:circle">Top 3 wins, top 3 risks.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80ce-8c67-e411322510b7" class="bulleted-list"><li style="list-style-type:circle">Key decisions needed (with recommendation).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8067-9f42-ddb5bd8b8b9c" class="bulleted-list"><li style="list-style-type:disc">Circulate <strong>pre-reads 48 hours in advance</strong> so leaders come prepared.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80c2-bf1b-cd61e3bee2b7" class="bulleted-list"><li style="list-style-type:disc">Confirm attendees and decision-makers — no observers unless required.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8051-90cb-c2afdd5bf511" class="bulleted-list"><li style="list-style-type:disc">Timebox: 30–60 mins for exec reviews, 60–90 mins for board.</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-802c-ba54-c45cd2cf46de"/></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-800a-8075-dede74eb5969" class=""><strong>❓ Question Prompts (During Meeting)</strong></h3></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8094-a011-ec057dbd91ea" class=""><strong>1. 
Opening Alignment (5 mins)</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-806e-8c94-f8775f60b4a9" class="bulleted-list"><li style="list-style-type:disc">“Are there any urgent risks or changes we need to address upfront?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-803a-9d4b-f8c74314cd10" class="bulleted-list"><li style="list-style-type:disc">“Has everyone reviewed the pre-read?” (Skip recap if yes.)</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-802f-b989-f2371385e1ba" class=""><strong>2. Business Review (15–20 mins)</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8021-b4c7-d9c110940e82" class="bulleted-list"><li style="list-style-type:disc">“What are the top 3 insights from this data?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80f8-816b-de2938be21cb" class="bulleted-list"><li style="list-style-type:disc">“Where are we ahead, and where are we falling behind?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80ba-ac35-c0041e710039" class="bulleted-list"><li style="list-style-type:disc">“Are there critical risks requiring escalation?”</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80b0-9686-fce750aabf2f" class=""><strong>3. 
Decision / Approval Items (20–30 mins)</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8016-a6a6-f10492733a08" class="bulleted-list"><li style="list-style-type:disc">“Do we have enough information to approve this now?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80ce-952b-fcc648634451" class="bulleted-list"><li style="list-style-type:disc">“What are the alternatives if we do not approve?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80a2-b903-f775fe3fdd56" class="bulleted-list"><li style="list-style-type:disc">“What is the expected ROI or risk mitigation?”</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8000-8859-e1b48dccf5b9" class=""><strong>4. 
Resource Alignment (5–10 mins)</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80e5-a229-d41fa70240a6" class="bulleted-list"><li style="list-style-type:disc">“What extra resources or budget are required?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8049-8ddb-dda4f9049dc6" class="bulleted-list"><li style="list-style-type:disc">“Who will own delivery and by when?”</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-8033-957e-fd548851effb"/></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-8089-977f-e75b4ac1ea68" class=""><strong>📝 Outcome Logging (End of Meeting)</strong></h3></div><div style="display:contents" dir="ltr"><table id="26fc5e6f-95bd-8088-9c64-f85fa26dcd74" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80a1-a10d-c3abf8769ebd"><th id="CaCK" class="simple-table-header-color simple-table-header"><strong>Decision / Approval</strong></th><th id="IxzX" class="simple-table-header-color simple-table-header"><strong>Owner</strong></th><th id="s;_&lt;" class="simple-table-header-color simple-table-header"><strong>Due Date</strong></th><th id="cX;l" class="simple-table-header-color simple-table-header"><strong>Follow-Up</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-802e-a426-e12f82c832bf"><td id="CaCK" class="">Approve $50k supplier investment</td><td id="IxzX" class="">CFO</td><td id="s;_&lt;" class="">Apr 12</td><td id="cX;l" class="">ROI report due in Q2 review</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80ee-a4d0-d35d643ea498"><td id="CaCK" class="">Greenlight new product SKU</td><td id="IxzX" class="">COO</td><td id="s;_&lt;" class="">Apr 30</td><td id="cX;l" class="">Launch plan in next exec call</td></tr></div><div style="display:contents" dir="ltr"><tr i
d="26fc5e6f-95bd-80f3-a24b-cfdfbf18c8ad"><td id="CaCK" class="">Expand marketing spend by 10%</td><td id="IxzX" class="">CMO</td><td id="s;_&lt;" class="">Immediate</td><td id="cX;l" class="">Updated media plan to board</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80bd-990e-d40eb141b24e" class="">📌 <strong>Google Docs / Slides</strong> – Updated live during meeting, shared immediately after.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-804c-b5d0-e3caaf73cbea" class="">📌 <strong>Jira</strong> – Strategic initiatives tracked as epics with owners.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8089-876d-da9e56679b60" class="">📌 <strong>Telegram</strong> – Post summary in leadership channel for visibility.</p></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-801e-97f9-cf42d3516ba3"/></div><div style="display:contents" dir="auto"><h1 id="26fc5e6f-95bd-804c-94ca-c35f3264cd82" class=""><strong>Retrospectives / Post-Mortems – Deep Dive</strong></h1></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-80d3-9b65-d59c2a9d47fe" class=""><strong>✅ Facilitator Checklist (Before Session)</strong></h3></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8070-9100-d242b907df42" class="bulleted-list"><li style="list-style-type:disc">Define <strong>scope</strong>: which project, campaign, sprint, or incident are we reviewing?</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80cc-9502-c16145cb33f4" class="bulleted-list"><li style="list-style-type:disc">Gather <strong>data + facts</strong>: Jira tickets closed, budgets used, delivery times, supplier reports, 
campaign metrics.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80ef-ad92-c7b3b683a682" class="bulleted-list"><li style="list-style-type:disc">Prepare a simple <strong>timeline</strong> of events (key milestones + issues).</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8021-a76c-dd11dc0ef2a8" class="bulleted-list"><li style="list-style-type:disc">Invite <strong>only relevant participants</strong>: project team, stakeholders, decision-makers.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-804d-b280-f010455da966" class="bulleted-list"><li style="list-style-type:disc">Set psychological safety: frame the session as <strong>blame-free learning</strong>, not finger-pointing.</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80a5-aa76-f5647737c1b2"/></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-807c-8079-efbd787eb261" class=""><strong>❓ Question Prompts (During Session)</strong></h3></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8026-a638-ee6d93f778cd" class=""><strong>1. Opening Context (5 mins)</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-806a-9ae5-ebdc18074034" class="bulleted-list"><li style="list-style-type:disc">“What was the original goal and success metric for this project?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80fe-9590-efc6e62ea68e" class="bulleted-list"><li style="list-style-type:disc">“What constraints did we face — budget, time, resources?”</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80b0-9115-f84e726b93cd" class=""><strong>2. 
What Went Well (10–15 mins)</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-801c-be86-eaaaf76f55a6" class="bulleted-list"><li style="list-style-type:disc">“What worked that we should repeat?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-802f-9c4f-d2a634a92131" class="bulleted-list"><li style="list-style-type:disc">“Where did we exceed expectations?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-803b-9c80-de21c34f7074" class="bulleted-list"><li style="list-style-type:disc">“Which decisions or processes saved us time or cost?”</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8072-a7ed-ef18442e8a4f" class=""><strong>3. What Didn’t Work (15–20 mins)</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80d8-9a8f-fc3a0f356908" class="bulleted-list"><li style="list-style-type:disc">“Where did we miss deadlines or quality targets?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80ac-b883-e9330fd01f25" class="bulleted-list"><li style="list-style-type:disc">“What was the root cause — process gap, unclear ownership, supplier issue?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8003-b0be-efe45eab82a3" class="bulleted-list"><li style="list-style-type:disc">“Which problems could have been caught earlier?”</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8091-a9f5-e8375e4e0c2c" class=""><strong>4. 
What We Change Next Time (10 mins)</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80c2-9c1a-fe484dbad3f5" class="bulleted-list"><li style="list-style-type:disc">“Which process step do we adjust or add?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80fa-bc45-cc91d46a11af" class="bulleted-list"><li style="list-style-type:disc">“What new checklist, dashboard, 
or automation do we need?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8016-a1e3-ff662bbd6a66" class="bulleted-list"><li style="list-style-type:disc">“Who will own implementing this change?”</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-8039-845a-fca2397890b8"/></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-8068-97b5-e5196b39777d" class=""><strong>📝 Outcome Logging (End of Session)</strong></h3></div><div style="display:contents" dir="ltr"><table id="26fc5e6f-95bd-8082-bca1-cf952a08ffed" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80ff-a512-e2200f26f3a6"><th id="lrk:" class="simple-table-header-color simple-table-header"><strong>Lesson / Action Item</strong></th><th id="V}VQ" class="simple-table-header-color simple-table-header"><strong>Owner</strong></th><th id="_yPa" class="simple-table-header-color simple-table-header"><strong>Deadline</strong></th><th id="^YZm" class="simple-table-header-color simple-table-header"><strong>Loop Closure</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80cf-8135-c49378d53ee7"><td id="lrk:" class="">Improve supplier onboarding checklist</td><td id="V}VQ" class="">Ops Lead</td><td id="_yPa" class="">Apr 15</td><td id="^YZm" class="">Updated doc shared in supplier handbook</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8015-b630-edc75d94fd42"><td id="lrk:" class="">Add quality-control checkpoint before shipment</td><td id="V}VQ" class="">QA Manager</td><td id="_yPa" class="">May 1</td><td id="^YZm" class="">New step live in SOP</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80cd-9b74-dbf7c51e9dda"><td id="lrk:" class="">Automate campaign budget tracking in Google Sheets</td><td id="V}VQ" class="">Marketing Ops</td><td id="_yPa" class="">Apr 22</td><td id="^YZm" c
lass="">Tool demoed in next planning session</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8021-992e-fd4137aee781" class="">📌 <strong>Google Docs</strong> – Create a dedicated “Lessons Learned” document linked to project folder.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-801d-93bb-c57ad36611fe" class="">📌 <strong>Jira</strong> – Log systemic issues as tasks with clear owners and due dates.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8091-805f-efc7a3d8e9f7" class="">📌 <strong>Team Handbook</strong> – Update SOPs, templates, or checklists immediately so future teams benefit.</p></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80cc-b358-dfc161b44813"/></div><div style="display:contents" dir="auto"><h1 id="26fc5e6f-95bd-808e-b6b9-c5cc4e9bfaf7" class=""><strong>1:1s &amp; 
Coaching Sessions – Deep Dive</strong></h1></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-8087-ac2f-fa12c9275cfc" class=""><strong>✅ Facilitator Checklist (Before Session)</strong></h3></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80e8-9cc0-f0be542727aa" class="bulleted-list"><li style="list-style-type:disc"><strong>Review last 1:1 notes</strong>: open loops, previous commitments.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-809f-ae81-f2b0690c5751" class="bulleted-list"><li style="list-style-type:disc">Pull <strong>Jira board / performance metrics</strong> relevant to this person’s work.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8022-857b-dd375e2a3861" class="bulleted-list"><li style="list-style-type:disc">Note <strong>wins</strong> to recognise and areas needing support.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8053-9d8d-df2fa5ede39c" class="bulleted-list"><li style="list-style-type:disc">Prepare 1–2 open questions about <strong>career growth</strong> or skill development.</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80c3-bdd9-d38825119925" class="bulleted-list"><li style="list-style-type:disc">Block a quiet, uninterrupted space (or private call channel on Telegram).</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80c2-bc19-dea34bec9fad"/></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-80a0-8cc2-df0d78fb203e" class=""><strong>❓ Question Prompts (During Session)</strong></h3></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80c7-82ad-e11560b977d2" class=""><strong>1. 
Opening (5 mins)</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8029-a4cb-d80523e2fb5a" class="bulleted-list"><li style="list-style-type:disc">“What’s going well for you right now?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80f7-9307-c86f107cedf3" class="bulleted-list"><li style="list-style-type:disc">“What are you most proud of since our last 1:1?”</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8095-8bb5-d373e231fbe0" class=""><strong>2. Workload + Priorities (10 mins)</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80a7-8e6e-d44a1b835918" class="bulleted-list"><li style="list-style-type:disc">“Are your current priorities clear?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8083-86a7-e7819857c3a4" class="bulleted-list"><li style="list-style-type:disc">“What feels blocked or confusing?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8053-bca9-d5da011dfe18" class="bulleted-list"><li style="list-style-type:disc">“Do you have what you need to succeed this week?”</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80e6-b021-c828118c161a" class=""><strong>3. 
Development &amp; Growth (10 mins)</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80d2-8cde-ee7ff04ea457" class="bulleted-list"><li style="list-style-type:disc">“What skill do you want to strengthen this quarter?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80c1-a947-c96b6e65f7a3" class="bulleted-list"><li style="list-style-type:disc">“Where do you feel underutilised?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-802c-9aa8-de6f6d21629b" class="bulleted-list"><li style="list-style-type:disc">“Would you like to shadow or lead an upcoming project?”</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-803f-8fad-e2cbc6eb7b48" class=""><strong>4. Feedback Exchange (5–10 mins)</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80ac-994a-f271f00d6ee8" class="bulleted-list"><li style="list-style-type:disc">“What feedback do you have for me?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-8097-9fbf-f91a93b55717" class="bulleted-list"><li style="list-style-type:disc">“How can I better support you?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-803b-8f4c-c08c404f6244" class="bulleted-list"><li style="list-style-type:disc">Offer 1–2 pieces of feedback tied to behaviours, not personality.</li></ul></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80b3-abf9-e3268cf9a413" class=""><strong>5. 
Wellbeing &amp; 
Culture Check (5 mins)</strong></p></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80e9-847f-cbb256acafe8" class="bulleted-list"><li style="list-style-type:disc">“How are you feeling about workload and balance?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80a6-ad39-fea4a3096f5f" class="bulleted-list"><li style="list-style-type:disc">“Do you feel connected to the team and mission?”</li></ul></div><div style="display:contents" dir="auto"><ul id="26fc5e6f-95bd-80d2-896d-d43bd69232ee" class="bulleted-list"><li style="list-style-type:disc">“Anything hurting morale that we need to address?”</li></ul></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-8087-8548-d62022939ee0"/></div><div style="display:contents" dir="auto"><h3 id="26fc5e6f-95bd-8088-9b3d-f810779d3061" class=""><strong>📝 Outcome Logging (End of Session)</strong></h3></div><div style="display:contents" dir="ltr"><table id="26fc5e6f-95bd-80fd-99d8-e981650c94f6" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8055-9a51-cb3d87fe6ae1"><th id="@aRo" class="simple-table-header-color simple-table-header"><strong>Commitment / Action</strong></th><th id="ydEi" class="simple-table-header-color simple-table-header"><strong>Owner</strong></th><th id="b:{q" class="simple-table-header-color simple-table-header"><strong>Due Date</strong></th><th id="r|tm" class="simple-table-header-color simple-table-header"><strong>Loop Closure</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80da-a2d7-ea5de0779556"><td id="@aRo" class="">Reprioritise design tasks for Product X</td><td id="ydEi" class="">Manager</td><td id="b:{q" class="">Friday</td><td id="r|tm" class="">Jira board updated</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-80b2-b5a5-d2523daf1fc3"><td id="@aRo" class="">Enrol in copywriting m
icro-course</td><td id="ydEi" class="">Team Member</td><td id="b:{q" class="">Apr 10</td><td id="r|tm" class="">Completion shared in next 1:1</td></tr></div><div style="display:contents" dir="ltr"><tr id="26fc5e6f-95bd-8040-824a-e8e82d1adbba"><td id="@aRo" class="">Schedule shadow session with Supplier Team</td><td id="ydEi" class="">Ops Lead</td><td id="b:{q" class="">Apr 18</td><td id="r|tm" class="">Debrief notes in Google Doc</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-80db-abb6-e9f56180b453" class="">📌 <strong>Google Doc</strong> – Maintain a shared 1:1 log per team member (restricted access).</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-806a-9802-df4d87d6cec2" class="">📌 <strong>Telegram / Slack</strong> – Share quick wins or follow-ups right after session.</p></div><div style="display:contents" dir="auto"><p id="26fc5e6f-95bd-8066-ba47-fab8cc5a99f4" class="">📌 <strong>Career Development Tracker</strong> – Record skill-building commitments so growth is measurable over time.</p></div><div style="display:contents" dir="auto"><hr id="26fc5e6f-95bd-80c6-af93-e8ed521b34ce"/></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
