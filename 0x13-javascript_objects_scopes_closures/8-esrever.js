#!/usr/bin/node
exports.esrever = function (list) {
  let a = list.length - 1;
  const mylist = [];

  while (a >= 0) {
    mylist.push(list[a]);
    a--;
  }
  return (mylist);
};
