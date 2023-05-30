#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const movieURL = 'https://swapi-api.alx-tools.com/api/films/' + movieID + '/';

function requestURL (url) {
  return new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function getCharacterNames () {
  const body = await requestURL(movieURL);
  const characters = body.characters;

  for (let i = 0; i < characters.length; i++) {
    const character = await requestURL(characters[i]);
    console.log(character.name);
  }
}

getCharacterNames();
