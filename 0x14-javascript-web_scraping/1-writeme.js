#!/usr/bin/node

const fs = require('fs');
const myFile = process.argv[2];
const content = process.argv[3];

fs.writeFile(myFile, content, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
