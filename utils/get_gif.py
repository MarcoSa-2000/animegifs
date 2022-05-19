from utils import gifs
import random

def get_gif(category = None):
    if category is None:
        raise Exception("No category has been specified.")
    else:
        if category == 'attack' or category == 'attacc':
            gif = random.choice(gifs.attack)
            
    return gif
