from main import *
from settings import *
from phrazes import *


class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))


    @commands.command(name=comm_ban, aliaces=aliaces_ban)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member = None, *, reason='не указана'):
        guild = ctx.guild
        await ctx.send(f"{ctx.author.display_name} забанил {user.display_name}, по причине: {reason}")
        await guild.ban(user)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
            return
        if isinstance(error, commands.MemberNotFound):
            await ctx.message.delete()
            await ctx.send(error_member, delete_after=time_5s)
    

def setup(bot):
    bot.add_cog(ban(bot))
