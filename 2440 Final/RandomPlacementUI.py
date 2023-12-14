import maya.cmds as cmds
import random


class RandomPlacementUI:
    def __init__(self):
        self.window_name = 'Randomized Placement'
        if cmds.window('%sWindow' % self.window_name, exists=True):
            self.delete_window()

    def delete_window(self):
        if cmds.window('%sWindow' % self.window_name, exists=True):
            cmds.deleteUI('%sWindow' % self.window_name)

    def create_ui(self):
        self.delete_window()
        self.window_name = cmds.window('%sWindow' % self.window_name, title='%s Tool' % self.window_name,
                                       widthHeight=(300, 100))
        cmds.columnLayout(adjustableColumn=True, rs=1)
        cmds.intSliderGrp("Number", label="Number of Duplicates", field=True)

        # Use floatSliderGrp for horizontal float sliders
        for axis in ["x", "y", "z"]:
            cmds.floatSliderGrp(f"{axis}Max", label=f"{axis.upper()} Max", value=100, field=True, min=-100, max=100, step=0.1,
                                changeCommand=lambda value, a=axis: self.update_slider_min_max(f"{a}Max",
                                                                                               f"{a}Min", value))
            cmds.floatSliderGrp(f"{axis}Min", label=f"{axis.upper()} Min", value=-100, field=True, min=-100, max=100, step=0.1,
                                changeCommand=lambda value, a=axis: self.update_slider_min_max(f"{a}Min",
                                                                                               f"{a}Max", value))

        cmds.button(label="Randomize", command=self.randomizer)
        cmds.showWindow(self.window_name)

    def update_slider_min_max(self, source_slider, target_slider, value, *args):
        # Get the current value of the source slider
        source_value = cmds.floatSliderGrp(source_slider, query=True, value=True)

        # Update the min or max value of the target slider based on which slider triggered the change
        if source_slider.endswith("Min"):
            cmds.floatSliderGrp(target_slider, edit=True, min=source_value)
        elif source_slider.endswith("Max"):
            cmds.floatSliderGrp(target_slider, edit=True, max=source_value)

    def randomizer(self, *args):
        selected_objects = cmds.ls(selection=True)
        x_min = cmds.floatSliderGrp("xMin", query=True, value=True)
        x_max = cmds.floatSliderGrp("xMax", query=True, value=True)
        y_min = cmds.floatSliderGrp("yMin", query=True, value=True)
        y_max = cmds.floatSliderGrp("yMax", query=True, value=True)
        z_min = cmds.floatSliderGrp("zMin", query=True, value=True)
        z_max = cmds.floatSliderGrp("zMax", query=True, value=True)

        dupes = cmds.intSliderGrp("Number", query=True, value=True)

        for obj in selected_objects:
            for i in range(dupes):
                y_coord = random.uniform(y_min, y_max)
                z_coord = random.uniform(z_min, z_max)
                x_coord = random.uniform(x_min, x_max)
                print(z_coord, x_coord, y_coord)
                dupe_obj = cmds.duplicate(obj)
                cmds.move(x_coord, y_coord, z_coord, dupe_obj, worldSpace=True, relative=False)

            y_coord = random.uniform(y_min, y_max)
            z_coord = random.uniform(z_min, z_max)
            x_coord = random.uniform(x_min, x_max)
            print(z_coord, x_coord, y_coord)
            cmds.move(x_coord, y_coord, z_coord, obj, worldSpace=True, relative=False)


ui_instance = RandomPlacementUI()
ui_instance.create_ui()
