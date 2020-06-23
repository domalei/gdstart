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


def face(xdim, ydim):
    face_pts = [Point3(0,0,0)]
    face_pts.append(Point3(0,ydim,0))
    face_pts.append(Point3(xdim,0,0))
    face_pts.append(Point3(xdim,ydim,0))
    return face_pts

def linearpath(x,y,z):
    outline = [Point3(0,0,0), Point3(0,0,10), Point3(0, 20, 10), Point3(x,y,z)]
    return outline

def extrude_cube():
    shape = face(2, 2)
    path = linearpath(0,20,0)
    scales = [1]
    extruded = extrude_along_path(shape_pts=shape, path_pts=path)
    return extruded


if __name__ == '__main__':
    outfn = 'outfile.scad'
    acube = extrude_cube()
    file_out = scad_render_to_file(acube, outfn)
    scad_render_to_file(acube, outfn)






