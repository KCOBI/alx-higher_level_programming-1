#!/usr/bin/node

const fstat = require('fs');

const args = process.argv;

fstat.writeFile(args[2], args[3], err => {
  if (err) {
    console.error(err);
  }
});
