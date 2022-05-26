#Made by ArhanCodes

#Function to draw the border
def drawborder():
    up()
    goto(-295,295)
    pd()
    pensize(5)
    speed(0)
    for i in range(4):
        fd(580)
        rt(90)


#function for drawing lines
def drawlines():
    #Horizontal line 1
##    ht()
    up()
    goto(-295,100)
    down()
    fd(580)
    #Horizontal line 2
    up()
    goto(-295,-100)
    down()
    fd(580)
    #Vertical line 1
    up()
    goto(-100,295)
    down()
    rt(90)
    fd(580)
    #Vertical line 2
    up()
    goto(100,295)
    down()
    fd(580)
    
def drawX(x,y):
    color("blue")
    up()
    goto(x+20,y-20)
    seth(-45)
    down()
    fd(220)
    up()
    goto(x+180,y-20)
    seth(-135)
    down()
    fd(220)
    up()

def draw0(x,y):
    color("green")
    up()
    goto(x+100,y-180)
    down()
    seth(0)
    circle(80)
    up()





def drawpieces():
    x=-300
    y=300

    for p in pieces:
        if p=='X':
            drawX(x,y)
        elif p=='O':
            draw0(x,y)

        x=x+200
        if x>100:
            x=-300
            y=y-200


def check_winner(win_combination):
    for i in win_combination:
        if pieces[i[0]] == pieces[i[1]] == pieces[i[2]]  == 'X':
            return 'X'
        if pieces[i[0]] == pieces[i[1]] == pieces[i[2]] == 'O':
            return 'O'

def clicked(x,y):
    try:
        #Identify square and then draw
        global pieces,Turn

        onscreenclick(None)

        

        if all(pieces):
             up()
             home()
             down()
             color("red")
             write("No one won, you all suck", align="center",font=("Courier",20,"normal"))
             done()
             return

        col=(x+300)//200
##        print("Column number is")
        row= (-y+300)//200
##        print("Row number is" ,row)
        boxno= int(col+row *3)
##        print("Box number is", boxno)
##        print("You clciked at x= ",x, " and y=",y)


        if pieces[boxno] =='':
            pieces[boxno]= Turn

            if Turn == 'X':
                Turn='O'
            else:
                Turn='X'

            drawpieces()

            winsound.PlaySound("Click.wav",winsound.SND_ASYNC)


            #Call function to check who wins
            winner=check_winner(win_combination)

            if winner=='X':
                up()
                home()
                down()
                color("red")
                write("X Won", align="center",font=("Courier",100,"normal"))
                done()

            if winner=='O':
                up()
                home()
                down()
                color("red")
                write("O Won", align="center",font=("Courier",100,"normal"))
                done()
             


        else:
            print("This Square is already taken. GO AWAY")

        onscreenclick(clicked)




    except:
        print("Game Over")
    



#Main Code
from turtle import *
#one screen and a pen is created
import winsound
title("TicTacToe")
setup(600,600)
bgcolor("lightgrey")
drawborder()
drawlines()


pieces=['','','','','','','','','']
Turn='X'
win_combination=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))


onscreenclick(clicked)








    
