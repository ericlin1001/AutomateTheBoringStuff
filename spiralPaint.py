import pyautogui, time
from selenium import webdriver

mousePos  =  {
        "1" : (375,  179),  
        "2" : (386,  242),  
        "3" : (161,  185),  
        "4" : (406,  483),  
        }
def spiralPaint():
    dist = 200;
    de = 5;
    dur = 0.2;
    pyautogui.click()
    while dist>de * 5:
        pyautogui.dragRel(dist, 0, duration = dur);
        dist = dist - de
        pyautogui.dragRel(0, dist, duration = dur);
        dist = dist - de
        pyautogui.dragRel( - dist, 0, duration = dur);
        dist = dist - de
        pyautogui.dragRel(0,  - dist, duration = dur);
        dist = dist - de

#
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True
f = webdriver.Firefox();
f.maximize_window()
f.get('http://www.speedpaint.info/');
dur = 0.25
print("start painting....");
time.sleep(2);
pyautogui.click( *mousePos["1"], duration = dur);
pyautogui.click( *mousePos["2"], duration = dur);
pyautogui.click( *mousePos["3"], duration = dur);
pyautogui.typewrite(['1', '0']);
pyautogui.click( *mousePos["4"], duration = dur);
#pyautogui.moveTo();
spiralPaint();
