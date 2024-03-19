import pyautogui

#clica no campo usuário
pyautogui.click(880, 393, duration=0.5)
#digita a matricula no campo
pyautogui.write('2022190014', inverval=0.5)

pyautogui.click(880, 500, duration=0.5)
pyautogui.write('00000000')

#clica no botão acessar
pyautogui.click(880, 530, duration=0.5)
