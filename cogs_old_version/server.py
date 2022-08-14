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

    @commands.command(name=comm_server, aliases=aliaces_server)
    # @commands.has_any_role(*roles)
    # @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def server(self, ctx):
        guild = ctx.guild
	
        await ctx.send(f'Server Name: {guild.name}')
        await ctx.send(f'Server Size: {len(guild.members)}')
        await ctx.send(f'Server Name: {guild.owner.display_name}')

def setup(bot):
    bot.add_cog(server(bot))
