from pybricks.parameters import Button, Stop
from pybricks.robotics import DriveBase
from robot import hub, drive

drive.use_gyro(True)
first_time = True
#7558, 0, 1889, 3, 7
drive.heading_control.pid(20000, 0, 25000, 3, 7)

while True:

    drive.straight(780 if first_time else 550)
    drive.turn(90)
    drive.straight(775)
    drive.turn(90)
    drive.straight(550)
    drive.turn(90)
    drive.straight(770)
    drive.turn(90)
    #drive.straight(-220)
    first_time = False
