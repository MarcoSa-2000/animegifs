from animegifs.distutils import errors
import requests
import urllib.parse

version = "v3"

def request_api(type, arg):
    try:
        if arg is not None:
            arg = urllib.parse.quote(arg)
    except TypeError:
        raise errors.ArgumentError
    if type == "get_gif":
        gif_url = requests.get(f"https://animegifs-enkidu.koyeb.app/{version}/api/?category={arg}")
        if gif_url.status_code != 200:
            raise errors.CategoryError
        data = gif_url.json()
        gif = data['gif']
        return gif
    elif type == "get_mal":
        gif_mal = requests.get(f"https://animegifs-enkidu.koyeb.app/{version}/get_mal/?gif={arg}")
        data = gif_mal.json()
        mal = data['mal']
        return mal
    elif type == "get_mal_id":
        gif_mal_id = requests.get(f"https://animegifs-enkidu.koyeb.app/{version}/get_malid/?gif={arg}")
        data = gif_mal_id.json()
        mal_id = data['mal_id']
        return mal_id
    elif type == "get_animetitle":
        gif_animetitle = requests.get(f"https://animegifs-enkidu.koyeb.app/{version}/get_animetitle/?gif={arg}")
        data = gif_animetitle.json()
        animetitle = data['animetitle']
        return animetitle
    elif type == "get_categories":
        categories = requests.get(f"https://animegifs-enkidu.koyeb.app/{version}/get_categories")
        if categories.status_code != 200:
            raise errors.APIError
        data = categories.json()
        categories = data['categories']
        return categories

class Animegifs:

    def __init__(self):
        self.category = None

    def get_gif(self, category: str) -> str:
        """
        Insert a valid category and get a gif.

        Args:
            category (str): Valid categories: attack, bite, bloodsuck, blush, bonk,
                brofist, cry, cuddle, dance, disgust, exploding, facedesk, facepalm, flick, flirt, french_kiss,
                handhold, happy, harass, highfive, hug, icecream, insult, kill, kiss,
                lick, love, marry, nod, nosebleed, note, nuzzle, pat, peck, poke, popcorn, pout,
                punch, punish, random, run, sad, scared, scold, shoot, shrug, sip, slap, smack, smirk,
                sorry, spank, stare, steal-magic, tease, threat, tickle, tired, wave, yawn.

        Returns:
            gif: gif (url) -> str
        """
        gif = request_api("get_gif", category)
        return gif

    def get_mal(self, gif) -> str:
        """
        Return the myanimelist page of the gif's anime.

        Args:
            gif (url: str)

        Returns:
            mal: mal (url) -> str
        """
        mal = request_api("get_mal", gif)
        if mal is None:
            raise errors.GifError
        return mal

    def get_malId(self, gif) -> int:
        """
        Return the myanimelist ID of the gif's anime.

        Args:
            gif (url: str)

        Returns:
            mal_id: mal_id -> int
        """
        mal_id = request_api("get_mal_id", gif)
        if mal_id is None:
            raise errors.GifError
        return mal_id

    def get_animetitle(self, gif) -> str:
        """
        Return the title of the gif's anime.

        Args:
            gif (url: str)

        Returns:
            title: title -> str
        """
        animetitle = request_api("get_animetitle", gif)
        if animetitle is None:
            raise errors.GifError
        return animetitle
    def get_categories(self) -> list:
        """
        Return the list of the available categories.

        Returns:
            categories: categories -> list
        """
        categories = request_api("get_categories", None)
        return categories
