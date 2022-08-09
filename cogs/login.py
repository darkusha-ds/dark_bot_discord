import discord, random, pytz
from datetime import datetime as dt
from discord.ext import commands
from main import *
from settings import *
from phrazes import *

class login(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send(f"login load {dt.now(pytz.timezone(region)).strftime(time_format)}")

    @commands.command(name="enter", aliases=aliaces_login)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def enter(self, ctx):
        mam = ctx.author.mention  # тег автора
        cci = ctx.channel.id
        if cci in channels:
            await ctx.send(random.choice(phrazes.login).format(mam))
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)

def setup(bot):
    bot.add_cog(login(bot))
