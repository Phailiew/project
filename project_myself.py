#token OTA5NDIyOTM4NDYwMTM1NDU0.YZEEHA.jIlroXtIrBu6azGqiOIXPpB1VNQ
import discord
from discord.colour import Color
from discord.ext import commands
from datetime import datetime, timedelta
#client = discord.Client()
bot = commands.Bot(command_prefix = "+", help_command = None)

message_lastseen = datetime.now()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def test(ctx, * , par):
    await ctx.channel.send("you typed {0}".format(par))


@bot.command()
async def send(ctx):
    await ctx.channel.send("Hello")


@bot.command()
async def help(ctx):
    #help,test,send    
    emBed = discord.Embed(title="All commands",description="Prefix: + \n How to use: type +COMMAND_NAME to use that command and enjoy", color=0x199f6b)
    emBed.add_field(name="help",value="To get more information about a specific commands", inline = False)
    emBed.add_field(name="test",value="Respond message that you have send", inline = False)
    emBed.add_field(name="send",value="Send hello message to user", inline = False)
    emBed.add_field(name="user",value="Send your username followed by hello message to user", inline = False)
    emBed.set_thumbnail(url = "https://media.istockphoto.com/vectors/suits-of-playing-cards-icon-vector-id911680094")
    emBed.set_footer(text="Hope you enjoy!!!", icon_url = "https://media.istockphoto.com/vectors/suits-of-playing-cards-icon-vector-id911680094")
    

    await ctx.channel.send(embed=emBed) 




@bot.event
async def on_message(message):
    global message_lastseen
    if message.content == "+hello" and datetime.now() >= message_lastseen:
        message_lastseen = datetime.now() + timedelta(seconds = 4)
        await message.channel.send("hi")
    elif message.content == "+user":
        await message.channel.send(str(message.author.name) + " " + "hello!")
    elif message.content == "+logout":
        await bot.logout()
  
    await bot.process_commands(message)




bot.run("OTA5NDIyOTM4NDYwMTM1NDU0.YZEEHA.jIlroXtIrBu6azGqiOIXPpB1VNQ")

