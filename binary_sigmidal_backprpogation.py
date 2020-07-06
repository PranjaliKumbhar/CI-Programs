import math

#input
print("Enter weights of layer1 of 1 i.e weights of X1:")
x1=[]
i=1
while i<=3:
    print("v1",i)
    x11=float(input("Enter value:"))
    x1.append(x11)
    i=i+1
    if(i==3):
        break
    
print("Enter weights of layer1 of 2 i.e weights of X2:")
x2=[]
i=1
while i<=3:
    print("v2",i)
    x22=float(input("Enter value:"))
    x2.append(x22)
    i=i+1
    if(i==3):
        break
    
#weights
print("Enter weights of hidden layer:")
w=[]
i=1
while i<=3:
    print("W",i)
    w11=float(input("Enter value:"))
    w.append(w11)
    i=i+1
    if(i==3):
        break


#target output
t_out=int(input("Enter target output:"))

#larning_rate 0.45
l_rate=float(input("Enter learning rate:"))

#input pattern
print("Enter input pattern:")
input_pat=[]
i=1
while i<=3:
    print("W",i)
    ip=float(input("Enter value:"))
    input_pat.append(ip)
    i=i+1
    if(i==3):
        break

#bias values for hidden layer
v01=float(input("Enter bias1:"))
v02=float(input("Enter bias1:"))

#bias value of output layer
w0=float(input("Enter output layer bias:"))

#calculate net input to hidden layer
print("Step 1:Calculate net input to z1 layer")
print("zin1 =")
zin1=v01+(input_pat[0]*x1[0])+(input_pat[1]*x2[0])
print(zin1)
print("zin2 =")
zin2=v02+(input_pat[0]*x1[1])+(input_pat[1]*x2[1])
print(zin2)

#Apply activation function
print("Step2:Apply activation function to calculated output")

#z1=f(zin1)=(1/1+e^-zin1)

print("z1=")
z1=(1/(1+math.exp(-zin1)))
print(z1)

print("z2=")
z2=(1/(1+math.exp(-zin2)))
print(z2)


#calculate net input to output layer for 'y' layer
print("Step3: Calculate net input to output layer")

print("yin=")
yin=w0+(z1*w[0])+(z2*w[1])
print(yin)


#calculate net output
print("Step4:Calculate net output")

#y=f(yin)=(1/1+e^-yin)

print("y=")
y=(1/(1+math.exp(-yin)))
print(y)

#check whether it is matching with target output

if y ==t_out:
    print("Target output",t_out," is equal to calculated output",y)
    exit(0)
else:
    print("Target output",t_out,"is not equal to calculated output",y)
    print("Error is present")

#compute error deltak
print("Step 5:Compute error")
print("deltak=")


dk=(t_out-y)*((y*(1-y)))
print(dk)

#find changes in weights between hidden and output layer

print("Step 6:Find changes in weights between hidden and output layer")

print("deltaw1 =")
dw1=l_rate*dk*z1
print(dw1)

print("deltaw2 =")
dw2=l_rate*dk*z2
print(dw2)

print("deltaw0 =")
dw0=l_rate*dk
print(dw0)


#Compute error between hidden & input layer
print("Step 7:Compute error between hidden & input layer")
print("din1=")
din1=dk*w[0]
print(din1)

print("din2=")
din2=dk*w[1]
print(din2)


#error delta1=deltain1*f'(zin1)
print("Delta 1=")
d1=din1*((z1*(1-z1)))
print(d1)

print("Delta 2=")
d2=din2*((z2*(1-z2)))
print(d2)

#find changes in weights between input and hidden layer
print("Step 8:find changes in weights between input and hidden layer")

#delta_v11=alpha*delta1*x1
print("delta_v11 =")
dv11=l_rate*d1*input_pat[0]
print(dv11)
print("delta_v21 =")
dv21=l_rate*d1*input_pat[1]
print(dv21)
print("delta_v01 =")
dv01=l_rate*d1
print(dv01)
print("delta_v12 =")
dv12=l_rate*d2*input_pat[0]
print(dv12)
print("delta_v22 =")
dv22=l_rate*d2*input_pat[1]
print(dv22)
print("delta_v02 =")
dv02=l_rate*d2
print(dv02)

#Compute final weights of the network
print("Step 9:Compute final weights of network")
print("v11(new) =")
v11n=x1[0]+dv11
print(v11n)

print("v12(new) =")
v12n=x1[1]+dv12
print(v12n)

print("v21(new) =")
v21n=x2[0]+dv21
print(v21n)

print("v22(new) =")
v22n=x2[1]+dv22
print(v22n)

print("w1(new) =")
w1n=w[0]+dw1
print(w1n)

print("w2(new) =")
w2=w[1]+dw2
print(w2)

print("v01(new) =")
v01n=v01+dv01
print(v01n)

print("v02(new) =")
v02n=v02+dv02
print(v02n)

print("w0(new) =")
w0n=w0+dw0
print(w0n)










