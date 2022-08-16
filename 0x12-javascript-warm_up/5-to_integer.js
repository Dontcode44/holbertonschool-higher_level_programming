#!/usr/bin/node

const pars = parseInt(process.argv[2]);
if (!pars) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
