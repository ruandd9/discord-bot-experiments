import os
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks
from datetime import time

load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    sincs = await bot.tree.sync()
    print(f"{len(sincs)} comandos sicronizados")
    enviar_mensagem.start()
    print("Ola , eu estou online!")

@bot.event
async def on_message(msg:discord.Message):
    
    if msg.author.bot:
        return
    await bot.process_commands(msg) 
    # await msg.reply(f"O usuario {msg.author.mention} mandou uma mensagem no canal {msg.channel.name}")

@bot.event 
async def on_member_join(membro:discord.Member):
    canal = bot.get_channel(1348179381524238356)
    await canal.send (f"{membro.mention} entrou no servidor!!")

@bot.event
async def on_reaction_add(reacao:discord.Reaction, membro:discord.Member):
    await reacao.message.reply(f"O membro {membro.mention} reagiu a mensagem com {reacao.emoji}") #usa o membro e a reacao, pega emoji reagido pelo membro

@bot.command()
async def falar(ctx:commands.Context, *,texto):
    
    await ctx.send(texto)

@bot.command()
async def somar(ctx:commands.Context, n1:int, n2:int):

    resultado = n1 + n2

    await ctx.send(f"A soma entre {n1} e {n2} é {resultado}")



@bot.command()
async def enviar_embed(ctx:commands.Context):
    minha_embed = discord.Embed()
    minha_embed.title = "Titulo da embed"
    minha_embed.description = "Descricao da embed"

    imagem = discord.File("img/bomdia.jpg", "bom_dia.jpg")
    minha_embed.set_image(url="attachment://bom_dia.jpg")

    minha_embed.set_footer(text="Esse e o footer da minha imagem")

    minha_embed.set_author(name="Son Goku", icon_url="https://i.pinimg.com/736x/c2/61/40/c26140a6eba1567aff271cf00eda2726.jpg", url="https://github.com/ruandd9/discord-bot-experiments")

    await ctx.reply(embed=minha_embed, file=imagem)

@tasks.loop(time=time(16, 48))
async def enviar_mensagem():
    canal = bot.get_channel(1348179381524238356)
    await canal.send("Mensagem programada!")

@bot.tree.command()
async def ola(interact:discord.Interaction):
    await interact.response.send_message(f"Ola {interact.user.name}!!", ephemeral=True)

@bot.tree.command()
async def falar(interact:discord.Interaction, texto:str):
    await interact.response.send_message(texto)

@bot.tree.command()
async def somar (interact:discord.Interaction, n1:int, n2:int):
    resultado = n1 + n2
    await interact.response.send_message(f"O resultado entre {n1} e {n2} é {resultado}")


@bot.tree.command()
async def selecionar_membro (interact:discord.Interaction, membro:discord.Member):
    await interact.response.send_message(f"O membro selecionado foi {membro.mention}!!")

    
bot.run(os.getenv("DISCORD_TOKEN"))