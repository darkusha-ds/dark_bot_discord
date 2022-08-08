import discord, datetime, random
from discord.ext import commands
from main import *
from settings import *

class example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send(f"example {load_text}")

    @commands.command(name='example', aliases=["ex"])
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def example(self, ctx):
        # mam = ctx.author.mention
        # mum = member.mention
        cci = ctx.channel.id
        if cci in channels:
            await ctx.send("Hi")
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send("Ошибка, вы пишете не в том канале", delete_after=time_10s)

def setup(bot):
    bot.add_cog(example(bot))
