from tkinter import *
from tkinter import ttk
import random
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


root=Tk()
root.title("Matrixer")
title=Label(root,relief=RIDGE,bg="slategray3",bd=10,text="",font=("times new roman",25,"bold")).pack(fill=X)
root.geometry("1000x600+250+70")


#FRAMES----
frame1=Frame(root,relief=RIDGE,bd=5,bg="light cyan")
frame1.place(height=500,width=495,x=5,y=70)
frame2=Frame(root,relief=RIDGE,bd=5,bg="light cyan")
frame2.place(height=500,width=495,x=500,y=70)
frame3=Frame(root,relief=RIDGE,bd=3,bg="spring green3")
frame3.place(height=63,width=485,x=505,y=500)
frame4=Frame(root,relief=RIDGE,bd=3,bg="gray7")
frame4.place(height=275,width=485,x=10,y=290)


#ENTRY----
lbl=Label(frame1,text="Enter Matrix:",font=("arial",10),bg="darkslategray1")
lbl.grid(column=0,row=0,sticky=W)
lbl=Label(frame1,text="|",font=("arial",17),bg="darkslategray1")
lbl.grid(column=4,row=1,sticky=W,ipadx=8,ipady=0.5)
lbl=Label(frame1,text="|",font=("arial",17),bg="darkslategray1")
lbl.grid(column=4,row=2,sticky=W,ipadx=8,ipady=0.5)
lbl=Label(frame1,text="|",font=("arial",17),bg="darkslategray1")
lbl.grid(column=4,row=3,sticky=W,ipadx=8,ipady=0.5)

a=Entry(frame1,justify=CENTER,font=("arial",10,"normal"),width=3)  #1
a.grid(column=1,row=1,sticky=W,ipadx=6,ipady=6)   
b=Entry(frame1,justify=CENTER,font=("arial",10,"normal"),width=3)  #2
b.grid(column=2,row=1,sticky=W,ipadx=6,ipady=6) 
c=Entry(frame1,justify=CENTER,font=("arial",10,"normal"),width=3)  #3
c.grid(column=3,row=1,sticky=W,ipadx=6,ipady=6) 
d=Entry(frame1,justify=CENTER,font=("arial",10,"normal"),width=3)  #4
d.grid(column=1,row=2,sticky=W,ipadx=6,ipady=6) 
e=Entry(frame1,justify=CENTER,font=("arial",10,"normal"),width=3)  #5
e.grid(column=2,row=2,sticky=W,ipadx=6,ipady=6) 
f=Entry(frame1,justify=CENTER,font=("arial",10,"normal"),width=3) #6
f.grid(column=3,row=2,sticky=W,ipadx=6,ipady=6)  
g=Entry(frame1,justify=CENTER,font=("arial",10,"normal"),width=3)  #7
g.grid(column=1,row=3,sticky=W,ipadx=6,ipady=6) 
h=Entry(frame1,justify=CENTER,font=("arial",10,"normal"),width=3)  #8      
h.grid(column=2,row=3,sticky=W,ipadx=6,ipady=6) 
i=Entry(frame1,justify=CENTER,font=("arial",10,"normal"),width=3)  #9
i.grid(column=3,row=3,sticky=W,ipadx=6,ipady=6) 
j=Entry(frame1,justify=CENTER,font=("arial",10,"normal"),width=3)
j.grid(column=5,row=1,sticky=W,ipadx=6,ipady=6) 
k=Entry(frame1,justify=CENTER,font=("arial",10,"normal"),width=3)
k.grid(column=5,row=2,sticky=W,ipadx=6,ipady=6) 
l=Entry(frame1,justify=CENTER,font=("arial",10,"normal"),width=3)
l.grid(column=5,row=3,sticky=W,ipadx=6,ipady=6) 

y=[]
def clear():
    for widgets in frame4.winfo_children():
        widgets.destroy()
    for widgets in frame2.winfo_children():
        widgets.destroy()
    
    lbl1.config(text="")
    lbl2.config(text="")
    lbl3.config(text="")
    lbl4.config(text="")
            
