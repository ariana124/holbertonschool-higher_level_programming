#!/usr/bin/node
// Checks if the arg passed can be converted to an integer
let number = process.argv[2];
number = parseInt(number);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
