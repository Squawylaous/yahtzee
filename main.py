import random
def remove(x,y):
    z=""
    for i in range(len(x)):
        if x[i]!=y: z=z+x[i]
    return z
def match(x):
    y=[0,0,0,0,0,0]
    for i in range(6):
        for ii in range(5):
            if x[ii]==i+1: y[i]+=1
    return y
def fill(x):
    x=str(x)+(" "*(3-len(str(x))))
    return x
def filll(x):
    x=str(x)+(" "*(18-len(str(x))))
    return x
def dice(x):
    y=""
    z=""
    w=""
    for i in range(5):
        if x[i]==1:
            y=y+"│       │    "
            w=w+"│       │    "
        elif x[i]==2 or x[i]==3:
            y=y+"│     • │    "
            w=w+"│ •     │    "
        elif x[i]==4 or x[i]==5 or x[i]==6:
            y=y+"│ •   • │    "
            w=w+"│ •   • │    "
        if x[i]==1 or x[i]==3 or x[i]==5: z=z+"│   •   │    "
        elif x[i]==2 or x[i]==4: z=z+"│       │    "
        elif x[i]==6: z=z+"│ •   • │    "
    print("┌───────┐    "*5,y,z,w,"└───────┘    "*5,sep="\n")
def reroll(x,y):
    y=list(remove(y,","))
    for i in range(len(y)): x[int(y[i])-1]=random.randint(1,6)
    return x
