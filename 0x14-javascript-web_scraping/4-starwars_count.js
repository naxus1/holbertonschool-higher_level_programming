#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;
let iter;

request.get(url, (err, response, content) => {
  if (err) {
    return console.log(err);
  }
  let allContent = JSON.parse(content);
  let onlyFilms = allContent['results'];
  for (i = 0; i < onlyFilms.length; i++) {
    let characterList = onlyFilms[i]['characters'];
    for (let j = 0; j < charList.length; j++) {
      if (charList[j].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
})
