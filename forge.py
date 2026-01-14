# Missions: 6, 3, 9
# Start position: BR3.0
# Authors: Cruz
# INCOMPLETE

from pybricks.tools import run_task
from robot import drive, left_attachment, right_attachment

async def forge():
    await drive.straight(800)
    await drive.turn(-90)
    await drive.straight(50)
    await drive.turn(85)
    await drive.straight(-700)
  #  await drive.turn(-34)
#    await drive.straight(400)
 #   await drive.turn(16)
   # await drive.straight(-140)
   # await drive.turn(-20)
   # await drive.straight(-300)

if __name__=="__main__":
    run_task(forge())
