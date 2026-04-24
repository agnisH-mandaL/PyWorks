# =============================================================================
# This program represents a simulation of a robot with the
# objective to escape an obstacle layout under given constraints.
# =============================================================================


import matplotlib.pyplot as plt
import random as rn


n=int(input("Size of layout: "))

#Creation of obstacle layout
# layout=[[0,0,0,1],[0,0,0,0],[0,0,1,0],[1,1,1,1]]
layout=[[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        if (j==0 and i==0) or (j==n-1 and i==(n-2)) or (j==0 and i==(n-2)):
            continue
        layout[i][j]=rn.choice([0,1])

for i in range(len(layout)):
    print(*layout[i],end="  ",sep="  ")
    print()


x=0
y=0
c=0

stepx=1
stepy=0

print((x,y))
yp=[0]
xp=[0]

battery=25
while battery>0:
    battery-=1
    
    if (x+stepx==n and layout[y+1][n-1]==1) or (y+stepy==n and layout[n-1][x-1]==1) or (y+stepy<0 and layout[0][x+1]==1) or (x+stepx<0 and layout[y-1][3]==1) :
        print("Stuck")
        break
    if x<n-1 and y<n-1 :
        if (layout[y][x+1]==1 and layout[y+1][x]==1) :
            print("Stuck")
            break
    if y>0 and x>0:
        if (layout[y][x-1]==1 and layout[y-1][x]==1):
            print("Stuck")
            break
    if x+stepx==n:
        stepx=0
        stepy=1
        c+=1
        print("turn",c)
        continue
    if x+stepx<0:
        stepx=0
        stepy=-1
        c+=1
        print("turn",c)
        continue
    if y+stepy==n:
        stepx=-1
        stepy=0
        c+=1
        print("turn",c)
        continue
    if y+stepy<0:
        stepx=1
        stepy=0
        c=0
        print("turn",c)
        continue
    if layout[y+stepy][x+stepx]==0 :
        x+=stepx
        y+=stepy
    elif c==0:
        stepx=0
        stepy=1
        c+=1
        print("turn",c)
        continue
    elif c==1:
        stepx=-1
        stepy=0
        c+=1
        print("turn",c)
        continue
    elif c==2:
        stepx=0
        stepy=-1
        c+=1
        print("turn",c)
        continue
    elif c==3:
        stepx=1
        stepy=0
        c=0
        print("turn",c)
        continue
    else :
        print("Stuck")
        break
    print((x,y))
    yp.append(y)
    xp.append(x)
    if (x==0 and y==(n-2)) or (x==(n-1) and y==n-2):
        print("Exit Successfully")
        break

if battery==0:
    print("Battery exhausted")
y0=[]
x0=[]
for i in range(n):
    for j in range(n):
        if layout[i][j]==0:
            x0.append(j)
            y0.append(i)

y1=[]
x1=[]
for i in range(n):
    for j in range(n):
        if layout[i][j]==1:
            x1.append(j)
            y1.append(i)
            
plt.scatter(x1,y1,label="Obstacle")
plt.scatter(x0,y0,label="Free path")
plt.scatter(xp,yp,label="Path ventured")
plt.legend()
plt.xlabel("X-axis")
plt.xlabel("Y-axis")
plt.title("Path Simulation")
plt.grid()
plt.text(0,n-2,"Exit-1")
plt.text(n-1,n-2,"Exit-2")
plt.text(0,0,"Start")
plt.gca().invert_yaxis()


        
        
        
        
        