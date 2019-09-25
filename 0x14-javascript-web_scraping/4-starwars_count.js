#!/usr/bin/node
let request = require('request');
const url = process.argv[2];
let counter = 0;
request(url, function (error, response, text) {
  let movies = JSON.parse(text).results;
  if (!error) {
    for (let cc in movies) {
      let ml = movies[cc].characters;
      for (let bc in ml) {
        if (ml[bc].includes('18')) {
          counter += 1;
        }
      }
    }
    console.log(counter);
  }
});
