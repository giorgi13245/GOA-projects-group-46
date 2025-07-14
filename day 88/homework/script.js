let name = "giorgi"
let btn = document.getElementById("btn")
btn.addEventListener("click", function(){
    console.log(`Hello ${name}`)
})

let numbr = 0
let btn1 = document.getElementById("btn1")
btn1.addEventListener("click", function(){
    console.log(numbr)
    num+=2
})