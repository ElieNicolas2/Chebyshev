import numpy as np
import time
bits = 18  # total bits in fixed point representation
decBits = 12  # No of decimal/fraction bits

start_time = time.time()


def float2fixedHexa(v, bits, decBits):
    # k = int(v * 2**decBits) # truncation (no rounding)
    # k = int(v * 2**(decBits+1) + 1) >> 1 # round decBits+1 bit position to the decBits bit position after decimal pnt
    k = int(abs(v) * 2 ** (decBits + 1) + 1) >> 1
    if v < 0:
        k = -k
        # k = int(v * 2**decBits)
        # print(" show me = ", hex(int(2**bits - 1)& k), hex(k))
        return (hex(int((2 ** bits - 1) & k)))
        # return(hex(k))
    else:
        # k = int(v * 2**(decBits+1) + 1) >> 1
        return (hex(k))


def fixedHexa2float(v):
    w = int(v, 16)
    if w & (1 << (bits - 1)):  # https://www.delftstack.com/howto/python/python-hex-to-int/
        w -= 1 << bits
    return (w / 2 ** decBits)


def printFloat2HexaArray(x):
    print("Float:       ", x)
    print("FixedPntDec:   ", end='')
    # Conversion from float to fixed point hexa
    y = []
    for v in x:
        print(int(v * 2 ** decBits), end=' ')
        y.append(float2fixedHexa(v, bits, decBits))
    print("\nFixedPntHexa:", y)

    # Verification of conversion
    z = []
    for v in y:
        z.append(fixedHexa2float(v))
    print("Hexa2Float:  ", z)
    print("QuantizError:", np.array(z) - np.array(x))  # quantization errors
    # print()


def printDenormalizationFactors(n):
    print("DenormFactors <-:", end='')
    y = []
    for k in range(1, bits - decBits + 1):
        v = 2 ** (k * n)
        print("%.6f" % v, end=' ')
        y.append(float2fixedHexa(v, bits, decBits))
    print("\nDenormFactors <-:", y)

    print("DenormFactors ->:", end='')
    y = []
    for k in range(1, decBits):
        v = 2 ** (-k * n)
        print("%.6f" % v, end=' ')
        y.append(float2fixedHexa(v, bits, decBits))
    print("\nDenormFactors ->:", y)
    print('\n')


print("x^1.3 2nd-Order Cheby Poly Coefs:")
x = [-0.06843752, 0.82816745, 0.24052977]
printFloat2HexaArray(x)
printDenormalizationFactors(1.3)

print("x^1.3 4th-Order Cheby Poly Coefs:")
# x = [-0.02598245,  0.63102386,  0.55984442, -0.20898585,  -31.04410164]
x = [-0.02598245, 0.63102386, 0.55984442, -0.20898585, 0.04410164]
printFloat2HexaArray(x)
printDenormalizationFactors(1.3)

print("x^0.65 4th-Order Cheby Poly Coefs:")
# x = [-0.02598245,  0.63102386,  0.55984442, -0.20898585,  -31.04410164]
x = [0.1243976, 1.29261396, -0.69259889, 0.36012275, -0.08453917]
printFloat2HexaArray(x)
printDenormalizationFactors(0.65)

print("sqrt(x) 4th-Order Cheby Poly Coefs:")
x = [0.23080201, 1.29086721, -0.88893983, 0.48257525, -0.11530993]
printFloat2HexaArray(x)
printDenormalizationFactors(0.5)

print("1/sqrt(x) 4th-Order Cheby Poly Coefs:")
x = [2.92288377, -5.43497755, 6.71965114, -4.33192462, 1.12443058]
printFloat2HexaArray(x)
printDenormalizationFactors(-0.5)

print("1/x 4th-Order Cheby Poly Coefs:")
x = [7.0710675, -19.69669938, 27.02349093, -18.26940232, 4.87184062]
printFloat2HexaArray(x)
printDenormalizationFactors(-1)

print("-31.04410164 = ", float2fixedHexa(-31.04410164, bits, decBits))
print("0x20f4c = ", fixedHexa2float('0x20f4c'))

approx = fixedHexa2float('0x18c2')
exact = fixedHexa2float('0x18c5')
print("exact: ", exact, "approx: ", approx, "error: ", approx - exact)

# Record end time
end_time = time.time()

# Calculate elapsed time
elapsed_time = (end_time - start_time)*1000

# Display timing
print("Elapsed time: {:.5f} milliseconds".format(elapsed_time))



