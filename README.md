# Summary
This script automates the process of acting as an exp-boosting ally for the custom game mode "Zombie Liberty (Beta) on StarCraft 2. It uses PyAutoGUI to automaticly set player game settings, adds the jewel necessary (if the player has one) and leaves the game. This assures that the active player receives the full ammount of experience by maximizing the number of potential kills they could get.

## Description
The script performs these tasks:
1. _Main Menu_ : Displays a menu to start/stop the script.
2. _Image Recognition_ : Uses temporary sceenshots to identify and locate where to click for the auto-skip button, and the jewel button.
3. _Automated Actions_ : Checks on small intervals if the game is active and ready for actions.

## Usage Instructions
1. _Prepare Images_ : Ensure that the necessary PNG images (`left_game.png` and `player_invite.png`) are in the same directory as the script.
2. _Run the Script_ : Execute the script `sc2auto.py` and follow the on-screen menu to start the automation.