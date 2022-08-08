import discord, datetime,pytz
from discord.ext import commands
from main import *
from settings import *

class servers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send(f"servers load {datetime.datetime.now(pytz.timezone('Asia/Yekaterinburg')).strftime('%d-%m-%Y at %H:%M:%S')}")

    @commands.command(name="servers", aliaces=["active", "servs"])
    @commands.has_permissions(administrator=True)
    async def servers(self, ctx):
        activeservers = bot.guilds
        for guild in activeservers:
            await ctx.send(f"{guild.name}; id: {guild.id}")

def setup(bot):
    bot.add_cog(servers(bot))
