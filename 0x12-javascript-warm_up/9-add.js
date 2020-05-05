#!/usr/bin/node
// Prints the sum of two integers
function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

let a = process.argv[2];
a = parseInt(a);
let b = process.argv[3];
b = parseInt(b);
add(a, b);
