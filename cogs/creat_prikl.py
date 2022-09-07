from main import *

class creat_prikl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))
    
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
    bot.add_cog(creat_prikl(bot))
