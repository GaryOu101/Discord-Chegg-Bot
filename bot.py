import discord
from discord import member, channel
from pynput.keyboard import Key, Controller
import time
import webbrowser
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
@client.event
async def on_ready():
    print('Bot is ready.')

async def help():
    await ctx.send('Type .chegg <link> to obtain a pdf file of the solutions to a question on Chegg. Owner of the bot must have a subscription to Chegg.')

@client.command()
async def chegg(ctx, arg):
    await ctx.send('Generating screenshots.. ')
    webbrowser.open(arg)    #opens link given by the user.
    keyboard = Controller() #used simulated key presses to save document as pdf.
    time.sleep(2)
    keyboard.press(Key.ctrl)
    keyboard.press('p')
    keyboard.release(Key.ctrl)
    keyboard.release('p')
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(4)       #increased time due to uncertainty in loading
    keyboard.type("1")
    time.sleep(0.5)
    keyboard.press(Key.enter)
    time.sleep(1)
    keyboard.press(Key.left)
    time.sleep(0.1)
    keyboard.press(Key.enter)
    time.sleep(0.1)
    file = discord.File(r"C:\Users\Gary\Downloads\1.pdf", filename="CheggSolutions.pdf") #saves file as 1.pdf, sends pdf as CheggSolutions.pdf
    embed = discord.Embed( title = 'Solutions uploaded as pdf')
    await ctx.send(file=file, embed=embed) #send user the pdf file.

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')


client.run('Nzg0OTE0NzA3ODA2OTQ1Mjgw.X8wOyQ.ZXu4HjRn2pbxq4-HdYPaJ9BGsUg') #Insert token generated for your bot from discord API
