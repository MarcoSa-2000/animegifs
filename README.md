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

API wrapper for animegifs. Get random anime gifs by category. Use Python (intended (for now) for Discord).

WIP - updated in time to time.
Version below v1.0 will not have the gifs library updated anymore and the gifs may return 404 as they were hosted on Discord.
For troubleshoots, known errors and categories list, check below.

`pip install animegifs`

# HOW TO USE
```py
#v1.2.0>
from animegifs import animegifs

gifs = animegifs.Animegifs()

gif = gifs.get_gif(category) #gifs.get_gif('hug') and return the url of the gif.
mal = gifs.get_mal(gif) #get url of the gif's anime myanimelist page.
title = gifs.get_animetitle(gif) #get the title of the gif's anime.
malid = gifs.get_malId(gif) #get the ID of the gif's anime myanimelist page.
categories = gifs.get_categories() #get a list of available ctegories.
```

```py
#v0.6>
from animegifs import animegifs

gifs = animegifs.Animegifs()

user_input = input() #let user send any input and search if that input matches a category.
#if user_input == "nom":  #nom as category doesn't exist, but is similar to bite (as example)
#   user_input = "bite"
try:
    gif = gifs.get_gif(user_input) #return the url of the gif if the category exists.
except animegifs.errors.CategoryError:
    print("not a valid gif category.")
```

## Category list:

**A**
* Attack

**B**
* Bite, Bloodsuck, Blush, Bonk, Brofist

**C**
* Cry, Cuddle

**D**
* Dance, Disgust

**E**
* Exploding

**F**
* Facedesk, Facepalm, Flick, Flirt

**H**
* Handhold, Happy, Harass, Highfive, Hug

**I**
* Icecream, Insult

**K**
* Kill, Kiss

**L**
* Lick, Love

**M**
* Marry

**N**
* Nod, Nosebleed, Note, Nuzzle

**P**
* Pat, Peck, Poke, Popcorn, Pout, Punch, Punish

**R**
* Run

**S**
* Sad, Scared, Shoot, Shrug, Sip, Slap, Smack, Smirk, Sorry, Spank, Stare

**T**
* Tease, Threat, Tickle, Tired

**W**
* Wave

**Y**
* Yawn

**Special Category List**

* Random, Steal-magic

# Live API

You can test out the API (and lib functionality) on my bot's website here: https://enkidu-app.github.io/animegifs

# Submit a GIF

If you also want to contribute to the gifs collection, you can submit a gif at: https://forms.gle/wxWmRuy5VCdDCZWp8

# Troubleshooting and other

If you encounter an error, please raise an issue on the issue page: https://github.com/MarcoSa-2000/animegifs/issues. 
Alternatively, you can join my Discord server (https://discord.com/invite/TKZJ4GJj2z) to request new categories, functions, provide feedback, or report any errors. 
I do also have a multi-function Discord bot. Feel free to check out the web dashboard here: https://enkidu-app.github.io.

# Copyright

This repository doesn't include any copyrighted material. 
If you happen to come across any copyrighted content within this repository (but hosted elsewhere) that you own or represent, email me at **grest0grest@gmail.com**. 
Please provide specific details about the copyrighted material and where it can be found.
Once I confirm your claim, I'll take immediate action to remove the identified material.