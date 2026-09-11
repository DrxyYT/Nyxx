import discord
from discord.ext import commands

from .Fun import Fun
from .Homebrews import Homebrews
from .Pretendo import Pretendo


class Community(Fun, Homebrews, Pretendo):
    """Community, homebrew, and Pretendo features."""

    def __init__(self, bot):
        Fun.__init__(self, bot)
        Homebrews.__init__(self, bot)
        Pretendo.__init__(self, bot)


def setup(bot):
    bot.add_cog(Community(bot))