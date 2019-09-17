#!/usr/bin/node
const repeats = process.argv[2];
let iter = 0;
if (isNaN(parseInt(repeats))) {
  console.log('Missing number of occurrences');
} else {
  while (iter < repeats) {
    console.log('C is fun');
    iter++;
  }
}
