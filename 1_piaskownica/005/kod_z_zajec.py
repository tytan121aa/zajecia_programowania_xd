import requests

# def nazwa_funkcji(argument1): anatomia funkcji 

def policz_znaki(argument):
    dlugosc_stringu = len(argument)
    return dlugosc_stringu

link = 'https://zajecia-programowania-xd.pl/kubus_puchatek'
kubus_raw = requests.get(link)
kubus_text = kubus_raw.text

#1.zabawa z indeksem
#link_b = link[10] pokaże 11 znak
#link_b = link[1:-1] pokaże znaki od 2 do przedostatniego
#link_b = link[::-1] pokaże ciag znaków od tyłu

#2.Metody wbudowane
#link_b = link.upper() #pokaże ciąg znaków drukowanymi literami
#link_b = link.lower() #pokaże ciąg znaków małymi literami
#link_b = link.replace("a", "b") zamieni wyraz na inny ...

#3.Dodawanie ciągów znaków
#link_b = link[:20].upper() + ' '+ link[20:] ze zwiększenie 2 cęści

#4. Dzielenie ciągów znaków na kawałki
# split()  rozbije ciag znaków na listę stringów pociętych przy znaku w nawiasie _(tokenizowanie ciągu znaków)

#5. Porównanie ciągów znaków ze sobą

#6. Sprawdzanie czy "abcd" występuje w "abcdefgh"
link = 'https://zajecia-programowania-xd.pl/kubus_puchatek'
ciag = 'Tutaj są jakieś słowa'
efekt = ciag.split("a") # rozbije ciag znaków na listę stringów pociętych przyh znaku w nawiasie _(tokenizowanie ciągu znaków)
print(link)
print(efekt)
print()
