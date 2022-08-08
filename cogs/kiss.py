import discord, datetime, random, requests, json, time, pytz
from discord.ext import commands
from main import *
from settings import *
from phrazes import *

class kiss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send(f"kiss load {datetime.datetime.now(pytz.timezone('Asia/Yekaterinburg')).strftime('%d-%m-%Y at %H:%M:%S')}")

    @commands.command(name="kiss", aliaces=["чмок", "поцеловать", "засосать"])
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def kiss(self, ctx, *, member: discord.Member = None):
        mam = ctx.author.mention
        mum = member.mention
        cci = ctx.channel.id
        getgifurl = tenor.random(str('kiss anime'))
        if cci in channels:
            if member is None:
                await ctx.channel.purge(limit=1)
                await ctx.send(
                    embed=discord.Embed(
                        color=0xff9900,
                        title=f'{ctx.author.name}#{ctx.author.discriminator}, **укажите пользователя**',
                        description=f'Пример: {pref}kiss **user**'
                ), delete_after=time_5s)
            else:
                if member == ctx.author:
                    await ctx.channel.purge(limit=1)
                    await ctx.send("Ошибка, вы не можете использовать эту команду против себя", delete_after=time_10s)
                else:
                    embed = discord.Embed(color=0xff9900, title='')
                    embed.add_field(name='Поцеловать', value=random.choice(phrazes.kiss).format(mam, mum), inline=False)
                    embed.set_image(url=getgifurl)
                    await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send("Ошибка, вы пишете не в том канале", delete_after=time_10s)

def setup(bot):
    bot.add_cog(kiss(bot))
