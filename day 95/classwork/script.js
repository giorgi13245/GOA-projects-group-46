const input = document.getElementById("inp")
const equal = document.getElementById("equal")

const display = function(num){
    input.value += num
}

const equation = function(){
    try{
        input.value = eval(input.value)
    } catch(Error) {
        input.value = "Error"
    };
    
}

const clearDisplay = function(){
    input.value = ""
}

const deleted = function(){
    if (input.value.length>0){
        input.value = input.value.slice(0, -1)
    }
}

const OddOrEven = function(){
    try{
        if(Number(input.value)%2===0){
            input.value = "Even"
        }else{
            input.value = "Odd"
        }
    }catch(Error){
        input.value = "Error"
    }
}

