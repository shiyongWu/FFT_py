import Mod
import numpy as np
import NTT_init as init
from numpy.polynomial import Polynomial as poly

def NTT(x,ROU,prime,n,inverse): #output is a numpy array
    IN = Mod.InvMod(n,prime)    # calculate inverse multiplication of n
    x = x % prime
    y_list = []
    for i in range(n):
        acm = 0                             #accumlation 
        for j in range(n):
            exp = Mod.MulMod(i,j,n)          #calculates power of i*j
            tmp = Mod.ExpMod(ROU,exp,prime)  #calculates w^(i*j)
            tmp = Mod.MulMod(x[j],tmp,prime) #calculate x[j]w^(ij)
            acm = Mod.AddMod(acm,tmp,prime)  
        y_list.append(acm)
    y = np.array(y_list)
    if(inverse == 1):
        y = y * IN
        y = y % prime
    return y

#main
p  =  7  #prime #20231
n =  3
#init parameter
ROU  = init.n_ROU(p,4,n)
init.PROU(ROU,n,p)
print("ROU:",str(ROU))
IROU = Mod.InvMod(ROU,p)
print("IROU:",str(IROU))
'''
x = np.zeros(n,dtype = int)
x[0] = 1
x[1] = 1
x[2] = 1
print(x)
inverse = 0 
y = NTT(x,ROU,p,n,inverse)
print(y)
'''
