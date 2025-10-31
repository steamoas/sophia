from pybricks.tools import wait
from robot import drive, left_attachment, right_attachment

async def mission5_6():
    for _ in range(4):
        drive.straight(100)
        drive.turn(90)


    drive.straight (235)
    drive.turn (90)
    drive.straight (890)
    drive.straight (-27)
    drive.straight(28)
    drive.straight (-27)
    drive.straight (28)
    drive.straight (-27)
    drive.straight (28)
    drive.straight (-27)
    drive.straight(28)
    wait(700)
