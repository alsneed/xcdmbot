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

bot.load_extension('commands.yt')

bot.run(keys['discord'])