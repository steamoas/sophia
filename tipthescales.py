# mission: 10
# Author: Mason
# Setuop: Redhome area 1.0 L wheel

from robot import drive, right_attachment

async def tipthescales():
    await drive.straight (250)
    await drive.turn (90)
    await drive.straight (1109)
    await right_attachment.run_angle(300,54)
    await drive.turn (-90)
    await drive.straight (70)
    await drive.straight (-100)
    await drive.turn (-90)
    drive.settings (straight_speed=400)
    await drive.straight (-850)
