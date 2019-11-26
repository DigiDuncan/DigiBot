import discord
from discord.ext import commands
import digiformatter as df

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

# Necessary.
def setup(bot):
    bot.add_cog(MainCog(bot))
