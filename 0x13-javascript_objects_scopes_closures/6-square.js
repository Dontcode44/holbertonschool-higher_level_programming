#!/usr/bin/node
const Rectangl = require('./5-square');

module.exports = class Square extends Rectangl {
  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    for (let index = 0; index < this.height; index++) {
      console.log(c.repeat(this.width));
    }
  }
};
