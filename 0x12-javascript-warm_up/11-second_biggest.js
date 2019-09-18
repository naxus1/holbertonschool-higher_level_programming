#!/usr/bin/node
const arrayNums = process.argv.slice(2);
let maxNum = 0;

if (arrayNums.length > 1) {
  arrayNums.sort();
  maxNum = arrayNums[arrayNums.length - 2];
}
console.log(maxNum);
