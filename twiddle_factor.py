def expmod(prime,comprime,exp):
    tmp = comprime ** (exp)
    tw = tmp % prime
    print(str(tw))
    return tw

def test_tw(tw,length,prime):
    f = open('tw_table.txt','w')
    for i in range(length):
          tmp = tw ** (i)
          tmp = tmp %  prime
          ch = str(tmp)
          f.write(ch)
          f.write("\n")
          if tmp == 1 and i != 0: 
             print("it is not twiddle factor")
    f.close()
    return 0

def n_th_ROU(tw,length,prime):
    tmp = tw ** (length)
    tmp = tmp % prime
    if tmp == 1:
        print(str(tmp))
        print("it is n-th root of unity")
    else:
        print("tmp is ",str(tmp))
        print("it is not n-th root of unity")

    return 0

# change your parameter
prime = 373489
print("prime:",str(prime))
length = 7781
print("length:",str(length))
# 
#twiddle = expmod(prime,comprime,exp)
twiddle = 333978
#print("prime: ",prime)
n_th_ROU(twiddle,length,prime)
test_tw(twiddle,length,prime)

