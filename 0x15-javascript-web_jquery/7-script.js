$.get('https://swapi.co/api/people/5/?format=json', function (data, textStatus) {
  $('#character').text(data.name);
};
