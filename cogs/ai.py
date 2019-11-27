from digiglobal import *

class AICog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fakequote(self, ctx):
        pass

# Necessary.
def setup(bot):
    bot.add_cog(AICog(bot))
