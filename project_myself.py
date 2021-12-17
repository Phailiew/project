# token OTA5NDIyOTM4NDYwMTM1NDU0.YZEEHA.jIlroXtIrBu6azGqiOIXPpB1VNQ
import discord
import random
import json
#from discord.colour import Color
from discord.ext import commands
from datetime import datetime, timedelta

# client = discord.Client()
# โพดำ Spade 9824
# ข้าวหลาม Diamond 9830
# ดอกจิก Club 9827
# โพแดง Heart 9829
# 1 ป๊อก9 2 ป๊อก8 3 ตอง 4 สเตจฟัจ 5 เรียง 6 เซียน 7 แต้ม
# ตองได้ 5 เท่า
# เรียง 3 เท่า
# เซียน 3 เท่า แพ้แค่ป๊อก8 9

# random.randrange(0, 101, 5) , <- random number from 0 to 100 increment by 5 each
roulette_lasttime = None
play_lasttime = None

# UNICODE
SPADE = 9824
DIAMOND = 9830
CLUB = 9827
HEART = 9829
# chr(SPADE)

#list of card
olst_card = ['As', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'Js', 'Qs', 'Ks', \
             'Ad', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'Jd', 'Qd', 'Kd', \
             'Ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc', \
             'Ah', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'Jh', 'Qh', 'Kh']

#list of value of card
olst_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, \
              1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]



#create class
class user_data:
    def __init__(self, name, uid, balance, last_time, play_time, win, lost, money_earn, money_lost):
        self.name = name
        self.id = uid
        self.balance = balance
        self.time = last_time
        self.play = play_time
        self.win = win
        self.lost = lost
        self.money_earn = money_earn
        self.money_lost = money_lost

#set prefix and remove default help command(The new one is embed)
bot = commands.Bot(command_prefix="+", help_command=None)


# message_lastseen = datetime.now()

#send message in console when bot is online
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

#help command 
@bot.command()
async def help(ctx):
    # help,play,credit,roulette,stat
    emBed = discord.Embed(title="All commands", description="Prefix: + \n How to use: type +COMMAND to use and enjoy",
                          color=0xf8b195)
    emBed.add_field(name="help", value="To get more information about a specific commands", inline=False)
    emBed.add_field(name="howto", value="To know about the condition about this game", inline=False)
    emBed.add_field(name="play", value="To enjoy your bet", inline=False)
    emBed.add_field(name="credit", value="To show how much credit you have left", inline=False)
    emBed.add_field(name="roulette", value="To earn more credit \n - you can use it once a day -", inline=False)
    emBed.add_field(name="stat", value="To see your lose/win stat and your earn/lose credit stat", inline=False)
    # emBed.add_field(name="balance",value="To see all the credits you have", inline = False)
    emBed.set_thumbnail(url="https://media.istockphoto.com/vectors/suits-of-playing-cards-icon-vector-id911680094")
    emBed.set_footer(text="Hope you enjoy!!!",
                     icon_url="https://media.istockphoto.com/vectors/suits-of-playing-cards-icon-vector-id911680094")

    await ctx.channel.send(embed=emBed)
    # อันแรกคือ parameter อันที่สองคือบอกว่าเราจะส่ง embed - from doc

