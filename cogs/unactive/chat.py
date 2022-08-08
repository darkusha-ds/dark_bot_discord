import discord, datetime, random
from discord.ext import commands
from imports import *

hi_words = ["Всем ку"]
answ = ["no", "yes"]

class chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send(f"example load at {datetime.datetime.now(dt_reg).strftime('%Y-%m-%d %H:%M:%S')}")

    @bot.event
    async def on_message(ctx):
        msg = ctx.content
        msgs = ctx.content.lower()
        answer = random.choice(answ)
        if msg in hi_words or msgs if hi_words:
            await ctx.channel.send(answer)

def setup(bot):
    bot.add_cog(chat(bot))
