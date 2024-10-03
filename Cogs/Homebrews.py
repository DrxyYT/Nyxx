import discord
from discord.ext import commands

class Homebrews(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
# Help command
    @discord.slash_command(name="hb", description="List of available commands.")
    async def hb(self, ctx):
        help_message = """
        # List of Homebrew Commands:
        /ninhb - Invite for the Nintendo Homebrew Discord Server
        
        /cfw3ds - Guide on how to install CFW on a Nintendo 3DS
        
        /cfwwiiu - Guide on how to install CFW on a Nintendo Wii U
        
        /f3ds - Latest Nintendo 3DS Firmware
        
        /fwiiu - Latest Nintendo Wii U Firmware
        """
        await ctx.respond(help_message)
        
@discord.slash_command(description="Latest 3DS Firmware")
async def f3ds(ctx):
    await ctx.respond(f"Current 3DS Firmware is: **11.17.0-50**. If you want to check what homebrew is available for your firmware, go to https://3ds.hacks.guide/")

@discord.slash_command(description="Latest Wii U Firmware")
async def fwiiu(ctx):
    await ctx.respond(f"Current Wii U Firmware is: **5.5.6** for USA and **5.5.5** for Europe. If you want to check what homebrew you can do, visit https://wiiu.hacks.guide/")

@discord.slash_command(description= "Current Switch Firmware")
async def fswitch(ctx):
    await ctx.respond(f"Current Switch Firmware is: **18.1.0**. If you want to check what homebrew you can do, visit https://nh-server.github.io/switch-guide/")
        
@discord.slash_command(desciption="Invite for the Nintendo Homebrew discord server")
async def ninhb(ctx):
    await ctx.respond("https://discord.gg/nintendohomebrew")     

def setup(bot):
    bot.add_cog(Homebrews(bot))