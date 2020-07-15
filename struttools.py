"""
Tools for making struts in SolidPython

Framework by David Palmer dmopalmer@gmail.com
Code by Dominic Alei alei.dominic@gmail.com
"""

import solid
# You can do solid.Cube, etc., or 'from solid import' what you need.
# It is common to abbreviate numpy as np, although there is nothing wrong with spelling it out in full everywhere
import numpy as np

def strut_between(xyz0, xyz1, strutsize=1, twist_deg=0):
    """
    Create a strut going between two points.
    :param xyz0: position of one end
    :param xyz1: position of other end
    :param strutsize: side of square cross section.  Later change to allow rectangular or other cross-sections
    :param twist_deg: By default, one face of the strut points down.  This allows a twist.
    :return: strut between requested locations
    """

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
    xyz0 = np.asarray(xyz0).resize(3)
    xyz1 = np.asarray(xyz1).resize(3)

    # You will want to know various things about the strut, such as its location,
    # length, angles, etc.
    # The position (of one end) is at xyz0, the other information is the same if
    # you placed that end at the 0,0,0 origin point, so get the position of the other
    # end in that frame

    xyz_diff = xyz1 - xyz0

    """
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
    """


if __name__ == '__main__':
    # In order of trickiness
    teststruts = [
        strut_between([0,0,0],[0,0,1]),
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

    for i, strut in enumerate(teststruts):
        scad_render_to_file(strut, f"strut_{i:d}.scad")
    


