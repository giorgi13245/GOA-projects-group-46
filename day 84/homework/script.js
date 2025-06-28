let num = Number(prompt("Enter number"))
let i = 0
while(i<num){
    console.log("hello")
    i++
}

//N2
function guessNum(num1){
    let num2 = Number(prompt("Enter number 1-10"))
    switch(num1){
        case num1===num2:
            console.log("ყოჩაღ, შენ გამოიცანი")
            break
        case num1 != num2:
            console.log("ვერ გამოიცანი")
            break
        default:
            num2 = Number(prompt("მიუთითე რიცხვი!!!"))
    }
}

//N3
function ageRestrictedDiscount(age){
    if(age>50){
        console.log("შენ მიიღე 50% ფასდაკლება")
    }else if(age>19){
        console.log("შენ მიიღე 10% ფასდაკლება")
    }else{
        console.log("შენ მიიღე 30% ფასდაკლება")
    }
}