import discord
import commands as command_list
from discord.ext import commands
from keys import keys

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('I live. Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    
@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    
    #banepost
    str_list = msg.lower().split(' ')
    for idx, string in enumerate(str_list, start = 1):
        if string == 'big' and idx != len(str_list):
           await msg.channel.send('For you')
           break

bot.load_extension('commands.yt')

bot.run(keys['discord'])
