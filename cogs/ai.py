from digiglobal import *

class AICog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    textgen = textgenrnn()
    textgen.load("text/weights.hdf5")

    @commands.command()
    async def fakequote(self, ctx, temp = 0.5):
        newmessage = await ctx.send(loadingemoji + " Generating...")
        newquote = self.textgen.generate(1, temperature = temp, return_as_list = True)[0]
        await newmessage.edit(content = newquote)

    @commands.command()
    async def aitrain(self, ctx, epochs = 5):
        self.textgen.train_from_file('text/quotes.txt', num_epochs=epochs)
        self.textgen.save(weights_path="text/weights.hdf5")

# Necessary.
def setup(bot):
    bot.add_cog(AICog(bot))
