---
tags: [security]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Detailed technical + compliance spec</title><style>
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
	
</style></head><body><article id="2c0c5e6f-95bd-805b-8521-d9a96a00edd3" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Detailed technical + compliance spec</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8075-9d59-daca0e36e5e7" class=""><strong>Technical + compliance spec</strong> for:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-8015-9498-ec6558aa061b" class="numbered-list" start="1"><li><strong>MISA integration</strong> (e-invoice + accounting).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-804c-b3cc-f4217f508b4b" class="numbered-list" start="2"><li><strong>Local payment gateways</strong>: MoMo, VNPAY, ViettelPay and local banks, with UI/flows similar to <strong>Grab / Xanh SM</strong> and compliant with Vietnamese regulation.</li></ol></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-804a-a464-d1be08b1a712"/></div><div style="display:contents" dir="auto"><h1 id="2c0c5e6f-95bd-8075-a72d-fb7053af725d" class=""><strong>0. Regulatory and Compliance Baseline (Vietnam)</strong></h1></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-807f-b085-dca778a3d328" class="">These are the main laws/standards your payment + invoicing design must align with:</p></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-808f-8dd0-eae9d1c4b3dd" class="bulleted-list"><li style="list-style-type:disc"><strong>Non-cash payments</strong>:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80ff-a385-f43d4ed39e2e" class="bulleted-list"><li style="list-style-type:circle">Decree <strong>101/2012/NĐ-CP</strong> on non-cash payments, amended by Decree <strong>80/2016/NĐ-CP</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8069-8d8c-e34289e76eea" class="bulleted-list"><li style="list-style-type:circle">SBV regulations on payment intermediaries and e-wallets.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-808a-a57b-c694f2b3effd" class="bulleted-list"><li style="list-style-type:disc"><strong>Bank cards / payment intermediaries</strong>:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80ee-a5fa-ef3f32df5fca" class="bulleted-list"><li style="list-style-type:circle">Circular <strong>19/2016/TT-NHNN</strong> on bank card operations.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80ee-a533-d46dceb06135" class="bulleted-list"><li style="list-style-type:disc"><strong>E-invoices</strong>:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80f3-b55e-fca18ea7010e" class="bulleted-list"><li style="list-style-type:circle">Decree <strong>123/2020/NĐ-CP</strong> and Circulars guiding e-invoices (MISA is certified to issue).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80c0-b3fe-ece2d7a31fea" class="bulleted-list"><li style="list-style-type:disc"><strong>Personal data</strong>:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8055-9581-ee1e2eceb09e" class="bulleted-list"><li style="list-style-type:circle">Decree <strong>13/2023/NĐ-CP</strong> on Personal Data Protection (PDPD) – financial &amp; payment data is <strong>sensitive data</strong> with extra safeguards.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-800f-90da-d94859865ae2" class="bulleted-list"><li style="list-style-type:disc"><strong>Cybersecurity / information security</strong>:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-804c-8008-da2bbbcac351" class="bulleted-list"><li style="list-style-type:circle">Law on Cyberinformation Security 2015 and Law on Cybersecurity 2018 – requirements on logging, incident handling, storing data in VN, etc.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8095-821f-df6d31a8c513" class=""><strong>Design principles:</strong></p></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-8062-a969-d9b72e1509c1" class="numbered-list" start="1"><li><strong>UniPower is not a payment intermediary</strong> (no e-wallet, no stored balance).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-80be-9a57-e714dcd5a490" class="numbered-list" start="2"><li><strong>Only licensed providers</strong> (MoMo, VNPAY, ViettelPay, banks) handle payment and store payment credentials.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-8027-8468-e6df96bbf243" class="numbered-list" start="3"><li><strong>UniPower only processes “necessary” personal data</strong>, with:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-801f-9048-fb8fa83491af" class="bulleted-list"><li style="list-style-type:disc">consent screens in app,</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-804a-a424-c971073f2a54" class="bulleted-list"><li style="list-style-type:disc">minimal data in callbacks,</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8051-921c-c77741aa9128" class="bulleted-list"><li style="list-style-type:disc">audit log for all payment events.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-8047-b42b-e8e4f628b2fc" class="numbered-list" start="4"><li><strong>All payment and invoice data stored on VN-based servers</strong>, with backups ≥ 5 years.</li></ol></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-8062-8bc6-ed1cd3079f35"/></div><div style="display:contents" dir="auto"><h1 id="2c0c5e6f-95bd-8024-a0da-fe247f4db4a9" class=""><strong>1. Unified Payment &amp; Invoice Architecture</strong></h1></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8028-9981-f9822f72c4c1" class="">Applies to <strong>all</strong> gateways and MISA.</p></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-8076-a6a6-c3f3e69fe357" class=""><strong>1.1 Components</strong></h2></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-800d-88c2-eaba36fab17f" class="bulleted-list"><li style="list-style-type:disc"><strong>UniApp-User</strong> – customer app (UniTaxi).</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8000-8edd-fd15c6d29e58" class="bulleted-list"><li style="list-style-type:disc"><strong>UniApp-Driver</strong> – driver app (UniTaxi Driver).</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80df-a92e-f258720ff28b" class="bulleted-list"><li style="list-style-type:disc"><strong>UniCore-API</strong> – backend for UniPower (Node/Java/PHP – language-agnostic).</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80c0-b5f2-c11db70383cb" class="bulleted-list"><li style="list-style-type:disc"><strong>UniPay-Service</strong> – internal payment abstraction service inside UniCore.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80c7-b713-eb239e7472bf" class="bulleted-list"><li style="list-style-type:disc"><strong>Gateways</strong>: MoMo, VNPAY, ViettelPay, Bank PGW/Napas.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8043-9312-d2964b5ba731" class="bulleted-list"><li style="list-style-type:disc"><strong>MISA eInvoice Service</strong> – certified e-invoice provider.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80d4-9209-e85b5e56e554" class="bulleted-list"><li style="list-style-type:disc"><strong>UniLedger</strong> – internal ledger + reconciliation DB.</li></ul></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-805c-b567-d9c4d826b858" class=""><strong>1.2 Core objects (internal)</strong></h2></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80f0-8f26-f270e81038f6" class="bulleted-list"><li style="list-style-type:disc">Ride – trip record.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80db-ba7b-eadd8b07326f" class="bulleted-list"><li style="list-style-type:disc">PaymentIntent – one planned payment for a Ride.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8056-84e5-e1efc01499fb" class="bulleted-list"><li style="list-style-type:disc">PaymentTransaction – actual gateway transaction instance.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8075-b8d1-c217d80f59d3" class="bulleted-list"><li style="list-style-type:disc">PaymentMethod – CASH, MOMO, VNPAY, VIETTELPAY, CARD_BANK.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8010-8068-e5c960cff620" class="bulleted-list"><li style="list-style-type:disc">InvoiceRequest / Invoice – for MISA.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80eb-948a-d9cdbf96ee2c" class="bulleted-list"><li style="list-style-type:disc">ReconciliationBatch – T+0/T+1 settlement batch per provider.</li></ul></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8064-a8d1-fc89fc5536ab" class="">Status mapping (internal):</p></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80cd-a9a3-c75bb3910da0" class="bulleted-list"><li style="list-style-type:disc">PaymentIntent.status: PENDING → IN_PROGRESS → SUCCEEDED / FAILED / CANCELED.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8063-9615-c66f9fb5f2f5" class="bulleted-list"><li style="list-style-type:disc">PaymentTransaction.status: CREATED / PENDING_GATEWAY / SUCCESS / FAILURE / REFUNDED.</li></ul></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-8023-b225-cf30f160b811"/></div><div style="display:contents" dir="auto"><h1 id="2c0c5e6f-95bd-8066-8f0c-f67cfb3c1202" class=""><strong>2. UI &amp; UX – Aligning with Grab / Xanh SM Patterns</strong></h1></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80a0-8b4f-ca0fb5237c80" class="">The following screens and flows should mimic the mental model of Grab/Xanh SM:</p></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-80b5-b811-cf004c240d68" class=""><strong>2.1 Payment selection before booking</strong></h2></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80c5-a55c-cae3ecf47073" class="bulleted-list"><li style="list-style-type:disc">On <strong>“Confirm booking”</strong> screen:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-806e-847a-c9237f7eee02" class="bulleted-list"><li style="list-style-type:circle">Section <strong>Payment method</strong>:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-804b-8f50-ca2d28715c0e" class="bulleted-list"><li style="list-style-type:square">Shows active method (e.g. “Tiền mặt”, “MoMo”, “VNPAY”, “ViettelPay”, “Thẻ ngân hàng”).</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8000-8f0d-fb80ebec3918" class="bulleted-list"><li style="list-style-type:square">Icon of wallet/card, same style as Grab/Xanh SM.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80b2-9975-c9cb2a61b847" class="bulleted-list"><li style="list-style-type:circle">Tap → <strong>Payment Methods Screen</strong>:</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-808a-a6a1-d4095f0072b9" class="">Fields:</p></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8096-9ac4-cab5eaaacf7a" class="bulleted-list"><li style="list-style-type:disc">List of methods:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80e0-a349-d4b0f4ab2aa6" class="bulleted-list"><li style="list-style-type:circle">Cash</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-801c-a0b0-dc25eebe2b73" class="bulleted-list"><li style="list-style-type:circle">MoMo E-Wallet</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-800f-9cab-fbff3ae1647f" class="bulleted-list"><li style="list-style-type:circle">VNPAY QR</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-805c-847b-ed3f60270594" class="bulleted-list"><li style="list-style-type:circle">ViettelPay</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-808f-8022-d8e932c0517b" class="bulleted-list"><li style="list-style-type:circle">Card / ATM (Napas) via VNPAY or other PGW.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80c8-87bd-c2ee01039c83" class="bulleted-list"><li style="list-style-type:disc">Each row:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-802f-9c8e-fd7a82767334" class="bulleted-list"><li style="list-style-type:circle">Logo, short description (“Thanh toán ngay trong ứng dụng”, “Quét QR”, …).</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8030-afae-fee9eb0e4339" class="bulleted-list"><li style="list-style-type:circle">Status: Đã liên kết, Chưa liên kết.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8077-9f4c-ef4d47e4a472" class="bulleted-list"><li style="list-style-type:disc">For wallet methods:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80cc-8565-e259e18bb969" class="bulleted-list"><li style="list-style-type:circle">Button “Liên kết” opens provider flow (for MoMo typically no long-term link, but you can store a pseudo-link state: “Preferred wallet MoMo”).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8087-93cb-eb2b14c8a94a" class="">UX rules:</p></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80da-8815-d78abae62d9f" class="bulleted-list"><li style="list-style-type:disc">User must <strong>always see</strong> total fare and chosen payment method on booking screen.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80e7-a52a-fe49e5f401d5" class="bulleted-list"><li style="list-style-type:disc">When switching from wallet → cash for an ongoing trip, mark PaymentIntent as SWITCHED_TO_CASH and show proper notice (“Chuyến này sẽ thanh toán tiền mặt”).</li></ul></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-8023-82b1-dd202e851958" class=""><strong>2.2 Payment confirmation after trip</strong></h2></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80b2-a27e-ea1c2ae00e02" class="bulleted-list"><li style="list-style-type:disc">After driver ends ride:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80a6-a1a4-d19841445e36" class="bulleted-list"><li style="list-style-type:circle">Screen Shows:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8046-80f2-df9cb1e936c0" class="bulleted-list"><li style="list-style-type:square">Final fare breakdown (base, surcharges, promotions).</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80ff-be5a-ca717327326f" class="bulleted-list"><li style="list-style-type:square">Payment method used (icon + text “Đã thanh toán qua MoMo”, etc.).</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8012-8dec-e2b77f37f780" class="bulleted-list"><li style="list-style-type:square">Status chip: Thành công, Đang xử lý…, Thất bại.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80f6-9ecc-ca27ad46b8ae" class="bulleted-list"><li style="list-style-type:circle">If gateway callback hasn’t arrived:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8000-94fa-f7ad331fb004" class="bulleted-list"><li style="list-style-type:square">Show spinner + message:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80f9-bf9b-c7f9f6879363" class="bulleted-list"><li style="list-style-type:disc">“Hệ thống đang xác nhận thanh toán. Nếu cần, vui lòng không đóng ứng dụng.”</li></ul></div></li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80c2-863c-d72899efb54c" class="bulleted-list"><li style="list-style-type:circle">If failure:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8098-bc0f-ed520271eedd" class="bulleted-list"><li style="list-style-type:square">Offer:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-801e-9dae-dedeb989a2b5" class="bulleted-list"><li style="list-style-type:disc">retry same method,</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80b5-8006-f4178475f1f3" class="bulleted-list"><li style="list-style-type:disc">switch to cash.</li></ul></div></li></ul></div></li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-808c-90b1-ccb3a0b87fd2" class=""><strong>2.3 Receipts &amp; invoices</strong></h2></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8015-9037-d376fc249550" class="bulleted-list"><li style="list-style-type:disc"><strong>Trip history</strong>:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8034-a95c-e2ac67f8c721" class="bulleted-list"><li style="list-style-type:circle">Each trip shows a tag:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80ae-8b9d-d5f1afdbea06" class="bulleted-list"><li style="list-style-type:square">“Tiền mặt”</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80ea-b95d-c9a576619d15" class="bulleted-list"><li style="list-style-type:square">“MoMo thành công”</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-808e-a96e-e38aff15958f" class="bulleted-list"><li style="list-style-type:square">“VNPAY QR thành công”</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-808e-8a34-d1128f7aca31" class="bulleted-list"><li style="list-style-type:circle">Tap → trip details:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8045-b5ee-d26c1c2921c5" class="bulleted-list"><li style="list-style-type:square">Payment reference: internal transaction_id + provider orderId or vnp_TxnRef.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80dc-bfad-d331caf8b5ec" class="bulleted-list"><li style="list-style-type:square">Button:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-807a-a74a-e4b99b29c43d" class="bulleted-list"><li style="list-style-type:disc">“Yêu cầu hóa đơn” (calls MISA through UniCore).</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80d3-8d1a-c43926150c1b" class="bulleted-list"><li style="list-style-type:disc">“Xem hóa đơn” (download from MISA).</li></ul></div></li></ul></div></li></ul></div></li></ul></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8046-b48b-d5d4c0063608" class="">UX, legally:</p></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-809e-906c-d8e0f8456174" class="bulleted-list"><li style="list-style-type:disc">Must show legal entity name and tax ID in the invoice section.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8035-be9a-e7cf33ea2406" class="bulleted-list"><li style="list-style-type:disc">Terms and data-protection links accessible from payment screens.</li></ul></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-801f-85da-f585cca71741"/></div><div style="display:contents" dir="auto"><h1 id="2c0c5e6f-95bd-8061-aef4-f57a4ed75e1d" class=""><strong>3. Document 1 – Detailed MISA Integration Spec</strong></h1></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-809b-ad9f-eef6f8757653" class="">Goal: <strong>end-to-end e-invoice</strong> for every non-cash payment, with optional invoices for cash trips.</p></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-809d-819d-eccc780d04a6" class=""><strong>3.1 Roles and assumptions</strong></h2></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8053-ba16-fecd196c5274" class="bulleted-list"><li style="list-style-type:disc">UniPower is the <strong>seller</strong> issuing VAT invoices.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8069-93d4-e8320dfe797b" class="bulleted-list"><li style="list-style-type:disc">MISA is the <strong>certified e-invoice platform</strong> (per VN tax regulations).</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-802f-9c74-d5edfeefbbee" class="bulleted-list"><li style="list-style-type:disc">UniCore connects to MISA via their official API (REST/JSON or SOAP depending on deployment).</li></ul></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-8050-8e1d-d2a4bd4ecb81" class=""><strong>3.2 Data model</strong></h2></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8005-ab95-c75ffa56cfac" class="">Key fields for InvoiceRequest:</p></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80d4-99fb-d5b46705c407" class="bulleted-list"><li style="list-style-type:disc">invoice_id (internal UUID)</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8013-abdf-daa4abb2a5d3" class="bulleted-list"><li style="list-style-type:disc">ride_id</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80ee-96a2-cbf6a5b8af10" class="bulleted-list"><li style="list-style-type:disc">payment_transaction_id</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8041-8aeb-ed4a664c8c3c" class="bulleted-list"><li style="list-style-type:disc">buyer_type: INDIVIDUAL / COMPANY</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8092-9925-c547d2a6bfeb" class="bulleted-list"><li style="list-style-type:disc">Buyer info:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-809a-adef-e0b1be3e39cc" class="bulleted-list"><li style="list-style-type:circle">buyer_name</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8025-8ef6-ebf81077a216" class="bulleted-list"><li style="list-style-type:circle">tax_code (company)</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80bf-8261-c5ae1cce71b6" class="bulleted-list"><li style="list-style-type:circle">company_name</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-808f-99d9-c5b2e0dc3fce" class="bulleted-list"><li style="list-style-type:circle">address</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8094-91c2-ce3076cd953f" class="bulleted-list"><li style="list-style-type:circle">email</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8000-9f3e-fb2a361fa3d9" class="bulleted-list"><li style="list-style-type:circle">phone</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-805e-80b8-ee4f398e408a" class="bulleted-list"><li style="list-style-type:disc">Invoice amounts:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80dd-afbd-eb7e816dfc9a" class="bulleted-list"><li style="list-style-type:circle">subtotal</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-801b-b55d-e379b3f834b9" class="bulleted-list"><li style="list-style-type:circle">tax_rate</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-801b-853e-f18e9f0b3abe" class="bulleted-list"><li style="list-style-type:circle">tax_amount</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8005-84c8-cc168ff414da" class="bulleted-list"><li style="list-style-type:circle">total_amount</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80f7-a3d9-da05355e22fa" class="bulleted-list"><li style="list-style-type:disc">Line items (array):<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8079-bb51-eb134e315a8c" class="bulleted-list"><li style="list-style-type:circle">description (e.g. “Dịch vụ vận chuyển hành khách bằng taxi công nghệ”)</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-809c-bcdf-dd69b83e417b" class="bulleted-list"><li style="list-style-type:circle">unit</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-805c-9cde-d5968b1b9d84" class="bulleted-list"><li style="list-style-type:circle">quantity</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80fd-a812-f978db472f82" class="bulleted-list"><li style="list-style-type:circle">unit_price</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8014-96a1-d331decf292e" class="bulleted-list"><li style="list-style-type:circle">line_total</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80c0-8e60-d7557d4951e2" class="bulleted-list"><li style="list-style-type:disc">Metadata:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80a7-a509-eeab608a041f" class="bulleted-list"><li style="list-style-type:circle">payment_method (CASH/MOMO/VNPAY/…)</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-800c-938b-e9ea36b8e0fe" class="bulleted-list"><li style="list-style-type:circle">payment_ref (gateway orderId / txnRef)</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80c6-9867-f3b2f6a68f50" class="bulleted-list"><li style="list-style-type:circle">issue_channel: MOBILE_APP</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80bf-ad1b-c2c27084f378" class="bulleted-list"><li style="list-style-type:circle">created_at, updated_at</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-8030-a221-f85e465c7408" class=""><strong>3.3 API flows</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2c0c5e6f-95bd-8070-afe0-cdb36f9ea710" class=""><strong>3.3.1 Customer requests invoice</strong></h3></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-802a-9f24-f880db09936c" class="">From UniApp:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-804d-b623-e7375266e7eb" class="numbered-list" start="1"><li>User taps <strong>“Yêu cầu hóa đơn”</strong> in trip details.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-80ef-b54b-efb90b3cde9e" class="numbered-list" start="2"><li>App shows form:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-805e-b7db-d51c72d36ee3" class="bulleted-list"><li style="list-style-type:disc">For individual: name, email, phone.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8068-b341-f159e265a1c5" class="bulleted-list"><li style="list-style-type:disc">For company: company name, tax code, address, email.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-80db-8018-ee94f2f69cef" class="numbered-list" start="3"><li>App POST → POST /api/invoices/request:</li></ol></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80fd-9ca7-e26912a45d09" class="">Example body (simplified):</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2c0c5e6f-95bd-80ff-b4c6-e1c30b6e3e1d" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">{
  &quot;ride_id&quot;: &quot;RIDE-123&quot;,
  &quot;buyer_type&quot;: &quot;COMPANY&quot;,
  &quot;company_name&quot;: &quot;Cong ty ABC&quot;,
  &quot;tax_code&quot;: &quot;0101234567&quot;,
  &quot;address&quot;: &quot;123 Pho Hue, Ha Noi&quot;,
  &quot;email&quot;: &quot;ketoan@abc.com&quot;
}</code></pre></div><div style="display:contents" dir="auto"><h3 id="2c0c5e6f-95bd-80d7-9427-d76fd5ab5c29" class=""><strong>3.3.2 UniCore creates InvoiceRequest</strong></h3></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8008-b69a-db6b24c127bc" class="bulleted-list"><li style="list-style-type:disc">Validate ride &amp; payment status SUCCEEDED.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8046-ae66-edd30b99c86a" class="bulleted-list"><li style="list-style-type:disc">Ensure no existing issued invoice for this ride.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8051-aa8d-e9198d43d17c" class="bulleted-list"><li style="list-style-type:disc">Save InvoiceRequest with status PENDING.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80d0-899d-ea20b098110b" class="bulleted-list"><li style="list-style-type:disc">Add to <strong>MISA dispatch queue</strong>.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2c0c5e6f-95bd-80bc-9bed-fa641e854bda" class=""><strong>3.3.3 Dispatch to MISA</strong></h3></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8008-a467-ca10653fb0bd" class="">Service MisaAdapter runs (sync or background job):</p></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-80ac-afe4-d85a99cb3891" class="numbered-list" start="1"><li>Fetch pending InvoiceRequests.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-8008-bc23-f8891200b398" class="numbered-list" start="2"><li>Transform to MISA request format:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8074-885d-c77857472ae6" class="bulleted-list"><li style="list-style-type:disc">mapping fields to MISA schema (customer info, items, tax rate).</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-8022-9120-ce140d390d04" class="numbered-list" start="3"><li>Call MISA API:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8062-97ec-e7ef28e216fe" class="bulleted-list"><li style="list-style-type:disc">CreateInvoice / IssueInvoice endpoint.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-802e-8d02-c372295d52b7" class="bulleted-list"><li style="list-style-type:disc">Include digital signature or token as required.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-8074-b986-db75769bcf6b" class="numbered-list" start="4"><li>MISA returns:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8039-b6ba-e9c5912b91fc" class="bulleted-list"><li style="list-style-type:disc">success: InvoiceNo, InvoiceSeries, IssueDate, LinkPDF or base64 PDF.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-800c-8335-f9da86d2517b" class="bulleted-list"><li style="list-style-type:disc">failure: error code + message.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><h3 id="2c0c5e6f-95bd-8052-a817-feab00d097e3" class=""><strong>3.3.4 Handling responses</strong></h3></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8048-bcec-d5bf149a6506" class="bulleted-list"><li style="list-style-type:disc">On success:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8011-bd70-eab8d2eb03cc" class="bulleted-list"><li style="list-style-type:circle">Update InvoiceRequest.status = ISSUED.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8061-b634-c4db0a3172a2" class="bulleted-list"><li style="list-style-type:circle">Store:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8008-9891-c9ae32670701" class="bulleted-list"><li style="list-style-type:square">misa_invoice_no</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8091-baa7-f159bfff21df" class="bulleted-list"><li style="list-style-type:square">misa_series</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80f1-93b0-f6019c260213" class="bulleted-list"><li style="list-style-type:square">misa_issue_date</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8025-b8d7-d771a661a0a6" class="bulleted-list"><li style="list-style-type:square">misa_pdf_url or stored blob.</li></ul></div></li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8061-8b0b-eb068e21c4d9" class="bulleted-list"><li style="list-style-type:disc">On failure:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80a7-b064-eaca2d2a9748" class="bulleted-list"><li style="list-style-type:circle">status = FAILED.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-800c-ba52-ee6bcc2c9ba0" class="bulleted-list"><li style="list-style-type:circle">Keep error message for support UI.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-806c-8d9f-d07da5744d00" class="bulleted-list"><li style="list-style-type:circle">Expose to admin to retry after fixing data.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2c0c5e6f-95bd-806a-b507-da36646b1c2f" class=""><strong>3.3.5 Customer view/download</strong></h3></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80d9-8a0d-d7a551159d73" class="">Endpoint: GET /api/invoices/{ride_id}</p></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80fa-a0ed-d43f8167850b" class="bulleted-list"><li style="list-style-type:disc">Returns invoice status + link.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-808b-841f-cd7020505903" class="bulleted-list"><li style="list-style-type:disc">If issued:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-803f-9676-daa120d3dbce" class="bulleted-list"><li style="list-style-type:circle">Provide pdf_url (reverse-proxied through UniCore) or direct MISA link.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8065-8bec-c496c5520237" class="bulleted-list"><li style="list-style-type:disc">App:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80e7-8c97-f90750db2c0b" class="bulleted-list"><li style="list-style-type:circle">Shows Đã phát hành + button <strong>“Tải hóa đơn”</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-806e-a924-c7ff4b831c52" class="bulleted-list"><li style="list-style-type:circle">Opens PDF viewer.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-8034-95e1-f8369b1a53b6" class=""><strong>3.4 Back-office UI (UniPortal)</strong></h2></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80af-ac8a-ef961eba4161" class="">Screens:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-80ed-a8a0-d98812d9b6cc" class="numbered-list" start="1"><li><strong>Invoice Queue</strong><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80da-a9cc-ed810210b37d" class="bulleted-list"><li style="list-style-type:disc">Columns: invoice_id, ride_id, buyer_name, tax_code, amount, status, last_error.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8054-9fb4-dbda32d2a361" class="bulleted-list"><li style="list-style-type:disc">Actions: “Gửi MISA lại”, “Hủy yêu cầu”.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-8046-8fc5-d5b6e5824052" class="numbered-list" start="2"><li><strong>Invoice Detail</strong><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8070-ba0e-f91392d14cd2" class="bulleted-list"><li style="list-style-type:disc">All input fields + gateway payment reference.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-801a-8ad5-d68ccc468d2e" class="bulleted-list"><li style="list-style-type:disc">Logs of MISA calls (timestamp, payload hash, status).</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-8094-8e0f-c36eb578b7ba" class="numbered-list" start="3"><li><strong>Reports</strong><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-803a-8d28-e18e5947da90" class="bulleted-list"><li style="list-style-type:disc">Export CSV for monthly tax declarations.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-8098-ba96-c806f3e2e0be" class=""><strong>3.5 Compliance controls</strong></h2></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8094-b414-ccbff1dc2307" class="bulleted-list"><li style="list-style-type:disc"><strong>Retention</strong>: store invoice metadata ≥ 10 years; PDFs replicated and backed up.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80dd-a258-d6e98c8a4f4d" class="bulleted-list"><li style="list-style-type:disc"><strong>Security</strong>:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80af-8619-c296c01b8e7e" class="bulleted-list"><li style="list-style-type:circle">protect tax information as <strong>sensitive personal data</strong> under PDPD.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80fd-827d-eb1c102cab8b" class="bulleted-list"><li style="list-style-type:circle">log access to Invoice records (who, when, from where).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80eb-aa16-dd1e9ed8eb67" class="bulleted-list"><li style="list-style-type:disc"><strong>Data localization</strong>:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8005-95ac-ecae4d612a5a" class="bulleted-list"><li style="list-style-type:circle">MISA servers are Vietnam-based; UniCore must ensure logs and copies remain in VN data centers.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-8055-a97b-c173f1eafd90"/></div><div style="display:contents" dir="auto"><h1 id="2c0c5e6f-95bd-80b5-b255-c82a34153045" class=""><strong>4. Document 2 – MoMo / VNPAY / ViettelPay / Local Bank Integration</strong></h1></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80a9-86dd-d348f1949737" class="">Goal: <strong>one unified payment abstraction</strong> within UniCore, with <strong>provider-specific adapters</strong>.</p></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-80fd-8d2e-f1b14ada5c9b" class=""><strong>4.1 General payment flow pattern (Grab/Xanh SM style)</strong></h2></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-804d-bfc6-fe4dbb55f7bd" class="numbered-list" start="1"><li><strong>Pre-trip</strong>:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8094-98ce-da36de05dec8" class="bulleted-list"><li style="list-style-type:disc">Customer selects or confirms payment method.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-8032-9819-c126e724a8b0" class="numbered-list" start="2"><li><strong>Trip completed</strong>:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80b3-8218-d128a2ddc765" class="bulleted-list"><li style="list-style-type:disc">Fare is finalised.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80d8-b488-ce6952534e86" class="bulleted-list"><li style="list-style-type:disc">UniCore creates PaymentIntent with amount, currency, method.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-801f-8bdc-e0f158815707" class="numbered-list" start="3"><li><strong>Gateway create payment</strong>:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8093-843b-ecf991a18c57" class="bulleted-list"><li style="list-style-type:disc">UniPay-Service calls specific adapter: MoMo/VNPAY/ViettelPay/Bank.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8073-af92-cfe592ebec8b" class="bulleted-list"><li style="list-style-type:disc">Adapter returns redirectUrl or deeplink (for wallet app).</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-8064-a9ce-d958714db75d" class="numbered-list" start="4"><li><strong>Customer pays</strong>:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80e6-b58b-c7a2acbc9100" class="bulleted-list"><li style="list-style-type:disc">App:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-806e-a598-c5ca652ca970" class="bulleted-list"><li style="list-style-type:circle">For wallets: opens wallet via deep link (MoMo) or webview (VNPAY QR).</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8058-b484-f3f32882d7ca" class="bulleted-list"><li style="list-style-type:circle">For card/banks: opens gateway page for card info or QR.</li></ul></div></li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-803b-a0e1-c18e2d5c6cd5" class="numbered-list" start="5"><li><strong>Gateway callback</strong>:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8031-8ec8-ee60dad32ed4" class="bulleted-list"><li style="list-style-type:disc">User returns to app using redirect URL (returnUrl).</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80dd-89f4-fa359c47ae8e" class="bulleted-list"><li style="list-style-type:disc">Gateway also sends server-to-server notification (IPN/webhook) to UniPay-Service.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-8090-9fce-fa43a418a959" class="numbered-list" start="6"><li><strong>UniCore verifies</strong>:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-809f-b3ed-f7e3259b7ee5" class="bulleted-list"><li style="list-style-type:disc">Verify cryptographic signature.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8011-a2aa-c26c32bac020" class="bulleted-list"><li style="list-style-type:disc">Check amount, orderId / transactionId, status.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80e1-b42f-fa577319776e" class="bulleted-list"><li style="list-style-type:disc">Update PaymentIntent &amp; Ride records.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-801a-ba82-f3cdeb59e6eb" class="numbered-list" start="7"><li><strong>Driver payout &amp; settlement</strong>:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80e9-b944-ea4aaca5b0f2" class="bulleted-list"><li style="list-style-type:disc">Internal settlement engine uses gateway settlement files (T+0/T+1) → ReconciliationBatch.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8001-b715-e302e38e3dfe" class="">This pattern is similar to how MoMo and VNPAY’s own docs describe web/mobile flows.</p></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-80b5-9f30-e895b85470b4"/></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-8065-85d1-d42485dec8d4" class=""><strong>4.2 MoMo Integration (Wallet / App-to-App)</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2c0c5e6f-95bd-801a-b2cd-c2652469198c" class=""><strong>4.2.1 Key parameters</strong></h3></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8047-9d93-ee73c94a94c2" class="">From MoMo docs (names may differ depending on product):</p></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8016-a324-d52a720f4167" class="bulleted-list"><li style="list-style-type:disc">partnerCode, accessKey, secretKey</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80dc-b676-c06afe76ae95" class="bulleted-list"><li style="list-style-type:disc">orderId, requestId</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80f0-ad15-c4b46e9e0ddb" class="bulleted-list"><li style="list-style-type:disc">amount</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-801c-a3bb-d74c35e2dc23" class="bulleted-list"><li style="list-style-type:disc">orderInfo</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8008-b96c-dd7b492249f2" class="bulleted-list"><li style="list-style-type:disc">redirectUrl (back to UniApp)</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-801c-a094-f751ec06c775" class="bulleted-list"><li style="list-style-type:disc">ipnUrl (UniCore notification)</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8051-882d-cec817ba862c" class="bulleted-list"><li style="list-style-type:disc">extraData</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80d6-9407-eec381d22493" class="bulleted-list"><li style="list-style-type:disc">signature (HMAC SHA256 over request fields)</li></ul></div><div style="display:contents" dir="auto"><h3 id="2c0c5e6f-95bd-8070-8f4a-f8be4de14524" class=""><strong>4.2.2 Create payment</strong></h3></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80b9-b9ae-c46ac7ef6b9b" class="">Endpoint (internal): POST /payments/momo/create</p></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8015-8bbc-ea90df727e5c" class="">Input:</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2c0c5e6f-95bd-80db-833e-fee5622da467" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">{
  &quot;ride_id&quot;: &quot;RIDE-123&quot;,
  &quot;amount&quot;: 120000,
  &quot;description&quot;: &quot;Cuoc phi UniTaxi 123&quot;,
  &quot;lang&quot;: &quot;vi&quot;
}</code></pre></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-803a-a1ef-f014d837f23a" class="">Steps:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-80c8-9da9-dda08c271bb3" class="numbered-list" start="1"><li>Validate ride is finished, not yet paid.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-809e-9820-d30e5cf86962" class="numbered-list" start="2"><li>Generate:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-800f-8cbb-c4611c63d195" class="bulleted-list"><li style="list-style-type:disc">orderId = &quot;UTX-&quot; + ride_id + &quot;-&quot; + timestamp</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8087-bf19-d375db54a1b2" class="bulleted-list"><li style="list-style-type:disc">requestId = UUID.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-805c-9496-f56cfe28f56d" class="numbered-list" start="3"><li>Build MoMo payload with fields above.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-80b4-8030-cbcce17abcf2" class="numbered-list" start="4"><li>Compute signature using secretKey.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-805a-b799-e46db3fb333b" class="numbered-list" start="5"><li>Call MoMo create/payment endpoint.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-809d-9da1-d486fbb1a69e" class="numbered-list" start="6"><li>On success, MoMo returns payUrl or deeplink URL.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-80bc-9301-d1b5c724f97d" class="numbered-list" start="7"><li>Save PaymentTransaction with status PENDING_GATEWAY, store orderId, requestId.</li></ol></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80eb-9792-e4f07e5bf8ff" class="">UniApp:</p></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-807b-ad7b-ffc25ea53c91" class="bulleted-list"><li style="list-style-type:disc">Opens payUrl in:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80ee-852a-cfc12f984bdd" class="bulleted-list"><li style="list-style-type:circle">mobile browser / in-app webview, or</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-800f-bc99-f1ac312ebc20" class="bulleted-list"><li style="list-style-type:circle">deep link to MoMo app for app-to-app experience (similar to Grab).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><h3 id="2c0c5e6f-95bd-80b9-95b1-e5f4dd6aa0c3" class=""><strong>4.2.3 Callback handling</strong></h3></div><div style="display:contents" dir="auto"><h3 id="2c0c5e6f-95bd-8011-8cb0-f3f61cad4ed4" class=""><strong>a) Customer redirect</strong></h3></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-809f-966e-ebdbab29b725" class="bulleted-list"><li style="list-style-type:disc">MoMo redirects user to redirectUrl with query params (orderId, resultCode, message, signature, …).</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-804d-b7c8-e422036594cc" class="bulleted-list"><li style="list-style-type:disc">App loads your redirectUrl route (via webview).</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8048-b59e-e08c51cb36ec" class="bulleted-list"><li style="list-style-type:disc">Backend verifies signature again and shows success/failure screen to user.</li></ul></div><div style="display:contents" dir="auto"><h3 id="2c0c5e6f-95bd-8065-9000-eed8425a9855" class=""><strong>b) IPN (server-to-server)</strong></h3></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80dd-a1d2-d5540cd8d151" class="">MoMo calls ipnUrl with JSON:</p></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80e2-a402-d21721843741" class="bulleted-list"><li style="list-style-type:disc">Contains orderId, amount, resultCode, transId, signature, etc.</li></ul></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-804f-98bb-c52fc8636924" class="">UniCore:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-8061-9660-c414d9068a54" class="numbered-list" start="1"><li>Verify signature with secretKey.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-80f0-8a6b-e10433003795" class="numbered-list" start="2"><li>Look up PaymentTransaction by orderId.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-808d-87ba-e4ae2d73a6bd" class="numbered-list" start="3"><li>If resultCode == 0 (success):<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8036-bbcf-ebf9a3ecf62e" class="bulleted-list"><li style="list-style-type:disc">mark PaymentTransaction.status = SUCCESS;</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-801a-8fea-d1f8ca96766e" class="bulleted-list"><li style="list-style-type:disc">mark PaymentIntent.status = SUCCEEDED;</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80d7-9bd6-d6bef9cbd212" class="bulleted-list"><li style="list-style-type:disc">set Ride.payment_status = PAID_NONCASH.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-80b1-ba50-f7fc60b1eea2" class="numbered-list" start="4"><li>If failure:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80c0-b5a2-e8064fe0210e" class="bulleted-list"><li style="list-style-type:disc">mark as FAILURE, keep reason.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-8034-9525-cdd0124a4693" class="numbered-list" start="5"><li>Idempotency: ignore duplicate IPNs by checking existing status.</li></ol></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-8058-a274-fb58f0c4ea23"/></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-80e4-8021-d8587f0ab927" class=""><strong>4.3 VNPAY Integration (QR / Card / Bank)</strong></h2></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8017-bf27-fc4898dd089b" class="">VNPAY is commonly used by VN platforms; integration pattern is <strong>redirect with signed query</strong>.</p></div><div style="display:contents" dir="auto"><h3 id="2c0c5e6f-95bd-80ca-a45c-de4646bfd107" class=""><strong>4.3.1 Key parameters</strong></h3></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80cc-85ae-c39434bd4234" class="">Common fields:</p></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80ec-afc0-dc5dc3ae7226" class="bulleted-list"><li style="list-style-type:disc">vnp_Version</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80cb-bf22-e236bae7cd84" class="bulleted-list"><li style="list-style-type:disc">vnp_TmnCode</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-806e-9760-cf862ff6891d" class="bulleted-list"><li style="list-style-type:disc">vnp_Amount (×100 per docs)</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8073-94a1-e4d3752d43c1" class="bulleted-list"><li style="list-style-type:disc">vnp_Command (pay)</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-804a-94e9-efbd8cf49ecb" class="bulleted-list"><li style="list-style-type:disc">vnp_CreateDate</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8057-8f63-e44cb062c931" class="bulleted-list"><li style="list-style-type:disc">vnp_CurrCode (VND)</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80a6-b824-f64af4a532b5" class="bulleted-list"><li style="list-style-type:disc">vnp_IpAddr</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80e3-8414-ee409bed75ee" class="bulleted-list"><li style="list-style-type:disc">vnp_Locale (vn)</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80fa-a668-fff9438e0f1a" class="bulleted-list"><li style="list-style-type:disc">vnp_OrderInfo</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8075-963f-d2eab80be752" class="bulleted-list"><li style="list-style-type:disc">vnp_OrderType</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8072-83e8-d2de277bd625" class="bulleted-list"><li style="list-style-type:disc">vnp_ReturnUrl (back to app)</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80c1-a044-d38ad1997c29" class="bulleted-list"><li style="list-style-type:disc">vnp_TxnRef (your order ref)</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80ab-9078-d093cc7e2567" class="bulleted-list"><li style="list-style-type:disc">vnp_SecureHash (HMAC over query string)</li></ul></div><div style="display:contents" dir="auto"><h3 id="2c0c5e6f-95bd-80e4-9746-e75a49764e42" class=""><strong>4.3.2 Create payment</strong></h3></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8024-969b-cd4319f52eca" class="">Endpoint: POST /payments/vnpay/create</p></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80a0-b59d-ecea50fc4e1f" class="">Steps:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-80bf-abcc-efe02a279e3c" class="numbered-list" start="1"><li>Similar to MoMo, but:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80af-af14-cf7e865d9142" class="bulleted-list"><li style="list-style-type:disc">build query parameters,</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8018-9568-fb65372f028c" class="bulleted-list"><li style="list-style-type:disc">sort and concatenate as required,</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-803e-b255-ea14bbeaa513" class="bulleted-list"><li style="list-style-type:disc">compute vnp_SecureHash.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-80e1-b77d-e91225a8a918" class="numbered-list" start="2"><li>Redirect URL:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8054-8631-d163a6e113d3" class="bulleted-list"><li style="list-style-type:disc">paymentUrl = vnp_Url + &quot;?&quot; + queryString + &quot;&amp;vnp_SecureHash=&quot; + hash.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-807e-a173-d861b65a9bb1" class="numbered-list" start="3"><li>Return to app for webview open.</li></ol></div><div style="display:contents" dir="auto"><h3 id="2c0c5e6f-95bd-8015-8e50-fade9aac2ca6" class=""><strong>4.3.3 ReturnUrl + IPN</strong></h3></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80a3-a001-fc6f1dbe0b2e" class="bulleted-list"><li style="list-style-type:disc">VNPAY hits ReturnUrl in browser with back query.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-801c-b91a-e80db45f4233" class="bulleted-list"><li style="list-style-type:disc">Also call <strong>IPN URL</strong> server-to-server with transaction status.</li></ul></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-805a-9942-fdf28709547d" class="">UniCore:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-8043-a987-fb52dacff49b" class="numbered-list" start="1"><li>Verify vnp_SecureHash.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-8046-9677-f7cb0718fffa" class="numbered-list" start="2"><li>Validate vnp_Amount vs internal.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-805b-8155-d5da6690cd7e" class="numbered-list" start="3"><li>Map vnp_ResponseCode:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8053-a9ed-dc0353b29579" class="bulleted-list"><li style="list-style-type:disc">00 = success.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-807a-b5ec-ea05fc0d6f76" class="numbered-list" start="4"><li>Update PaymentTransaction and PaymentIntent same as MoMo.</li></ol></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-803d-abe3-f657f7236801"/></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-8087-a3c5-ea17df37ffe3" class=""><strong>4.4 ViettelPay Integration</strong></h2></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8025-9e4f-ed61187f2e64" class="">ViettelPay (or Viettel Money) exposes similar REST APIs:</p></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8050-b3ae-db5d25d14089" class="bulleted-list"><li style="list-style-type:disc">Create transaction → receive transaction code + redirect URL.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80c7-96c6-d9a3005b89d2" class="bulleted-list"><li style="list-style-type:disc">Customer pays in app or via OTP.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-800d-b388-ce3457051c78" class="bulleted-list"><li style="list-style-type:disc">ViettelPay notifies result via callback.</li></ul></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-803e-bcb9-e2edbc782a31" class="">Integration pattern:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-80d2-98fc-e33902985546" class="numbered-list" start="1"><li>UniCore builds signed request (appId, partnerCode, amount, orderCode, callbackUrl, …).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-8035-8965-e73175330ce8" class="numbered-list" start="2"><li>Uses HTTPS POST to ViettelPay gateway.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-80ab-8b08-e985078552a7" class="numbered-list" start="3"><li>Receives paymentUrl.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-804e-b377-c6eab9378517" class="numbered-list" start="4"><li>App opens paymentUrl.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-80c6-b0df-c8e2048346ab" class="numbered-list" start="5"><li>ViettelPay sends callback to UniPay-Service with signed payload.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-80af-882d-ca7b93d1831c" class="numbered-list" start="6"><li>UniCore verifies signature and updates status.</li></ol></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8054-82cd-ef4a9e8a81aa" class="">The exact field names &amp; signature algorithms must follow ViettelPay’s partner document, but you keep <strong>the same internal abstraction</strong> as for MoMo/VNPAY.</p></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-80c6-8f9d-f6f54d8c0351"/></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-8045-b6d0-ef7b27509161" class=""><strong>4.5 Local bank / card payments (Napas / Internet banking)</strong></h2></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-802b-b1de-d25e524a270a" class="">Usually provided through:</p></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-809f-bc19-c314413e403f" class="bulleted-list"><li style="list-style-type:disc">VNPAY Card/ATM product, or</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-803a-ae96-d12b7566e1b6" class="bulleted-list"><li style="list-style-type:disc">another PGW using <strong>Napas 2.0</strong> switching standard.</li></ul></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8057-b295-e9614392d775" class="">Pattern:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-803a-86c9-fd86c6a33868" class="numbered-list" start="1"><li>UniCore calls PGW with:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-804c-9b1b-c918ff0be9ea" class="bulleted-list"><li style="list-style-type:disc">transaction info,</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8081-b08f-d6d9b80d341a" class="bulleted-list"><li style="list-style-type:disc">selected bank code,</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80e7-88b6-d80a4c259aae" class="bulleted-list"><li style="list-style-type:disc">callback URLs.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-80c5-b15f-ce68d9e92eb3" class="numbered-list" start="2"><li>PGW:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-801a-967a-f94b608e667e" class="bulleted-list"><li style="list-style-type:disc">shows bank login page or QR.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-8083-983c-ff7c6f1cd88a" class="numbered-list" start="3"><li>Bank authenticates and authorizes.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-8048-b58a-cc87e88f6a50" class="numbered-list" start="4"><li>PGW sends result to UniCore IPN.</li></ol></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-807a-9b9f-c022ca05ee28" class="">Implementation in UniCore:</p></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8072-970b-e4376b6ccd57" class="bulleted-list"><li style="list-style-type:disc">Treat as <strong>CARD_BANK method</strong> but reuse the <strong>VNPAY-style adapter</strong>:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80ef-a09b-ec51b445f5f3" class="bulleted-list"><li style="list-style-type:circle">same internal createPayment, handleCallback, mapStatus.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-8082-b9c3-e1911270613f"/></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-8072-b165-d28ef2999ecd" class=""><strong>4.6 Internal APIs (uni pay service)</strong></h2></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8013-b18d-fff9c7621977" class="">Define a <strong>provider-agnostic</strong> interface:</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2c0c5e6f-95bd-8096-8f7e-e29e637560bc" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">interface PaymentProvider {
  createPayment(intent: PaymentIntent): Promise&lt;CreatePaymentResult&gt;;
  handleCallback(payload: any): PaymentResult;
  handleIpn(payload: any): PaymentResult;
}</code></pre></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80c6-a208-f14b77e1fe0a" class="">Where:</p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2c0c5e6f-95bd-80af-a933-fb28c1cbac3d" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">type CreatePaymentResult = {
  payment_transaction_id: string;
  redirect_url: string;
  provider_metadata: any;
};

