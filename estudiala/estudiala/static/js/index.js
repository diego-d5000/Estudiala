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

function coursesGrid () {
	var colors = ["#F44336","#E91E63","#9C27B0","#672AB7","#3F51B5","#2196F3","#03A9F4","#00BCD4","#009688","#4CAF50","#8BC34A","#CDDC39","#009688","#FFC107","#FF9800","#FF5722","#795548","#9E9E9E","#607D8B"];
	var elements = document.getElementsByClassName("Estudiala-course");

	for (var i = elements.length - 1; i >= 0; i--) {
		var height = elements[i].style.width;
		var random = Math.floor(Math.random() * colors.length);
		var color = colors[random];
		elements[i].style.backgroundColor = color;
	};
}

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