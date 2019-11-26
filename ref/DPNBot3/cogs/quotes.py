import discord
from discord.ext import commands
from globaldpn import *
import datetime
import os

quotefile = 'C:\\Users\\DigiDuncan\\Documents\\GitHub\\DPNQuotes\\DPN Quotes.txt'
now = datetime.datetime.now()

class QuotesCog:
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def quote(self, ctx, arg):
		arg = int(arg)
		if (arg <= 0):
			return 0
		f = open(quotefile, "r")
		lines = f.readlines()
		quotetext = lines[arg - 1]
		quotetext = quotetext.replace(";", "\n")
		await ctx.send("Quote {0}: {1}".format(str(arg), quotetext))

	@commands.command()
	async def addquote(self, ctx, name, line):
		f = open(quotefile, "a+")
		line = line.replace("/n", ";")
		f.write(str('\n"{0}" *-- {1}, {2}*').format(line, name, str(now.year)))
		#os.system("C:\\Users\\DigiDuncan\\Desktop\\DPNBot3\\push.bat")
		f.close()
		f = open(quotefile, "r")
		lines = f.readlines()
		await ctx.send("Quote {0} written.".format(len(lines)))

	@commands.command()
	async def allquotes(self, ctx):
		f = open(quotefile, "r")
		lines = f.readlines()
		for x in range(len(lines)):
				quotetext = lines[x]
				quotetext = quotetext.replace(";", "\n")
				await ctx.send("Quote {0}: {1}".format(str(x + 1), quotetext))
				await asyncio.sleep(1)
		f.close()

#Necessary.
def setup(bot):
	bot.add_cog(QuotesCog(bot))
