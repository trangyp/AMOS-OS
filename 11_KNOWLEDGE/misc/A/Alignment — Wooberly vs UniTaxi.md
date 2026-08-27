---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Alignment — Wooberly vs UniTaxi</title><style>
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
	
</style></head><body><article id="294c5e6f-95bd-8044-aef6-d74049565e57" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Alignment — Wooberly vs UniTaxi</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="ltr"><table id="294c5e6f-95bd-8012-ab00-ffc5db66fe40" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80c5-abcf-c5b8b382a8bf"><th id="}_fR" class="simple-table-header-color simple-table-header"><strong>Area</strong></th><th id="=BRy" class="simple-table-header-color simple-table-header" style="width:180.578125px"><strong>Feature Set</strong></th><th id="DYnx" class="simple-table-header-color simple-table-header" style="width:132.3515625px"><strong>Wooberly OOTB</strong></th><th id=";pzB" class="simple-table-header-color simple-table-header"><strong>UniTaxi Needs</strong></th><th id="BqHW" class="simple-table-header-color simple-table-header"><strong>Gap / Note</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8086-9afe-d5209ccf40be"><td id="}_fR" class="">Rider App UX</td><td id="=BRy" class="" style="width:180.578125px">Signup/OTP</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" class="">☑️</td><td id="BqHW" class="">Meets</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80d0-8249-fb1fc438d1a0"><td id="}_fR" class=""></td><td id="=BRy" class="" style="width:180.578125px">Set pickup/drop, 
suggestions</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" class="">☑️</td><td id="BqHW" class="">Meets</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-807d-b94e-e54616b05e76"><td id="}_fR" class=""></td><td id="=BRy" class="" style="width:180.578125px">Multi-vehicle categories</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" class="">☑️</td><td id="BqHW" class="">Meets</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8094-8719-e044aadf73f5"><td id="}_fR" class=""></td><td id="=BRy" class="" style="width:180.578125px">Promo codes</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" class="">☑️</td><td id="BqHW" class="">Meets</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8006-af71-cb1a3f1c1064"><td id="}_fR" class=""></td><td id="=BRy" class="" style="width:180.578125px">Cancel with reason</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" class="">☑️</td><td id="BqHW" class="">Meets</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-807a-a661-d5601a5629ac"><td id="}_fR" class=""></td><td id="=BRy" class="" style="width:180.578125px">In-app chat</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" class="">☑️</td><td id="BqHW" class="">Meets</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-805d-9218-ff0ab14e60b0"><td id="}_fR" class=""></td><td id="=BRy" class="" style="width:180.578125px">Schedule ride</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" class="">☑️</td><td id="BqHW" class="">Meets</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8081-b7e2-d24512027ec2"><td id="}_fR" class=""></td><td id="=BRy" class="" style="width:180.578125px">Emergency contacts (basic)</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" c
lass="">☑️</td><td id="BqHW" class="">Meets (enhance later for SOS)</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-808c-aef1-ca09e3efa5cd"><td id="}_fR" class=""></td><td id="=BRy" class="" style="width:180.578125px">RTL / Multi-language basics</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" class="">☑️</td><td id="BqHW" class="">Meets</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-808f-bc5c-d2bd90b87197"><td id="}_fR" class="">Driver App UX</td><td id="=BRy" class="" style="width:180.578125px">Availability toggle</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" class="">☑️</td><td id="BqHW" class="">Meets</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80bb-afeb-c21104e31535"><td id="}_fR" class=""></td><td id="=BRy" class="" style="width:180.578125px">Accept/decline jobs</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" class="">☑️</td><td id="BqHW" class="">Meets</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8046-8a5c-de016e8de75d"><td id="}_fR" class=""></td><td id="=BRy" class="" style="width:180.578125px">Extra fees (e.g., toll)</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" class="">☑️</td><td id="BqHW" class="">Meets</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-800c-8a02-ece10e780f55"><td id="}_fR" class=""></td><td id="=BRy" class="" style="width:180.578125px">Earnings dashboard</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" class="">☑️</td><td id="BqHW" class="">Meets</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80ea-844c-d6e762493dd2"><td id="}_fR" class=""></td><td id="=BRy" class="" style="width:180.578125px">Trip history, ratings, 
notifications</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" class="">☑️</td><td id="BqHW" class="">Meets</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80a1-b8e4-e3cb92335699"><td id="}_fR" class=""></td><td id="=BRy" class="" style="width:180.578125px">In-app chat</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" class="">☑️</td><td id="BqHW" class="">Meets</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80f0-9929-f32ab380d731"><td id="}_fR" class="">Admin</td><td id="=BRy" class="" style="width:180.578125px">Dashboard (live map/heatmap)</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" class="">☑️</td><td id="BqHW" class="">Meets</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80eb-9757-e4eab2cc2a1c"><td id="}_fR" class=""></td><td id="=BRy" class="" style="width:180.578125px">Manage riders/drivers/vehicles</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" class="">☑️</td><td id="BqHW" class="">Meets</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80e1-82cb-c11ae0345b61"><td id="}_fR" class=""></td><td id="=BRy" class="" style="width:180.578125px">Categories/locations/geofencing</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" class="">☑️</td><td id="BqHW" class="">Meets</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8097-aee0-f324ff867227"><td id="}_fR" class=""></td><td id="=BRy" class="" style="width:180.578125px">Fare mgmt, bookings (incl. 
scheduled)</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" class="">☑️</td><td id="BqHW" class="">Meets</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80b9-b19c-e4c095252784"><td id="}_fR" class=""></td><td id="=BRy" class="" style="width:180.578125px">Cancellations &amp; reasons</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" class="">☑️</td><td id="BqHW" class="">Meets</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80e3-b021-f32b6d9cd33f"><td id="}_fR" class=""></td><td id="=BRy" class="" style="width:180.578125px">Ratings, promo codes, notifications</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" class="">☑️</td><td id="BqHW" class="">Meets</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80c1-8a2c-fb94800453e0"><td id="}_fR" class=""></td><td id="=BRy" class="" style="width:180.578125px">Multi-language &amp; chat monitoring</td><td id="DYnx" class="" style="width:132.3515625px">☑️</td><td id=";pzB" class="">☑️</td><td id="BqHW" class="">Meets</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h1 id="294c5e6f-95bd-80c7-918d-e23a99a95fec" class=""><strong>Gaps — UniTaxi (VN) Requirements to Build</strong></h1></div><div style="display:contents" dir="auto"><h2 id="294c5e6f-95bd-803e-888b-ce7ecc8a71a5" class=""><strong>A) Legal, tax &amp; 
compliance (VN)</strong></h2></div><div style="display:contents" dir="ltr"><table id="294c5e6f-95bd-807d-996b-db9437e3dd11" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-806f-a380-cde9d17458aa"><th id="I@[v" class="simple-table-header-color simple-table-header" style="width:245.9140625px"><strong>Requirement</strong></th><th id="p]if" class="simple-table-header-color simple-table-header" style="width:135.1640625px"><strong>Wooberly OOTB</strong></th><th id="=P{s" class="simple-table-header-color simple-table-header" style="width:120px"><strong>UniTaxi Needs</strong></th><th id="ckEo" class="simple-table-header-color simple-table-header"><strong>Action / Build</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-800d-8c69-dc356549e60b"><td id="I@[v" class="" style="width:245.9140625px">E-Invoice end-to-end (MISA/Viettel), B2C invoice flow, status sync (Queued/Sent/Accepted/Rejected), PDF/XML ≥5y, GDT ≤24h, edit/cancel per Decree 123/TT78, Admin Invoice Centre</td><td id="p]if" class="" style="width:135.1640625px">⬜</td><td id="=P{s" class="" style="width:120px">☑️</td><td id="ckEo" class="">Build <strong>Invoice Service + Rider invoice UI + Admin E-Invoice Centre</strong></td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8098-a9fa-caf1e6b975b3"><td id="I@[v" class="" style="width:245.9140625px">Data residency (VN), PDPD consent, PII masking, AES-256 at rest, TLS 1.3, immutable audit</td><td id="p]if" class="" style="width:135.1640625px">⬜</td><td id="=P{s" class="" style="width:120px">☑️</td><td id="ckEo" class="">Build <strong>Security &amp; 
Compliance layer</strong> (consent UX, masking, audit ledger)</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8047-9ecb-cae78821a7f1"><td id="I@[v" class="" style="width:245.9140625px">Driver onboarding per Decree 10/Circular 12 (CCCD, B2+, health cert, police clearance), OCR + face match, expiry checks, one-driver-per-CCCD, approval workflow &amp; alerts</td><td id="p]if" class="" style="width:135.1640625px">⬜</td><td id="=P{s" class="" style="width:120px">☑️</td><td id="ckEo" class="">Build <strong>KYC module</strong> (OCR/FR SDK) + <strong>Verification queue</strong> + <strong>Expiry scheduler</strong></td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h2 id="294c5e6f-95bd-80b3-93f6-eb4db607ae9f" class=""><strong>B) Payments &amp; finance</strong></h2></div><div style="display:contents" dir="ltr"><table id="294c5e6f-95bd-8005-af43-cff6c607a9e5" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-808f-ad04-fbf7bc38c079"><th id="irsR" class="simple-table-header-color simple-table-header"><strong>Requirement</strong></th><th id="PttD" class="simple-table-header-color simple-table-header"><strong>Wooberly OOTB</strong></th><th id=":eyA" class="simple-table-header-color simple-table-header"><strong>UniTaxi Needs</strong></th><th id="Zsbj" class="simple-table-header-color simple-table-header"><strong>Action / Build</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-801e-8caa-c80d66d8c391"><td id="irsR" class="">Local payments: <strong>VNPay/MoMo/ZaloPay</strong> + reconciliation + cash fallback</td><td id="PttD" class="">⬜</td><td id=":eyA" class="">☑️</td><td id="Zsbj" class="">Build <strong>Payment gateway adapters</strong> + settlement reports</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-802a-b637-d1b83850e816"><td id="irsR" class="">Referral &amp; 
Rewards <strong>3% lifetime</strong> (immutable link, “retained profit” calc, <strong>Referral Wallet</strong>, <strong>PIT 5%</strong> withholding, anti-fraud, exports)</td><td id="PttD" class="">⬜</td><td id=":eyA" class="">☑️</td><td id="Zsbj" class="">Build <strong>Referral Engine + Ledger</strong> + anti-fraud + FIN exports</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8095-9c88-db983a67e564"><td id="irsR" class="">Wallets &amp; payouts (drivers + referrals), sub-ledgers, negative balance, approvals, PIT reports, bank/e-wallet disburse</td><td id="PttD" class="">⬜</td><td id=":eyA" class="">☑️</td><td id="Zsbj" class="">Build <strong>Ledger service</strong> + <strong>Payout orchestrator</strong></td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h2 id="294c5e6f-95bd-80a4-bd2c-e4a0a64e7379" class=""><strong>D) Pricing, dispatch &amp; analytics</strong></h2></div><div style="display:contents" dir="ltr"><table id="294c5e6f-95bd-80cc-92e0-ee3258726183" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80a7-bf92-da9bbc5b198f"><th id="Rw[w" class="simple-table-header-color simple-table-header"><strong>Requirement</strong></th><th id="K|:[" class="simple-table-header-color simple-table-header" style="width:132.1640625px"><strong>Wooberly OOTB</strong></th><th id="e@Ct" class="simple-table-header-color simple-table-header"><strong>UniTaxi Needs</strong></th><th id="plac" class="simple-table-header-color simple-table-header"><strong>Action / Build</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-805f-8fb6-dbfe2098597a"><td id="Rw[w" class="">VN pricing governance: versioned fare tables per city/zone, ToD/surge, multi-PSP fees, approval &amp; 
full audit</td><td id="K|:[" class="" style="width:132.1640625px">⬜</td><td id="e@Ct" class="">☑️</td><td id="plac" class="">Build <strong>Pricing service</strong> (change logs, role approvals)</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8016-8a65-c1e0b26151a8"><td id="Rw[w" class="">SLO/SLA &amp; 
monitoring: P95/99 API targets, uptime 99.9%, ops dashboards (match time P50/P90, completion), alerting (payments, e-invoice, SOS)</td><td id="K|:[" class="" style="width:132.1640625px">⬜</td><td id="e@Ct" class="">☑️</td><td id="plac" class="">Build <strong>Observability stack + Ops dashboard + Alerts</strong></td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="294c5e6f-95bd-804a-9967-fffbb531b936"/></div><div style="display:contents" dir="auto"><h1 id="294c5e6f-95bd-8002-bfc2-dc968547b1d4" class=""><strong>🧾 Wooberly Deliverables — Free vs Paid Comparison.</strong></h1></div><div style="display:contents" dir="ltr"><table id="294c5e6f-95bd-80d6-99d7-df7ea649da97" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8081-878a-c8092d2392bb"><th id="fdG_" class="simple-table-header-color simple-table-header" style="width:142.28125px"><strong>Category</strong></th><th id="Ji^k" class="simple-table-header-color simple-table-header" style="width:250.015625px"><strong>Item / Service</strong></th><th id="MLE&gt;" class="simple-table-header-color simple-table-header" style="width:81.078125px"><strong>Included (Free)</strong></th><th id="tMwh" class="simple-table-header-color simple-table-header"><strong>Additional Cost / Notes</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80b4-a73b-ffc4b063483b"><td id="fdG_" class="" style="width:142.28125px">🎯 <strong>Product</strong></td><td id="Ji^k" class="" style="width:250.015625px">Full source code (Admin, Rider App, 
Driver App)</td><td id="MLE&gt;" class="" style="width:81.078125px">☑️</td><td id="tMwh" class="">Delivered within 8 hours post-payment</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8063-b2b8-fa109f585d37"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">1-time setup / installation on 1 server</td><td id="MLE&gt;" class="" style="width:81.078125px">☑️</td><td id="tMwh" class="">Only once; 
reinstallation later = paid</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-802e-89fa-c118e053ffe0"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">Hosting / server</td><td id="MLE&gt;" class="" style="width:81.078125px">⬜</td><td id="tMwh" class="">You must provide (AWS / DigitalOcean etc.)</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80c8-966c-c5173406c0eb"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">Base product features (same as demo)</td><td id="MLE&gt;" class="" style="width:81.078125px">☑️</td><td id="tMwh" class="">Any new feature = paid customisation</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8008-82f4-e2a7c1c27e1d"><td id="fdG_" class="" style="width:142.28125px">💻 <strong>Technology Stack</strong></td><td id="Ji^k" class="" style="width:250.015625px">Flutter mobile apps (iOS/Android)</td><td id="MLE&gt;" class="" style="width:81.078125px">☑️</td><td id="tMwh" class="">Unified codebase</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8039-a7a3-f7da47f31726"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">NodeJS, ExpressJS, ReactJS, 
GraphQL backend</td><td id="MLE&gt;" class="" style="width:81.078125px">☑️</td><td id="tMwh" class="">Standard open-source frameworks</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80a1-91fd-d049d22bede1"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">MySQL database</td><td id="MLE&gt;" class="" style="width:81.078125px">☑️</td><td id="tMwh" class="">You host / manage</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80ae-9bb8-c0e1b17efed8"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">Firebase, Socket.IO, Google Maps SDK</td><td id="MLE&gt;" class="" style="width:81.078125px">☑️</td><td id="tMwh" class="">You provide API keys + pay usage</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8040-abc6-c22aa21e290b"><td id="fdG_" class="" style="width:142.28125px">🔧 <strong>Installation Process</strong></td><td id="Ji^k" class="" style="width:250.015625px">Trello setup with installation team</td><td id="MLE&gt;" class="" style="width:81.078125px">☑️</td><td id="tMwh" class="">Closed after 30 days inactivity</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80fc-ae11-f47050740232"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">Installation documentation (Ubuntu/Mac)</td><td id="MLE&gt;" class="" style="width:81.078125px">☑️</td><td id="tMwh" class="">Provided after purchase</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8086-a87d-cada6659b370"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">Folder structure &amp; 
architecture doc</td><td id="MLE&gt;" class="" style="width:81.078125px">☑️</td><td id="tMwh" class="">Included</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-806c-bdce-d7cbbf56445f"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">API specification document</td><td id="MLE&gt;" class="" style="width:81.078125px">☑️</td><td id="tMwh" class="">Included</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-802f-8adb-dd220d8df7a6"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">Support for design uploads (icons, logos)</td><td id="MLE&gt;" class="" style="width:81.078125px">⬜</td><td id="tMwh" class="">You must provide assets; 
design work = paid</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-802a-9b12-cde749f8d68a"><td id="fdG_" class="" style="width:142.28125px">💰 <strong>Third-Party Requirements (Your cost)</strong></td><td id="Ji^k" class="" style="width:250.015625px">Twilio SMS / OTP</td><td id="MLE&gt;" class="" style="width:81.078125px">⬜</td><td id="tMwh" class="">You pay per usage</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8028-95e9-e7d58a9bc628"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">Google Maps Billing</td><td id="MLE&gt;" class="" style="width:81.078125px">⬜</td><td id="tMwh" class="">You pay per usage</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80cc-9aec-c53fc65e4cf6"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">Stripe account (default payment)</td><td id="MLE&gt;" class="" style="width:81.078125px">⬜</td><td id="tMwh" class="">You set up / share API keys</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80b7-a27a-df6ebf2f2e64"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">Custom payment gateways (VNPay, MoMo, ZaloPay)</td><td id="MLE&gt;" class="" style="width:81.078125px">⬜</td><td id="tMwh" class="">Requires paid customization</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8080-aed7-d60fcd7981af"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">Apple Developer Account</td><td id="MLE&gt;" class="" style="width:81.078125px">⬜</td><td id="tMwh" class="">US$99/year, 
must grant direct access</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8056-bc0c-e1d14a4ebfa1"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">Google Play Developer Account</td><td id="MLE&gt;" class="" style="width:81.078125px">⬜</td><td id="tMwh" class="">US$25 one-time</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8079-adcc-d3058b7ea1f5"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">SSL Certificate (Let’s Encrypt)</td><td id="MLE&gt;" class="" style="width:81.078125px">☑️</td><td id="tMwh" class="">Free (optional paid SSL = +US$50/install)</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8048-9a94-c6e629742c98"><td id="fdG_" class="" style="width:142.28125px">🌐 <strong>App Store Design &amp; 
Submission</strong></td><td id="Ji^k" class="" style="width:250.015625px">Base UI included (same as demo)</td><td id="MLE&gt;" class="" style="width:81.078125px">☑️</td><td id="tMwh" class="">Meets Android Play rules</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8004-b134-cbe48732cec9"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">iOS app submission design work</td><td id="MLE&gt;" class="" style="width:81.078125px">⬜</td><td id="tMwh" class="">+US$400 (16h) for compliant design</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8026-b4aa-c21fb8cfdd09"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">Design review of external team assets</td><td id="MLE&gt;" class="" style="width:81.078125px">⬜</td><td id="tMwh" class="">+US$100 (4h)</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80c4-8a3c-c7a034f9b7e8"><td id="fdG_" class="" style="width:142.28125px">📞 <strong>Technical Support</strong></td><td id="Ji^k" class="" style="width:250.015625px">Free support period (bug fix, text/color changes)</td><td id="MLE&gt;" class="" style="width:81.078125px">☑️</td><td id="tMwh" class="">Starts from purchase date</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-803f-a842-fc49f41bb6ec"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">Translation support (up to 3 languages, 
2 iterations)</td><td id="MLE&gt;" class="" style="width:81.078125px">☑️</td><td id="tMwh" class="">Beyond that = paid</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80fd-9506-cb2437abf60b"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">Critical bug fixing</td><td id="MLE&gt;" class="" style="width:81.078125px">☑️</td><td id="tMwh" class="">Free with time frame commitment</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80a3-92f4-da97a284e0da"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">Reinstallation or modified code issues</td><td id="MLE&gt;" class="" style="width:81.078125px">⬜</td><td id="tMwh" class="">Not covered</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80de-a77b-ccbeaf83d659"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">Custom changes / new features</td><td id="MLE&gt;" class="" style="width:81.078125px">⬜</td><td id="tMwh" class="">US$25/hour</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80b7-a49a-d0334321ac69"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">Local setup / Git issues</td><td id="MLE&gt;" class="" style="width:81.078125px">⬜</td><td id="tMwh" class="">Not supported</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80eb-9c65-f2524bff2ffc"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">Communication channel</td><td id="MLE&gt;" class="" style="width:81.078125px">☑️</td><td id="tMwh" class="">Email only (no calls/WhatsApp)</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8074-af28-c372638f1282"><td id="fdG_" class="" style="width:142.28125px">⏱ <strong>Support SLA</strong></td><td i
d="Ji^k" class="" style="width:250.015625px">Response time 24–48h on business days</td><td id="MLE&gt;" class="" style="width:81.078125px">☑️</td><td id="tMwh" class="">No weekend support</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80c4-a8da-f73ab805a939"><td id="fdG_" class="" style="width:142.28125px">📑 <strong>Legal &amp; Policy</strong></td><td id="Ji^k" class="" style="width:250.015625px">Terms &amp; 
Conditions</td><td id="MLE&gt;" class="" style="width:81.078125px">☑️</td><td id="tMwh" class="">https://www.rentallscript.com/terms-and-conditions/</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8023-a0ee-e0720dd78dd7"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">Refund policy (no refunds post-delivery)</td><td id="MLE&gt;" class="" style="width:81.078125px">☑️</td><td id="tMwh" class="">https://www.rentallscript.com/returns-refunds-policy/</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80c3-9bfb-d83efb51916b"><td id="fdG_" class="" style="width:142.28125px"></td><td id="Ji^k" class="" style="width:250.015625px">FAQ (product-specific)</td><td id="MLE&gt;" class="" style="width:81.078125px">☑️</td><td id="tMwh" class="">https://www.rentallscript.com/uber-clone/#faq</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h1 id="294c5e6f-95bd-8091-b260-ed6b7a1e61a2" class=""><strong>✅ Summary — What You Get “Free”</strong></h1></div><div style="display:contents" dir="auto"><ul id="294c5e6f-95bd-8004-87ce-f2d03f9174ba" class="bulleted-list"><li style="list-style-type:disc">Complete source code for <strong>Admin + Rider + Driver apps</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="294c5e6f-95bd-8007-ab7e-fa1c6c3a85b2" class="bulleted-list"><li style="list-style-type:disc">One-time installation on your server.</li></ul></div><div style="display:contents" dir="auto"><ul id="294c5e6f-95bd-8087-a2f6-e6fd939c7de6" class="bulleted-list"><li style="list-style-type:disc">Documentation (installation, architecture, 
API).</li></ul></div><div style="display:contents" dir="auto"><ul id="294c5e6f-95bd-8044-aeda-c3752a10c372" class="bulleted-list"><li style="list-style-type:disc">Free support for:<div style="display:contents" dir="auto"><ul id="294c5e6f-95bd-809e-9dec-e5da8c9a118b" class="bulleted-list"><li style="list-style-type:circle">Text/color/static content changes.</li></ul></div><div style="display:contents" dir="auto"><ul id="294c5e6f-95bd-809b-ac85-f05ff379ea04" class="bulleted-list"><li style="list-style-type:circle">Translation (3 languages, ≤2 rounds).</li></ul></div><div style="display:contents" dir="auto"><ul id="294c5e6f-95bd-80d0-b280-eef4f4097354" class="bulleted-list"><li style="list-style-type:circle">Critical bug fixes.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="294c5e6f-95bd-8024-aab8-efc7fb0dda75" class="bulleted-list"><li style="list-style-type:disc">SSL via <strong>Let’s Encrypt</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="294c5e6f-95bd-8018-b9bc-f6b5fb25315a" class="bulleted-list"><li style="list-style-type:disc">Trello project coordination + email support.</li></ul></div><div style="display:contents" dir="auto"><h1 id="294c5e6f-95bd-809b-823f-f756a86bd6d6" class=""><strong>💵 What’s Not Free / Paid Customisation</strong></h1></div><div style="display:contents" dir="auto"><ul id="294c5e6f-95bd-801b-a5e6-d49a6f7e9738" class="bulleted-list"><li style="list-style-type:disc">New features (e.g., <strong>VNPay/MoMo/ZaloPay</strong>, <strong>MISA/Viettel eInvoice</strong>, <strong>iSAC integration</strong>, <strong>ESG/CO₂e</strong>, <strong>Referral wallet</strong>, etc.).</li></ul></div><div style="display:contents" dir="auto"><ul id="294c5e6f-95bd-8091-9d93-f82096a1d044" class="bulleted-list"><li style="list-style-type:disc">Server, domains, 
Apple/Google developer accounts.</li></ul></div><div style="display:contents" dir="auto"><ul id="294c5e6f-95bd-8052-9d07-d8db6435cd26" class="bulleted-list"><li style="list-style-type:disc">Any <strong>redesign</strong> for iOS store acceptance (US$400 typical).</li></ul></div><div style="display:contents" dir="auto"><ul id="294c5e6f-95bd-80a9-a71b-e7b1b2d07ca6" class="bulleted-list"><li style="list-style-type:disc">Additional installs or re-installs.</li></ul></div><div style="display:contents" dir="auto"><ul id="294c5e6f-95bd-8037-95d7-dec5abc8f9c2" class="bulleted-list"><li style="list-style-type:disc">All <strong>third-party API usage</strong> (Twilio, Google Maps, Stripe, etc.).</li></ul></div><div style="display:contents" dir="auto"><ul id="294c5e6f-95bd-802e-921a-e359a49f132b" class="bulleted-list"><li style="list-style-type:disc">Extended support, local/Git issues, 
or modified code.</li></ul></div><div style="display:contents" dir="auto"><hr id="294c5e6f-95bd-80ea-b95b-dd0d1f8af1d6"/></div><div style="display:contents" dir="auto"><h1 id="294c5e6f-95bd-8060-8c3d-dd91b5da90b4" class=""><strong>🚀 Next Steps to Launch UniTaxi MVP </strong></h1></div><div style="display:contents" dir="auto"><hr id="294c5e6f-95bd-8054-83d5-ce55563799f7"/></div><div style="display:contents" dir="auto"><h2 id="294c5e6f-95bd-8075-a738-cb8791215df0" class=""><strong>PHASE 0 – PREPARATION </strong></h2></div><div style="display:contents" dir="auto"><p id="294c5e6f-95bd-8027-b5c4-da514856cad0" class=""><strong>🎯 Goal:</strong> Secure environment and admin access for the installation team.</p></div><div style="display:contents" dir="ltr"><table id="294c5e6f-95bd-807d-a205-ee5e19019f35" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80dc-accd-e20ec4eaa472"><th id="=c]k" class="simple-table-header-color simple-table-header"><strong>Task</strong></th><th id="aom[" class="simple-table-header-color simple-table-header"><strong>Responsible</strong></th><th id="N|un" class="simple-table-header-color simple-table-header"><strong>Deliverable</strong></th><th id="t^[f" class="simple-table-header-color simple-table-header"><strong>Notes</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80a3-b7cb-e1c337162713"><td id="=c]k" class="">✅ Purchase Wooberly license</td><td id="aom[" class="">UniPower</td><td id="N|un" class="">Payment confirmation</td><td id="t^[f" class="">Choose “Wooberly Taxi” base version</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8044-a3f8-ca5dd29949b7"><td id="=c]k" class="">✅ Share server access</td><td id="aom[" class="">UniPower</td><td id="N|un" class="">SSH root to clean Ubuntu 24.04</td><td id="t^[f" class="">AWS or DigitalOcean (4GB RAM / 50GB SSD min)</td></tr></div><div s
tyle="display:contents" dir="ltr"><tr id="294c5e6f-95bd-806e-a152-c2efc45805c6"><td id="=c]k" class="">✅ Provide domain &amp; SSL</td><td id="aom[" class="">UniPower</td><td id="N|un" class="">app.unitaxi.vn + Let’s Encrypt SSL</td><td id="t^[f" class="">SSL free via Let’s Encrypt</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80f2-8f57-dd4c966138f1"><td id="=c]k" class="">✅ Prepare developer accounts</td><td id="aom[" class="">UniPower</td><td id="N|un" class="">Apple ($99/yr) + Google ($25 one-time)</td><td id="t^[f" class="">Business-level, DUNS verified</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8082-81e1-cdacfed13dd9"><td id="=c]k" class="">✅ Provide branding package</td><td id="aom[" class="">UniPower</td><td id="N|un" class="">Logo, colour codes, app icons</td><td id="t^[f" class="">PNG/SVG per their design folder format</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80ed-be36-c45148bebbd2"><td id="=c]k" class="">✅ Share Google Maps &amp; Firebase API keys</td><td id="aom[" class="">UniPower</td><td id="N|un" class="">API credentials</td><td id="t^[f" class="">Enable Directions, Distance Matrix, Geocode, and Billing</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80a8-997e-dbaf3538a485"><td id="=c]k" class="">✅ Sign technical engagement email</td><td id="aom[" class="">UniPower &amp; 
RadicalStart</td><td id="N|un" class="">Formal approval to begin installation</td><td id="t^[f" class="">Needed for Trello activation</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="294c5e6f-95bd-80ae-8d31-fbb006cc111b"/></div><div style="display:contents" dir="auto"><h2 id="294c5e6f-95bd-80de-932a-cba5ceab4de3" class=""><strong>PHASE 1 – BASE INSTALLATION </strong></h2></div><div style="display:contents" dir="auto"><p id="294c5e6f-95bd-801f-8269-d61283adfc15" class=""><strong>🎯 Goal:</strong> Deploy stock Wooberly + configure environment.</p></div><div style="display:contents" dir="ltr"><table id="294c5e6f-95bd-802f-91a1-cdb1fa9371cc" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-804e-b93f-dda5d94d0a74"><th id="YgXX" class="simple-table-header-color simple-table-header"><strong>Task</strong></th><th id="O\ie" class="simple-table-header-color simple-table-header"><strong>Responsible</strong></th><th id="^DXQ" class="simple-table-header-color simple-table-header"><strong>Deliverable</strong></th><th id="Iy[=" class="simple-table-header-color simple-table-header"><strong>Notes</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8016-b446-dc80f0eaf78d"><td id="YgXX" class="">Install admin + rider + driver apps</td><td id="O\ie" class="">RadicalStart</td><td id="^DXQ" class="">Base app live on your server</td><td id="Iy[=" class="">One-time free installation</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80f2-8c08-d337f5035b8e"><td id="YgXX" class="">Configure Firebase, Maps, 
Twilio (OTP)</td><td id="O\ie" class="">RadicalStart</td><td id="^DXQ" class="">Working demo environment</td><td id="Iy[=" class="">You cover API usage cost</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-800f-813e-e9514b0877d7"><td id="YgXX" class="">Upload UniPower branding</td><td id="O\ie" class="">RadicalStart</td><td id="^DXQ" class="">Themed login &amp; splash screens</td><td id="Iy[=" class="">Uses your colours and logo</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80b1-aa33-e043cc9e9abe"><td id="YgXX" class="">Connect domain + SSL</td><td id="O\ie" class="">RadicalStart</td><td id="^DXQ" class="">HTTPS app URLs</td><td id="Iy[=" class="">Done via Let’s Encrypt</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80d6-b0a7-e587893feffc"><td id="YgXX" class="">Verify OTP, booking, dispatch flow</td><td id="O\ie" class="">UniPower QA</td><td id="^DXQ" class="">Confirm working end-to-end flow</td><td id="Iy[=" class="">Using internal test numbers</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="294c5e6f-95bd-802d-a6b9-dda8f0ff8f07"/></div><div style="display:contents" dir="auto"><h2 id="294c5e6f-95bd-802d-aa4e-f5e383ebdebf" class=""><strong>PHASE 2 – LOCALISATION &amp; COMPLIANCE </strong></h2></div><div style="display:contents" dir="auto"><p id="294c5e6f-95bd-80f7-846f-dc1537df976a" class=""><strong>🎯 Goal:</strong> Make app usable in Vietnam &amp; 
compliant with Decree 10.</p></div><div style="display:contents" dir="ltr"><table id="294c5e6f-95bd-802b-9527-c1a01f0d5abd" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8067-aa4c-db127ff692cd"><th id="&lt;{QM" class="simple-table-header-color simple-table-header"><strong>Task</strong></th><th id="j?=&gt;" class="simple-table-header-color simple-table-header"><strong>Responsible</strong></th><th id="IRSd" class="simple-table-header-color simple-table-header"><strong>Deliverable</strong></th><th id="KRz[" class="simple-table-header-color simple-table-header"><strong>Notes</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8037-be49-fb6d65d03c30"><td id="&lt;{QM" class="">Translate static content</td><td id="j?=&gt;" class="">RadicalStart (Free)</td><td id="IRSd" class="">VN/EN bilingual text</td><td id="KRz[" class="">Max 3 languages / 2 iterations</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8028-ab3b-f77b0f5b7116"><td id="&lt;{QM" class="">Localise address &amp; 
map defaults</td><td id="j?=&gt;" class="">RadicalStart</td><td id="IRSd" class="">vi_VN locale, VN road naming</td><td id="KRz[" class="">Verify map accuracy for HCMC/Hanoi</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8039-a442-e0b4c5d0f458"><td id="&lt;{QM" class="">Enable multi-currency (VND)</td><td id="j?=&gt;" class="">RadicalStart</td><td id="IRSd" class="">VND symbol, 
zero decimals</td><td id="KRz[" class="">Check formatting in fare display</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8041-b149-fb5ff47c0e20"><td id="&lt;{QM" class="">Configure SMS Gateway (Twilio or local VN)</td><td id="j?=&gt;" class="">UniPower</td><td id="IRSd" class="">Local number for OTP</td><td id="KRz[" class="">Optional: migrate to VN Gateway later</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-803a-b75b-d3ef1a89c0ae"><td id="&lt;{QM" class="">Test driver onboarding (manual review)</td><td id="j?=&gt;" class="">UniPower Ops</td><td id="IRSd" class="">Verify KYC flow</td><td id="KRz[" class="">Manual upload until OCR module ready</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="294c5e6f-95bd-80aa-8116-ef73bbda93dc"/></div><div style="display:contents" dir="auto"><h2 id="294c5e6f-95bd-805a-932e-f41ea8dc5950" class=""><strong>PHASE 3 – CUSTOM INTEGRATIONS </strong></h2></div><div style="display:contents" dir="auto"><p id="294c5e6f-95bd-809e-9f95-c71aec966f01" class=""><strong>🎯 Goal:</strong> Add critical Vietnam-only modules.</p></div><div style="display:contents" dir="ltr"><table id="294c5e6f-95bd-8074-8fac-df617fab02c0" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80c8-bade-e42009ddbe15"><th id="zc{g" class="simple-table-header-color simple-table-header"><strong>Task</strong></th><th id="dq&gt;J" class="simple-table-header-color simple-table-header"><strong>Responsible</strong></th><th id="Vl]@" class="simple-table-header-color simple-table-header"><strong>Deliverable</strong></th><th id="azfS" class="simple-table-header-color simple-table-header"><strong>Notes</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8016-bfd6-eafaee87976d"><td id="zc{g" class="">Add eInvoice provider API (MISA or Viettel)</td><td id="dq&gt;J" c
lass="">UniPower Tech Partner</td><td id="Vl]@" class="">Invoice Service (Admin + Rider)</td><td id="azfS" class="">Custom build (start parallel)</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8096-9c6c-cb68bbb155e9"><td id="zc{g" class="">Replace Stripe with VNPay/MoMo/ZaloPay</td><td id="dq&gt;J" class="">RadicalStart / Partner</td><td id="Vl]@" class="">Local payment integration</td><td id="azfS" class="">+US$25/hour est. 
40–60h</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8002-b3ee-f043307e43c1"><td id="zc{g" class="">Connect iSAC API (battery %, nearest charger)</td><td id="dq&gt;J" class="">UniPower Tech Partner</td><td id="Vl]@" class="">EV data visible in driver app</td><td id="azfS" class="">Sidecar API ready</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8001-b891-f4c5eea8a1b2"><td id="zc{g" class="">Build referral wallet (3% lifetime)</td><td id="dq&gt;J" class="">UniPower Dev</td><td id="Vl]@" class="">Sub-ledger + Admin reports</td><td id="azfS" class="">Phase 3 optional if time permits</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="294c5e6f-95bd-8094-965c-d247ef30445f"/></div><div style="display:contents" dir="auto"><h2 id="294c5e6f-95bd-801e-ab86-f5325566a0d9" class=""><strong>PHASE 4 – TESTING &amp; 
PILOT </strong></h2></div><div style="display:contents" dir="auto"><p id="294c5e6f-95bd-803d-9a27-f76bde9dc496" class=""><strong>🎯 Goal:</strong> Validate stability, speed, and compliance.</p></div><div style="display:contents" dir="ltr"><table id="294c5e6f-95bd-803d-9c58-f1e32a1ed34b" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8069-8488-d5191add4a8e"><th id="?iVv" class="simple-table-header-color simple-table-header"><strong>Task</strong></th><th id="\\&gt;l" class="simple-table-header-color simple-table-header"><strong>Responsible</strong></th><th id="JKIe" class="simple-table-header-color simple-table-header"><strong>Deliverable</strong></th><th id="BhLk" class="simple-table-header-color simple-table-header"><strong>Notes</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80ae-8378-f0f624badfee"><td id="?iVv" class="">Functional testing</td><td id="\\&gt;l" class="">UniPower QA</td><td id="JKIe" class="">Checklist: booking, cancel, payment, invoice, SOS</td><td id="BhLk" class="">Match time ≤ 60s</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-805e-b6ca-d25706eb9ca7"><td id="?iVv" class="">Performance testing</td><td id="\\&gt;l" class="">RadicalStart</td><td id="JKIe" class="">API latency report (P95 &lt; 
300ms)</td><td id="BhLk" class="">Load 300 drivers, 1k rides/day</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-803c-8ba9-cb1cb9fafb44"><td id="?iVv" class="">App Store submissions</td><td id="\\&gt;l" class="">RadicalStart</td><td id="JKIe" class="">Play Store + TestFlight builds</td><td id="BhLk" class="">Apple review may require unique branding</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80e7-ab7b-e705550a6ed0"><td id="?iVv" class="">Safety check: SOS, masked calls</td><td id="\\&gt;l" class="">UniPower Ops</td><td id="JKIe" class="">Verify live GPS &amp; call routing</td><td id="BhLk" class="">Critical for legal compliance</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="294c5e6f-95bd-80b0-a916-d92c8ee96f9b"/></div><div style="display:contents" dir="auto"><h2 id="294c5e6f-95bd-8003-bcd4-c9114ac2c0ca" class=""><strong>PHASE 5 – LAUNCH &amp; 
TRAINING </strong></h2></div><div style="display:contents" dir="auto"><p id="294c5e6f-95bd-803e-9700-d82eee8eb67f" class=""><strong>🎯 Goal:</strong> Go live with 300 EV drivers (pilot phase).</p></div><div style="display:contents" dir="ltr"><table id="294c5e6f-95bd-80b4-9d0e-dc0da0bc275d" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8024-8e7a-ef164c5e749b"><th id="xOLo" class="simple-table-header-color simple-table-header"><strong>Task</strong></th><th id="bszg" class="simple-table-header-color simple-table-header"><strong>Responsible</strong></th><th id="VuFq" class="simple-table-header-color simple-table-header"><strong>Deliverable</strong></th><th id="L;aX" class="simple-table-header-color simple-table-header"><strong>Notes</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80b3-a458-c5019220b183"><td id="xOLo" class="">Final data migration</td><td id="bszg" class="">UniPower</td><td id="VuFq" class="">Fleet, driver, station data</td><td id="L;aX" class="">Import via UniPortal</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8098-a98f-d8b6289de294"><td id="xOLo" class="">Admin dashboard handover</td><td id="bszg" class="">RadicalStart</td><td id="VuFq" class="">Credentials &amp; guide</td><td id="L;aX" class="">Full operational control</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80f9-9d36-c5833198bf37"><td id="xOLo" class="">Pilot launch (300 EVs, 10 Đội trưởng)</td><td id="bszg" class="">UniPower</td><td id="VuFq" class="">MVP Go-live</td><td id="L;aX" class="">With driver training &amp; safety briefing</td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-805c-9d10-d81634cb48cb"><td id="xOLo" class="">Feedback &amp; 
optimisation plan</td><td id="bszg" class="">Both teams</td><td id="VuFq" class="">Post-launch backlog</td><td id="L;aX" class="">Prioritise automation + ESG module next</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><hr id="294c5e6f-95bd-80ff-a357-de084c7d67d2"/></div><div style="display:contents" dir="auto"><h1 id="294c5e6f-95bd-8086-be23-e1e0f59c430f" class=""><strong>⚙️ Post-Launch </strong></h1></div><div style="display:contents" dir="auto"><p id="294c5e6f-95bd-80a7-9616-f462422bdcc5" class="">After MVP launch, focus on:</p></div><div style="display:contents" dir="auto"><ul id="294c5e6f-95bd-80c3-b343-cf0602e20bc6" class="bulleted-list"><li style="list-style-type:disc">Automating <strong>driver onboarding (OCR, face match)</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="294c5e6f-95bd-803b-a4c6-c33a17ceb595" class="bulleted-list"><li style="list-style-type:disc">Implementing <strong>referral wallet + PIT tax handling</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="294c5e6f-95bd-80fa-916e-c2a492de2e83" class="bulleted-list"><li style="list-style-type:disc">Expanding to <strong>UniPortal v2.0</strong> with finance, compliance, 
and EV dashboards.</li></ul></div><div style="display:contents" dir="auto"><ul id="294c5e6f-95bd-80dd-be23-c2d339b78e84" class="bulleted-list"><li style="list-style-type:disc">Adding <strong>Carbon Scoring / ESG reports</strong> for corporate clients.</li></ul></div><div style="display:contents" dir="auto"><ul id="294c5e6f-95bd-8080-b13a-fb9c31a557d7" class="bulleted-list"><li style="list-style-type:disc">Integrating <strong>charging loyalty programs</strong> with partner minimarts.</li></ul></div><div style="display:contents" dir="auto"><hr id="294c5e6f-95bd-80ea-a75a-edd6f60ff39b"/></div><div style="display:contents" dir="auto"><h1 id="294c5e6f-95bd-8014-a0b3-c4913255edb1" class=""><strong>📋 Quick Checklist for UniPower to Start Installation</strong></h1></div><div style="display:contents" dir="ltr"><table id="294c5e6f-95bd-803b-bfb5-f6f6756719a0" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-805c-a2c8-f860c47c85f9"><th id="iW`&gt;" class="simple-table-header-color simple-table-header" style="width:561px"><strong>✅</strong></th><th id="txvR" class="simple-table-header-color simple-table-header"><strong>Item</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80e5-a56e-f99320c1f7a3"><td id="iW`&gt;" class="" style="width:561px">☐ Purchase Wooberly license (confirm version)</td><td id="txvR" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8073-a0e2-f684afcca4b7"><td id="iW`&gt;" class="" style="width:561px">☐ Set up clean Ubuntu 24.04 server (AWS / DO)</td><td id="txvR" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-804f-9ce2-db5c0de9cba5"><td id="iW`&gt;" class="" style="width:561px">☐ Register Apple &amp; 
Google developer accounts</td><td id="txvR" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-800c-8d8e-cca915e29afe"><td id="iW`&gt;" class="" style="width:561px">☐ Purchase domain + SSL (Let’s Encrypt free)</td><td id="txvR" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80c9-8bc3-ec3444260640"><td id="iW`&gt;" class="" style="width:561px">☐ Prepare logo, colours, app icons</td><td id="txvR" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-808f-bd47-d615d56b755f"><td id="iW`&gt;" class="" style="width:561px">☐ Generate Google Maps API key (with billing)</td><td id="txvR" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-8081-bd16-c2eed5b12348"><td id="iW`&gt;" class="" style="width:561px">☐ Create Firebase project (iOS &amp; Android)</td><td id="txvR" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-80e0-8ea9-f139a187f029"><td id="iW`&gt;" class="" style="width:561px">☐ Twilio / VN Gateway SMS credentials</td><td id="txvR" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-800d-be9f-e66c9d97bd95"><td id="iW`&gt;" class="" style="width:561px">☐ Share all credentials via Trello board</td><td id="txvR" class=""></td></tr></div><div style="display:contents" dir="ltr"><tr id="294c5e6f-95bd-803c-9eff-ebaf4834ecf1"><td id="iW`&gt;" class="" style="width:561px">☐ Approve installation start</td><td id="txvR" class=""></td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><p id="294c5e6f-95bd-8057-9dbf-f508f31384f8" class="">
</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
