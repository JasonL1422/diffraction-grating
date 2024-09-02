#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 23:28:56 2024

@author: jongcheollee
"""

import numpy as np
import matplotlib.pyplot as plt

def angle(thetai,lamda,m):
    d=3.33 * 10**-6; # typical d: 300 slits per mm. 
    return np.arcsin(np.sin(thetai * np.pi / 180) - m*lamda/d) * 180 / np.pi


m_values = list(range(-4,5))
plt.figure(dpi=400,figsize=(5,5))
for i in m_values:
    lamda=530e-9
    x = np.linspace(0, 90, 1000)
    y = angle (x,lamda,i)
    plt.plot(x,y,label=f'm={i}')

plt.xlabel('Incident angle (°)')
plt.ylabel('Diffraction angle (°)')
plt.xlim(0,80)
plt.ylim(-20,80)
plt.text(0,82,f'λ={lamda*1e9:.0f}nm', fontsize=12)
plt.legend()
plt.show()

m_values = list(range(-4,5))
plt.figure(dpi=300,figsize=(5,5))
for i in m_values:
    thetai=20
    x = np.linspace(400e-9, 700e-9, 2000)
    y = angle (thetai,x,i)
    plt.plot(x * 10**9,y,label=f'm={i}')

plt.xlabel('Wavelength (nm)')
plt.ylabel('Diffraction angle (°)')
plt.xlim(400, 700)
plt.ylim(-20,80)
plt.text(400,82,f'Inc angle ={thetai}(°)', fontsize=12)
plt.legend()
plt.show()

print(m_values)

"""
lamda=630e-9
x = np.linspace(0, 90, 1000)
y = angle (x,lamda)
plt.figure(dpi=300)
plt.plot(x,y,label=f'lamde={lamda*1e9:.0f}nm')
plt.xlabel('Incident angle (°)')
plt.ylabel('Diffraction angle (°)')
plt.legend()
plt.show()

thetai=40
x = np.linspace(400e-9, 800e-9, 2000)
y = angle (thetai,x)
plt.figure(dpi=300)
plt.plot(x * 10**9,y,label=f'Incident angle={thetai}°')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Diffraction angle (°)')
plt.legend()
plt.show()
"""

"""
fig = plt.figure(dpi=300, figsize=(8,8))
ax = fig.add_subplot(111, projection = '3d')

thetai = np.linspace(10,80,200)
lamda = np.linspace(400e-9,800e-9,10000)

x, y = np.meshgrid(thetai,lamda)
z = angle(x, y)
ax.plot_surface(x, y*1e9, z, cmap='copper')
ax.set_xlabel('Inc angle (°)', labelpad=5)
ax.set_ylabel('Wavelength (nm)', labelpad=5)
ax.set_zlabel('Dif angle (°)', labelpad=5)

ax.set_box_aspect([1, 1, 1])

#pos1 = ax.get_position()
#print('pos1=',pos1)
#ax.set_position([pos1.x0*0.01, pos1.y0*0.01, pos1.width * 0.8, pos1.height])
#pos2 = ax.get_position()
#print('pos2=',pos2)
ax.view_init(elev=30, azim=15) #elevation (tilt) and rotation (azimuth)

plt.subplots_adjust(left=0., right=0.9, top=0.9, bottom=0.1)
plt.show()
"""