type PaymentResult = {
  payment_transaction_id: string;
  status: &quot;SUCCESS&quot; | &quot;FAILURE&quot;;
  provider_txn_id?: string;
  error_code?: string;
  raw_payload: any;
};</code></pre></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80ef-a598-ec5bec4adc54" class="">Concrete adapters:</p></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80ee-be06-d2c47c22157d" class="bulleted-list"><li style="list-style-type:disc">MomoProvider</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-802c-b7c4-d055b56ff49b" class="bulleted-list"><li style="list-style-type:disc">VnpayProvider</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8031-a0f0-ee0950d00c07" class="bulleted-list"><li style="list-style-type:disc">ViettelPayProvider</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8072-a569-eb7d99131f41" class="bulleted-list"><li style="list-style-type:disc">BankProvider (could wrap VNPAY card product)</li></ul></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-80c6-b950-ec9b6026258d"/></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-8084-b21a-ded9226c22a8" class=""><strong>4.7 Reconciliation &amp; settlement</strong></h2></div><div style="display:contents" dir="auto"><h3 id="2c0c5e6f-95bd-80e2-9f24-ec39ed628fa9" class=""><strong>4.7.1 Daily process (T+0 / T+1)</strong></h3></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80b5-bfa0-ded88c971ccc" class="">For each provider:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-806b-845e-e3ddf05dde9f" class="numbered-list" start="1"><li><strong>Download settlement file</strong> (CSV, Excel, API) for previous day.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-8061-9b26-ec448976b4af" class="numbered-list" start="2"><li>Import into ReconciliationBatch with fields:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-804a-b56d-ccbcf8abd99b" class="bulleted-list"><li style="list-style-type:disc">provider_txn_id</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8069-bbe0-c5c9fee5f542" class="bulleted-list"><li style="list-style-type:disc">merchant_order_id (orderId/TxnRef)</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8077-b735-d52bbe514ccd" class="bulleted-list"><li style="list-style-type:disc">amount</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-809b-921f-f1449b68bc33" class="bulleted-list"><li style="list-style-type:disc">fee</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8092-b13e-ea4774f8cfc2" class="bulleted-list"><li style="list-style-type:disc">net_amount</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-800b-9c93-ec431ccf0253" class="bulleted-list"><li style="list-style-type:disc">status</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80ad-8778-e917f50dd469" class="bulleted-list"><li style="list-style-type:disc">payout_date</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-80cb-b225-f9085a31c6d9" class="numbered-list" start="3"><li>Match against internal PaymentTransaction:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80e4-8289-cb71c90358e5" class="bulleted-list"><li style="list-style-type:disc"><strong>FULL MATCH</strong>: amount &amp; status align → mark RECONCILED.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-805c-ab4d-d223913974c7" class="bulleted-list"><li style="list-style-type:disc"><strong>MISMATCH</strong>: log for manual investigation.</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2c0c5e6f-95bd-806e-a8fc-fcfc32958179" class="numbered-list" start="4"><li>Generate summary per day:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80df-839c-cc4110cc858b" class="bulleted-list"><li style="list-style-type:disc">total collected,</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-809b-a7b2-ca7467616d7e" class="bulleted-list"><li style="list-style-type:disc">total fees,</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80e3-939c-e03fd31b9fc6" class="bulleted-list"><li style="list-style-type:disc">net to UniPower,</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80db-aff3-e2784173f53f" class="bulleted-list"><li style="list-style-type:disc">net to drivers (if using split-payment via future feature).</li></ul></div></li></ol></div><div style="display:contents" dir="auto"><h3 id="2c0c5e6f-95bd-80f8-affc-c07cf9a64a44" class=""><strong>4.7.2 Audit &amp; logging</strong></h3></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80c5-a3cf-d56c45a4d837" class="bulleted-list"><li style="list-style-type:disc">Every change of payment status must keep:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8039-8ea2-d4d3b9ae5c43" class="bulleted-list"><li style="list-style-type:circle">old_status, new_status,</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8073-b6ad-f43b77fb7c4b" class="bulleted-list"><li style="list-style-type:circle">actor (system/cron/admin),</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8070-ade3-f159b81e2bcb" class="bulleted-list"><li style="list-style-type:circle">source (IPN, admin fix, manual adjustment).</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-809e-a700-f837d19179fc" class="bulleted-list"><li style="list-style-type:disc">Logs kept ≥ 5 years.</li></ul></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-8063-8083-ecb2da36ea58"/></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-80e3-9c6e-d935697751bd" class=""><strong>4.8 Security &amp; Infosec</strong></h2></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-80d7-aee1-f47cf7fd0e57" class="">Consistent with your Canberra-level Infosec background:</p></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80bf-9b67-d52e45a3d078" class="bulleted-list"><li style="list-style-type:disc"><strong>Key management</strong><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-803e-a197-dfd55db4e33a" class="bulleted-list"><li style="list-style-type:circle">partner keys (secretKey, certificates) stored in HSM or at least encrypted at rest.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8073-b0a3-e9a5687fa4e2" class="bulleted-list"><li style="list-style-type:circle">Rotation plan with very limited staff access.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8034-bc82-e472bb7c3021" class="bulleted-list"><li style="list-style-type:disc"><strong>Network</strong><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80e8-af02-d7e9322db3e7" class="bulleted-list"><li style="list-style-type:circle">restrict payment callback endpoints by IP allow-list where provider supports.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-802c-a287-e3673558f954" class="bulleted-list"><li style="list-style-type:disc"><strong>Data</strong><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8070-a655-ee83808e57e2" class="bulleted-list"><li style="list-style-type:circle">Never store full card PAN or CVV (handled by PGWs).</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8091-b590-eed1138de107" class="bulleted-list"><li style="list-style-type:circle">Store only masked card numbers for display.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80c3-96c9-cc64ffb0f6a6" class="bulleted-list"><li style="list-style-type:disc"><strong>Monitoring</strong><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80b6-89b2-d23eee6abd40" class="bulleted-list"><li style="list-style-type:circle">Alert when:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-804f-8dbe-f7e40edea2d3" class="bulleted-list"><li style="list-style-type:square">unusually high failure rate per provider,</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-808a-8623-eb810fbde3f5" class="bulleted-list"><li style="list-style-type:square">bursts of small repeated payments,</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80fd-945e-c9f50ce972b6" class="bulleted-list"><li style="list-style-type:square">abnormal refund activity.</li></ul></div></li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-8045-a6e5-d68061e37dbd"/></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-8093-823f-f6b7d42bf34f" class=""><strong>4.9 Edge cases / flows</strong></h2></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8019-80e3-f48767e03364" class="bulleted-list"><li style="list-style-type:disc"><strong>Payment timeout</strong><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80ac-a8da-f76be4b9c233" class="bulleted-list"><li style="list-style-type:circle">If IPN not received within X minutes:<div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-805c-a933-ca8e77568031" class="bulleted-list"><li style="list-style-type:square">mark PaymentIntent as PENDING_REVIEW.</li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-807c-9227-cf09c8be0596" class="bulleted-list"><li style="list-style-type:square">show message: “Hệ thống chưa nhận được kết quả thanh toán. Vui lòng kiểm tra lại trong Lịch sử chuyến đi.”</li></ul></div></li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80ec-880d-c23b9993d148" class="bulleted-list"><li style="list-style-type:disc"><strong>Customer pays but app closed</strong><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80c8-b364-ca00a8dbbe85" class="bulleted-list"><li style="list-style-type:circle">Rely solely on IPN → update backend → trip history shows paid.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8019-8685-e775a276a939" class="bulleted-list"><li style="list-style-type:disc"><strong>Partial refunds</strong><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-8042-8215-de4340f58764" class="bulleted-list"><li style="list-style-type:circle">Implement Refund entity with mapping to provider’s refund API when available.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-807e-9573-fdd923320ef7" class="bulleted-list"><li style="list-style-type:disc"><strong>Disputes</strong><div style="display:contents" dir="auto"><ul id="2c0c5e6f-95bd-80f0-a2ed-f793198ae5b3" class="bulleted-list"><li style="list-style-type:circle">Store all gateway payloads exactly as received for evidence.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-809e-aa54-c50c00947573"/></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-8012-9585-f90c2ef300e9" class=""><strong>1. MoMo Payment Flow (App-to-App)</strong></h2></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2c0c5e6f-95bd-803c-9a9c-ec267b5fb200" class="code code-wrap"><code class="language-Mermaid" style="white-space:pre-wrap;word-break:break-all">sequenceDiagram
    participant User as User (UniApp)
    participant App as UniApp Backend
    participant Pay as UniPay-Service
    participant MoMo as MoMo Gateway

    User-&gt;&gt;App: End ride → request non-cash payment (MoMo)
    App-&gt;&gt;Pay: createPayment(ride_id, amount, method=MoMo)

    Pay-&gt;&gt;Pay: Create PaymentIntent + PaymentTransaction (PENDING_GATEWAY)
    Pay-&gt;&gt;MoMo: POST /payment (partnerCode, orderId, amount, redirectUrl, ipnUrl, signature)
    MoMo--&gt;&gt;Pay: payUrl / deeplink

    Pay--&gt;&gt;App: redirect_url (payUrl)
    App--&gt;&gt;User: Open MoMo app/webview with payUrl

    User-&gt;&gt;MoMo: Confirm payment (PIN/OTP)
    MoMo--&gt;&gt;User: Payment result screen

    %% Browser redirect
    MoMo--&gt;&gt;App: Redirect to redirectUrl (orderId, resultCode, signature)
    App-&gt;&gt;Pay: handleRedirect(orderId, resultCode,...)

    %% Server-to-server IPN
    MoMo--&gt;&gt;Pay: IPN to ipnUrl(orderId, amount, resultCode, transId, signature)
    Pay-&gt;&gt;Pay: Verify signature &amp; amount

    alt resultCode == 0 (success)
        Pay-&gt;&gt;Pay: Update PaymentTransaction=SUCCESS&lt;br/&gt;PaymentIntent=SUCCEEDED
        Pay-&gt;&gt;App: Notify ride paid (non-cash)
        App--&gt;&gt;User: Show &quot;Thanh toán MoMo thành công&quot;
    else failure
        Pay-&gt;&gt;Pay: Update PaymentTransaction=FAILURE
        Pay-&gt;&gt;App: Notify payment failed
        App--&gt;&gt;User: Show failure + options (retry / cash)
    end</code></pre></div><div style="display:contents" dir="auto"><p id="2c0c5e6f-95bd-8055-a545-f1e44b704793" class="">
