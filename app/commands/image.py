import random
from io import BytesIO

from PIL import Image

import discord
import os
from traceback import print_exc
from discord.ext import commands

from loguru import logger


class ImageGenerator(commands.Cog):
    """
    Music cog for discord bot
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command('image', help='Generate random image (work in progress)')
    async def generate(self, ctx, *, size):
        """
        Generate command for generate random image
        :param ctx:
        :param size:
        :return:
        """
        try:
            size = int(size)
            if size > 2048:
                await ctx.send('Sorry, maximum size is 2048')

            # get image
            image = self.generate_random_image((size, size) if size else (128, 128))

            # image to bytes
            image_bytes = BytesIO()
            image.save(image_bytes, format='PNG')
            image_bytes.seek(0)

            # send image
            await ctx.send(file=discord.File(image_bytes, filename='image.png'))

        except Exception as e:
            logger.error(e)
            print_exc()
            await ctx.send(f'Sorry, there\'s something wrong with me. Please, try again later 🤧')

    def generate_random_image(self, size):
        """
        Generate random image
        :param size:
        :return:
        """
        # generate random image
        image = Image.new('RGB', size)

        # fill random color
        image.putdata([tuple([int(random.random() * 255) for _ in range(3)]) for _ in range(size[0] * size[1])])

        return image
