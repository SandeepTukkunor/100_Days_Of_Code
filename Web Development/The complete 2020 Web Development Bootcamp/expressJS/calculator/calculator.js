const express = require("express");


const bodyparser = require("body-parser");

const app = express();
app.use(bodyparser.urlencoded({ extended: false }));

app.get("/", function(request, respones) {
    respones.sendFile(__dirname + "/index.html");

});


app.post("/", function(request, respones) {
    var num1 = request.body.num1;
    var num2 = request.body.num2;
    var result = parseInt(num1) + parseInt(num2);

    respones.send("Result of the calsulation is " + result);
});

app.get("/bmiCalculator", function(request, respones) {

    respones.sendFile(__dirname + "/bmiCalculator.html");
})

app.post("/bmiCalculator", function(request, respones) {
    var weight = parseFloat(request.body.weight);
    var height = parseFloat(request.body.height);
    var result = weight / (height * height);
    
    respones.send("Your BMI is " + result);
})


app.listen(3000, function(){
    console.log("server started in port 3000")
}); 
