from main import *
from settings import *
from phrazes import *


class setmute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setmute(self, ctx, mute_id: int):
        mute_name = get(ctx.guild.roles, id=mute_id)

        mute_roles[str(ctx.guild.id)] = mute_id
        write_json(json_mutes, mute_roles)

        await ctx.send(f"Set mute role `{mute_name}`")

    @setmute.error
    async def setmute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)


def setup(bot):
    bot.add_cog(setmute(bot))