import pyautogui
import os
import GetCh

getch = GetCh.getch
if len(os.sys.argv)>1:
    file = os.sys.argv[1];
else:
    file = 'screenshot.png'

a = getch();
p1= pyautogui.position();
print(p1);
a = getch();
p2= pyautogui.position();
print(p2);
b = pyautogui.screenshot('/tmp/tmp.png', (p1[0], p1[1], p2[0] - p1[0], p2[1] -  p1[1]));
print("saving to file:", file);
b.save(file);

