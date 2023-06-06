# animegifs.py
<p align="center">
    <a href="https://pypi.org/project/animegifs/">
    <img src="https://img.shields.io/pypi/dm/animegifs?logo=PyPI&style=for-the-badge" alt="PyPi Downloads"/></a>
    <a href="https://discord.gg/TKZJ4GJj2z">
    <img src="https://img.shields.io/discord/856005478789677096?logo=Discord&style=for-the-badge" alt="Discord Server"/></a>
    <a href="https://pypi.org/project/animegifs/">
    <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/MarcoSa-2000/animegifs?style=for-the-badge"></a>
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/animegifs?logo=Python&logoColor=%23FFFF00&style=for-the-badge">
    <img alt="GitHub watchers" src="https://img.shields.io/github/watchers/MarcoSa-2000/animegifs?style=social">
</p>

Get random anime gifs by category. Use Python (intended (for now) for Discord).

WIP - updated in time to time. Versions below v0.5.3 aren't expected to work flawlessly or at all. Version below v0.6 will not have the gifs library updated anymore.

`pip install animegifs`

# HOW TO USE
```py
#v0.5.3>
from animegifs import animegifs

gifs = animegifs.Animegifs()

gif = gifs.get_gif(category) #return the url of the gif.
```

```py
#v0.6>
from animegifs import animegifs

gifs = animegifs.Animegifs()

gif = gifs.get_gif(category) #return the url of the gif.
mal = gifs.get_mal(gif) #get url of the gif's anime myanimelist page.
title = gifs.get_animetitle(gif) #get the title of the gif's anime.
malid = gifs.get_malId(gif) #get the ID of the gif's anime myanimelist page.
```

**Category list:** 

* Attack
* Bite
* Bloodsuck
* Blush
* Bonk
* Brofist
* Cry
* Cuddle
* Dance
* Disgust
* Exploding
* Facedesk
* Facepalm
* Flick
* Flirt
* Handhold
* Happy
* Harass
* Highfive
* Hug
* Icecream
* Insult
* Kill
* Kiss
* Lick
* Love
* Marry
* Nod
* Nosebleed
* Nuzzle
* Pat
* Peck
* Poke
* Popcorn
* Pout
* Punch
* Punish
* Run
* Sad
* Scared
* Shoot
* Shrug
* Sip
* Slap
* Smirk
* Sorry
* Spank
* Stare
* Tease
* Threat
* Tickle
* Tired
* Wave
* Yawn

**Special Category List**

* Random
* Steal-magic

# Troubleshooting and other

If you encounter an error raise an issue on the issue page: https://github.com/MarcoSa-2000/animegifs/issues 
or join the discord server to request new categories, new functions, feedback and even errors.
