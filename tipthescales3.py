# Author(s): Mason

from pybricks.tools import run_task
from robot import drive, right_attachment, left_attachment

async def tipthescales3():
    await drive. straight (260)
    await drive. turn (-90)
    await drive. straight (524)
    await drive. turn (90)
    await right_attachment.run_angle(60,45)
    await drive.straight (20)
    await right_attachment.run_angle(60,-45)
    await drive.straight (-65)
    await drive.turn (-90)
    await drive.straight (-750)
if __name__=="__main__":
    run_task(tipthescales3())
