import discord
import os
from traceback import print_exc
from discord import Intents, Embed, Colour
from discord.ext import commands
from discord.ext.commands import Bot, Command
from youtubesearchpython import VideosSearch
import bardapi
import random

import re

from loguru import logger

BARD_TOKEN = os.getenv('BARD_TOKEN')


class Music(commands.Cog):
    """
    Music cog for discord bot
    """

    def __init__(self, bot):
        self.bot = bot
        self.bard = bardapi.core.Bard(BARD_TOKEN)

    @commands.command('play', help='Play random music. Just give me a keyword which describe your mood (ex: sad, '
                                   'happy, etc.)')
    async def play(self, ctx, *, message):
        """
        Play command for play music randomly
        :param ctx:
        :param message:
        :return:
        """
        mood = message

        try:
            # get response from bard api
            response = self.bard.get_answer('Can you give me a at least 3 youtube search music text for this mood: ' + mood + '?'
                                            ' Please, don\'t add any keywords except text you will send me'
                                            '. No need explanation. Texts must be inside of double quotes')

            # get text from response
            text = response['content']

            logger.debug(text)

            # extract text inside of double quotes by regex
            texts = re.findall(r'"([^"]*)"', text)

            # random 3 of them
            texts = random.sample(texts, 3 if len(texts) > 3 else len(texts))

            logger.debug(texts)

            urls = []
            for text in texts:
                # search video
                videos_search = VideosSearch(text, limit=10)

                # get result
                result = videos_search.result()

                # select random video from result
                video = random.choice(result['result'])

                # get video url
                url = video['link']

                # append to urls
                urls.append(url)

            # send message
            await ctx.send(f'🎶 I found this videos for you 🎶 : ')
            for url in urls:
                await ctx.send(url)
        except Exception as e:
            logger.error(e)
            print_exc()
            await ctx.send(f'Sorry, I can\'t find any video for this mood 🤧 : {mood}')

    @commands.command('video', help='Play random video. Just give me a keyword or sentence (ex: how to make '
                                    'a sandwich etc.)')
    async def play_video(self, ctx, *, message):
        """
        Play command for play music randomly
        :param ctx:
        :param message:
        :return:
        """
        mood = message

        try:
            # get response from bard api
            response = self.bard.get_answer('Can you give me a at least 3 youtube search video text for this sentences:' 
                                            ' ' + mood + '? Don\'t add any keywords except text you will send me'
                                            '. No need explanation. Texts must be inside of double quotes')

            # get text from response
            text = response['content']

            logger.debug(text)

            # extract text inside of double quotes by regex
            texts = re.findall(r'"([^"]*)"', text)

            # random 3 of them
            texts = random.sample(texts, 3 if len(texts) > 3 else len(texts))

            logger.debug(texts)

            urls = []
            for text in texts:
                # search video
                videos_search = VideosSearch(text, limit=10)

                # get result
                result = videos_search.result()

                # select random video from result
                video = random.choice(result['result'])

                # get video url
                url = video['link']

                # append to urls
                urls.append(url)

            # send message
            await ctx.send(f'🎶 I found this videos for you 🎶 : ')
            for url in urls:
                await ctx.send(url)
        except Exception as e:
            logger.error(e)
            print_exc()
            await ctx.send(f'Sorry, I can\'t find any video for this mood 🤧 : {mood}')


