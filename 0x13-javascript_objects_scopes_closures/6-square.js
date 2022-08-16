#!/usr/bin/node
const Rectan = require('./5-square');

module.exports = class Square extends Rectan {
  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    for (let index = 0; index < this.height; index++) {
      console.log(c.repeat(this.width));
    }
  }
};
