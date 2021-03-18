import discord
import json
import sys

from utils.ctx_class import MyContext
from utils.cog_class import Cog

from discord.ext import commands
from discord.utils import get

with open('release.json') as f:
    data = json.load(f)
    release = data['ghVersion']

class Tools(Cog):
    @commands.command()
    async def version(self, ctx: MyContext):
        verEmbed = discord.Embed(title="Grick Heart Version Info", description='', color=0x239B56)
        verEmbed.add_field(name='Version', value=data['ghVersion'], inline='true')
        verEmbed.add_field(name='Release Date', value=data['releaseDate'], inline='true')
        verEmbed.add_field(name='Have Issues?', value='Let us know at our GitHub page!\n https://github.com/Grick-Heart-Project/Grick-Heart', inline='false')
        verEmbed.add_field(name='System Info', value=f'Running Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} on {sys.platform}', inline='true')
        await ctx.send(embed=verEmbed)

    @commands.command()
    async def invite(self, ctx: MyContext):
        inviteEmbed = discord.Embed(title='Grick Heart Invite Links', color=0xF1C40F)
        inviteEmbed.add_field(name='Bot Invite', value='https://discord.com/oauth2/authorize?client_id=778756422275956766&scope=bot&permissions=335801458', inline=True)
        inviteEmbed.add_field(name='Support Server Invite', value='https://discord.gg/2uGynhee4K')
        inviteEmbed.set_footer(text=f'Current Bot Version: v{release}')
        await ctx.send(embed=inviteEmbed)

    @commands.command()
    async def credits(self, ctx: MyContext):
        hydro: discord.User = await self.bot.fetch_user(711960088553717781)
        eyes: discord.User =  await self.bot.fetch_user(138751484517941259)
        walker: discord.User = await self.bot.fetch_user(712401279774621827)
        hydro_mention: str = hydro.mention
        eyes_mention: str = eyes.mention
        walker_mention: str = walker.mention
        creditsEmbed = discord.Embed(title='Grick Heart Credits', color=0xF1C40F)
        creditsEmbed.add_field(name='Developer', value=hydro_mention)
        creditsEmbed.add_field(name='Bot Framework Developer', value=eyes_mention)
        creditsEmbed.add_field(name='Bot Requestor', value=walker_mention)
        creditsEmbed.add_field(name='API', value='https://open5e.com')
        creditsEmbed.add_field(name='Copyright', value='Dungeons and Dragons is a trademark of Wizards of the Coast. I do not own this.', inline=False)
        creditsEmbed.set_footer(text=f'Current Bot Version: v{release}')
        await ctx.send(embed=creditsEmbed)

    #@commands.command()
    #async def convert(self, ctx: MyContext, currency1, currency2, amount):


setup = Tools.setup