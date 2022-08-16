#!/usr/bin/node

exports.addMeMaybe = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction.call();
  }
};
