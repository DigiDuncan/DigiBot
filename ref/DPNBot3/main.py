import discord
from discord.ext import commands
import re
import datetime
import sys
import os
import time
from datetime import date
from datetime import *
import math
import random
from decimal import *
from colored import fore, back, style, fg, bg, attr
from pathlib import Path
import string
import traceback
from discord.ext import commands
from math import *
import asyncio
import codecs

from globaldpn import *

#Get authtoken from file.
with open("_authtoken.txt") as f:
	authtoken = f.readlines()
authtoken = [x.strip() for x in authtoken]
authtoken = authtoken[0]

#Predefined variables.
prefix = '&'
description = '''DPNBot3 is pretty dumb!'''
initial_extensions = ['cogs.commands', 'cogs.quotes', 'cogs.fun']

#Obviously we need this printed in the terminal.
print(ascii)

bot = commands.Bot(command_prefix=prefix, description=description)
bot.remove_command("help")

@bot.event
#Output header.
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	await bot.change_presence(activity=discord.Game(name="Doki Doki Literature Club"))

@bot.event
async def on_message(message):
	#Easter egg.
	if "monika" in message.content.lower():
		print("Monika detected.")
		if random.randrange(10) == 7:
			print("Monika triggered.")
			await message.channel.send(monikaline() + "<:monika:488162370154266645>"
				,delete_after=5)

	await bot.process_commands(message)

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
	for extension in initial_extensions:
		#try:
		bot.load_extension(extension)


bot.run(authtoken)
