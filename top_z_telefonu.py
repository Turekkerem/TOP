from math import gcd
import math
from math import factorial as silnia
lista_dlugosc_od_n=[[0] * 700 for _ in range(700)]
def wspolczynniki(a,n):
    k=gcd(a,n)
    i=gcd(n//k,k)
    j=(n//i)//k
    b=gcd(k,a//k)
    l=(a//k)//b
    #print(f"k = {k}")
    #print(f"a = {a} b = {b} l = {l}")
    #3print(f"n = {n} i = {i} j = {j} ")
    #print(f"spr a = {b*l*k}")
    return (k,l,b),(k,j,i)
def euler_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            # Jeśli p jest dzielnikiem n, to zaktualizuj wynik
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    # Jeśli n jest większe niż 1, to jest liczba pierwsza
    if n > 1:
        result -= result // n
    return result
def zbior(a,n):
    phi_n=euler_totient(n)
    #print(wspolczynniki(a,n))
    print((a,n),phi_n,a%n)
    k=gcd(a,n)
    #for i in range(10):
        #print(pow(k,i,n))
    g=[1]
    for i in range(0,4000000000009):
        w=(g[-1]*a)%n
        if w in g:
            print("dl",len(g),"+1",pow(a,i+1,n),"phi+1",pow(a,phi_n+1,n),"phi(n)",pow(a,phi_n,n))
            #stop=input('')
            return g,len(g)
        g.append(w)
def przedluzenie(a,n):
    t=zbior(a,n)
    return (t[-1]*a)%n
#print(zbior(10000*2137*17*50*331,50*2137*17*23**5))
"""
for a in range(2,700):
    for n in range(2,700):
        w=wspolczynniki(a,n)
        [k,j,i]=w[1]
        if 1:
            z,dl=zbior(a,n)
            lista_dlugosc_od_n[a][n]=dl
            #print(lista_dlugosc_od_n)
            #input('')
            print("================")
"""
deskryptor=open('top_szczegolowe.txt','w')
for n1 in range(2,700):
    for a1 in range(2,700):
        z=zbior(a1,n1)
        w=wspolczynniki(a1,n1)
        deskryptor.write(f"n={str(n1)}  a={a1} dl={z[1]} \n")
        deskryptor.write(f"phi(n)={euler_totient(n1)} k={w[0][0]} phi(k)={w[0][0]} j={w[1][1]} phi(j)={euler_totient(w[1][1])} \n" )
        deskryptor.write(f"i={w[1][2]} phi(i)={euler_totient(w[1][2])} b={w[0][2]} phi(b)={w[0][2]}\n")
        deskryptor.write(f"l={w[0][1]} phi(l)={euler_totient(w[0][1])}\n")
        deskryptor.write(str(z[0]))
        deskryptor.write("\n")
        deskryptor.write("===================================================\n")
#print(pow(40*2137,euler_totient(2137*31),2137*31))
#print(zbior(40*2137,31*2137))
#print(pow(126,16,13*31))
#print(zbior(3,7))
#print(zbior(126,2418))
#print(pow(42,4,105))
#print(zbior(1024*4*17,1024*31*157))
#print(pow(126,16-1,13*31))
#print(zbior(42*3*31,42*157))
#for i in range(100):
    #print(pow(42*3*31,i,42*157))
#print((413696*1024*4*17)%(1024*31*157))
#print(euler_totient(31*157)%80)
exit()
dlugosci=[]
maxg=[]
mn=0
ma=0
maxile=0
tab=set()
s=dict()
czy=0
for k in range(2,200):
    if k>10:
        break
    for b in range(2,10):
        for l in range(2,10):
            if gcd(b,l)!=1 or gcd(k,l)!=1:
                break
            for i in range(1,100):
                
                for j in range(1,100):
                    if gcd(j,k)!=1 or gcd(j,i)!=1:
                        break
                    #print("="*20)
                    #print("a = ",k*b*l,"n = ",i*j*k)
                    #print("k = ",k,"b = ",b,"l = ",l,"i = ",i,"j = ",j)
                    a=k*b*l
                    n=i*j*k
                    t=zbior(a,n)
                    print(t)
#print("set:",s)
for klucz in s:
    print("="*10)
    print(klucz,len(s[klucz]))
    for h in s[klucz]:
        print(h)
if czy==1:
    print("r",tab)                  
exit(0)
for i in range(1000):
    for j in range(2,i):
        if gcd(i,j)==1:
            continue
        z=zbior(i,j)
        if len(z)>maxile:
            maxg=z
            ma=i
            mn=j
            maxile=len(z)
        dlugosci.append(len(z))
print(ma,mn,maxile)
print(maxg)
print(list(set(dlugosci)))
