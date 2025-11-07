# mission: 1,2,3
# Author: Lewis

from pybricks.tools import multitask, run_task, wait
from robot import drive
from robot import right_attachment, left_attachment


async def run1():
    drive.heading_control.pid(20000, 0, 2500, 3, 7)
    drive.use_gyro(True)
    drive.settings(straight_speed=450)

    await right_attachment.run_angle(50,40)
    await drive.straight(800)
    await drive.turn(-22)
    await drive.straight(25)
    await right_attachment.run_time(225, 700)
    await drive.turn(22)
    await drive.straight(-450)
    await drive.turn(60)
    await drive.straight(300)
    await right_attachment.run_angle(700,-150)
    await drive.straight(-300)
    await drive.turn(-45)
    await drive.straight(-200)
if __name__ == "__main__":
    run_task(run1())
