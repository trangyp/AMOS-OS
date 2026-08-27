---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>The Cost of “Acceptable Harm”</title><style>
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
	
</style></head><body><article id="2e4c5e6f-95bd-8077-93a4-df299c0a71fe" class="page sans"><header><h1 class="page-title" dir="auto"><strong>The Cost of “Acceptable Harm”</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80a3-9e5e-fb93f35f050a" class=""><strong>How Systems Convert Human Damage Into Operating Margin</strong></h2></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-806c-84e8-fdd3e93a2345"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8062-a515-c4dd5642d353" class=""><strong>The Inescapable Truth</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b9-bc54-ddec91cd5d79" class="">“Acceptable harm” is not a description.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8063-a8d2-c8e868adf0a2" class="">It is a <strong>permission structure</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-807c-989a-fc18e242d02f" class="">The moment harm is declared acceptable, it is no longer an accident.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-801a-b9bb-f4ed118e5b3d" class="">It becomes <strong>authorized damage</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ea-b6d9-fc0ce358bfaa" class="">From that point on, suffering is not a failure of the system.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-802a-951b-efc9e48e8cd1" class="">It is a <strong>feature that keeps it running</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80b0-855e-e627ca505da4"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8096-bd12-e2d009b30230" class=""><strong>The Prime Law</strong></h2></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-80c7-b7cf-e3731046e72d" class="">Harm is not inevitable.</blockquote></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-802c-bd48-f8fabdd6cc01" class="">Its acceptance is engineered, priced, and enforced.</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8059-b8a4-e5b4e5980001" class="">Every system that tolerates “acceptable harm” has already made four decisions:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8068-bec0-e47eecafaf3a" class="numbered-list" start="1"><li>Harm will occur.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-805c-803b-c04c9b44ec4d" class="numbered-list" start="2"><li>Harm will not stop execution.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-809a-8b3f-c586a5a1393d" class="numbered-list" start="3"><li>Harm will be borne by others.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80fb-867d-f5037d864361" class="numbered-list" start="4"><li>Harm will not threaten power.</li></ol></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ef-a0e1-e5581ce1c3ce" class="">This is not ethics.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-809e-9d0a-fccb97c5b294" class="">This is <strong>economics</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80a8-bb8d-fe29ca181d3e"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80f5-aa37-e45c363f9be6" class=""><strong>What “Acceptable Harm” Really Means</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8013-a90c-c43fd6f2433a" class="">“Acceptable harm” never means:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8062-aa98-db0fedfcdc9a" class="bulleted-list"><li style="list-style-type:disc">harm is unavoidable</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80cc-9ba7-c515c36dec5e" class="bulleted-list"><li style="list-style-type:disc">harm is minimal</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8094-bc42-d4eb9ddaf78c" class="bulleted-list"><li style="list-style-type:disc">harm is temporary</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-802d-9458-ec11d1a86626" class="">It means:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-801d-af65-d6b868893cf6" class="bulleted-list"><li style="list-style-type:disc">harm has been <strong>normalized</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802d-8bf3-d6109c1e095a" class="bulleted-list"><li style="list-style-type:disc">harm has been <strong>externalized</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-807c-800c-c2443e4df8d2" class="bulleted-list"><li style="list-style-type:disc">harm has been <strong>accounted for</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-808f-8e2f-c47e508375a2" class="bulleted-list"><li style="list-style-type:disc">harm has been <strong>depoliticized</strong></li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8032-9ac7-e120eae882b4" class="">Once harm is acceptable, it is no longer debated.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80e9-81ba-c60a92f3c03d" class="">It is <strong>budgeted</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80aa-ba3f-eb77a6d7d47a"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80fd-9f44-cf239cc098f7" class=""><strong>Who Decides — and Why It Is Never the Injured</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ef-b76f-f88c99d1bb09" class="">There is a universal asymmetry:</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8091-99eb-ee8895af87d6" class="">Those who define acceptable harm:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80fc-a2ef-f16c7de3d259" class="bulleted-list"><li style="list-style-type:disc">do not experience it</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-800b-b467-cad212a22459" class="bulleted-list"><li style="list-style-type:disc">do not absorb its cost</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c5-8764-cdfac0156259" class="bulleted-list"><li style="list-style-type:disc">do not suffer its accumulation</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e2-a1a3-c9c0d5d09cb8" class="bulleted-list"><li style="list-style-type:disc">do not live with its aftermath</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8051-9ea1-db80c779a2e6" class="">Those who experience harm:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8001-b189-d80756e8a0ec" class="bulleted-list"><li style="list-style-type:disc">did not consent</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80ea-9c6e-dbe8c09a4106" class="bulleted-list"><li style="list-style-type:disc">could not refuse</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c4-a93a-da3bed6a1420" class="bulleted-list"><li style="list-style-type:disc">lacked leverage</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8048-abbb-d29b7ceb4266" class="bulleted-list"><li style="list-style-type:disc">lacked alternatives</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80be-b458-dfa33e8ef9c6" class="">This is not moral failure.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8033-9bb3-f0b364860187" class="">It is <strong>power geometry</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-806d-85b7-ca84551ee8a9"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-80b6-9764-ea114195da08" class=""><strong>Acceptable Harm as a Sorting Mechanism</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80de-90a5-d756ab833855" class="">“Acceptable harm” is how systems decide:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8037-8c1b-df5cebf8410d" class="bulleted-list"><li style="list-style-type:disc">whose bodies are expendable</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802e-b892-e67b94da1495" class="bulleted-list"><li style="list-style-type:disc">whose time can be consumed</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80f4-8339-ed1386d8b4cf" class="bulleted-list"><li style="list-style-type:disc">whose health can be degraded</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8073-9936-c02da1de688b" class="bulleted-list"><li style="list-style-type:disc">whose lives can be destabilized</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80df-865c-e040be5aac91" class="bulleted-list"><li style="list-style-type:disc">whose futures can be discounted</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-804f-b409-c623c14ee7b7" class="">Harm flows predictably toward:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80be-9f5a-f6e2e3759fda" class="bulleted-list"><li style="list-style-type:disc">workers instead of owners</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d2-8113-e2ac8d1737a4" class="bulleted-list"><li style="list-style-type:disc">users instead of platforms</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-804d-b9ef-e671bc918e72" class="bulleted-list"><li style="list-style-type:disc">tenants instead of developers</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80eb-b4a1-cdf2b272a518" class="bulleted-list"><li style="list-style-type:disc">patients instead of systems</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d2-bc94-f125868bca85" class="bulleted-list"><li style="list-style-type:disc">the poor instead of the protected</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-802f-a635-f6d9ed752291" class="bulleted-list"><li style="list-style-type:disc">the future instead of the present</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b6-9d2f-c95f003c657a" class="">This is not bias.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-805c-9012-f3342f363103" class="">It is <strong>structural optimization</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80dd-ab4e-c456512e6feb"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8088-a244-e1ddffd74d50" class=""><strong>The Quiet Normalization Process</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c3-815a-e197680915f4" class="">Harm is not normalized through cruelty.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8023-bd80-d3202ac002e0" class="">It is normalized through <strong>administration</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-802f-bca8-d98873949fa6" class="">The sequence is invariant:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-804f-8f1d-ecac050db1d2" class="numbered-list" start="1"><li>Harm appears as an exception</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80c1-8e45-fdb26f8928d3" class="numbered-list" start="2"><li>Language softens (“edge case,” “acceptable risk”)</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8038-b066-d4c44ca582c2" class="numbered-list" start="3"><li>Metrics exclude it</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8002-9701-fe61e133f2fb" class="numbered-list" start="4"><li>Responsibility diffuses</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8042-a33e-e5139df42994" class="numbered-list" start="5"><li>Complaints are reframed as noise</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80fe-b0bf-f618b8343a02" class="numbered-list" start="6"><li>Harm becomes background condition</li></ol></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80a5-b802-c7e395d767e9" class="">No villain is required.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80dc-9973-cf7a2ec26075" class="">The system stabilizes around damage.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-808e-8156-cd676832c913"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-805a-af41-d9a8acb5e2a3" class=""><strong>Language as a Weapon of Legitimacy</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8005-9ef6-f2fc1e6e8ea1" class="">Phrases like:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8045-8d1d-d1be0de30043" class="bulleted-list"><li style="list-style-type:disc">“acceptable harm”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806c-941b-f5f1531993eb" class="bulleted-list"><li style="list-style-type:disc">“tradeoff”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8031-b968-c9b4b977695a" class="bulleted-list"><li style="list-style-type:disc">“collateral impact”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e2-8b2c-c1085d0648a8" class="bulleted-list"><li style="list-style-type:disc">“externality”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-806d-8638-e4cb08aad75e" class="bulleted-list"><li style="list-style-type:disc">“statistical loss”</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ba-b4ce-ec30c023a61b" class="">exist to <strong>strip harm of moral status</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80e6-a24c-d87d42333225" class="">Once harm is abstracted:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8097-bcff-d6115d997c35" class="bulleted-list"><li style="list-style-type:disc">it becomes governable</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8033-b744-df1a6d71477c" class="bulleted-list"><li style="list-style-type:disc">it becomes deniable</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-805d-928f-ef206037c45a" class="bulleted-list"><li style="list-style-type:disc">it becomes permanent</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80d0-a6c2-d827fc06bfae" class="">This is how systems injure without ever admitting injury.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8068-af75-ca1e9f12d148"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8097-aa00-db0ca05d2721" class=""><strong>Why “Acceptable Harm” Always Expands</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f0-bde4-db71ebf8ac01" class="">Acceptable harm is metastable.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-801c-959d-dcc7f91ad601" class="">It grows because:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8092-bc78-d1027ba29dbb" class="bulleted-list"><li style="list-style-type:disc">thresholds are raised incrementally</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80b3-a9b5-e9f255dd6cf7" class="bulleted-list"><li style="list-style-type:disc">safeguards are quietly relaxed</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-808b-88c6-e3c3d64cd1de" class="bulleted-list"><li style="list-style-type:disc">affected groups are marginalized</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80d9-9a03-fd34c7568158" class="bulleted-list"><li style="list-style-type:disc">correction is deferred</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8027-917c-e73d85e9d7bf" class="bulleted-list"><li style="list-style-type:disc">success metrics reward continuation</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-800d-ab1f-f496d5ded87b" class="">What was once intolerable becomes routine.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80e8-913e-fe8e55b4df18" class="">Not because people changed —</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803c-b39f-c835cd480963" class="">but because <strong>systems reward adaptation to harm</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80a4-80d9-e5fdfa3e77f5"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-804c-ac9c-d56b3cd5c9bc" class=""><strong>Metrics as Harm-Laundering Infrastructure</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8091-8430-e6242a22c2d9" class="">Metrics do not merely hide harm.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-808b-8546-ff9e1387f41b" class="">They <strong>sanitize it</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803e-834d-ec7316653c82" class="">When harm:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8098-a438-c9bbfc7b8133" class="bulleted-list"><li style="list-style-type:disc">is long-term</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e7-8dfa-e7ed14d11a90" class="bulleted-list"><li style="list-style-type:disc">is diffuse</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8058-ba67-d01705824be0" class="bulleted-list"><li style="list-style-type:disc">is psychological</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8060-88db-c3e9ae1c788c" class="bulleted-list"><li style="list-style-type:disc">is social</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-804d-989c-c9fe37da356c" class="bulleted-list"><li style="list-style-type:disc">is cumulative</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80e7-9431-cee091117838" class="">it disappears from dashboards.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-806c-9b20-ff2355bd4041" class="">Systems then claim:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e4-8c26-d40d28c72e4b" class="bulleted-list"><li style="list-style-type:disc">“no evidence”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8048-bc58-c1203f31fd1b" class="bulleted-list"><li style="list-style-type:disc">“no measurable impact”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-801a-8690-f7ece4720a04" class="bulleted-list"><li style="list-style-type:disc">“no signal”</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8089-99a6-d06f21c77d86" class="">Metrics do not fail to see harm.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-807a-a8bb-eadbcab09ca2" class="">They are <strong>designed not to count it</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8089-adcb-c43672bf542f"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8012-b44b-e73599574674" class=""><strong>Tradeoffs Without Consent Are Not Tradeoffs</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8027-aa8d-e28962a481c5" class="">A tradeoff is legitimate only if:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-805b-9496-cbf2328c96ba" class="bulleted-list"><li style="list-style-type:disc">all affected parties consent</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8081-b3cd-de4853a11959" class="bulleted-list"><li style="list-style-type:disc">all can refuse</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8078-9062-d65ca2f373f5" class="bulleted-list"><li style="list-style-type:disc">all share risk symmetrically</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c2-8de9-d5eeec8e8bf4" class="">Most “tradeoffs” fail all three.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8058-bfc1-e6a41be189da" class="">They are unilateral impositions justified after the fact.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803f-aaf7-f2a51429df68" class="">Calling imposed harm a tradeoff is not realism.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f7-97a0-da61ed65b3ab" class="">It is <strong>ethical evasion</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-80ae-9109-e2f1c6207791"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8042-b32d-c7bfbfb05211" class=""><strong>Why Compensation Is Not Repair</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8030-a979-d7cb24c4f43c" class="">Compensation assumes harm is acceptable as long as it is paid for.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8002-81f5-eb1982938d7f" class="">This logic fails because:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8087-bb9a-fc7c10778c4c" class="bulleted-list"><li style="list-style-type:disc">damage accumulates</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8062-a0a2-cda12980a391" class="bulleted-list"><li style="list-style-type:disc">dignity is not fungible</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8099-9465-fa96fabb44fc" class="bulleted-list"><li style="list-style-type:disc">health does not reset</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8035-98d8-c7de171fcce0" class="bulleted-list"><li style="list-style-type:disc">trust does not replenish linearly</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8069-8f70-e586c74f0214" class="">Compensation legitimizes harm rather than preventing it.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80f9-9769-fe0a1cb313ec" class="">It is a <strong>license to continue</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-8084-89f7-dccc4cb8fe6e"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-8024-8b1e-cc5e2425dd61" class=""><strong>The Ethical Intelligence™ Rejection</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8090-835e-e928ae23557d" class="">Ethical Intelligence™ rejects “acceptable harm” as a valid category.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80c0-96a5-d520fb98fd90" class="">Instead, it enforces:</p></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80a6-a9eb-eb560f8f8cb7" class="numbered-list" start="1"><li>Harm identified <em>before</em> execution.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8064-9e3b-c472a80065c4" class="numbered-list" start="2"><li>Harm prevention prioritized over optimization.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-80a2-ae0f-c19aa4019171" class="numbered-list" start="3"><li>Explicit ownership of harm by decision-makers.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8011-bd20-f6afa9d7f80e" class="numbered-list" start="4"><li>Consent from those exposed to risk.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-804a-80df-e221b37db3dc" class="numbered-list" start="5"><li>Refusal without penalty.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-803a-b62e-e203799f36c1" class="numbered-list" start="6"><li>Reversibility wherever possible.</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="2e4c5e6f-95bd-8063-bc95-cd26c17be5b3" class="numbered-list" start="7"><li>Thresholds that tighten under scale.</li></ol></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8061-879f-ece66c014df7" class="">If harm must occur, it must be:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c8-a785-ea0b5186168b" class="bulleted-list"><li style="list-style-type:disc">minimal</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8036-b266-d39752f6a9c9" class="bulleted-list"><li style="list-style-type:disc">temporary</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8037-b6ce-d7366faf6ed2" class="bulleted-list"><li style="list-style-type:disc">reversible</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-804e-8c1f-dda3d67617e7" class="bulleted-list"><li style="list-style-type:disc">consented to</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80c7-99dd-c56e0a8c3258" class="bulleted-list"><li style="list-style-type:disc">borne by those who choose it</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8085-b5da-e21ddb4d8803" class="">Anything else is structural abuse.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-802d-8261-d2e44a822cc3"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-809f-a377-c22dfe580c79" class=""><strong>The Question That Ends the Argument</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80ac-a46c-c378c5b38538" class="">Ask one question — and do not soften it:</p></div><div style="display:contents" dir="auto"><blockquote id="2e4c5e6f-95bd-80f9-b5ed-f6583ca409f8" class="">Who is being harmed, and why are they considered expendable?</blockquote></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b7-9f58-dafcfb12d0e8" class="">If the answer is:</p></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80cb-af8b-ec6aa568269b" class="bulleted-list"><li style="list-style-type:disc">“they don’t have a choice”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-8095-9921-e57cb8acc5f6" class="bulleted-list"><li style="list-style-type:disc">“that’s how the system works”</li></ul></div><div style="display:contents" dir="auto"><ul id="2e4c5e6f-95bd-80e3-9a9b-d9d7a4564c64" class="bulleted-list"><li style="list-style-type:disc">“it’s the cost of progress”</li></ul></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803b-a09c-f76b6055741e" class="">Then harm is not acceptable.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-801e-b166-fbf78f6abd3f" class="">It is <strong>engineered exploitation</strong>.</p></div><div style="display:contents" dir="auto"><hr id="2e4c5e6f-95bd-808e-adbe-c6d620522125"/></div><div style="display:contents" dir="auto"><h2 id="2e4c5e6f-95bd-800d-b529-e1185a888174" class=""><strong>The Final Law</strong></h2></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8002-bcb0-e0ed8dee5a7f" class="">“Acceptable harm” is the language systems use when they have decided that some people are worth less than continuation.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-80b9-8a08-fbc64f973daf" class="">Systems that rely on acceptable harm do not scale ethically.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-803c-bdce-f8711fbf10da" class="">They scale <strong>by consuming human integrity</strong>.</p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8033-b69f-fd159dab2df4" class=""><strong>Ethical Intelligence™ draws a hard line:</strong></p></div><div style="display:contents" dir="auto"><p id="2e4c5e6f-95bd-8069-9d19-fc8a0357f3f9" class=""><strong>harm is not a cost of progress — it is evidence of design failure.</strong></p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
