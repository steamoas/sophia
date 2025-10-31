from pybricks.tools import run_task

from robot import drive

async def mission1():
    await drive.straight(650)
    await drive.turn(-53)
    await drive.straight(225)
    await drive.turn(-37)
    await drive.straight(1300)
    await drive.turn(-90)
    await drive.straight(490)
    await drive.turn(-90)
    await drive.straight(1300)

if __name__ == "__main__":
    run_task(mission1())
