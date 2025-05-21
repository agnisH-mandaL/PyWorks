from tkinter import *
from tkinter import ttk


root=Tk()
root.title("Matrixer")
root.geometry("800x500+300+100")


#FRAMES----
frame1=Frame(root,relief=RIDGE,bd=5,bg="gray12")
frame1.place(height=450,width=395,x=5,y=15)
frame2=Frame(root,relief=RIDGE,bd=5,bg="gray12")
frame2.place(height=450,width=395,x=400,y=15)
frame3=Frame(root,relief=RIDGE,bd=3,bg="midnightblue")
frame3.place(height=63,width=385,x=405,y=400)

data_set=[]
rb=[]
lbl=Label(frame2,text="Enter elements of Matrix (row-wise) :",bg="gray12",font=("arial",10),fg="white").place(x=0,y=0)
lbl=Label(frame2,text="No. of columns:",bg="gray12",font=("arial",10),fg="white").place(x=0,y=110)
lbl=Label(frame2,text="Enter elements of b(Ax=b):",bg="gray12",font=("arial",10),fg="white").place(x=0,y=240)


entry=Entry(frame2,bg="slategrey",fg="white",font=("arial",10),width=53)
entry.place(x=5,y=20)
entry_b=Entry(frame2,bg="slategrey",fg="white",font=("arial",10),width=53)
entry_b.place(x=5,y=260)
#row=Entry(frame2,bg="slategrey",fg="white",font=("arial",10),width=3)
#row.place(x=0,y=130)
col=Entry(frame2,bg="slategrey",justify=CENTER,fg="white",font=("arial",10),width=3)
col.place(x=100,y=110)



global lbl_ds
lbl_ds=Label(frame2,text="Data set: ",fg="white",bg="gray12",font=("arial",10))
lbl_ds.place(x=0,y=40)

global lbl_b
lbl_b=Label(frame2,text="Data set: ",fg="white",bg="gray12",font=("arial",10))
lbl_b.place(x=0,y=280)

def enter():
    e=entry.get()
    data_set.append(e)
    x_="Data set: "+str(data_set)
    lbl_ds.config(text=x_)

def enterb():
    e=entry_b.get()
    rb.append(e)
    x_="Data set: "+str(rb)
    lbl_b.config(text=x_)

def clear():
    for widgets in frame1.winfo_children():
        widgets.destroy()
    lbl1.config(text="")
    lbl2.config(text="")
    lbl3.config(text="")
    lbl4.config(text="")
    lbl5.config(text="")

def eqn():
    global lbl1,lbl2,lbl3,lbl4,lbl5,lbl6
    global r1,r2,r3
    #e=int(row.get())
    j=int(col.get())
    r1=data_set[:j]
    r2=data_set[j:j*2]
    r3=data_set[j*2:j*3]
    lbl1=Label(frame2,text="Matrix entered:",font=("arial",10),fg="white",bg="gray12")
    lbl1.place(x=0,y=160)
    line_1=r1
    line_2=r2
    line_3=r3
    line_4="b="+str(rb)
    lbl2=Label(frame2,text=line_1,font=("arial",10),fg="white",bg="gray12")
    lbl2.place(x=0,y=180)
    lbl3=Label(frame2,text=line_2,font=("arial",10),fg="white",bg="gray12")
    lbl3.place(x=0,y=200)
    lbl4=Label(frame2,text=line_3,font=("arial",10),fg="white",bg="gray12")
    lbl4.place(x=0,y=220)
    lbl5=Label(frame2,text=line_4,font=("arial",10),fg="white",bg="gray12")
    lbl5.place(x=0,y=330)
