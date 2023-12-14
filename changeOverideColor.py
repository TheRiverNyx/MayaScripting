import maya.cmds as cmds

def Change_Shape_Color(color):
    selected_objects = cmds.ls(selection=True)  # get selected objects

    if not selected_objects:  # if there is nothing selected send a warning
        cmds.warning("Please select an object.")
        return

    for obj in selected_objects:  # for each object get their shape nodes
        shape_nodes = cmds.listRelatives(obj, shapes=True)

        if not shape_nodes:  # check for shape nodes
            cmds.warning(f"No Shape node found for {obj}.")
            continue

        print(f"Changing color for {obj}'s shape node(s): {shape_nodes}")

        for shape in shape_nodes:  # change color of overRideColor Attribute
            # Enable color override
            cmds.setAttr(f"{shape}.overrideEnabled", True)
            cmds.setAttr(f"{shape}.overrideRGBColors", True)
            # Set the RGB color values
            cmds.setAttr(f"{shape}.overrideColorRGB", *color)

# Example usage
Change_Shape_Color((1.0, 0.3, 0.1))  # RGB value
