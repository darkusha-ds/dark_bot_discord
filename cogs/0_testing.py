from main import *
from settings import *
from phrazes import *


class testing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))
    
    @commands.command()
    async def test(self, ctx, texf: str = "asd"):
        await ctx.send('Тест прошел успешно!')
    #     with open("jsons/test.json", "r") as r:
    #         test_json = json.load(r)

    #     # test_json[str(ctx.guild.id)][0][str(ctx.author.id)] = []
    #     test_json[str(ctx.guild.id)][0][str(ctx.author.id)] = texf

    #     with open("jsons/test.json", "w") as out:
    #         json.dump(test_json, out, ensure_ascii=False, indent=4)
    #     await ctx.send(test_json[str(ctx.guild.id)])
    
    # @commands.command()
    # async def test2(self, ctx):
    #     with open("jsons/test.json", "r") as r:
    #         test_json = json.load(r)

    #     test_json[str(ctx.guild.id)][0].pop(str(ctx.author.id))

    #     with open("jsons/test.json", "w") as out:
    #         json.dump(test_json, out, ensure_ascii=False, indent=4)
    #     await ctx.send(test_json[str(ctx.guild.id)])

def setup(bot):
    bot.add_cog(testing(bot))

# roles_list = [role.id for role in ctx.guild.roles]