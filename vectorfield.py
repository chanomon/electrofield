#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

#u is the position vector
#  q is charge
# v is the position of q
k = 9e9 #N * m**2 / C**2
def Electrostaticfield(u,q,X,Y):
    q1 = 1.
    x0 = u[0]
    y0 = u[1]
    


    #asdf
    r_vecx = x-x0
    r_vecy = y-y0
    r = np.hypot(r_vecx,r_vecy)
    
#    r = np.sqrt(r_vec.dot(r_vec))# mod(v-u)
    
    E = [k*( q /r**3) * (r_vec_x) , k*( q /r**3) * (r_vec_y)]
    return E

u = np.array([0,0,0])
q = 1.

nx, ny = 64, 64
x = np.linspace(-2,2,nx)
y = np.linspace(-2,2,ny)
X, Y = np.meshgrid(x,y)

#field = []

[Ex, Ey] = electrostaticfield(u,q,[x,y])

#v = [1e-6,0,0]
#F = Electrostaticfield(u,q,v)
#print F


    
