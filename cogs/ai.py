from digiglobal import *
from textgenrnn import textgenrnn

class AICog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fakequote(self, ctx):
        newmessage = yield await ctx.send("Generating...")
        textgen.train_from_file('quotes.txt')
        newquote = textgen.generate(1, temperature=1.0)
        newmessage.edit(newquote)
# Necessary.
def setup(bot):
    bot.add_cog(AICog(bot))
