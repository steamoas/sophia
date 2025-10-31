from robot import drive
from robot import right_attachment, left_attachment
drive.heading_control.pid(20000, 0, 2500, 3, 7)
drive.use_gyro(True)
drive.settings(straight_speed=450)

drive.straight(800)
drive.turn(-22)
drive.straight(25)
right_attachment.run_time(1000, 700,)
