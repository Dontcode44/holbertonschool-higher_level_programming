#!/usr/bin/node

exports.esrever = function (list) {
  const revr = new Array;
  for (var i = list.length - 1; i >= 0; i--) {
    revr.push(list[i]);
  }
  return revr;
};
