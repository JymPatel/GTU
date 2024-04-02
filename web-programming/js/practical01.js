// Declare and assign variables
let num1 = 5;
let num2 = 3;
let name = "Shree Swami Atmanand Saraswati Institute of Technology";
let code = 76;
let averageSPI = 5.2;
let recommanded = false;

// Operators and expressions
let result1 = num1 + num2 * 2;
let result2 = num2 / 3 - 5;

// Looping in JavaScript
for (let i = 0; i < 5; i++) {
  document.write("Loop iteration: " + (i + 1) + "<br>");
}

// Declare an array
let fruits = ["Apple", "Banana", "Orange"];

// User-defined function
function greet(name) {
  return "Hello, " + name + "!";
}

// Built-in function
let upperCaseFruit = fruits[0].toUpperCase();
document.write(upperCaseFruit+ "<br>");

let joinedFruits = fruits.join(", ");
document.write(joinedFruits+ "<br>");

let indexOrange = fruits.indexOf("Orange");
document.write(indexOrange+ "<br>");

fruits.push("Mango");
document.write(fruits + "<br>");

let removedFruit = fruits.pop();
document.write(fruits+ "<br>");

let slicedFruits = fruits.slice(0, 2);
document.write(slicedFruits+ "<br>");

let numAsString = "123";
document.write(numAsString+ "<br>");

let parsedNumber = parseInt(numAsString);
document.write(parsedNumber+ "<br>");

let fixedNumber = (3.14159).toFixed(2);
document.write(fixedNumber+ "<br>");

// Dialog boxes
alert("The result of the expression is: " + result1);
let userName = prompt("Please enter your name:");
alert(greet(userName));
confirm("Press OK to see the joined fruits: " + joinedFruits);
alert("Fruits: " + joinedFruits);
