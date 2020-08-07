import pyautogui
import time
time.sleep(3)
for i in range(200):
    pyautogui.write("IDIOT")
    pyautogui.press('\n')
    if input()=='esc':
        exit()
pyautogui.press('enter')
