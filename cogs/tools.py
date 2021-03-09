import discord
import json

from utils.ctx_class import MyContext
from utils.cog_class import Cog

from discord.ext import commands
from discord.utils import get

with open('release.json') as f:
    data = json.load(f)
    release = data['ghVersion']

class Tools(Cog):
    @commands.command()
    async def invite(self, ctx: MyContext):
        inviteEmbed = discord.Embed(title='Grick Heart Invite Links', color=0x239B56)
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
        creditsEmbed = discord.Embed(title='Grick Heart Credits', color=0x239B56)
        creditsEmbed.add_field(name='Developer', value=hydro_mention)
        creditsEmbed.add_field(name='Bot Framework Developer', value=eyes_mention)
        creditsEmbed.add_field(name='Bot Requestor', value=walker_mention)
        creditsEmbed.add_field(name='API', value='https://open5e.com')
        creditsEmbed.set_footer(text=f'Current Bot Version: v{release}')
        await ctx.send(embed=creditsEmbed)


setup = Tools.setup