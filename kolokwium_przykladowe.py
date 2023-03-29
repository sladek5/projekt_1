import math

#a = int(input('podaj a: '))
#if not type(a) is int:
  #raise TypeError("Only integers are allowed")
#b = int(input('podaj b: '))
#if not type(b) is int:
  #raise TypeError("Only integers are allowed")
#h = math.pow(a,2)+(a*b)+math.pow(b,2)
#print(h)
#f = open("zadanie_1.txt", "x")
#f.write("%i" %h)

list_1 = [1,3,5,7]
list_2 = [2,4,6,8]
list_3 = [list_1[i]+list_2[i] for i in range(len(list_1))]
print(list_3)