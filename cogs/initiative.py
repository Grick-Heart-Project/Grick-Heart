import discord
import random

from discord.ext import commands, tasks
from discord.utils import get

from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.models import get_from_db


class Initiative(Cog):
    @commands.has_role('Game Access')
    @commands.group(aliases=['init'])
    async def initiative(self, ctx: MyContext):
        """
        Initiative Handler
        """
        if not ctx.invoked_subcommand:
            await ctx.send("Grick Heart's Initiative command!\nSyntax: `!init <option>`")

    @initiative.command()
    async def roll(self, ctx: MyContext, modifiers = 0):
        """
        Rolls for initiative and adds modifiers
        """
        rawValue = random.randint(1, int(20))
        value = rawValue + modifiers
        await ctx.send(f"{ctx.author.mention}, you rolled a {value} for initiative!")
        db_user = await get_from_db(ctx.author)
        db_user.initNum = value 
        await db_user.save()
    
    @initiative.command()
    async def whatsmy(self, ctx: MyContext):
        """
        Returns your current initiative score
        """
        db_user = await get_from_db(ctx.author)
        await ctx.send(f'{ctx.author.mention}, your initiative number is {db_user.initNum}')
    
    @initiative.command()
    async def list(self, ctx: MyContext):
        """
        Returns your guilds initiative list
        """
        gameRole = get(ctx.guild.roles, name='Game Access')
        if gameRole is None:
            await ctx.send('Hmm you havent set your server up correctly')
        empty = True
        embed = discord.Embed(title=f'Initiative List for {ctx.guild.name}', color=0x239B56)
        for member in ctx.guild.members:
            if gameRole in member.roles:
                db_user1 = await get_from_db(member)
                if (db_user1.initNum == 0):
                    initNum = 'Not yet rolled for initiative'
                else:
                    initNum = db_user1.initNum
                embed.add_field(name=member, value=str(initNum), inline=False)
                empty = False
        if empty:
            await ctx.send('No Players')
        await ctx.send(embed=embed)

    @commands.has_any_role('DM', 'DM Helper')
    @initiative.command()
    async def reset(self, ctx: MyContext):
        """
        Resets all initiative scores
        """
        gameRole = get(ctx.guild.roles, name='Game Access')
        if gameRole is None:
            await ctx.send('Hmm you havent set your server up correctly')
        empty = True
        for member in ctx.guild.members:
            if gameRole in member.roles:
                db_user1 = await get_from_db(member)
                db_user1.initNum = 0
                await db_user1.save()
                await ctx.send('All initiative numbers reset!')
                empty = False
        if empty:
            await ctx.send('No Players')

setup = Initiative.setup
