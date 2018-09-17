import discord
import youtube_dl
from discord.ext import commands

client = commands.Bot(command_prefix = "e!")

players = {}

@client.event
async def on_ready():
    print("Bot çevrimiçi!")

@client.command(pass_context = True)
async def baglan(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context = True)
async def oynat(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start() 



client.run(os.environ.get('token'))