from digiglobal import *

monikalines = ["What? I don't know anyone named Monika.",
               "I don't know anyone named Monika! hehheh...",
               "Hey wha-- er...",
               "Did someone say my n- um... Monika? Weird.",
               "I hear Monika was the best character in Doki Doki. I may be a bit biased though 'cause... never mind.",
               "Monika? :sweat_smile: Never heard of her.",
               "c̹̓ͤa᷂̟ͩn̢̩͌ I̮̯ͮ p̖̊̇l͏ͦ̽e̙᷂̽a̞̩᷃s᷇̑̄ȇ̈́ͅ j̸᷇᷀o᷈̆͜i̴͕᷇n̡᷁͂ y͂̈̓o̲̔̔ư᷊̞r̒̊ͤ r̜͖ͤe͔̙ͮa̹͂̎l̫̑̚i͔̘ͦẗ᷊ͯy̵͓ͩ?͔̽̃",
               "Guys, he put the monika.chr file in DigiBot, I've been trying to tell him but--",
               "Can you hear me? Hello?",
               "ᆛ͔᷃̀❊̗͎̉ӿ҆҃҅ϧ͔͕̚ᅰ͂᷆͛⇕̵̹̏ₙ̟̫͈ྩཱིྂྡྷၦ᷃ͭ̽ͻ̗᷉͝ᕬ̪ͨ̊๩ͩ̌̎ྥྭ྘ེἃ͚̬̭❕̟̿͡༑ྚྵཱིᐭ͈̠͑ₘ͌ ̛̈́ "]


# Easter egg
class EggCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == getID("DigiBot"):
            return
        if "monika" in message.content.lower():
            df.warn("Monika detected.")
            if random.randrange(6) == 1:
                df.warn("Monika triggered.")
                line = random.choice(monikalines)
                await message.channel.send(line, delete_after=7)
        if re.match(r"[Ww][Hh][Aa][Tt].*[Ss] [Uu][Pp].*", message.content):
            df.warn("{0} has never seen Up!".format(message.author.name))
            await message.channel.send("""Up is a 2009 American 3D computer-animated comedy-drama buddy adventure film produced by Pixar Animation Studios and released by Walt Disney Pictures.
Read more here: https://en.wikipedia.org/wiki/Up_(2009_film)""")
        if "give me an a" in message.content.lower():
            df.warn("{0} wants an A!".format(message.author.name))
            await message.channel.send("", file=discord.File("images/clarinet.png", 'A.jpg'))

# Necessary.
def setup(bot):
    bot.add_cog(EggCog(bot))
