#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 09:12:24 2023

@author: bruno.souza
"""


########### Analysis the data from Ipe beamline simulation    ###########
# this script obtain:
    # the fit curve of FWHM Z - that varies with R1X or R4X angle
    # the angle that provides a minimum of FWHM Z
    # the shift of mean X point

## Packages:

import math as mt                                 # package with mathematical functions
import time                                       # package to work with time
import numpy as np                                # scientific computing library 
import sys                                        # library that allows indicating a path of  a folder
import pandas as pd                               # package to work with data analysis
import matplotlib.pyplot as plt                   # library for creating charts and plots  
from itertools import product as prod             # function used to perform combinations
from run_ipe import run_Ipe                       # import the function that simulates the ipe beamline 
from optlnls.importing import read_shadow_beam    # function to read beam information
from optlnls.plot import plot_beam                # function to plot the beam information
from scipy.optimize import curve_fit              # function to fit curves
from scipy.optimize import minimize_scalar        # function to find the minimum of a parabola
sys.path.insert(0, '/home/ABTLUS/bruno.souza/miniconda3/envs/py38/lib/python3.8/site-packages/oasys_srw/')   


# Importing the data and putting it in vectors
data=pd.read_csv('Case27_IPE_beam_size_930eV_R1X=0.0002_R4X=0.0005.csv')
R1X, R4X     = data['R1X'], data['R4X'] 
fwhmx, fwhmz = data['fwhm_x'], data['fwhm_z']
meanx, meanz = data['mean_x'], data['mean_z']
energy=data['energy'].iloc[0]
case=27   #data['case'].iloc[0]

# Plot Control 
saveplot = True   # if saveplot = True the generated images are saved 

# Chosing the data according to the case
if case == 1 or case == 3 or case == 4: 
    xdata = R1X 
else:
    xdata = R4X


# FITING A PARABOLA 

# Defining the fit curve 

def parab(x, a, b, c):
    return a*x**2 + b*x + c

poptpar, pcovpar = curve_fit(parab, xdata, fwhmz)

# Find the minimum of a parabola
parab_min=-poptpar[1]/(2*poptpar[0])    # min = -b/2*a
    
# Fitting curve: parabola

xfit = np.linspace(-282, -243, 101) 
yfit = parab(xfit, *poptpar)

# Calcuting the standard error
errorp=np.sqrt(np.diag(pcovpar))     



## FITING A LINE 

## Defining the fit curve 

######################## FITING A LINE ########################
def line(s,m,n):
    return m*s+n

poptline, pcovline = curve_fit(line, xdata, meanx)

# Fitting curve: line
xfit1 = np.linspace(-26, 10, 101)   
yfit1 = line(xfit1, *poptline)

# Calcuting the standard error
errorl=np.sqrt(np.diag(pcovline))

# Find the position that FWHM Z is minimum
position = poptline[0]*(parab_min) + poptline[1]



############### FWHM Z ###############

# plt.figure()
# plt.title("Beam Size at 58 m, E={}eV ".format(energy))
# plt.plot(xdata,fwhmz, '.',color='black', label='data')

# if case == 1 or case == 3 or case == 4:
#     plt.xlabel("R1X [$\mu$rad]")
# else: 
#     plt.xlabel("R4X [$\mu$rad]")
    
# plt.ylabel("FWHM Z [$\mu$m]")
# # plt.grid(which='both',color='black',linewidth=0.15)
# plt.minorticks_on()
# plt.axhspan(8.914717444461758, 9.806189188907934, color='b', alpha=0.25, lw=0, label='focus')
# plt.plot(xfit, yfit, '-', label='fit', color='r',alpha=0.5)
# plt.legend(loc='lower left')


# ## Table with fit information

# text =[ ['Equation', 'y = a$x^2$ + bx + c ',''] , 
#         [ '', '$Value$', 'Error' ],
#         [ 'a', f'{poptpar[0]:.4f}' , f'{errorp[0]:.4f}'],
#         [ 'b', f'{poptpar[1]:.4f}' , f'{errorp[1]:.4f}'],
#         [ 'c', f'{poptpar[2]:.4f}' , f'{errorp[2]:.4f}'], 
#         [ '$x_{(y=min)}$', f'{parab_min:.4f}', '-' ] ]

# columswidths = [0.2, 0.2, 0.2]
# cellcolours = [['lightgray', 'white', 'white'],
#   ['lightgray', 'lightgray', 'lightgray'],
#   ['lightgray', 'white', 'white'],
#   ['lightgray', 'white', 'white'],
#   ['lightgray', 'white', 'white'],
#   ['lightgray', 'white', 'white'] ]

# plt.table(text,cellLoc='center',loc='upper center',colWidths=columswidths,cellColours=cellcolours)

# if saveplot:
#     plt.savefig('FWHMZ_''case_'+str(case),dpi=600)





############### POSITION OF MEAN X ###############

plt.figure()
plt.title("Position of Mean X")
plt.plot(xdata, meanx, '.', color='black', label='data')

if case == 1 or case == 3 or case == 4:
    plt.xlabel("R1X [$\mu$rad]")
else: 
    plt.xlabel("R4X [$\mu$rad]")
     
plt.ylabel("Position [$\mu$m]")

# Drawn the center of the beam
plt.axhline(y = position, ls=':', color = 'royalblue', label = 'beam center',alpha=0.5)
plt.axvline(x= parab_min, color = 'royalblue',ls=':', alpha=0.5)

# Data plot
plt.plot(xfit1, yfit1, '-', label='fit', color='r',alpha=0.5)



## Table with fit information

text =[ ['Equation', 'y = mx + n',''] , 
        [ '', '$Value$', 'Error' ],
        [ 'm', f'{poptline[0]:.5f}' , f'{errorl[0]:.5f}'],
        [ 'n', f'{poptline[1]:.5f}' , f'{errorl[1]:.5f}'],
        [ 'y(x='+str(f'{parab_min:.5f})'), f'{position:.5f}', '-' ] ]

columswidths = [0.15, 0.2, 0.2]
cellcolours = [ ['lightgray', 'white', 'white'],
                ['lightgray', 'lightgray', 'lightgray'],
                ['lightgray', 'white', 'white'],
                ['lightgray', 'white', 'white'],
                ['lightgray', 'white', 'white']]
        
plt.table(text,cellLoc='center',loc='upper right',colWidths=columswidths,cellColours=cellcolours)
# plt.plot(0,0,'x',label='slit center',color='purple',alpha=0.25) 
plt.minorticks_on()
plt.legend(loc='lower left')

if saveplot:
    plt.savefig('MeanX_position_''case_'+str(case),dpi=600)

# # Save a .csv file with data

titlecsv='Case'+str(int(case))+'_Fit_curve_parameters.csv'

a,b,c=poptpar[0],poptpar[1],poptpar[2]
m,n=poptline[0],poptline[1]

output={"a":[poptpar[0]],"b":[poptpar[1]],"c":[poptpar[2]],'x0':[parab_min],'m':[poptline[0]],'n':[poptline[1]],'y(x0)':[position] } 
df=pd.DataFrame(output)
df.to_csv(titlecsv,index=False)

    
    