#poznane funkcje wbudowane:
# print() - wyświetl na ekranie
# read() - przeczytaj ale jak?
# open() - otwórz ale co i jak?
# type() - typ danych

#stworzone:
#dodwanie()

text=3    #po hashu mamy komenntarz ktory nie bedzie czytany przez program
print("Geralt")

X = "heja"
print(X)

print()
X = "siema"
print(X)

def dodawanie(a=1,b=1):   #definicja ma nazwe z nawiasem i dwukropkiem!
    return a + b

print(dodawanie()) #by wywołać funkcję trzeba podać jej nazwę z nawiasem!

def witcher():
    a = "Geralt " 
    b = "Yennefer"
    c = "za "
    d = "podążał "
    return a + d + c + b
x = witcher()  #przypisanie funkcji do zmiennej, również nnnazzwa funkcji z nawiasami !

print(witcher())
print(witcher()[:18])    # wywołanie funkcji skróconej do x znaków [:x] za x odtawic liczbę
print(x)

text = "To jest string"
text2 = " 3"
print(text + text2)

text3 = 1 #zmienna typy integar (int) liczba całkowita
text4 = 1.1 #zmienna typy floating (float) liczba zmiennoprzecinkowa
text5 = True #zmienna typy boolean(bool) prawda/fałsz zmienne logiczne
text6 = "BajlaMorena" #zmienna typy string (str) text, ciag znaków "cudzysłowie" 

print(type(text3))    #type() pokazuje typ danych
print(type(text4))
print(type(text5))
print(text6, type(text6))


