from main import *


class moder_clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))


    @commands.command(name=comm_clear, aliases=aliaces_clear)
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit = amount + 1)
        await ctx.send(
            embed=discord.Embed(description=f':white_check_mark: Удалено {amount} сообщений', color=discord.Colour.random()), delete_after=time_10s)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)

def setup(bot):
    bot.add_cog(moder_clear(bot))
