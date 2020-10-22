---
date: 2019-09-30
title: Jupyter Notebook Slideshow
tags: [Data Science]
featured-img: slides
img-type: jpg
summary: Example Exporting a Jupyter Notebook online as a slideshow for business presentations using the Facebook Performance Metrics Dataset.
github: https://github.com/pierpaolo28/Companies-Data-Science-Challenges/tree/master/Facebook%20Performance%20Metrics%20Dataset
---

<link
 rel="shortcut icon"
 href="../assets/img/icons/favicon.ico"
 type="image/x-icon"
/>
<title>Jupyter Notebook Slideshow | Pier Paolo Ippolito</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>

<!-- General and theme style sheets -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.5.0/css/reveal.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.5.0/css/theme/simple.css" id="theme">

<!-- If the query includes 'print-pdf', include the PDF print sheet -->
<script>
if( window.location.search.match( /print-pdf/gi ) ) {
        var link = document.createElement( 'link' );
        link.rel = 'stylesheet';
        link.type = 'text/css';
        link.href = 'https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.5.0/css/print/pdf.css';
        document.getElementsByTagName( 'head' )[0].appendChild( link );
}

</script>

<!--[if lt IE 9]>
<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.5.0/lib/js/html5shiv.js"></script>
<![endif]-->

<!-- Loading the mathjax macro -->
<!-- Load mathjax -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-AMS_HTML"></script>
<!-- MathJax configuration -->
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    tex2jax: {
        inlineMath: [ ['$','$'], ["\\(","\\)"] ],
        displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
        processEscapes: true,
        processEnvironments: true
    },
    // Center justify equations in code and markdown cells. Elsewhere
    // we use CSS to left justify single line equations in code cells.
    displayAlign: 'center',
    "HTML-CSS": {
        styles: {'.MathJax_Display': {"margin": 0}},
        linebreaks: { automatic: true }
    }
});
</script>
<!-- End of mathjax configuration -->

<!-- Get Font-awesome from cdn -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css">

<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.7.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.fa-pull-left {
  float: left;
}
.fa-pull-right {
  float: right;
}
.fa.fa-pull-left {
  margin-right: .3em;
}
.fa.fa-pull-right {
  margin-left: .3em;
}
/* Deprecated as of 4.4.0 */
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-feed:before,
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper-pp:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-resistance:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-y-combinator-square:before,
.fa-yc-square:before,
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-intersex:before,
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-genderless:before {
  content: "\f22d";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}
