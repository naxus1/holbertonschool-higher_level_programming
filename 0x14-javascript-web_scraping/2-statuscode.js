#!/usr/bin/node
/* Status code */
const myUrl = process.argv[2];
const request = require('request');

request.get(myUrl, (err, res) => {
  if (err) {
    return console.log(err);
  }
  console.log('code: %s', res.statusCode);
});
