import discord, datetime, pytz
from discord.ext import commands
from main import *
from settings import *


class clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send(f"clear load {datetime.datetime.now(pytz.timezone('Asia/Yekaterinburg')).strftime('%d-%m-%Y at %H:%M:%S')}")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(
            embed=discord.Embed(description=f':white_check_mark: Удалено {amount} сообщений', color=0x0c0c0c), delete_after=time_10s)

def setup(bot):
    bot.add_cog(clear(bot))
