import discord, pytz
from datetime import datetime as dt
from discord.ext import commands
from main import *
from settings import *

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send(f"help load {dt.now(pytz.timezone(region)).strftime(time_format)}")

    @commands.group(name="help", aliases=aliaces_help, invoke_without_command=True)
    @commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
    async def help(self, ctx):
        cci = ctx.channel.id
        if cci in channels:
            emb = discord.Embed(
                title='Навигация по командам :clipboard:',
                colour=(discord.Colour.random())
            )
            emb.add_field(
                name='**Основные**', value=f"`{pref}pat` `{pref}kill` `{pref}snowball` `{pref}hug` `{pref}rip` `{pref}poke` `{pref}kiss` `{pref}afk` `{pref}зайти` `{pref}выйти` `{pref}afk` `{pref}un_afk` `{pref}hit` `{pref}выйти`", inline=False)
            emb.add_field(
                name='**Приколюшки**', value=f"`{pref}password` `{pref}key` `{pref}шар` `{pref}ютуб`", inline=False
            )
            emb.add_field(
                name='**Модерация**', value=f"`{pref}clear`", inline=False
            )
            await ctx.send(embed=emb)
        else:
            await ctx.author.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)

    @help.command()
    @commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
    async def one(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send("h1", delete_after=time_20s)

    @help.command()
    @commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
    async def two(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send("h2", delete_after=time_20s)

    @help.command()
    @commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
    async def three(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send("h3", delete_after=time_20s)

def setup(bot):
    bot.add_cog(help(bot))
