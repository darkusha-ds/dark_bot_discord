import discord, random
from discord.ext import commands
from main import *
from settings import *
from phrazes import *

class server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))

    

def setup(bot):
    bot.add_cog(server(bot))
