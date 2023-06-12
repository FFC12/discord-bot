import discord
import os
from traceback import print_exc
from discord.ext import commands
from youtubesearchpython import VideosSearch
import bardapi
import random

import re

from loguru import logger

BARD_TOKEN = os.getenv('BARD_TOKEN')


class Chatbot(commands.Cog):
    """
    Music cog for discord bot
    """

    def __init__(self, bot):
        self.bot = bot
        self.bard = bardapi.core.Bard(BARD_TOKEN)

    @commands.command('chat', help='Write something to chatbot and it will answer you')
    async def chat(self, ctx, *, message):
        """
        Play command for play music randomly
        :param ctx:
        :param message:
        :return:
        """
        try:
            # get response from bard api
            response = self.bard.get_answer(message)

            # get text from response
            text = response['content']

            logger.debug(text)

            await ctx.send(f'👾 Bot:')

            if len(text) > 2000:
                # split text by 2000 characters
                texts = [text[i:i+2000] for i in range(0, len(text), 2000)]

                logger.debug(texts)

                # send message
                for text in texts:
                    await ctx.send(text)
            else:
                await ctx.send(text)

        except Exception as e:
            logger.error(e)
            print_exc()
            await ctx.send(f'Sorry, there\'s something wrong with me. Please, try again later 🤧')
