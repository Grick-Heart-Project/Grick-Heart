import discord
import json

from discord.ext import commands

from utils.ctx_class import MyContext
from utils.cog_class import Cog

with open('release.json') as f:
    releaseData = json.load(f)

class Info(Cog):
    @commands.command()
    async def version(self, ctx: MyContext):
        verEmbed = discord.Embed(title="Grick Heart Version Info", description='version info', color=0x00e5e5)
        verEmbed.add_field(name='Version', value=releaseData['ghVersion'], inline='true')
        await ctx.send(embed=verEmbed)

setup = Info.setup