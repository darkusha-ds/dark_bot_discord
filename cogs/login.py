import discord, random
from discord.ext import commands
from main import *
from settings import *
from phrazes import *

class login(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command(name=comm_login, aliases=aliaces_login)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def enter(self, ctx):
        mam = ctx.author.mention  # тег автора
        cci = ctx.channel.id
        if cci in channels:
            await ctx.send(random.choice(phrazes.login).format(mam))
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)

    @enter.error
    async def enter_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)

        if isinstance(error, commands.CommandError):
            await ctx.message.delete()

            embed = discord.Embed(color=discord.Colour.random())
            embed.add_field(name='Ошибка', value=error_comm + pref + comm_login + error_comm_nick)
            await ctx.send(embed=embed, delete_after=time_5s)

            ctx.command.reset_cooldown(ctx)

def setup(bot):
    bot.add_cog(login(bot))
