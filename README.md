# Chebyshev Approximation Technique Design Repository

This repository contains Python code for software simulation/coefficient generation and SystemVerilog code for hardware implementation of the Chebyshev Approximation Technique Design algorithm.

## Overview

The Optimized Chebyshev Design algorithm is utilized for the design of digital filters, particularly to optimize passband and stopband ripple characteristics. This repository offers both hardware and software implementations of the algorithm, providing flexibility for various applications.

## Contents

1. **Software Simulations**
   - `cheby.py`: Python module for simulating the chebyshev algorithm in software environment which can be imported and used to find the Chebyshev Coefficients.
   - `Chebyshev.c`: Alternative C code for the same purpose.

2. **Hardware Implementation**
   - `ChebyshevOptimized.sv`: SystemVerilog code implementing the Optimized Chebyshev Design in hardware in which we input the coeffients as parameter logic.

## Usage

### Software Simulations
To perform software simulations, ensure you have Python installed along with the necessary libraries (e.g., NumPy). Import `cheby.py` to execute the software simulation. Use the fit function followed by the asTaylor function to obtain the coefficients as shown:


```Python
import cheby
import numpy as np

# Define the function which you want to approximate
def cos(a):
    return np.cos(a)
    
# Use the fit function: fit(function, a, b, degree of approximation)
c = cheby.Cheby.fit(cos, 0, 1, 4)

# AsTaylor function outputs the Chebyshev coefficients as 
# [a0, a1, a2, a3, a4] -> a0 + a1x + a2x^2 + a3x^3 + a4x^4 
coef = cheby.Cheby.asTaylor(c)

print(coef)
```

Next, used the `float2fixed.py` with the generated coefficients to obtain them in hexadecimal format to be inputted to `ChebyshevOptimized.sv`. Modify the script as needed to adjust parameters and analyze results.

### Hardware Implementation
To use the hardware implementation, you need a SystemVerilog compiler and a hardware description language (HDL) compatible toolchain. Simply include `ChebyshevOptimized.sv` in your project and instantiate the module as required. We also included top_level files.

## Contributing

Contributions to improve the implementations, fix issues, or add new features are welcome. Please follow the standard pull request process.

## License

This repository is licensed under the [License](LICENSE). Feel free to use the code in accordance with the terms specified in the license.

## Acknowledgments

Special thanks to contributors and the open-source community for their valuable contributions and support.
