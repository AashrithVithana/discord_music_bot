import discord
from dotenv import load_dotenv
from googleapiclient.discovery import build
from discord.ext import commands
import discord
import requests
import yt_dlp
import os


load_dotenv()
api_key = os.getenv("API_KEY1")
youtube = build("youtube", "v3", developerKey=api_key)




load_dotenv()
api_key = os.getenv("API_KEY")

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True


bot = commands.Bot(command_prefix="$", intents=intents)

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = response.json()
    return json_data['url']


def get_video(query: str):
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=5
    )
    response = request.execute()
    for item in response["items"]:
        video_id = item["id"]["videoId"]
        return f"https://youtube.com/watch?v={video_id}"

def get_audio_url(youtube_url: str):
    ydl_opts = {"format": "bestaudio[ext=m4a]/bestaudio/best", "noplaylist": "True"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        return info['url']



@bot.event
async def on_ready():
        print('Logged on as {0}!'.format(bot.user))

@bot.event
async def on_message(message):
        if message.author == bot.user:
            return 
        if message.content.startswith('$hello'):
            await message.channel.send('Heyyy!')
        if message.content.startswith('%meme'):
            await message.channel.send(get_meme())
        if message.content.startswith('pencil'):
            await message.channel.send('nee pelli cancel 🤭')
        if message.content.startswith('six'):
            await message.channel.send('nee pelli fix 😏')

        if message.content.startswith('$join'):
            if message.author.voice:
                channel = message.author.voice.channel
                await channel.connect()
                await message.channel.send("Joined Voice Channel!")
        if message.content.startswith('bye') or message.content.startswith('Bye') :
            await message.channel.send(f"Bye {message.author}!")

        if message.content.startswith('$leave'):
            voice_client = message.guild.voice_client
            if voice_client:
                await voice_client.disconnect()
                await message.channel.send("disconnected")
            else:
                 await message.channel.send("Not connected to the voice channel.")
        await bot.process_commands(message)        

@bot.command()
async def play(ctx, *arr):
    result = " ".join(arr)
    if not ctx.author.voice:
        await ctx.send("You are not in the VC.")
        return
    channel = ctx.author.voice.channel
    vc = ctx.guild.voice_client
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    if not vc:
        vc = await channel.connect()
    url = get_video(result)
    audio_url = get_audio_url(url)
    if vc.is_playing():
        vc.stop()
    vc.play(discord.FFmpegPCMAudio(audio_url, **FFMPEG_OPTIONS))
    await ctx.send(f"Now playing {result}")


bot.run(api_key)