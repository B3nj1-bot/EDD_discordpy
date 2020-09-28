from discord.ext.commands import Bot
import asyncio
import discord

PREFIX = '& '
token='' #Put your bot token in the string '', (located at https://discord.com/developers/applications in the bot tab of your application)
client = Bot(command_prefix=PREFIX)

@client.command (name='hi')
async def hi(ctx):
    await ctx.channel.send('hello!')

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if msg.content == '& greeting':
        await msg.channel.send('How are you today? :)')
    #Put your commands here
    await client.process_commands(msg)

@client.event
async def on_ready():
    print('Succesfully logged in as:')
    print(client.user.name)
    print('~~~~~~~~')
client.run(token)
