#!/usr/bin/node
const lenArgv = process.argv.length;
if (lenArgv < 3) {
  console.log('No argument');
} else if (lenArgv === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
