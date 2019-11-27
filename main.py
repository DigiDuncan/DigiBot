from digiglobal import *

launch = datetime.datetime.now()

# Get authtoken from file.
with open("_authtoken.txt") as f:
    authtoken = f.readlines()
authtoken = [x.strip() for x in authtoken]
authtoken = authtoken[0]

# Predefined variables.
prefix = '$'
description = '''A Discord bot with many unrelated functions. A personal coding project.'''
initial_extensions = ['cogs.main',
                    'cogs.quote',
                    'cogs.eastereggs']

bot = commands.Bot(command_prefix=prefix, description=description)
#bot.remove_command("help")

@bot.event
# Output header.
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name="Just Monika."))
    df.warn("Warn test.")
    df.crit("Crit test.")
    df.test("Test test.")
    finishlaunch = datetime.datetime.now()
    elapsed = finishlaunch - launch
    df.test(f"DigiBot launched in {round((elapsed.total_seconds() * 1000), 3)} milliseconds.")
    print()


@bot.event
async def on_message(message):
    if message.content.startswith("$") and message.content.endswith("$"): return #Ignore Tupperboxes being mistaken for commands.
    #if not message.content.startswith(allowbrackets): message.content = removebrackets(message.content)
    await bot.process_commands(message)

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        # try:
        bot.load_extension(extension)


bot.run(authtoken)
