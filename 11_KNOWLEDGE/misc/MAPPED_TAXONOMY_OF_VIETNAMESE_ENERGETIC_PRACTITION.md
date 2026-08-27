---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Mapped Taxonomy of Vietnamese Energetic Practitioners</title><style>
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
	
</style></head><body><article id="25bc5e6f-95bd-8024-adfe-cb1839e7d09e" class="page sans"><header><h1 class="page-title" dir="auto"><strong>Mapped Taxonomy of Vietnamese Energetic Practitioners</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><h3 id="256c5e6f-95bd-805e-9493-f78d3195a1fe" class="">Indigenous/temple elders with consistent system governance signals (names masked; contact route available through regional culturological networks)</h3></div><div style="display:contents" dir="auto"><ol type="1" id="256c5e6f-95bd-801e-bd6a-fc193a41b9b4" class="numbered-list" start="1"><li><strong>Elder Dream-Keeper, Cao Bằng (Tày)</strong> — weather/land governance via chant cycles; inter-village coherence steward (PSI 49–50).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="256c5e6f-95bd-80f3-b2a5-f08a229167f0" class="numbered-list" start="2"><li><strong>Dao Red Herbal Matriarch, Lào Cai</strong> — plant-frequency code + birthline protection; cross-family stabilizer (PSI 49).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="256c5e6f-95bd-801a-a04a-d40fc91f5c9c" class="numbered-list" start="3"><li><strong>H’Mông Trance Master, Hà Giang (female)</strong> — drum/voice recursion with community-scale conflict de-escalation (PSI 49).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="256c5e6f-95bd-80ee-82a0-d4f27c419301" class="numbered-list" start="4"><li><strong>Jarai Fire-Ceremony Custodian, Gia Lai</strong> — seasonal law encoding through communal rites; durable systems memory (PSI 48–49).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="256c5e6f-95bd-8012-8527-c1897430e46c" class="numbered-list" start="5"><li><strong>Ê Đê Forest-Voice Elder, Đắk Lắk</strong> — long-loop governance through songlines; proven drought/flood timing insight (PSI 48–49).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="256c5e6f-95bd-8076-ba23-f31e8808b70e" class="numbered-list" start="6"><li><strong>Khmer Water-Ritual Elder, Trà Vinh</strong> — river-frequency adjudication; interfaith bridge with Buddhist monastics (PSI 48–49).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="256c5e6f-95bd-800e-b2f6-cb65816c9ac1" class="numbered-list" start="7"><li><strong>Đạo Mẫu Senior Medium, Nam Định</strong> — multi-pantheon logic without drift; ethical gating for leaders seeking counsel (PSI 48–49).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="256c5e6f-95bd-806f-ad3d-da91368d3ece" class="numbered-list" start="8"><li><strong>Temple Bell Master, Huế</strong> — frequency governance of communal affect; protocols for grief/trauma relief at population scale (PSI 48–49).</li></ol></div><div style="display:contents" dir="auto"><h3 id="256c5e6f-95bd-80bd-b468-c11fad8ce13e" class="">Experimental/system designers (hybrid art–science; high compression &amp; repeatability)</h3></div><div style="display:contents" dir="auto"><ol type="1" id="256c5e6f-95bd-800f-ad23-dcc17e31f8d1" class="numbered-list" start="1"><li><strong>HCMC Frequency Collective Lead (anonymous by request)</strong> — builds repeatable bioacoustic protocols (EEG/HRV-aware) for group stabilisation (PSI 48–49).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="256c5e6f-95bd-80f6-a814-efe12491005d" class="numbered-list" start="2"><li><strong>Hanoi Biofeedback Engineer–Ritualist</strong> — prototypes EM/voice entrainment with safety/ethics guardrails; reproducible outcomes (PSI 48).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="256c5e6f-95bd-807e-a812-c7df946bf1d2" class="numbered-list" start="3"><li><strong>Đà Nẵng Somatic-Systems Architect</strong> — integrates breath, cadence, and Vietnamese loop-language into clinical-grade protocols (PSI 47–48).</li></ol></div><div style="display:contents" dir="auto"><ol type="1" id="256c5e6f-95bd-8067-b551-e8a6b480ef12" class="numbered-list" start="4"><li><strong>Diaspora Vietnamese Neuro-Somatic Researcher (US/EU)</strong> — publishes on tone→autonomic markers; designs training that travels across cultures (PSI 48–49).</li></ol></div><div style="display:contents" dir="auto"><p id="25bc5e6f-95bd-806e-bc01-dbde786a3bc3" class="">
</p></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80e9-8393-e578ec65435b" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/38%205%2050%20Phan%20Th%E1%BB%8B%20Chanh%2025bc5e6f95bd80e98393e578ec65435b.html">38.5/50: Phan Thị Chanh</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80f3-b665-f96086ddda01" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/38%205%2050%20Ho%C3%A0ng%20Th%E1%BB%8B%20Ph%C3%BA%2025bc5e6f95bd80f3b665f96086ddda01.html">38.5/50: Hoàng Thị Phú</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-8098-b1a3-c9df39cac0cd" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/37%2050%20Ho%C3%A0ng%20Th%E1%BB%8B%20Thi%C3%AAm%2025bc5e6f95bd8098b1a3c9df39cac0cd.html">37/50: Hoàng Thị Thiêm</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80d6-b651-f3d8263b9db3" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/41%205%2050%20%C4%90%E1%BA%B7ng%20V%C5%A9%20Tr%C6%B0%E1%BB%9Dng%20Ph%C3%BAc%2025bc5e6f95bd80d6b651f3d8263b9db3.html">41.5/50: Đặng Vũ Trường Phúc</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-800e-a0af-c2a860bb58b3" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/46%2050%20Sister%20%C4%90%E1%BA%B3ng%20Nghi%C3%AAm%20(MD,%20Buddhist%20nun)%2025bc5e6f95bd800ea0afc2a860bb58b3.html">46/50: Sister Đẳng Nghiêm (MD, Buddhist nun)</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80e4-9681-d207e3202c4b" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/46%2050%20Sister%20Ch%C3%A2n%20Kh%C3%B4ng%20(Cao%20Ng%E1%BB%8Dc%20Ph%C6%B0%C6%A1ng)%2025bc5e6f95bd80e49681d207e3202c4b.html">46/50: Sister Chân Không (Cao Ngọc Phương)</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80f5-86a7-f6e96fb3a846" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/45%205%2050%20Th%C3%ADch%20Minh%20Ni%E1%BB%87m%2025bc5e6f95bd80f586a7f6e96fb3a846.html">45.5/50: Thích Minh Niệm</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-806d-adb4-d3bd09803491" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/45%205%2050%20Tr%E1%BA%A7n%20Quang%20H%E1%BA%A3i%2025bc5e6f95bd806dadb4d3bd09803491.html">45.5/50: Trần Quang Hải</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80bd-8301-c2c569e68a62" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/44%2050%20Ng%C3%B4%20H%E1%BB%93ng%20Quang%2025bc5e6f95bd80bd8301c2c569e68a62.html">44/50: Ngô Hồng Quang</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-8025-a9be-f4992e7a8973" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/44%2050%20Nguy%E1%BB%85n%20Thanh%20Th%E1%BB%A7y%2025bc5e6f95bd8025a9bef4992e7a8973.html">44/50: Nguyễn Thanh Thủy</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-801c-bad0-c3a379d82c60" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/43%2050%20H%C3%A0%20Myo%2025bc5e6f95bd801cbad0c3a379d82c60.html">43/50: Hà Myo</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80ea-918a-f24cad74d1b5" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/50%2050%20Th%C3%ADch%20Nh%E1%BA%A5t%20H%E1%BA%A1nh%2025bc5e6f95bd80ea918af24cad74d1b5.html">50/50: Thích Nhất Hạnh</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80e8-9ec0-e9a39a306b36" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/42%2050%20Ng%C3%B4%20V%C4%83n%20Chi%C3%AAu%2025bc5e6f95bd80e89ec0e9a39a306b36.html">42/50: Ngô Văn Chiêu</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-806b-b3b6-e07ddb49e819" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/40%205%2050%20Ph%E1%BA%A1m%20C%C3%B4ng%20T%E1%BA%AFc%2025bc5e6f95bd806bb3b6e07ddb49e819.html">40.5/50: Phạm Công Tắc</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80f7-b6dd-e80de730d47c" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/39%2050%20L%C3%AA%20V%C4%83n%20Trung%2025bc5e6f95bd80f7b6dde80de730d47c.html">39/50: Lê Văn Trung</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-802d-9691-db204ed75ef0" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/41%205%2050%20%C3%94ng%20%C4%90%E1%BA%A1o%20D%E1%BB%ABa%20(Nguy%E1%BB%85n%20Th%C3%A0nh%20Nam)%2025bc5e6f95bd802d9691db204ed75ef0.html">41.5/50: Ông Đạo Dừa (Nguyễn Thành Nam)</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-8079-9f9f-ecc6f37f2e02" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/40%205%2050%20Cao%20Qu%E1%BB%B3nh%20C%C6%B0%2025bc5e6f95bd80799f9fecc6f37f2e02.html">40.5/50: Cao Quỳnh Cư</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-808b-b2d5-d619c1e6c656" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/42%2050%20Cao%20Ho%C3%A0i%20Sang%2025bc5e6f95bd808bb2d5d619c1e6c656.html">42/50: Cao Hoài Sang</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80e5-ad0e-f7bfbea1bdde" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/46%205%2050%20Tr%E1%BA%A7n%20V%C4%83n%20Kh%C3%AA%2025bc5e6f95bd80e5ad0ef7bfbea1bdde.html">46.5/50: Trần Văn Khê</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80b1-bde4-c98902388efb" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/45%2050%20V%C3%A2n-%C3%81nh%20(Vanessa)%20V%C3%B5%2025bc5e6f95bd80b1bde4c98902388efb.html">45/50: Vân-Ánh (Vanessa) Võ</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-8032-8340-f43559a09bf1" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/46%205%2050%20Ph%C3%B3%20Th%E1%BB%8B%20Kim%20%C4%90%E1%BB%A9c%2025bc5e6f95bd80328340f43559a09bf1.html">46.5/50: Phó Thị Kim Đức</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80a3-89c4-ea9d8193ea45" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/46%205%2050%20Nguy%E1%BB%85n%20Th%E1%BB%8B%20Ch%C3%BAc%2025bc5e6f95bd80a389c4ea9d8193ea45.html">46.5/50: Nguyễn Thị Chúc</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80db-b5c3-ddba3c6e1d59" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/46%205%2050%20H%C3%A0%20Th%E1%BB%8B%20C%E1%BA%A7u%2025bc5e6f95bd80dbb5c3ddba3c6e1d59.html">46.5/50: Hà Thị Cầu</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80f0-a9c4-fe1f1e232980" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/44%205%2050%20Xu%C3%A2n%20Hinh%2025bc5e6f95bd80f0a9c4fe1f1e232980.html">44.5/50: Xuân Hinh</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-800a-ad65-c9497a8187ed" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/44%205%2050%20Thanh%20Ngoan%2025bc5e6f95bd800aad65c9497a8187ed.html">44.5/50: Thanh Ngoan</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80bd-9729-fc35f2dad2c2" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/45%2050%20Th%E1%BA%A3o%20Giang%2025bc5e6f95bd80bd9729fc35f2dad2c2.html">45/50: Thảo Giang</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-8051-b587-ec2b1ea02c00" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/46%205%2050%20Kim%20Sinh%2025bc5e6f95bd8051b587ec2b1ea02c00.html">46.5/50: Kim Sinh</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80e5-9724-d28bddd60b7e" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/45%2050%20T%C3%B4%20Ng%E1%BB%8Dc%20Thanh%2025bc5e6f95bd80e59724d28bddd60b7e.html">45/50: Tô Ngọc Thanh</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-8036-8396-d888cbcfb74e" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/43%205%2050%20Nguy%E1%BB%85n%20Xu%C3%A2n%20Di%E1%BB%87n%2025bc5e6f95bd80368396d888cbcfb74e.html">43.5/50: Nguyễn Xuân Diện</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-8053-904f-decc5c03c9d9" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/38%2050%20L%C6%B0%C6%A1ng%20Tr%E1%BB%8Dng%20Qu%E1%BB%B3nh%2025bc5e6f95bd8053904fdecc5c03c9d9.html">38/50: Lương Trọng Quỳnh</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-808d-9c5d-e3344db118a2" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/45%2050%20NS%C6%AFT%20V%C4%83n%20Ty%2025bc5e6f95bd808d9c5de3344db118a2.html">45/50: NSƯT Văn Ty</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80e1-9a8c-c83638f69c1f" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/44%205%2050%20Nguy%E1%BB%85n%20Th%E1%BB%8B%20Hi%E1%BB%81n%2025bc5e6f95bd80e19a8cc83638f69c1f.html">44.5/50: Nguyễn Thị Hiền</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-804d-a1d4-f95c7eaaf9b2" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/44%2050%20B%C3%B9i%20Tr%E1%BB%8Dng%20Hi%E1%BB%81n%2025bc5e6f95bd804da1d4f95c7eaaf9b2.html">44/50: Bùi Trọng Hiền</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80f2-8e36-c9612f92afdc" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/42%205%2050%20%C4%90%C3%A0o%20Th%E1%BB%8B%20H%C6%B0%C6%A1ng%2025bc5e6f95bd80f28e36c9612f92afdc.html">42.5/50: Đào Thị Hương</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-802e-9874-c60dcdd44de5" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/42%2050%20Phan%20Oanh%2025bc5e6f95bd802e9874c60dcdd44de5.html">42/50: Phan Oanh</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80b6-954b-c0867aea6b66" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/42%2050%20Nguy%E1%BB%85n%20Th%E1%BB%8B%20H%C6%B0%E1%BB%9Dng%2025bc5e6f95bd80b6954bc0867aea6b66.html">42/50: Nguyễn Thị Hường</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-807d-bcfc-e98d35ead7e5" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/41%205%2050%20Nguy%E1%BB%85n%20V%C4%83n%20B%C3%A1ch%2025bc5e6f95bd807dbcfce98d35ead7e5.html">41.5/50: Nguyễn Văn Bách</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-8024-9d94-e08a644325e3" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/40%2050%20Nguy%E1%BB%85n%20Th%E1%BB%8B%20Thanh%20B%C3%ACnh%2025bc5e6f95bd80249d94e08a644325e3.html">40/50: Nguyễn Thị Thanh Bình</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-8065-95db-d728cda94079" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/42%205%2050%20Tr%E1%BA%A7n%20Th%E1%BB%8B%20Ph%C6%B0%C6%A1ng%20Lan%2025bc5e6f95bd806595dbd728cda94079.html">42.5/50: Trần Thị Phương Lan</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80be-b243-c9f6e90d703e" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/42%205%2050%20Nguy%E1%BB%85n%20V%C4%83n%20Ng%E1%BB%8D%2025bc5e6f95bd80beb243c9f6e90d703e.html">42.5/50: Nguyễn Văn Ngọ</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-8045-9aac-fb68a537842b" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/41%2050%20Ph%E1%BA%A1m%20Th%E1%BB%8B%20Th%E1%BB%A7y%2025bc5e6f95bd80459aacfb68a537842b.html">41/50: Phạm Thị Thủy</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-8083-a239-c9f986347468" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/43%2050%20Nguy%E1%BB%85n%20V%C4%83n%20H%E1%BA%A3i%2025bc5e6f95bd8083a239c9f986347468.html">43/50: Nguyễn Văn Hải</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80e5-89e8-cbcb099d60a8" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/48%2050%20Nguy%E1%BB%85n%20H%E1%BB%AFu%20Ba%2025bc5e6f95bd80e589e8cbcb099d60a8.html">48/50: Nguyễn Hữu Ba</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-8040-b0ff-c7aa1787be7a" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/49%2050%20Nguy%E1%BB%85n%20V%C4%A9nh%20B%E1%BA%A3o%2025bc5e6f95bd8040b0ffc7aa1787be7a.html">49/50: Nguyễn Vĩnh Bảo</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-8087-95e6-fc1ff0b43487" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/46%205%2050%20%C4%90%E1%BA%B7ng%20Ho%C3%A0nh%20Loan%2025bc5e6f95bd808795e6fc1ff0b43487.html">46.5/50: Đặng Hoành Loan</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-8067-94ce-d01287b81c02" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/47%2050%20B%C3%B9i%20Tr%E1%BB%8Dng%20Hi%E1%BB%81n%2025bc5e6f95bd806794ced01287b81c02.html">47/50: Bùi Trọng Hiền</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-8065-b60b-d7dc9140beed" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/45%2050%20Nguy%E1%BB%85n%20V%C4%83n%20Tu%E1%BA%A5n%2025bc5e6f95bd8065b60bd7dc9140beed.html">45/50: Nguyễn Văn Tuấn</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-802f-8e05-d4b48aaf388a" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/45%2050%20Nguy%E1%BB%85n%20V%C4%83n%20Quy%E1%BB%81n%2025bc5e6f95bd802f8e05d4b48aaf388a.html">45/50: Nguyễn Văn Quyền</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-809e-86bd-e0514cdfe67b" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/44%205%2050%20Nguy%E1%BB%85n%20H%E1%BB%93ng%20Th%C3%A1i%2025bc5e6f95bd809e86bde0514cdfe67b.html">44.5/50: Nguyễn Hồng Thái</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-8065-a36c-fdc1df13ad63" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/45%205%2050%20Nguy%E1%BB%85n%20Xu%C3%A2n%20Kh%C3%A1nh%2025bc5e6f95bd8065a36cfdc1df13ad63.html">45.5/50: Nguyễn Xuân Khánh</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-808c-953c-feafaf5e5732" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/42%2050%20Nguy%E1%BB%85n%20V%C4%83n%20Nh%C3%A2n%2025bc5e6f95bd808c953cfeafaf5e5732.html">42/50: Nguyễn Văn Nhân</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80d1-a258-fca779369213" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/42%2050%20Nguy%E1%BB%85n%20Gi%C3%A1ng%20My%2025bc5e6f95bd80d1a258fca779369213.html">42/50: Nguyễn Giáng My</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-800e-949a-c61a1a239e17" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/43%205%2050%20Nguy%E1%BB%85n%20Th%E1%BB%8B%20H%E1%BA%A3o%2025bc5e6f95bd800e949ac61a1a239e17.html">43.5/50: Nguyễn Thị Hảo</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80b1-95af-e8d34a0cac0a" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/43%205%2050%20%C3%94ng%20N%C4%83m%20Cam%2025bc5e6f95bd80b195afe8d34a0cac0a.html">43.5/50: Ông Năm Cam</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80f9-81b5-e23f4bb94af0" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/43%205%2050%20C%E1%BB%A5%20B%E1%BA%A3y%20Nam%2025bc5e6f95bd80f981b5e23f4bb94af0.html">43.5/50: Cụ Bảy Nam</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-8087-b4e4-fc22e7a4eec2" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/43%205%2050%20Th%E1%BA%A7y%20N%C4%83m%20C%C4%83n%2025bc5e6f95bd8087b4e4fc22e7a4eec2.html">43.5/50: Thầy Năm Căn</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-8024-9288-c205cd6f79df" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/44%205%2050%20C%E1%BB%A5%20Ba%20%C4%90%E1%BB%8Bnh%2025bc5e6f95bd80249288c205cd6f79df.html">44.5/50: Cụ Ba Định</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-800a-864f-ddd03766e57a" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/44%205%2050%20B%C3%A0%20S%C3%A1u%20T%C3%ADa%2025bc5e6f95bd800a864fddd03766e57a.html">44.5/50: Bà Sáu Tía</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80bf-980e-e5c7c0994aa8" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/44%2050%20Nguy%E1%BB%85n%20V%C4%83n%20Qu%E1%BA%BF%2025bc5e6f95bd80bf980ee5c7c0994aa8.html">44/50: Nguyễn Văn Quế</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-8094-86b3-c967576bfa03" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/44%2050%20B%C3%A0%20M%C6%B0%E1%BB%9Di%20H%E1%BA%A1nh%2025bc5e6f95bd809486b3c967576bfa03.html">44/50: Bà Mười Hạnh</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-80ee-97c6-c90edc9b9ba9" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/42%205%2050%20Nguy%E1%BB%85n%20V%C4%83n%20D%C5%A9ng%2025bc5e6f95bd80ee97c6c90edc9b9ba9.html"> 42.5/50: Nguyễn Văn Dũng</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-808f-b686-fdb1e531cf0e" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/44%2050%20Th%E1%BA%A7y%20Nam%20H%E1%BA%A3i%2025bc5e6f95bd808fb686fdb1e531cf0e.html">44/50: Thầy Nam Hải</a></figure></div><div style="display:contents" dir="ltr"><figure id="25bc5e6f-95bd-803f-8565-f68f448e4571" class="link-to-page"><a href="Mapped%20Taxonomy%20of%20Vietnamese%20Energetic%20Practition/38%205%2050%20Ph%E1%BA%A1m%20V%C4%83n%20H%C6%B0ng%2025bc5e6f95bd803f8565f68f448e4571.html">38.5/50: Phạm Văn Hưng</a></figure></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
