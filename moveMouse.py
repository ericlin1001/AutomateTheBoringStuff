import pyautogui

dur = 0.25
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5
for i in range(10):
    pyautogui.moveRel(100, 0, duration = dur);
    pyautogui.moveRel(0, 100, duration = dur);
    pyautogui.moveRel( -100, 0, duration = dur);
    pyautogui.moveRel( 0,  -100, duration = dur);
