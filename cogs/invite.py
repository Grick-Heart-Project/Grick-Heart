import discord

from utils.ctx_class import MyContext
from utils.cog_class import Cog

from discord.ext import commands
from discord.utils import get

class Invite(Cog):
    @commands.command()
    async def invite(self, ctx: MyContext):
        inviteEmbed = discord.Embed(title='Grick Heart Invite Links', color=0x239B56)
        inviteEmbed.add_field(name='Bot Invite', value='https://discord.com/oauth2/authorize?client_id=778756422275956766&scope=bot&permissions=335801458', inline=True)
        inviteEmbed.add_field(name='Support Server Invite', value='https://discord.gg/2uGynhee4K')
        await ctx.send(embed=inviteEmbed)


setup = Invite.setup