from digiglobal import *

class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, *, message: str):
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command()
    async def sing(self, ctx, *, string: str):
        await ctx.message.delete()
        newstring = ":musical_score: *" + string + "* :musical_note:"
        await ctx.send(newstring)

    @commands.command()
    async def roll(self, ctx, dString):
        rolls = []
        usedrolls = []
        dSides = 0
        dNum = 0
        dDrops = 0
        dTotal = 0
        stop = False
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
        if dSides > 1000000:
            await ctx.send('Too many sides!')
            df.warn(f"{ctx.message.author.id} ({ctx.message.author.nick}) tried to roll a {dSides}-sided die!")
            stop = True
        if dNum > 250:
            await ctx.send('Too many dice!')
            df.warn(f"{ctx.message.author.id} ({ctx.message.author.nick}) tried to roll {dNum} dice!")
            stop = True
        if stop: return
        for x in range(dNum):
            currentRoll = (random.randrange(1, dSides + 1))
            rolls.append(currentRoll)
        rolls.sort(key=int)
        for x in range(dDrops, len(rolls)):
            dTotal = dTotal + rolls[x]
            usedrolls.append(rolls[x])
        dropped = rolls
        for item in usedrolls: dropped.remove(item)
        sendstring = "{0} rolled {1} and got {2}!\nDice: {3}".format(ctx.message.author.nick, dString, str(dTotal), str(usedrolls))
        if dropped != []: sendstring = sendstring + "\n~~Dropped: {0}~~".format(str(dropped))
        df.msg(f"{ctx.message.author.id} ({ctx.message.author.nick}) rolled {dString}.")
        await ctx.send(sendstring)

    @commands.command()
    async def emojify(self, ctx, *, string):
        df.msg("User {0} requested emojification of the string \"{1}\".".format(ctx.message.author.name, string))
        emojistring = ""
        if string == "$test":
            df.msg("Sending test message.")
            string = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789 .,!?,*#*'‽+-=<>^¥€£"
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
            messagelist = []
            emojilist = []
            currentmessage = ""
            currentemoji = ""
            currentcolon = 0
            for char in emojistring:
                currentemoji += char
                if char == ":": currentcolon += 1
                if currentcolon % 2 == 0 and currentcolon != 0:
                    emojilist.append(currentemoji)
                    currentemoji = ""
            for emoji in emojilist:
                if len(currentmessage + emoji) > 2000:
                    messagelist.append(currentmessage)
                    currentmessage = ""
                currentmessage += emoji
            for message in messagelist:
                await ctx.send(message)
                await asyncio.sleep(1)
            #df.msg("User {0} requested an emojified string too long for Discord.".format(ctx.message.author.id))
            #await ctx.send("<@{0}>, Emojified string too long for Discord.".format(ctx.message.author.id), delete_after=5)
        else:
            await ctx.send(emojistring)

    @commands.command()
    async def digipee(self, ctx):
        await ctx.send(f"DigiDuncan also has to pee.")
        df.msg("DigiDuncan also has to pee.")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("!digipee"):
            cont = await self.bot.get_context(message)
            await cont.invoke(self.bot.get_command("digipee"))
# Necessary.
def setup(bot):
    bot.add_cog(MainCog(bot))
