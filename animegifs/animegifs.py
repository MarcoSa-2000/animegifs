import random
from animegifs.dis_utils import gifs

class Animegifs():

    def __init__(self):
        self.category = None

    def get_gif(self, category=None):
        if category is None:
            raise Exception("No category has been specified.")
        else:
            if category == 'attack' or category == 'attacc':
                gif = random.choice(gifs.access()[0])
            elif category == 'bite':
                gif = random.choice(gifs.access()[1])
            elif category == 'bloodsuck':
                gif = random.choice(gifs.access()[2])
            elif category == 'blush':
                gif = random.choice(gifs.access()[3])
            elif category == 'bonk':
                gif = random.choice(gifs.access()[4])
            elif category == 'brofist':
                gif = random.choice(gifs.access()[5])
            elif category == 'cry':
                gif = random.choice(gifs.access()[6])
            elif category == 'cuddle':
                gif = random.choice(gifs.access()[7])
            elif category == 'dance':
                gif = random.choice(gifs.access()[8])
            elif category == 'disgust':
                gif = random.choice(gifs.access()[9])
            elif category == 'facedesk':
                gif = random.choice(gifs.access()[10])
            elif category == 'facepalm':
                gif = random.choice(gifs.access()[11])
            elif category == 'flick':
                gif = random.choice(gifs.access()[12])
            elif category == 'flirt':
                gif = random.choice(gifs.access()[13])
            elif category == 'handhold':
                gif = random.choice(gifs.access()[14])
            elif category == 'happy':
                gif = random.choice(gifs.access()[15])
            elif category == 'harass':
                gif = random.choice(gifs.access()[16])
            elif category == 'highfive':
                gif = random.choice(gifs.access()[17])
            elif category == 'hug':
                gif = random.choice(gifs.access()[18])
            elif category == 'icecream':
                gif = random.choice(gifs.access()[19])
            elif category == 'insult':
                gif = random.choice(gifs.access()[20])
            elif category == 'kill':
                gif = random.choice(gifs.access()[21])
            elif category == 'kiss':
                gif = random.choice(gifs.access()[22])
            elif category == 'lick':
                gif = random.choice(gifs.access()[23])
            else:
                raise Exception("Not a valid category. You can check valid categories at: https://github.com/MarcoSa-2000/animegifs")
        return gif
        