import requests

token = 'b37d5c607fb5327517cfe16e157a1412'
host = 'https://pokemonbattle.me:9104'
in_pokeball = requests.post(f'{host}/trainers/add_pokeball', json =
                       {
                            "pokemon_id": "12492"
                            },
                       headers = {"Content-Type": "application/json", "trainer_token": token})
print(in_pokeball.text, in_pokeball.status_code)