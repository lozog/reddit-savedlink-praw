// requires nano.js

function refreshDB() {
  ajxpgn('mainlisting', '/getSavedLinks?', false, false, '', function() {
    console.log('done retrieving data');
  });
}
