#!/usr/bin/node

const request = require('request');
const episode = process.argv[2];
const endpoint = 'http://swapi.co/api/films/' + episode;

request(endpoint, (err, response, content) => {
  if (err) {
    console.log(err);
  } else {
    const allContent = JSON.parse(content);
    console.log(allContent.title);
  }
});
