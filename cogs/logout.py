import discord, random
from discord.ext import commands
from main import *
from settings import *
from phrazes import *

class logout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command(name="exit", aliases=aliaces_logout)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def ex(self, ctx):
        mam = ctx.author.mention  # тег автора
        cci = ctx.channel.id
        if cci in channels:
            await ctx.send(random.choice(phrazes.logout).format(mam))
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)

def setup(bot):
    bot.add_cog(logout(bot))
