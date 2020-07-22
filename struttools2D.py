"""
Tools for making struts in SolidPython

Framework by David Palmer dmopalmer@gmail.com
Code by Dominic Alei alei.dominic@gmail.com


import solid
# You can do solid.Cube, etc., or 'from solid import' what you need.
# It is common to abbreviate numpy as np, although there is nothing wrong with spelling it out in full everywhere

from euclid3 import Point3
import numpy as np
from solid import scad_render_to_file
from solid.utils import extrude_along_path

from solid import scad_render_to_file
from solid.objects import cube, cylinder, hole, part, rotate
from solid.utils import FORWARD_VEC, right, up


    

def face(startpt, sidelength):
    #start = starting point as an array [0,0,0]
    #sidelength = int value
    #plane = decide which plane your face is on ('xy' for xy plane, etc..)
    face_pts = [Point3(startpt[0],startpt[1],0), Point3(startpt[0]+sidelength, startpt[1],0), Point3(startpt[0]+sidelength, startpt[1]+sidelength,0), Point3(startpt[0], startpt[1]+sidelength,0)]  
                 
    return face_pts
    
def linearpath(startpt, endpt):
    c = solid.objects.cube(2, startpt)
    return    

    
def extrude_object():
    sidelength = 2
    startpt = [0,0]
    endpt = [2,3]
    face(startpt, sidelength)
    linearpath(startpt, endpt)
        
        
    return

if __name__ == '__main__':
    outfn = 'outfile.scad'
    aobject = extrude_object()
    file_out = scad_render_to_file(aobject, outfn)
    scad_render_to_file(bridge, outfn)    
"""
    
#CREATE CUBE BETWEEN TWO POINTS

import numpy as np
from euclid3 import Point3
import math
from solid import scad_render_to_file
from solid.utils import *
import matplotlib.pyplot as plt
from solid import *

SEGMENTS = 48  
   
    
def createjoint(p,t):   
    #loop through nodes
    return left(p[0])(
                forward(p[1])(
                    color(Blue)(
                        cylinder(r=t/2, h=t, segments=SEGMENTS)
                    )
                )
            )

def createseg(p1,p2,t):
    
    linearpath = [Point3(0,0,0), Point3(0,0,t)]
    #calculations for the four corners of the face
    #alpha is the angle of the segment from the x-axis CCW
    if p2[0] == p1[1]:
        alpha = np.pi/2
    alpha = np.arctan((p2[1]-p1[1])/(p2[0]-p1[0]))
    #the x displacement of the corner from p1 and p2
    xoff = math.sin(alpha)*(t/2)
    #the y displacement of the corner from p1 and p2
    yoff = math.cos(alpha)*(t/2)    
    
    #1Acorner
    A1corner = [p1[0]-xoff,p1[1]+yoff]
    #B1corner
    B1corner = [p1[0]+xoff,p1[1]-yoff]
    #A2corner
    A2corner = [p2[0]-xoff,p2[1]+yoff]
    #B2corner
    B2corner = [p2[0]+xoff,p2[1]-yoff]
    
    #make the face from the 4 points that were defined earlier.
    face_pts = [Point3(A1corner[0], A1corner[1],0)]
    face_pts.append(Point3(A2corner[0], A2corner[1],0))
    face_pts.append(Point3(B2corner[0], B2corner[1],0))
    face_pts.append(Point3(B1corner[0], B1corner[1],0))
    #creates segment
    seg = extrude_along_path(shape_pts=face_pts,path_pts=linearpath)
    return seg

