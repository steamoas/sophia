from pybricks.tools import run_task, multitask, wait
from robot import drive, left_attachment, right_attachment

# Authors: Lewis, Jony
# Setup: 1.2 left


async def minecart():
    drive.heading_control.pid(14000, 0, 2000, 3, 7)
    drive.use_gyro(True)
    drive.settings(straight_speed=300)
   # await right_attachment.run_until_stalled(-80, duty_limit=20)
    await drive.straight(875)
    await drive.turn(75)
    await drive.straight(200)
    await  right_attachment.run_angle(300,170)
    #await wait(1000)
    #await  right_attachment.run_angle(205,-180)
    #drive.settings(straight_speed=500)
    #await drive.straight(-45)
    #await drive.turn(53)
    #await drive.straight(380)
    #await right_attachment.run_angle(900,267)
    #await drive.straight(-170)
    #await drive.turn(-45)
    #await drive.straight(620)
    #await drive.turn(54)
    #await right_attachment.run_angle(165,-220)
    #await drive.turn(-55)
    #await drive.straight(100)
    #await drive.turn(45)
    #await drive.straight(50)
    #await multitask(drive.straight(100),right_attachment.run_angle(100))
    #await drive.straight(-300)
    #await drive.turn(-90)
    #await drive.straight(-200)
    #await drive.turn(-30)
    #await drive.straight(-700)
    #await right_attachment.run_angle(200,-175)







if __name__ == "__main__":
    run_task(minecart())

