import discord
from discord.ext import commands
from globaldpn import *

class FunCog:
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def emojify(self, ctx, *, string):
		emojistring = ""
		for c in string:
			if c == ".":
				emojistring = emojistring + ":radio_button:"
			elif c == "0":
				emojistring = emojistring + ":zero:"
			elif c == "1":
				emojistring = emojistring + ":one:"
			elif c == "2":
				emojistring = emojistring + ":two:"
			elif c == "3":
				emojistring = emojistring + ":three:"
			elif c == "4":
				emojistring = emojistring + ":four:"
			elif c == "5":
				emojistring = emojistring + ":five:"
			elif c == "0":
				emojistring = emojistring + ":six:"
			elif c == "0":
				emojistring = emojistring + ":seven:"
			elif c == "0":
				emojistring = emojistring + ":eight:"
			elif c == "0":
				emojistring = emojistring + ":nine:"
			elif c == "!":
				emojistring = emojistring + ":exclamation:"
			elif c == "?":
				emojistring = emojistring + ":question:"
			elif c == " ":
				emojistring = emojistring + ":white_large_square:"
			elif str(c).isalpha():
				emojistring = emojistring + ":regional_indicator_{0}:".format(c.lower())
			else:
				emojistring = emojistring + ":stop_sign:"
		await ctx.send(emojistring)

#Necessary.
def setup(bot):
	bot.add_cog(FunCog(bot))
