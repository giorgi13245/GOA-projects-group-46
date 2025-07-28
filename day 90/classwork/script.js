let name1 = "giorgi"
let btn = document.getElementById("btn")
btn.addEventListener("click", function(){
    console.log(`Hello ${name1}`)
})

//scope არის რამდენად ხელმისაწვდომია ცვლადი, არსებობს სამი სკოუპი, 
// global scope ნიშნავს იმას რომ ეს ცვლადი ყველგან ხელმისაწვდომია,
// block scope ცვლადები ხელმისაწვდომია მხოლოდ იმ კოდის ბლოკში სადაც შეიქმნა,
// function scope ცვლადები ხელმისაწვდომია მხოლოდ იმ ფუნცქციაში რომელშიც შეიქმნა

let number = 2025
let btn1 = document.getElementById("btn1")
btn1.addEventListener("click", function(){
    number+=2
    console.log(number)
})