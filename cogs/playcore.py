import time
import discord
import random
import json

from discord.ext import commands
from discord.ext.commands import bot
from discord.utils import get

from utils.cog_class import Cog
from utils.ctx_class import MyContext

def spelljson(spellname):
    with open('Grick-Heart-Data/spells/spells.json') as f:
        data = json.load(f)
        return data[spellname]

def spellembed(name, source, level, school, time, range, components, duration, classes):
    embed = discord.Embed(title=f'Spell Data for {name}', color=0x239B56)
    embed.add_field(name='Source', value=source, inline='true')
    embed.add_field(name='Level', value=level, inline='true')
    embed.add_field(name='School', value=school, inline='true')
    embed.add_field(name='Time', value=time, inline='true')
    embed.add_field(name='Range', value=range, inline='true')
    embed.add_field(name='Components', value=components, inline='true')
    embed.add_field(name='Duration', value=duration, inline='true')
    embed.add_field(name='Classes', value=classes, inline='true')
    embed.add_field(name='Spell Text', value='Look in message below', inline='true')
    return embed

class PlayCore(Cog):
    @commands.command()
    async def roll(self, ctx: MyContext, dice, modifiers = 0):
        diceNum = ''.join(dice.split('d', 1))
        value = random.randint(1, int(diceNum)) + modifiers
        await ctx.send(f"{ctx.author.mention}, you rolled a {value}!")

    @commands.has_any_role('DM', 'DM Helper')
    @commands.command()
    async def game(self, ctx: MyContext, option, member: discord.Member):
        if (option == 'add'):
            role = get(ctx.guild.roles, name='Game Access')
            gameChannel = get(ctx.guild.channels, name='table')
            await gameChannel.send(f'{member} has been added to the game!')
            await member.add_roles(role)
            await ctx.send(f'{member} has been added to the game!')
        if (option == 'remove'):
            role = get(ctx.guild.roles, name='Game Access')
            gameChannel = get(ctx.guild.channels, name='table')
            await gameChannel.send(f'{member} has been removed from the game!')
            await member.remove_roles(role)
            await ctx.send(f'{member} has been removed from the game!')


setup = PlayCore.setup
