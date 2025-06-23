//N1
let x=Number(prompt("Enter number"))
i=0
while(i<x){
    console.log(i)
    i++
}

//N2
let a=prompt("enter name")
while(a.length<10){
    a = prompt("Try again")
}

//N3
let pincode = Number(prompt("enter pincode"))
while(pincode != 6446){
    pincode = Number(prompt("Enter again"))
}

//N4
let pass = prompt("Enter password")
while(pass != "ვანიჩკა"){
    pass = prompt("Wrong password, try again")
}