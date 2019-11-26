import discord
from discord.ext import commands
from globalWIP import *
import requests
import random
import asyncio
import io
import re
import json
import csv
import sys

os.system("")
os.system("chcp 65001")
print(load("fun.py cog loaded." + style.RESET))
#sys.setdefaultencoding('utf8')
#print(load("Encoding set to UTF-8." + style.RESET))

class FunCog:
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def ascii(self, ctx, *, string):
		print(msg("User {0} requested ASCII of the string \"{1}\".".format(ctx.message.author.name, string)))
		string = string.replace(" ", "+")
		response = requests.get("http://artii.herokuapp.com/make?text={0}&font=big".format(string))
		art = response.content.decode("utf-8")
		art = "```\n" + art + "```"
		await ctx.send(art)

	@commands.command()
	async def wellthissays(self, ctx, *, string):
		print(msg("User {0} requested image of the string \"{1}\".".format(ctx.message.author.name, string)))
		stringbu = string
		string = string.replace("+", "0x2B")
		string = string.replace("#", "0x23")
		string = string.replace("%", "0x25")
		string = string.replace("&", "0x26")
		string = string.replace(" ", "+")
		if string == "E":
			print(msg("Delivering meme."))
			response = requests.get("https://dummyimage.com/800/0000ff/ff0000&text={0}".format(string))
		else:
			response = requests.get("https://dummyimage.com/800x3:1/00/ffffff&text={0}".format(string))
		image = response.content
		await ctx.message.delete()
		if stringbu.endswith(".") or stringbu.endswith("!") or stringbu.endswith("?"):
			punct = ""
		else:
			punct = "."
		if string == "E":
			await ctx.send('***E***', file=discord.File(image, 'E.png'))
		else:
			await ctx.send('Well *this* says {0}{1}'.format(stringbu, punct), file=discord.File(image, 'output.png'))

	@commands.command()
	async def wellthisays(self, ctx):
		print(msg("User {0} spelled \"wellthissays\" wrong.".format(ctx.message.author.name)))
		await ctx.send('<@{0}> spelled `wellthissays` wrong.'.format(ctx.message.author.id), delete_after=5)


	@commands.command()
	async def emojify(self, ctx, *, string):
		print(msg("User {0} requested emojification of the string \"{1}\".".format(ctx.message.author.name, string)))
		emojistring = ""
		if string == "$test":
			print(msg("Sending test message."))
			string = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789 .!?,*#*'‽+-=<>^¥€£"
		if string.lower() == "b":
			emojistring = ":b:"
		else:
			for c in string:
				for k, v in emojidict.items():
					if c == k:
						emojistring = emojistring + v
				if c not in emojidict:
					emojistring = emojistring + ":stop_sign:"
		if len(emojistring) >= 2000:
			print(msg("User {0} requested an emojified string too long for Discord.".format(ctx.message.author.id)))
			await ctx.send("<@{0}>, Emojified string too long for Discord.".format(ctx.message.author.id), delete_after=5)
		else:
			await ctx.send(emojistring)

	@commands.command()
	async def roll(self, ctx, dString, modType : str = None, mod : int = None):
		rolls = []
		usedrolls = []
		dSides = 0
		dNum = 0
		dDrops = 0
		dTotal = 0
		printModType = ""
		printMod = ""
		dArray = dString.split("d")
		if len(dArray) == 2:
			dNum = int(dArray[0])
			dSides = int(dArray[1])
		elif len(dArray) == 3:
			dNum = int(dArray[0])
			dSides = int(dArray[1])
			dDrops = int(dArray[2])
		else:
			await ctx.send('Format has to be in XdY or XdYdZ.')
			return
		print(msg("User {0} rolled {1} {2}-sided dice and dropped {3}.".format(ctx.message.author.name, dNum, dSides, dDrops)))
		for x in range(dNum):
			currentRoll = (random.randrange(1, dSides))
			rolls.append(currentRoll)
		rolls.sort(key=int)
		for x in range(dDrops, len(rolls)):
			dTotal = dTotal + rolls[x]
			usedrolls.append(rolls[x])
		#diffs = set(rolls).symmetric_difference(set(usedrolls))
		if modType != None and mod != None:
			printMod = mod
			printModType = modType
			if modType == "+": dTotal += mod
			if modType == "-": dTotal -+ mod
		print(msg("User {0} rolled {1} {3}{4} for a total of {2}".format(ctx.message.author.name, str(usedrolls), str(dTotal), printModType, printMod)))
		await ctx.send("{0} rolled {1} {4}{5} and got {2}!\nDice: {3} {4}{5}".format(ctx.message.author.name, dString, str(dTotal), str(usedrolls), printModType, printMod))

	@commands.command()
	async def game(self, ctx):
		print(msg("User {0} wished to play a game.".format(ctx.message.author.name)))
		await ctx.send("`SHALL WE PLAY A GAME?`", file=discord.File("images/games.jpg", 'games.jpg'))
		await ctx.send("You found an easter egg! The first one to find this was: **Arceus3251**")

	@commands.command()
	async def sing(self, ctx, *, string : str):
		print(msg("User {0} sang the string \"{1}\".".format(ctx.message.author.name, string)))
		await ctx.message.delete()
		newstring = ":musical_score: *" + string + "* :musical_note:"
		await ctx.send(newstring)

	@commands.command()
	async def lyrics(self, ctx, *, title):
		title = str(title)
		print(msg("User {0} displayed the lyrics to {1}{2}{3}.".format(ctx.message.author.name, attr(4), title.title(), attr(24))))
		song = await ctx.send("*Loading lyrics...*")
		title = title.replace(" ", "_")
		title = title.lower()
		try:
			f = io.open("lyrics/{0}.blf".format(title), mode="r", encoding="utf-8")
			print(time() + load("Loaded {0}.blf.".format(title)))
			lyrics = f.readlines()
			linenum = 0
			lasttimestamp = 0.0
			header = ""
			for line in lyrics:
				linenum = linenum + 1
				if linenum == 1:
					header = "**" + line.rstrip() + "** by "
				elif linenum == 2:
					header = header + line.rstrip()
					await song.edit(content = header)
					await song.edit(content = str(song.content + newline + ("-" * (len(song.content) + 18) )))
				elif linenum == 3:
					if ":" in line:
						linenumbers = line.split(":")
						lasttimestamp = (int(linenumbers[0]) * 60) + float(linenumbers[1])
					else:
						lasttimestamp = float(line)
				else:
					if linenum % 2 == 0:
						paren = line.startswith("(") or line.startswith(":")
						colon = line.startswith(":")
						if not colon: out = song.content + newline + ":musical_note: "
						if colon: out = song.content + newline
						if not paren: out = out + "*"
						out = out + line.rstrip()
						if not paren: out = out + "*"
						if not colon: out = out + " :musical_note:"
						await song.edit(content = str(out))
					else:
						if ":" in line:
							linenumbers = line.split(":")
							timestamp = (int(linenumbers[0]) * 60) + float(linenumbers[1])
						else:
							timestamp = float(line.rstrip())
						await asyncio.sleep(timestamp - lasttimestamp)
						lasttimestamp = float(line)
		except Exception as e:
			print(warn("{0}.blf does not exist.".format(title)))
			await song.edit(content = "**{0}.blf not found!** If this is a song you'd want, or you think this is a bug, report it with `{1}report [message]`\n`{2}`".format(title, prefix, e))

	@commands.command()
	async def gh(self, ctx, dir, *, notes):
		lefty = "l" in dir.lower()
		print(msg("User {0} made the chart \"{1}\", Lefty = {2}.".format(ctx.message.author.name, notes, lefty)))
		notelist = notes.split()
		dir = dir.upper()
		chartlist = []
		if "l" in dir.lower():
			for s in notelist:
				chartlist.append(ghline(True, s))
		else:
			for s in notelist:
				chartlist.append(ghline(False, s))
		if "d" not in dir.lower(): chartlist.reverse()
		finishedstring = "*Chart by <@{0}>.*".format(ctx.message.author.id) + newline
		if "d" not in dir.lower():
			finishedstring = finishedstring + "*(Chart is read bottom-to-top, like Guitar Hero.)*" + newline
		else:
			finishedstring = finishedstring + "*(Chart is read top-to-bottom, like Discord.)*" + newline
		for item in chartlist:
			finishedstring = finishedstring + item + newline
		if len(finishedstring) >= 2000:
			await ctx.send("Chart too long to output to Discord.")
		else:
			await ctx.send(finishedstring)

	@commands.command()
	async def image(self, ctx, *, img):
		imagesent = False
		print(msg("User {0} requested the image \"{1}\".".format(ctx.message.author.name, img)))
		print(msg("Deleting user {0}'s command message.".format(ctx.message.author.name)))
		await ctx.message.delete()
		path = "imagecommand"
		for filename in os.listdir(path):
			if re.match("{0}\.\w+".format(img), filename):
				print(time() + load("Loaded {0}.".format(filename)))
				await ctx.send(" ", file=discord.File(path + "/" + filename, '{0}.jpg'.format(img)))
				imagesent = True
		if imagesent == False:
			print(warn("Loaded {0}.".format(filename)))
			await ctx.send("Image \"{0}\" does not exist.".format(img))

	@commands.command()
	async def morse(self, ctx, subcommand, *, string):
		if subcommand == "e" or subcommand == "encode":
			print(msg("User {0} requested morse encoding of the string \"{1}\".".format(ctx.message.author.name, string)))
			response = requests.get("http://www.morsecode-api.de/encode?string={0}".format(string))
			dict = json.loads(response.content.decode("utf-8"))
			out = dict['morsecode']
			out = out.replace('?', '')
			out = out.replace('.......', '/')
			await ctx.message.delete()
			await ctx.send("{0} said this in ASCII to Morse:\n`{1}`".format(ctx.message.author.name,out))
		elif subcommand == "eb" or subcommand == "encodebinary":
			print(msg("User {0} requested binarymorse encoding of the string \"{1}\".".format(ctx.message.author.name, string)))
			response = requests.get("http://www.morsecode-api.de/encode?string={0}".format(string))
			dict = json.loads(response.content.decode("utf-8"))
			out = dict['morsecode']
			out = out.replace('?', '')
			out = out.replace('.......', '11111110')
			out = out.replace('.', '10')
			out = out.replace('-', '1110')
			out = out.replace(' ', '')
			await ctx.message.delete()
			await ctx.send("{0} said this in ASCII to Binary Morse:\n`{1}`".format(ctx.message.author.name,out))
		elif subcommand == "d" or subcommand == "decode":
			print(msg("User {0} requested morse encoding of the string \"{1}\".".format(ctx.message.author.name, string)))
			string = string.replace("/", ".......")
			response = requests.get("http://www.morsecode-api.de/decode?string={0}".format(string))
			dict = json.loads(response.content.decode("utf-8"))
			out = dict['plaintext']
			await ctx.message.delete()
			await ctx.send("{0} said this in Morse to ASCII:\n`{1}`".format(ctx.message.author.name,out))
		else:
			await ctx.send("Incorrect subcommand.", delete_after=5)

	@commands.command()
	async def dpnsync(self, ctx, subcommand = None, *, string):
		os.system("curl https://docs.google.com/spreadsheets/d/e/2PACX-1vS_OORJ_wr6XFRIpLe_Oa9KhGPMQSZdZy0Cas0Yp_mCaAYiJpgLs_90iymKynd6twuYKPLGIj2CVvo6/pub?output=csv >> dpnsync.txt")
		with open("dpnsync.txt", encoding = "utf-8") as dpnfile:
				dpncsv = csv.reader(dpnfile)
				for row in dpncsv:
					print((row[0]))
					#print((row[0]).encode(sys.stdout.encoding, errors='replace'))
		#if subcommand == "search":

#Necessary.
def setup(bot):
	bot.add_cog(FunCog(bot))
