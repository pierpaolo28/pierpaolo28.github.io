var readingBar = document.getElementById("reading-bar");
	addEventListener("scroll", function(event){
		var total = document.body.scrollHeight - window.innerHeight;
      // console.log(total);
      // console.log(scrollY);
		var percent = (window.scrollY / total) * 100;

    if (percent < 3)
      readingBar.style.display = "none";
    else
      readingBar.style.display = "block";

		if (percent > 4)
			readingBar.style.width = percent + "%";

		if (percent > 85)
			readingBar.className = "finished";
		else
			readingBar.className = "";
	});
