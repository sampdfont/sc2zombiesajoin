import pyautogui as pyg
import time

# TO DO later: leave instantly after skipping wave and jewels

def main():
      menu()
      time.sleep(3)

def menu():
      print("Select mode:\na- Start\nb- Exit")
      choice = input("Option: ")

      if choice == "a":
            print("Starting script..")
            listener()
            
      if choice == "b":
            print("Exit.")
            time.sleep(1)


# Helper function
def findClick(nameOfFile):
    try:
        location = pyg.locateOnScreen(nameOfFile + '.png', confidence=0.8)
        print(location)
        time.sleep(5)
        if location: 
            print("Player has left, leaving game.")
            return True
        else:
            print(location)
            time.sleep(5)
    except Exception as e:
         print(f"Error in findClick with {nameOfFile}: {e}")
         return False

# If other player leaves
def checkLeaveGame():
    findClick("left_game")
    time.sleep(1)
    pyg.press("f10")
    time.sleep(1.5)
    pyg.press("q")

# if other player invites
def joinGame():
    findClick("player_invite")
    pyg.click()

def listener():
    active = True
    while active:
        print("Listening..")
        checkLeaveGame()
        time.sleep(5) # msg leaves around 15 sec.
        

main()














# # main loop
# Alive = True
# while Alive:
#       findClick("left_game")
      


# test commit
