import requests
import pytest

token = 'b37d5c607fb5327517cfe16e157a1412'
host = 'https://pokemonbattle.me:9104'

def test_status_code():
    answer = requests.get(f'{host}/trainers')
    assert answer.status_code == 200

def test_part_of_answer():
    answer_body = requests.get(f'{host}/trainers', params = {'trainer_id' : 4302})
    assert answer_body.json()['trainer_name'] == 'Мелик'