from discord.ext import commands

from .ReactionRoles import ReactionRoles
from .RoleManagement import RoleManagement
from .ServerManagement import ServerManagement


class Server(RoleManagement, ServerManagement, ReactionRoles):
    """Server administration, role management, and reaction roles."""

    def __init__(self, bot):
        RoleManagement.__init__(self, bot)
        ServerManagement.__init__(self, bot)
        ReactionRoles.__init__(self, bot)


def setup(bot):
    bot.add_cog(Server(bot))