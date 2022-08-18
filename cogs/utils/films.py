from main import *
from settings import *
from phrazes import *

class films(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command(name=comm_films, aliases=aliaces_films)
    @commands.cooldown(rate=1, per=120, type=commands.BucketType.user)
    async def films(self, ctx):
        for role in ctx.author.roles:
            if role.id in roles[str(ctx.guild.id)]:
                if ctx.channel.id in channels[str(ctx.guild.id)]:
                    link = await bot.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
                    await ctx.send(f"Click the blue link!\n{link}", delete_after=time_120s)
                else:
                    await ctx.channel.purge(limit=1)
                    await ctx.send(error_message, delete_after=time_10s)
                return
        else:
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)

def setup(bot):
    bot.add_cog(films(bot))
