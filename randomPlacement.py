import maya.cmds as cmds
import random


def randomizer(y_range, x_range, z_range):
    selected_objects = cmds.ls(selection=True)
    for obj in selected_objects:  # gets random float in a range for each coord
        y_coord = random.uniform(y_range[0], y_range[1])
        z_coord = random.uniform(z_range[0], z_range[1])
        x_coord = random.uniform(x_range[0], x_range[1])
        print(z_coord, x_coord, y_coord)
        cmds.move(x_coord, y_coord, z_coord, obj, worldSpace=True, relative=False)  # moves object to randomized coords


randomizer([-10.0, 10.0], [-10.0, 10.0], [-10.0, 10.0])
