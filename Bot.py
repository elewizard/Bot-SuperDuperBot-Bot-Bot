import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("")
TOKEN = "NDUzNTIyNzU5NzQ2NzE1NjQ4.DfhDNA.AJP3OJcYGJRLo8D9VU5xIvkdu3w"

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='Shit',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['shit', 'Fuck', 'fuck'],
                pass_context=True)
async def eight_ball(context):
    await client.say(context.message.author.mention + ", " + "Chill :smirk:")
        
client.run(TOKEN)
