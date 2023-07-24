#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:29:48 2023

@author: bruno.souza
"""

########### Run IPE Beamline ###########
# cff = 2.25

# Packages:
    
import numpy as np   # scientific computing library 
import Shadow        # used for shadow simulations


# Function to run IPE:
def run_Ipe(n_rays=1000000, energy=930, sig_h=0.0210644, sig_v=0.0086504, div_h=3.08582e-5, div_v=2.80626e-05,R1X=0,R4X=0):
   
    '''
    
   Run IPE Beamline 
   
   Parameters:
       
       - n_rays: number of rays in the simulation (float);
       - energy: energy [eV] (float, array or list);
       - sig_h: horizontal beam size [mm] (float);  
       - sig_v: vertical beam size [mm] (float); 
       - div_h: horizontal beam divergence [rad] (float);  
       - div_v: vertical beam divergence [rad] (float);  
       - R1X: Rx misalignment of IPE 1 (Shadow frame);
       - R4X: Rx misalignment of IPE 1 (Shadow frame);  
       
    
    Returns:
     
       - R: a file with the characteristics of the beam after passing through the optical elements of the simulation (Shadow extension);
       
     '''   
    
   
    # write (1) or not (0) SHADOW files start.xx end.xx star.xx
    iwrite = 0
    
    
    
    # initialize shadow3 source (oe0) and beam
    # oe - optical elements
    beam = Shadow.Beam()
    oe0 = Shadow.Source()
    oe1 = Shadow.OE()
    oe2 = Shadow.OE()
    oe3 = Shadow.OE()
    oe4 = Shadow.OE()
    oe5 = Shadow.OE()
    # oe6 = Shadow.OE()
    
    
    # Define variables. See meaning of variables in: 
    #  https://raw.githubusercontent.com/srio/shadow3/master/docs/source.nml 
    #  https://raw.githubusercontent.com/srio/shadow3/master/docs/oe.nml
    
    # Optical element 00: Source
    oe0.FDISTR = 3
    oe0.F_PHOT = 0
    oe0.HDIV1 = 0.00012
    oe0.HDIV2 = 0.00012
    oe0.IDO_VX = 0
    oe0.IDO_VZ = 0
    oe0.IDO_X_S = 0
    oe0.IDO_Y_S = 0
    oe0.IDO_Z_S = 0
    oe0.ISTAR1 = 5676561
    oe0.NPOINT = n_rays #1000000
    oe0.PH1 = energy    #930.0
    oe0.SIGDIX = div_h  #3.08582e-05
    oe0.SIGDIZ = div_v  #2.80626e-05
    oe0.SIGMAX = sig_h  #0.0210644
    oe0.SIGMAZ = sig_v  #0.0086504
    oe0.VDIV1 = 0.00012
    oe0.VDIV2 = 0.00012
    
    # Optical element 01: Toroidal mirror 
    oe1.ALPHA = 270.0
    oe1.DUMMY = 0.1
    oe1.FHIT_C = 1
    oe1.FILE_REFL = b'/home/ABTLUS/bruno.souza/Oasys/Au.dat'
    oe1.FMIRR = 3
    oe1.FWRITE = 1
    oe1.F_EXT = 1
    oe1.F_MOVE = 1
    oe1.F_REFLEC = 1
    oe1.RLEN1 = 140.0
    oe1.RLEN2 = 140.0
    oe1.RWIDX1 = 5.0
    oe1.RWIDX2 = 5.0
    oe1.R_MAJ = 2104733.6716
    oe1.R_MIN = 752.0631
    oe1.T_IMAGE = 0.0
    oe1.T_INCIDENCE = 89.213
    oe1.T_REFLECTION = 89.213
    oe1.T_SOURCE = 27377.0
    oe1.X_ROT = R1X
    
    # Optical element 02: PGM-MP
    oe2.ALPHA = 90.0
    oe2.DUMMY = 0.1
    oe2.FHIT_C = 1
    oe2.FILE_REFL = b'/home/ABTLUS/bruno.souza/Oasys/Au.dat'
    oe2.FWRITE = 1
    oe2.F_REFLEC = 1
    oe2.RLEN1 = 240.0
    oe2.RLEN2 = 240.0
    oe2.RWIDX1 = 5.0
    oe2.RWIDX2 = 5.0
    oe2.T_IMAGE = 0.0
    oe2.T_INCIDENCE = 87.49854
    oe2.T_REFLECTION = 87.49854
    oe2.T_SOURCE = 1123.0
    
    # Optical element 03: PGM-GR
    oe3.ALPHA = 180.0
    oe3.DUMMY = 0.1
    oe3.FHIT_C = 1
    oe3.FWRITE = 1
    oe3.F_GRATING = 1
    oe3.RLEN1 = 70.0
    oe3.RLEN2 = 70.0
    oe3.RULING = 1100.0
    oe3.RWIDX1 = 5.0
    oe3.RWIDX2 = 5.0
    oe3.T_IMAGE = 0.0
    oe3.T_INCIDENCE = 88.46116
    oe3.T_REFLECTION = 86.53592
    oe3.T_SOURCE = 876.9999999999989
    
    # Optical element 04: Cylindrical mirror
    oe4.ALPHA = 270.0
    oe4.CIL_ANG = 90.0
    oe4.DUMMY = 0.1
    oe4.FCYL = 1
    oe4.FHIT_C = 1
    oe4.FILE_REFL = b'/home/ABTLUS/bruno.souza/Oasys/Au.dat'
    oe4.FMIRR = 1
    oe4.FWRITE = 1
    oe4.F_EXT = 1
    oe4.F_MOVE = 1
    oe4.F_REFLEC = 1
    oe4.RLEN1 = 125.0
    oe4.RLEN2 = 125.0
    oe4.RMIRR = 753.8375872541807
    oe4.RWIDX1 = 7.5
    oe4.RWIDX2 = 7.5
    oe4.T_IMAGE = 0.0
    oe4.T_INCIDENCE = 89.1888
    oe4.T_REFLECTION = 89.1888
    oe4.T_SOURCE = 2000.0
    oe4.X_ROT = R4X
    
    # Optical element 05: Slit
    oe5.DUMMY = 0.1
    oe5.FWRITE = 3
    oe5.F_REFRAC = 2
    oe5.F_SCREEN = 1
    oe5.I_SLIT = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    oe5.N_SCREEN = 1
    oe5.RX_SLIT = np.array([1000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    oe5.RZ_SLIT = np.array([1000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    oe5.T_IMAGE = 0.0
    oe5.T_INCIDENCE = 0.0
    oe5.T_REFLECTION = 180.0
    oe5.T_SOURCE = 26623.0
    
    # Optical element 06: Ellipsoid mirror
    # oe6.ALPHA = 180.0
    # oe6.DUMMY = 0.1
    # oe6.FHIT_C = 1
    # oe6.FILE_REFL = b'/home/ABTLUS/bruno.souza/Oasys/Au.dat'
    # oe6.FMIRR = 2
    # oe6.FWRITE = 1
    # oe6.F_DEFAULT = 0
    # oe6.F_REFLEC = 1
    # oe6.RLEN1 = 75.0
    # oe6.RLEN2 = 75.0
    # oe6.RWIDX1 = 7.5
    # oe6.RWIDX2 = 7.5
    # oe6.SIMAG = 1500.0
    # oe6.SSOUR = 33500.0
    # oe6.THETA = 88.5
    # oe6.T_IMAGE = 0.0
    # oe6.T_INCIDENCE = 88.5
    # oe6.T_REFLECTION = 88.5
    # oe6.T_SOURCE = 33500.0
    
    
    
    #Run SHADOW to create the source
    
    if iwrite:
        oe0.write("start.00")
    
    beam.genSource(oe0)
    
    if iwrite:
        oe0.write("end.00")
        beam.write("begin.dat")
    
    
    #
    #run optical element 1
    #
    print("    Running optical element: %d"%(1))
    if iwrite:
        oe1.write("start.01")
    
    beam.traceOE(oe1,1)
    
    if iwrite:
        oe1.write("end.01")
        beam.write("star.01")
    
    
    #
    #run optical element 2
    #
    print("    Running optical element: %d"%(2))
    if iwrite:
        oe2.write("start.02")
    
    beam.traceOE(oe2,2)
    
    if iwrite:
        oe2.write("end.02")
        beam.write("star.02")
    
    
    #
    #run optical element 3
    #
    print("    Running optical element: %d"%(3))
    if iwrite:
        oe3.write("start.03")
    
    beam.traceOE(oe3,3)
    
    if iwrite:
        oe3.write("end.03")
        beam.write("star.03")
    
    
    #
    #run optical element 4
    #
    print("    Running optical element: %d"%(4))
    if iwrite:
        oe4.write("start.04")
    
    beam.traceOE(oe4,4)
    
    if iwrite:
        oe4.write("end.04")
        beam.write("star.04")
    
    
    #
    #run optical element 5
    #
    print("    Running optical element: %d"%(5))
    if iwrite:
        oe5.write("start.05")
    
    beam.traceOE(oe5,5)
    
    if iwrite:
        oe5.write("end.05")
        beam.write("star.05")
    
    
    # #
    # #run optical element 6
    # #
    # print("    Running optical element: %d"%(6))
    # if iwrite:
    #     oe6.write("start.06")
    
    # beam.traceOE(oe6,6)
    
    # if iwrite:
    #     oe6.write("end.06")
    #     beam.write("star.06")
    
    
    # Shadow.ShadowTools.plotxy(beam,1,3,nbins=101,nolost=1,title="Real space")
    # Shadow.ShadowTools.plotxy(beam,1,4,nbins=101,nolost=1,title="Phase space X")
    # Shadow.ShadowTools.plotxy(beam,3,6,nbins=101,nolost=1,title="Phase space Z")
    
    return beam