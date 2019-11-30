from digiglobal import *

class WiiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wiisearch(self, ctx):
        pass

# Necessary.
def setup(bot):
    bot.add_cog(AICog(bot))
