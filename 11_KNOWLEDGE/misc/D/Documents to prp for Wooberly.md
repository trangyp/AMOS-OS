---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Documents to prp for Wooberly</title><style>
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
	
</style></head><body><article id="29dc5e6f-95bd-8012-9ca7-cc2a070831ff" class="page sans"><header><h1 class="page-title" dir="auto">Documents to prp for Wooberly</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-8083-9343-cb1ef2c91dd8" class="">Excellent question — and you’re thinking exactly like a CTO who wants zero future liability.</p></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-8089-b611-eb1323f71b82" class="">Since you’ll be working <strong>directly with the Wooberly core team</strong>, and paying feature-by-feature (milestone-by-milestone), the correct approach is to prepare a <strong>“Master Service &amp; IP Ownership Agreement (MSA)”</strong> with attached <strong>Statement(s) of Work (SOWs)</strong> per feature.</p></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-80ff-aa4d-c458cbc2e31e" class="">Below is a full professional breakdown of the contracts and clauses you should have in place — covering <strong>IP ownership, confidentiality, deliverables, payments, warranties, and security</strong> — so you’re fully protected both legally and operationally.</p></div><div style="display:contents" dir="auto"><hr id="29dc5e6f-95bd-805f-b8da-c840676bcba3"/></div><div style="display:contents" dir="auto"><h2 id="29dc5e6f-95bd-8066-bd2d-deb851a9db15" class=""><strong>⚖️ 1. Master Service Agreement (MSA)</strong></h2></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-80c5-b468-e04e23c31c38" class="">This is your <strong>umbrella contract</strong> that governs <em>all current and future collaborations</em> with Wooberly (or any vendor).</p></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-80f5-8bc7-fdabc1d85fcf" class="">You only sign it once, and then issue separate SOWs under it for each feature or milestone.</p></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-80bb-aa61-eb370b57446c" class=""><strong>🔹 Purpose:</strong></h3></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-80df-934d-c2ea15fa3516" class="bulleted-list"><li style="list-style-type:disc">Establishes <strong>legal relationship and accountability</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-807e-8fb1-c0b28559aec4" class="bulleted-list"><li style="list-style-type:disc">Defines <strong>ownership of deliverables, confidentiality, liability, warranties, and dispute mechanisms</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-8037-abb8-e65638dbbed1" class="bulleted-list"><li style="list-style-type:disc">Prevents reuse or resale of UniTaxi’s IP</li></ul></div><div style="display:contents" dir="auto"><hr id="29dc5e6f-95bd-80d4-b669-cb49b0a889f4"/></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-809a-93a2-e0fc4058b744" class=""><strong>Core MSA Sections</strong></h3></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-8084-b9cc-ef1d11e28e87" class=""><strong>1.</strong></h3></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-8055-b50d-e190562a740d" class=""><strong>Parties &amp; Relationship</strong></h3></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-8004-85c5-e992bd0f0f57" class="">Defines UniPower/UniTaxi as the<div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-8039-9d69-f3a11bda09e8" class=""><em>Client</em></p></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-8010-92af-f81e4dfd7d22" class=""><em>Vendor</em></p></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-80ea-a5ad-ed04d80640b4" class=""><em>independent contractors</em></p></div></blockquote></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-8021-b0e9-f1e2522eed02" class=""><strong>2.</strong></h3></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-8096-ad6f-cccb6c7abcfc" class=""><strong>Scope of Engagement</strong></h3></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-8070-8532-c939f367187e" class="">All work will be defined through<div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-80af-ad2d-c2d1c7fdbab5" class=""><strong>separate SOWs</strong></p></div></blockquote></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-8060-a093-e57420a81679" class=""><strong>3.</strong></h3></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-80f9-9f52-db1a4e2693fd" class=""><strong>Intellectual Property Ownership</strong></h3></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-80fd-8fd9-c41d0f29e7b1" class=""><strong>Critical Clause:</strong></p></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-80a8-83bc-f96db239cabf" class="">All deliverables, source code, and derivative works created under this Agreement shall be deemed “work made for hire” and are the sole property of the Client.</blockquote></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-80f9-a860-e1a28e385c04" class="">Vendor retains no ownership, license, or right to reuse or resell the code, design, or any component derived from UniTaxi’s project.</blockquote></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-8053-8027-dfb06eb548c2" class="">If local laws prevent “work made for hire,” Vendor hereby irrevocably assigns all IP rights to Client upon payment of each milestone.</blockquote></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-807f-8ac4-df578a037184" class=""><strong>4.</strong></h3></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-8070-bca3-ce826a013e61" class=""><strong>Confidentiality &amp; Non-Disclosure</strong></h3></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-8008-88d4-eb45246ac164" class="">Both parties agree not to disclose or use any confidential information — including code, documentation, credentials, or business data — outside the project.</blockquote></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-8082-a101-f1569686f31c" class="">Confidentiality survives 3 years after termination.</blockquote></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-8097-97f8-e7642f35c1cd" class=""><strong>5.</strong></h3></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-8000-9c15-e1b5539ce842" class=""><strong>Non-Resale / Non-Competition</strong></h3></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-800f-a850-f3358b7d4a41" class="">Vendor shall not sell, license, replicate, or repackage any custom modules, integrations, or derivative code developed for UniTaxi to any other ride-hailing, logistics, or EV-related entity within Vietnam for<div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-80ac-a24c-c20c1db59a98" class=""><strong>36 months</strong></p></div></blockquote></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-80be-a922-f81d1871bb52" class=""><strong>6.</strong></h3></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-80f0-8ebf-f93f93d4da92" class=""><strong>Deliverables &amp; Acceptance</strong></h3></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-80ca-a0c4-d9f548fcbe0c" class="">Each SOW will define specific deliverables.</blockquote></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-8040-921d-c3fcca899b28" class="">Deliverables are accepted only after:</blockquote></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-8034-a6b4-f8358f619d49" class="bulleted-list"><li style="list-style-type:disc">Delivery to UniTaxi’s staging or Git repository,</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-8076-910c-ddbd7895da79" class="bulleted-list"><li style="list-style-type:disc">Successful demo,</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-80a5-8732-e411ab5e932b" class="bulleted-list"><li style="list-style-type:disc">Completion of 3-day functional testing by Client.<div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-8048-b734-ced2866c0f92" class="">Payment shall follow acceptance, not delivery.</blockquote></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-8090-86a3-db85174e1ec9" class=""><strong>7.</strong></h3></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-8084-83a3-c60248a545b0" class=""><strong>Payment &amp; Invoicing</strong></h3></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-8092-91e1-c2de4e7f2713" class="">Payments are milestone-based, using escrow (Upwork, Wise, or Stripe).</blockquote></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-80a7-810a-d73605acf2e3" class="">No prepayment unless mutually agreed.</blockquote></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-80b3-b6cf-e7239aeac816" class="">All costs are capped per SOW.</blockquote></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-8095-982d-d1b351b3422f" class=""><strong>8.</strong></h3></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-80d6-8639-f35001fe6e02" class=""><strong>Warranty &amp; Defect Rectification</strong></h3></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-80d8-8f00-ec5ee50e8bff" class="">Vendor warrants all code will:</blockquote></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-8038-990b-d8e049271100" class="bulleted-list"><li style="list-style-type:disc">Function as intended for 90 days post-acceptance,</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-8024-9eb6-fce25a546c96" class="bulleted-list"><li style="list-style-type:disc">Be free from malicious code or backdoors,</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-8041-8728-d5bd926636b5" class="bulleted-list"><li style="list-style-type:disc">Conform to agreed technical and security standards (AES-256, TLS 1.3, etc.).<div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-80b9-a4f6-c853ca96a30a" class="">Bugs discovered within the warranty period must be fixed at no additional cost.</blockquote></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-8065-a4b4-da0eaa5aabb0" class=""><strong>9.</strong></h3></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-802b-a5b0-d69e25c8f29c" class=""><strong>Security &amp; Data Protection</strong></h3></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-8059-b9d1-e8af896eba76" class="">Vendor must follow industry best practices:</blockquote></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-8083-a486-d61c5cd82100" class="bulleted-list"><li style="list-style-type:disc">No production credentials stored in code.</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-8000-a361-f19425723f4d" class="bulleted-list"><li style="list-style-type:disc">All transfers over TLS 1.3.</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-80de-a342-c7f21d093a17" class="bulleted-list"><li style="list-style-type:disc">Passwords and secrets handled via environment variables.</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-80d1-bfdf-c2c318154ae4" class="bulleted-list"><li style="list-style-type:disc">Any data breach or loss must be reported within 24 hours.</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-800f-84ef-e06a766c422c" class="bulleted-list"><li style="list-style-type:disc">All data and builds remain stored on UniTaxi-approved infrastructure (Viettel IDC / FPT Cloud).</li></ul></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-8055-9715-cd4f80f8a138" class=""><strong>10.</strong></h3></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-8069-8880-e9e30237f4ff" class=""><strong>Audit &amp; Access Control</strong></h3></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-8016-bc5b-fcb2c09834a1" class="">Vendor access is limited to feature-specific repos.</blockquote></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-80be-955f-f3ed5e704f8e" class="">UniTaxi reserves the right to audit logs, commits, and activity.</blockquote></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-80cf-ad3c-f297fe2fff4d" class="">Vendor must comply with DevOps access control and security reviews.</blockquote></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-80eb-82e6-d7c22b35270e" class=""><strong>11.</strong></h3></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-8010-a0d3-de81b5234bbe" class=""><strong>Termination</strong></h3></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-8058-b8c1-e79671685de7" class="">Either party may terminate for convenience with 10 days’ notice or for cause (non-performance, breach, etc.) immediately.</blockquote></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-806f-8b20-dcd56451078f" class="">Upon termination, all code, documentation, and deliverables are transferred to Client.</blockquote></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-80f5-8787-df15bb85551d" class=""><strong>12.</strong></h3></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-801e-8782-fd62166965bc" class=""><strong>Indemnity</strong></h3></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-8056-915a-ee4e200a8934" class="">Vendor shall indemnify and hold harmless Client against any claims arising from:</blockquote></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-8074-9884-cad4f537c0c0" class="bulleted-list"><li style="list-style-type:disc">IP infringement,</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-8038-a4e6-ea11aac4e193" class="bulleted-list"><li style="list-style-type:disc">Data breaches caused by Vendor,</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-801f-b83a-cef1b8bad76b" class="bulleted-list"><li style="list-style-type:disc">Negligence or intentional misconduct.</li></ul></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-8046-89a2-f345da88f478" class=""><strong>13.</strong></h3></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-80bb-bb7f-c5790496ff72" class=""><strong>Governing Law &amp; Dispute Resolution</strong></h3></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-80ce-9613-da2a578d4dee" class="">Governed by<div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-80d5-9017-d8439e2812a2" class=""><strong>Singapore</strong></p></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-8001-abab-c35905096950" class=""><strong>Australia</strong></p></div></blockquote></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-80ff-96ce-c1af42f3a4a5" class="">Disputes resolved by<div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-80a2-9b5c-e6c0b5551aeb" class=""><strong>arbitration</strong></p></div></blockquote></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-8010-aa29-f459811e61c2" class=""><strong>14.</strong></h3></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-80d1-b640-cbbc141ad728" class=""><strong>Entire Agreement &amp; Survivability</strong></h3></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-804e-9645-fc1c80a33239" class="">MSA supersedes all prior communications.</blockquote></div><div style="display:contents" dir="auto"><blockquote id="29dc5e6f-95bd-8051-92db-d09e1c0f4c14" class="">IP ownership, confidentiality, and warranties survive termination.</blockquote></div><div style="display:contents" dir="auto"><hr id="29dc5e6f-95bd-8098-a512-c312a3c8a6b8"/></div><div style="display:contents" dir="auto"><h2 id="29dc5e6f-95bd-804f-b8ae-e41b7a724bec" class=""><strong>📄 2.</strong></h2></div><div style="display:contents" dir="auto"><h2 id="29dc5e6f-95bd-805b-bce6-cf208b4a796d" class=""><strong>Statement of Work (SOW)</strong></h2></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-80bc-b1c0-e1649d5349d2" class="">Each <strong>SOW</strong> corresponds to a specific feature (e.g., “Payment Gateway Integration”, “Wallet &amp; Payouts”, “E-Invoice”).</p></div><div style="display:contents" dir="auto"><h3 id="29dc5e6f-95bd-8053-80eb-db52a4a0fb50" class=""><strong>Structure:</strong></h3></div><div style="display:contents" dir="ltr"><table id="29dc5e6f-95bd-805a-84d3-d8624020dab0" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-8065-a0fb-c49381cf1d6f"><th id="aNt]" class="simple-table-header-color simple-table-header"><strong>Section</strong></th><th id="]kaq" class="simple-table-header-color simple-table-header" style="width:481px"><strong>Example Content</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-8064-b8c7-d55ea88a30b9"><td id="aNt]" class=""><strong>Feature Name</strong></td><td id="]kaq" class="" style="width:481px">Payment Gateway Integration (VNPay, MoMo, ZaloPay)</td></tr></div><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-801e-a219-f0ac7627551c"><td id="aNt]" class=""><strong>Scope of Work</strong></td><td id="]kaq" class="" style="width:481px">Implement API integrations, webhook handlers, daily reconciliation, success/failure logs, retry logic.</td></tr></div><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-804f-936f-d14995e0e6ef"><td id="aNt]" class=""><strong>Deliverables</strong></td><td id="]kaq" class="" style="width:481px">- Working integration for 3 PSPs- Admin dashboard for status- Documentation + test data- Source code in Git repo</td></tr></div><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-8070-aff3-c281b8c86e44"><td id="aNt]" class=""><strong>Estimated Hours / Cost</strong></td><td id="]kaq" class="" style="width:481px">120 hours × $25/h = USD 3,000 (capped)</td></tr></div><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-8007-a7e7-ce034e11055b"><td id="aNt]" class=""><strong>Timeline</strong></td><td id="]kaq" class="" style="width:481px">2–3 weeks from kickoff</td></tr></div><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-8066-bc5b-e1bfc695d62a"><td id="aNt]" class=""><strong>Acceptance Criteria</strong></td><td id="]kaq" class="" style="width:481px">- Payment flow successful- Webhook validated- Ledger reconciles 100%- All test cases passed</td></tr></div><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-8097-a1ee-cd2f3c7de674"><td id="aNt]" class=""><strong>Dependencies</strong></td><td id="]kaq" class="" style="width:481px">Access to VNPay/MoMo sandbox accounts</td></tr></div><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-80d5-9f6d-d579b45c0b12"><td id="aNt]" class=""><strong>Testing &amp; QA</strong></td><td id="]kaq" class="" style="width:481px">Vendor performs UAT; Client performs staging acceptance</td></tr></div><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-80a6-ba20-f951cf4f6a46"><td id="aNt]" class=""><strong>Milestones &amp; Payment Terms</strong></td><td id="]kaq" class="" style="width:481px">- 50% after delivery to staging- 50% after acceptance testing (3 days)</td></tr></div><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-80da-aac5-c593be7ee99e"><td id="aNt]" class=""><strong>Change Requests</strong></td><td id="]kaq" class="" style="width:481px">Out of scope changes require new written SOW</td></tr></div><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-80bb-84b4-ec9c79125a94"><td id="aNt]" class=""><strong>Warranty Period</strong></td><td id="]kaq" class="" style="width:481px">90 days from acceptance</td></tr></div><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-80e8-a4de-ddd026441f69"><td id="aNt]" class=""><strong>Documentation</strong></td><td id="]kaq" class="" style="width:481px">API references, setup guide, and architecture note</td></tr></div><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-8051-ab26-d410ca17a9cb"><td id="aNt]" class=""><strong>Ownership Transfer</strong></td><td id="]kaq" class="" style="width:481px">Full source code + build files transferred upon final payment</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="29dc5e6f-95bd-803b-98e1-ca68a3b93282"/></div><div style="display:contents" dir="auto"><h2 id="29dc5e6f-95bd-80fe-bb5d-c45e948b869a" class=""><strong>🧱 3.</strong></h2></div><div style="display:contents" dir="auto"><h2 id="29dc5e6f-95bd-802b-9911-ddd9704dadcd" class=""><strong>Supporting Documents</strong></h2></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-8080-b0af-d2c72f929d53" class="">To keep everything airtight, add:</p></div><div style="display:contents" dir="auto"><ol type="1" id="29dc5e6f-95bd-806c-af1c-f3fcf8fa8faa" class="numbered-list" start="1"><li><strong>Mutual NDA</strong><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-80af-bb95-f5b5e35b7075" class="bulleted-list"><li style="list-style-type:disc">Sign this before sharing any technical documentation or credentials.</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-80ae-82b9-cdf5bc37c0af" class="bulleted-list"><li style="list-style-type:disc">Covers confidentiality, IP, and non-circumvention.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="29dc5e6f-95bd-800f-8e7f-d2722afc1b7b" class="numbered-list" start="2"><li><strong>IP Assignment Letter (if required by local law)</strong><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-80d2-b7de-daba294585d2" class="bulleted-list"><li style="list-style-type:disc">Separate short document where Wooberly formally assigns IP rights for each milestone delivered.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="29dc5e6f-95bd-80d0-9ae3-e27e3720d0b9" class="numbered-list" start="3"><li><strong>Change Control Template</strong><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-80e4-9b75-fe054044d811" class="bulleted-list"><li style="list-style-type:disc">A 1-page form for any new features or extra work beyond scope.</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-808a-92a7-f37544a777e8" class="bulleted-list"><li style="list-style-type:disc">Ensures scope creep doesn’t turn into cost creep.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="29dc5e6f-95bd-8021-905e-fdc820526be0" class="numbered-list" start="4"><li><strong>Code Access &amp; Security Policy</strong><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-80b7-8bde-e3629200a9ef" class="bulleted-list"><li style="list-style-type:disc">Defines how they access repos, environments, and credentials.</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-805e-a255-fc879406dea3" class="bulleted-list"><li style="list-style-type:disc">Example: “Only feature-branch access via GitHub Teams; SSH keys rotated monthly.”</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><hr id="29dc5e6f-95bd-80f8-a9e5-e086654fb0ab"/></div><div style="display:contents" dir="auto"><h2 id="29dc5e6f-95bd-80d8-a9ee-f91f73f44563" class=""><strong>🧩 4.</strong></h2></div><div style="display:contents" dir="auto"><h2 id="29dc5e6f-95bd-80e8-8918-f4525015953e" class=""><strong>Optional but Recommended Add-ons</strong></h2></div><div style="display:contents" dir="ltr"><table id="29dc5e6f-95bd-80df-b3d3-c5406997bbfa" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-803c-9cd2-dc8f47cf1228"><th id="zUMK" class="simple-table-header-color simple-table-header"><strong>Clause / Document</strong></th><th id="COHe" class="simple-table-header-color simple-table-header"><strong>Why It Matters</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-80e8-987c-e40ab0f9eca1"><td id="zUMK" class=""><strong>Source Code Escrow Agreement</strong></td><td id="COHe" class="">Guarantees you get the latest code if Wooberly goes out of business or stops support.</td></tr></div><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-80d3-a1fd-fb1700e40950"><td id="zUMK" class=""><strong>Service Level Agreement (SLA)</strong></td><td id="COHe" class="">Defines uptime, response time for bugs, and penalties for major delays.</td></tr></div><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-8047-968d-f7cfaa7bb17c"><td id="zUMK" class=""><strong>Data Processing Addendum (DPA)</strong></td><td id="COHe" class="">Ensures PDPD compliance (mandatory if personal data handled).</td></tr></div><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-8036-925a-ce818a80316a"><td id="zUMK" class=""><strong>No-Reuse Clause (exclusive customisation)</strong></td><td id="COHe" class="">Prevents Wooberly from selling your VN localisation modules to other clients for 36 months.</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="29dc5e6f-95bd-80af-b8d3-d1a71771ae5d"/></div><div style="display:contents" dir="auto"><h2 id="29dc5e6f-95bd-8009-9ad8-fa1f582256cb" class=""><strong>✅</strong></h2></div><div style="display:contents" dir="auto"><h2 id="29dc5e6f-95bd-808d-84b5-c98ac9669f9d" class=""><strong>Recommended Contract Stack (Final Summary)</strong></h2></div><div style="display:contents" dir="ltr"><table id="29dc5e6f-95bd-80b6-a50c-fe211c6b4aa8" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-8028-9d81-e42e1c0edb33"><th id=";Qzc" class="simple-table-header-color simple-table-header"><strong>Document</strong></th><th id="Aw@}" class="simple-table-header-color simple-table-header"><strong>Purpose</strong></th><th id="tO}G" class="simple-table-header-color simple-table-header"><strong>When to Use</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-8081-9a0e-f5d4856e6c3b"><td id=";Qzc" class=""><strong>Mutual NDA</strong></td><td id="Aw@}" class="">Protect confidential data</td><td id="tO}G" class="">Before sharing any scope or repo</td></tr></div><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-809d-8481-dd5b823fa679"><td id=";Qzc" class=""><strong>Master Service Agreement (MSA)</strong></td><td id="Aw@}" class="">Governs the entire relationship</td><td id="tO}G" class="">Sign once before work starts</td></tr></div><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-80cc-864c-fe7af1450174"><td id=";Qzc" class=""><strong>Statement of Work (SOW)</strong></td><td id="Aw@}" class="">Defines each feature, hours, acceptance</td><td id="tO}G" class="">One per milestone</td></tr></div><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-80a5-bfe6-d8402b0c1259"><td id=";Qzc" class=""><strong>IP Assignment Letter</strong></td><td id="Aw@}" class="">Confirms code ownership</td><td id="tO}G" class="">At each milestone completion</td></tr></div><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-805e-ba3b-cb1f55c26282"><td id=";Qzc" class=""><strong>Source Code Escrow Agreement</strong> <em>(optional)</em></td><td id="Aw@}" class="">Backup in case vendor failure</td><td id="tO}G" class="">After 2+ milestones or $10k+ spend</td></tr></div><div style="display:contents" dir="ltr"><tr id="29dc5e6f-95bd-80af-b666-de5fa46009ea"><td id=";Qzc" class=""><strong>SLA + DPA</strong> <em>(optional)</em></td><td id="Aw@}" class="">For uptime, support, PDPD compliance</td><td id="tO}G" class="">After MVP goes live</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="29dc5e6f-95bd-80e6-92e5-e906e0497180"/></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-807c-8f18-dfa6d7332c46" class="">Would you like me to <strong>draft a clean, lawyer-ready MSA + SOW template</strong> (in Word format) tailored for your UniTaxi project — with IP, non-resale, and security clauses included?</p></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-80ca-b9fd-cd172d5dddb4" class="">You could use it directly with Wooberly or any future vendor.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
