import discord, datetime, random
from discord.ext import commands
from discord_components import DiscordComponents, Button, SelectOption, Select
from imports import *

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        DiscordComponents(self.bot)
        channel = bt.get_channel(l_bot)
        await channel.send(f"test load at {datetime.datetime.now(dt_rg).strftime('%Y-%m-%d %H:%M:%S')}")

    @commands.command()
    async def test(self, ctx):
        emb = discord.Embed(
            title='Навигация по командам :clipboard:',
            colour=(discord.Colour.random())
        )
        emb.add_field(name='**Основные команды**', value=f'''
        ``{pr}тык``\nзатыкать человечка
        ``{pr}убить``\nубить злого человека
        ``{pr}снежок``\nкинуть снежок в человечка
        ``{pr}обнять``\nустроить обнимашки
        ``{pr}умереть``\nсделать самоубийство(ОСУЖДАЮ)
        ``{pr}погладить``\nпогладить сладкого пирожка
        ``{pr}поцеловать``\nпочеловать человечка
        ``{pr}afk``\nвойти в АФК
        ``{pr}exit``\nвыйти из АФК
        ``{pr}зайти``
        ``{pr}выйти``
        ''', inline=False)
        emb.add_field(name='**Приколюшки**', value=f'''
        ``{pr}password``\nгенератор паролей
        ``{pr}key``\nгенератор uuid идентификатора
        ``{pr}шар``\nзадать вопрос магическому шару
        ``{pr}ютуб``\nпосмотреть ютубчик в дискорде
           P.S чтобы посмотреть ют, надо зайти в голосовой
        ''', inline=False)
        await ctx.send(
            "Описание",
            components=[
                Select(
                    placeholder="Выберите группу...",
                    options=[
                        SelectOption(label="1", emoji='🌈', value=f"value1"),
                        SelectOption(label="2", emoji='🌈', value=f"value2"),
                        SelectOption(label="3", emoji='🌈', value=f"value3"),
                        SelectOption(label="4", emoji='🌈', value=f"value4"),
                    ],
                    custom_id="select1",
                )
            ],
        )

        while True:
            interaction = await bot.wait_for(
                "select_option", check=lambda inter: inter.custom_id == "select1"
            )
            await interaction.send(content=interaction.value[0])

# await interaction.send(embed=emb)

def setup(bot):
    bot.add_cog(test(bot))
