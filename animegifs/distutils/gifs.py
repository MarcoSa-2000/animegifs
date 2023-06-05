import json
import requests
import jwt
from animegifs.distutils import errors

global TOKEN
TOKEN = None
gifs_name_list = ["attack",
                  "bite", 'bloodsuck', 'blush', 'bonk', 'brofist',
                  'cry', 'cuddle',
                  'dance', 'disgust',
                  'exploding',
                  'facedesk', 'facepalm', 'flick', 'flirt',
                  'handhold', 'happy', 'harass', 'highfive', 'hug',
                  'icecream', 'insult',
                  'kill', 'kiss',
                  'lick', 'love',
                  'marry',
                  'nod', 'nosebleed', 'nuzzle',
                  'pat', 'peck', 'poke', 'popcorn', 'pout', 'punch', 'punish',
                  'random', 'run',
                  'sad', 'scared', 'shoot', 'shrug', 'sip', 'slap', 'smirk', 'sorry', 'spank', 'stare',
                  'tease', 'threat', 'tickle', 'tired',
                  'wave',
                  'yawn']

def authentication():
    try:
        response = requests.post("https://enkidu-app-5a3qq2fqya-uc.a.run.app/key1", timeout=10)
    except requests.exceptions.Timeout:
        try:
            response = requests.post("https://enkidu-app-5a3qq2fqya-uc.a.run.app/key1", timeout=25)
        except requests.exceptions.Timeout as exc:
            raise errors.AuthTimeout(exc)
    if response.status_code == 200:
        auth_key = response.json()['key']
    else:
        exc = response.status_code
        raise errors.AuthError(exc)
    return auth_key

def access():
    global TOKEN
    if TOKEN:
        data = jwt.decode(TOKEN, "enkidu-key", algorithms="HS512")
        data = list(data.keys())
        data = requests.get(data[0]).content
        data = json.loads(data)
    else:
        TOKEN = authentication()
        data = jwt.decode(TOKEN, "enkidu-key", algorithms="HS512")
        data = list(data.keys())
        data = requests.get(data[0]).content
        data = json.loads(data)

    return data
