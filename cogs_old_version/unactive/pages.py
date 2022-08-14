import discord, datetime
from discord.ext import commands
from dpymenus import Page, PaginatedMenu
from imports import *

class pages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bt.get_channel(l_bot)
        await channel.send(f"pages load at {datetime.datetime.now(dt_rg).strftime('%Y-%m-%d %H:%M:%S')}")

    @commands.command()
    async def pages(self, ctx):
        p1 = Page(title='Page 1', description='First page test!')
        p1.add_field(name='Example A', value='Example B')

        p2 = Page(title='Page 2', description='Second page test!')
        p2.add_field(name='Example C', value='Example D')

        p3 = Page(title='Page 3', description='Third page test!')
        p3.add_field(name='Example E', value='Example F')

        menu = PaginatedMenu(ctx)
        menu.add_pages([p1, p2, p3])
        await menu.open()

def setup(bot):
    bot.add_cog(pages(bot))
