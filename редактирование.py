import requests

token = 'b37d5c607fb5327517cfe16e157a1412'
host = 'https://pokemonbattle.me:9104'
edit = requests.put(f'{host}/pokemons', json =
                       {
                            "pokemon_id": "12492",
                            "name": "Питонист ред 2",
                            "photo": "https://dolnikov.ru/pokemons/albums/014.png"
                            },
                       headers = {"Content-Type": "application/json", "trainer_token": token})
print(edit.text, edit.status_code)