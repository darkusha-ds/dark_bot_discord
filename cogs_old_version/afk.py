import discord
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
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command(name=comm_afk, aliases=aliaces_afk, pass_context=True)
    @commands.has_any_role(*roles)
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def afk(self, ctx):
        current_nick = ctx.author.nick
        move_1 = current_nick.replace("[AFK]", "").replace("[AFК]", "").replace("[АFK]", "").replace("[АFК]", "")
        move_2 = move_1.replace("[AФK]", "").replace("[AФК]", "").replace("[АФK]", "").replace("[АФК]", "")
        move_3 = move_2.replace("AFK]", "").replace("AFК]", "").replace("АFK]", "").replace("АFК]", "")
        move_4 = move_3.replace("AФK]", "").replace("AФК]", "").replace("АФK]", "").replace("АФК]", "")
        move_5 = move_4.replace("[AFK", "").replace("[AFК", "").replace("[АFK", "").replace("[АFК", "")
        move_6 = move_5.replace("[AФK", "").replace("[AФК", "").replace("[АФK", "").replace("[АФК", "")
        move_7 = move_6.replace("AFK", "").replace("AFК", "").replace("АFK", "").replace("АFК", "")
        old_nick = move_7.replace("AФK", "").replace("AФК", "").replace("АФK", "").replace("АФК", "")
        cci = ctx.channel.id
        if cci in channels:
            if "[AFK]" in current_nick or "[AFК]" in current_nick or "[АFK]" in current_nick or "[АFК]" in current_nick or \
               "[AФK]" in current_nick or "[AФК]" in current_nick or "[АФK]" in current_nick or "[АФК]" in current_nick or \
               "AFK]" in current_nick or "AFК]" in current_nick or "АFK]" in current_nick or "АFК]" in current_nick or \
               "AФK]" in current_nick or "AФК]" in current_nick or "АФK]" in current_nick or "АФК]" in current_nick or \
               "[AFK" in current_nick or "[AFК" in current_nick or "[АFK" in current_nick or "[АFК" in current_nick or \
               "[AФK" in current_nick or "[AФК" in current_nick or "[АФK" in current_nick or "[АФК" in current_nick or \
               "AFK" in current_nick or "AFК" in current_nick or "АFK" in current_nick or "АFК" in current_nick or \
               "AФK" in current_nick or "AФК" in current_nick or "АФK" in current_nick or "АФК" in current_nick:
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
