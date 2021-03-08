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
    embed = discord.Embed(name=f'Spell Data for {name}', color=0x239B56)
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
    async def roll(self, ctx: MyContext, dice):
        value = random.randint(1, int(dice))
        await ctx.reply(f"You rolled a {value}!")
    
    @commands.command()
    async def spell(self, ctx: MyContext, spellname):
        try:
            sD = spelljson(spellname)
        except KeyError:
            await ctx.send(f':octagonal_sign: ERROR: Could not find spell {spellname}')
            return
        embed = spellembed(sD['name'], sD['source'], sD['level'], sD['school'], sD['time'], sD['range'], sD['components'], sD['duration'], sD['classes'])
        await ctx.send(embed=embed)
        await ctx.send(f"Spell Text {sD['text']}")

    @commands.has_role('DM' or 'DM Helper')
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
