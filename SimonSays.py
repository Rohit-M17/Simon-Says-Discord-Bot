import discord
import asyncio
from discord.ext import commands,tasks
from discord.voice_client import VoiceClient
import youtube_dl

from random import choice

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

#Standard format given by ytdl app and ffmpeg



ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=1.0):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')


    @classmethod

    async def from_url(cls, url, *, loop=None, stream=False):
        
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


bot = commands.Bot(command_prefix='!')


mood = ['Vibing to music','Looking for some new Heat','AFK','In the Stu']

Queue = []
Rqueue = []
   
      
@bot.event
async def on_ready():
	change_mood.start()
	print('Simon is online')

@bot.command(name='join', help='Joins the user voice channel')
async def join(ctx):
	if not ctx.message.author.voice:
		await ctx.send("You are not in a Voice Channel")
		return
    
	else:
		voice_channel = ctx.message.author.voice.channel

	await voice_channel.connect()

@bot.command(name='play', help='Plays a song immediately')
async def play(ctx,url):
	server = ctx.message.guild
	voice_channel = server.voice_client   
	Queue.append(url)
	voice_channel.stop()
	async with ctx.typing():
		player = await YTDLSource.from_url(url,  loop = bot.loop)
		Rqueue.append(player.title)
	await ctx.send("**Added:** " + player.title + "** to the Queue**")
	while True:
		await asyncio.sleep(1)
		if voice_channel.is_playing() == False:
			
			voice_channel.play(player, after=lambda e: Rqueue.pop(0))
    		
	

@bot.command(name='enqueue', help='Adds a song to the queue')
async def enqueue(ctx,url):
	server = ctx.message.guild
	voice_channel = server.voice_client   
	Queue.append(url)
	async with ctx.typing():
		player = await YTDLSource.from_url(url,  loop = bot.loop)
		Rqueue.append(player.title)
	await ctx.send("**Added:** " + player.title + "** to the Queue**")
	while True:
		await asyncio.sleep(5)
		if voice_channel.is_playing() == False:
			voice_channel.play(player, after=lambda e: Rqueue.pop(0))
			
	
	

@bot.command(name='queue', help='Shows all songs in the queue')
async def queue(ctx):
	if Rqueue == []:
		await ctx.send('**Nothing is in the Queue**')
	else:
		await ctx.send(f'Queue:\n')
		for number, letter in enumerate(Rqueue):	
			await ctx.send(f'`{number+1}.{letter}`')    

@bot.command(name='np', help='Shows the current song')
async def np(ctx):
	server = ctx.message.guild
	voice_channel = server.voice_client 
	if voice_channel.is_playing() == False:
		await ctx.send('**Nothing is Playing**')
	else:
		await ctx.send(Rqueue[0] + " **is now playing**"	)




@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
	server = ctx.message.guild
    
	voice_channel = server.voice_client

	voice_channel.pause()
@bot.command(name='resume', help='This command resumes the song')
async def resume(ctx):
	server = ctx.message.guild
    
	voice_channel = server.voice_client

	voice_channel.resume()
@bot.command(name='skip', help='This command skips the song')
async def skip(ctx):
	server = ctx.message.guild
    
	voice_channel = server.voice_client

	voice_channel.stop()

@bot.command(name='disconnect', help='This command makes the bot leave the voice channel')
async def disconnect(ctx):
	voice_channel = ctx.message.guild.voice_client
	await voice_channel.disconnect()

@tasks.loop(seconds=180)
async def change_mood():
	await bot.change_presence(activity=discord.Game(choice(mood)))	
@tasks.loop(seconds=180)
async def change_mood():
	await bot.change_presence(activity=discord.Game(choice(mood)))	

bot.run('token')














