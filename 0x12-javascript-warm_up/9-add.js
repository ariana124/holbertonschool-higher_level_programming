#!/usr/bin/node
// Prints the sum of two integers
function add(a, b) {
  let sum = a + b
  console.log(sum);
}

let a = parseInt(process.argv[2]);
let b = parseInt(process.argv[3]);
add(a, b);
