import discord
from discord.ext import commands,tasks
import youtube_dl

from random import choice

client = commands.Bot(command_prefix='!')

status = ['Vibing to music','Looking for some new Heat','AFK']

@client.event
async def on_ready():
	change_status.start()
	print('Simon is online')

@tasks.loop(seconds=180)
async def change_status():
	await client.change_presence(activity=discord.Game(choice(status)))	

client.run('ODEzMTgxMTg4OTU3MDEyMDE4.YDLj_w.o9GJQG75-P9lV5vs-23AhkedAOU')