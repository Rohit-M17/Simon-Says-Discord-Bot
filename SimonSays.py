




import discord
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
    def __init__(self, source, *, data, volume=0.5):
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



@bot.event
async def on_ready():
	change_mood.start()
	print('Simon is online')

@bot.command()
async def join(ctx):
   
    channel = ctx.author.voice.channel
    await channel.connect()


@bot.command(name='play', help='Plays songs directly from Youtube and Soundcloud')
async def play(ctx, url):
    if ctx.message.author.voice:
    	await ctx.send('You must connect to a voice channel to connect')
    else:
    global queue

    queue.append(url)

    channel = ctx.author.voice.channel
    await channel.connect()

    server = ctx.message.guild
    voice_channel = server.voice_client
    
    async with ctx.typing():

        player = await YTDLSource.from_url(url, loop=bot.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('**Playing:** {}'.format(player.title))
    

@bot.command(name='queue', help='Adds a song to the queue')
async def queue_(ctx):
    await ctx.send(f'Queue: `{queue}`')

@bot.command(name='skip', help='This command skips the song')
async def skip(ctx):
    server = ctx.message.guild
    
    voice_channel = server.voice_client

    voice_channel.stop()

@bot.command(name='pause', help='This command pauses the given song')
async def pause(ctx):
	server = ctx.message.guild
    
    voice_channel = server.voice_client

    voice_channel.pause()

@bot.command(name='resume', help='This command resumes a paused song')
async def resume(ctx):
	server = ctx.message.guild
    
    voice_channel = server.voice_client

    voice_channel.resume()


@tasks.loop(seconds=180)
async def change_mood():
	await bot.change_presence(activity=discord.Game(choice(mood)))	

bot.run('ODEzMTgxMTg4OTU3MDEyMDE4.YDLj_w.o9GJQG75-P9lV5vs-23AhkedAOU')














