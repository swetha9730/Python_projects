#import required library
from tkinter import *
import random

#Opening GUI
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Swetha\'s-Rock,Paper,Scissor')
root.config(bg ='seashell3')


#heading
Label(root, text = 'Rock, Paper and Scissor' , font='arial 20 bold', bg = 'seashell2', fg='red').pack()


##user choice
user_take = StringVar()
Label(root, text = 'choose any one: rock, paper, scissor' , font='arial 15 bold', bg = 'seashell2').place(x = 20,y=70) 
Entry(root, font = 'arial 15', textvariable = user_take , bg = 'antiquewhite1').place(x=90 , y = 130)



#computer choice
comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissor'
    



##function to play
Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie,you both selected  the same and have same IQ.')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose,PC selected paper,dumber than your PC')
    elif user_pick == 'rock' and comp_pick == 'scissor':
        Result.set('you win,PC selected scissor,smarter than your PC')
    elif user_pick == 'paper' and comp_pick == 'scissor':
        Result.set('you loose,PC selected scissor,dumber than your PC')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win,PC selected rock,smarter than your PC')
    elif user_pick == 'scissor' and comp_pick == 'rock':
        Result.set('you loose,PC selected rock,dumber than your PC')
    elif user_pick == 'scissor' and comp_pick == 'paper':
        Result.set('you win ,PC selected paper,smarter than your PC')
    else:
        Result.set('invalid: choose any one: rock, paper, scissor')
    
        
    
##fun to reset
def Reset():
    Result.set("") 
    user_take.set("")

##fun to exit
def Exit():
    root.destroy()


###### button
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2',width = 50,).place(x=25, y = 250)

Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).place(x=150,y=190)

Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = Reset).place(x=70,y=310)

Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=230,y=310)

root.mainloop()
