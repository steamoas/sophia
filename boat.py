from pybricks.tools import wait, run_task
from robot import drive, right_attachment,left_attachment

async def boat():
    await right_attachment.run_angle(200,-400)
    await drive.straight(60)
    await drive.turn(90)
    await drive.straight(355)
    await right_attachment.run_angle(200,-135)
    await drive.straight(-90)
    await right_attachment.run_angle(200,130)
    await drive.turn(5)
    await drive.straight(150)
    await right_attachment.run_angle(200,300)
    await wait(1000)
    await drive.straight(100)
    await drive.straight(-100)
    await drive.straight(100)
    await right_attachment.run_angle(200,-300)
    await drive.straight(-500)

if __name__ == "__main__":
    run_task(boat())
