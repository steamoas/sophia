from pybricks.tools import wait, run_task
from robot import drive, right_attachment,left_attachment

async def three_balls():

    await drive.straight(800)
    await drive.turn(-90)
    await drive.straight(110)
    await drive.turn(70)
    drive.settings(straight_speed=900)
    await drive.straight(-800)
if __name__ == "__main__":
    run_task(three_balls())
