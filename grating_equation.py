#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 11:09:38 2023

@author: bruno.souza
"""
########### Calculates the in and out angles of the grid as well as the plane mirror ###########


# Packages
import scipy.constants
import scipy as sc
import numpy as np


# Parameters
cff=2.25         # Cff constant [adim]
m=0              # order [adim]                   m não deveria ser negativo?
N = 1100*(1000)  # line density [lines/m]
E = 930          # energy [eV]

# Constants
c=sc.constants.c                            # speed of light [m/s]
h_js=sc.constants.h                         # Planck constant [J.s]
h_ev=h_js/(sc.constants.elementary_charge)  # Planck constant [eV.s]
lambd=(h_ev*c)/(E)                          # wavelength [m]

# Angle calculating (Grating equation)
sin_alfa= np.sqrt(1 + (  (cff*m*N*lambd)/(1-(cff)**2) )**2  ) + (m*N*lambd/(1-(cff)**2))
sin_beta= - (1 + (  (cff*m*N*lambd)/(1-(cff)**2) )**2  )**(1/2) - (((cff)**2)*m*N*lambd/(1-(cff)**2))

alfa_rad=np.arcsin(sin_alfa)
beta_rad=np.arcsin(sin_beta)

# Convert rad to degree
alfa_deg=np.rad2deg(alfa_rad)
beta_deg=np.rad2deg(beta_rad)

# angle of incidence of plane mirror
inc_angle_mirror= ((alfa_deg) + (abs(beta_deg)))/2

print('O ângulo de entrada na grade em relação a superfície é {:.5f}º \n'.format(90-alfa_deg))
print('O ângulo de saída da grade em relação a superfície é {:.5f}º \n'.format(90-abs(beta_deg)))
print('O ângulo de incidência no espelho plano em relação a superfície é {:.5f}º \n'.format(90-inc_angle_mirror))


