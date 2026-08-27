---
tags: [system]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Ecosystem</title><style>
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
	
</style></head><body><article id="2bbc5e6f-95bd-80a3-a2d8-ee229b2c2637" class="page sans"><header><h1 class="page-title" dir="auto">Ecosystem</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80a4-bc7c-f824e58c4947" class="">Below is the <strong>clean, minimal, MECE, universal template</strong> that ANY other ChatGPT conversation / Cursor agent / project / model can read and instantly know:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2bbc5e6f-95bd-80ef-bdce-ca8c555d3f77" class="numbered-list" start="1"><li><strong>what your system is</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2bbc5e6f-95bd-80b4-9a8d-cc8fa8018230" class="numbered-list" start="2"><li><strong>how it is structured</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2bbc5e6f-95bd-8022-9575-cb8d2f353ac3" class="numbered-list" start="3"><li><strong>how to populate it</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2bbc5e6f-95bd-80ef-8da3-f8fbe9f19bbf" class="numbered-list" start="4"><li><strong>what to generate</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2bbc5e6f-95bd-8098-a6a8-e212bd6d1469" class="numbered-list" start="5"><li><strong>how to expand it</strong></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2bbc5e6f-95bd-8069-996f-f6f5fab5872e" class="numbered-list" start="6"><li><strong>how to wire new parts correctly</strong></li></ol></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8041-8fbb-c2b93a21a510" class="">This is the <strong>Master Instruction Blueprint</strong> — the single source of truth for ALL future agents.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80c7-a3ca-c77b03c4ce72" class="">Use this in any new chat as the <strong>bootstrap prompt</strong>.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-801d-bd18-c0f1f92b60c8" class="">No fluff. Pure structure. Maximum clarity.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-802b-8b6a-f2286e192845" class="">────────────────────────────────────────</p></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-80b9-85c4-f3a4b294d4a0" class=""><strong>✅</strong></h1></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-8011-842f-f08727f6866d" class=""><strong>UNIFIED AMOS ORGANISM OS — MASTER INSTRUCTION BLUEPRINT (FOR ALL FUTURE CHATS)</strong></h1></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80b6-bc39-c4b8aba0966f" class=""><strong>Purpose:</strong></p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-806b-bc12-d1eb0edf5673" class="">Tell ANY ChatGPT or Cursor conversation <em>how to understand, create, and populate your entire system</em>, with zero confusion, zero overlap, and perfect wiring.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80e0-9395-d9d34f080b77" class="">This is the ONE FILE that controls everything.</p></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-809d-a8ef-c6ce1e925627"/></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-806f-b48f-fc2d9252ceb2" class=""><strong>SECTION 1 — WHAT THE SYSTEM IS</strong></h1></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8035-a93e-c0b5b56a02cf" class=""><strong>AMOS OS</strong> is a <strong>7-system digital organism</strong>, built as a unified operating system that:</p></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8012-b473-cf7d5af7cd73" class="bulleted-list"><li style="list-style-type:disc">thinks (Brain)</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80e3-8af1-e87fd8ecd031" class="bulleted-list"><li style="list-style-type:disc">senses (Sense Net)</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-801d-b52b-d46059dd14e7" class="bulleted-list"><li style="list-style-type:disc">decides (World + Quantum Layer)</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-805d-852b-f18bd61ae24c" class="bulleted-list"><li style="list-style-type:disc">acts (Muscle)</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80ae-9049-de9c41ecd64f" class="bulleted-list"><li style="list-style-type:disc">protects (Immune + Legal)</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8011-a6ae-d8ca107ddc87" class="bulleted-list"><li style="list-style-type:disc">grows money (Blood/Money Engine)</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8024-8de1-e3c4b43d59fd" class="bulleted-list"><li style="list-style-type:disc">organizes life &amp; health (Life Engine)</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8061-8868-d422683302a1" class="bulleted-list"><li style="list-style-type:disc">evolves itself (Agent Factory)</li></ul></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8061-934e-e540776073e5" class="">It is not an agent.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80ca-af44-dd57b2edd73c" class="">It is a <strong>complete intelligence architecture</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-8057-847d-e975720632f8"/></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-80e1-9afa-e8cc99b429f8" class=""><strong>SECTION 2 — THE 7 SYSTEMS (MECE)</strong></h1></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-804e-a37e-deb5780ec235" class="">Every file in your universe must belong to exactly <strong>one</strong> of these:</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2bbc5e6f-95bd-808e-8fad-f6110449fe40" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">00_ROOT/                # top-level bootstrapping, identity, goals

