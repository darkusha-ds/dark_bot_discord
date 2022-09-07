from main import *


class moder_mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = bot.get_channel(load_bot)
        await channel.send('Module {} is loaded'.format(self.__class__.__name__))


    @commands.command(name=comm_mute, aliaces=aliaces_mute)
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member, amout, *, reason = 'не указана'):
        times_start = datetime.datetime.today()
        emb_user = discord.Embed(title = '**Уведомление - Mute**', color = 0xe74c3c)
        emb_user.add_field(name = '**Выдал:**', value = ctx.author.mention, inline = False)
        emb_user.add_field(name = '**Причина:**', value = reason, inline = False)
        emb_user.add_field(name = '**Длительность:**', value = amout, inline = False)
        emb_user.add_field(name = '**Сервер:**', value = ctx.guild.name, inline = False)
        emb_user.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')
    
        emb_user_stop = discord.Embed(title = '**Уведомление - Unmute**', color = 0xe74c3c)
        emb_user_stop.add_field(name = '**Снял:**', value = ctx.author.mention, inline = False)
        emb_user_stop.add_field(name = '**Сервер:**', value = ctx.guild.name, inline = False)
        emb_user_stop.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')

        emb_unmute = discord.Embed(title = '**System - Unmute**', color = 0xe74c3c)
        emb_unmute.add_field(name = '**Снял:**', value = ctx.author.mention, inline = False)
        emb_unmute.add_field(name = '**Нарушитель:**', value = member.mention, inline = False)
        emb_unmute.add_field(name = '**ID нарушителя:**', value = member.id, inline = False)
        emb_unmute.add_field(name = '**Причина:**', value = 'окончание наказания', inline = False)
        emb_unmute.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')

        muted_role = discord.utils.get(ctx.guild.roles, id=mute_roles[str(ctx.guild.id)])

        time_convert = {'s' : 1, 'm' : 60, 'h' : 3600, 'd' : 86400, 'y' : 31536000, 'с' : 1, 'м' : 60, 'ч' : 3600, 'д' : 86400, 'г' : 31536000}
        start_time = int(amout[:-1])
        end_time = amout[-1:]
        time = start_time * time_convert[end_time]
    
        if member is None:
            emb = discord.Embed(title = '[ERROR] Mute', description = f'{ctx.author.mention}, Укажите пользователя!', color = 0xe74c3c)
            emb.add_field(name = 'Пример:', value = f'{prefix[str(ctx.guild.id)]}мьют [@участник] <время(с/s, м/m, ч/h, д/d)> [причина]', inline = False)
            emb.add_field(name = 'Пример 1:', value = f'{prefix[str(ctx.guild.id)]}мьют @Xpeawey 1ч пример')
            emb.add_field(name = 'Время:', value = f'с/s - секунды\nм/m - минуты\nч/h - часы\nд/d - дни')
    
            await ctx.send(embed = emb)
        
        if muted_role in member.roles:
            emb = discord.Embed(title='[ERROR] Mute', description=f'{member.mention} уже наказан.', color=0xff0000)
            emb.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')
    
            await ctx.send(embed = emb)

        else:
            if end_time == 'с' or end_time == 's':
                emb = discord.Embed(title = f'**System - Mute**', color = 0xe74c3c)
                emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
                emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
                emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
                emb.add_field(name = 'Причина:', value = reason, inline = False)
                emb.add_field(name = 'Длительность:', value = '{} секунд'.format(start_time))
                emb.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')

            elif end_time == 'м' or end_time == 'm':
                emb = discord.Embed(title = f'**System - Mute**', color = 0xe74c3c)
                emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
                emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
                emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
                emb.add_field(name = 'Причина:', value = reason, inline = False)
                emb.add_field(name = 'Длительность:', value = '{} минут'.format(start_time))
                emb.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')

            elif end_time == 'ч' or end_time == 'h':
                emb = discord.Embed(title = f'**System - Mute**', color = 0xe74c3c)
                emb.add_field(name = '**Выдал:**', value = ctx.author.mention, inline = False)
                emb.add_field(name = '**Нарушитель:**', value = member.mention, inline = False)
                emb.add_field(name = '**ID нарушителя:**', value = member.id, inline = False)
                emb.add_field(name = '**Причина:**', value = reason, inline = False)
                emb.add_field(name = '**Длительность:**', value = '{} час(ов)'.format(start_time))
                emb.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')

            elif time == 'д' or time == 'd':
                emb = discord.Embed(title = f'**System - Mute**', color = 0xe74c3c)
                emb.add_field(name = '**Выдал:**', value = ctx.author.mention, inline = False)
                emb.add_field(name = '**Нарушитель:**', value = member.mention, inline = False)
                emb.add_field(name = '**ID нарушителя:**', value = member.id, inline = False)
                emb.add_field(name = '**Причина:**', value = reason, inline = False)
                emb.add_field(name = '**Длительность:**', value = '{} день(ей)'.format(start_time), inline = False)
                emb.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')


            await member.add_roles(muted_role)
            await ctx.send(embed = emb)
            await member.send(embed = emb_user)
            await asyncio.sleep(time)
            await member.remove_roles(muted_role)
            await ctx.send(embed = emb_unmute)
            await member.send(embed = emb_user_stop)
    

    @commands.command(name=comm_unmute, aliaces=aliaces_unmute)
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: discord.Member = None):
        times_start = datetime.datetime.today()
        
        emb_user_stop = discord.Embed(title = '**Уведомление - Unmute**', color = 0xe74c3c)
        emb_user_stop.add_field(name = '**Снял:**', value = ctx.author.mention, inline = False)
        emb_user_stop.add_field(name = '**Сервер:**', value = ctx.guild.name, inline = False)
        emb_user_stop.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')
        mute_role = discord.utils.get(ctx.guild.roles, id = mute_roles[str(ctx.guild.id)])

        await member.remove_roles(mute_role)
        await member.send(embed = emb_user_stop)
    

def setup(bot):
    bot.add_cog(moder_mute(bot))
