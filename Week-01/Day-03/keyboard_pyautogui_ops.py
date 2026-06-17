import pyautogui
import pyscreeze
import time
#pyautogui.typewrite('Hello, World!', interval=0.1)
#time.sleep(1)  # Type 'Hello, World!' with a 0.1 second delay between each character
#pyautogui.hotkey('ctrl', 'a')  # Press 'Ctrl' + 'A' to select all text
#time.sleep(1)  # Wait for 1 second before executing the next command
#pyautogui.hotkey('ctrl', 'c')  # Press 'Ctrl' + 'C' to copy the selected text
#time.sleep(1)  # Wait for 1 second before executing the next command
#pyautogui.press('enter')  # Press 'Enter' to create a new line
time.sleep(1)  # Wait for 1 second before executing the next command
pyautogui.typewrite('This is a test of PyAutoGUI.', interval=0.1)  # Type the new text with a 0.1 second delay between each character
screenshot = pyautogui.screenshot()
screenshot.save('screenshot.png')  # Save the screenshot as 'screenshot.png'