import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    print("Ola Mundo!!")
    print("Ola , eu estou online!")

@bot.command()
async def ola_u(ctx:commands.Context):
    
    name = ctx.author.name
    await ctx.reply(f"Olá, {name} eu estou online!!")

bot.run(os.getenv("DISCORD_TOKEN"))