import os

from app.bot import DiscordBot
from app.commands.manage import Greetings, UserManage
from app.commands.music import Music
from app.commands.chatbot import Chatbot
from app.commands.image import ImageGenerator

import asyncio

TOKEN = os.getenv('DISCORD_TOKEN')


async def init():
    # Create bot instance
    bot = DiscordBot(token=TOKEN)

    # Register cogs
    await bot.register_cog(Greetings(bot))
    await bot.register_cog(UserManage(bot))
    await bot.register_cog(Music(bot))
    await bot.register_cog(Chatbot(bot))
    await bot.register_cog(ImageGenerator(bot))

    return bot

if __name__ == '__main__':
    # Get event loop
    loop = asyncio.get_event_loop()

    # Init bot
    bot = loop.run_until_complete(init())

    # Run bot
    bot.run()
