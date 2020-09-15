/*

var firstname = "Sandeep";
console.log(firstname);

var lastname = "Tukkunor";
var age = 23;

var fullAge = true;
console.log(fullAge);


var job;
console.log(job);
//these are the variables 
/*
this is how multiline commenting is done 

job = "teacher";
console.log(job) // will taje var job as input  






// variable mutation and type correction 

var firstname = "Sandeep";
var age = 28;

console.log(firstname + " " , age);


var job, isMarried;

job = "teacher";
isMarried = false;

console.log(firstname + " is a " + age + " years old " + job + " is he a married? " + isMarried );


// variable mutatipns

age = 'twenty eight';
job = "student"


//alert(firstname + " is a " + age + " years old " + job + " is he a married? " + isMarried );


var lastname = prompt("what is your last name?")
console.log(firstname + " " + lastname)



//basic math operators


var year , yearJohn, yearMark;

now = 2018;
ageJohn = 28;
ageMark = 33;


yearJohn = now - ageJohn;
yearMark= now- ageMark;

console.log(yearJohn);

console.log(now +2);
console.log(now *2);
console.log(now/2);

// logical operators
var johnOlder = ageJohn > ageMark;

console.log(johnOlder);



// Type of operator 
console.log(typeof johnOlder);
console.log(typeof ageJohn)

console.log(typeof "Mark is older")



// operator percedence 

var now = 2018;
var yearJohn = 1998;
var fullAge = 18;

var isFullAge = now - yearJohn >= fullAge;
console.log(isFullAge);   

// Grouping 
var ageJohn = now - yearJohn;
var ageMark = 35;

var average = (ageJohn + ageMark)/2;

console.log(average);

// Grouping and multiple assignment 
var x, y;
x = y = (3+5) * 4 -6;
console.log(x, y)


//more operators 
x = x +2 ;
x += 2;
console.log(x)



// coading challenge 

var massMark = 78; //kg
var heightMark = 1.69; //meters 

var massJohn = 92;
var heightJohn = 1.95;

var bmiMark = massMark / (heightMark*heightMark);

var bmiJohn = massJohn / (heightJohn* heightJohn);

console.log(bmiMark, bmiJohn)

var markheigherBMI = bmiMark > bmiJohn;


console.log("is Marks\'s Bmi higher than Johns\'s" + markheigherBMI)



// if and else statements 

var firstname = "John";
var civilstatus = "single";
var isMarried = true;


if ( isMarried){
    console.log(firstname + " is  married ");

} else {
    console.log(firstname + " is not married");
}



var massMark = 78; //kg
var heightMark = 1.69; //meters 

var massJohn = 92;
var heightJohn = 1.95;

var bmiMark = massMark / (heightMark*heightMark);

var bmiJohn = massJohn / (heightJohn* heightJohn);

console.log(bmiMark, bmiJohn)
if (bmiMark<bmiJohn) {
    console.log("marks is higher then john");
} else {
    console.log("nothing")
}

//var markheigherBMI = bmiMark > bmiJohn;



//console.log("is Marks\'s Bmi higher than Johns\'s" + markheigherBMI)




//******Boolean logic ******


var firstname = "John";
var age = 16;

if (age<13){
    console.log(firstname + " is a boy ");
} else if (age >= 13 && age <20){
    console.log(firstname + " is a teenager ");
} else {
    console.log(firstname + " he is a adult");
}



// ternary operators

var firstname = "john";
var age = 16;

age >= 18 ? console.log(firstname + " drinks whater")
: console.log(firstname + " does not drink water ") ;

var drink = age > 18 ? "beer" : "juice";

console.log(drink);



//ternary is alternative for if and else satatemensts 


//switch statemens 

var job = "teacher";
switch (job) {
    case "teacher":
        console.log(firstname + " tecaches coading");
        break
    case "driver":
        console.log(firstname + " he drives a car ");
        break
    
}




age = 56;

switch(true) {
    case age <13:
        console.log("he is still a child");
        break
    case age >= 13 && age < 20:
        console.log("he is a teeager ");
        break
    case age >= 20 && age <30:
        console.log("he is a young man ");
        break
    default:
        console.log("he is man")
}






// trurhy and falsy values and equally operators 

var height;
height = 23;
if (height || height === 0 ) {
    console.log("variable is defined");


} else {
    console.log("variable not defined")
}

// equality opeator

if (height == "23"){
    console.log("the == opertaor does type cohersion");

}



//coading challeneg 2

var scoreJohn = (89+ 120+ 103)/3;
var scoreMike = (116+ 94+ 123)/3;
var scoreMary = (97+ 134+105)/3;

console.log(scoreJohn, scoreMike, scoreMary);
if (scoreJohn > scoreMike && scoreJohn > scoreMary){
    console.log("john wins the game");
} else if (scoreMike > scoreJohn && scoreMike > scoreMary){
    console.log("mike wins the game")
} else if (scoreMary > scoreJohn && scoreMary > scoreMike){
    console.log("mary wins the game ")
} else {
    console.log("its a draw")
}



// if (scoreJohn > scoreMike) {
//     console.log("John wins the game");
// } else if (scoreMike > scoreJohn){
//     console.log("mike wins the game");
// } else {
//     console.log("the match is drawn");
// }

*/

// functions

function calculateAge(birthYear){
    return 2018 - birthYear;
    

}





