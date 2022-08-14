import discord, datetime, random
from discord.ext import commands
from main import *
from settings import *

class link(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send(f"link {load_text}")

    @commands.command(name='create_invite', aliases=["link"])
    @commands.has_permissions(administrator=True)
    async def create_invite(self, ctx):
        guild = bot.get_guild(990718922087088169)
        invite = await guild.create_invite(max_age=300, max_uses=5)
        await ctx.send(f"https://discord.gg/{invite.code}")

def setup(bot):
    bot.add_cog(link(bot))
