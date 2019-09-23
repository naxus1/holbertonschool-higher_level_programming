#!/usr/bin/node
let myCount = 0;
exports.logMe = function (item) {
  console.log(myCount + ': ' + item);
  myCount++;
};
