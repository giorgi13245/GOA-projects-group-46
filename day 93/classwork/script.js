let btn = document.getElementById("loginbtn")
let div = document.getElementById("div")
let form = document.getElementById("form")
let photos = [
    "https://th.bing.com/th/id/OIP.rKJG7UYCM2u2w5nm7pZBpAHaLH?w=128&h=192&c=7&r=0&o=7&pid=1.7&rm=3",
    "https://th.bing.com/th/id/OIP.H16qEA7qO-s9u75504DPhAHaLH?w=128&h=192&c=7&r=0&o=7&pid=1.7&rm=3",
    "https://th.bing.com/th/id/OIP.hLTThhxHPeGqFQVjpD1-hwHaE8?w=288&h=192&c=7&r=0&o=7&pid=1.7&rm=3"
]

btn.addEventListener("click" , function(e){
    e.preventDefault()

    if(form.name.value != " " && form.pass.value != " "){
        div.innerHTML += `
        <img src="${photos[Math.floor(Math.random * 2)]}" alt="pic">`
    }
})

