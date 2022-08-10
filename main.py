import discord, os, datetime, pytz, TenGiphPy, random
from discord.ext import commands
from discord_together import DiscordTogether
from datetime import datetime as dt
from config import *
from settings import *

# Дьяволенок v1
pref = D_v1["prefix"]
tok = D_v1["token"]

# Дьяволенок v2
# pref = D_v2["prefix"]
# tok = D_v2["token"]

tenor = TenGiphPy.Tenor(token=teno["token"])
bot = commands.Bot(command_prefix=pref)
bot.remove_command("help")

@bot.event
async def on_ready():
    bot.togetherControl = await DiscordTogether(tok)
    channel = bot.get_channel(load_bot)
    print("We have logged in as {0.user}".format(bot))
    await channel.send(f"=====================================\n"
                       "{0.user} ".format(bot) + f"load {dt.now(pytz.timezone(region)).strftime(time_format)}"
                       f"\n=====================================")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(f'{pref}help'))

@bot.command()
async def load(ctx, extension):
    if ctx.author.id in admins_id:
        bot.load_extension(f'cogs.{extension}')
        await ctx.message.add_reaction("✅")
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send("You aren't bot creator", delete_after=time_5s)

@bot.command()
async def unload(ctx, extension):
    if ctx.author.id in admins_id:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.message.add_reaction("✅")
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send("You aren't bot creator", delete_after=time_5s)

@bot.command()
async def reload(ctx, extension):
    if ctx.author.id in admins_id:
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
        await ctx.message.add_reaction("✅")
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send("You aren't bot creator", delete_after=time_5s)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        retry_after = str(datetime.timedelta(seconds=error.retry_after)).split('.')[0]
        await ctx.channel.purge(limit=1)
        await ctx.send(f'**Вы устали! Приходите через {retry_after}**', delete_after=time_5s)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(tok)

# 𝕯𝖆𝖗𝖐 𝕬𝖓𝖌𝖊𝖑