if __name__ == '__main__':
    #---------------------- initialization
    debug = True
    outfn = 'bridge.scad'
    
    scalefactor = 10
    #define nodes
    nodes = np.array([[0,0],[.5,1],[.8,.8],[1.5,2],[1.7,1.6],[2,1.3],[2.5,2.7],[3,2],[4.2, 3.2],[4.5,2.1],[5,2.65],[5.5,3.2],[6,2.1],[7.9,3.1],[7.8,2.1],[9.2,2],[9.9,2.6],[9.9,1.5],[10.5,1.2],[10.5,0.7],[11,1.1],[11.5,0]])
    scalednodes = []
    for n in nodes:
        scalednodes.append([n[0]*scalefactor, n[1]*scalefactor])
    #segments number coresponds to the indicies of the two nodes to connect. Example 0,1                        connects 0,0 and 1,3
    segments = [[0,1],[1,2],[0,2],[1,3],[2,3],[2,4],[2,5],[3,4],[4,5],[3,6],[4,7],[5,7],[6,7],[6,8],[7,9],[7,8],[7,11],[10,11],[8,11],[9,10],[9,12],[10,12],[11,12],[11,14],[12,14],[11,13],[13,14],[13,15],[14,15],[14,17],[13,16],[15,17],[16,17],[17,19],[17,18],[18,19],[19,20],[19,21],[16,18],[16,20],[19,20],[18,20],[20,21]]
    #sparwidth
    t = 2.0  
    #---------------------- here we go
    #initialize bridge
    bridge = createjoint([0,0],0)
    #loop through nodes and create them
    for p in scalednodes:
        bridge = bridge + createjoint(p,t)
    #loop through segments and create them
    for s in segments:
        bridge = bridge + createseg(scalednodes[s[0]],scalednodes[s[1]],t)

    #render to openScad    
    scad_render_to_file(bridge, outfn)      

#------------------------------END, Random below-------------------------------

    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:13:45 2020

