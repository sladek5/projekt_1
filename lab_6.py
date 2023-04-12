import numpy as np

a = np.array([[0, 1], [2,3]])
print(a)

b = np.arange(2, 5, 0.1)
print(b)
#typ zmiennej tablicy
print(type(a))
#typ danych tablicy
print(a.dtype)

a = np.arange(2, dtype='int64')
print(a.dtype)
print(a)

c = a.astype('float')
print(c)
print(c.dtype)

print(a.shape)

print(a.ndim)

m = np.array([np.arange(2), np.arange(2)])
print(m.shape)
print(type(m))
zera = np.zeros((5, 5), dtype='int32')
jedynki = np.ones((4, 4))
print(zera)
print(jedynki)

print(zera.dtype)
print(jedynki.dtype)


pusta = np.empty((2,2))
print(pusta)

macierz = np.array([[12, 11], [2, 1]])
print(macierz)

poz_1 = macierz[1, 1]
poz_2 = macierz[0][1]
print(poz_1)
print(poz_2)

liczby_lin = np.linspace(1, 2, 5, endpoint=False)
print(liczby_lin)

z = np.indices((5, 3))
print(z)
print(z[0][1][2])

mat_diag = np.diag([a for a in range(5)])
print(mat_diag)

znaki = 'ogolna'
z3 = np.array(list(znaki))
z4 = np.array(list(znaki), dtype='S1')
z5 = np.array(list(b'ogolna'))
z6 = np.fromiter(znaki, dtype='S1')
print(z3)
print(z4)
print(z5)
print(z6)

a = np.arange(10)
print(a)
s = slice(2, 7, 2)
s = range(2, 7, 2)
print(a[s])

print(a[2:7:2])

print(a[1:])
print(a[2:5])

mat = np.arange(25)
mat = mat.reshape((5, 5))
print(mat)
print(mat[1:])
print(mat[:, 1])
print(mat[:, -1])
print(mat[2:5, 1:3])
print(mat[:, [2,4]])
print('')

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print(y)