def apply():
    x=[]
    a_=a.get()
    b_=b.get()
    c_=c.get()
    d_=d.get()
    e_=e.get()
    f_=f.get()
    g_=g.get()
    h_=h.get()
    i_=i.get()
    j_=j.get()
    k_=k.get()
    l_=l.get()
    x.extend((a_,b_,c_,d_,e_,f_,g_,h_,i_,j_,k_,l_))
    global y
    y=[]
    y=x

def solve():
    def show(m,b):
        row1=str(m[0:3])+" "+"|"+" "+str(b[0:3])
        row2=str(m[3:6])+" "+"|"+" "+str(b[3:6])
        row3=str(m[6:9])+" "+"|"+" "+str(b[6:9])
        lbl=Label(frame2,text=row1,font=("arial",8)).pack(anchor='w')
        lbl=Label(frame2,text=row2,font=("arial",8)).pack(anchor='w')
        lbl=Label(frame2,text=row3,font=("arial",8)).place(anchor='w')
    m=[]
    for i in range(0,9):
        m.append(float(y[i]))
    b=[1,0,0,0,1,0,0,0,1]
   
    if (m[0]*(m[4]*m[8]-m[5]*m[7])+m[1]*(m[5]*m[6]-m[3]*m[8])+m[2]*(m[3]*m[7]-m[4]*m[6]))==0:
        lbl=Label(frame2,fg="white",text="Error: Matrix is not invertible.",font=("arial",12,"bold"),bg="firebrick2").pack()
        lbl=Label(frame2,fg="white",text="Equations cannot be solved.",font=("arial",12,"bold"),bg="firebrick2").pack()
    else:
        
        if m[0]==0 and m[3]!=0:
            c=m[0:3]
            m[0:3]=m[3:6]       
            m[3:6]=c[0:3]
            c_=b[0:3]
            b[0:3]=b[3:6]
            b[3:6]=c_[0:3]
 
            
        if m[0]==0 and m[3]==0:
            c=m[0:3]
            m[0:3]=m[6:9]       
            m[6:9]=c[0:3]
            c_=b[0:3]
            b[0:3]=b[6:9]
            b[6:9]=c_[0:3]
            
        if m[0]!=0:       
            d=m[6]/m[0]
            for i in range(6,9):
                m[i]=m[i]-m[i-6]*d
                b[i]=b[i]-b[i-6]*d
             
        if m[0]!=0:
            d=m[3]/m[0]
            for i in range(3,6):
                m[i]=m[i]-m[i-3]*d
                b[i]=b[i]-b[i-3]*d
            
        d=m[7]/m[4]
        for i in range(6,9):
            m[i]=m[i]-m[i-3]*d
            b[i]=b[i]-b[i-3]*d
        
        d=1/m[8]
        for i in range(6,9):
            m[i]=m[i]*d
            b[i]=b[i]*d
        
        d=m[5]
        for i in range(3,6):
            m[i]=m[i]-m[i+3]*d
            b[i]=b[i]-b[i+3]*d
        
        d=1/m[4]
        for i in range(3,6):
            m[i]=m[i]*d
            b[i]=b[i]*d
        
        d=m[2]
        d_=m[1]
        for i in range(0,3):
            m[i]=m[i]-m[i+6]*d-m[i+3]*d_
            b[i]=b[i]-b[i+6]*d-b[i+3]*d_
        
        d=1/m[0]
        for i in range(0,3):
            m[i]=m[i]*d
            b[i]=b[i]*d
        
        row1=str(b[0:3])
        row2=str(b[3:6])
        row3=str(b[6:9])
        lbl=Label(frame2,text="Inverse of the matrix:",font=("arial",12),bg="light cyan").place(x=0,y=0)
        lbl=Label(frame2,text=row1,font=("arial",10),bg="light cyan").place(x=0,y=20)
        lbl=Label(frame2,text=row2,font=("arial",10),bg="light cyan").place(x=0,y=40)
        lbl=Label(frame2,text=row3,font=("arial",10),bg="light cyan").place(x=0,y=60)
        
        c=[]
        for i in range(0,3):
            v=0
            y_=0
            u=i*3
            for j in range(0,3):
                y_+=b[u]*float(y[v+9])
                u+=1
                v+=1
            c.append(y_)
        
        row1a="x="+str(c[0])
        row2a="y="+str(c[1])
        row3a="z="+str(c[2])
        lbl=Label(frame2,text="Solution of the Equations:",bd=3,relief=RIDGE,font=("arial",15),bg="light cyan").place(x=0,y=100)
        lbl=Label(frame2,text=row1a,font=("arial",10),bg="spring green").place(x=5,y=140)
        lbl=Label(frame2,text=row2a,font=("arial",10),bg="spring green").place(x=5,y=160)
        lbl=Label(frame2,text=row3a,font=("arial",10),bg="spring green").place(x=5,y=180)
           
