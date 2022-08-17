from main import *
from settings import *
from phrazes import *


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
    
    @commands.command()
    # You must specify the roles ids that can use this command
    @commands.has_any_role()
    async def mute(self, ctx, member: discord.Member = None, time: str = None, *, reason="не указана"):
        if member is None:
            return await ctx.send("User not specified")
        if member.bot is True:
            return await ctx.send("You can't mute the bot")
        if member == ctx.author:
            return await ctx.send("You can't mute yourself")
        if len(reason) > 150:
            return await ctx.send("The reason is too long")
        if member and member.top_role.position >= ctx.author.top_role.position:
            return await ctx.send("You can't mute a man up with a role above yours")
        if time is None:
            return await ctx.send("You didn't specify the duration")
        else:
            try:
                seconds = int(time[:-1])
                duration = time[-1]
                if duration == "s":
                    pass
                if duration == "m":
                    seconds *= 60
                if duration == "h":
                    seconds *= 3600
                if duration == "d":
                    seconds *= 86400
            except:
                return await ctx.send("Wrong duration specified")
            mute_expiration = (datetime.datetime.now() + datetime.timedelta(seconds=int(seconds))).strftime("%c")
            role = self.mutedrole
            if not role:
                return await ctx.send("I can't find the mute role")
            mutes = load_json("jsons/mutes.json")
            try:
                member_mute = mutes[str(member.id)]
                return await ctx.send("The user is already in mute")
            except:
                mutes[str(member.id)] = str(mute_expiration)
                write_json("jsons/mutes.json", mutes)
                await member.add_roles(role)
                await member.move_to(channel=None)
                await ctx.send(f"{ctx.author.name} muted {member.display_name}"
                               f" until {mute_expiration} for a reason: {reason}")

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.message.delete()
            await ctx.send("Not enough permissions to use this command", delete_after=5)
            return
        if isinstance(error, commands.MemberNotFound):
            await ctx.message.delete()
            await ctx.send("Member not found", delete_after=5)
            return


    @commands.command()
    # You must specify the roles ids that can use this command
    @commands.has_any_role()
    async def unmute(self, ctx, member: discord.Member):
        await member.remove_roles(self.mutedrole)
        await ctx.send(f"{ctx.author.name} unmute {member.display_name}")
        mutes = load_json("jsons/mutes.json")
        mutes.pop(str(member.id))
        write_json("jsons/mutes.json", mutes)

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.message.delete()
            await ctx.send("Not enough permissions to use this command", delete_after=5)
            return
        if isinstance(error, commands.MemberNotFound):
            await ctx.message.delete()
            await ctx.send("Member not found", delete_after=5)
            return

def setup(bot):
    bot.add_cog(Moderation(bot))
