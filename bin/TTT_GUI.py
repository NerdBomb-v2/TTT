from tkinter import Tk, Label, Button, NORMAL, DISABLED
from ttt_sim import TTT
root = Tk()
root.geometry("200x190")
game = TTT()
def f(x,y):
    buttons[x-1][y-1]['state']=DISABLED
    game.set_cross(x,y)
    buttons[x-1][y-1]['bg']='blue'
    buttons[x-1][y-1]['text']='X'
    game.ai_move('O')
    buttons[game.ai_choice[0]-1][game.ai_choice[1]-1]['state']=DISABLED
    buttons[game.ai_choice[0]-1][game.ai_choice[1]-1]['bg']='red'
    buttons[game.ai_choice[0]-1][game.ai_choice[1]-1]['text']='O'
    val = f'Winner: {game.winner}'
    val = val.replace('None',' ');val = val.replace('True','O');val = val.replace('False','X')
    Label(root,text=val).grid(row=4,column=1)
    if game.winner!=None:
        for i in range(3):
            for j in range(3):
                buttons[i][j]['state']=DISABLED

def reset_button(x,y):
    buttons[x][y]['state']=NORMAL
    buttons[x][y]['bg']='white'
    buttons[x][y]['text']='-'
def reset_game():
    for i in range(3):
        for j in range(3):
            reset_button(i,j)
    game.reset()
    game.winner=None
    
box1 = Button(root,text='-',padx=25,pady=15,command=lambda : f(1,1),fg="black",bg="white")
box1.grid(row=1,column=1)
box2 = Button(root,text='-',padx=25,pady=15,command=lambda : f(1,2),fg="black",bg="white")
box2.grid(row=1,column=2)
box3 = Button(root,text='-',padx=25,pady=15,command=lambda : f(1,3),fg="black",bg="white")
box3.grid(row=1,column=3)


box4 = Button(root,text='-',padx=25,pady=15,command=lambda : f(2,1),fg="black",bg="white")
box4.grid(row=2,column=1)
box5 = Button(root,text='-',padx=25,pady=15,command=lambda : f(2,2),fg="black",bg="white")
box5.grid(row=2,column=2)
box6 = Button(root,text='-',padx=25,pady=15,command=lambda : f(2,3),fg="black",bg="white")
box6.grid(row=2,column=3)

box7 = Button(root,text='-',padx=25,pady=15,command=lambda : f(3,1),fg="black",bg="white")
box7.grid(row=3,column=1)
box8 = Button(root,text='-',padx=25,pady=15,command=lambda : f(3,2),fg="black",bg="white")
box8.grid(row=3,column=2)
box9 = Button(root,text='-',padx=25,pady=15,command=lambda : f(3,3),fg="black",bg="white")
box9.grid(row=3,column=3)

buttons = [[box1,box2,box3],[box4,box5,box6],[box7,box8,box9]]  
#root.resizable(False,False)
reset = Button(root,text='Reset',padx=15,command=reset_game,fg="black",bg="white").grid(row=4,column=2)


root.mainloop()
