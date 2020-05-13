#!/usr/bin/node
// Script that prints all characters of a Star Wars movie

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body).characters;
    for (const character of movie) {
      request(character, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          const name = JSON.parse(body).name;
          console.log(name);
        }
      });
    }
  }
});
