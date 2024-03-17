import cheby
import numpy as np


def sigmoid(a):
    return 1 / (1 + np.exp(-a))


def round_coefficients(c):
    return [int(round(x * 2**16, 0)) for x in c]


def return_coefficients(c):
    return [round(x/2**16, 4) for x in c]


b6n = cheby.Cheby.fit(sigmoid, -6, -5, 4)
b5n = cheby.Cheby.fit(sigmoid, -5, -4, 4)
b4n = cheby.Cheby.fit(sigmoid, -4, -3, 4)
b3n = cheby.Cheby.fit(sigmoid, -3, -2, 4)
b2n = cheby.Cheby.fit(sigmoid, -2, -1, 4)
b1n = cheby.Cheby.fit(sigmoid, -1, 0, 4)
b1 = cheby.Cheby.fit(sigmoid, 0, 1, 4)
b2 = cheby.Cheby.fit(sigmoid, 1, 2, 4)
b3 = cheby.Cheby.fit(sigmoid, 2, 3, 4)
b4 = cheby.Cheby.fit(sigmoid, 3, 4, 4)
b5 = cheby.Cheby.fit(sigmoid, 4, 5, 4)
b6 = cheby.Cheby.fit(sigmoid, 5, 6, 4)
###############################################
c6n = cheby.Cheby.asTaylor(b6n)
c5n = cheby.Cheby.asTaylor(b5n)
c4n = cheby.Cheby.asTaylor(b4n)
c3n = cheby.Cheby.asTaylor(b3n)
c2n = cheby.Cheby.asTaylor(b2n)
c1n = cheby.Cheby.asTaylor(b1n)
c1 = cheby.Cheby.asTaylor(b1)
c2 = cheby.Cheby.asTaylor(b2)
c3 = cheby.Cheby.asTaylor(b3)
c4 = cheby.Cheby.asTaylor(b4)
c5 = cheby.Cheby.asTaylor(b5)
c6 = cheby.Cheby.asTaylor(b6)
###############################################
print('###############################################')
print('Actual Coefficients')
print('###############################################')
print(c6n)
print(c5n)
print(c4n)
print(c3n)
print(c2n)
print(c1n)
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)
###############################################
print('###############################################')
print('Rounded Coefficients')
print('###############################################')
print(return_coefficients(round_coefficients(c6n)))
print(return_coefficients(round_coefficients(c5n)))
print(return_coefficients(round_coefficients(c4n)))
print(return_coefficients(round_coefficients(c3n)))
print(return_coefficients(round_coefficients(c2n)))
print(return_coefficients(round_coefficients(c1n)))
print(return_coefficients(round_coefficients(c1)))
print(return_coefficients(round_coefficients(c2)))
print(return_coefficients(round_coefficients(c3)))
print(return_coefficients(round_coefficients(c4)))
print(return_coefficients(round_coefficients(c5)))
print(return_coefficients(round_coefficients(c6)))

