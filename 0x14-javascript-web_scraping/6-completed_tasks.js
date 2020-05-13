#!/usr/bin/node
// Script that computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const completed = {};
  const tasks = JSON.parse(body);
  for (const task of tasks) {
    if (task.completed === true) {
      if (task.userId in completed) {
        completed[task.userId]++;
      } else {
        completed[task.userId] = 1;
      }
    }
  }
  console.log(completed);
});
