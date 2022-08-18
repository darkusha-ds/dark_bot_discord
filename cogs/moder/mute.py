from main import *
from settings import *
from phrazes import *


class mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))

    
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
    

def setup(bot):
    bot.add_cog(mute(bot))
