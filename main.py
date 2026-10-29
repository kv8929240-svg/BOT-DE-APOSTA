
import os
import discord
from discord import app_commands
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot conectado: {bot.user}")


@bot.tree.command(name="painel", description="Abrir painel de ORG e AP")
async def painel(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🔥 PAINEL ORG & AP",
        description=(
            "🎮 Filas de Free Fire\n"
            "🛡️ Painel de mediadores\n"
            "🎟️ Tickets da organização\n"
            "💰 Pagamentos Pix sujeitos à aprovação do ADM\n\n"
            "Painel inicial do bot."
        ),
        color=discord.Color.orange()
    )
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="filas", description="Consultar as filas")
async def filas(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🎮 Sistema de filas será configurado na próxima etapa."
    )


@bot.tree.command(name="mediadores", description="Consultar mediadores")
async def mediadores(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🛡️ Painel de mediadores será configurado na próxima etapa."
    )


if not TOKEN:
    raise RuntimeError("Configure a variável DISCORD_TOKEN.")

bot.run(TOKEN)
