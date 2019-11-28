from digiglobal import *

class QuoteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quote(self, ctx, *, commandstring : str):
        #"Add" subcommand.
        if commandstring.startswith("add "):
            quotetoadd = commandstring[4:].replace("\n", ";")
            with io.open("quotes.txt", "a", encoding="utf-8") as quotefile:
                quotefile.write(quotetoadd + newline)
            with io.open("quotes.txt", "r", encoding="utf-8") as quotefile:
                quoteslist = quotefile.readlines()
            quoteslist = [x.strip() for x in quoteslist]
            await ctx.send(f"""***Quote added***:
{quotetoadd}""")
            await bot.get_channel('560143208311422976').send(f"***Quote {len(quoteslist)}:*** {quotetoadd}".replace(";", "\n"))
            df.msg(f"{ctx.message.author.name} added quote {len(quoteslist)}:\n{quotetoadd}")
        if commandstring.startswith("random") or commandstring == "":
            with io.open("quotes.txt", encoding="utf-8") as quotefile:
                quoteslist = quotefile.readlines()
            quoteslist = [x.strip() for x in quoteslist]
            quoteid = random.randrange(len(quoteslist))
            printquote = quoteslist[quoteid]
            printquote = printquote.replace(";", "\n")
            await ctx.send(f"""***Random Quote {quoteid}:***
{printquote}""")
            df.msg(f"{ctx.message.author.name} printed a random quote {quoteid}.")
        #Print a quote.
        else:
            with io.open("quotes.txt", encoding="utf-8") as quotefile:
                quoteslist = quotefile.readlines()
            quoteslist = [x.strip() for x in quoteslist]
            quoteid = int(commandstring)
            if quoteid < 1:
                await ctx.send("Quote ID cannot be less than 1.")
                df.warn(f"{ctx.message.author.name} tried to print quote {quoteid}, but it's less than 1.")
                return
            if quoteid > len(quoteslist):
                await ctx.send(f"Quote ID cannot be higher than the most recent quote (Quote {len(quoteslist)}).")
                df.warn(f"{ctx.message.author.name} tried to print quote {quoteid}, but it's higher than the max ID.")
                return
            printquote = quoteslist[quoteid - 1]
            printquote = printquote.replace(";", "\n")
            await ctx.send(f"""***Quote {quoteid}:***
{printquote}""")
            df.msg(f"{ctx.message.author.name} printed quote {quoteid}.")

    @commands.command()
    async def allquotes(self, ctx):
        if ctx.message.author.id in getID("DigiDuncan", "AWK", "DigiBot"):
            with io.open("quotes.txt", "r", encoding="utf-8") as quotefile:
                quoteslist = quotefile.readlines()
            quoteslist = [x.strip() for x in quoteslist]
            quotenum = 0
            for quote in quoteslist:
                quotenum += 1
                await ctx.send(f"***Quote {quotenum}:*** {quote}".replace(";", "\n"))
        else:
            await ctx.send("You are not allowed to use this command.")
            df.warn(f"{ctx.message.author.name} tried to print all quotes, but they are forbidden!")

# Necessary.
def setup(bot):
    bot.add_cog(QuoteCog(bot))
