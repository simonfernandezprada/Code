var display = document.getElementById("display").getContext("2d"); // we declare the variable display as = to the canvas element and then we get the context of that canvas element

display.canvas.height = 400; // this one seems to be the position eventhough tut guy says its  
display.canvas.width = 800; // the size of the canvas.

display.fillStyle = "#264b96"; // it fills the background of the canvas
display.fillRect(0, 0, 800, 400); //takes the fill color and extends it on a rectangle

display.strokeStyle = "#ffffff"; // the color of the line
display.lineJoin = "round"; // the border of the line joint, it could be round or miter which is pointy
display.lineWidth = 4; //this is the size of the line

display.fillStyle = "#f9a73e"; // sets the color to paint the triangle
display.beginPath(); // begins the drawing of the triangle
display.moveTo(10,10); // drags the pen
display.lineTo(10,90); // drags the pen
display.lineTo(90,10); // drags the pen
display.closePath(); // closes the drawing brings you back to the start point
display.fill();  // paints the triangle
display.stroke(); // draws the outline

display.beginPath(); //begins the drawing
display.moveTo(0, 400); // (hor place, ver place, they start at the topleft, )
display.bezierCurveTo(80, 0, 80, 180, 160, 90, 180, 160);

display.stroke();

display.fillStyle = "#bf212f"; //sets the color of the shape
display.beginPath();//begins the drawing
display.rect(280, 300, 500, 80);//(horizontal place, vertical place, hor lenght, ver height)
display.fill();// fills color of the shape
display.stroke();// displays the outline

display.fillStyle = "#006f3c"; //sets color of drawing
display.beginPath(); // begins the drawing
display.arc(650, 190, 90, 0, Math.PI*2); //(horizontal place, vertical place, size, begnning of drawing, end of drawing)
display.fill(); // fills color of the shape
display.stroke(); // displays the outline

