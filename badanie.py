maks=0
wybrane_wiersze=[]
with open("top_ogolne.txt") as dane:
    for wiersz in dane:
        wiersz=wiersz.strip()
        for indeks_znaku in range(len(wiersz)):
            if wiersz[indeks_znaku]==':':
                poczatek=indeks_znaku+1
                break
        lista=list(map(int,wiersz[poczatek:-1].split()))
        if 157 in lista:
            wybrane_wiersze.append(wiersz)
        maks=max(maks,max(lista))
print(maks)
print(wybrane_wiersze)