#!/usr/bin/node

const request = require('request');
const args = process.argv;

const option = {
  url: 'https://swapi-api.hbtn.io/api/films/' + args[2],
  method: 'GET'
};

request(option, function (err, res, body) {
  if (!err) {
    console.log(`${JSON.parse(body).title}`);
  }
});
