import json
import requests

gifs_name_list = ["attack",
                  "bite", 'bloodsuck', 'blush', 'bonk', 'brofist',
                  'cry', 'cuddle',
                  'dance', 'disgust',
                  'facedesk', 'facepalm', 'flick', 'flirt',
                  'handhold', 'happy', 'harass', 'highfive', 'hug',
                  'icecream', 'insult',
                  'kill', 'kiss',
                  'lick', 'love',
                  'marry',
                  'nosebleed', 'nuzzle']

def access():
    data = requests.get("https://objectstorage.eu-frankfurt-1.oraclecloud.com/p/zDPowf1lXXMMpXzo_Lnb31IOtUyxrtD-kDS7fpKxLuCYnR5xr-171Tyz0tW0EhKV/n/frqs54dqeajn/b/animegifs_lib/o/gifs.json").content
    data = json.loads(data)

    return data
