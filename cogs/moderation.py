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
    async def clear(self, ctx, amount: int):
        if ctx.author.id in admins_id:
            await ctx.channel.purge(limit=amount)
            await ctx.send(
                embed=discord.Embed(description=f':white_check_mark: Удалено {amount} сообщений', color=discord.Colour.random()), delete_after=time_10s)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send("You aren't bot admin", delete_after=time_5s)
    

    @commands.command(name=comm_ban, aliaces=aliaces_ban)
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, userid: int, reason='not specified'):
        user = await self.bot.fetch_user(userid)
        try:
            await ctx.guild.unban(user)
            await ctx.send(f"{user} has been unbanned. Reason: {reason}")
            return
        except:
            return await ctx.send(f"The user {user} is not banned!", delete_after=5)

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            await ctx.send("Not enough permissions to use this command", delete_after=5)


    @commands.command(name=comm_unban, aliaces=aliaces_unban)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member = None, *, reason='not specified'):
        guild = ctx.guild
        await ctx.send(f"{ctx.author.display_name} banned a user {user.display_name}. Reason: {reason}")
        await guild.ban(user)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            await ctx.send("Not enough permissions to use this command", delete_after=5)
            return
        if isinstance(error, commands.MemberNotFound):
            await ctx.message.delete()
            await ctx.send("Member not found", delete_after=5)

def setup(bot):
    bot.add_cog(Moderation(bot))
