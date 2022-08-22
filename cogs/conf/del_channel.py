from main import *
from settings import *
from phrazes import *


class del_channel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def del_channel(self, ctx, channel_id: int):
        channel_name = get(ctx.guild.channels, id=channel_id)

        channels[str(ctx.guild.id)].remove(channel_id)
        write_json(json_channels, channels)

        await ctx.send(f"Remove channel `{channel_name}`")

    @del_channel.error
    async def del_channel_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)


def setup(bot):
    bot.add_cog(del_channel(bot))