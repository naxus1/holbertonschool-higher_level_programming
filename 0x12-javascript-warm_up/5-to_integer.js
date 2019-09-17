#!/usr/bin/node
let num = parseInt(process.argv[2], 10);
if (isNaN(num) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
