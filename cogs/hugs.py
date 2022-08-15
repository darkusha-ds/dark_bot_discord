import discord, random
from discord.ext import commands
from main import *
from settings import *
from phrazes import *

class hugs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command(name='hug', aliases=aliaces_hugs)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def hugs(self, ctx, member: discord.Member = None):
        mam = ctx.author.mention
        mum = member.mention
        cci = ctx.channel.id
        if cci in channels:
            if member == ctx.author:
                await ctx.channel.purge(limit=1)
                await ctx.send(error_ctx_user, delete_after=time_10s)
            else:
                embed = discord.Embed(
                    color=discord.Colour.random(),
                    description=random.choice(phrazes.hugs).format(mam, mum)
                )
                embed.set_image(url=tenor.random(str(f'{comm_hugs} anime')))
                await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)

    @hugs.error
    async def hugs_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)

        if isinstance(error, commands.MemberNotFound):
            await ctx.message.delete()
            await ctx.send(error_member, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)

        if isinstance(error, commands.CommandError):
            await ctx.message.delete()

            embed = discord.Embed(color=discord.Colour.random())
            embed.add_field(name='Ошибка', value=error_comm + pref + comm_hugs + error_comm_nick)
            await ctx.send(embed=embed, delete_after=time_5s)

            ctx.command.reset_cooldown(ctx)

def setup(bot):
    bot.add_cog(hugs(bot))
