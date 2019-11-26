import discord
from discord.ext import commands
import os
from colored import *
from globalWIP import *
import requests
import random
import re

#Enable colors in terminal for Windows.
os.system("")

#Indicate loading.
print(load("main.py loaded."))

#Get authtoken from file.

with open("../_authtoken.txt") as f:
    authtoken = f.readlines()
authtoken = [x.strip() for x in authtoken]
authtoken = authtoken[0]

#Predefined variables.
description = '''WIPBot is written by DigiDuncan.'''
initial_extensions = ['cogs.fun', 'cogs.help']

bot = commands.Bot(command_prefix=prefix, description=description)
bot.remove_command("help")

@bot.event
#Output header.
async def on_ready():
    print(fore.CYAN + 'Logged in as')
    print(bot.user.name)
    print(version)
    print(bot.user.id)
    print('------' + style.RESET)
    await bot.change_presence(activity=discord.Game(name="Doki Doki Panic Club"))
    print(load("Load test."))
    print(time() + "Time test.")
    print(msg("Msg test."))
    print(warn("Warn test."))
    print(crit("Crit test."))
    print(test("Test test."))
    print(fore.CYAN + '------' + style.RESET)
    #Obviously we need this printed in the terminal.
    print(bg(24) + fg(202) + style.BOLD +ascii + style.RESET)

@bot.event
async def on_message(message):
    #Easter eggs.
    if message.author.id != bot_id:
        if "monika" in message.content.lower():
            randomchance = random.randrange(10)
            print(warn("Monika detected. ({0}) [{1}]".format(message.author.name, randomchance)))
            if randomchance == 7:
                print(warn("Monika triggered. ({0})".format(message.author.name)))
                await message.channel.send(monikaline() + "<:monika:495819371772641280>"
                    ,delete_after=5)
        if "computer" in message.content.lower():
            randomchance = random.randrange(10)
            print(warn("Computer detected. ({0}) [{1}]".format(message.author.name, randomchance)))
            if randomchance == 7:
                print(warn("{0} doesn't know what a computer is.".format(message.author.name)))
                await message.channel.send("What's a computer?", file=discord.File("images/whatsacomputer.jpg", 'wac.jpg'))
        if message.content.lower().startswith("aaaaaa"):
            print(warn("{0} is ANGERY.".format(message.author.name)))
            await message.channel.send("", file=discord.File("images/dokiaaa.jpg", 'dokiaaa.jpg'))
        if re.match(r"[Ww][Hh][Aa][Tt].*[Ss] [Uu][Pp].*", message.content):
            print(warn("{0} has never seen Up!".format(message.author.name)))
            await message.channel.send("""Up is a 2009 American 3D computer-animated comedy-drama buddy adventure film produced by Pixar Animation Studios and released by Walt Disney Pictures.
Read more here: https://en.wikipedia.org/wiki/Up_(2009_film)""")
        if "give me an a" in message.content.lower():
            await message.channel.send("", file=discord.File("images/clarinet.png", 'A.jpg'))
    await bot.process_commands(message)



# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        #try:
        bot.load_extension(extension)

bot.run(authtoken)
