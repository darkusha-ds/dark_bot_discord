import discord, uuid
from random import shuffle
from typing import Union
from discord.ext import commands
from main import *
from settings import *
from phrazes import *

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command(name=comm_films, aliases=aliaces_films)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=120, type=commands.BucketType.user)
    async def films(self, ctx):
        if ctx.channel.id in channels[str(ctx.guild.id)]:
            link = await bot.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
            await ctx.send(f"Click the blue link!\n{link}", delete_after=time_120s)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)

    @films.error
    async def films_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)

            ctx.command.reset_cooldown(ctx)
    
    @commands.command(name=comm_key, aliases=aliaces_key)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def key(self, ctx):
        if ctx.channel.id in channels[str(ctx.guild.id)]:
            await ctx.send(f'Key : {uuid.uuid4()}')
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)

    @key.error
    async def key_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)

            ctx.command.reset_cooldown(ctx)

    @commands.command(name=comm_pg, aliases=aliaces_pg)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def password(self, ctx, type=None, length: Union[int, str]=None):
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
                    shuffle(alphabet)
                    await ctx.send(''.join(alphabet[:length]))

                elif type == '2' and 8 <= length <= 32:
                    spass = alphabet + numbers
                    shuffle(spass)
                    await ctx.send(''.join(spass[:length]))

                elif type == '3' and 8 <= length <= 32:
                    spass = alphabet + numbers + symbols
                    shuffle(spass)
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

    @password.error
    async def password_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)

            ctx.command.reset_cooldown(ctx)

def setup(bot):
    bot.add_cog(Utilities(bot))
