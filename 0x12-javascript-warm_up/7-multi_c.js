#!/usr/bin/node

const arr = process.argv[2];

if (isNaN(arr)) {
  console.log('Missing number of occurrences');
} else {
  for (let a = 0; a < parseInt(arr); a++) {
    console.log('C is fun');
  }
}
