import discord, random
from datetime import datetime as dt
from discord.ext import commands
from main import *
from settings import *
from phrazes import *

class example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send(f"{comm_example} load {dt.now(pytz.timezone(region)).strftime(time_format)}")

    @commands.command(name='example', aliases=aliaces_example)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def example(self, ctx):
        mam = ctx.author.mention
        # mum = member.mention
        cci = ctx.channel.id
        if cci in channels:
            await ctx.send("{0}, Hi".format(mam))
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)

def setup(bot):
    bot.add_cog(example(bot))
