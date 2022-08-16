import discord
from discord.ext import commands
from main import *
from settings import *
from phrazes import *

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))
    
    @commands.command()
    async def test(self, ctx):
        if ctx.author.roles in roless[str(ctx.guild.id)]:
            embed = discord.Embed(color=discord.Colour.random(), title='')
            embed.add_field(name="hello", inline=False)
            await ctx.send(embed=embed)
        else:
            # await ctx.channel.purge(limit=1)
            await ctx.send(ctx.author.roles)
            
            ctx.command.reset_cooldown(ctx)


def setup(bot):
    bot.add_cog(Information(bot))