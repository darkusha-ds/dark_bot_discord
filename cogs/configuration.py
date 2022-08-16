from main import *
from settings import *
from phrazes import *


class Configuration(commands.Cog):
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
        with open("jsons/prefix.json", "w") as f:
            json.dump(prefix, f, indent=4)

        await ctx.send(f"New prefix `{new}`")

    @setprefix.error
    async def setprefix_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def add_role(self, ctx, role_id: int):
        role_name = get(ctx.guild.roles, id=role_id)

        roless[str(ctx.guild.id)].append(str(role_id))

        with open("jsons/roles.json", "w", encoding='utf8') as f:
            json.dump(roless, f, indent=4, ensure_ascii=False)

        await ctx.send(f"Add new role `{role_name}`")

    @add_role.error
    async def add_role_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def del_role(self, ctx, role_id: int):
        role_name = get(ctx.guild.roles, id=role_id)

        roless[str(ctx.guild.id)].remove(str(role_id))

        with open("jsons/roles.json", "w", encoding='utf8') as f:
            json.dump(roless, f, indent=4, ensure_ascii=False)

        await ctx.send(f"Remove role `{role_name}`")

    @del_role.error
    async def del_role_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def add_channel(self, ctx, channel_id: int):
        channel_name = get(ctx.guild.channels, id=channel_id)

        channels[str(ctx.guild.id)].append(channel_id)

        with open("jsons/channels.json", "w", encoding='utf8') as f:
            json.dump(channels, f, indent=4, ensure_ascii=False)

        await ctx.send(f"Add new channel `{channel_name}`")

    @add_channel.error
    async def add_channel_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def del_channel(self, ctx, channel_id: int):
        channel_name = get(ctx.guild.channels, id=channel_id)

        channels[str(ctx.guild.id)].remove(channel_id)

        with open("jsons/channels.json", "w", encoding='utf8') as f:
            json.dump(channels, f, indent=4, ensure_ascii=False)

        await ctx.send(f"Remove channel `{channel_name}`")

    @del_channel.error
    async def del_channel_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)


def setup(bot):
    bot.add_cog(Configuration(bot))