#play command 
@bot.command()
#+play __ <- amount of our bet
async def play(ctx, *, par):
    #open file for read only
    file = open("data.json", 'r')
    #load the information
    data = json.load(file)
    #close
    file.close()
    #debug -> send in console
    print('play')

    score_p = 0
    score_d = 0
    lst_card = olst_card.copy()
    lst_value = olst_value.copy()
    emBed = discord.Embed(color=0xf67280)
    emBed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
    emBed.set_footer(text="Hope you enjoy!!!",
                     icon_url="https://media.istockphoto.com/vectors/suits-of-playing-cards-icon-vector-id911680094")

    try:
        par = int(par)
    except:
        print('wrong input')
        await ctx.channel.send("wrong input")

    user = ctx.message.author
    D_user = None
    #check if user already use bot or not
    for i in range(len(data['users'])):
        if data['users'][i]['id'] == user.id:
            D_user = user_data(data['users'][i]['name'], data['users'][i]['id'], data['users'][i]['balance'],
                               data['users'][i]['time'], data['users'][i]['play'], data['users'][i]['win'], data['users'][i]['lost'],
                               data['users'][i]['money_earn'], data['users'][i]['money_lost'])
            data['users'].pop(i)
            break
    if D_user is None:
        dt = (datetime.now() - timedelta(days=1))
        dt = dt.strftime("%Y-%m-%d %H:%M:%S")
        dp = (datetime.now() - timedelta(hours=1))
        dp = dp.strftime("%Y-%m-%d %H:%M:%S")
        D_user = user_data(user.name, user.id, 50, dt, dp, 0, 0, 0, 0)

    play_lasttime = datetime.strptime(D_user.play, "%Y-%m-%d %H:%M:%S")
    if play_lasttime == None or play_lasttime + timedelta(hours=1) <= datetime.now():   
        lst_popp = []  # player
        lst_popd = []  # dealer
        s = ""
        #random 2 cards
        for i in range(2):
            rand1 = random.randint(0, len(lst_card) - 1)
            lst_popp.append(lst_card.pop(rand1))
            score_p += lst_value.pop(rand1)
            score_p %= 10
            rand2 = random.randint(0, len(lst_card) - 1)
            lst_popd.append(lst_card.pop(rand2))
            score_d += lst_value.pop(rand2)
            score_d %= 10

        for x in lst_popp:
            s = s + " " + x

        def convert_icon(st):
            st = st.replace("s", chr(SPADE))
            st = st.replace("d", chr(DIAMOND))
            st = st.replace("c", chr(CLUB))
            st = st.replace("h", chr(HEART))
            return st

        sa = convert_icon(s)

        emBed.add_field(name="Player's cards", value=sa, inline=False)

        msg = await ctx.channel.send(embed=emBed)

        emoji1 = '🙆‍♀️'
        emoji2 = '🙅‍♀️'
        await msg.add_reaction(emoji1)
        await msg.add_reaction(emoji2)

        if score_d < 4:
            rand2 = random.randint(0, len(lst_card) - 1)
            lst_popd.append(lst_card.pop(rand2))
            score_d += lst_value.pop(rand2)
            score_d %= 10

        elif not (score_d == 4 and lst_popd[0][-1] == lst_popd[1][-1]):

            if score_d < 8:
                if random.random() * 10 % 2 == 0:
                    rand2 = random.randint(0, len(lst_card) - 1)
                    lst_popd.append(lst_card.pop(rand2))
                    score_d += lst_value.pop(rand2)
                    # เอาแค่หลักหน่วย
                    score_d %= 10

        if score_p < 4:
            rand1 = random.randint(0, len(lst_card) - 1)
            lst_popp.append(lst_card.pop(rand1))
            score_p += lst_value.pop(rand1)
            score_p %= 10
        elif not (score_p == 4 and lst_popp[0][-1] == lst_popp[1][-1]):
            # emojis = [emoji1, emoji2]
            test = True
            while test:
                def check(reaction, user):
                    return user == ctx.message.author and (str(reaction.emoji) == '🙆‍♀️' or str(reaction.emoji) == '🙅‍♀️')

                reaction, user = await bot.wait_for('reaction_add', check=check)
                if str(reaction) == '🙆‍♀️':
                    print("Hit")
                    num = random.randint(0, len(lst_card) - 1)
                    lst_popp.append(lst_card.pop(num))
                    score_p += lst_value.pop(num)
                    score_p %= 10
                    test = False
                elif str(reaction) == '🙅‍♀️':
                    print("emoji2")
                    test = False

        print(lst_popp, lst_popd)

        def scoring(cards, score):
            if len(cards) == 2:
                if score == 9:
                    return 1
                if score == 8:
                    return 2

            n = []
            royal = ['J', 'K', 'Q']
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
            display = 'You won'
            D_user.win += 1

            if player == 6 or player == 5 or player == 4:
                D_user.balance += par * 3
                D_user.money_earn += par * 3
            elif player == 3:
                D_user.balance += par * 5
                D_user.money_earn += par * 5
            elif lst_popp[0][-1] == lst_popp[1][-1] and (player == 1 or player == 2):
                D_user.balance += par * 2
                D_user.money_earn += par * 2
                print("player")
            else:
                D_user.balance += par
                D_user.money_earn += par


        elif player > dealer:
            display = 'You lost'
            D_user.lost += 1

            if dealer == 6 or dealer == 5 or dealer == 4:
                D_user.balance -= par * 3
                D_user.money_lost += par * 3
            elif dealer == 3:
                D_user.balance -= par * 5
                D_user.money_lost += par * 5
            elif lst_popd[0][-1] == lst_popd[1][-1] and (dealer == 1 or dealer == 2):
                D_user.balance -= par * 2
                D_user.money_lost += par * 2
                print("dealer")
            else:
                D_user.balance -= par
                D_user.money_lost += par

        else:
            if player == dealer == 7:
                if score_p > score_d:
                    display = 'You won'
                    D_user.win += 1
                    D_user.balance += par
                    D_user.money_earn += par
                elif score_p < score_d:
                    display = 'You lost'
                    D_user.lost += 1
                    D_user.balance -= par
                    D_user.money_lost += par
                elif score_p == score_d:
                    display = 'Draw'
                    D_user.lost += 0
                    D_user.win += 0
                    D_user.balance += 0
                    D_user.money_earn += 0
                    D_user.money_lost += 0

            elif player == dealer == 1 or player == dealer == 2:
                prioP = lst_popp[0][-1] == lst_popp[1][-1]
                prioD = lst_popd[0][-1] == lst_popd[1][-1]
                if prioP and not prioD:
                    display = 'You won'
                    D_user.win += 1
                    D_user.balance += par * 2
                    D_user.money_earn += par * 2

                elif not prioP and prioD:
                    display = 'You lost'
                    D_user.lost += 1
                    D_user.balance -= par * 2
                    D_user.money_lost += par * 2

                else:
                    display = 'Draw'

            else:
                display = 'Draw'

        file = open("data.json", 'w')
        data['users'].append(D_user.__dict__)
        json.dump(data, file)
        file.close()

        x = ""  # player
        z = ""  # dealer
        for y in lst_popp:
            x = x + " " + y
        for a in lst_popd:
            z = z + " " + a

        # convert s,d,c,h to Icon using UNICODE value
        # for both player and dealer
        x = convert_icon(x)
        z = convert_icon(z)

        emBed = discord.Embed(color=0xc06c84)
        emBed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        emBed.add_field(name="Player's cards", value=x, inline=False)
        emBed.add_field(name="Dealer's cards", value=z, inline=False)
        emBed.add_field(name="Status", value=display, inline=True)
        emBed.set_footer(text="Hope you enjoy!!!",
                        icon_url="https://media.istockphoto.com/vectors/suits-of-playing-cards-icon-vector-id911680094")

        msg = await ctx.channel.send(embed=emBed) 

        D_user.play = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    else:
        nextPlay = (datetime.strptime(D_user.time, "%Y-%m-%d %H:%M:%S") + timedelta(hours=1) - datetime.now())
        await ctx.channel.send(f"Next play in {str(nextPlay).split('.')[0]}")
    
    file = open("data.json", 'w')
    data['users'].append(D_user.__dict__)
    json.dump(data, file)
    file.close()

    


