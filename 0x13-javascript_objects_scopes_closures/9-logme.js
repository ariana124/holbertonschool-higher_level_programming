#!/usr/bin/node
// Function that prints the arguent count

let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