</p></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-803c-9bca-ddc2dcdf22a5"/></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-80a1-87f6-c1570632d4d7" class=""><strong>2. VNPAY (QR / Card / Bank) Flow</strong></h2></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2c0c5e6f-95bd-8003-8f03-dc1872c10188" class="code code-wrap"><code class="language-Mermaid" style="white-space:pre-wrap;word-break:break-all">sequenceDiagram
    participant User as User (UniApp)
    participant App as UniApp Backend
    participant Pay as UniPay-Service
    participant VNPAY as VNPAY Gateway

    User-&gt;&gt;App: End ride → choose VNPAY (QR/Card/Bank)
    App-&gt;&gt;Pay: createPayment(ride_id, amount, method=VNPAY)

    Pay-&gt;&gt;Pay: Create PaymentIntent + PaymentTransaction (PENDING_GATEWAY)
    Pay-&gt;&gt;Pay: Build vnp_* params + vnp_SecureHash
    Pay-&gt;&gt;VNPAY: Redirect URL (browser/webview open with params)
    VNPAY--&gt;&gt;User: Show QR / card form / bank list

    User-&gt;&gt;VNPAY: Pay via QR scan / bank auth
    VNPAY--&gt;&gt;User: Show result

    %% Browser return
    VNPAY--&gt;&gt;App: Redirect to vnp_ReturnUrl(vnp_TxnRef, vnp_ResponseCode, vnp_SecureHash,...)
    App-&gt;&gt;Pay: handleReturn(vnp_*)

    %% IPN
    VNPAY--&gt;&gt;Pay: IPN(vnp_TxnRef, vnp_ResponseCode, vnp_SecureHash,...)
    Pay-&gt;&gt;Pay: Verify signature + amount

    alt vnp_ResponseCode == &quot;00&quot;
        Pay-&gt;&gt;Pay: PaymentTransaction=SUCCESS&lt;br/&gt;PaymentIntent=SUCCEEDED
        Pay-&gt;&gt;App: Notify ride paid
        App--&gt;&gt;User: Show &quot;Thanh toán VNPAY thành công&quot;
    else
        Pay-&gt;&gt;Pay: PaymentTransaction=FAILURE
        Pay-&gt;&gt;App: Notify payment failed
        App--&gt;&gt;User: Show failure + options (retry / cash)
    end</code></pre></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-80bd-8fb3-ce66bd45edca"/></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-8066-95cc-f72793816417" class=""><strong>3. ViettelPay Flow (same abstraction)</strong></h2></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2c0c5e6f-95bd-80e8-81da-cc56fe191321" class="code code-wrap"><code class="language-Mermaid" style="white-space:pre-wrap;word-break:break-all">sequenceDiagram
    participant User as User (UniApp)
    participant App as UniApp Backend
    participant Pay as UniPay-Service
    participant VT as ViettelPay Gateway

    User-&gt;&gt;App: End ride → choose ViettelPay
    App-&gt;&gt;Pay: createPayment(ride_id, amount, method=ViettelPay)

    Pay-&gt;&gt;Pay: Create PaymentIntent + PaymentTransaction
    Pay-&gt;&gt;VT: POST /createTransaction(appId, orderCode, amount, callbackUrl, signature)
    VT--&gt;&gt;Pay: paymentUrl

    Pay--&gt;&gt;App: redirect_url(paymentUrl)
    App--&gt;&gt;User: Open ViettelPay app/webview

    User-&gt;&gt;VT: Confirm payment
    VT--&gt;&gt;User: Show result

    VT--&gt;&gt;Pay: Callback(orderCode, resultCode, signature)
    Pay-&gt;&gt;Pay: Verify signature + amount

    alt resultCode == SUCCESS
        Pay-&gt;&gt;Pay: PaymentTransaction=SUCCESS&lt;br/&gt;PaymentIntent=SUCCEEDED
        Pay-&gt;&gt;App: Notify ride paid
        App--&gt;&gt;User: Show success
    else
        Pay-&gt;&gt;Pay: PaymentTransaction=FAILURE
        Pay-&gt;&gt;App: Notify failure
        App--&gt;&gt;User: Show failure + options
    end</code></pre></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-8056-b392-c810351c8531"/></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-80d4-aa6e-c8a5f7c64ea7" class=""><strong>4. MISA E-Invoice Flow (after successful non-cash payment)</strong></h2></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2c0c5e6f-95bd-80ae-a415-d5a806b6d638" class="code code-wrap"><code class="language-Mermaid" style="white-space:pre-wrap;word-break:break-all">sequenceDiagram
    participant User as User (UniApp)
    participant App as UniApp Backend
    participant Core as UniCore-API
    participant MISA as MISA eInvoice

    User-&gt;&gt;App: Open trip detail → Tap &quot;Yêu cầu hóa đơn&quot;
    App-&gt;&gt;Core: POST /invoices/request(ride_id, buyer info)

    Core-&gt;&gt;Core: Validate ride &amp; payment SUCCEEDED
    Core-&gt;&gt;Core: Create InvoiceRequest (status=PENDING)

    Note over Core: Invoice job / service

    Core-&gt;&gt;MISA: CreateInvoice(InvoiceRequest mapped → MISA format)
    MISA--&gt;&gt;Core: Response(success: invoiceNo, series, issueDate, pdfLink&lt;br/&gt;or failure: errorCode, message)

    alt success
        Core-&gt;&gt;Core: Update InvoiceRequest=ISSUED&lt;br/&gt;store MISA metadata
        Core--&gt;&gt;App: invoice_status=ISSUED, pdf_url
        App--&gt;&gt;User: Show &quot;Đã phát hành&quot; + button &quot;Tải hóa đơn&quot;
        User-&gt;&gt;App: Download / view PDF (via Core proxy or MISA link)
    else failure
        Core-&gt;&gt;Core: InvoiceRequest=FAILED, store error
        Core--&gt;&gt;App: invoice_status=FAILED, reason
        App--&gt;&gt;User: Show message “Không phát hành được hóa đơn, vui lòng liên hệ CSKH”
    end</code></pre></div><div style="display:contents" dir="auto"><hr id="2c0c5e6f-95bd-804d-a448-e005dd4336a9"/></div><div style="display:contents" dir="auto"><h2 id="2c0c5e6f-95bd-8032-810f-dc9017de421a" class=""><strong>5. Full Ride → Pay → Invoice Overview</strong></h2></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="2c0c5e6f-95bd-8056-ad0a-c484d2eaf197" class="code code-wrap"><code class="language-Mermaid" style="white-space:pre-wrap;word-break:break-all">sequenceDiagram
    participant User as User (UniApp)
    participant Driver as Driver App
    participant Core as UniCore-API
    participant Pay as UniPay-Service
    participant PGW as Payment Gateway (MoMo/VNPAY/VT)
    participant MISA as MISA eInvoice

    User-&gt;&gt;Core: Request ride
    Core--&gt;&gt;Driver: Offer ride
    Driver--&gt;&gt;Core: Accept
    Note over User,Driver: Trip in progress

    Driver-&gt;&gt;Core: End trip (distance/time)
    Core-&gt;&gt;Core: Compute fare, create Ride
    User-&gt;&gt;Core: Confirm payment method (wallet/card/cash)

    alt Non-cash
        Core-&gt;&gt;Pay: createPayment(ride_id, amount, method)
        Pay-&gt;&gt;PGW: Create transaction
        PGW--&gt;&gt;User: Payment UI
        User-&gt;&gt;PGW: Confirm payment
        PGW--&gt;&gt;Pay: IPN result
        Pay-&gt;&gt;Core: Payment SUCCEEDED
        Core--&gt;&gt;User: Show paid status

        User-&gt;&gt;Core: Request invoice
        Core-&gt;&gt;MISA: CreateInvoice(...)
        MISA--&gt;&gt;Core: Invoice issued
        Core--&gt;&gt;User: Link PDF / view
    else Cash
        Core-&gt;&gt;Core: Mark Ride as CASH_DUE
        Driver-&gt;&gt;User: Collect cash
        Driver-&gt;&gt;Core: Confirm collected
        Core--&gt;&gt;User: Trip marked paid (cash)
        opt Cash invoice
            User-&gt;&gt;Core: Request invoice (cash)
            Core-&gt;&gt;MISA: CreateInvoice(...)
            MISA--&gt;&gt;Core: Invoice issued
            Core--&gt;&gt;User: Link PDF
        end
    end</code></pre></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