def solveb():
    z=[]
    a=[float(i) for i in r1]
    b=[float(i) for i in r2]
    c=[float(i) for i in r3]
    r_b=[float(i) for i in rb]
    for j in range(0,len(a)):    
        if a[j]!=0:
            alpha=b[j]/a[j]
            beta=c[j]/a[j]
            gama=a[j]
            for i in range(0,len(a)):
                b[i]=b[i]-a[i]*alpha
                c[i]=c[i]-a[i]*beta
            r_b[1]=r_b[1]-r_b[0]*alpha
            r_b[2]=r_b[2]-r_b[0]*beta
            for i in range(0,len(a)):
                a[i]=a[i]/gama
            r_b[0]=r_b[0]/gama
            break

    #print(a,"\n",b,"\n",c,"\n", r_b)
    for j in range(0,len(b)):
        if b[j]!=0:
            alpha=c[j]/b[j]
            beta=a[j]/b[j]

            gama=b[j]
            for i in range(0,len(b)):
                c[i]=c[i]-b[i]*alpha
                a[i]=a[i]-b[i]*beta
            r_b[2]=r_b[2]-r_b[1]*alpha
            r_b[0]=r_b[0]-r_b[1]*beta
            for i in range(0,len(b)):
                b[i]=b[i]/gama
            r_b[1]=r_b[1]/gama
            break

   # print(a,"\n",b,"\n",c,"\n", r_b)
    for j in range(0,len(c)):
        if c[j]!=0:
            alpha=b[j]/c[j]
            beta=a[j]/c[j]
            gama=c[j]
            for i in range(0,len(c)):
                b[i]=b[i]-c[i]*alpha
                a[i]=a[i]-c[i]*beta
            r_b[1]=r_b[1]-r_b[2]*alpha
            r_b[0]=r_b[0]-r_b[2]*beta
            for i in range(0,len(c)):
                c[i]=c[i]/gama
            r_b[2]=r_b[2]/gama
            break

    #print(a,"\n",b,"\n",c,"\n", r_b)
    r=[a,b,c]
    a_=len(a)
    b_=len(a)
    c_=len(a)
    u=[a_,b_,c_]
    for i in range(0,len(r)):
        for j in range(0,len(a)):
            if r[i][j]!=0:
                u[i]=j
                break
            
    for i in range(0, len(u)-1):
        swapped=False
        for j in range(len(u)-1,i,-1):
            if u[j]<u[j-1]:
                u[j],u[j-1]=u[j-1],u[j]
                r[j],r[j-1]=r[j-1],r[j]
                r_b[j],r_b[j-1]=r_b[j-1],r_b[j]
                swapped=True
        if not swapped:
            break

    #print(r[0],"\n",r[1],"\n",r[2])    

    fv=[i for i in range(len(a)) if i not in u]
    pv=[i for i in u if i!=len(a)]        

    for i in range(0,len(fv)):
        z.append(chr(97+i))
        
    r_1=[]
    r_2=[]
    for i in range(len(pv)):
        x=[-(r[i][j]) for j in fv]
        y=[str(x[k])+str(z[k]) for k in range(len(x)) if x[k]!=0]
        r_1.append(y)
        r_2.append(x)
    #print(r_2)
    sol=[]
    p=0
    q=0
    for i in range(0, len(a)):
        if i in fv:
            x=0
            p+=1
        else:
            x=r_b[q]
            q+=1
        sol.append(x)
    #print(sol)

    p=[]
    q=[]
    s=[]
    d=0
    e=0
    t=0
    for i in range(0, len(a)):
        if i in fv: 
            if t==0:    
                p.append(1)
                q.append(0)
                s.append(0)
                t+=1
            elif t==1:
                p.append(0)
                q.append(1)
                s.append(0)
                t+=1
            elif t==2:
                 p.append(0)
                 q.append(0)
                 s.append(1)
        else:
            try:
                p.append(r_2[d][e])
                q.append(r_2[d][e+1])
                s.append(r_2[d][e+2])
            except IndexError:
                s.append(0)
            d+=1
    lbl=Label(frame1,text="Solution:",fg="white",bg="gray12",font=("arial",10)).place(x=0, y=160)
    lbl=Label(frame1,text=str(p),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=180)
    lbl=Label(frame1,text=str(q),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=200)
    lbl=Label(frame1,text=str(s),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=220)
    lbl=Label(frame1,text=str(sol),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=240)

    
