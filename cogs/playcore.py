import time
import discord
import json
import random

from discord.ext import commands

from utils.cog_class import Cog
from utils.ctx_class import MyContext


def spelljson(spellname):
    with open('Grick-Heart-Data/spells/spells.json') as f:
        data = json.load(f)
        return data[spellname]


def spellembed(name, source, level, school, time, range, components, duration, classes):
    embed = discord.Embed(title=f"Spell Data for {name}", desciption='', color=0x00e5e5)
    embed.add_field(name='Source', value=source, inline='true')
    embed.add_field(name='Level', value=level, inline='true')
    embed.add_field(name='School', value=school, inline='true')
    embed.add_field(name='Time', value=time, inline='true')
    embed.add_field(name='Range', value=range, inline='true')
    embed.add_field(name='Components', value=components, inline='true')
    embed.add_field(name='Duration', value=duration, inline='true')
    embed.add_field(name='Classes', value=classes, inline='true')
    embed.add_field(name='Text', value='Look in message below', inline='true')
    return embed


class PlayCore(Cog):
    @commands.command()
    async def roll(self, ctx: MyContext, dice):
        value = random.randint(1, int(dice))
        await ctx.reply(f"You rolled a {value}!")

    @commands.command()
    async def spell(self, ctx: MyContext, spellname):
        sD = spelljson(spellname)
        await ctx.send(embed=spellembed(sD['name'], sD['source'], sD['level'], sD['school'], sD['time'], sD['range'], sD['components'], sD['duration'], sD['classes']))
        await ctx.send(f"Text: {sD['text']}")


setup = PlayCore.setup
