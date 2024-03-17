import numpy as np

bits = 18  # total bits in fixed point representation
decBits = 12  # No of decimal/fraction bits
x = [-1.81581252, 8.84356223, -20.46942933, 21.93965266, -8.51356541]  # coefficients from Cheby class after fitting
print(x)

# Conversion from float to fixed point hexa
y = []
for v in x:
    print(int(v * 2**decBits), end=' ')
    #  k = int(v * 2**decBits) # truncation (no rounding)
    k = int(v * 2**(decBits+1) + 1) >> 1  # round decBits+1 bit position to decBits bit position after the decimal pnt
    if v < 0:
        y.append(hex(int((2**bits - 1) & k)))
    else:
        y.append(hex(k))
print("\n", y)

# Verification of conversion
z = []
for v in y:
    w = int(v, 16)
    if w & (1 << (bits-1)):  # https://www.delftstack.com/howto/python/python-hex-to-int/
        w -= 1 << bits
    z.append(w / 2**decBits)

print(z)
print(np.array(z) - np.array(x))  # quantization errors
