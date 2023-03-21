import random

a = [1-x for x in range(1, 11)]
print(a)
b = [4**y for y in range(8)]
print(b)
c = [y for y in b if y % 2 == 0]
print(c)
lista1 = []
for i in range(10):
    r = random.randint(1,10)
    lista1.insert(i,r)
print(lista1)
lista2 = [n for n in lista1 if n % 2 == 0 ]
print(lista2)
produkty = {'mąka': 'kg', 'jajka': 'szt', 'bułki': 'szt', 'ziemniaki': 'kg'}
ilosc = 'kg'
produkty2 = [m for m in produkty.keys()]
print(produkty2)