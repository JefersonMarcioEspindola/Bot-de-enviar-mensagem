
import pyautogui
import pyperclip 
import time 



#Mensagens

mns1 = f"""Opa tudo bom, me chamo Jeferson, e sou representante da Machine Tech."""
mns2 = f"""Sou especialista em design e construção de sites de diversos nichos."""
mns3 = f"""A Machine Tech foi criada no intuito de ajudar empreendedores a expandir e a consolidar os seus projetos. Se quiser dar uma olhada no nosso trabalho, temos nosso próprio website."""
mns4 = f"""Aqui segue o link: https://www.machinetech.com.br/."""
mns5 = f"""Estava dando uma olhada no seu perfil do instagram , acredito que tem um ótimo potencial, por isso que acabei entrando em contato com você para te fazer um convite."""
mns6 = f"""O que você acha de conversarmos um pouco sobre seu negócio e principalmente sobre a parte estratégica e o marketing dele?"""
mns7 = f"""Acredito que é uma área importantíssima e a maioria dos concorrentes não se atentam muito pra isso."""
mns8 = f"""O que você me diz? eu tenho certeza que não vai ser perda de tempo para você."""

#----------------------------------------------------------------------------------------------------------------

#Abrir o google

time.sleep(1)
pyautogui.hotkey("win", "2") 

time.sleep(1)

#cliente 1 ------------------------------------------------------------------------------------------------------

pyautogui.hotkey("ctrl", "1")
time.sleep(1)
pyautogui.click(x=300, y=52)
time.sleep(2)

for b in range(5):
    pyautogui.hotkey("shift", "tab")
    time.sleep(0.7)

#mensagem 1
pyperclip.copy(mns1)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)
#mensagem 2
pyperclip.copy(mns2)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)
#mensagem 3
pyperclip.copy(mns3)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)
#mensagem 4
pyperclip.copy(mns4)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)
#mensagem 5
pyperclip.copy(mns5)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)
#mensagem 6
pyperclip.copy(mns6)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)
#mensagem 7
pyperclip.copy(mns7)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)
#mensagem 8
pyperclip.copy(mns8)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)

#cliente 2 a 10 ------------------------------------------------------------------------------------------------

for a in range(2): 

    pyautogui.hotkey("ctrl", "tab")
    time.sleep(0.2)
    pyautogui.click(x=300, y=52)
    time.sleep(0.2)

    for b in range(5):
        pyautogui.hotkey("shift", "tab")
        time.sleep(0.2)

    #mensagem 1
    pyperclip.copy(mns1)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2)
    #mensagem 2
    pyperclip.copy(mns2)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2)
    #mensagem 3
    pyperclip.copy(mns3)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2)
    #mensagem 4
    pyperclip.copy(mns4)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2)
    #mensagem 5
    pyperclip.copy(mns5)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2)
    #mensagem 6
    pyperclip.copy(mns6)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2)
    #mensagem 7
    pyperclip.copy(mns7)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2)
    #mensagem 8
    pyperclip.copy(mns8)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2)


print("Ababou")
