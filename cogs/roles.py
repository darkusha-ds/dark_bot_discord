import discord, pytz
from datetime import datetime as dt
from discord.ext import commands
from main import *
from settings import *

class roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send(f"roles load {dt.now(pytz.timezone(region)).strftime(time_format)}")

    @commands.command(name='rols', aliases=aliaces_roles)
    async def get_roles_id(self, ctx):
        guild = bot.get_guild(763632193150779412)
        await ctx.send(guild.roles)

def setup(bot):
    bot.add_cog(roles(bot))