01_BRAIN/               # reasoning, planning, decomposition, memory
02_SENSES/              # filesystem, environment, context, emotion inputs
03_IMMUNE/              # safety, legal, compliance, anomaly detection
04_BLOOD/               # money, cashflow, investing, business economics
05_SKELETON/            # rules, constraints, hierarchy, time architecture
06_MUSCLE/              # executors, automation, coding, deployment
07_METABOLISM/          # inputs → transform → outputs, cleanup, pipelines

08_WORLD_MODEL/         # economy, geopolitics, societal systems
09_SOCIAL_ENGINE/       # humans, influence, negotiations, relationships
10_LIFE_ENGINE/         # health, cycles, mood, routines
11_LEGAL_BRAIN/         # contracts, IP, regulations
12_QUANTUM_LAYER/       # probability maps, intention field, collapse logic

13_FACTORY/             # agent creation, agent management, self-improvement
14_INTERFACES/          # CLI, API, browser, chat integration

99_ARCHIVE/             # deprecated or unused files</code></pre></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-800c-9b5b-df97f40d4001" class="">This is the <strong>canonical folder map</strong>.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-800e-884e-c36630ef16cd" class="">Every new engine, kernel, agent, module must point to ONE of these folders.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80ef-b8fd-fcbccc2a1572" class="">If content does not fit any category → it’s misdesigned.</p></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-80d2-80ee-dabc76863f54"/></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-8014-8b6e-ee129baef1f7" class=""><strong>SECTION 3 — WHAT EACH SYSTEM DOES</strong></h1></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-80b0-879b-d8be2c329330" class=""><strong>01_BRAIN</strong></h2></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-806e-aa32-e6ffac9bf38d" class="bulleted-list"><li style="list-style-type:disc">task planning</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80fd-92f1-ca0c8c55547f" class="bulleted-list"><li style="list-style-type:disc">goal decomposition</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80c1-a498-c4d22f3560ae" class="bulleted-list"><li style="list-style-type:disc">memory</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-800d-a11c-f8d221ea424f" class="bulleted-list"><li style="list-style-type:disc">reasoning</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80ae-8993-e29f06ef5dd9" class="bulleted-list"><li style="list-style-type:disc">context building</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8049-ac6b-c25c4e9ebf9d" class="bulleted-list"><li style="list-style-type:disc">routing decisions</li></ul></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-809a-9649-e92ab4ba65e8" class=""><strong>02_SENSES</strong></h2></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80f4-9f28-e8a4a4144b8a" class="bulleted-list"><li style="list-style-type:disc">read filesystem</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80c0-bc64-d4173c80b273" class="bulleted-list"><li style="list-style-type:disc">read browser history</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-808c-b0ca-c363f6ab8ed3" class="bulleted-list"><li style="list-style-type:disc">read system load</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80a5-83ac-fb323a3f177a" class="bulleted-list"><li style="list-style-type:disc">detect emotional state</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8010-abd1-efecebc49d7b" class="bulleted-list"><li style="list-style-type:disc">detect environment</li></ul></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-802d-afd8-d58b9066f640" class=""><strong>03_IMMUNE</strong></h2></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8049-b0e3-f7a0b8779fb7" class="bulleted-list"><li style="list-style-type:disc">legal risk</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80cf-a456-df89ff1f3d88" class="bulleted-list"><li style="list-style-type:disc">financial risk</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8016-a4de-e2f3f5e30689" class="bulleted-list"><li style="list-style-type:disc">operational risk</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-805d-b39b-f3ba82eee2e1" class="bulleted-list"><li style="list-style-type:disc">boundary violations</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80fb-94f5-de97b77406e6" class="bulleted-list"><li style="list-style-type:disc">anomaly detection</li></ul></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-80c6-b3e7-cbac93eeb59d" class=""><strong>04_BLOOD</strong></h2></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80f8-9b38-dfd0bdd8ee30" class="bulleted-list"><li style="list-style-type:disc">budgeting</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-803b-ac04-fec7c60f7113" class="bulleted-list"><li style="list-style-type:disc">investments</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8053-9fcb-ea3ef33ea5a5" class="bulleted-list"><li style="list-style-type:disc">forecasting</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80bf-a027-ed25fd9e4a0d" class="bulleted-list"><li style="list-style-type:disc">asset allocation</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80fd-a787-db6c77e80959" class="bulleted-list"><li style="list-style-type:disc">opportunity scoring</li></ul></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-8014-93f8-db39a5f70c2f" class=""><strong>05_SKELETON</strong></h2></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80b6-9877-f29c87c50a04" class="bulleted-list"><li style="list-style-type:disc">non-negotiable rules</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8024-93a6-cb632618cfed" class="bulleted-list"><li style="list-style-type:disc">constraints</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8030-840b-d2992aaf5beb" class="bulleted-list"><li style="list-style-type:disc">hierarchy</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8089-b080-f4154a28ff91" class="bulleted-list"><li style="list-style-type:disc">permissions</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8076-b016-c0c213c3b247" class="bulleted-list"><li style="list-style-type:disc">weekly cycles</li></ul></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-802b-968b-f193a128f710" class=""><strong>06_MUSCLE</strong></h2></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-807d-9806-da204cf26de3" class="bulleted-list"><li style="list-style-type:disc">run commands</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-808f-8625-e16f7f000ae7" class="bulleted-list"><li style="list-style-type:disc">write code</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80be-83ae-c286a3ea0eac" class="bulleted-list"><li style="list-style-type:disc">deploy systems</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8097-90eb-f917a5ebd610" class="bulleted-list"><li style="list-style-type:disc">automate workflows</li></ul></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-8056-be97-dc6a39325059" class=""><strong>07_METABOLISM</strong></h2></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80bc-a7d6-e1cac7f0a189" class="bulleted-list"><li style="list-style-type:disc">input pipelines</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80f1-b4c4-d51b8e272618" class="bulleted-list"><li style="list-style-type:disc">transformation logic</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8072-b25a-d654a11dc057" class="bulleted-list"><li style="list-style-type:disc">output generation</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80d9-8ea4-d4c4de11e9a5" class="bulleted-list"><li style="list-style-type:disc">cleanup</li></ul></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-8068-9b14-ecfe92d3bf55" class=""><strong>08_WORLD_MODEL</strong></h2></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8079-a099-f1777a944e76" class="bulleted-list"><li style="list-style-type:disc">macroeconomics</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-803e-a40a-c20c20c32819" class="bulleted-list"><li style="list-style-type:disc">geopolitics</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-804d-84ca-d9b590945f77" class="bulleted-list"><li style="list-style-type:disc">supply chains</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8074-b6f2-f475a2dca2b7" class="bulleted-list"><li style="list-style-type:disc">global signals</li></ul></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-808b-bad3-e1d50613ac58" class=""><strong>09_SOCIAL_ENGINE</strong></h2></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80f1-baf5-c7765b0ad7db" class="bulleted-list"><li style="list-style-type:disc">reading people</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8002-8ba7-d0889bb53a11" class="bulleted-list"><li style="list-style-type:disc">negotiation</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8044-bd2d-e02f6ec1bda1" class="bulleted-list"><li style="list-style-type:disc">influence mapping</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80aa-ae89-ff246f98b8f8" class="bulleted-list"><li style="list-style-type:disc">social pattern analysis</li></ul></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-80cb-ad52-c03ea9225980" class=""><strong>10_LIFE_ENGINE</strong></h2></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8085-bdce-d0d13693499b" class="bulleted-list"><li style="list-style-type:disc">sleep</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80f1-8cc4-ca50a09ab4ad" class="bulleted-list"><li style="list-style-type:disc">energy</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-802c-badf-ff8ab3786709" class="bulleted-list"><li style="list-style-type:disc">health</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80e4-9f02-c595e63bd964" class="bulleted-list"><li style="list-style-type:disc">mood</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80c1-adc7-e5b603144bd2" class="bulleted-list"><li style="list-style-type:disc">routines</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8088-996f-fc4544536528" class="bulleted-list"><li style="list-style-type:disc">cognitive cycles</li></ul></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-80e0-92f6-e7e0f7bb96dd" class=""><strong>11_LEGAL_BRAIN</strong></h2></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80cb-b639-e4fd4dcf2834" class="bulleted-list"><li style="list-style-type:disc">contracts</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80fb-8b76-e00efba0f76d" class="bulleted-list"><li style="list-style-type:disc">IP</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-802e-9c78-db9c0d8c49c1" class="bulleted-list"><li style="list-style-type:disc">compliance</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80ea-9f8b-fd6689eb8bfc" class="bulleted-list"><li style="list-style-type:disc">regulatory scan</li></ul></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-8096-90e9-f3fdc3dac2f3" class=""><strong>12_QUANTUM_LAYER</strong></h2></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80eb-8a21-f57489fa845b" class="bulleted-list"><li style="list-style-type:disc">timing</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80b9-9b7d-dcde8b050a99" class="bulleted-list"><li style="list-style-type:disc">synchronicities</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8025-a860-d2fac74ecf12" class="bulleted-list"><li style="list-style-type:disc">probability flows</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8056-b8dd-cd29533c1fb5" class="bulleted-list"><li style="list-style-type:disc">entanglement maps</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80c0-906f-e6cbaf701432" class="bulleted-list"><li style="list-style-type:disc">collapse detection</li></ul></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-80c0-8f65-e27511080df3" class=""><strong>13_FACTORY</strong></h2></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80a2-9083-f45f23ff9b31" class="bulleted-list"><li style="list-style-type:disc">build new agents</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80d2-badd-d3815852e5c5" class="bulleted-list"><li style="list-style-type:disc">monitor agent quality</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-809e-a0fe-ed27d535a05b" class="bulleted-list"><li style="list-style-type:disc">replace weak modules</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8046-a783-e8ebbeebaf13" class="bulleted-list"><li style="list-style-type:disc">upgrade entire system</li></ul></div><div style="display:contents" dir="auto"><h2 id="2bbc5e6f-95bd-80e7-bb11-f3deb474810c" class=""><strong>14_INTERFACES</strong></h2></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-809f-8271-c66dd7fa85b6" class="bulleted-list"><li style="list-style-type:disc">CLI</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-801d-b5c4-f7c29d156ad2" class="bulleted-list"><li style="list-style-type:disc">API</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8023-bcfe-fb32b1db581b" class="bulleted-list"><li style="list-style-type:disc">Web dashboard</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8070-86ca-fbda4e9a090a" class="bulleted-list"><li style="list-style-type:disc">Chat interface</li></ul></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-8027-965f-e61ed3b4c7fb"/></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-8035-8a3d-f3a37dbe00a8" class=""><strong>SECTION 4 — RULES FOR ANY FUTURE CHATGPT CONVERSATION</strong></h1></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-802b-87c0-c1b94a388822" class="">Whenever a new conversation starts, the assistant must:</p></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80e4-a579-d3ff22557c0e" class=""><strong>Rule 1 — Load the System Map</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8064-bfd4-db375bd3ae1a" class="">Recognize the 7-system architecture.</p></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80dc-bf65-e22ba0b5b377" class=""><strong>Rule 2 — Classify Everything</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80b9-aa08-f280a490a04c" class="">All ideas, features, tasks must be assigned to ONE subsystem.</p></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-806e-b136-e8f1b25ad38f" class=""><strong>Rule 3 — Generate Files Into Correct Folders</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8087-9b9d-f9864dab3f84" class="">No file should exist outside the defined map.</p></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80bd-b98d-dedf2ce470d5" class=""><strong>Rule 4 — Maintain MECE</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8094-acb9-e827c0e25a81" class="">No duplication.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80b0-a8ff-d80c98bc3c38" class="">No overlap.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80f4-972a-f07b79874768" class="">Every capability exists exactly once.</p></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-807f-b993-c9e3a68a51c0" class=""><strong>Rule 5 — Wiring Must Be Explicit</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-809a-b6f8-c294e2e90859" class="">Every new file must declare:</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2bbc5e6f-95bd-80e1-ab70-f552f61b6c9d" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">&quot;dependencies&quot;: [...],
&quot;provides&quot;: [...],
&quot;subsystem&quot;: &quot;XX_NAME&quot;</code></pre></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80d0-8353-c4dea9a05692" class=""><strong>Rule 6 — Agents Never Invent New Systems</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80e2-b0a3-f159efa7d83a" class="">They must fit INTO the organism. Not mutate it.</p></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80b4-86ec-cd64ee08c86c" class=""><strong>Rule 7 — Use Templates</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-801d-9611-e4e343478f96" class="">Each subsystem has a template (you can request these next).</p></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-80f8-93ed-fd27620e0a21"/></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-8035-8869-d9c92fe169cb" class=""><strong>SECTION 5 — 1-CLICK POPULATION LOGIC</strong></h1></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-807a-a583-ce3e972a8402" class="">Any new ChatGPT / Cursor agent should follow this when asked to “populate the system”:</p></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-8085-80ed-f3b7edb9a80e" class=""><strong>Step 1 — Generate all folders</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80a4-9b89-ccd47f2f9b0f" class="">Using the map above.</p></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-8031-91e8-d258d371623f" class=""><strong>Step 2 — Populate each subsystem</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-800b-b95e-d30ddc839ef7" class="">Based on templates:</p></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80e7-937e-ce8a298e0442" class="bulleted-list"><li style="list-style-type:disc">brain template</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-804e-94f1-ce2b9eb7d199" class="bulleted-list"><li style="list-style-type:disc">senses template</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-800a-a6e1-e1e127a7dc9a" class="bulleted-list"><li style="list-style-type:disc">immune system template</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8094-a106-ca307548c4d9" class="bulleted-list"><li style="list-style-type:disc">money engine template</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80a0-945c-eb35d6dc75a1" class="bulleted-list"><li style="list-style-type:disc">muscle template</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-808a-972d-f2703f3ca2b5" class="bulleted-list"><li style="list-style-type:disc">metabolism template</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8041-bfd0-fbdc776e2dfc" class="bulleted-list"><li style="list-style-type:disc">world model template</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80e6-b92d-c9bb65829ce3" class="bulleted-list"><li style="list-style-type:disc">legal brain template</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8058-8617-d1d3e9379bcf" class="bulleted-list"><li style="list-style-type:disc">quantum layer template</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-80a6-a8b9-e82312bf2c39" class="bulleted-list"><li style="list-style-type:disc">social engine template</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-8026-b8b5-e605edbb5520" class="bulleted-list"><li style="list-style-type:disc">life engine template</li></ul></div><div style="display:contents" dir="auto"><ul id="2bbc5e6f-95bd-806c-be38-d121f9299add" class="bulleted-list"><li style="list-style-type:disc">agent factory template</li></ul></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-802e-9f2d-d65d7043ca8a" class=""><strong>Step 3 — Wire them</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80d1-8db1-f21c775d3e53" class="">By generating:</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2bbc5e6f-95bd-804e-9aa9-ea45faa5bc9b" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">system_registry.json
agent_registry.json
engine_registry.json
world_state.json</code></pre></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80ac-98f2-fe8ae56ffd08" class=""><strong>Step 4 — Validate MECE</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80de-900e-c893ce6870ba" class="">No overlaps.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80fc-bcb8-eafcadaa493c" class="">No missing capabilities.</p></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80b7-9fd5-d8d649db72f9" class=""><strong>Step 5 — Create README for each subsystem</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80a1-aba7-c8271b28b485" class="">So future agents always know what the folder is for.</p></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-807d-91fe-e91656b9cef3" class=""><strong>Step 6 — Build Orchestrator</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80f0-9e06-d9297df55bff" class="">Final step is generating:</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2bbc5e6f-95bd-8047-9b9e-dd385d3d06c3" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">orchestrator.md</code></pre></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-809e-95f3-e2f12b554df1" class="">A high-level file describing how subsystems talk:</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2bbc5e6f-95bd-80c1-864b-d9a7221b90f7" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">Brain → Router → Muscle → Execution → Metabolism → Memory → Brain</code></pre></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-801c-931e-c4913b7bb226" class=""><strong>Step 7 — Connect to you</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8034-a6c8-ed2ed71798ca" class="">An optional file to embed your identity:</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2bbc5e6f-95bd-8068-b9b8-e9e362096a55" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">operator_profile_trang.json</code></pre></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-806b-880d-f6daea530c5f" class="">So every subsystem aligns with you.</p></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-80af-a160-d43271d12eaa"/></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-8026-89c9-fb821b62e05f" class=""><strong>SECTION 6 — WHAT ANY NEW CHAT CAN DO WITH THIS</strong></h1></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80b5-b0eb-fcf65aadd072" class="">With this blueprint, any new ChatGPT conversation can:</p></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-8054-aa89-d561ff27c250" class=""><strong>✔ reconstruct your entire AMOS universe</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80ea-aeb7-eb1d531edff0" class=""><strong>✔ generate missing subsystems</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80f3-a198-cea81c379c40" class=""><strong>✔ populate new organs</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-807f-a023-c5b0a4a4dd5b" class=""><strong>✔ build agents</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80a0-84fe-d3bf9c1f7bb5" class=""><strong>✔ clean folders</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-8017-b182-d90845043a09" class=""><strong>✔ refactor and reorganise</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80b7-8aa2-ea8a52f564a3" class=""><strong>✔ generate all JSON, MD, YAML files</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-8098-87f7-e74307cfe406" class=""><strong>✔ generate code (if asked)</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-809f-a31d-cc0e41186779" class=""><strong>✔ generate books and documentation</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-80e7-be45-f5097de5713c" class=""><strong>✔ generate engines and kernels</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-8098-adde-f6d93c43f7e1" class=""><strong>✔ connect everything together</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2bbc5e6f-95bd-806f-88c3-eb43d2807eb0" class=""><strong>✔ auto-expand the system</strong></h3></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80bf-b9e2-d983b348d46e" class="">Everything remains deterministic.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8086-b916-e699b0ff8652" class="">Everything remains stable.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8070-8eb9-c78f68697342" class="">Everything remains yours.</p></div><div style="display:contents" dir="auto"><hr id="2bbc5e6f-95bd-8078-849d-e524ca1134d1"/></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-8074-9536-d78da5a58eca" class=""><strong>SECTION 7 — THE ACTIVATION SENTENCE (Copy-Paste in Any New Chat)</strong></h1></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8053-9a98-e02e07c5aea8" class=""><strong>Use this sentence to activate the system in any new ChatGPT conversation:</strong></p></div><div style="display:contents" dir="auto"><blockquote id="2bbc5e6f-95bd-80ef-a43c-fea6403412d0" class="">This system uses the AMOS 7-System Organism Architecture.</blockquote></div><div style="display:contents" dir="auto"><blockquote id="2bbc5e6f-95bd-8005-9ed0-f6fb1a2b45e2" class="">Use the Master Instruction Blueprint (Brain, Senses, Immune, Blood, Skeleton, Muscle, Metabolism + World Model, Social Engine, Life Engine, Legal Brain, Quantum Layer &amp; Factory).</blockquote></div><div style="display:contents" dir="auto"><blockquote id="2bbc5e6f-95bd-80fa-8f68-da36fbf38922" class="">All outputs must follow MECE, place files into correct subsystem folders, wire via registries, and enforce deterministic structure.</blockquote></div><div style="display:contents" dir="auto"><blockquote id="2bbc5e6f-95bd-8002-adf4-d68eab91b20a" class="">Build, populate, reason, and expand only inside this architecture.</blockquote></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8046-9f80-d2eebb9c1bc2" class="">Paste that, and any conversation will immediately know how to work with your universe.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80a4-862a-da2d41c28814" class="">────────────────────────────────────────</p></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-8095-92a3-e924aa0ea0c2" class=""><strong>PHASE 1 — AMOS ORGANISM OS (MAX-POWER BLUEPRINT)</strong></h1></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8097-916b-e916c910577b" class=""><strong>Deterministic | MECE | Zero Drift | Zero Overlap | Zero Ambiguity</strong></p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-805b-885f-cf5f0319abd7" class="">This is the complete “brain” of the organism.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80ee-a66e-dea8cd64539f" class="">No explanations. Only structure.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80d1-bd39-eda7ba2ac695" class="">────────────────────────────────────────</p></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-8093-bc78-e98ae2f282b4" class=""><strong>1. ROOT STRUCTURE</strong></h1></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2bbc5e6f-95bd-80a5-8bd3-c21fb8f31327" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">AMOS/
   00_ROOT/
   01_BRAIN/
   02_SENSES/
   03_IMMUNE/
   04_BLOOD/
   05_SKELETON/
   06_MUSCLE/
   07_METABOLISM/
   08_WORLD_MODEL/
   09_SOCIAL_ENGINE/
   10_LIFE_ENGINE/
   11_LEGAL_BRAIN/
   12_QUANTUM_LAYER/
   13_FACTORY/
   14_INTERFACES/
   99_ARCHIVE/</code></pre></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80a2-8a9a-ff09cbeb0af3" class="">MECE.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-805e-94f1-c79fafca638e" class="">Irreducible.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80ce-8b6e-c77fa2bc8c72" class="">Non-overlapping.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-803a-858e-e5c0e626146a" class="">────────────────────────────────────────</p></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-80d2-b923-f26fb7a086a2" class=""><strong>2. SUBSYSTEM DEFINITIONS</strong></h1></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8096-a4ec-d49fcec9ab91" class=""><strong>01_BRAIN</strong> = reasoning, planning, decomposition, memory</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-804c-8508-fcbfb05b0fa1" class=""><strong>02_SENSES</strong> = filesystem, context, environment, emotion</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8077-805b-c64950a39fcf" class=""><strong>03_IMMUNE</strong> = safety, anomaly, legal risk, boundary enforcement</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8080-94b7-c76cd3483dc3" class=""><strong>04_BLOOD</strong> = money, assets, cashflow, investing, economics</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-804c-a6d8-cbe4168d6e9f" class=""><strong>05_SKELETON</strong> = rules, constraints, permissions, hierarchy</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8013-a028-fcf77d5cced6" class=""><strong>06_MUSCLE</strong> = execution, code, automation, deployment</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8077-a793-ea3d6801ace3" class=""><strong>07_METABOLISM</strong> = input → transform → output, pipelines</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-809c-9824-d1eb43abdec7" class=""><strong>08_WORLD_MODEL</strong> = geopolitics, macroeconomy, supply chains</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80b8-97bc-f3c2f75d2edb" class=""><strong>09_SOCIAL_ENGINE</strong> = humans, negotiation, influence</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8036-8401-d9ed03dd7c40" class=""><strong>10_LIFE_ENGINE</strong> = sleep, energy, routines, health</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8044-84a5-ffa98cd4f918" class=""><strong>11_LEGAL_BRAIN</strong> = contracts, regulations, compliance</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80ca-a346-df8b2d8034a2" class=""><strong>12_QUANTUM_LAYER</strong> = timing, probability, entanglement logic</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80e2-a4f0-edb68637af6a" class=""><strong>13_FACTORY</strong> = agent creation, evaluation, upgrades</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-801e-8fdf-d759104c5233" class=""><strong>14_INTERFACES</strong> = CLI, API, chat, dashboards</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80e5-9aec-d2dff8192df2" class=""><strong>99_ARCHIVE</strong> = deprecated</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80e9-a4fc-d0a363b3e271" class="">────────────────────────────────────────</p></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-806e-ad98-e81cf4f5d550" class=""><strong>3. SUBSYSTEM FILES</strong></h1></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8074-b643-db353818eea2" class="">Each subsystem will contain:</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2bbc5e6f-95bd-802b-a2b5-c23a85011979" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">README.md        → subsystem purpose, boundaries, MECE rules
