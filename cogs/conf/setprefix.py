from main import *
from settings import *
from phrazes import *


class setprefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setprefix(self, ctx, new: str):
        prefix[str(ctx.guild.id)] = new
        write_json(json_prefix, prefix)

        await ctx.send(f"New prefix `{new}`")

    @setprefix.error
    async def setprefix_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)

def setup(bot):
    bot.add_cog(setprefix(bot))