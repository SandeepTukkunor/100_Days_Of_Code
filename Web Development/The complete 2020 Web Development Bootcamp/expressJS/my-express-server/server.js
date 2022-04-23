const express = require("express");
const app = express()

app.get("/", function(request, response){
    response.send("<h1>Hello World</h1>");
})


app.get("/contact",  function(request, response){
    response.send("contact me at @SandeepTukkunor")
})

app.get("/about", function(request, response){
    response.send("I am Sandeep And I study at Indian Institute of technolgy Madras ")

})

app.get("/hobbies", function(request, response){
    response.send("<ul><li>Coffee </li><li>Tea</li><li>Milk </li></ul>")
})
app.listen(3000, function(){
    console.log("server started in port 3000")
}); 
