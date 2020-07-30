
    
#CREATE CUBE BETWEEN TWO POINTS

import numpy as np
from euclid3 import Point3
import math
from solid import scad_render_to_file
from solid.utils import *
import matplotlib.pyplot as plt
from solid import *
from Documents.PracticeCoding.Structtools.optimizetruss import getstructuredetails



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
    alpha = np.arctan2((p2[1]-p1[1]),(p2[0]-p1[0]))
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

    nodes,segs = getstructuredetails('Warren')
    scalednodes = []
    for n in nodes:
        scalednodes.append([n[0]*scalefactor, n[1]*scalefactor])
    #sparwidth
    t = 2.0  
    #---------------------- here we go
    #initialize bridge
    bridge = createjoint([0,0],0)
    #loop through nodes and create them
    for p in scalednodes:
        bridge = bridge + createjoint(p,t)
    #loop through segments and create them
    for s in segs:
        bridge = bridge + createseg(scalednodes[s[0]],scalednodes[s[1]],t)

    #render to openScad    
    scad_render_to_file(bridge, outfn)      

#------------------------------END, Random below-------------------------------

    
