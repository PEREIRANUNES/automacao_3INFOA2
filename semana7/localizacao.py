import pyautogui

nome_XY = pyautogui.locateCenterOnScreen('./semana7/campo_nome.png', confidence=0.9)
pyautogui.click(nome_XY, duration=0.5)
pyautogui.write('Luis Eduardo')

cpf_XY = pyautogui.locateCenterOnScreen('./semana7/campo_cpf.png', confidence=0.9)
pyautogui.click(cpf_XY, duration=0.5) #clica
pyautogui.write('123.456.789-10')
