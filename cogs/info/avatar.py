from main import *
from settings import *
from phrazes import *

class avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))

    
    @commands.command(name=comm_avatar, aliases=aliaces_avatar)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def avatar(self, ctx, member: discord.Member = None):
        if ctx.channel.id in channels[str(ctx.guild.id)]:
            if member is None:
                member = ctx.author
            embed = discord.Embed(
                color=discord.Colour.random(),
                title=f"Аватар {member.display_name}"
            )
            embed.set_image(url=member.avatar_url)
            await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)
            
            ctx.command.reset_cooldown(ctx)
    
    
def setup(bot):
    bot.add_cog(avatar(bot))
