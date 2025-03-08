a=[]
ac=[]
print("Enter elements of matrix row wise(ex: for 1st row elements [1 2 3], enter 1 then 2 then 3 and so on):")

for i in range(0,9):
    n=float(input())
    a.append(n)
for i in range(0,9):
    ac.append(a[i])
b=[1,0,0,0,1,0,0,0,1]

def show():   
    print(a[0:3],"|",b[0:3])
    print(a[3:6],"|",b[3:6])
    print(a[6:9],"|",b[6:9])
    
def mul(a,b):
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
    print("Product of A and its inverse:")  
    print(c[0:3])
    print(c[3:6])
    print(c[6:9])

if (a[0]*(a[4]*a[8]-a[5]*a[7])+a[1]*(a[5]*a[6]-a[3]*a[8])+a[2]*(a[3]*a[7]-a[4]*a[6]))==0:
    print("Matrix is not invertible")
else:
    show()
    if a[0]==0 and a[3]!=0:
        c=a[0:3]
        a[0:3]=a[3:6]       
        a[3:6]=c[0:3]
        c_=b[0:3]
        b[0:3]=b[3:6]
        b[3:6]=c_[0:3]
        show()
        print()
    if a[0]==0 and a[3]==0:
        c=a[0:3]
        a[0:3]=a[6:9]       
        a[6:9]=c[0:3]
        c_=b[0:3]
        b[0:3]=b[6:9]
        b[6:9]=c_[0:3]
        show()
        print()
        
    if a[0]!=0:       
        d=a[6]/a[0]
        for i in range(6,9):
            a[i]=a[i]-a[i-6]*d
            b[i]=b[i]-b[i-6]*d
        show()
        print() 
    if a[0]!=0:
        d=a[3]/a[0]
        for i in range(3,6):
            a[i]=a[i]-a[i-3]*d
            b[i]=b[i]-b[i-3]*d
        show()
    print()
    d=a[7]/a[4]
    for i in range(6,9):
        a[i]=a[i]-a[i-3]*d
        b[i]=b[i]-b[i-3]*d
    show()
    print()
    d=1/a[8]
    for i in range(6,9):
        a[i]=a[i]*d
        b[i]=b[i]*d
    show()
    print()
    d=a[5]
    for i in range(3,6):
        a[i]=a[i]-a[i+3]*d
        b[i]=b[i]-b[i+3]*d
    show()
    print()
    d=1/a[4]
    for i in range(3,6):
        a[i]=a[i]*d
        b[i]=b[i]*d
    show()
    print()
        
    d=a[2]
    d_=a[1]
    for i in range(0,3):
        a[i]=a[i]-a[i+6]*d-a[i+3]*d_
        b[i]=b[i]-b[i+6]*d-b[i+3]*d_
    show()
    print()
    d=1/a[0]
    for i in range(0,3):
        a[i]=a[i]*d
        b[i]=b[i]*d
    show()
    print()
    mul(ac,b)
print("The inverse of the matrix:")
print(b[0:3])
print(b[3:6])
print(b[6:9])