@author: leafuser
"""


'''
if debug:
    print('alpha= ',alpha)
    print('xoff= ',xoff)
    print('yoff= ',yoff)
    #plt.plot([1,5,10,20], [1,5,10,20]   )
    plt.gca().set_aspect("equal")
    plt.plot(p1[0],p1[1], 'bo')
    plt.plot(p2[0],p2[1], 'bo')
    
    #A1corner
    plt.plot((p1[0]-xoff),(p1[1]+yoff), 'r+')
    #B1corner
    plt.plot((p1[0]+xoff),(p1[1]-yoff), 'r+')
    #A2corner
    plt.plot((p2[0]-xoff),(p2[1]+yoff), 'r+')
    #B2corner
    plt.plot((p2[0]+xoff),(p2[1]-yoff), 'r+')
    
    #plt.show()

def face(start, sidelength, plane):
    #start = starting point as an array [0,0,0]
    #sidelength = int value
    #plane = decide which plane your face is on ('xy' for xy plane, etc..)
    face_pts = [Point3(start[0], start[1], start[2])]  
    
    if plane == 'xy':
        face_pts.append(Point3(start[0]-sidelength, start[1], start[2]))
        face_pts.append(Point3(start[0]-sidelength, start[1]+sidelength, start[2]))
        face_pts.append(Point3(start[0], start[1]+sidelength, start[2]))

                
    return face_pts

def linearpath(start, end):
    outline = [Point3(start[0], start[1], start[2]), Point3(end[0], end[1], end[2])]

def extrude_bridge():
    startpt = [0,0,0]
    endpt = [3,4,0]
    face1 = face(startpt, 2, 'xy')
    path1 = linearpath(startpt,endpt)
    cube1 = extrude_along_path(shape_pts=face1, path_pts=path1)
    return cube1



   
    
    
    
    

    Create a strut going between two points.
    :param xyz0: position of one end
    :param xyz1: position of other end
    :param strutsize: side of square cross section.  Later change to allow rectangular or other cross-sections
    :param twist_deg: By default, one face of the strut points down.  This allows a twist.
    :return: strut between requested locations

    
    # To make a strut between two points you will want to:
    # 1) Make a strut of the right length, sticking straight up (z direction)
    # 2) Move it so that it is centered in (x,y)
    # 3) Turn it to point in the right direction
    # 4) Move it to put it in the right place

    # Positions are labeled 0,1 because arrays in Python and most other languages
    # start with element 0

    # It is easier if you know what type the coordinates are (list, tuple, array, etc.)
    # A numpy array of 3 values is a good choice.
    # This will convert the inputs to that type even if they are something else

    # You will want to know various things about the strut, such as its location,
    # length, angles, etc.
    # The position (of one end) is at xyz0, the other information is the same if
    # you placed that end at the 0,0,0 origin point, so get the position of the other
    # end in that frame
    
    

    DOMINIC, Here is where you start coding
    
    # Use Pythagoras's theorem to get the length of the new strut
    # (which will be the same length as the old strut, since it has only moved, not stretched)
    # The fast way to do this in Numpy is as follows
    # strutlength = np.sqrt(np.sum(xyz_diff ** 2))
    # but try writing it out on your own piece by piece

    strutlength = DOMINIC CODE

    # You will want to know what angles it is pointing at.
    # Angles in 3 dimensions are very tricky.
    # You have to know about:
    # The order in which you do rotations matters (the 'do not commute')
    #   Read up on Euler angles.
    #   Think about it a lot
    #   This will probably require a full video telecon with a lot of hand waving
    # What are radians vs degrees.
    #   Numpy uses radians (2*pi in a circle), solidpython uses degrees (360 in a circle).
    #   Convert with np.deg2rad() and np.rad2deg()
    # How do you go from xyz to angles?
    #   np.atan2 is very useful
        
        
    # Here's how to start
    # What is the angle of the strut projected onto the xy plane.
    #  In other words, what is the rotation about the z axis
    
    xyangle = np.atan2(.......)   # I always forget the order of arguments
    xylength = ......  # How much of the length is in the xy plane, using Pythagoras
    # The zlength is just the z part of xyz_diff
    # How far off the z axis do you want to be
    zdistangle = np.atan2(.....)   # 0 for straight up, pi (=180 degrees) for straight down, pi/2 (= 90 degrees) for horizontal
    

    # Now, do the steps
    # 1) Make a strut of the right length, sticking straight up (z direction)
    strut_up = Cube([size, size, strutlength])
    # 2) Move it so that it is centered in (x,y)
    # Should you be centering it?   
    # That will prevent different sized struts from having a face in the same plane for your build plate
    strut_up_centeredxy = translate([-size/2, -size/2, 0])(strut_up)
    # 3) Turn it to point in the right direction
    # First twist (is this the right direction?)
    strut_up_twisted = rotate([0, 0, twist_deg])(strut_up_centeredxy)
    # Then slant it by rotating it around the y axis (is htis the right axis? direction? units?)
    strut_slanted = rotate([0, np.rad2def(zangle), 0])(strut_up_twisted)
    # Then Rotate it around the z axis (again) to point it in the right direction
    # Always the same questions
    strut_turned = rotate([0,0,np.rad2def(zdistangle)])(strut_slanted)
    # 4) Move it to put it in the right place
    # The strut starts at the origin, so move it so it starts at the right starting place
    strut_moved = translate(xyz0)(strut_turned)
    
    return strut_moved

    #strut_up = Cube([10,10, 5])
    #strut_up_centeredxy = translate([-size/2, -size/2, 0])(strut_up) 
    ##strut_slanted = rotate([0, np.rad2deg(zangle), 0])(strut_up_twisted)
        
    
    
if __name__ == '__main__':
    # In order of trickiness
    teststruts = [
        strut_between([0,0],[0,0], 10),
        # strut_between([0, 0, 0], [0, 0, 10]),
        # strut_between([0, 0, 0], [10, 0, 0]),
        # strut_between([0, 0, 0], [0, 10, 0]),
        # strut_between([5, 0, 0], [5, 10, 0]),
        # strut_between([0, 0, 0], [10, 20, 0]),
        # strut_between([0, 0, 0], [0, 20, 10]),
        # strut_between([0, 0, 0], [10, 20, 30]),
        # strut_between([20, 30, 40], [30, 20, -50]),
        # And add twists, different sizes, etc, when you have that figured out
    ]
'''
    #for i, strut in enumerate(teststruts):
        #scad_render_to_file(strut, f"strut_{i:d}.scad")
               