import json
import requests

def access():
    data = requests.get("https://objectstorage.eu-frankfurt-1.oraclecloud.com/p/zDPowf1lXXMMpXzo_Lnb31IOtUyxrtD-kDS7fpKxLuCYnR5xr-171Tyz0tW0EhKV/n/frqs54dqeajn/b/animegifs_lib/o/gifs.json").content
    data = json.loads(data)

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
    highfive = data['highfive']  # 17
    hug = data['hug']  # 18
    icecream = data['icecream']  # 19
    insult = data['insult']  # 20
    kill = data['kill']  # 21
    kiss = data['kiss']  # 22
    lick = data['lick']  # 23

    del data

    return attack, bite, bloodsuck, blush, bonk, brofist, cry, cuddle, dance, disgust, facedesk, facepalm, flick, \
           flirt, handhold, happy, harass, highfive, hug, icecream, insult, kill, kiss, lick


