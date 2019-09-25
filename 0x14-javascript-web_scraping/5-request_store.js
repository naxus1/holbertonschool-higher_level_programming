#!/usr/bin/node
let fs = require('fs');
let request = require('request');
const url = process.argv[2];
const path = process.argv[3];
request(url).pipe(fs.createWriteStream(path, 'utf8'));
