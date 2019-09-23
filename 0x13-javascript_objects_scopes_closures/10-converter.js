#!/usr/bin/node
exports.converter = function (base) {
  this.base = base;
  function numconv (number) {
    return number.toString(this.base);
  }
  return numconv;
};
