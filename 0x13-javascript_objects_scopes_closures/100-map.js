#!/usr/bin/node
const myList = require('100-data.js').list;
const myArray = myList.map((i, k) => i * k);
console.log(myList);
console.log(myArray);
