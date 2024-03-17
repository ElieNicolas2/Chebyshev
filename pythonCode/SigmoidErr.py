import cheby
import numpy as np
import matplotlib.pyplot as plt


def sigmoid(a):
    return 1 / (1 + np.exp(-a))


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


x = np.arange(-6., 6., 0.2)
sig = sigmoid(x)

b5 = cheby.Cheby.fit(sigmoid, -6, 6, 5)
c5 = cheby.Cheby.asTaylor(b5)
sig_approx_5 = cheby_approx_5th(x)
plt.plot(x, abs(sig_approx_5 - sig), label='5th order Chebyshev Approximated Sigmoid Error Function')

b4 = cheby.Cheby.fit(sigmoid, -6, 6, 4)
c4 = cheby.Cheby.asTaylor(b4)
sig_approx_4 = cheby_approx_4th(x)
plt.plot(x, abs(sig_approx_4 - sig), label='4th order Chebyshev Approximated Sigmoid Error Function')

b3 = cheby.Cheby.fit(sigmoid, -1, 1, 3)
print(b3)
c3 = cheby.Cheby.asTaylor(b3)
print(b3)
sig_approx_3 = cheby_approx_3rd(x)
plt.plot(x, abs(sig_approx_3 - sig), label='3rd order Chebyshev Approximated Sigmoid Error Function')

b2 = cheby.Cheby.fit(sigmoid, -6, 6, 2)
c2 = cheby.Cheby.asTaylor(b2)
sig_approx_2 = cheby_approx_2nd(x)
plt.plot(x, abs(sig_approx_2 - sig), label='2nd order Chebyshev Approximated Sigmoid Error Function')

b1 = cheby.Cheby.fit(sigmoid, -6, 6, 1)
c1 = cheby.Cheby.asTaylor(b1)
sig_approx_1 = cheby_approx_1st(x)
plt.plot(x, abs(sig_approx_1 - sig), label='1st order Chebyshev Approximated Sigmoid Error Function')

leg = plt.legend()
plt.show()

