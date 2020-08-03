#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:50:42 2020

@author: leafuser
"""
import random
import inspect
import matplotlib.pyplot as plt
#from matplotlib.widgets import Slider
import numpy as np
from anastruct import SystemElements

from optimizetruss import getstructuredetails
#these are in millimeters
minthickness = 0.25
strutwidth = 1.5
#50MPa tensile strength in N/mm2
tensilePLA = 50e6*(1e-3*1e-3)
#grams per cubic millimeter
densityPLA = 1.24e-3

tensileABS = 25e6*(1e-3*1e-3)
densityABS = 1.04e-3

elasticmodulusPLA = 3300e6*(1e-3*1e-3)
elasticmodulusABS = 1800e6*(1e-3*1e-3)

def makestructure(nodes,segs,fixednodes,loadnodes,thicknesses,tensile=tensilePLA,totalload = 100):
    
    ss = SystemElements()
    #loop through segments and create them
    for s,thickness in zip(segs,thicknesses):
        ss.add_element(location=[nodes[s[0]], nodes[s[1]]], EA=tensile*thickness*strutwidth,g=0, spring ={1:0.0001,2:0.0001})
    
    for f,supporttype in fixednodes:
        if supporttype == 'hinged':
            ss.add_support_hinged(node_id=f+1)
        elif supporttype == 'roll':
            ss.add_support_roll(node_id=f+1, direction='x')
        elif supporttype == 'fixed':
            ss.add_support_fixed(node_id=f+1)
    #add in other types of supports here
    for l in loadnodes:
        ss.point_load(l+1, Fx=0,Fy=-totalload/len(loadnodes))
    
    
    return ss

def thicknessforforce(force):
    if force == 0:
        thickness = minthickness
    elif force > 0:
        #tension
        thickness = force/(tensilePLA*strutwidth)
    elif force < 0:
        #compression(not technically correct)
        thickness = (-force)/(tensilePLA*strutwidth)
    return max(minthickness,thickness)
    


def optimize_segment_weights(nodes,segs,fixednodes,loadnodes,thicknesses,tensile=tensilePLA):
    nodes = np.reshape(np.asarray(nodes),(-1,2))	# Ensure an [[x,y],…] array shape
    
    if segs is None or loadnodes is None:
        raise RuntimeError('Need to specify segments and load values')
    
    for i in range(10):
        ss = makestructure(nodes,segs,fixednodes,loadnodes,thicknesses,tensile=tensilePLA)
        
        
        
        
        #supports and loads
        #ss.point_load(2,Fx=20,rotation=90)
        #ss.add_support_fixed(node_id=ss.id_last_node)
        #ss.point_load(2, Fx=0,Fy=-10)
        #ss.point_load(4, Fx=0,Fy=-10)
    
        #print(info)
        
        ss.show_structure()
        ss.solve()
        noderesults = ss.get_node_results_system()
        elementsresults = ss.get_element_results()
        newthicknesses = [thicknessforforce(result['N']) for result in elementsresults]
        print(thicknesses)
        
        #ss.show_bending_moment(factor=0.5)
        #ss.show_displacement(factor=1)
        ss.show_axial_force(factor=.05)
        #ss.show_reaction_force()
        #ss.show_shear_force()
        '''if np.allclose(newthicknesses, thicknesses, atol = 0.01):
            break'''
        thicknesses = newthicknesses
    elementweights = [thickness*strutwidth*result['length']*densityPLA
                      for thickness,result in zip(thicknesses,elementsresults)]
    totalweight = np.sum(elementweights)
    print(totalweight)
    return totalweight, thicknesses, ss



def main():
    nodes,segs,fixednodes,loadnodes = getstructuredetails('Warren')
    thicknesses = np.ones(len(segs))
    totalweight,thicknesses,ss = optimize_segment_weights(nodes,segs,fixednodes,loadnodes,thicknesses,tensile=tensilePLA)
            



if __name__ == '__main__':
    main()
