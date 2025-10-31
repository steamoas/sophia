# import basic pybricks stuff
# this should be done automatically for you
# if you use tab to autocomplete
from pybricks.parameters import Button
from pybricks.tools import multitask, run_task, wait

# import our main drive base and hub
# the drive base is needed in order to change its settings,
# and the hub is needed to check which buttons are pressed
# and to display the current run number
from robot import hub, drive

# import the async functions from our other files
# the first thing is the filename without the .py extension,
# and the second thing is the name of the function
from mission1_COPY import mission1
from mission5_6_COPY import mission5_6

# set the hub's stop button to the left and right buttons simulataneously
# so that it doesn't conflict with the switcher's cancelling behavior
hub.system.set_stop_button((Button.LEFT, Button.RIGHT))

async def center_button_pressed_task():
    """
    A function that returns when the hub's center button is pressed.
    This is useful for multitasking.
    """
    # wait 3/4 of a second so that the run isn't instantly canceled when it is started
    await wait(750)

    # loop forever
    while True:

        # checks if the center button is in the hub's list of currently pressed buttons
        if Button.CENTER in hub.buttons.pressed():
            # end the function, cancelling the run
            return

        # wait 100 milliseconds between checking if the button is pressed
        await wait(100)

async def switcher(run_list: Dict, min_run_number: int, max_run_number:int):
    """
    A function to take in a list of programs and allow the user to
    switch between programs within the list on the robot.
    They can start and cancel the program that is currently active by pressing the center button
    and switch between the programs with the left and right arrow buttons.
    If you go under or over the min or max run number, it will wrap back around.

    Args:
        run_list (Dict): A dictionary that holds the runs you want to switch between.
        There should be no gaps in the keys.
        min_run_number (int): The minumum run number within run dictionary.
        max_run_number (int): The maximum run number within the dictionary.
    """

    # set the current run number to the minimum value
    current_run_number = min_run_number

     # collect the default drive base settings into a variable for use later
    default_drive_settings = drive.settings()

    # loop forever
    while True:

        # display the current run number on the hub
        hub.display.number(current_run_number)

        # collect a list of all the buttons currently being pressed on the robot
        pressed_buttons = hub.buttons.pressed()

        # checks if the left button is in the list of pressed buttons
        if Button.LEFT in pressed_buttons:
            # wrap the current run number back around to the maximum run number
            # if it is already at the minimum run number
            if current_run_number == min_run_number:
                current_run_number = max_run_number

            # subtract 1 from the current run number if it isn't already at the minimum value
            else:
                current_run_number -= 1

        # checks if the right button is in the list of pressed buttons
        if Button.RIGHT in pressed_buttons:
            # wrap the current run number back around to the minimum run number
            # if it is already at the maximum run number
            if current_run_number == max_run_number:
                current_run_number = min_run_number

            # add 1 to the current run number if it isn't already at the maximum value
            else:
                current_run_number += 1

        # checks if the center button is in the list of pressed buttons
        if Button.CENTER in pressed_buttons:

            # reset the drive base to the default settings in case the
            # previous program modified them
            # notice the asterisk: it converts the value we got earlier
            # to the values that the function requires
            drive.settings(*default_drive_settings)

            # set the drive base to use the gyro
            # this isn't strictly necessary, but it is good practice
            # because it doesn't always apply correctly
            drive.use_gyro(True)

            # starts the run associated with the current run number in the program list
            # if the current run number is missing from the program list, the program will crash
            # the multitask races it against the center button pressed task, effectively
            # cancelling it if the center button is pressed prior to the run finishing
            # if this happens, the robot will return to the switcher
            await multitask(run_list[current_run_number](), center_button_pressed_task(), race=True)

            # wait 3/4 of a second before returning control to the switcher so that the
            # user doesn't instantly start the task again
            await wait(750)

        # wait for 125 milliseconds before going to the next loop iteration, ensuring that the
        # run number switches slowly on the robot
        # if this was not here, the robot would loop though all the run numbers pretty much
        # instentaneously when an arrow button is pressed
        await wait(125)

# make an empty run list
run_list = {}

# add mission1 as run 1 in the run list
# the number represents the run number seen on the switcher,
# and the function represents the function that will be executed
# when the switcher is run with that number selected
# note that the parentheses are omitted: we do not want to run
# the function yet
run_list.update({1 : mission1})

# add mission 5_6 as run 2 in the run list
# rember not to add parentheses here
run_list.update({2 : mission5_6})

# runs the switcher task, passing in the run list we created,
# 1 as the min_run_number,
# and 2 as the max_run_number
run_task(switcher(run_list, 1, 2))
