//N1
for (let i=2; i<21; i+=2) {
    console.log(i)
}

//N2
let x="strings"
for(let i=0; i<x.length; i++){
    console.log(x.at(i))
}

//N3
let y=[1,2,3,4,5,6,78,8,99,7]
for(let i=0; i<y.length; i++){
    console.log(i%2==0 ? y.at(i) : "Not on odd index") 
}

//N4
let i=0
while(i<51){
    if(i%2===0){
        console.log(i)
        i++
    }else{
        i++
    }
}

//N5
let res = 0
let i2=0
while(i2<81){
    if(i2%2===0){
        res+=i2
        i2++
    }else{
        i2++
    }
}
console.log(res)