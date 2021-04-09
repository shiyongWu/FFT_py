# FFT_py
以python實現ntt function，用來練習python coding技巧。
implement NTT(FFT over the finite field) and Bluestein's NTT

## Mod.py
implement modular operation,實現NTT運算時會用到的模運算。
| module name | descript |
| ----------- | ---------|
| AddMod(a,b,P)| 執行加法並最後得到在模數P下的值|
| SubMod(a,b,P)| 執行減法並最後得到在模數P下的值|
| DivMod(a,b,P)| 執行除法並最後得到在模數P下的值，相當於a 乘上 b的乘法反元素|
| MulMod(a,b,P)| 執行乘法並最後得到在模數P下的值|
| ExpMod(a,exp,P)|執行a的exp次方運算並最後得到在模數P下的值|
|  InvMod(a,P) | 求出 a在模數P下的乘法反元素|
|   XGCD(a,P)  | 輾轉相除法|

## NTT_init.py 
NTT_init，在計算NTT轉換所使用的n-th primitive root of unity
| module name | descript |
|-------------|----------|
| n_ROU(Prime,comprime,n)| 計算 n-th Root of unity，必要條件 n必須為 (Prime-1)的因數。(依據費馬小定理)|
| PROU(ROU,n,Prime) | 測試 n-th Root  of unity，是否為primitive root of unity。 即為  (ROU)^(i) != 1 , for 0<i<n|

## NTT.py
NTT(DFT over the finite field)function 實現
| module name | descript |
| ------------|----------|
| NTT(x,ROU,prime,n,inverse)| x: input data sequence, ROU: primitive root of unity, n: the length of the input sequence, inverse: must be zero or one, inverse is 1代表執行INTT|


## FFT.py
FFT(FFT over the finite field)function 實現
|module name| descipt|
|-----------|--------|
| BU(A,B,P) | Radix-2 butterfly unit|
| FFT(Array,P,root,N,inverse)| Radix-2 FFT(DIF)，當Inverse = 1 時代表執行IFFT|


//Readme version 1.1
//At 2021/04/9
