#Inserir o link da página do usuário que se deseja curtir. Ex: "https://www.instagram.com/cordeiro/" e apertar enter
import webbrowser, pyautogui
from time import sleep
webbrowser.open('https://www.instagram.com/cristiano/')
sleep(10)
#Clicar na publicação mais recente
pyautogui.click(787,733, duration=1.5)
sleep(2)
#Colocar no range quantas fotos deseja curtir
for video in range(10):
    #Curtir a foto caso não esteja curtida
    pyautogui.doubleClick(714,539)
    sleep(1)
    #Passar a foto caso esteja curtida
    pyautogui.press('right')
    sleep(3.5)

