#!/usr/bin/node

const { list } = require('./100-data.js');

const data = require('./100-data.js').list;

const list = data.map((index, list) => index * list);
console.log(data);
console.log(list);
