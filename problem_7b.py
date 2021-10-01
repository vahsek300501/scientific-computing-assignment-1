# Problem 7b: Implementation of the Taylor series formula for
# estimation of the number e.
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import numpy.linalg as npla
import scipy.linalg as spla
import math

def calculate_e_relative_error():
    num = 1
    tmpFact = 1
    e_calc = 1.
    while(tmpFact != 0):
        tmpFact = (1/(math.factorial(num)))
        e_calc = e_calc + tmpFact
        num+=1
    return abs((e_calc-np.e)/np.e)

# Write some a looping construct to compute e by using the Taylor
# series sum. But, first, determine what stopping criterion you should
# use for determining if the sum has been computed.

# Notice that you cannot, of course, compute infinitely many terms of
# the sum. Thus, you will need to truncate the sum. Where should
# truncate it. It cannot be some user specified number of
# terms. However, Problem 6(b) may given you some hint.

print("\nThe relative error in computing e via Taylor series is "+str(calculate_e_relative_error()))
print("\nThe relative error in computing e via Taylor series upto 15th precision " +"is %1.15f"%calculate_e_relative_error())