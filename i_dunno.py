from robot import drive
drive.heading_control.pid(20000, 0, 2500, 3, 7)
drive.use_gyro(True)
drive.settings(straight_speed=300)
drive.straight(850)
drive.straight(-850)
