#!/usr/bin/node
const numFact = process.argv.slice(2);
let res = 0;

function factorial (n) {
  if (n === 1) {
    return 1;
  } else {
    return (factorial(n - 1) * n);
  }
}
if (!numFact[0]) {
  res = 1;
} else {
  res = factorial(numFact[0]);
}
console.log(res);
