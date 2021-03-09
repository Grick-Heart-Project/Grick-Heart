from discord.ext import commands
import discord
import json

with open('release.json') as f:
    data = json.load(f)
    release = data['ghVersion']


class EmbedHelpCommand(commands.HelpCommand):
    """This is an example of a HelpCommand that utilizes embeds.
    It's pretty basic but it lacks some nuances that people might expect.
    1. It breaks if you have more than 25 cogs or more than 25 subcommands. (Most people don't reach this)
    2. It doesn't DM users. To do this, you have to override `get_destination`. It's simple.
    Other than those two things this is a basic skeleton to get you started. It should
    be simple to modify if you desire some other behaviour.

    To use this, pass it to the bot constructor e.g.:

    bot = commands.Bot(help_command=EmbedHelpCommand())
    """

    def get_command_signature(self, command):
        return '{0.qualified_name} {0.signature}'.format(command)

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title='Grick Heart Commands', colour=0x239B56)
        embed.set_footer(text=f'Current Bot Version: v{release}')
        embed.add_field(name='Roll Command', value='You can roll any dice on the planet with `!roll <dice type> <modifiers>` (replace <dice type> with the kind of dice you want to role i.e. `!roll d20`)', inline=False)
        embed.add_field(name='Spell Command', value='You can look up any spell in the D&D universe with `!spell <spell name>`.', inline=False)
        embed.add_field(name='Weapon Command', value='You can look up any weapon in the D&D universe with `!weapon <weapon name>`.', inline=False)
        embed.add_field(name='Game Command', value='This command allows DMs to control who is in the game. You can add players with `!game add <player>` and remove them with `!game remove <player>`. Be sure that you have set up your roles and channels correctly!', inline=False)
        embed.add_field(name='Initiative Command', value="By far the most handy command in the bot, you can roll for initiative with `!init roll <modifiers>` and then see your initiative number with `!init whatsmy`. You can also see all member's number with `!init list`. DMs can reset the initiative with `!init reset`.", inline=False)
        embed.add_field(name='Experience Command', value="This command stores experience scores in out database. You can see how much experience you have with `!xp whatsmy`, and your friends with `!xp list`. DM's can control xp with `!xp <add, remove, reset> <amount>`.")
        await self.get_destination().send(embed=embed)