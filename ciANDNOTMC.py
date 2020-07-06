print("Enter the ANDNOT Truth Table:")
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
    
print ("X1  X2  Y")
i=0
while i <=len(x1):
    
    print(x1[i]," ",x2[i]," ",y[i])
    i=i+1
    if(i==len(x1)):
        break


print("Assume Both weights are excitory i.e w1=w2=1")
yin=[]
w1=1
w2=1
i=0
while i <=len(x1):
    add=int(x1[i]*w1)+int(x2[i]*w2)
    print("yin=",x1[i],"*",w1,"+",x2[i],"*",w2,"=",add)
    i=i+1
    if(i==len(x1)):
        break
print ("These weights are not suitable")

print("Assume one weight excitory and other inhibitory i.e w1=1 & w2=-1")

w1=1
w2=-1
i=0

while i <=len(x1):
    a=int(x2[i])*int(w2)
    add=int(x1[i]*w1)+a
    print("yin=",x1[i],"*",w1,"+",x2[i],"*",w2,"=",add)
    i=i+1
    if(i==len(x1)):
        break

print ("These weights are suitable and value of \u03B8=1")