@bot.command()
async def howto(ctx):
    # help,test,send
    emBed = discord.Embed(title="How to play", color=0x6c5b7b)
    emBed.add_field(name="Press 🙆‍♀️", value="To hit : pick one more card", inline=False)
    emBed.add_field(name="Press 🙅‍♀️", value="To stand : stay with the same cards", inline=False)
    emBed.add_field(name="Conditions",
                    value="1. If player's starting card of 2 cards has a numerical value of 4 with the same suit \n   - We will automatically stand for you - \n 2. If player's starting card of 2 cards has a numerical value less than 4 \n   - We will automatically hit one more card for you - ",
                    inline=False)
    emBed.set_footer(text="Hope you enjoy!!!",
                     icon_url="https://media.istockphoto.com/vectors/suits-of-playing-cards-icon-vector-id911680094")
    await ctx.channel.send(embed=emBed)


@bot.command()
async def stat(ctx):
    file = open("data.json", 'r')
    data = json.load(file)
    file.close()
    user = ctx.message.author
    D_user = None
    for i in range(len(data['users'])):
        if data['users'][i]['id'] == user.id:
            D_user = user_data(data['users'][i]['name'], data['users'][i]['id'], data['users'][i]['balance'],
                               data['users'][i]['time'],data['users'][i]['play'], data['users'][i]['win'], data['users'][i]['lost'],
                               data['users'][i]['money_earn'], data['users'][i]['money_lost'])
            data['users'].pop(i)
            break
    if D_user is None:
        dt = (datetime.now() - timedelta(days=1))
        dt = dt.strftime("%Y-%m-%d %H:%M:%S")
        dp = (datetime.now() - timedelta(hours=1))
        dp = dp.strftime("%Y-%m-%d %H:%M:%S")
        D_user = user_data(user.name, user.id, 50, dt, dp, 0, 0, 0, 0)

    emBed = discord.Embed(title="Player Stats", color=0x6c5b7b)
    emBed.add_field(name="Win", value=D_user.win, inline=False)
    emBed.add_field(name="lost", value=D_user.lost, inline=False)
    emBed.add_field(name="Money won", value=D_user.money_earn, inline=False)
    emBed.add_field(name="Money lost", value=D_user.money_lost, inline=False)
    emBed.set_footer(text="Hope you enjoy!!!",
                     icon_url="https://media.istockphoto.com/vectors/suits-of-playing-cards-icon-vector-id911680094")
    await ctx.channel.send(embed=emBed)


