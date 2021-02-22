import discord
from discord.ext import commands,tasks
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

#class that sources youtube and souncloud links through youtube downloader and fffmpeg

client = commands.Bot(command_prefix='!')

status = ['Vibing to music','Looking for some new Heat','AFK']

queue = []


@client.event
async def on_ready():
	change_status.start()
	print('Simon is online')

@tasks.loop(seconds=180)
async def change_status():
	await client.change_presence(activity=discord.Game(choice(status)))	

client.run('ODEzMTgxMTg4OTU3MDEyMDE4.YDLj_w.o9GJQG75-P9lV5vs-23AhkedAOU')
