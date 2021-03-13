#fast fourier transform over finite field
import Mod
import math
import numpy as np

def BU(A,B,P):  #radix-2 butterfly unit
    tmp_ay = np.zeros((1,2),dtype = int) #tmp_array
    tmp_a = Mod.AddMod(A,B,P)
    tmp_b = Mod.SubMod(A,B,P)
    tmp_ay[0][0] = tmp_a  #a+b
    tmp_ay[0][1] = tmp_b  #a-b
    return tmp_ay 


def FFT(Array,P,root,N,inverse):     #radix-2 FFT
    # If inverse = 1, doing IFFT.
    # automatically compute inverse ROU.
    # root : foward root of unity
    # N : array length
    # P :Prime
    S  = math.ceil(math.log2(N))   #Stage
    bias = N
    A_t = np.zeros((1,bias),dtype = int)
    
    #if inverse = 1,compute inverse ROU
    if(inverse ==1):
        root = Mod.InvMod(root,P)
        
    # DIT
    for i in range(S):
        nc = N//bias  #number of class
        ne = bias    #number of elements (in a class)
        A_t= np.reshape(A_t,(nc,ne))  # reshape array  
        bias = bias >> 1      # each stage right shift one bit
   
        for j in range(nc):
            for jj in range(ne):
                index_tmp  = j*ne +jj
                A_t[j][jj] = Array[0][index_tmp]
        
        if(i==0):
            factor = root
        else:
            factor = Mod.MulMod(factor,factor,P)

        for s in range(nc):
            for ss in range(ne//2):
                tmp = BU(A_t[s][ss],A_t[s][ss+bias],P)
                factor_t = Mod.ExpMod(factor,ss,P)
                A_t[s][ss] = tmp[0][0]
                A_t[s][ss+bias] = tmp[0][1]
                A_t[s][ss+bias] = Mod.MulMod(A_t[s][ss+bias],factor_t,P)
                
        for x in range(nc):
            for y in range(ne):
                Array[0][x*ne + y] = A_t[x][y]

    #data relocation
    #bitreverse
    for i in range(N):
        p_tmp = i
        exchange_position = 0
        for ls in range(S):
            bit = p_tmp % 2
            bit_weight = 1 << ((S-1)-ls)
            if(bit == 1):
                exchange_position = exchange_position + bit_weight
            else:
                exchange_position = exchange_position
            p_tmp = p_tmp >> 1

        if (exchange_position > i):
           tmp = Array[0][i]
           Array[0][i] = Array[0][exchange_position]
           Array[0][exchange_position] = tmp
           
    #inverse FFT need to multiply each element by 1/n
    if(inverse ==1):
        IN = Mod.InvMod(N,P)
        Array = Array * IN
        Array = Array % P
    return Array
