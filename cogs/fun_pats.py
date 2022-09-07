from main import *

class fun_pats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))
        

    @commands.command(name=comm_pats, aliases=aliaces_pats)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def pat(self, ctx, member: discord.Member = None):
        mam = ctx.author.mention
        mum = member.mention
        for role in ctx.author.roles:
            if role.id in roles[str(ctx.guild.id)]:
                if ctx.channel.id in channels[str(ctx.guild.id)]:
                    if member == ctx.author:
                        await ctx.channel.purge(limit=1)
                        await ctx.send(error_ctx_user, delete_after=time_10s)
                        return
                    else:
                        embed = discord.Embed(
                            color=discord.Colour.random(),
                            description=random.choice(pats).format(mam, mum)
                        )
                        embed.set_image(url=tenor.random(str(f'{comm_pats} anime')))
                        await ctx.send(embed=embed)
                    return
                else:
                    await ctx.channel.purge(limit=1)
                    await ctx.send(error_message, delete_after=time_10s)
                    
                    ctx.command.reset_cooldown(ctx)
                    return
        else:
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)


    @pat.error
    async def pat_error(self, ctx, error):
        for role in ctx.author.roles:
            if role.id in roles[str(ctx.guild.id)]:
                if isinstance(error, commands.MemberNotFound):
                    await ctx.message.delete()
                    await ctx.send(error_member, delete_after=time_5s)
                    
                    ctx.command.reset_cooldown(ctx)
                    return

                if isinstance(error, commands.CommandError):
                    await ctx.message.delete()

                    embed = discord.Embed(color=discord.Colour.random())
                    embed.add_field(name='Ошибка', value=error_comm + prefix[str(ctx.guild.id)] + comm_pats + error_comm_nick)
                    await ctx.send(embed=embed, delete_after=time_5s)

                    ctx.command.reset_cooldown(ctx)
                    return
                return
        else:
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)


def setup(bot):
    bot.add_cog(fun_pats(bot))
