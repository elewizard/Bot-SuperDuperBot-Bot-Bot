mport discord
from discord.voice_client import VoiceClient
from discord.ext import commands

startup_extensions = ["Music"]
bot = commands.Bot("")

@bot.event
async def on_ready():
    print("Bot Online")

class Main_Commands():
    def __init__(self, bot):
        self.bot = bot


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '(): ()'.format(type(e).__name__, e)
            print('Failed to load extension()\n()'.format(extension, exc))


bot.run('NDUzNTIyNzU5NzQ2NzE1NjQ4.DfhDNA.AJP3OJcYGJRLo8D9VU5xIvkdu3w')
