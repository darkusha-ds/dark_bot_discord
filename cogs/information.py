import discord
from discord.ext import commands
from main import *
from settings import *

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))

    @commands.group(name=comm_help, aliases=aliaces_help, invoke_without_command=True)
    # @commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
    async def help(self, ctx):
        cci = ctx.channel.id
        if cci in channels:
            embed = discord.Embed(
                title="Доступные команды:",
                description=f"Вы можете получить детальную справку по каждой команде указав название. Например: `{pref}хелп инфо` (пока в разработке)",
                color=discord.Colour.random(),
            )

            embed.set_thumbnail(url=logo)

            embed.add_field(
                name=f"📋  Информация ({pref}хелп Информация)",
                value=f"`{pref}help` `{pref}user`",
                inline=False
            )
            embed.add_field(
                name=f"🛡️  Модерирование ({pref}хелп Модерирование)",
                value=f"`{pref}clear`",
                inline=False
            )
            embed.add_field(
                name=f"😄  Весёлое ({pref}хелп Весёлое)",
                value=f"`{pref}afk` `{pref}шар` `{pref}hit` `{pref}hug` `{pref}kill` `{pref}kiss` `{pref}зайти` `{pref}выйти` `{pref}pat` `{pref}poke` `{pref}rip` `{pref}snowball`",
                inline=False
            )
            embed.add_field(
                name=f"🔧  Утилиты ({pref}хелп Утилиты)",
                value=f"`{pref}password` `{pref}key` `{pref}ютуб`",
                inline=False
            )

            embed.add_field(
                name=f":man_technologist:  Для создателя)",
                value=f"`{pref}servers`",
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

    
    @commands.command(name=comm_userinfo, aliases=aliaces_userinfo)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def user(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        embed = discord.Embed(title=f"Info {member.name}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Nickname", value=member.display_name, inline=True)
        embed.add_field(name="Top role", value=member.top_role.mention, inline=True)
        embed.add_field(name="Created at", value=member.created_at.strftime("%d.%m.%Y %H:%M:%S"), inline=True)
        embed.add_field(name="Joined at", value=member.joined_at.strftime("%d.%m.%Y %H:%M:%S"), inline=True)
        embed.add_field(name="Bot?", value=member.bot, inline=True)
        await ctx.send(embed=embed)
    
    @commands.command(name=comm_server, aliases=aliaces_server)
    # @commands.has_any_role(*roles)
    # @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def server(self, ctx):
        guild = ctx.guild
	
        await ctx.send(f'Server Name: {guild.name}')
        await ctx.send(f'Server Size: {len(guild.members)}')
        await ctx.send(f'Server Name: {guild.owner.display_name}')

def setup(bot):
    bot.add_cog(Information(bot))
