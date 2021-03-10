import discord
import json

from discord.ext import commands
from discord.utils import get

from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.models import get_from_db

class BotSetup(Cog):
    @commands.has_guild_permissions(administrator=True)
    @commands.group()
    async def initialize(self, ctx: MyContext):
        db_guild = await get_from_db(ctx.guild)
        if not ctx.invoked_subcommand:
            if (db_guild.isInit > 1):
                await ctx.send(f"It looks like you have already set your guild up!")
                return
            else:
                embed = discord.Embed(title='Setting up Grick Heart', color=0xF1C40F)
                embed.add_field(name='Game Role', value="Please create a game role, and then run `!initialize role <EXACT ROLE NAME>`.", inline=False)
                embed.add_field(name='Game Table', value="Please create a channel for the game to take place in, and then run `!initialize channel <EXACT CHANNEL NAME>`.", inline=False)
                await ctx.send(embed=embed)
    
    @initialize.command()
    async def role(self, ctx: MyContext, *, role):
        db_guild = await get_from_db(ctx.guild)
        if (db_guild.isInit > 1):
                await ctx.send(f"It looks like you have already set your guild up!")
                return
        else:
            db_guild.gameRole = role
            db_guild.isInit = db_guild.isInit + 1
            await db_guild.save()
            await ctx.send(f"Set {ctx.guild.name}'s game role to {role}")

    @initialize.command()
    async def channel(self, ctx: MyContext, *, channel):
        db_guild = await get_from_db(ctx.guild)
        if (db_guild.isInit > 1):
                await ctx.send(f"It looks like you have already set your guild up!")
                return
        else:
            db_guild.gameChannel = channel
            db_guild.isInit = db_guild.isInit + 1
            await db_guild.save()
            await ctx.send(f"Set {ctx.guild.name}'s game channel to {channel}")

    @initialize.command()
    async def reset(self, ctx: MyContext):
        db_guild = await get_from_db(ctx.guild)
        if (db_guild.isInit < 2):
                await ctx.send(f"It looks like you haven't set your guild up!")
                return
        else:
            db_guild.gameChannel = 'none'
            db_guild.gameRole = 'none'
            db_guild.isInit = 0
            await db_guild.save()
            await ctx.send(f'Reset bot! Please reinitialize soon for access to `game` commands!')



setup = BotSetup.setup