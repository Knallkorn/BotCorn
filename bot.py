import os
import datetime
import time
import random
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks
from discord.utils import get

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='~',intents=intents)

startTime = str(datetime.datetime.now())[0:16]

petsfilepath = here = os.path.dirname(os.path.abspath(__file__))
petsfiledir = os.path.join(here, 'pets.txt')

cooldown = {'annoy': 0}

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
              'the stomach of a small child',
              'an as-of-yet unknown star system inhabited by phallic aliens',
              'a watermelon',
              'a fondue fountain filled with urine',
              'a barrel filled with nuclear waste']

    response = random.choice(actions) + ' ' + random.choice(places)
    await ctx.send(response)

@bot.command(name='corn', help='corn')
async def corn(ctx, number=1):
    if number > 150:
        number = 150
    response = ''
    for i in range(0,number):
        response += ':corn:'
    msg = await ctx.send(response)
    await msg.add_reaction('🌽')

@bot.command(name='uptime', help='see when the bot last restarted', aliases=('starttime','restarttime'))
async def uptime(ctx):
    await ctx.send('Last restarted at: ' + startTime)

@bot.command(name='dice', help='roll some dice', aliases=('chance','die'))
async def dice(ctx, sides=6, num=1):
    result = 1

    if num > 100:
        await ctx.send('You rolled too many dice and lost them all!')
        return

    if sides > 1000:
        await ctx.send('Your dice had too many sides and created a tear in space time!')
        return

    for i in range(0,num):
        result += random.choice(range(1,sides))
    
    if num == 1:
        prefix = 'You rolled a '
    else:
        prefix = 'You rolled a total of '
    
    await ctx.send(prefix + str(result))
  
@bot.command(name='magic', help='bippity boppity boo', aliases=('bippity','alakazam','shazam'))
async def magic(ctx):
    await ctx.send(':cloud: poof :cloud:')

@bot.command(name='pet', help='pet the boi', aliases=('pat','bonk'))
async def pet(ctx):
    petsfile = open(petsfiledir, 'r')
    pets = petsfile.read()
    petsfile.close()
    pets = int(pets)
    pets += 1
    petsfile = open(petsfiledir, 'w')
    petsfile.write(str(pets))
    petsfile.close()
    await ctx.send('The boi has been petted ' + str(pets) + ' times') 

@bot.command(name='annoy', help='annoy someone', aliases=('ping','@','bruh'))
async def annoy(ctx):
    if (time.time() - cooldown['annoy']) > 600:
        curGuild = ctx.guild.id
        ping = await ctx.send('<@' + str(ctx.guild.members[random.choice(range(0,len(ctx.guild.members)))].id) + '>')
        ping_id = ping.id
        await ping.delete()
        cooldown['annoy'] = time.time()
    else:
        await ctx.send("You can't ping anyone for another " + str(600 - round((time.time() - cooldown['annoy']))) + ' seconds')

bot.run(TOKEN)