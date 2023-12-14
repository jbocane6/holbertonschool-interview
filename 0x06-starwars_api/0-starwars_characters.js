#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name by line in the same order of the list “characters”
// in the /films/ response
// You must use the Star wars API
// You must use the module request

// Require request which includes put() function
const API_URL = "https://swapi-api.hbtn.io/api/films/";

const pelicula = process.argv.slice(2);
url_con_elicula = API_URL.concat(pelicula);

async function getCharacters() {
  try {
    const response = await fetch(url_con_elicula);
    const characters = await response.json();

    for (var i = 0; i < characters.characters.length; i++) {
      const rutas_personajes = characters.characters[i];
      const response = await fetch(rutas_personajes);
      const personajes = await response.json();
      console.log(personajes.name);
    }
    //console.log(characters)
  } catch (error) {
    console.error("no ingrese datos erroneos");
  }
}
getCharacters();
