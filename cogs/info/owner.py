from main import *

class owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))

    
    # @commands.command(name=comm_userinfo, aliases=aliaces_userinfo)
    # # @commands.has_any_role(*roles)
    # # @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    # async def owner(self, ctx, member: discord.Member = None):
    #     if member is None:
    #         member = ctx.author
    #     embed = discord.Embed(title=f"Info {member.name}")
    #     embed.set_thumbnail(url=member.avatar_url)
    #     embed.add_field(name="ID", value=member.id, inline=True)
    #     embed.add_field(name="Nickname", value=member.display_name, inline=True)
    #     embed.add_field(name="Top role", value=member.top_role.mention, inline=True)
    #     embed.add_field(name="Created at", value=member.created_at.strftime("%d.%m.%Y %H:%M:%S"), inline=True)
    #     embed.add_field(name="Joined at", value=member.joined_at.strftime("%d.%m.%Y %H:%M:%S"), inline=True)
    #     embed.add_field(name="Bot?", value=member.bot, inline=True)
    #     await ctx.send(embed=embed)
    

def setup(bot):
    bot.add_cog(owner(bot))
