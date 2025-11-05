from pybricks.tools import run_task
from robot import drive
async def i_dunno():
    drive.heading_control.pid(20000, 0, 2500, 3, 7)
    drive.use_gyro(True)
    drive.settings(straight_speed=300)
    await drive.straight(850)
    await drive.straight(-850)
