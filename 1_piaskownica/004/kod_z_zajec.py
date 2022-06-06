import requests # pobiera bibliotekę requests 

link = 'https://zajecia-programowania-xd.pl/kubus_puchatek'
kubus_raw = requests.get(link) # pobiera info czy strona działa [response 200]
kubus_text = kubus_raw.text #  wyciąga tekst strony [.encode('utf_8') jeśli problem ze znakami plus zamknięcie w str()]

kubus_linie_b = kubus_text.split('</p>') #usuwa </p> i tnie tekst na kolejne linie po danym znaku
#czyszczenie
kubus_linie = []
for l in kubus_linie_b:
    #l =l[4:]              #wycina pierwsze 3 znaki l ciąg znaków 
    l = l.replace('<p>','') # replace zamienia "coś",w "coś innego"
    l = l.strip() #czyści puste spacje, białe znaki
    kubus_linie.append(l) #łączy razem numery z liniami tekstu, wbija w liste
    
#wyświetlanie 
koszyk = ["jabłko", "maliny", "mango", "agrest"] #lista
start = 100
end = 400
tajemniczy_bohater0 = "Młody"
tajemniczy_bohater = "Superman"
tajemniczy_bohater2 = "Joker"
tajemniczy_bohater3 = "SpongeBob Kanciastoporty"
for index, linia in enumerate(kubus_linie): #enumerate numeruje linie, cała pętla pokazuje linie ze słowem Kubuś i je numeruje
    if index >= start and index <= end:
        linia = linia.replace("Kubuś", tajemniczy_bohater0)
        linia = linia.replace("Puchatek", tajemniczy_bohater)
        linia = linia.replace("Królik", tajemniczy_bohater2)
        linia = linia.replace("Prosiaczek", tajemniczy_bohater3)
        linia = '<p>' + linia + "</p>"
        print(linia)
print("<p> Czytała Krystyna Czubówna</p>")

print(len(kubus_linie))
