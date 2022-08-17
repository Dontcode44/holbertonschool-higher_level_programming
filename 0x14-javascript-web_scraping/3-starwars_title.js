#!/usr/bin/node

const axios = require('axios').default;

axios.get('https://swapi-api.hbtn.io/api/films/:id')
  .then(function (response) {
    console.log('code: ' + response.status);
  })
  .catch(function (error) {
    // handle error
    console.log('code: ' + error.response.status);
  });
