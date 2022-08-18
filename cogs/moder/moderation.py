from main import *
from settings import *
from phrazes import *


class un_mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))


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
    bot.add_cog(un_mute(bot))
