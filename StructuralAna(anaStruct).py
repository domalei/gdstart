#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:50:42 2020

@author: leafuser
"""
import matplotlib as plt
#from matplotlib.widgets import Slider
import numpy as np
from anastruct import SystemElements
ss = SystemElements()
#axSlider1 = plt.axes([0.1, 0.2, 0.8, 0.05])
#slider1 = Slider(axSlider1, 'Slider1', valmin=0, valmax=5)


#1
ss.add_element(location=[[0, 0], [.5, 1]])

#2
ss.add_element(location=[[0, 0], [.8, .8]])
#3
ss.add_element(location=[[.8, .8], [.5, 1]])
#4
ss.add_element(location=[[.5,1], [1.5,2]])
#5
ss.add_element(location=[[.8,.8], [1.7,1.6]])
#6
ss.add_element(location=[[.8, .8], [2, 1.3]])
#7
ss.add_element(location=[[2, 1.3], [1.7,1.6]])
#8
ss.add_element(location=[[1.7,1.6], [1.5,2]])
#9
ss.add_element(location=[[2, 1.3], [3, 2]])
#10
ss.add_element(location=[[1.7,1.6], [3, 2]])
#11
ss.add_element(location=[[1.5,2], [2.5, 2.7]])
#12
ss.add_element(location=[[2.5, 2.7], [3, 2]])
#13
ss.add_element(location=[[2.5, 2.7], [4.2, 3.2]])
#14
ss.add_element(location=[[3, 2], [4.2, 3.2]])
#15
ss.add_element(location=[[3, 2], [5.5,3.2]])
#16
ss.add_element(location=[[4.2, 3.2], [5.5,3.2]])
#17
ss.add_element(location=[[3, 2], [4.5,2.1]])
#18
ss.add_element(location=[[4.5,2.1], [5.5,3.2]])
#19
ss.add_element(location=[[4.5,2.1], [6,2.1]])
#20
ss.add_element(location=[[6,2.1], [5,2.65]])
#21
ss.add_element(location=[[5.5,3.2], [6,2.1]])
#22
ss.add_element(location=[[6,2.1], [7.8,2.1]])
#23
ss.add_element(location=[[5.5,3.2], [7.9,3.1]])
#24
ss.add_element(location=[[5.5,3.2], [7.8,2.1]])
#25
ss.add_element(location=[[7.9,3.1], [7.8,2.1]])
#26
ss.add_element(location=[[7.8,2.1], [9.2,2]])
#27
ss.add_element(location=[[9.2,2], [9.9,2.6]])
#28
ss.add_element(location=[[7.9,3.1], [9.9,2.6]])
#29
ss.add_element(location=[[7.9,3.1], [9.2,2]])
#30
ss.add_element(location=[[9.2,2], [9.9,1.5]])
#31
ss.add_element(location=[[7.8,2.1], [9.9,1.5]])
#32
ss.add_element(location=[[9.9,2.6], [9.9,1.5]])
#33
ss.add_element(location=[[9.9,1.5], [10.5,1.2]])
#34
ss.add_element(location=[[9.9,2.6], [10.5,1.2]])
#35
ss.add_element(location=[[10.5,1.2], [10.5,0.7]])
#36
ss.add_element(location=[[9.9,1.5], [10.5,0.7]])
#37
ss.add_element(location=[[10.5,0.7], [11,1.1]])
#38
ss.add_element(location=[[10.5,1.2], [11,1.1]])
#39
ss.add_element(location=[[9.9,2.6], [11,1.1]])
#40
ss.add_element(location=[[10.5,0.7], [11.5,0]])
#41
ss.add_element(location=[[11,1.1], [11.5,0]])

#supports and loads
ss.add_support_fixed(node_id=[1])
ss.point_load(10,Fx=10,rotation=90)
ss.add_support_fixed(node_id=ss.id_last_node)
#ss.q_load(q=-20, element_id=23, direction='element')
#ss.q_load(q=-20, element_id=16, direction='element')
#ss.q_load(q=-20, element_id=13, direction='element')
#ss.q_load(q=-20, element_id=28, direction='element')
ss.show_structure()
ss.solve()
#ss.show_bending_moment()
ss.show_displacement()
#ss.show_reaction_force()
#ss.show_shear_force()
plt.gca()
line = ax.lines[0]
line.get_xydata()

