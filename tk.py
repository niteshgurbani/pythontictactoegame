from tkinter import *
import tkinter.messagebox
root=Tk()
root.title("Tic Tac Toe")
initial=PhotoImage(file="base.png")
img1=PhotoImage(file="x.png")
img2=PhotoImage(file="o.png")
wincom=[{1,2,3},{4,5,6},{7,8,9},{1,5,9},{3,5,7},{1,4,7},{3,6,9},{2,5,8}]
def Result():
    global lb1
    for s in wincom:
        if s.issubset(pl1):
            lb1['text']='Game Over'
            tkinter.messagebox.showinfo('Result','Congratulations....Player 1 Wins')
            Initializegame()
            return True
        if s.issubset(pl2):
            lb1['text']='Game Over'
            tkinter.messagebox.showinfo('Result','Congratulations....Player 2 Wins')
            Initializegame()
            return True
    return False
def Game(cord):
    global lb
    global flag
    global counter
    global pl1
    global pl2
    global lb1
    index=cord[0]*3+cord[1]
    if flag:
        pl1.add(index+1)
        lb[index]['image']=img1
        lb[index]['state']='disable'
        lb1['text']='Player 2 to Play'
        flag=False
    else:
        pl2.add(index+1)
        lb[index]['image']=img2
        lb[index]['state']='disable'
        lb1['text']='Player 1 to Play'
        flag=True
    counter=counter+1
    if counter>=5:
        f=Result()
    if counter==9 and f==False:
        lb1['text']='Game Over'
        tkinter.messagebox.showwarning('Result',"There's a Draw")
        Initializegame()
def StartGame():
    global lb
    global lb1
    lb1=Label(text="Player 1 to Play",font="arial 20 bold")
    lb1.grid(row=3,column=1,padx=10,pady=10,sticky='nswe')
    global start
    start['state']='disable'
    for b in lb:
        b['state']='active'
def Display():
    print("Hello Boi")
def Initializegame():
    global lb
    global flag
    global counter
    global start
    global pl1
    global pl2
    pl1=set()
    pl2=set()
    counter=0
    lb=[]
    flag=True
    for i in range(3):
        for j in range(3):
            b1=Button(root,state='disable',image=initial,command=lambda cord=(i,j):Game(cord))
            b1.grid(row=i,column=j,padx=10,pady=10,sticky='nswe')
            lb.append(b1)
    start=Button(root,text='Start',font='arial 20 bold',relief=RAISED,bd=5,command=StartGame)
    start.grid(row=3,column=1,padx=10,pady=10,sticky='nswe')
    for i in range(4):
        root.grid_rowconfigure(i,weight=1)
    for i in range(3):
        root.grid_columnconfigure(i,weight=1)
Initializegame()
root.mainloop()
