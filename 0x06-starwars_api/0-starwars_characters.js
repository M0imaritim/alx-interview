#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];

request(
  `https://swapi-api.hbtn.io/api/films/${filmId}`,
  function (err, res, body) {
    if (err) {
      console.error(err);
      process.exit(1);
    }

    const actors = JSON.parse(body).characters;
    printInOrder(actors, 0);
  }
);

function printInOrder (actors, index) {
  if (index === actors.length) return;
  request(actors[index], function (err, res, body) {
    if (err) {
      console.error(err);
      process.exit(1);
    }

    console.log(JSON.parse(body).name);
    printInOrder(actors, index + 1);
  });
}
