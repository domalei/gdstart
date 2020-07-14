#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:28:33 2020

@author: leafuser
"""
#CREATE CUBE OF GIVEN DIMENSIONS
'''#import solid library and numpy
from solid import cube,scad_render_to_file
import numpy
#create array that will input 
dim = numpy.array(input().split(),int)
b = cube(dim)
scad_render_to_file(b, 'out_file.scad')'''

#CREATE CUBE BETWEEN TWO POINTS
import sys
from math import cos, radians, sin
import numpy as np
from euclid3 import Point3

from solid import scad_render_to_file
from solid.utils import extrude_along_path

SEGMENTS = 48


'''def sinusoidal_ring(rad=25, segments=SEGMENTS):
    outline = []
    for i in range(segments):
        angle = i * 360 / segments
        x = rad * cos(radians(angle))
        y = rad * sin(radians(angle))
        z = 2 * sin(radians(angle * 6))
        outline.append(Point3(x, y, z))
    return outline'''

'''def star(num_points=5, outer_rad=15, dip_factor=0.5):
    star_pts = []
    for i in range(2 * num_points):
        rad = outer_rad - i % 2 * dip_factor * outer_rad
        angle = radians(360 / (2 * num_points) * i)
        star_pts.append(Point3(rad * cos(angle), rad * sin(angle), 0))
    return star_pts'''


def face(start, sidelength, plane):
    #start = starting point as an array [0,0,0]
    #sidelength = int value
    #plane = decide which plane your face is on ('xy' for xy plane, etc..)
    face_pts = [Point3(start[0], start[1], start[2])]  
    
    if plane == 'xy':
        face_pts.append(Point3(start[0]-sidelength, start[1], start[2]))
        face_pts.append(Point3(start[0]-sidelength, start[1]+sidelength, start[2]))
        face_pts.append(Point3(start[0], start[1]+sidelength, start[2]))
    elif plane == 'yz':
        face_pts.append(Point3(start[0], start[1]+sidelength, start[2]))
        face_pts.append(Point3(start[0], start[1]+sidelength, start[2]+sidelength))
        face_pts.append(Point3(start[0], start[1], start[2]+sidelength))
    elif plane == 'xz':
        face_pts.append(Point3(start[0]+sidelength, start[1], start[2]))
        face_pts.append(Point3(start[0]+sidelength, start[1]+sidelength, start[2]))
        face_pts.append(Point3(start[0], start[1]+sidelength, start[2]))
                
    return face_pts

def linearpath(start, extrudelength, direction):
    if direction == 'x':
        outline = [Point3(start[0], start[1], start[2]), Point3(start[0]+extrudelength, start[1], start[2])]
    elif direction == 'y':
        outline = [Point3(start[0], start[1]+10, start[2]), Point3(start[0], start[1]+extrudelength, start[2])]
    elif direction == 'z':
        outline = [Point3(start[0], start[1], start[2]), Point3(start[0], start[1], start[2]+extrudelength)]
    return outline
 
def extrude_bridge():
    start1 = [0,0,0]
    
    face1 = face(start1, 2, 'xy')
    path1 = linearpath(start1,10,'z')
    cube1 = extrude_along_path(shape_pts=face1, path_pts=path1)
    
    start2 = [0,0,10]
    face2 = face(start2, 2, 'xz')
    print(np.array(face2))
    path2 = linearpath(start2,32,'y')
    print(np.array(path2))
    cube2 = extrude_along_path(shape_pts=face2, path_pts=path2)
    
    start3 = [0,10,0]
    face3 = face(start3, 2, 'xy')
    path3 = linearpath(start3,10,'z')
    cube3 = extrude_along_path(shape_pts=face3, path_pts=path3)
    
    return cube1+cube2+cube3


if __name__ == '__main__':
    outfn = 'outfile.scad'
    bridge = extrude_bridge()
    file_out = scad_render_to_file(bridge, outfn)
    scad_render_to_file(bridge, outfn)






