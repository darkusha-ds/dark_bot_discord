import discord
from discord.ext import commands
from main import *
from settings import *

class servers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command(name="servers", aliaces=aliaces_servers)
    @commands.has_permissions(administrator=True)
    async def servers(self, ctx):
        activeservers = bot.guilds
        for guild in activeservers:
            await ctx.send(f"{guild.name} \n id: {guild.id}")

def setup(bot):
    bot.add_cog(servers(bot))
