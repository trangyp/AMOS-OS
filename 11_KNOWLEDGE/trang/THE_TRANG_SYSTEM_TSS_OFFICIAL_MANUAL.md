---
tags: [trang]
---
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>The Trang System™ (TSS) – Official Manual</title><style>
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
	
</style></head><body><article id="2b1c5e6f-95bd-809a-b7b0-d07e1a7d665e" class="page sans"><header><h1 class="page-title" dir="auto"><strong>The Trang System™ (TSS) – Official Manual</strong></h1><p class="page-description" dir="auto"></p></header><div class="page-body"><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-801f-96bd-cb35a740906f" class="">The Trang System™ (TSS) is a universal structural framework for understanding how human-linked systems evolve. From families and organizations to states and civilizations, TSS provides a shared language for describing why systems grow, why they destabilize, and how they ultimately renew or collapse. TSS is not a theory tied to any ideology, time period, or culture. Instead, it identifies the structural forces that operate in every system shaped by human cooperation, conflict, and decision-making. It translates these forces into a compact architecture of four variables, seven developmental cycles, and four long-term outcomes. This architecture allows researchers, policymakers, analysts, and institutions to evaluate system health, anticipate transitions, and design interventions with clarity and precision.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-803f-9128-e440c3990977" class=""><strong>1. Purpose of the Trang System™</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80fd-8027-d5cc33439019" class="">The purpose of TSS is to provide a unified, science-based model to interpret system behaviour across scales. Traditional disciplines offer valuable but partial views: economics studies markets, political science studies governments, sociology studies groups, and history studies events. TSS integrates these perspectives by identifying the structural patterns that repeat across all systems. It answers five fundamental questions that matter for long-term stability and governance:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-806d-8ecc-dd8216e1cacd" class="">What stage of development is this system in?</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8043-999d-c4a8a1fc31ed" class="">What forces are strengthening or weakening it?</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8042-81be-d6fe3cd2698f" class="">Is it stabilizing, drifting, or destabilizing?</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8070-b438-e668ea8cbb93" class="">What structural futures are possible or impossible?</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8056-8497-c2b70cd68522" class="">What actions can meaningfully change its direction?</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80fc-83b1-d5a33d5ff2ac" class="">TSS supports responsible governance by helping leaders avoid misinterpretation of surface events and instead focus on underlying structural realities.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8096-b528-cbd6ec423aaa" class=""><strong>2. The Structural Foundations of TSS</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8061-81cf-e80c1b5e42c3" class="">TSS is built on three finite sets:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80e9-b4a9-df2cbfd78ad2" class=""><strong>Four structural variables</strong> that define the internal and external pressures acting on a system.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a0-a319-f3acce31fa77" class=""><strong>Seven structural cycles</strong> describing the universal development path.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a3-aad5-f8bbecba516c" class=""><strong>Four long-term outcomes</strong> representing all possible endings a system can experience.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80e6-b5c5-eb73b37e2272" class="">These sets are complete and exhaustive. Every known system maps into them without requiring extra categories.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-809c-8053-f0575fdefd1f" class=""><strong>3. The Four Universal Variables</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-805f-8bb0-fddd30008bb8" class="">The four variables of TSS—Overload (Ω), Cohesion (H), Fragmentation (F), and Shocks (S)—capture the essential forces shaping system behaviour. They apply equally to individuals, organizations, governments, and civilizations.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-8059-991b-fbb3dd4bf546" class=""><strong>3.1 Overload (Ω)</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-805d-89b9-fc6e55ff5621" class="">Overload represents the degree to which a system is asked to handle more than its capacity allows. It includes administrative burden, economic pressure, institutional complexity, demographic strain, environmental limits, and informational overload. Systems with low overload have flexibility and buffer space. Systems with high overload become brittle and vulnerable. Rising overload moves systems toward overreach (C3), fragmentation (C4), and crisis (C5).</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-80d0-857b-e1b11cc05e41" class=""><strong>3.2 Cohesion (H)</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-800e-8f6f-c2b4dd25ae5b" class="">Cohesion measures internal unity: trust, shared identity, legitimacy of leadership, and willingness to cooperate. Cohesion is a stabilizing force. High cohesion enables systems to withstand shocks and respond to challenges. Low cohesion erodes collective action, reduces resilience, and increases the risk of internal conflict. Cohesion acts as the main protective buffer against overload and shocks.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-80d0-8d82-ee3be1cec601" class=""><strong>3.3 Fragmentation (F)</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-801c-b158-f686f946c381" class="">Fragmentation refers to internal division into competing subgroups, factions, or parallel structures. Fragmentation may be political, social, organizational, regional, or ideological. Low fragmentation means disagreements are manageable within a shared identity. High fragmentation means the system behaves as multiple semi-independent units, making coordination difficult. Fragmentation magnifies the effects of overload and shocks.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-807e-9a00-fd1d22a7aca0" class=""><strong>3.4 Shocks (S)</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-801f-9cda-d2551259f371" class="">Shocks are disruptive events that force rapid adaptation or reveal hidden weaknesses. They may come from external forces such as wars, global economic crises, pandemics, or climate shocks. They may also come from internal failures such as leadership collapse, institutional breakdown, corruption scandals, or sudden policy shifts. The severity and frequency of shocks influence whether the system can remain in its current cycle or is forced into crisis or collapse.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-8017-8edc-f123f700145e" class=""><strong>3.5 Why These Variables Are Sufficient</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80c2-8ae1-f07f6b094d81" class="">All surface-level events ultimately translate into changes in Ω, H, F, or S. Political shifts change cohesion and fragmentation. Economic pressure increases overload. Cultural conflict increases fragmentation. Environmental stress and geopolitical competition increase shocks. TSS deliberately abstracts away surface categories to focus on their structural effects.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80ee-9d35-f0f8ff254a00" class=""><strong>4. The Seven Cycles of System Evolution</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8013-9df3-ff263b2987c4" class="">Systems evolve according to seven universal cycles. The duration of each may vary, but the order is consistent across history and scale.</p></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-80b3-80b9-c4e738fa2a09" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8000-86a1-df14413f927b"><th id="x@RE" class="simple-table-header-color simple-table-header"><strong>Cycle</strong></th><th id="_mvy" class="simple-table-header-color simple-table-header"><strong>Description</strong></th><th id="&lt;&lt;Xs" class="simple-table-header-color simple-table-header"><strong>Structural Pattern</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-808f-aa50-d13e2fc76ca7"><td id="x@RE" class="">C1 Emergence</td><td id="_mvy" class="">System forms with a unified core</td><td id="&lt;&lt;Xs" class="">Ω low, H high, F low, S low</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80ce-82e0-d416a13754e8"><td id="x@RE" class="">C2 Expansion</td><td id="_mvy" class="">System grows in size and complexity</td><td id="&lt;&lt;Xs" class="">Ω rising, H strong, F manageable</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-809d-aa39-c00cad90c79a"><td id="x@RE" class="">C3 Peak &amp; Overreach</td><td id="_mvy" class="">Maximum strength combined with rising strain</td><td id="&lt;&lt;Xs" class="">Ω high, H falling, F rising</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-807d-8999-e2bc94e16c76"><td id="x@RE" class="">C4 Fragmentation</td><td id="_mvy" class="">The system splits internally</td><td id="&lt;&lt;Xs" class="">Ω high, H low, F high</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8040-b1c9-ee6c80c2e347"><td id="x@RE" class="">C5 Crisis–Shock</td><td id="_mvy" class="">Major stress forces structural confrontation</td><td id="&lt;&lt;Xs" class="">S high, F high, H unstable</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-806e-bce6-f16c230e07d1"><td id="x@RE" class="">C6 Collapse</td><td id="_mvy" class="">Old model fails; authority and structure break down</td><td id="&lt;&lt;Xs" class="">Ω unsustainable, F extreme</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8029-aeb8-d3566aac0d7c"><td id="x@RE" class="">C7 Reset</td><td id="_mvy" class="">A new structure emerges and stabilizes</td><td id="&lt;&lt;Xs" class="">Ω reducing, H rising, F decreasing</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-806c-a4c5-c18ae0984945" class=""><strong>4.1 C1 – Emergence</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80da-a504-c2644f026ada" class="">A system is founded, typically by a small aligned leadership group. Cohesion is strong, complexity is low, and identity is clear. Early decisions shape long-term direction.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-80a2-ab47-df5a08710a21" class=""><strong>4.2 C2 – Expansion</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80d1-994d-f60a316f2306" class="">The system grows through success, increased capacity, and rising legitimacy. Operations expand, complexity increases, and new members join. Overload begins rising slowly.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-806a-aca3-ff55773f9bba" class=""><strong>4.3 C3 – Peak &amp; Overreach</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-809e-8bee-e263df4b49c0" class="">The system reaches peak capability and becomes overstretched. Decision-making slows, institutions strain, and efficiency declines. Cohesion weakens as different groups experience pressure differently.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-8004-a75b-ee5dad53fddd" class=""><strong>4.4 C4 – Fragmentation</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-805e-a586-e5253c2ee6f2" class="">Internal divisions widen. Rival factions, regions, or departments act independently or competitively. Coordination becomes difficult. The system has lost its shared identity and struggles to respond to stress.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-8004-af0a-e8542714fe80" class=""><strong>4.5 C5 – Crisis–Shock</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8096-891f-d3d65c3458d6" class="">A major crisis exposes underlying fragility. Shocks may be external (war, recession, pandemic) or internal (scandal, legitimacy failure). The system must choose between transformation or decline.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-8064-b94d-c51816a9943f" class=""><strong>4.6 C6 – Collapse</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8071-86e4-fc2813fb78cd" class="">The previous operating model loses authority and functionality. Institutions fail or lose relevance. The system may continue physically but not structurally. Collapse is the end of the old model, not necessarily the end of the system’s existence.</p></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-8096-8b1a-ce18abd52c41" class=""><strong>4.7 C7 – Reset</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8041-b4a6-d7407973ed9c" class="">The system builds a new model, often with new leadership, rules, and identity. Overload decreases, cohesion strengthens, and fragmentation declines. This cycle leads back into C1 and C2.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8001-86dc-fb07cce103e6" class=""><strong>5. The Four Long-Term Outcomes</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80d7-94fb-cc2c1bdb79ae" class="">Systems end in one of four structural outcomes. These outcomes are mutually exclusive and collectively exhaustive across all historical cases.</p></div><div style="display:contents" dir="ltr"><table id="2b1c5e6f-95bd-800a-91e7-c7a53869542d" class="simple-table"><thead class="simple-table-header"><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80d5-bc02-d6be58b618f5"><th id="oO_S" class="simple-table-header-color simple-table-header"><strong>Outcome</strong></th><th id="kkBd" class="simple-table-header-color simple-table-header"><strong>Meaning</strong></th><th id="}puJ" class="simple-table-header-color simple-table-header"><strong>Description</strong></th></tr></div></thead><tbody><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80da-9e20-cb01601ac977"><td id="oO_S" class="">Renewal (R)</td><td id="kkBd" class="">System rebuilds</td><td id="}puJ" class="">A new model emerges with continuity</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8032-be62-f73e89e49de2"><td id="oO_S" class="">Termination (T)</td><td id="kkBd" class="">System ends</td><td id="}puJ" class="">It ceases to exist as an independent actor</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-80fc-b9b6-f038d0cc5f75"><td id="oO_S" class="">Absorption (A)</td><td id="kkBd" class="">System joins another</td><td id="}puJ" class="">It becomes part of a larger system</td></tr></div><div style="display:contents" dir="ltr"><tr id="2b1c5e6f-95bd-8072-9f41-faa8d34473b2"><td id="oO_S" class="">Stagnation (Sg)</td><td id="kkBd" class="">System freezes</td><td id="}puJ" class="">It persists in a low-change, low-growth state</td></tr></div></tbody></table></div><div style="display:contents" dir="auto"><h3 id="2b1c5e6f-95bd-80fb-baa0-d8a33edb44a3" class=""><strong>5.1 Why Only Four Outcomes Exist</strong></h3></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8089-88b6-c015b52e137f" class="">Across thousands of years of history, no additional structurally distinct ending has consistently appeared. All endings can be categorized into these four. Renewal creates a new cycle. Termination ends the cycle permanently. Absorption merges the system into a larger one. Stagnation freezes the system in a low-mobility equilibrium.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80a9-b3c7-ce6117142c79" class=""><strong>6. How Variables Interact (Structural Mechanics)</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-803d-bc0d-d3fcd1ac48ac" class="">Overload raises risk by increasing demands on limited capacity. Cohesion counters risk by enabling coordinated action. Fragmentation amplifies risk by weakening collective response. Shocks trigger transitions by exposing structural weaknesses. Risk arises when Ω rises faster than capacity, H declines due to legitimacy loss, F rises due to conflict, and S intensifies through external or internal disturbances. Stability arises when Ω is controlled, H is strengthened, F is reduced, and S is managed or buffered.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80b8-b0e0-c362523aca6c" class=""><strong>7. System Drift</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8022-b7d2-c65de214245d" class="">Systems naturally drift toward:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8067-a01b-d66e41ed7ce4" class="">Higher overload (because responsibilities grow faster than capacity).</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8035-b59c-d046ec185ba4" class="">Lower cohesion (as diversity and complexity increase).</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8086-b1c1-d856defa81ac" class="">Higher fragmentation (due to power shifts and specialization).</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-803b-8fd7-dd4c4c6d1bcc" class="">Higher shock exposure (due to interconnectedness and global dependencies).</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80ab-a155-dad1ccbe8fbe" class="">This drift explains why long-term stability is rare without intentional interventions. TSS highlights that decay is not moral failure but a structural consequence of scale and complexity.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8060-b1d9-c5fc24eec3ca" class=""><strong>8. Intervening to Change System Trajectories</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80e1-b271-e00d119db60c" class="">Interventions are effective when they change the direction of structural variables. Examples include:</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8039-b475-edda82296039" class="">Reducing overload by simplifying bureaucracy, increasing capacity, or adjusting expectations.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80d0-90b1-d286b8252c47" class="">Increasing cohesion through fair governance, transparent communication, and shared narratives.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-803f-9557-fc2719762893" class="">Reducing fragmentation by reconciling interests, aligning incentives, or restructuring institutions.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-807b-81e7-ed6383906ef0" class="">Managing shocks by building resilience, creating buffers, and anticipating external risks.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8022-9eaf-e2fbe759764d" class="">Successful interventions often target multiple variables simultaneously.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-808a-84e7-fe0af400e7ad" class=""><strong>9. TSS Across Human Scales</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8025-a9fa-d4c5c89011a0" class="">TSS works consistently at different scales because structural forces manifest similarly across them.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8096-9093-d71fc3a31888" class="">Individuals experience overload as stress, cohesion as internal clarity, fragmentation as conflicting identities, and shocks as life events.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8015-8ecd-c615a0f2b826" class="">Organizations experience overload as excessive workload, fragmentation as departmental conflict, and shocks as market or leadership disruptions.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-8039-9030-e499bf2b0de3" class="">Governments experience overload as fiscal and administrative strain, fragmentation as political polarization, and shocks as crises.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80c6-b71c-c1064985527c" class="">Civilizations experience overload as resource and demographic pressure, fragmentation as competing blocs, and shocks as climate or technological change.</p></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-809e-b82a-c1ae5416f85d" class="">The same structural logic applies everywhere.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-8002-8874-f2efafb4d959" class=""><strong>10. TSS and Predictive Analysis (Relationship to TPE)</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80cf-b01c-c7b8afa3f5ce" class="">TSS provides the structural map. TPE interprets this map to forecast system trajectories. TPE identifies which cycles a system is moving toward, evaluates risk based on variable trends, and models cascading outcomes. TSS ensures predictions remain grounded in structure rather than speculation.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80e4-bae7-e9d7e674abe6" class=""><strong>11. Scientific Boundaries</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-805e-b96e-c29d90641307" class="">TSS does not predict precise dates or individual behaviours. It respects scientific uncertainty by focusing on structural patterns that can be reliably predicted. It is suitable for governance, institutional design, and long-term planning but must be applied responsibly.</p></div><div style="display:contents" dir="auto"><h2 id="2b1c5e6f-95bd-80e9-b7f5-f8e50e2d9a07" class=""><strong>12. Summary</strong></h2></div><div style="display:contents" dir="auto"><p id="2b1c5e6f-95bd-80a0-8849-ea6b08063e77" class="">The Trang System™ is a comprehensive framework that explains the dynamics of human-linked systems through a universal structure. With four variables, seven developmental cycles, and four possible outcomes, it provides clarity and coherence to understanding how systems evolve. TSS creates a shared language accessible to analysts, policymakers, and researchers across disciplines. It enables structural understanding that supports prediction, decision-making, crisis prevention, and sustainable long-term governance.</p></div><div style="display:contents" dir="auto"><hr id="2b1c5e6f-95bd-80c0-9810-f4f7009e8e96"/></div></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
