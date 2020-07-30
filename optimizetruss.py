# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:53:49 2020
@author: leafuser
"""


'''from . struttools2D import createjoint, createseg, teststructure
import anastruct
from functools import partial


def minweight(nodelocations,  *, segments=None, loads=None, **kwargs):
	weight, *otherresults = optimize_segment_weights(nodelocations,  *, segments, loads, **kwargs)
	return weight

def optimize_segment_weights(nodelocations, *, segments=None, loads=None, otherargs):
	nodelocations = np.asarray(nodelocations).resize((-1,2))	# Ensure an [[x,y],…] array shape
	if segments is None or loads is None:
		raise RuntimeError(“Need to specify segments and load values”)
	
	# For a few iterations, calculate the minimum weight of each segment that can bear the given loads
       ….
	return totalweight, segmentthicknesses, otherstuff 



#create another function that takes arguments(nodelocation, setments, seg thicknesses, other things) returns an anastruct model
    #results of optimize are nodelocations, segments, seg thicknesses, total weight
#first thing is to write function that returns anastruct model. create variables that control both the anastruct and solid python. 
    #also takes the same set of arguments and returns a solid python model.
    #	'''
#trusstype takes on one of three values: Warren, Miller, and Howe.
def getstructuredetails(trusstype):
    if trusstype == 'Warren':
        nodes = [[0,0],[5,10],[10,0],[15,10],[20,0]]
        segs = [[0,1],[1,2],[2,3],[3,4],[0,4 ],[1,3]]
    elif trusstype == "Howe":
        nodes = ([0,0],[5,10],[10,0],[15,10],[20,0])
        segs = ([0,1],[1,2],[2,3],[])
    elif trusstype == "Miller":
        nodes = ([0,0],[5,10],[10,0],[15,10],[20,0])
        segs = ([0,1],[1,2],[2,3],[])
    return nodes,segs
    
    



	
'''def optimal_structure(various_arguments)
	…
	# Set up the initial set of nodelocations, segments, desired loads, which nodes are fixed (footprint) vs which are free, etc.
    nodelocations = 
	loopstuff:
		# do things to change the segments around and generally try a different starting point
		#setup initial load locations and segements and optimize the loads. optimize by allowing the location to change
        ...
		function_to_optimize = partial(minweight, segments=segments, loads=loads, otherarg=otherarg, yetanother=yetanother...)
		result = scipy.optimize.whichever(function_to_optimize, starting_locations,…)
		…
        

def main():
    scalednodes,segments = teststructure()
    totalweight, segmentthicknesses, otherstuff = optimize_segment_weights()'''

