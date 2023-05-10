import random
from animegifs.distutils import gifs, errors

gifs_dict = {"attack": random.choice(gifs.access()[0]),
             "bite": random.choice(gifs.access()[1]),
             'bloodsuck': random.choice(gifs.access()[2]),
             'blush': random.choice(gifs.access()[3]),
             'bonk': random.choice(gifs.access()[4]),
             'brofist': random.choice(gifs.access()[5]),
             'cry': random.choice(gifs.access()[6]),
             'cuddle': random.choice(gifs.access()[7]),
             'dance': random.choice(gifs.access()[8]),
             'disgust': random.choice(gifs.access()[9]),
             'facedesk': random.choice(gifs.access()[10]),
             'facepalm': random.choice(gifs.access()[11]),
             'flick': random.choice(gifs.access()[12]),
             'flirt': random.choice(gifs.access()[13]),
             'handhold': random.choice(gifs.access()[14]),
             'happy': random.choice(gifs.access()[15]),
             'harass': random.choice(gifs.access()[16]),
             'highfive': random.choice(gifs.access()[17]),
             'hug': random.choice(gifs.access()[18]),
             'icecream': random.choice(gifs.access()[19]),
             'insult': random.choice(gifs.access()[20]),
             'kill': random.choice(gifs.access()[21]),
             'kiss': random.choice(gifs.access()[22]),
             'lick': random.choice(gifs.access()[23])
             }

class Animegifs:

    def __init__(self):
        self.category = None

    def get_gif(self, category: str) -> str:
        """
        Insert a valid category and get a gif.

        Args:
            category (str): Valid categories: attack, bite, bloodsuck, blush, bonk,
                brofist, cry, cuddle, dance, disgust, facedesk, facepalm, flick, flirt,
                handhold, happy, harass, highfive, hug, icecream, insult, kill, kiss,
                lick.

        Returns:
            gif: gif (url) -> str
        """
        if type(category) is int:
            raise errors.CategoryIntegral
        elif category.lower() in gifs_dict:
            gif = gifs_dict[category.lower()]
        else:
            raise errors.CategoryError
        return gif
        