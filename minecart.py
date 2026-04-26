from pybricks.tools import run_task, multitask, wait
from robot import drive, left_attachment, right_attachment, hub

# Authors: Lewis, Jony
# Setup: 1.2 left


async def minecart():
    print(hub.battery.voltage())
    drive.heading_control.pid(14000, 0, 2000, 3, 7)
    drive.use_gyro(True)
    drive.settings(straight_speed=300)
    await right_attachment.run_until_stalled(-80, duty_limit=20)
    await drive.straight(875)
    await drive.turn(74)
    await drive.straight(200)
    await  right_attachment.run_angle(200,200)
    await  right_attachment.run_angle(205,-180)
    drive.settings(straight_speed=500)
    await drive.straight(-45)
    await drive.turn(58)
    await drive.straight(360)
    await right_attachment.run_angle(900,267)
    await drive.straight(-170)
    await drive.turn(-42)
    await drive.straight(630)
    await drive.turn(54)
    await right_attachment.run_angle(165,-250)
   # await right_attachment.run_angle(165,50)
   # await drive.straight(-50)
    #await drive.turn(-56)
    print("starting")
    await right_attachment.run_angle(300,-30)
    print("ending")
    await drive.straight(100)
    await drive.turn(47)
    await drive.straight(70)
    # await drive.straight(60)
    await right_attachment.run_angle(165,30)
    await multitask(drive.straight(130),right_attachment.run_angle(250,100))
    # drive.settings(straight_speed=927)
    # await drive.straight(140)
    # await drive.straight(-50)
    # await drive.turn(-45)
    # await drive.straight(400)
    # await drive.turn(90)
    # await drive.straight(600)

    #await drive.straight(-300)
    #await drive.turn(-90)
    #await drive.straight(-200)
    #await drive.turn(-30)
    #await drive.straight(-700)
    #await right_attachment.run_angle(200,-175)








if __name__ == "__main__":
    run_task(minecart())

