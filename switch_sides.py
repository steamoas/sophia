from pybricks.robotics import DriveBase
from pybricks.tools import run_task
from robot import drive

async def switch_sides():


    drive.settings(straight_speed=500)
    await drive.straight(300)
    await drive.turn(95)
    await drive.straight(2000)
   # await drive.straight

if __name__=="__main__":
    run_task(switch_sides())
