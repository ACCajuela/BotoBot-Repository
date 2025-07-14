import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from db_setup import init_db
from commands import add_task, list_tasks_command
from scheduler import scheduler

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

bot.add_command(add_task)
bot.add_command(list_tasks_command)

@bot.event
async def on_ready():
    await init_db()

    
    if not scheduler.running:
        scheduler.start() 

    print(f"✅ Bot online como {bot.user}")

bot.run(os.getenv("DISCORD_TOKEN"))
