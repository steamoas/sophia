from pybricks.tools import run_task, wait
from robot import drive, left_attachment, right_attachment

async def mission5_6():
    for _ in range(4):
        await drive.straight(100)
        await drive.turn(90)


    await drive.straight (235)
    await drive.turn (90)
    await drive.straight (890)
    await drive.straight (-27)
    await drive.straight(28)
    await drive.straight (-27)
    await drive.straight (28)
    await drive.straight (-27)
    await drive.straight (28)
    await drive.straight (-27)
    await drive.straight(28)
    await wait(700)

if __name__ == "__main__":
    run_task(mission5_6())
