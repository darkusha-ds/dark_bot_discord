import discord, random
from discord.ext import commands
from main import *
from settings import *
from phrazes import *

class poke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command(name=comm_poke, aliases=aliaces_poke)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def poke(self, ctx, member: discord.Member = None):
        mam = ctx.author.mention
        mum = member.mention
        cci = ctx.channel.id
        if cci in channels:
            if member == ctx.author:
                await ctx.channel.purge(limit=1)
                await ctx.send(error_ctx_user, delete_after=time_10s)
            else:
                embed = discord.Embed(
                    colour=discord.Colour.random(),
                    description=random.choice(phrazes.poke).format(mam, mum)
                )
                embed.set_image(url=tenor.random(str(f'{comm_poke} anime')))
                await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)

def setup(bot):
    bot.add_cog(poke(bot))
