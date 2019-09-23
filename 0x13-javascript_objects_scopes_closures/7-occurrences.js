#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let mycount = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      mycount++;
    }
    i++;
  }
  return (mycount);
};
