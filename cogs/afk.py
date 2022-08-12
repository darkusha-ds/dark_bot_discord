import discord, pytz
from datetime import datetime as dt
from discord.ext import commands
from main import *
from settings import *

afk_pref = "[AFK]"

class afk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send(f"afk load {dt.now(pytz.timezone(region)).strftime(time_format)}")

    @commands.command(name='afk', aliases=aliaces_afk, pass_context=True)
    @commands.has_any_role(*roles)
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def afk(self, ctx):
        current_nick = ctx.author.nick
        move_1 = current_nick.replace("[AFK]", "") # all letters in English
        move_2 = move_1.replace("[AFК]", "")       # K in Russian
        move_3 = move_2.replace("[АFK]", "")       # A in Russian
        move_4 = move_3.replace("[АFК]", "")       # A and K in Russian
        move_5 = move_4.replace("[AФK]", "")       # A and K in English
        move_6 = move_5.replace("[AФК]", "")       # K in Russian
        move_7 = move_6.replace("[АФK]", "")       # A in Russian
        old_nick = move_7.replace("[АФК]", "")     # all letters in Russian
        cci = ctx.channel.id
        if cci in channels:
            if "[AFK]" in current_nick or "[AFК]" in current_nick or "[АFK]" in current_nick or "[АFК]" in current_nick or \
               "[AФK]" in current_nick or "[AФК]" in current_nick or "[АФK]" in current_nick or "[АФК]" in current_nick:
                await ctx.author.edit(nick=old_nick)
                await ctx.send(f'{ctx.author.mention} вышел из АФК')
            else:
                nick = f"{afk_pref} {current_nick}"
                await ctx.author.edit(nick=nick)
                await ctx.send(f'{current_nick} ушел в АФК')
        else:
            await ctx.send(error_message, delete_after=time_10s)

def setup(bot):
    bot.add_cog(afk(bot))
