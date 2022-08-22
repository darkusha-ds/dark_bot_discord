from main import *
from settings import *
from phrazes import *


class mut(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))


    @commands.command()
    async def tempmute(self, ctx, member: discord.Member, time, *, reason=None):
        if discord.utils.get(ctx.guild.roles, id=mute_roles[str(ctx.guild.id)]):
            muted_role = discord.utils.get(ctx.guild.roles, id=mute_roles[str(ctx.guild.id)])
        else:
            perms = discord.Permissions(send_messages=False, add_reactions=False, connect=False, speak=False)
            await ctx.guild.create_role(name='Muted', permissions=perms)
            muted_role = discord.utils.get(ctx.guild.roles, name='Muted')

        time_convert = {'s' : 1 , 'm' : 60 , 'h' : 3600 , 'd' : 86400, 'y' : 31536000, 'с' : 1 , 'м' : 60 , 'ч' : 3600 , 'д' : 86400, 'г' : 31536000}
        end_time = time[-1]
        start_time = int(time[:-1])
        mute_time = start_time * time_convert[end_time]
        role_if_muted = discord.utils.find(lambda r: r.id == mute_roles[str(ctx.guild.id)], ctx.guild.roles)

        if role_if_muted in member.roles:
            alreadymuted_embed = discord.Embed(title='Already Muted!', description=f'The user, {member.mention} is already muted for {mute_time} seconds.', color=0xff0000)
            alreadymuted_embed.set_footer(text=ctx.author)
            alreadymuted_embed.set_author(name="{0.user}".format(bot))
            await ctx.channel.send(embed=alreadymuted_embed)
        else:
            if reason == None:
                await member.add_roles(muted_role)
                tempmuted_embed = discord.Embed(title='Temporary Mute Successfull!', description=f'{member.mention} has been muted for {mute_time} seconds successfully! \n \n Reason: No reason given.', color=0x4fff4d)
                tempmuted_embed.set_author(name="{0.user}".format(bot))
                tempmuted_embed.set_footer(text=ctx.author)
            else:
                await member.add_roles(muted_role)
                tempmuted_embed = discord.Embed(title='Temporary Mute Successfull!', description=f'{member.mention} has been muted for {mute_time} seconds successfully! \n \n Reason: {reason}', color=0x4fff4d)
                tempmuted_embed.set_author(name="{0.user}".format(bot))
                tempmuted_embed.set_footer(text=ctx.author)

        await ctx.channel.send(embed=tempmuted_embed)
        await asyncio.sleep(mute_time)
        await member.remove_roles(muted_role)


    @commands.command()
    async def unmute2(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, id=mute_roles[str(ctx.guild.id)])
        await member.remove_roles(role)
        await ctx.send(f"{ctx.author.name} unmute {member.display_name}")
        mutes = load_json("jsons/mutes.json")
        mutes[str(ctx.guild.id)][0].pop(str(member.id))
        write_json("jsons/mutes.json", mutes)

def setup(bot):
    bot.add_cog(mut(bot))