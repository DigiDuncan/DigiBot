import discord
from discord.ext import commands
from globaldpn import *

class NSFWCog:
	def __init__(self, bot):
		self.bot = bot

	@commands.command()

#Necessary.
def setup(bot):
	bot.add_cog(NSFWCog(bot))
