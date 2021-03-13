###MY HW5

#Ben Moreau

import numpy as np
import scipy as sp

Areas=[]
N=1000
for jj in range(2,N):
    
    def NonTrivial(i):
        return i**2+1

    ys= NonTrivial(np.linspace(-1,1,jj))

    from matplotlib import pyplot as plt

    def f(i,mx):
        return np.exp(np.sqrt((-i)**2))*mx

    fs=f(np.linspace(-1,1,jj),max(ys))

    def Prob(i,mx):
        return np.random.randint(0,10**6*np.exp(np.sqrt((-i)**2)))/10**6*mx


    prob= Prob(np.linspace(-1,1,jj),max(ys))
    '''
    def Prob2(i,mx):
        return np.random.randint(0,10**6*(-np.exp(np.sqrt((.5-i)**2))+np.exp(1)))/10**6*mx
        
    prob2= Prob2(np.linspace(0,1,10000),max(ys))
    '''
    passes=0
    total=0
    x=-1

    greens=[]
    greensx=[]
    for i in range(len(prob)):
        if(prob[i]<x**2+1):
            passes+=1
            greens.append(prob[i])
            greensx.append(x)
        total+=1    
        x+=2/len(prob)
    Areas.append(np.trapz(fs,np.linspace(-1,1,jj))*passes/total)

#print("The amount of points that pass is ",passes," out of",total,"points, and the total area under our f is ",np.trapz(fs,np.linspace(-1,1,10000)),"so the area of abs(sin(pi*x) from zero to one is ", np.trapz(fs,np.linspace(-1,1,10000))*passes/total)

print("The MC integral gives: ",Areas[N-5])
plt.scatter(np.linspace(2,N,N-2),Areas,label="Result of MC integration")
plt.xlabel("Number of points")
plt.ylabel("Area")

### My HW6

#Ben Moreau


from math import  *



xi=[0,-1/3*sqrt(5-2*sqrt(10/7)),-1/3*sqrt(5+2*sqrt(10/7)),1/3*sqrt(5-2*sqrt(10/7)),1/3*sqrt(5+2*sqrt(10/7))]
wi=[128/225,322/900+13*sqrt(70)/900,322/900-13*sqrt(70)/900]

Area=0
Area+=NonTrivial(xi[0])*wi[0]
Area+=NonTrivial(xi[1])*wi[1]
Area+=NonTrivial(xi[2])*wi[2]
Area+=NonTrivial(xi[3])*wi[1]
Area+=NonTrivial(xi[4])*wi[2]

A=[]
x=[]
for i in range(N):
    x.append(i)
    A.append(Area)
print("The gaussian integral gives: ",Area)
plt.scatter(x,A,label="Gaussian Result")
plt.legend()
plt.show()
