from discord.ext import commands

import statcord
from toml import load

from utils.config import load_config
from utils.ctx_class import MyContext

config = load_config()


class StatcordPost(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.key = config['auth']['statcord']['token']
        self.api = statcord.Client(self.bot,self.key)
        self.api.start_loop()


    @commands.Cog.listener()
    async def on_command(self,ctx):
        self.api.command_run(ctx)

    @commands.command()
    async def stats(self, ctx: MyContext):
        await ctx.send(f'Check out {self.bot.user.name}\'s Statcord page at https://statcord.com/bot/{self.bot.user.id}')


def setup(bot):
    bot.add_cog(StatcordPost(bot))