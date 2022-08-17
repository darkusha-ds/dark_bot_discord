from config import *
from settings import *
from phrazes import *

# Дьяволенок v1
tok = D_v1["token"]

# Дьяволенок v2
# tok = D_v2["token"]


def get_prefix(bot, message):
    with open("jsons/prefix.json", "r") as f:
        prefix = json.load(f)
    return prefix[str(message.guild.id)]

intents = discord.Intents.default()
intents.members = True

tenor = TenGiphPy.Tenor(token=teno["token"])
bot = commands.Bot(command_prefix=get_prefix, intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    bot.togetherControl = await DiscordTogether(tok)
    channel = bot.get_channel(load_bot)
    print("We have logged in as {0.user}".format(bot))
    await channel.send(f"=====================================\n"
                       "{0.user} ".format(bot) + f"load {dt.now(pytz.timezone(region)).strftime(time_format)}")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(f'Напишите help для просмотра команд'))

# SET PREFIX FOR EACH SERVER
@bot.event
async def on_guild_join(guild):
    prefix[str(guild.id)] = "$"
    write_json(json_prefix, prefix)
        
    roles[str(guild.id)] = []
    write_json(json_roles, roles)
        
    channels[str(guild.id)] = []
    write_json(json_channels, channels)
        
    owners[str(guild.id)] = str(guild.owner.id)
    write_json(json_owners, owners)
        
    mute_roles[str(guild.id)] = ""
    write_json(json_mutes, mute_roles)

# @bot.event
# async def on_guild_remove(guild):
#     prefix.pop(str(guild.id))
#     with open("jsons/prefix.json", "w") as f:
#         json.dump(prefix, f, indent=4)
    
#     roless.pop(str(guild.id))
#     with open("jsons/roles.json", "w") as f:
#         json.dump(roless, f, indent=4)
    
#     channels.pop(str(guild.id))
#     with open("jsons/channels.json", "w") as f:
#         json.dump(channels, f, indent=4)
    
#     owners.pop(str(guild.id))
#     with open("jsons/owners.json", "w") as f:
#         json.dump(owners, f, indent=4)


# COGS FOR COMMANDS
@bot.command()
async def load(ctx, extension):
    if ctx.author.id == 391682780322594840:
        bot.load_extension(f'cogs.{extension}')
        await ctx.message.add_reaction("✅")
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send("You aren't bot creator", delete_after=time_5s)

@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == 391682780322594840:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.message.add_reaction("✅")
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send("You aren't bot creator", delete_after=time_5s)

@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == 391682780322594840:
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
        await ctx.message.add_reaction("✅")
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send("You aren't bot creator", delete_after=time_5s)


# ERROR COMMAND
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        retry_after = str(datetime.timedelta(seconds=error.retry_after)).split('.')[0]
        await ctx.channel.purge(limit=1)
        await ctx.send(f'**ЭЭЭ, харе спамить, приходи через {retry_after}**', delete_after=time_5s)

# COGS LOAD FROM DIR
for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and not filename.startswith("_"):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(tok)

# 𝕯𝖆𝖗𝖐 𝕬𝖓𝖌𝖊𝖑
