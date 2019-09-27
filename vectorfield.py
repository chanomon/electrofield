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
    #q0 = -1.
    x0 = u[0] + 1.
    y0 = u[1]
    r_vecx = X-x0
    r_vecy = Y-y0
    r = np.hypot(r_vecx,r_vecy)
    
#    r = np.sqrt(r_vec.dot(r_vec))# mod(v-u)
    
    E0 = [k*( q /r**3) * (r_vecx) , k*( q /r**3) * (r_vecy)]


    x1 = u[0]
    y1 = u[1]
    r_vecx = X - x1
    r_vecy = Y - y1
        
    r = np.hypot(r_vecx,r_vecy)
    E = [E0[0] + k * (-q / r**3) * (r_vecx), E0[1] + k * (-q / r**3) * (r_vecy)]
    
    return E

u = np.array([-0.5,0.])
q = 1.

nx, ny = 64, 64
x = np.linspace(-1,1,nx)
y = np.linspace(-1,1,ny)
X, Y = np.meshgrid(x,y)

#field = []

[Ex, Ey] = Electrostaticfield(u,q,X,Y)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.streamplot(x,y,Ex, Ey, linewidth = 1 , cmap = plt.cm.inferno, density = 2 , arrowstyle = "->", arrowsize = 2)
plt.show()
#v = [1e-6,0,0]
#F = Electrostaticfield(u,q,v)
#print F


    
