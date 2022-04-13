#!/usr/bin/node

const args = process.argv;
const fs = require('fs');
fs.readFile(args[2], 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  }
  console.log(data);
});
