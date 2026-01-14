from pybricks.tools import run_task
from robot import drive,right_attachment

async def heavy_lifting():

    await right_attachment.run_angle(150,-175)
    await drive.straight(775)
    await drive.turn(38)
    await right_attachment.run_angle(100, 97)
    await drive.straight(130)

    await right_attachment.run_angle(100, -113)
    await drive.straight(-100)
    await drive.turn(60)
    await drive.straight(-800)
    await drive.turn(110)
    await drive.straight(215)
    await right_attachment.run_angle(100, 165)
    await drive.straight(-100)
    await right_attachment.run_angle(100, -150)
    await drive.straight(-175)
    await drive.turn(-78)
    await drive.straight(265)
    await right_attachment.run_angle(100, 150)
    await drive.turn(-25)
    await drive.turn(-25)
    await right_attachment.run_angle(100, - 150)
    await drive.straight(250)
    await drive.turn(30)
    await drive.straight(250)
    await drive.turn(60)
    await drive.straight(650)



if __name__=="__main__":
    run_task(heavy_lifting())
