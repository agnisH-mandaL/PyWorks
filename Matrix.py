a=[]
print("Enter values for matrix one")
for i in range(1,10):
    x=int(input())
    a.append(x)
print(a[0:3])
print(a[3:6])
print(a[6:9])
b=[]
print("Enter values for matrix two")

for i in range(1,10):
    x=int(input())
    b.append(x)
print(b[0:3])
print(b[3:6])
print(b[6:9])

def mul():
    c=[]
    v=0
    for i in range(0,9):
        y=0
        v=i%3
        if i<3:
            u=0
        elif i<6 and i>=3:
            u=3
        else:
            u=6     
        for j in range(0,3):
            y+=a[u]*b[v]
            u+=1
            v+=3
        c.append(y)
    print("Product:")  
    print(c[0:3])
    print(c[3:6])
    print(c[6:9])
def add():
    c=[]
    v=0
    u=0

    for i in range(0,9):
        y=a[u]+b[v]
        u+=1
        v+=1
        c.append(y)
        
    print("Sum:")  
    print(c[0:3])
    print(c[3:6])
    print(c[6:9])
y=1
while y==1:
    print("1.Multiply")
    print("2.Add")
    n=int(input("Enter number according to options:"))
    if n==1:
        mul()
    if n==2:
        add()
    m=input("Want to end?")
    if m=="y":
        y=2