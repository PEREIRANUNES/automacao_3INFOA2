'''fazer uma pesquisa no google clique no campo 
de pesquisa, após digite o texto 
como automatizar o whatsapp após pressione a tecla enter'''

import pyautogui
pyautogui.click(444, 456, duration=0.5)
pyautogui.write('como automatizar whatsapp')
pyautogui.press('enter')
pyautogui.moveTo(32,404, duration=0.5)
pyautogui.dragTo(505,573, duration=0.5)
pyautogui.hotkey('ctrl', 'c')
pyautogui.moveTo(1088,521, duration=0.5)
pyautogui.click(1088, 521, duration=0.5)
pyautogui.hotkey('ctrl', 'v')