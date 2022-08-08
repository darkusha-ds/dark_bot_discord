import discord, datetime, pytz
from discord.ext import commands
from main import *
from settings import *

class roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send(f"roles load {datetime.datetime.now(pytz.timezone('Asia/Yekaterinburg')).strftime('%d-%m-%Y at %H:%M:%S')}")

    @commands.command(name='rols', aliases=["roles", "role"])
    @commands.has_permissions(administrator=True)
    async def get_roles_id(self, ctx):
        cci = ctx.channel.id
        if cci == channels[0]:
            guild = bot.get_guild(servers_id[0])
            await ctx.send(guild.roles)

        elif cci == channels[2]:
            guild = bot.get_guild(servers_id[1])
            await ctx.send(guild.roles)

        elif cci == channels[4]:
            guild = bot.get_guild(servers_id[2])
            await ctx.send(guild.roles)

def setup(bot):
    bot.add_cog(roles(bot))
