import random
from mal import Anime
from animegifs.distutils import gifs, errors

class Animegifs:

    def __init__(self):
        self.category = None

    def get_gif(self, category: str) -> str:
        """
        Insert a valid category and get a gif.

        Args:
            category (str): Valid categories: attack, bite, bloodsuck, blush, bonk,
                brofist, cry, cuddle, dance, disgust, exploding, facedesk, facepalm, flick, flirt,
                handhold, happy, harass, highfive, hug, icecream, insult, kill, kiss,
                lick, love, marry, nod, nosebleed, nuzzle, pat, peck, poke, popcorn, pout,
                punch, punish, random, run, sad, scared, shoot, shrug, sip, slap, smirk,
                sorry, spank, stare, steal-magic, tease, threat, tickle, tired, wave, yawn.

        Returns:
            gif: gif (url) -> str
        """
        if type(category) is int:
            raise errors.CategoryIntegral(category)
        if category.lower() in list(gifs.access().keys()) or category.lower() == 'random':
            if category.lower() == 'random':
                gif_list = []
                for key, gif_url in gifs.access().items():
                    for urls in gif_url:
                        gif_list.append(urls[0])
                gif = gif_list
            else:
                gifs_list = gifs.access()[category.lower()]
                gif = [gif_url[0] for gif_url in gifs_list]
            gif = random.choice(gif)
        elif category.lower() not in list(gifs.access().keys()):
            raise errors.CategoryError(category)
        else:
            raise errors.CategoryUnknown(category)
        return gif

    def get_mal(self, gif) -> str:
        """
        Return the myanimelist page of the gif's anime.

        Args:
            gif (url: str)

        Returns:
            mal: mal (url) -> str
        """
        for key, gif_url in gifs.access().items():
            for gif_name in gif_url:
                if gif_name[0] == gif:
                    result = gif_name[1]
                    try:
                        mal = f"https://myanimelist.net/anime/{int(result)}/"
                    except ValueError as exc:
                        raise errors.MethodNotUpdated(gif) from exc
                    return mal
            else:
                continue

    def get_malId(self, gif) -> int:
        """
        Return the myanimelist ID of the gif's anime.

        Args:
            gif (url: str)

        Returns:
            malid: malId -> int
        """
        for key, gif_url in gifs.access().items():
            for gif_name in gif_url:
                if gif_name[0] == gif:
                    result = gif_name[1]
                    try:
                        malid = int(result)
                    except ValueError as exc:
                        raise errors.MethodNotUpdated(gif) from exc
                    return malid
            else:
                continue

    def get_animetitle(self, gif) -> str:
        """
        Return the title of the gif's anime.

        Args:
            gif (url: str)

        Returns:
            title: title -> str
        """
        for key, gif_url in gifs.access().items():
            for gif_name in gif_url:
                if gif_name[0] == gif:
                    result = gif_name[1]
                    try:
                        title = Anime(int(result)).title
                    except ValueError as exc:
                        raise errors.MethodNotUpdated(gif) from exc
                    return title
            else:
                continue
