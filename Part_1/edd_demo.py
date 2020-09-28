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
async def on_message(ctx):
    if ctx.author == client.user:
        return
    if ctx.content == '& greeting':
        await ctx.channel.send('How are you today? :)')
    #Put your commands here
    await client.process_commands(ctx)

@client.event
async def on_ready():
    print('Succesfully logged in as:')
    print(client.user.name)
    print('~~~~~~~~')
client.run(token)
