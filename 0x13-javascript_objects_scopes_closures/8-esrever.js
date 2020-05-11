#!/usr/bin/node
// Function that returns the reversed version of a list

exports.esrever = function (list) {
  const array = [];
  for (let i = 0; i < list.length; i++) {
    array.unshift(list[i]);
  }
  return array;
};
