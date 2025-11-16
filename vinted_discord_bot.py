import os
import discord
from discord.ext import commands

TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    raise RuntimeError("TOKEN manquant : définis la variable TOKEN sur Heroku")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connecté : {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong !")

bot.run(TOKEN)
