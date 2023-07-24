#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 14:03:27 2023

@author: bruno.souza
"""

########### Calculate de geometric parameters of the photon beam (size and divergence) ###########

# Packages:  
from optlnls.source import get_k, und_source

# dml - dimensionless

# Parameters:
per = 58e-03                                     # undulator period [m]
k_max = 5.2                                      # K parameter   [dml]
e_spread = 0.084/100                             # energy spread [dml]
N_per = 18                                       # period number [dml]
L = N_per*per                                    # Undulator Length [m]
e_beam_size_h, e_beam_size_v = [19.3e-6, 1.9e-6] # electron beam size [μm]
e_beam_div_h, e_beam_div_v = [12.9e-6, 1.3e-6]   # electron beam divergence [μrad]
energy = 930                                     # energy [eV]
emm_h=250e-12                                    # horizontal emmitance [pm]
emm_v = (2/100)*emm_h                            # vertical emmitance (emm_v = emm_h*xy_coupling) [pm]
beta_h,beta_v=1.50,1.43                          # beta parameters
h = 1                                            # harmonics (in 90% of the cases is used h=1)

# Calculate beam size and divergence:
size_h, div_h = und_source(emittance=emm_h, beta=beta_h, e_spread=e_spread, und_length=L, und_period=per, 
                        ph_energy=energy, harmonic=h) # [μm], [μrad]
size_v, div_v = und_source(emittance=emm_v, beta=beta_v, e_spread=e_spread, und_length=L, und_period=per, 
                        ph_energy=energy, harmonic=h) # [μm], [μrad]


print('\n')
print('The horizontal and vertical beam size are: {:.5f} μm, {:.5f} μm '.format(size_h,size_v))
print('\n')
print('The horizontal and vertical beam divergence are: {:.5f} μrad, {:.5f} μrad '.format(div_h,div_v))


# One way to verify if the obtained values make sense is to look at the graph of beam size/divergence as a function of energy
# (typically found in line commissioning documents)
# FWHM_XY = 2.355*(σ _XY)