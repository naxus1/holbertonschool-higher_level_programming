#!/usr/bin/node
const lenArgv = process.argv.length;

if (lenArgv < 3) {
  console.log('undefined is undefined');
} else if (lenArgv === 3) {
  console.log(process.argv[2] + ' is undefined');
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
