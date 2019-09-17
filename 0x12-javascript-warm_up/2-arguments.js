#!/usr/bin/node
const argv_lenght = process.argv.length;
if (argv_lenght < 3) {
  console.log('No argument');
} else if (argv_lenght === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
