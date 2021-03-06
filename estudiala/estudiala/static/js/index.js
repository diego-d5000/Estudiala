window.onscroll = function(ev) {
	var B= document.body; //IE 'quirks'
    var D= document.documentElement; //IE with doctype

    D = window.pageYOffset;
	
	if (D == 0){
		document.getElementById("logo").setAttribute("src", "../../static/images/logo.png");
		document.getElementById("title").style.color = "#F44336";
		document.getElementById("rightBrand").style.color = "#F44336";
		document.getElementById("nav").style.backgroundColor = "transparent";
		document.getElementById("nav").style.boxShadow = "none";
	} else {
		document.getElementById("logo").setAttribute("src", "../../static/images/logowhite.png");
		document.getElementById("title").style.color = "#F9F9F9";
		document.getElementById("rightBrand").style.color = "#F9F9F9";
		document.getElementById("nav").style.backgroundColor = "#F44336";
		document.getElementById("nav").style.boxShadow = "0 2px 5px rgba(0, 0, 0, 0.26)";
	}
};

function showForms(form1, form2) {
	var form = document.getElementById(form1);
	var form2 = document.getElementById(form2);

	form.style.display = "block";
	form2.style.display = "none";
}

function close(form) {
	var form = document.getElementById(form);
	form.style.display = "none";
}