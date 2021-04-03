from operator import add
from os import name
import time
import discord
import random
import json

from discord.ext import commands
from discord.ext.commands import bot
from discord.utils import get

from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.models import get_from_db

class PlayCore(Cog):
    @commands.command()
    async def roll(self, ctx: MyContext, dice, modifiers = 0):
        """
        Rolls literally ANY dice you want
        """
        diceNum = ''.join(dice.split('d', 1))
        value = random.randint(1, int(diceNum)) + modifiers
        await ctx.send(f"{ctx.author.mention}, you rolled a {value}!")

    @commands.has_any_role('DM', 'DM Helper')
    @commands.command()
    async def game(self, ctx: MyContext, option, member: discord.Member):
        """
        Game Handler. This command controls who is in the game and who isn't
        """
        db_guild = await get_from_db(ctx.guild)
        if (db_guild.isInit < 2):
            await ctx.send(f'This guild is not initialized! Go bother your admins to run `!initialize`!')
            return
        else:
            if (option == 'add'):
                role = get(ctx.guild.roles, name=db_guild.gameRole)
                gameChannel = get(ctx.guild.channels, name=db_guild.gameChannel)
                await gameChannel.send(f'{member} has been added to the game!')
                await member.add_roles(role)
                await ctx.send(f'{member} has been added to the game!')
            if (option == 'remove'):
                role = get(ctx.guild.roles, name=db_guild.gameRole)
                gameChannel = get(ctx.guild.channels, name=db_guild.gameChannel)
                await gameChannel.send(f'{member} has been removed from the game!')
                await member.remove_roles(role)
                await ctx.send(f'{member} has been removed from the game!')

    @commands.group(aliases=['xp'])
    async def experience(self, ctx: MyContext):
        """
        Experience Point Handler
        """
        if not ctx.invoked_subcommand:
            await ctx.send("Grick Heart's Experience command!\nSyntax: `!xp <option>`")

    @commands.has_role('DM')
    @experience.command(aliases=['give'])
    async def add(self, ctx: MyContext, player: discord.Member, addAmount):
        """
        Adds Experience Points
        """
        addXP = int(addAmount)
        db_user = await get_from_db(player)
        oldXPNum = db_user.xpNum
        db_user.xpNum = oldXPNum + addXP
        await db_user.save()
        await ctx.send(f"Added {addAmount}xp to {player.mention}'s expereince score. {player.mention} now has {db_user.xpNum} experience")

    @commands.has_role('DM')
    @experience.command(aliases=['revoke', 'take'])
    async def remove(self, ctx: MyContext, player: discord.Member, removeAmount):
        """
        Removes Experience Points
        """
        subtractXP = int(removeAmount)
        db_user = await get_from_db(player)
        oldXPNum = db_user.xpNum
        db_user.xpNum = oldXPNum - subtractXP
        await db_user.save()
        await ctx.send(f"Subtracted {removeAmount}xp from {player.mention}'s expereince score. {player.mention} now has {db_user.xpNum} experience")

    @commands.has_role('DM')
    @experience.command()
    async def reset(self, ctx: MyContext, player: discord.Member):
        """
        Resets Experience Points
        """
        db_user = await get_from_db(player)
        db_user.xpNum = 0
        await db_user.save()
        await ctx.send(f"Reset {player.mention}'s experience score.")

    @commands.has_role('Game Access')
    @experience.command()
    async def whatsmy(self, ctx: MyContext):
        """
        Returns the amount of experience the author has
        """
        db_user = await get_from_db(ctx.author)
        await ctx.send(f"{ctx.author.mention}, your experience score is {db_user.xpNum}.")

    @commands.has_any_role('Game Access', 'DM', 'DM Helper')
    @experience.command()
    async def list(self, ctx: MyContext):
        """
        Lists the experience total for all those at the table
        """
        embed = discord.Embed(title=f'Experience Scores for {ctx.guild.name}', color=0xF1C40F)
        gameRole = get(ctx.guild.roles, name='Game Access')
        if gameRole is None:
            await ctx.send('Hmm you havent set your server up correctly')
        empty = True
        for member in ctx.guild.members:
            if gameRole in member.roles:
                db_user1 = await get_from_db(member)
                xpNum = db_user1.xpNum
                embed.add_field(name=member, value=str(xpNum), inline=False)
                empty = False
        if empty:
            await ctx.send('No Players')
        await ctx.send(embed=embed)

    




setup = PlayCore.setup
