from tkinter import *
from PIL import ImageTk,Image
import time
import numpy as np

root=Tk()
root.title("Baller")
root.geometry("960x480+250+200")
ico=Image.open("C:/Users/AGNISH MANDAL/Downloads/Pyworks/pixil-frame-0 (2).ico")
icon=ImageTk.PhotoImage(ico)
root.wm_iconphoto(False,icon)

theta=DoubleVar()
global g
g=9.8

frame=Canvas(root,bg="black")
frame.place(height=480,width=720,x=0,y=0)
frame2=Frame(root,bg="gray12",borderwidth=5,relief=RIDGE)
frame2.place(x=720,y=0,height=480,width=240)
labv=Label(frame2,text="Velocity(m/s)",bg="gray12",fg="white",font=("arial",10)).place(x=0,y=30)
v=Entry(frame2,width=5,bg="slategrey",fg="white",font=("arial",10))
v.place(x=0,y=50)

scale=Scale(frame2,variable=theta,from_=0,to=180,fg="white",bg="gray12",label="Angle(in degrees)",length=220,orient=HORIZONTAL)
scale.place(x=0,y=80)

labt=Label(frame2,text="Time of Flight(s)",bg="gray12",fg="white",font=("arial",10)).place(x=0,y=170)
labh=Label(frame2,text="Max Height(m)",bg="gray12",fg="white",font=("arial",10)).place(x=0,y=230)
labr=Label(frame2,text="Range(m)",bg="gray12",fg="white",font=("arial",10)).place(x=0,y=290)

lbl_t=Label(frame2,text="",bg="gray12",fg="white",font=("arial",10))
lbl_t.place(x=0,y=210)
lbl_h=Label(frame2,text="",bg="gray12",fg="white",font=("arial",10))
lbl_h.place(x=0,y=250)
lbl_r=Label(frame2,text="",bg="gray12",fg="white",font=("arial",10))
lbl_r.place(x=0,y=330)

loc="C:/Users/AGNISH MANDAL/Downloads/Pyworks/pix-bag.png"
ball=Image.open("C:/Users/AGNISH MANDAL/Downloads/Pyworks/pixil-frame-0.png")
bac=Image.open(loc)
bac=bac.resize((720,480))
bac=ImageTk.PhotoImage(bac)   
fix=frame.create_image(0,0,image=bac,anchor=NW)
ball=ImageTk.PhotoImage(ball)
ballfix=frame.create_image(250,325,image=ball,anchor=NW)
width=ball.width()
height=ball.height()
def run():
    lbl_t.config(text="")
    lbl_h.config(text="")
    lbl_r.config(text="")
    try:
        vel=int(v.get())
    except ValueError:
        vel=0
    ang=int(theta.get())
    velx=vel*np.cos(np.radians(ang))
    vely=-(vel*np.sin(np.radians(ang)))
    y=0
    x=0
    dt=0.1
    tof=abs(2*vely/g)
    mh=vely**2/(2*g)
    ran=abs(velx*tof)
    t=0
    r=0
    h=0
    while True:
        cord=frame.coords(ballfix)
        if (cord[1]>325.5):
            frame.moveto(ballfix,cord[0],325)
            break
        if (cord[0]>720) or (cord[0]<0):
            frame.moveto(ballfix,250,cord[1])
            
        frame.move(ballfix,x,y)
        vely=vely+g*dt
        x=velx*dt
        y=vely*dt+(g/2)*dt**2
        tim=str(t)  
        x_dist=str(r)
        t+=dt
        r+=x
        lbl=Label(frame2,text=tim,bg="gray12",fg="white",font=("arial",10)).place(x=0,y=190)
        lbl=Label(frame2,text=x_dist,bg="gray12",fg="white",font=("arial",10)).place(x=0,y=310)
        root.update()
        time.sleep(0.01)

    tof="~"+str(tof)+" (True Value)"
    mh=str(mh)
    ran="~"+str(ran)+" (True Value)"
    lbl_t.config(text=tof)
    lbl_h.config(text=mh)
    lbl_r.config(text=ran)
def Center():
    frame.moveto(ballfix,250,325)
def g10():
    global g
    Center()
    g=10
    btng1.config(bg="white")
    btng2.config(bg="lawngreen") 
def g98():
    global g
    Center()
    g=9.8
    btng1.config(bg="lawngreen")
    btng2.config(bg="white")     
    
btn=Button(frame2,text="Launch!",bg="lawngreen",command=run).place(x=0,y=140)
btn=Button(frame2,width=7,text="Center",bg="lawngreen",command=Center).place(x=52,y=140)
btng1=Button(frame2,width=7,text="g=10",bg="lawngreen",command=g10)
btng1.place(x=110,y=140)
btng2=Button(frame2,width=7,text="g=9.8",bg="white",command=g98)
btng2.place(x=168,y=140)

root.mainloop()
