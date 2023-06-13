import discord
from discord import Intents, Embed, Colour
from discord.ext import commands
from discord.ext.commands import Bot, Command


class Greetings(commands.Cog):
    """
    Greetings cog for discord bot
    """

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """
        Greetings when member join
        :param member:
        :return:
        """
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'Welcome {member.mention}.')

    @commands.command('hello', help='Say hello to bot')
    async def hello(self, ctx, *, member: discord.Member = None):
        """
        Hello command for greetings who join
        :param ctx:
        :param member:
        :return:
        """
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Hello {member.name}~')
        else:
            await ctx.send(f'Hello {member.name}... This feels familiar.')
        self._last_member = member


class UserManage(commands.Cog):
    """
    User manage cog for discord bot
    """

    def __init__(self, bot):
        self.bot = bot

    # Echo my message
    @commands.command('echo', help='Echo message')
    async def echo(self, ctx, *, message):
        """
        Echo command for echo message
        :param ctx:
        :param message:
        :return:
        """
        await ctx.send(message)

    @commands.command('kick', help='Kick member from server')
    @commands.has_role('moderation')
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """
        Kick command for kick member
        :param ctx:
        :param member:
        :param reason:
        :return:
        """
        await member.kick(reason=reason)
        await ctx.send(f'{member} has kicked. Reason: {reason}')

    @commands.command('ban', help='Ban member from server')
    @commands.has_role('moderation')
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """
        Ban command for ban member
        :param ctx:
        :param member:
        :param reason:
        :return:
        """
        await member.ban(reason=reason)
        await ctx.send(f'{member} has banned. Reason: {reason}')

    @commands.command('unban', help='Unban member from server')
    @commands.has_role('moderation')
    async def unban(self, ctx, *, member):
        """
        Unban command for unban member
        :param ctx:
        :param member:
        :return:
        """
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} has unbanned.')
                return

    @commands.command('clear', help='Clear message')
    @commands.has_role('moderation')
    async def clear(self, ctx, amount=5):
        """
        Clear command for clear message
        :param ctx:
        :param amount:
        :return:
        """
        if amount > 10:
            await ctx.send('You can only delete 10 messages at a time.')
        else:
            await ctx.channel.purge(limit=amount + 1)

    @commands.command('ask', help='Ask question')
    @commands.has_role('moderation')
    async def ask(self, ctx, *, question):
        """
        Ask command for ask question
        :param ctx:
        :param question:
        :return:
        """
        await ctx.send(f'{ctx.author} asked: {question}')

    @commands.command('everyone', help='Mention everyone 3 times')
    @commands.has_role('moderation')
    async def everyone(self, ctx):
        """
        Everyone command for mention everyone 3 times
        :param ctx:
        :return:
        """
        for i in range(3):
            await ctx.send('@everyone This is a announcement! Please read it.')
