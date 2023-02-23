import math


def calculateDegreeToDestination(currentX1, currentX2, currentX3, currentX4, destinationCenterH, destinationCenterW):

    centerFrontX = int((currentX1[0] + currentX2[0]) / 2)
    centerFrontY = int((currentX1[1] + currentX2[1]) / 2)
    centerFront = (centerFrontX, centerFrontY)

    centerBackX = int((currentX4[0] + currentX3[0]) / 2)
    centerBackY = int((currentX4[1] + currentX3[1]) / 2)
    centerBack = (centerBackX, centerBackY)

    currentCenterW = (centerFrontX + centerBackX) /2
    currentCenterH = (centerFrontY + centerBackY) /2

    if centerBack[0] - centerFront[0] == 0:
        a2 = 1
    else:
        a2 = (centerBack[1] - centerFront[1]) / (centerBack[0] - centerFront[0])

    a1 = (currentCenterH - destinationCenterH) / (currentCenterW - destinationCenterW)

    radian = math.atan(abs((a2 - a1) / (1 + a1 * a2)))
    degree = radian * (180 / math.pi)
    return degree, centerFront, centerBack