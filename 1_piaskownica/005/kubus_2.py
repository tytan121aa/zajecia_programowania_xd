import requests

link = 'https://zajecia-programowania-xd.pl/kubus_puchatek'
kubus_raw = requests.get(link)
kubus_text = kubus_raw.text

kubus_text = kubus_text.replace('<p>', '')
kubus_text = kubus_text.replace('</p>', '')

dlugosc_kubusia = len(kubus_text)
print(kubus_text)
print(dlugosc_kubusia)

kubus_puchatek_slowa = kubus_text.split(" ")
kubus_puchatek_slowa_n = len(kubus_puchatek_slowa)
print(type(kubus_puchatek_slowa))
print(kubus_puchatek_slowa_n)
#x=0     moja propozycja policzenia slów Kubuś w tekście
#for e in kubus_puchatek_slowa:
 #   if e == "Kubuś":
 #       x += 1
 #       print(x)
 
 # kod pokazany na zajęciach : (różnice. print poza ifem, pokaże konkretną liczbę, w ifie pokaże liczbę dla każdego Kubusia)
kubus_n = 0 
for s in kubus_puchatek_slowa:
    if s == "Kubuś":
        kubus_n += 1 #iteracja dla każdego Kubusia dodaje 1 do zmiennej kubus_n
       # kubus_n = kubus_n + 1 - dokładnie to samo co u góry
print(kubus_n)

# dodanie enumearte
kubus_n = 0
for i,s in enumerate(kubus_puchatek_slowa):
    #if s == "Kubuś":
     #   kubus_n += 1 #iteracja dla każdego Kubusia dodaje 1 do zmiennej kubus_n
     #   print(i,s)
    if "Kubuś" in s: # tutaj jeśl "Kubuś" znajduje się w słowach to dostajemy większą liczbę kubusiów
        # ze względu na formę zapisania tekstu - teoretycznie lepszy sposób
        print(i,s) 
        kubus_n +=1
       # kubus_n = kubus_n + 1 - dokładnie to samo co u góry
print(kubus_n)

x = "    ABC  vff   "
x = x.strip()#wycina spacje z przodu i tyłu znaków ale nie pomiędzy
x1 = x.rstrip() # wycina spacje z tyłu
print(x)
print(len(x))
