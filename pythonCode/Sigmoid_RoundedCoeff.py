import cheby
import numpy as np
import matplotlib.pyplot as plt

# We have to take into consideration that we are limited to 12 bits of precision after the decimal point. Therefore,
# We round 4 digits after the decimal point to reduce the error of loss in representing these numbers and
# Coefficients Note that we chose to fit the sigmoid between -6 and 6 due to the fact that beyond this range it will
# Be approximately 0 or 1 respectively


def sigmoid(a):
    return 1 / (1 + np.exp(-a))


def round_coefficients(c):
    return [int(round(x * 2 ** 16, 0)) for x in c]


def return_coefficients(c):
    return [round(x / 2 ** 16, 4) for x in c]


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
b5 = cheby.Cheby.fit(sigmoid, -6, 6, 5)
c5 = cheby.Cheby.asTaylor(b5)
print(c5)
sig_approx_5 = cheby_approx_5th(x)
plt.plot(x, sig_approx_5, label='5th order Chebyshev Approximated Sigmoid with exact coefficients')
b4 = cheby.Cheby.fit(sigmoid, -6, 6, 4)
c4 = cheby.Cheby.asTaylor(b4)
print(c4)
sig_approx_4 = cheby_approx_4th(x)
plt.plot(x, sig_approx_4, label='4th order Chebyshev Approximated Sigmoid with exact coefficients')
b3 = cheby.Cheby.fit(sigmoid, -6, 6, 3)
c3 = cheby.Cheby.asTaylor(b3)
print(c3)
sig_approx_3 = cheby_approx_3rd(x)
plt.plot(x, sig_approx_3, label='3rd order Chebyshev Approximated Sigmoid with exact coefficients')
b2 = cheby.Cheby.fit(sigmoid, -6, 6, 2)
c2 = cheby.Cheby.asTaylor(b2)
print(c2)
sig_approx_2 = cheby_approx_2nd(x)
plt.plot(x, sig_approx_2, label='2nd order Chebyshev Approximated Sigmoid with exact coefficients')
b1 = cheby.Cheby.fit(sigmoid, -6, 6, 1)
c1 = cheby.Cheby.asTaylor(b1)
print(c1)
sig_approx_1 = cheby_approx_1st(x)
plt.plot(x, sig_approx_1, label='1st order Chebyshev Approximated Sigmoid with exact coefficients')
plt.legend()
plt.show()
plt.close()
# Print rounded coefficients; Note that we round by shifting each coefficient 16 bits to the left by multiplying by
# 2^16 and taking the whole part of the number (since it would become a really large number) Then, we shift the
# Number 16 bits to the right by dividing by 2^16
c5 = return_coefficients(round_coefficients(c5))
print(c5)
sig_approx_5_r = cheby_approx_5th(x)
plt.plot(x, sig_approx_5_r, label='5th order Chebyshev Approximated Sigmoid with rounded coefficients')
c4 = return_coefficients(round_coefficients(c4))
print(c4)
sig_approx_4_r = cheby_approx_4th(x)
plt.plot(x, sig_approx_4_r, label='4th order Chebyshev Approximated Sigmoid with rounded coefficients')
c3 = return_coefficients(round_coefficients(c3))
print(c3)
sig_approx_3_r = cheby_approx_3rd(x)
plt.plot(x, sig_approx_3_r, label='3rd order Chebyshev Approximated Sigmoid with rounded coefficients')
c2 = return_coefficients(round_coefficients(c2))
print(c2)
sig_approx_2_r = cheby_approx_2nd(x)
plt.plot(x, sig_approx_2_r, label='2nd order Chebyshev Approximated Sigmoid with rounded coefficients')
c1 = return_coefficients(round_coefficients(c1))
print(c1)
sig_approx_1_r = cheby_approx_1st(x)
plt.plot(x, sig_approx_1_r, label='1st order Chebyshev Approximated Sigmoid with rounded coefficients')
plt.legend()
plt.show()
plt.close()
# Compare the values of the rounded coefficients with the actual coefficients to how much error does the rounding cause
plt.plot(x, abs(sig_approx_5 - sig_approx_5_r), label='Rounding Coefficients error for 5th order Chebyshev Approx')
plt.plot(x, abs(sig_approx_4 - sig_approx_4_r), label='Rounding Coefficients error for 4th order Chebyshev Approx')
plt.plot(x, abs(sig_approx_3 - sig_approx_3_r), label='Rounding Coefficients error for 3rd order Chebyshev Approx')
plt.plot(x, abs(sig_approx_2 - sig_approx_2_r), label='Rounding Coefficients error for 2nd order Chebyshev Approx')
plt.plot(x, abs(sig_approx_1 - sig_approx_1_r), label='Rounding Coefficients error for 1st order Chebyshev Approx')
plt.legend()
plt.show()