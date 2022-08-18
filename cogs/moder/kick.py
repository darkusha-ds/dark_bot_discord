from main import *
from settings import *
from phrazes import *


class kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))


    @commands.command(name=comm_kick, aliaces=aliaces_kick, pass_context = True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member = None, *, reason='не указана'):
        if user.server_permissions.administrator:
            await bot.say("Ошибка, вы выбрали админа")
        else:
            await user.kick(reason)
            await bot.say(f"{ctx.author.display_name} кикнул {user.display_name}, по причине: {reason}")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
            return
        if isinstance(error, commands.MemberNotFound):
            await ctx.message.delete()
            await ctx.send(error_member, delete_after=time_5s)
    
    

def setup(bot):
    bot.add_cog(kick(bot))
