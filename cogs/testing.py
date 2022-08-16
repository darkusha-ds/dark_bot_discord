from main import *
from settings import *
from phrazes import *

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))
    
    @commands.command()
    async def test(self, ctx):
        for rol in ctx.author.roles:
            if rol in roless[str(ctx.guild.id)]:
                embed = discord.Embed(color=discord.Colour.random(), title='', description='hello')
                await ctx.send(embed=embed)
        else:
            # await ctx.channel.purge(limit=1)
            await ctx.send('error')
            
            ctx.command.reset_cooldown(ctx)


def setup(bot):
    bot.add_cog(Information(bot))

# roles_list = [role.id for role in ctx.guild.roles]