#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let index = 0; index < this.height; index++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const he = this.height;
    this.height = this.width;
    this.width = he;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
