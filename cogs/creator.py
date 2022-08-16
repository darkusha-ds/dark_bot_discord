from main import *
from settings import *
from phrazes import *

class Creator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command(name=comm_servers, aliaces=aliaces_servers)
    @commands.has_permissions(administrator=True)
    async def servers(self, ctx):
        if ctx.author.id == 391682780322594840:
            activeservers = bot.guilds
            for guild in activeservers:
                await ctx.send(f"{guild.name} \n id: {guild.id}")
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send("You aren't bot creator", delete_after=time_5s)
    
    @commands.command(name=comm_roles, aliases=aliaces_roles)
    @commands.has_permissions(administrator=True)
    async def get_roles_id(self, ctx):
        if ctx.author.id == 391682780322594840:
            guild = bot.get_guild(763632193150779412)
            await ctx.send(guild.roles)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send("You aren't bot creator", delete_after=time_5s)
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def prikl(self, ctx, *, text = None):
        if ctx.author.id == 391682780322594840:
            channel = bot.get_channel(870241377114533899)
            await channel.send(text)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send("You aren't bot creator", delete_after=time_5s)

def setup(bot):
    bot.add_cog(Creator(bot))
