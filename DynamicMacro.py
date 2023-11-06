import maya.cmds as cmds

size = 7.0  # base body size
bodyNumber = 8  # how many body segments there will be
moveUpLength = 0.0  # starting value
mayaObject = []  # object in maya

for x in range(bodyNumber):
    mayaObject.append(cmds.polySphere(r=size, sx=20, ax=(0, 1, 0), cuv=2, ch=1))  # creates polySphere with size=radius
    moveUpLength += 1.75 * size
    cmds.move(0, moveUpLength - size, 0, mayaObject[-1], r=True, os=True, wd=True)  # move sphere up 1.75* the height
    size -= size / bodyNumber  # move sphere down just a little bit
