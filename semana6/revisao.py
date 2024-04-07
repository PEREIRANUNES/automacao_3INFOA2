import pyautogui

#movimentar o mouse
pyautogui.moveTo(960,540, duration=0.5)
pyautogui.moveReal(100, 100, duration=0.5)

#arrasta o mouse
pyautogui.dragTo(960,540, duration=0.5)
pyautogui.dragRel(960,540, duration=0.5)

#clicar
pyautogui.click(960, 540, clicks=2, button='right')

#rolagem
pyautogui.scroll(-2)

#teclado

#escrever
pyautogui.write('Olá', interval=0.3)

#precionar um tecla especifica
pyautogui.press('enter')

#precionar teclas simultâneas 
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'v')

#manter teclas precionadas e soltar depois
pyautogui.keyDown('a')
pyautogui.keyUp('a')