#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 09:18:32 2021
Ejemplo de Ulises dibujado en mi generador de gausianillas
@author: juanjimenez
"""
import sys
# Add paths
sys.path.insert(1, './GNC')
sys.path.insert(1, './graphics')
sys.path.insert(1, './postproc')
sys.path.insert(1, './vehicles')
sys.path.insert(1, './algorithm')


import matplotlib.pyplot as pl
import numpy as np
from numpy import linalg as la
import gauss_dist

fig = pl.figure(7)
ax = pl.axes(projection='3d')

x = np.arange(0.,1000,10)
y = np.arange(0.,900,10)


[X,Y] = np.meshgrid(x,y)
Z = gauss_dist.gausianillas(X,Y,[600,600],[1000/np.sqrt(2),1000/np.sqrt(2)],0,1)
# Z2 = gausianillas(X,Y,[0.5,0.2],[0.1,0.2],np.pi/3,.5)
# Z3 = gausianillas(X,Y,[-0.9,-0.2],[0.2,0.4],np.pi/2,2)
# Z  = Z1 + Z2 + Z3

# ax.plot3D(500,500, gauss_dist.gausianillas(800,800,[600,600],[5000,5000],0,1),'o')
# ax.plot3D(600,600, gauss_dist.gausianillas(600,600,[600,600],[5000,5000],0,1),'o')
ax.plot_surface(X,Y,Z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

