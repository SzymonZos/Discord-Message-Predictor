import os
import sys
import random

import discord
from dotenv import load_dotenv
from discord.ext.commands import Bot

from utils import dump_msgs

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = Bot(command_prefix='!')


@bot.event
async def on_ready():
    guild = bot.get_guild(int(GUILD))
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@bot.command(name='advice', help='Responds with a random great advice')
async def advice(ctx):
    advices = [
        'Uderz pięścią w stół!',
        'Pamiętaj, nie warto!',
        'Wyjdź do ludzi, pobiegaj!',
    ]
    response = random.choice(advices)
    await ctx.send(response)


@bot.event
async def on_error(event, *args, **kwargs):
    with open('logs/err.log', 'a') as f:
        f.write(f'{event} Unhandled message: {args[0]} {sys.exc_info()}\n')
        raise


@bot.command(name='history', help='Responds with a message containing history of user')
async def history(ctx, member: discord.Member):
    logs = []
    for channel in ctx.guild.text_channels:
        try:
            async for message in channel.history(limit=None):
                if message.author == member:
                    logs.append(message.content)
        except discord.errors.Forbidden:
            pass
    await dump_msgs(member, logs)
    await ctx.send(f'{member.mention} has sent **{len(logs)}** messages in this server.')


bot.run(TOKEN)
