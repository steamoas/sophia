# Author(s): Mason

from pybricks.tools import run_task
from robot import drive, right_attachment, left_attachment

async def tipthescales3():
    #await right_attachment.run_until_stalled(-180, duty_limit=20)
    #await right_attachment.run_angle(180,-20)
    await drive. straight (375)
    await drive.turn (-50)
    await drive.straight(115)
    await drive.turn(-55)
    await drive.straight(-50)
    await drive.turn(-45)
    await drive.staight(200)
    await drive.turn(-)
#     await drive. straight (526)
#     await drive. turn (100)
#     await drive.straight (12)
#     await right_attachment.run_angle(200,-90)
#     await drive.straight (-64)
#     await drive.turn (-90)
#     drive.settings (straight_speed=1000)
#     await drive.straight (-750)
if __name__=="__main__":
    run_task(tipthescales3())
