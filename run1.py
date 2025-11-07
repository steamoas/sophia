# mission: 1,2,3
# Author: Lewis

from pybricks.tools import multitask, run_task, wait
from robot import drive
from robot import right_attachment, left_attachment
drive.heading_control.pid(20000, 0, 2500, 3, 7)
drive.use_gyro(True)
drive.settings(straight_speed=450)

async def run1():
    await right_attachment.run_time(35, 700)
    await drive.straight(800)
    await drive.turn(-22)
    await drive.straight(25)
    await right_attachment.run_time(225, 700)
    await drive.turn(22)
    await drive.straight(-700)
    await drive.turn(-90)

    await right_attachment.run_time(-275, 700)

    await drive.turn(90)
    await drive.straight(-100)
    await drive.turn(20)
    await drive.straight(100)
    await drive.turn(-20)
    await drive.straight(650)
    await drive.turn(90)
    await drive.straight(450)
    await drive.turn(-90)
    await drive.straight(55)

    await multitask(right_attachment.run_angle(200, 130), drive.straight(-12))
    await wait(1000)
    await right_attachment.run_angle(400,-360)

if __name__ == "__main__":
    run_task(run1())
