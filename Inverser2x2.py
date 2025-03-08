a=[]
ac=[]
b=[1,0,0,1]
print("Enter elements of matrix row wise(ex: for 1st row elements [1 2 3], enter 1 then 2 then 3 and so on):")

for i in range(0,4):
    n=float(input())
    a.append(n)
print(a[0:2])
print(a[2:4])

for i in range(0,4):
    ac.append(a[i])
    
def show():   
    print(a[0:2],"|",b[0:2])
    print(a[2:4],"|",b[2:4])
    
def mul(a,b):
    c=[]
    v=0
    for i in range(0,4):
        y=0
        v=i%2
        if i<2:
            u=0
        else:
            u=2
        for j in range(0,2):
            y+=a[u]*b[v]
            u+=1
            v+=2
        c.append(y)
    print("Product of A and its inverse:")  
    print(c[0:2])
    print(c[2:4])


if (a[0]*a[3]-a[1]*a[2])==0:
    print("Matrix is not invertible")
else:
    if a[0]==0 and a[2]!=0:
        #R2<->R1
        c=a[0:2]
        a[0:2]=a[2:4]       
        a[2:4]=c[0:2]
        c_=b[0:2]
        b[0:2]=b[2:4]
        b[2:4]=c_[0:2]
        show()
        print()
    if a[0]!=1:
        if a[0]<a[2]:
            #R2<->R1
            c=a[0:2]
            a[0:2]=a[2:4]
            a[2:4]=c[0:2]
            c_=a[0:2]
            b[0:2]=b[2:4]
            b[2:4]=c_[0:2]
        d=(a[0]-1)/a[2]
        show()
        print()
        #R1->R1-dR2
        for i in range(0,2):
            a[i]=a[i]-a[i+2]*d
            b[i]=b[i]-b[i+2]*d
        show()
        print()
    if a[2]!=0:
        #R2->R2-dR1
        d=a[2]/a[0]
        for i in range(2,4):
            a[i]=a[i]-a[i-2]*d
            b[i]=b[i]-b[i-2]*d
        show()
        print()
    if a[3]!=0:
        #R2->d*R2  s.t. 2nd row-[0,1]
        b[2]=b[2]/a[3]
        b[3]=b[3]/a[3]
        a[3]=a[3]/a[3]
        
        show()
        print()
    if a[1]!=0:
        #R1->R1-dR2
        b[1]=b[1]-b[3]*a[1]
        b[0]=b[0]-b[2]*a[1]
        a[1]=a[1]-a[3]*a[1]
        show()
        print()
       
    mul(ac,b)
print("The inverse of the matrix:")
print(b[0:2])
print(b[2:4])
