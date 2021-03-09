import discord
import json
from discord.ext.commands import context
import requests

from discord.ext import commands
from discord.utils import get

from utils.ctx_class import MyContext
from utils.cog_class import Cog

def spellAPI(spellname):
    request = requests.get(f'https://api.open5e.com/spells/{spellname}')
    data = json.loads(request.text)
    return data

def monsterAPI(monstername):
    request = requests.get(f'https://api.open5e.com/monsters/{monstername}')
    data = json.loads(request.text)
    return data

def weaponAPI(weaponname):
    request = requests.get(f'https://api.open5e.com/weapons/{weaponname}')
    data = json.loads(request.text)
    return data

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

'''
def monsterembed(name, size, type, armor_class, hit_points, strength, dexterity, constitution, intelligence, wisdom, charisma, damage_resistances, damages_immunities, condition_immunities, senses, languages, actions, reactions, legendary_actions):
    if (damage_resistances == ""):
        damage_resistances = 'None'
    if (damages_immunities == ""):
        damages_immunities = 'None'
    if (condition_immunities == ""):
        condition_immunities = 'None'
    if (actions == ""):
        actions = 'None'
    if (legendary_actions == ""):
        legendary_actions = 'None'
    actions1 = str(actions)
    embed = discord.Embed(title=f'Monster Data for {name}', color=0x239B56)
    embed.add_field(name='Size', value=size, inline=False)
    embed.add_field(name='Type', value=type, inline=False)
    embed.add_field(name='Armor Class', value=armor_class, inline=True)
    embed.add_field(name='Hit Points', value=hit_points, inline=True)
    embed.add_field(name='Strength', value=strength, inline=True)
    embed.add_field(name='Dexterity', value=dexterity, inline=True)
    embed.add_field(name='Constitution', value=constitution, inline=True)
    embed.add_field(name='Intelligence', value=intelligence, inline=True)
    embed.add_field(name='Wisdom', value=wisdom, inline=True)
    embed.add_field(name='Charisma', value=charisma, inline=True)
    embed.add_field(name='Damage Resistances', value=damage_resistances, inline=False)
    embed.add_field(name='Damage Immunities', value=damages_immunities, inline=False)
    embed.add_field(name='Condition Immunities', value=condition_immunities, inline=False)
    embed.add_field(name='Senses', value=senses, inline=False)
    embed.add_field(name='Languages', value=languages, inline=False)
    embed.add_field(name='Actions', value=actions1, inline=False)
    embed.add_field(name='Reactions', value=reactions, inline=False)
    embed.add_field(name='Legendary Actions', value=legendary_actions, inline=False)
    return embed
    #vars = str(name + size + type + str(armor_class) + str(hit_points) + str(strength) + str(dexterity) + str(constitution) + str(intelligence) + str(wisdom) + str(charisma) + damage_resistances +damages_immunities +condition_immunities + senses+ languages +str(actions)+str(reactions)+str(legendary_actions))
    #return vars
'''

def weaponembed(name, category, source, cost, damage_dice, damage_type, weight):
    damage = damage_dice +" "+damage_type
    embed = discord.Embed(title=f'Weapon Data for {name}', color=0x239B56)
    embed.add_field(name='Source', value=source, inline=True)
    embed.add_field(name='Cost', value=cost, inline=True)
    embed.add_field(name='Damage', value=damage, inline=True)
    embed.add_field(name='Weight', value=weight, inline=True)
    return embed

class Searches(Cog):
        @commands.command()
        async def spell(self, ctx: MyContext, *, spellname):
            spellName1 = '-'.join(spellname.split(' '))
            try:
                sD = spellAPI(spellName1)
            except KeyError:
                await ctx.send(f':octagonal_sign: ERROR: Could not find spell {spellname}')
                return
            embed = spellembed(sD['name'], sD['page'], sD['level'], sD['school'], sD['casting_time'], sD['range'], sD['components'], sD['duration'], sD['dnd_class'])
            await ctx.send(embed=embed)
            spellText = sD['desc'] +" At Higher Levels: "+ sD['higher_level']
            await ctx.send(f"Spell Text: {spellText}")

        '''
        @commands.command()
        async def monster(self, ctx: MyContext, *, monstername):
            monstername1 = '-'.join(monstername.split(' '))
            try:
                mD = monsterAPI(monstername1)
            except KeyError:
                await ctx.send(f':octagonal_sign: ERROR: Could not find monster {monstername}')
                return
            embed = monsterembed(mD['name'], mD['size'], mD['type'], mD['armor_class'], mD['hit_points'], mD['strength'], mD['dexterity'], mD['constitution'], mD['intelligence'], mD['wisdom'], mD['charisma'], mD['damage_resistances'], mD['damage_immunities'], mD['condition_immunities'], mD['senses'], mD['languages'], mD['actions'], mD['reactions'], mD['legendary_actions'])
            await ctx.send(embed=embed)
        '''     

        @commands.command()
        async def weapon(self, ctx: MyContext, *, weaponname):
            weaponname1 = '-'.join(weaponname.split(' '))
            try:
                wD = weaponAPI(weaponname1)
            except KeyError:
                await ctx.send(f':octagonal_sign: ERROR: Could not find weapon {weaponname}')
                return
            embed = weaponembed(wD['name'], wD['category'], wD['document__slug'], wD['cost'], wD['damage_dice'], wD['damage_type'], wD['weight'])
            await ctx.send(embed=embed)


setup = Searches.setup