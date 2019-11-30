from digiglobal import *

class WiiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def getAttribute(soup, attr):
        lookup = soup.find("table", class_="GameData").find("td", string=attr)
        if lookup == None: lookup = soup.find("table", class_="GameData").find("td", string=attr + newline)
        if lookup == None:
            return ""
        returnattr = lookup.next_sibling
        if returnattr == None: return ""

        attrstring = str(returnattr).replace(newline, "")
        if re.search(">(.*?)<", attrstring) != None: return re.search(">(.*?)<", attrstring).group(1)
        return ""

    def getAttributes(GAMEID):
        response = requests.get(f"https://www.gametdb.com/Wii/{GAMEID}", headers=hdr)
        imageresponse = requests.get(f"https://art.gametdb.com/wii/cover/US/{GAMEID}.png", headers=hdr, stream=True)
        soup = BeautifulSoup(response.content, "html.parser")

        attrdict = {}
        attrdict['ID'] = GAMEID
        attrdict['name'] = getAttribute(soup, "title (EN)")
        if attrdict['name'] == "": attrdict['name'] = getAttribute(soup, "title (JP)")
        attrdict['region'] = getAttribute(soup, "region")
        attrdict['type'] = getAttribute(soup, "type")
        attrdict['region'] = getAttribute(soup, "region")
        attrdict['languages'] = getAttribute(soup, "languages")
        attrdict['synopsis'] = getAttribute(soup, "synopsis (EN)")
        if attrdict['synopsis'] == "": attrdict['synopsis'] = getAttribute(soup, "synopsis (JP)")
        attrdict['developer'] = getAttribute(soup, "developer")
        attrdict['publisher'] = getAttribute(soup, "publisher")
        attrdict['date'] = getAttribute(soup, "release date")
        attrdict['genre'] = getAttribute(soup, "genre")
        attrdict['rating'] = getAttribute(soup, "rating")
        attrdict['cover'] = imageresponse.raw #This is an image in a file-type object.

        return attrdict

    wiidictionary = {}
    with io.open("text/wiitdb.txt", encoding="utf-8") as wiidb:
        lines = wiidb.readlines()
        for line in lines:
            splitline = line.split(" = ")
            wiidictionary[splitline[0]] = splitline[1].strip()


    @commands.command()
    async def wiisearch(self, ctx, searchterm, flags = None):
        if searchterm.upper() in wiidictionary.keys():
            #The searchterm is a Game ID.
            #TEMP CODE.
            message = ""
            for item in getAttributes(searchterm.upper()).items():
                message += (item[0] + " : " + item[1] + newline)
                await ctx.send(message)
        else:
            #Use a searching tool to find relevant suggestions, then use the most revelant one,
            #favoring NTSC-U games, then PAL games with a EN language, then JPN games.
            pass

# Necessary.
def setup(bot):
    bot.add_cog(WiiCog(bot))
