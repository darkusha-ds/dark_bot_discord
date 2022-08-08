import discord, datetime, pytz
from discord.ext import commands
from main import *
from settings import *

class afk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send(f"afk load {datetime.datetime.now(pytz.timezone('Asia/Yekaterinburg')).strftime('%d-%m-%Y at %H:%M:%S')}")

    @commands.command(pass_context=True)
    @commands.has_any_role(*roles)
    @commands.cooldown(1, 1200, commands.BucketType.user)
    async def afk(self, ctx, *, reason=None):
        cam = ctx.author.mention
        can = ctx.author.name
        cci = ctx.channel.id
        if cci in channels:
            if reason is None:
                await ctx.send(
                    embed=discord.Embed(
                        color=0xff9900,
                        title=f'{can}#{ctx.author.discriminator}, **укажите причину**',
                        description=f'Пример: {pref}afk **причина**'
                ), delete_after=time_5s)
            else:
                nick = f"[AFK] {can}"
                await ctx.author.edit(nick=nick)
                await ctx.send(f'{cam} ушел в афк по причине {reason}')
        else:
            await ctx.send("Ошибка, вы пишете не в том канале", delete_after=time_10s)

def setup(bot):
    bot.add_cog(afk(bot))
