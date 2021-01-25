import discord
import json
import sys

from discord.ext import commands

from utils.ctx_class import MyContext
from utils.cog_class import Cog

with open('release.json') as f:
    releaseData = json.load(f)

class Info(Cog):
    @commands.command()
    async def version(self, ctx: MyContext):
        verEmbed = discord.Embed(title="Grick Heart Version Info", description='', color=0x00e5e5)
        verEmbed.add_field(name='Version', value=releaseData['ghVersion'], inline='true')
        verEmbed.add_field(name='Release Date', value=releaseData['releaseDate'], inline='true')
        verEmbed.add_field(name='Have Issues?', value='Let us know at our GitHub page!\n https://github.com/Grick-Heart-Project/Grick-Heart', inline='false')
        verEmbed.add_field(name='System Info', value=f'Running Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} on {sys.platform}', inline='true')
        await ctx.send(embed=verEmbed)

setup = Info.setup