#ROCK PAPER SCISSOR BY VARUN SHARMA
print("\n\n\nRock Paper Scissors by Varun Sharma\n\npresss Ctrl+. when you feel like exitting the game.")
input("\n\n<<PRESS ENTER TO BEGIN>>\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

#Declaring varibale
MoveSet = [1,2,3]
Cmove=0
Pmove=0
Cscore=0
Pscore=0


#Declaring Framework
from time import sleep
from random import choice
def game():
    print("\n\n\n\n\n\n\n\nDecide your move, enter \"R\" for Rock, \"S\" for Scissors and \"P\"for Paper")
    tempVal=input()
    while tempVal != 'R' and tempVal != 'S' and tempVal != 'P' and tempVal != 'r' and tempVal != 's' and tempVal != 'p':
        print("Decide your move, enter \"R\" for Rock, \"S\" for Scissors and \"P\"for Paper")
        tempVal=input();
    sleep(0.13)
    if tempVal == "R" or tempVal == "r":
        Pmove=1
    elif tempVal == "P" or tempVal == "p":
        Pmove=2
    elif tempVal == "S" or tempVal == "s":
        Pmove=3
    else:
        print("Custom_ERROR-01 : can't recognize user's input")
        raise SystemExit(0);
    sleep(0.13)
    Cmove=choice(MoveSet)
    if Cmove == 1:
        PCmove='Rock'
    elif Cmove == 2:
        PCmove='Paper'
    elif Cmove == 3:
        PCmove='Scissor'
    else:
        print("Custom_ERROR-00 : PC's move unrecognizable")
        raise SystemExit(0)
    del tempVal;
    sleep(0.038)
    return Cmove, Pmove, PCmove
def decisive(Cmove,Pmove):
    if [Cmove,Pmove] == [1,3] or [Cmove,Pmove] == [2,1] or [Cmove,Pmove] == [3,2]:
        winner=1
    elif [Cmove,Pmove] == [1,2] or [Cmove,Pmove] == [2,3] or [Cmove,Pmove] == [3,1]:
        winner=2
    elif [Cmove,Pmove] == [1,1] or [Cmove,Pmove] == [2,2] or [Cmove,Pmove] == [3,3]:
        winner=0
    else:
        print("Custom_ERROR-03 : Set [PCmove,playermove] was assigned an unexpected value")
        raise SystemExit(0)
    return winner
def Scoreboard(winner,cm,cs,ps):
    if winner == 1:
        print("\nPC won the round by choosing",cm)
        cs=cs+1
    elif winner == 2:
        print("\nPlayer won the round!")
        ps=ps+1
    else:
        print("Custom_ERROR-02 : Scoreboard function recieved explicit values")
        raise SystemExit(0)
    print("\nSession Score:")
    print("Player : ",ps)
    print("PC : ",cs)
    return cs, ps



#Driver Code
while True:
    Cmove,Pmove,PCmove=game()
    winner=decisive(Cmove,Pmove)
    while winner == 0:
        print("WoW! A Draw!\nBoth Player and PC have chosen",PCmove)
        print("let's go again")
        Cmove,Pmove,PCmove=game()
        winner=decisive(Cmove,Pmove)
    sleep(0.13)
    cmCache=PCmove;
    print("PC - ",cmCache)
    RoundWinner=winner
    cs,ps=Scoreboard(RoundWinner,cmCache,Cscore,Pscore)
    Cscore=cs; Pscore=ps
    input("<<< PRESS ENTER TO CONTINUE >>>");
