import discord, random, datetime, pytz
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
        await channel.send(f"login load {datetime.datetime.now(pytz.timezone('Asia/Yekaterinburg')).strftime('%d-%m-%Y at %H:%M:%S')}")

    @commands.command(name="enter", aliases=["войти", "зайти", "вошёл", "зашел", "зашёл"])
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def enter(self, ctx):
        mam = ctx.author.mention  # тег автора
        cci = ctx.channel.id
        if cci in channels:
            await ctx.send(random.choice(phrazes.login).format(mam))
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send("Ошибка, вы пишете не в том канале", delete_after=time_10s)

def setup(bot):
    bot.add_cog(login(bot))
