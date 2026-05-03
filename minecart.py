from pybricks.tools import run_task, multitask, wait
from robot import drive, left_attachment, right_attachment

# Authors: Lewis, Jony
# Setup: 1.2 left


async def minecart():
    drive.heading_control.pid(14000, 0, 2000, 3, 7)
    drive.use_gyro(True)
    drive.settings(straight_speed=450)

    await right_attachment.run_until_stalled(-80, duty_limit=20)
    await drive.straight(875)
    await drive.turn(73)
    await drive.straight(200)
    await right_attachment.run_angle(250,240)
    await right_attachment.run_angle(205,-190)
    #minecart
    drive.settings(straight_speed=500)
    await drive.straight(-45)
    await drive.turn(59)
    await drive.straight(360)
    await right_attachment.run_angle(500,267)
    # dino thing
    await drive.straight(-170)
    await drive.turn(-40)
    await drive.straight(530)
    await drive.turn(90)
    await drive.straight(105)
    await drive.turn(-87)
    await right_attachment.run_angle(165,-260)
    await right_attachment.run_angle(165,110)
    # tip the scales
    await drive.turn(-75)
    await drive.straight(210)
    await drive.turn(111)
    await right_attachment.run_until_stalled(-180, duty_limit=20)
    await wait(1000)
    await right_attachment.run_angle(165,65)
    await drive.straight(225)
    await multitask(drive.straight(80),right_attachment.run_angle(400,120))
    await right_attachment.run_angle(200,-35)
    await drive.straight(-120)
    drive.settings(straight_speed=900)
    await drive.turn(-35)
    await drive.straight(380)
    await drive.turn(65)
    await drive.straight(800)
   #  #await drive.straight(-300)
   #  #await drive.turn(-90)
   #  #await drive.straight(-200)
   #  #await drive.turn(-30)
   #  #await drive.straight(-700)
   #  #await right_attachment.run_angle(200,-175)







if __name__ == "__main__":
    run_task(minecart())