def eqn():
    global lbl1
    global lbl2
    global lbl3
    global lbl4
    lbl1=Label(frame1,text="Equation entered:",font=("arial",10),bg="light cyan")
    lbl1.grid(column=0,row=4,sticky=W)
    line_1=y[0]+"x+"+y[1]+"y+"+y[2]+"z"+"="+y[9]
    line_2=y[3]+"x+"+y[4]+"y+"+y[5]+"z"+"="+y[10]
    line_3=y[6]+"x+"+y[7]+"y+"+y[8]+"z"+"="+y[11]
    lbl2=Label(frame1,text=line_1,font=("arial",10),bg="light cyan")
    lbl2.grid(column=0,row=5,sticky=W)
    lbl3=Label(frame1,text=line_2,font=("arial",10),bg="light cyan")
    lbl3.grid(column=0,row=6,sticky=W)
    lbl4=Label(frame1,text=line_3,font=("arial",10),bg="light cyan")
    lbl4.grid(column=0,row=7,sticky=W)
    
def plot():
    global y
    normal1 = np.array(y[0:3])
    normal2= np.array(y[3:6])
    normal3= np.array(y[6:9])

    d1=float(y[9])
    d2=float(y[10])
    d3=float(y[11])
    x = np.linspace(-20, 20, 50)
    y_ = np.linspace(-20, 20, 50)
    X, Y = np.meshgrid(x, y_)
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    if float(normal1[2])!=0:    
        Z = (-float(normal1[0]) * X - float(normal1[1]) * Y - d1) * 1. /float(normal1[2])
        ax.plot_surface(X, Y, Z, cmap='gnuplot_r')
    else:
        Z=0
        
    if float(normal2[2])!=0: 
        Z=(-float(normal2[0] )* X - float(normal2[1]) * Y - d2) * 1. /float(normal2[2])
        ax.plot_surface(X, Y, Z, cmap='cubehelix')
    else:
        Z=0
    
    if float(normal3[2])!=0:
        Z=(-float(normal3[0]) * X - float(normal3[1]) * Y - d3) * 1. /float(normal3[2])
        ax.plot_surface(X, Y, Z, cmap='Purples_r')
    else:
        Z=0
        
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")

    ax.set_title("System of Equations")

    plt.savefig("3dplot.png")
    img=Image.open("C:/Users/AGNISH MANDAL/Downloads/Pyworks/3dplot.png")
    img=img.resize((485,275))
    img=ImageTk.PhotoImage(img)    
    imagefix=Label(frame4,image=img)
    imagefix.image=img
    imagefix.pack()

#BUTTONS----
btn=Button(frame3,width=15,text="Plot",fg="white",activebackground="cadet blue1",bg="cadet blue3",font=("arial",10,"bold"),command=plot).grid(column=0,row=0)
btn=Button(frame3,width=15,text="Clear",fg="white",activebackground="red",bg="indian red",font=("arial",10,"bold"),command=clear).grid(column=0,row=1)
btn=Button(frame3,width=15,text="Solve",fg="white",activebackground="cadet blue1",bg="cadet blue3",font=("arial",10,"bold"),command=solve).grid(column=2,row=0)
btn=Button(frame3,width=15,text="Equation",fg="white",activebackground="cadet blue1",bg="cadet blue3",font=("arial",10,"bold"),command=eqn).grid(column=1,row=1)
btn=Button(frame3,width=15,text="Enter Matrix",fg="white",activebackground="cadet blue1",bg="cadet blue3",font=("arial",10,"bold"),command=apply).grid(column=1,row=0)


root.mainloop()