.fa-yc:before,
.fa-y-combinator:before {
  content: "\f23b";
}
.fa-optin-monster:before {
  content: "\f23c";
}
.fa-opencart:before {
  content: "\f23d";
}
.fa-expeditedssl:before {
  content: "\f23e";
}
.fa-battery-4:before,
.fa-battery:before,
.fa-battery-full:before {
  content: "\f240";
}
.fa-battery-3:before,
.fa-battery-three-quarters:before {
  content: "\f241";
}
.fa-battery-2:before,
.fa-battery-half:before {
  content: "\f242";
}
.fa-battery-1:before,
.fa-battery-quarter:before {
  content: "\f243";
}
.fa-battery-0:before,
.fa-battery-empty:before {
  content: "\f244";
}
.fa-mouse-pointer:before {
  content: "\f245";
}
.fa-i-cursor:before {
  content: "\f246";
}
.fa-object-group:before {
  content: "\f247";
}
.fa-object-ungroup:before {
  content: "\f248";
}
.fa-sticky-note:before {
  content: "\f249";
}
.fa-sticky-note-o:before {
  content: "\f24a";
}
.fa-cc-jcb:before {
  content: "\f24b";
}
.fa-cc-diners-club:before {
  content: "\f24c";
}
.fa-clone:before {
  content: "\f24d";
}
.fa-balance-scale:before {
  content: "\f24e";
}
.fa-hourglass-o:before {
  content: "\f250";
}
.fa-hourglass-1:before,
.fa-hourglass-start:before {
  content: "\f251";
}
.fa-hourglass-2:before,
.fa-hourglass-half:before {
  content: "\f252";
}
.fa-hourglass-3:before,
.fa-hourglass-end:before {
  content: "\f253";
}
.fa-hourglass:before {
  content: "\f254";
}
.fa-hand-grab-o:before,
.fa-hand-rock-o:before {
  content: "\f255";
}
.fa-hand-stop-o:before,
.fa-hand-paper-o:before {
  content: "\f256";
}
.fa-hand-scissors-o:before {
  content: "\f257";
}
.fa-hand-lizard-o:before {
  content: "\f258";
}
.fa-hand-spock-o:before {
  content: "\f259";
}
.fa-hand-pointer-o:before {
  content: "\f25a";
}
.fa-hand-peace-o:before {
  content: "\f25b";
}
.fa-trademark:before {
  content: "\f25c";
}
.fa-registered:before {
  content: "\f25d";
}
.fa-creative-commons:before {
  content: "\f25e";
}
.fa-gg:before {
  content: "\f260";
}
.fa-gg-circle:before {
  content: "\f261";
}
.fa-tripadvisor:before {
  content: "\f262";
}
.fa-odnoklassniki:before {
  content: "\f263";
}
.fa-odnoklassniki-square:before {
  content: "\f264";
}
.fa-get-pocket:before {
  content: "\f265";
}
.fa-wikipedia-w:before {
  content: "\f266";
}
.fa-safari:before {
  content: "\f267";
}
.fa-chrome:before {
  content: "\f268";
}
.fa-firefox:before {
  content: "\f269";
}
.fa-opera:before {
  content: "\f26a";
}
.fa-internet-explorer:before {
  content: "\f26b";
}
.fa-tv:before,
.fa-television:before {
  content: "\f26c";
}
.fa-contao:before {
  content: "\f26d";
}
.fa-500px:before {
  content: "\f26e";
}
.fa-amazon:before {
  content: "\f270";
}
.fa-calendar-plus-o:before {
  content: "\f271";
}
.fa-calendar-minus-o:before {
  content: "\f272";
}
.fa-calendar-times-o:before {
  content: "\f273";
}
.fa-calendar-check-o:before {
  content: "\f274";
}
.fa-industry:before {
  content: "\f275";
}
.fa-map-pin:before {
  content: "\f276";
}
.fa-map-signs:before {
  content: "\f277";
}
.fa-map-o:before {
  content: "\f278";
}
.fa-map:before {
  content: "\f279";
}
.fa-commenting:before {
  content: "\f27a";
}
.fa-commenting-o:before {
  content: "\f27b";
}
.fa-houzz:before {
  content: "\f27c";
}
.fa-vimeo:before {
  content: "\f27d";
}
.fa-black-tie:before {
  content: "\f27e";
}
.fa-fonticons:before {
  content: "\f280";
}
.fa-reddit-alien:before {
  content: "\f281";
}
.fa-edge:before {
  content: "\f282";
}
.fa-credit-card-alt:before {
  content: "\f283";
}
.fa-codiepie:before {
  content: "\f284";
}
.fa-modx:before {
  content: "\f285";
}
.fa-fort-awesome:before {
  content: "\f286";
}
.fa-usb:before {
  content: "\f287";
}
.fa-product-hunt:before {
  content: "\f288";
}
.fa-mixcloud:before {
  content: "\f289";
}
.fa-scribd:before {
  content: "\f28a";
}
.fa-pause-circle:before {
  content: "\f28b";
}
.fa-pause-circle-o:before {
  content: "\f28c";
}
.fa-stop-circle:before {
  content: "\f28d";
}
.fa-stop-circle-o:before {
  content: "\f28e";
}
.fa-shopping-bag:before {
  content: "\f290";
}
.fa-shopping-basket:before {
  content: "\f291";
}
.fa-hashtag:before {
  content: "\f292";
}
.fa-bluetooth:before {
  content: "\f293";
}
.fa-bluetooth-b:before {
  content: "\f294";
}
.fa-percent:before {
  content: "\f295";
}
.fa-gitlab:before {
  content: "\f296";
}
.fa-wpbeginner:before {
  content: "\f297";
}
.fa-wpforms:before {
  content: "\f298";
}
.fa-envira:before {
  content: "\f299";
}
.fa-universal-access:before {
  content: "\f29a";
}
.fa-wheelchair-alt:before {
  content: "\f29b";
}
.fa-question-circle-o:before {
  content: "\f29c";
}
.fa-blind:before {
  content: "\f29d";
}
.fa-audio-description:before {
  content: "\f29e";
}
.fa-volume-control-phone:before {
  content: "\f2a0";
}
.fa-braille:before {
  content: "\f2a1";
}
.fa-assistive-listening-systems:before {
  content: "\f2a2";
}
.fa-asl-interpreting:before,
.fa-american-sign-language-interpreting:before {
  content: "\f2a3";
}
.fa-deafness:before,
.fa-hard-of-hearing:before,
.fa-deaf:before {
  content: "\f2a4";
}
.fa-glide:before {
  content: "\f2a5";
}
.fa-glide-g:before {
  content: "\f2a6";
}
.fa-signing:before,
.fa-sign-language:before {
  content: "\f2a7";
}
.fa-low-vision:before {
  content: "\f2a8";
}
.fa-viadeo:before {
  content: "\f2a9";
}
.fa-viadeo-square:before {
  content: "\f2aa";
}
.fa-snapchat:before {
  content: "\f2ab";
}
.fa-snapchat-ghost:before {
  content: "\f2ac";
}
.fa-snapchat-square:before {
  content: "\f2ad";
}
.fa-pied-piper:before {
  content: "\f2ae";
}
.fa-first-order:before {
  content: "\f2b0";
}
.fa-yoast:before {
  content: "\f2b1";
}
.fa-themeisle:before {
  content: "\f2b2";
}
.fa-google-plus-circle:before,
.fa-google-plus-official:before {
  content: "\f2b3";
}
.fa-fa:before,
.fa-font-awesome:before {
  content: "\f2b4";
}
.fa-handshake-o:before {
  content: "\f2b5";
}
.fa-envelope-open:before {
  content: "\f2b6";
}
.fa-envelope-open-o:before {
  content: "\f2b7";
}
.fa-linode:before {
  content: "\f2b8";
}
.fa-address-book:before {
  content: "\f2b9";
}
.fa-address-book-o:before {
  content: "\f2ba";
}
.fa-vcard:before,
.fa-address-card:before {
  content: "\f2bb";
}
.fa-vcard-o:before,
.fa-address-card-o:before {
  content: "\f2bc";
}
.fa-user-circle:before {
  content: "\f2bd";
}
.fa-user-circle-o:before {
  content: "\f2be";
}
.fa-user-o:before {
  content: "\f2c0";
}
.fa-id-badge:before {
  content: "\f2c1";
}
.fa-drivers-license:before,
.fa-id-card:before {
  content: "\f2c2";
}
.fa-drivers-license-o:before,
.fa-id-card-o:before {
  content: "\f2c3";
}
.fa-quora:before {
  content: "\f2c4";
}
.fa-free-code-camp:before {
  content: "\f2c5";
}
.fa-telegram:before {
  content: "\f2c6";
}
.fa-thermometer-4:before,
.fa-thermometer:before,
.fa-thermometer-full:before {
  content: "\f2c7";
}
.fa-thermometer-3:before,
.fa-thermometer-three-quarters:before {
  content: "\f2c8";
}
.fa-thermometer-2:before,
.fa-thermometer-half:before {
  content: "\f2c9";
}
.fa-thermometer-1:before,
.fa-thermometer-quarter:before {
  content: "\f2ca";
}
.fa-thermometer-0:before,
.fa-thermometer-empty:before {
  content: "\f2cb";
}
.fa-shower:before {
  content: "\f2cc";
}
.fa-bathtub:before,
.fa-s15:before,
.fa-bath:before {
  content: "\f2cd";
}
.fa-podcast:before {
  content: "\f2ce";
}
.fa-window-maximize:before {
  content: "\f2d0";
}
.fa-window-minimize:before {
  content: "\f2d1";
}
.fa-window-restore:before {
  content: "\f2d2";
}
.fa-times-rectangle:before,
.fa-window-close:before {
  content: "\f2d3";
}
.fa-times-rectangle-o:before,
.fa-window-close-o:before {
  content: "\f2d4";
}
.fa-bandcamp:before {
  content: "\f2d5";
}
.fa-grav:before {
  content: "\f2d6";
}
.fa-etsy:before {
  content: "\f2d7";
}
.fa-imdb:before {
  content: "\f2d8";
}
.fa-ravelry:before {
  content: "\f2d9";
}
.fa-eercast:before {
  content: "\f2da";
}
.fa-microchip:before {
  content: "\f2db";
}
.fa-snowflake-o:before {
  content: "\f2dc";
}
.fa-superpowers:before {
  content: "\f2dd";
}
.fa-wpexplorer:before {
  content: "\f2de";
}
.fa-meetup:before {
  content: "\f2e0";
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
div.traceback-wrapper pre.traceback {
  max-height: 600px;
  overflow: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
[dir="rtl"] #ipython_notebook {
  margin-right: 10px;
  margin-left: 0;
}
[dir="rtl"] #ipython_notebook.pull-left {
  float: right !important;
  float: right;
}
.flex-spacer {
  flex: 1;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#kernel_logo_widget {
  margin: 0 10px;
}
span#login_widget {
  float: right;
}
[dir="rtl"] span#login_widget {
  float: left;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
.modal-header {
  cursor: move;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
[dir="rtl"] .center-nav form.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] .center-nav .navbar-text {
  float: right;
}
[dir="rtl"] .navbar-inner {
  text-align: right;
}
[dir="rtl"] div.text-left {
  text-align: right;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  position: absolute;
  display: block;
  width: 100%;
  height: 100%;
  overflow: hidden;
  cursor: pointer;
  opacity: 0;
  z-index: 2;
}
.alternate_upload .btn-xs > input.fileinput {
  margin: -1px -5px;
}
.alternate_upload .btn-upload {
  position: relative;
  height: 22px;
}
::-webkit-file-upload-button {
  cursor: pointer;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
[dir="rtl"] ul#tabs.nav-tabs > li {
  float: right;
}
[dir="rtl"] ul#tabs.nav.nav-tabs {
  padding-right: 0;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons .pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .list_toolbar .col-sm-4,
