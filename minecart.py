from pybricks.tools import run_task, multitask, wait
from robot import drive, left_attachment, right_attachment

# Authors: Lewis, Jony
# Setup: 1.2 left

async def minecart():
    drive.heading_control.pid(20000, 0, 2500, 3, 7)
    drive.use_gyro(True)
    drive.settings(straight_speed=300)
    await right_attachment.run_until_stalled(-100,duty_limit=20)
    await drive.straight(705)
    await drive.turn(90)
    await drive.straight(450)
    await drive.turn(-90)
    await drive.straight(74)

    await multitask(right_attachment.run_angle(180, 200), drive.straight(-16))
    await drive.straight(6)
    await right_attachment.run_angle(180,20)
    await wait(500)
    await right_attachment.run_angle(400,-180)
    await drive.straight(-61)
    await drive.turn(90)
    await drive.straight(-350)
    await drive.turn(-90)
    await drive.straight(-700)




if __name__=="__main__":
    run_task(minecart())
