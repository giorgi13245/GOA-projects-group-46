let myNum = 10
let hisNum = Number(prompt("enter number"))
let btn = document.getElementById("btn")
btn.addEventListener("click" ,function(){
  myNum === hisNum ? console.log("you guessed my number") : console.log("you didnt guess my number")
})

let div = document.getElementById("div")
div.addEventListener("click", function(){
  div.style.backgroundColor = 'green'
  div.style.width = "600px"
  div.style.height = "600px"
})