import os

import discord
from discord import Intents, Embed, Colour
from discord.ext import commands
from discord.ext.commands.bot import Bot


class DiscordBot:
    # Intents
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='/', intents=intents)

    def __init__(self, token):
        self.token = token

    def run(self):
        """
        Run bot
        :return:
        """
        DiscordBot.bot.run(self.token)

    async def register_cog(self, cog):
        """
        Register cog to bot
        :param cog:
        :return:
        """
        await DiscordBot.bot.add_cog(cog)


@DiscordBot.bot.event
async def on_ready():
    print(f'{DiscordBot.bot.user} has connected to Discord!')


@DiscordBot.bot.event
async def on_disconnect():
    print(f'{DiscordBot.bot.user} has disconnected to Discord!')
