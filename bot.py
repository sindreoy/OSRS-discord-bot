from formatter import print_table_of_combinations
from items import LIST_OF_COMBINATIONS
import os
from io import StringIO

from discord.ext import commands
import discord
from dotenv import load_dotenv

from combine_items import get_money_making_combinations

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True


bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


@bot.command(
    name="combinations",
    help="Prints out a table of prices for combining items into a product",
)
async def combinations(ctx):
    combinations = get_money_making_combinations(
        combinations=LIST_OF_COMBINATIONS
    )
    response = print_table_of_combinations(combinations)
    buffer = StringIO(response)
    f = discord.File(buffer, filename="combinations.txt")
    await ctx.send(file=f)


bot.run(TOKEN)
