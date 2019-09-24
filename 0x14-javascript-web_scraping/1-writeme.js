#!/usr/bin/node
/* Write a script that writes a string to a file. */
const f = require('fs');
const myFile = process.argv[2];
const content = process.argv[3];
f.writeFile(myFile, content, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  }
});
