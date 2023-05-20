import random
from animegifs.distutils import gifs, errors

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
            raise errors.CategoryIntegral(category)
        elif category.lower() in gifs.gifs_name_list:
            gifs_list = gifs.access()[category.lower()]
            gif = random.choice(gifs_list)
        elif category.lower() not in gifs.gifs_name_list:
            raise errors.CategoryError(category)
        else:
            raise errors.CategoryUnknown(category)
        return gif
        