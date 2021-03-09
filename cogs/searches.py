import discord
import json
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

def magicitemsAPI(itemname):
    request = requests.get(f'https://api.open5e.com/magicitems/{itemname}')
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
    def monsterembed(name, size, type, armor_class, hit_points, strength, dexterity, constitution, intelligence, wisdom, charisma, damage_vulnerabilities, damage_immunities, condition_immunities, senses, languages, actions, reactions, legendary_actions):
        if (damage_vulnerabilities == ''):
            damage_vulnerabilities = "None"
        if (damage_immunities == ''):
            damage_immunities = "None"
        if (condition_immunities == ''):
            condition_immunities = "None"
        if (legendary_actions == ''):
            legendary_actions = "None"
        embed = discord.Embed(title=f'Monster Data for {name}', color=0x239B56)
    '''


def weaponembed(name, category, source, cost, damage_dice, damage_type, weight):
    damage = damage_dice +" "+damage_type
    embed = discord.Embed(title=f'Weapon Data for {name}', color=0x239B56)
    embed.add_field(name='Source', value=source, inline=True)
    embed.add_field(name='Cost', value=cost, inline=True)
    embed.add_field(name='Damage', value=damage, inline=True)
    embed.add_field(name='Weight', value=weight, inline=True)
    return embed

def magicitemembed(name, type, rarity, requires_attunement, source):
    if (requires_attunement == 'requires attunement'):
        requires_attunement = 'true'
    else:
        requires_attunement = 'false'
    embed = discord.Embed(title=f'Magic Item Data for {name}', color=0x239B56)
    embed.add_field(name='Source', value=source, inline=True)
    embed.add_field(name='Type', value=type, inline=True)
    embed.add_field(name='Rarity', value=rarity, inline=True)
    embed.add_field(name='Requires Attunement?', value=requires_attunement, inline=True)
    embed.add_field(name='Description', value='Look in message below', inline=False)
    return embed


class Searches(Cog):
        @commands.command()
        async def spell(self, ctx: MyContext, *, spellname):
            spellName1 = '-'.join(spellname.split(' '))
            try:
                sD = spellAPI(spellName1)
                embed = spellembed(sD['name'], sD['page'], sD['level'], sD['school'], sD['casting_time'], sD['range'], sD['components'], sD['duration'], sD['dnd_class'])
                await ctx.send(embed=embed)
                if (sD['higher_level'] == ""):
                    higher_level = 'No Bonuses'
                spellText = sD['desc'] +" At Higher Levels: "+ higher_level
                await ctx.send(f"Spell Text: {spellText}")
            except KeyError:
                await ctx.send(f':octagonal_sign: ERROR: Could not find spell {spellname}')
                return
        '''
        @commands.command()
        async def monster(self, ctx: MyContext, monstername):
            monstername1 = '-'.join(monstername.split(' '))
            try:
                mD = monsterAPI(monstername1)

            except KeyError:
                await ctx.send(f':octagonal_sign: ERROR: Could not find monster {monstername}')
        '''

        @commands.command()
        async def weapon(self, ctx: MyContext, *, weaponname):
            weaponname1 = '-'.join(weaponname.split(' '))
            if (weaponname == 'Molotov Cocktail' or weaponname == 'molotov cocktail'):
                if (ctx.author.id == '712401279774621827'):
                    await ctx.send(f"{ctx.author.mention}, you lack the skill to use that")
                    return
                else:
                    hydro: discord.User = await self.bot.fetch_user(711960088553717781)
                    hydro_mention: str = hydro.mention
                    await ctx.send(f"Be careful with that, you wouldn't want to hurt {hydro_mention}")
                    return
            else:
                try:
                    wD = weaponAPI(weaponname1)
                    embed = weaponembed(wD['name'], wD['category'], wD['document__slug'], wD['cost'], wD['damage_dice'], wD['damage_type'], wD['weight'])
                    await ctx.send(embed=embed)
                except KeyError:
                    await ctx.send(f':octagonal_sign: ERROR: Could not find weapon {weaponname}')
                    return
        
        @commands.command(aliases=['mitem'])
        async def magicitem(self, ctx: MyContext, *, itemname):
            itemname1 = '-'.join(itemname.split(' '))
            try:
                iD = magicitemsAPI(itemname1)
                embed = magicitemembed(iD['name'], iD['type'], iD['rarity'], iD['requires_attunement'], iD['document__slug'])
                await ctx.send(embed=embed)
                itemText = iD['desc']
                await ctx.send(f'Item Description: {itemText}')
            except KeyError:
                await ctx.send(f':octagonal_sign: ERROR: Could not find magic item {itemname}')
                return


setup = Searches.setup