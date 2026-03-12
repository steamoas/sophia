# Author(s): Lewis

from pybricks.tools import run_task, wait
from robot import drive, right_attachment, left_attachment

async def silo():
    await right_attachment.run_angle(500,90)
    await drive.straight (430)
    await drive.turn(5)
    for _ in range(3):
        await right_attachment.run_angle(800,-100)
        await right_attachment.run_angle(800,100)



if __name__=="__main__":
    run_task(silo())
