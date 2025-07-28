const form = document.getElementById("myForm")
const result = document.getElementById("result")

form.addEventListener("submit", function(e){
    e.preventDefault();

    const name = form.name.value
    const surname = form.surname.value
    let date = form.date.value
    date = date.split("-")

    let obj = {
    "01" : "january",
    "02" : "february",
    "03" : "march",
    "04" : "april",
    "05" : "may",
    "06" : "june",
    "07" : "july",
    "08" : "august",
    "09" : "september",
    "10" : "october",
    "11" : "november",
    "12" : "december",
}


    result.innerHTML += `
    <p>Your Fullname is: ${name} ${surname}, Your were born in ${date[0]}, Your birth of month is ${obj[date[1]]}, Your day of birth is ${date[2]}</p>
    `
})