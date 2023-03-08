import sys

print(sys.version)
lista = ['a0', 2, 4, 5, [7, 6, 5], 5.5]
print(lista[4])
lista.append(6.5)
print(lista)
#dodanie elementu na pozycje
#dodanie kilku elementów na koniec listy
#usuwanie elementu po indeksie
#usuwanie elementu po wartości elementu
#odwrócenie listy
#sortowanie
lista.insert(3, 10)
print(lista)
lista.pop(2)
print(lista)
lista.remove(5.5)
print(lista)
lista.reverse()
print(lista)
lista.pop(1)
print(lista)
lista.pop(4)
lista.sort()
print(lista)
lista2 = [3, 1]
lista.extend(lista2)
print(lista)
lista.sort()
print(lista)

slownik={'a': 1, 3: 1, 5: 'b', 'a': 5}
print(slownik)
print(slownik['a'])

slownik['klucz'] = 'wartość'
print(slownik)

slownik.pop('a')
print(slownik)

print(slownik.keys())
print(slownik.values())

print('a = %(zm)d' % {'zm': 12})
print('a = {}, b = {}'.format(12, 14))

# if warunek:
#       instrukcja 1
#       instrukcja 2
# elif warunek 2:
#       instrukcja 1
#       instrukcja 2
# else:
#       instrukcja1
# a = input('podaj a: ')
# b = input('podaj b: ')
# c = input('podaj c: ')
# d = input('podaj d: ')
# print(a)
# print(b)
# print(c)
# print(d)
# print(type(a))
# print(type(b))
# a = int(a)
# b = int(b)
# print(type(a))
# print(type(b))

#if a > b:
    #print('a = ' + str(a))
#elif a < b:
    #print('b = ' + str(b))
#else:
    #print('a równe b')

# if a==b:
    # print('a równe b')
# else:
    # print('a i b są różne')

# if (a > b) & (c > d):
    # print(a, c)
# else:
    # print('a nie większe od b lub c nie jest większe od d')

# for element in sekwencja:
#       instrukcja 1
#       instrukcja 2
# else:
#       instrukcja 1

for x in range(1, 6, 1):
    print(x)
print("")
for x in lista:
    print(x)

# range(start, stop, step) for(int i = 0, i < lista.count(), i++)

for x in range(len(lista)):
    print(x)

#while warunek:
    # instrukcja 1
    # instrukcja 2
# else:
#     instrukcja 1

# licznik = 0
# while licznik != len(lista):
    # print(lista[licznik])
    # licznik += 1

# liczby = [3, 45, 1, 7, 8, 5]
# licznik = 0
# a = int(input('podaj a:'))
# while licznik != len(liczby):
    # if a - liczby[licznik] == 0:
        # print('{} - {} = 0'.format(a, liczby[licznik]))
        # break
    # licznik += 1

liczby = [1,2,2,2,2,3]
print(liczby)
a = 0
while a<len(liczby):
    if liczby[a] == 2:
        liczby.pop(a)
    else: a=a+1
print(liczby)