[dir="rtl"] .list_toolbar .col-sm-8 {
  float: right;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: text-bottom;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
[dir="rtl"] .list_item > div input {
  margin-right: 0;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_modified {
  margin-right: 7px;
  margin-left: 7px;
}
[dir="rtl"] .item_modified.pull-right {
  float: left !important;
  float: left;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
[dir="rtl"] .item_buttons.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .item_buttons .kernel-name {
  margin-left: 7px;
  float: right;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
.sort_button {
  display: inline-block;
  padding-left: 7px;
}
[dir="rtl"] .sort_button.pull-right {
  float: left !important;
  float: left;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
[dir="rtl"] #button-select-all.btn {
  float: right ;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
  margin-top: 2px;
  height: 16px;
}
[dir="rtl"] #select-all.pull-left {
  float: right !important;
  float: right;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.fa-pull-left {
  margin-right: .3em;
}
.folder_icon:before.fa-pull-right {
  margin-left: .3em;
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.fa-pull-left {
  margin-right: .3em;
}
.file_icon:before.fa-pull-right {
  margin-left: .3em;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
#new-menu .dropdown-header {
  font-size: 10px;
  border-bottom: 1px solid #e5e5e5;
  padding: 0 0 3px;
  margin: -3px 20px 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.move-button {
  display: none;
}
.download-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
.CodeMirror-dialog {
  background-color: #fff;
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI escape sequences */
/* The color values are a mix of
   http://www.xcolors.net/dl/baskerville-ivorylight and
   http://www.xcolors.net/dl/euphrasia */
.ansi-black-fg {
  color: #3E424D;
}
.ansi-black-bg {
  background-color: #3E424D;
}
.ansi-black-intense-fg {
  color: #282C36;
}
.ansi-black-intense-bg {
  background-color: #282C36;
}
.ansi-red-fg {
  color: #E75C58;
}
.ansi-red-bg {
  background-color: #E75C58;
}
.ansi-red-intense-fg {
  color: #B22B31;
}
.ansi-red-intense-bg {
  background-color: #B22B31;
}
.ansi-green-fg {
  color: #00A250;
}
.ansi-green-bg {
  background-color: #00A250;
}
.ansi-green-intense-fg {
  color: #007427;
}
.ansi-green-intense-bg {
  background-color: #007427;
}
.ansi-yellow-fg {
  color: #DDB62B;
}
.ansi-yellow-bg {
  background-color: #DDB62B;
}
.ansi-yellow-intense-fg {
  color: #B27D12;
}
.ansi-yellow-intense-bg {
  background-color: #B27D12;
}
.ansi-blue-fg {
  color: #208FFB;
}
.ansi-blue-bg {
  background-color: #208FFB;
}
.ansi-blue-intense-fg {
  color: #0065CA;
}
.ansi-blue-intense-bg {
  background-color: #0065CA;
}
.ansi-magenta-fg {
  color: #D160C4;
}
.ansi-magenta-bg {
  background-color: #D160C4;
}
.ansi-magenta-intense-fg {
  color: #A03196;
}
.ansi-magenta-intense-bg {
  background-color: #A03196;
}
.ansi-cyan-fg {
  color: #60C6C8;
}
.ansi-cyan-bg {
  background-color: #60C6C8;
}
.ansi-cyan-intense-fg {
  color: #258F8F;
}
.ansi-cyan-intense-bg {
  background-color: #258F8F;
}
.ansi-white-fg {
  color: #C5C1B4;
}
.ansi-white-bg {
  background-color: #C5C1B4;
}
.ansi-white-intense-fg {
  color: #A1A6B2;
}
.ansi-white-intense-bg {
  background-color: #A1A6B2;
}
.ansi-default-inverse-fg {
  color: #FFFFFF;
}
.ansi-default-inverse-bg {
  background-color: #000000;
}
.ansi-bold {
  font-weight: bold;
}
.ansi-underline {
  text-decoration: underline;
}
/* The following styles are deprecated an will be removed in a future version */
.ansibold {
  font-weight: bold;
}
.ansi-inverse {
  outline: 0.5px dotted;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  position: relative;
  overflow: visible;
}
div.cell:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: transparent;
}
div.cell.jupyter-soft-selected {
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected,
div.cell.selected.jupyter-soft-selected {
  border-color: #ababab;
}
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #42A5F5;
}
@media print {
  div.cell.selected,
  div.cell.selected.jupyter-soft-selected {
    border-color: transparent;
  }
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
}
.edit_mode div.cell.selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #66BB6A;
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  /* Note that this should set vertical padding only, since CodeMirror assumes
       that horizontal padding will be set on CodeMirror pre */
  padding: 0.4em 0;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. This sets horizontal padding only,
    use .CodeMirror-lines for vertical */
  padding: 0 0.4em;
  border: 0;
  border-radius: 0;
}
.CodeMirror-cursor {
  border-left: 1.4px solid black;
}
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .CodeMirror-cursor {
    border-left: 2px solid black;
  }
}
@media screen and (min-width: 4320px) {
  .CodeMirror-cursor {
    border-left: 4px solid black;
  }
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
div.output_area .mglyph > img {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 1px 0 1px 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul:not(.list-inline),
.rendered_html ol:not(.list-inline) {
  padding-left: 2em;
}
.rendered_html ul {
  list-style: disc;
}
.rendered_html ul ul {
  list-style: square;
  margin-top: 0;
}
.rendered_html ul ul ul {
  list-style: circle;
}
.rendered_html ol {
  list-style: decimal;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin-top: 0;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
  padding: 0px;
  background-color: #fff;
}
.rendered_html code {
  background-color: #eff0f1;
}
.rendered_html p code {
  padding: 1px 5px;
}
.rendered_html pre code {
  background-color: #fff;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  color: #000;
  font-size: 100%;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: none;
  border-collapse: collapse;
  border-spacing: 0;
  color: black;
  font-size: 12px;
  table-layout: fixed;
}
.rendered_html thead {
  border-bottom: 1px solid black;
  vertical-align: bottom;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  text-align: right;
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html tbody tr:nth-child(odd) {
  background: #f5f5f5;
}
.rendered_html tbody tr:hover {
  background: rgba(66, 165, 245, 0.2);
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
.rendered_html .alert {
  margin-bottom: initial;
}
.rendered_html * + .alert {
  margin-top: 1em;
}
[dir="rtl"] .rendered_html p {
  text-align: right;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.rendered .rendered_html tr,
.text_cell.rendered .rendered_html th,
.text_cell.rendered .rendered_html td {
  max-width: none;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.text_cell .dropzone .input_area {
  border: 2px dashed #bababa;
  margin: -1px;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
.jupyter-keybindings {
  padding: 1px;
  line-height: 24px;
  border-bottom: 1px solid gray;
}
.jupyter-keybindings input {
  margin: 0;
  padding: 0;
  border: none;
}
.jupyter-keybindings i {
  padding: 6px;
}
.well code {
  background-color: #ffffff;
  border-color: #ababab;
  border-width: 1px;
  border-style: solid;
  padding: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.tags_button_container {
  width: 100%;
  display: flex;
}
.tag-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  overflow: hidden;
  position: relative;
}
.tag-container > * {
  margin: 0 4px;
}
.remove-tag-btn {
  margin-left: 4px;
}
.tags-input {
  display: flex;
}
.cell-tag:last-child:after {
  content: "";
  position: absolute;
  right: 0;
  width: 40px;
  height: 100%;
  /* Fade to background color of cell toolbar */
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #EEE);
}
.tags-input > * {
  margin-left: 4px;
}
.cell-tag,
.tags-input input,
.tags-input button {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  box-shadow: none;
  width: inherit;
  font-size: inherit;
  height: 22px;
  line-height: 22px;
  padding: 0px 4px;
  display: inline-block;
}
.cell-tag:focus,
.tags-input input:focus,
.tags-input button:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.cell-tag::-moz-placeholder,
.tags-input input::-moz-placeholder,
.tags-input button::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.cell-tag:-ms-input-placeholder,
.tags-input input:-ms-input-placeholder,
.tags-input button:-ms-input-placeholder {
  color: #999;
}
.cell-tag::-webkit-input-placeholder,
.tags-input input::-webkit-input-placeholder,
.tags-input button::-webkit-input-placeholder {
  color: #999;
}
.cell-tag::-ms-expand,
.tags-input input::-ms-expand,
.tags-input button::-ms-expand {
  border: 0;
  background-color: transparent;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
.cell-tag[readonly],
.tags-input input[readonly],
.tags-input button[readonly],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  background-color: #eeeeee;
  opacity: 1;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  cursor: not-allowed;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button {
  height: auto;
}
select.cell-tag,
select.tags-input input,
select.tags-input button {
  height: 30px;
  line-height: 30px;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button,
select[multiple].cell-tag,
select[multiple].tags-input input,
select[multiple].tags-input button {
  height: auto;
}
.cell-tag,
.tags-input button {
  padding: 0px 4px;
}
.cell-tag {
  background-color: #fff;
  white-space: nowrap;
}
.tags-input input[type=text]:focus {
  outline: none;
  box-shadow: none;
  border-color: #ccc;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
[dir="rtl"] #kernel_logo_widget {
  float: left !important;
  float: left;
}
.modal .modal-body .move-path {
  display: flex;
  flex-direction: row;
  justify-content: space;
  align-items: center;
}
.modal .modal-body .move-path .server-root {
  padding-right: 20px;
}
.modal .modal-body .move-path .path-input {
  flex: 1;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
[dir="rtl"] #menubar .navbar-toggle {
  float: right;
}
[dir="rtl"] #menubar .navbar-collapse {
  clear: right;
}
[dir="rtl"] #menubar .navbar-nav {
  float: right;
}
[dir="rtl"] #menubar .nav {
  padding-right: 0px;
}
[dir="rtl"] #menubar .navbar-nav > li {
  float: right;
}
[dir="rtl"] #menubar .navbar-right {
  float: left !important;
}
[dir="rtl"] ul.dropdown-menu {
  text-align: right;
  left: auto;
}
[dir="rtl"] ul#new-menu.dropdown-menu {
  right: auto;
  left: 0;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
[dir="rtl"] i.menu-icon.pull-right {
  float: left !important;
  float: left;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
[dir="rtl"] ul#help_menu li a {
  padding-left: 2.2em;
}
[dir="rtl"] ul#help_menu li a i {
  margin-right: 0;
  margin-left: -1.2em;
}
[dir="rtl"] ul#help_menu li a i.pull-right {
  float: left !important;
  float: left;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
[dir="rtl"] .dropdown-submenu > .dropdown-menu {
  right: 100%;
  margin-right: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.fa-pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.fa-pull-right {
  margin-left: .3em;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
[dir="rtl"] .dropdown-submenu > a:after {
  float: left;
  content: "\f0d9";
  margin-right: 0;
  margin-left: -10px;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
[dir="rtl"] #notification_area {
  float: left !important;
  float: left;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] .indicator_area {
  float: left !important;
  float: left;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
[dir="rtl"] #kernel_indicator {
  float: left !important;
  float: left;
  border-left: 0;
  border-right: 1px solid;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] #modal_indicator {
  float: left !important;
  float: left;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  height: 30px;
  margin-top: 4px;
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  width: 50%;
  flex: 1;
}
span.save_widget span.filename {
  height: 100%;
  line-height: 1em;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
[dir="rtl"] span.save_widget.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] span.save_widget span.filename {
  margin-left: 0;
  margin-right: 16px;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
  white-space: nowrap;
  padding: 0 5px;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
    padding: 0 0 0 5px;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
.toolbar-btn-label {
  margin-left: 6px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
[dir="rtl"] .btn-group > .btn,
.btn-group-vertical > .btn {
  float: right;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
[dir="rtl"] ul.typeahead-list i {
  margin-left: 0;
  margin-right: -10px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
ul.typeahead-list  > li > a.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .typeahead-list {
  text-align: right;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  min-width: 20px;
  color: transparent;
}
[dir="rtl"] .no-shortcut.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .command-shortcut.pull-right {
  float: left !important;
  float: left;
}
.command-shortcut:before {
  content: "(command mode)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
[dir="rtl"] .edit-shortcut.pull-right {
  float: left !important;
  float: left;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control {
  border-left: none;
}
[dir="rtl"] #find-and-replace .input-group-btn + .form-control {
  border-right: none;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>
<style type="text/css">

/* Temporary definitions which will become obsolete with Notebook release 5.0 */
.ansi-black-fg { color: #3E424D; }
.ansi-black-bg { background-color: #3E424D; }
.ansi-black-intense-fg { color: #282C36; }
.ansi-black-intense-bg { background-color: #282C36; }
.ansi-red-fg { color: #E75C58; }
.ansi-red-bg { background-color: #E75C58; }
.ansi-red-intense-fg { color: #B22B31; }
.ansi-red-intense-bg { background-color: #B22B31; }
.ansi-green-fg { color: #00A250; }
.ansi-green-bg { background-color: #00A250; }
.ansi-green-intense-fg { color: #007427; }
.ansi-green-intense-bg { background-color: #007427; }
.ansi-yellow-fg { color: #DDB62B; }
.ansi-yellow-bg { background-color: #DDB62B; }
.ansi-yellow-intense-fg { color: #B27D12; }
.ansi-yellow-intense-bg { background-color: #B27D12; }
.ansi-blue-fg { color: #208FFB; }
.ansi-blue-bg { background-color: #208FFB; }
.ansi-blue-intense-fg { color: #0065CA; }
.ansi-blue-intense-bg { background-color: #0065CA; }
.ansi-magenta-fg { color: #D160C4; }
.ansi-magenta-bg { background-color: #D160C4; }
.ansi-magenta-intense-fg { color: #A03196; }
.ansi-magenta-intense-bg { background-color: #A03196; }
.ansi-cyan-fg { color: #60C6C8; }
.ansi-cyan-bg { background-color: #60C6C8; }
.ansi-cyan-intense-fg { color: #258F8F; }
.ansi-cyan-intense-bg { background-color: #258F8F; }
.ansi-white-fg { color: #C5C1B4; }
.ansi-white-bg { background-color: #C5C1B4; }
.ansi-white-intense-fg { color: #A1A6B2; }
.ansi-white-intense-bg { background-color: #A1A6B2; }

.ansi-bold { font-weight: bold; }

    </style>
<style type="text/css">
    /*This file contains any manual css for this page that needs to override the global styles.
This is only required when different pages style the same element differently. This is just
a hack to deal with our current css styles and no new styling should be added in this file.*/

#ipython-main-app {
    position: relative;
}
#jupyter-main-app {
    position: relative;
}

    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
.reveal {
  font-size: 160%;
}
.reveal pre {
  width: inherit;
  padding: 0.4em;
  margin: 0px;
  font-family: monospace, sans-serif;
  font-size: 80%;
  box-shadow: 0px 0px 0px rgba(0, 0, 0, 0);
}
.reveal pre code {
  padding: 0px;
}
.reveal section img {
  border: 0px solid black;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0);
}
.reveal i {
  font-style: normal;
  font-family: FontAwesome;
  font-size: 2em;
}
.reveal .slides {
  text-align: left;
}
.reveal.fade {
  opacity: 1;
}
.reveal .progress {
  position: static;
}
.reveal .controls .navigate-left,
.reveal .controls .navigate-left.enabled {
  border-right-color: #727272;
}
.reveal .controls .navigate-left.enabled:hover,
.reveal .controls .navigate-left.enabled.enabled:hover {
  border-right-color: #dfdfdf;
}
.reveal .controls .navigate-right,
.reveal .controls .navigate-right.enabled {
  border-left-color: #727272;
}
.reveal .controls .navigate-right.enabled:hover,
.reveal .controls .navigate-right.enabled.enabled:hover {
  border-left-color: #dfdfdf;
}
.reveal .controls .navigate-up,
.reveal .controls .navigate-up.enabled {
  border-bottom-color: #727272;
}
.reveal .controls .navigate-up.enabled:hover,
.reveal .controls .navigate-up.enabled.enabled:hover {
  border-bottom-color: #dfdfdf;
}
.reveal .controls .navigate-down,
.reveal .controls .navigate-down.enabled {
  border-top-color: #727272;
}
.reveal .controls .navigate-down.enabled:hover,
.reveal .controls .navigate-down.enabled.enabled:hover {
  border-top-color: #dfdfdf;
}
.reveal .progress span {
  background: #727272;
}
div.input_area {
  padding: 0.06em;
}
div.code_cell {
  background-color: transparent;
}
div.prompt {
  width: 11ex;
  padding: 0.4em;
  margin: 0px;
  font-family: monospace, sans-serif;
  font-size: 80%;
  text-align: right;
}
div.output_area pre {
  font-family: monospace, sans-serif;
  font-size: 80%;
}
div.output_prompt {
  /* 5px right shift to account for margin in parent container */
  margin: 5px 5px 0 0;
}
div.text_cell.rendered .rendered_html {
  /* The H1 height seems miscalculated, we are just hidding the scrollbar */
  overflow-y: hidden;
}
a.anchor-link {
  /* There is still an anchor, we are only hidding it */
  display: none;
}
.rendered_html p {
  text-align: inherit;
}
::-webkit-scrollbar
{
  width: 6px;
  height: 6px;
}
::-webkit-scrollbar *
{
  background:transparent;
}
::-webkit-scrollbar-thumb
{
  background: #727272 !important;
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<div class="reveal">
<div class="slides">
<section><section>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><h1>Table of Contents<span class="tocSkip"></span></h1></p>
<div class="toc"><ul class="toc-item"><li><span><a href="#Data-Preprocessing" data-toc-modified-id="Data-Preprocessing-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Data Preprocessing</a></span></li><li><span><a href="#Exploratory-Data-Analysis-(EDA)" data-toc-modified-id="Exploratory-Data-Analysis-(EDA)-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Exploratory Data Analysis (EDA)</a></span><ul class="toc-item"><li><span><a href="#Correlation-Matrix" data-toc-modified-id="Correlation-Matrix-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Correlation Matrix</a></span></li><li><span><a href="#Total-Page-Likes" data-toc-modified-id="Total-Page-Likes-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Total Page Likes</a></span></li><li><span><a href="#Category" data-toc-modified-id="Category-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Category</a></span></li><li><span><a href="#Post-Month" data-toc-modified-id="Post-Month-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Post Month</a></span></li><li><span><a href="#Post-Weekday" data-toc-modified-id="Post-Weekday-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Post Weekday</a></span></li><li><span><a href="#Post-Hour" data-toc-modified-id="Post-Hour-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Post Hour</a></span></li><li><span><a href="#Paid" data-toc-modified-id="Paid-2.7"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>Paid</a></span></li><li><span><a href="#Comments" data-toc-modified-id="Comments-2.8"><span class="toc-item-num">2.8&nbsp;&nbsp;</span>Comments</a></span></li><li><span><a href="#Likes" data-toc-modified-id="Likes-2.9"><span class="toc-item-num">2.9&nbsp;&nbsp;</span>Likes</a></span></li><li><span><a href="#Shares" data-toc-modified-id="Shares-2.10"><span class="toc-item-num">2.10&nbsp;&nbsp;</span>Shares</a></span></li><li><span><a href="#Lifetime-Data-Analysis" data-toc-modified-id="Lifetime-Data-Analysis-2.11"><span class="toc-item-num">2.11&nbsp;&nbsp;</span>Lifetime Data Analysis</a></span></li></ul></li><li><span><a href="#Machine-Learning" data-toc-modified-id="Machine-Learning-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Machine Learning</a></span><ul class="toc-item"><li><span><a href="#SVM-Feature-Importance" data-toc-modified-id="SVM-Feature-Importance-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>SVM Feature Importance</a></span></li><li><span><a href="#Linear-Regression" data-toc-modified-id="Linear-Regression-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Linear Regression</a></span></li><li><span><a href="#Random-Forest" data-toc-modified-id="Random-Forest-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Random Forest</a></span></li></ul></li></ul></div>
</div>
</div>
</div></section></section><section><section>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Facebook-performance-metrics">Facebook performance metrics<a class="anchor-link" href="#Facebook-performance-metrics">&#182;</a></h1>
</div>
</div>
</div></section><section>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Data-Preprocessing">Data Preprocessing<a class="anchor-link" href="#Data-Preprocessing">&#182;</a></h2>
</div>
</div>
</div><div class="fragment">
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[48]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">from</span> <span class="nn">keras.utils</span> <span class="k">import</span> <span class="n">np_utils</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">from</span> <span class="nn">matplotlib.pyplot</span> <span class="k">import</span> <span class="n">figure</span>
<span class="kn">import</span> <span class="nn">seaborn</span> <span class="k">as</span> <span class="nn">sns</span>
<span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="k">import</span> <span class="n">LabelEncoder</span>
<span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="k">import</span> <span class="n">StandardScaler</span>
<span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="k">import</span> <span class="n">train_test_split</span>
<span class="kn">from</span> <span class="nn">sklearn.ensemble</span> <span class="k">import</span> <span class="n">RandomForestRegressor</span>
<span class="kn">from</span> <span class="nn">sklearn.metrics</span> <span class="k">import</span> <span class="n">r2_score</span>
<span class="kn">from</span> <span class="nn">scipy.stats</span> <span class="k">import</span> <span class="n">spearmanr</span><span class="p">,</span> <span class="n">pearsonr</span>
<span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="k">import</span> <span class="n">LinearRegression</span>
</pre></div>

    </div>
</div>
</div>

</div></div></section></section><section><section>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s2">&quot;dataset_Facebook.csv&quot;</span><span class="p">,</span><span class="s2">&quot;;&quot;</span><span class="p">)</span>
<span class="n">df</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[2]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Page total likes</th>
      <th>Type</th>
      <th>Category</th>
      <th>Post Month</th>
      <th>Post Weekday</th>
      <th>Post Hour</th>
      <th>Paid</th>
      <th>Lifetime Post Total Reach</th>
      <th>Lifetime Post Total Impressions</th>
      <th>Lifetime Engaged Users</th>
      <th>Lifetime Post Consumers</th>
      <th>Lifetime Post Consumptions</th>
      <th>Lifetime Post Impressions by people who have liked your Page</th>
      <th>Lifetime Post reach by people who like your Page</th>
      <th>Lifetime People who have liked your Page and engaged with your post</th>
      <th>comment</th>
      <th>like</th>
      <th>share</th>
      <th>Total Interactions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>139441</td>
      <td>Photo</td>
      <td>2</td>
      <td>12</td>
      <td>4</td>
      <td>3</td>
      <td>0.0</td>
      <td>2752</td>
      <td>5091</td>
      <td>178</td>
      <td>109</td>
      <td>159</td>
      <td>3078</td>
      <td>1640</td>
      <td>119</td>
      <td>4</td>
      <td>79.0</td>
      <td>17.0</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>139441</td>
      <td>Status</td>
      <td>2</td>
      <td>12</td>
      <td>3</td>
      <td>10</td>
      <td>0.0</td>
      <td>10460</td>
      <td>19057</td>
      <td>1457</td>
      <td>1361</td>
      <td>1674</td>
      <td>11710</td>
      <td>6112</td>
      <td>1108</td>
      <td>5</td>
      <td>130.0</td>
      <td>29.0</td>
      <td>164</td>
    </tr>
    <tr>
      <th>2</th>
      <td>139441</td>
      <td>Photo</td>
      <td>3</td>
      <td>12</td>
      <td>3</td>
      <td>3</td>
      <td>0.0</td>
      <td>2413</td>
      <td>4373</td>
      <td>177</td>
      <td>113</td>
      <td>154</td>
      <td>2812</td>
      <td>1503</td>
      <td>132</td>
      <td>0</td>
      <td>66.0</td>
      <td>14.0</td>
      <td>80</td>
    </tr>
    <tr>
      <th>3</th>
      <td>139441</td>
      <td>Photo</td>
      <td>2</td>
      <td>12</td>
      <td>2</td>
      <td>10</td>
      <td>1.0</td>
      <td>50128</td>
      <td>87991</td>
      <td>2211</td>
      <td>790</td>
      <td>1119</td>
      <td>61027</td>
      <td>32048</td>
      <td>1386</td>
      <td>58</td>
      <td>1572.0</td>
      <td>147.0</td>
      <td>1777</td>
    </tr>
    <tr>
      <th>4</th>
      <td>139441</td>
      <td>Photo</td>
      <td>2</td>
      <td>12</td>
      <td>2</td>
      <td>3</td>
      <td>0.0</td>
      <td>7244</td>
      <td>13594</td>
      <td>671</td>
      <td>410</td>
      <td>580</td>
      <td>6228</td>
      <td>3200</td>
      <td>396</td>
      <td>19</td>
      <td>325.0</td>
      <td>49.0</td>
      <td>393</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div></section></section><section><section>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Exploratory-Data-Analysis-(EDA)">Exploratory Data Analysis (EDA)<a class="anchor-link" href="#Exploratory-Data-Analysis-(EDA)">&#182;</a></h2>
</div>
</div>
</div></section><section>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Correlation-Matrix">Correlation Matrix<a class="anchor-link" href="#Correlation-Matrix">&#182;</a></h3>
</div>
</div>
</div><div class="fragment">
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span><span class="mi">7</span><span class="p">))</span>
<span class="n">sns</span><span class="o">.</span><span class="n">heatmap</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">corr</span><span class="p">(),</span><span class="n">annot</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span><span class="n">cbar</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[5]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.axes._subplots.AxesSubplot at 0x2dc88131d30&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div></div></section><section>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Total-Page-Likes">Total Page Likes<a class="anchor-link" href="#Total-Page-Likes">&#182;</a></h3>
</div>
</div>
</div><div class="fragment">
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">iloc</span><span class="p">[:,</span><span class="mi">0</span><span class="p">])</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Total pages likes&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[8]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Text(0.5, 1.0, &#39;Total pages likes&#39;)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div></div></section><section>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Category">Category<a class="anchor-link" href="#Category">&#182;</a></h3>
</div>
</div>
</div><div class="fragment">
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">objects</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;Photos&#39;</span><span class="p">,</span> <span class="s1">&#39;Status&#39;</span><span class="p">,</span> <span class="s1">&#39;Link&#39;</span><span class="p">,</span> <span class="s1">&#39;Video&#39;</span><span class="p">)</span>
<span class="n">y_pos</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">objects</span><span class="p">))</span>

<span class="n">plt</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="n">y_pos</span><span class="p">,</span> <span class="n">df</span><span class="o">.</span><span class="n">iloc</span><span class="p">[:,</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span><span class="o">.</span><span class="n">values</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xticks</span><span class="p">(</span><span class="n">y_pos</span><span class="p">,</span> <span class="n">objects</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Number of posts&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Different types of post compared&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[10]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Text(0.5, 1.0, &#39;Different types of post compared&#39;)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div></div></section></section><section><section>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span><span class="mi">7</span><span class="p">))</span>

<span class="n">sns</span><span class="o">.</span><span class="n">countplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s1">&#39;Type&#39;</span><span class="p">,</span><span class="n">hue</span><span class="o">=</span><span class="s1">&#39;Paid&#39;</span><span class="p">,</span><span class="n">data</span><span class="o">=</span><span class="n">df</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Number of posts: Paid vs Not Paid&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s2">&quot;Number of posts&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[11]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Text(0, 0.5, &#39;Number of posts&#39;)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div></section></section><section><section>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Post-Month">Post Month<a class="anchor-link" href="#Post-Month">&#182;</a></h3>
</div>
</div>
</div></section><section>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span><span class="mi">7</span><span class="p">))</span>

<span class="n">objects</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;Jenuary&#39;</span><span class="p">,</span> <span class="s1">&#39;Febraury&#39;</span><span class="p">,</span> <span class="s1">&#39;March&#39;</span><span class="p">,</span> <span class="s1">&#39;April&#39;</span><span class="p">,</span><span class="s1">&#39;May&#39;</span><span class="p">,</span><span class="s1">&#39;June&#39;</span><span class="p">,</span><span class="s1">&#39;July&#39;</span><span class="p">,</span><span class="s1">&#39;August&#39;</span><span class="p">,</span><span class="s1">&#39;September&#39;</span><span class="p">,</span><span class="s1">&#39;October&#39;</span><span class="p">,</span><span class="s1">&#39;November&#39;</span><span class="p">,</span><span class="s1">&#39;December&#39;</span><span class="p">)</span>
<span class="n">y_pos</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">objects</span><span class="p">))</span>

<span class="n">plt</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="n">y_pos</span><span class="p">,</span> <span class="n">df</span><span class="o">.</span><span class="n">iloc</span><span class="p">[:,</span><span class="mi">3</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span><span class="o">.</span><span class="n">values</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xticks</span><span class="p">(</span><span class="n">y_pos</span><span class="p">,</span> <span class="n">objects</span><span class="p">,</span> <span class="n">rotation</span><span class="o">=</span><span class="mi">70</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Number of posts&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Number of posts for each month&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[12]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Text(0.5, 1.0, &#39;Number of posts for each month&#39;)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div></section></section><section><section>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Post-Weekday">Post Weekday<a class="anchor-link" href="#Post-Weekday">&#182;</a></h3>
</div>
</div>
</div></section><section>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span><span class="mi">7</span><span class="p">))</span>

<span class="n">objects</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;Monday&#39;</span><span class="p">,</span> <span class="s1">&#39;Tuesday&#39;</span><span class="p">,</span> <span class="s1">&#39;Wednsday&#39;</span><span class="p">,</span> <span class="s1">&#39;Thoursday&#39;</span><span class="p">,</span><span class="s1">&#39;Friday&#39;</span><span class="p">,</span><span class="s1">&#39;Saturday&#39;</span><span class="p">,</span><span class="s1">&#39;Sunday&#39;</span><span class="p">)</span>
<span class="n">y_pos</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">objects</span><span class="p">))</span>

<span class="n">plt</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="n">y_pos</span><span class="p">,</span> <span class="n">df</span><span class="o">.</span><span class="n">iloc</span><span class="p">[:,</span><span class="mi">4</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span><span class="o">.</span><span class="n">values</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xticks</span><span class="p">(</span><span class="n">y_pos</span><span class="p">,</span> <span class="n">objects</span><span class="p">,</span> <span class="n">rotation</span><span class="o">=</span><span class="mi">70</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Number of posts&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Number of posts for each week-day&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[13]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Text(0.5, 1.0, &#39;Number of posts for each week-day&#39;)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div></section></section><section><section>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Post-Hour">Post Hour<a class="anchor-link" href="#Post-Hour">&#182;</a></h3>
</div>
</div>
</div></section><section>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span><span class="mi">7</span><span class="p">))</span>

<span class="n">objects</span> <span class="o">=</span> <span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">24</span><span class="p">))</span>
<span class="n">y_pos</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">objects</span><span class="p">))</span>
<span class="c1"># print(len(y_pos))</span>
<span class="c1"># print(len(a))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="n">y_pos</span><span class="p">,</span> <span class="n">a</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xticks</span><span class="p">(</span><span class="n">y_pos</span><span class="p">,</span> <span class="n">objects</span><span class="p">,</span> <span class="n">rotation</span><span class="o">=</span><span class="mi">70</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Number of posts&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Number of posts for each hour of the day&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[15]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Text(0.5, 1.0, &#39;Number of posts for each hour of the day&#39;)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div></section></section><section><section>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Paid">Paid<a class="anchor-link" href="#Paid">&#182;</a></h3>
</div>
</div>
</div></section><section>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span><span class="mi">7</span><span class="p">))</span>

<span class="n">objects</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;Free&#39;</span><span class="p">,</span> <span class="s1">&#39;Paid&#39;</span><span class="p">)</span>
<span class="n">y_pos</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">objects</span><span class="p">))</span>

<span class="n">plt</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="n">y_pos</span><span class="p">,</span> <span class="n">df</span><span class="o">.</span><span class="n">iloc</span><span class="p">[:,</span><span class="mi">6</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span><span class="o">.</span><span class="n">values</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xticks</span><span class="p">(</span><span class="n">y_pos</span><span class="p">,</span> <span class="n">objects</span><span class="p">,</span> <span class="n">rotation</span><span class="o">=</span><span class="mi">70</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Number of posts&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Number of posts: Free vs Paid&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[16]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Text(0.5, 1.0, &#39;Number of posts: Free vs Paid&#39;)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div></section><section>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span><span class="mi">7</span><span class="p">))</span>
<span class="n">sns</span><span class="o">.</span><span class="n">countplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s1">&#39;Post Weekday&#39;</span><span class="p">,</span><span class="n">hue</span><span class="o">=</span><span class="s1">&#39;Paid&#39;</span><span class="p">,</span><span class="n">data</span><span class="o">=</span><span class="n">df</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Number of posts: Free vs Paid&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[17]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Text(0.5, 1.0, &#39;Number of posts: Free vs Paid&#39;)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div></section><section>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Comments">Comments<a class="anchor-link" href="#Comments">&#182;</a></h3>
</div>
</div>
</div><div class="fragment">
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[18]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">iloc</span><span class="p">[:,</span><span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">columns</span><span class="p">)</span><span class="o">-</span><span class="mi">4</span><span class="p">])</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Comments per post distribution&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[18]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Text(0.5, 1.0, &#39;Comments per post distribution&#39;)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div></div></section><section>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Likes">Likes<a class="anchor-link" href="#Likes">&#182;</a></h3>
</div>
</div>
</div><div class="fragment">
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[19]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">iloc</span><span class="p">[:,</span><span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">columns</span><span class="p">)</span><span class="o">-</span><span class="mi">3</span><span class="p">])</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Likes per post distribution&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>C:\Users\hp\Anaconda3\lib\site-packages\numpy\lib\histograms.py:824: RuntimeWarning: invalid value encountered in greater_equal
  keep = (tmp_a &gt;= first_edge)
C:\Users\hp\Anaconda3\lib\site-packages\numpy\lib\histograms.py:825: RuntimeWarning: invalid value encountered in less_equal
  keep &amp;= (tmp_a &lt;= last_edge)
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[19]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Text(0.5, 1.0, &#39;Likes per post distribution&#39;)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div></div></section><section>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Shares">Shares<a class="anchor-link" href="#Shares">&#182;</a></h3>
</div>
</div>
</div><div class="fragment">
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">iloc</span><span class="p">[:,</span><span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">columns</span><span class="p">)</span><span class="o">-</span><span class="mi">2</span><span class="p">])</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Share per post distribution&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[20]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Text(0.5, 1.0, &#39;Share per post distribution&#39;)</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div></div></section><section>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Lifetime-Data-Analysis">Lifetime Data Analysis<a class="anchor-link" href="#Lifetime-Data-Analysis">&#182;</a></h3>
</div>
</div>
</div><div class="fragment">
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[21]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dfplot</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">columns</span><span class="p">[</span><span class="mi">7</span><span class="p">:</span><span class="mi">15</span><span class="p">],</span><span class="n">axis</span> <span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">sns</span><span class="o">.</span><span class="n">pairplot</span><span class="p">(</span><span class="n">data</span><span class="o">=</span><span class="n">dfplot</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span><span class="mi">7</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[21]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;Figure size 504x504 with 0 Axes&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_text output_subarea ">
<pre>&lt;Figure size 504x504 with 0 Axes&gt;</pre>
</div>

</div>

</div>
</div>

</div></div></section></section><section><section>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Machine-Learning">Machine Learning<a class="anchor-link" href="#Machine-Learning">&#182;</a></h2>
</div>
</div>
</div></section><section>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[22]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">lb_make</span> <span class="o">=</span> <span class="n">LabelEncoder</span><span class="p">()</span>
<span class="n">df</span><span class="p">[</span><span class="s2">&quot;Type&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">lb_make</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s2">&quot;Type&quot;</span><span class="p">])</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
<span class="n">df</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[22]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Page total likes</th>
      <th>Type</th>
      <th>Category</th>
      <th>Post Month</th>
      <th>Post Weekday</th>
      <th>Post Hour</th>
      <th>Paid</th>
      <th>Lifetime Post Total Reach</th>
      <th>Lifetime Post Total Impressions</th>
      <th>Lifetime Engaged Users</th>
      <th>Lifetime Post Consumers</th>
      <th>Lifetime Post Consumptions</th>
      <th>Lifetime Post Impressions by people who have liked your Page</th>
      <th>Lifetime Post reach by people who like your Page</th>
      <th>Lifetime People who have liked your Page and engaged with your post</th>
      <th>comment</th>
      <th>like</th>
      <th>share</th>
      <th>Total Interactions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>139441</td>
      <td>1</td>
      <td>2</td>
      <td>12</td>
      <td>4</td>
      <td>3</td>
      <td>0.0</td>
      <td>2752</td>
      <td>5091</td>
      <td>178</td>
      <td>109</td>
      <td>159</td>
      <td>3078</td>
      <td>1640</td>
      <td>119</td>
      <td>4</td>
      <td>79.0</td>
      <td>17.0</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>139441</td>
      <td>2</td>
      <td>2</td>
      <td>12</td>
      <td>3</td>
      <td>10</td>
      <td>0.0</td>
      <td>10460</td>
      <td>19057</td>
      <td>1457</td>
      <td>1361</td>
      <td>1674</td>
      <td>11710</td>
      <td>6112</td>
      <td>1108</td>
      <td>5</td>
      <td>130.0</td>
      <td>29.0</td>
      <td>164</td>
    </tr>
    <tr>
      <th>2</th>
      <td>139441</td>
      <td>1</td>
      <td>3</td>
      <td>12</td>
      <td>3</td>
      <td>3</td>
      <td>0.0</td>
      <td>2413</td>
      <td>4373</td>
      <td>177</td>
      <td>113</td>
      <td>154</td>
      <td>2812</td>
      <td>1503</td>
      <td>132</td>
      <td>0</td>
      <td>66.0</td>
      <td>14.0</td>
      <td>80</td>
    </tr>
    <tr>
      <th>3</th>
      <td>139441</td>
      <td>1</td>
      <td>2</td>
      <td>12</td>
      <td>2</td>
      <td>10</td>
      <td>1.0</td>
      <td>50128</td>
      <td>87991</td>
      <td>2211</td>
      <td>790</td>
      <td>1119</td>
      <td>61027</td>
      <td>32048</td>
      <td>1386</td>
      <td>58</td>
      <td>1572.0</td>
      <td>147.0</td>
      <td>1777</td>
    </tr>
    <tr>
      <th>4</th>
      <td>139441</td>
      <td>1</td>
      <td>2</td>
      <td>12</td>
      <td>2</td>
      <td>3</td>
      <td>0.0</td>
      <td>7244</td>
      <td>13594</td>
      <td>671</td>
      <td>410</td>
      <td>580</td>
      <td>6228</td>
      <td>3200</td>
      <td>396</td>
      <td>19</td>
      <td>325.0</td>
      <td>49.0</td>
      <td>393</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div></section><section>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[36]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">X</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="s1">&#39;like&#39;</span><span class="p">],</span> <span class="n">axis</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">values</span>
<span class="n">Y</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">&#39;like&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">values</span>

<span class="n">X</span> <span class="o">=</span> <span class="n">StandardScaler</span><span class="p">()</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">X</span><span class="p">)</span>

<span class="n">X_Train</span><span class="p">,</span> <span class="n">X_Test</span><span class="p">,</span> <span class="n">Y_Train</span><span class="p">,</span> <span class="n">Y_Test</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">Y</span><span class="p">,</span> <span class="n">test_size</span> <span class="o">=</span> <span class="mf">0.30</span><span class="p">,</span> <span class="n">random_state</span> <span class="o">=</span> <span class="mi">101</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div></section></section><section><section>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="SVM-Feature-Importance">SVM Feature Importance<a class="anchor-link" href="#SVM-Feature-Importance">&#182;</a></h3>
</div>
</div>
</div></section></section><section><section>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[37]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn</span> <span class="k">import</span> <span class="n">svm</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="k">def</span> <span class="nf">feature_plot</span><span class="p">(</span><span class="n">classifier</span><span class="p">,</span> <span class="n">feature_names</span><span class="p">,</span> <span class="n">top_features</span><span class="o">=</span><span class="mi">4</span><span class="p">):</span>
    <span class="n">coef</span> <span class="o">=</span> <span class="n">classifier</span><span class="o">.</span><span class="n">coef_</span><span class="o">.</span><span class="n">ravel</span><span class="p">()</span>
    <span class="n">top_positive_coefficients</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">argsort</span><span class="p">(</span><span class="n">coef</span><span class="p">)[</span><span class="o">-</span><span class="n">top_features</span><span class="p">:]</span>
    <span class="n">top_negative_coefficients</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">argsort</span><span class="p">(</span><span class="n">coef</span><span class="p">)[:</span><span class="n">top_features</span><span class="p">]</span>
    <span class="n">top_coefficients</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">hstack</span><span class="p">([</span><span class="n">top_negative_coefficients</span><span class="p">,</span> <span class="n">top_positive_coefficients</span><span class="p">])</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">18</span><span class="p">,</span> <span class="mi">7</span><span class="p">))</span>
    <span class="n">colors</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;green&#39;</span> <span class="k">if</span> <span class="n">c</span> <span class="o">&lt;</span> <span class="mi">0</span> <span class="k">else</span> <span class="s1">&#39;blue&#39;</span> <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">coef</span><span class="p">[</span><span class="n">top_coefficients</span><span class="p">]]</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">2</span> <span class="o">*</span> <span class="n">top_features</span><span class="p">),</span> <span class="n">coef</span><span class="p">[</span><span class="n">top_coefficients</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="n">colors</span><span class="p">)</span>
    <span class="n">feature_names</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">feature_names</span><span class="p">)</span>
    <span class="c1">#plt.xticks(np.arange(1 + 2 * top_features), feature_names[top_coefficients], rotation=45, ha=&#39;right&#39;)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="s1">&#39;like&#39;</span><span class="p">],</span> <span class="n">axis</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">columns</span><span class="o">.</span><span class="n">values</span><span class="p">)</span>

<span class="n">trainedsvm</span> <span class="o">=</span> <span class="n">svm</span><span class="o">.</span><span class="n">LinearSVC</span><span class="p">()</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">Y</span><span class="p">)</span>
<span class="n">feature_plot</span><span class="p">(</span><span class="n">trainedsvm</span><span class="p">,</span> <span class="n">df</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="s1">&#39;like&#39;</span><span class="p">],</span> <span class="n">axis</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">columns</span><span class="o">.</span><span class="n">values</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[&#39;Page total likes&#39; &#39;Type&#39; &#39;Category&#39; &#39;Post Month&#39; &#39;Post Weekday&#39;
 &#39;Post Hour&#39; &#39;Paid&#39; &#39;Lifetime Post Total Reach&#39;
 &#39;Lifetime Post Total Impressions&#39; &#39;Lifetime Engaged Users&#39;
 &#39;Lifetime Post Consumers&#39; &#39;Lifetime Post Consumptions&#39;
 &#39;Lifetime Post Impressions by people who have liked your Page&#39;
 &#39;Lifetime Post reach by people who like your Page&#39;
 &#39;Lifetime People who have liked your Page and engaged with your post&#39;
 &#39;comment&#39; &#39;share&#39; &#39;Total Interactions&#39;]
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>C:\Users\hp\Anaconda3\lib\site-packages\sklearn\svm\base.py:931: ConvergenceWarning: Liblinear failed to converge, increase the number of iterations.
  &#34;the number of iterations.&#34;, ConvergenceWarning)
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div></section></section><section><section>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Linear-Regression">Linear Regression<a class="anchor-link" href="#Linear-Regression">&#182;</a></h3>
</div>
</div>
</div></section><section>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[38]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">reg</span> <span class="o">=</span> <span class="n">LinearRegression</span><span class="p">()</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_Train</span><span class="p">,</span><span class="n">Y_Train</span><span class="p">)</span>
<span class="n">reg</span><span class="o">.</span><span class="n">score</span><span class="p">(</span><span class="n">X_Train</span><span class="p">,</span><span class="n">Y_Train</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[38]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>1.0</pre>
</div>

</div>

</div>
</div>

</div></section></section><section><section>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Random-Forest">Random Forest<a class="anchor-link" href="#Random-Forest">&#182;</a></h3>
</div>
</div>
</div></section><section>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[50]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">randomforest</span> <span class="o">=</span> <span class="n">RandomForestRegressor</span><span class="p">(</span><span class="n">n_estimators</span><span class="o">=</span><span class="mi">500</span><span class="p">,</span><span class="n">min_samples_split</span><span class="o">=</span><span class="mi">10</span><span class="p">)</span>
<span class="n">randomforest</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_Train</span><span class="p">,</span><span class="n">Y_Train</span><span class="p">)</span>

<span class="n">p_train</span> <span class="o">=</span> <span class="n">rf</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_Train</span><span class="p">)</span>
<span class="n">p_test</span> <span class="o">=</span> <span class="n">rf</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_Test</span><span class="p">)</span>

<span class="n">train_acc</span> <span class="o">=</span> <span class="n">r2_score</span><span class="p">(</span><span class="n">Y_Train</span><span class="p">,</span> <span class="n">p_train</span><span class="p">)</span>
<span class="n">test_acc</span> <span class="o">=</span> <span class="n">r2_score</span><span class="p">(</span><span class="n">Y_Test</span><span class="p">,</span> <span class="n">p_test</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Training Score: &quot;</span><span class="p">,</span> <span class="n">train_acc</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Test Score: &quot;</span><span class="p">,</span> <span class="n">test_score</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Training Score:  0.9184766137141158
Test Score:  0.9863946408914626
</pre>
</div>
</div>

</div>
</div>

</div></section></section>
</div>
</div>

<script>

require(
    {
      // it makes sense to wait a little bit when you are loading
      // reveal from a cdn in a slow connection environment
      waitSeconds: 15
    },
    [
      "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.5.0/lib/js/head.min.js",
      "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.5.0/js/reveal.js"
    ],

    function(head, Reveal){

        // Full list of configuration options available here: https://github.com/hakimel/reveal.js#configuration
        Reveal.initialize({
            controls: true,
            progress: true,
            history: true,

            transition: "slide",

            // Optional libraries used to extend on reveal.js
            dependencies: [
                { src: "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.5.0/lib/js/classList.js",
                  condition: function() { return !document.body.classList; } },
                { src: "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.5.0/plugin/notes/notes.js",
                  async: true,
                  condition: function() { return !!document.body.classList; } }
            ]
        });

        var update = function(event){
          if(MathJax.Hub.getAllJax(Reveal.getCurrentSlide())){
            MathJax.Hub.Rerender(Reveal.getCurrentSlide());
          }
        };

        Reveal.addEventListener('slidechanged', update);

        function setScrollingSlide() {
            var scroll = false
            if (scroll === true) {
              var h = $('.reveal').height() * 0.95;
              $('section.present').find('section')
                .filter(function() {
                  return $(this).height() > h;
                })
                .css('height', 'calc(95vh)')
                .css('overflow-y', 'scroll')
                .css('margin-top', '20px');
            }
        }

        // check and set the scrolling slide every time the slide change
        Reveal.addEventListener('slidechanged', setScrollingSlide);

    }

);
</script>