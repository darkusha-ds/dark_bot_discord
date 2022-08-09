import discord, random, pytz
from datetime import datetime as dt
from discord.ext import commands
from main import *
from settings import *

class prikl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send(f"prikl load {dt.now(pytz.timezone(region)).strftime(time_format)}")

    @commands.command()
    async def prikl(self, ctx, *, chan, text = None):
        if chan == 1: #smer
            channel = bot.get_channel(939864015037935760)
            await channel.send(text)
        elif chan == 2: #test server
            channel = bot.get_channel(726482240506298378)
            await channel.send(text)

def setup(bot):
    bot.add_cog(prikl(bot))
