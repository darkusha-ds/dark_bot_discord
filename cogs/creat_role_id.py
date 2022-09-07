from main import *

class creat_roles_id(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))
    
    @commands.command(name=comm_roles, aliases=aliaces_roles)
    @commands.has_permissions(administrator=True)
    async def get_roles_id(self, ctx):
        if ctx.author.id == 391682780322594840:
            guild = bot.get_guild(763632193150779412)
            await ctx.send(guild.roles)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send("You aren't bot creator", delete_after=time_5s)

def setup(bot):
    bot.add_cog(creat_roles_id(bot))