def solve():
    z=[]
    a=[]
    b=[]
    c=[]
    
    
    for i in r1:
        a.append(float(i))
    for i in r2:
        b.append(float(i))
    for i in r3:
        c.append(float(i))
    for j in range(0,len(a)):    
        if a[j]!=0:
            alpha=b[j]/a[j]
            beta=c[j]/a[j]
            gama=a[j]
            for i in range(0,len(a)):
                b[i]=b[i]-a[i]*alpha
                c[i]=c[i]-a[i]*beta
            for i in range(0,len(a)):
                
                a[i]=a[i]/gama
            break

    print(a,"\n",b,"\n",c)
    for j in range(0,len(b)):
        if b[j]!=0:
            alpha=c[j]/b[j]
            beta=a[j]/b[j]
            gama=b[j]
            for i in range(0,len(b)):
                c[i]=c[i]-b[i]*alpha
                a[i]=a[i]-b[i]*beta
            for i in range(0,len(b)):
                b[i]=b[i]/gama
            break

    print(a,"\n",b,"\n",c)
    for j in range(0,len(c)):
        if c[j]!=0:
            alpha=b[j]/c[j]
            beta=a[j]/c[j]
            gama=c[j]
            for i in range(0,len(c)):
                b[i]=b[i]-c[i]*alpha
                a[i]=a[i]-c[i]*beta
            for i in range(0,len(c)):
                c[i]=c[i]/gama
            break

    print(a,"\n",b,"\n",c)
    r=[a,b,c]
    a_=len(a)
    b_=len(a)
    c_=len(a)
    u=[a_,b_,c_]
    for i in range(0,len(r)):
        for j in range(0,len(a)):
            if r[i][j]!=0:
                u[i]=j
                break
            
    for i in range(0, len(u)-1):
        swapped=False
        for j in range(len(u)-1,i,-1):
            if u[j]<u[j-1]:
                u[j],u[j-1]=u[j-1],u[j]
                r[j],r[j-1]=r[j-1],r[j]
                swapped=True
        if not swapped:
            break

    print(r[0],"\n",r[1],"\n",r[2])    

    fv=[i for i in range(len(a)) if i not in u]
    pv=[i for i in u if i!=len(a)]        

    for i in range(0,len(fv)):
        z.append(chr(97+i))
        
    s1=[]
    s2=[]
    for i in range(len(pv)):
        x=[-(r[i][j]) for j in fv]
        y=[str(x[k])+str(z[k]) for k in range(len(x)) if x[k]!=0]
        s1.append(y)
        s2.append(x)

    sol=[]
    p=0
    q=0
    for i in range(0, len(a)):
        if i in fv:
            x=z[p]
            p+=1
        else:
            x=s1[q]
            q+=1
        sol.append(x)
    print(sol)

    p=[]
    q=[]
    s=[]
    f=0
    e=0
    t=0
    for i in range(0, len(a)):
        if i in fv: 
            if t==0:    
                p.append(1)
                q.append(0)
                s.append(0)
                t+=1
            elif t==1:
                p.append(0)
                q.append(1)
                s.append(0)
                t+=1
            elif t==2:
                 p.append(0)
                 q.append(0)
                 s.append(1)
        else:
            try:
                p.append(s2[f][e])
                q.append(s2[f][e+1])
                s.append(s2[f][e+2])
            except IndexError:
                s.append(0)
            f+=1
    txt1="Rank="+str(len(pv))
    txt2="Dimension="+str(len(fv))
    lbl=Label(frame1,text="Basis vector:",fg="white",bg="gray12",font=("arial",10)).place(x=0, y=40)
    lbl=Label(frame1,text=str(p),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=60)
    lbl=Label(frame1,text=str(q),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=80)
    lbl=Label(frame1,text=str(s),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=100)
    lbl=Label(frame1,text=txt1,fg="white",bg="gray12",font=("arial",10)).place(x=0, y=120)
    lbl=Label(frame1,text=txt2,fg="white",bg="gray12",font=("arial",10)).place(x=0, y=140)
    return pv,fv
def delete():
    data_set.pop()
    x_="Data set: "+str(data_set)
    lbl_ds.config(text=x_)
def deleteb():
    rb.pop()
    x_="Data set: "+str(rb)
    lbl_b.config(text=x_)

    
#BUTTONS----
btn=Button(frame3,width=22,text="Clear",fg="white",activebackground="red",bg="indian red",font=("arial",10,"bold"),command=clear).place(x=0,y=28)
btn=Button(frame3,width=23,text="Solve(Ax=0)",fg="white",activebackground="medium spring green",bg="lime green",font=("arial",10,"bold"),command=solve).place(x=185,y=28)
btn=Button(frame3,width=22,text="Equation",fg="white",activebackground="cadet blue1",bg="cadet blue3",font=("arial",10,"bold"),command=eqn).place(x=0,y=0)
btn=Button(frame2,width=10,text="Enter",fg="white",activeforeground="lawngreen",activebackground="gray15",bg="gray20",font=("arial",10,"bold"),command=enter).place(x=0,y=70)
btn=Button(frame2,width=10,text="Enter",fg="white",activeforeground="lawngreen",activebackground="gray15",bg="gray20",font=("arial",10,"bold"),command=enterb).place(x=0,y=305)
btn=Button(frame2,width=10,text="Delete",fg="white",activeforeground="red",activebackground="gray15",bg="gray20",font=("arial",10,"bold"),command=delete).place(x=90,y=70)
btn=Button(frame2,width=10,text="Delete",fg="white",activeforeground="red",activebackground="gray15",bg="gray20",font=("arial",10,"bold"),command=deleteb).place(x=90,y=305)
btn=Button(frame3,width=23,text="General solution(Ax=b)",fg="white",bg="limegreen",activebackground="medium spring green",font=("arial",10,"bold"),command=solveb).place(x=185,y=0)


root.mainloop()
