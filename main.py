import pyautogui as bot
import keyboard as kb
import time

time.sleep(1.5)

quantas_kills = 10000
sell = (569, 273)

for i in range(quantas_kills):
    bot.hotkey('9') # Vai pra plot 1
    time.sleep(0.4)
    bot.keyDown('w')
    time.sleep(0.8)
    bot.keyUp('w')
    bot.leftClick()
    time.sleep(0.4)
    bot.hotkey('delete') # Abre o armazém
    time.sleep(0.4)
    bot.moveTo(sell) # Move pra vender
    time.sleep(0.4)
    bot.leftClick()
    time.sleep(1)

    bot.hotkey('0') # Vai pra plot 2
    time.sleep(0.4)
    bot.keyDown('w')
    time.sleep(0.8)
    bot.keyUp('w')
    bot.leftClick()
    time.sleep(0.4)
    bot.hotkey('delete') # Abre o armazém
    time.sleep(0.4)
    bot.moveTo(sell) # Move pra vender
    time.sleep(0.4)
    bot.leftClick()
    time.sleep(1)
    
