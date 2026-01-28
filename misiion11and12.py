from pybricks.tools import wait
from robot import drive, right_attachment,left_attachment

right_attachment.run_angle(200,-400)
drive.straight(60)
drive.turn(90)
drive.straight(350)
right_attachment.run_angle(200,-125)
drive.straight(-70)
right_attachment.run_angle(200,130)
drive.straight(140)
right_attachment.run_angle(200,300)
wait(1000)
drive.straight(-500)
