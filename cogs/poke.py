import discord, random, datetime, pytz
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
        await channel.send(f"poke load {datetime.datetime.now(pytz.timezone('Asia/Yekaterinburg')).strftime('%d-%m-%Y at %H:%M:%S')}")

    @commands.command(name='poke', aliases=["тык", "тыкнуть"])
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def poke(self, ctx, member: discord.Member = None):
        mam = ctx.author.mention
        mum = member.mention
        cci = ctx.channel.id
        getgifurl = tenor.random(str('poke anime'))
        if cci in channels:
            if member == ctx.author:
                await ctx.channel.purge(limit=1)
                await ctx.send("Ошибка, вы не можете использовать эту команду против себя", delete_after=time_10s)
            else:
                embed = discord.Embed(
                    colour=(discord.Colour.random()),
                    description=random.choice(phrazes.poke).format(mam, mum)
                )
                embed.set_image(url=(getgifurl))
                await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send("Ошибка, вы пишете не в том канале", delete_after=time_10s)

def setup(bot):
    bot.add_cog(poke(bot))
