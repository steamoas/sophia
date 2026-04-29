from pybricks.tools import run_task
from robot import drive,right_attachment
from pybricks.tools import run_task
from robot import drive,right_attachment

async def silo_mill():

    drive.settings(straight_speed=350)
    await right_attachment.run_until_stalled(80, duty_limit=20)
    await right_attachment.run_angle(500,-300)
    await drive.straight(310)
    await right_attachment.run_angle(1000,300)
    await right_attachment.run_angle(600,-300)
    await right_attachment.run_angle(1000,300)
    await right_attachment.run_angle(600,-300)
    await right_attachment.run_angle(1000,300)
    await right_attachment.run_angle(600,-300)
    await drive.straight(500)
    await drive.turn(39)
    await right_attachment.run_angle(1000,300)
    await drive.straight(200)
    await right_attachment.run_angle(600,-300)
    await drive.straight(-200)
    await drive.turn(-45)
    await drive.straight(-700)


if __name__=="__main__":
    run_task(silo_mill())
