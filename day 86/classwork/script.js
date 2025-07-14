//N1
let list1 = [1,23,546,5334,444,23,4,67,2]

for(let i of list1){
    console.log(i)
}

//N2
let strng = "adrvswefg"
for(let i of strng){
    console.log(i)
}

//N3
let objct = {
    name : "nika",
    surname : "boloshvili",
    age : 67
}

for(let i in objct){
    console.log(i)
    console.log(objct[i])
}

//N4
//block scope-ტიპის ცვლადები, არიან let და const, როდესაც მათ შევქმნით {აქ} (ფუნქციის გარდა), მათზე წვდომა ფრჩხილებს გარეთ არ გვაქ
//global scope-არის var, ხელმისაწვდომია ყველგან შექმნის დროს (ფუნქციის გარდა)
//function scope- არის სამივე keyword-ით შექმნილი, ეს იმას ნიშნავს რომ ფუნქციაში შექმნილ არანაირ ცვლადზე არ გვაქ წვდომა მის გარეთ



