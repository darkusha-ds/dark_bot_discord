from main import *
from settings import *
from phrazes import *

class Funny(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command(name=comm_afk, aliases=aliaces_afk)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=300, type=commands.BucketType.user)
    async def afk(self, ctx):
        current_nick = ctx.author.nick
        move_1 = current_nick.replace("[AFK]", "").replace("[AFК]", "").replace("[АFK]", "").replace("[АFК]", "")
        move_2 = move_1.replace("[AФK]", "").replace("[AФК]", "").replace("[АФK]", "").replace("[АФК]", "")
        move_3 = move_2.replace("AFK]", "").replace("AFК]", "").replace("АFK]", "").replace("АFК]", "")
        move_4 = move_3.replace("AФK]", "").replace("AФК]", "").replace("АФK]", "").replace("АФК]", "")
        move_5 = move_4.replace("[AFK", "").replace("[AFК", "").replace("[АFK", "").replace("[АFК", "")
        move_6 = move_5.replace("[AФK", "").replace("[AФК", "").replace("[АФK", "").replace("[АФК", "")
        move_7 = move_6.replace("AFK", "").replace("AFК", "").replace("АFK", "").replace("АFК", "")
        old_nick = move_7.replace("AФK", "").replace("AФК", "").replace("АФK", "").replace("АФК", "")

        if ctx.channel.id in channels[str(ctx.guild.id)]:
            if "[AFK]" in current_nick or "[AFК]" in current_nick or "[АFK]" in current_nick or "[АFК]" in current_nick or \
               "[AФK]" in current_nick or "[AФК]" in current_nick or "[АФK]" in current_nick or "[АФК]" in current_nick or \
               "AFK]" in current_nick or "AFК]" in current_nick or "АFK]" in current_nick or "АFК]" in current_nick or \
               "AФK]" in current_nick or "AФК]" in current_nick or "АФK]" in current_nick or "АФК]" in current_nick or \
               "[AFK" in current_nick or "[AFК" in current_nick or "[АFK" in current_nick or "[АFК" in current_nick or \
               "[AФK" in current_nick or "[AФК" in current_nick or "[АФK" in current_nick or "[АФК" in current_nick or \
               "AFK" in current_nick or "AFК" in current_nick or "АFK" in current_nick or "АFК" in current_nick or \
               "AФK" in current_nick or "AФК" in current_nick or "АФK" in current_nick or "АФК" in current_nick:
                await ctx.author.edit(nick=old_nick)
                await ctx.send(f'{ctx.author.mention} вышел из АФК')
            else:
                nick = f"[AFK] {current_nick}"
                await ctx.author.edit(nick=nick)
                await ctx.send(f'{current_nick} ушел в АФК')
        else:
            await ctx.send(error_message, delete_after=time_10s)
            
            ctx.command.reset_cooldown(ctx)
            
    @afk.error
    async def afk_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)

    @commands.command(name=comm_ball, aliases=aliaces_ball)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def magic_eight_ball(self, ctx, *, arg=None):
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
            else:
                embed = discord.Embed(color=discord.Colour.random(), title='')
                embed.add_field(name=arg, value=random.choice(ball), inline=False)
                await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)
            
            ctx.command.reset_cooldown(ctx)

    @magic_eight_ball.error
    async def ball_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)

    @commands.command(name=comm_hit, aliases=aliaces_hit)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def hit(self, ctx, member: discord.Member = None):
        mam = ctx.author.mention
        mum = member.mention
        if ctx.channel.id in channels[str(ctx.guild.id)]:
            if member == ctx.author:
                await ctx.channel.purge(limit=1)
                await ctx.send(error_ctx_user, delete_after=time_10s)
            else:
                embed = discord.Embed(
                    color=discord.Colour.random(),
                    description=random.choice(hit).format(mam, mum)
                )
                embed.set_image(url=tenor.random(str(f'{comm_hit} anime')))
                await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)
            
            ctx.command.reset_cooldown(ctx)
            
    @hit.error
    async def hit_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)

        if isinstance(error, commands.MemberNotFound):
            await ctx.message.delete()
            await ctx.send(error_member, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)

        if isinstance(error, commands.CommandError):
            await ctx.message.delete()

            embed = discord.Embed(color=discord.Colour.random())
            embed.add_field(name='Ошибка', value=error_comm + prefix[str(ctx.guild.id)] + comm_hit + error_comm_nick)
            await ctx.send(embed=embed, delete_after=time_5s)

            ctx.command.reset_cooldown(ctx)

    @commands.command(name=comm_hugs, aliases=aliaces_hugs)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def hugs(self, ctx, member: discord.Member = None):
        mam = ctx.author.mention
        mum = member.mention
        if ctx.channel.id in channels[str(ctx.guild.id)]:
            if member == ctx.author:
                await ctx.channel.purge(limit=1)
                await ctx.send(error_ctx_user, delete_after=time_10s)
            else:
                embed = discord.Embed(
                    color=discord.Colour.random(),
                    description=random.choice(hugs).format(mam, mum)
                )
                embed.set_image(url=tenor.random(str(f'{comm_hugs} anime')))
                await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)
            
            ctx.command.reset_cooldown(ctx)
            
    @hugs.error
    async def hugs_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)

        if isinstance(error, commands.MemberNotFound):
            await ctx.message.delete()
            await ctx.send(error_member, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)

        if isinstance(error, commands.CommandError):
            await ctx.message.delete()

            embed = discord.Embed(color=discord.Colour.random())
            embed.add_field(name='Ошибка', value=error_comm + prefix[str(ctx.guild.id)] + comm_hugs + error_comm_nick)
            await ctx.send(embed=embed, delete_after=time_5s)

            ctx.command.reset_cooldown(ctx)

    @commands.command(name=comm_kill, aliases=aliaces_kill)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def kill(self, ctx, *, member: discord.Member = None):
        mam = ctx.author.mention  # тег автора
        mum = member.mention  # тег участника
        if ctx.channel.id in channels[str(ctx.guild.id)]:
            if member is None:
                await ctx.channel.purge(limit=1)
                await ctx.send("Error", delete_after=time_5s)
            else:
                if member == ctx.author:
                    await ctx.channel.purge(limit=1)
                    await ctx.send(error_ctx_user, delete_after=time_10s)
                else:
                    embed = discord.Embed(
                        color=discord.Colour.random(),
                        description=random.choice(kill).format(mam, mum)
                    )
                    embed.set_image(url=tenor.random(str(f'{comm_kill} anime')))
                    await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)
            
            ctx.command.reset_cooldown(ctx)
            
    @kill.error
    async def kill_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)

        if isinstance(error, commands.MemberNotFound):
            await ctx.message.delete()
            await ctx.send(error_member, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)

        if isinstance(error, commands.CommandError):
            await ctx.message.delete()

            embed = discord.Embed(color=discord.Colour.random())
            embed.add_field(name='Ошибка', value=error_comm + prefix[str(ctx.guild.id)] + comm_kill + error_comm_nick)
            await ctx.send(embed=embed, delete_after=time_5s)

            ctx.command.reset_cooldown(ctx)

    @commands.command(name=comm_kiss, aliaces=aliaces_kiss)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def kiss(self, ctx, *, member: discord.Member = None):
        mam = ctx.author.mention
        mum = member.mention
        if ctx.channel.id in channels[str(ctx.guild.id)]:
            if member == ctx.author:
                await ctx.channel.purge(limit=1)
                await ctx.send(error_ctx_user, delete_after=time_10s)
            else:
                embed = discord.Embed(
                    color=discord.Colour.random(),
                    description=random.choice(kiss).format(mam, mum)
                )
                embed.set_image(url=tenor.random(str(f'{comm_kiss} anime')))
                await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)
            
            ctx.command.reset_cooldown(ctx)
            
    @kiss.error
    async def kiss_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)

        if isinstance(error, commands.MemberNotFound):
            await ctx.message.delete()
            await ctx.send(error_member, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)

        if isinstance(error, commands.CommandError):
            await ctx.message.delete()

            embed = discord.Embed(color=discord.Colour.random())
            embed.add_field(name='Ошибка', value=error_comm + prefix[str(ctx.guild.id)] + comm_kiss + error_comm_nick)
            await ctx.send(embed=embed, delete_after=time_5s)

            ctx.command.reset_cooldown(ctx)

    @commands.command(name=comm_login, aliases=aliaces_login)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def enter(self, ctx):
        mam = ctx.author.mention  # тег автора
        if ctx.channel.id in channels[str(ctx.guild.id)]:
            await ctx.send(random.choice(login).format(mam))
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)
            
            ctx.command.reset_cooldown(ctx)
            
    @enter.error
    async def enter_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)

    @commands.command(name=comm_logout, aliases=aliaces_logout)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def logout(self, ctx):
        mam = ctx.author.mention  # тег автора
        if ctx.channel.id in channels[str(ctx.guild.id)]:
            await ctx.send(random.choice(logout).format(mam))
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)
            
            ctx.command.reset_cooldown(ctx)

    @logout.error
    async def logout_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)

    @commands.command(name=comm_pats, aliases=aliaces_pats)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def pat(self, ctx, member: discord.Member = None):
        mam = ctx.author.mention
        mum = member.mention
        if ctx.channel.id in channels[str(ctx.guild.id)]:
            if member == ctx.author:
                await ctx.channel.purge(limit=1)
                await ctx.send(error_ctx_user, delete_after=time_10s)
            else:
                embed = discord.Embed(
                    color=discord.Colour.random(),
                    description=random.choice(pats).format(mam, mum)
                )
                embed.set_image(url=tenor.random(str(f'{comm_pats} anime')))
                await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)
            
            ctx.command.reset_cooldown(ctx)

    @pat.error
    async def pat_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)
            
        if isinstance(error, commands.MemberNotFound):
            await ctx.message.delete()
            await ctx.send(error_member, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)

        if isinstance(error, commands.CommandError):
            await ctx.message.delete()

            embed = discord.Embed(color=discord.Colour.random())
            embed.add_field(name='Ошибка', value=error_comm + prefix[str(ctx.guild.id)] + comm_pats + error_comm_nick)
            await ctx.send(embed=embed, delete_after=time_5s)

            ctx.command.reset_cooldown(ctx)

    @commands.command(name=comm_poke, aliases=aliaces_poke)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def poke(self, ctx, member: discord.Member = None):
        mam = ctx.author.mention
        mum = member.mention
        if ctx.channel.id in channels[str(ctx.guild.id)]:
            if member == ctx.author:
                await ctx.channel.purge(limit=1)
                await ctx.send(error_ctx_user, delete_after=time_10s)
            else:
                embed = discord.Embed(
                    colour=discord.Colour.random(),
                    description=random.choice(poke).format(mam, mum)
                )
                embed.set_image(url=tenor.random(str(f'{comm_poke} anime')))
                await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)
            
            ctx.command.reset_cooldown(ctx)

    @poke.error
    async def poke_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)

        if isinstance(error, commands.MemberNotFound):
            await ctx.message.delete()
            await ctx.send(error_member, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)

        if isinstance(error, commands.CommandError):
            await ctx.message.delete()

            embed = discord.Embed(color=discord.Colour.random())
            embed.add_field(name='Ошибка', value=error_comm + prefix[str(ctx.guild.id)] + comm_poke + error_comm_nick)
            await ctx.send(embed=embed, delete_after=time_5s)

            ctx.command.reset_cooldown(ctx)

    @commands.command(name=comm_rip, aliases=aliaces_rip)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def rip(self, ctx):
        mam = ctx.author.mention  # тег автора
        if ctx.channel.id in channels[str(ctx.guild.id)]:
            await ctx.send(random.choice(rip).format(mam))
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)
            
            ctx.command.reset_cooldown(ctx)
            
    @rip.error
    async def rip_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)

    @commands.command(name=comm_snow, aliases=aliaces_snowball)
    @commands.has_any_role(*roles)
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def snowball(self, ctx, member: discord.Member=None):
        mam = ctx.author.mention  # тег автора
        mum = member.mention  # тег участника
        if ctx.channel.id in channels[str(ctx.guild.id)]:
            if member is None:
                await ctx.channel.purge(limit=1)
                await ctx.send("Error")
            else:
                if member == ctx.author:
                    await ctx.channel.purge(limit=1)
                    await ctx.send("Ошибка, вы не можете использовать эту команду против себя", delete_after=time_10s)
                else:
                    await ctx.send(random.choice(snowball).format(mam, mum))
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(error_message, delete_after=time_10s)
            
            ctx.command.reset_cooldown(ctx)

    @snowball.error
    async def snowball_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)

            ctx.command.reset_cooldown(ctx)
            
        if isinstance(error, commands.MemberNotFound):
            await ctx.message.delete()
            await ctx.send(error_member, delete_after=time_5s)

            ctx.command.reset_cooldown(ctx)

        if isinstance(error, commands.CommandError):
            await ctx.message.delete()

            embed = discord.Embed(color=discord.Colour.random())
            embed.add_field(name='Ошибка', value=error_comm + prefix[str(ctx.guild.id)] + comm_snow + error_comm_nick)
            await ctx.send(embed=embed, delete_after=time_5s)

            ctx.command.reset_cooldown(ctx)

def setup(bot):
    bot.add_cog(Funny(bot))
