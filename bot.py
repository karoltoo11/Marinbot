import os
import random
import discord
from discord import app_commands
from discord.ext import commands
from typing import Optional, List

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

GUILD_ID = os.getenv("DISCORD_GUILD_ID", "").strip()
if GUILD_ID:
    try:
        GUILD_ID = int(GUILD_ID)
    except ValueError:
        GUILD_ID = None

TOKEN = os.getenv("DISCORD_TOKEN", "").strip()

# --- KLASA BOTA ---
class marinBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.default(),
            activity=discord.Game(name="Wearing Cosplay"),
            status=discord.Status.online,
        )

    async def setup_hook(self):
        if GUILD_ID:
            guild = discord.Object(id=GUILD_ID)
            await self.tree.sync(guild=guild)
            print(f"Logged in as {self.user} | Command sinchronize on server {GUILD_ID}.")
        else:
            await self.tree.sync()
            print(f"Logged in as {self.user} | Command sinchronize globally")

bot = marinBot()

@bot.tree.command(name="help", description="Information about commands and creator.")
async def help_command(interaction: discord.Interaction):
    embed = discord.Embed(title="🎲 Information MarinBot", color=discord.Color.pink())
    embed.add_field(name="Commands", value=(
        "`/happy` - Happy Marin gif.\n"
        "`/sad` - Sad Marin gif.\n"
        "`/ahhh` - Surprised Marin gif.\n"
        "`/happycry` - Marin weeping with happiness gif.\n"
        "`/angry` - Angry Marin gif.\n"
        "`/eating` - Marin eating pocky snack gif.\n"
        "`/dancing` - Dancing Marin gif.\n"
        "`/outro` - Outro My Dress-Up Darling gif.\n"
    ), inline=False)
    embed.add_field(name="Have a great time with Marin!", value="~karoltoo11 || <@1343819837625073687> ||", inline=False)
    embed.set_footer(text="Version 0.1  | MarinBot Gif System")

    await interaction.response.send_message(embed=embed)


from pathlib import Path
import discord

@bot.tree.command(
    name="happy",
    description="Happy Marin gif."
)
async def happy_command(interaction: discord.Interaction):
    gif_path = Path(__file__).with_name("happy.gif")

    await interaction.response.send_message(
        file=discord.File(gif_path, filename="happy.gif")
    )


@bot.tree.command(
    name="sad",
    description="Sad Marin gif."
)
async def sad_command(interaction: discord.Interaction):
    gif_path = Path(__file__).with_name("sad.gif")

    await interaction.response.send_message(
        file=discord.File(gif_path, filename="sad.gif")
    )

@bot.tree.command(
    name="ahhhh",
    description="Surprised Marin gif."
)
async def ahhhh_command(interaction: discord.Interaction):
    gif_path = Path(__file__).with_name("ahhh.gif")

    await interaction.response.send_message(
        file=discord.File(gif_path, filename="ahhh.gif")
    )

@bot.tree.command(
    name="sleeping",
    description="Sleeping Marin gif."
)
async def sleeping_command(interaction: discord.Interaction):
    gif_path = Path(__file__).with_name("sleeping.gif")

    await interaction.response.send_message(
        file=discord.File(gif_path, filename="sleeping.gif")
    )

@bot.tree.command(
    name="happycry",
    description="Marin weeping with happiness gif."
)
async def happycry_command(interaction: discord.Interaction):
    gif_path = Path(__file__).with_name("happy_cry.gif")

    await interaction.response.send_message(
        file=discord.File(gif_path, filename="happy_cry.gif")
    )

@bot.tree.command(
    name="angry",
    description="Angry Marin gif."
)
async def angry_command(interaction: discord.Interaction):
    gif_path = Path(__file__).with_name("angry.gif")

    await interaction.response.send_message(
        file=discord.File(gif_path, filename="angry.gif")
    )

@bot.tree.command(
    name="eating",
    description="Marin eating pocky snack gif."
)
async def eating_command(interaction: discord.Interaction):
    gif_path = Path(__file__).with_name("eating.gif")

    await interaction.response.send_message(
        file=discord.File(gif_path, filename="eating.gif")
    )

@bot.tree.command(
    name="dancing",
    description="Dancing Marin gif."
)
async def dancing_command(interaction: discord.Interaction):
    gif_path = Path(__file__).with_name("dancing.gif")

    await interaction.response.send_message(
        file=discord.File(gif_path, filename="dancing.gif")
    )

@bot.tree.command(
    name="outro",
    description="Outro My Dress-Up Darling gif."
)
async def outro_command(interaction: discord.Interaction):
    gif_path = Path(__file__).with_name("outro.gif")

    await interaction.response.send_message(
        file=discord.File(gif_path, filename="outro.gif")
    )



if not TOKEN:
    raise RuntimeError("Discord token is missing. Set the DISCORD_TOKEN environment variable.")

bot.run(TOKEN)


