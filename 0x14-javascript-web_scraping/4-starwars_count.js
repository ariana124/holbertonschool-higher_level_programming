#!/usr/bin/node
// Script that prints the number of movies where the character Wedge Antilles is present

let count = 0;
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).results;
    for (const film of data) {
      for (const role of film.characters) {
        if (role.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
