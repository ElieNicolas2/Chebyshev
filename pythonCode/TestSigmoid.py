import cheby
import numpy as np


def sigmoid(a):
    # return a**0.7
    return 1 / (1 + np.exp(-a))
    # return np.cos(a)
    # return np.log10(a)


b6 = cheby.Cheby.fit(sigmoid, 0, 1, 6)
c6 = cheby.Cheby.asTaylor(b6)
b5 = cheby.Cheby.fit(sigmoid, 0, 1, 5)
c5 = cheby.Cheby.asTaylor(b5)
b4 = cheby.Cheby.fit(sigmoid, 0, 1, 4)
c4 = cheby.Cheby.asTaylor(b4)
b3 = cheby.Cheby.fit(sigmoid, 0, 1, 3)
c3 = cheby.Cheby.asTaylor(b3)
b2 = cheby.Cheby.fit(sigmoid, 0, 1, 2)
c2 = cheby.Cheby.asTaylor(b2)
b1 = cheby.Cheby.fit(sigmoid, 0, 1, 1)
c1 = cheby.Cheby.asTaylor(b1)

# b6 = cheby.Cheby.fit(sigmoid, 1, 2, 6)
# c6 = cheby.Cheby.asTaylor(b6)
# b5 = cheby.Cheby.fit(sigmoid, 1, 2, 5)
# c5 = cheby.Cheby.asTaylor(b5)
# b4 = cheby.Cheby.fit(sigmoid, 1, 2, 4)
# c4 = cheby.Cheby.asTaylor(b4)
# b3 = cheby.Cheby.fit(sigmoid, 1, 2, 3)
# c3 = cheby.Cheby.asTaylor(b3)
# b2 = cheby.Cheby.fit(sigmoid, 1, 2, 2)
# c2 = cheby.Cheby.asTaylor(b2)
# b1 = cheby.Cheby.fit(sigmoid, 1, 2, 1)
# c1 = cheby.Cheby.asTaylor(b1)


def cheby_approx_6th(a):
    return c6[0] + c6[1] * a + c6[2] * a ** 2 + c6[3] * a ** 3 + c6[4] * a ** 4 + c6[5] * a ** 5 + c6[6] * a ** 6


def cheby_approx_5th(a):
    return c5[0] + c5[1] * a + c5[2] * a ** 2 + c5[3] * a ** 3 + c5[4] * a ** 4 + c5[5] * a ** 5


def cheby_approx_4th(a):
    return c4[0] + c4[1] * a + c4[2] * a ** 2 + c4[3] * a ** 3 + c4[4] * a ** 4


def cheby_approx_3rd(a):
    return c3[0] + c3[1] * a + c3[2] * a ** 2 + c3[3] * a ** 3


def cheby_approx_2nd(a):
    return c2[0] + c2[1] * a + c2[2] * a ** 2


def cheby_approx_1st(a):
    return c1[0] + c1[1] * a


def improvement(cheby_approx_bef, cheby_approx_aft):
    return abs(cheby_approx_aft - cheby_approx_bef)


print(b4)
print('c =  ', c4)
print('sigmoid(x) = ', sigmoid(0.9))
print('6th order Chebyshev Approximation:', cheby_approx_6th(0.9))
print('5th order Chebyshev Approximation:', cheby_approx_5th(0.9))
print('4th order Chebyshev Approximation:', cheby_approx_4th(0.9), 'with an improvement of: ',
      improvement(cheby_approx_3rd(0.9), cheby_approx_4th(0.9)))
print('3rd order Chebyshev Approximation:', cheby_approx_3rd(0.9), 'with an improvement of: ',
      improvement(cheby_approx_2nd(0.9), cheby_approx_3rd(0.9)))
print('2nd order Chebyshev Approximation:', cheby_approx_2nd(0.9), 'with an improvement of: ',
      improvement(cheby_approx_1st(0.9), cheby_approx_2nd(0.9)))
print('1st order Chebyshev Approximation:', cheby_approx_1st(0.9))


