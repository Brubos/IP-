#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 14:22:04 2023

@author: bruno.souza
"""
########### Generate the graphics   ###########
# this script obtain:
    # a graph of mirrors angular variation (R1X versus R4X);
    # a graph of movement of X mean position (X mean position versus R1X);
    # a table with the fitting curve parameters
    # a graph of FWHM Z vs R1X
    # a graph of FWHM X vs R1X

## Packages:
import matplotlib.pyplot as plt                   # library for creating charts and plots  
from scipy.optimize import curve_fit              # function to fit curves
import numpy as np                                # scientific computing library 
import pandas as pd                               # package to work with data analysis

# Values from simulation (IPE BEAMLINE - 930 eV - cff=2.25 - focus at 58 m) :

# Variation of R1X (Rx misalignment of IPE 1 (Shadow frame) [µrad] ) between [-5e-4:5e-4]º in µrad
R1X= [-104.719755, -87.2664626, -69.8131701, -52.3598776, -34.906585, -17.4532925, -8.726646259971648, -6.981317007977318,
      -5.23598775598299, -3.4906585039886586, -1.7453292519943293, 0.0, 1.7453292519943302,3.4906585039886586, 5.23598775598299,
      6.981317007977319, 8.726646259971648, 17.4532925, 34.906585,52.3598776,69.8131701,87.2664626,104.719755]

# X mean position
mean=[-7585.4314,-6316.8771,-5050.3188,-3783.7683,-2524.783,-1277.1918,-648.2126,-517.7913,-399.1901,-266.9667,-148.0422,
-12.3598,102.9159,237.4111,354.3049,486.5794,603.5388,1237.3898,2495.9634,3753.1261,5014.4781,6276.9738,7545.5044]      
      
# # Variation of R4X [µrad]
# when we plot FWHM Z in function of R1X we obtain a parabola. The last points of the parabola within focus are y_min and y_max. 
# the y_cen represent the value of R1X where FWHM Z is minimal

y_min = [247.8367, 204.2035, 160.5702, 116.9370, 73.3038, 29.6705, 6.98131, 3.49065,-1.74532,-6.98131,-10.47197,
        -13.96263,-19.19862,-22.68928,-27.92526,-31.41592,-36.65191, -57.5958,-101.2290,-144.8623,-190.2408,-233.8741,-277.5073]

y_cen = [262.889, 219.0071, 175.1567, 131.3018, 87.5857, 44.0811,22.2308,17.7738,13.5388,9.0480,4.8070,0.2512,-3.9213,
          -8.4548,-12.6578,-17.1495,-21.3537,-43.2958,-87.0103,-130.7007,-174.4731,-218.2715,-262.1890]

y_max = [277.5073, 233.8741, 190.2408, 146.6076, 102.9744, 59.3411, 36.65191,33.16125,27.92526,24.43460,19.19862,15.70796,
          10.47197,6.98131,1.74532,-1.74532,-6.98131,-27.9252,-71.5584,-115.1917,-158.8249,-202.4581,-246.0914]

# FWHM Z (minimal value)

fwhmz = [8.8267,8.8485,8.8543,8.8647,8.8743,8.8763,8.8796,8.8867,8.8786,8.8829,8.8807,8.8842,8.8758,8.8837,8.8769,
         8.8875,8.8771,8.891,8.8786,8.8821,8.8771,8.8646,8.8464]

# FWHM X (average value)

fwhmx = [60.8737,59.5461,58.1478,56.9985,56.3065,55.4306,55.3378,55.3202,55.4129,55.424,55.4648,55.5275,55.5044,55.5182,55.4883,55.5372,55.5635,56.0362,
         56.7215,57.7542,59.1218,60.7519,61.7133]

# Creata a data frame to store the data
cases=[31,32,33,34,35,36,20,21,22,23,24,25,26,27,28,29,30,37,38,39,40,41,42] # simulation cases
data={'case':cases,'R1X [µrad]':R1X,'min [µrad]':y_min, 'middle [µrad]':y_cen,'max[µrad]':y_max, 'mean':mean, 'fwhmx':fwhmx, 'fwhmz':fwhmz}
 

##########################################################################################################################################################      

# Defining the function
def line(s,m,n):
    return m*s+n

def parab(x,a,b,c):
    return a*(x**2)+b*x+c

##########################################################################################################################################################

# Get the optimized parameters
poptline_min, pcovline_min = curve_fit(line, R1X, y_min)
poptline_cen, pcovline_cen = curve_fit(line, R1X, y_cen)
poptline_max, pcovline_max = curve_fit(line, R1X, y_max)
poptline_meanp, pcovline_meanp = curve_fit(line, R1X, mean)
poptparz, pcovz = curve_fit(parab,R1X,fwhmz)
poptparx, pcovx = curve_fit(parab, R1X, fwhmx)

##########################################################################################################################################################

# Fitting curve: line
xfit_min = np.linspace(-110, 110, 101) 
yfit_min = line(xfit_min, *poptline_min)

xfit_cen = np.linspace(-110, 110, 101)   
yfit_cen = line(xfit_cen, *poptline_cen)

xfit_max = np.linspace(-110, 110, 101) 
yfit_max = line(xfit_max, *poptline_max)

xfit_meanp=np.linspace(-110,110,101)
yfit_meanp=line(xfit_meanp, *poptline_meanp)

##########################################################################################################################################################

# Fitting curve: parabola
xfit_z=np.linspace(-110,110,101)
yfit_z=parab(xfit_z,*poptparz)

xfit_x=np.linspace(-110,110,101)
yfit_x=parab(xfit_x,*poptparx)

##########################################################################################################################################################
# Calcuting the standard error
error_min=np.sqrt(np.diag(pcovline_min))
error_cen=np.sqrt(np.diag(pcovline_cen))
error_max=np.sqrt(np.diag(pcovline_max))
error_meanp=np.sqrt(np.diag(pcovline_meanp))
error_parz =np.sqrt(np.diag(pcovz))
error_parx =np.sqrt(np.diag(pcovx))

##########################################################################################################################################################
# # Plot (R1X vs R4X)

# plt.figure()
# plt.title("Mirrors angular variation that maintains focus at 58m")
# plt.ylabel("R4X [$\mu$rad]")
# plt.xlabel("R1X [$\mu$rad]")

# plt.plot(R1X,y_cen, '.',color='black',alpha=1)
# plt.plot(xfit_cen, yfit_cen, '-', label='central', color='blue',alpha=0.3)

# plt.plot(R1X,y_max, '.',color='black',alpha=1)
# plt.plot(xfit_max, yfit_max, '-', color='gold',alpha=0.3)

# plt.plot(R1X,y_min, '.',color='black', label='data',alpha=1)
# plt.plot(xfit_min, yfit_min, '-', label='extremes', color='gold',alpha=0.3)

# # plt.fill_between(R1X, y_min, y_max, color='lightsalmon', alpha=0.5, label='allowed area')   # painting between two lines
# plt.minorticks_on() 
# plt.grid()
# plt.legend()
# plt.savefig('Mirrors_angular_variation',dpi=600)


# # Table with fit information

# plt.figure()
# plt.title("Fitting parameters", x=0.5,y=0.73)
# text =[ ['Equation', '$R4X$ = m($R1X$) + n',''] , 
#         [ '', '$Value$', 'Error' ],
#         [ '$m_{ext}$', f'{poptline_max[0]:.4f}' , f'{error_max[0]:.4f}'],
#         [ '$n_{ext}$', f'{poptline_max[1]:.4f}' , f'{error_max[1]:.4f}'],
#         [ '$m_{min}$', f'{poptline_cen[0]:.4f}' , f'{error_cen[0]:.4f}'],
#         [ '$n_{min}$', f'{poptline_cen[1]:.4f}' , f'{error_cen[1]:.4f}'],
#         [ '$m_{ext}$', f'{poptline_min[0]:.4f}' , f'{error_min[0]:.4f}'],
#         [ '$n_{ext}$', f'{poptline_min[1]:.4f}' , f'{error_min[1]:.4f}'],]

# columswidths = [0.2, 0.35, 0.35]
# cellcolours = [ ['lightgray', 'lightgray', 'lightgray'],
#                 ['lightgray', 'lightgray', 'lightgray'],
#                 ['lightgray', 'whitesmoke', 'whitesmoke'],
#                 ['lightgray', 'white', 'white'],
#                 ['lightgray', 'whitesmoke', 'whitesmoke'],
#                 ['lightgray', 'white', 'white'],
#                 ['lightgray', 'whitesmoke', 'whitesmoke'],
#                 ['lightgray', 'white', 'white'],]
                
# plt.table(text,cellLoc='center',loc='center',colWidths=columswidths,cellColours=cellcolours)
# plt.legend(loc='lower left')
# plt.axis('off')
# # Save the figure
# plt.savefig('Fitting curves parameters',dpi=600)

# ##########################################################################################################################################################

# # Plot (R1X vs X mean position)

# plt.figure()
# plt.title("Movement of X mean position")
# plt.ylabel("X mean position [$\mu$m]")
# plt.xlabel("R1X [$\mu$rad]")

# plt.plot(R1X,mean,'.',color='black', label='data')
# plt.plot(xfit_meanp,yfit_meanp,'-',color='red', label='fit',alpha=0.4)
# plt.grid(alpha=0.1)
# plt.minorticks_on() 
# plt.legend(loc='lower right')

# # Table with fit information
# text =[ ['Equation', 'y = mx + n',''] , 
#         [ '', '$Value$', 'Error' ],
#         [ 'm', f'{poptline_meanp[0]:.4f}' , f'{error_meanp[0]:.4f}'],
#         [ 'n', f'{poptline_meanp[1]:.4f}' , f'{error_meanp[1]:.4f}'] ]

# columswidths = [0.1, 0.14, 0.14]
# cellcolours = [ ['lightgray', 'white', 'white'],
#                 ['lightgray', 'lightgray', 'lightgray'],
#                 ['lightgray', 'white', 'white'],
#                 ['lightgray', 'white', 'white']]
              

# plt.table(text,cellLoc='center',loc='upper left',colWidths=columswidths,cellColours=cellcolours)
# # Save the figure
# plt.savefig('Movement_X_mean_position',dpi=600)

# # ##########################################################################################################################################################

# # Plot (R1X vs FWHM Z)
# plt.figure()
# plt.title("Minimum value of FWHM Z")
# plt.ylabel("FWHM Z [$\mu$m]")
# plt.xlabel("R1X [$\mu$rad]")
# plt.plot(xfit_z,yfit_z,'-',color='red', label='fit',alpha=0.4)
# plt.plot(R1X,fwhmz,'.',color='black', label='data',alpha=0.8)
# plt.grid(alpha=0.5)
# # Save the figure
# plt.savefig('FWHM_Z',dpi=600)

# # Table with fit information
# plt.figure()
# plt.title("Fitting curve parameters - (R1X vs FWHM Z)", x=0.5,y=0.73)
# text =[ ['Equation', '$FWHM_Z$ = a${(R1X)}^2$ + b(R1X) + c',''] , 
#         [ '', '$Value$', 'Error' ],
#         [ '$a$', f'{poptparz[0]:.7f}' , f'{error_parz[0]:.7f}'],
#         [ '$b$', f'{poptparz[1]:.7f}' , f'{error_parz[1]:.7f}'],
#         [ '$c$', f'{poptparz[2]:.7f}' , f'{error_parz[0]:.7f}'],]

# columswidths = [0.2, 0.35, 0.35]
# cellcolours = [ ['lightgray', 'lightgray', 'lightgray'],
#                 ['lightgray', 'lightgray', 'lightgray'],
#                 ['lightgray', 'whitesmoke', 'whitesmoke'],
#                 ['lightgray', 'whitesmoke', 'whitesmoke'],
#                 ['lightgray', 'whitesmoke', 'whitesmoke'],]

# plt.table(text,cellLoc='center',loc='center',colWidths=columswidths,cellColours=cellcolours)
# plt.axis('off')
# # Save the figure
# plt.savefig('FWHM_Z fitting parameters',dpi=600)

# # ##########################################################################################################################################################

# # PLOT (R1X vs FWHM X)
# plt.figure()
# plt.title("Average value of FWHM X")
# plt.ylabel("FWHM X [$\mu$m]")
# plt.xlabel("R1X [$\mu$rad]")
# plt.plot(xfit_x,yfit_x,'-',color='red', label='fit',alpha=0.4)
# plt.plot(R1X,fwhmx,'.',color='black', label='data')
# plt.grid(alpha=0.5)
# # Save the figure
# plt.savefig('FWHM_X',dpi=600)

# # Table with fit information
# plt.figure()
# plt.title("Parameters of fitting curve - (R1X vs FWHM X)", x=0.5,y=0.73)
# text =[ ['Equation', '$FWHM_X$ = a${(R1X)}^2$ + b(R1X) + c',''] , 
#         [ '', '$Value$', 'Error' ],
#         [ '$a$', f'{poptparx[0]:.4f}' , f'{error_parx[0]:.4f}'],
#         [ '$b$', f'{poptparx[1]:.4f}' , f'{error_parx[1]:.4f}'],
#         [ '$c$', f'{poptparx[2]:.4f}' , f'{error_parx[0]:.4f}'],]

# columswidths = [0.2, 0.35, 0.35]
# cellcolours = [ ['lightgray', 'lightgray', 'lightgray'],
#                 ['lightgray', 'lightgray', 'lightgray'],
#                 ['lightgray', 'whitesmoke', 'whitesmoke'],
#                 ['lightgray', 'whitesmoke', 'whitesmoke'],
#                 ['lightgray', 'whitesmoke', 'whitesmoke'],]

# plt.table(text,cellLoc='center',loc='center',colWidths=columswidths,cellColours=cellcolours)
# plt.legend(loc='lower left')
# plt.axis('off')
# # Save the figure
# plt.savefig('FWHM_X fitting parameters',dpi=600)



# Save the data in .csv file
df=pd.DataFrame(data)
df.to_csv('analysis.csv',index=False)

