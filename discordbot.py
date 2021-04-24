import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '!') # put your own prefix in the '' for example: !, ?, *.
token = '' # to get your token, in the discord application page there should be a copy token button, click it and paste it into the ''.

@client.event
async def on_ready():
    print(f'we have logged in as {client.user.name}')
    
@client.command()
async def test(ctx): # you can replace test with whatever you like
    await ctx.send('placeholder') # replace placeholder with whatever you like
# when using this command make sure to put your prefix before you use it for an example if my prefix was ! i would do !test and the bot would respond
client.run(token)
