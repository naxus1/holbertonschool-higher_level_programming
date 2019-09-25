#!/usr/bin/node

const myUrl = process.argv[2];
const idObj = {};
const request = require('request');

request.get(myUrl, function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  let json = JSON.parse(body);
  for (let i = 0; i < json.length; i++) {
    let flag = 0;
    let idNum = json[i]['userId'];
    let compTasks = json[i]['completed'];
    if (!(idObj.hasOwnProperty(idNum))) {
      if (compTasks === false) {
        idObj[idNum] = 0;
      } else if (compTasks === true) {
        flag = 1;
        idObj[idNum] = 1;
      }
    }
    if (idObj.hasOwnProperty(idNum) && compTasks === true && flag !== 1) {
      idObj[idNum] += 1;
    }
  }
  console.log(idObj);
});
