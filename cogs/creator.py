import discord
from discord.ext import commands
from main import *
from settings import *

class creator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command(name=comm_servers, aliaces=aliaces_servers)
    @commands.has_permissions(administrator=True)
    async def servers(self, ctx):
        activeservers = bot.guilds
        for guild in activeservers:
            await ctx.send(f"{guild.name} \n id: {guild.id}")
    
    @commands.command(name=comm_roles, aliases=aliaces_roles)
    async def get_roles_id(self, ctx):
        guild = bot.get_guild(763632193150779412)
        await ctx.send(guild.roles)
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def prikl(self, ctx, *, text = None):
        channel = bot.get_channel(870241377114533899)
        await channel.send(text)

def setup(bot):
    bot.add_cog(creator(bot))
