#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

#u is the position vector
#  q is charge
# v is the position of q
k = 9e9 #N * m**2 / C**2
def Electrostaticforce(u,q,v):
    q1 = 1.
    r_vec = v - u 
    r = np.sqrt(r_vec.dot(r_vec))# mod(v-u)
    
    F = (k  * q1 * q /r**3)*r_vec
    return F

u = np.array([0,0,0])
q = 1.

nx, ny = 64, 64
x = np.linspace(-2,2,nx)
y = np.linspace(-2,2,ny)

field = []
for a in x:
    for b in y:
        field.append(electrostaticforce(u,q,[a,b]))

v = [1e-6,0,0]
F = Electrostaticforce(u,q,v)
print F


    
