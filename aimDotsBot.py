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
    "Welcome to aimDotsBot, a bot made for Aim Dots© v1.19 by SoloOne\nFollow the procedure :"
    "\n1. Visit this link : https://scratch.mit.edu/projects/285825495/"
    "\n2. Put the project in fullscreen"
    "\n3. Launch the project by clicking on the green flag"
    "\n4. Press 'OK' to run the script"
    "\nThe bot plays independently. Press 'alt' button to pause/launch the process, press 'space' to stop the process...")

if userInput == "OK":
    # variables
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
    botRunning = True
    botToggle = True
    FPS = 0
    targetR = 255
    targetG = 255
    targetB = 255
    screenShotRegion = (394, 192, 1155, 826)
    imgResearchStep = 5
    # (x=394, y=192)
    # (x=1549, y=1018)

    # screenshot demo : pyautogui.screenshot("screenshot.png", region=screenShotRegion)

    # main loop
    while botRunning:
        # main script
        if botToggle:
            img = pyautogui.screenshot(region=screenShotRegion)
            imgX = 0
            imgY = 0
            while imgY < screenShotRegion[3]:
                if img.getpixel((imgX, imgY))[0] == targetR:
                    pyautogui.moveTo(screenShotRegion[0] + imgX, screenShotRegion[1] + imgY)
                    break
                else:
                    imgX += imgResearchStep
                    if imgX > screenShotRegion[2]-1:
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
