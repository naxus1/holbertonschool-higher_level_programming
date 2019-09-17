#!/usr/bin/node
const argv_lenght = process.argv.length;

if (argv_lenght < 3) {
  console.log('undefined is undefined');
} else if (argv_lenght === 3) {
  console.log(process.argv[2] + ' is undefined');
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
