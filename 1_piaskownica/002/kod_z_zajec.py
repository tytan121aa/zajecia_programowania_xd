x = 10
print(x,type(x))

y = "10"
print(y,type(y))

z = 10.0
print(z,type(z))

zz = True
print(zz,type(zz))
print("To mój program")

dzien = "środa"
if dzien == "środa":  # == operator porównania. jeśli x = x
    print("Tak, dzisiaj jest środa")    #wcięcie 4 spacje lub 8 lub TAB
else: # przeciwnym wypadku
    print("Nie, dzisiaj jest środa")

zwierzak = "baran" 
if zwierzak == "kot":                 #jeżeli
    print("To jest kot")
elif zwierzak == "byk":                   # a jeśli
    print("Znak zodiaku")
else:                                # w innych przypadkach
    print("To nie znak zodiaku i nie kot")

zmienna1 = "środa"
zmienna2 = "środa"
print("Zmienna1:", zmienna1,type(zmienna1))
print("Zmienna2:", zmienna2,type(zmienna2))
if zmienna1 == zmienna2:
    print("zmienna1 = zmienna2")

hasło_uzytkownika = "trzasło"
hasło_u_nas = "masło"
if hasło_uzytkownika == hasło_u_nas:
    print("Hasło się zgadza")
else:
    print("Złe hasło")

lista = [1,2,3,4,5,6,7]  #kontenery danych
słownik = {"klucz":"wartosc","klucz":"wartosc"}
tupla = (1,2,3,4)

dni_pracujace = ["poniedziałek","wtorek","środa", "czwartek","piątek"]
weekend = ["sobota","niedziela"]
print(dni_pracujace)
print(weekend)

dzisiaj = "środa"
print("1. Definiujemy zmienną")
dzien = "sobota"
print(dzien)
#if dzien == dzisiaj:
  #  print("Tak,dzisiaj jes środa")
if dzien in dni_pracujace: #if x in y jeśli zmmienna znajduje sie w kontenerze
    print("2a. Dzisiaj jest", dzien ,"- dzień pracujący")
elif dzien in weekend:
    print("2b. Dzisiaj jest" ,dzien,"-weekend:D") #delikatnie zmodyfikowany z tym co było na zajęciah
else:
    print("2c. Źle napisałeś dzień tygodnia")
print("3. Koniec")

zwierzak = "szczur"   #mój
zodiak = ["baran","byk","rak","lew","skorpion","koziorożec","ryby","ryba"]
chinski_znak_zodiaku = ["szczur","wół","tygrys","krolik","smok","wąż","koń","owca","małpa","kogut","pies","świnia"]
if zwierzak == "kot":                 #jeżeli
    print("To jest kot")
elif zwierzak in zodiak:                   # a jeśli
    print("Znak zodiaku", zwierzak.upper())  #x.upper() metoda zmieniająca litery  wielkie, wrzutka osobista z innych zajęć
elif zwierzak in chinski_znak_zodiaku:
    print("Chiński znak zodiaku", zwierzak.upper())
else:
    print("To nie znak zodiaku i nie kot")# w innych przypadkach

x = 18
if x == 10:
    print("xD")
elif x == 11:
    print(":)")
elif x == 12:
    print("O_o")
else:
    print(":0", "Podałeś liczbę:",x)
