import discord, datetime, pytz
from discord.ext import commands
from main import *
from settings import *

class films(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send(f"films load {datetime.datetime.now(pytz.timezone('Asia/Yekaterinburg')).strftime('%d-%m-%Y at %H:%M:%S')}")

    @commands.command(name="films", aliases=["film", "youtube", "yt", "фильм", "ютуб"])
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=120, type=commands.BucketType.user)
    async def films(self, ctx):
        cci = ctx.channel.id
        if cci in channels:
            link = await bot.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
            await ctx.send(f"Click the blue link!\n{link}", delete_after=time_120s)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send("Ошибка, вы пишете не в том канале", delete_after=time_10s)

def setup(bot):
    bot.add_cog(films(bot))
