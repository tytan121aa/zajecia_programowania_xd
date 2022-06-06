import random
import string

lowercase = string.ascii_lowercase  # alfabet małe litery
uppercase = string.ascii_uppercase # alfabet duże litery
#letters = string.ascii_letters # alfabet mały i duży
digits = string.digits #cyfry
efekt = lowercase
print(lowercase)
print(uppercase)
#print(letters)
print(digits)
print(efekt)
efekt1a = lowercase.upper()

if "A" in efekt:          #ma warunek do spełnienia
    print("1. OK")
elif ";" in efekt:    # ma warunek do spełnienia, sprawdzany kiedy poprzedni jest False
    print("2. ; jest w ciągu ") 
elif ":" in efekt:    # ma warunek do spełnienia, sprawdzany kiedy poprzedni jest False
    print("3. : jest w ciągu ")
elif "]" in efekt:    # ma warunek do spełnienia, sprawdzany kiedy poprzedni jest False
    print("4. ] jest w ciągu ")
elif "a" in efekt:    # ma warunek do spełnienia, sprawdzany kiedy poprzedni jest False
    print("5. a jest w ciągu ")
else:   # wszystko co nie spełnia powyższych warunków, sprawdzany kiedy wszystko powyżej false             
    print("6.NO")

if "a" in efekt:  #w tym bloku kodu mamy 2 pytania a więc oba printy się pokażą
    print("1.OK") # w przypadku if/elif zadajemy jedno pytanie z wieloma warunkami a interpreter 
if "abcde" in efekt: # zatrzymuje się na pierwszym spełnionym
    print("2.OK")

                    # c pojedyncza literka (character)
for  c in efekt:      #iterowanie (przechodzenie kolejno przez elementy listy a stringi zachowują się jak listy)
    c += "xyz"       # doda do każdej literki w ciągu xyz
    x = len(c)   # długość ciągu c +="xyz"
    print(c,x)            # wydrukuje ciąg c oraz długość ciągu 

# wcięcie w for,if, def oraz class

efekt1 = efekt.replace("fgh", "xDDDDDD") #podmienia ciąg znaków na inny
efekt2 = efekt.split("x") #wycina x i powstaną 2 ciągi znaków do x i od x (yz)
efekt3 = efekt1a.split("X")
print()
print(efekt)
print(efekt1)
print(efekt2)
print(efekt3)
print()

#GENERATOR HASEŁ
# - string - ciąg znaków
# - losowe hasło
# - określona liczba znaków
# - znaki specjalne
# - duże litery
# - małe litery
# - cyfry

n_znakow = 8
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
punctuation = string.punctuation
print(punctuation)
digits = string.digits
wszystkie_znaki = lowercase + uppercase + digits + punctuation
losowe_znaki = random.sample(wszystkie_znaki, n_znakow) #wylosuj 2 znaki ze zmiennej lowercase w formie listy
haslo = ''.join(losowe_znaki)  #łączy elementy  listy w string(działa na liście stringów)

print("Generator haseł:")
#print(haslo, type(haslo))  #wydrukuje liste
#print(haslo[0], type(haslo[0])) #wydrukuje elementy
print(haslo,type(haslo))
print()

print("Generator domowy:")
#generator haseł na stronę pod zakładką geneartor haseł
#Udoskonalić genererator
#1. Po 2 losowe cyfry/znaki i duże/małe litery
#2. losowa kolejność cyfr, znaków, dużych i małych liter
#3. Co zrobić aby dobrze działał dla różnej liczby znaków
#Sprawdź sobie: itertools co za biblioteka?
n= input("Z ilu znaków ma się składać Twoje hasło:")
n_sign = int(n)
n_sign_lowercase = "".join(random.sample(string.ascii_lowercase, 10))
n_sign_uppercase = "".join(random.sample(string.ascii_uppercase, 10))
n_sign_digits = "".join(random.sample(string.digits, 10))
n_sign_punctuation = "" .join(random.sample(string.punctuation, 10))
passwords_generator = "".join(random.sample(n_sign_lowercase + n_sign_uppercase + n_sign_digits + n_sign_punctuation, n_sign))

if n_sign>7 and n_sign <21:
    print(passwords_generator)   
else:
    print("Wybrana liczba musi zawierać się w przedziale <8-20>")
print()
print("Generator przez +")
for i in lowercase:
    haslo += random.sample(lowercase, 1)[0]
print(list(range(10)))
