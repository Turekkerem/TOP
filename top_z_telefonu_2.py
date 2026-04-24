from math import gcd
import math
from math import factorial as silnia
def is_prime(n):
    if n==2:
        return 1
    if n%2==0:
        return 0
    i=3
    while i*i<=n:
        if n%i==0:
            return 0
        i+=2
    return 1
def log_dysk(a,n,x):
    x=x%n
    a=a%n
    wyniki=[1]
    i=1
    while 1:
        r=(wyniki[-1]*a)%n
        if r==x:
            return i
        if r in wyniki:
            print("brak rozwiazania")
            return 0
        else:
            wyniki.append(r)
        i+=1
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
    #print(wspolczynniki(a,n))
    #print((a,n),euler_totient(n),a%n)
    k=gcd(a,n)
    #for i in range(10):
        #print(pow(k,i,n))
    #g=[1]
    w=1
    for i in range(0,4000000000009):
        w=(w*a)%n
        if w==1:
            print("dl",i+1)
            f.write("dl "+str(i+1)+"\n")
            return i+1
        #g.append(w)
def przedluzenie(a,n):
    t=zbior(a,n)
    return (t[-1]*a)%n
#print(zbior(20,438))
#print(zbior(48*4*13*7*19,48*6*17*19*5*5))
#print(zbior(2*3*4,17*4))
#print(zbior(168,168*24000*17))
#print(zbior(13,65))
"""liczba=98
zbiory=dict()
for f in range(liczba):
    z=sorted(zbior(f,liczba))
    s=""
    for e in z:
        s+=str(e)
        s+="|"
    if s in zbiory:
        zbiory[s].append(f)
    else:
        zbiory[s]=[f]
print(zbiory)
for q in zbiory:
    print(q,zbiory[q])"""
print("wersja z grupami modulo tj. jako n same potęgi liczb pierwszych")
f=open("anomalie2.txt","w")
for n in range(200):
    if is_prime(n)==0:
        continue
    for a in range(2,n):
        #a,n=map(int,input().split())
        kopia_n=n
        p=euler_totient(n)
        z_poprzednik=1
        for i in range(10):
            print("="*10)
            print(f"R({a},n^{i+1} = {kopia_n})")
            print("Odwrotność a to: ",pow(a,-1,kopia_n))
            f.write("="*10)
            f.write(f"R({a},n^{i+1} = {kopia_n}) \n")
            f.write("Odwrotność a to: "+str(pow(a,-1,kopia_n))+"\n")
            z=zbior(a,kopia_n)
            if z//z_poprzednik!=n and i>0:
                phi=euler_totient(z)
                print(f"Problem przy R({a},n^{i+1})")
                print("phi(n) = ",phi)
                print("phi(phi(n)) = ",euler_totient(phi))
                f.write(f"Problem przy R({a},n^{i+1}) \n")
                f.write("phi(n) = "+str(phi)+"\n")
                f.write("phi(phi(n)) = "+str(euler_totient(phi))+"\n")
            z_poprzednik=z
            #print(z)
            #print(pow(a,len(z),n))
            #print("phi(n) = ",(kopia_n//n)*p)
            p*=n
            kopia_n*=n
        #(print(z)
    #break
    #z=zbior(a,n)
    #print(z)
    continue
    for e in z:
        print(wspolczynniki(e,n))
exit(0)
for x in range(200,1000):
    for y in range(200,1000):
        #z=zbior(x,y)
        p=euler_totient(y)
        w=wspolczynniki(x,y)
        if (pow(x,p+2,y)!=pow(x,3,y) and (w[1][0]!=1 and w[1][1]!=1 and w[1][2]!=1 and w[0][2]!=1 and w[0][1]!=1)):
            print("======")
            z=zbior(x,y)
            print(z)
            print(w)
            print((x-1)%w[1][1])
        if (x+y)%700==0:
            input()
exit()
print(log_dysk(30,4913,56))
print((zbior(6,314)))
print((zbior(3,107)))
#print(zbior(10000*2137*50,157*331*3331*31*50))
exit()
for a in range(2,30):
    for n in range(2,30):
        w=wspolczynniki(a,n)
        [k,j,i]=w[1]
        if i==1 and j>1 and k>1:
            print(zbior(a,n))
 
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