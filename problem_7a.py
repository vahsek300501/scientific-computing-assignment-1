# Problem 7a: Implementation of the formula (n + 1/n)**n for
# estimation of the number e.

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import numpy.linalg as npla
import scipy.linalg as spla

def e_by_limit(n):
    # Here n is the value
    # Your code for computing
    # e_n using the formula
    # goes here

    tmp = 1 + (1/n)
    e_n = pow(tmp,n)
    return abs((np.e-e_n)/np.e)

# Write some initializing statements and
# a looping construct within which to call
# the above function. Accumlate the error
# for each n in err_n

n = [10**k for k in range(1, 16)]
err_n = list(map(e_by_limit,n))

# Plot err_n versus n.
# Note that a log scale for the x-axis is better suited in displaying
# this plot.


N = [10**k for k in range(1, 16)]
plt.figure()
plt.semilogx(N, err_n, 'bo')
plt.grid(True)
plt.ylabel("$|e - (1 + 1/n)^n|/|e|$")
plt.xlabel("$n$")
plt.title("Error in computing e using the limit formula", fontsize=14)
plt.savefig("problem7a.pdf")