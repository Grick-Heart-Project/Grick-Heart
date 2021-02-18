import time
import discord
import random

from discord.ext import commands

from utils.cog_class import Cog
from utils.ctx_class import MyContext

class roll(Cog):
    @commands.command()
    async def roll(self, ctx, dice):
        value = random.randint(1, int(dice))
        await ctx.reply(f"You rolled a {value}!")

setup = roll.setup

