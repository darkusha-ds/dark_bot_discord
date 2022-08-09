import discord, pytz
from datetime import datetime as dt
from discord.ext import commands
from random import shuffle
from typing import Union
from main import *
from settings import *

alphabet = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
numbers = list('1234567890')
symbols = list('!@#$%^&*()_+~=[]}{:;/<>-')

class pg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send(f"pg load {dt.now(pytz.timezone(region)).strftime(time_format)}")

    @commands.command(aliases=aliaces_pg)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def password(self, ctx, type=None, length: Union[int]=None):
        cci = ctx.channel.id
        if type is None:
            await ctx.channel.purge(limit=1)
            await ctx.send('Напишите уровень защиты: `1` , `2` или `3`', delete_after=time_10s)
        elif length is None:
            await ctx.channel.purge(limit=1)
            await ctx.send('Напишите длину пароля (от 8 до 32)', delete_after=time_10s)
        else:
            if cci in channels:
                if type == '1' and 8 <= length <= 32:
                    shuffle(alphabet)
                    await ctx.send(''.join(alphabet[:length]))

                elif type == '2' and 8 <= length <= 32:
                    spass = alphabet + numbers
                    shuffle(spass)
                    await ctx.send(''.join(spass[:length]))

                elif type == '3' and 8 <= length <= 32:
                    spass = alphabet + numbers + symbols
                    shuffle(spass)
                    await ctx.send(''.join(spass[:length]))
                else:
                    await ctx.send(
                        f'{ctx.author.mention}  \nОшибка, доступны только 3 уровня сложности: `1` , `2` , `3` , и длина пароля от `8` до `32` символов', delete_after=time_10s)
            else:
                await ctx.channel.purge(limit=1)
                await ctx.send(error_message, delete_after=time_10s)

def setup(bot):
    bot.add_cog(pg(bot))
