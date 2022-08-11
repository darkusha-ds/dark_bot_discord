import discord, pytz, random
from datetime import datetime as dt
from discord.ext import commands
from main import *
from settings import *


class clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send(f"clear load {dt.now(pytz.timezone(region)).strftime(time_format)}")

    @commands.command(name='clear', aliases=aliaces_clear)
    async def clear(self, ctx, amount: int):
        if ctx.author.id in admins_id:
            await ctx.channel.purge(limit=amount)
            await ctx.send(
                embed=discord.Embed(description=f':white_check_mark: Удалено {amount} сообщений', color=discord.Colour.random()), delete_after=time_10s)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send("You aren't bot admin", delete_after=time_5s)

def setup(bot):
    bot.add_cog(clear(bot))
