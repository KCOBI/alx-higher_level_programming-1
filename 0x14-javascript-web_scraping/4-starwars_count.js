#!/usr/bin/node

const request = require('request');
const args = process.argv;

const option = {
  url: args[2],
  method: 'GET'
};

let meh = 0;
request(option, function (err, res, body) {
  if (!err) {
    const jfile = JSON.parse(body);
    // console.log (jfile.results);
    jfile.results.forEach(element => {
      if (
        element.characters.includes('https://swapi-api.hbtn.io/api/people/18/')
      ) {
        meh++;
      }
    });
  }
  console.log(meh);
});
