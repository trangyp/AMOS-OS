---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Data → Reward Flow Map </title><style>
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
	
</style></head><body><article id="24ac5e6f-95bd-8091-b6cf-d2358bbd24d7" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Data → Reward Flow Map</strong> </h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8082-985a-f879f872f831" class=""><strong>1 — Base Eligibility (Consensus-Required)</strong></h2></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-802e-bffd-f986293d403c" class=""><strong>Directly determines if a session gets </strong><em><strong>any</strong></em><strong> payout.</strong></p></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-807b-a2e1-f9d03cbb10e9" class="bulleted-list"><li style="list-style-type:disc"><code>signal_hash</code> → Confirms authorized master waveform.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80c3-a95a-ed7a5789f7b5" class="bulleted-list"><li style="list-style-type:disc"><code>spec_version</code> → Valid protocol compliance.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-808c-8417-dda9eb43284b" class="bulleted-list"><li style="list-style-type:disc"><code>node_pubkey</code> → Identifies payout recipient.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8079-8131-e724850fb842" class="bulleted-list"><li style="list-style-type:disc"><code>timestamp_start</code> / <code>timestamp_end</code> → Valid measurement window.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-807d-8648-f10e7815cbe5" class="bulleted-list"><li style="list-style-type:disc"><code>consent_token</code> → Proof of opt-in.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-803e-a58d-c92c29be048e" class="bulleted-list"><li style="list-style-type:disc"><code>hrv_rmssd_delta_ms</code> &amp; <code>rsa_delta</code> → Core effect score (<code>S_eff</code>).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80f0-a631-ca89731a64f3" class="bulleted-list"><li style="list-style-type:disc"><code>artifact_rate</code> → Quality gate + part of <code>S_qual</code>.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80fa-a731-d399f7b570e2" class="bulleted-list"><li style="list-style-type:disc"><code>psb_hash</code> &amp; <code>node_signature</code> → Authenticates the Proof-of-Signal Block.</li></ul></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-807e-9e36-d34db05d33fd" class=""><strong>Reward algorithm stage:</strong></p></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8097-8b74-e0d7ff13f19e" class="bulleted-list"><li style="list-style-type:disc"><strong>Preconditions</strong> → Fail = <code>Reward_sats = 0</code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80a1-a7dd-c753d3e195bb" class="bulleted-list"><li style="list-style-type:disc"><code>S_eff</code> computed from <code>hrv_rmssd_delta_ms</code> &amp; <code>rsa_delta</code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-802c-8706-ff8b640ae272" class="bulleted-list"><li style="list-style-type:disc"><code>artifact_rate</code> feeds into <code>Q_art</code> in <code>S_qual</code>.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80bb-9418-d7c35a016e35"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-80d9-a7b0-d762e1cd5cce" class=""><strong>2 — Reward Multiplier Inputs</strong></h2></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8091-916a-cbed693d02ec" class=""><strong>Increase sats earned per valid session.</strong></p></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-8015-8b87-fccf0f1b6796" class=""><strong>A. Effect &amp; Quality</strong></h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8072-a17b-e7d190ee96e8" class="bulleted-list"><li style="list-style-type:disc"><code>affect_var_delta</code> → Bonus in <code>S_eff</code> (optional weight)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-809a-9b04-ea9e41d18ce2" class="bulleted-list"><li style="list-style-type:disc"><code>min_valid_rr_count</code> → <code>Q_rr</code> multiplier in <code>S_qual</code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-807e-9afb-d1db11ca7601" class="bulleted-list"><li style="list-style-type:disc"><code>r2_fit</code> → Quality bonus in <code>S_qual</code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8084-993e-ed4a14ab3992" class="bulleted-list"><li style="list-style-type:disc"><code>motion_vector</code> → Motion penalty in <code>S_qual</code></li></ul></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-809b-818f-e91eb4fc9d29" class=""><strong>B. Context Completeness</strong></h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80fe-bace-cc99f9b3c6e0" class="bulleted-list"><li style="list-style-type:disc"><code>ambient_noise_level</code> → <code>C_env</code> in <code>S_ctx</code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8024-b212-ee2499a2dbde" class="bulleted-list"><li style="list-style-type:disc"><code>ambient_light_level</code> → <code>C_env</code> in <code>S_ctx</code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80f7-87b8-fe09e719d8f4" class="bulleted-list"><li style="list-style-type:disc"><code>delivery_modalities</code> → <code>C_mods</code> in <code>S_ctx</code></li></ul></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-80f7-8bf4-c8a190af0f4d" class=""><strong>C. Coverage &amp; Trust</strong></h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8023-a699-cce4db458fbf" class="bulleted-list"><li style="list-style-type:disc"><code>geo_hint</code> → Scarcity index for <code>S_cov</code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80fe-9aec-cb4ab4b3f2b9" class="bulleted-list"><li style="list-style-type:disc"><code>accept_rate_90d</code> / <code>anom_rate_30d</code> → <code>S_trust</code></li></ul></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-803e-be90-da897c6a3c38" class=""><strong>Reward algorithm stage:</strong></p></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80b7-aef1-c5e9f0e93e7d" class="bulleted-list"><li style="list-style-type:disc"><strong>Multipliers applied after </strong><code><strong>S_eff</strong></code><strong> and </strong><code><strong>S_qual</strong></code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80aa-a9d8-c49bb35de05e" class="bulleted-list"><li style="list-style-type:disc"><code>S_ctx</code> adds up to +10%</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80bd-8496-dbec9b1c6d5f" class="bulleted-list"><li style="list-style-type:disc"><code>S_cov</code> adds up to +30% (geo/time scarcity)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8007-b230-c7971f4bb423" class="bulleted-list"><li style="list-style-type:disc"><code>S_trust</code> adds up to +20% for long-term good behavior</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-800a-a813-e266d4c89447"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8013-a790-d013e7b9bcea" class=""><strong>3 — Vault-Only Monetizable (No Direct Reward Impact)</strong></h2></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8071-86c3-f13921f0560d" class=""><strong>Not part of the reward formula, but high market value in Sovereign Data Vault.</strong></p></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80b4-a6f9-c64fbe340dc1" class="bulleted-list"><li style="list-style-type:disc"><code>rr_intervals_series</code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-800b-97e1-d246074e40b2" class="bulleted-list"><li style="list-style-type:disc"><code>ppg_waveform_segments</code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80a6-a055-dc064071ca07" class="bulleted-list"><li style="list-style-type:disc"><code>ecg_waveform_segments</code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80b2-97e3-ccfdca813099" class="bulleted-list"><li style="list-style-type:disc"><code>respiration_trace</code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8077-b882-f26cbd2b3274" class="bulleted-list"><li style="list-style-type:disc"><code>device_profile</code> &amp; <code>sensor_sampling_rate</code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8077-9fbd-c5024852d980" class="bulleted-list"><li style="list-style-type:disc"><code>mood_index</code>, <code>calmness_index</code>, <code>alertness_index</code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8060-acdf-f3b499da00df" class="bulleted-list"><li style="list-style-type:disc"><code>open_comment</code></li></ul></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-80d7-9136-c412a674d209" class=""><strong>Monetization path:</strong></p></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80ae-a825-fa38e57be344" class="bulleted-list"><li style="list-style-type:disc">Licensed to research, healthcare, or wellness partners for BTC payments</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-806e-a7c9-cf4fd80f4a6f" class="bulleted-list"><li style="list-style-type:disc">Does not influence sats per session (keeps reward formula predictable and fair)</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-8079-91b0-e4064cb38075"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-808a-a48d-f3cf903524d0" class=""><strong>4 — Final Reward Formula Recap</strong></h2></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="24ac5e6f-95bd-8028-9acb-f07d9bb1ff76" class="code code-wrap"><code style="white-space:pre-wrap;word-break:break-all">Reward_sats = floor( B_base * S_eff * S_qual * S_ctx * S_cov * S_trust )
</code></pre></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8019-aa7a-c5f006a9841b" class="bulleted-list"><li style="list-style-type:disc"><strong>B_base</strong>: Base sats per PSB (epoch-controlled)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-808f-b15c-e5b0f9876cb6" class="bulleted-list"><li style="list-style-type:disc"><strong>S_eff</strong>: Effect score from <code>hrv_rmssd_delta_ms</code>, <code>rsa_delta</code> (+optional affect_var_delta)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80a0-a395-fb2e8f737b22" class="bulleted-list"><li style="list-style-type:disc"><strong>S_qual</strong>: Quality score from <code>artifact_rate</code>, <code>min_valid_rr_count</code>, <code>r2_fit</code>, <code>motion_vector</code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-808c-b2d7-d6a9fada6492" class="bulleted-list"><li style="list-style-type:disc"><strong>S_ctx</strong>: Completeness bonus from <code>ambient_noise_level</code>, <code>ambient_light_level</code>, <code>delivery_modalities</code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-807f-b4cc-f4a3350a464e" class="bulleted-list"><li style="list-style-type:disc"><strong>S_cov</strong>: Scarcity multiplier from <code>geo_hint</code> (opt-in) &amp; time slot coverage</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-807e-b194-d89858338ee4" class="bulleted-list"><li style="list-style-type:disc"><strong>S_trust</strong>: Trust multiplier from acceptance rate &amp; anomaly rate history</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80f5-894e-dd3be3f02835"/></div><div style="display:contents" dir="auto"><pre id="24ac5e6f-95bd-8040-880e-e0019327e450" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">flowchart TD
    subgraph CR[Consensus-Required - Base Eligibility]
        A1(signal_hash)
        A2(spec_version)
        A3(node_pubkey)
        A4(timestamp_start / timestamp_end)
        A5(consent_token)
        A6(hrv_rmssd_delta_ms)
        A7(rsa_delta)
        A8(artifact_rate)
        A9(psb_hash)
        A10(node_signature)
    end

    subgraph RM[Reward Multiplier Inputs]
        B1(affect_var_delta)
        B2(min_valid_rr_count)
        B3(r2_fit)
        B4(motion_vector)
        B5(ambient_noise_level)
        B6(ambient_light_level)
        B7(delivery_modalities)
        B8(geo_hint)
        B9(accept_rate_90d / anom_rate_30d)
    end

    subgraph VM[Vault-Only Monetizable]
        C1(rr_intervals_series)
        C2(ppg_waveform_segments)
        C3(ecg_waveform_segments)
        C4(respiration_trace)
        C5(device_profile / sensor_sampling_rate)
        C6(mood_index / calmness_index / alertness_index)
        C7(open_comment)
    end

    CR --&gt; F[Reward Formula]
    RM --&gt; F
    VM --&gt; D[Monetization Layer: BTC licensing / research data sales]

    style CR fill:#ffcccc,stroke:#333,stroke-width:1px
    style RM fill:#ccffcc,stroke:#333,stroke-width:1px
    style VM fill:#ccccff,stroke:#333,stroke-width:1px
    style F fill:#ffffcc,stroke:#333,stroke-width:1px
    style D fill:#e6e6fa,stroke:#333,stroke-width:1px
