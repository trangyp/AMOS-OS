---
tags: [signal]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Master Signal Spec — Genesis v1.0 (Proof‑of‑Signal Network)</title><style>
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
	
</style></head><body><article id="24ac5e6f-95bd-806b-a364-dcbfb2f527c6" class="page sans"><header><h1 class="page-title" dir="auto">Master Signal Spec — Genesis v1.0 (Proof‑of‑Signal Network)</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8088-85ff-dfd8144d8139" class="">0. Purpose</h2></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8063-ad4c-d7eb3f63d0c7" class="">Define the canonical parasympathetic activation signal and its delivery/verification stack for a decentralized biological stability network. This spec is <strong>implementation‑ready</strong>, <strong>auditable</strong>, and <strong>governance‑agnostic</strong>.</p></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-8065-b926-d6561a58f202"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8058-9890-f1b02b88e505" class="">1. Biological Objective &amp; KPIs</h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80dd-a671-f9be86aee874" class="bulleted-list"><li style="list-style-type:disc"><strong>Primary objective:</strong> Increase parasympathetic activity and prosocial neural patterns through non‑invasive multi‑sensory stimulation.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8057-a132-d6b891740015" class="bulleted-list"><li style="list-style-type:disc"><strong>Population scope:</strong> Unbounded; node‑local calibration enables global deployment.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80ab-8c90-e3492ee7e2b4" class="bulleted-list"><li style="list-style-type:disc"><strong>Key performance indicators (30‑day moving window):</strong><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8067-91e6-ea7dec8b368a" class="bulleted-list"><li style="list-style-type:circle">HRV baseline shift: <strong>+15 ms</strong> (RMSSD or SDRR) from personal baseline.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-801b-ba3c-eb8f139e5456" class="bulleted-list"><li style="list-style-type:circle">Vagal tone (RSA): <strong>↑ statistically significant</strong> vs. baseline (p ≤ 0.05, node‑local test).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-803b-9f6c-ccacbe7f921e" class="bulleted-list"><li style="list-style-type:circle">Affect variability: <strong>≥20% reduction</strong> in day‑to‑day variability index.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-806d-af02-f2f3ce41f6ef"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-806d-971a-ebc3a8be92cb" class="">2. Signal Architecture</h2></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-807d-af0d-dba9f05bee21" class="">2.1 Core Waveform (Audio/Bioacoustic)</h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8040-af36-c54ce1f99ec3" class="bulleted-list"><li style="list-style-type:disc"><strong>Base frequency envelope:</strong> 0.08–0.14 Hz (respiratory sinus arrhythmia band), center default <strong>0.10 Hz</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80aa-911a-c12eee766b47" class="bulleted-list"><li style="list-style-type:disc"><strong>Harmonic support:</strong> 4–7 Hz (theta) tapered at −18 dB relative to base.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80d2-9c1d-fb2500a096ee" class="bulleted-list"><li style="list-style-type:disc"><strong>Waveform shape:</strong> Band‑limited sine with THD &lt; 2%.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80d9-b7ae-ebdcce1a7e62" class="bulleted-list"><li style="list-style-type:disc"><strong>Sample rate:</strong> 48 kHz (min), 24‑bit PCM.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80bf-8533-d981acb62452" class="bulleted-list"><li style="list-style-type:disc"><strong>SPL at ear:</strong> 60–70 dB A‑weighted (end‑user adjustable 55–72 dB with limiter).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80bc-8a5b-c26352c7f17c" class="bulleted-list"><li style="list-style-type:disc"><strong>Amplitude modulation:</strong> 0.10 Hz depth 30% (±5% adaptive), eased cosine ramp.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-803c-af01-dc11f6b002af" class="bulleted-list"><li style="list-style-type:disc"><strong>Session duration:</strong> 5–12 min (node‑selectable); refractory period ≥ 15 min.</li></ul></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-808c-9410-e9b48464252b" class="">2.2 Haptic Layer (Optional)</h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80a5-93d7-c218d04785e7" class="bulleted-list"><li style="list-style-type:disc"><strong>Carrier:</strong> 100–200 Hz vibrotactile; amplitude‑modulated at <strong>0.10 Hz</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8047-b735-ff8d54336b9e" class="bulleted-list"><li style="list-style-type:disc"><strong>Duty cycle:</strong> 40–60% with soft attack/decay ≥ 200 ms.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80b7-ad64-c1c23c7c1f4d" class="bulleted-list"><li style="list-style-type:disc"><strong>Skin safety:</strong> Peak acceleration ≤ 2 g RMS.</li></ul></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-8048-8eb5-d33316296210" class="">2.3 Visual Layer (Optional)</h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80fa-ab58-fc0a23950e65" class="bulleted-list"><li style="list-style-type:disc"><strong>Modulation:</strong> Luminance or chroma modulation ≤ 2 Hz (no stroboscopic risk).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8021-878a-f0926e05fcef" class="bulleted-list"><li style="list-style-type:disc"><strong>Peak luminance:</strong> Device default; avoid exceeding local comfort thresholds.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-803a-8b6a-c214bcea26c3" class="bulleted-list"><li style="list-style-type:disc"><strong>Accessibility:</strong> Photosensitive epilepsy guard (see §5).</li></ul></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-80c0-b222-d2846c5163be" class="">2.4 Bioelectromagnetic Layer (If used)</h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80e7-ac77-cac5656cc560" class="bulleted-list"><li style="list-style-type:disc"><strong>Intent:</strong> Ambient field coherence cues; <strong>not required</strong> for baseline deployment.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80b9-ac3a-e48c8ac5c788" class="bulleted-list"><li style="list-style-type:disc"><strong>Exposure bounds:</strong> Keep below conservative public EMF guidelines; exact values device‑specific.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-8036-b045-e44fde317300"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8075-8061-eec2127b5e7b" class="">3. Safety &amp; Accessibility Constraints</h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8071-a303-c6bffc134cbc" class="bulleted-list"><li style="list-style-type:disc"><strong>Audio:</strong> Peak limiter; slow attack/release; avoid sudden transients.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8013-9548-d1fd811f94d8" class="bulleted-list"><li style="list-style-type:disc"><strong>Visual:</strong> Flicker index &lt; 0.1; exclude 3–55 Hz flashing.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-802e-ac39-d714995d295b" class="bulleted-list"><li style="list-style-type:disc"><strong>Haptic:</strong> Thermal monitoring for continuous actuators.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8035-b90b-d9bfb70bcbaa" class="bulleted-list"><li style="list-style-type:disc"><strong>Session scheduling:</strong> Enforce refractory period; daily cap default <strong>6 sessions</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8085-a352-d14ff63cf8f5" class="bulleted-list"><li style="list-style-type:disc"><strong>User controls:</strong> Immediate stop, volume/brightness limits, opt‑out from data sharing.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80ef-867e-fe00334a9bb0"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8011-b79e-d060fbb3d535" class="">4. Encoding, Packaging, and Integrity</h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-801a-b227-fb2a71f99034" class="bulleted-list"><li style="list-style-type:disc"><strong>Audio master:</strong> WAV/FLAC, 48 kHz/24‑bit.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80ba-8e7a-e297ea082299" class="bulleted-list"><li style="list-style-type:disc"><strong>Haptic pattern:</strong> Binary envelope table @ 200 Hz control rate.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80d0-aa67-ce8791ed6d72" class="bulleted-list"><li style="list-style-type:disc"><strong>Manifest (YAML):</strong><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8019-8574-c982d744d69a" class="bulleted-list"><li style="list-style-type:circle"><code>spec_version</code>, <code>signal_id</code>, <code>sha256_master</code>, <code>created_utc</code>, <code>author_fingerprint</code> (Ed25519 pubkey), <code>safety_profile</code>, <code>calibration_profile</code>.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8052-bd09-c4e7b17e1b27" class="bulleted-list"><li style="list-style-type:disc"><strong>Integrity:</strong><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8080-b186-f2f8880b5a12" class="bulleted-list"><li style="list-style-type:circle"><strong>SHA‑256</strong> of each asset.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-800a-b2fe-cfc552d09d20" class="bulleted-list"><li style="list-style-type:circle"><strong>Ed25519 signature</strong> over manifest.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-804f-a607-c2a4bc4d039c" class="bulleted-list"><li style="list-style-type:circle">Node verifies manifest → assets → local render hash before delivery.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-8015-8802-c662307c8e53"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-80f0-bd06-d544fb35e2b7" class="">5. Risk Mitigation &amp; Consent</h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8034-b89a-e108fa6b0681" class="bulleted-list"><li style="list-style-type:disc"><strong>Screening prompts:</strong> Cardiovascular conditions, epilepsy/photosensitivity, pregnancy, implanted devices (informational), acute psychiatric distress.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8007-a0a1-ed2a72a70acf" class="bulleted-list"><li style="list-style-type:disc"><strong>Fail‑safe:</strong> One‑tap stop; persistent setting to disable certain modalities.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8059-9461-d6c72a6259fb" class="bulleted-list"><li style="list-style-type:disc"><strong>Informed consent:</strong> Plain‑language opt‑in; modality‑specific toggles.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-806c-9810-d0610b10136a"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-809d-bc16-e5efaa66ce4f" class="">6. Calibration Protocol (Node‑Local)</h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-804d-bfa9-e5ccb33b556b" class="bulleted-list"><li style="list-style-type:disc"><strong>Baseline capture:</strong> 3‑day rolling HRV baseline (≥ 15 min/day passive or structured).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-804a-8f5b-fb08d1a73335" class="bulleted-list"><li style="list-style-type:disc"><strong>Session calibration:</strong><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-80df-a71c-d04ad10ba3ff" class="numbered-list" start="1"><li>Pre‑window 90 s baseline.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-8052-9d9b-f77db9914266" class="numbered-list" start="2"><li>Delivery window (5–12 min).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-80fe-b1ae-f1f6ea92bc5c" class="numbered-list" start="3"><li>Post‑window 180 s capture.</li></ol></div></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8059-a581-d5f3c90523a9" class="bulleted-list"><li style="list-style-type:disc"><strong>Adaptive parameters:</strong><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80b2-935d-fbe8a8de9e6b" class="bulleted-list"><li style="list-style-type:circle">Base frequency drift ±0.01 Hz to match respiratory pace.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8025-9c7d-d790ef0fbb43" class="bulleted-list"><li style="list-style-type:circle">AM depth ±5% within comfort.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80b5-abd3-c211decb0f09" class="bulleted-list"><li style="list-style-type:disc"><strong>Quality gates:</strong><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80a0-8ac8-c424283c8b56" class="bulleted-list"><li style="list-style-type:circle">Motion artifact filter (accelerometer‑assisted).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-805c-a53b-fc9d20d5e323" class="bulleted-list"><li style="list-style-type:circle">Minimum valid R‑R count: 250 beats/session.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80a8-a3cc-e1d96f5540f4"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-80cf-a3f1-ebeb16d3a88a" class="">7. Proof‑of‑Signal (PoSg) Metadata</h2></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8081-98fa-dfe96f0e0ca5" class="">Each session emits a <strong>Proof‑of‑Signal Block</strong> (PSB):</p></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-806d-bd00-edd7c9d2cbe2" class="bulleted-list"><li style="list-style-type:disc"><code>signal_hash</code> (SHA‑256 of master asset bundle)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80fc-bc33-d2877c4591f2" class="bulleted-list"><li style="list-style-type:disc"><code>node_pubkey</code> (Ed25519)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-807e-a185-e13ee7dc35ff" class="bulleted-list"><li style="list-style-type:disc"><code>timestamp_start</code>, <code>timestamp_end</code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80ea-92e2-cd218cb2a30e" class="bulleted-list"><li style="list-style-type:disc"><code>kpi_delta</code>: { <code>hrv_rmssd_delta_ms</code>, <code>rsa_delta</code>, <code>affect_var_delta</code> }</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8074-b7ac-e2add8e0b863" class="bulleted-list"><li style="list-style-type:disc"><code>quality</code>: { <code>artifact_rate</code>, <code>r2_fit</code>, <code>temp_flag</code> }</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80fd-a0c8-ca79fea140ab" class="bulleted-list"><li style="list-style-type:disc"><code>geo_hint</code> (optional, coarse)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80f0-9754-f0a5e79ffbf0" class="bulleted-list"><li style="list-style-type:disc"><code>consent_token</code> (blind signature proving consent)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80b5-969d-f464b25a3136" class="bulleted-list"><li style="list-style-type:disc"><code>psb_hash</code> and <code>node_signature</code></li></ul></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8095-8498-e7c9d0806ce5" class=""><strong>Validation rules (validator nodes):</strong></p></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-809d-a386-e26418e530a8" class="bulleted-list"><li style="list-style-type:disc">Hash == current authorized master; timestamps in window; KPI deltas within plausible bounds (node‑local model). Blocks failing checks are rejected.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-809d-8369-c32c299ad216"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8042-8aeb-cf80f8d87780" class="">8. Difficulty Adjustment &amp; Rewards (Protocol Outline)</h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80d3-998f-c93550dd90fd" class="bulleted-list"><li style="list-style-type:disc"><strong>Epoch:</strong> 30 days.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80be-a6ea-d12342c6c08b" class="bulleted-list"><li style="list-style-type:disc"><strong>Target acceptance rate:</strong> X PSBs/day (configurable by governance).</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8057-9a14-ee3e33981f52" class="bulleted-list"><li style="list-style-type:disc"><strong>Adjustment:</strong> Statistical threshold for minimum effect size auto‑adjusted to hit target acceptance rate, analogous to mining difficulty.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80b8-8a3d-dc455cfc9d90" class="bulleted-list"><li style="list-style-type:disc"><strong>Rewards:</strong> Micropayments to <code>node_pubkey</code> for accepted PSBs.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80be-b7bd-da18a2414474"/></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-80d2-8a8f-c65476863a7e" class="">8.1 Reward Function (Normative)</h3></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-80c5-a3b7-de176d38159e" class=""><strong>Preconditions (quality gates):</strong> reward=0 if any true — <code>artifact_rate ≥ τ_art</code> (default 0.20), <code>min_valid_rr_count &lt; 250</code>, invalid time window, <code>signal_hash</code> mismatch/spec mismatch, or attestation fail.</p></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8099-b43b-f522f119e076" class=""><strong>Base payout</strong>: <code>B_base = B_epoch</code> (epoch budgeted base sats). Halving every <code>HALVING_EPOCHS</code>.</p></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-80e6-b3fb-f4928ae3a9f3" class=""><strong>Effect score</strong> (baseline‑normalized):</p></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8083-b6af-d664b032ab84" class="bulleted-list"><li style="list-style-type:disc"><code>z_rmssd = (RMSSD_post − RMSSD_pre) / σ_rmssd_personal</code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8006-b0b2-f04ba544dc4d" class="bulleted-list"><li style="list-style-type:disc"><code>z_rsa = (RSA_post − RSA_pre) / σ_rsa_personal</code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80c6-a6dc-dd459dcf3fd8" class="bulleted-list"><li style="list-style-type:disc"><code>S_eff = clamp( α*z_rmssd + (1−α)*z_rsa , 0 , 2.0 )</code> (default <code>α=0.5</code>). If <code>S_eff &lt; θ_eff</code> → reward=0.</li></ul></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8070-b706-c0ddf0391cb2" class=""><strong>Quality score:</strong></p></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-805c-ac77-fd89273173d6" class="bulleted-list"><li style="list-style-type:disc"><code>Q_art = (1 − artifact_rate) ^ β_art</code> (default <code>β_art=1.5</code>)</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-801e-81e8-de4fc8eb0750" class="bulleted-list"><li style="list-style-type:disc"><code>Q_rr = 1 + min((min_valid_rr_count−250)/500, 0.10)</code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80c5-b171-feafbcd6f37e" class="bulleted-list"><li style="list-style-type:disc">`Q_mot</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8038-92d9-d9828395b6c5" class="bulleted-list"><li style="list-style-type:disc"><strong>HR/HRV:</strong> PPG or ECG with validated R‑R extraction.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-804b-8a5c-e47a3ad7b0bb" class="bulleted-list"><li style="list-style-type:disc"><strong>Sampling:</strong> ECG ≥ 250 Hz; PPG ≥ 64 Hz.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80f1-8ede-dc0a33a159ff" class="bulleted-list"><li style="list-style-type:disc"><strong>IMU:</strong> 3‑axis accelerometer for artifact suppression.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8099-83e5-c46afdc0c4f6" class="bulleted-list"><li style="list-style-type:disc"><strong>Clock:</strong> NTP or GNSS‑synced; drift &lt; 100 ms per session.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-805f-8748-fe5215f9d0be" class="bulleted-list"><li style="list-style-type:disc"><strong>TEE/SE:</strong> Trusted execution or secure element for key storage and attestation.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-808f-8cde-fc0135d03d7d"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-80a2-9411-de81cc615453" class="">10. Networking &amp; Privacy</h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8014-9b2e-ca401e11b766" class="bulleted-list"><li style="list-style-type:disc"><strong>PSB transport:</strong> gRPC/QUIC with TLS 1.3.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8054-ba75-d41dfc8e4ffd" class="bulleted-list"><li style="list-style-type:disc"><strong>Privacy:</strong> Differential privacy on aggregates; raw waveforms and raw R‑R intervals remain on device unless explicit user export.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80b9-b0b6-ff565eec8e8e" class="bulleted-list"><li style="list-style-type:disc"><strong>Provenance:</strong> PSB and master manifest hashes timestamped on Bitcoin (OP_RETURN/Taproot commit).</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-80fa-ac83-fd81a5545e76"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8002-b55e-e7b4870afe50" class="">11. APIs (Excerpt)</h2></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-800e-8e78-c5e8b8626778" class="">11.1 Local Render API</h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8077-93e9-e8942fbe025c" class="bulleted-list"><li style="list-style-type:disc"><code>GET /signal/current</code> → manifest + hashes.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8097-a87d-c046067f9df7" class="bulleted-list"><li style="list-style-type:disc"><code>POST /signal/render</code> {device_profile} → returns device‑specific render pack.</li></ul></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-8084-85a1-dd9e3fde99f1" class="">11.2 Session Control API</h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-803d-b386-c31d8a8723d8" class="bulleted-list"><li style="list-style-type:disc"><code>POST /session/start</code> {modalities, target_duration}</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80c3-9736-e45520e4d3ff" class="bulleted-list"><li style="list-style-type:disc"><code>POST /session/stop</code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-809d-ae60-f64ba96d82ce" class="bulleted-list"><li style="list-style-type:disc"><code>GET /session/result/:id</code> → KPIs + PSB</li></ul></div><div style="display:contents" dir="auto"><h3 id="24ac5e6f-95bd-8027-bd66-c215d9798912" class="">11.3 PSB Submit API</h3></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-807c-9995-cc174f4ce7d3" class="bulleted-list"><li style="list-style-type:disc"><code>POST /psb/submit</code> {psb} → {status, reward_txid}</li></ul></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-8083-b8e9-f1e470e7285b" class="">Schemas are JSON; all responses signed by node key.</p></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-804a-aef9-c8f2a39c0e68"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8077-a663-e6d7f04657f6" class="">12. Governance &amp; Versioning</h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80f0-8d6c-d5e15e9843c5" class="bulleted-list"><li style="list-style-type:disc"><strong>spec_version:</strong> <code>1.0.0‑genesis</code></li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8015-9843-e5e5d6d54a4a" class="bulleted-list"><li style="list-style-type:disc"><strong>Change control:</strong> Multi‑sig proposal → on‑chain hash → community client auto‑update.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8084-9ff4-e479003fa57a" class="bulleted-list"><li style="list-style-type:disc"><strong>Backward compatibility:</strong> Clients must support ≥ 2 prior spec versions.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-8030-b2ea-ee7071dde4f9"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-807f-8261-ebb53499520f" class="">13. Test Suite (Conformance)</h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80d8-b38c-c3fa448be27f" class="bulleted-list"><li style="list-style-type:disc"><strong>Audio conformance:</strong> THD, sample‑accurate hash, SPL sweep.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8023-82d9-dc8d3bcf2c0f" class="bulleted-list"><li style="list-style-type:disc"><strong>Sensor conformance:</strong> R‑R accuracy vs. reference, artifact rejection under motion.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-804e-9281-c4a793ee90ee" class="bulleted-list"><li style="list-style-type:disc"><strong>PSB conformance:</strong> Schema validity, signature correctness, replay‑attack resistance.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-805d-a157-cf5b28507057"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-803e-ac0d-e53ff15d4850" class="">14. Deployment Profiles</h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8031-9d06-c6436c789a33" class="bulleted-list"><li style="list-style-type:disc"><strong>Mobile (baseline):</strong> Audio‑only or audio+haptic; PPG from camera or wearable bridge.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80a2-be11-cd926ff56935" class="bulleted-list"><li style="list-style-type:disc"><strong>Wearable:</strong> Haptic+audio; native PPG/ECG.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-808e-9654-c75ed1eba247" class="bulleted-list"><li style="list-style-type:disc"><strong>Public node:</strong> Environmental audio/light; aggregate PSBs only with opt‑in personal devices nearby.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-806f-ab48-f1a5091d3c73"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-80ed-b6c1-cefc7fd90e32" class="">15. Legal &amp; Compliance Notes</h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-80a1-8ba9-ee27c636888c" class="bulleted-list"><li style="list-style-type:disc"><strong>Classification:</strong> Wellness/relaxation technology; not a diagnostic or therapeutic device.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-805b-9883-cf8dab059271" class="bulleted-list"><li style="list-style-type:disc"><strong>Data:</strong> User‑controlled; exportable; subject to regional privacy laws.</li></ul></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-801a-9715-d35492fbe8f1"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-801d-aac5-f7f4635fd38e" class="">16. Genesis Procedure</h2></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-807c-a3c4-d33b4fa73c4c" class="numbered-list" start="1"><li>Freeze this spec → compute <code>spec_sha256</code>.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-804c-a20f-ed45a9faaa8d" class="numbered-list" start="2"><li>Freeze master asset bundle → compute <code>sha256_master</code>.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-80c2-8629-c523dc7c37b3" class="numbered-list" start="3"><li>Publish both hashes on Bitcoin (timestamp txid recorded in manifest).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="24ac5e6f-95bd-80d2-a768-ec2dfe0eab46" class="numbered-list" start="4"><li>Release open‑source clients + validator.</li></ol></div><div style="display:contents" dir="auto"><hr id="24ac5e6f-95bd-8001-b67f-f04e88189087"/></div><div style="display:contents" dir="auto"><h2 id="24ac5e6f-95bd-8088-99cc-de29691c5c2a" class="">17. Roadmap to v1.1</h2></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-8099-8aba-e8d19c9a5022" class="bulleted-list"><li style="list-style-type:disc">Personalized respiratory pacing model.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-802e-a699-f908094b752b" class="bulleted-list"><li style="list-style-type:disc">Multi‑recipient group coherence mode.</li></ul></div><div style="display:contents" dir="auto"><ul id="24ac5e6f-95bd-801f-ae12-f4772bbccd3d" class="bulleted-list"><li style="list-style-type:disc">Expanded validator heuristics (robustness to spoofing).</li></ul></div><div style="display:contents" dir="auto"><p id="24ac5e6f-95bd-80c0-97c3-cb47512f62b9" class=""><strong>End of Spec</strong></p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
