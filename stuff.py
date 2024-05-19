import pyautogui as pyg
import time
import os



def main():
      menu()
      time.sleep(10)



# Helper function
def findClick(nameOfFile):
    nameOfFile = pyg.locateOnScreen(nameOfFile + '.png', confidence=0.8)
    pyg.moveTo(nameOfFile.left, nameOfFile.top)
    pyg.click()
    

# If other player leaves
if (findClick("left_game")):
      pyg.keyDown("F10")
      os.sleep(1.5)
      pyg.keyDown("Q")

# if other player invites
findClick("player_invite")
pyg.click()

# main loop
Alive = True
while Alive:
      findClick("left_game")
      


main()