</code></pre></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8075-8b3a-e9413095a0d3" class="">This shows:</p></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8043-b4c6-f8735a2a3c9a" class="bulleted-list"><li style="list-style-type:disc"><strong>Red</strong> = minimum data for consensus (no reward without it)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8090-ad99-e1306e170102" class="bulleted-list"><li style="list-style-type:disc"><strong>Green</strong> = optional reward multipliers</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80bd-8de2-d87fc737e72c" class="bulleted-list"><li style="list-style-type:disc"><strong>Blue</strong> = vault-only monetizable data</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-807b-abdb-dc91eefdbf57" class="bulleted-list"><li style="list-style-type:disc"><strong>Yellow</strong> = reward calculation</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8050-affc-c45c649fc658" class="bulleted-list"><li style="list-style-type:disc"><strong>Lavender</strong> = off-chain monetization</li></ul></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8059-a0c6-de89ac6f1000" class="">Do you want me to now create the <strong>Bitcoin-style PSB block diagram</strong> that visually packages these datapoints before they are timestamped on-chain?</p></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-8031-99ab-e2cd3011c8db"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8092-8724-cf02c8f53599" class=""><strong>1 — Data → Reward Flow Map</strong> (Mermaid)</h2></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8078-908c-f22868b31fd4" class=""><em>(Shows how each datapoint type connects to the payout formula)</em></p></div><div style="display:contents" dir="auto"><pre id="24ac5e6f-95bd-8004-82bd-d5b0937e8e73" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">flowchart TD
    subgraph CR[&quot;Consensus-Required (Base Eligibility)&quot;]
        A1(signal_hash)
        A2(spec_version)
        A3(node_pubkey)
        A4(timestamp_start / timestamp_end)
        A5(consent_token)
        A6(hrv_rmssd_delta_ms)
        A7(rsa_delta)
        A8(artifact_rate)
        A9(psb_hash)
        A10(node_signature)
    end

    subgraph RM[&quot;Reward Multiplier Inputs&quot;]
        B1(affect_var_delta)
        B2(min_valid_rr_count)
        B3(r2_fit)
        B4(motion_vector)
        B5(ambient_noise_level)
        B6(ambient_light_level)
        B7(delivery_modalities)
        B8(geo_hint)
        B9(accept_rate_90d / anom_rate_30d)
    end

    subgraph VM[&quot;Vault-Only Monetizable&quot;]
        C1(rr_intervals_series)
        C2(ppg_waveform_segments)
        C3(ecg_waveform_segments)
        C4(respiration_trace)
        C5(device_profile / sensor_sampling_rate)
        C6(mood_index / calmness_index / alertness_index)
        C7(open_comment)
    end

    CR --&gt; F[&quot;Reward Formula: Reward_sats = floor( B_base * S_eff * S_qual * S_ctx * S_cov * S_trust )&quot;]
    RM --&gt; F
    VM --&gt; D[&quot;Monetization Layer: BTC licensing / research data sales&quot;]

    style CR fill:#ffcccc,stroke:#333,stroke-width:1px
    style RM fill:#ccffcc,stroke:#333,stroke-width:1px
    style VM fill:#ccccff,stroke:#333,stroke-width:1px
    style F fill:#ffffcc,stroke:#333,stroke-width:1px
    style D fill:#e6e6fa,stroke:#333,stroke-width:1px
