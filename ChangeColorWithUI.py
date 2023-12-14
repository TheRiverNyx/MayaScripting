import maya.cmds as cmds


class ChangeColorUI:
    def __init__(self):
        self.window_name = 'Color Changer'
        if cmds.window('%sWindow' % self.window_name, exists=True):
            self.delete_window()

    def delete_window(self):
        if cmds.window('%sWindow' % self.window_name, exists=True):
            cmds.deleteUI('%sWindow' % self.window_name)

    def create_ui(self):
        self.delete_window()
        self.window_name = cmds.window('%sWindow' % self.window_name, title='%s Tool' % self.window_name,
                                       widthHeight=(300, 100))
        cmds.columnLayout(adjustableColumn=True)
        cmds.colorSliderGrp("colorSlider", label="Color", rgb=(1.0, 1.0, 1.0))
        cmds.button(label="Change Color", command=self.change_shape_color)
        cmds.showWindow(self.window_name)

    def change_shape_color(self, color):
        selected_objects = cmds.ls(selection=True)  # get selected objects
        color = cmds.colorSliderGrp("colorSlider", query=True, rgb=True)

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


UI = ChangeColorUI()
UI.create_ui()
