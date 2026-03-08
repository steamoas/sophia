from pybricks.tools import run_task, multitask, wait
from robot import drive, left_attachment, right_attachment

# Authors: Lewis, Jony
# Setup: 1.2 left


async def minecart():
    drive.heading_control.pid(20000, 0, 2500, 3, 7)
    drive.use_gyro(True)
    drive.settings(straight_speed=300)
   # await right_attachment.run_until_stalled(-80, duty_limit=20)
    await drive.straight(932)
    await drive.turn(80)
    await drive.straight(202)
    await  right_attachment.run_angle(165,200)
    await wait(1000)
    await  right_attachment.run_angle(205,-180)
    drive.settings(straight_speed=900)
    await drive.straight(-200)
    await drive.turn(-80)
    await drive.straight(-925)






if __name__ == "__main__":
    run_task(minecart())
