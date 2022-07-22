import random
import json
from urllib.request import urlopen

def access():
    url = 'https://github.com/MarcoSa-2000/marcosa-2000.github.io/raw/main/utils/animegifs_project/gifs.json'
    response = urlopen(url)
    data = json.loads(response.read())

    attack = data['attack']  #0
    bite = data['bite']  #1
    bloodsuck = data['bloodsuck']  #2
    blush = data['blush']  #3
    bonk = data['bonk']  #4
    brofist = data['brofist']  #5
    cry = data['cry']  #6
    cuddle = data['cuddle']  #7
    dance = data['dance']  #8
    disgust = data['disgust']  #9
    facedesk = data['facedesk']  #10
    facepalm = data['facepalm']  #11
    flick = data['flick']  #12
    flirt = data['flirt']  #13
    handhold = data['handhold']  #14
    happy = data['happy']  # 15
    harass = data['harass']  # 16

    del data

    return attack, bite, bloodsuck, blush, bonk, brofist, cry, cuddle, dance, disgust, facedesk, facepalm, flick, \
           flirt, handhold, happy, harass

class Animegifs():

    def __init__(self, category=None):
        if category is None:
            raise Exception("No category has been specified.")
        else:
            self.category = category

    def get_gif(self):
        if self.category == 'attack' or self.category == 'attacc':
            gif = random.choice(access()[0])
        elif self.category == 'bite':
            gif = random.choice(access()[1])
        elif self.category == 'bloodsuck':
            gif = random.choice(access()[2])
        elif self.category == 'blush':
            gif = random.choice(access()[3])
        elif self.category == 'bonk':
            gif = random.choice(access()[4])
        elif self.category == 'brofist':
            gif = random.choice(access()[5])
        elif self.category == 'cry':
            gif = random.choice(access()[6])
        elif self.category == 'cuddle':
            gif = random.choice(access()[7])
        elif self.category == 'dance':
            gif = random.choice(access()[8])
        elif self.category == 'disgust':
            gif = random.choice(access()[9])
        elif self.category == 'facedesk':
            gif = random.choice(access()[10])
        elif self.category == 'facepalm':
            gif = random.choice(access()[11])
        elif self.category == 'flick':
            gif = random.choice(access()[12])
        elif self.category == 'flirt':
            gif = random.choice(access()[13])
        elif self.category == 'handhold':
            gif = random.choice(access()[14])
        elif self.category == 'happy':
            gif = random.choice(access()[15])
        elif self.category == 'harass':
            gif = random.choice(access()[16])
        else:
            raise Exception("Not a valid category.")
        return gif
