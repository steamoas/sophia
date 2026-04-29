# Author(s): Lewis

from pybricks.tools import run_task, wait

from robot import drive, right_attachment, left_attachment
async def mission9():
    await right_attachment.run_until_stalled(-80, duty_limit=20)

    await right_attachment.run_angle(100, 80)

    await drive.straight(245)
    await drive.turn(-45)
    await drive.straight(280)

    await right_attachment.run_angle(100, -22)
    await drive.straight(35)
    await right_attachment.run_angle(100, -88)
    await wait(500)

    await drive.straight(-75)
    await wait(500)
    await drive.straight(50)
    await right_attachment.run_angle(100, 60)
    await drive.straight(-100)

    await drive.turn(15)
    await right_attachment.run_angle(100, -30)
    await drive.straight(45)
    await drive.turn(-50)

    await drive.straight(-200)
    await drive.turn(80)
    await drive.straight(-350)


if __name__=="__main__":
    run_task(mission9())
