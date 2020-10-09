from discord.ext.commands import Bot
import asyncio
import discord
import datetime
import sys
PREFIX = '& '
token='' #Put your bot token in the string '', (located at https://discord.com/developers/applications in the bot tab of your application)
client = Bot(command_prefix=PREFIX)

@client.command(name='greeting')
async def greeting(ctx):
    def pred(m):
        return m.author == ctx.author and m.channel == ctx.channel
    await ctx.send('hello!')
    await ctx.send('What time of day is it!')
    try:
        msg = await client.wait_for('message',check=pred,timeout=10)
    except asyncio.TimeoutError:
        await ctx.send('You did not respond in time. Goodbye.')
    else:
        if msg.content == 'morning':
            await ctx.send('Bright and early! Good morning! :sunny:')
        elif msg.content == 'afternoon':
            await ctx.send('How was lunch? Good afternoon!')
        elif msg.content == 'evening':
            await ctx.send('Getting kind of dark...Good evening!')
        else:
            await ctx.send('I\'m not sure what time it is, so I\'ll just say hi.')

@client.command(name='shutdown')
async def kill(ctx):
    await ctx.send('shutting down...')
    sys.exit()

@client.event
async def on_message(ctx):
    if ctx.author == client.user:
        return
    # if ctx.content == '& greeting':
    #     await ctx.send('How are you today? :)')
    #Put your commands here
    await client.process_commands(ctx)

@client.event
async def on_ready():
    print('Succesfully logged in as:')
    print(client.user.name)
    print('~~~~~~~~')
client.run(token)
