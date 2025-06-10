from tkinter import *
from tkinter import ttk


root=Tk()
root.title("Matrixer")
root.geometry("800x600+300+100")


#FRAMES----
frame1=Frame(root,relief=RIDGE,bd=5,bg="gray12")
frame1.place(height=480,width=395,x=5,y=15)
frame2=Frame(root,relief=RIDGE,bd=5,bg="gray12")
frame2.place(height=480,width=395,x=400,y=15)
frame3=Frame(root,relief=RIDGE,bd=3,bg="midnightblue")
frame3.place(height=63,width=790,x=5,y=495)

data_set=[]
rb=[]
rows=[]

lbl=Label(frame2,text="Enter elements of Matrix (row-wise) :",bg="gray12",font=("arial",10),fg="white").place(x=0,y=0)
lbl=Label(frame2,text="No. of columns:",bg="gray12",font=("arial",10),fg="white").place(x=0,y=110)

lbl=Label(frame2,text="Enter elements of b(Ax=b):",bg="gray12",font=("arial",10),fg="white").place(x=0,y=320)

lbl=Label(frame2,text="No. of rows:",bg="gray12",font=("arial",10),fg="white").place(x=130,y=110)

entry=Entry(frame2,bg="slategrey",fg="white",font=("arial",10),width=53)
entry.place(x=5,y=20)
entry_b=Entry(frame2,bg="slategrey",fg="white",font=("arial",10),width=53)
entry_b.place(x=5,y=350)
row=Entry(frame2,bg="slategrey",justify=CENTER,fg="white",font=("arial",10),width=3)
row.place(x=210,y=110)
col=Entry(frame2,bg="slategrey",justify=CENTER,fg="white",font=("arial",10),width=3)
col.place(x=100,y=110)


global lbl_ds
lbl_ds=Label(frame2,text="Data set: ",fg="white",bg="gray12",font=("arial",10))
lbl_ds.place(x=0,y=40)

global lbl_b
lbl_b=Label(frame2,text="Data set: ",fg="white",bg="gray12",font=("arial",10))
lbl_b.place(x=0,y=375)

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
    lines=[]
    j=int(col.get())
    k=int(row.get())
    for i in range(1,k+1):
        rowx=data_set[j*(i-1):j*i]
        rows.append(rowx)
    for i in range(7):
        try:
            lines.append(rows[i])
        except:
            lines.append("")
    lbl1=Label(frame2,text="Matrix entered:",font=("arial",10),fg="white",bg="gray12")
    lbl1.place(x=0,y=160)
    line_4="b="+str(rb)
    lbl2=Label(frame2,text=lines[0],font=("arial",10),fg="white",bg="gray12")
    lbl2.place(x=0,y=180)
    lbl3=Label(frame2,text=lines[1],font=("arial",10),fg="white",bg="gray12")
    lbl3.place(x=0,y=200)
    lbl4=Label(frame2,text=lines[2],font=("arial",10),fg="white",bg="gray12")
    lbl4.place(x=0,y=220)
    lbl5=Label(frame2,text=lines[3],font=("arial",10),fg="white",bg="gray12")
    lbl5.place(x=0,y=240)
    lbl5=Label(frame2,text=lines[4],font=("arial",10),fg="white",bg="gray12")
    lbl5.place(x=0,y=260)
    lbl5=Label(frame2,text=lines[5],font=("arial",10),fg="white",bg="gray12")
    lbl5.place(x=0,y=280)
    lbl5=Label(frame2,text=lines[6],font=("arial",10),fg="white",bg="gray12")
    lbl5.place(x=0,y=300)
    lbl5=Label(frame2,text=line_4,font=("arial",10),fg="white",bg="gray12")
    lbl5.place(x=0,y=440)
def solveb():
    z=[]
    d=[]
    j=0
    while True:
        rowx=[float(i) for i in rows[j]]
        d.append(rowx)
        j+=1
        if j==len(rows):
            break

    r_b=[float(i) for i in rb]
    
    l=len(rows[0])
    
    #Echelon row reduction--
    for k in range(0,len(d)):           
        for j in range(l):      
            if d[k][j]!=0:
                gama=d[k][j]
                for i in range(len(d)):      
                    if d[i]!=d[k]:
                        alpha=d[i][j]/gama
                        for m in range(l):
                            d[i][m]=d[i][m]-d[k][m]*alpha
                        r_b[i]=r_b[i]-r_b[k]*alpha
                for m in range(l):
                    d[k][m]=d[k][m]/gama
                r_b[k]=r_b[k]/gama
                break
    
    r=d
    u=[l for i in range(len(r))]
    for i in range(0,len(r)):
        for j in range(0,l):
            if r[i][j]!=0:
                u[i]=j
                break
    #Sorting rows in ascending order of indices of occurence of first non-zero entry
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
    
    #Declaration of free variables and pivot variables indices
    fv=[i for i in range(l) if i not in u]
    pv=[i for i in u if i!=l]        

    for i in range(0,len(fv)):
        z.append(chr(97+i))
        
    r_1=[]
    r_2=[]
    
    #Declaration of pivot variables in terms of free variables
    for i in range(len(pv)):
        x=[-(r[i][j]) for j in fv]
        y=[str(x[k])+str(z[k]) for k in range(len(x)) if x[k]!=0]
        r_1.append(y)
        r_2.append(x)
    #print(r_2)
    sol=[]
    p=0
    q=0
    
    #Particular solution--
    for i in range(0,l):
        if i in fv:
            x=0
            p+=1
        else:
            x=r_b[q]
            q+=1
        sol.append(x)
    #print(sol)


    d=0
    e=0
    t=0
    basis=[[] for i in range(len(r))]
    #Solutions--
    for i in range(0,l):
        if i in fv: 
            for k in range(len(r)):
                if t==k:
                    for j in range(len(r)):    
                        if j==t:    
                            basis_dat=1
                        else:
                            basis_dat=0
                        basis[j].append(basis_dat)
                    t+=1
                    break
        else:
            try:
                for i in range(len(r)):
                    basis[i].append(r_2[d][e+i])
            except IndexError:
                pass
            d+=1             
 
    lines=[]
    for i in range(7):
        try:
            lines.append(basis[i])
        except:
            lines.append("")        
    lbl=Label(frame1,text="Solution:",fg="white",bg="gray12",font=("arial",10)).place(x=0, y=240)
    lbl=Label(frame1,text=str(lines[0]),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=260)
    lbl=Label(frame1,text=str(lines[1]),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=280)
    lbl=Label(frame1,text=str(lines[2]),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=300)
    lbl=Label(frame1,text=str(lines[3]),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=320)
    lbl=Label(frame1,text=str(lines[4]),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=340)
    lbl=Label(frame1,text=str(lines[5]),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=360)
    lbl=Label(frame1,text=str(lines[6]),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=380)
    lbl=Label(frame1,text=str(sol),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=400)
    
