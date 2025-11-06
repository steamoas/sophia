
from pybricks.parameters import Button
from pybricks.tools import multitask, run_task, wait

from robot import hub, drive

hub.system.set_stop_button((Button.LEFT,Button.RIGHT))

async def center_button_pressed_task():

    while Button.CENTER in hub.buttons.pressed():
        await wait(15)
    while True:
        if Button.CENTER in hub.buttons.pressed():
            return
        await wait(75)

async def switcher(run_list: Dict, min_run_number: int, max_run_number:int):
    current_run_number = min_run_number
    default_drive_settings = drive.settings()
    hub.display.number(current_run_number)

    while True:

        pressed_buttons = hub.buttons.pressed()

        if Button.LEFT in pressed_buttons:
            if current_run_number == min_run_number:
                current_run_number = max_run_number
            else:
                current_run_number -= 1
            hub.display.number(current_run_number)
            while Button.LEFT in hub.buttons.pressed():
                await wait(15)

        elif Button.RIGHT in pressed_buttons:
            if current_run_number == max_run_number:
                current_run_number = min_run_number
            else:
                current_run_number += 1
            hub.display.number(current_run_number)
            while Button.RIGHT in hub.buttons.pressed():
                await wait(15)

        elif Button.CENTER in pressed_buttons:

            drive.settings(*default_drive_settings)
            drive.use_gyro(True)
            await multitask(run_list[current_run_number](),center_button_pressed_task(),race=True)
            drive.stop()

            while Button.CENTER in hub.buttons.pressed():
                await wait(15)
    await wait(25)

from tipthescales import tipthescales
from run1 import run1
from forge import forge

run_list = {}
run_list.update({1:run1})
run_list.update({2:tipthescales})
run_list.update({3:forge})

run_task(switcher(run_list,1,3))
