import discord
from discord.ext import commands, tasks
import asyncio

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents)

# This code checks for duplicate names for commands. To help get rid of console errors.
commands = [
    {"name": "commands", "description": "This is command 1"},
    {"name": "pn", "description": "This is command 2"},
    {"name": "mod", "description": "This is command 3"},
    {"name": "hb", "description": "This is command 4"},
]

unique_commands = []
command_names = set()

for command in commands:
    if command["name"] not in command_names:
        unique_commands.append(command)
        command_names.add(command["name"])
    else:
        print(f"Duplicate command found: {command['name']}")

@bot.event
async def on_ready():
    print(f'Nyxx is online and ready to go!')
    change_status.start()

@tasks.loop(seconds=10)  # Change status every 10 seconds
async def change_status():
    server_count = len(bot.guilds)
    statuses = [
        discord.Game(name="Now Online 24/7 thanks to Dires!"),
        discord.Game(name="Rewritten codebase!"),
        discord.Game(name="Helping users with Homebrew!"),
        discord.Game(name="Watching the Discord Server!"),
        discord.Game(name="Im in {server_count} servers!"),
    ]
    for status in statuses:
        await bot.change_presence(activity=status, status=discord.Status.online)
        await asyncio.sleep(10)  # Wait for 10 seconds before changing to the next status

# Load cogs (modules)
bot.load_extension('Cogs.Moderation')
bot.load_extension('Cogs.General')
bot.load_extension('Cogs.Homebrews')
bot.load_extension('Cogs.Pretendo')

bot.run("TOKEN_HERE")