def solve():
    z=[]
    d=[]
    j=0
    while True:
        rowx=[float(i) for i in rows[j]]
        d.append(rowx)
        j+=1
        if j==len(rows):
            break
   
    l=len(rows[0])
    #d=[a,b,c]
    for k in range(0,len(d)):
        for j in range(l):      
            if d[k][j]!=0:
                gama=d[k][j]
                for i in range(len(d)):      
                    if d[i]!=d[k]:
                        alpha=d[i][j]/gama
                        for m in range(l):
                            d[i][m]=d[i][m]-d[k][m]*alpha
                for m in range(l):
                    d[k][m]=d[k][m]/gama
                break
    
    r=d
    u=[l for i in range(len(r))]
    for i in range(0,len(r)):
        for j in range(0,l):
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

    fv=[i for i in range(l) if i not in u]
    pv=[i for i in u if i!=l]        

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
    for i in range(0, l):
        if i in fv:
            x=z[p]
            p+=1
        else:
            x=s1[q]
            q+=1
        sol.append(x)
    print(sol)

    d=0
    e=0
    t=0
    basis=[[] for i in range(len(r))]
    #Solutions--
    for i in range(0,l):
        if i in fv: 
            for k in range(len(r)):
                if t==k:
                    for j in range(len(r)):    
                        if j==t:    
                            basis_dat=1
                        else:
                            basis_dat=0
                        basis[j].append(basis_dat)
                    t+=1
                    break
        else:
            try:
                for i in range(len(r)):
                    basis[i].append(s2[d][e+i])
            except IndexError:
                pass
            d+=1       
    lines=[]
    for i in range(7):
        try:
            lines.append(basis[i])
        except:
            lines.append("")
    txt1="Rank="+str(len(pv))
    txt2="Dimension="+str(len(fv))
    lbl=Label(frame1,text="Basis vector:",fg="white",bg="gray12",font=("arial",10)).place(x=0, y=40)
    lbl=Label(frame1,text=str(lines[0]),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=60)
    lbl=Label(frame1,text=str(lines[1]),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=80)
    lbl=Label(frame1,text=str(lines[2]),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=100)
    lbl=Label(frame1,text=str(lines[3]),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=120)
    lbl=Label(frame1,text=str(lines[4]),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=140)
    lbl=Label(frame1,text=str(lines[5]),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=160)
    lbl=Label(frame1,text=str(lines[6]),fg="lawngreen",bg="gray12",font=("arial",10)).place(x=0, y=180)
    lbl=Label(frame1,text=txt1,fg="white",bg="gray12",font=("arial",10)).place(x=0, y=200)
    lbl=Label(frame1,text=txt2,fg="white",bg="gray12",font=("arial",10)).place(x=0, y=220)
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
btn=Button(frame3,width=22,text="Clear",fg="white",activebackground="red",bg="indian red",font=("arial",10,"bold"),command=clear).place(x=395,y=28)
btn=Button(frame3,width=24,text="Solve(Ax=0)",fg="white",activebackground="medium spring green",bg="lime green",font=("arial",10,"bold"),command=solve).place(x=580,y=28)
btn=Button(frame3,width=22,text="Equation",fg="white",activebackground="cadet blue1",bg="cadet blue3",font=("arial",10,"bold"),command=eqn).place(x=395,y=0)
btn=Button(frame2,width=10,text="Enter",fg="white",activeforeground="lawngreen",activebackground="gray15",bg="gray20",font=("arial",10,"bold"),command=enter).place(x=0,y=70)
btn=Button(frame2,width=10,text="Enter",fg="white",activeforeground="lawngreen",activebackground="gray15",bg="gray20",font=("arial",10,"bold"),command=enterb).place(x=0,y=405)
btn=Button(frame2,width=10,text="Delete",fg="white",activeforeground="red",activebackground="gray15",bg="gray20",font=("arial",10,"bold"),command=delete).place(x=90,y=70)
btn=Button(frame2,width=10,text="Delete",fg="white",activeforeground="red",activebackground="gray15",bg="gray20",font=("arial",10,"bold"),command=deleteb).place(x=90,y=405)
btn=Button(frame3,width=24,text="General solution(Ax=b)",fg="white",bg="limegreen",activebackground="medium spring green",font=("arial",10,"bold"),command=solveb).place(x=580,y=0)

root.mainloop()
