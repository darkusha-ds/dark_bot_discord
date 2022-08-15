import discord
from discord.ext import commands
from main import *
from settings import *


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command(name=comm_clear, aliases=aliaces_clear)
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(
            embed=discord.Embed(description=f':white_check_mark: Удалено {amount} сообщений', color=discord.Colour.random()), delete_after=time_10s)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
    

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
    bot.add_cog(Moderation(bot))
