from main import *

class utils_password(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))


    @commands.command(name=comm_pg, aliases=aliaces_pg)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def password(self, ctx, type=None, length: typing.Union[int, str]=None):
        for role in ctx.author.roles:
            if role.id in roles[str(ctx.guild.id)]:
                if type is None:
                    await ctx.channel.purge(limit=1)
                    
                    embed = discord.Embed(color=discord.Colour.random())
                    embed.add_field(name='Ошибка', value=error_comm + prefix[str(ctx.guild.id)] + comm_pg + ' ***уровень защиты: `1` , `2` или `3`***')
                    await ctx.send(embed=embed, delete_after=time_5s)

                    ctx.command.reset_cooldown(ctx)
                elif length is None:
                    await ctx.channel.purge(limit=1)

                    embed = discord.Embed(color=discord.Colour.random())
                    embed.add_field(name='Ошибка', value=error_comm + prefix[str(ctx.guild.id)] + comm_pg + ' ' + type + ' ***длину пароля (от 8 до 32)***')
                    await ctx.send(embed=embed, delete_after=time_5s)

                    ctx.command.reset_cooldown(ctx)
                else:
                    if ctx.channel.id in channels[str(ctx.guild.id)]:
                        if type == '1' and 8 <= length <= 32:
                            random.shuffle(alphabet)
                            await ctx.send(''.join(alphabet[:length]))

                        elif type == '2' and 8 <= length <= 32:
                            spass = alphabet + numbers
                            random.shuffle(spass)
                            await ctx.send(''.join(spass[:length]))

                        elif type == '3' and 8 <= length <= 32:
                            spass = alphabet + numbers + symbols
                            random.shuffle(spass)
                            await ctx.send(''.join(spass[:length]))
                        else:
                            await ctx.channel.purge(limit=1)
                            await ctx.send(
                                f'{ctx.author.mention}  \nОшибка, доступны только 3 уровня сложности: `1` , `2` , `3` , и длина пароля от `8` до `32` символов', delete_after=time_10s)

                            ctx.command.reset_cooldown(ctx)
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
    bot.add_cog(utils_password(bot))
