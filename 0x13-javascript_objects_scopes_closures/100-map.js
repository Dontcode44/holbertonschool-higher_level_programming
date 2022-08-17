#!/usr/bin/node

const data = require('./100-data.js').list;

const list = data.map((index, list) => index * list);
console.log(data);
console.log(list);
