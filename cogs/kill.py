import discord, random, pytz
from datetime import datetime as dt
from discord.ext import commands
from main import *
from settings import *
from phrazes import *

class kill(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send(f"kill load {dt.now(pytz.timezone(region)).strftime(time_format)}")

    @commands.command(name="kill", aliases=aliaces_kill)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def kill(self, ctx, *, member: discord.Member = None):
        mam = ctx.author.mention  # тег автора
        mum = member.mention  # тег участника
        cci = ctx.channel.id
        if cci in channels:
            if member is None:
                await ctx.channel.purge(limit=1)
                await ctx.send("Error", delete_after=time_5s)
            else:
                if member == ctx.author:
                    await ctx.channel.purge(limit=1)
                    await ctx.send("Ошибка, вы не можете использовать эту команду против себя", delete_after=time_10s)
                else:
                    await ctx.send(random.choice(phrazes.kill).format(mam, mum))
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)

def setup(bot):
    bot.add_cog(kill(bot))