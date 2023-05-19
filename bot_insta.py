import webbrowser, pyautogui
from time import sleep

usuario = 'cristiano'
qntd_fotos = 10

webbrowser.open(f'https://www.instagram.com/{usuario}/')
sleep(10)

pyautogui.click(787,733, duration=1.5)
sleep(2)

for video in range(qntd_fotos):
    
    pyautogui.doubleClick(714,539)
    sleep(1)
    
    pyautogui.press('right')
    sleep(3.5)

