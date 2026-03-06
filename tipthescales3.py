# Author(s): Mason

from pybricks.tools import run_task
from robot import drive, right_attachment, left_attachment

async def tipthescales3():
    await drive. straight (260)
    await right_attachment.run_angle(60,90)
    await drive. turn (-90)
    await drive. straight (526)
    await drive. turn (100)
    await drive.straight (12)
    await right_attachment.run_angle(60,-90)
    await drive.straight (-64)
    await drive.turn (-90)
    drive.settings (straight_speed=1000)
    await drive.straight (-750)
if __name__=="__main__":
    run_task(tipthescales3())
