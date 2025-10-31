# this allows you to run an async function
# it should be automatically imported
# if you use tab to autocomplete
from pybricks.tools import run_task

from robot import drive

# define the run as an async function
async def mission1():
    # notice the use of "await"
    # this tells the robot to wait
    # for the function to finish before
    # moving to the next line

    # this is used when the thing you are doing "takes time"
    
    await drive.straight(650)
    await drive.turn(-53)
    await drive.straight(225)
    await drive.turn(-37)
    await drive.straight(1300)
    await drive.turn(-90)
    await drive.straight(490)
    await drive.turn(-90)
    await drive.straight(1300)

# this line checks if we are directly running the file
# we don't want want to automatically run the function when
# we import it into the switcher!
# if we are directly running the file,
# the function will be run
if __name__ == "__main__":
    run_task(mission1())
