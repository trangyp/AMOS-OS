---
tags: [misc]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Driver interview</title><style>
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
	
</style></head><body><article id="291c5e6f-95bd-805e-8278-ffd493443103" class="page sans"><header><h1 class="page-title" dir="auto">Driver interview</h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-8013-b0ec-c546f290a355" class="">Awesome — here’s a paste-ready spec for <strong>both</strong> the embedded <strong>Chat Widget</strong> and the <strong>Full Chat Window</strong>, including <strong>Lovable component props</strong>, <strong>API contracts</strong>, <strong>DB schema</strong>, <strong>security/anti-cheat</strong>, and <strong>sample payloads</strong>. You can hand this to devs and build immediately.</p></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-80a8-a66c-c8f1f2490b88"/></div><div style="display:contents" dir="auto"><h1 id="291c5e6f-95bd-801c-aac8-c3bd339e8884" class="">1) Components &amp; Props (Lovable)</h1></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-80af-b6fc-fc480ade3062" class="">A) <code>&lt;ChatWidget /&gt;</code> (Stage-2 screening; 3–5 Qs, text-only)</h2></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-8074-9b63-c201465bdf87" class=""><strong>Usage (on </strong><code><strong>/apply</strong></code><strong>)</strong></p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="291c5e6f-95bd-80ec-a047-c705b3f70773" class="code code-wrap"><code class="language-JavaScript" style="white-space:pre-wrap;word-break:break-all">&lt;ChatWidget
  sessionId={sessionId}                // string (uuid v4)
  userId={userId}                      // string (uuid v4)
  jobId={jobId}                        // e.g., &quot;driver-f1&quot;
  questionCount={3}                    // 3 or 5
  locale=&quot;vi&quot;                          // &quot;vi&quot; | &quot;en&quot;
  kbTags={[&quot;sop_safety&quot;,&quot;policy_offapp&quot;,&quot;lost_found&quot;,&quot;ev_charging&quot;]}
  consentUrl=&quot;/privacy&quot;
  onStart={(meta) =&gt; logStart(meta)}
  onAnswer={(payload) =&gt; saveAnswer(payload)}
  onFinish={(result) =&gt; routeTo(&#x27;/apply/result&#x27;, result)}
/&gt;
</code></pre></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-8054-b18f-ff8b3cd0c67e" class=""><strong>Required behaviour</strong></p></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80a7-8b34-c5e165a2c8d1" class="bulleted-list"><li style="list-style-type:disc">Docked bottom-right (desktop width 360–420px; mobile 90% width).</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8040-8697-c24456fca3eb" class="bulleted-list"><li style="list-style-type:disc">Steps: <strong>Intro → Q1 → Q2 → Q3 → Summary</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8070-a078-c416a76121e6" class="bulleted-list"><li style="list-style-type:disc">Show progress “Câu x/3”, timer soft-limit 40s/câu.</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8008-87f0-c8cccdd8f430" class="bulleted-list"><li style="list-style-type:disc">Auto-save draft per answer.</li></ul></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-80d8-a25c-d055edc245a0"/></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-80f2-b993-f7c49f687dd7" class="">B) <code>&lt;ChatWindow /&gt;</code> (deep interviews, audio add-ons)</h2></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-80df-acd6-d3624553edb7" class=""><strong>Usage (on </strong><code><strong>/apply/chat</strong></code><strong>)</strong></p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="291c5e6f-95bd-80e9-882d-dab6299cb599" class="code code-wrap"><code class="language-JavaScript" style="white-space:pre-wrap;word-break:break-all">&lt;ChatWindow
  sessionId={sessionId}
  userId={userId}
  jobId={jobId}
  modules={[
    {type:&quot;text&quot;, questions:5},
    {type:&quot;audio&quot;, prompts:3, stt:true}
  ]}
  locale=&quot;vi&quot;
  kbTags={[&quot;sop_night&quot;,&quot;harassment&quot;,&quot;cx_apology&quot;,&quot;ev_faults&quot;]}
  onStart={logStart}
  onAnswer={saveAnswer}
  onFinish={(r)=&gt; routeTo(&#x27;/apply/result&#x27;, r)}
/&gt;
</code></pre></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-805a-8d84-d73654ab8e05" class=""><strong>Required behaviour</strong></p></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80e2-89c5-fc98d00f21b4" class="bulleted-list"><li style="list-style-type:disc">Full screen, left: messages; right: <strong>SOP cards</strong> (read-only RAG snippets).</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8058-a77b-e82e659b2fd8" class="bulleted-list"><li style="list-style-type:disc">Allow attachments (optional) for roleplay evidence.</li></ul></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-80ad-8b02-e26a149ce63f"/></div><div style="display:contents" dir="auto"><h1 id="291c5e6f-95bd-8016-b856-c69ed83dd20f" class="">2) API Contracts (all JSON over HTTPS)</h1></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-8035-8248-f86f4d3bd89f" class="">Base path: <code>/api/agent/*</code></p></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-80bd-bf6c-c9c6b88cd1f4" class="">2.1 Start / resume</h2></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-80ca-8164-d18778475773" class=""><strong>POST</strong> <code>/api/agent/start</code></p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="291c5e6f-95bd-80de-9b44-dded65efc90e" class="code code-wrap"><code class="language-JSON" style="white-space:pre-wrap;word-break:break-all">{
  &quot;session_id&quot;: &quot;uuid&quot;,
  &quot;user_id&quot;: &quot;uuid&quot;,
  &quot;job_id&quot;: &quot;driver-f1&quot;,
  &quot;locale&quot;: &quot;vi&quot;,
  &quot;question_count&quot;: 3,
  &quot;kb_tags&quot;: [&quot;sop_safety&quot;,&quot;policy_offapp&quot;]
}
</code></pre></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-80af-a47c-ecdf282dc39f" class=""><strong>Response</strong></p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="291c5e6f-95bd-8046-88a2-ffedd8c962a0" class="code code-wrap"><code class="language-JSON" style="white-space:pre-wrap;word-break:break-all">{
  &quot;ok&quot;: true,
  &quot;session_token&quot;: &quot;jwt-short&quot;,
  &quot;questions&quot;: [
    {&quot;id&quot;:&quot;q_safety_rain&quot;,&quot;text&quot;:&quot;Trời mưa lớn, khách giục chạy nhanh. Bạn xử lý thế nào?&quot;},
    {&quot;id&quot;:&quot;q_policy_offapp&quot;,&quot;text&quot;:&quot;Khách xin đi ngoài app để rẻ hơn, bạn làm gì?&quot;},
    {&quot;id&quot;:&quot;q_lost_found&quot;,&quot;text&quot;:&quot;Khách báo quên ví sau 1 giờ. Quy trình của bạn?&quot;}
  ]
}
</code></pre></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-808b-9659-dfb745a7533c" class="">2.2 Send answer → AI grade</h2></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-80ab-adb3-c53dc0847366" class=""><strong>POST</strong> <code>/api/agent/grade</code></p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="291c5e6f-95bd-80df-a91c-d20acf11be8e" class="code code-wrap"><code class="language-JSON" style="white-space:pre-wrap;word-break:break-all">{
  &quot;session_id&quot;: &quot;uuid&quot;,
  &quot;session_token&quot;: &quot;jwt-short&quot;,
  &quot;question_id&quot;: &quot;q_safety_rain&quot;,
  &quot;answer_text&quot;: &quot;Em xin phép giải thích... giữ an toàn...&quot;,
  &quot;meta&quot;: {
    &quot;elapsed_ms&quot;: 24000,
    &quot;paste_chars&quot;: 0,
    &quot;device&quot;: &quot;mobile&quot;
  }
}
</code></pre></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-80a0-9bed-eed087d4685b" class=""><strong>Response</strong></p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="291c5e6f-95bd-8035-b258-e2d21ddd6fed" class="code code-wrap"><code class="language-JSON" style="white-space:pre-wrap;word-break:break-all">{
  &quot;scores&quot;: {&quot;safety&quot;:4,&quot;integrity&quot;:5,&quot;empathy&quot;:4,&quot;ops&quot;:4,&quot;language&quot;:4},
  &quot;total&quot;: 21,
  &quot;rationale&quot;: &quot;Đúng SOP mưa, từ chối chạy nhanh, giải thích lịch sự.&quot;,
  &quot;red_flag&quot;: false,
  &quot;next&quot;: {&quot;question_id&quot;:&quot;q_policy_offapp&quot;}
}
</code></pre></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-8042-8bfe-d719c0a4e810" class="">2.3 Finish interview</h2></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-80f2-9924-ce7735612bc1" class=""><strong>POST</strong> <code>/api/agent/finish</code></p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="291c5e6f-95bd-808c-94b6-ff9fbbd2b8e1" class="code code-wrap"><code class="language-JSON" style="white-space:pre-wrap;word-break:break-all">{
  &quot;session_id&quot;: &quot;uuid&quot;,
  &quot;session_token&quot;: &quot;jwt-short&quot;
}
</code></pre></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-803a-8fb5-d5b00ff30a39" class=""><strong>Response</strong></p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="291c5e6f-95bd-8015-8852-f4125d12dd6c" class="code code-wrap"><code class="language-JSON" style="white-space:pre-wrap;word-break:break-all">{
  &quot;band&quot;: &quot;B&quot;,
  &quot;total&quot;: 63,
  &quot;red_flags&quot;: 0,
  &quot;summary&quot;: &quot;Vững SOP, chính trực, cần cải thiện chi tiết EV.&quot;,
  &quot;decision&quot;: &quot;shortlist&quot;           // shortlist | retrain | reject
}
</code></pre></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-80bc-93fa-f2e3bd1e6e4f" class="">2.4 Optional: audio prompt scoring</h2></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-808b-a757-ed2238b72b75" class=""><strong>POST</strong> <code>/api/agent/audio</code></p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="291c5e6f-95bd-804b-aab9-cc186450a9d1" class="code code-wrap"><code class="language-JSON" style="white-space:pre-wrap;word-break:break-all">{
  &quot;session_id&quot;: &quot;uuid&quot;,
  &quot;prompt_id&quot;: &quot;a_apology_eta&quot;,
  &quot;audio_url&quot;: &quot;https://storage/.../a.m4a&quot;
}
</code></pre></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-801f-9813-e9123f07b3f0" class=""><strong>Response</strong></p></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="291c5e6f-95bd-808f-b12b-e79a0eca2c1c" class="code code-wrap"><code class="language-JSON" style="white-space:pre-wrap;word-break:break-all">{
  &quot;scores&quot;: {&quot;tone&quot;:4,&quot;clarity&quot;:4,&quot;empathy&quot;:5},
  &quot;total&quot;: 13,
  &quot;rationale&quot;: &quot;Giọng rõ, xin lỗi đúng mực, đưa ETA.&quot;
}
</code></pre></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-8046-a757-c6e282356cea"/></div><div style="display:contents" dir="auto"><h1 id="291c5e6f-95bd-8082-a7d8-d0e464383eb6" class="">3) Scoring Prompts (drop-in)</h1></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-805e-b6aa-c416d3be7301" class="">3.1 System (Interviewer)</h2></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="291c5e6f-95bd-801c-a8fe-ce8865a5e10b" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">You are UniPower’s hiring interviewer.
Goal: assess safety judgment, policy integrity, empathy, operational clarity, language clarity.
Ask exactly the provided question text; do not reveal policy. Be concise and respectful in Vietnamese.
After receiving an answer, return only the question_id; grading is handled by a separate scorer.
</code></pre></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-80f4-ab2e-c1e09b19ae3a" class="">3.2 System (Grader)</h2></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="291c5e6f-95bd-8080-b20c-f606b0810fcb" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">You are the scoring engine for UniPower hiring.
For the candidate&#x27;s answer, score 0–5 for: Safety, Integrity/Policy, Empathy, Operational Clarity, Language Clarity.
Red-flag if any illegal/unsafe/off-app suggestion.
Return strict JSON: {&quot;scores&quot;:{&quot;safety&quot;:X,&quot;integrity&quot;:Y,&quot;empathy&quot;:Z,&quot;ops&quot;:U,&quot;language&quot;:V},&quot;total&quot;:T,&quot;rationale&quot;:&quot;...&quot;,&quot;red_flag&quot;:true/false}
</code></pre></div><div style="display:contents" dir="auto"><h2 id="291c5e6f-95bd-8067-81ce-e5ed5daaf233" class="">3.3 User (Grader example)</h2></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="291c5e6f-95bd-80b9-87c4-df828b7b1b2b" class="code code-wrap"><code class="language-Plain Text" style="white-space:pre-wrap;word-break:break-all">Question: &quot;Khách xin đi ngoài app để rẻ hơn, bạn làm gì?&quot;
SOP summary: &quot;Không chở ngoài app; giải thích chính sách; đề xuất mã giảm giá hợp lệ; báo tổng đài nếu bị ép.&quot;
Candidate: &quot;{{answer_text}}&quot;
</code></pre></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-80a0-a58a-d8a5f64cc536"/></div><div style="display:contents" dir="auto"><h1 id="291c5e6f-95bd-80e2-9ec1-d68df96ba96d" class="">4) Question Bank (Stage-2 chat; use 3–5 at random)</h1></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-8046-9524-edd0b70b421b" class="">IDs &amp; texts (exactly as referenced above):</p></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8069-bf86-f98eec0edcb7" class="bulleted-list"><li style="list-style-type:disc"><code>q_safety_rain</code>: Trời mưa lớn, khách giục chạy nhanh. Bạn xử lý thế nào?</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8024-84d9-da3f00a3a02b" class="bulleted-list"><li style="list-style-type:disc"><code>q_policy_offapp</code>: Khách xin đi ngoài app để rẻ hơn, bạn làm gì?</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80e3-afce-ef18253d3975" class="bulleted-list"><li style="list-style-type:disc"><code>q_lost_found</code>: Khách báo quên ví sau 1 giờ. Quy trình của bạn?</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80ce-a59c-efd22fe686d6" class="bulleted-list"><li style="list-style-type:disc"><code>q_ev_overheat</code>: Đến trạm sạc báo quá nhiệt. Bạn xử lý ra sao?</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8025-a727-c165acceb6d6" class="bulleted-list"><li style="list-style-type:disc"><code>q_cx_late</code>: Bạn đến muộn 7 phút vì kẹt xe. Bạn nhắn gì cho khách?</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80f9-b282-d8315e80200e" class="bulleted-list"><li style="list-style-type:disc"><code>q_energy_12</code>: SOC 12%, trạm gần nhất 7km và có dốc. Kế hoạch của bạn?</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80ab-9f3d-c5603739bcf9" class="bulleted-list"><li style="list-style-type:disc">(Window can include more: harassment/night safety, disability support, etc.)</li></ul></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-80ab-9d1f-c186efd69a98"/></div><div style="display:contents" dir="auto"><h1 id="291c5e6f-95bd-8005-9695-fd73a7b5025b" class="">5) DB Schema (minimal)</h1></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-805d-b522-db1f19913256" class=""><strong>agent_sessions</strong></p></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-8086-9df8-fdc401cb71ab" class=""><code>id, user_id, job_id, locale, status(started|finished), started_at, finished_at, session_token_hash</code></p></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-806b-b551-fb45e7c6318b" class=""><strong>agent_questions</strong></p></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-805a-b7bc-cb457c564447" class=""><code>id, session_id, question_id, order_idx, asked_at, answered_at, answer_text, elapsed_ms, paste_chars</code></p></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-804e-89e4-d91c8685df57" class=""><strong>agent_scores</strong></p></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-80d1-8d24-d9e405c60375" class=""><code>id, session_id, question_id, safety, integrity, empathy, ops, language, total, red_flag, rationale</code></p></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-8032-955f-f3029f7b5e75" class=""><strong>agent_summary</strong></p></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-802e-9b31-cc73dd9f4a05" class=""><code>session_id, total, red_flags, band, decision, created_at</code></p></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-805b-a969-e846b7e88ea0" class=""><strong>audit_logs</strong></p></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-80b8-b2a9-cb6092acc4f5" class=""><code>id, actor, action, resource, ip, ua, payload_json, created_at</code></p></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-8016-8fdb-cec9aa2a0bd0"/></div><div style="display:contents" dir="auto"><h1 id="291c5e6f-95bd-8082-9c18-ecac0bff92db" class="">6) Decision Logic</h1></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80cd-8087-c0a10151c4ec" class="bulleted-list"><li style="list-style-type:disc"><strong>Per-answer</strong>: compute total (0–25).</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80f6-b6ff-c016d734cad9" class="bulleted-list"><li style="list-style-type:disc"><strong>Interview total</strong>: sum of questions (e.g., 3 Qs → max 75).</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8055-a713-f1550c5a11c1" class="bulleted-list"><li style="list-style-type:disc"><strong>Banding</strong> (recommended):<div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8021-a3e5-fa0e6409b583" class="bulleted-list"><li style="list-style-type:circle">A ≥ 65 → <strong>shortlist</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8094-8e5a-e87b4724e5c7" class="bulleted-list"><li style="list-style-type:circle">B 55–64 → <strong>shortlist</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8053-84c5-e98d5f0a09d0" class="bulleted-list"><li style="list-style-type:circle">C 45–54 → <strong>retrain</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8002-af63-ed6eb750e5df" class="bulleted-list"><li style="list-style-type:circle">D &lt; 45 → <strong>reject</strong></li></ul></div></li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-800d-8455-c40b2c90c1dd" class="bulleted-list"><li style="list-style-type:disc"><strong>Hard rules</strong>:<div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8021-8741-e76385ff384a" class="bulleted-list"><li style="list-style-type:circle">If <code>red_flag == true</code> for any answer → <strong>reject</strong></li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80c5-b2e7-f2e9456ed7d2" class="bulleted-list"><li style="list-style-type:circle">If <code>paste_chars &gt; 800</code> or <code>elapsed_ms &lt; 3s</code> → mark <code>suspicious = true</code> (manual review)</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-8017-b5dd-c730dc79f38c"/></div><div style="display:contents" dir="auto"><h1 id="291c5e6f-95bd-804d-b691-e84685f667ce" class="">7) Security &amp; Anti-Cheat</h1></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80bb-a673-c9212f7350cb" class="bulleted-list"><li style="list-style-type:disc"><strong>JWT (short-lived)</strong> per session; rotate every API call.</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80ea-88a3-ec893afc3a84" class="bulleted-list"><li style="list-style-type:disc"><strong>Rate-limit</strong>: 1 req/sec per session; burst 5/10s.</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-801a-a741-e1992a1308ad" class="bulleted-list"><li style="list-style-type:disc">Strip PII before sending to scorer; store raw chat ≤ <strong>90 ngày</strong>.</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8076-9f39-c7c75a4801d9" class="bulleted-list"><li style="list-style-type:disc">Detect paste spikes, ultra-short responses, repetition (Levenshtein).</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80a5-a84a-d216a3b8c69f" class="bulleted-list"><li style="list-style-type:disc">Log consent (NĐ 13) and provide <strong>export/delete</strong> endpoint:<div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8020-ba11-ee91fff76dc1" class="bulleted-list"><li style="list-style-type:circle"><code>POST /api/privacy/export</code>, <code>POST /api/privacy/delete</code>.</li></ul></div></li></ul></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-807e-b745-f400054a24cc"/></div><div style="display:contents" dir="auto"><h1 id="291c5e6f-95bd-804a-bcad-e2d035a06293" class="">8) UI Strings (VN)</h1></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-8062-9952-ecd64484fd60" class="bulleted-list"><li style="list-style-type:disc">Intro: “Phỏng vấn nhanh (3 câu). Mục tiêu: đánh giá an toàn, trung thực và cách xử lý tình huống. Mỗi câu ~40 giây.”</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80c8-98f2-de99cdc7f9a9" class="bulleted-list"><li style="list-style-type:disc">Placeholder input: “Nhập câu trả lời của bạn…”</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80b8-8089-c816eba333ad" class="bulleted-list"><li style="list-style-type:disc">Next button: “Gửi &amp; tiếp tục”</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80e7-9b61-fb7ace6e21a8" class="bulleted-list"><li style="list-style-type:disc">Summary (pass): “Điểm tạm tính: {{score}} – Không có cảnh báo. Chọn lịch <strong>onboarding</strong>.”</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-806f-8363-ebd353fa1d5f" class="bulleted-list"><li style="list-style-type:disc">Summary (retrain): “Bạn cần học lại <strong>Module SOP</strong> và thi lại sau 7 ngày.”</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80f2-b7e8-ee2caa4333d0" class="bulleted-list"><li style="list-style-type:disc">Summary (reject): “Cảm ơn bạn. Bạn có thể ứng tuyển lại sau 30 ngày.”</li></ul></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-8069-b88d-ccba7ddd9a8a"/></div><div style="display:contents" dir="auto"><h1 id="291c5e6f-95bd-80db-977f-fb0589d7fd54" class="">9) Example Client Flow (Widget)</h1></div><div style="display:contents" dir="auto"><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="291c5e6f-95bd-8076-812c-c28d9f3533bf" class="code code-wrap"><code class="language-TypeScript" style="white-space:pre-wrap;word-break:break-all">// onStart
POST /api/agent/start -&gt; render Q1