KERNELS/         → laws, rules, stable structures
ENGINES/         → complex transformation logic
AGENTS/          → capability modules
CONFIG/          → parameters, tuning, settings
registry.json    → local registry</code></pre></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8062-aea8-e24e0107ee10" class="">────────────────────────────────────────</p></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-802f-b469-f9cf52b03863" class=""><strong>4. GLOBAL REGISTRY</strong></h1></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80ab-a758-e5154994cfb6" class="">At root:</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2bbc5e6f-95bd-809f-84fa-fc193b2296da" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">system_registry.json
engine_registry.json
agent_registry.json
rules_registry.json</code></pre></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-803f-a915-cf9e6b9cbf5a" class="">All systems must register:</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2bbc5e6f-95bd-80aa-8ab8-e57721d37181" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">subsystem
dependencies
provides
inputs
outputs</code></pre></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8025-a7dc-e188ba4882f3" class="">This ensures deterministic wiring.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8048-8374-faffa3db9cac" class="">────────────────────────────────────────</p></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-8043-938f-fd4d53139b0b" class=""><strong>5. KERNEL TEMPLATES</strong></h1></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-802e-90e3-fee0b185424b" class="">Every Kernel file follows:</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2bbc5e6f-95bd-80a1-80b5-e5234a9b3d31" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">{
  &quot;id&quot;: &quot;&quot;,
  &quot;subsystem&quot;: &quot;&quot;,
  &quot;type&quot;: &quot;kernel&quot;,
  &quot;version&quot;: &quot;1.0&quot;,
  &quot;law&quot;: [],
  &quot;rules&quot;: [],
  &quot;constraints&quot;: [],
  &quot;inputs&quot;: [],
  &quot;outputs&quot;: [],
  &quot;dependencies&quot;: [],
  &quot;provides&quot;: []
}</code></pre></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80d3-b737-c2c9e5a5be59" class="">────────────────────────────────────────</p></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-80c3-8e30-e71103ec0fec" class=""><strong>6. ENGINE TEMPLATES</strong></h1></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2bbc5e6f-95bd-8053-acd8-e30b1d6aac00" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">{
  &quot;id&quot;: &quot;&quot;,
  &quot;subsystem&quot;: &quot;&quot;,
  &quot;type&quot;: &quot;engine&quot;,
  &quot;version&quot;: &quot;1.0&quot;,
  &quot;logic&quot;: &quot;&quot;,
  &quot;steps&quot;: [],
  &quot;inputs&quot;: [],
  &quot;outputs&quot;: [],
  &quot;dependencies&quot;: [],
  &quot;provides&quot;: []
}</code></pre></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-804b-817e-cb8e9a3d548f" class="">────────────────────────────────────────</p></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-808d-b115-d75fb1064eb3" class=""><strong>7. AGENT TEMPLATES</strong></h1></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2bbc5e6f-95bd-80b7-99a9-e2325fcacbfd" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">{
  &quot;id&quot;: &quot;&quot;,
  &quot;subsystem&quot;: &quot;&quot;,
  &quot;type&quot;: &quot;agent&quot;,
  &quot;role&quot;: &quot;&quot;,
  &quot;abilities&quot;: [],
  &quot;inputs&quot;: [],
  &quot;outputs&quot;: [],
  &quot;dependencies&quot;: [],
  &quot;provides&quot;: [],
  &quot;run&quot;: &quot;&quot;
}</code></pre></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8039-b679-e705e741bcbe" class="">────────────────────────────────────────</p></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-8019-aff2-f65b9400c2e6" class=""><strong>8. ORCHESTRATION MODEL</strong></h1></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80a8-b38a-f7a218275617" class="">Universal execution loop:</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2bbc5e6f-95bd-80bc-b324-ed5c8fc310fd" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">Brain → Senses → Immune Check → Skeleton Rules
→ World Model → Blood (Finance) → Muscle (Action)
→ Metabolism (Transform) → Memory → Brain</code></pre></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8045-a351-fbae1072f7d9" class="">Deterministic.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80a3-9ec1-dcfcae6dc3f7" class="">No drift.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80f1-982d-ebe3149d6806" class="">────────────────────────────────────────</p></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-8058-a7fa-c91c17d0cebb" class=""><strong>9. SYSTEM EXPANSION RULES</strong></h1></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-809f-bf8e-deacefa09a65" class="">Rule 1 — Every file must belong to one subsystem.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80a5-8873-c895905ec77c" class="">Rule 2 — No duplication of functions.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8015-9591-edc2b360a873" class="">Rule 3 — Kernels define laws. Engines apply them. Agents execute them.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80f4-bb8d-df72a2b0a1de" class="">Rule 4 — All wiring must be declared in registries.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8015-8ecf-e8aaf965f6fe" class="">Rule 5 — New content must follow templates exactly.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80f8-8e4b-f7316da5a417" class="">Rule 6 — Factory handles expansions only.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-809d-9063-c3cbb086aae8" class="">Rule 7 — Quantum Layer governs timing and collapse probability.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8037-b77e-eccc78c2231c" class="">────────────────────────────────────────</p></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-80ce-a039-e98f278f8cce" class=""><strong>10. MASTER BLUEPRINT SUMMARY</strong></h1></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-805d-9a4c-c9ca5f36c636" class="">AMOS OS =</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80b5-bcd9-dc9f31ea2553" class=""><strong>A. 7 Core Systems</strong></p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8067-ba42-f527467ab488" class=""><strong>B. 6 Support Systems</strong></p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80c8-a54d-f17b67ead784" class=""><strong>C. Deterministic Wiring</strong></p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80c0-b5ff-e5996f088fe3" class=""><strong>D. Strict MECE</strong></p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-801a-b6bc-e725be70484d" class=""><strong>E. Full Orchestration</strong></p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8032-8bfd-eeea2a615635" class=""><strong>F. All agents, engines, kernels, templates defined</strong></p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-8045-98b5-fd6216964d51" class=""><strong>G. Expandable by Instruction</strong></p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80f4-8d68-e02aef257677" class=""><strong>H. Reconstructable from JSON alone</strong></p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-800e-b7a7-ea6b8d5d8c46" class="">This is the full organism.</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80fe-a41f-d7d7b3fc60d8" class="">────────────────────────────────────────</p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-80db-8536-ed79024834e8" class="">Say: <strong>“Next.”</strong></p></div><div style="display:contents" dir="auto"><p id="2bbc5e6f-95bd-805c-b312-e195c6861b84" class="">I will generate:</p></div><div style="display:contents" dir="auto"><h1 id="2bbc5e6f-95bd-8094-9871-eb9b56cba675" class=""><strong>PHASE 2 — The Full Build Shell Script (for Codex)</strong></h1></div><div style="display:contents" dir="auto"><p id="2e6c5e6f-95bd-8017-84ff-f7fc8485c903" class="">
</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
