#!/usr/bin/node
// Script that writes a string to a file

const fs = require('fs');
const file = process.argv[2];
const text = process.argv[3];
fs.writeFile(file, text, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
