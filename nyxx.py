import discord

intents = discord.Intents.default()
intents.members = True

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'Nyxx is online and ready to go!')
    await bot.change_presence(activity=discord.Game(name="Now Online 24/7 thanks to Dires!!"), status=discord.Status.online)

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello there **{member.name}**! Welcome to the Nyxx server! Please read #rules and check #github for updates! Enjoy your stay! <3'
    )

# Commands
@bot.command(description="Sends the bot's latency.") 
async def ping(ctx):
    await ctx.respond(f"Pong! Latency is {bot.latency}")

@bot.command(description="List of commands")
async def help(ctx):
    help_message = """
    **Command Categories:**
    /ping

    /drxy
    
    /nyxx

    /socialbears

    /yuki

    /kys

    /drxyyt

    /userinfo

    /serverinfo
    
    Feel free to contact the bot owner for additional assistance.
    """

    await ctx.respond(content=help_message)

@bot.command(description="Kick a user from the server")
async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
    if ctx.author.guild_permissions.kick_members:
        await member.kick(reason=reason)
        await ctx.respond(f"{member.mention} has been kicked. Reason: **{reason}**")
    else:
        await ctx.respond("You don't have the necessary permissions to kick members.")

@bot.command(description="Ban a user from the server")
async def ban(ctx, member: discord.Member, *, reason="No reason provided"):
    if ctx.author.guild_permissions.ban_members:
        await member.ban(reason=reason)
        await ctx.respond(f"{member.mention} has been banned. Reason: **{reason}**")
    else:
        await ctx.respond("You don't have the necessary permissions to ban members.")

@bot.command(description= "Mute a user from the server")
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not role:
        try:
            role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(role, speak=False, send_messages=False)
        except discord.Forbidden:
            return await ctx.respond("I don't have permissions to do that.")
    await member.add_roles(role)
    await ctx.respond(f"{member.mention} has been muted.")

@bot.command(description= "Unmute a user from the server")
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not role:
        return await ctx.respond("The Muted role does not exist.")
    await member.remove_roles(role)
    await ctx.respond(f"{member.mention} has been unmuted.")

@bot.command(description="Info about Drxy! My creator!") 
async def drxy(ctx):
    await ctx.respond(f"Drxy is a 15 yr old boy from the U.S and he helped create me! He is a beginner programmer and he is learning Python! More info: https://github.com/DrxyYT/DrxyYT")

@bot.command(description="Info about Nyxx! Myself!")
async def nyxx(ctx):
    await ctx.respond(f"Hello! Im Nyxx! I was created to help you with 3DS homebrew and for fun! My creator is Drxy and he is learning to program me! I hope we can get along!")

@bot.command(description="Social bears discord server!")
async def socialbears(ctx):
    await ctx.respond("Support the Owner Ashy!! <3 https://discord.gg/socialbears")

@bot.command(description="Invite for the Drxys 3DS hacking discord server")
async def drxy3ds(ctx):
    await ctx.respond("https://discord.gg/Vr887CyF9t")

@bot.command(description="Gives the invite for Yukis server")
async def yuki(ctx):
    await ctx.respond("https://discord.gg/nuSCQF5CQP")

@bot.command(description="Gives you the basic meaning of Nintendo 3DS homebrew")
async def hb3ds(ctx):
    await ctx.respond("3DS Homebrew literally means the unofficial software developed by hobbyists for the Nintendo 3DS game console. It gives users the freedom to control their 3DS in any way they want even when it is not supported officially by Nintendo. **GUIDE:** https://3ds.hacks.guide/")

@bot.command(desciption="Invite for the Nintendo Homebrew discord server")
async def ninhb(ctx):
    await ctx.respond("https://discord.gg/nintendohomebrew")

@bot.command(description="KYS")
async def kys(ctx):
    await ctx.respond("KYS? Yes I will. **K**eep **Y**ourself **S**ave.")

@bot.command(description="Reasons why to dont use video guides")
async def vguides(ctx):
    embed = discord.Embed(
        title='Why you should not use video guides',
        description='',
        color=discord.Color.blue()
    )

    embed.add_field(name='Outdated', value='Most uploaders do not edit their guides after uploading, even if there are mistakes', inline=False)
    embed.add_field(name='Methods', value='When methods become outdated, the information is not updated', inline=True)
    embed.add_field(name='Difficulty (speaking)', value='Difficult to give assistance with', inline=False)
    embed.add_field(name='Zip files', value='Most videos also refer to a pre-packaged download, which are often outdated and poorly organised', inline=False)

    embed.set_footer(text='In general, just use the official guides.')

    await ctx.respond(embed=embed)

@bot.command(description="List of moderation commands")
async def modhelp(ctx):
    if any(role.name in ["Admins", "Mods"] for role in ctx.author.roles):
                           # ^ change to your actual role name
        help_message = """
        **Moderation Commands:**
        /kick

        /ban

        /mute

        /unmute
        
        Feel free to contact the bot owner for additional assistance.
        """
        await ctx.respond(content=help_message)
    else:
        await ctx.respond("Sorry, you do not have permission to use this command.")

@bot.command(description="List of Homebrew commands")
async def hbhelp(ctx):
    help_message = """
    **Homebrew Commands:**
    /drxy3ds

    /hb3ds

    /ninhb

    /vguides

    /f3ds

    /fwiiu

    /fswitch

    Feel free to contact the bot owner for additional assistance.
    """

    await ctx.respond(content=help_message)

@bot.command(description="Latest 3DS Firmware")
async def f3ds(ctx):
    await ctx.respond(f"Current 3DS Firmware is: **11.17.0-50**. If you want to check what homebrew is available for your firmware, go to https://3ds.hacks.guide/")

@bot.command(description="Latest Wii U Firmware")
async def fwiiu(ctx):
    await ctx.respond(f"Current Wii U Firmware is: **5.6.0**. If you want to check what homebrew you can do, visit https://wiiu.hacks.guide/")

@bot.command(description= "Current Switch Firmware")
async def fswitch(ctx):
    await ctx.respond(f"Current Switch Firmware is: **17.0.1**. If you want to check what homebrew you can visit, https://nh-server.github.io/switch-guide/")

@bot.command(description="Drxy's Youtube")
async def drxyyt(ctx):
    await ctx.respond("Go sub to him, he needs more subs :( https://www.youtube.com/channel/UCXdpegfis3xk_03AYq_Zq8A")

@bot.command(description="Gives information about a user")
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"{member.name}'s info", description=f"Here is {member.name}'s info:")
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Nickname", value=member.nick, inline=True)
    embed.add_field(name="Joined", value=member.joined_at, inline=True)
    await ctx.respond(embed=embed)

@bot.command(description="Gives information about the server")
async def serverinfo(ctx):
    guild = ctx.guild
    embed = discord.Embed(title=f"{guild.name}'s info", description=f"Here is {guild.name}'s info:")
    embed.add_field(name="ID", value=guild.id, inline=True)
    embed.add_field(name="Members", value=guild.member_count, inline=True)
    embed.add_field(name="Created at", value=guild.created_at, inline=True)
    await ctx.respond(embed=embed)

bot.run("BOT TOKEN HERE")
