import discord, os, datetime, pytz, TenGiphPy, random, json, uuid
from discord.ext import commands
from discord.utils import get
from discord_together import DiscordTogether
from random import shuffle
from typing import Union
from datetime import datetime as dt
from phrazes import *

# channel, where I can see bot time load
load_bot = 1008775005439545366  # test_server

# roles from servers
role = [
    # midgard
    791830818385297409,        # Активный болтун
    791827665886642247,        # Топчег
    904885228542234664,        # VIP
    874495163274252289,        # Малыши-Викинги
    874500630507569234,        # Бывалые Воины
    874501130653138965,        # Вольфхеднары
    874501540726063166,        # Берсеки
    874503002688483378,        # Ассы
    874511898052276225,        # Древние
    874514040657961050,        # ХОЗЯИН ВСЕГО СУЩЕГО
    791824007666204714,        # Страж
    794739618528493608,        # Сыщик
    792131111979450419,        # Ленивая жепа
    791822957697564742,        # Важный человек
    791829976957059083,        # This is cookie
    791958424497160202,        # Жена старшего
    791804288871039006,        # Старшой
    794824368945365004,        # Server booster
    # test server
    # 726483138548858933,        # Админы
    # 726484481799618602,        # Главный Админ
    # 726483340831490050,        # Участники
    # смертные
    939858722824548372,        # everyone
    # DoDoshka 2.0
    870237741739302912,        # everyone
    # Ksusha's server
    763632193150779412,        # everyone
]

def load_json(filename):
    with open(filename, encoding="utf-8") as infile:
        return json.load(infile)

def write_json(filename, content):
    with open(filename, "w") as outfile:
        json.dump(content, outfile, ensure_ascii=False, indent=4)

prefix = load_json(json_prefix)
roles = load_json(json_roles)
channels = load_json(json_channels)
owners = load_json(json_owners)
mute_roles = load_json(json_mutes)