import discord, asyncio, datetime
from discord.ext import commands
from imp import bt, pr, dt_rg, roles, l_bot, adm_id, c0, c1, c2, c3, c4, c5, c6


class mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bt.get_channel(l_bot)
        await channel.send(f"mute load at {datetime.datetime.now(dt_rg).strftime('%Y-%m-%d %H:%M:%S')}")

    @commands.command(aliases=['mute'])
    async def __mute(self, ctx, member: discord.Member = None, amount_time=None, *, reason=None):
        if member is None:
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=discord.Embed(
                title=f'{ctx.author.mention}, **укажите пользователя**',
                description=f'Пример: {pr}mute **@user** time reason'
            ))
        elif amount_time is None:
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=discord.Embed(
                title=f'{ctx.author.mention}, **укажите кол-во времени**',
                description=f'Пример: {pr}mute @user **time** reason'
            ))
        elif reason is None:
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=discord.Embed(
                title=f'{ctx.author.mention}, **укажите причину**',
                description=f'Пример: {pr}mute @user time **reason**'
            ))
        else:
            if 'm' in amount_time:
                await ctx.send(embed=discord.Embed(
                    description=f'''**{member.mention}** Вы были замучены на **{amount_time}**.
                    **Выдал мут:** {ctx.author}
                    ```css
    Причина: [{reason}]
                    ```
                    ''',
                    color=0x36393E,
                ))

                mute_role = discord.utils.get(ctx.guild.roles, id=714369082492846150)
                await member.add_roles(mute_role)
                await asyncio.sleep(int(amount_time[:-1]) * 60)
                await member.remove_roles(mute_role)

                await ctx.send(embed=discord.Embed(
                    description=f'''**{member.mention}** Время мута истекло, вы были размучены''',
                    color=0x2F3136
                ))
            elif 'h' in amount_time:
                await ctx.send(embed=discord.Embed(
                    description=f'''**{member.mention}** Вы были замучены на **{amount_time}**.
                    **Выдал мут:** {ctx.author}
                    ```css
    Причина: [{reason}]
                    ```
                    ''',
                    color=0x36393E,
                ))

                mute_role = discord.utils.get(ctx.guild.roles, id=714369082492846150)
                await member.add_roles(mute_role)
                await asyncio.sleep(int(amount_time[:-1]) * 60 * 60)
                await member.remove_roles(mute_role)

                await ctx.send(embed=discord.Embed(
                    description=f'''**{member.mention}** Время мута истекло, вы были размучены''',
                    color=0x2F3136
                ))
            elif 'd' in amount_time:
                await ctx.send(embed=discord.Embed(
                    description=f'''**{member.mention}** Вы были замучены на **{amount_time}**.
                    **Выдал мут:** {ctx.author}
                    ```css
    Причина: [{reason}]
                    ```
                    ''',
                    color=0x36393E,
                ))

                mute_role = discord.utils.get(ctx.guild, id=714369082492846150)
                await member.add_roles(mute_role)
                await asyncio.sleep(int(amount_time[:-1]) * 60 * 60 * 24)
                await member.remove_roles(mute_role)

                await ctx.send(embed=discord.Embed(
                    description=f'''**{member.mention}** Время мута истекло, вы были размучены''',
                    color=0x2F3136
                ))
            else:
                await ctx.send(embed=discord.Embed(
                    description=f'''**{member.mention}** Вы были замучены на **{amount_time}s**.
                    **Выдал мут:** {ctx.author}
                    ```css
    Причина: [{reason}]
                    ```
                    ''',
                    color=0x36393E,
                ))

                mute_role = discord.utils.get(ctx.guild.roles, id=934530689024540703)
                await member.add_roles(mute_role)
                await asyncio.sleep(int(amount_time))
                await member.remove_roles(mute_role)

                await ctx.send(embed=discord.Embed(
                    description=f'''**{member.mention}** Время мута истекло, вы были размучены''',
                    color=0x2F3136
                ))

def setup(bot):
    bot.add_cog(mute(bot))