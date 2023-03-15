import math

a = pow(math.e, 10)
print(a)
b = pow(math.log((5+pow(math.sin(8),2))),(1/6))
print(b)
imie = "MATEUSZ"
nazwisko = "ŚLADOWSKI"
imie_2 = imie.capitalize()
nazwisko_2 = nazwisko.capitalize()
print(imie_2, nazwisko_2)
dogs = "who let the dogs out? who, who, who, who, who? who let the dogs out? who, who, who, who, who?"
who = dogs.count("who")
print(who)
imie_3 = imie[1]
print(imie_3)
imie_4 = imie[6]
print(imie_4)
tekst = "placek"
pi = float(3.14)
szesna = 0xff1e
print(szesna)
print('{} jest rowny {} a oto jakas losowa szesnastka: {}'.format(tekst, pi, szesna))
ciach = dogs.split()
print(ciach)
sporty = ["badminton", "ping pong", "tenis" ]
print(sporty)
sporty.reverse()
print(sporty)
sporty_2 = ['snowboard', 'lyzwiarstwo']
sporty.extend(sporty_2)
print(sporty)
skroty = {'np': 'na przykład', "tj": "to jest", "tzn": "to znaczy"}
print(skroty)
print(skroty['np'])
print(len(skroty))
zdanie = input("Podaj zdanie: ")
zdanie_2 = zdanie.count("a")
print(zdanie_2)
a = input('podaj a: ')
b = input('podaj b: ')
c = input('podaj c: ')
if (a>b) & (a>c): print("a jest najwieksza liczba")
elif (b>c): print("b jest najwieksza liczba")
else: print("c jest najwieksza liczba")
potegi = [3, 3.2, 4, 1, 5.5]
for i in range(len(potegi)):
    potegi[i] = pow(potegi[i], 2)
    print(potegi[i])