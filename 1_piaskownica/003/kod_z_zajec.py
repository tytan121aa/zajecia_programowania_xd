#import requests #pobranie z internetu (pip3 install nazwa biblioteki - instlcja na serwerze), kod  źródłowy i dokumenacje, mają różne wersje
#Lista
#lista = [1,2,3,4]
#lista = []
#lista = [1]
#print(lista)
#koszyk = ["jabłko1","jabłko2","jabłko3","garść malin","gruszka"] #napisy typu: str (string)
# pętla
#print("Zaczynam")
#for owoc in koszyk:
#    print()
#    print("1. Wyciągam",owoc) #intendation wcięcie 4/8 spacji/TAB
#    print("2. Myję owoc", owoc)
 #   print("3. Zjadam", owoc)
 #   if owoc == "garść malin":
 #       continue
 #   print("4. Wyrzucam ogryzek po", owoc)
#print("Skończyłem")

#import
#import pandas
#import os, sys
# requests panda

#link = "https://zajecia-programowania-xd.pl/flagi"
#flagi_response = requests.get(link) #.get dowiedzieć się

#flagi_tekst = flagi_response.text
#print(flagi_tekst) #treść strony  grupy link
#lista ="brtkborkbokbq"
#       0123456789
#print(lista)
#for i in lista:
#    print(i)
#dlugosc_listy = len(lista)
#print("Długość:", dlugosc_listy)

#element = lista[6] 
#print("Element:", element)

#print(flagi_tekst)

import requests
link ='http://zajecia-programowania-xd.pl/flagi' 
flagi_response = requests.get(link) 
flagi_tekst = flagi_response.text# wyciąga tekst HTML z linku
print(flagi_tekst)

flagi = flagi_tekst.split('</p>') # dzieli listę na elementy?
for f in flagi:
    f = f[3:]
    print("-",f)
