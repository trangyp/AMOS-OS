---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>What can it read?</title><style>
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
	
</style></head><body><article id="291c5e6f-95bd-8038-89e0-eeb86d9a39b7" class="page sans"><header><h1 class="page-title" dir="auto">What can it read?</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-8009-8e5b-fba1317f1a3c" class="">Here’s a <strong>comprehensive (practically exhaustive)</strong> catalogue of what NeuroSyncAI™ can read/derive today, grouped by signal family. I’ll also note which are <strong>typical on smartwatches</strong> vs. which need <strong>optional medical sensors</strong>.</p></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-804e-8e7b-c209c7524e12"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-8039-9553-ccf357d6af11" class="">1) Cardiovascular &amp; Autonomic (ANS)</h2></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-8030-800b-e193e6f6ad3d" class=""><strong>From smartwatch (PPG/optical HR):</strong></p></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80e1-905e-c367ac9bff1c" class="bulleted-list"><li style="list-style-type:disc"><strong>HR (heart rate)</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8023-bcf4-c6810789023c" class="bulleted-list"><li style="list-style-type:disc"><strong>HRV</strong> (time-domain: <strong>RMSSD, SDNN, pNN50</strong>; frequency-domain: <strong>LF, HF, LF/HF</strong>; non-linear: <strong>SD1/SD2, DFA-α, Sample Entropy</strong>)</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8009-955d-e86fb87f0040" class="bulleted-list"><li style="list-style-type:disc"><strong>Pulse amplitude/shape</strong>, <strong>beat-to-beat variability</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8079-ad5a-fcf08a69e202" class="bulleted-list"><li style="list-style-type:disc"><strong>Pulse Transit Time (PTT)</strong> (proxy for BP trends where feasible)</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80f7-94f9-ee166de7a738" class="bulleted-list"><li style="list-style-type:disc"><strong>Nocturnal HR/HRV trends</strong> (recovery depth)</li></ul></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-802c-8ca1-dcf46ebc83a2" class=""><strong>With optional ECG/clinical monitor:</strong></p></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-809e-a477-da8f67a38b55" class="bulleted-list"><li style="list-style-type:disc"><strong>12/1-lead ECG morphology</strong> (PR/QRS/QT, ST shifts)</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8071-9d4e-d6026e75d661" class="bulleted-list"><li style="list-style-type:disc"><strong>Arrhythmia flags</strong> (AFib, PVC burden), <strong>QTc</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8099-a4d9-ecc002e7e724" class="bulleted-list"><li style="list-style-type:disc"><strong>Baroreflex sensitivity</strong> (if ECG + BP available)</li></ul></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-80bc-9cd2-d3130470de74" class=""><strong>Emotional/physiological inferences:</strong> sympathetic arousal vs. parasympathetic recovery, acute stress, calm/soothe states, fatigue load.</p></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-805a-92c4-c8c2c10e0732"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-80fc-a3fa-c9957b749ed9" class="">2) Respiratory</h2></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-8041-8c52-c6b6699e47cc" class=""><strong>From smartwatch/PPG + IMU:</strong></p></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-804e-a3e0-e53d58782134" class="bulleted-list"><li style="list-style-type:disc"><strong>Respiratory rate (RR)</strong>, <strong>respiratory variability</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80b1-b93d-e806a86a5903" class="bulleted-list"><li style="list-style-type:disc"><strong>Respiratory Sinus Arrhythmia (RSA)</strong> (via HRV coupling)</li></ul></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-80ed-a384-d1a381863026" class=""><strong>With optional respiratory belt/capnography:</strong></p></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80f3-849b-d14c51b617e3" class="bulleted-list"><li style="list-style-type:disc"><strong>Tidal volume trend</strong>, <strong>minute ventilation</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8076-8585-f91db86a9ccc" class="bulleted-list"><li style="list-style-type:disc"><strong>CO₂ end-tidal (EtCO₂)</strong> (clinical)</li></ul></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-8016-a05c-f192354cca4b" class=""><strong>Inferences:</strong> anxiety/relaxation patterns, breath dysregulation, hyperventilation risk, restorative breathing phases.</p></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-8038-b54c-e7427efbd8eb"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-8091-8a24-ee71a82b30d2" class="">3) Oxygenation &amp; Perfusion</h2></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-8029-acaa-cdb7d37ac2aa" class=""><strong>From smartwatch/PPG:</strong></p></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80c7-b04a-cd83c4cf3bee" class="bulleted-list"><li style="list-style-type:disc"><strong>SpO₂ (oxygen saturation)</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80c0-9451-f5603420ed2e" class="bulleted-list"><li style="list-style-type:disc"><strong>Perfusion index</strong> (if exposed by device)</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80e3-9064-d965dfc647d1" class="bulleted-list"><li style="list-style-type:disc"><strong>Peripheral perfusion patterns</strong> (pulse shape)</li></ul></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-8011-a8df-dc1e606cbcb2" class=""><strong>With optional oximeter/ABG:</strong></p></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8014-be0e-e3259a667f57" class="bulleted-list"><li style="list-style-type:disc"><strong>Continuous SpO₂ high precision</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8036-a078-ef285e949b30" class="bulleted-list"><li style="list-style-type:disc"><strong>Lactate/ABG</strong> (clinical lab)</li></ul></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-80c0-99ab-c4e9253a771e" class=""><strong>Inferences:</strong> hypoxia risk, metabolic strain, recovery quality during sleep, altitude/stress adaptation.</p></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-80bf-9efd-f5322004b4c9"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-807d-b997-c3eeb3d742d7" class="">4) Electrodermal &amp; Skin</h2></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-80d6-9a22-d18bbd0378ee" class=""><strong>From EDA/GSR-enabled wearables:</strong></p></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8009-9b8c-ee984cb1086c" class="bulleted-list"><li style="list-style-type:disc"><strong>EDA tonic (SCL)</strong> &amp; <strong>phasic SCRs</strong> (frequency, amplitude, rise/decay)</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8069-9302-d625790153a3" class="bulleted-list"><li style="list-style-type:disc"><strong>Skin micro-temperature</strong> &amp; <strong>gradients</strong> (core–peripheral proxies)</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80c6-ab03-e256d4cfd7a6" class="bulleted-list"><li style="list-style-type:disc"><strong>Skin blood flow</strong> (inferred via PPG/thermal trends)</li></ul></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-8020-83b1-d01bfe16a9ef" class=""><strong>Inferences:</strong> emotional arousal, nociceptive (pain-like) responses, startle/orienting responses, thermal stress.</p></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-80a3-a7cd-c7cd15315aec"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-80a5-9f97-e91941a346f5" class="">5) Thermoregulation &amp; Circadian</h2></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-804f-81dd-eb64f9efbc99" class=""><strong>From smartwatch/skin sensors:</strong></p></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80ae-9ddd-e492a8affa5e" class="bulleted-list"><li style="list-style-type:disc"><strong>Skin temperature (absolute &amp; delta)</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-805c-aa25-e743cda22d61" class="bulleted-list"><li style="list-style-type:disc"><strong>Circadian phase markers</strong> (sleep–wake, body temp rhythm)</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-806e-bb51-d13ffa3152bb" class="bulleted-list"><li style="list-style-type:disc"><strong>Menstrual/ovulatory temp trends</strong> (if enabled)</li></ul></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-8053-8c96-cd2b9ddc1eb0" class=""><strong>Inferences:</strong> inflammation/stress load, recovery window timing, circadian alignment/misalignment.</p></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-80e3-8a43-e17547fbc8f2"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-80d8-a11a-fc55bd0732fb" class="">6) Sleep &amp; Arousal Architecture</h2></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-801f-b947-cdcb25eb91a2" class=""><strong>From smartwatch (actigraphy + HRV/SpO₂):</strong></p></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-809e-8d09-d086a2c48ece" class="bulleted-list"><li style="list-style-type:disc"><strong>Sleep/wake detection</strong>, <strong>stage estimates</strong> (light/deep/REM; model-dependent)</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8060-8d58-e11206f7ba95" class="bulleted-list"><li style="list-style-type:disc"><strong>Sleep efficiency, latency, fragmentation</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8024-8a3e-f2306700abed" class="bulleted-list"><li style="list-style-type:disc"><strong>Arousal index</strong>, <strong>nocturnal desaturations</strong></li></ul></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-804f-9151-f698069e33cb" class=""><strong>Inferences:</strong> restorative sleep depth, autonomic recovery, insomnia/OSA risk cues (screening, not diagnosis).</p></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-809c-a2f6-e5647bdc92c4"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-8083-a45a-c21f3db0b081" class="">7) Movement, Posture &amp; Motor Micro-Signals</h2></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-8024-b143-f8764df82c3f" class=""><strong>From IMU (accelerometer/gyroscope):</strong></p></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80be-9529-fe705959f5b1" class="bulleted-list"><li style="list-style-type:disc"><strong>Posture</strong>, <strong>macro/micro-movements</strong>, <strong>tremor spectra</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8034-9b9f-ecd18539208c" class="bulleted-list"><li style="list-style-type:disc"><strong>Gait stability</strong>, <strong>freezing events</strong> (trend-level)</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8070-af3a-e692e66d6a8b" class="bulleted-list"><li style="list-style-type:disc"><strong>Startle micro-movements</strong>, <strong>restlessness</strong></li></ul></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-807e-9941-d8f60b012089" class=""><strong>Inferences:</strong> discomfort/agitation, pain-avoidance behavior, sedation/agitation balance, fall-risk cues.</p></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-805e-9848-da7e6033c69a"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-8000-aa14-e1a691b560e9" class="">8) Neuro-cardiac Synchrony (when available)</h2></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-80ed-b39b-e2a623657ad1" class=""><strong>With EEG/ECG or advanced wearables:</strong></p></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80d7-bb6c-d3263d38501f" class="bulleted-list"><li style="list-style-type:disc"><strong>Cardio–vagal coupling</strong>, <strong>brain–heart coherence indices</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80ef-a916-db09931e1308" class="bulleted-list"><li style="list-style-type:disc"><strong>Event-related autonomic responses</strong> to stimuli</li></ul></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-80ab-b17e-f40381890792" class=""><strong>Inferences:</strong> covert responsiveness, sensory processing, depth of consciousness trends (supportive, not diagnostic).</p></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-8008-87fe-c1e1531814de"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-8015-a70e-db0109029daf" class="">9) Metabolic &amp; Endocrine Proxies</h2></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-809b-9ed7-c138af65a43e" class=""><strong>From smartwatch &amp; optional sensors:</strong></p></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-802c-afc7-e6ed2bb0ad34" class="bulleted-list"><li style="list-style-type:disc"><strong>Energy expenditure proxies</strong>, <strong>activity thermogenesis</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80c6-8538-fcf8ebb4a58d" class="bulleted-list"><li style="list-style-type:disc"><strong>CGM (continuous glucose monitor)</strong> (optional) → glycemic variability</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8097-91df-e1d59558e5bd" class="bulleted-list"><li style="list-style-type:disc"><strong>Hydration proxies</strong> (EDA/temp/HRV composite)</li></ul></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-807f-8540-e84341fd9ef2" class=""><strong>Inferences:</strong> metabolic stress/fatigue, glycemic instability (with CGM), dehydration risk signals.</p></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-8049-9acb-eb0499650bec"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-8040-8af6-e2be9388ecda" class="">10) Environmental &amp; Contextual Signals</h2></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-8026-88a3-d38c08708f30" class=""><strong>From phone/watch &amp; room sensors:</strong></p></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8064-9008-fc5b2cd4da5d" class="bulleted-list"><li style="list-style-type:disc"><strong>Ambient light/noise/temperature/humidity</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-808a-92ab-ec3a35f96da6" class="bulleted-list"><li style="list-style-type:disc"><strong>Stimulus timing</strong> (nursing interventions, repositioning)</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-800f-9b06-f72a3ad8d2ad" class="bulleted-list"><li style="list-style-type:disc"><strong>Geospatial context</strong> (ICU vs. home; motion artifact likelihood)</li></ul></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-8005-96e9-e713fdb6568c" class=""><strong>Inferences:</strong> environment–physiology coupling (e.g., noise → arousal spikes), micro-intervention opportunities (dim lights, reduce noise).</p></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-80a2-a29a-eb5e955250f3"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-80b7-8a40-f11962795ae5" class="">11) Composite Indices (NeuroSyncAI™ outputs)</h2></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8043-8df3-de4b3483138f" class="bulleted-list"><li style="list-style-type:disc"><strong>Sympathetic Activation Index</strong> (stress/pain likelihood)</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80dd-b0f0-c6cfa9ccdec1" class="bulleted-list"><li style="list-style-type:disc"><strong>Parasympathetic Recovery Index</strong> (soothing/restorative trend)</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80a8-b1b0-c09f681d9001" class="bulleted-list"><li style="list-style-type:disc"><strong>Discomfort/Distress Probability</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-803b-95ea-d9fc6e0c0a3f" class="bulleted-list"><li style="list-style-type:disc"><strong>Responsiveness Likelihood Score</strong> (covert response trends)</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80dd-b3b8-e72b9d45eeb3" class="bulleted-list"><li style="list-style-type:disc"><strong>Sleep Restoration Score</strong>, <strong>Fatigue/Overload Score</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80c0-b276-ddf0d850dc96" class="bulleted-list"><li style="list-style-type:disc"><strong>Stability/Volatility Index</strong> (state drift risk)</li></ul></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-806d-b37c-e0e396cb741f" class="">All indices are <strong>explainable</strong>: which raw signals contributed, how they were weighted, and why a state was inferred.</p></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-80fc-ad4d-c895c5540659"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-80c4-8574-c579854b9f16" class="">Important Boundaries (What it does <em>not</em> do)</h2></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8010-9463-e4b67a1d2a88" class="bulleted-list"><li style="list-style-type:disc"><strong>No mind-reading or “future telling.”</strong> It detects <strong>pre-verbal micro-signals</strong> and <strong>near-term trajectories</strong>, not thoughts.</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80d8-a2ab-fa566c17e979" class="bulleted-list"><li style="list-style-type:disc"><strong>Not a standalone diagnosis.</strong> Outputs are <strong>clinical decision support</strong> and require human oversight.</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80d8-8bf3-d08c0d750194" class="bulleted-list"><li style="list-style-type:disc"><strong>Sensor quality matters.</strong> Motion artifacts, poor fit, or low perfusion can degrade signal; the system flags low confidence.</li></ul></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-8048-acc1-cb4c7a3e7fc0"/></div><div style="display:contents" dir="auto"><h3 id="291c5e6f-95bd-80b2-af2b-d5bdd3390115" class="">Bottom line</h3></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-804e-9969-f6e67e454a16" class=""><strong>Yes — emotional signals are included</strong>, but they are <strong>inferred from measurable physiology</strong> (HRV, EDA, respiration, temp, movement) and, where available, <strong>neuro-cardiac coupling</strong>. NeuroSyncAI™ provides a <strong>full-stack map of the body’s state</strong>: autonomic, metabolic, behavioral, circadian, and context — translated into <strong>actionable, explainable insights</strong> for care teams.</p></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-8040-95f0-e7bcfa980be5" class="">
</p></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-8069-a1a8-f5f7c9896cc2" class="">The <strong>Institute of Unified Biological Intelligence™</strong> and <strong>Quantum Logic Systems™ (QLS)</strong> together form the foundational scientific body redefining intelligence as a <em>biologically measurable and logically verifiable</em> function.</p></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-80b0-84e7-e1ca34f0e621" class="">We develop <strong>first-principle frameworks</strong> that unify biology and logic — establishing measurable standards for nervous system stability, cognitive precision, emotional regulation, and total structural alignment.</p></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-80c9-89c5-de335dab340b" class="">Our research replaces legacy IQ models, abstract psychology, and emotional generalisations with a single unified benchmark: <strong>Absolute Biological Integrity™</strong>. Through Quantum Logic Systems™, we integrate biological intelligence with the quantum architecture of logic — enabling deterministic interaction between human cognition and advanced artificial systems.</p></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-8022-b320-e1f0b1bad5cf" class="">Our mission is to build the intellectual, somatic, and technological foundation for <strong>post-chaos civilisation</strong> — where intelligence is no longer theoretical but <em>biologically enforced and logically exact</em>.</p></div><div style="display:contents" dir="auto"><h2 id="29dc5e6f-95bd-8067-a695-f291f53f680e" class=""><strong>Core Frameworks Include:</strong></h2></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-8085-98d7-d01859793961" class="bulleted-list"><li style="list-style-type:disc"><strong>Unified Biological Intelligence™ (UBI)</strong> — a measurable system of human and artificial cognition based on structural integrity and nervous system stability.</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-8050-9b45-dd7dcf937c08" class="bulleted-list"><li style="list-style-type:disc"><strong>Quantum Logic Systems™ (QLS)</strong> — the governing logic architecture linking biological intelligence with universal computation; establishes the laws through which information becomes measurable, transferable, and self-consistent.</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-806c-b9a2-f9d07327b780" class="bulleted-list"><li style="list-style-type:disc"><strong>NeuroSyncAI™</strong> — the first AI architecture trained through live nervous system enforcement, eliminating emotional drift and logic instability.</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-80c9-847d-d0765589eefa" class="bulleted-list"><li style="list-style-type:disc"><strong>Bioelectromagnetic Intelligence™</strong> — a biologically grounded model of emotion, cognition, and regulation derived from muscle signal, hormone response, and electromagnetic balance.</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-80d9-99fc-d02773024de1" class="bulleted-list"><li style="list-style-type:disc"><strong>Ethical Intelligence Infrastructure</strong> — biologically enforced design systems for emotional accuracy, relational integrity, and moral stability across human–machine ecosystems.</li></ul></div><div style="display:contents" dir="auto"><h2 id="29dc5e6f-95bd-80fb-af7a-c364fb7316b8" class=""><strong>Scientific Foundation: </strong></h2></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-8023-b7bf-c7f78432d038" class="">Drawing from <strong>neuroscience, quantum physics, somatic diagnostics, behavioural systems, and systems engineering</strong>, our frameworks derive from <em>biological function and logical law</em>, not theory — creating reproducible architectures for restoring individual, institutional, and systemic intelligence.</p></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-8004-b2f3-d378a083e8d9" class="">
</p></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-80cb-948b-e93e01a4ed4b" class="">Excellent — that’s exactly the right shift for executive tone. Below is the <strong>final refined version</strong> of your CTO profile written in <strong>third-person</strong>, with a focus on <strong>responsibility, impact, and strategic vision</strong> — the way it would appear in a corporate report, investor deck, or board profile.</p></div><div style="display:contents" dir="auto"><hr id="29dc5e6f-95bd-8081-b953-c129ba90c3d6"/></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-8081-a410-fae1a144f025" class="">Leads the architecture, integration, and operation of Vietnam’s first unified electric mobility and energy ecosystem, connecting electric transport, logistics, charging infrastructure, and green finance into one intelligent platform. Encompasses not only technology development but also organisational design, process governance, and strategic advisory, ensuring that UniPower’s technological infrastructure evolves in alignment with both national energy policy and global innovation standards.</p></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-80e3-a9bb-e42617a4c99b" class="">Core Responsibilities:</p></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-80ef-8791-d2909270d45a" class="bulleted-list"><li style="list-style-type:disc">Oversee the design and deployment of UniOS, UniPower’s central operating system — synchronising data from vehicles, drivers, and charging stations across the country.</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-80e5-b690-dcc69b588734" class="bulleted-list"><li style="list-style-type:disc">Build and enforce standardised operational processes integrating data, AI, and automation across all business units to enhance transparency and efficiency.</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-8041-87b7-f55ef0cb4358" class="bulleted-list"><li style="list-style-type:disc">Lead research and market intelligence on AI, IoT, e-mobility, and clean energy technologies — identifying opportunities for adoption, localisation, and strategic partnerships.</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-8034-8439-e9eb981918ed" class="bulleted-list"><li style="list-style-type:disc">Provide technology strategy and policy advisory to the CEO and Board of Directors, aligning long-term infrastructure plans with Vietnam’s digital and energy transition goals.</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-801e-b29b-c3c1018e8783" class="bulleted-list"><li style="list-style-type:disc">Establish data and cybersecurity governance frameworks in compliance with national regulations, including Decree 13/2023/NĐ-CP.</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-80ab-a885-d811e66c3dfa" class="bulleted-list"><li style="list-style-type:disc">Supervise cross-functional engineering, data, and product teams, ensuring system scalability, interoperability, and business continuity.</li></ul></div><div style="display:contents" dir="auto"><ul id="29dc5e6f-95bd-8049-bbf6-f676450d8e96" class="bulleted-list"><li style="list-style-type:disc">Develop and oversee internal training frameworks on automation, data-driven management, and AI integration for technical and leadership teams.</li></ul></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-809d-b25b-e00ca695d56a" class="">Strategic Vision: To establish UniPower as the national backbone for intelligent, ethical, and sustainable energy automation — where technology not only optimizes performance but advances human capability and environmental balance.</p></div><div style="display:contents" dir="auto"><p id="29dc5e6f-95bd-800f-bf61-ef29d7b35576" class="">Guiding Principle: “Data-driven Energy, Human-centered Technology” — positioning UniPower as a catalyst for Vietnam’s leadership in AI-integrated mobility, clean energy infrastructure, and intelligent governance.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
