import discord
from discord.ext import commands
import digiformatter as df
from digiglobal import *

class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, *, message: str):
        await ctx.message.delete()
        if ctx.message.author.id == digiid:
            await ctx.send(message)

    @commands.command()
    async def sing(self, ctx, *, string: str):
        await ctx.message.delete()
        newstring = ":musical_score: *" + string + "* :musical_note:"
        await ctx.send(newstring)

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
        df.msg("User {0} rolled {1} {2}-sided dice and dropped {3}.".format(ctx.message.author.name, dNum, dSides, dDrops))
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
        df.msg("User {0} rolled {1} {3}{4} for a total of {2}".format(ctx.message.author.name, str(usedrolls), str(dTotal), printModType, printMod))
        await ctx.send("{0} rolled {1} {4}{5} and got {2}!\nDice: {3} {4}{5}".format(ctx.message.author.name, dString, str(dTotal), str(usedrolls), printModType, printMod))

    @commands.command()
    async def emojify(self, ctx, *, string):
        df.msg("User {0} requested emojification of the string \"{1}\".".format(ctx.message.author.name, string))
        emojistring = ""
        if string == "$test":
            df.msg("Sending test message.")
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
            df.msg("User {0} requested an emojified string too long for Discord.".format(ctx.message.author.id))
            await ctx.send("<@{0}>, Emojified string too long for Discord.".format(ctx.message.author.id), delete_after=5)
        else:
            await ctx.send(emojistring)

# Necessary.
def setup(bot):
    bot.add_cog(MainCog(bot))
