#!/usr/bin/node

const data = require('./100-data.js').list;

const map = data.map((index, lists) => index * lists);
console.log(data);
console.log(map);
