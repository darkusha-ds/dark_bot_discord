from main import *

class fun_rip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))
    

    @commands.command(name=comm_rip, aliases=aliaces_rip)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def rip(self, ctx):
        mam = ctx.author.mention  # тег автора
        for role in ctx.author.roles:
            if role.id in roles[str(ctx.guild.id)]:
                if ctx.channel.id in channels[str(ctx.guild.id)]:
                    await ctx.send(random.choice(rip).format(mam))
                else:
                    await ctx.channel.purge(limit=1)
                    await ctx.send(error_message, delete_after=time_10s)
                    
                    ctx.command.reset_cooldown(ctx)
                return
        else:
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)
        

def setup(bot):
    bot.add_cog(fun_rip(bot))
