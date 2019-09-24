#!/usr/bin/node

const myUrl = process.argv[2];
const request = require('request');

request.get(myUrl, (err, res) => {
  if (err) {
    return console.error(err);
  }
  console.log('code: %s', res.statusCode);
});
