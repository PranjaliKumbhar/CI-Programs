print("Enter the XOR Truth Table:")
x1=[]
x2=[]
y=[]

for i in range(0,4):
    i1=input("Enter values of X1:")
    x1.append(i1)

for i in range(0,4):
    i2=input("Enter values of X2:")
    x2.append(i2)


for i in range(0,4):
    i3=input("Enter values of Y:")
    y.append(i3)
    
print ("X1  X2   Y")
i=0
while i <=len(x1):
    
    print(x1[i]," ",x2[i],"  ",y[i])
    i=i+1
    if(i==len(x1)):
        break

alpha=0.2
w1=0.1
w2=0.3
theta=0.5
yin=[]
i=0
while i <=len(x1):
    yin_res=float(float(w1)*int(x1[i]))+float(float(w2)*int(x2[i]))
    yin.append(yin_res)
    i=i+1
    if(i==len(x1)):
        break
print(yin)
y_0=[]
i=0
while i <=len(x1):
    if(float(yin[i])>=float(theta)):
        y_0.append('1')
    else:
        y_0.append('0')

    i=i+1

    if(i==len(x1)):
        break


print(y_0)

print("Weight changes:")


        



