from tkinter import *
from PIL import ImageTk,Image
import time
import numpy as np

root=Tk()
root.title("Baller")
root.geometry("960x480+250+200")
ico=Image.open("C:/Users/AGNISH MANDAL/Downloads/Pyworks/pixil-frame-0.png")
icon=ImageTk.PhotoImage(ico)
root.wm_iconphoto(False,icon)

theta=DoubleVar()

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
    vel=int(v.get())
    ang=int(theta.get())
    velx=vel*np.cos(np.radians(ang))
    vely=-(vel*np.sin(np.radians(ang)))
    y=0
    x=0
    dt=0.1
    tof=abs(2*vely/9.8)
    mh=vely**2/19.6
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
        vely=vely+9.8*dt
        x=velx*dt
        y=vely*dt+4.9*dt**2
        tim=str(t)  
        x_dist=str(r)
        t+=dt
        r+=x
        lbl=Label(frame2,text=tim,bg="gray12",fg="white",font=("arial",10)).place(x=0,y=190)
        lbl=Label(frame2,text=x_dist,bg="gray12",fg="white",font=("arial",10)).place(x=0,y=310)
            

        root.update()
        time.sleep(0.01)
    tof="~"+str(tof)
    mh=str(mh)
    ran="~"+str(ran)
    lbl=Label(frame2,text=tof,bg="gray12",fg="white",font=("arial",10)).place(x=0,y=210)
    lbl=Label(frame2,text=mh,bg="gray12",fg="white",font=("arial",10)).place(x=0,y=250)
    lbl=Label(frame2,text=ran,bg="gray12",fg="white",font=("arial",10)).place(x=0,y=330)
    
btn=Button(frame2,text="Launch!",bg="lawngreen",command=run).place(x=0,y=140)
root.mainloop()
