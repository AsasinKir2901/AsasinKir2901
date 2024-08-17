import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

img_url = ['https://mo.hartiya.com/upload/iblock/9cf/1_14.jpg',
           'https://hobbi.guru/wp-content/uploads/2023/01/800fd77fa8cc252fdee83c572d533de7.jpeg',
           'https://9b6bfb45-2bd9-42bf-ad07-e1af1c458da3.selstorage.ru/main/c/c8b3d7035e42b5170f00908735985c68.jpg',
           'https://yazhevika.ru/wp-content/uploads/2023/09/podelki-iz-musora-187.png',
           'https://kak-svoimi-rukami.com/images/2022/04/podelki-iz-musora-svoimi-rukami-2.jpg',]

@bot.command()
async def sort_musor(ctx):
    await ctx.send('''Зачем нужно сортировать мусор
                   
Чтобы из общей массы мусора выделить полезные отходы, пригодные для дальнейшей переработки и использования, нужно разделять его на этапе возникновения.

Наряду с обычными отходами, существуют опасные виды мусора, утилизация которых требует соблюдения специальных норм и правил. Чтобы минимизировать их негативное влияние на экологию планеты, надо отдельно складировать предметы, несущие потенциальную угрозу. В дальнейшем требуется сдача опасных отходов организациям, обеспечивающим их утилизацию без негативного влияния на окружающую среду.

Задачи, решаемые благодаря раздельному сбору отходов:
                   
снижение потребления природных ресурсов из-за использования вторсырья;                  
сокращение объема складируемого мусора на полигонах ТБО и несанкционированных свалках;    
улучшение экологической обстановки;
сокращение расходов на повторную переработку.''')
    
@bot.command()
async def diy(ctx):
    await ctx.send(random.choice(img_url))

@bot.command()
async def commands(ctx):
    await ctx.send('''
diy
sort_musor
video
    ''')

@bot.command()
async def video(ctx):
    await ctx.send('''
https://www.google.com/search?q=%D1%87%D1%82%D0%BE+%D0%BC%D0%BE%D0%B3%D1%83%D1%82+%D1%81%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C+%D0%BF%D0%BE%D0%B4%D1%80%D0%BE%D1%81%D1%82%D0%BA%D0%B8+%D1%87%D1%82%D0%BE%D0%B1%D1%8B+%D1%81%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C+%D1%81%D0%B2%D0%BE%D0%B9+%D1%80%D0%BE%D0%B4%D0%BD%D0%BE%D0%B9+%D0%B3%D0%BE%D1%80%D0%BE%D0%B4+%D1%87%D0%B8%D1%89%D0%B5+%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE&sca_esv=e29e6d704abed028&sca_upv=1&biw=1920&bih=953&sxsrf=ADLYWIJhOGxPE8f0drzdNr8GSez-mlP59w%3A1723877988758&ei=ZErAZs33LZ3s7_UP0caigQU&ved=0ahUKEwjNuZ_5ufuHAxUd9rsIHVGjKFAQ4dUDCA8&uact=5&oq=%D1%87%D1%82%D0%BE+%D0%BC%D0%BE%D0%B3%D1%83%D1%82+%D1%81%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C+%D0%BF%D0%BE%D0%B4%D1%80%D0%BE%D1%81%D1%82%D0%BA%D0%B8+%D1%87%D1%82%D0%BE%D0%B1%D1%8B+%D1%81%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C+%D1%81%D0%B2%D0%BE%D0%B9+%D1%80%D0%BE%D0%B4%D0%BD%D0%BE%D0%B9+%D0%B3%D0%BE%D1%80%D0%BE%D0%B4+%D1%87%D0%B8%D1%89%D0%B5+%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE&gs_lp=Egxnd3Mtd2l6LXNlcnAiggHRh9GC0L4g0LzQvtCz0YPRgiDRgdC00LXQu9Cw0YLRjCDQv9C-0LTRgNC-0YHRgtC60Lgg0YfRgtC-0LHRiyDRgdC00LXQu9Cw0YLRjCDRgdCy0L7QuSDRgNC-0LTQvdC-0Lkg0LPQvtGA0L7QtCDRh9C40YnQtSDQstC40LTQtdC-SABQAFgAcAB4AZABAJgBAKABAKoBALgBA8gBAPgBAZgCAKACAJgDAJIHAKAHAA&sclient=gws-wiz-serp#fpstate=ive&vld=cid:3dddf5d8,vid:Gb0smDHUs9A,st:0)
''')


bot.run('ne_dam')
