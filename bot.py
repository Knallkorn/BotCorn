import os
import datetime
import random
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='~')

startTime = str(datetime.datetime.now())[0:16]

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Grilling some cobs'))
    print(f'{bot.user.name} has connected to Discord')

@bot.command(name='drink', help='take a drink from somewhere', aliases=('thirst','slurp'))
async def drink(ctx):

    actions = ['You take a drink from',
               'You down a gallon from',
               'You viscously inhale an inexplicable amount from',
               'You tentatively take a sip from',
               'You drown yourself in',
               'You lick a small portion from',
               'You nearly die by drinking so much from',
               'You gulp down some liquid from',
               'You swallow a capacity equal to a bathtub from',
               'You quaff an unsolicited amount from',
               'You take a swig from',
               'You consume the daily intake of an adult midget from',
               'You absorb the surrounding molecules from']
    
    places = ['the YandereDev chalice',
              'a glass of water from Flint, Michagan',
              'a deep sea brine pool',
              'some tap water',
              'the dead sea',
              'the toilet',
              'the sewers',
              'an inexplicably banana-shaped mug',
              'the corpse of a blue whale',
              'a used condom',
              'an inflatable pool filled with spinal fluid',
              'an alternate universe where Canada and the Bahamas switched places in 86 BCE',
              'a thick anime waifu',
              "the dank corner of a sex offender's crack den",
              'a the stomach of a small child',
              'an as-of-yet unknown star system inhabited by phallic aliens',
              'a watermelon',
              'a fondue fountain filled with urine',
              'a barrel filled with nuclear waste']

    response = random.choice(actions) + ' ' + random.choice(places)
    await ctx.send(response)

@bot.command(name='corn', help='corn')
async def corn(ctx, number=1):
    if number > 100:
        number = 100
    response = ''
    for i in range(0,number):
        response += ':corn:'
    msg = await ctx.send(response)
    await msg.add_reaction('🌽')

@bot.command(name='uptime', help='see when the bot last restarted', aliases=('starttime','restarttime'))
async def uptime(ctx):
    await ctx.send(startTime)

@bot.command(name='dice', help='roll some dice', aliases=('chance','die'))
async def dice(ctx, sides=6, num=1):
    result = 0

    if num > 100:
        await ctx.send('You rolled too many dice and lost them all!')
        return

    if sides > 1000:
        await ctx.send('Your dice had too many sides and created a tear in space time!')
        return

    for i in range(0,num):
        result += random.choice(range(0,sides))
    
    if num == 1:
        prefix = 'You rolled a '
    else:
        prefix = 'You rolled a total of '
    
    await ctx.send(prefix + str(result))
    
@bot.command(name='pog', help='poggers!', aliases=('pogchamp','poggers'))
async def pog(ctx):
    pog = [ #I put this in a dictionary so I could close it
        '⠄⠄⠄⠄⠄⠄⣀⣀⣀⣤⣶⣿⣿⣶⣶⣶⣤⣄⣠⣴⣶⣿⣿⣿⣿⣶⣦⣄⠄⠄ ⠄⠄⣠⣴⣾⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦ ⢠⠾⣋⣭⣄⡀⠄⠄⠈⠙⠻⣿⣿⡿⠛⠋⠉⠉⠉⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿ ⡎⣾⡟⢻⣿⣷⠄⠄⠄⠄⠄⡼⣡⣾⣿⣿⣦⠄⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⣿⣿ ⡇⢿⣷⣾⣿⠟⠄⠄⠄⠄⢰⠁⣿⣇⣸⣿⣿⠄⠄⠄⠄⠄⠄⠄⣠⣼⣿⣿⣿⣿ ⢸⣦⣭⣭⣄⣤⣤⣤⣴⣶⣿⣧⡘⠻⠛⠛⠁⠄⠄⠄⠄⣀⣴⣿⣿⣿⣿⣿⣿⣿ ⠄⢉⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⢰⡿⠛⠛⠛⠛⠻⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⠸⡇⠄⠄⢀⣀⣀⠄⠄⠄⠄⠄⠉⠉⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⠄⠈⣆⠄⠄⢿⣿⣿⣿⣷⣶⣶⣤⣤⣀⣀⡀⠄⠄⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⠄⠄⣿⡀⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠄⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⠄⠄⣿⡇⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⠄⠄⣿⡇⠄⠠⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⠄⠄⣿⠁⠄⠐⠛⠛⠛⠛⠉⠉⠉⠉⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿ ⠄⠄⠻⣦⣀⣀⣀⣀⣀⣀⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄'
          ]
    await ctx.send(pog[0])

bot.run(TOKEN)