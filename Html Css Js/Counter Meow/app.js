

var input = document.getElementById("input");
var output = document.getElementById("output");
var counter = 0;

var click = function(event) {

    counter += 1;
    output.innerHTML = "Le has dado al MEOW " + counter + " veces!";

};

input.addEventListener("click", click);