#token OTA5NDIyOTM4NDYwMTM1NDU0.YZEEHA.jIlroXtIrBu6azGqiOIXPpB1VNQ
import discord
import random
from discord.colour import Color
from discord.ext import commands
from datetime import datetime, timedelta
#client = discord.Client()
#โพดำ Spade 9824
#ข้าวหลาม Diamond 9830 
#ดอกจิก Club 9827
#โพแดง Heart 9829 
# 1 ป๊อก9 2 ป๊อก8 3 ตอง 4 สเตจฟัจ 5 เรียง 6 เซียน 7 แต้ม
# ตองได้ 5 เท่า
# เรียง 3 เท่า ดอกสูงสุด 4 เท่า 
# เซียน 3 เท่า แพ้แค่ป๊อก8 9

# random.randrange(0, 101, 5) , <- random number from 0 to 100 increment by 5 each
roulette_lasttime =  None

SPADE = 9824
DIAMOND = 9830
CLUB = 9827
HEART = 9829
playing = False
olst_card = ['As','2s','3s','4s','5s','6s','7s','8s','9s','10s','Js','Qs','Ks',\
            'Ad','2d','3d','4d','5d','6d','7d','8d','9d','10d','Jd','Qd','Kd',\
            'Ac','2c','3c','4c','5c','6c','7c','8c','9c','10c','Jc','Qc','Kc',\
            'Ah','2h','3h','4h','5h','6h','7h','8h','9h','10h','Jh','Qh','Kh'
            ]
olst_value = [1,2,3,4,5,6,7,8,9,0,0,0,0,1,2,3,4,5,6,7,8,9,0,0,0,0,\
             1,2,3,4,5,6,7,8,9,0,0,0,0,1,2,3,4,5,6,7,8,9,0,0,0,0]


balance = 0

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

@bot.command()
async def play(ctx, * , par):
    print('play')
    playing = True
    score_p = 0
    score_d = 0
    lst_card = olst_card.copy()
    lst_value = olst_value.copy()
    emBed = discord.Embed(color=0x199f6b)
    emBed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
    emBed.set_footer(text="Hope you enjoy!!!", icon_url="https://media.istockphoto.com/vectors/suits-of-playing-cards-icon-vector-id911680094")
    
    lst_popp = [] # player
    lst_popd = [] # dealer
    s = ""
    for i in range(2):
      rand1 = random.randint(0, len(lst_card)-1)
      lst_popp.append(lst_card.pop(rand1))
      score_p += lst_value.pop(rand1)
      score_p %= 10
      rand2 = random.randint(0, len(lst_card)-1)
      lst_popd.append(lst_card.pop(rand2))
      score_d += lst_value.pop(rand2)
      score_d %= 10
    
    for x in lst_popp:
        s = s + " " + x
        
    emBed.add_field(name="Player's cards",value= s, inline = False)

    msg = await ctx.channel.send(embed=emBed)
    
    emoji1 = '👍'
    emoji2 = '👎'
    await msg.add_reaction(emoji1)
    await msg.add_reaction(emoji2)

    if score_d < 4:
        rand2 = random.randint(0, len(lst_card)-1)
        lst_popd.append(lst_card.pop(rand2))
        score_d += lst_value.pop(rand2)
        score_d %= 10
        
    elif score_d < 9:
      if random.random()*10%2 == 0:
        rand2 = random.randint(0, len(lst_card)-1)
        lst_popd.append(lst_card.pop(rand2))
        score_d += lst_value.pop(rand2)
        score_d %= 10
    
    if score_p < 4:
      rand1 = random.randint(0, len(lst_card)-1)
      lst_popp.append(lst_card.pop(rand1))
      score_p += lst_value.pop(rand1) 
      score_p %= 10
    else:
      # emojis = [emoji1, emoji2]
      test = True
      while test:
          def check(reaction, user):
              return user == ctx.message.author and (str(reaction.emoji) == '👍' or str(reaction.emoji) == '👎')
                        
          reaction, user = await bot.wait_for('reaction_add', check=check)
          if str(reaction) == '👍':
              print("Hit")
              num = random.randint(0, len(lst_card)-1)
              lst_popp.append(lst_card.pop(num))
              score_p += lst_value.pop(num) 
              score_p %= 10
              test = False
          elif str(reaction) == '👎':
              print("emoji2")
              test = False
    
    print(lst_popp, lst_popd)
    
    def scoring(cards, score):
        if score == 9:
            return 1
        if score == 8:
            return 2
        
        n = []
        royal = ['J','K','Q']
        for i in range(len(cards)): 
            n.append(cards[i].replace(cards[i][-1], ""))

        sorted = sorting(n)
        print(n)

        if len(n) == 3:
            if n[0] == n[1] == n[2]:
                return 3
            
            elif sorted[0] + 1 == sorted[1] and sorted[1] + 1 == sorted[2]:
            
                if cards[0][-1] == cards[1][-1] == cards[2][-1]:
                    return 4
                else:
                    return 5

            elif (cards[0][0] in royal) and (cards[1][0] in royal) and (cards[2][0] in royal):     
                return 6
        return 7


    def sorting(n):
        arr = []
        for s in n:
            if s == 'A':
                arr.append(1)
            elif s == 'J':
                arr.append(11)
            elif s == 'Q':
                arr.append(12)
            elif s == 'K':
                arr.append(13)  
            else:
                arr.append(int(s))
        arr.sort()
        return arr
    
    player = scoring(lst_popp, score_p)
    dealer = scoring(lst_popd, score_d)
    

    if player < dealer:
        print('player')
    elif player > dealer:
        print('dealer')
    else:
        if player == dealer == 7:
            print('player') if score_p > score_d else print('dealer')
        else:
            print('unknow')
    
    

@bot.command()
async def stat(ctx):
 print("stat")

@bot.command()
async def roulette(ctx):
  global roulette_lasttime
  if roulette_lasttime == None or roulette_lasttime + timedelta(days=1) <= datetime.now():     
    global balance 
    receive = random.randrange(0, 101, 5)
    balance = balance + receive
    await ctx.channel.send(f"You received {receive}\n Current balance: {balance}")
    roulette_lasttime = datetime.now()
  else:
    await ctx.channel.send(f"Next spin in {(roulette_lasttime + timedelta(days=1) - datetime.now()).time}")  

@bot.command()
async def credit(ctx):
  await ctx.channel.send(f"You have {balance} now")


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




bot.run("OTA5NDIyOTM4NDYwMTM1NDU0.YZEEHA.nWsu_X_dmDwqTAgvXqdXfvW7pJU")