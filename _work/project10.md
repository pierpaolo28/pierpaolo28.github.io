---
date: 2019-07-29
tags: [Extra]
permalink: Projects/Unity/project10.html
title: Unity Online Game
featured-img: unity
img-type: jpg
summary: Unity Game created as part of the "Alleviate Children's Health Issues through Games and Machine Learning" research project.
---

<title>Unity Online Game | Pier Paolo Ippolito</title>
<link
 rel="shortcut icon"
 href="../../assets/img/icons/favicon.ico"
 type="image/x-icon"
/>
<link rel="stylesheet" href="../../assets/dist/TemplateData/style.css" />
<script src="../../assets/dist/TemplateData/UnityProgress.javascript"></script>
<script src="../../assets/dist/Build/UnityLoader.js"></script>
<script>
  var gameInstance = UnityLoader.instantiate(
    "gameContainer",
    "../../assets/dist/Build/Puzzle.json",
    { onProgress: UnityProgress }
  );
</script>
<body>
<div class="webgl-content">
  <div id="gameContainer" style="width: 960px; height: 700px"></div>
</div>
<script src="../../assets/dist/TemplateData/responsive.javascript"></script>
</body>
<div class="simmer">
Made by:
<a href="https://ppiconsulting.dev/" target="_blank"
  >Pier Paolo Ippolito</a
>
</div>