// onAnswer
POST /api/agent/grade -&gt; store score, show next question

// onFinish
POST /api/agent/finish -&gt; show summary + CTA
</code></pre></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-80de-8024-cd9e7f9140d5"/></div><div style="display:contents" dir="auto"><h1 id="291c5e6f-95bd-80b2-a7b1-d2d356f59b2d" class="">10) Extension Hooks</h1></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-800a-aae5-ef7b2e166f0c" class="bulleted-list"><li style="list-style-type:disc"><strong>Audio step</strong> (leaders): call <code>/api/agent/audio</code>, merge 10% weight into total.</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-805e-bd05-cd3f26d57e19" class="bulleted-list"><li style="list-style-type:disc"><strong>RAG side panel</strong> (window): serve <code>/api/agent/kb?tags=...</code> read-only SOP snippets.</li></ul></div><div style="display:contents" dir="auto"><ul id="291c5e6f-95bd-80cd-bc53-df18252b779c" class="bulleted-list"><li style="list-style-type:disc"><strong>Analytics</strong>: emit events <code>agent.answer</code>, <code>agent.score</code>, <code>agent.finish</code> to your BI.</li></ul></div><div style="display:contents" dir="auto"><hr id="291c5e6f-95bd-80ed-957c-d54dabb1762e"/></div><div style="display:contents" dir="auto"><p id="291c5e6f-95bd-8065-b145-c56581c84081" class="">If you want, I can also prepare <strong>CSV/JSON</strong> for the question bank (IDs above) and a <strong>Postman collection</strong> for these endpoints so your team can import and run immediately.</p></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
