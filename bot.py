#Import libraries

import os
import datetime
import time
import random
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks
from discord.utils import get

#Initialise token from env variable

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Set intents

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='~',intents=intents)

#Other initialisation stuff

startTime = str(datetime.datetime.now())[0:16] #Set restart time

petsfilepath = here = os.path.dirname(os.path.abspath(__file__)) #Find current location
petsfiledir = os.path.join(here, 'pets.txt') #Find petting file location

cooldown = {'annoy': 0} #Cooldown dictionary

global delIgnore #Message deletion ignore

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Grilling some cobs')) #Discord presence
    print(f'{bot.user.name} is now ready') #Console ready

@bot.event
async def on_connect():
    print(f'{bot.user.name} has connected to Discord') #Console connected

@bot.event
async def on_message(message):
    await bot.process_commands(message) #Process commands
    
    if message.author.id != 742641971973324891 and message.author.id != 743436583625162813 and message.content.startswith('~') != True: #Check if not Bot, BotDev or command
        messageLower = message.content.lower() #Lowercase message for processing
        if 'corn' in messageLower:
            await message.channel.send(f'I HAVE BEEN SUMMONED BY {message.author.name.upper()}') #Say stuff if corn is said

@bot.event
async def on_message_delete(message):
    if message.author.id != 742641971973324891 and message.author.id != 743436583625162813 and message.id != delIgnore: #Check if Bot, BotDev or message deletion has been marked to ignore
        await message.channel.send(message.author.name + "'s message that was just deleted said: " + message.content) #Say deleted message with message author

@bot.command(name='drink', help='take a drink from somewhere', aliases=('thirst','slurp'))
async def drink(ctx):

    #Drinking actions
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
    
    #Drinking locations
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

    response = random.choice(actions) + ' ' + random.choice(places) #Choose random action and location
    await ctx.send(response)

@bot.command(name='corn', help='corn')
async def corn(ctx, number=1):
    if number > 150: #Cap at 150
        number = 150
    response = ''
    for i in range(0,number): #Send many corns
        response += ':corn:'
    msg = await ctx.send(response)
    await msg.add_reaction('🌽') #React with corn

@bot.command(name='uptime', help='see when the bot last restarted', aliases=('starttime','restarttime'))
async def uptime(ctx):
    await ctx.send('Last restarted at: ' + startTime)

@bot.command(name='dice', help='roll some dice', aliases=('chance','die'))
async def dice(ctx, sides=6, num=1):
    result = 1

    if num > 100:
        await ctx.send('You rolled too many dice and lost them all!') #Limit on dice
        return

    if sides > 1000:
        await ctx.send('Your dice had too many sides and created a tear in space time!') #Limit on sides
        return

    for i in range(0,num):
        result += random.choice(range(1,sides)) #Generate random
    
    if num == 1: #Correct grammar
        prefix = 'You rolled a '
    else:
        prefix = 'You rolled a total of '
    
    await ctx.send(prefix + str(result)) #Send
  
@bot.command(name='magic', help='bippity boppity boo', aliases=('bippity','alakazam','shazam'))
async def magic(ctx):
    poof = await ctx.send(':cloud: poof :cloud:') #Send

@bot.command(name='pet', help='pet the boi', aliases=('pat','bonk'))
async def pet(ctx):
    petsfile = open(petsfiledir, 'r') #Read file
    pets = petsfile.read()
    petsfile.close()
    pets = int(pets) #Turn into int
    pets += 1
    petsfile = open(petsfiledir, 'w') #Write new to file
    petsfile.write(str(pets))
    petsfile.close()
    await ctx.send('The boi has been petted ' + str(pets) + ' times') #Send message

@bot.command(name='annoy', help='annoy someone', aliases=('ping','@','bruh'))
async def annoy(ctx):
    if (time.time() - cooldown['annoy']) > 600: #Cooldown control
        ping = await ctx.send('<@' + str(ctx.guild.members[random.choice(range(0,len(ctx.guild.members)))].id) + '>') #Mention
        await ping.delete() #Delete message
        global delIgnore
        delIgnore = ctx.message.id #Mark original command for unnoticed deletion
        await ctx.message.delete() #Delete original command
        cooldown['annoy'] = time.time() #Reset cooldown
    else:
        await ctx.send("You can't ping anyone for another " + str(600 - round((time.time() - cooldown['annoy']))) + ' seconds') #Cooldown message

bot.run(TOKEN)