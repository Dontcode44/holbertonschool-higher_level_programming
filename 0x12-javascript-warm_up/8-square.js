#!/usr/bin/node

const place = process.argv[2];

if (isNaN(place)) {
  console.log('Missing size');
} else {
  for (let sq = 0; sq < parseInt(place); sq++) {
    console.log('X'.repeat(parseInt(place)));
  }
}
