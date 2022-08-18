from main import *
from settings import *
from phrazes import *

class testing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))
    
    @commands.command()
    async def test(self, ctx, *, tipe: int):
        for role in ctx.author.roles:
            if role.id in roles[str(ctx.guild.id)]:
                if tipe == 1:
                    await ctx.send('test 1')
                    return
                else:
                    await ctx.send('test')
                return
        else:
            await ctx.send('no')


def setup(bot):
    bot.add_cog(testing(bot))

# roles_list = [role.id for role in ctx.guild.roles]