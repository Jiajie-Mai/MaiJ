// Alex - Jiajie Mai, Alex Liu 
// SoftDev1 pd7
// K29 -- Sequential Progression II: Electric Boogaloo
// 2018-12-19

var fibonacci = function(n){
    if (n == 0) return 0;
    if (n <= 2) return 1;

    return fibonacci(n - 1) + fibonacci(n-2);
}

var displayFib = function(){
    var x = fibonacci(12);
    console.log(x);
}

var gcd = (a,b) => {
    if (!b){
	return a;
    }
    return gcd(b, a % b);
}

var displayGcd = () => {
    var x = gcd(135,81);
    console.log(x);
}

var students = ["MaiJ", "LiuA", "adayR", "aschJ","belkebirl","chenJ","chowdhuryJ"]

var randomStudent = function(){
     var index = parseInt(Math.random() * students.length);
  return students[index];
}

var displayStudent = function(){
    var x = randomStudent();
    console.log(x);
}

var but1 = document.getElementById("a");
but1.addEventListener("click", displayFib);

var but2 = document.getElementById("b");
but2.addEventListener("click", displayGcd);

var but3 = document.getElementById("c");
but3.addEventListener("click", displayStudent);
