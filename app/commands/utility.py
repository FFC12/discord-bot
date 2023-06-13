import os

import discord
from discord.ext import commands


class Utility(commands.Cog):
    """
    Utility cog for discord bot
    """
    TODO_LIST = []

    def __init__(self, bot):
        self.bot = bot

    @commands.command('todo', help='Add TODO list')
    @commands.has_role('moderation')
    async def todo(self, ctx, *, message):
        """
        Add TODO list
        :param ctx:
        :param message:
        :return:
        """
        Utility.TODO_LIST.append(message)

        await ctx.send(f'Added "{message}" to TODO list')

    @commands.command('todolist', help='Show TODO list')
    async def todolist(self, ctx):
        """
        Show TODO list
        :param ctx::
        :return:
        """
        await ctx.send(f'TODO list:\n')
        for todo in Utility.TODO_LIST:
            await ctx.send(f'🔲 {todo}')

    @commands.command('remove', help='Remove TODO list')
    @commands.has_role('moderation')
    async def remove(self, ctx, *, index):
        """
        Remove TODO list
        :param ctx:
        :param index:
        :return:
        """
        try:
            index = int(index)
            if index < 0 or index >= len(Utility.TODO_LIST):
                raise ValueError

            Utility.TODO_LIST.pop(index)

            await ctx.send(f'Removed TODO list at index {index}')
        except ValueError:
            await ctx.send(f'Invalid index')


