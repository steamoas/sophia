# mission: 1,2,3
# Author: Lewis
# Setup: Right Wheel 2.3

from pybricks.tools import multitask, run_task, wait
from robot import drive
from robot import right_attachment, left_attachment


async def run1():
    drive.heading_control.pid(20000, 0, 2500, 3, 7)
    drive.use_gyro(True)
    drive.settings(straight_speed=450, straight_acceleration=400)

    await right_attachment.run_angle(200, 55)
    await drive.straight(760)
    await drive.turn(-28)
    await drive.straight(45)
    await right_attachment.run_angle(200, 75)
    await drive.straight(100)
    await drive.turn(10)
    await drive.turn(-10)
    await drive.straight(-140)
    await drive.turn(38)
    await drive.straight(-350)
    await drive.turn(50)
    await drive.straight(300)
    await right_attachment.run_angle(200, -80)
    await drive.turn(5)
    drive.settings(straight_speed=1000)
    await drive.straight(-200)
    await drive.turn(40)
    await drive.straight(1700)


if __name__ == "__main__":
    run_task(run1())
