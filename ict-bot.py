import discord
import os

disClient = discord.Client()

@disClient.event
async def on_message(message):
    return


@disClient.event
async def on_ready():
    await disClient.change_presence(game=discord.Game(name='https://ict.gg'))
    print('Logged in as')
    print(disClient.user.name)
    print(disClient.user.id)
    print('------')


disClient.run(os.environ['DISCORD_TOKEN'])