</code></pre></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80e9-8b95-cc143ba50b9a"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-80bd-9e36-caac7b6e50b5" class=""><strong>2 — Bitcoin-style PSB Structure</strong></h2></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-807a-9fdf-ee7c3c57df7f" class=""><em>(Shows how datapoints are packaged into a Proof-of-Signal Block before on-chain timestamping)</em></p></div><div style="display:contents" dir="auto"><pre id="24ac5e6f-95bd-8083-b2dd-f6a470c425b7" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">graph TB
    subgraph PSB[Proof-of-Signal Block]
        H1[Block Header]
        H2[Previous PSB Hash]
        H3[Timestamp]
        H4[Node Public Key]
        H5[Validator Signature]

        subgraph DATA[Payload]
            D1[Consensus-Required Data]
            D2[Reward Multiplier Data]
            D3[Vault-Only Monetizable Data]
        end

        H6[Block Hash]
    end

    H1 --&gt; H2 --&gt; H3 --&gt; H4 --&gt; H5 --&gt; DATA --&gt; H6
    style PSB fill:#f0f8ff,stroke:#333,stroke-width:1px
    style DATA fill:#f9f9f9,stroke:#333,stroke-width:1px
</code></pre></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-807f-a4ec-da7a4b3ca93a"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-80d6-a65c-f97a10f43bbf" class=""><strong>3 — Monetization Path Diagram</strong></h2></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-80d8-b5f7-e0aa8761747e" class=""><em>(Shows reward vs external licensing flows)</em></p></div><div style="display:contents" dir="auto"><pre id="24ac5e6f-95bd-802e-861a-e0685d19c2a7" class="code code-wrap"><code class="language-mermaid" style="white-space:pre-wrap;word-break:break-all">flowchart LR
    A[Data Collection Node] --&gt; B[Proof-of-Signal Block]
    B --&gt; C[Reward Engine]
    B --&gt; D[Sovereign Data Vault]

    C --&gt; E[On-Chain BTC Reward]
    D --&gt; F[Off-Chain Licensing]
    D --&gt; G[Research / Healthcare Partnerships]

    style A fill:#ffebcc,stroke:#333,stroke-width:1px
    style B fill:#f0f8ff,stroke:#333,stroke-width:1px
    style C fill:#ffffcc,stroke:#333,stroke-width:1px
    style D fill:#ccccff,stroke:#333,stroke-width:1px
    style E fill:#ccffcc,stroke:#333,stroke-width:1px
    style F fill:#e6e6fa,stroke:#333,stroke-width:1px
    style G fill:#e6e6fa,stroke:#333,stroke-width:1px
</code></pre></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-8093-bca9-c4c1a8121752"/></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-800c-8e38-cefd1fc128a1" class="">If you want, I can also <strong>link all three diagrams into a single “Signal Economy Architecture” doc</strong> so it’s ready for investor decks and engineering wikis.</p></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-805d-921f-e45b48a6d83d" class="">Do you want me to package them like that next?</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
