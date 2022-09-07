from main import *


class moder_unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))
    

    @commands.command(name=comm_unban, aliaces=aliaces_unban)
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, userid: int, reason='не указана'):
        user = await self.bot.fetch_user(userid)
        try:
            await ctx.guild.unban(user)
            await ctx.send(f"{user} был разбанен по причине: {reason}")
            return
        except:
            return await ctx.send(f"{user} не забанен!", delete_after=time_5s)

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
    

def setup(bot):
    bot.add_cog(moder_unban(bot))
