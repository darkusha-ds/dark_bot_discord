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
    @commands.cooldown(1, 600, commands.BucketType.user)
    async def afk(self, ctx):
        current_nick = ctx.author.nick
        old_nick = current_nick.replace(afk_pref,"")
        cci = ctx.channel.id
        if cci in channels:
            if afk_pref in current_nick:
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
