import cheby
import numpy as np


def exponential(a):
    return np.exp(a)


b5 = cheby.Cheby.fit(exponential, 0, 1, 5)
c5 = cheby.Cheby.asTaylor(b5)
b4 = cheby.Cheby.fit(exponential, 0, 1, 4)
c4 = cheby.Cheby.asTaylor(b4)
b3 = cheby.Cheby.fit(exponential, 0, 1, 3)
c3 = cheby.Cheby.asTaylor(b3)
b2 = cheby.Cheby.fit(exponential, 0, 1, 2)
c2 = cheby.Cheby.asTaylor(b2)
b1 = cheby.Cheby.fit(exponential, 0, 1, 1)
c1 = cheby.Cheby.asTaylor(b1)


def cheby_approx_5th(a):
    return c5[0] + c5[1] * a + c5[2] * a ** 2 + c5[3] * a ** 3 + c5[4] * a ** 4 + c5[5] * a ** 5


def cheby_approx_4th(a):
    return c4[0] + c4[1] * a + c4[2] * a ** 2 + c4[3] * a ** 3 + c4[4] * a ** 4


def cheby_approx_3rd(a):
    return c3[0] + c3[1] * a + c3[2] * a ** 2 + c3[3] * a ** 3


def cheby_approx_2nd(a):
    return c2[0] + c2[1] * a + c2[2] * a ** 2


def cheby_approx_1st(a):
    return c4[0] + c4[1] * a


print(b4)
print('c =  ', c4)
print('exp(x) = ', exponential(0.9))
print('5th order Chebyshev Approximation:', cheby_approx_5th(0.9))
print('4th order Chebyshev Approximation:', cheby_approx_4th(0.9))
print('3rd order Chebyshev Approximation:', cheby_approx_3rd(0.9))
print('2nd order Chebyshev Approximation:', cheby_approx_2nd(0.9))
print('1st order Chebyshev Approximation:', cheby_approx_1st(0.9))