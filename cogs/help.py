from dis import disco
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
    # @commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
    async def help(self, ctx):
        cci = ctx.channel.id
        if cci in channels:
            # emb = discord.Embed(
            #     title='Навигация по командам :clipboard:',
            #     colour=(discord.Colour.random())
            # )
            # emb.add_field(
            #     name='**Основные**', value=f"`{pref}pat` `{pref}kill` `{pref}snowball` `{pref}hug` `{pref}rip` `{pref}poke` `{pref}kiss` `{pref}afk` `{pref}зайти` `{pref}выйти` `{pref}afk` `{pref}un_afk` `{pref}hit` `{pref}выйти`", inline=False)
            # emb.add_field(
            #     name='**Приколюшки**', value=f"`{pref}password` `{pref}key` `{pref}шар` `{pref}ютуб`", inline=False
            # )
            # emb.add_field(
            #     name='**Модерация**', value=f"`{pref}clear`", inline=False
            # )
            # await ctx.send(embed=emb)
            embed = discord.Embed(
                title="Доступные команды:",
                description=f"Вы можете получить детальную справку по каждой команде указав название. Например: `{pref}хелп инфо` (пока в разработке)",
                color=discord.Colour.random(),
            )

            embed.set_thumbnail(url=logo)

            embed.add_field(
                name=f"📋  Информация ({pref}хелп Информация)",
                value=f"`{pref}help`",
                inline=False
                )
            embed.add_field(
                name=f"🛡️  Модерирование ({pref}хелп Модерирование)",
                value=f"`{pref}clear`",
                inline=False
                )
            embed.add_field(
                name=f"😄  Весёлое ({pref}хелп Весёлое)",
                value=f"`{pref}pat` `{pref}kill` `{pref}snowball` `{pref}hug` `{pref}rip` `{pref}poke` `{pref}kiss` `{pref}afk` `{pref}зайти` `{pref}выйти` `{pref}afk` `{pref}un_afk` `{pref}hit` `{pref}выйти`",
                inline=False
                )
            embed.add_field(
                name=f"🔧  Утилиты ({pref}хелп Утилиты)",
                value=f"`{pref} Value`",
                inline=False
                )

            embed.set_footer(
                text="Dark Angel © 2022",
                icon_url=logo_adm,
            )

            await ctx.send(embed=embed)
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
