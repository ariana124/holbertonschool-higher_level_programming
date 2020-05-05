#!/usr/bin/node
// Checks if the arg passed can be converted to an integer
const number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number ' + number);
}
