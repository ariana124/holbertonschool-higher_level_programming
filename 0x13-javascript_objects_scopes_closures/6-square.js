#!/usr/bin/node
// Creates the Square class and prints it using the letter c

const square = require('./5-square');
module.exports = class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
};
