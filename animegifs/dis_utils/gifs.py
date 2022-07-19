import json
from urllib.request import urlopen

url = 'https://github.com/MarcoSa-2000/marcosa-2000.github.io/raw/main/utils/animegifs_project/gifs.json'
response = urlopen(url)
data = json.loads(response.read())

attack = data['attack']
bite = data['bite']
bloodsuck = data['bloodsuck']
blush = data['blush']
bonk = data['bonk']
brofist = data['brofist']
cry = data['cry']
cuddle = data['cuddle']
dance = data['dance']
disgust = data['disgust']
facedesk = data['facedesk']
facepalm = data['facepalm']
flick = data['flick']
flirt = data['flirt']
handhold = data['handhold']
