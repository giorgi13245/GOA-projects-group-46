let btn = document.getElementById("btn")
let form = document.getElementById("form")
btn.addEventListener("click", function(e){
    e.preventDefault()

    console.log(form.name.value)
    console.log(form.pass.value)
})