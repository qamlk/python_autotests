import requests

token = 'b37d5c607fb5327517cfe16e157a1412'
host = 'https://pokemonbattle.me:9104'
create = requests.post(f'{host}/pokemons', json =
                       {
                            "name": "Питонист 2",
                            "photo": "https://dolnikov.ru/pokemons/albums/012.png"
                            },
                       headers = {"Content-Type": "application/json", "trainer_token": token})
print(create.text, create.status_code)