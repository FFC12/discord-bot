import discord
from discord import Intents, Embed, Colour
from discord.ext import commands
from discord.ext.commands.bot import Bot


class DiscordBot:
    # Intents
    intents = discord.Intents.default()
    intents.message_content = True

    # Discord client instance with intents
    client = discord.Client(intents=intents)

    bot = commands.Bot(command_prefix='/', intents=intents)

    def __init__(self, token):
        self.token = token

    @staticmethod
    @client.event
    async def on_ready():
        print(f'{DiscordBot.client.user} has connected to Discord!')

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
