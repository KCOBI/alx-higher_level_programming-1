#!/usr/bin/node

const request = require('request');
const args = process.argv;

const option = {
  url: args[2],
  method: 'GET'
};

request(option, function (err, res, body) {
  if (!err) {
    // console.log (res.statusCode);
    // console.log (body);
    // console.log (`${JSON.parse (body)[0]['userId']}`);
  } else {
    console.log(err);
    return;
  }
  const bodyx = JSON.parse(body);
  const userids = [];
  const final = {};
  bodyx.forEach(element => {
    if (!userids.includes(element.userId)) {
      userids.push(element.userId);
    }
  });
  // console.log ('user_ids: ', user_ids);
  userids.forEach(element => {
    final[element.toString()] = 0;
  });
  //  console.log ('final: ', final);

  bodyx.forEach(element => {
    if (element.completed) {
      final[element.userId.toString()]++;
    }
  });
  console.log(final);

  userids.forEach(element => {
    if (final[element.toString()] === 0) {
      console.log('smaking');
      // final[element.toString()];
    }
  });
});
