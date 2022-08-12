import discord, random
from datetime import datetime as dt
from discord.ext import commands
from main import *
from settings import *
from phrazes import *

class server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send(f"{comm_server} load {dt.now(pytz.timezone(region)).strftime(time_format)}")

    @commands.command(name=comm_server, aliases=aliaces_server)
    @commands.has_any_role(*roles)
    # @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def server(self, ctx):
        mam = ctx.author.mention
        # mum = member.mention
        cci = ctx.channel.id
        if cci in channels:
            name = str(ctx.guild.name)

            owner = str(ctx.guild.owner)
            id = str(ctx.guild.id)
            channel = str(ctx.guild.channel_count)
            memberCount = str(ctx.guild.member_count)

            icon = str(ctx.guild.icon_url)
            
            embed = discord.Embed(
                title="Информация о сервере " + name,
                color=discord.Color.blue()
                )

            embed.set_thumbnail(url=icon)
            embed.add_field(name="Участники", value=f"Всего: {memberCount}", inline=True)
            embed.add_field(name="Владелец", value=owner, inline=True)
            embed.add_field(name="Каналы", value=channel, inline=True)

            embed.set_footer(
                text="ID: " + id
            )

            await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)

def setup(bot):
    bot.add_cog(server(bot))
