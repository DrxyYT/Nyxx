import discord
from discord.ext import commands
from discord import Embed
from datetime import datetime

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Events
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Hello there **{member.mention}**! Welcome to the server! Please read #rules and check #github for updates! Enjoy your stay! <3'
        )
        
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        log_channel = self.bot.get_channel(1217102409482899517)
        embed = discord.Embed(title="Member Left", description=f"{member.name} has left the server.", color=discord.Color.red())
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Created at", value=member.created_at, inline=True)
        await log_channel.send(embed=embed)

    # Listen for message deletions
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        # Check if the message is from the specific server (replace with server ID)
        specific_guild_id = 1279209602373910638  # Replace with specific server's ID
        
        if message.guild and message.guild.id == specific_guild_id:
            log_channel = self.bot.get_channel(1286734858395320445)  # Replace with log channel ID
            
            # Create an embed for the deleted message
            embed = discord.Embed(
                title="Message Deleted",
                description=f"A message from **{message.author.name}** was deleted.",
                color=discord.Color.orange()
            )

    # Slash commands for moderation
    @discord.slash_command(name="kick", description="Kick a user from the server")
    async def kick(self, ctx, member: discord.Member, reason: str = "No reason provided"):
        if ctx.author.guild_permissions.kick_members:
            await member.kick(reason=reason)
            embed = Embed(title="User Kicked", description=f"{member.mention} has been kicked.", color=discord.Color.red())
            embed.add_field(name="Reason", value=reason, inline=False)
            # Adding the date and time to the footer
            embed.set_footer(text=f"Kicked by {ctx.author.name} | {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}")
            embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
            await ctx.respond(embed=embed)
        else:
            embed = Embed(title="Permission Denied", description="You don't have permission to kick members.", color=discord.Color.orange())
            await ctx.respond(embed=embed, ephemeral=True)

    @discord.slash_command(name="ban", description="Ban a user from the server")
    async def ban(self, ctx, member: discord.Member, reason: str = "No reason provided"):
        if ctx.author.guild_permissions.ban_members:
            await member.ban(reason=reason)
            embed = Embed(title="User Banned", description=f"{member.mention} has been banned.", color=discord.Color.red())
            embed.add_field(name="Reason", value=reason, inline=False)
            # Adding the date and time to the footer
            embed.set_footer(text=f"Banned by {ctx.author.name} | {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}")
            embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
            await ctx.respond(embed=embed)
        else:
            embed = Embed(title="Permission Denied", description="You don't have permission to ban members.", color=discord.Color.orange())
            await ctx.respond(embed=embed, ephemeral=True)

    @discord.slash_command(name="mute", description="Mute a user from the server")
    async def mute(self, ctx, member: discord.Member, reason: str = "No reason provided"):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        await member.edit(mute=True, reason=reason)
        await member.send(f"You have been muted in the server. Reason: **{reason}**")
        await ctx.respond(f"{member.mention} has been muted. Reason: **{reason}**")
        
    @discord.slash_command(name="unmute", description="Unmute a user from the server")
    async def unmute(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not role:
            return await ctx.respond("The Muted role does not exist.", ephemeral=True)
        await member.remove_roles(role)
        await ctx.respond(f"{member.mention} has been unmuted.")
        
@discord.slash_command(name="mod", description="List of moderation commands")
async def mod(ctx):
    if any(role.name in ["Admins", "Moderators", "Owner", "Staff", "Head Admin", "Head Moderator", "Trainee Moderators"] for role in ctx.author.roles):
        help_message = """
        # Moderation Commands:
        /kick - Kick a user from the server

        /ban - Ban a user from the server

        /mute - Mute a user from the server

        /unmute - Unmute a user from the server

        """
        await ctx.respond(content=help_message)
    else:
        await ctx.respond("Sorry, you do not have permission to use this command.")

def setup(bot):
    bot.add_cog(Moderation(bot))
