import discord, datetime
from discord.ext import commands
from imports import *

inter_client = InteractionClient(bt)

class dropdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bt.get_channel(l_bot)
        await channel.send(f"dropdown load at {datetime.datetime.now(dt_rg).strftime('%Y-%m-%d %H:%M:%S')}")

    # @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.command()
    async def drop(self, ctx):
        msg = await ctx.send(
            "This message has a select menu!",
            components=[
                SelectMenu(
                    custom_id="test",
                    placeholder="Choose up to 1 option",
                    max_values=1,
                    options=[
                        SelectOption("Option 1", "value 1"),
                        SelectOption("Option 2", "value 2"),
                        SelectOption("Option 3", "value 3")
                    ]
                )
            ]
        )
        # Wait for someone to click on it
        inter = await msg.wait_for_dropdown()
        # Send what you received
        labels = [option.label for option in inter.select_menu.selected_options]
        await inter.reply(f"Options: {', '.join(labels)}")

def setup(bot):
    bot.add_cog(dropdown(bot))
