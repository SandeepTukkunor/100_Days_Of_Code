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



// functions

function calculateAge(birthYear){
    return 2018 - birthYear;
    

}

var ageSandeep = calculateAge(1997);
var ageMike = calculateAge(1948);
var ageJane = calculateAge(1969);
console.log(ageSandeep, ageMike, ageJane);



// calculte the years untill the retiremnet 
function yearUntillRetirement(birthYear, firstname){
    var age = calculateAge(birthYear);
    var retirement = 65- age;
    
    if (retirement >0){
        console.log(firstname + " retires in "+ retirement + " years");

    } else {
        console.log(firstname + " is already retired")
    }


}

yearUntillRetirement(1990, "john");
yearUntillRetirement(1948, "mike")
yearUntillRetirement(1969, "jane")





// * function Statements and expressions 

var whatDoYouDo = function(job, firstname){
    switch(job){
        case "teacher":
            return firstname + " teaches how to code"
        case "driver":
            return firstname + " drives a car in chennai"
        case "designer":
            return firstname + " Design beautiful websites"

        default:
            return firstname + " does something else"
    }
}


console.log(whatDoYouDo("designer", "sandeep")) 




// Arrays: collection of variables
var names = ["sandeep", "sunil", "Anil"];
var years = new Array(1997, 1999, 2001);
console.log(names[0])
console.log(names.length);
names[1] = "bhagyashree"
console.log(names)
names[names.length] = "Sunil"
console.log(names)




// different data types in arrays 

var john = ["john", "smith", 1990, "teacher", false];
john.push("blue"); // ads at the end 
john.unshift("mr"); // adds at the beginning 
john.pop() // removest the element from the end
john.shift() // removes the first element of the array 
console.log(john.indexOf(1990))
console.log(john);


var isDesigner = john.indexOf("designer") === -1 ? "john is not a designer ": "john is a designer"
console.log(isDesigner)





// coding challenge : tip calculator


function tipCalculator(bill) {
    var percentage;
    if (bill < 50) {

        percentage = 0.2;
    } else if (bill > 50 && bill < 200){
        percentage = 0.15;
    } else {
        percentage = 0.1;
    }
    return percentage * bill
}

var bills = [124, 48, 268];
var tips = [tipCalculator(bills[0]), tipCalculator(bills[1]), tipCalculator(bills[2])];
console.log(tips)



// * Objects and prorperties ** 

var john = {
    firstName :"John", 
    lastName : "Smith", 
    birthYear : 1990,
    family: ["jane", "mark", "bob", "Emily"],
    job : "teacher", 
    isMarried : false
};

console.log(john.firstName)
console.log(john["lastName"])


john.job = "designer";
john.isMarried = true;

console.log(john)



var jane  = new Object()
jane.lastName = "morris";
jane.birthYear = 1998;
jane.job = "web developer";
jane.isMarried = true;
console.log(jane)

 


// Methods

var john = {
    firstName :"John", 
    lastName : "Smith", 
    birthYear : 1990,
    family: ["jane", "mark", "bob", "Emily"],
    job : "teacher", 
    isMarried : false,
    calcAge: function (birthYear) {
        return 2018 - this.birthYear;
    }
};

john.age = john.calcAge()
console.log(john)


*/

// coading challenge objects and methods 

var john = {
    fullname : "john smith",
    mass : 92,
    height : 1.95,
    calcBMI : function(){
        this.bmi = this.mass / (this.height* this.height)
        return this.bmi
    }
}


var mark = {
    fullname : "Mark Miler",
    mass : 78,
    height : 1.69,
    calcBMI : function(){
        this.bmi = this.mass / (this.height* this.height)
        return this.bmi
    }
}



john.calcBMI();
mark.calcBMI();
console.log(john, mark)

if (john.bmi > mark.bmi) {
    console.timeLog(john.fullname + " has a higher BMI ");

}  else if (mark.bmi > john.bmi){
    console.log(mark.fullname + " has higher BMI")
} else {
    console.log("they have the same to same  BMI")
}





