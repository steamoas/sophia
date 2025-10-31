# these should be automatically imported if you use tab to autocomplete
from pybricks.tools import run_task, wait

# import our main drivebase and motors
from robot import drive, left_attachment, right_attachment

# async function with the run
async def mission5_6():

    # everything indented underneath this will be run four times
    # think of it as loop(4)
    for _ in range(4):
        await drive.straight(100)
        await drive.turn(90)
    

    # use await to tell the robot to wait for the current function
    # to finish before moving on to the next line of the program
    # this is only needed when the function "takes time to finish"
    
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
    
    # notice the await here
    await wait(700)

# this checks if we are running the file directly
# we don't want to automatically run the function when
# we import it into main.py!

if __name__ == "__main__":
    # run_task is how we run an async function
    run_task(mission5_6())
