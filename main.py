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

async def switcher(run_list: Dict):
    min_run_number = min(run_list.keys())
    max_run_number = max(run_list.keys())

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

from tipthescales3 import tipthescales3
from run1 import run1
from switch_sides import switch_sides
from minecart import minecart
from forge import forge
from mission9 import mission9
from heavy_lifting import heavy_lifting

run_list = {}

run_list.update({1:run1})
run_list.update({2:minecart})
run_list.update({3:switch_sides})
run_list.update({4:heavy_lifting})
run_list.update({5:tipthescales3})
run_list.update({6:forge})
run_list.update({7:mission9})

run_task(switcher(run_list))
