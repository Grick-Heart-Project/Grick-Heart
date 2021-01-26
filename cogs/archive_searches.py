import discord
import json

from discord.ext import commands

from utils.ctx_class import MyContext
from utils.cog_class import Cog

class ArchiveCommands(Cog):
    @commands.command()
    async def spell(self, ctx: MyContext, *, args):
        with open('dnd-data/spells/spells.json') as f:
            spellData = json.load(f)
        try:
            spellName = spellData[args]['name']
            spellSource = spellData[args]['source']
            spellLevel = spellData[args]['level']
            spellSchool = spellData[args]['school']
            spellTime = spellData[args]['time']
            spellRange = spellData[args]['range']
            spellComponents = spellData[args]['components']
            spellDuration = spellData[args]['duration']
            spellText = spellData[args]['text']
        except KeyError:
            await ctx.send(f'Unable to find spell {args}')
            return
        spellEmbed = discord.Embed(name=f'Archival Data on {args}', description='', color=0x00e5e5)
        spellEmbed.add_field(name='Spell Name', value=spellName, inline='false')
        spellEmbed.add_field(name='Spell Source', value=spellSource, inline='false')
        spellEmbed.add_field(name='Spell Level', value=spellLevel, inline='false')
        spellEmbed.add_field(name='Spell School', value=spellSchool, inline='false')
        spellEmbed.add_field(name='Spell Time', value=spellTime, inline='false')
        spellEmbed.add_field(name='Spell Range', value=spellRange, inline='false')
        spellEmbed.add_field(name='Spell Components', value=spellComponents, inline='false')
        spellEmbed.add_field(name='Spell Duration', value=spellDuration, inline='false')
        spellEmbed.add_field(name='Spell Text', value=spellText, inline='false')
        try:
            await ctx.send(embed=spellEmbed)
        except discord.errors.HTTPException:
            await ctx.send('Error sending spell data!')

setup = ArchiveCommands.setup