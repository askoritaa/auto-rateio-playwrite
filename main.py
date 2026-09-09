import pyautogui as au
import time as t

#Point(x=368, y=1020) dropdown
#Point(x=592, y=1040) selecione
#Point(x=844, y=535)  pesquisar id
#Point(x=1646, y=1028) percentual
#Point(x=1240, y=534) buscar



# au.hotkey("ctrl","up")
# au.hotkey("ctrl","up")
# t.sleep(1)
# au.hotkey("ctrl","c")
# au.hotkey("ctrl","down")
# au.press("down")

# au.hotkey("alt","tab")
# t.sleep(3)

# repetir = input()
# au.hotkey("ctrl","v")
# au.press("enter")
# print(repetir)

repetir = int(input("quantas vezes repetir? "))
au.hotkey("alt","tab")

i = 0
while i <= repetir:
    au.hotkey("ctrl","c")
    t.sleep(3)
    au.hotkey("ctrl","pgdn")
    au.moveTo(368,1020)
    au.click()
    t.sleep(4)
    au.write("centro")
    au.press("enter")
    au.moveTo(592,1040)
    au.click()
    au.moveTo(844,535)
    t.sleep(4)
    au.click()
    au.hotkey("ctrl","v")
    t.sleep(4)
    au.moveTo(1240,534)
    t.sleep(4)
    au.click()
    t.sleep(4)
    au.press("tab")
    au.press("space")
    t.sleep(4)
    au.hotkey("ctrl","pgdn")
    au.hotkey("ctrl","right")
    au.hotkey("ctrl","c")
    au.press("down")
    au.hotkey("ctrl","left")
    t.sleep(4)
    au.hotkey("ctrl","pgdn")
    au.moveTo(1646,1028)
    au.click()
    t.sleep(4)
    au.hotkey("ctrl","v")
    au.press("tab")
    au.press("enter")
    t.sleep(4)
    au.hotkey("ctrl","pgdn")


au.hotkey("win", "l")