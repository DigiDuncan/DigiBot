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
            #Format the game ID.
            gameid = searchterm.upper()
            #Get the attributes of the game based on its ID.
            gameattrs = getWiiAttributes(gameid)

            #Build the embed.
            embed = discord.Embed(title = f"{gameattrs['name']} [{gameid}]", description = gameattrs["synopsis"], color = gameattrs["color"])
            embed.set_author(name = f"{self.bot.user.name} - {prefix}wiisearch", icon_url = gameattrs["icon"])
            embed.set_footer(text = ctx.message.author.name, icon_url = ctx.message.author.avatar_url)
            embed.set_image(url = gameattrs["cover"])
            embed.set_thumbnail(url = gametdblogo)
            embed.add_field(name = "Console", value = gameattrs["type"], inline = True)
            embed.add_field(name = "Region", value = gameattrs["region"])
            embed.add_field(name = "Languages", value = gameattrs["languages"])
            embed.add_field(name = "Developer", value = gameattrs["developer"])
            embed.add_field(name = "Publisher", value = gameattrs["publisher"])
            embed.add_field(name = "Genre", value = gameattrs["genre"])
            embed.add_field(name = "ESRB/PEGI Rating", value = gameattrs["rating"])
            embed.add_field(name = "Release Date", value = gameattrs["date"])

            #Delete the loading message.
            await initialmessage.delete()
            #Send the embed.
            await ctx.send(f"<@{ctx.message.author.id}>", embed = embed)


        else:
        #TEMP
            ctx.send("The game `{searchterm.upper()}` was not found in the database.")

        #else:
        #The searchterm is a search term. :P
            #Use a searching tool to find relevant suggestions, then use the most revelant one,
            #favoring NTSC-U games, then PAL games with a EN language, then JPN games.

# Necessary.
def setup(bot):
    bot.add_cog(WiiCog(bot))
