import discord
from discord.ext import commands
from main import *
from settings import *

class films(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command(name=comm_films, aliases=aliaces_films)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=120, type=commands.BucketType.user)
    async def films(self, ctx):
        cci = ctx.channel.id
        if cci in channels:
            link = await bot.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
            await ctx.send(f"Click the blue link!\n{link}", delete_after=time_120s)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)

def setup(bot):
    bot.add_cog(films(bot))
