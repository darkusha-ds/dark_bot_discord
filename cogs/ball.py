import imp
import discord, random, pytz
from datetime import datetime as dt
from discord.ext import commands
from main import *
from settings import *
from phrazes import *

class ball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send(f"ball load {dt.now(pytz.timezone(region)).strftime(time_format)}")

    @commands.command(name='ball', aliases=aliaces_ball)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def magic_eight_ball(self, ctx, *, arg=None):
        cci = ctx.channel.id
        if cci in channels:
            if arg is None:
                await ctx.channel.purge(limit=1)
                await ctx.send(
                    embed=discord.Embed(
                        color=0xff9900,
                        title=f'{ctx.author.name}#{ctx.author.discriminator}, **укажите пользователя**',
                        description=f'Пример: {pref}ball **вопрос**'
                ), delete_after=time_5s)
            else:
                embed = discord.Embed(color=discord.Colour.random(), title='')
                embed.add_field(name=arg, value=random.choice(phrazes.ball), inline=False)
                await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)

def setup(bot):
    bot.add_cog(ball(bot))