@bot.command()
async def roulette(ctx):
    file = open("data.json", 'r')
    data = json.load(file)
    file.close()
    user = ctx.message.author
    D_user = None
    for i in range(len(data['users'])):
        if data['users'][i]['id'] == user.id:
            D_user = user_data(data['users'][i]['name'], data['users'][i]['id'], data['users'][i]['balance'],
                               data['users'][i]['time'],data['users'][i]['play'], data['users'][i]['win'], data['users'][i]['lost'],
                               data['users'][i]['money_earn'], data['users'][i]['money_lost'])
            data['users'].pop(i)
            break
    if D_user is None:
        dt = (datetime.now() - timedelta(days=1))
        # เป็น obj
        dt = dt.strftime("%Y-%m-%d %H:%M:%S")
        dp = (datetime.now() - timedelta(hours=1))
        dp = dp.strftime("%Y-%m-%d %H:%M:%S")
        D_user = user_data(user.name, user.id, 50, dt, dp, 0, 0, 0, 0)
        # แปลงเป็น str
    roulette_lasttime = datetime.strptime(D_user.time, "%Y-%m-%d %H:%M:%S")
    # แปลงจาก str เป็น object ของ datetime

    if roulette_lasttime == None or roulette_lasttime + timedelta(days=1) <= datetime.now():
        receive = random.randrange(0, 101, 5)
        D_user.balance = D_user.balance + receive
        await ctx.channel.send(f"You received {receive}\n Current balance: {D_user.balance}")
        D_user.time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # แปลงจาก object datetime เป็น str ตาม format ในวงเล็บ
    else:
        nextTime = (datetime.strptime(D_user.time, "%Y-%m-%d %H:%M:%S") + timedelta(days=1) - datetime.now())
        await ctx.channel.send(f"Next spin in {str(nextTime).split('.')[0]}")

    file = open("data.json", 'w')
    data['users'].append(D_user.__dict__)
    json.dump(data, file)
    file.close()


@bot.command()
async def credit(ctx):
    file = open("data.json", 'r')
    data = json.load(file)
    file.close()
    user = ctx.message.author
    D_user = None
    for i in range(len(data['users'])):
        if data['users'][i]['id'] == user.id:
            D_user = user_data(data['users'][i]['name'], data['users'][i]['id'], data['users'][i]['balance'],
                               data['users'][i]['time'],data['users'][i]['play'], data['users'][i]['win'], data['users'][i]['lost'],
                               data['users'][i]['money_earn'], data['users'][i]['money_lost'])
            data['users'].pop(i)
            break
    if D_user is None:
        dt = (datetime.now() - timedelta(days=1))
        dt = dt.strftime("%Y-%m-%d %H:%M:%S")
        dp = (datetime.now() - timedelta(hours=1))
        dp = dp.strftime("%Y-%m-%d %H:%M:%S")
        D_user = user_data(user.name, user.id, 50, dt, dp, 0, 0, 0, 0)
    await ctx.channel.send(f"You have " + str(D_user.balance) + " now")


bot.run("")