def roll():
    x=[random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
    dice(x)
    for i in range(2):
        if i==0: hello="2 rerolls"
        else: hello="1 reroll"
        y=input("Type the numbers of the dice you want to reroll seperated by commas, or hit enter to reroll none. You have "+hello+" left. ")
        if y=="": break
        x=reroll(x,y)
        dice(x)
    return x
def turn(p):
    input("Player "+data[p-1][18]+"'s turn!")
    print("┌──────────────────┐\n│"+filll(data[p-1][18])+"│\n├────────────┬─────┤\n│ Catagories │Score│\n├────────────┼─────┤\n│  Ones      │"+fill(data[p-1][0])," │\n│  Twos      │"+fill(data[p-1][1])," │\n│  Threes    │"+fill(data[p-1][2])," │\n│  Fours     │"+fill(data[p-1][3])," │\n│  Fives     │"+fill(data[p-1][4])," │\n│  Sixes     │"+fill(data[p-1][5])," │\n│  Subtotal  │"+fill(data[p-1][6])," │\n│  Bonus     │"+fill(data[p-1][7])," │\n│  Top Total │"+fill(data[p-1][8])," │\n├────────────┼─────┤\n│3 of a kind │"+fill(data[p-1][9])," │\n│4 of a kind │"+fill(data[p-1][10])," │\n│Full House  │"+fill(data[p-1][11])," │\n│SM Straight │"+fill(data[p-1][12])," │\n│LG Straight │"+fill(data[p-1][13])," │\n│Yahtzee     │"+fill(data[p-1][14])," │\n│Chance      │"+fill(data[p-1][15])," │\n│Bottom Total│"+fill(data[p-1][16])," │\n├────────────┼─────┤\n│Grand Total │"+fill(data[p-1][17])," │\n└────────────┴─────┘")
    x=roll()
    y=match(x)
    u=0
    t=False
    w=False
    z=False
    v=False
    s=False
    for i in range(6):
        if int(y[i])==2: z=True
        if int(y[i])>=3: w=True
        if int(y[i])>=4: v=True
        if int(y[i])==5: s=True
        if int(y[i])>=1: u+=1
    if u>=4:
        if u>=5 and (y[0]==1 or y[5]==1):
            t=True
        if y[2]>=1 and y[3]>=1:
            if y[1]>=1:
                if y[0]>=1 or y[4]>=1: u=True
                else: u=False
            elif y[4]>=1 and y[5]>=1: u=True
            else: u=False
        else: u=False
    else: u=False
    imp=20
    while data[p-1][imp-1]!="":
        inp=int(input("Input 1-6 to go for a number, 7 for 3 of a kind , 8 for 4 of a kind , 9 for Full House , 10 for a SM Straight , 11 for a LG Straight , 12 for a Yahtzee, or 13 for Chance. "))
        imp=inp
        if inp>6: imp+=3
    if inp<7: imp=y[inp-1]*inp
    else:
        if (w and inp==7) or (v and inp==8) or inp==13: imp=x[0]+x[1]+x[2]+x[3]+x[4]
        elif z and w and inp==9: imp=25
        elif u and inp==10: imp=30
        elif t and inp==11: imp=40
        elif s and inp==12: imp=50
        else: imp=0
        inp+=3
    inp-=1
    data[p-1][inp]=imp
    if data[p-1][0]!="" and data[p-1][1]!="" and data[p-1][2]!="" and data[p-1][3]!="" and data[p-1][4]!="" and data[p-1][5]!="":
        data[p-1][6]=int(data[p-1][0])+int(data[p-1][1])+int(data[p-1][2])+int(data[p-1][3])+int(data[p-1][4])+int(data[p-1][5])
        if data[p-1][6]>62: data[p-1][7]=35
        else: data[p-1][7]=0
        data[p-1][8]=data[p-1][6]+data[p-1][7]
    if data[p-1][9]!="" and data[p-1][10]!="" and data[p-1][11]!="" and data[p-1][12]!="" and data[p-1][13]!="" and data[p-1][14]!="" and data[p-1][15]: data[p-1][16]=int(data[p-1][9])+int(data[p-1][10])+int(data[p-1][11])+int(data[p-1][12])+int(data[p-1][13])+int(data[p-1][14])+int(data[p-1][15])
    if data[p-1][8]!="" and data[p-1][16]!="": data[p-1][17]=int(data[p-1][8])+int(data[p-1][16]) 
    print("┌──────────────────┐\n│"+filll(data[p-1][18])+"│\n├────────────┬─────┤\n│ Catagories │Score│\n├────────────┼─────┤\n│  Ones      │"+fill(data[p-1][0])," │\n│  Twos      │"+fill(data[p-1][1])," │\n│  Threes    │"+fill(data[p-1][2])," │\n│  Fours     │"+fill(data[p-1][3])," │\n│  Fives     │"+fill(data[p-1][4])," │\n│  Sixes     │"+fill(data[p-1][5])," │\n│  Subtotal  │"+fill(data[p-1][6])," │\n│  Bonus     │"+fill(data[p-1][7])," │\n│  Top Total │"+fill(data[p-1][8])," │\n├────────────┼─────┤\n│3 of a kind │"+fill(data[p-1][9])," │\n│4 of a kind │"+fill(data[p-1][10])," │\n│Full House  │"+fill(data[p-1][11])," │\n│SM Straight │"+fill(data[p-1][12])," │\n│LG Straight │"+fill(data[p-1][13])," │\n│Yahtzee     │"+fill(data[p-1][14])," │\n│Chance      │"+fill(data[p-1][15])," │\n│Bottom Total│"+fill(data[p-1][16])," │\n├────────────┼─────┤\n│Grand Total │"+fill(data[p-1][17])," │\n└────────────┴─────┘")
#┌───────┐
#│ • • • │
#│ • • • │
#│ • • • │
#└───────┘
#┌──────────────────┐
#│Player 1          │
#├────────────┬─────┤
#│ Catagories │Score│
#├────────────┼─────┤
#│  Ones      │2    │
#│  Twos      │8    │
#│  Threes    │6    │
#│  Fours     │12   │
#│  Fives     │15   │
#│  Sixes     │24   │
#│  Subtotal  │67   │
#│  Bonus     │35   │
#│  Top Total │102  │
#├────────────┼─────┤
#│3 of a kind │     │
#│4 of a kind │     │
#│Full House  │     │
#│SM Straight │     │
#│LG Straight │     │
#│Yahtzee     │     │
#│Chance      │     │
#│Bottom Total│     │
#├────────────┼─────┤
#│Grand Total │     │
#└────────────┴─────┘
p=int(input("How many players are there? "))
data=list(" "*p)
x=0
for i in range(p): 
    name=input("Player "+str(p)+"'s name? ")
    data[i]=["","","","","","","","","","","","","","","","","","",name,1]
for i in range(13):
    for i in range(p):
        turn(i+1)
for i in range(p):
    if data[i][17]>x:
        x=data[i][17]
        y=i+1
    print("┌──────────────────┐\n│"+filll(data[p-1][18])+"│\n├────────────┬─────┤\n│ Catagories │Score│\n├────────────┼─────┤\n│  Ones      │"+fill(data[p-1][0])," │\n│  Twos      │"+fill(data[p-1][1])," │\n│  Threes    │"+fill(data[p-1][2])," │\n│  Fours     │"+fill(data[p-1][3])," │\n│  Fives     │"+fill(data[p-1][4])," │\n│  Sixes     │"+fill(data[p-1][5])," │\n│  Subtotal  │"+fill(data[p-1][6])," │\n│  Bonus     │"+fill(data[p-1][7])," │\n│  Top Total │"+fill(data[p-1][8])," │\n├────────────┼─────┤\n│3 of a kind │"+fill(data[p-1][9])," │\n│4 of a kind │"+fill(data[p-1][10])," │\n│Full House  │"+fill(data[p-1][11])," │\n│SM Straight │"+fill(data[p-1][12])," │\n│LG Straight │"+fill(data[p-1][13])," │\n│Yahtzee     │"+fill(data[p-1][14])," │\n│Chance      │"+fill(data[p-1][15])," │\n│Bottom Total│"+fill(data[p-1][16])," │\n├────────────┼─────┤\n│Grand Total │"+fill(data[p-1][17])," │\n└────────────┴─────┘")
print("Player",data[y-1][18],"won with",x,"points!")
