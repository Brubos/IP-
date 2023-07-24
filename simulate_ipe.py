#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:49:47 2023

@author: bruno.souza
"""

########### Simulate IPE Beamline - LNLS   ###########
# this script obtain the graphics:
    # FWHM Z 
    # FWHM X 
    # X mean position
    # Z mean position
    
# and a file .csv with the data 

## Packages:

import math as mt                                 # package with mathematical functions
import numpy as np                                # scientific computing library 
import time                                       # package to work with time
import sys                                        # library that allows indicating a path of a folder
import pandas as pd                               # package to work with data analysis
import matplotlib.pyplot as plt                   # library for creating charts and plots  
from itertools import product as prod             # function used to perform combinations
from run_ipe import run_Ipe                       # import the function that simulates the ipe beamline 
from optlnls.importing import read_shadow_beam    # function to read beam information
from optlnls.plot import plot_beam                # function to plot the beam information
sys.path.insert(0, '/home/ABTLUS/bruno.souza/miniconda3/envs/py38/lib/python3.8/site-packages/oasys_srw/')   

## Fixed Parameters:
energy = 930           # photon beam energy [eV]
n_rays = 1000000       # number of rays for shadow 
sig_h  = 0.0210644     # horizontal photon beam size [mm]
sig_v  = 0.0086504     # vertical photon beam size   [mm]
div_h  = 3.08582e-05   # horizontal photon beam divergence  [rad]
div_v  = 2.80626e-05   # vertical photon beam divergence    [rad]          


## Mirror angles [deg]
# R1X_deg = [-0.001,-0.0009,-0.0008,-0.0007,-0.0006,-0.0005,-0.0004,-0.0003,-0.0002,-0.0001,0  # Rx misalignment of IPE 1 (Shadow frame) [deg]
#             ,0.0001,0.0002,0.0003,0.0004,0.0005,0.0006,0.0007,0.0008,0.0009,0.001]  

# R4X_deg = [-0.001,-0.0009,-0.0008,-0.0007,-0.0006,-0.0005,-0.0004,-0.0003,-0.0002,-0.0001,0  # Rx misalignment of IPE 4 (Shadow frame) [deg]
#             ,0.0001,0.0002,0.0003,0.0004,0.0005,0.0006,0.0007,0.0008,0.0009,0.001]  

R4X_deg= [-0.0147, -0.0146, -0.0145, -0.0144, -0.0143, -0.0142, -0.0141,
       -0.014 , -0.0139, -0.0138, -0.0137, -0.0136, -0.0135, -0.0134,
       -0.0133, -0.0132, -0.0131, -0.013 , -0.0129, -0.0128, -0.0127]


# Fixed angle for case 05
ang_deg = 55e-4                        # fixed angle [deg]


## Plot control:
  
plot_figure = True   # plots beam size and divergence
show_plots  = True   # show beam size and divergence plots  


## Lists to store data:

fwhm_h_size_list, fwhm_v_size_list = [] , []
x_peak_list, z_peak_list = [] , [] 
r1_µrad_list,r4_µrad_list = [] , []   
energy_list = []
case_list = []

t0 = time.time() 

## Case control:
case=5

# 01 - R1X varies and R4X stationary
# 02 - R1X stationary and R4X varies
# 03 - R1X = R4X varies equally
# 04 - R1X =- R4X varies equally in module
# 05 - R1X= fixed angle and R4X varies
    

###################################### (CASE 01: R1X e R4X=0) ##################################### 
# if(case == 1):
#     srx    = 1200e-3         # horizontal size range 
#     sry    = 25e-3           # vertical size range
    
#     for (r1,r4) in prod(R1X_deg,[0]):
#         print('r1={}, r4={}'.format(r1,r4))
#         print('\n')
#         title='Beam Size: 58 m, {}eV   R1X={}° e R4X={}°'.format(energy,r1,r4) 

# ####################################### (CASE 02: R1X=0 e R4X) ##################################### 
# if(case == 2): 
#     srx    = 1.2         # horizontal size range 
#     sry    = 20e-3       # vertical size range
    
#     for (r1,r4) in prod([0],R4X_deg):
#         print('r1={}, r4={}'.format(r1,r4))
#         print('\n')
#         title='Beam Size: 58 m, {}eV   R1X={}° e R4X={}°'.format(energy,r1,r4) 
    
# ####################################### (CASE 03: R1X = R4X) #####################################  
# if(case == 3):
#     srx    = 2.2         # horizontal size range 
#     sry    = 30e-3       # vertical size range
    
#     for (r1,r4) in zip(R1X_deg,R4X_deg):
#         print('r1={}, r4={}'.format(r1,r4))
#         print('\n')
#         title='Beam Size: 58 m, {}eV   R1X=R4X={}°'.format(energy,r1) 
        
        
# ###################################### (CASE 04: R1X = - R4X) ####################################  
# if(case == 4):
#     srx    = 1400e-3 #300e-3           # horizontal size range 
#     sry    = 30e-3 #20e-3            # vertical size range
#     for (r1,r4) in zip(R1X_deg,R4X_deg[::-1]):
#         print('r1={}, r4={}'.format(r1,r4))
#         print('\n')
#         title='Beam Size: 58 m, {}eV   R1X,R4X={}°,{}°'.format(energy,r1,r4)  


# ###################################### (CASE 05: R1X = ang e R4X) ####################################  
if(case == 5): 
    srx    = 3      # horizontal size range 
    sry    = 0.02     # vertical size range
    
    
    for (r1,r4) in prod([ang_deg],R4X_deg):
        print('r1={}, r4={}'.format(r1,r4))
        print('\n')
        title='Beam Size: 58 m, {}eV   R1X={}°,R4X={}°'.format(energy,r1,r4) 
    
# ###################################### (ESPECIAL CASE: R1X = ang e R4X = ang) ###################################  
# if(case == 10): 
#     srx    = 1.5      # horizontal size range 
#     sry    = 0.02     # vertical size range
    
    
#     for (r1,r4) in prod([ang_deg],R4X_deg):
#         print('r1={}, r4={}'.format(r1,r4))
#         print('\n')
#         title='Beam Size: 58 m, {}eV   R1X={}°,R4X={}°'.format(energy,r1,r4) 
    
#######################################################################################################  

    
    
############### Run IPE beamline:                  
            
        beam=run_Ipe(n_rays=n_rays, energy=energy, sig_h=sig_h, sig_v=sig_v, div_h=div_h, div_v=div_v,R1X=r1,R4X=r4)
            
# Plots beam size and divergence until the last element:
             
        if(plot_figure):
            beam2D_size = read_shadow_beam(beam, x_column_index=3, y_column_index=1, nbins_x=150, nbins_y=150, nolost=1, 
                                                  ref=23, zeroPadding=1, gaussian_filter=0)
                
            outputs_beam = plot_beam(beam2D_size, outfilename='IPE_beam_size_'+str(int(energy))+'eV_R1X='+str(float(r1))+'_R4X='+str(float(r4))+'.png',
                                        cut=0, textA=1, textB=5, textC=3, textD=0, fitType=3, xlabel='Hor.', ylabel='Ver.', plot_title=title, unitFactor=1e3,
                                        fwhm_threshold=0.5, x_range=1, y_range=1, x_range_min=-srx, x_range_max=srx, y_range_min=-sry, y_range_max=sry, cmap='jet',
                                        integral=0, zero_pad_x=40, zero_pad_y=16, export_slices=0, zlabel='ph/s/100mA/$\mu$m', show_plot=show_plots)
                
## Save the data       
            fwhm_h_size_list.append(outputs_beam['fwhm_x'])
            fwhm_v_size_list.append(outputs_beam['fwhm_z'])
            x_peak_list.append(outputs_beam['mean_x'])
            z_peak_list.append(outputs_beam['mean_z'])
            r1_µrad_list.append(mt.radians(r1)*1e6)          # convert degree to µrad and save in a list
            r4_µrad_list.append(mt.radians(r4)*1e6)          # convert degree to µrad and save in a list
            energy_list.append(energy)
            case_list.append(case)                           
        
# Print the total simulation time
 
print('Total time = %.2f s' %(time.time()-t0))

# Transform the list 'data' into DataFrame
data={"R1X":r1_µrad_list,"R4X":r4_µrad_list,"fwhm_x":fwhm_h_size_list, "fwhm_z":fwhm_v_size_list, 
      "mean_x":x_peak_list, "mean_z":z_peak_list, 'energy':energy_list, 'case':case_list}
df = pd.DataFrame(data)


## PLOTS

if(show_plots):
   
    ##### FWHM X
    plt.figure()
    plt.title("Beam Size at 58 m, E={}eV ".format(energy))
    plt.ylabel("FWHM X [$\mu$m]")
        
    if case == 1 or case == 3 or case == 4:
        plt.xlabel("R1X [$\mu$rad]")
        plt.plot(df['R1X'],df['fwhm_x'], '.')
    else: 
        plt.xlabel("R4X [$\mu$rad]")
        plt.plot(df['R4X'],df['fwhm_x'], '.')
         
    plt.ylabel("FWHM X [$\mu$m]")
    plt.grid(which='both',color='black',linewidth=0.15)
    plt.minorticks_on()
    plt.axhspan(55.58620714401975, 61.144827858421735, color='red', alpha=0.25, lw=0)
    plt.savefig('FWHMX',dpi=600)
   
    ##### FWHM Z
    plt.figure()
    plt.title("Beam Size at 58 m, E={}eV ".format(energy))
  
    if case == 1 or case == 3 or case == 4:
        plt.xlabel("R1X [$\mu$rad]")
        plt.plot(df['R1X'],df['fwhm_z'], '.')
    else: 
        plt.xlabel("R4X [$\mu$rad]")
        plt.plot(df['R4X'],df['fwhm_z'], '.')
          
    plt.ylabel("FWHM Z [$\mu$m]")
    plt.grid(which='both',color='black',linewidth=0.15)
    plt.minorticks_on()
    plt.axhspan(8.914717444461758, 9.806189188907934, color='b', alpha=0.25, lw=0)
    plt.savefig('FWHMZ',dpi=600)
    
    ##### POSITION OF MEAN X
    plt.figure()
    plt.title("Position of Mean X")
 
    if case == 1 or case == 3 or case == 4:
        plt.xlabel("R1X [$\mu$rad]")
        plt.plot(df['R1X'],df['mean_x'], '.')
    else: 
        plt.xlabel("R4X [$\mu$rad]")
        plt.plot(df['R4X'],df['mean_x'], '.')
          
    plt.ylabel("Position [$\mu$m]")
    plt.grid(which='both',color='black',linewidth=0.15)
    plt.minorticks_on()
    plt.savefig('Mean X',dpi=600)
    
    ##### POSITION OF MEAN Z
    plt.figure()
    plt.title("Position of Mean Z")
    
    if case == 1 or case == 3 or case == 4:
       plt.xlabel("R1X [$\mu$rad]")
       plt.plot(df['R1X'],df['mean_z'], '.')
    else: 
       plt.xlabel("R4X [$\mu$rad]")
       plt.plot(df['R4X'],df['mean_z'], '.')
              
    plt.ylabel("Position [$\mu$m]")
    plt.grid(which='both',color='black',linewidth=0.15)
    plt.minorticks_on()
    plt.savefig('Mean Z',dpi=600)
 
# # Save a .csv file with data
titlecsv='Case'+str(int(case))+'_IPE_beam_size_'+str(int(energy))+'eV_R1X='+str(float(r1))+'_R4X='+str(float(r4))+'.csv'
df.to_csv(titlecsv,index=False)


    