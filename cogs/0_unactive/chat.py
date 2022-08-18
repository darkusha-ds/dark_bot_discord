import discord, datetime, random
from discord.ext import commands
from main import *
from settings import *

hi_words = ["Всем ку"]
answ = ["no", "yes"]

class chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))

    @bot.event
    async def on_message(ctx):
        msg = ctx.content
        msgs = ctx.content.lower()
        answer = random.choice(answ)
        if msg in hi_words or msgs in hi_words:
            await ctx.channel.send(answer)

def setup(bot):
    bot.add_cog(chat(bot))
