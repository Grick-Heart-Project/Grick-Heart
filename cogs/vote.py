import discord
import dbl
import asyncio

from discord.ext import commands, tasks
from discord.utils import get

from typing import Dict

from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.bot_class import MyBot
from utils.config import load_config

config = load_config()

class VoteCog(Cog):
    def __init__(self, bot):
        self.user_callbacks: Dict[int, asyncio.Task] = {}
        self.done_user_callbacks: Dict[int, asyncio.Task] = {}
        self.bot = bot
        self.token = config['auth']['top']['token']
        self.dblpy = dbl.DBLClient(self.bot, self.token, webhook_path='/api/topwebhook', webhook_auth=config['auth']['top']['password'], webhook_port=5000)

    @commands.command()
    async def vote(self, ctx: MyContext):
        await ctx.send(f"Hey! Why don't you vote for {self.bot.user.name} on top.gg? You can do that at https://top.gg/bot/778756422275956766")

    @commands.Cog.listener()
    async def on_dbl_test(self, data):
        user_id = data['user']
        user = await self.bot.fetch_user(user_id)
        thanks_embed = discord.Embed(title='Thanks For Voting!', description=f"Hey {user.mention}!\n\nThanks for voting for {self.bot.user.name}! I will remind you in 12 hours to vote for me again! (This is a Test!)", color=0xF1C40F)
        await user.send(embed=thanks_embed)

    @commands.Cog.listener()
    async def on_dbl_vote(self, data):
        user_id = data['user']
        user = await self.bot.fetch_user(user_id)
        thanks_embed = discord.Embed(title='Thanks For Voting!', description=f"Hey {user.mention}!\n\nThanks for voting for {self.bot.user.name}! I will remind you in 12 hours to vote for me again!", color=0xF1C40F)
        await user.send(embed=thanks_embed)
        task = asyncio.create_task(self.vote_reminder(user))
        self.user_callbacks[user.id] = task

    async def vote_reminder(self, user: discord.User):
        await asyncio.sleep(86460)
        remind_embed = discord.Embed(title='A Friendly Reminder to Vote!', description=f"Hey {user.display_name}! It's been 12 hours since you voted, and this is a reminder to do it again! You can vote at https://top.gg/bot/778756422275956766. Thanks!", color=0xF1C40F)
        await user.send(embed=remind_embed)
        user_callback = self.user_callbacks.pop(user.id)
        if isinstance(user_callback, asyncio.Task):
            self.done_user_callbacks[user.id] = user_callback

setup = VoteCog.setup