#!/usr/bin/node
// Prints 'C is fun' x times
let number = process.argv[2];
number = parseInt(number);

if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
