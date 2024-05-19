import pyautogui as pyg
import time
import os



#top left  634,706
#bottom right 1003,749
regionChatBox = (634,706, 1003, 749)


def findClick(nameOfFile):
      nameOfFile = pyg.locateOnScreen(nameOfFile + '.png', confidence=0.8)
      pyg.moveTo(nameOfFile.left, nameOfFile.top)
      pyg.click()


fgsdjkfgjsd

#pyg.locateOnScreen(nameOfFile + ".png", confidence = 0.5)

#pyg.screenshot(None, region=regionChatBox)