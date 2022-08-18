from main import *
from settings import *
from phrazes import *

class bal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))


    @commands.command(name=comm_ball, aliases=aliaces_ball)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def magic_eight_ball(self, ctx, *, arg=None):
        for role in ctx.author.roles:
            if role.id in roles[str(ctx.guild.id)]:
                if ctx.channel.id in channels[str(ctx.guild.id)]:
                    if arg is None:
                        await ctx.channel.purge(limit=1)
                        await ctx.send(
                            embed=discord.Embed(
                                color=discord.Colour.random(),
                                title='Ошибка',
                                description=error_comm + prefix[str(ctx.guild.id)] + comm_snow + error_comm_question
                            ), delete_after=time_5s)
                        ctx.command.reset_cooldown(ctx)
                        return
                    else:
                        embed = discord.Embed(color=discord.Colour.random(), title='')
                        embed.add_field(name=arg, value=random.choice(ball), inline=False)
                        await ctx.send(embed=embed)
                    return
                else:
                    await ctx.channel.purge(limit=1)
                    await ctx.send(error_message, delete_after=time_10s)
                    
                    ctx.command.reset_cooldown(ctx)
        else:
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)

        
def setup(bot):
    bot.add_cog(bal(bot))
