#!/usr/bin/node

const request = require('request');
const args = process.argv;

const option = {
  url: args[2],
  method: 'GET'
};

request(option, function (err, res, body) {
  if (!err) {
    console.log(`code: ${res.statusCode}`);
  }
});
