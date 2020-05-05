#!/usr/bin/node
// Prints a square
let size = process.argv[2];
size = parseInt(size);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < size; x++) {
    for (let y = 0; y < size; y++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
