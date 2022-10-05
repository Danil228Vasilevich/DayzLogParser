import nextcord
import os 
from config import settings
from nextcord.ext import commands
import asyncio
thumbnail = settings['thumbnail']
bot = commands.Bot()


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

#@bot.slash_command(description="My first slash command")
#async def pi(interaction: nextcord.Interaction):
    #await interaction.send("Hello!")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        #print("тип загрузил")

bot.run(settings['token'])