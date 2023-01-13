import discord 
from discord.ext import commands
from youtube_dl import YoutubeDL
YDL_OPTIONS={'format':'worstaudio/best', 'noplaylist':'False','simylate':'True', 'key':'FFmpegExtractAudio'}
FFMPEG_OPTIONS={'before_options':'-reconect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}
bot = commands.Bot(command_prefix='*')



@bot.event
async def on_ready(self):
    print('logged on as {0}!'.format(self.user))
async def on_message(self, message):
    print('Message from {0.author}: {0.contont}'.format(message))
@bot.command()
async def play(ctx, url):
    vc = await ctx.message.authot.voice.channel.connect()
    with YoutubeDL(YDL_OPTINIONS) as ydl:
        if 'https://' in url:
            info - ydl.extract_info(url,download=False)
        else:
            info= ydl.extract_info(f'ytsearch: {url}',download=False)['entries'][0]
    link = info['formats'][0][url]
    vc.play(discord.FFmpegPCMAudio(executable='ffmpeg//ffmpeg.exe', source=link,**FFMPEG_OPTIONS))
bot.run('MTA2MzMyOTY4ODg1ODEzMjUyMA.G4O8AW.EezTpG20uh5wZXGouimMTFggetp5ZKrts-JAzk')