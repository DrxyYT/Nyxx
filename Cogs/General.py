import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Simple ping command
    @discord.slash_command(name="ping", description="Sends the bot's latency.")
    async def ping(self, ctx):
        await ctx.respond(f"Pong! Latency is {self.bot.latency * 1000:.2f}ms")

    # Help command
    @discord.slash_command(name="commands", description="List of available commands.")
    async def commands(self, ctx):
        help_message = """
    # List of Commands:
    /ping - Check bot latency
    
    /userinfo - Get information about a user
    
    /serverinfo - Get server information
    """
        await ctx.respond(help_message)

    # User info command
    @discord.slash_command(name="userinfo", description="Gives information about a user.")
    async def userinfo(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        
        # Format the dates for readability
        joined_at = member.joined_at.strftime('%Y-%m-%d %H:%M:%S UTC') if member.joined_at else "Unknown"
        created_at = member.created_at.strftime('%Y-%m-%d %H:%M:%S UTC')
        
        embed = discord.Embed(
            title=f"{member.name}'s Info",
            description=f"Here is some information about {member.mention}.",
            color=discord.Color.blue()
        )
        
        # Add user's profile picture
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        
        # Add fields for user information
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Nickname", value=member.nick if member.nick else "No nickname", inline=True)
        embed.add_field(name="Joined Server", value=joined_at, inline=True)
        embed.add_field(name="Account Created", value=created_at, inline=True)
        embed.add_field(name="Highest Role", value=member.top_role.mention, inline=True)
        
        # Send the embed
        await ctx.respond(embed=embed)

    # Server info command
    @discord.slash_command(name="serverinfo", description="Gives information about the server.")
    async def serverinfo(self, ctx):
        guild = ctx.guild
        
        # Format the date for readability
        created_at = guild.created_at.strftime('%Y-%m-%d %H:%M:%S UTC')
        
        embed = discord.Embed(
            title=f"{guild.name}'s Info",
            description=f"Here is some information about the server **{guild.name}**.",
            color=discord.Color.green()
        )
        
        # Add server icon to the embed
        embed.set_thumbnail(url=guild.icon.url if guild.icon else "No server icon")

        # Add fields for server information
        embed.add_field(name="ID", value=guild.id, inline=True)
        embed.add_field(name="Members", value=guild.member_count, inline=True)
        embed.add_field(name="Created At", value=created_at, inline=True)
        
        # Send the embed
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(General(bot))
