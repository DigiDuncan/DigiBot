from digiglobal import *

class WiiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wiisearch(self, ctx, searchterm, flags = None):
        df.msg(f"{ctx.message.author.name} requested a WiiSearch on the term \"{searchterm}\".")
        initialmessage = await ctx.send(f"{loadingemoji} Processing {ctx.message.author.name}'s Wii search...")
        if searchterm.upper() in wiidictionary.keys():
            #The searchterm is a Game ID.
            #TODO: Make into an embed.
            gameid = searchterm.upper()
            message = "**" + getWiiAttributes(gameid)["name"] + "**" + newline
            for item in getWiiAttributes(gameid).items():
                if item[0] != "cover" and item[0] != "name": message += (item[0] + " : " + item[1] + newline)
            imgurl = getWiiAttributes(gameid)["cover"]
            imgresponse = requests.get(imgurl, stream=True)
            with open(f"temp/{searchterm}.png", "wb") as out_file:
                shutil.copyfileobj(imgresponse.raw, out_file)
            initialmessage.delete()
            await ctx.send(message, file=discord.File(f"temp/{searchterm}.png", "f{gameid}.png"))
        #else:
            #Use a searching tool to find relevant suggestions, then use the most revelant one,
            #favoring NTSC-U games, then PAL games with a EN language, then JPN games.

# Necessary.
def setup(bot):
    bot.add_cog(WiiCog(bot))
