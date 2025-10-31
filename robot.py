from pybricks.hubs import PrimeHub
from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Port, Direction

hub = PrimeHub()

right_attachment = Motor(Port.B, Direction.COUNTERCLOCKWISE)
left_attachment = Motor(Port.F, Direction.CLOCKWISE)

left_drivemotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_drivemotor = Motor(Port.D, Direction.CLOCKWISE)
drive = DriveBase(left_drivemotor, right_drivemotor, 64, 112)
drive.use_gyro(True)
drive.heading_control.pid(7558, 0, 1889, 3, 7)
# default(7558, 0, 1889, 3, 7)
