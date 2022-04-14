#!/usr/bin/node
const request = require('request');
const args = process.argv;

const option = {
  url: args[2],
  method: 'GET'
};

request(option, function (err, res, body) {
  res.setEncoding('utf8');
  if (!err) {
    // console.log (`${res.body}`);
  }
  const fstat = require('fs');
  fstat.writeFile(args[3], res.body, err => {
    if (err) {
      console.error(err);
    }
  });
});
