import Mod 

#find n-th root of unity function
def n_ROU(Prime,comprime,n):
    if((Prime % n) != 1):
        print("ERROR!!,n is not factor of (Prime-1) ")
    i = (Prime - 1)//n  ##integer quotient
    ROU = Mod.ExpMod(comprime,i,Prime)
    return ROU

#test primivite n-th roots of unity
def PROU(ROU,n,Prime):
    f = open('ROU_table.txt','w')
    if((n%2) == 0):
        for i in range(n):
            tmp = Mod.ExpMod(ROU,i,Prime)
            print(i,"-th: ",tmp)
            ch = str(tmp)
            f.write(ch)
            f.write("\n")
            if tmp == 1 and i != 0:
                print("it is not primitive root of unity")
    else:
        for i in range(n):
            tmp = Mod.ExpMod(ROU,i,Prime)
            ch = str(tmp)
            f.write(ch)
            f.write("\n")
            if tmp==1 and i != 0:
                print("it is not primitve root of unity")
    return 0
##test parameter
Prime = 17
n = 16
for a  in range(2,Prime):
    print("a:",a)
    ROU = n_ROU(Prime,a,n)
    print("16-th ROU:",ROU)
    PROU(ROU,n,Prime)


