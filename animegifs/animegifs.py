from .dis_utils import gifs
import random

class Animegifs():

    def __init__(self, category=None):
        if category is None:
            raise Exception("No category has been specified.")
        else:
            self.category = category

    def get_gif(self):
        if self.category == 'attack' or self.category == 'attacc':
            gif = random.choice(gifs.attack)
        elif self.category == 'bite':
            gif = random.choice(gifs.bite)
        elif self.category == 'bloodsuck':
            gif = random.choice(gifs.bloodsuck)
        elif self.category == 'blush':
            gif = random.choice(gifs.blush)
        elif self.category == 'bonk':
            gif = random.choice(gifs.bonk)
        elif self.category == 'brofist':
            gif = random.choice(gifs.brofist)
        elif self.category == 'cry':
            gif = random.choice(gifs.cry)
        elif self.category == 'cuddle':
            gif = random.choice(gifs.cuddle)
        elif self.category == 'dance':
            gif = random.choice(gifs.dance)
        else:
            raise Exception("Not a valid category.")
        return gif
