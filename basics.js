// let a=BigInt(12);
// let b = false;
// console.log(a+b);
// console.log(typeof(a+b));

// const prompt = require('prompt-sync')();

// let a = " Hey whats your age? ";
// a = Number.parseInt(a);
// console.log(typeof a);

// if (a > 0) {
//     console.log("Hi!");
// } else {
//     console.log("Invalid age");
// }


for(let i in "qwlknqf"){
    console.log(i)                  //print index, work fine in objects
}
for(let i of "qwlknqf"){
    console.log(i)                  //prints characters, works fine in arrays
}