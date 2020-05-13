#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const path = process.argv[3];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(path, body, 'utf-8', (err) => {
      if (err) { console.log(err); }
    });
  }
});
