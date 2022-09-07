from main import *

class fun_afk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command(name=comm_afk, aliases=aliaces_afk)
    @commands.cooldown(rate=1, per=300, type=commands.BucketType.user)
    async def afk(self, ctx):
        current_nick = ctx.author.nick
        old_nick = current_nick.replace("[AFK]", "").replace("[AFК]", "").replace("[АFK]", "").replace("[АFК]", "").replace("[AФK]", "").replace("[AФК]", "").replace("[АФK]", "").replace("[АФК]", "").replace("AFK]", "").replace("AFК]", "").replace("АFK]", "").replace("АFК]", "").replace("AФK]", "").replace("AФК]", "").replace("АФK]", "").replace("АФК]", "").replace("[AFK", "").replace("[AFК", "").replace("[АFK", "").replace("[АFК", "").replace("[AФK", "").replace("[AФК", "").replace("[АФK", "").replace("[АФК", "").replace("AFK", "").replace("AFК", "").replace("АFK", "").replace("АFК", "").replace("AФK", "").replace("AФК", "").replace("АФK", "").replace("АФК", "")

        for role in ctx.author.roles:
            if role.id in roles[str(ctx.guild.id)]:
                if ctx.channel.id in channels[str(ctx.guild.id)]:
                    if "[AFK]" in current_nick or "[AFК]" in current_nick or "[АFK]" in current_nick or "[АFК]" in current_nick or "[AФK]" in current_nick or "[AФК]" in current_nick or "[АФK]" in current_nick or "[АФК]" in current_nick or "AFK]" in current_nick or "AFК]" in current_nick or "АFK]" in current_nick or "АFК]" in current_nick or "AФK]" in current_nick or "AФК]" in current_nick or "АФK]" in current_nick or "АФК]" in current_nick or "[AFK" in current_nick or "[AFК" in current_nick or "[АFK" in current_nick or "[АFК" in current_nick or "[AФK" in current_nick or "[AФК" in current_nick or "[АФK" in current_nick or "[АФК" in current_nick or "AFK" in current_nick or "AFК" in current_nick or "АFK" in current_nick or "АFК" in current_nick or "AФK" in current_nick or "AФК" in current_nick or "АФK" in current_nick or "АФК" in current_nick:
                        await ctx.author.edit(nick=old_nick)
                        await ctx.send(f'{ctx.author.mention} вышел из АФК')
                        return
                    else:
                        nick = f"[AFK] {current_nick}"
                        await ctx.author.edit(nick=nick)
                        await ctx.send(f'{current_nick} ушел в АФК')
                    return
                else:
                    await ctx.send(error_message, delete_after=time_10s)
                    
                    ctx.command.reset_cooldown(ctx)
                    return
                return
        else:
            await ctx.message.delete()
            await ctx.send(error_perms, delete_after=time_5s)
            
            ctx.command.reset_cooldown(ctx)
       
       
def setup(bot):
    bot.add_cog(fun_afk(bot))
