import discord
from discord.ext import commands
import os    
import random
import asyncio

token=''
boomerbot = commands.Bot(command_prefix = commands.when_mentioned)

@boomerbotbot.event
async def on_message(message):
    if message.author.id == int(''): #insert the id of your target user here
        randimg = random.choice(os.listdir("./Memes/")) #create a 'Memes' folder and populate with random images
        path = "./Memes/" + randimg
        await message.channel.send(file=discord.File(path))
        await message.channel.send('OK BOOMER')
boomerbot.run(token)
