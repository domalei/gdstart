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
ss = SystemElements()
from Documents.PracticeCoding.Structtools.optimizetruss import getstructuredetails


#axSlider1 = plt.axes([0.1, 0.2, 0.8, 0.05])
#slider1 = Slider(axSlider1, 'Slider1', valmin=0, valmax=5)
'''Add in the cordinates of the nodes and then refer to them rather than hard coding'''

#random generation

'''iterations =[]
for i in range(28):
    nums = random.uniform(0,3)
    iterations.append(nums)'''


#print(iterations)



#slider = Slider('Force', valmin=0, valmax=100)
#N takes out the info from details. n[0] incourperates all of the nodes and n[1] incourperates all of the segments. Therefore n[0][0] gives the first node independtly. 
nodes,segs = getstructuredetails('Warren')

#loop through segments and create them
for s in segs:
    ss.add_element(location=[nodes[s[0]], nodes[s[1]]], EA=15000, g=2)


#supports and loads
ss.add_support_fixed(node_id=[1])
#ss.point_load(2,Fx=20,rotation=90)
ss.add_support_fixed(node_id=ss.id_last_node)
ss.point_load(2, Fx=0,Fy=-10)
ss.point_load(4, Fx=0,Fy=-10)
info = []
info.append(ss.get_node_results_system())
#print(info)

ss.show_structure()
ss.solve()
#ss.show_bending_moment()
#ss.show_displacement(factor=1)
#ss.show_reaction_force()
#ss.show_shear_force()


