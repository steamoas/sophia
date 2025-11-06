from robot import drive
from robot import right_attachment, left_attachment
drive.heading_control.pid(20000, 0, 2500, 3, 7)
drive.use_gyro(True)
drive.settings(straight_speed=450)

def run1():
    right_attachment.run_time(35, 700)
    drive.straight(800)
    drive.turn(-22)
    drive.straight(25)
    right_attachment.run_time(225, 700,)

run1()
drive.turn(22)
drive.straight(-700)
drive.turn(-90)

right_attachment.run_time(-275, 700)

drive.turn(90)
drive.straight(-100)
drive.turn(20)
drive.straight(100)
drive.turn(-20)
drive.straight(650)
drive.turn(90)
drive.straight(425)
drive.turn(-90)
drive.straight(45)

right_attachment.run_angle(200, 90)
