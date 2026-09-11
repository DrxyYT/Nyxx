import discord
from discord.ext import commands

from .AutoFeatures import AutoFeatures
from .General import General


class Information(General, AutoFeatures):
    """General information commands and automatic member features."""

    def __init__(self, bot):
        General.__init__(self, bot)
        AutoFeatures.__init__(self, bot)


def setup(bot):
    bot.add_cog(Information(bot))