from main import *


class conf_add_role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def add_role(self, ctx, role_id: int):
        role_name = get(ctx.guild.roles, id=role_id)

        roles[str(ctx.guild.id)].append(role_id)
        write_json(json_roles, roles)

        await ctx.send(f"Add new role `{role_name}`")

    @add_role.error
    async def add_role_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)


def setup(bot):
    bot.add_cog(conf_add_role(bot))