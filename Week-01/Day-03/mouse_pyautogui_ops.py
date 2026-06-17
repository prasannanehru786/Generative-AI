import pyautogui
import time
time.sleep(1)  # Wait for 3 seconds before executing the next commands
#pyautogui.leftClick(100, 100)  # Move the mouse to (100, 100) and click
#pyautogui.moveTo(200, 200, duration=1)  # Move the mouse to (200, 200) over 1 second
#pyautogui.rightClick(300, 300)  # Move the mouse to (300, 300) and right-click
#pyautogui.doubleClick(400, 400)  # Move the mouse to (400, 400) and double-click
pyautogui.scroll(500)  # Scroll up 500 units
pyautogui.scroll(-500)  # Scroll down 500 units