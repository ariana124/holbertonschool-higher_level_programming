// Script that fetches and replaces the name of this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data, status) {
  if (status === 'success') {
    $('#character').text(data.name);
  }
});
