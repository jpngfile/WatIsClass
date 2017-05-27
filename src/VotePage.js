var currentPage = 0;
var pictures = [
	["../img/blackCat.jpg",
	"../img/catPair.jpg",
	"../img/furryCat.jpg",
	"../img/tallCat.jpg",
	"../img/catBall.jpg",
	"../img/blackCat.jpg",
	"../img/catPair.jpg",
	"../img/furryCat.jpg",
	"../img/tallCat.jpg",
	"../img/catBall.jpg"
	],
	["../img/tallCat.jpg",
	"../img/catBall.jpg",
	"../img/furryCat.jpg",
	"../img/tallCat.jpg",
	]
]

function printId(id){
	console.log(id);
}

function flipPage(increment){
	var numPages = pictures.length;
	if (currentPage + increment >= numPages || currentPage + increment < 0){
		console.log ("No page available");
		return;
	}
	currentPage = currentPage + increment;
	var pictureContainer = document.getElementById('notes-container');
	pictureContainer.innerHTML = '';
	for (var i = 0; i < pictures[currentPage].length; i++){
		var img = document.createElement('img');
		img.src = pictures[currentPage][i];
		img.alt = "cat pic";
		img.width = "500";
		img.onclick = function() { addBorder(this); };
		img.id = "pic" + (i+1).toString();
		pictureContainer.appendChild(img);
	}
}

function addBorder(element){
	console.log("add border");
	console.log(currentPage);
	var pictureStackSize = pictures[currentPage].length;
	for (var i = 1; i <= pictureStackSize; i++){
		var id = "pic" + i.toString();
		var pic = document.getElementById(id);
		pic.style.border = null;
	}
	element.style.border = "5px solid red";
}