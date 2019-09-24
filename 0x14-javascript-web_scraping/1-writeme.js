#!/usr/bin/node
const fs = require('fs');
const myFile = process.argv[2];
const content = process.argv[3];
fs.writeFile(myFile, content, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  }
});
