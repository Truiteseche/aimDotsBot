"""
Game link : https://scratch.mit.edu/projects/285825495/
Put it in fullscreen
Run the python script
"""

import time
import keyboard
import pyautogui

time.sleep(1)
userInput = pyautogui.confirm(
    "Welcome to illuminatiClickerBot, a bot made for ILLUMINATI CLICKER© v1.19 by Nickro_01\nFollow the procedure :"
    "\n1. Visit this link : https://scratch.mit.edu/projects/493520075/"
    "\n2. Put the project in fullscreen"
    "\n3. Launch the project by clicking on the green flag"
    "\n4. Press 'OK' to run the script"
    "\n5. Place your mouse on the illuminati triangle"
    "\nThe bot click automatically. Press 'alt' button to pause/launch the process, press 'space' to stop the process...")

if userInput == "OK":
    # variables
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
    botRunning = True
    botToggle = True
    FPS = 30
    targetR = 255
    targetG = 255
    targetB = 255
    screenShotRegion = (350, 123, 1200, 900)
    imgResearchStep = 5
    # (x=350, y=123)
    # (x=1551, y=1023)

    # main loop
    while botRunning:
        # main script
        if botToggle:
            img = pyautogui.screenshot(region=screenShotRegion)
            imgX = 0
            imgY = 0
            while imgY < screenShotRegion[3]:
                if img.getpixel((imgX, imgY))[0] == (targetR, targetG, targetB):
                    pyautogui.moveTo(screenShotRegion[0] + imgX, screenShotRegion[1] + imgY)
                    print("Loop broken")
                    break
                else:
                    imgX += imgResearchStep
                    if imgX > screenShotRegion[2]-1:
                        # print("imgX reset / imgY updated")
                        imgX = 0
                        imgY += imgResearchStep
                # print((imgX, imgY))

            # FPS manager
            if not FPS == 0:
                time.sleep(1 / FPS)

        try:
            if keyboard.is_pressed('alt'):
                botToggle = not botToggle
                while keyboard.is_pressed('alt'):
                    continue
            if keyboard.is_pressed('space'):
                botRunning = False
        except:
            print("Error : Something went wrong...")
            break
