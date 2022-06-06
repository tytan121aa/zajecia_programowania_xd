import requests


#pobieranie tekstu ze strony (jako tafle tekstu)
orangutan = "https://zajecia-programowania-xd.pl/flagi"
print(type(orangutan), orangutan)
surowe_info = requests.get(orangutan)
text = surowe_info.text

# Cel: Lista linków wszystkich

#przykładowe rozwiązanie
# lista = [ ]
    #"link1.pl"
    # "link2.pl"
    
#przygotowanie
lista_linii = text.split("</p>") # podział tekstu w miejscu </p>

#Realizacja
linki = [] # inicjujemy pustą listę
#linki = list() # też dobru sposó na inicjacje


for linia in lista_linii:  
    link= linia.replace("<p>", "") #jeśli znajdziesz <p> zmień na " "
    link = link.replace("- ","") 
    link = link.strip() # usuń spacje
    
    if " " in link or "<" in link:
        continue
    linki.append(link)
    print(link) #"\n" - robi enter. Koniecznie slash w tę stronę
                   
#Cel: policz ile jest domen z .pl :)

#Realizacja:
domeny_pl = 0
domeny_com = 0
domeny_com_pl = 0
wszystkie_kropki = 0
for i, link in enumerate(linki):
    print(i,link)
    if ".pl" in link:
        domeny_pl += 1
    if ".com" in link:
        domeny_com += 1
    if (".pl" in link) and (".com" in link):
        domeny_com_pl +=1
        
    #Ile jest kropek w linkach:
    
    n_kropek = link.count('.') #policzy iloś kropek w podanym stringu
    wszystkie_kropki += n_kropek
print("domeny pl:" , domeny_pl)
print("domeny com:", domeny_com)
print("domeny com.pl:", domeny_com_pl)
print("ilość kropek:", wszystkie_kropki)

def policz_pomidory(pierwsze_pudelko, drugie_pudelko):
    ile_pomidorow = pierwsze_pudelko + drugie_pudelko
    return ile_pomidorow #zwraca coś

#pudełka z pomidorami
pierwsze_pudelko = 8
drugie_pudelko = 2

#ile jest razem pomidorów? użyj funkcji aby policzyć
liczba_pomidorów = policz_pomidory(pierwsze_pudelko, drugie_pudelko)
#pokaż wynik
print("Liczba pomidorów:", liczba_pomidorów)

# Funkcja która zadanej liście domen zliczy wszystkie domeny które są TYLKO .pl

def policz_domeny_pl(linki): # ciało funkcji def nazwa (ewentualne argumenty)
    n_domen_pl = 0
    for link in linki: 
        if link.count('.') > 1:
            continue
        elif '.pl' in link:
            n_domen_pl += 1
    return n_domen_pl

wynik = policz_domeny_pl(linki)
print("ilość domen tylko .pl:", wynik)
        
