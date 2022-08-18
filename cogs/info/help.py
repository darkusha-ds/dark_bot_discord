from main import *
from settings import *
from phrazes import *

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))

    @commands.group(name=comm_help, aliases=aliaces_help, invoke_without_command=True)
    # @commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
    async def help(self, ctx):
        embed = discord.Embed(
            title="Доступные команды:",
            description=f"Вы можете получить детальную справку по каждой команде указав название. Например: `{prefix[str(ctx.guild.id)]}хелп инфо` (пока в разработке)",
            color=discord.Colour.random(),
        )

        embed.set_thumbnail(url=bot.user.avatar_url)

        embed.add_field(
            name=f"📋  Информация ({prefix[str(ctx.guild.id)]}хелп Информация)",
            value=\
                f"`{prefix[str(ctx.guild.id)]}{comm_help}`  " +
                f"`{prefix[str(ctx.guild.id)]}{comm_userinfo}`  " +
                f"`{prefix[str(ctx.guild.id)]}{comm_avatar}`  ",
            inline=False
        )
        embed.add_field(
            name=f"🛡️  Модерирование ({prefix[str(ctx.guild.id)]}хелп Модерирование)",
            value=\
                f"`{prefix[str(ctx.guild.id)]}{comm_clear}`  " +
                f"`{prefix[str(ctx.guild.id)]}{comm_ban}`  " +
                f"`{prefix[str(ctx.guild.id)]}{comm_unban}`  ",
            inline=False
        )
        embed.add_field(
            name=f"😄  Весёлое ({prefix[str(ctx.guild.id)]}хелп Весёлое)",
            value=\
                f"`{prefix[str(ctx.guild.id)]}{comm_afk}`  " +
                f"`{prefix[str(ctx.guild.id)]}{comm_ball}`  " +
                f"`{prefix[str(ctx.guild.id)]}{comm_hit}`  " +
                f"`{prefix[str(ctx.guild.id)]}{comm_hugs}`  " +
                f"`{prefix[str(ctx.guild.id)]}{comm_kill}`  " +
                f"`{prefix[str(ctx.guild.id)]}{comm_kiss}`  " +
                f"`{prefix[str(ctx.guild.id)]}{comm_login}`  " +
                f"`{prefix[str(ctx.guild.id)]}{comm_logout}`  " +
                f"`{prefix[str(ctx.guild.id)]}{comm_pats}`  " +
                f"`{prefix[str(ctx.guild.id)]}{comm_poke}`  " +
                f"`{prefix[str(ctx.guild.id)]}{comm_rip}`  " +
                f"`{prefix[str(ctx.guild.id)]}{comm_snow}`  ",
            inline=False
        )
        embed.add_field(
            name=f"💻  Конфигурация ({prefix[str(ctx.guild.id)]}хелп Конфигурация)",
            value=\
                f"`{prefix[str(ctx.guild.id)]}{comm_setpref}`  " +
            #   f"`{prefix[str(ctx.guild.id)]}{comm_setmute}`  " +
                f"`{prefix[str(ctx.guild.id)]}{comm_add_role}`  " +
                f"`{prefix[str(ctx.guild.id)]}{comm_del_role}`  " +
                f"`{prefix[str(ctx.guild.id)]}{comm_add_channel}`  " +
                f"`{prefix[str(ctx.guild.id)]}{comm_del_channel}`  ",
            inline=False
        )
        embed.add_field(
            name=f"🔧  Утилиты ({prefix[str(ctx.guild.id)]}хелп Утилиты)",
            value=\
                f"`{prefix[str(ctx.guild.id)]}{comm_pg}`  " +
                f"`{prefix[str(ctx.guild.id)]}{comm_key}`  " +
                f"`{prefix[str(ctx.guild.id)]}{comm_films}`  ",
            inline=False
        )

        embed.set_footer(
            text="Dark Angel © 2022",
            icon_url=logo_adm,
        )

        await ctx.send(embed=embed)

    @help.command()
    @commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
    async def информация(self, ctx):
        await ctx.send("h1")

    @help.command()
    @commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
    async def модерация(self, ctx):
        await ctx.send("h2")

    @help.command()
    @commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
    async def веселое(self, ctx):
        await ctx.send("h3")

    @help.command()
    @commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
    async def утилиты(self, ctx):
        await ctx.send("h4")
        

def setup(bot):
    bot.add_cog(help(bot))
