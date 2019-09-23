#!/usr/bin/node
const myList = require('100-data.js').list;
console.log(myList);
let myArray = mylist.map(function (x, i) {
  return x * i;
});
console.log(myArray);
