import nextcord 
import asyncio
from opengsq.protocols import Source
import datetime as DT
from nextcord.ext import commands,tasks
from nextcord.ext.commands import has_permissions, MissingPermissions

from nextcord.ext import tasks



Token = 'token'
ip = 'ip'
port = 2365


bot = commands.Bot(command_prefix='!')
bot.remove_command("help")

@bot.event  # сообщение подключение
async def on_ready():
    print("Подключился к серверу!")
    send_cha.start()
    
@tasks.loop(seconds=90)
async def send_cha():
    try:
        source = Source(address=ip, query_port=port)
        info = await source.get_info()
        #print(info)
        time = info['Keywords'].split(',')[-1]
        Players = info['Players']
        maxPlayers = info['MaxPlayers']
        #print(f"Игроков на сервере:{Players}/{maxPlayers}\nвремя: {time}")
        n = f"🎮{Players}/{maxPlayers}| {time}⏰"
        await bot.change_presence(activity=nextcord .Game(name=n))
        await asyncio.sleep(60)
    except:
        #await ctx.reply("Сервер offline")
        #print("Сервер offline")
        await bot.change_presence(activity=nextcord .Game(name="Сервер offlin 🔴"))
bot.run(Token)