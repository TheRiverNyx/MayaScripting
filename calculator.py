import maya.cmds as cmds


class CalculatorUI:
    def __init__(self):
        self.window_name = 'Calculate'
        if cmds.window('%sWindow' % self.window_name, exists=True):
            cmds.deleteUI('%sWindow' % self.window_name)

    def delete(self):
        if cmds.window('%sWindow' % self.window_name, exists=True):
            cmds.deleteUI('%sWindow' % self.window_name)

    def create(self):
        self.delete()
        self.window_name = cmds.window('%sWindow' % self.window_name, title='%s Tool' % self.window_name,
                                       widthHeight=(300, 100))
        cmds.columnLayout(adjustableColumn=True)
        cmds.button()
        cmds.button()
        cmds.button()
        cmds.showWindow(self.window_name)


myUi = CalculatorUI()
myUi.delete()
