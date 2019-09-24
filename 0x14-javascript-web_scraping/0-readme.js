#!/usr/bin/node
/* Import module fs to open and read a file */
const file = require('fs');
file.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
