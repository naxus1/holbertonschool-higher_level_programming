#!/usr/bin/node
const url = process.argv[2];
const file = process.argv[3];
const request = require('request');

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const fs = require('fs');
  fs.writeFile(file, body, 'utf8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
