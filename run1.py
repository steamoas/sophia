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
    await left_attachment.run_angle(200, -275)
    await drive.straight(760)
    await drive.turn(-32)
    await drive.straight(45)
    await right_attachment.run_angle(200, 100)
    await drive.straight(100)
    await drive.turn(-10)
    await drive.straight(-125)
    await drive.turn(35)
    drive.settings(straight_speed=1000)
    await drive.straight(-205)
    await drive.turn(-15)
    await drive.straight(23)
    await wait(700)
    await left_attachment.run_angle(800, 400)
    await left_attachment.run_angle(200,-200)
    await drive.turn(20)
    await drive.straight(-500)

if __name__ == "__main__":
    run_task(run1())
