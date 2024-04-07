import pyautogui
pyautogui.scroll(-200)
pyautogui.click(112, 480, clicks=1, button='left')
pyautogui.moveTo(112, 672, duration=0.5)
pyautogui.click(112, 672, clicks=1, button='left')
pyautogui.write('Luis Eduardo', interval=0.1)
pyautogui.moveTo(112, 860, duration=0.5)
pyautogui.click(112, 860, clicks=1, button='left')
pyautogui.write('000.000.000-00', interval=0.1)
duration = 1
pyautogui.scroll(-200)
pyautogui.moveTo(112, 860, duration=0.5)
pyautogui.click(112, 837, clicks=1, button='left')
pyautogui.moveTo(112, 994, duration=0.5)
pyautogui.click(112, 994, clicks=1, button='left')

