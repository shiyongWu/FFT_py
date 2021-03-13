
def AddMod(a,b,P):
    tmp = a + b
    tmp = tmp % P
    return tmp

def SubMod(a,b,P):
    tmp = a-b
    if(tmp < 0):
        tmp = tmp + P
    tmp = tmp % P
    return tmp

def DivMod(a,b,P):
    Ib  = InvMod(b,P)  #inverse b in finite filed P  {GF(P)}
    tmp = a * Ib
    tmp = tmp % P
    return tmp

def MulMod(a,b,P):
    if a<0 or b<0:
        print("a or b is negative number,return 0")
        return 0
    else:
        tmp = a*b
        tmp = tmp % P
        return tmp

def ExpMod(a,exp,P):
    tmp = a ** (exp)
    tmp = tmp % P
    return tmp

def InvMod(a,P):
    tmp = XGCD(a,P)
    return tmp

def XGCD(a,P):
    x0 = 1
    y0 = 0
    x1 = 0
    y1 = 1
    u  = a
    v  = P
    while u!= 0:
        q = v // u #only integer quotient
        r = v % u
        v = u
        u = r
        x2 = x0 - (q*x1)
        y2 = y0 - (q*y1)
        x0 = x1
        x1 = x2
        y0 = y1
        y1 = y2
        
    if(y0 < 0):
        y0 = y0 + P
    return y0 


