import discord, os, datetime, pytz, TenGiphPy, random, json, uuid, asyncio, traceback, time, itertools, sys, youtube_dl, typing, functools
from discord_together import DiscordTogether
from discord.ext import commands, tasks
from async_timeout import timeout
from discord.utils import get
from phrazes import *

# channel, where I can see bot time load
load_bot = 1008775005439545366  # test_server

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
mute_list = load_json(json_mute_list)