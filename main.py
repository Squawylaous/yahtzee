import random
def dice(x):
    y=""
    z=""
    w=""
    for i in range(5):
        if x[i]==1:
            y=y+"|       |    "
            w=w+"|       |    "
        elif x[i]==2 or x[i]==3:
            y=y+"|     • |    "
            w=w+"| •     |    "
        elif x[i]==4 or x[i]==5 or x[i]==6:
            y=y+"| •   • |    "
            w=w+"| •   • |    "
        if x[i]==1 or x[i]==3 or x[i]==5: z=z+"|   •   |    "
        elif x[i]==2 or x[i]==4: z=z+"|       |    "
        elif x[i]==6: z=z+"| •   • |    "
    print(" _______     "*5,y,z,w," ‾‾‾‾‾‾‾     "*5,x,sep="\n")
#     _______      _______
#    | •   • |    | • • • |
#    |   •   |    | • • • |
#    |       |    | • • • |
#     ‾‾‾‾‾‾‾      ‾‾‾‾‾‾‾
input("Player 1's turn!")
dice([random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)])
