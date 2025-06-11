from tkinter import * 
from tkinter import ttk
from PIL import ImageTk,Image
import random

root=Tk()
root.title("Dice")
root.geometry("400x300+500+160")
ico=Image.open("Dice/DICE.jpg")
icon=ImageTk.PhotoImage(ico)
root.wm_iconphoto(False,icon)
frame=Frame(root,bg="black")
frame.place(x=0,y=0,height=300,width=400)
dice=["one","two","three","four","five","six"]

def roll():
    n=random.randint(1, 6)
    for i in range(1,7):
        if n==i:
            name="Dice/"+dice[i-1]+".jpeg"
            img=Image.open(name)
            img=img.resize((150,150))
            img=ImageTk.PhotoImage(img)    
            imagefix=Label(frame,image=img)
            imagefix.image=img
            imagefix.place(x=120,y=30)
            break

btn=Button(frame,width=20,activebackground="lawngreen",font=("arial",12,"bold"),bg="white",text="Roll",command=roll).place(x=100,y=240)
root.mainloop()
