import math
import Mod as mod
import numpy as np
import NTT_init as init
from FFT import FFT

#calculate H(2) circulant matrix 
# this ROU  need to 2n-th root of unity
def bluestein_FFT_init(prime,ROU,n):
    h  = np.zeros((1,n),dtype = np.int64)
    IROU = mod.InvMod(ROU,prime) # inverse ROU
    print("IROU:",str(IROU))
    for i in range(n):
        exp = i ** 2
        tmp = mod.ExpMod(IROU,exp,prime)
        h[0][i] = tmp  
    L1  = 2*n-2  #calculate the length of H1
    S  = math.log2(L1)
    M  = 2**(math.ceil(S))
    h2 = np.zeros((1,M),dtype = np.int64)
    for j in range(M):   #generate circulant matrix
        if j < (n-1):
            h2[0][j] = h[0][j]
        elif (j >= (M-n+1)):
            h2[0][j] = h[0][M-j]
    print("h2:\n",h2)
    print("\n")
    ##doing FFT for h2
    #prime is another prime , another prime % M = 1
    p_pof2 = 1601 # power of 2  prime , p_pof2 % M =1
    ROU_pof2 = 1291 # 8-th root of unity
    h2_freq = FFT(h2,p_pof2,ROU_pof2,M,0) # doing FFT for h2
    print("f2_freq:\n",h2_freq)
    return h2_freq

#ROU: 2n-th root of unity
#prime:2n prime
def bluestein_FFT(x,ROU,prime,n,h2_freq):
    #power of 2 parameter
    p_pof2    = 1601
    #calculate M
    L1 = 2*n - 2
    S  = math.log2(L1)
    M  = 2 ** (math.ceil(S))
    print("M:",M)
    #calculate M-th root of unity
    ROU_pof2  = 1291
    IROU_pof2 = 1193
    y = np.zeros((1,M),dtype = np.int64)
    for i in range(n):
        exp = i ** 2
        tmp = mod.ExpMod(ROU,exp,prime)
        y[0][i] = mod.MulMod(tmp,x[0][i],prime)
    print("y:\n",y)
    Y = FFT(y,p_pof2,ROU_pof2,M,0) # FFT
    print("Y:\n",Y)
    Z = np.zeros((1,M),dtype = np.int64)
    for i in range(M):
        Z[0][i] = Y[0][i] * h2_freq[0][i] # element-wise multipy
    Z = Z % p_pof2
    print("Z:\n",Z)
    z = FFT(Z,p_pof2,IROU_pof2,M,1) # inverse-FFT
    print("z:\n",z)
    X = np.zeros((1,n))
    for j in range(n):
        exp = j ** 2
        tmp = mod.ExpMod(ROU,exp,prime)
        X[0][j] = mod.MulMod(tmp,z[0][j],prime)
    return X


prime = 11
ROU = 2
n = 5
M = 8
H2 = bluestein_FFT_init(prime ,ROU,n)
x = np.zeros((1,5))
x[0][0] = 1
x[0][1] = 1
print("x:\n",x)
X = bluestein_FFT(x,ROU,prime,n,H2)
print("X:\n",X)

