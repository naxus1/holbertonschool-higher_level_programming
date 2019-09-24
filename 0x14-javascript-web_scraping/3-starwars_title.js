#!/usr/bin/node

const request = require('request');
const episode = process.argv[2];
const endpoint = 'http://swapi.co/api/films/' + episode;

request.get(endpoint, (err, response, content) => {
  if (err) {
    console.error(err);
  }
  const allContent = JSON.parse(content);
  console.log(allContent.title);
});
