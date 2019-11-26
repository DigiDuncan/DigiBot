import discord
from discord.ext import commands
from globalWIP import *
import requests
import random

os.system("")
print(load("help.py cog loaded." + style.RESET))

class HelpCog:
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def help(self, ctx, subcommand = None):
		print(msg("User {0} requested the help for: {1}.".format(ctx.message.author.name, subcommand)))
		if subcommand == None: subcommand = "none"
		if subcommand.lower() == "emojify":
			helpstring = """
`{0}emojify <string>`: \"Emojifies\" a string. For example, turns \"abc\" into :regional_indicator_a::regional_indicator_b::regional_indicator_c:.
Supports the following characters: [AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789.!?,*#*'‽+-=<>^¥€£_] and space.
Now supports full-width versions of most if not all characters, thanks BlankNam3dKid.""".format(prefix)
		elif subcommand.lower() == "wellthissays":
			helpstring = """
`{0}wellthissays <string>`: This one's... hard to explain. There's a joke Digi likes to do that goes like this:
*Person A:* [gives an opinion]
*Person B:* Oh yeah? Well this says otherwise.
*Person B sends a picture that says \"Otherwise\".*
This command takes this a step further, letting you make a picture that says anything as the punchline to a joke.
Basically, it's a text to image command.""".format(prefix)
		elif subcommand.lower() == "lyrics":
			pass
		elif subcommand != "none":
			helpstring = """
Sorry! {0} doesn't have a help file.""".format(subcommand)
		else:
			helpstring = """
**{1} version {2}**
*by DigiDuncan*

`{0}help [subcommand]`: this command. Items with a **†** are able to be used as a subcommand of `help` for more info.
`{0}sing <string>`: Has {1} sing a string.
`{0}roll <X>d<Y>[d<Z>]`: Rolls X number of Y sided dice, dropping the lowest Z amount.
`{0}emojify`**†**: <string>: \"Emojifies\" a string.
`{0}ascii <string>`: Makes a string into ASCII art.
`{0}wellthissays <string>`**†**: Punchlin**e** to the joke: 'Well *this* says X.'
`{0}lyrics <song>`**†**: Command for on-time lyric printing. Use `{0}help lyrics` for a list of available songs.
`{0}image <image>`**†**: Produces a reaction image. Use `{0}help image` for a list of available images.
`{0}game`: Plays a game with {1}.
`{0}easteregg`: Gives details about how to report an easter egg, and view the Leaderboard!
`{0}report`: Send a message to the bot owner to report a bug or feature request.""".format(prefix, botname, version)
		await ctx.send("<@{0}>{1}".format(ctx.message.author.id, helpstring))

	@commands.command()
	async def easteregg(self, ctx):
		print(msg("User {0} called the easteregg command.".format(ctx.message.author.name)))
		printstring = """
**Easter eggs?** Of course!
This bot contains some easter eggs! If you're the first to find it, you'll be added to this list!
Use {0}report and tell me which egg you thought you found!
***Easter Egg Leaderboard:***
`Easter egg #G: Arceus3251 [Sep 24 2018]`
`Easter egg #C: MLBoost [Oct 13 2018]`""".format(prefix)
		await ctx.send("<@{0}>{1}".format(ctx.message.author.id, printstring))

	@commands.command()
	async def report(self, ctx, *, message : str):
		print(msg("User {0} sent a report: \"{1}\".".format(ctx.message.author.name, message)))
		try:
			await self.bot.get_user(digi_id).send("<@{0}>: {1}".format(ctx.message.author.id, message))
		except:
			print(crit("Report failed! Digi can't code."))

#Necessary.
def setup(bot):
	bot.add_cog(HelpCog(bot))
