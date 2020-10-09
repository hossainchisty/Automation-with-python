'''
Author: Hossain Chisty
'''
import pyautogui
pyautogui.FAILSAFE = False
from time import sleep
for i in range(0,100):
    sleep(2)
    pyautogui.press('j')
    sleep(2)   
    pyautogui.press('l')
    sleep(0.5)
    pyautogui.press('tab')  
    sleep(0.5)
    pyautogui.press('enter')

    