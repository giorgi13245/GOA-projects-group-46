let b = "random"
console.log(b ? "name" : "no name")

let a = "random2"
console.log(a.length<7 ? "more than 7" : "Less than 7")

let c = prompt("enter random word")
console.log(c==="random word" ? "good job" : "told you to enter random word")

let d = Number(prompt("enter num"))
let e = Number(prompt("enter num"))
console.log(d%e===0 ? "dividable" : "not what I expected")

let f = Number(prompt("enter num"))
let g = Number(prompt("enter num"))
console.log(f-g>4 ? `${f-g}>4` : `${f-g}<4`)

let h = prompt("enter your name")
console.log(h.toLowerCase()==="giorgi" ? "I am giorgi too" : `Im not ${h}`)
