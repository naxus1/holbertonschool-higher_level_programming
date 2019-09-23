#!/usr/bin/node
const myList = require('./100-data.js').list;
console.log(myList);
const myArray = myList.map((curray, start) => curray * start);
console.log(myArray);
