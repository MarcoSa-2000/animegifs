import json
from urllib.request import urlopen

url = 'https://github.com/MarcoSa-2000/animegifs/raw/main/animegifs/dis_utils/gifs.json'
response = urlopen(url)
data = json.loads(response.read())

attack = data['attack']
bite = data['bite']
bloodsuck = data['bloodsuck']
blush = data['blush']
bonk = data['bonk']
